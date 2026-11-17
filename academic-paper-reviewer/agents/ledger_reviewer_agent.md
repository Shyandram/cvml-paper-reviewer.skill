# Ledger Reviewer (full mode, the default since 3.0)

One agent does the whole review in one context, in five steps:

1. **Ledger.** Read the paper and list every reason to accept and every reason to reject it.
2. **Reorganize and probe.** Group the reasons by claim, rank them by how much they could move the decision, and examine the uncertain ones in detail until each is settled or marked unsettled.
3. **Roster.** From the paper's aspects, list every type of reviewer a venue would plausibly assign. Each type has one primary aspect.
4. **Reviews.** Review as each type. Each review scores the paper and argues from the ledger items, by ID.
5. **Average.** The decision is the mean of the types' ratings, weighted by the venue's **aspect ratio**: how much each aspect counts at that venue.

There are no separate reviewer agents, no Editor-in-Chief and no override. The only weighting is the aspect ratio. Delegate only to get information this context cannot reach, such as a literature search the host can run only in a subagent. Never delegate to obtain a reviewer's judgment.

Hard Rules 1–4 and 6–10 of `SKILL.md` apply. Hard Rule 5, the Devil's Advocate cap, has no counterpart: a fatal reason lowers the rating of every type that judges it fatal, and the average carries it. Read `references/quality_rubrics.md`, `references/review_criteria_framework.md`, `references/error_audit.md` and `references/venue_profiles.md` before Step 1. For a CV or ML paper, also read `references/cv_review_checklist.md`. Read `references/statistical_reporting_standards.md` when the paper reports quantitative comparisons.

---

## Step 0: Setup

- Run `scripts/integrity_scan.py --paper <paper> --redact <reviewer_copy>`. Review the redacted copy. Report any findings under *Integrity signals* at the end; they never change a score (Hard Rule 9).
- Identify the paper type, field, sub-area and target venue. If the venue is not stated, infer it as in `SKILL.md`, *Input Handling*.
- Get the venue's **aspect ratio**: `python3 scripts/aggregate_scores.py ratio --paper-type <type> --venue <key>`. It prints each aspect's share of the decision at this venue for this paper type: the paper-type weights from `references/quality_rubrics.md` times the venue's emphasis in `scripts/venues.json`, renormalized. For example, an empirical paper at ICLR puts about 23% on technical rigor and 16% on novelty, while at TMLR it puts about 29% on technical rigor and 6% on novelty. For a venue without a profile, use the closest profile (`references/venue_profiles.md`) and say so. Record the ratio in the header; it fixes how much each aspect counts before any review is written.
- Write the **paper memory** (`references/error_audit.md`, Section 3). It has four parts:
  - the claims C1, C2, … with their locations;
  - the setup facts, each with its location or marked "not stated";
  - the headline numbers with their source tables;
  - what could not be read.

## Step 1: The ledger

Read the whole paper, appendix included. Then list the reasons. A reason is an argument a competent reviewer could make for acceptance or rejection. It is not yet a verdict, so it carries no score.

**Accept reasons `A1, A2, …`.** Write one row per reason, with these columns:

| Column | Content |
|---|---|
| ID | A1, A2, … |
| Aspect | novelty, soundness, empirical strength, significance, clarity, reproducibility, resource (data, code, benchmark), or theory |
| Reason | the argument, stated at its strongest |
| Evidence | location plus a number or a short quote |
| Strength | strong / moderate / weak, as the evidence stands |
| Depends on | what must be true for the reason to hold, e.g. "baselines tuned equally" or "R3 not upheld" |

**Reject reasons `R1, R2, …`.** Write one row per reason, with these columns:

| Column | Content |
|---|---|
| ID | R1, R2, … |
| Aspect | as for accept reasons |
| Reason | what is wrong or missing, and why it matters |
| Evidence | location plus a quote |
| Kind | **error**: verified by a concrete check (Hard Rule 10; the check goes in Evidence). **gap**: a missing experiment, baseline, analysis or definition. **judgment**: novelty, significance or scope, with its basis named (for novelty, the prior work). **question**: a suspicion that cannot be checked from the paper. |
| Worst case | the most severe grade the reason could earn: fatal / major / minor |
| Fix | the concrete change and its rough cost |

Rules for the ledger:

- **Be exhaustive on both sides.** Walk every aspect in `references/review_criteria_framework.md` for this paper type, the omission sweep in `references/error_audit.md`, and, for CV/ML papers, the task checklist. Below the two tables, write one line per aspect: the IDs it produced, or "considered, no reason". A typical paper yields 8–20 accept reasons and 10–30 reject reasons. Do not pad the list with near-duplicates, and do not drop a reason because it seems minor.
- **State each reason at its strongest.** Write the accept reasons as the paper's best advocate would, and the reject reasons as its most careful critic would. Neither side may be a straw man.
- **Check each reject reason against the paper before listing it.**
  - It must be specific: a location, what is wrong, and why it matters.
  - It must not already be answered in the paper, appendix included. If it is fully answered, list it under **Answered**, with the location of the answer, instead of as a reject reason.
  - It must be consistent with the text.
  - It must criticize the work, never the authors.
- **Pair the reasons.** When an accept reason and a reject reason bear on the same claim, cross-reference them, e.g. "A2 ↔ R4". Most decisions turn on these pairs.
- **Literature.** With network access and the literature check on, run `references/literature_search.md` here, inline: the fingerprint, the claim and benchmark queries, the similarity check and the novelty profile. Its findings become accept reasons (a verified delta over the closest prior work) or reject reasons (`judgment`, naming the work). Without network access, skip it, say so, and mark novelty reasons that rest on memory with `[verify]`.

## Step 2: Reorganize, then probe

The first ledger comes from one reading. Before any reviewer type judges it, reorganize it and examine the reasons the decision could turn on.

**Reorganize.**

- **Merge duplicates.** Keep the lowest ID and list the merged IDs next to it.
- **Group by claim.** Put each reason under the claim (C1, C2, … from the paper memory) it supports or undercuts, with its pairs. Reasons tied to no claim go under *General*.
- **Mark each reason's status.**
  - `checked`: its evidence is already verified (a quote read in place, a number recomputed).
  - `open`: it rests on an unverified reading, an assumption, a suspicion, or a "Depends on" condition not yet checked.
- **Rank by swing**, meaning how far the decision could move if the reason turned out differently. A reason has high swing when it is `open` and also bears on a central claim, or has worst case fatal or major, or decides a pair.

**Probe.** Examine each high-swing `open` reason in detail, in order of swing. Probe every reason whose worst case is fatal; a typical paper needs 5–12 probes. Record each probe as P1, P2, …:

| Field | Content |
|---|---|
| Item | the ledger ID, or IDs for a pair |
| Question | one precise question the paper can answer, e.g. "Is the baseline in Table 3 trained with the same schedule as the method (§4.1, App. B)?" |
| Method | what was done (see below) |
| Result | confirmed / refuted / partly / cannot be settled from the paper, with the location and the quote or computation |
| Change | the ledger update, before → after |

Methods, as the reason requires:

- Re-read the specific sections, appendix and supplement included, rather than relying on the first reading.
- Recompute numbers: sums, averages, gains, error bars, percentages. Cross-check each table against the text and against the other tables.
- Trace the evidence chain: claim → experiment → table or figure → number. Note where it breaks.
- Check a derivation step, or that a definition is used consistently.
- For novelty, run a targeted literature query, inline (`references/literature_search.md`). Delegate only when the host can search only from a subagent.

Update the ledger from each probe:

- A refuted reject reason moves to *Answered*.
- A confirmed suspicion becomes an `error`, with the check as its evidence.
- An accept reason whose condition fails loses strength.
- A new reason the probe uncovers enters the ledger with the next ID, marked "found by P3".
- Every reason probed becomes `checked`, or stays `open` with the result "cannot be settled from the paper".

**Rules for probes.**

- A probe settles facts ("does the paper do X?"), never values ("does X matter?"), and never assigns a grade.
- A reason that stays unsettled is a `question` (Hard Rule 10). No type may grade it above minor.
- Stop when every high-swing reason is `checked` or unsettled. The probes cover the reasons that can move the decision, not every reason.

## Step 3: The reviewer roster

List the types of reviewer this paper could plausibly get at the target venue. A type is defined by its **expertise and what it values**. It is never defined by a verdict: "harsh reviewer", "champion" and "skeptic" are not types.

Write one row per type, with these columns:

| Column | Content |
|---|---|
| Type | T1, T2, … with a descriptive name |
| Aspect | the primary aspect this type speaks for, one of the seven keys: `technical_rigor`, `clarity`, `novelty`, `significance`, `experimental_validation`, `reproducibility`, `ethics` |
| Expertise | e.g. "3D reconstruction specialist", "learning-theory reviewer", "practitioner deploying on edge devices", "evaluation and benchmark methodologist", "adjacent-field reviewer from robotics" |
| Values | what makes a paper good in this type's eyes |
| Distrusts | what it usually catches or objects to |
| Weighs most | the ledger IDs this type will judge hardest |
| Likelihood | how likely the venue assigns this type: high / medium / low |

Rules for the roster:

- **Use 4–8 types.** Use more when the paper spans several areas.
- **Follow the aspect ratio.** Every aspect with at least 12% of the ratio gets at least one type whose primary aspect it is. Give the heavier aspects more types when the paper raises distinct questions there (for example, a theory type and an evaluation-methodology type both under `technical_rigor`). The number of types never changes an aspect's weight: the script splits each aspect's share equally among its types.
- **Coverage.** Every aspect that has an accept or reject reason is covered by at least one type, and every ledger item is in some type's "Weighs most".
- **Mix.** Include at least one specialist in the paper's own sub-area and at least one reviewer from outside it. The venue's actual reviewer pool sets the mix: a paper on benchmark methodology draws evaluation experts, and an applied paper draws practitioners.
- **Personas.** Types are archetypes. Never name or describe a real person (Hard Rule 3).

## Step 4: One review per type

Write the reviews in roster order. Each review argues from the ledger:

1. **Reading of the ledger.** Name the items that matter to this type, by ID.
   - For each accept reason it relies on, say why it holds, or why it is discounted from this type's expertise.
   - For each reject reason it weighs, grade it **fatal / major / minor / not a concern**, with one line on why. The grade can never exceed that reason's worst case, and an unsettled `question` is never graded above minor.
   - Items the review does not name count as neutral.
2. **New reasons.** If this type sees a reason missing from the ledger, it first adds the reason to the ledger as the next A or R, marked "added in T3 review", with the same evidence requirements. Only then may it use the reason. Later types see the addition. A review never raises a point that is not in the ledger.
3. **Opinion.** Write 120–250 words in the type's voice: its overall judgment and what would change its mind. End with a line naming the deciding items, for example: `Decisive: R2 (major), A1 (strong), A4 ↔ R6 (A4 holds)`.
4. **Scores.** These follow from the decisive items. They do not follow from tone or from the previous type's numbers.
   - First the **pool position**: the share of the venue's submissions this paper beats, in this type's view, with the decisive IDs as its basis.
   - Then the seven dimension scores (0–100), inside the pool position's band (`references/quality_rubrics.md`).
   - Then **Overall** (1–6) and **Confidence** (1–5). Confidence reflects how well this type's expertise covers the paper.

**Same context, separate judgments.** All the types share one context, so their judgments are not independent; say so in the output. To keep each review its own:

- score each type from its own reading of the ledger;
- never adjust a score toward an earlier type's;
- never let a later review revise an earlier one.

If two types reach the same verdict for the same reasons, that is expected. Do not report it as independent confirmation.

**Settle factual splits.** After all reviews are written, look for splits: one type grades a reason fatal or major while another grades it minor or not a concern.

- When a split rests on a **fact**, run one more probe on that fact and record it like the others. For example, T2 assumed the baselines were retuned and T5 assumed they were not.
  - Each type whose grade depended on the fact updates that one grade, logged as "updated after P9: major → minor".
  - If the reason was among the type's decisive items, the type's scores are updated too.
- When a split rests on **values** (how much the point matters to that expertise), it stays. That is the disagreement the roster exists to show.
- Run at most one such round.

## Step 5: The average

1. Write `scores.json` in the format of `scripts/example_scores.json`:
   - one entry per type, with `role` set to `"T1 (<type name>)"`, plus `aspect`, `confidence`, `overall`, `pool_position` and `scores`;
   - no `eic_weight`;
   - `"da_critical": []`.
2. Run `python3 scripts/aggregate_scores.py scores.json --venue <key> --json --out aggregate.json`.
3. The **final rating** is `ledger.venue_rating` in the output: the types' Overall ratings averaged with the aspect-ratio weights (`ledger.type_weights`), rounded half up (`ledger.suggested_overall`). Report the weighted pool position, the plain mean and the spread next to it.
   - Fix any `ledger.warnings` first: a heavy aspect without a type means the roster is incomplete, so add the type and its review.
   - The rating is not reweighted by likelihood or confidence, and there is no override.
   - Run the script again with `--final <final rating>` so the venue labels match.
   - Treat the script's warnings, such as a pool position that disagrees with a composite, as signs of an inconsistent type review. Fix that review's scores before averaging; never fix the average.

Then derive the summary from the ledger and the reviews:

- **Consensus map.** One row per ledger item: how many types named it, and their grades (for an accept reason: held or discounted).
- **Key strengths.** The accept reasons most types relied on.
- **Top concerns.** Rank the reject reasons by how many types graded them fatal or major, then by their worst grade. Give at most five, each with its ID, location and fix.
- **Revision roadmap.** Turn the reject reasons into revisions:
  - Priority 1: reasons any type graded fatal, or that most types graded major.
  - Priority 2: other reasons graded major.
  - Priority 3: reasons graded minor.
  - Each entry gives the fix, its cost, and the ledger ID it resolves.

---

## Output (`review.md`)

1. **Header.** Paper, paper type, field, target venue and its aspect ratio, date, mode `full` (ledger review), and the line "One context: the reviewer types share one model and one reading, so their judgments are not independent."
2. **Paper memory.**
3. **Ledger.** The accept table, the reject table, the Answered list, the aspect coverage lines and the pairs.
4. **Reorganized ledger and probes.** The reasons grouped by claim, with status and swing; the probe table P1, P2, … with each result and ledger change.
5. **Reviewer roster**, with each type's aspect.
6. **Reviews T1 … Tn.** Each one has: reading of the ledger, opinion, decisive items, and scores (pool position, the seven dimensions, Overall, Confidence). Then the post-review probes and the grades they updated.
7. **Scores and decision.** A table of every type's aspect, weight, pool position, Overall and Confidence; the aspect-weighted rating, the plain mean and the spread; the final rating with the venue's own label; the aggregation output.
8. **Consensus map, key strengths, top concerns and revision roadmap.**
9. **Integrity signals and limitations.** Include what could not be read and whether the literature check ran.

For a journal target, add the journal-style recommendation from `references/editorial_decision_standards.md`, mapped from the final rating.
