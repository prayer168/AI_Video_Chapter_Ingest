---
chapter_id: CH06
part_id: P02
locale: en-US
slug: chapter-06
title: "Story, Plot, and Causal Structure"
translation_status: review-needed
revision: 2.1.0-draft
source_chapter: null
source_ids: [R046, R047, R048, R049, R050]
last_updated: 2026-10-21
---

# Story, Plot, and Causal Structure

> Editorial status: research draft; this English text is a working translation. Theoretical page locators, film-viewing notes, and bilingual copyediting remain open. The workflows, prompts, and exercises below are practical demonstrations, not findings of empirical research.

## Learning objectives {#CH06-S01}

By the end of this chapter, readers should be able to distinguish story material from plot arrangement; analyze a sequence through causality, character goals, information disclosure, and audience inference; write scenes as filmable actions and consequences; compare linear, flashback, multiple-perspective, and elliptical structures; and use traceable structured data to support AI collaboration without treating model output as a verified screenplay. Prerequisites: the film language in CH01, shot and viewing position in CH02–CH03, and genre and representation ethics in CH05.

## Prerequisites {#CH06-S02}

This chapter does not require readers to adopt a three-act structure or any single commercial formula. Readers should understand a basic scene as action by people under constraints in a particular time and place, with image, sound, and editing controlling when viewers receive information. When analyzing an existing film, use a lawfully obtained edition and record its release/version, subtitle or dub version, and reproducible timecodes. This chapter does not claim unverified shot-level timecodes.

## Key terms {#CH06-S03}

| ID | Traditional Chinese | English | Operational definition in this chapter |
|---|---|---|---|
| TERM-CH06-STORY | 故事 | story | The overall temporal relations among events, characters, and world conditions that viewers infer from a work's cues; an operational working definition here. |
| TERM-CH06-PLOT | 情節 | plot | The events a work selects, orders, delays, or presents more than once. |
| TERM-CH06-CAUSALITY | 因果關係 | causality | A relation that changes later possibilities through an earlier action or condition and can be explained with textual evidence; temporal succession alone is not causation. |
| TERM-CH06-MOTIVATION | 動機 | motivation | A goal, belief, need, or pressure that helps explain a character's choice of action. |
| TERM-CH06-INCITING-INCIDENT | 觸發事件 | inciting incident | An event that prompts a principal character to act anew or makes the prior balance difficult to sustain; a practical term here, not a universal theoretical definition. |
| TERM-CH06-REVERSAL | 情勢逆轉 | reversal / peripeteia | A turn in circumstances produced by action; Aristotle discusses reversal in tragic plot, not as a required formula for all films. |
| TERM-CH06-RECOGNITION | 認知／發現 | recognition / anagnorisis | A changed understanding of a consequential identity, relation, or fact by a character or audience; a component of complex plot in the *Poetics*. |
| TERM-CH06-FORESHADOWING | 預示 | foreshadowing | An earlier cue that makes a later event more intelligible in retrospect; over-signaling may reduce discovery. |

These bilingual entries are working chapter definitions pending terminology review. Aristotle's discussion of plot, complete action, reversal, and recognition comes from a theory of tragedy; this chapter turns those concepts into analytical questions rather than claiming that every genre must use them [R046].

## History and principles {#CH06-S04}

In the *Poetics*, Aristotle describes tragic plot (*mythos*) as the arrangement of incidents and discusses complete action, beginning/middle/end, probability or necessity, reversal, and recognition. This is historical material on ancient Greek tragedy, not a universal rule for modern screenplays; translated terms also vary by edition [R046]. Film-narrative study analyzes event order and the way viewers receive information together with image and sound. Bordwell's study of narration in fiction film addresses principles of narrative representation and different storytelling patterns; the publisher's page confirms the book's scope and bibliography, but page-specific claims still need checking against the adopted edition [R047].

This chapter uses four practical questions: What does a character want to do? Why do they act? What changes because of the action? What does the audience know, misunderstand, or not yet know? A chain written only as “and then” may become a chronology list. Rephrasing links as “because / but / therefore” can diagnose causality, but it is an editorial test, not a guarantee of dramatic effect. Coincidence, silence, stasis, nonlinear form, and open endings can be purposeful; the question is whether the work creates a perceptible pattern and expectation.

## Traditional production practice {#CH06-S05}

Writers often develop material through characters, circumstances, wants, obstacles, and choices, then revise it through outlines, beat sheets, scene lists, and screenplay drafts. Producers, directors, performers, and editors assess shootability, character action, scene turns, information disclosure, and connections between scenes. This does not mean every scene must “advance the main plot”: a scene may establish relationships, atmosphere, theme, or audience expectation, provided the writer understands how it affects the overall experience.

For each causal node, record the premise, actor, goal, choice, obstacle, outcome, downstream cost, and information available to the audience. If deleting an event leaves everything that follows unchanged, decide whether it is a deliberate pause for rhythm/theme or redundant material that can be combined. For flashbacks and multiple perspectives, track story time separately from presentation order, then note what each retelling adds, omits, or changes. A character's account should not automatically be treated as objective truth.

## AI-era workflow and limits {#CH06-S06}

A language model can propose alternative causal links, flag unsupported motivation, organize scene data, and draft alternate orderings. These are testable workflow hypotheses, not evidence that a model can judge psychological realism, cultural context, or artistic value. A model may turn coincidence into foreshadowing, add facts absent from the source, confuse characters or versions, or produce locally plausible but globally contradictory events. For each run, preserve the prompt, model/version when available, date, input revision hash, accepted and rejected suggestions, and human edits.

Use the rule “the human owns the story bible; the model proposes only within explicit boundaries.” Supply fixed facts, world rules, and prohibited additions. Require every suggestion to cite source evidence or label itself as inference; the author decides whether to adopt it. Do not submit confidential or unlicensed scripts or personal performer data to an external service. Data retention, training use, and commercial rights must be checked against the tool's current official terms and project contracts; a subscription does not establish those terms.

## Step-by-step workflow {#CH06-S07}

1. **Write the core action in one sentence:** what observable goal does the protagonist pursue under what constraints?
2. **List story facts:** distinguish approved facts, character beliefs, audience knowledge, and unresolved author decisions.
3. **Build causal nodes:** for each node record trigger, action, obstacle, outcome, and the next question it creates.
4. **Test character agency:** does the character choose, and if not, is passivity intentional?
5. **Design information order:** decide what is shown, delayed, repeated, or retold; mark what each presentation adds.
6. **Set scene objectives:** record entry state, character goal, tactic, change, exit state, and filmable action.
7. **Test causality and coincidence:** summarize links with “because / therefore / but”; identify events that are merely adjacent in time. If coincidence remains, document its thematic or formal purpose.
8. **Use AI for bounded diagnosis:** ask for issues and evidence locations, not an automatic rewrite of the whole work.
9. **Make author decisions and record versions:** accept or reject each suggestion, then update the story bible and change log.
10. **Validate through table read and editorial reordering:** check whether goals are legible, information is fair, and turns are traceable; reorder scene cards to test pacing.

## Prompt and technical parameters {#CH06-S08}

The following model-neutral prompt is an instructional template, not tested against a specific model. Remove confidential and unlicensed material; test on an invented short film first. JSON output supports diffing. The `evidence` field must point to a supplied `scene_id` or explicitly say `inference`.

```text
Role: You are a screenplay-structure diagnostic assistant, not a co-author or source of story facts.
Task: Diagnose only the supplied scene chain. Do not add characters, world rules, props, or events.
Fixed facts: {story_facts}
Scene data: {scenes}
Check: causal links, evidence for motivation, choices and costs, information order, continuity conflicts.
For each finding return: scene_id, issue type, source evidence (brief excerpt or field), impact, up to two revision options, and an inference flag.
If evidence is absent, return “cannot determine”; do not fill gaps.
Output: valid plain JSON matching the schema below; do not write screenplay prose.
```

```json
{
  "schema_version": "1.0",
  "chapter_id": "CH06",
  "findings": [
    {
      "scene_id": "S03",
      "issue_type": "causal_gap",
      "evidence": "Source field or excerpt; use inference if speculative",
      "impact": "Possible effect on audience comprehension or character choice",
      "options": ["Revision option A", "Revision option B"],
      "inference": true
    }
  ]
}
```

Save inputs and outputs in UTF-8 with schema version, source revision, model/tool/version, and run date. Validate JSON with a parser and schema. If a tool version is unavailable, record “not recorded” rather than guessing. No token, temperature, or vendor setting is prescribed because semantics, availability, and controls vary by tool.

## Film case and viewing exercise {#CH06-S09}

*Rashomon* (1950) is a case for repeated narration and perspective differences. The Criterion film page provides production/year information and a summary in which several characters give differing accounts of an event; Stephen Prince's essay further interprets its flashbacks and multiple narrations. These are catalogue and critical sources, not evidence that this book's author has completed a viewing [R048, R049]. The case raises analytical questions; it should not be reduced to “everyone lies” or to a claim that there must be one solvable answer.

Viewing task: choose a lawfully accessible edition and create an event table before viewing. For each retelling, log the teller, available visual/auditory evidence, agreements and differences from prior versions, and what the audience knows at that point. Record release/version, runtime, subtitle version, and timecodes; do not mix timecodes across edits. Select one difference and determine whether it changes the event, a character's self-image, audience trust, or the source of information. Add shot-level details only after the author has watched and logged the film; no shot timecode is asserted here.

Original practice exercise: three characters describe the same missing key. Each account may differ only through knowledge, interest, or observation position; fixed events cannot change without cause. Compare how information differences reshape audience inference. Do not copy *Rashomon* characters, plot, or visual design.

## Common errors and quality checks {#CH06-S10}

- **Confusing sequence with cause:** restate links as “because / therefore”; if only “then” works, add an intermediate action or acknowledge coincidence.
- **Vague character goals:** write observable actions instead of abstractions such as “wants happiness / to be understood.”
- **Surprise through authorial concealment:** check whether earlier scenes fairly establish cues; if narration is unreliable, the audience still needs to understand the source of unreliability.
- **Repeated flashbacks add nothing:** require each retelling to add identifiable information or alter the interpretation of prior material.
- **Treating a structure formula as law:** consider genre, duration, cultural form, and authorial intention; three-act models and beat sheets are tools, not guarantees.
- **AI invents facts:** compare every suggestion against the story bible; ungrounded content remains a proposal until the author approves it.
- **Attributing a paraphrase as an author's exact claim:** check the adopted edition, translation, and locator; separate analysis from sourced fact.

Quality checklist: each core event has an ID; principal actor, goal, obstacle, and outcome are identifiable; causes, coincidences, and unknowns are tagged; story time and presentation order are separate; retelling differences are logged; every AI suggestion has evidence/inference status and a human decision; reordering does not break fixed facts; each cited source exists and has a non-invented locator. Automated checks can validate IDs, required fields, JSON, bilingual alignment, and link formatting. Character credibility, emotional force, and artistic effect require human assessment.

## Exercises, assessment, and further research {#CH06-S11}

**Exercise A (causal map):** Write an original 6–10-node short-film event chain. Mark each node's premise, character choice, outcome, and next step. Separately write the order in which the plot presents information; do not conflate the two lists.

**Exercise B (retelling design):** Design two accounts of the same event. State what each teller knows, withholds, or may misremember. Ask peers to infer the difference from film evidence without an author explanation.

**Exercise C (AI diagnosis):** Run the chapter template on an anonymized scene list and manually verify that every finding has source evidence. Score 0–4 for traceable causality, specific character choices, legible information differences, and traceable AI suggestions. This is a classroom tool, not a validated empirical instrument.

Further research: variation in causal expectations and closure across narrative traditions; viewer inference about unreliable narration; cross-scene consistency in generative models and human editing strategies for it. Research reports should record corpus, model version, test conditions, and ethics/licensing arrangements.

## References {#CH06-S12}

- **R046 | Primary theoretical text (English translation):** Aristotle. *Poetics*. Trans. S. H. Butcher, Internet Classics Archive, MIT. Chapters 6–11 address plot, complete action, probability/necessity, reversal, and recognition; this web text does not provide the print pagination adopted by this project. A theory of tragedy, not a universal law across media. <https://classics.mit.edu/Aristotle/poetics.1.1.html> (accessed 2026-10-21).
- **R047 | Film-narrative monograph:** Bordwell, David. *Narration in the Fiction Film*. University of Wisconsin Press, 1985. Publisher page confirms bibliographic data and scope; full text was not consulted in this run, so specific arguments and page locators must be checked against the adopted edition. <https://uwpress.wisc.edu/Books/N/Narration-in-the-Fiction-Film> (accessed 2026-10-21).
- **R048 | Film catalogue:** The Criterion Collection, “Rashomon” (1950). Used for film identification, production data, and the catalogue synopsis of multiple perspectives; not a substitute for the author's viewing or shot locator. <https://www.criterion.com/films/307-rashomon> (accessed 2026-10-21).
- **R049 | Film criticism:** Stephen Prince, “The Rashomon Effect,” The Criterion Collection. Used to attribute a named critic's interpretation of multiple narration, not as the author's independent viewing conclusion. <https://www.criterion.com/current/posts/195-the-rashomon-effect> (accessed 2026-10-21).
- **R050 | Cross-check film catalogue:** AFI Silver Theatre and Cultural Center, “RASHOMON.” The catalogue describes multiple perspectives, director/screenwriters, source stories, and restoration information; version and programming details are time-sensitive and should be rechecked before publication. <https://silver.afi.com/movies/detail/0100001442/> (accessed 2026-10-21).
