import hashlib
import re
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]


class Chapter07ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = (ROOT / "content/zh-TW/chapters/CH07-chapter-07.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "content/en-US/chapters/CH07-chapter-07.md").read_text(encoding="utf-8")
        cls.alignment = yaml.safe_load((ROOT / "metadata/translations/CH07-alignment.yaml").read_text(encoding="utf-8"))
        cls.figures = yaml.safe_load((ROOT / "assets/chapters/CH07/figure-manifest.yaml").read_text(encoding="utf-8"))["figures"]
        cls.terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))
        cls.references = yaml.safe_load((ROOT / "data/references.yaml").read_text(encoding="utf-8"))

    def test_stable_bilingual_section_ids_align(self):
        ids_zh = re.findall(r"\{#(CH07-S\d+)\}", self.zh)
        ids_en = re.findall(r"\{#(CH07-S\d+)\}", self.en)
        self.assertEqual(ids_zh, ids_en)
        self.assertEqual(ids_zh, [f"CH07-S{i:02d}" for i in range(14)])
        self.assertEqual([x["id"] for x in self.alignment["sections"]], ids_zh)

    def test_terms_are_registered_bilingual_and_used(self):
        term_ids = [x["term_id"] for x in self.terms["terms"] if x["term_id"].startswith("TERM-CH07-")]
        self.assertEqual(len(term_ids), 8)
        for item in self.terms["terms"]:
            if item["term_id"].startswith("TERM-CH07-"):
                self.assertTrue(item["preferred"].get("zh-TW"))
                self.assertTrue(item["preferred"].get("en-US"))
                self.assertEqual(item["status"], "draft")
        self.assertEqual(set(term_ids), set(self.alignment["terms"]))

    def test_references_exist_and_cases_are_attributed_as_secondary_analysis(self):
        ref_ids = {x["id"] for x in self.references}
        for ref_id in self.alignment["references"]:
            self.assertIn(ref_id, ref_ids)
        self.assertIn("secondary-source case studies", self.en)
        self.assertIn("二手資料案例", self.zh)
        self.assertIn("timecode", self.en.lower())

    def test_figures_exist_hash_match_and_are_not_approved(self):
        self.assertEqual([f["figure_id"] for f in self.figures], ["CH07-FIG-001", "CH07-FIG-002"])
        for figure in self.figures:
            path = ROOT / figure["asset_original"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), figure["sha256"])
            self.assertIsNone(figure["asset_approved"])
            self.assertEqual(figure["approval_status"], "pending")
            self.assertTrue(figure["alt_zh"] and figure["alt_en"])
            self.assertIn(figure["figure_id"], self.zh)
            self.assertIn(figure["figure_id"], self.en)

    def test_svg_is_well_formed_and_captions_preserve_original_not_film_still_notice(self):
        import xml.etree.ElementTree as ET
        for figure in self.figures:
            path = ROOT / figure["asset_original"]
            ET.parse(path)
            self.assertIn("原創", figure["caption_zh"])
            self.assertIn("非電影劇照", figure["caption_zh"])
            self.assertIn("original", figure["caption_en"].lower())
            self.assertIn("not a film still", figure["caption_en"].lower())

    def test_docx_staging_rasterizes_svg_without_changing_originals(self):
        from scripts.publishing.build_books import stage_sources_for_pandoc
        source = ROOT / "content/zh-TW/chapters/CH07-chapter-07.md"
        original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        def fake_inkscape(args, **kwargs):
            output = next(arg.split("=", 1)[1] for arg in args if arg.startswith("--export-filename="))
            Path(output).write_bytes(b"test png payload")
            return SimpleNamespace(returncode=0, stderr="")
        with tempfile.TemporaryDirectory(prefix="test-ch07-docx-media-", dir=ROOT / "tmp") as directory:
            with patch("scripts.publishing.build_books.subprocess.run", side_effect=fake_inkscape) as converter:
                staged, _ = stage_sources_for_pandoc("zh-TW", [source], "docx", Path(directory))
            text = staged[0].read_text(encoding="utf-8")
            self.assertEqual(converter.call_count, 2)
            self.assertEqual(text.count("../media/"), 2)
            self.assertEqual(text.count(".png)"), 2)
            self.assertTrue(all((Path(directory) / "media").glob("*.png")))
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), original_hash)


if __name__ == "__main__":
    unittest.main()
