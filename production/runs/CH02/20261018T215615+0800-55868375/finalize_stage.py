from pathlib import Path
import hashlib, json, re, xml.etree.ElementTree as ET
import yaml
ROOT=Path(__file__).resolve().parents[4]
STAGE=ROOT/'staging/CH02-V4'
zhp=STAGE/'zh-TW/CH02-camera-language.md'; enp=STAGE/'en-US/CH02-camera-language.md'
zh=zhp.read_text(encoding='utf-8'); en=enp.read_text(encoding='utf-8')
# Align source citations to stable project IDs; Columbia camera movement is already R012.
zh=zh.replace('[R012][R025]','[R012]').replace('[R001][R009][R010][R011][R025][R026][R027]','[R001][R009][R010][R011][R026][R027]')
en=en.replace('[R012][R025]','[R012]').replace('[R001][R009][R010][R011][R025][R026][R026]','[R001][R009][R010][R011][R026][R027]')
# Fix chapter-local new source references and their matching citations.
en=en.replace('the shot plan. [R026]','the shot plan. [R025]')
# Reference records are local drafts until global bibliography review.
refs='''% CH02 source records; staged only until global metadata merge and editorial review. Accessed 2026-10-18.\n@misc{R025, author={{Columbia University Center for New Media Teaching and Learning}}, title={180-Degree Rule}, howpublished={Columbia Film Language Glossary}, url={https://filmglossary.ccnmtl.columbia.edu/term/180-degree-rule/}, note={Accessed 2026-10-18; educational glossary describing the convention and screen-direction function.}}\n@article{R026, author={{Jay Holben}}, title={Shot Craft: Tools for Camera Movement}, journal={American Cinematographer}, date={2024-04-05}, url={https://theasc.com/article/shot-craft-camera-movement/}, note={Accessed 2026-10-18; professional practice account; includes dolly-zoom setup on Jaws (1975).}}\n@misc{R027, author={{ZEISS}}, title={Zoom or Prime Lens? A Shootout Comparison}, howpublished={ZEISS Lens Blog}, url={https://lenspire.zeiss.com/photo/en/article/1-zoom-or-prime-lens-a-shootout-comparison/}, note={Accessed 2026-10-18; manufacturer technical education; perspective depends on camera position.}}\n@misc{R028, author={{Canon Europe}}, title={Depth of Field}, howpublished={Canon RF Lens World}, url={https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/depth-of-field/index.html}, note={Accessed 2026-10-18; manufacturer explanation of depth-of-field factors.}}\n@misc{R029, author={{Runway Help Center}}, title={Gen-4 Video Prompting Guide}, publisher={Runway}, url={https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide}, note={Accessed 2026-10-18; model-specific official prompting guidance, not a guarantee of physical camera control.}}\n'''
(STAGE/'references.bib').write_text(refs,encoding='utf-8')
# R025–R029 bibliography summaries; R012 remains the camera-history glossary source.
for path,body in [(zhp,zh),(enp,en)]: path.write_text(body,encoding='utf-8')
# Add original SVG draft figures to the relevant sections, with shared IDs and bilingual captions.
insertions_zh=[
('**教學提醒**：','\n\n![景別尺度對照示意圖：五種人物景別比較。](../figures/CH02-DIAG-01-shot-scale.svg)\n\n**CH02-DIAG-001｜景別尺度對照。** 原創可編輯 SVG 草圖；景別邊界依語境而異，尚未編入正式圖號。\n\n**教學提醒**：'),
('不同平台的 UI 安全區可能隨產品變化，正式輸出須另外查核。','不同平台的 UI 安全區可能隨產品變化，正式輸出須另外查核。\n\n![16:9 到 9:16 裁切與安全構圖示意圖。](../figures/CH02-DIAG-05-aspect-safe-area.svg)\n\n**CH02-DIAG-005｜橫直式重構圖。** 原創可編輯 SVG 草圖；平台介面安全區仍須依當前規格查證。'),
('運鏡至少要說清楚四件事：','![Dolly 與 Zoom 對照示意圖。](../figures/CH02-DIAG-02-dolly-vs-zoom.svg)\n\n**CH02-DIAG-002｜Dolly 與 Zoom。** 原創可編輯 SVG 草圖。\n\n運鏡至少要說清楚四件事：'),
('## 2.7 空間連續性與 180 度規則','## 2.7 空間連續性與 180 度規則'),
('## 傳統攝影製作流程','![Pan 與 Truck 運鏡差異示意圖。](../figures/CH02-DIAG-03-pan-vs-truck.svg)\n\n**CH02-DIAG-003｜Pan 與 Truck。** 原創可編輯 SVG 草圖。\n\n## 傳統攝影製作流程')]
for old,new in insertions_zh:
 if old not in zh: raise SystemExit('missing zh insertion marker: '+old)
 zh=zh.replace(old,new,1)
marker='### 2.7.2 專業審片問題'
if marker not in zh: raise SystemExit('missing axis insertion marker')
zh=zh.replace(marker,'![對話動作軸與常用攝影機側的俯視示意圖。](../figures/CH02-DIAG-04-180-axis.svg)\n\n**CH02-DIAG-004｜180 度軸線。** 原創可編輯 SVG 草圖；此為連戲慣例示意，不是禁令。\n\n'+marker,1)
zhp.write_text(zh,encoding='utf-8')
# English figure placements correspond to the same IDs.
en=en.replace('## Key terms and bilingual glossary {#CH02-S03}','## Key terms and bilingual glossary {#CH02-S03}')
en=en.replace('| `TERM-CH02-PERSPECTIVE` | 透視 | Perspective | Projected spatial depth and relative size/position relations, affected by camera position. |','| `TERM-CH02-PERSPECTIVE` | 透視 | Perspective | Projected spatial depth and relative size/position relations, affected by camera position. |\n\n![Original editable schematic comparing five shot scales.](../figures/CH02-DIAG-01-shot-scale.svg)\n\n**CH02-DIAG-001 | Shot-scale comparison.** Original editable SVG draft; shot-size boundaries vary by context and this graphic has no canonical book figure number yet.')
en=en.replace('A move can be narratively effective while the camera stays still.','A move can be narratively effective while the camera stays still.\n\n![Original editable schematic comparing dolly and zoom.](../figures/CH02-DIAG-02-dolly-vs-zoom.svg)\n\n**CH02-DIAG-002 | Dolly versus zoom.** Original editable SVG draft.')
en=en.replace('For dialogue or movement, first define the action axis.','![Original editable schematic comparing pan and truck.](../figures/CH02-DIAG-03-pan-vs-truck.svg)\n\n**CH02-DIAG-003 | Pan versus truck.** Original editable SVG draft.\n\nFor dialogue or movement, first define the action axis.')
en=en.replace('## Step-by-step workflow {#CH02-S07}','![Original editable top-down schematic of an action axis.](../figures/CH02-DIAG-04-180-axis.svg)\n\n**CH02-DIAG-004 | The 180-degree axis.** Original editable SVG draft; a continuity convention, not a prohibition.\n\n## Step-by-step workflow {#CH02-S07}')
en=en.replace('Platform interface safe zones change and must be checked against the current platform specifications.','Platform interface safe zones change and must be checked against the current platform specifications.\n\n![Original editable schematic showing a portrait crop in a 16:9 frame.](../figures/CH02-DIAG-05-aspect-safe-area.svg)\n\n**CH02-DIAG-005 | Reframing from 16:9 to 9:16.** Original editable SVG draft; current platform interface safe zones still need checking.')
enp.write_text(en,encoding='utf-8')
# Ensure current ASC URL and R025/R026 references are accurate in English references.
en=enp.read_text(encoding='utf-8')
en=en.replace('- [R012] and [R025] Columbia University Center for New Media Teaching and Learning, “Camera Movement,” *Columbia Film Language Glossary*. Educational glossary; access date 2026-10-18. Its historical overview should be checked against specialist film histories.','- [R012] Columbia University Center for New Media Teaching and Learning, “Camera Movement,” *Columbia Film Language Glossary*. Educational glossary; access date 2026-10-18. Its historical overview should be checked against specialist film histories.')
en=en.replace('- [R026] Columbia University Center for New Media Teaching and Learning, “180-Degree Rule,” *Columbia Film Language Glossary*. Access date 2026-10-18.','- [R025] Columbia University Center for New Media Teaching and Learning, “180-Degree Rule,” *Columbia Film Language Glossary*. Access date 2026-10-18.')
en=en.replace('verify the staging-host URL and full article metadata before publication.','published 2024-04-05; professional practice account.')
enp.write_text(en,encoding='utf-8')
# Correct SVG intrinsic viewBox dimensions in the manifest and calculate definitive hashes.
manifest=yaml.safe_load((STAGE/'figure-manifest.yaml').read_text(encoding='utf-8'))
for rec in manifest['figures']:
 p=ROOT/rec['file_path']; root=ET.parse(p).getroot(); nums=root.attrib['viewBox'].split(); rec['width']=int(float(nums[2])); rec['height']=int(float(nums[3])); rec['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(STAGE/'figure-manifest.yaml').write_text(yaml.safe_dump(manifest,allow_unicode=True,sort_keys=False),encoding='utf-8')
# Update bilingual section/term/figure alignment map.
def ids(path): return sorted(set(re.findall(r'\{#(CH02-S\d+)\}',path.read_text(encoding='utf-8'))))
zh_ids=ids(zhp); en_ids=ids(enp)
zh_terms=re.findall(r'`(TERM-CH02-[A-Z0-9-]+)`',zhp.read_text(encoding='utf-8'))
en_terms=re.findall(r'`(TERM-CH02-[A-Z0-9-]+)`',enp.read_text(encoding='utf-8'))
align={'schema_version':1,'chapter_id':'CH02','status':'draft-alignment-needs-editor-review','section_pairs':[{'id':i,'zh-TW':i,'en-US':i,'status':'draft-aligned'} for i in zh_ids if i in en_ids],'term_pairs':[{'term_id':i,'status':'draft-aligned'} for i in zh_terms if i in en_terms],'figure_pairs':[{'figure_id':r['figure_id'],'zh_caption':r['zh_caption'],'en_caption':r['en_caption'],'zh_alt':r['alt_zh'],'en_alt':r['alt_en'],'status':'draft-aligned'} for r in manifest['figures']]}
(STAGE/'CH02-alignment.yaml').write_text(yaml.safe_dump(align,allow_unicode=True,sort_keys=False),encoding='utf-8')
(STAGE/'source-records/CH02-source-crosswalk.md').write_text('''# CH02 source-pack reference crosswalk\n\nSource-pack labels are mapped to project-wide stable IDs; the source labels R01–R05 are not used as global IDs.\n\n| Source-pack label | Project source ID | Source | Status |\n|---|---|---|---|\n| R01 | R002 | Runway Academy Prompting Guide | official; product claims time-sensitive |\n| R02 | R006 | Runway Gen-4 Video Prompting Guide | official; Gen-4-specific |\n| R03 | R003 | Runway Image-to-Video Prompting Guide | official; model-specific |\n| R04 | R007 | Runway AI camera prompts article | vendor education; not independent theory |\n| R05 | R008 | Runway AI camera control article | vendor education; recheck version before publication |\n| Added | R012 | Columbia Camera Movement | educational film glossary; bounded history |\n| Added | R025 | Columbia 180-Degree Rule | educational film glossary |\n| Added | R026 | American Cinematographer camera-movement article | accessed official article 2024-04-05 record |\n| Added | R027 | ZEISS perspective/lens article | manufacturer technical education |\n| Added | R028 | Canon depth-of-field page | manufacturer technical education |\n| Added | R029 | Runway Gen-4 prompt guide | official model-specific guide |\n\nAccess date for live pages: 2026-10-18. Page locators for the named cinematography books still require edition-level inspection.\n''',encoding='utf-8')
print('Finalized staging; sections zh/en:',len(zh_ids),len(en_ids),'terms:',len(zh_terms),len(en_terms),'figures:',len(manifest['figures']))
