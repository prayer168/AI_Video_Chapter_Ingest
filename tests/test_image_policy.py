from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from image_policy import publication_blockers, redact_unapproved_images


class ImagePublicationPolicyTests(unittest.TestCase):
    def make_project(self, status: str = "pending") -> tuple[Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        chapter = root / "chapters" / "01-01-test.md"
        image = root / "assets" / "test.png"
        chapter.parent.mkdir(parents=True)
        image.parent.mkdir(parents=True)
        image.write_bytes(b"not-rendered-in-this-policy-test")
        chapter.write_text("![Test image](../assets/test.png)\n", encoding="utf-8")
        record = {
            "id": "ASSET-TEST-01", "path": "assets/test.png", "license": "CC BY 4.0",
            "creator": "Test author", "attribution": "Test author", "permission": "Approved for test fixture",
            "figure_id": "FIG-TEST-01", "paragraph_reference": "01-01 §1", "description": "Fixture image",
            "tool_name": None, "tool_version": None,
            "approval_status": status,
            "review_status": {"technical": status, "quality": status, "rights": status, "final": status},
            "rights_risk_review": {"status": status},
            "publication_targets": {key: status for key in ("zh-TW-book", "en-book", "zh-TW-site", "en-site")},
            "caption_zh_tw": "繁中圖說", "caption_en": "English caption",
            "teaching_purpose": "Test purpose", "original_prompt_or_method": "Hand-drawn test fixture",
            "production_log": [{"date": "2026-10-18", "change": "Fixture"}],
            "research_sources": [{"source_id": "R001", "accessed": "2026-10-18", "purpose": "Fixture"}],
        }
        (root / "data").mkdir()
        (root / "data" / "assets.yaml").write_text(yaml.safe_dump([record]), encoding="utf-8")
        (root / "data" / "references.yaml").write_text(yaml.safe_dump([{"id": "R001"}]), encoding="utf-8")
        return root, chapter

    def test_pending_image_blocks_publication(self) -> None:
        root, _ = self.make_project()
        blockers = publication_blockers(root, "zh-TW-site")
        self.assertTrue(any("approval_status is pending" in item for item in blockers))

    def test_approved_image_passes_target_gate(self) -> None:
        root, _ = self.make_project("approved")
        self.assertEqual(publication_blockers(root, "zh-TW-site"), [])

    def test_external_image_is_blocked(self) -> None:
        root, chapter = self.make_project("approved")
        chapter.write_text("![Remote](https://example.com/image.png)\n", encoding="utf-8")
        self.assertTrue(any("external/unsupported" in item for item in publication_blockers(root, "zh-TW-site")))


    def test_unregistered_local_image_is_blocked(self) -> None:
        root, chapter = self.make_project("approved")
        chapter.write_text("![Unknown](../assets/unknown.png)\n", encoding="utf-8")
        self.assertTrue(any("missing from data/assets.yaml" in item for item in publication_blockers(root, "zh-TW-site")))

    def test_approval_is_specific_to_publication_target(self) -> None:
        root, _ = self.make_project("approved")
        rows_path = root / "data" / "assets.yaml"
        rows = yaml.safe_load(rows_path.read_text(encoding="utf-8"))
        rows[0]["publication_targets"]["en-site"] = "pending"
        rows_path.write_text(yaml.safe_dump(rows), encoding="utf-8")
        self.assertEqual(publication_blockers(root, "zh-TW-site"), [])
        self.assertTrue(any("en-site approval is pending" in item for item in publication_blockers(root, "en-site")))

    def test_preview_replaces_pending_image(self) -> None:
        root, chapter = self.make_project()
        original = chapter.read_text(encoding="utf-8")
        result = redact_unapproved_images(original, root, chapter, "zh-TW-site")
        self.assertIn("插圖待審核：Test image", result)
        self.assertNotIn("test.png", result)


if __name__ == "__main__":
    unittest.main()
