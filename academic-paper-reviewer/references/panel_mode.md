# Panel Mode (the 2.x review)

The review that was the default before 3.0: five reviewers with fixed roles (Methodology, Domain, Perspective, Generalist, Devil's Advocate), a literature check and a report check, and an Editor-in-Chief who weights the reviewers and decides. It runs when the user asks for a "panel review", "five reviewers" or a review "with an editor", and in `guided` mode on request. Since 3.0 the default `full` mode is the single-agent ledger review (`agents/ledger_reviewer_agent.md`).

Hard Rules 1–4 and 6–10 of `SKILL.md` apply. Panel mode keeps no ledger, so in place of Hard Rule 5 (traceability to the ledger) this rule applies:

**Panel rule (Hard Rule 5 in panel mode): upheld DA-CRITICAL issues block acceptance.** If the Devil's Advocate raises a CRITICAL issue and the EIC upholds it after checking it against the paper, the decision is capped at Borderline Accept (4) when the fix needs only clarification or minor additions, and at Borderline Reject (3) when it needs new data, experiments or a redesign. See `references/editorial_decision_standards.md`.

In this mode the integrity findings (Hard Rule 9) go to the EIC alone: the five reviewers read the redacted copy, and only the EIC sees the findings.

## Workflow

### Phase 0: Field Analysis and Reviewer Configuration

Read the complete paper, then follow `agents/field_analyst_agent.md` to identify the discipline, paper type, venue tier and maturity, and to configure five fictional reviewer personas plus the EIC (meta-reviewer).

Present the **Reviewer Configuration Card**, state any assumptions, and proceed with the review. Pause only if the user requests panel approval or missing input prevents a useful review. Apply later corrections without repeating completed work.

Phase 0 also produces the **paper memory** (`references/error_audit.md`, Section 3): the claims C1, C2, … with locations, the setup facts (splits, data, backbone, compute, seeds, each located or "not stated"), the headline numbers with their source tables, a summary of what the appendix and supplement add, and what could not be read. It is a factual record, not a judgment, and every reviewer receives it. Phase 0 also runs `scripts/integrity_scan.py --paper paper.txt --redact reviewer_copy.txt` on the paper text (Hard Rule 9). The reviewers in Phase 1 read `reviewer_copy.txt` and the paper memory; the findings go to the EIC alone. A flagged sentence is replaced by a neutral placeholder. If it held real content, the EIC restores it in Phase 2.

When network access is available, Phase 0 also writes the **fingerprint** for the literature check (`scripts/related_search.py fingerprint`): title, method names, identifiers, distinctive phrases and cutoff date. It is used only to exclude the paper from searches.

### Phase 1: Separate Multi-Perspective Review

| Reviewer | Agent file | Focus | Primary scoring responsibility |
|----------|-----------|-------|------------------|
| Reviewer 1 (Methodology) | `agents/methodology_reviewer_agent.md` | Design, statistics, fairness of comparison, reproducibility | Technical Rigor, Experimental Validation, Reproducibility |
| Reviewer 2 (Domain) | `agents/domain_reviewer_agent.md` | Literature positioning, theory, domain contribution | Novelty & Originality |
| Reviewer 3 (Perspective) | `agents/perspective_reviewer_agent.md` | Cross-disciplinary links, deployment, assumptions, broader impact | Significance & Impact, Ethical Compliance |
| Reviewer 4 (Generalist) | `agents/generalist_reviewer_agent.md` | Contribution clarity, venue fit, presentation, balanced overall judgment | Clarity & Presentation |
| Devil's Advocate | `agents/devils_advocate_reviewer_agent.md` | Strongest counter-argument, logic, overclaiming | CRITICAL/MAJOR/MINOR issue list |

**Execution and separation.** Use parallel reviewers only when the host permits delegation and the tools are available. Give each reviewer the manuscript, its own role file, the template, and the relevant references, without other reviewers' reports. Otherwise perform five separate role-based passes and disclose that they share one model context; do not claim independent agents ran. Even separate subagents share one model, so describe them as separate reviewers, never as independent judges whose agreement confirms a point. Each pass examines the manuscript from its own angle. Preserve genuine agreement; merge overlap in Phase 2. Missing delegation never blocks a full review.

Each report uses `templates/peer_review_report_template.md`, except the Devil's Advocate, whose format is defined in its agent file. Before scoring, read `references/quality_rubrics.md`. For CV/ML papers, the Methodology and Domain reviewers also read `references/cv_review_checklist.md`.

**Error audit** (`references/error_audit.md`). The Methodology Reviewer runs the claim-grounded audit and the omission sweep, and keeps an Error Log (categories E1–E9, each entry with location, verbatim quote, how it was verified, confidence and severity). The Domain Reviewer checks citations (E7). The Devil's Advocate checks claim distortion (E5), which LLM reviewers detect least reliably, and re-checks the errors behind its CRITICAL issues.

The EIC is **not** in Phase 1. It sees the reports only in Phase 2.

### Phase 1.5: Literature Check (after the five reports are drafted; needs network access)

The literature check comes **after** the reviewers have read the whole paper, so it supplements their reading and never replaces it. Follow `references/literature_search.md`:
1. **Round 1, claim-driven and benchmark searches** (concept words only; the script refuses queries that could retrieve the paper and drops results that are the paper itself, its reviews or its outcome):
   - one query per contribution claim, using the claim IDs (C1, C2, …) from the Methodology Reviewer's claim-to-evidence map (`--purpose claim --tag C1`);
   - one query per external benchmark the paper reports on (`related_search.py benchmarks` lists them; `--purpose baseline`), then `scout` to find prior work reporting on that benchmark.
2. **Round 2, expansion:** run `coverage` and fill its gaps (years with no prior work, dataset or foundational papers behind the baselines, claims with no query) with `--purpose expansion`. At most 12 queries in total; stop earlier when the gaps are closed.
3. Run `related_search.py similarity` to find the **closest prior works** and any **text overlap**.
4. The Domain Reviewer adds a **literature-check addendum** to its report: a per-claim novelty verdict from the claim-level profile (typed claims, prior works rated 1–5 for coverage, `related_search.py novelty`; one established claim is MAJOR at most, never "the paper is known"), a novelty delta table against the closest prior works, a **baseline scout table**, a short **field snapshot** (what counts as significant in this sub-field right now), and verified missing references. The Devil's Advocate may add a criterion-7 issue ("known results presented as new"). The other reports are not rewritten.
5. Only results labelled **prior (peer-reviewed)** or **prior (arXiv-only, 6+ months before the cutoff)** can be required comparisons. **Recent preprints**, **concurrent** and **newer** work are "worth discussing" only: never a weakness on their own, and never a reason to lower a score.

Default mode is `on`. Use `strict` (drops everything after the cutoff) to simulate a review as of submission. Without network access, skip this phase, say so, and rely on knowledge with `[verify]`.

### Phase 1.6: Report Check (after Phase 1.5, before the EIC)

**Order:** Phase 1 → Phase 1.5 → Phase 1.6 → Phase 2. The check runs after the literature-check addendum is written, so it covers the addendum too. When Phase 1.5 is skipped, it runs right after Phase 1.

The Synthesizer checks every weakness in the five reports before it builds the package (`agents/editorial_synthesizer_agent.md`, Step 0). This is the same kind of check that the ICLR 2025 feedback agent ran on human reviews. Each weakness must pass four tests:
1. **Specific.** It names a location, what is wrong, and why it matters. Rewrite a vague weakness, or drop it.
2. **Not already answered.** Search the paper, appendix included, for the point. If the paper answers it, drop it or turn it into a question about clarity.
3. **Consistent with the paper.** It makes no claim the paper contradicts. Novelty statements about prior work must match that work's abstract.
4. **Actionable and professional.** It gives a concrete fix and critiques the work, never the authors.

Then order each report's weaknesses by severity and move cosmetic issues into one *Minor* line. Reviews that overweight minor issues were the most common complaint about AI reviews at AAAI-26. Record what changed in a short table (dropped / rewritten / moved, with reasons). Scores are not changed here. The EIC sees the table.

### Phase 2: EIC Meta-Review and Decision

1. **Synthesizer, part A** (`agents/editorial_synthesizer_agent.md`): deduplicate issues, classify them (CONSENSUS-4/5, CONSENSUS-3, CONSENSUS-2, SPLIT, SOLO, DA-CRITICAL), mark the issues the outcome may hinge on, and compute the **official** score (plain mean of the reviewers' raw scores) with `scripts/aggregate_scores.py`.
2. **EIC meta-review** (`agents/eic_agent.md`, panel mode):
   1. Read all five reports and the package **first**.
   2. Read the paper briefly, checking every decisive point against the text.
   3. Give each reviewer a **quality weight** (0.5–1.5) for how much their comments and scores should count.
   4. Rule on each DA-CRITICAL issue with the AC test (uphold, or downgrade to MAJOR).
   5. Rerun the script for the **EIC assessment**. The **EIC-weighted mean of the reviewers' Overall ratings** is the starting point, and the 0–100 composite is a cross-check.
   6. **Make the final decision**, explaining any departure from the starting point and any disagreement with the cross-check. The decision can never exceed the DA ceiling. Rerun with `--final <N>` so the venue labels reflect the decision.
3. **Synthesizer, part B**: record the decision, then assemble the Editorial Decision Package and the Revision Roadmap using `templates/editorial_decision_template.md`.

For a journal target, also report the journal-style recommendation (Accept / Minor Revision / Major Revision / Reject) using the mapping in `references/editorial_decision_standards.md`.

**Venue translation (always for the target venue; for all venues on `compare venues`).** Run the aggregation with `--venue <key>` (or `--all-venues`). This produces the target venue's own scores (e.g., ICLR Soundness/Presentation/Contribution and rating, the ICML 1–5 recommendation, the TMLR Yes/No criteria) and, on request, a **Cross-Venue Outlook**: how the same paper would likely fare at each venue, and why. Present each venue's scale with its verification status. Never present an `assumed`, `secondary` or `unpublished` label as official wording.

**Venue format.** If the user asks for `venue format`, also render each reviewer's report using the target venue's form fields (listed in `scripts/venues.json`) instead of the generic template, keeping the same content.

### Phase 2.5: Revision Coaching (on request, if the decision is below Accept)

A Socratic dialogue led by the EIC (see `agents/eic_agent.md`): open with agreed strengths, ask what surprised the author, steer toward consensus issues, ask "If you could change only three things, which three?", rehearse a response to the DA's strongest challenge, then plan the revision. One question per turn, 200–400 words per turn, at most 8 rounds. "Just fix it" skips straight to the final Roadmap.

## Scores in panel mode

Every non-DA reviewer gives two complementary sets of scores, and the DA gives the 0–100 set. The full rubrics and mappings are in `references/quality_rubrics.md`.

| Scale | Dimensions | Purpose |
|-------|-----------|---------|
| NeurIPS-style 1–4 | Quality, Clarity, Significance, Originality | Familiar coarse ratings |
| Overall 1–6 | 6 Strong Accept … 1 Strong Reject | Recommendation (definitions in `references/editorial_decision_standards.md`) |
| Confidence 1–5 | Reviewer certainty | Weights the EIC assessment (with the EIC weight) |
| EIC-weighted rating | Weighted mean of the reviewers' Overall ratings | **The decision's starting point**; the 0–100 composite is a cross-check |
| EIC quality weight 0.5–1.5 | Set by the EIC per reviewer, after checking reviews against the paper | Multiplies confidence for the EIC assessment |
| Dimension scores 0–100 | Technical Rigor, Clarity & Presentation, Novelty & Originality, Significance & Impact, Experimental Validation, Reproducibility, Ethical Compliance | Fine-grained, calibrated, aggregated by paper type |

## Quality standards in panel mode

| Standard | Requirement |
|----------|-------------|
| Perspective differentiation | Each reviewer covers a distinct angle; the synthesizer merges duplicates |
| Evidence-based | Every point has a location in the manuscript; nothing fabricated (Hard Rules 1–2) |
| Specificity | "Table 3 compares against Mask2Former at 512² but the proposed method at 640²", not "baselines may be unfair" |
| Precision | Every claimed error has a location, a quote and a concrete check; suspicions are questions (Hard Rule 10) |
| Prioritization | Weaknesses ordered by severity; cosmetic issues grouped as Minor; presentation issues do not crowd out substance |
| Balance | Strengths and weaknesses are both substantive; minimum 3 strengths and 2 weaknesses per standard report |
| Actionability | Every weakness has a concrete fix and, where relevant, its effort or compute cost |
| Calibration | Each report states a pool position with its deciding evidence; scores follow the pool-position bands (a typical accepted paper 62–72, a typical rejected submission 42–54); field norms respected (see the CV calibration notes) |
| Meta-review | The EIC verifies every decisive point against the paper, justifies every reviewer weight, and explains any decision that departs from the starting point (the EIC-weighted rating) |
| Professional tone | Critique the work, never the authors; no sarcasm |
| DA completeness | One strongest counter-argument; CRITICAL used only for fatal issues; "No CRITICAL issues found" stated explicitly when true (the usual case) |
