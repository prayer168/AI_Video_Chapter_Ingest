from __future__ import annotations

import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

import yaml

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / "staging" / "CH02-V4"


class CH02StagingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh_path = STAGE / "zh-TW" / "CH02-camera-language.md"
        cls.en_path = STAGE / "en-US" / "CH02-camera-language.md"
        cls.zh = cls.zh_path.read_text(encoding="utf-8")
        cls.en = cls.en_path.read_text(encoding="utf-8")

    def test_required_bilingual_section_ids_are_complete_and_aligned(self):
        expected = {f"CH02-S{i:02d}" for i in range(13)}
        for text in (self.zh, self.en):
            self.assertEqual(set(re.findall(r"\{#(CH02-S\d+)\}", text)), expected)
            self.assertGreater(len(re.sub(r"<[^>]+>|[#`*_{}]", "", text)), 5000)

    def test_all_26_bilingual_terms_have_same_stable_ids(self):
        zh_ids = set(re.findall(r"`(TERM-CH02-[A-Z0-9-]+)`", self.zh))
        en_ids = set(re.findall(r"`(TERM-CH02-[A-Z0-9-]+)`", self.en))
        glossary = yaml.safe_load((STAGE / "glossary-CH02.yaml").read_text(encoding="utf-8"))
        glossary_ids = {term["term_id"] for term in glossary["terms"]}
        self.assertEqual(len(zh_ids), 26)
        self.assertEqual(zh_ids, en_ids)
        self.assertEqual(zh_ids, glossary_ids)

    def test_original_svg_files_are_well_formed_hashed_and_referenced(self):
        manifest = yaml.safe_load((STAGE / "figure-manifest.yaml").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["figures"]), 5)
        for figure in manifest["figures"]:
            path = ROOT / figure["file_path"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), figure["sha256"])
            svg = ET.parse(path).getroot()
            self.assertTrue(svg.tag.endswith("svg"))
            self.assertEqual(figure["asset_status"], "draft-original-svg")
            self.assertEqual(figure["publication_status"], "pending-publication-approval")
            self.assertIn(path.name, self.zh)
            self.assertIn(path.name, self.en)
            self.assertTrue(figure["alt_zh"] and figure["alt_en"])
            self.assertTrue(figure["zh_caption"] and figure["en_caption"])

    def test_demo_shot_list_is_contiguous_and_totals_60_seconds(self):
        shot = json.loads((ROOT / "chapters/01-02-camera-language-assets/shot-lists/CH02-science-shortfilm.json").read_text(encoding="utf-8"))
        entries = shot["shots"]
        self.assertEqual(shot["duration_seconds"], 60)
        self.assertEqual(entries[0]["start_seconds"], 0)
        self.assertEqual(entries[-1]["end_seconds"], 60)
        self.assertTrue(all(a["end_seconds"] == b["start_seconds"] for a, b in zip(entries, entries[1:])))
        self.assertTrue(all(a["end_seconds"] > a["start_seconds"] for a in entries))
        self.assertTrue(all(entry["status"] == "planned" for entry in entries))

    def test_source_archives_and_existing_v2_scaffolds_are_unchanged(self):
        record = json.loads((STAGE / "SOURCE-AND-ASSET-RECORD.json").read_text(encoding="utf-8"))
        source = ROOT / "chapters/source-packs/AI-Filmmaking-Bible-CH02-Codex.zip"
        legacy = ROOT / "chapters/01-02-camera-language.md"
        canonical_zh = ROOT / "content/zh-TW/chapters/CH02-camera-language.md"
        canonical_en = ROOT / "content/en-US/chapters/CH02-camera-language.md"
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), record["archive_sha256"])
        with ZipFile(source) as archive:
            self.assertIsNone(archive.testzip())
        self.assertEqual(hashlib.sha256(legacy.read_bytes()).hexdigest(), record["legacy_sha256"])
        self.assertEqual(hashlib.sha256(canonical_zh.read_bytes()).hexdigest(), record["canonical_zh_sha256_before"])
        self.assertEqual(hashlib.sha256(canonical_en.read_bytes()).hexdigest(), record["canonical_en_sha256_before"])


if __name__ == "__main__":
    unittest.main()
