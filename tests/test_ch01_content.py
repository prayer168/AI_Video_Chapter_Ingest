import hashlib
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "content/zh-TW/chapters/CH01-cinematic-language.md"
EN = ROOT / "content/en-US/chapters/CH01-cinematic-language.md"


def body_by_section(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## .+?\{#(CH01-S\d{2})\}\s*$", text, re.M))
    result = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1)] = text[match.end():end].strip()
    return result


class Chapter01ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh_text = ZH.read_text(encoding="utf-8")
        cls.en_text = EN.read_text(encoding="utf-8")
        cls.alignment = yaml.safe_load((ROOT / "metadata/translations/CH01-alignment.yaml").read_text(encoding="utf-8"))
        cls.terms = yaml.safe_load((ROOT / "metadata/terminology.yaml").read_text(encoding="utf-8"))["terms"]
        cls.figures = yaml.safe_load((ROOT / "assets/chapters/CH01/figure-manifest.yaml").read_text(encoding="utf-8"))["figures"]

    def test_all_required_sections_have_substantive_bilingual_text(self):
        zh, en = body_by_section(self.zh_text), body_by_section(self.en_text)
        self.assertEqual(set(zh), set(en))
        self.assertEqual(set(zh), {f"CH01-S{i:02d}" for i in range(1, 14)})
        for section_id in zh:
            self.assertGreater(len(zh[section_id]), 120, f"short Chinese section: {section_id}")
            self.assertGreater(len(en[section_id]), 120, f"short English section: {section_id}")
            for placeholder in ("<!-- Add ", "pending editorial translation", "This scaffold is not a completed chapter"):
                self.assertNotIn(placeholder, zh[section_id])
                self.assertNotIn(placeholder, en[section_id])

    def test_translation_map_matches_stable_anchors_and_cases(self):
        rows = self.alignment["sections"]
        ids = [row["section_id"] for row in rows]
        self.assertEqual(ids, [f"CH01-S{i:02d}" for i in range(1, 14)])
        anchors_zh = set(re.findall(r"\{#(CH01-S\d{2}|CH01-P\d{3})\}", self.zh_text))
        anchors_en = set(re.findall(r"\{#(CH01-S\d{2}|CH01-P\d{3})\}", self.en_text))
        self.assertEqual(anchors_zh, anchors_en)
        self.assertEqual(anchors_zh & {f"CH01-P{i:03d}" for i in range(1, 6)}, {f"CH01-P{i:03d}" for i in range(1, 6)})

    def test_chapter_terms_are_bilingual_and_registered(self):
        registered = {row["term_id"]: row for row in self.terms}
        ids = next(row["term_ids"] for row in self.alignment["sections"] if row["section_id"] == "CH01-S03")
        self.assertEqual(len(ids), 26)
        for term_id in ids:
            row = registered[term_id]
            for lang in ("zh-TW", "en-US"):
                self.assertTrue(row["preferred"][lang].strip())
                self.assertTrue(row["definitions"][lang].strip())
            self.assertEqual(row["status"], "draft")
            self.assertIn(row["preferred"]["zh-TW"], self.zh_text)
            self.assertIn(row["preferred"]["en-US"], self.en_text)

    def test_all_chapter_citations_exist_in_bibliography(self):
        bib = (ROOT / "metadata/references.bib").read_text(encoding="utf-8")
        keys = set(re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", bib))
        for text in (self.zh_text, self.en_text):
            cited = set(re.findall(r"\[(R\d{3})\]", text))
            self.assertTrue(cited)
            self.assertLessEqual(cited, keys)
            anchors = set(re.findall(r'<span id="(ref-R\d{3})"></span>', text))
            self.assertTrue({f"ref-{reference}" for reference in cited} <= anchors)

    def test_imported_figures_exist_and_remain_pending_review(self):
        self.assertEqual(len(self.figures), 5)
        expected_ids = [f"CH01-HOMAGE-FIG-{i:03d}" for i in range(1, 6)]
        self.assertEqual([figure["figure_id"] for figure in self.figures], expected_ids)
        for figure in self.figures:
            self.assertEqual(figure["asset_status"], "draft-generated")
            self.assertEqual(figure["rights_status"], "original-ai-illustration-pending-final-review")
            self.assertEqual(figure["asset_approved"], None)
            self.assertEqual(figure["rights_review"], "pending")
            self.assertEqual(figure["technical_review"], "pending")
            self.assertEqual(figure["editorial_review"], "pending")
            self.assertEqual(figure["publication_status"], "pending-publication-approval")
            image = ROOT / figure["file_path"]
            self.assertTrue(image.is_file(), f"missing image: {image}")
            data = image.read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), figure["generation"]["sha256"])
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            self.assertTrue(figure["zh_caption"].startswith("圖 "))
            self.assertIn("本圖為原創示意圖", figure["zh_caption"])
            self.assertIn("並非電影原劇照", figure["zh_caption"])
            self.assertTrue(figure["en_caption"].startswith("Figure "))
            self.assertIn("This is an original illustrative image", figure["en_caption"])
            self.assertIn("It is not an official film still.", figure["en_caption"])
            self.assertTrue(figure["alt_zh"].strip())
            self.assertTrue(figure["alt_en"].strip())
            for text in (self.zh_text, self.en_text):
                self.assertIn(figure["figure_id"], text)
                self.assertIn(figure["file_path"], text)

    def test_website_projection_renders_figure_ids_and_alt_text(self):
        for locale, site_locale in (("zh-TW", "zh-tw"), ("en-US", "en")):
            projection = ROOT / f"apps/web/src/content/docs/{site_locale}/CH01-cinematic-language.md"
            page = projection.read_text(encoding="utf-8")
            for figure in self.figures:
                self.assertIn(f'<figure id="{figure["figure_id"]}">', page)
                self.assertIn("<figcaption>", page)
                self.assertNotIn(f"{{#{figure['figure_id']}}}", page)
                expected_alt = figure["alt"][locale]
                self.assertIn(expected_alt, page)

    def test_bilingual_figure_manifest_and_caption_register_are_synchronized(self):
        registry = yaml.safe_load((ROOT / "metadata/figure-registry.yaml").read_text(encoding="utf-8"))["figures"]
        registered = {item["figure_id"]: item for item in registry}
        aligned = {item["figure_id"]: item for item in self.alignment["figures"]}
        captions = (ROOT / "assets/chapters/CH01/figures/figure-captions.md").read_text(encoding="utf-8")
        for figure in self.figures:
            self.assertIn(figure["figure_id"], registered)
            self.assertIn(figure["figure_id"], aligned)
            self.assertEqual(figure["file_path"], registered[figure["figure_id"]]["asset_original"])
            self.assertEqual(figure["zh_caption"], aligned[figure["figure_id"]]["caption_zh"])
            self.assertEqual(figure["en_caption"], aligned[figure["figure_id"]]["caption_en"])
            self.assertIn(figure["zh_caption"], captions)
            self.assertIn(figure["en_caption"], captions)



if __name__ == "__main__":
    unittest.main()
