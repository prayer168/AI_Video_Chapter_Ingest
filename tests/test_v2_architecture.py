import csv, hashlib, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from scripts.publishing.build_books import pdf_font_args
class ArchitectureTests(unittest.TestCase):
    def test_v2_validator(self):
        result=subprocess.run([sys.executable, str(ROOT/'scripts/v2_validate.py')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
    def test_registry_has_60_ids(self):
        import re
        ids=re.findall(r'^- chapter_id: (CH\d{2})$', (ROOT/'metadata/chapters.yaml').read_text(encoding='utf-8'), re.M)
        self.assertEqual(len(ids), 60); self.assertEqual(len(set(ids)), 60)
    def test_language_pairs_have_stable_ids(self):
        for i in range(1,61):
            zh=list((ROOT/'content/zh-TW/chapters').glob(f'CH{i:02d}-*.md'))
            en=list((ROOT/'content/en-US/chapters').glob(f'CH{i:02d}-*.md'))
            self.assertEqual(len(zh),1); self.assertEqual(len(en),1)
            self.assertIn(f'chapter_id: CH{i:02d}', zh[0].read_text(encoding='utf-8'))
            self.assertIn(f'chapter_id: CH{i:02d}', en[0].read_text(encoding='utf-8'))
    def test_legacy_manifest_hashes(self):
        path=ROOT/'legacy/2026-v1/migration-manifest.csv'
        with path.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row['status'],'verified',row['source'])
            self.assertEqual(row['sha256_source'],row['sha256_backup'],row['source'])
    def test_no_auto_deploy_workflow(self):
        workflows=ROOT/'.github/workflows'
        for path in workflows.glob('*.yml') if workflows.exists() else []:
            text=path.read_text(encoding='utf-8').lower()
            self.assertNotIn('deploy-pages',text); self.assertNotIn('gh-pages',text)
    def test_site_projection_is_current(self):
        result=subprocess.run([sys.executable, str(ROOT/'scripts/publishing/sync_site_content.py'), '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
    def test_formal_book_build_rejects_unapproved_content_before_tool_check(self):
        result=subprocess.run([sys.executable, str(ROOT/'scripts/publishing/build_books.py'), '--locale', 'en-US', '--format', 'epub'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('not editorially approved', result.stderr)
    def test_bilingual_pdf_command_includes_cjk_font_for_english_glossary(self):
        args=pdf_font_args('Times New Roman','Microsoft JhengHei')
        self.assertIn('mainfont=Times New Roman',args)
        self.assertIn('CJKmainfont=Microsoft JhengHei',args)
if __name__=='__main__': unittest.main()
