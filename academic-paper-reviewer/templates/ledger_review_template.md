# Ledger Review Template (full mode)

The output layout for `agents/ledger_reviewer_agent.md`. The sections follow its Steps 0–5 and its *Output* list, in order. Every grade, decisive item, top concern and Roadmap entry names its ledger ID (Hard Rule 5). Omit a section only where a mode says so: quick, methodology-focus and re-review use subsets of this layout.

---

```markdown
# Peer Review: [Full paper title]

| | |
|---|---|
| Date | [YYYY-MM-DD] |
| Mode | full (ledger review) |
| Paper type | [empirical / theoretical / dataset / system / benchmark / analysis / position] |
| Field, sub-area | [e.g., computer vision, 3D reconstruction] |
| Task | [row(s) of references/task_neighbors.md; "adapted from <row>" if not listed] |
| Neighboring fields | [fields used for the novelty check and the roster] |
| Target venue | [venue; "inferred from <basis>" if not stated] |
| Aspect ratio | [output of `aggregate_scores.py ratio`, e.g. rigor 23%, validation 19%, novelty 16%, …] |
| Literature check | [ran: N queries / off / no network] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

---

## 1. Paper memory

**Claims.** C1: [claim] ([location]). C2: …
**Setup facts.** [fact] ([location] or "not stated"); …
**Headline numbers.** [number] ([table]); …
**Could not be read.** [figures, garbled equations, missing supplement, …]

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | | | [location + number or quote] | strong / moderate / weak | |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | | | [location + quote; the check for an error] | error / gap / judgment / question | fatal / major / minor | [change + rough cost] |

### Answered

- [concern] — answered at [location].

### Aspect coverage

- [aspect]: A…, R… / considered, no reason

### Pairs

- A2 ↔ R4: [the claim they bear on]

---

## 3. Reorganized ledger and probes

### By claim

**C1: [claim]**
- A1 (checked), R3 (open, high swing; merged: R9), A2 ↔ R4 (open, decides the pair)

**General**
- …

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R3 | [one precise question] | [re-read / recompute / trace / derivation / literature query] | confirmed / refuted / partly / cannot be settled — [location, quote or computation] | [before → after] |

---

## 4. Reviewer roster

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 [name] | technical_rigor | [the task / a neighbor] | | | | R2, R5, A1 | high / medium / low |

---

## 5. Reviews

### T1: [type name] ([aspect]; [field])

**Reading of the ledger.**
- Holds: A1 ([why]). Discounts: A3 ([why, from this expertise]).
- R2: major ([one line]). R5: minor ([one line]). R7: not a concern ([one line]).

**Opinion.** [120–250 words in the type's voice: overall judgment, and what would change its mind.]

Decisive: [e.g. R2 (major), A1 (strong), A4 ↔ R6 (A4 holds)]

**Scores.** Pool position [0–100] (basis: [IDs]). Technical Rigor [ ], Clarity [ ], Novelty [ ], Significance [ ], Experimental Validation [ ], Reproducibility [ ], Ethics [ ]. Overall [1–6]. Confidence [1–5].

### T2: …

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P9 | T2 vs T5 on R4 | [fact] | [result + location] | T2: major → minor |

(Splits on values stay as they are and are listed in the consensus map.)

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 | | [ledger.type_weights] | | | |

- **Aspect-weighted rating:** [ledger.venue_rating] → **final rating [ledger.suggested_overall]** ([venue's own label]).
- Weighted pool position [ ]; plain mean [ ]; spread [max − min].
- Uncovered aspects and warnings: [ledger.warnings, or "none"].
- [For a journal target: the journal-style recommendation from references/editorial_decision_standards.md.]
- [On `compare venues`: one row per venue with its re-weighted rating, label and scale verification status.]

<details><summary>Aggregation output</summary>

[the script's Markdown output]

</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R2 | 4 of 6 | T1 major, T3 major, T4 minor, T6 fatal |

### Key strengths

- A1: [reason] — held by [n] of [N] types.

### Top concerns (at most five)

1. R2: [concern] ([location]). Fix: [change, cost].

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R2 | | |
| 2 | | | |
| 3 | | | |

---

## 8. Integrity signals and limitations

- **Integrity signals:** [integrity_scan findings, with quote and location; "none found"]. These never change a score.
- **Limitations:** [what could not be read; whether the literature check ran; novelty reasons marked [verify]; the types share one context.]
```
