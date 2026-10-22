---
chapter_id: CH10
part_id: P02
number: 10
title: "Screenplay Format, Adaptation, and Revision Management"
status: draft
translation_status: review-needed
source_revision: 2.1.0-draft
last_researched: 2026-10-22
last_updated: 2026-10-22
claim_types: [verified-fact, theory, practice, ai-hypothesis, demo]
---

<a id="CH10-S00"></a>
# Screenplay Format, Adaptation, and Revision Management
> Editorial state: English working translation of a Traditional Chinese research draft. The title follows the registry topic and needs approval. Sources support only their stated scope; book locators, full-text interpretation, viewing editions, and timecodes remain unchecked. Original SVGs are drafts pending rights and publication review.

<a id="CH10-S01"></a>
## Learning Objectives and Audience
Readers will be able to:

1. Explain how screenplay format supports reading, rehearsal, budgeting, and departmental handoffs, while recognizing variation by market and production stage.
2. Separate adaptation material, granted rights, creative transformation, and legal questions; a completed screenplay does not establish adaptation rights.[R072]
3. Maintain revision records with dates, authors, status, change summaries, and affected scenes.
4. Compare drafts by stable scene IDs and route formatting, continuity, and creative decisions to appropriate review.
5. Assess whether a text-markup format such as Fountain can serve a project's interchange needs, testing a sample first.[R075]

This chapter is for screenwriters, directors, producers, script coordinators, and AI practitioners who hand scripts across departments. Prerequisites are basic scene headings, action, character cues, and dialogue. No software or single industry convention is assumed.

<a id="CH10-S02"></a>
## Prerequisites
Readers should be familiar with scenes, action, character cues, dialogue, and basic screenplay reading. Adaptation rights are not a prerequisite for studying format; when existing works are involved, record rights status separately from the start.

<a id="CH10-S03"></a>
## Core Concepts and Professional Terms
| Term ID | 繁體中文 | English | Working definition |
|---|---|---|---|
| TERM-CH10-SCREENPLAY | 電影劇本 | screenplay | A text for creative work, reading, and production communication; format serves the task and does not require literal reproduction on screen.[R070] |
| TERM-CH10-SCENE-HEADING | 場景標題 | scene heading | A scene-opening line identifying information such as interior/exterior, location, and time; fields depend on the adopted specification or team convention. |
| TERM-CH10-SLUGLINE | 場景行／slugline | slugline | A common industry term for a screenplay scene heading; usage varies by region and format. |
| TERM-CH10-ADAPTATION | 改編 | adaptation | The creative process of reorganizing existing material into another work form; creative method and rights status are distinct.[R072] |
| TERM-CH10-DERIVATIVE-WORK | 衍生作品 | derivative work | A work adapting, transforming, or recasting a preexisting work as defined in U.S. copyright law; this is not advice for other jurisdictions.[R072] |
| TERM-CH10-REVISION-SET | 修訂稿次 | revision set | A production practice identifying a revision and its changes; the team defines colors and marks.[R073] |
| TERM-CH10-LOCKED-PAGES | 鎖定頁 | locked pages | A production version-management method for preserving page references; timing and procedure depend on workflow.[R074] |
| TERM-CH10-SCREENPLAY-INTERCHANGE | 劇本交換格式 | screenplay interchange format | A format or convention for transferring screenplay text and structure between tools; verify elements, pagination, and notes after conversion.[R075] |

These are draft working definitions awaiting bilingual terminology review. The Academy Nicholl resource notes variation among professional writers; its guide is a reference, not a global mandate.[R070]

<a id="CH10-S04"></a>
## History and Principles
A screenplay page is both narrative text and a collaboration interface. Scene headings help a crew locate interiors/exteriors, places, and times; action, character cues, and dialogue support reading, rehearsal, and production estimates. Format can reduce handoff friction but cannot replace discussion among directors, actors, design, camera, producing, and editorial teams. The Academy Nicholl resource collects common U.S. practices and acknowledges variation. Follow the commissioning party, contest, or production requirements first; use familiar conventions as a default only when requirements are absent.[R070]

A writing draft and a production draft have different jobs. Plain-text markup can support diffs and preservation; dedicated software may offer pagination, revision colors, locked pages, and departmental delivery. Fountain represents scene headings, characters, dialogue, transitions, and notes with readable markers. Its specification documents syntax, but this does not ensure every application supports every feature or produces identical pages.[R075]

Creative adaptation decides what to retain, reorganize, remove, or re-express. Rights review asks who may authorize which uses, territories, periods, media, languages, and scopes. U.S. copyright law lists translation, dramatization, and motion-picture versions among examples of derivative works; rights in a derivative do not automatically cover source material used unlawfully.[R072] This summarizes U.S. statutory text, not global law or legal advice.

<a id="CH10-S05"></a>
## Traditional Production Practice
1. **Confirm delivery requirements:** record medium, language, page or software format, filenames, revision naming, recipient, and deadline. Follow stated requirements.
2. **Prepare a readable writing draft:** use scene headings, action, character cues, and dialogue. Include information that supports story, performance, or production decisions; avoid turning every camera idea or undecided detail into a command.
3. **Prepare production information:** maintain character/location lists, shooting needs, revision summaries, and open questions separately as needed. If scene numbers are required, assign an owner and numbering milestone.
4. **Manage revisions:** Final Draft documentation describes Revision Mode additions/deletions, revision colors, and revision sets. The production defines its actual conventions.[R073]
5. **Lock pages at the right stage:** Final Draft advises against locking pages too early and discusses locking in a preproduction/production workflow.[R074] Locked pages can still change through a controlled process.
6. **Deliver and archive:** retain a readable draft, change summary, revision ID, delivery date, source file, and SHA-256 to identify the version actually used.

### Adaptation source register

Record source title and edition, author/rightsholder, acquisition source, license-document location, territory/term/media/language, promotional uses, credit terms, and restrictions. Mark unknowns pending. A separate transformation map records material retained, combined, removed, reordered, or added; it is an editorial tool, not a legal decision.

<a id="CH10-S06"></a>
## AI-Era Technical Changes and Limits
With team authorization and confirmed data rights, scripts or models may assist with extracting scene headings, characters, repeated terms, draft differences, missing fields, and questions. These are workflow experiments, not guarantees about current tools. Do not submit unlicensed source material, confidential scripts, or personal data to an unapproved service; check current terms, retention policies, and security rules.

- **Programmatic checks:** required fields, stable scene IDs, revision labels, reference existence, author/date records, and readable exports.
- **Model-assisted candidates:** within authorized text, produce a diff summary or questions linked to source lines/scene IDs; never write them into the master automatically.
- **Human decisions:** adaptation rights, representation, story choices, performance intent, page locking, and formal delivery belong to authors, producers, or legal professionals.

A model may misclassify uppercase action as a character cue, mistake abbreviations for scene headings, or miss manual revision marks. A diff is a review clue; textual similarity does not prove copying, authorization, or author intent.

<a id="CH10-S07"></a>
## Step-by-Step Workflow
| Step | Owner and operation | Deliverable and check |
|---|---|---|
| 1. Intake | Script coordinator records submitter, date, language, source hash, and access limits. | Read-only source, source ID, rights status. |
| 2. Confirm format | Writer/producer confirms delivery requirements, template, revision rules, and tools. | Format decision; clarify ambiguity with recipient. |
| 3. Establish master | Author writes in selected tool and assigns stable scene IDs or a crosswalk. | Editable master, revision ID, date. |
| 4. Register adaptation basis | Producer/rights contact checks source and written license; author maps transformations. | Rights-file location and open issues; completion is not authorization. |
| 5. Check draft | Assistant/software checks format, character names, duplicate scenes, citations, and package. | Reproducible report; confirm suspected issues manually. |
| 6. Record revisions | Author names revision set; production assignee manages colors, pages, and locks. | Change summary, diff, pagination, affected departments. |
| 7. Exchange formats | Test a representative sample among Fountain, FDX, PDF, or others; inspect elements, dialogue, notes, characters, and pagination. | Conversion checklist and compatibility matrix. |
| 8. Deliver/archive | Producer specifies package and retains source, PDF, revision ID, and receipt. | Recoverable package, hashes, access controls. |

Suggested JSON revision fields: `project_id`, `document_id`, `revision_id`, `parent_revision`, `author`, `created_at`, `change_summary`, `changed_scene_ids`, `rights_basis`, `approval_state`, and `source_hash`. This is a demonstration, not an interchange standard.

<a id="CH10-S08"></a>
## Prompt and Technical Parameters
This model-neutral example is illustrative, not a service test. It specifies no provider or unverified parameters. Use only authorized text and the minimum needed.

```text
Role: screenplay revision organization assistant; do not rewrite or approve.
Input: two authorized drafts, revision IDs, stable scene-ID crosswalk.
Task: list additions, removals, moves, and text changes with scene IDs and source lines.
Constraints: add no story; infer no intent; decide no copying or rights status;
report unmatched items as unknown; keep source drafts read-only.
JSON: {"from_revision":"...","to_revision":"...","changes":[{"scene_id":"...","kind":"added|removed|moved|text-change|format-change","source_lines":["..."],"summary":"...","human_review":"required"}],"unmatched_items":[],"limitations":[]}
```

Test 3–5 representative scenes and compare each result manually. Record tool, version, date, input scope, and errors. For software diffs record encoding, newline, normalization, and diff-tool version.

<a id="CH10-S09"></a>
## Film Case Study
### *The Wizard of Oz* (1939)

The AFI Catalog connects the 1939 film to L. Frank Baum's 1900 novel *The Wonderful Wizard of Oz* and records clues about multiple screenwriters and production changes.[R076] This creates research questions: which motivations changed, which passages were reorganized, and which expressions were redesigned for cinema? This section uses catalog-level bibliographic and production-history evidence only. It does not claim project viewing, a single author's intent, or access to the complete screenplay.

**Exercise:** Using lawfully available editions of the novel and film, select a short passage and record source event, film counterpart, medium-specific change, retained/removed material, and an effect hypothesis. Cite page or timecode. Check rights separately; availability of a source edition does not establish film adaptation permission.

For any adaptation, compare source events, screenplay structure, audiovisual expression, and rights context separately. Shot/performance analysis requires a selected edition and viewing log. Legal conclusions require qualified review in the applicable jurisdiction. Catalog or AI summaries do not substitute for the source text or film.

<figure id="CH10-FIG-001"><img src="/images/chapters/CH10/CH10-FIG-001-revision-lifecycle.svg" alt="Four version nodes connect a writing draft, revision drafts, production draft, and archived delivery." /><figcaption>Figure 10-1.</figcaption></figure> Versions should trace source, author, changes, and delivery status; this is a working model. This is an original editable SVG illustration for this book, not a film still. Attribution, rights, and publication approval are pending.

<figure id="CH10-FIG-002"><img src="/images/chapters/CH10/CH10-FIG-002-adaptation-map.svg" alt="A diagram separates source material, rights review, creative choices, and a new screenplay, with a legal-review gate." /><figcaption>Figure 10-2.</figcaption></figure> Creative transformation and rights review need separate records; the diagram is not legal advice. This is an original editable SVG illustration for this book and depicts no specific work. Rights and publication approval are pending.

<figure id="CH10-FIG-003"><img src="/images/chapters/CH10/CH10-FIG-003-change-review.svg" alt="A diagram compares earlier and revised drafts for one scene ID, summarizes differences, and routes them to human review." /><figcaption>Figure 10-3.</figcaption></figure> Diff tools provide review cues; authors decide whether to accept changes and which departments they affect. This is an original editable SVG illustration for this book, not a production screenplay page. Rights and publication approval are pending.

<a id="CH10-S10"></a>
## Common Errors and Quality Checks
| Error | Risk | Check |
|---|---|---|
| Treating one format as global | Fails recipient requirements | Confirm requirements and log the format decision.[R070] |
| Locking pages or renumbering too early | Department references drift | Set a milestone and compare revisions.[R074] |
| Treating revision colors as universal | Team misreads revision | Define colors and revision IDs in delivery notes.[R073] |
| Treating an adaptation map as permission | Rights/distribution risk | Legal review of rightsholder, scope, and documents.[R072] |
| Checking only word count after conversion | Elements or pagination may be lost | Compare representative scenes, bilingual characters, marks, and pages.[R075] |
| Writing AI summaries into the master | Unapproved changes become canonical | Isolate analysis; designated author edits and logs the master. |

**Automatable:** metadata, bilingual S01–S12 alignment, term/reference IDs, local image paths/hashes/SVG XML, captions/alt, site routes, and draft format structure. **Human judgment:** recipient compliance, adaptation merits, case analysis, representation, chain of title, page proofing, English fluency, and author approval. Automation must not report human items as PASS.

<a id="CH10-S11"></a>
## Exercises, Assessment, and Further Research
1. **Format analysis:** mark elements on one lawfully available screenplay page; record source and format rule without reproducing extensive text.
2. **Adaptation map:** use lawful source text and viewing access, complete a transformation table, and cite edition/page/timecode. Leave unknown differences unresolved.
3. **Revision diff:** assign stable scene IDs to two original short drafts and classify additions, removals, moves, formatting edits, and story changes.
4. **Interchange test:** create a sample with interior/exterior headings, Chinese names, bilingual dialogue, parentheticals, scene numbers, and notes. Test two verified tools and record losses.
5. **Rights exercise:** use fictional source material to complete the source/license checklist; leave unknowns pending. This is not legal advice.

Score each item 0–2: traceable delivery/version; separation of creative transformation and rights; diffs mapped to scene IDs; tested conversion losses; clear human/tool responsibilities and open tasks. 0 = no evidence, 1 = partly traceable, 2 = complete steps, sources, and limits. This assesses process records, not artistic quality.

Further research: compare delivery conventions across countries/media; inspect current tool import/export documentation and versions; conduct a scene comparison with lawfully obtained source and film; study the effect of revision systems on handoffs and creative decisions.

<a id="CH10-S12"></a>
## References
- [R070] Academy of Motion Picture Arts and Sciences, “Nicholl Screenwriting Resources,” https://www.oscars.org/nicholl/screenwriting-resources. Formatting guidance and variation, used within page scope.
- [R071] Writers Guild of America West, “WGAW Registry,” https://www.wgawregistry.org/. Official registry information; not legal advice.
- [R072] U.S. Copyright Office, *Copyright Law of the United States (Title 17)*, Chapter 1, §§101–103, https://www.copyright.gov/title17/92chap1.html. U.S. law; do not generalize to other jurisdictions.
- [R073] Final Draft Knowledge Base, “How do I use Revision Mode?”, https://kb.finaldraft.com/hc/en-us/articles/27813588722708-How-do-I-use-Revision-Mode. Vendor documentation; verify against installed version.
- [R074] Final Draft Knowledge Base, “How do I lock or unlock script pages and use the locking tools?”, https://kb.finaldraft.com/hc/en-us/articles/27817054455828-How-do-I-lock-or-unlock-script-pages-and-use-the-locking-tools. Vendor workflow; not universal practice.
- [R075] Fountain, “Syntax,” https://fountain.io/syntax/. Format syntax; application support and conversion require testing.
- [R076] American Film Institute, AFI Catalog, *The Wizard of Oz* (1939), https://catalog.afi.com/Film/7892-THE-WIZARDOFOZ. Catalog/production-history clues; not viewing or rights clearance.

Web sources accessed 2026-10-22. Book locators, film edition/timecodes, and tool interoperability require human verification.
