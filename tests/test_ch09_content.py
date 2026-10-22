import hashlib,re,unittest,xml.etree.ElementTree as ET
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
class CH09Tests(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  c.zh=(ROOT/'content/zh-TW/chapters/CH09-chapter-09.md').read_text(encoding='utf-8'); c.en=(ROOT/'content/en-US/chapters/CH09-chapter-09.md').read_text(encoding='utf-8'); c.a=yaml.safe_load((ROOT/'metadata/translations/CH09-alignment.yaml').read_text(encoding='utf-8')); c.f=yaml.safe_load((ROOT/'assets/chapters/CH09/figure-manifest.yaml').read_text(encoding='utf-8'))['figures']; c.t=yaml.safe_load((ROOT/'metadata/terminology.yaml').read_text(encoding='utf-8'))['terms']; c.r=yaml.safe_load((ROOT/'data/references.yaml').read_text(encoding='utf-8'))
 def test_sections_align(self):
  want=[f'CH09-S{i:02}' for i in range(1,13)]; z=re.findall(r'\{#(CH09-S\d+)\}',self.zh); e=re.findall(r'\{#(CH09-S\d+)\}',self.en); self.assertEqual(z,['CH09-S00',*want]); self.assertEqual(e,['CH09-S00',*want]); self.assertEqual([x['id'] for x in self.a['sections']],want)
 def test_terms_sources_registered(self):
  terms=[x for x in self.t if x['term_id'].startswith('TERM-CH09-')]; self.assertEqual(len(terms),9); self.assertEqual({x['term_id'] for x in terms},set(self.a['terms'])); self.assertTrue(all(x['status']=='draft' and x['preferred'].get('zh-TW') and x['preferred'].get('en-US') for x in terms)); ids={x['id'] for x in self.r}; self.assertTrue(set(self.a['references'])<=ids)
 def test_figures_are_present_hashes_and_pending(self):
  self.assertEqual([x['figure_id'] for x in self.f],[f'CH09-FIG-{i:03}' for i in range(1,4)])
  for f in self.f:
   p=ROOT/f['asset_original']; self.assertTrue(p.is_file()); self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),f['sha256']); ET.parse(p); self.assertIsNone(f['asset_approved']); self.assertEqual(f['approval_status'],'pending'); self.assertTrue(f['alt_zh'] and f['alt_en']); self.assertIn(f['figure_id'],self.zh); self.assertIn(f['figure_id'],self.en); self.assertIn('pending',f['rights_status'])
 def test_draft_not_placeholder(self):
  for text in (self.zh,self.en): self.assertNotRegex(text.lower(),r'\b(?:todo|placeholder|tbd)\b'); self.assertGreater(len(text),8000)
if __name__=='__main__': unittest.main()

