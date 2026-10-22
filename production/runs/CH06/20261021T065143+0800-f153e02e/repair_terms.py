from pathlib import Path
p=Path('metadata/terminology.yaml')
t=p.read_text(encoding='utf-8')
start=t.index('\n- term_id: TERM-CH06-STORY\n')+1
end=t.index('\n- term_id: TERM-CH01-MULTIPLE-PERSPECTIVE\n', start)
block=t[start:end]
footer='  references:\n  - R013\n  - R020\n  status: draft\n  reviewed_by: null\n  reviewed_on: null'
if not block.endswith(footer):
    raise SystemExit('Unexpected terminology block boundary; no changes made')
block=block[:-len(footer)].rstrip()+'\n'
t=t[:start]+footer+'\n'+t[end+1:]
t=t.rstrip()+'\n\n'+block
p.write_text(t,encoding='utf-8')
print('Moved CH06 term entries to end and restored CH01 deep-focus metadata')
