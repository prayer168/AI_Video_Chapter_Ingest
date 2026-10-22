"""Append CH16-only bibliography, terminology, and figure records without reserializing existing registries."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-10-23"

references = [
    {"id":"R112","type":"technical-guide","title":"The Essential Reference Guide for Filmmakers","authors":["Eastman Kodak Company"],"publisher":"Eastman Kodak Company","publication_date":"n.d.","url":"https://www.kodak.com/content/products-brochures/Film/kodak-essential-reference-guide-for-filmmakers.pdf","accessed":TODAY,"locator":"PDF pp. 49–55 (Basic Sensitometry and Characteristics of Film), 109–114 (Exposing Film), 115–122 (Exposure Tools).","language":"en","status":"verified-source-page-scope-limited","notes":"Official manufacturer technical guide; source locator checked against PDF table of contents."},
    {"id":"R113","type":"technical-white-paper","title":"Dynamic Range – White Paper","authors":["ARRI"],"publisher":"ARRI","publication_date":"2022-09-28","url":"https://www.arri.com/resource/blob/295460/e10ff8a5b3abf26c33f8754379b57442/2022-09-28-arri-dynamic-range-whitepaper-data.pdf","accessed":TODAY,"locator":"PDF pp. 13–18; exposure, EI, ALEXA false-color zones, highlights/shadows, and exposure latitude.","language":"en","status":"verified-source-page-scope-limited","notes":"Manufacturer white paper. Scope limited to the ALEXA and Log C systems discussed; do not generalize all thresholds or ARRIRAW behavior."},
    {"id":"R114","type":"manufacturer-technical-page","title":"Column-Parallel A/D Conversion Circuit","authors":["Sony Semiconductor Solutions Group"],"publisher":"Sony Semiconductor Solutions Group","publication_date":"n.d.","url":"https://www.sony-semicon.com/en/technology/is/columnad.html","accessed":TODAY,"locator":"Overview and Technical Features sections.","language":"en","status":"verified-source-page-scope-limited","notes":"Official explanation of a specific sensor readout architecture and its claimed benefits."},
    {"id":"R115","type":"manufacturer-glossary","title":"Glossary of Motion Picture Terms","authors":["Eastman Kodak Company"],"publisher":"Eastman Kodak Company","publication_date":"n.d.","url":"https://www.kodak.com/en/motion/page/glossary-of-motion-picture-terms/","accessed":TODAY,"locator":"Entries Exposure, Exposure Index, Characteristic Curve, Toe, Straight-Line Region, Shoulder, Sensitometry.","language":"en","status":"verified-source-page-scope-limited","notes":"Official manufacturer glossary; definitions are source material for working terms, not a complete theory reference."},
    {"id":"R116","type":"camera-user-manual","title":"ALEXA LF User Manual, Software Update Package 4.0","authors":["ARRI"],"publisher":"ARRI","publication_date":"n.d.","url":"https://www.arri.com/resource/blob/147832/ccb47e7386f7e1f9161a885bf42781a0/arri-alexa-lf-user-manual-sup-4-0-data.pdf","accessed":TODAY,"locator":"Camera Controls p. 59; Shutter pp. 66–67. PDF text checked for shutter-angle formula and EI notes.","language":"en","status":"verified-source-page-scope-limited","notes":"Camera model and software-update-package specific. Do not present its settings as universal camera behavior."},
    {"id":"R117","type":"scientific-history-reference","title":"The Nobel Prize in Physics 2009 — Illustrated Information","authors":["Nobel Prize Outreach"],"publisher":"Nobel Prize Outreach","publication_date":"2009","url":"https://www.nobelprize.org/prizes/physics/2009/illustrated-information/?print=1","accessed":TODAY,"locator":"The masters of light; CCD image-sensor description and Boyle/Smith chronology.","language":"en","status":"verified-source-page-scope-limited","notes":"Nobel Prize background page; used for the CCD historical summary and basic description, not as a sensor design manual."},
    {"id":"R118","type":"manufacturer-technical-history-page","title":"Common Technology of Image Sensors","authors":["Sony Semiconductor Solutions Group"],"publisher":"Sony Semiconductor Solutions Group","publication_date":"n.d.","url":"https://www.sony-semicon.com/en/technology/is/index.html","accessed":TODAY,"locator":"Types and structural comparison of CCD and CMOS image sensors; Sony technology chronology.","language":"en","status":"verified-source-page-scope-limited","notes":"Company-authored technology account; historical claims are explicitly scoped to Sony's technologies and products."},
    {"id":"R119","type":"manufacturer-image-science-faq","title":"Visual Effects FAQ","authors":["ARRI"],"publisher":"ARRI","publication_date":"n.d.","url":"https://www.arri.com/en/learn/camera-systems/image-science/vfx-faq","accessed":TODAY,"locator":"FAQ entry 'What is the Log C format?' (web page lines 64–72 in the checked version).","language":"en","status":"verified-source-page-scope-limited","notes":"Official ARRI image-science explanation; Log C / negative-scan similarity is an encoding analogy, not sensor equivalence."},
]

terms = [
    ("EXPOSURE","曝光","exposure","光在一定時間內作用於感光材料或感光元件所形成的記錄條件；在電影攝影中須同時說明場景照度、曝光時間及影像系統的測光／感光設定。 / The recording condition produced when light acts on a photosensitive material or sensor for a period of time; specify illumination, exposure time, and system settings.",["R112","R115"]),
    ("EXPOSURE-INDEX","曝光指數","exposure index (EI)","用以表示曝光／感光度參照的設定或標示；底片 EI 與數位攝影機 EI 的實作與意義不可逕行等同。 / A setting or rating used as an exposure/sensitivity reference; film and digital-camera EI are not automatically equivalent.",["R113","R115","R116"]),
    ("SPEED-RATING","感光度標示","speed rating / ISO rating","按指定標準或廠商方法描述感光材料／系統響應的標示；提高數值本身不會增加到達感光面的光子。 / A rating of response under a stated standard or method; changing the number does not itself deliver more photons to the sensor.",["R115","R116"]),
    ("IMAGE-SENSOR","感光元件","image sensor","將入射光轉成電荷或電子訊號，再由讀出與影像處理鏈轉為影像資料的器件。 / A device that converts incident light into charge or an electronic signal, then into image data through readout and processing.",["R114","R117","R118"]),
    ("PHOTODIODE","光電二極體","photodiode","感光元件中吸收光並產生電荷的光敏結構；實際像素電路會因架構而不同。 / A photosensitive sensor structure that absorbs light and produces charge; pixel circuits vary by architecture.",["R117","R118"]),
    ("DYNAMIC-RANGE","動態範圍","dynamic range","成像系統在可接受品質下同時記錄暗部至亮部的範圍；數值依定義、噪訊門檻、格式與測試方法而異。 / The dark-to-bright range an imaging system can record at acceptable quality; values depend on definition, noise threshold, format, and test method.",["R113"]),
    ("SATURATION-CLIPPING","飽和／剪裁","saturation / clipping","訊號到達系統可表示或可區分的上限後，更多入射光不再帶來可分辨的亮部資訊；顯示端剪裁可能不同於感光元件飽和。 / A signal reaches its representable or distinguishable upper limit; display clipping may differ from sensor saturation.",["R113","R116"]),
    ("SNR","訊噪比","signal-to-noise ratio (SNR)","有用影像訊號相對於噪訊的比值；須標明量測條件。 / The ratio of useful image signal to noise; measurement conditions should be stated.",["R113","R114"]),
    ("SENSITOMETRY","感光測定","sensitometry","研究感光乳劑或材料對受控曝光的反應；底片特性曲線呈現曝光與處理後密度的關係。 / The study of photosensitive materials under controlled exposure; a film characteristic curve relates exposure to processed density.",["R112","R115"]),
    ("CHARACTERISTIC-CURVE","特性曲線","characteristic curve","顯示感光材料曝光量與處理後影像密度關係的曲線；數位 Log 編碼與底片密度曲線不是同一物理量。 / A curve relating material exposure to processed density; digital Log encoding and film density are different physical quantities.",["R112","R115"]),
    ("SHUTTER-ANGLE","快門角度","shutter angle","以角度表示每一影格的曝光時間；ARRI ALEXA LF 手冊所列關係為曝光時間＝角度÷（360×感光影格率）。 / An angle expressing exposure time per frame; the ARRI ALEXA LF manual gives exposure time = angle ÷ (360 × sensor frame rate).",["R116"]),
    ("EXPOSURE-LATITUDE","曝光寬容度","exposure latitude","曝光偏離參考值後仍可接受地重現影像的範圍；須指明媒介、觀看條件及接受標準。 / The range over which an image remains acceptable after exposure departs from a reference; specify medium, viewing conditions, and criteria.",["R112","R113","R115"]),
]

def append_yaml_list(path: str, rows: list[dict]) -> None:
    p = ROOT / path
    existing = yaml.safe_load(p.read_text(encoding="utf-8")) or []
    ids = {row.get("id") for row in existing if isinstance(row, dict)}
    add = [row for row in rows if row.get("id") not in ids]
    if add:
        with p.open("a", encoding="utf-8", newline="\n") as f:
            f.write("\n" + yaml.safe_dump(add, allow_unicode=True, sort_keys=False, width=110))

append_yaml_list("data/references.yaml", references)

data_terms = []
metadata_terms = []
for suffix, zh, en, definition, sources in terms:
    data_terms.append({"id":f"TERM-CH16-{suffix}","zh_TW":zh,"en":en,"variants":[],"definition":definition,"domain":"cinematography and image science","status":"draft","source_ids":sources,"related_terms":[],"notes":"CH16 working definition; bilingual and cinematography review pending.","updated":TODAY})
    metadata_terms.append({"term_id":f"TERM-CH16-{suffix}","preferred":{"zh-TW":zh,"en-US":en},"definitions":{"zh-TW":definition.split(" / ",1)[0],"en-US":definition.split(" / ",1)[1]},"domain":"cinematography and image science","context":"CH16 working definition; bilingual and cinematography review pending.","synonyms":{"zh-TW":[],"en-US":[]},"see_also":[],"status":"draft","reviewed_by":None,"reviewed_on":None,"references":sources})
append_yaml_list("data/terms.yaml", data_terms)

figure_specs = [
    {"id":"CH16-FIG-001","section":"CH16-S05","placement":"after:CH16-S05","display":"16-1","file":"assets/chapters/CH16/figures/originals/CH16-FIG-001-image-formation-pipeline.svg","zh":"圖 16-1｜底片與數位影像形成路徑。原創手繪技術示意圖，依 R112、R114、R117–R118 文字資料自行繪製，非電影劇照。","en":"Figure 16-1 | Film and digital image-formation paths. Original hand-authored technical schematic based on R112, R114, R117, and R118; not a film still.","altzh":"雙欄流程圖比較電影底片與數位感光元件的受光、訊號形成、處理及交付路徑，並標示兩者不可直接等同。","alten":"A two-column flow diagram compares light capture, signal formation, processing, and delivery for film and digital sensors, noting that the processes are not equivalent.","sources":["R112","R114","R117","R118"],"purpose":"對照底片化學成像與數位感光元件訊號鏈，避免把特性曲線與數位 Log 視為相同物理量。"},
    {"id":"CH16-FIG-002","section":"CH16-S07","placement":"after:CH16-S07","display":"16-2","file":"assets/chapters/CH16/figures/originals/CH16-FIG-002-exposure-decision-workflow.svg","zh":"圖 16-2｜曝光決策與驗證工作流。原創手繪流程示意，非電影畫面或特定器材操作順序。","en":"Figure 16-2 | Exposure decision and verification workflow. Original hand-authored workflow schematic, not a film image or a device-specific control sequence.","altzh":"流程圖從敘事優先事項開始，經場景反差與拍攝條件，進入測量、測試、訊號驗證與拍攝紀錄。","alten":"A workflow begins with narrative priorities, moves through scene contrast and capture conditions, then metering, testing, signal verification, and camera-report documentation.","sources":["R113","R116"],"purpose":"把敘事資訊保留、測光測試、訊號確認及交接紀錄整理為可檢查流程。"},
]

registry_figures=[]
assets=[]
manifest_figures=[]
for fig in figure_specs:
    p=ROOT/fig["file"]
    raw=p.read_bytes()
    import xml.etree.ElementTree as ET
    root=ET.fromstring(raw)
    view=root.attrib["viewBox"].split()
    width,height=int(float(view[2])),int(float(view[3]))
    digest=hashlib.sha256(raw).hexdigest()
    fig_id=fig["id"]
    registry_figures.append({"figure_id":fig_id,"chapter_id":"CH16","section_id":fig["section"],"placement_after":fig["placement"],"source_ids":fig["sources"],"asset_original":fig["file"],"asset_approved":None,"rights_review":"pending","technical_review":"pending","editorial_review":"pending","publication_status":"pending-publication-approval","display_number":fig["display"],"asset_status":"draft-original-svg","rights_status":"original-project-svg-pending-human-review","caption_zh":fig["zh"],"caption_en":fig["en"],"alt_zh":fig["altzh"],"alt_en":fig["alten"],"creator":"AI Video Bible project; individual attribution pending confirmation","attribution":"Creator and rights-holder attribution pending confirmation.","permission":"Publication approval pending.","original_prompt_or_method":"Hand-authored editable bilingual SVG; no third-party images or generative image model.","note":"Technical, editorial, accessibility, similarity, rights, and author review pending.","sha256":digest,"bytes":len(raw),"width":width,"height":height,"production_log":[{"date":TODAY,"change":"Hand-authored editable SVG; dimensions, byte count and SHA-256 recorded."}]})
    assets.append({"id":f"ASSET-{fig_id}","path":fig["file"],"type":"original-svg-diagram","description":fig["zh"],"creator":"AI Video Bible project; individual attribution pending confirmation","source_url":None,"created_at":TODAY,"license":"Unconfirmed","permission":"Publication approval pending.","attribution":"Creator and rights-holder attribution pending confirmation.","chapter_ids":["CH16"],"notes":"Technical, editorial, accessibility, similarity, rights, and author review pending.","media_kind":"image","figure_id":fig_id,"paragraph_reference":f"CH16 {fig_id}","teaching_purpose":fig["purpose"],"research_sources":[{"source_id":sid,"accessed":TODAY,"locator":"Textual context only; no source image used.","purpose":"Background for original schematic; not copied artwork."} for sid in fig["sources"]],"production_method":"Hand-authored editable bilingual SVG; no third-party imagery or generative image model.","sha256":digest,"bytes":len(raw),"width":width,"height":height,"caption_zh_tw":fig["zh"],"caption_en":fig["en"],"alt_zh_tw":fig["altzh"],"alt_en":fig["alten"],"approval_status":"pending","publication_targets":{"zh-TW-book":"pending","en-book":"pending","zh-TW-site":"pending","en-site":"pending"},"review_status":{"technical":"pending","quality":"pending","rights":"pending","final":"pending"},"original_prompt_or_method":"Hand-authored editable bilingual SVG; no third-party imagery or generative image model.","tool_name":None,"tool_version":None,"production_log":[{"date":TODAY,"change":"Hand-authored editable SVG; recorded dimensions, byte count, and SHA-256."}],"rights_risk_review":{"status":"pending","checked_at":None,"reviewer":"pending","findings":"Similarity, authorship, accessibility, and publication rights need human review."}})
    manifest_figures.append({"figure_id":fig_id,"chapter_id":"CH16","section_id":fig["section"],"display_number":fig["display"],"asset_original":fig["file"],"asset_approved":None,"asset_status":"draft-original-svg","rights_status":"original-project-svg-pending-human-review","rights_review":"pending","technical_review":"pending","editorial_review":"pending","publication_status":"pending-publication-approval","source_ids":fig["sources"],"teaching_purpose":fig["purpose"],"caption_zh":fig["zh"],"caption_en":fig["en"],"alt_zh":fig["altzh"],"alt_en":fig["alten"],"creator":"AI Video Bible project; individual attribution pending confirmation","attribution":"Creator and rights-holder attribution pending confirmation.","permission":"Publication approval pending.","original_prompt_or_method":"Hand-authored editable bilingual SVG; no third-party imagery or generative image model.","note":"Draft schematic; do not mark approved or publication-ready.","sha256":digest,"bytes":len(raw),"width":width,"height":height,"production_log":[{"date":TODAY,"change":"Created original editable SVG and recorded SHA-256."}]})

append_yaml_list("data/assets.yaml", assets)

def append_registry(path: str, key: str, rows: list[dict]) -> None:
    p=ROOT/path
    data=yaml.safe_load(p.read_text(encoding="utf-8"))
    id_key="term_id" if key == "terms" else "figure_id"
    existing={row.get(id_key) for row in data.get(key,[])}
    add=[row for row in rows if row.get(id_key) not in existing]
    if add:
        block=yaml.safe_dump(add,allow_unicode=True,sort_keys=False,width=110)
        prefix="  " if path.startswith("assets/chapters/") else ""
        indented="\n".join(prefix+line if line else line for line in block.rstrip().splitlines())
        with p.open("a",encoding="utf-8",newline="\n") as f:
            f.write("\n"+indented+"\n")

append_registry("metadata/figure-registry.yaml","figures",registry_figures)
append_registry("metadata/terminology.yaml","terms",metadata_terms)
append_registry("assets/chapters/CH16/figure-manifest.yaml","figures",manifest_figures)

# Update only the CH16 translation status block and chapter record; do not reserialize registries.
status_path=ROOT/"metadata/translation-status.yaml"
text=status_path.read_text(encoding="utf-8")
text,n=re.subn(r"(?m)^  CH16:\n    zh-TW: .*\n    en-US: .*\n    sync_revision: .*", "  CH16:\n    zh-TW: review-needed\n    en-US: review-needed\n    sync_revision: 2.1.0-draft", text, count=1)
if n != 1: raise RuntimeError("Could not update unique CH16 translation status block")
status_path.write_text(text,encoding="utf-8",newline="\n")

chapter_path=ROOT/"metadata/chapters.yaml"
text=chapter_path.read_text(encoding="utf-8")
pattern=r"(?ms)(- chapter_id: CH16\n.*?  title_en: ).*?(\n  legacy_status: ).*?(\n  zh_status: ).*?(\n  en_status: ).*?(?=\n- chapter_id:|\Z)"
replacement=r"\g<1>'Exposure, Image Sensors, and Image Formation'\g<2>review-needed\g<3>review-needed\g<4>review-needed"
text,n=re.subn(pattern,replacement,text,count=1)
if n != 1: raise RuntimeError("Could not update unique CH16 chapter metadata")
chapter_path.write_text(text,encoding="utf-8",newline="\n")

bib=ROOT/"metadata/references.bib"
bib_records = """
@misc{R112, author = {{Eastman Kodak Company}}, title = {The Essential Reference Guide for Filmmakers}, url = {https://www.kodak.com/content/products-brochures/Film/kodak-essential-reference-guide-for-filmmakers.pdf}, note = {Official technical guide; pp. 49--55, 109--122; accessed 2026-10-23}}
@misc{R113, author = {{ARRI}}, title = {Dynamic Range -- White Paper}, date = {2022-09-28}, url = {https://www.arri.com/resource/blob/295460/e10ff8a5b3abf26c33f8754379b57442/2022-09-28-arri-dynamic-range-whitepaper-data.pdf}, note = {ALEXA/Log C scope; PDF pp. 13--18; accessed 2026-10-23}}
@misc{R114, author = {{Sony Semiconductor Solutions Group}}, title = {Column-Parallel A/D Conversion Circuit}, url = {https://www.sony-semicon.com/en/technology/is/columnad.html}, note = {Manufacturer technical page; accessed 2026-10-23}}
@misc{R115, author = {{Eastman Kodak Company}}, title = {Glossary of Motion Picture Terms}, url = {https://www.kodak.com/en/motion/page/glossary-of-motion-picture-terms/}, note = {Official glossary; accessed 2026-10-23}}
@misc{R116, author = {{ARRI}}, title = {ALEXA LF User Manual, Software Update Package 4.0}, url = {https://www.arri.com/resource/blob/147832/ccb47e7386f7e1f9161a885bf42781a0/arri-alexa-lf-user-manual-sup-4-0-data.pdf}, note = {Model/version-specific; accessed 2026-10-23}}
@misc{R117, author = {{Nobel Prize Outreach}}, title = {The Nobel Prize in Physics 2009 -- Illustrated Information}, url = {https://www.nobelprize.org/prizes/physics/2009/illustrated-information/?print=1}, note = {CCD historical background; accessed 2026-10-23}}
@misc{R118, author = {{Sony Semiconductor Solutions Group}}, title = {Common Technology of Image Sensors}, url = {https://www.sony-semicon.com/en/technology/is/index.html}, note = {Sony technology history, scope limited to named products; accessed 2026-10-23}}
@misc{R119, author = {{ARRI}}, title = {Visual Effects FAQ}, url = {https://www.arri.com/en/learn/camera-systems/image-science/vfx-faq}, note = {Official FAQ, Log C format entry; accessed 2026-10-23}}
"""
bib_path=ROOT/"metadata/references.bib"
bibtext=bib_path.read_text(encoding="utf-8")
new_bib=[]
for block in bib_records.strip().splitlines():
    rid=re.search(r"\{(R\d+),",block).group(1)
    if f"{{{rid}," not in bibtext: new_bib.append(block)
if new_bib: bib_path.write_text(bibtext.rstrip()+"\n\n"+"\n\n".join(new_bib)+"\n",encoding="utf-8",newline="\n")

print(f"Registered {len(references)} sources, {len(terms)} bilingual terms, and {len(figure_specs)} figures.")
