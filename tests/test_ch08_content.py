import hashlib
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class Chapter08ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = (ROOT / "content/zh-TW/chapters/CH08-chapter-08.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "content/en-US/chapters/CH08-chapter-08.md").read_text(encoding="utf-8")
        cls.alignment = yaml.safe_load((ROOT / "metadata/translations/CH08-alignment.yaml").read_text(encoding="utf-8"))
        cls.figures = yaml.safe_load((ROOT / "assets/chapters/CH08/figure-manifest.yaml").read_text(encoding="utf-8"))["figures"]
        cls.terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))["terms"]
        cls.references = yaml.safe_load((ROOT / "data/references.yaml").read_text(encoding="utf-8"))

    def test_bilingual_stable_sections_align(self):
        ids_zh = re.findall(r"\{#(CH08-S\d+)\}", self.zh)
        ids_en = re.findall(r"\{#(CH08-S\d+)\}", self.en)
        self.assertEqual(ids_zh, [f"CH08-S{i:02d}" for i in range(1, 13)])
        self.assertEqual(ids_zh, ids_en)
        self.assertEqual(ids_zh, [item["id"] for item in self.alignment["sections"]])

    def test_eight_bilingual_terms_are_draft_and_aligned(self):
        terms = [item for item in self.terms if item["term_id"].startswith("TERM-CH08-")]
        self.assertEqual(len(terms), 8)
        self.assertEqual({item["term_id"] for item in terms}, set(self.alignment["terms"]))
        for item in terms:
            self.assertTrue(item["preferred"].get("zh-TW"))
            self.assertTrue(item["preferred"].get("en-US"))
            self.assertEqual(item["status"], "draft")

    def test_sources_are_registered_and_caveats_present(self):
        reference_ids = {item["id"] for item in self.references}
        self.assertTrue(set(self.alignment["references"]).issubset(reference_ids))
        self.assertIn("版次", self.zh)
        self.assertIn("edition", self.en.lower())
        self.assertIn("pending", self.en.lower())

    def test_figures_hash_xml_captions_alt_and_approval_state(self):
        self.assertEqual([item["figure_id"] for item in self.figures], ["CH08-FIG-001", "CH08-FIG-002"])
        self.assertEqual({item["id"] for item in self.alignment["figures"]}, {item["figure_id"] for item in self.figures})
        for item in self.figures:
            path = ROOT / item["asset_original"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item["sha256"])
            ET.parse(path)
            self.assertIsNone(item["asset_approved"])
            self.assertEqual(item["approval_status"], "pending")
            self.assertTrue(item["alt_zh"] and item["alt_en"])
            self.assertIn("原創", item["caption_zh"])
            self.assertIn("非電影劇照", item["caption_zh"])
            self.assertIn("original", item["caption_en"].lower())
            self.assertIn("not a film still", item["caption_en"].lower())
            self.assertIn(item["figure_id"], self.zh)
            self.assertIn(item["figure_id"], self.en)

    def test_chapter_has_no_placeholder_sections(self):
        for text in (self.zh, self.en):
            self.assertNotRegex(text.lower(), r"\b(?:todo|placeholder|tbd)\b")
            self.assertGreater(len(text), 4000)


if __name__ == "__main__":
    unittest.main()
