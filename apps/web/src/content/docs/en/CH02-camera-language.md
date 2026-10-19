---
chapter_id: CH02
part_id: P01
lang: en-US
title: "AI Video Bible | Chapter 2"
book_title: AI Video Bible
registry_title: "Shot, Scene, and Editing: The Basic Units of Film Language"
working_title: "Shot Scale, Composition, and Camera Language: From Directorial Intent to Verifiable Shot Specifications"
translation_status: review-needed
editorial_status: draft-for-human-review
canonical_status: draft-migration-pending
revision: 2.1.0-draft
source_zh: staging/CH02-V4/zh-TW/CH02-camera-language.md
last_updated: 2026-10-18
claim_types: [verified-fact, theory, practice, ai-hypothesis, demo]
related_chapters: [CH01]
---

<a id="CH02"></a>
# CH02 | Shot, Scene, and Editing: The Basic Units of Film Language
> Editorial note: The source manuscript uses “Shot Scale, Composition, and Camera Language” as its subtitle. The difference from the book registry title needs editorial confirmation.

> **Translation status: draft; not professionally reviewed.** This English text is an editorial translation draft of the Traditional Chinese source, not an independently researched or approved edition. All film, theory, and tool-specific claims retain the source's limitations and review flags.

<a id="CH02-S00"></a>
## Chapter overview
This chapter provides a practical method for translating narrative intent into shootable or generatable shot specifications. It covers shot scale, composition, camera angle, focal length, perspective, depth of field, camera movement, and continuity across shots. Traditional cinematography provides the working baseline; AI prompts and shot specifications are treated as descriptions of intent that must be checked against visible evidence, not as guarantees of physical camera control.

<a id="CH02-S01"></a>
## Learning outcomes
After completing this chapter, learners should be able to:

1. Select and explain extreme wide, wide, full, medium-long, medium, medium close-up, close-up, and extreme close-up framings.
2. Distinguish shot scale, composition, camera angle, focal length, camera-to-subject distance, perspective, and depth of field.
3. Explain why camera position affects perspective and distinguish a dolly move from a zoom.
4. Compare pan, tilt, truck, dolly, pedestal, crane, orbit, handheld, and locked-off camera approaches.
5. Use eyelines, the 180-degree convention, headroom, lead room, and continuity planning to make screen space understandable.
6. Write a JSON shot specification with observable acceptance criteria.
7. Plan a 30–60 second short film and submit a shot list, prompt versions, production record, and reflection.

<a id="CH02-S02"></a>
## Prerequisites
Basic editing and shot vocabulary are helpful; no prior camera-gear experience is required. Learners should recognize scenes, shots, frames, and timecodes. The practical assignments can be completed with a camera, a video generator whose use is authorized, or still-frame diagrams. Generated imagery must not be represented as evidence of a physical or scientific result.

<a id="CH02-S03"></a>
## Key terms and bilingual glossary
Definitions below are working definitions. Framing boundaries differ among productions; the glossary is a draft and requires review by a cinematography or film-education editor.

| Term ID | Traditional Chinese | English preferred term | Working definition |
|---|---|---|---|
| `TERM-CH02-EWS` | 極遠景 | Extreme Wide Shot (EWS) | The subject is very small relative to an environment that carries most of the visual information. |
| `TERM-CH02-WS` | 遠景 | Wide Shot (WS) | Frames a person's full or most of their body together with surrounding space. |
| `TERM-CH02-FS` | 全身景 | Full Shot (FS) | Generally includes the full body; conventions vary by context. |
| `TERM-CH02-MLS` | 中遠景 | Medium Long Shot (MLS) | Often frames around the knees upward; this is not a universal boundary. |
| `TERM-CH02-MS` | 中景 | Medium Shot (MS) | Often frames roughly from the waist up, balancing gesture, expression, and context. |
| `TERM-CH02-MCU` | 中近景 | Medium Close-Up (MCU) | Often frames a person from the chest up, with limited surrounding context. |
| `TERM-CH02-CU` | 特寫 | Close-Up (CU) | Makes a face or important object the primary visual information. |
| `TERM-CH02-ECU` | 大特寫 | Extreme Close-Up (ECU) | Shows a very small detail of a face or object. |
| `TERM-CH02-OTS` | 越肩鏡頭 | Over-the-Shoulder (OTS) | Frames a person or space past a foreground shoulder or head. |
| `TERM-CH02-POV` | 主觀視角 | Point of View (POV) | Organizes an image as a character's view or perception, established by context. |
| `TERM-CH02-DOLLY` | 攝影機前後移動 | Dolly Movement | Physically translates the camera forward or backward through space. |
| `TERM-CH02-ZOOM` | 變焦 | Zoom | Changes focal length and angle of view, potentially from a fixed camera position. |
| `TERM-CH02-PAN` | 水平搖攝 | Pan | Rotates the camera horizontally around a fixed or near-fixed position. |
| `TERM-CH02-TILT` | 垂直搖攝 | Tilt | Rotates the camera vertically around a fixed or near-fixed position. |
| `TERM-CH02-TRUCK` | 橫向平移 | Truck Movement | Translates the camera sideways; it is distinct from a pan in place. |
| `TERM-CH02-PEDESTAL` | 上下平移 | Pedestal | Moves the whole camera vertically; it is distinct from a tilt. |
| `TERM-CH02-ORBIT` | 環繞運鏡 | Orbit | Moves the camera position along an arc around a subject. |
| `TERM-CH02-RACK-FOCUS` | 轉焦 | Rack Focus | Shifts sharp focus from one distance plane to another within a shot. |
| `TERM-CH02-DEPTH-OF-FIELD` | 景深 | Depth of Field (DoF) | The range of object distances that appear acceptably sharp under specified viewing conditions. |
| `TERM-CH02-CONTINUITY` | 連續性 | Continuity | Editing consistency that keeps time, space, action, eyeline, and prop relations understandable. |
| `TERM-CH02-180-DEGREE-RULE` | 180 度軸線規則 | 180-Degree Rule | A continuity convention that keeps cameras on one side of an action axis to preserve screen direction; an intentional crossing requires reorienting the viewer. |
| `TERM-CH02-LEAD-ROOM` | 前方留白／視線留白 | Lead Room | Space left in front of a person in the direction of gaze or movement. |
| `TERM-CH02-HEADROOM` | 頭頂留白 | Headroom | Space between the top of a person's head and the upper edge of the frame. |
| `TERM-CH02-NEGATIVE-SPACE` | 負空間 | Negative Space | Areas around the subject not occupied by primary objects but functioning compositionally. |
| `TERM-CH02-FOCAL-LENGTH` | 焦距 | Focal Length | A lens-system parameter that, together with sensor size, relates to angle of view. |
| `TERM-CH02-PERSPECTIVE` | 透視 | Perspective | Projected spatial depth and relative size/position relations, affected by camera position. |

<figure id="CH02-FIG-001"><img src="/images/chapters/CH02/CH02-DIAG-01-shot-scale.svg" alt="Original schematic comparing subject scale across five shot sizes." /><figcaption>Figure 2-1A | Original schematic comparing subject scale across five shot sizes. This is an original editable SVG schematic, not a filmed example or tool benchmark.</figcaption></figure>

<a id="CH02-S04"></a>
## History and principles
Camera movement can refer to the physical movement of camera equipment through space or to movement perceived by the viewer. Columbia University's film-language glossary describes early cinematographer Eugenio Promio mounting a camera on moving vehicles and boats, and notes that swivel heads around 1900 increased the use of pans. It explicitly cautions that the first camera movement cannot be identified with certainty; this chapter therefore does not call Promio the “first camera-movement practitioner.” The glossary also summarizes later developments and constraints. Treat this as a bounded educational summary, not a complete global history; a film historian should verify it against specialist histories before publication. [R012]

For shot design, keep separate records for shot scale (the subject's relative size in frame), composition (the arrangement of elements), angle (camera position relative to the subject), lens and optical look, camera movement, and duration. A bundle of style words can conceal incompatible instructions. Start with the viewer's attention and the subject-space relationship; translate those into visible actions and frame changes before selecting gear or generation settings. These are professional concepts and production recommendations; book-specific locators remain unverified. [R001][R009][R010][R011][R026][R027]

### Shot scale

Shot scale names the subject's relative size in the frame; it is not a focal-length category. Extreme wide shots emphasize environment and distance. Wide and full framings can establish space, body movement, and routes. Medium framings balance gesture, expression, and context. Close-ups and extreme close-ups isolate a face, object, or detail. Naming conventions vary, and a close-up may show an object rather than a face. Select a scale for the information the viewer needs, not because closer framing is inherently more emotional.

### Composition and visual emphasis

The rule of thirds is a positioning aid, not a law. Centered or symmetrical framing can feel direct, balanced, or ceremonial; off-center placement can leave space in the direction of gaze or imply imbalance. Headroom, lead room, negative space, foreground/middle-ground/background layers, leading lines, symmetry, and frame-within-frame are options whose effects depend on context. Do not apply them mechanically. Plan likely crops and subtitle space when delivering multiple aspect ratios. Platform interface safe zones change and must be checked against the current platform specifications.

<figure id="CH02-FIG-005"><img src="/images/chapters/CH02/CH02-DIAG-05-aspect-safe-area.svg" alt="Schematic portrait crop and subject-safe framing." /><figcaption>Figure 2-1E | Schematic portrait crop and subject-safe framing. This is an original editable SVG schematic, not a filmed example or tool benchmark.</figcaption></figure>

### Camera angle and point of view

Eye-level, high-angle, low-angle, overhead, Dutch-angle, POV, and over-the-shoulder describe different viewing relations. Angle and shot scale are separate: a low-angle image can be either a wide shot or a close-up. An angle may suggest status, vulnerability, spatial information, or disorientation in a particular context, but it does not guarantee one meaning or a neutral viewpoint.

### Lens, distance, perspective, and depth of field

Focal length is not shot scale. Focal length and sensor size relate to angle of view; camera-subject distance affects subject size and perspective. When a cinematographer changes camera position to preserve subject size while changing focal length, the resulting viewpoint change affects foreground/background size relations. A focal-length change alone from a fixed position does not move the viewpoint. State the sensor format or full-frame equivalent when comparing focal lengths.

Depth of field is affected by aperture, focal length, focus distance, camera-to-subject distance, subject-to-background distance, sensor format, and viewing conditions. A shallow depth of field can separate a subject from the background; deeper focus can keep information across distances legible. A prompt such as “f/1.8” is not proof that a generative model simulated a lens. Verify the visible result. [R027][R028]

### Camera movement

A pan rotates the camera from a position; a truck translates it sideways. A tilt rotates vertically; a pedestal moves the camera vertically. A dolly physically translates the camera; a zoom changes focal length. A dolly zoom combines camera translation with an opposing zoom to keep subject scale roughly stable while changing the background perspective. Crane/jib, orbit, handheld, locked-off, tracking, rack focus, and whip pan describe distinct movement or focus patterns. For every move, specify start and end framing, direction, duration, speed profile, subject motion, and what should remain stable. A move can be narratively effective while the camera stays still.

<figure id="CH02-FIG-002"><img src="/images/chapters/CH02/CH02-DIAG-02-dolly-vs-zoom.svg" alt="Camera translation changes viewpoint and parallax; zoom changes angle of view." /><figcaption>Figure 2-1B | Camera translation changes viewpoint and parallax; zoom changes angle of view. This is an original editable SVG schematic, not a filmed example or tool benchmark.</figcaption></figure>

### Screen space and the 180-degree convention

<figure id="CH02-FIG-003"><img src="/images/chapters/CH02/CH02-DIAG-03-pan-vs-truck.svg" alt="Pan changes orientation; truck changes camera position." /><figcaption>Figure 2-1C | Pan changes orientation; truck changes camera position. This is an original editable SVG schematic, not a filmed example or tool benchmark.</figcaption></figure>

For dialogue or movement, first define the action axis. Staying on one side commonly preserves screen direction and eyelines; crossing the line is possible, but the viewer may need a neutral shot, visible movement, or a clear spatial re-establishment. Treat the convention as a continuity tool, not an absolute ban. Record screen-left/right, eyelines, prop and doorway positions, light direction, and any deliberate axis crossing in the shot plan. [R025]

<a id="CH02-S05"></a>
## Traditional production practice
Translate a scene into a shot plan before the shoot. Clarify the dramatic or informational purpose; block actors and objects; choose camera positions and lens coverage; check screen direction, eyelines, focus, exposure, movement paths, and sound; rehearse; then record takes and continuity. The script supervisor and camera department keep records that help the editor understand action, props, framing, and selected takes. The specific workflow varies by production size and jurisdiction; this is a practice model, not a universal regulation. [R001][R010][R011]

Before recording, confirm the subject, background, frame edges, focus distance, safe crop, and movement start/end marks. During takes, distinguish camera movement from subject and environmental movement. On review, check focus, exposure, unwanted shake, motion continuity, screen direction, and whether the shot provides the intended editorial options. Preserve metadata and source media when handing footage to editorial.

<a id="CH02-S06"></a>
## AI-era workflow and limitations
Generative-video tools may interpret a camera term as a visual direction rather than as a mechanically constrained camera move. Separate subject motion, environment motion, camera motion, and temporal progression. Use observable results such as “the foreground object shifts left relative to the window as the camera advances,” not just “cinematic dolly.” Tool documentation is time-sensitive and model-specific. Runway's prompting material describes prompt elements and camera-motion language for named products; it is vendor guidance, not independent proof of repeatable camera physics or a guarantee for other tools. [R002][R003][R006][R029]

Keep the selected model, version, date, settings, input image hashes, prompt, take ID, and review notes. Where a tool does not expose a parameter, record `null`; do not invent lens metadata. If exact geometry or scientific behavior matters, use live-action footage, a 3D scene, or a verified diagram rather than treating generated appearance as evidence.

<figure id="CH02-FIG-004"><img src="/images/chapters/CH02/CH02-DIAG-04-180-axis.svg" alt="Top-down schematic of an action axis and conventional camera side." /><figcaption>Figure 2-1D | Top-down schematic of an action axis and conventional camera side. This is an original editable SVG schematic, not a filmed example or tool benchmark.</figcaption></figure>

<a id="CH02-S07"></a>
## Step-by-step workflow
1. Define the viewer's attention and the shot's narrative or teaching purpose.
2. Map subjects, props, doors, windows, eyelines, movement routes, and the action axis.
3. Select shot scale, camera angle, camera position, lens look, movement, and duration as separate fields.
4. Write a shot specification with a start state, end state, visible motion, continuity constraints, and acceptance criteria.
5. For traditional production, rehearse and mark camera/actor positions; for AI production, select an authorized tool and retain its model/version settings.
6. Generate or record one principal change at a time where feasible; keep source inputs and all takes.
7. Review image evidence: framing, scale, parallax, focus, screen direction, identity, object continuity, and unintended motion.
8. Revise the shot specification or production method, not just the adjectives. Escalate precision-critical work to practical cinematography, 3D, or compositing.
9. Hand off selected media with shot IDs, hashes, prompt/production metadata, audio notes, and unresolved defects.
10. Archive the accepted and rejected takes and explain the editorial decision.

<a id="CH02-S08"></a>
## Prompts and technical parameters
Treat prompts as testable intent, not camera-control commands. A model-neutral specification can include:

```text
Shot ID: S02
Purpose: show the student approaching the experiment table
Start frame: medium-wide; student screen-left; glass on table screen-right
Subject motion: student walks slowly toward the table
Camera motion: lateral track left-to-right, parallel to the student
Duration: 9 s (planned; not a tool guarantee)
Lens/look: natural perspective; keep face and glass readable
Continuity: window remains camera-left; glass stays on marked table position
Acceptance: background shows coherent parallax; no unintended reframing or prop duplication
```

For image-to-video, a neutral prompt pattern is: “The subject [one action]. The camera [one move and direction]. The environment [limited motion]. Maintain [continuity constraints]. One continuous shot.” Add details incrementally and inspect outcomes. Official vendor guides recommend iterating and separating motion elements, but results remain model- and version-dependent. No prompts in this chapter have been represented as successful generation tests. [R002][R003][R006]

### Editable shot specification example

```json
{
  "shot_id": "S03",
  "duration_seconds": 8,
  "shot_size": "CU",
  "angle": "eye-level",
  "camera_motion": "locked-off",
  "subject_motion": "student slowly tilts the glass toward the window",
  "continuity": ["glass shape and water level stable", "window remains camera-left"],
  "acceptance": ["glass rim stays intact", "camera does not drift", "observation remains visible"],
  "model": null,
  "model_version": null,
  "generation_status": "not-run"
}
```

<a id="CH02-S09"></a>
## Shot and film case study
### Film-form reference: a dolly-zoom setup

The American Society of Cinematographers' camera-movement article includes discussion of setting up a dolly-zoom shot associated with *Jaws* (1975). This supports a production-technique reference, not a complete interpretation of the film or a verified timecode for a particular edition. A researcher should select a lawful viewing edition and add the exact sequence, timecode, shot observation, and source edition before a detailed analysis is published. [R026]

### Demonstration: *Where Does the Light Come From?*

This 60-second science-short film is a planning demonstration, not a filmed or generated sequence. Its seven-shot list moves from an establishing wide shot to a medium tracking shot, a locked close-up of a glass, a reaction, an over-the-shoulder teacher demonstration, an overhead insert, and a final wide shot. The planned timings total 60 seconds with adjacent boundaries and no gaps or overlaps. They are planning values, not tested model durations.

The complete editable shot list is included in the chapter source asset pack (`CH02-science-shortfilm.json`). The refraction image is a prompt concept only: AI-generated optics must not be presented as experimental evidence. A science teacher should validate the live setup and explain the conditions before any factual science claim is made.

<a id="CH02-S10"></a>
## Common errors and quality checks
| Observed problem | Possible cause | Check or correction |
|---|---|---|
| Dolly prompt produces only a zoom-like enlargement | The model approximated scale change without viewpoint motion | Compare foreground/background parallax; use a practical move, 3D, or a new shot if needed. |
| Locked-off shot drifts | The tool introduces motion or the prompt is ambiguous | Reduce subject/environment motion; compare frame edges; stabilize only if the result remains acceptable. |
| Person changes identity or clothing | Reference continuity is weak or too many variables changed | Lock authorized references; reduce simultaneous changes; compare successive frames. |
| Left/right positions reverse | Blocking and screen direction were not specified or checked | Use a top-down blocking map; verify eyelines and entry/exit direction. |
| Close-up loses necessary context | No establishing or contextual insert | Add a wide/OTS/insert if the viewer needs spatial information. |
| Focus effect hides the clue | Visual style conflicts with information priority | Shift focus, deepen focus, or separate the information into another shot. |
| Generated optical effect is physically wrong | A generative image is not a validated experiment | Record live footage or use a sourced scientific diagram; label any illustration as a demonstration. |
| 9:16 crop cuts off hands or props | The shot was designed only for a wide frame | Reframe for each delivery ratio and inspect current platform interface areas. |

Compare source and candidate frames using identity, clothes, prop position, window direction, eyeline, lighting direction, framing, and continuity. Separate observable mismatch from uncertainty; appearance alone cannot establish physical accuracy. Retain failed takes and note why they were rejected.

<a id="CH02-S11"></a>
## Exercises, assessment, and further research
**Exercise A — Three scales, one action.** Record or storyboard a teacher lifting a transparent glass as an extreme-wide, medium, and close-up shot. Note what each version lets the viewer notice and what it withholds.

**Exercise B — Dolly versus zoom.** Use distinct foreground, middle-ground, and background objects. Compare a dolly-in with a zoom-in. Inspect relative displacement and write down any result that differs from the specification.

**Exercise C — A 30–60 second short film.** Use 5–8 shots, including a wide, a medium, a close-up, two angles, one locked-off shot, and one motivated camera move. Submit a shot list, two prompt versions if AI is authorized, the final film or boards, provenance records, and a one-page reflection.

| Assessment area | Points | Evidence of achievement |
|---|---:|---|
| Narrative purpose of scale and composition | 25 | Shot choices have a clear, observable reason. |
| Angle and camera-movement distinctions | 20 | The plan distinguishes rotations, translations, optical changes, and focus shifts. |
| Spatial and action continuity | 20 | Positions, eyelines, props, and movement remain understandable. |
| AI specification and version record | 20 | Inputs, prompts, model/version, takes, and revisions are traceable; unsupported values are marked unknown. |
| Quality review and reflection | 15 | The learner identifies defects and explains evidence-based corrections and model limits. |

The grade bands in the source draft (90–100, 80–89, etc.) are author-proposed teaching guidance, not an official standard; calibrate them with instructors before use.

Further research: How do shot-size conventions change across genres and production contexts? How can a camera cross an action axis without confusing viewers? What evidence distinguishes perspective change from digital zoom in a generated clip? How should reframing preserve information across delivery ratios?

<a id="CH02-S12"></a>
## References
- [R001] David Bordwell, Kristin Thompson, and Jeff Smith, *Film Art: An Introduction*, 13th ed. (McGraw Hill, 2026). Publisher identifies the edition; chapter-specific page locators have not been checked.
- [R009] Bruce Block, *The Visual Story: Creating the Visual Structure of Film, TV, and Digital Media*. Edition and relevant page locators need confirmation.
- [R010] Joseph V. Mascelli, *The Five C’s of Cinematography: Motion Picture Filming Techniques*. Relevant edition and page locators need confirmation.
- [R011] Blain Brown, *Cinematography: Theory and Practice: Image Making for Cinematographers and Directors*. Edition and page locators need confirmation.
- [R012] Columbia University Center for New Media Teaching and Learning, “Camera Movement,” *Columbia Film Language Glossary*. Educational glossary; access date 2026-10-18. Its historical overview should be checked against specialist film histories.
- [R025] Columbia University Center for New Media Teaching and Learning, “180-Degree Rule,” *Columbia Film Language Glossary*. Access date 2026-10-18.
- [R026] American Society of Cinematographers, “Shot Craft: Tools for Camera Movement,” *American Cinematographer*. Access date 2026-10-18; published 2024-04-05; professional practice account.
- [R027] ZEISS, “Zoom or Prime Lens? A Shootout Comparison,” ZEISS Lens Blog. Access date 2026-10-18; manufacturer technical education.
- [R028] Canon Europe, “Depth of Field,” Canon RF Lens World. Access date 2026-10-18; manufacturer technical education.
- [R002], [R003], [R006], [R029] Runway Academy / Help Center prompt guides. Access date 2026-10-18; official, product-specific, time-sensitive guidance, not independent film theory or a guarantee of exact camera physics.

### Editorial and production TODOs

- Confirm the chapter title against the book table of contents; no TOC was changed in this draft.
- Verify editions and chapter/page locators for the cinematography textbooks; none are invented here.
- Confirm lawful viewing editions, exact film sequence, timecode, and shot observations for any film analysis.
- Review all 26 bilingual terms and this English translation with a professional editor.
- Check the five original editable SVGs for visual clarity, localization, scaling, color contrast, and technical accuracy before giving them stable canonical IDs.
- Test prompts only with an authorized model; record actual model version, settings, date, input hashes, and outcomes. Prompts currently remain `not-run`.
- Validate the glass/refraction lesson with a reproducible live experiment or authoritative science source before presenting factual science.
- Run the final chapter website, PDF, DOCX, EPUB, font embedding, EPUBCheck, and full-page visual proof only after editorially reviewed content is integrated; current V2 canonical files remain unchanged.

