import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class Chapter06ContentTests(unittest.TestCase):
    def setUp(self):
        self.zh = (ROOT / 'content/zh-TW/chapters/CH06-chapter-06.md').read_text(encoding='utf-8')
        self.en = (ROOT / 'content/en-US/chapters/CH06-chapter-06.md').read_text(encoding='utf-8')

    def test_stable_sections_align(self):
        ids = lambda text: re.findall(r'\{#(CH06-S\d{2})\}', text)
        self.assertEqual(ids(self.zh), ids(self.en))
        self.assertEqual(ids(self.zh), [f'CH06-S{i:02}' for i in range(1, 13)])

    def test_terms_and_references_registered(self):
        terms = yaml.safe_load((ROOT / 'metadata/terminology.yaml').read_text(encoding='utf-8'))['terms']
        refs = yaml.safe_load((ROOT / 'data/references.yaml').read_text(encoding='utf-8'))
        term_ids = {t['term_id'] for t in terms}
        ref_ids = {r['id'] for r in refs}
        for term_id in ['TERM-CH06-STORY','TERM-CH06-PLOT','TERM-CH06-CAUSALITY','TERM-CH06-MOTIVATION','TERM-CH06-INCITING-INCIDENT','TERM-CH06-REVERSAL','TERM-CH06-RECOGNITION','TERM-CH06-FORESHADOWING']:
            self.assertIn(term_id, term_ids)
        for ref_id in ['R046','R047','R048','R049','R050']:
            self.assertIn(ref_id, ref_ids)

    def test_no_scaffold_and_ai_demo_labeled(self):
        for text in (self.zh, self.en):
            self.assertNotIn('This scaffold is not', text)
            self.assertIn('JSON', text)
            self.assertIn('review-needed', text)


if __name__ == '__main__':
    unittest.main()
