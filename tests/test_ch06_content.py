import re
import hashlib
import tempfile
from unittest.mock import patch
from types import SimpleNamespace
import unittest
from pathlib import Path

import yaml
from scripts.publishing.build_books import stage_sources_for_pandoc, figure_is_approved

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
        for ref_id in ['R046','R047','R048','R049','R050','R051']:
            self.assertIn(ref_id, ref_ids)


    def test_figures_registered_and_pending_review(self):
        manifest = yaml.safe_load((ROOT / 'assets/chapters/CH06/figure-manifest.yaml').read_text(encoding='utf-8'))
        figures = manifest['figures']
        self.assertEqual([f['figure_id'] for f in figures], ['CH06-FIG-001', 'CH06-FIG-002'])
        for fig in figures:
            asset = ROOT / fig['asset_original']
            self.assertTrue(asset.is_file())
            self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), fig['sha256'])
            self.assertIsNone(fig['asset_approved'])
            self.assertEqual(fig['publication_status'], 'pending-publication-approval')
            self.assertIn('publication approval pending', fig['caption_en'].lower())
            self.assertIn('出版核准待審', fig['caption_zh'])
        for text in (self.zh, self.en):
            for fig_id in ['CH06-FIG-001', 'CH06-FIG-002']:
                self.assertEqual(text.count('{' + '#' + fig_id), 1)
                self.assertIn(fig_id, text)

    def test_pandoc_svg_staging_keeps_sources_and_uses_vector_pdf_for_print(self):
        source = ROOT / 'content/zh-TW/chapters/CH06-chapter-06.md'
        original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory(prefix='test-ch06-media-', dir=ROOT / 'tmp') as directory:
            def fake_inkscape(args, **kwargs):
                output = next(arg.split('=', 1)[1] for arg in args if arg.startswith('--export-filename='))
                Path(output).write_bytes(b'%PDF-1.4 test vector')
                return SimpleNamespace(returncode=0, stderr='')
            with patch('scripts.publishing.build_books.subprocess.run', side_effect=fake_inkscape) as converter:
                staged, staged_dir = stage_sources_for_pandoc('zh-TW', [source], 'pdf', Path(directory))
            text = staged[0].read_text(encoding='utf-8')
            self.assertEqual(converter.call_count, 2)
            self.assertEqual(text.count('../media/'), 2)
            self.assertIn('.pdf)', text)
            self.assertTrue(all((Path(directory) / 'media').glob('*.pdf')))
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), original_hash)

    def test_publication_gate_accepts_reviewed_svg_provenance_without_ai_model_fields(self):
        path = 'assets/chapters/CH06/figures/originals/CH06-FIG-001-causal-chain.svg'
        figure = {'asset_approved': path, 'rights_review': 'approved', 'technical_review': 'approved',
                  'editorial_review': 'approved', 'figure_id': 'CH06-FIG-001', 'teaching_goal': 'Explain a causal chain',
                  'caption_zh': '圖說', 'caption_en': 'Caption', 'alt_zh': '替代文字', 'alt_en': 'Alt text',
                  'method': 'Hand-authored editable SVG', 'production_log': [{'date': '2026-10-21', 'change': 'Created'}]}
        requested = ROOT / path
        self.assertTrue(figure_is_approved(figure, 'zh-TW', requested))
        figure['asset_approved'] = None
        self.assertFalse(figure_is_approved(figure, 'zh-TW', requested))

    def test_publication_gate_keeps_raster_generation_provenance_required(self):
        path = 'assets/chapters/CH06/figures/originals/CH06-FIG-001-causal-chain.svg'
        figure = {'asset_approved': path, 'rights_review': 'approved', 'technical_review': 'approved',
                  'editorial_review': 'approved', 'figure_id': 'CH06-FIG-001', 'teaching_goal': 'Explain',
                  'caption_zh': '圖說', 'caption_en': 'Caption', 'alt_zh': '替代文字', 'alt_en': 'Alt text'}
        self.assertFalse(figure_is_approved(figure, 'en-US', ROOT / path))

    def test_no_scaffold_and_ai_demo_labeled(self):
        for text in (self.zh, self.en):
            self.assertNotIn('This scaffold is not', text)
            self.assertIn('JSON', text)
            self.assertIn('review-needed', text)


if __name__ == '__main__':
    unittest.main()
