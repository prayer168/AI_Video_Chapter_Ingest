from __future__ import annotations
import re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.image_policy import markdown_image_refs

errors, warnings = [], []

def check_registry():
    if yaml is None:
        errors.append('PyYAML is required to validate V2 metadata; install requirements-v2.txt')
        return
    try:
        chapter_data = yaml.safe_load((ROOT / 'metadata/chapters.yaml').read_text(encoding='utf-8')) or []
        part_data = yaml.safe_load((ROOT / 'metadata/parts.yaml').read_text(encoding='utf-8')) or []
        translation_data = yaml.safe_load((ROOT / 'metadata/translation-status.yaml').read_text(encoding='utf-8')) or {}
        term_data = yaml.safe_load((ROOT / 'metadata/terminology.yaml').read_text(encoding='utf-8')) or {}
        figure_data = yaml.safe_load((ROOT / 'metadata/figure-registry.yaml').read_text(encoding='utf-8')) or {}
    except Exception as exc:
        errors.append(f'Invalid V2 YAML metadata: {exc}')
        return
    ids = [row.get('chapter_id') for row in chapter_data if isinstance(row, dict)]
    if len(ids) != 60 or len(set(ids)) != 60 or set(ids) != {f'CH{i:02d}' for i in range(1, 61)}:
        errors.append(f'chapter registry expected CH01–CH60 exactly once, got {len(ids)} unique IDs')
    if len(part_data) != 12 or len({row.get('part_id') for row in part_data if isinstance(row, dict)}) != 12:
        errors.append('part registry expected 12 unique part IDs')
    if not isinstance(translation_data.get('chapters'), dict) or set(translation_data['chapters']) != set(ids):
        errors.append('translation status registry must have one entry for each chapter ID')
    allowed_states = set(translation_data.get('statuses', []))
    if not isinstance(term_data.get('terms'), list): errors.append('terminology registry must define a terms list')
    if not isinstance(figure_data.get('figures'), list): errors.append('figure registry must define a figures list')
    terms = term_data.get('terms', [])
    term_ids = [row.get('term_id') for row in terms if isinstance(row, dict)]
    if len(term_ids) != len(set(term_ids)): errors.append('duplicate term_id in terminology registry')
    reference_text = (ROOT / 'metadata/references.bib').read_text(encoding='utf-8')
    reference_ids = set(re.findall(r'@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,', reference_text))
    for term in terms:
        if not isinstance(term, dict): errors.append('terminology entries must be mappings'); continue
        if not re.fullmatch(r'TERM-[A-Z0-9][A-Z0-9-]*', str(term.get('term_id', ''))): errors.append(f'invalid term_id: {term.get("term_id")}')
        for block in ('preferred', 'definitions'):
            values = term.get(block, {}) or {}
            for lang in ('zh-TW', 'en-US'):
                if not isinstance(values.get(lang), str) or not values[lang].strip(): errors.append(f'{term.get("term_id")}: missing {block}.{lang}')
        for ref in term.get('references', []):
            if ref not in reference_ids: errors.append(f'{term.get("term_id")}: unknown bibliography ID {ref}')
        if term.get('status') == 'approved' and (not term.get('reviewed_by') or not term.get('reviewed_on')):
            errors.append(f'{term.get("term_id")}: approved term needs reviewer and review date')
    for locale in ('zh-TW', 'en-US'):
        files = sorted((ROOT / 'content' / locale / 'chapters').glob('CH*.md'))
        file_by_id = {}
        if len(files) != 60: errors.append(f'{locale}: expected 60 scaffolds, got {len(files)}')
        for path in files:
            body = path.read_text(encoding='utf-8')
            try:
                if not body.startswith('---\n'): raise ValueError('opening YAML delimiter missing')
                _, raw, _ = body.split('---', 2)
                meta = yaml.safe_load(raw)
                if not isinstance(meta, dict): raise ValueError('frontmatter is not a YAML mapping')
            except Exception as exc:
                errors.append(f'invalid frontmatter: {path.relative_to(ROOT)} ({exc})'); continue
            chapter_id = meta.get('chapter_id')
            if chapter_id in file_by_id: errors.append(f'duplicate {locale} file for {chapter_id}')
            file_by_id[chapter_id] = (path, meta, body)
            if meta.get('locale') != locale: errors.append(f'locale mismatch: {path.relative_to(ROOT)}')
            if chapter_id not in set(ids): errors.append(f'unknown chapter ID: {chapter_id} ({path.name})')
            if locale == 'en-US' and meta.get('translation_status') == 'approved': errors.append(f'unreviewed English scaffold marked approved: {path.name}')
            state = (translation_data.get('chapters', {}).get(chapter_id, {}) or {}).get(locale)
            if state not in allowed_states: errors.append(f'unknown translation state {chapter_id}/{locale}: {state!r}')
            if state != meta.get('translation_status'):
                errors.append(f'translation state mismatch {chapter_id}/{locale}: metadata={state!r}, chapter={meta.get("translation_status")!r}')
        if set(file_by_id) != set(ids): errors.append(f'{locale}: chapter file IDs do not match chapter registry')
    zh = {re.search(r'^chapter_id: (CH\d{2})$', text, re.M).group(1): set(re.findall(r'\{#([A-Za-z0-9_-]+)\}', text)) for text in [(ROOT / 'content/zh-TW/chapters' / p.name).read_text(encoding='utf-8') for p in sorted((ROOT / 'content/zh-TW/chapters').glob('CH*.md'))] if re.search(r'^chapter_id: (CH\d{2})$', text, re.M)}
    en = {re.search(r'^chapter_id: (CH\d{2})$', text, re.M).group(1): set(re.findall(r'\{#([A-Za-z0-9_-]+)\}', text)) for text in [(ROOT / 'content/en-US/chapters' / p.name).read_text(encoding='utf-8') for p in sorted((ROOT / 'content/en-US/chapters').glob('CH*.md'))] if re.search(r'^chapter_id: (CH\d{2})$', text, re.M)}
    for chapter_id in set(zh) & set(en):
        if zh[chapter_id] != en[chapter_id]: errors.append(f'bilingual anchor mismatch: {chapter_id}')
def check_manifest():
    path = ROOT/'legacy/2026-v1/migration-manifest.csv'
    if not path.exists(): errors.append('migration manifest missing'); return
    import csv
    with path.open(encoding='utf-8-sig', newline='') as f: rows=list(csv.DictReader(f))
    if not rows: errors.append('migration manifest has no file entries')
    for row in rows:
        if row['status'] != 'verified' or row['sha256_source'] != row['sha256_backup']: errors.append(f"migration checksum mismatch: {row['source']}")
def check_figures():
    seen_ids = set()
    for path in (ROOT/'assets/chapters').glob('CH*/figure-manifest.yaml'):
        try:
            data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        except Exception as exc:
            errors.append(f'invalid figure manifest {path}: {exc}'); continue
        if not isinstance(data.get('figures'), list):
            errors.append(f'figure manifest needs a figures list: {path}'); continue
        folder_chapter_id = path.parent.name
        for fig in data['figures']:
            if not isinstance(fig, dict): errors.append(f'figure entries must be mappings: {path}'); continue
            figure_id = fig.get('figure_id')
            if not re.fullmatch(r'CH\d{2}-FIG-\d{3}', str(figure_id or '')): errors.append(f'invalid figure_id in {path}: {figure_id}')
            if figure_id in seen_ids: errors.append(f'duplicate figure_id: {figure_id}')
            seen_ids.add(figure_id)
            if fig.get('chapter_id') != folder_chapter_id: errors.append(f'figure chapter_id/folder mismatch: {figure_id} in {path}')
            if any(fig.get(key, 'pending') not in ('pending', 'approved', 'rejected', 'not-applicable') for key in ('rights_review', 'technical_review', 'editorial_review')):
                errors.append(f'invalid figure review status: {figure_id} in {path}')
def check_links():
    for path in [* (ROOT/'apps/web/src/content/docs').rglob('*.mdx'), * (ROOT/'apps/web/src/content/docs').rglob('*.md'), * (ROOT/'content').rglob('*.md')]:
        text=path.read_text(encoding='utf-8')
        for url, _alt in markdown_image_refs(text):
            if re.match(r'(?i)^(https?:|data:|file:|//)', url.strip()):
                errors.append(f'external/inline image prohibited: {url} ({path.name})')

if __name__ == '__main__':
    check_registry(); check_manifest(); check_figures(); check_links()
    if errors:
        print('V2 validation FAILED')
        for error in errors: print(f'ERROR: {error}')
        sys.exit(1)
    print('V2 validation PASS: 12-part/60-chapter registries, bilingual scaffolds, legacy checksums, and image policy gates.')
    print('NOTE: editorial review, external reference checks, visual layout, PDF font embedding, and web build are separate gates.')
