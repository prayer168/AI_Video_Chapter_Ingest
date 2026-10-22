from pathlib import Path
import hashlib
import re

import yaml
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Chapter05Tests(unittest.TestCase):
    def test_bilingual_chapter_sections_and_terms_align(self):
        zh = (ROOT / "content/zh-TW/chapters/CH05-chapter-05.md").read_text(encoding="utf-8")
        en = (ROOT / "content/en-US/chapters/CH05-chapter-05.md").read_text(encoding="utf-8")
        self.assertEqual(set(re.findall(r"\{#(CH05-S\d+)\}", zh)), set(re.findall(r"\{#(CH05-S\d+)\}", en)))
        self.assertEqual(len(re.findall(r"\{#(CH05-S\d+)\}", zh)), 13)
        terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))
        chapter_terms = [t for t in terms["terms"] if t["term_id"].startswith("TERM-CH05-")]
        self.assertEqual(len(chapter_terms), 8)
        self.assertTrue(all(t["preferred"].get("zh-TW") and t["preferred"].get("en-US") and t["definitions"].get("zh-TW") and t["definitions"].get("en-US") for t in chapter_terms))


    def test_figures_exist_hash_match_and_remain_pending(self):
        manifest = yaml.safe_load((ROOT / "assets/chapters/CH05/figure-manifest.yaml").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["figures"]), 2)
        for figure in manifest["figures"]:
            path = ROOT / figure["asset_original"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), figure["sha256"])
            self.assertIsNone(figure["asset_approved"])
            self.assertEqual(figure["publication_status"], "pending-publication-approval")
            self.assertTrue(figure["caption_zh"] and figure["caption_en"] and figure["alt_zh"] and figure["alt_en"])


    def test_translation_map_and_reference_ids_exist(self):
        alignment = yaml.safe_load((ROOT / "metadata/translations/CH05-alignment.yaml").read_text(encoding="utf-8"))
        bib = (ROOT / "metadata/references.bib").read_text(encoding="utf-8")
        bib_ids = set(re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", bib))
        self.assertEqual(len(alignment["sections"]), 13)
        self.assertEqual(len(set(s["id"] for s in alignment["sections"])), 13)
        self.assertTrue(set(alignment["references"]).issubset(bib_ids))
