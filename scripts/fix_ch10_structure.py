from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]
mapping={10:11,9:10,8:9,7:8,6:7,5:6,4:5,3:4,2:3}
for locale in ('zh-TW','en-US'):
 p=R/f'content/{locale}/chapters/CH10-chapter-10.md'; s=p.read_text(encoding='utf-8')
 for old,new in mapping.items(): s=s.replace(f'CH10-S{old:02}',f'CH10-S{new:02}')
 if locale=='zh-TW':
  needle='## 核心概念與專業術語 {#CH10-S03}'
  intro='## 先備知識 {#CH10-S02}\n\n建議讀者熟悉場景、動作、角色名、對白及基本劇本閱讀。改編權利並非劇本格式課程的先備條件；涉及既有作品時，權利狀態應從研究開始單獨登錄。\n\n'
 else:
  needle='## Core Concepts and Professional Terms {#CH10-S03}'
  intro='## Prerequisites {#CH10-S02}\n\nReaders should be familiar with scenes, action, character cues, dialogue, and basic screenplay reading. Adaptation rights are not a prerequisite for studying format; when existing works are involved, record rights status separately from the start.\n\n'
 s=s.replace(needle,intro+needle,1)
 h='## 參考資料 {#CH10-S11}' if locale=='zh-TW' else '## References {#CH10-S11}'
 h2='## 參考資料 {#CH10-S12}' if locale=='zh-TW' else '## References {#CH10-S12}'
 s=s.replace(h,h2,1); p.write_text(s,encoding='utf-8')
p=R/'metadata/translations/CH10-alignment.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
zh=['學習目標與適用對象','先備知識','核心概念與專業術語','歷史與基本原理','傳統製作方法','AI 時代的技術轉換與限制','詳細工作流程','提示詞與技術參數','電影案例分析','常見錯誤與品質驗證','練習、評量與延伸研究','參考資料']
en=['Learning Objectives and Audience','Prerequisites','Core Concepts and Professional Terms','History and Principles','Traditional Production Practice','AI-Era Technical Changes and Limits','Step-by-Step Workflow','Prompt and Technical Parameters','Film Case Study','Common Errors and Quality Checks','Exercises, Assessment, and Further Research','References']
d['sections']=[{'id':f'CH10-S{i:02}','zh':z,'en':e} for i,(z,e) in enumerate(zip(zh,en),1)]; p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
p=R/'assets/chapters/CH10/figure-manifest.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
for f,sid in zip(d['figures'],('CH10-S07','CH10-S09','CH10-S10')): f['section_id']=sid; f['placement_after']=f'after:{sid}'
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
p=R/'metadata/figure-registry.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
for f,sid in zip([x for x in d['figures'] if x.get('figure_id','').startswith('CH10-FIG-')],('CH10-S07','CH10-S09','CH10-S10')): f['section_id']=sid
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
# Bring CH10 image records up to the current schema.
p=R/'data/assets.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
figs=yaml.safe_load((R/'assets/chapters/CH10/figure-manifest.yaml').read_text(encoding='utf-8'))['figures']
for i,f in enumerate(x for x in d if str(x.get('id','')).startswith('ASSET-CH10-FIG-')):
 fig=figs[i]
 f.update({'media_kind':'image','paragraph_reference':f"CH10 {fig['section_id']}",'teaching_purpose':fig['alt_zh'],'research_sources':[{'source_id':fig['source_ids'][0],'accessed':'2026-10-22','locator':None,'purpose':'Conceptual context only; original diagram contains no external image.'}],'original_prompt_or_method':fig['original_prompt_or_method'],'tool_name':None,'tool_version':None,'production_log':fig['production_log'],'rights_risk_review':{'status':'pending','checked_at':'2026-10-22','reviewer':'Codex preliminary review','findings':'Original editable SVG; attribution, accessibility, technical quality, similarity, and publication authorization require human review.'},'caption_zh_tw':fig['caption_zh'],'caption_en':fig['caption_en'],'review_status':fig['review_status'],'approval_status':'pending','publication_targets':fig['publication_targets'],'creator':fig['creator'],'license':'Unconfirmed pending author review','permission':'Not approved for publication','attribution':fig['attribution'],'chapter_ids':['CH10']})
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
print('CH10 now follows stable S01-S12 chapter template.')
