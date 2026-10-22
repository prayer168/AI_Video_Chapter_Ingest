from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "content/zh-TW/chapters/CH04-chapter-04.md"
EN = ROOT / "content/en-US/chapters/CH04-chapter-04.md"


class Chapter04ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = ZH.read_text(encoding="utf-8")
        cls.en = EN.read_text(encoding="utf-8")
        cls.terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))["terms"]
        cls.manifest = yaml.safe_load((ROOT / "assets/chapters/CH04/figure-manifest.yaml").read_text(encoding="utf-8"))
        cls.references = yaml.safe_load((ROOT / "data/references.yaml").read_text(encoding="utf-8"))

    def test_bilingual_section_ids_match_and_are_substantive(self):
        pattern = r"^#{1,2} .+?\{#(CH04-S\d{2})\}"
        zh_ids = re.findall(pattern, self.zh, re.M)
        en_ids = re.findall(pattern, self.en, re.M)
        self.assertEqual(zh_ids, en_ids)
        self.assertEqual(len(zh_ids), 14)
        for chapter in (self.zh, self.en):
            for section_id in zh_ids:
                self.assertIn(section_id, chapter)
            self.assertNotIn("pending editorial translation", chapter.lower())
            self.assertNotIn("<!-- Add observable outcomes", chapter)

    def test_glossary_entries_and_reference_ids_exist(self):
        terms = {item["term_id"]: item for item in self.terms}
        for term_id in re.findall(r"TERM-CH04-[A-Z0-9-]+", self.zh + self.en):
            self.assertIn(term_id, terms)
        source_ids = {row["id"] for row in self.references}
        cited_ids = set(re.findall(r"\bR\d{3}\b", self.zh + self.en))
        self.assertTrue(cited_ids)
        self.assertTrue(cited_ids.issubset(source_ids), cited_ids - source_ids)

    def test_figures_have_bilingual_captions_alt_hash_and_pending_rights(self):
        self.assertEqual(len(self.manifest["figures"]), 2)
        for figure in self.manifest["figures"]:
            path = ROOT / figure["asset_original"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), figure["sha256"])
            self.assertEqual(path.stat().st_size, figure["bytes"])
            self.assertIn(figure["figure_id"], self.zh)
            self.assertIn(figure["figure_id"], self.en)
            self.assertEqual(figure["rights_review"], "pending")
            self.assertEqual(figure["publication_status"], "pending-publication-approval")
            self.assertIsNone(figure["asset_approved"])
            self.assertIn("caption_zh", figure)
            self.assertIn("caption_en", figure)

    def test_chapter_remains_review_needed(self):
        for source in (ZH, EN):
            frontmatter = source.read_text(encoding="utf-8").split("---", 2)[1]
            self.assertIn("translation_status: review-needed", frontmatter)
        self.assertIn("不宣稱正式出版核准", self.zh)
        self.assertIn("has not been approved for publication", self.en.lower())


if __name__ == "__main__":
    unittest.main()
