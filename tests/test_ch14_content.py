from pathlib import Path
import hashlib,re,unittest,xml.etree.ElementTree as ET,yaml
ROOT=Path(__file__).resolve().parents[1]
class CH14ContentTests(unittest.TestCase):
 def test_bilingual_sections_align(self):
  z=(ROOT/'content/zh-TW/chapters/CH14-chapter-14.md').read_text(encoding='utf8'); e=(ROOT/'content/en-US/chapters/CH14-chapter-14.md').read_text(encoding='utf8'); a=yaml.safe_load((ROOT/'metadata/translations/CH14-alignment.yaml').read_text(encoding='utf8')); ids=re.findall(r'\{#(CH14-S\d+)\}',z); self.assertEqual(ids,re.findall(r'\{#(CH14-S\d+)\}',e)); self.assertEqual(ids,[x['section_id'] for x in a['sections']]); self.assertEqual(len(ids),13)
 def test_drafts_have_body_and_sources(self):
  for loc in ('zh-TW','en-US'):
   t=(ROOT/f'content/{loc}/chapters/CH14-chapter-14.md').read_text(encoding='utf8'); self.assertGreater(len(t),2500); self.assertNotIn('Add observable outcomes',t); self.assertTrue(all(f'R{i}' in t for i in range(101,107)))
 def test_terms_registered_and_bilingual(self):
  terms=yaml.safe_load((ROOT/'metadata/terminology.yaml').read_text(encoding='utf8'))['terms']; ch=[x for x in terms if x['term_id'].startswith('TERM-CH14-')]; self.assertEqual(len(ch),5); self.assertTrue(all(x['preferred']['zh-TW'] and x['preferred']['en-US'] and x['definitions']['zh-TW'] and x['definitions']['en-US'] for x in ch))
 def test_figures_hash_alt_rights_and_embeds(self):
  m=yaml.safe_load((ROOT/'assets/chapters/CH14/figure-manifest.yaml').read_text(encoding='utf8')); reg=yaml.safe_load((ROOT/'metadata/figure-registry.yaml').read_text(encoding='utf8'))['figures']; ids={x['figure_id'] for x in reg}
  for f in m['figures']:
   b=(ROOT/f['asset_original']).read_bytes(); self.assertEqual(hashlib.sha256(b).hexdigest(),f['sha256']); ET.fromstring(b); self.assertIn(f['figure_id'],ids); self.assertTrue(f['alt_zh'] and f['alt_en']); self.assertEqual(f['publication_status'],'pending-publication-approval'); self.assertIsNone(f['asset_approved']); self.assertIn('not an official film still',f['caption_en'].lower()); self.assertIn('並非任何電影原劇照',f['caption_zh'])
   for loc in ('zh-TW','en-US'): self.assertEqual((ROOT/f'content/{loc}/chapters/CH14-chapter-14.md').read_text(encoding='utf8').count('{#'+f['figure_id']+' '),1)
