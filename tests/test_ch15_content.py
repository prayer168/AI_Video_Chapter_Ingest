from pathlib import Path
import hashlib, re, unittest, xml.etree.ElementTree as ET, yaml
ROOT=Path(__file__).resolve().parents[1]
class CH15ContentTests(unittest.TestCase):
 def test_bilingual_sections_align(self):
  z=(ROOT/'content/zh-TW/chapters/CH15-chapter-15.md').read_text(encoding='utf-8'); e=(ROOT/'content/en-US/chapters/CH15-chapter-15.md').read_text(encoding='utf-8'); a=yaml.safe_load((ROOT/'metadata/translations/CH15-alignment.yaml').read_text(encoding='utf-8')); ids=re.findall(r'\{#(CH15-S\d+)\}',z); self.assertEqual(ids,re.findall(r'\{#(CH15-S\d+)\}',e)); self.assertEqual(ids,[x['section_id'] for x in a['sections']]); self.assertEqual(len(ids),12)
 def test_substantive_drafts_and_sources(self):
  for loc in ('zh-TW','en-US'):
   t=(ROOT/f'content/{loc}/chapters/CH15-chapter-15.md').read_text(encoding='utf-8'); self.assertGreater(len(t),6500); self.assertNotIn('Add observable outcomes',t); self.assertTrue(all(f'R{i}' in t for i in range(107,112)))
 def test_terms_registered_bilingually(self):
  terms=yaml.safe_load((ROOT/'metadata/terminology.yaml').read_text(encoding='utf-8'))['terms']; ch=[x for x in terms if x['term_id'].startswith('TERM-CH15-')]; self.assertEqual(len(ch),6); self.assertTrue(all(x['preferred']['zh-TW'] and x['preferred']['en-US'] and x['definitions']['zh-TW'] and x['definitions']['en-US'] for x in ch))
 def test_figures_hash_alt_rights_and_embeds(self):
  m=yaml.safe_load((ROOT/'assets/chapters/CH15/figure-manifest.yaml').read_text(encoding='utf-8')); reg=yaml.safe_load((ROOT/'metadata/figure-registry.yaml').read_text(encoding='utf-8'))['figures']; ids={x['figure_id'] for x in reg}
  for f in m['figures']:
   b=(ROOT/f['asset_original']).read_bytes(); self.assertEqual(hashlib.sha256(b).hexdigest(),f['sha256']); ET.fromstring(b); self.assertIn(f['figure_id'],ids); self.assertTrue(f['alt_zh'] and f['alt_en']); self.assertEqual(f['publication_status'],'pending-publication-approval'); self.assertIsNone(f['asset_approved'])
   for loc in ('zh-TW','en-US'): self.assertEqual((ROOT/f'content/{loc}/chapters/CH15-chapter-15.md').read_text(encoding='utf-8').count('{#'+f['figure_id']+' '),1)
 def test_source_ids_exist_and_reviews_stay_open(self):
  refs={x['id'] for x in yaml.safe_load((ROOT/'data/references.yaml').read_text(encoding='utf-8'))}; self.assertTrue({'R107','R108','R109','R110','R111'} <= refs); checklist=(ROOT/'assets/chapters/CH15/CH15-HUMAN-REVIEW-CHECKLIST.md').read_text(encoding='utf-8'); self.assertIn('NEEDS HUMAN REVIEW',checklist)
if __name__=='__main__': unittest.main()
