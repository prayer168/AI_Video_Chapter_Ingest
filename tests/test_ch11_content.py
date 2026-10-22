from pathlib import Path
import hashlib
import re
import unittest
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CH11Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh_path = ROOT / 'content/zh-TW/chapters/CH11-chapter-11.md'
        cls.en_path = ROOT / 'content/en-US/chapters/CH11-chapter-11.md'
        cls.zh = cls.zh_path.read_text(encoding='utf-8')
        cls.en = cls.en_path.read_text(encoding='utf-8')
        cls.alignment = yaml.safe_load((ROOT / 'metadata/translations/CH11-alignment.yaml').read_text(encoding='utf-8'))
        cls.manifest = yaml.safe_load((ROOT / 'assets/chapters/CH11/figure-manifest.yaml').read_text(encoding='utf-8'))['figures']
        cls.terms = yaml.safe_load((ROOT / 'metadata/terminology.yaml').read_text(encoding='utf-8'))['terms']
        cls.references = yaml.safe_load((ROOT / 'data/references.yaml').read_text(encoding='utf-8'))

    def test_stable_bilingual_sections_align(self):
        expected = [f'CH11-S{i:02}' for i in range(13)]
        for text in (self.zh, self.en):
            self.assertEqual(re.findall(r'\{#(CH11-S\d+)\}', text), expected)
        self.assertEqual([row['id'] for row in self.alignment['sections']], expected)
        self.assertEqual(self.alignment['status'], 'review-needed')

    def test_terms_and_sources_registered(self):
        terms = [term for term in self.terms if term['term_id'].startswith('TERM-CH11-')]
        self.assertEqual(len(terms), 8)
        self.assertEqual({term['term_id'] for term in terms}, set(self.alignment['terms']))
        self.assertTrue(all(term['status'] == 'draft' for term in terms))
        ref_ids = {ref['id'] for ref in self.references}
        self.assertTrue(set(self.alignment['references']) <= ref_ids)
        self.assertEqual(set(self.alignment['references']), {f'R{i:03}' for i in range(77, 87)})

    def test_original_figures_are_valid_hashed_and_pending(self):
        self.assertEqual([figure['figure_id'] for figure in self.manifest], ['CH11-FIG-001', 'CH11-FIG-002'])
        for figure in self.manifest:
            path = ROOT / figure['asset_original']
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), figure['sha256'])
            ET.parse(path)
            self.assertIsNone(figure['asset_approved'])
            self.assertEqual(figure['approval_status'], 'pending')
            self.assertIn('pending', figure['rights_status'])
            self.assertTrue(figure['alt_zh'] and figure['alt_en'])
            self.assertIn(figure['figure_id'], self.zh)
            self.assertIn(figure['figure_id'], self.en)
            self.assertIn('not a film still', figure['caption_en'].lower())

    def test_bilingual_drafts_have_content_without_scaffold(self):
        for text in (self.zh, self.en):
            self.assertGreater(len(text), 7000)
            self.assertNotRegex(text.lower(), r'\b(?:todo|placeholder|tbd)\b')
            self.assertNotIn('This scaffold is not a completed chapter', text)
        self.assertIn('source-draft', self.zh)
        self.assertIn('review-needed', self.en)

    def test_site_projections_contain_ch11_figures_and_unique_sections(self):
        for locale in ('zh-tw', 'en'):
            text = (ROOT / f'apps/web/src/content/docs/{locale}/CH11-chapter-11.md').read_text(encoding='utf-8')
            ids = re.findall(r'<a id="([^"]+)"|<figure id="([^"]+)"', text)
            flat = [left or right for left, right in ids]
            self.assertEqual(len(flat), len(set(flat)))
            self.assertIn('<figure id="CH11-FIG-001">', text)
            self.assertIn('<figure id="CH11-FIG-002">', text)
            self.assertNotIn('assets/chapters/CH11/figures/originals', text)


if __name__ == '__main__':
    unittest.main()
