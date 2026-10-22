import hashlib
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CH10Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = (ROOT / "content/zh-TW/chapters/CH10-chapter-10.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "content/en-US/chapters/CH10-chapter-10.md").read_text(encoding="utf-8")
        cls.align = yaml.safe_load((ROOT / "metadata/translations/CH10-alignment.yaml").read_text(encoding="utf-8"))
        cls.figures = yaml.safe_load((ROOT / "assets/chapters/CH10/figure-manifest.yaml").read_text(encoding="utf-8"))["figures"]
        cls.terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))["terms"]
        cls.refs = yaml.safe_load((ROOT / "data/references.yaml").read_text(encoding="utf-8"))

    def test_sections_align(self):
        expected = [f"CH10-S{i:02}" for i in range(1, 13)]
        for text in (self.zh, self.en):
            self.assertEqual(re.findall(r"\{#(CH10-S\d+)\}", text), ["CH10-S00", *expected])
        self.assertEqual([row["id"] for row in self.align["sections"]], expected)

    def test_terms_and_references_registered(self):
        terms = [t for t in self.terms if t["term_id"].startswith("TERM-CH10-")]
        self.assertEqual(len(terms), 8)
        self.assertEqual({t["term_id"] for t in terms}, set(self.align["terms"]))
        self.assertTrue(all(t["status"] == "draft" and t["preferred"].get("zh-TW") and t["preferred"].get("en-US") for t in terms))
        self.assertTrue(set(self.align["references"]) <= {r["id"] for r in self.refs})

    def test_figures_exist_are_original_and_pending(self):
        self.assertEqual([f["figure_id"] for f in self.figures], [f"CH10-FIG-{i:03}" for i in range(1, 4)])
        for f in self.figures:
            path = ROOT / f["asset_original"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), f["sha256"])
            ET.parse(path)
            self.assertIsNone(f["asset_approved"])
            self.assertEqual(f["approval_status"], "pending")
            self.assertTrue(f["alt_zh"] and f["alt_en"])
            self.assertIn(f["figure_id"], self.zh)
            self.assertIn(f["figure_id"], self.en)
            self.assertIn("pending", f["rights_status"])

    def test_bilingual_drafts_have_substance_and_not_approved(self):
        for text in (self.zh, self.en):
            self.assertNotRegex(text.lower(), r"\b(?:todo|placeholder|tbd)\b")
            self.assertGreater(len(text), 7000)
        self.assertEqual(self.align["status"], "review-needed")


if __name__ == "__main__":
    unittest.main()
