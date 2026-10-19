from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.chapter_pipeline import start_run, update_run


class ChapterPipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "metadata").mkdir()
        (self.root / "production/runs").mkdir(parents=True)
        (self.root / "metadata/chapters.yaml").write_text(
            "- chapter_id: CH01\n  part_id: P01\n  number: 1\n  slug: cinematic-language\n  title_zh: 電影語言\n  title_en: Cinematic Language\n",
            encoding="utf-8",
        )
        (self.root / "metadata/translation-status.yaml").write_text(
            "chapters:\n  CH01:\n    zh-TW: review-needed\n    en-US: translation-needed\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_start_records_registry_and_creates_unique_checkpoints(self):
        first = start_run(self.root, 1)
        second = start_run(self.root, 1)
        self.assertNotEqual(first, second)
        data = json.loads((first / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(data["chapter_id"], "CH01")
        self.assertEqual(data["translation_status"]["zh-TW"], "review-needed")
        self.assertEqual(data["status"], "in-progress")
        self.assertTrue((first / "CHECKLIST.md").is_file())

    def test_step_and_finish_are_logged_without_touching_manuscripts(self):
        original = b"original chapter"
        chapter = self.root / "content/zh-TW/chapters/CH01-test.md"
        chapter.parent.mkdir(parents=True)
        chapter.write_bytes(original)
        run = start_run(self.root, 1)
        update_run(self.root, 1, run, "inventory=pass", "Registry and existing draft reviewed")
        with self.assertRaises(ValueError):
            update_run(self.root, 1, run, finish="complete")
        with self.assertRaisesRegex(ValueError, "chapter-audit"):
            update_run(self.root, 1, run, finish="partial")
        update_run(self.root, 1, run, "chapter-audit=pass", "Acceptance checklist completed; unresolved items remain itemized")
        update_run(self.root, 1, run, finish="partial", note="Draft deliverable complete; review gates remain open")
        self.assertEqual(chapter.read_bytes(), original)
        data = json.loads((run / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(data["steps"]["inventory"]["status"], "pass")
        self.assertEqual(data["steps"]["chapter-audit"]["status"], "pass")
        self.assertEqual(data["status"], "partial")

    def test_unknown_chapter_and_unsafe_run_path_are_rejected(self):
        with self.assertRaises(ValueError):
            start_run(self.root, 2)
        run = start_run(self.root, 1)
        outside = self.root / "other"
        outside.mkdir()
        with self.assertRaises(ValueError):
            update_run(self.root, 1, outside, "inventory=pass")


if __name__ == "__main__":
    unittest.main()
