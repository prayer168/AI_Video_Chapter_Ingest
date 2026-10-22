from pathlib import Path
import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CH16ContentTests(unittest.TestCase):
    def test_bilingual_sections_align(self):
        zh = (ROOT / "content/zh-TW/chapters/CH16-chapter-16.md").read_text(encoding="utf-8-sig")
        en = (ROOT / "content/en-US/chapters/CH16-chapter-16.md").read_text(encoding="utf-8-sig")
        alignment = yaml.safe_load((ROOT / "metadata/translations/CH16-alignment.yaml").read_text(encoding="utf-8"))
        zh_ids = re.findall(r"\{#(CH16-S\d+)\}", zh)
        self.assertEqual(zh_ids, re.findall(r"\{#(CH16-S\d+)\}", en))
        self.assertEqual(zh_ids, [row["section_id"] for row in alignment["sections"]])
        self.assertEqual(len(zh_ids), 12)

    def test_substantive_drafts_and_registered_sources(self):
        refs = {row["id"] for row in yaml.safe_load((ROOT / "data/references.yaml").read_text(encoding="utf-8"))}
        for locale in ("zh-TW", "en-US"):
            text = (ROOT / f"content/{locale}/chapters/CH16-chapter-16.md").read_text(encoding="utf-8-sig")
            self.assertGreater(len(text), 8000)
            self.assertNotIn("Add observable outcomes", text)
            used = set(re.findall(r"\[(R\d{3})\]", text))
            self.assertTrue({"R112", "R113", "R114", "R115", "R116", "R117", "R118", "R119"} <= used)
            self.assertTrue(used <= refs)

    def test_bilingual_terms_registered(self):
        registry = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))["terms"]
        chapter_terms = [row for row in registry if row["term_id"].startswith("TERM-CH16-")]
        self.assertEqual(len(chapter_terms), 12)
        self.assertTrue(all(row["preferred"].get("zh-TW") and row["preferred"].get("en-US") and row["definitions"].get("zh-TW") and row["definitions"].get("en-US") for row in chapter_terms))

    def test_figures_exist_hash_match_and_remain_pending(self):
        manifest = yaml.safe_load((ROOT / "assets/chapters/CH16/figure-manifest.yaml").read_text(encoding="utf-8"))
        registry = yaml.safe_load((ROOT / "metadata/figure-registry.yaml").read_text(encoding="utf-8"))["figures"]
        registered = {row["figure_id"]: row for row in registry}
        self.assertEqual(len(manifest["figures"]), 2)
        for fig in manifest["figures"]:
            raw = (ROOT / fig["asset_original"]).read_bytes()
            ET.fromstring(raw)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), fig["sha256"])
            self.assertEqual(fig["sha256"], registered[fig["figure_id"]]["sha256"])
            self.assertIsNone(fig["asset_approved"])
            self.assertEqual(fig["publication_status"], "pending-publication-approval")
            self.assertTrue(fig["alt_zh"] and fig["alt_en"] and fig["caption_zh"] and fig["caption_en"])
            self.assertIn("pending", fig["rights_status"])
            for locale in ("zh-TW", "en-US"):
                text = (ROOT / f"content/{locale}/chapters/CH16-chapter-16.md").read_text(encoding="utf-8-sig")
                self.assertEqual(text.count("{#" + fig["figure_id"] + " "), 1)

    def test_prompt_json_and_human_review_gate(self):
        text = (ROOT / "content/en-US/chapters/CH16-chapter-16.md").read_text(encoding="utf-8-sig")
        blocks = re.findall(r"```json\s*(.*?)\s*```", text, flags=re.S)
        self.assertEqual(len(blocks), 1)
        payload = json.loads(blocks[0])
        self.assertEqual(payload["chapter_id"], "CH16")
        checklist = (ROOT / "assets/chapters/CH16/CH16-HUMAN-REVIEW-CHECKLIST.md").read_text(encoding="utf-8")
        self.assertIn("NEEDS HUMAN REVIEW", checklist)
        self.assertIn("Film viewing and timecode", checklist)


if __name__ == "__main__":
    unittest.main()
