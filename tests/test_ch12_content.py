from pathlib import Path
import hashlib, re, unittest, xml.etree.ElementTree as ET, yaml
ROOT=Path(__file__).resolve().parents[1]
class CH12ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh=(ROOT/'content/zh-TW/chapters/CH12-chapter-12.md').read_text(encoding='utf-8')
        cls.en=(ROOT/'content/en-US/chapters/CH12-chapter-12.md').read_text(encoding='utf-8')
        cls.manifest=yaml.safe_load((ROOT/'assets/chapters/CH12/figure-manifest.yaml').read_text(encoding='utf-8'))
        cls.align=yaml.safe_load((ROOT/'metadata/translations/CH12-alignment.yaml').read_text(encoding='utf-8'))
    def test_stable_bilingual_section_ids(self):
        ids=[f'CH12-S{i:02d}' for i in range(14)]
        for text in (self.zh,self.en):
            for sid in ids: self.assertIn('{#'+sid+'}',text)
        self.assertEqual(ids,[r['section_id'] for r in self.align['sections']])
    def test_substantive_not_scaffold(self):
        for text in (self.zh,self.en):
            self.assertGreater(len(text),8000)
            self.assertNotRegex(text,r'(?i)TODO|placeholder|lorem ipsum|待填寫')
            for sid in ('CH12-FIG-001','CH12-FIG-002'): self.assertIn(sid,text)
    def test_terms_and_sources_registered(self):
        terms=yaml.safe_load((ROOT/'metadata/terminology.yaml').read_text(encoding='utf-8'))['terms']
        ids=self.align['term_ids']; indexed={t['term_id'] for t in terms}
        self.assertTrue(set(ids).issubset(indexed))
        refs=yaml.safe_load((ROOT/'data/references.yaml').read_text(encoding='utf-8'))
        available={r['id'] for r in refs}
        self.assertTrue(set(self.align['reference_ids']).issubset(available))
    def test_figures_hash_xml_alt_and_pending_review(self):
        self.assertEqual(2,len(self.manifest['figures']))
        for item in self.manifest['figures']:
            p=ROOT/item['asset_original']; self.assertTrue(p.is_file()); ET.parse(p)
            self.assertEqual(item['sha256'],hashlib.sha256(p.read_bytes()).hexdigest())
            self.assertTrue(item['alt_zh'] and item['alt_en'])
            self.assertEqual('pending-publication-approval',item['publication_status'])
            self.assertIsNone(item['asset_approved'])
            self.assertIn('非電影劇照',item['caption_zh'])
            self.assertIn('not a film still',item['caption_en'])
    def test_translation_and_authority_status_not_approved(self):
        status=yaml.safe_load((ROOT/'metadata/translation-status.yaml').read_text(encoding='utf-8'))['chapters']['CH12']
        self.assertEqual('source-draft',status['zh-TW']); self.assertEqual('review-needed',status['en-US'])
        self.assertEqual('review-needed',self.align['status'])
if __name__=='__main__': unittest.main()
