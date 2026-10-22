from pathlib import Path
import hashlib,re,unittest,xml.etree.ElementTree as ET,yaml
ROOT=Path(__file__).resolve().parents[1]
class CH13ContentTests(unittest.TestCase):
 def test_bilingual_sections_align(self):
  zh=(ROOT/'content/zh-TW/chapters/CH13-chapter-13.md').read_text(encoding='utf8'); en=(ROOT/'content/en-US/chapters/CH13-chapter-13.md').read_text(encoding='utf8'); a=yaml.safe_load((ROOT/'metadata/translations/CH13-alignment.yaml').read_text(encoding='utf8')); ids=re.findall(r'\{#(CH13-S\d+)\}',zh); self.assertEqual(ids,re.findall(r'\{#(CH13-S\d+)\}',en)); self.assertEqual(ids,[x['section_id'] for x in a['sections']]); self.assertEqual(len(ids),13)
 def test_drafts_substantive(self):
  for loc in ('zh-TW','en-US'):
   t=(ROOT/f'content/{loc}/chapters/CH13-chapter-13.md').read_text(encoding='utf8'); self.assertGreater(len(t),6000); self.assertNotIn('Add observable outcomes',t)
 def test_terms_and_refs_registered(self):
  refs=yaml.safe_load((ROOT/'data/references.yaml').read_text(encoding='utf8')); ids={x['id'] for x in refs}; terms=yaml.safe_load((ROOT/'metadata/terminology.yaml').read_text(encoding='utf8'))['terms']; ch=[x for x in terms if x['term_id'].startswith('TERM-CH13-')]; self.assertGreaterEqual(len(ch),6); self.assertTrue(all(set(x['references'])<=ids for x in ch)); self.assertTrue(set(f'R{i:03d}' for i in range(94,101))<=ids)
 def test_figures_integrity_pending(self):
  m=yaml.safe_load((ROOT/'assets/chapters/CH13/figure-manifest.yaml').read_text(encoding='utf8')); reg=yaml.safe_load((ROOT/'metadata/figure-registry.yaml').read_text(encoding='utf8'))['figures']; registered={x['figure_id'] for x in reg}
  for f in m['figures']:
   raw=(ROOT/f['asset_original']).read_bytes(); self.assertEqual(hashlib.sha256(raw).hexdigest(),f['sha256']); ET.fromstring(raw); self.assertIn(f['figure_id'],registered); self.assertIsNone(f['asset_approved']); self.assertIn('not an official film still',f['caption_en'].lower()); self.assertIn('並非任何電影原劇照',f['caption_zh']); self.assertTrue(f['alt_zh'] and f['alt_en']); self.assertEqual(f['publication_status'],'pending-publication-approval')
 def test_figure_ids_in_both(self):
  for loc in ('zh-TW','en-US'):
   t=(ROOT/f'content/{loc}/chapters/CH13-chapter-13.md').read_text(encoding='utf8')
   for fid in ('CH13-FIG-001','CH13-FIG-002'): self.assertEqual(t.count('{#'+fid+' '),1)

