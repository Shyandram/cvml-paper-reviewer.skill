# Peer Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | benchmark |
| Field, sub-area | machine learning; LLM agents for software engineering, code benchmarks |
| Task | Repository-level issue resolution / software-engineering agent benchmark (not listed; adapted from the "LLMs, NLP" row of `references/task_neighbors.md`) |
| Neighboring fields | LLM evaluation and data contamination (from the row); evaluation science / benchmark methodology (from the row); LLMs / NLP (from the row); empirical software engineering and mining software repositories (*added*); LLM agent systems and tool use (*added*); software testing and program repair (*added*) |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | significance 21%, experimental validation 19%, technical rigor 17%, clarity 15%, reproducibility 14%, novelty 10%, ethics 4% (`aggregate_scores.py ratio --paper-type benchmark --venue iclr`) |
| Literature check | off: no network in this evaluation; novelty reasons that rest on memory are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

---

## 1. Paper memory

**Claims.**
- C1: a contamination-resistant collection strategy. Public and held-out sets use only GPL/copyleft repositories, and a commercial set comes from proprietary startup codebases. The paper claims to be "the first to systematically apply such a methodology" (Abstract; Section 1; Section 3.1; Section 3.3).
- C2: challenging, long-horizon, enterprise-level tasks. Reference patches average 107.4 LOC across 4.1 files, every problem has at least 10 lines, and tasks "may require hours to days for a professional software engineer" (Title; Abstract; Section 1).
- C3: a three-stage human augmentation and verification workflow (problem statement, requirements, interface; test verification) ensures resolvability (Section 1; Section 3.2; Section 4.2; Section 4.3).
- C4: frontier models score below 25% Pass@1 (GPT-5 23.3% public, Opus 4.1 17.8% commercial). The public-commercial gap reflects "the greater complexity of enterprise codebases" (Abstract; Section 1; Section 5; Tables 1–2).
- C5: an LLM-as-judge analysis shows distinct failure modes. Large models fail on semantic correctness; small models fail on syntax, tool use and context (Section 1; Section 6.2; Table 3).
- C6: performance varies by language and repository (Section 6.1; Figure 4).

**Setup facts.**
- Size: 1,865 problems from 41 repositories. Public 731 from 11 repos, commercial 276 from 18, held-out 858 from 12 (Abstract; Section 3.3). Recomputed: 731+276+858 = 1865 and 11+12+18 = 41.
- Languages: Python, JS, TS, Go (Section 3.2; Section 7.1).
- Scaffold: SWE-Agent, the same prompt for all models, a maximum of 200 turns, open models on vLLM with 8×H100, models "as of September 18th, 2025" (Section 5).
- Metric: Pass@1, single run. Seeds and decoding settings: not stated after search.
- Augmentation: problem statement, requirements and interface are always provided at evaluation time (Section 5, Issue Ambiguity).
- Failure judge: GPT-5, last 20 turns, one bucket per instance (Section 6.2; App. B.1).
- Annotators: number, expertise, agreement and time are not stated after search.
- Held-out set: not evaluated (Section 5).

**Headline numbers.**
- Public set: GPT-5 23.3, Opus 4.1 22.7, Sonnet 4 17.6, Gemini 2.5 Pro 13.5, SWE-Smith-32B 6.8, GPT-4o 4.9, Qwen-3 32B 3.4 (Table 1).
- Commercial set: Opus 4.1 17.8, GPT-5 14.9, Gemini 10.1, Sonnet 4 9.1, GPT-4o 3.6 (Table 2).
- ">70%" on SWE-Bench Verified ([15], Section 1).
- Patches: 107.4 LOC, 4.1 files on average (Section 1).
- Verified: 161/500 one-to-two-line problems (Section 1).

**Appendix.** App. A gives a full Open Library instance (problem statement, requirements, interface) and Table 4 (original commit message vs rewritten issue). App. B.1 gives the full judge prompt.

**Could not be read.** Figures 1–4 (text only; captions used). Tables 1–3 are partly merged in extraction but legible. Supplementary material and the released data were not available. Data and code links were removed for review.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | The benchmark restores headroom after SWE-Bench Verified saturated: the best Pass@1 is 23.3% (public) and 17.8% (commercial). | Abstract; Table 1; Table 2; Section 1 | strong | Tasks are resolvable and the difficulty is not an artifact (R17, R5) |
| A2 | novelty | Contamination resistance comes from licence and access control: a GPL public set, a private held-out set and a proprietary commercial set. | Section 1 "exclusively selecting repositories distributed under strong copyleft licenses (GPL)"; Section 3.1; Section 3.3 | moderate | The design actually reduces contamination (R4) |
| A3 | significance | The commercial set (276 problems, 18 proprietary repos) evaluates on code no model developer can have trained on. | Section 3.3; Section 4.1; Table 2 | moderate | Its tasks are comparable and representative (R6, R23) |
| A4 | empirical strength | Tasks are larger: 107.4 LOC over 4.1 files on average, at least 10 lines each, and >100 tasks above 100 lines. Verified has 161/500 one-to-two-line tasks. | Section 1 "reference solutions span 107.4 lines of code across 4.1 files" | moderate | Patch size tracks difficulty (R5, R21) |
| A5 | soundness | Human augmentation targets false negatives from underspecification and misnamed interfaces. | Section 3.2; Section 4.2; App. A.1–A.3; Table 4 | moderate | Augmentation does not leak solutions (R10) |
| A6 | soundness | Test hygiene: tests are run three times and inconsistent ones filtered; annotators drop too-broad or irrelevant fail2pass tests; Docker environments are built by engineers. | Section 3.2 "we run each set of tests 3 times"; Section 4.3 | moderate | — |
| A7 | reproducibility | The public set is on HuggingFace; pre-built Docker images are promised; data and code links are given (removed); the judge prompt is released. | Section 3.2 Environments; Section 3.3; App. B.1 | moderate | The release happens as promised |
| A8 | significance | 41 actively maintained repos (consumer, B2B, dev tools), four languages, bug fixes and features, with a per-repo cap. | Section 1; Section 3.1; Figure 3 caption | moderate | — |
| A9 | analysis | Language and repository breakdowns show heterogeneity: Go and Python are higher, and some repos are below 10% for all models. | Section 6.1; Figure 4 (caption only) | weak | The figure supports the text (unavailable) |
| A10 | analysis | A failure taxonomy across six models, with the full judge prompt. | Section 6.2; Table 3; App. B.1 | weak (after P1, P2) | Table 3 is consistent (R2, R3) and the judge is valid (R14) |
| A11 | evaluation | A controlled comparison: one scaffold, the same prompt, a 200-turn cap, stated hosting and model date. | Section 5 | moderate | The scaffold is not model-biased (R8) |
| A12 | clarity | The task format is clear from a full worked instance and an original-vs-rewritten table. | App. A; Table 4 | moderate | — |
| A13 | ethics / honesty | Candid limitations: languages, test dependence, and augmentation "may inadvertently make problems too prescriptive". | Section 7.1 | moderate | — |
| A14 | significance | The held-out set (858 problems, 12 repos) is reserved for future overfitting checks. | Section 1; Section 3.3 | weak | Governance and an actual use (R19, R4) |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | clarity / correctness | The text and Table 1 disagree: Sonnet 4 is 16.3% in the text and 17.6 in the table, GPT-4o 3.9% and 4.9. The text also says "DeepSeek Qwen-3 32B". | Section 5 "also achieves a 16.3% resolve rate" vs Table 1 (cross-referenced) | error | minor | Align the text; minutes |
| R2 | soundness | Table 3's counts cannot come from the stated population. Section 6.2 says it filters "to only unresolved instances" of the public set (N=731), yet Submitted+Not-submitted is 920 for Opus 4.1 (≈565 expected), 915 for Gemini (≈632), 792 for Qwen (≈706), 789 for GPT-4o (≈695), 724 for GPT-5 (≈561) and 699 for Sonnet 4 (≈602). Four totals exceed 731. | Table 3; Table 1; Section 6.2 (recomputed, P1) | error (question in first reading) | major | State the unit of analysis, recompute Table 3 and fix the text; hours |
| R3 | soundness | The failure narrative contradicts Table 3. Qwen "exhibits the highest tool error rate (42.0%)", but Table 3 gives Qwen 349/792 = 44.1% and GPT-5 446/724 = 61.6%. Section 1 says smaller models fail more on syntax, but syntax is 223/920 = 24.2% for Opus against 184/792 = 23.2% for Qwen. | Section 6.2; Section 1; Table 3 (recomputed, P2) | error (question in first reading) | major | Rewrite the conclusions from corrected counts; hours |
| R4 | soundness | Contamination resistance (C1) is never tested: there is no held-out evaluation, no public-vs-held-out gap, no commit-date analysis and no memorization probe. The legal-barrier argument for GPL is asserted, and the gold patches sit in public git history. | Section 3.1 "we ensure benchmark content is unlikely to appear in proprietary model training sets"; Section 5 "we keep the private set held-out for future analysis" | gap | major | Evaluate the held-out set; stratify by commit date vs cutoff; soften the legal claim; days of compute |
| R5 | significance / scope | "Long-horizon" and "hours to days" are unmeasured. Difficulty is operationalized only by LOC and files, and the requirements and interface name exact files, functions and URLs (App. A.2–A.3), which removes much of the exploration. (Contribution check, Q2.) | Abstract "may require hours to days for a professional software engineer"; Section 5 "after being given significant details" | judgment | major | A human solve-time study on a sample, or agent-step statistics; or narrow the title |
| R6 | experimental validation | The public-commercial gap is attributed to enterprise complexity without controls. The commercial set's statistics are not reported, it has ≈15 problems per repo against ≈66, and rankings change (Sonnet 4 drops from 17.6 to 9.1, below Gemini's 10.1). | Section 1 "underscoring the greater complexity of enterprise codebases"; Tables 1–2; Figure 3 caption | gap | major | Commercial-set statistics; stratified comparison; or descriptive wording; hours |
| R7 | experimental validation | Single run with no uncertainty. The 95% binomial CI is about ±3.1 pp on the public set and ±4.5 pp on the commercial set (derived), so GPT-5 (23.3) and Opus (22.7) are not separable. | Abstract "GPT-5 achieving the highest score to date at 23.3%"; Tables 1–2 (derived, P11) | gap | major | Add CIs; 3 seeds for the top models |
| R8 | experimental validation | There is one scaffold. Agentless is dismissed without numbers. GPT-5 does not submit in 63.1% of its failures, 97.6% of them tool-use, which suggests scaffold mismatch. Open models get tool use by "syntax parsing". | Section 5 "Agentless has difficulty in multi-file editing, thus, produces low evaluation scores"; Table 3 | gap | major | Agentless numbers plus a second scaffold for the top models; days |
| R9 | experimental validation | The ">70%" contrast comes from external reports with different scaffolds and is not measured under this paper's setting. | Section 1 "over 70% pass rate on SWE-Bench-Verified [15]"; Figure 2 caption; Section 8 | gap | major | Run the same scaffold on Verified; about one day |
| R10 | soundness | The augmentation and verification pipeline is unquantified: no annotator count or expertise, no time, agreement or attrition. The claim of no leakage is asserted while the requirements name exact paths and functions. | Section 3.2; Section 4.2–4.3; App. A.2 "Requirements never include specific code implementation and don't leak solutions" | gap | major | Pipeline statistics plus an independent leakage audit |
| R11 | experimental validation | There is no ablation of the problem statement, requirements and interface, so the false-negative claim and the source of difficulty are untested. | Section 3.1 "the setting without requirements is potentially interesting"; Section 7.1 | gap | major | Three settings × 2–3 models on the public set |
| R12 | novelty | The pipeline refines SWE-bench (commit pairs, fail2pass, Docker, verification "Similar to SWE-Bench Verified"). The deltas are licence-based selection, private sets, augmentation and a size filter: moderate novelty (contribution check, Q3). The "first" claim is unchecked [verify]. | Section 1 "the first to systematically apply such a methodology"; Section 3.1; Section 4.1; prior: [13], [15], [19], [25] | judgment | major | Position the deltas explicitly; qualify "first" |
| R13 | novelty / related work | There is no quantitative comparison table with prior SWE benchmarks, and related work is missing: SWE-Lancer, SWE-Gym, LiveCodeBench, and SWE-smith (evaluated in the paper but not cited). | Section 2.1; Section 5 "e.g. SWE-Smith" | gap | minor | Add the table and citations |
| R14 | experimental validation | The judge is not validated here. The 87% figure is borrowed from [22]. The 20-turn choice is "highest correspondence with human validations" with no numbers. GPT-5 judges itself. The Table 3 buckets do not match the App. B.1 categories. | Section 6.2 "Our work follows Yang et al. [22], who demonstrate 87% alignment"; Table 3; App. B.1 | gap | major | Human-label about 100 trajectories; a non-participant judge; a bucket mapping |
| R15 | reproducibility | Statistics are given only for the public set. | Figure 3 caption "Distributions in the public set"; Section 3.3 | gap | minor | A table for all three sets |
| R16 | clarity / correctness | Per-repo counts are inconsistent: "between 50 and 100 instances, with a strict cap of 100" (Section 1), "50-100+ instances" (Section 3.1), and the commercial set has 276/18 = 15.3 per repo. | Section 1; Section 3.1; Section 3.3 (derived) | error | minor | Correct and list per-repo counts |
| R17 | soundness | The Figure 1 caption names "difficulty filtering"; only the size filter is described. If any model-based filter was used, the low scores are partly by construction. | Figure 1 caption; Section 1; Section 3.1 | question | major (graded ≤ minor while unsettled) | Describe all filters and their attrition |
| R18 | reproducibility | Decoding settings, context handling, cost, exact model IDs and the prompt are not given ("a basic prompt outlining the task"). | Section 5 Evaluation settings | gap | minor | Appendix; cheap |
| R19 | reproducibility / significance | The private sets have no described governance (who evaluates, how often, submission process, release of held-out results), and the commercial results cannot be reproduced. | Section 3.3 "will update in the leaderboard"; Section 5 | gap | major | Describe the evaluation service, versioning and per-instance results |
| R20 | experimental validation | Open-weight coverage is thin: two 32B models on the public set and none on the commercial set. | Table 1; Table 2 | gap | minor | Add stronger open coding models |
| R21 | experimental validation | Resolve rate by patch size or file count, the direct test of C2, is not in the text. The Figure 4 caption mentions "10+ files and 500+ LOC" categories that the text does not describe. | Figure 4 caption; Section 6.1 | question | minor | A table of resolve rate by LOC and file bins |
| R22 | clarity / citations | Citation slips: "SWE-Bench [25]" (abstract) where [25] is "Swe-bench goes live!"; "social media posts [1, 25]" cites arXiv papers; "SWE-Bench Verified [13]" where Verified is [15]. | Abstract; Section 1; References | error | minor | Fix the keys |
| R23 | ethics | Commercial repos include acquired companies and startups founded by the authoring organization's employees: representativeness and COI are not discussed, nor is contributor consent. The legal claim about GPL is unsupported. | Section 4.1; Section 3.1 "creates legal barriers" | judgment | minor | Discuss selection, COI and consent; qualify the legal claim |
| R24 | clarity | Table 3 mixes percentage bases without saying so; "endless file reading" (text) is "Stuck in Loop" (table); "exclude trivial edits (1–10 lines of code)" conflicts with "at least 10 lines of change"; promotional wording in Section 8. | Table 3; Section 6.2; Section 1; Section 8 | gap | minor | Edit |

### Answered

- Flaky tests could cause false failures: answered at Section 3.2 (Tests: three runs, inconsistent tests filtered) and Section 4.3 (Environment verification).
- Trivial one-line problems: answered at Section 1 (edits below 10 lines excluded).
- Valid solutions failing because of naming: answered at Section 3.2 (Interface) and App. A.3. The residual risk is acknowledged in Section 7.1.
- Language coverage: disclosed at Section 7.1 ("Limited Language Coverage").
- Single-repository dominance: answered at Section 1 and Section 3.1 (per-repo cap; the count inconsistency is kept as R16).

### Aspect coverage

- significance: A1, A3, A8, A14; R5, R6, R19
- novelty: A2; R12, R13
- technical rigor / soundness: A5, A6; R2, R4, R10, R16, R17
- experimental validation: A9, A10, A11; R3, R6, R7, R8, R9, R11, R14, R20, R21
- reproducibility: A7; R15, R18, R19
- clarity: A12; R1, R22, R24
- ethics: A13; R23

**Omission sweep:**
- splits: present (public, commercial and held-out, Section 3.3);
- seeds and runs: not stated after search (R7);
- baseline settings: present (Section 5);
- hyperparameters and decoding: not stated after search (R18);
- compute: present (8×H100, Section 5), cost not stated;
- licence: present (GPL, Section 1; partnership agreements, Abstract);
- consent of contributors to the commercial code: not stated (R23);
- limitations: present (Section 7.1);
- code and data: present (public set on HuggingFace, Section 3.3; links removed).

### Pairs

- A2 ↔ R4: contamination resistance (C1)
- A3 ↔ R6: what the commercial set shows (C1/C4)
- A4 ↔ R5, R21: task complexity and "long-horizon" (C2)
- A5 ↔ R10, R11: augmentation (C3)
- A1 ↔ R9, R17: size and source of the headroom (C4)
- A11 ↔ R8: controlled comparison vs scaffold confound (C4)
- A10 ↔ R2, R3, R14: failure analysis (C5)
- A7, A14 ↔ R19: openness and governance

---

## 3. Reorganized ledger and probes

No duplicates needed merging: R17 and R21 both bear on C2 but ask different facts.

### By claim

- **C1: contamination resistance.** A2 (checked), A3 (checked), A14 (checked), R4 (checked after P3; high swing; decides A2 ↔ R4), R12 (checked as judgment after P10; high swing), R19 (checked; medium swing), R23 (checked; low).
- **C2: complex, long-horizon tasks.** A4 (checked), A8 (checked), R5 (checked after P4; high swing; decides A4 ↔ R5), R16 (checked; low), R17 (open after P9; high swing, unsettled question), R15 (checked; low), R21 (open after P12; medium, unsettled question).
- **C3: human augmentation and verification.** A5 (checked), A6 (checked), R10 (checked after P8; high), R11 (checked after P8; high).
- **C4: headline results and the public-commercial gap.** A1 (checked), A11 (checked), R1 (checked; low), R6 (checked after P5; high), R7 (checked after P11; medium), R8 (checked after P6; high; decides A11 ↔ R8), R9 (checked after P7; high), R18 (checked; low), R20 (checked; low).
- **C5: failure modes.** A10 (checked, weakened by P1/P2), R2 (checked, error after P1; high), R3 (checked, error after P2; high), R14 (checked; medium).
- **C6: language and repository variation.** A9 (open: the figure is unavailable; low swing).
- **General.** A7, A12, A13 (checked), R13, R22, R24 (checked; low).

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R2, A10 | Do Table 3's failure counts match the unresolved public instances (N=731)? | Recompute Submitted+Not-submitted and 731×(1−resolve) | **confirmed.** Opus 681+239 = 920 vs ≈565; GPT-5 724 vs ≈561; Sonnet 699 vs ≈602; Gemini 915 vs ≈632; GPT-4o 789 vs ≈695; Qwen 792 vs ≈706. Four exceed 731. Internal sums are consistent: Opus sub-columns sum to 681, and 330/681 = 48.5%. | R2 question → error (major worst case); A10 moderate → weak |
| P2 | R3 | Does Table 3 support "highest tool error rate (42.0%)" for Qwen and Section 1's syntax claim? | Recompute shares of all failures | **confirmed.** Qwen tool-use 349/792 = 44.1% (86.0% of not-submitted); GPT-5 446/724 = 61.6%. Syntax: Opus 24.2%, Qwen 23.2%. The text's other figures do match shares of all failures (Opus wrong 330/920 = 35.9%, Sonnet long-context 249/699 = 35.6%). | R3 question → error |
| P3 | R4, A2 | Does the paper measure contamination anywhere? | Re-read Sections 3.1, 3.3, 5, 6; search "contamin", "held-out", "cutoff" | **confirmed absent.** Section 5: "we keep the private set held-out for future analysis". | R4 → checked; A2 holds as design, effect unmeasured |
| P4 | R5, A4 | Is "hours to days" measured? | Search "hours", "days", "time" | **confirmed absent.** The phrase occurs only in the abstract. | R5 → checked |
| P5 | R6, A3 | Are commercial-set statistics or stratified comparisons reported? | Re-read Section 3.3, Section 5, the Table 2 and Figure 3 captions | **confirmed absent.** The Figure 3 caption says "Distributions in the public set". Sonnet 4 moves from 17.6 (third) to 9.1 (fourth). | R6 → checked |
| P6 | R8, A11 | Are Agentless or second-scaffold numbers given, and is there evidence of scaffold mismatch? | Re-read Section 5; Table 3 | **confirmed.** No numbers. GPT-5 has 63.1% not submitted, 97.6% of those tool-use. | R8 → checked; A11 conditional on R8 |
| P7 | R9, A1 | Are the >70% Verified numbers measured here? | Re-read Section 1, the Figure 2 caption, Section 8, ref. [15] | **confirmed not measured.** [15] is an external page. | R9 → checked; A1 holds, but the size of the drop is unmeasured |
| P8 | R10, R11, A5 | Are annotation statistics or an augmentation ablation reported? | Search "annotator", "requirements"; re-read Sections 3–4, 7.1, App. A | **confirmed absent.** Section 3.1 calls the no-requirements setting "potentially interesting". | R10, R11 → checked |
| P9 | R17 | What is the "difficulty filtering" in the Figure 1 caption? | Re-read Sections 1, 3.1, 4 | **partly.** Only the size and multi-file filter is described. Whether a model-based filter was used cannot be settled from the paper. | R17 stays question (open), graded at most minor |
| P10 | R12, A2 | Is the pipeline new relative to SWE-bench, and is "first" checked? | Re-read Sections 2, 3.1, 4.1 (no literature query, no network) | **partly.** The pipeline is explicitly "Similar to SWE-Bench Verified" and Section 4.1 mirrors SWE-bench's commit-pair and fail2pass design. "First" cannot be checked without a search. | R12 → checked as judgment; prior-work part [verify] |
| P11 | R7 | Are the top-model differences larger than sampling noise? | Binomial SE | **confirmed small.** N=731, p=.233: SE 1.56 pp, CI ±3.06. N=276, p=.178: SE 2.30 pp, CI ±4.51. The GPT-5 vs Opus difference is 0.6 pp. | R7 → checked |
| P12 | R21 | Does the text report resolve rate by LOC or file count? | Search "LOC", "files", "500"; re-read Section 6.1 | **cannot be settled.** The caption mentions such bins, the text is silent and the figure is unavailable. | R21 stays question (open) |

All high-swing open reasons are now checked, except R17 and R21, which stay unsettled questions.

---

## 4. Reviewer roster

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 SWE-agent benchmark specialist | significance | the task: repository-level SWE agent benchmarks | builds and uses SWE-bench-style benchmarks | headroom, realism, uptake by the community | difficulty by construction, framing beyond the setting | A1, A2, A3, A4, A8, A14; R4, R5, R9, R12, R17, R19 | high |
| T2 Evaluation and benchmark methodologist | experimental_validation | evaluation science / ML measurement | measurement validity, statistics of leaderboards | uncertainty, controlled comparisons, validated analyses | single runs, confounded comparisons, unvalidated LLM judges | A1, A9, A10, A11; R2, R3, R6, R7, R8, R9, R11, R14, R20, R21 | high |
| T3 LLM data-contamination researcher | technical_rigor | LLM evaluation and contamination | memorization probes, contamination-free benchmarks | contamination claims backed by measurement | legal or access arguments offered as evidence | A2, A3, A14; R4, R6, R12, R19, R23 | high |
| T4 Empirical SE / MSR researcher (*added neighbor*) | technical_rigor | empirical software engineering, mining software repositories | commit mining, test-based oracles, dataset construction validity | documented pipelines, construct validity, annotation reliability | unquantified human curation, LOC as a difficulty proxy | A4, A5, A6, A8; R2, R5, R10, R11, R12, R13, R15, R16, R23 | medium |
| T5 General LLM reviewer (presentation) | clarity | LLMs / NLP | broad ICLR LLM reviewer | precise, internally consistent writing | numbers that disagree across text and tables, overclaiming | A12, A13; R1, R2, R3, R5, R13, R16, R21, R22, R24 | high |
| T6 Agent-scaffold engineer and benchmark user (*added neighbor*) | reproducibility | LLM agent systems and tool use | builds coding agents, runs benchmarks | runnable environments, full settings, open evaluation | private sets without governance, scaffold-specific results | A1, A7, A11, A14; R2, R7, R8, R10, R15, R18, R19, R20 | medium |

Every aspect with ≥12% of the ratio has a type. Novelty (10%) and ethics (4%) have no type of their own. Their reasons (R12, R13, R23) sit in the "Weighs most" of T1, T3 and T4, and the script renormalizes those aspects' shares away. Every ledger item is in some type's "Weighs most" (R1, R24 → T5; R18 → T6; A13 → T5; A12 → T5).

---

## 5. Reviews

### T1: SWE-agent benchmark specialist (significance; the task)

**Reading of the ledger.**
- Holds:
  - A1: the headroom is real under any reading of R9;
  - A3: a genuinely private test bed is something the field lacks;
  - A4 and A8: the tasks are larger and more varied than Verified's;
  - A2: as a design.
- Discounts:
  - A10: the failure analysis is secondary for a benchmark, and P1/P2 weaken it;
  - A14: unused so far.
- Grades:
  - R4 major: the selling point "contamination-resistant" has no measurement;
  - R5 major: the title's "long-horizon" is not what is measured, and the requirements hand over file paths;
  - R6 minor: the gap is descriptive, and an over-strong sentence can be softened;
  - R9 minor: headroom stands either way;
  - R12 minor: refinement novelty is normal for a benchmark;
  - R13 minor;
  - R17 minor: an unsettled question;
  - R19 minor: the public set alone is useful;
  - R11 minor;
  - R2 minor: the failure analysis is not why I would use this benchmark;
  - R8 minor.

**Contribution check.**
- Q1 (what does a reader learn): frontier agents resolve under a quarter of larger, multi-file tasks and fewer on private code. Why they fail is not reliably shown (R2, R3). This is mostly a ranking: partial fail.
- Q2 (framing): "long-horizon" and "enterprise-level" exceed what is operationalized (R5, R6): fail.
- Q3 (delta): a refinement of the SWE-bench and Verified pipeline with licence- and access-based sourcing (R12): moderate.
- Q4 (transfer): heavily specified tasks may not transfer to underspecified real issues (Section 7.1, R11): limited.

**Opinion.** As someone who uses these benchmarks, I want this benchmark to exist: Verified is saturated (A1), and a private commercial set (A3) is the right idea. The paper argues for the benchmark more than it measures it, though. Contamination resistance, its first contribution, rests on a licence argument and on access control, and neither the held-out set nor any date-based analysis is used to show it works (R4). The title promises long-horizon work, yet the evidence is LOC and file counts, and the augmentation gives agents file paths, function names and URLs (R5). Those two framings are what would lift the benchmark from "a harder SWE-bench" to a new evaluation standard. Without them, the delta over SWE-bench Verified is a careful refinement (R12). I would move up with a held-out evaluation, an ablation without requirements, and either a time study or a narrower title.

Decisive: R4 (major), R5 (major), A1 (strong), A3 (moderate)

**Scores.** Bracket: above B (A1, A3: the claims are tested on real agents in the target setting, unlike B's toy evidence), below C (R4, R5: like C, a useful artifact without an insight, and its framing exceeds the setting; C was at least fully tuned). Pool position 48 (basis: R4, R5, A1, A3). Technical Rigor 52, Clarity 60, Novelty 48, Significance 52, Experimental Validation 50, Reproducibility 60, Ethics 62. Overall 3. Confidence 4.

### T2: Evaluation and benchmark methodologist (experimental_validation; evaluation science)

**Reading of the ledger.**
- Holds:
  - A1;
  - A11: one scaffold and one prompt is at least controlled.
- Discounts:
  - A9: the figure is unavailable and no numbers are given in the text;
  - A10: its table is internally inconsistent (P1).
- Grades:
  - R2 major: the unit of analysis is wrong or unstated, so Table 3 cannot be interpreted;
  - R3 major: two stated conclusions are contradicted by the paper's own table;
  - R6 major: a causal reading of an uncontrolled comparison;
  - R8 major: GPT-5's 63% non-submission points to scaffold fit, not capability;
  - R9 major: the motivating contrast is measured under different conditions;
  - R11 major: the key design choice is never ablated;
  - R14 major: the judge is unvalidated and self-judging;
  - R7 minor: N=731 is decent, and the CI matters only for the top-two ranking;
  - R20 minor;
  - R21 minor (question);
  - R1 minor;
  - R17 minor (question).

**Contribution check.**
- Q1: rankings only, and the mechanisms claimed in Section 6.2 do not survive P1 and P2.
- Q2: not supported (R6, R9).
- Q3: refinement.
- Q4: unclear, given the scaffold dependence (R8).

**Opinion.** A benchmark paper lives or dies by the validity of its measurements, and here too many of them are unsupported. Table 3 reports more failed trajectories than there are problems (R2), and two of its stated conclusions contradict its own numbers (R3). The public-commercial gap is read causally with no controls (R6). The headline contrast with SWE-Bench Verified compares numbers from different scaffolds (R9). One scaffold, which GPT-5 visibly struggles with, carries every model comparison (R8). The augmentation that defines the task is never ablated (R11), and the failure judge is a participating model with no reported human agreement (R14). None of this is fatal to the dataset itself, but the evaluation section does not yet support the paper's claims. I would move up if Table 3 were recomputed, a second scaffold and a Verified run under the same settings were added, and an augmentation ablation were reported.

Decisive: R2 (major), R8 (major), R11 (major), R6 (major), A1 (strong)

**Scores.** Bracket: above B (A1, A11: the benchmark is evaluated in its real setting), below C (R2, R8, R11: C's comparisons were carefully tuned and internally consistent; here the analysis has an internal counting error and confounded comparisons). Pool position 36 (basis: R2, R8, R11, R6). Technical Rigor 44, Clarity 54, Novelty 46, Significance 50, Experimental Validation 36, Reproducibility 52, Ethics 60. Overall 2. Confidence 4.

### T3: LLM data-contamination researcher (technical_rigor; LLM evaluation and contamination)

**Reading of the ledger.**
- Holds: A3, because access control is real contamination resistance for the commercial set.
- Discounts:
  - A2: GPL licensing is not a technical barrier, and many public code crawls are not licence-filtered [verify]. The public set's gold patches are public commits, and the set is now on HuggingFace.
  - A14: a held-out set that is never evaluated shows nothing yet.
- Grades:
  - R4 major: the core claim is untested;
  - R19 major: without governance, the held-out set cannot do its stated job;
  - R6 major: the public-commercial gap is the only contamination-relevant signal, and it is confounded;
  - R12 minor;
  - R17 minor (question);
  - R23 minor;
  - R9 minor.

**Contribution check.**
- Q1: no contamination finding is reported.
- Q2: "contamination-resistant" is a design intent, not a demonstrated property.
- Q3: access-controlled private test sets and time-based contamination control exist in neighboring benchmarks (LiveBench [19] and SWE-bench-Live [25] are cited). The licence-based twist is new to me, but its effect is unshown [verify].
- Q4: the commercial set's results transfer only if its tasks are representative (R23).

**Opinion.** The paper's first contribution is a collection strategy that reduces contamination, but nothing in it measures contamination. The obvious test is available to the authors: run the same models on the 858-problem held-out set and compare with the public set. If the GPL argument works, the two should match. Other tests would be resolve rate by commit date against model cutoffs, or completion probes on gold patches. None is reported (R4, P3). The legal reasoning is an assertion, and the public set's patches are public git history. The commercial set is genuinely uncontaminated (A3), but its gap with the public set is confounded with repository mix (R6), so it cannot double as a contamination measurement. The held-out set's value also depends on governance the paper does not describe (R19). I would raise my score with a held-out evaluation and a date-stratified analysis.

Decisive: R4 (major), R19 (major), A3 (moderate)

**Scores.** Bracket: above B (A3: unlike B, the setting matches the claim for the commercial subset), below C (R4: the central claim lacks the measurement that C's rigor would have provided). Pool position 40 (basis: R4, R19, R6, A3). Technical Rigor 42, Clarity 58, Novelty 48, Significance 52, Experimental Validation 48, Reproducibility 50, Ethics 58. Overall 3. Confidence 4.

### T4: Empirical SE / mining-software-repositories researcher (technical_rigor; neighbor)

**Reading of the ledger.**
- Holds:
  - A4: larger patches are a real shift from Verified;
  - A6: test filtering is sound practice;
  - A8.
- Discounts: A5, because the process is described but its reliability is not measured.
- Grades:
  - R10 major: human curation is the paper's third contribution, and there is no annotator, agreement or attrition data;
  - R11 major: without the ablation we cannot tell whether requirements make the task a specification-implementation exercise;
  - R5 major: LOC is a weak proxy for effort, as the SE literature on change complexity, which the paper itself cites ([9], [16]), would suggest;
  - R2 major: a counting error in the one empirical analysis of agent behaviour;
  - R16 minor;
  - R15 minor;
  - R13 minor;
  - R12 minor;
  - R17 minor (question);
  - R23 minor.

**Contribution check.**
- Q1: little beyond "larger patches are harder".
- Q2: "enterprise-level" and "long-horizon" are not operationalized beyond size (R5).
- Q3: commit-pair mining with fail2pass tests is the SWE-bench pipeline (Section 4.1).
- Q4: the requirements strongly shape the tasks, so transfer to real issue resolution is uncertain.

**Opinion.** The sourcing pipeline is standard and correctly described: commit pairs, test patch vs gold patch, fail2pass/pass2pass, Docker environments, repeated test runs (A6). What the paper adds is human augmentation, which is precisely the part with no numbers (R10). How many annotators, with what expertise, how long per task, how many problems and tests were dropped at each stage, and how was leakage audited? The appendix example's requirements name the exact file, function and URL to implement. That supports the authors' own worry in Section 7.1 and makes the absent ablation (R11) central. The "long-horizon" claim rests on LOC and files only (R5). The dataset is likely useful, but the construction claims need data.

Decisive: R10 (major), R5 (major), R11 (major), A6 (moderate)

**Scores.** Bracket: above B (A4, A6: the construction is real and correctly executed), below C (R10, R5: less documented than a careful study like C). Pool position 44 (basis: R10, R5, R11, A6). Technical Rigor 46, Clarity 56, Novelty 46, Significance 54, Experimental Validation 50, Reproducibility 48, Ethics 58. Overall 3. Confidence 3.

### T5: General LLM reviewer, presentation (clarity; LLMs / NLP)

**Reading of the ledger.**
- Holds:
  - A12: the appendix example makes the task concrete;
  - A13.
- Grades:
  - R2 major: a reader cannot interpret Table 3;
  - R3 major: the text states conclusions the table contradicts;
  - R1 minor;
  - R22 minor;
  - R24 minor;
  - R16 minor;
  - R5 minor: wording that can be fixed;
  - R21 minor (question);
  - R13 minor.

**Contribution check.**
- Q1: the headline difficulty is clear, the mechanisms less so.
- Q2: the title overstates (R5).
- Q3: refinement.
- Q4: not assessed from my expertise.

**Opinion.** The paper is easy to follow at the level of what the benchmark is: Sections 3–4 and the Open Library example (A12) explain the task format well, and the limitations section is candid (A13). The internal consistency is poor, though:
- the Results text and Table 1 disagree on two models (R1);
- Table 3's counts exceed the set size (R2);
- Section 6.2's "highest tool error rate" claim is contradicted by the same table (R3);
- per-repository counts are stated three ways (R16);
- several citation keys point to the wrong paper (R22);
- Table 3 mixes percentage bases without saying so (R24).

Individually these are fixable at revision, but together they make the reader distrust the numbers. A clean pass over every number and citation would move me up.

Decisive: R2 (major), R3 (major), A12 (moderate)

**Scores.** Bracket: above B (A12, A13), below C (R2, R3: C was internally consistent). Pool position 46 (basis: R2, R3, R1, A12). Technical Rigor 50, Clarity 52, Novelty 50, Significance 54, Experimental Validation 48, Reproducibility 56, Ethics 62. Overall 3. Confidence 3.

### T6: Agent-scaffold engineer and benchmark user (reproducibility; neighbor)

**Reading of the ledger.**
- Holds:
  - A7: a public set with Docker environments is directly usable;
  - A11;
  - A1.
- Discounts: A14, because without a protocol I cannot use it.
- Grades:
  - R19 major: I cannot evaluate my agent on the commercial or held-out sets and no process is described;
  - R8 major: the tool-use failures of GPT-5 look like scaffold and format problems I see in practice;
  - R18 minor: missing decoding settings and the prompt are easy to add;
  - R20 minor;
  - R7 minor;
  - R10 minor;
  - R15 minor;
  - R2 minor at first, "probably several runs pooled", updated after P13 to major.

**Contribution check.**
- Q1: a usable harder test bed, with no new insight.
- Q2: the "enterprise" framing rests on a set I cannot run.
- Q3: refinement.
- Q4: results are scaffold-specific (R8).

**Opinion.** From a builder's perspective, the public set with pre-built environments is what I would actually use, and the paper gets that part right (A7, A11). Two-thirds of the benchmark is closed, though, and the paper does not say how outsiders get evaluated on it, how often results are refreshed, or how the held-out set will be used (R19). Without that, the commercial numbers in Table 2 are claims I cannot reproduce. All comparisons also run through one scaffold, which seems to suit some models' tool formats better than others (R8). The missing prompt and decoding settings (R18) are easy to fix. I would move up with a documented evaluation service and a second scaffold.

Decisive: R19 (major), R8 (major), A7 (moderate)

**Scores.** Bracket: above B (A7, A11: a runnable artifact in the target setting), not above C (R19, R8). No accept reason shows a D-like new result, and a released artifact alone does not cross C. Pool position 50 (basis: R19, R8, A7). Technical Rigor 50, Clarity 60, Novelty 48, Significance 54, Experimental Validation 50, Reproducibility 56, Ethics 60. Overall 3. Confidence 4.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P13 | T6 (minor) vs T2, T4, T5 (major) on R2 | Could Table 3 pool the public and commercial sets, which would explain the counts? | **refuted.** Section 5: "For all analysis, we use the public set"; the Table 3 caption says "public set". Even pooled, Opus unresolved = 565 + 276×0.822 ≈ 792 ≠ 920. | T6: R2 minor → major (updated after P13). R2 was not among T6's decisive items, so T6's scores are unchanged. |

T1's minor grade on R2 rests on value (the failure analysis matters little for a benchmark's significance), not on a fact, so it stays. Other value splits also stay:
- R6: T2 and T3 major, T1 minor.
- R8: T2 and T6 major, T1 minor.
- R5: T1 and T4 major, T5 minor.
- R19: T3 and T6 major, T1 minor.

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 SWE-agent benchmark specialist | significance | 0.240 | 48 | 3 | 4 |
| T2 Evaluation and benchmark methodologist | experimental_validation | 0.219 | 36 | 2 | 4 |
| T3 LLM data-contamination researcher | technical_rigor | 0.098 | 40 | 3 | 4 |
| T4 Empirical SE / MSR researcher | technical_rigor | 0.098 | 44 | 3 | 3 |
| T5 General LLM reviewer, presentation | clarity | 0.180 | 46 | 3 | 3 |
| T6 Agent-scaffold engineer and benchmark user | reproducibility | 0.164 | 50 | 3 | 4 |

- **Aspect-weighted rating:** 2.781 → **final rating 3 (Borderline Reject)**. The ICLR view for the same number is **4 on {0, 2, 4, 6, 8, 10}** (5 on the older {1, 3, 5, 6, 8, 10} scale), with sub-scores Soundness 2, Presentation 2, Contribution 2. The ICLR scale status is *secondary*: recent forms use this scale; verify it against the current form.
- Weighted pool position 44.2; plain mean 2.83; spread 1 (2 to 3).
- Uncovered aspects and warnings: none from the script. Novelty (10%) and ethics (4%) have no type of their own and are renormalized away.
- Composites (54.1, 47.3, 50.2, 50.8, 52.2, 53.5) all match their types' Overall; no cross-check warnings.

<details><summary>Aggregation output</summary>

```
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (SWE-agent benchmark specialist) | significance | 21% | 0.240 |
| T2 (Evaluation and benchmark methodologist) | experimental_validation | 19% | 0.219 |
| T3 (LLM data-contamination researcher) | technical_rigor | 17% | 0.098 |
| T4 (Empirical software-engineering / mining-software-repositories researcher) | technical_rigor | 17% | 0.098 |
| T5 (General LLM reviewer, presentation) | clarity | 15% | 0.180 |
| T6 (Agent-scaffold engineer and benchmark user) | reproducibility | 14% | 0.164 |

**Final rating (aspect-weighted mean)**: **2.78** → **3 (Borderline Reject)** · plain mean 2.83 · weighted pool position 44.2

| Venue | Venue-weighted composite | Band | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|
| ICLR (2026) | 51.2 | 3 → 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) | Soundness 2, Presentation 2, Contribution 2 | secondary |
```

Full JSON: `aggregate.json`; pre-final run: `before.json`.

</details>

This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R2 | 5 of 6 | T1 minor, T2 major, T4 major, T5 major, T6 major (after P13) |
| R3 | 2 of 6 | T2 major, T5 major |
| R4 | 2 of 6 | T1 major, T3 major |
| R5 | 3 of 6 | T1 major, T4 major, T5 minor |
| R6 | 3 of 6 | T1 minor, T2 major, T3 major |
| R8 | 3 of 6 | T1 minor, T2 major, T6 major |
| R11 | 3 of 6 | T1 minor, T2 major, T4 major |
| R19 | 3 of 6 | T1 minor, T3 major, T6 major |
| R9 | 3 of 6 | T1 minor, T2 major, T3 minor |
| R10 | 2 of 6 | T4 major, T6 minor |
| R14 | 1 of 6 | T2 major |
| R17 | 4 of 6 | T1, T2, T3, T4 minor (unsettled question) |
| R12 | 3 of 6 | T1, T3, T4 minor |
| R13 | 3 of 6 | T1, T4, T5 minor |
| R7 | 2 of 6 | T2, T6 minor |
| R1, R16, R21 | 2 of 6 | minor (T2/T5; T4/T5; T2/T5) |
| R15, R20, R23 | 2 of 6 | minor (T4/T6; T2/T6; T3/T4) |
| R18, R22, R24 | 1 of 6 | minor (T6; T5; T5) |
| A1 | 3 of 6 | held by T1, T2, T6 |
| A3 | 2 of 6 | held by T1, T3 |
| A4, A8 | 2 of 6 | held by T1, T4 |
| A11 | 2 of 6 | held by T2, T6 |
| A2 | 2 of 6 | held by T1, discounted by T3 |
| A14 | 3 of 6 | discounted by T1, T3, T6 |
| A10 | 2 of 6 | discounted by T1, T2 |
| A5 | 1 of 6 | discounted by T4 |
| A9 | 1 of 6 | discounted by T2 |
| A6, A7, A12, A13 | 1 of 6 each | held (T4; T6; T5; T5) |

### Key strengths

- A1: headroom after Verified's saturation (best 23.3% public, 17.8% commercial). Held by 3 of 6 types.
- A3: a genuinely private commercial set from proprietary codebases. Held by 2 of 6.
- A4 / A8: larger, multi-file, multi-language tasks from 41 repositories. Held by 2 of 6.
- A11: a controlled single-scaffold, single-prompt comparison. Held by 2 of 6, conditional on R8.

### Top concerns (at most five)

1. **R2**: Table 3's failure counts exceed the number of public problems for four models and the expected number of unresolved instances for all six (Table 3 vs Table 1, Section 6.2). Fix: state the unit of analysis, recompute Table 3 and the Section 6.2 percentages (hours).
2. **R4**: contamination resistance, the first contribution, is never measured (Section 3.1; Section 5 "we keep the private set held-out for future analysis"). Fix: evaluate the held-out set against the public set, and stratify by commit date vs model cutoff (days of compute).
3. **R5**: "long-horizon" and "hours to days" are unmeasured, and the requirements and interface name exact files and functions (Title; Abstract; App. A.2–A.3). Fix: a human solve-time study on a sample, or agent-step statistics; otherwise narrow the title.
4. **R6**: the public-commercial gap is attributed to enterprise complexity without controls or commercial-set statistics (Section 1; Tables 1–2; Figure 3 caption). Fix: report commercial-set statistics and a stratified comparison (hours).
5. **R8**: all comparisons use one scaffold; Agentless numbers are withheld, and GPT-5's 63.1% non-submission suggests scaffold mismatch (Section 5; Table 3). Fix: report Agentless and a second scaffold for the top models (days).

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R2 | Recompute Table 3 on the unresolved public instances, state the unit, and correct the Section 6.2 percentages | hours |
| 2 | R3 | Rewrite the failure-mode conclusions (Section 1, Section 6.2) from the corrected table | hours |
| 2 | R4 | Held-out evaluation, public-vs-held-out gap, commit-date stratification; qualify the GPL legal claim | days of compute |
| 2 | R5 | Human solve-time estimates or agent-step statistics; or narrow "long-horizon" / "hours to days" | small study or wording |
| 2 | R6 | Commercial-set statistics; stratified public-vs-commercial comparison | hours |
| 2 | R8 | Agentless numbers plus a second scaffold for the top models | days |
| 2 | R9 | Same-scaffold run on SWE-Bench Verified | ~1 day |
| 2 | R10 | Annotation statistics (annotators, hours, attrition per stage) plus a leakage audit | low if logs exist |
| 2 | R11 | Augmentation ablation: statement only / +requirements / +interface | 2 extra runs × 2–3 models |
| 2 | R14 | Human agreement on ~100 trajectories; a non-participant judge; bucket mapping | ~1 day annotation |
| 2 | R19 | Document the evaluation service, versioning and held-out release policy | writing / policy |
| 3 | R1, R16, R22, R24 | Fix text/table numbers, per-repo counts, citation keys, Table 3 bases and labels | minutes–hours |
| 3 | R7 | Binomial or bootstrap CIs; seeds for the top models | cheap / ~3× compute |
| 3 | R12, R13 | Position against SWE-bench, Verified and time-based contamination-free benchmarks; add a comparison table and the missing related work | writing |
| 3 | R15, R18 | Statistics for all three sets; prompt, decoding, model IDs, cost | cheap |
| 3 | R17, R21 | Describe every filter and its attrition; resolve rate by LOC and file bins | cheap |
| 3 | R20 | Add stronger open-weight models | days of GPU time |
| 3 | R23 | Discuss repository selection, conflict of interest and contributor consent | writing |

**Missing references suggested (R13).** SWE-Lancer (Miserendino et al., 2025); SWE-Gym (Pan et al., "Training Software Engineering Agents and Verifiers with SWE-Gym", 2024/2025); LiveCodeBench (Jain et al., 2024; ICLR 2025); SWE-smith (Yang et al., 2025); METR's "Measuring AI Ability to Complete Long Tasks" (Kwa et al., 2025), relevant to the "hours to days" framing; SWE-PolyBench (2025) [verify].

---

## 8. Integrity signals and limitations

**Integrity signals.**
- `integrity_scan.py --redact` found no reviewer-directed text or hidden characters. No out-of-place instructions were seen while reading; App. B.1 is the authors' own judge prompt, which is data.
- Anonymization: the blinded text still names, in Section 4.1, the organization whose employees founded some of the source startups. Data and code links were removed. This is a matter for the venue's anonymity policy and does not change any score.

**Limitations.**
- Figures 1–4 were not available. Claims that depend on them, notably A9, R21 and the Figure 3 distributions, were judged from captions and text only.
- No supplement or released data was inspected.
- The literature check did not run (no network). R12's "first" claim and the prior-work statements in R13 and T3 rest on memory, and uncertain items are marked [verify].
- The six reviewer types share one context and one reading, so their agreement is not independent confirmation.
