# Peer Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | benchmark |
| Field, sub-area | machine learning, LLM agents for software engineering (code-generation evaluation) |
| Task | adapted from "LLMs, NLP" (no software-engineering-agent row in `references/task_neighbors.md`): repository-level issue-resolution benchmark for coding agents |
| Neighboring fields | evaluation science / NLP benchmarking (from file); LLM data contamination and memorization (from file, "contamination"); LLM agents and tool use (generated); empirical software engineering / mining software repositories (generated); code-generation benchmarks and program synthesis (generated); datasets-and-benchmarks documentation and data governance (generated) |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | significance 21%, experimental validation 19%, technical rigor 17%, clarity 15%, reproducibility 14%, novelty 10%, ethics 4% (`aggregate_scores.py ratio --paper-type benchmark --venue iclr`) |
| Literature check | off (no network); novelty reasons that rest on memory are marked [verify] where unsure |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Input note: the review uses text extracted from the PDF. Figures 1-4 were not available, so I judged figure-dependent claims (Figure 3 distributions, Figure 4 per-language and per-repository results) from their captions and the text only.

---

## 1. Paper memory

**Claims.**
- C1: SWE-Bench Pro is contamination-resistant by design: GPL/copyleft public and held-out sets, a private commercial set bought from startups, and three access tiers (Abstract; §1 contribution 1; §3.1; §3.3).
- C2: the tasks are challenging, long-horizon, enterprise-level and diverse. That means 1,865 problems from 41 repositories, an average of 107.4 LOC over 4.1 files, at least 10 lines per task, and 50-100 instances per repository (Abstract; §1 contribution 2; §3.1).
- C3: a three-stage human augmentation and verification workflow (problem statement, requirements, interface; test verification) ensures that tasks can be resolved (Abstract; §1 contribution 3; §3.2; §4).
- C4: frontier models resolve fewer than 25% of tasks: GPT-5 23.3% on the public set and at most 17.8% on the commercial set. That is far below the >70% reported on SWE-Bench Verified, and the public-commercial gap reflects enterprise complexity (Abstract; §1; Tables 1-2; §5).
- C5: an LLM-judge failure analysis separates frontier-model failures (semantic, wrong solution) from small-model failures (syntax, tool use, context management) (§1; §6.2; Table 3).
- C6: difficulty varies by language and repository, and frontier models are more consistent across them (§6.1; Figure 4).

**Setup facts.**
- Subsets: public 731 / 11 repos, commercial 276 / 18 repos, held-out 858 / 12 repos (§3.3; Abstract).
- Languages: Python, JavaScript, TypeScript, Go (§3.2 Environments; §7.1).
- Scaffold: SWE-Agent, a single basic prompt, a 200-turn cap, native tool use where possible and "syntax parsing" for open-weight models; models at their latest versions as of 2025-09-18; vLLM on 8×H100 (§5).
- Metric: Pass@1 as the resolve rate (§5).
- The evaluated setting includes the problem statement, requirements and interface (§5 Issue Ambiguity).
- Seeds or number of runs: not stated (single run implied). Temperature, reasoning effort, context limits, cost caps: not stated.
- Tests: fail2pass and pass2pass, each run 3 times to remove flaky tests, with human filtering of broad or irrelevant fail2pass tests (§3.2; §4.3).
- Human annotation: annotator count, expertise, agreement and funnel counts not stated.
- Failure judge: GPT-5, last 20 turns of each unresolved trajectory, one category per instance (§6.2; App. B.1).
- Commit dates of the tasks: not stated.
- Licence of the release: public set "with copy-left license" (§3.3); terms for the commercial code not stated.

**Headline numbers.**
- Public set (Table 1): GPT-5 23.3; Opus 4.1 22.7; Sonnet 4 17.6; Gemini 2.5 Pro 13.5; SWE-Smith-32B 6.8; GPT-4o 4.9; Qwen-3 32B 3.4.
- Commercial set (Table 2): Opus 4.1 17.8; GPT-5 14.9; Gemini 10.1; Sonnet 4 9.1; GPT-4o 3.6.
- SWE-Bench Verified ">70%" (§1, ref [15], Figure 2 caption; not measured here).
- 107.4 LOC across 4.1 files on average (§1).

**Appendix.**
- App. A gives one full example: problem statement, requirements, interface, and a rewritten issue (Table 4).
- App. B gives the judge prompt.
- There are no extra experiments.

**Could not be read.** Figures 1-4: images not available, only captions. Table 1 and Table 2 were merged side by side in extraction, but each row was legible.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | Timely need: SWE-Bench Verified is near saturation (>70% reported), so a harder issue-resolution benchmark with large headroom (best 23.3% Pass@1) restores signal for agent research. | §1 ("over 70% pass rate on SWE-Bench-Verified"); Table 1 (GPT-5 23.3) | strong | R6 (size of the gap is not like-for-like) |
| A2 | novelty | Contamination-mitigation design that is new for SWE benchmarks: copyleft (GPL) repositories for the public/held-out sets plus purchased private startup codebases, with three access tiers (public, held-out, commercial). | §1 contribution 1; §3.1; §3.3 | moderate | R4 not upheld as measured resistance |
| A3 | significance | Tasks are substantially larger than SWE-Bench Verified: trivial edits excluded, reference patches average 107.4 LOC across 4.1 files, every task at least 10 changed lines. | §1 ("107.4 lines of code across 4.1 files"); Figure 3 caption | strong | R9, R25 (how many tasks are large) |
| A4 | experimental_validation | Scale and spread: 1,865 problems from 41 repositories (11+12+18), four languages, per-repository cap of 100 instances to limit single-repo overfitting. | Abstract; §1; §3.3 (731+276+858=1,865) | moderate | R3 (commercial per-repo counts) |
| A5 | technical_rigor | Human augmentation adds a problem statement, test-grounded requirements and an explicit interface, removing a known false-negative mode (wrong class/function names) and under-specification of commit-derived tasks. | §3.2 Interface; §4.2; App. A.1-A.3; Table 4 | moderate | R11, R12, R10 |
| A6 | technical_rigor | Test reliability controls: tests run 3 times and flaky ones dropped; annotators filter fail2pass tests that are too broad or irrelevant; problems dropped when no valid test remains. | §3.2 Tests ("we run each set of tests 3 times"); §4.3 | moderate | R12 |
| A7 | reproducibility | Public set (731 instances) released; containerized per-language environments; one scaffold (SWE-Agent), one prompt, 200-turn cap, model versions dated; judge prompt given in full. | §3.3; §3.2 Environments; §5 Evaluation settings; App. B.1 | moderate | R20, R11 |
| A8 | experimental_validation | Evaluates a broad model set under one scaffold: frontier closed models, open-weight models and a SWE-trajectory fine-tuned model (SWE-Smith-32B), on both public and commercial sets. | Table 1; Table 2; §5 | moderate | R8, R7 |
| A9 | significance | Diagnostic analyses beyond a single number: per-language and per-repository resolve rates and an LLM-judge failure taxonomy contrasting frontier (semantic/wrong solution) and small models (syntax, tool use, context). | §6.1; Figure 4; §6.2; Table 3 | weak | R1, R14 not upheld |
| A10 | significance | A private held-out set from separate repositories is kept to detect future overfitting to the public set. | §3.3 Held-Out; §1 | moderate | R18 |
| A11 | ethics | Limitations are stated honestly: language coverage, issue-resolution scope only, dependence on tests, and over-prescriptive augmentation. | §7.1 | moderate | - |
| A12 | clarity | Task format is concrete and easy to follow, with a full worked example of problem statement, requirements and interface, and a before/after rewrite. | §3.2; App. A.1-A.3; Table 4 | moderate | R22, R28 |
| A13 | significance | The commercial set gives enterprise codebases no public benchmark has, and the paper reports results on it (best 17.8%). | §3.3 Commercial; Table 2 | moderate | R17, R3 |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | experimental_validation | Table 3 counts are inconsistent with the evaluated set: per-model failure counts exceed both N=731 and the number of unresolved instances, so the unit of the failure analysis is unclear and its percentages cannot be interpreted. | Table 3; §6.2 "we programmatically filter to only unresolved instances". Recomputed: Opus 681+239=920, Gemini 491+424=915, GPT-4o 569+220=789, Qwen 386+406=792 > 731; expected unresolved for Opus 731x(1-0.227)=565. | error | major | State the unit (runs x instances?), recompute Table 3 on unresolved public instances only; hours. |
| R2 | clarity | Results text contradicts Table 1: Sonnet 4 given as 16.3% (Table 1: 17.6) and GPT-4o as 3.9% (Table 1: 4.9). | §5 Results "also achieves a 16.3% resolve rate"; "at 3.4% and 3.9% respectively" vs Table 1. Cross-referenced. | error | minor | Correct the text; minutes. |
| R3 | technical_rigor | The commercial set cannot satisfy the stated per-repository range: 276 problems over 18 repositories is about 15 per repository, against 'between 50 and 100 instances' per repository and 'a similar number of problems per repo'. | §1 "Each repository contributes between 50 and 100 instances, with a strict cap of 100 instances"; §3.3 (276 problems), Abstract (18 repositories). Recomputed 276/18=15.3. | error | major | Report per-repository counts for every subset and restrict the claim to the public/held-out sets; hours. |
| R4 | technical_rigor | The headline 'contamination-resistant' claim is argued, not measured: no memorization probe, no public vs held-out comparison (the held-out set exists), and the GPL 'legal barrier' argument is asserted without evidence that copyleft code is absent from training corpora. | §3.1 "the nature of these licenses creates legal barriers to their inclusion in commercial training corpora"; Abstract "contamination-resistant testbed"; no contamination experiment in §5-§6 (text search). | gap | major | Report public vs held-out resolve rates for 2-3 models, add a memorization/completion probe on public repos (e.g., in the style of Golchin & Surdeanu 2024); about one GPU-week plus API cost. |
| R5 | ethics | Evaluating closed API models on the private commercial and held-out sets sends that code to model providers; the paper does not discuss how this affects long-term contamination resistance or the data-use terms agreed with the startups. | §5 (closed models evaluated on commercial set, Table 2); §3.3; no discussion found. | gap | minor | Describe API data-retention settings and the agreements; a paragraph. |
| R6 | experimental_validation | The 'substantially more challenging' comparison is not like-for-like: the >70% figure on SWE-Bench Verified comes from other reports and tuned scaffolds, while SWE-Bench Pro numbers use SWE-Agent with a basic prompt and 200 turns; the same harness is never run on Verified. | §1 "substantially lower than the >70% Pass@1 reported on SWE-Bench Verified [15]"; Figure 2 caption; §5. Text search: no Verified run. | gap | major | Run the same SWE-Agent configuration on SWE-Bench Verified for the Table 1 models; one to two days of API compute. |
| R7 | experimental_validation | Single run, no variance or confidence intervals; with N=731 the 95% interval is about ±3.1 pp, so GPT-5 vs Opus 4.1 (23.3 vs 22.7) and the commercial ranking (17.8 vs 14.9, ±4.5 pp at N=276) are not separable, yet the abstract states a ranking. | Table 1; Table 2; Abstract "GPT-5 achieving the highest score to date at 23.3%". Binomial SE recomputed. | gap | major | Report 3 runs or bootstrap CIs; soften ranking language; one to three API-days. |
| R8 | experimental_validation | Harness parity and settings are under-specified: open-weight models use 'syntax parsing' for tools while closed models use native tool calls; GPT-5 fails to submit on 63.1% of failures, 97.6% of them tool-use, which suggests a harness incompatibility; temperature, reasoning effort, context limits and cost caps are not stated. | §5 "for open-weight models, we use syntax parsing to enable tool-use"; Table 3 GPT-5 row; §6.2 "GPT-5 indicates potential differences in effective-tool-use". | gap | major | Report all decoding/agent settings; diagnose GPT-5 non-submissions; rerun with a fixed tool interface; days. |
| R9 | significance | The 'long-horizon', 'hours to days' framing is not operationalized: no human solve-time is measured, and the evaluated setting supplies requirements and interfaces that name files, functions and expected strings, turning much of the search into specified implementation. | Abstract "may require hours to days for a professional software engineer to complete"; §5 Issue Ambiguity; App. A.2-A.3. Text search: no time measurement. | judgment | major | Measure expert solve time on a sample, or retitle/reframe; report task-length statistics (median LOC, files); weeks for a time study. |
| R10 | experimental_validation | No ablation of the augmentation: models are never evaluated without requirements and/or interface, so how much of the task the augmentation gives away, and how hard the underlying issues are, is unknown. | §3.1 "the setting without requirements is potentially interesting"; §5 Issue Ambiguity (only the fully specified setting). | gap | major | Evaluate 2-3 models with statement-only and statement+requirements; one to two API-days. |
| R11 | reproducibility | The human pipeline is undocumented: no annotator count, qualifications, time per task, agreement, QA protocol, or funnel counts (candidate commit pairs to final tasks) for the 'three-stage' process. | §1 "We design a novel three-stage human-in-the-loop process"; §4.2-§4.3. Text search: no annotator statistics. | gap | major | Add a datasheet-style section with funnel counts, annotator details and agreement; a few days of writing. |
| R12 | technical_rigor | Resolvability is asserted but not validated: no human solves a sample, and no failed model patches are audited for false negatives, although tests are acknowledged as an imperfect verifier. | Abstract "All tasks are human-verified and augmented with sufficient context to ensure resolvability."; §7.1 Dependency on Test Suite. | gap | major | Have engineers solve a random sample from the statement+requirements alone; audit ~100 failed patches; one to two weeks. |
| R13 | technical_rigor | Figure 1 states 'difficulty filtering', but the text describes only a size filter; if tasks were filtered by model success, the low resolve rates are partly by construction. | Figure 1 caption "We design the dataset with contamination resistance, difficulty filtering, and human augmentation/verification."; §4. | question | major | State every filter, and whether any model was used to select tasks; minutes. |
| R14 | experimental_validation | The failure-mode analysis has weak validity: GPT-5 judges its own trajectories, only the last 20 turns are read, the human agreement behind the 20-turn choice is not reported (the 87% figure is borrowed from [22]), the prompt's 10 categories do not map stated onto Table 3's 9 columns, 'Other' is 63.4% of Sonnet's submitted failures, and the prompt hard-codes 'Final state: Failed (no successful patch generated)' even for submitted patches. | §6.2 "utilizing GPT-5 as the judge", "We determined 20 turns to have the highest correspondence with human validations"; Table 3; App. B.1. | gap | major | Report human agreement on a labelled sample, use a judge not under evaluation (or several), give the category mapping; days. |
| R15 | clarity | Analysis text misreads Table 3: Qwen's tool-use share is 349/792=44.1%, not 42.0%, and it is not the highest (GPT-5: 446/724=61.6%). | §6.2 "exhibits the highest tool error rate (42.0%)"; Table 3 Qwen and GPT-5 rows. Recomputed. | error | minor | Correct the sentence; minutes. |
| R16 | novelty | The delta over prior SWE benchmarks is a refinement: the commit-pair sourcing, fail2pass/pass2pass tests and human verification follow SWE-bench/SWE-Bench Verified; contamination-resistant and multi-language SWE benchmarks (SWE-bench-Live [25], Multi-SWE-bench [24], SWE-rebench, SWE-Lancer, LiveCodeBench) are not compared, and 'the first to systematically apply such a methodology' is not supported. | §1 "to the best of our knowledge, this work is the first to systematically apply such a methodology"; §2.1 (no comparison table); §4.1. Literature check offline: memory, [verify]. | judgment | major | Add a comparison table vs prior SWE benchmarks (size, languages, LOC, contamination strategy) and narrow the 'first' claim; a day. |
| R17 | experimental_validation | The public-commercial gap is attributed to enterprise complexity without controls: the commercial set has no reported statistics (Figure 3 covers the public set only), languages or task sizes may differ, and Table 2 omits two Table 1 models. | §1 "underscoring the greater complexity of enterprise codebases"; §5; Table 2 vs Table 1; Figure 3 caption. | gap | major | Report commercial-set statistics and a size/language-matched comparison; a day. |
| R18 | reproducibility | The held-out set is undescribed: no statistics or results, so 'mirroring the public set' cannot be checked. | §3.3 "We hold out a set of 858 problems mirroring the public set but use a separate set of repositories." | gap | minor | Report summary statistics and one model's score; hours. |
| R19 | significance | Language coverage is narrow (Python, JS, TS, Go), weaker than prior multi-language SWE benchmarks, which limits the 'diverse' claim. | §7.1 Limited Language Coverage; §2.1 Multi-SWE-bench covers seven languages. | judgment | minor | Narrow the diversity wording or add languages; months for new data. |
| R20 | reproducibility | Commercial results cannot be reproduced by others by design; environments 'will be released'; agent configuration files are not given. | §3.2 "All environments will be released as pre-built docker images"; §3.3 Commercial. | gap | minor | Release images and configs; offer a hosted evaluation for the commercial set. |
| R21 | clarity | Citation errors: SWE-Bench is cited as [25] (SWE-bench goes live!) in the abstract; 'social media posts [1, 25]' cites two arXiv papers; SWE-Bench Verified is cited as [13] (original SWE-bench); SWE-Smith is evaluated but not cited. | Abstract "builds upon the best practices of SWE-Bench [25]"; §1 "social media posts [1, 25]"; §1 "SWE-Bench Verified [13]"; §5 SWE-Smith; References. Cross-referenced. | error | minor | Fix the references; minutes. |
| R22 | clarity | Presentation is thin for a main-track paper: short analysis, typos ("models current perform better"), inconsistent names ("DeepSeek Qwen-3 32B", 'private set' for held-out), Figure 4 caption refers to file/LOC bins it does not describe, and Table 3 columns are not defined. | Figure 4 caption; §5 "earlier generation models like DeepSeek Qwen-3 32B"; §5 "we keep the private set held-out"; Table 3. | gap | minor | Copy-edit; define columns; a day. |
| R23 | ethics | Data-governance details are missing: terms under which startup code was purchased and may be evaluated, contributor consent, annotator compensation, GPL compliance for the redistributed public set. | §3.1 "where we contacted the company and purchased their engineering repos"; §4.1. Text search: no ethics statement. | gap | minor | Add an ethics/data statement; hours. |
| R24 | ethics | Anonymization: the text names the organization whose employees founded some source startups, which identifies the authors in a double-blind venue. Flagged for the editor; not a scientific weakness. | §4.1 "startups founded by Scale employees" | gap | minor | Remove identifying text; minutes. |
| R25 | clarity | Only the mean patch size is given; with a 10-line minimum and only 'over 100 tasks' above 100 lines, the distribution is heavy-tailed and the median would say how many tasks are actually large. | §1 "Every problem involves at least 10 lines of change, and over 100 tasks demand more than 100 lines of modification."; "107.4 lines" | question | minor | Report median and quartiles of LOC and files per subset; minutes. |
| R26 | experimental_validation | Agentless is dismissed as producing 'low evaluation scores' without numbers, so scaffold sensitivity of the benchmark is not shown. | §5 Scaffold "Agentless has difficulty in multi-file editing, thus, produces low evaluation scores" | gap | minor | Report the Agentless numbers; hours. |
| R27 | technical_rigor | No date-based contamination check: commit dates of public and commercial tasks are not reported against model training cutoffs, so even a simple temporal check of the contamination claim is impossible. *(added in T4 review)* | §4.1 (commit-pair sourcing, no dates); §5 "latest versions as of September 18th, 2025". Text search: no commit dates. | gap | major | Report commit-date distributions and resolve rate before/after each model's cutoff; hours. |
| R28 | clarity | Description of the requirements contradicts the example: §4.2 and A.2 say requirements do not prescribe implementation or leak solutions, yet the A.2 example fixes file paths, a function name and a tuple's contents. *(found by P8)* | §4.2 "does not prescribe how the solution should be implemented"; App. A.2 "Requirements never include specific code implementation and don’t leak solutions." vs A.2 example (`stage_from_google_books`, `STAGED_SOURCES`). | judgment | minor | Describe precisely what requirements may specify; quantify leakage via R10; hours. |

### Answered

- Tasks may be trivial one-to-two-line edits as in SWE-Bench Verified: answered at §1 "Every problem involves at least 10 lines of change"; §3.1.
- Flaky tests could make outcomes noisy: answered at §3.2 Tests (run 3 times, inconsistent tests filtered); §4.3 Environment verification.
- A few repositories could dominate the public set: answered at §1 cap of 100 per repository; §3.3 731 over 11 repositories = 66.5 average.
- Correct patches could fail on naming mismatches with the tests: answered at §3.2 Interface; App. A.3.
- Analysis on the commercial set could leak its content: answered at §5 "For all analysis, we use the public set to avoid potential leakage with the commercial set.".
- Subset sizes may not add up to the stated totals: answered at §3.3 and Abstract: 731+276+858=1,865 problems and 11+12+18=41 repositories (recomputed).

### Aspect coverage

- Significance: A1, A3, A9, A10, A13; R9, R19.
- Experimental validation: A4, A8; R1, R6, R7, R8, R10, R14, R17, R26.
- Technical rigor: A5, A6; R3, R4, R12, R13, R27.
- Clarity: A12; R2, R15, R21, R22, R25, R28.
- Reproducibility: A7; R11, R18, R20.
- Novelty: A2; R16.
- Ethics: A11; R5, R23, R24.
- Omission sweep (`references/error_audit.md` §4):
  - split and tuning: no tuning, so not applicable;
  - seeds and variance: not stated after search (R7);
  - baseline settings: partly stated (§5), with gaps (R8);
  - hyperparameters: not stated (R8);
  - compute: hardware stated (§5), API cost not stated;
  - licence, consent and personal data: partly stated (R23);
  - failure cases and limitations: present (§6.2, §7.1);
  - code and data: public set released, environments promised (R20).
- CV checklist: not applicable (no vision content). VLM/LLM evaluation items from `references/statistical_reporting_standards.md` were applied: model versions are present; prompts are partly given; variance is missing (R7); LLM-judge validation is missing (R14); contamination analysis is missing (R4, R27).

### Pairs

- A2 ↔ R4, R27, R5: the contamination-resistance claim (C1).
- A3 ↔ R9, R25, R10: the long-horizon, challenging claim (C2).
- A4 ↔ R3, R19: diversity and per-repository balance (C2).
- A13 ↔ R17: the enterprise-complexity interpretation of the commercial gap.
- A5 ↔ R11, R12, R28: the human-augmentation and resolvability claim (C3).
- A1 ↔ R6: the size of the gap with SWE-Bench Verified (C4).
- A8 ↔ R7, R8, R26: the model comparison (C4).
- A9 ↔ R1, R14, R15: the failure-mode findings (C5).
- A10 ↔ R18: the held-out set.
- A7 ↔ R20, R11: reproducibility.

---

## 3. Reorganized ledger and probes

No duplicates were merged. Swing is high when a reason is open and bears on a central claim, or has a major worst case, or decides a pair.

### By claim

**C1: contamination resistance**
- A2 (checked), A10 (checked), R4 (checked by P5, high swing; decides A2 ↔ R4), R27 (checked, added in T4 review), R5 (checked, low swing), R18 (checked, low swing).

**C2: challenging, long-horizon, enterprise-level, diverse**
- A3 (checked), A4 (checked, weakened by P3), A13 (checked).
- R9 (checked by P8, high swing), R10 (checked by P8, high swing), R3 (checked by P3, high swing).
- R13 (open after P9, unsettled question, capped at minor), R17 (checked, medium swing), R19 (checked, low), R25 (open question, low).

**C3: human augmentation ensures resolvability**
- A5 (checked), A6 (checked).
- R11 (checked by P10, high swing), R12 (checked by P10, high swing), R28 (checked, found by P8, low).

**C4: frontier models below 25%, far below Verified**
- A1 (checked), A8 (checked).
- R6 (checked by P6, high swing; decides A1 ↔ R6), R7 (checked by P7, medium), R8 (checked; P13 after reviews), R2 (checked by P2, low), R26 (checked, low).

**C5: failure modes**
- A9 (checked, weakened by P1).
- R1 (checked by P1, high swing; decides A9 ↔ R1), R14 (checked by P11, high swing), R15 (checked by P4, low).

**General**
- A7, A11, A12 (checked).
- R16 (checked against the paper's own text by P12; the external delta rests on memory), R20, R21, R22, R23, R24 (checked by reading in place).

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R1 | Do Table 3 counts equal the unresolved public-set instances for each model? | recompute: sum Submitted+Not-Submitted per row; compare with 731 x (1 - Table 1 rate) | confirmed (Table 3; Table 1; §6.2) | R1 question -> error (checked); A9 moderate -> weak |
| P2 | R2 | Do the resolve rates in §5 Results match Table 1? | cross-reference §5 text vs Table 1 | confirmed (§5 Results; Table 1) | R2 open -> error (checked) |
| P3 | R3, A4 | Can every subset satisfy 50-100 instances per repository? | recompute 731/11, 858/12, 276/18 | confirmed (§1; §3.1; §3.3; Abstract) | R3 open -> error (checked); A4 strong -> moderate |
| P4 | R15 | Is Qwen's tool-use share 42.0% and the highest in Table 3? | recompute tool-use / (Submitted+Not-Submitted) per row | confirmed (§6.2; Table 3) | R15 open -> error (checked) |
| P5 | R4, A2 | Does the paper measure contamination anywhere (memorization probe, held-out vs public scores, dates)? | re-read §3-§7 and appendix; text search for held-out results and contamination tests | confirmed (§3.1; §3.3; §5; §6) | R4 open -> checked (gap confirmed); A2 holds as design, not as measured resistance |
| P6 | R6, A1 | Is SWE-Bench Verified run under the same scaffold and settings? | text search for Verified; trace the >70% figure to [15] | confirmed (§1; Figure 2 caption; §5; ref [15]) | R6 open -> checked (no same-harness run); A1 holds for headroom, not for the size of the gap |
| P7 | R7 | Are the reported rankings separable given N? | binomial standard errors: N=731, p=0.233 -> ±3.06 pp; N=276, p=0.178 -> ±4.51 pp | confirmed (Table 1; Table 2; Abstract) | R7 open -> checked |
| P8 | R9, R10, A3 | Does the paper measure human solve time or evaluate without requirements/interface? | re-read §3.1, §4.2, §5, §7.1, App. A.2-A.3 | confirmed (§3.1; §5 Issue Ambiguity; App. A.2) | R9, R10 open -> checked; new R28 (found by P8) |
| P9 | R13 | What is the 'difficulty filtering' named in the Figure 1 caption? | text search for difficulty/filter across all sections | unsettled (Figure 1 caption; §1; §4) | R13 stays question (open); capped at minor |
| P10 | R11, R12, A5 | Are annotator statistics, funnel counts, agreement or a human-solve check reported? | text search (annotator, agreement, verified, solve) and re-read §4 | confirmed (§1; §3.2; §4.2-§4.3) | R11, R12 open -> checked; A5 holds as design only |
| P11 | R14 | Is the judge validated on this data, and do its categories map onto Table 3? | re-read §6.2 and App. B.1; compare 10 prompt categories with 9 table columns | confirmed (§6.2; Table 3; App. B.1) | R14 open -> checked |
| P12 | R16 | Does the paper position itself against contamination-resistant and multi-language SWE benchmarks? | re-read §1-§2; literature check offline (memory, [verify]) | partly (§1; §2.1; refs [1], [24], [25]) | R16 open -> checked for the paper's own text; the external delta rests on memory |

Probe computations:
- **P1:** expected unresolved = 731 × (1 − rate): Opus 565, GPT-5 561, Sonnet 602, Gemini 632, GPT-4o 695, Qwen 706. Table 3 totals are 920, 724, 699, 915, 789 and 792. Every row exceeds its expected count, and four rows exceed 731 itself. The per-cell percentages are internally consistent (330/681 = 48.5%; 167/239 = 69.9%), and the §6.2 text uses the shares of the row total (330/920 = 35.9%). So the arithmetic inside the table is right, but its population does not match the stated one.
- **P3:** 731/11 = 66.5 and 858/12 = 71.5 are consistent with "50-100". 276/18 = 15.3 is not.
- **P4:** Qwen 349/792 = 44.1%; GPT-5 446/724 = 61.6%; Gemini 356/915 = 38.9% (text: 38.8%).
- **P7:** 95% binomial interval ±3.06 pp at p = 0.233, N = 731; ±4.51 pp at p = 0.178, N = 276.
- **P8:** A.2 requires that "a function named `stage_from_google_books` must attempt to fetch and stage metadata". That contradicts "Requirements never include specific code implementation and don’t leak solutions" (A.2), so R28 was added.

---

## 4. Reviewer roster

Aspects at ≥ 12% (significance, experimental validation, technical rigor, clarity, reproducibility) each have a type. Novelty (10%) gets its own type because the paper raises a distinct question there: its delta over prior SWE benchmarks. Ethics (4%) has no type; its reasons sit in T6's and T4's "Weighs most", and the script renormalizes its share away.

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 SWE-agent and code-LLM benchmark specialist | significance | the task: repository-level SWE-agent evaluation | builds and evaluates SWE agents on SWE-bench-style suites | headroom, realism, adoption-ready resources | benchmarks that saturate or are contaminated; harness artifacts | A1, A2, A3, A4, A5, A8, A10, A13, A9; R4, R6, R7, R8, R9, R10, R12, R13, R16, R17, R19, R1, R14, R5 | high |
| T2 Evaluation and measurement methodologist | experimental_validation | evaluation science / NLP benchmarking | benchmark validity, statistics, LLM-as-judge validation | construct validity, like-for-like comparisons, uncertainty | unvalidated judges, single runs, unmatched comparisons | A3, A6, A8, A9, A1; R1, R4, R6, R7, R8, R10, R12, R14, R17, R2, R13, R15, R18, R26 | high |
| T3 Empirical software-engineering researcher | technical_rigor | empirical SE / mining software repositories | commit mining, test adequacy, human-annotated SE datasets | documented pipelines, funnel counts, test oracles | test-as-oracle false negatives, undocumented annotation, size claims without distributions | A5, A6, A3, A12; R11, R12, R3, R9, R10, R1, R4, R25, R28, R2, R22, R26 | medium |
| T4 Data-contamination and training-data researcher | technical_rigor | LLM data contamination and memorization | memorization probes, temporal splits, corpus licensing | measured, not argued, contamination resistance | licence-based arguments; private data sent to APIs | A2, A10, A13; R4, R27, R5, R18, R16, R6, R13, R3, R21 | medium |
| T5 LLM-agent researcher, general ICLR reviewer | clarity | LLM agents and tool use | agent scaffolds and tool-use evaluation | clear claims matched by evidence, consistent numbers | text/table mismatches, overclaimed framing | A12, A1, A9; R1, R9, R6, R14, R2, R15, R21, R22, R24, R28, R25 | high |
| T6 Open-science and dataset-documentation reviewer | reproducibility | datasets-and-benchmarks documentation / data governance | datasheets, release practice, data licensing | releasable artifacts, documented provenance and consent | private-only results, promised-but-unreleased artifacts | A7, A12, A11, A10; R11, R8, R20, R23, R18, R12, R24, R5 | medium |
| T7 Code-generation benchmark and program-synthesis researcher | novelty | code-generation benchmarks / program synthesis | HumanEval-to-SWE-bench lineage, live and multilingual benchmarks | a clear conceptual delta over prior benchmarks | re-runs of SWE-bench recipes framed as new; "first" claims | A2, A4, A13, A3, A1; R16, R9, R4, R19, R6, R21, R17 | medium |

---

## 5. Reviews

### T1: SWE-agent and code-LLM benchmark specialist (significance; the task)

**Reading of the ledger.**
- Holds:
  - A1: Verified is near saturation and a 23.3% ceiling restores signal.
  - A3: 107.4 LOC over 4.1 files is a real step up from one-to-two-line fixes.
  - A2: copyleft plus purchased code is a sensible design, whatever its measured effect.
  - A4, A5, A8, A10, A13: useful resource properties.
- Discounts: A9, because the failure taxonomy rests on Table 3, whose counts do not add up (R1).
- Grades:
  - R4: major. Contamination resistance is the benchmark's selling point and it is not measured.
  - R8: minor. I assumed GPT-5's non-submissions reflect the model under a standard scaffold (updated after P13: minor → major).
  - R6: minor. The headroom exists either way; only its size is uncertain.
  - R7: minor. A single run is normal for agent leaderboards at this N.
  - R9: minor. Multi-file, 100-line tasks are long enough for today's agents.
  - R10: minor.
  - R12: minor.
  - R13: minor (unsettled question).
  - R16: minor.
  - R17: minor.
  - R19: minor.
  - R1: minor for me as a resource reviewer.
  - R14: minor.
  - R5: minor.

**Contribution check.**
1. What does a reader learn? That frontier agents resolve under a quarter of large, multi-file, test-verified tasks. That is mostly a leaderboard, though A13 adds the commercial-set gap.
2. Does the setting support the framing? Only partly. Task size supports "challenging", but "hours to days" is unmeasured (R9).
3. Conceptual delta or refinement? Mostly a refinement of the SWE-bench recipe. The sourcing strategy (A2) is the conceptual part.
4. Would it transfer? Plausibly yes for practitioners on Python/JS/TS/Go codebases.

**Opinion.** As someone who uses these suites daily, I want this benchmark to exist. SWE-Bench Verified no longer separates frontier agents. A suite whose tasks average over a hundred changed lines, with a private commercial tier and a held-out tier, is the resource the community needs next (A1, A3, A13). The data-sourcing idea is simple but fills a gap no current issue-resolution benchmark covers (A2). My hesitation is that the paper sells "contamination-resistant" without one measurement (R4), even though the held-out set needed for a basic check exists. The analysis sections are thin, and some of their numbers do not reconcile (R1), but for me those are secondary to the artifact. Numbers showing that public and held-out scores agree would move me to a clear accept. Evidence that public scores are inflated would move me down.

Decisive: A1 (strong), A3 (strong), A2 (moderate, holds as design), R4 (major)

**Scores.**
- Pool position 66 (basis: A1, A3, A2 against R4).
- Dimensions: Technical Rigor 58, Clarity 60, Novelty 60, Significance 72, Experimental Validation 58, Reproducibility 64, Ethics 62.
- Overall 4. Confidence 4.

### T2: Evaluation and measurement methodologist (experimental_validation; evaluation science)

**Reading of the ledger.**
- Holds:
  - A3: task size is a measured property.
  - A6: flaky-test filtering is sound.
  - A8: the model coverage is broad.
- Discounts:
  - A9: the taxonomy's population is wrong (R1) and the judge is unvalidated (R14).
  - A1: the headroom is real, but its contrast with Verified is unmatched (R6).
- Grades:
  - R1: major. The failure analysis covers more instances than exist.
  - R6: major. The central contrast with Verified ("substantially lower than the >70% Pass@1") is not like-for-like.
  - R7: major. Rankings within ±3 to ±4.5 pp are stated as findings.
  - R8: major. A harness issue may drive GPT-5's 63% non-submissions.
  - R10: major. Without the ablation, the construct being measured is unclear.
  - R12: major. Resolvability is asserted, not measured.
  - R14: major. The judge evaluates its own model's trajectories without reported agreement.
  - R17: major. A causal reading of the commercial gap without controls.
  - R4: major.
  - R2: minor.
  - R13: minor (unsettled question).
  - R15: minor.
  - R18: minor.
  - R26: minor.

**Contribution check.**
1. What does a reader learn? A ranking and a failure taxonomy whose numbers do not reconcile. The insight is weak.
2. Does the setting support the framing? Not for "long-horizon" (R9) or "contamination-resistant" (R4).
3. Conceptual delta or refinement? A refinement of SWE-bench (R16).
4. Would it transfer? Likely, but limited by the fully specified setting (R10).

**Opinion.** A benchmark paper's claims are measurement claims, and this paper validates few of them. The comparison with SWE-Bench Verified, which motivates the whole paper, sets a number reported elsewhere under other scaffolds against a single configuration here (R6). No interval accompanies results whose ranking the abstract highlights (R7). The failure analysis, the paper's only analytic contribution, reports more failures per model than there are unresolved tasks: Opus has 920 against an expected 565 (R1). It is also labelled by GPT-5, one of the models judged, with no agreement figure on this data (R14). Resolvability, the property that makes a low score meaningful, is never checked by a human solve or a false-negative audit (R12). Each item is fixable in a revision. Together they mean that today the paper establishes a dataset, not a measurement. A same-harness Verified run, CIs, a corrected Table 3 and a solvability audit would move me to borderline accept.

Decisive: R6 (major), R14 (major), R1 (major), R12 (major), A3 (holds)

**Scores.**
- Pool position 40 (basis: R6, R14, R1, R12).
- Dimensions: Technical Rigor 48, Clarity 54, Novelty 55, Significance 62, Experimental Validation 42, Reproducibility 58, Ethics 60.
- Overall 3. Confidence 4.

### T3: Empirical software-engineering researcher (technical_rigor; empirical SE / mining software repositories)

**Reading of the ledger.**
- Holds:
  - A5: requirements and interfaces address a known false-negative problem.
  - A6: repeated test runs are standard good practice.
  - A3: the size statistics are as stated.
- Discounts: A12. The example is clear, but it reveals how prescriptive the requirements are (R28).
- Grades:
  - R11: major. A human-curated dataset with no annotator statistics or funnel counts cannot be assessed.
  - R12: major. Tests are an imperfect oracle (§7.1), and no false-negative audit is reported.
  - R3: major. The commercial set contradicts the per-repository design claim.
  - R9: major. File paths and function names in the requirements shorten the horizon.
  - R10: major.
  - R1: major.
  - R4: minor (outside my expertise).
  - R25: minor (question).
  - R28: minor.
  - R2: minor.
  - R22: minor.
  - R26: minor.

**Contribution check.**
1. What does a reader learn? Mostly a leaderboard.
2. Does the setting support the framing? Partly (R9).
3. Conceptual delta or refinement? The commit-pair mining, fail2pass and pass2pass are the SWE-bench recipe, so a refinement (R16).
4. Would it transfer? Plausibly, to the four languages tested.

**Opinion.** From an empirical-SE standpoint, the dataset construction is the contribution, and it is described at the level of intent rather than procedure. We are told there is a "three-stage human-in-the-loop process". We are not told how many engineers took part, how long a task took, how disagreements were resolved, or how many commit pairs survived each filter (R11). The statement that every task is resolvable rests on that process alone, with no human solve or audit of failing patches (R12). The A.2 example shows requirements that name exact functions and data structures. That conflicts with the claim that requirements do not prescribe implementation (R28), and it weakens the long-horizon framing (R9). The commercial set's 276 tasks over 18 repositories, about 15 each, contradicts the stated 50-100 per repository (R3). A datasheet with funnel counts and a solvability audit would change my view substantially.

Decisive: R11 (major), R12 (major), R9 (major), R3 (major), A6 (holds)

**Scores.**
- Pool position 44 (basis: R11, R12, R9, R3).
- Dimensions: Technical Rigor 46, Clarity 55, Novelty 54, Significance 63, Experimental Validation 50, Reproducibility 54, Ethics 58.
- Overall 3. Confidence 4.

### T4: Data-contamination and training-data researcher (technical_rigor; LLM data contamination)

**New reason.** Added R27 to the ledger before using it: there is no date-based contamination check, because commit dates are not reported against model cutoffs (§4.1, §5; text search found no commit dates).

**Reading of the ledger.**
- Holds:
  - A2: licence-based and private sourcing is a reasonable prior.
  - A10: a held-out tier is the right instrument.
  - A13: private commercial code is the strongest protection.
- Grades:
  - R4: major. "contamination-resistant" is the title-level claim, and the paper runs none of the standard tests.
  - R27: major. Even a temporal check is impossible from what is reported.
  - R5: minor. API evaluation of private sets erodes protection over time and deserves a paragraph.
  - R18: minor.
  - R16: minor.
  - R6: minor.
  - R13: minor (unsettled question).
  - R3: minor.
  - R21: minor.

**Contribution check.**
1. What does a reader learn? A plausible design, but not whether it works.
2. Does the setting support the framing? The "contamination-resistant" claim is unsupported by measurement.
3. Conceptual delta or refinement? Licence-based selection is a modest conceptual idea. Private held-out sets are standard practice in evaluation.
4. Would it transfer? Yes, if validated.

**Opinion.** The argument in §3.1, that copyleft licences create "legal barriers" to inclusion in training corpora, is a hypothesis about lab behaviour. It is not a property of the data. Copyleft code is public on GitHub and appears in general web crawls. The paper's own public release now makes the public set available to future crawls. The design gives the authors the means to test the claim: compare public and held-out scores (A10), probe models for memorization of public-repo files, or split by commit date against each model's cutoff (R27). None of this is reported (R4). I also want a note on what happens to the private sets once closed APIs have processed them (R5). I like the design and would support the paper if one of these checks showed the public set is not inflated.

Decisive: R4 (major), R27 (major), A2 (holds as design), A10 (holds)

**Scores.**
- Pool position 45 (basis: R4, R27 against A2, A10).
- Dimensions: Technical Rigor 45, Clarity 56, Novelty 58, Significance 64, Experimental Validation 50, Reproducibility 55, Ethics 56.
- Overall 3. Confidence 4.

### T5: LLM-agent researcher, general ICLR reviewer (clarity; LLM agents and tool use)

**Reading of the ledger.**
- Holds:
  - A12: the task format and example are clear.
  - A1: the motivation is clear and timely.
- Discounts: A9. The failure findings are stated more confidently than the numbers allow (R1, R15).
- Grades:
  - R1: major. A reader cannot reconcile Table 3 with Table 1.
  - R14: major. The taxonomy columns are undefined and the Other bucket dominates one model.
  - R9: major. The title promises "long-horizon" and the evaluated setting is fully specified.
  - R6: major. Figure 2's headline contrast (>70% vs <25%) compares unlike settings.
  - R2: minor.
  - R15: minor.
  - R21: minor.
  - R22: minor.
  - R24: minor (editorial).
  - R28: minor.
  - R25: minor (question).

**Contribution check.**
1. What does a reader learn? The headline number, but little about why agents fail that survives scrutiny (R1, R14).
2. Does the setting support the framing? The title's "long-horizon" is not backed (R9).
3. Conceptual delta or refinement? A refinement.
4. Would it transfer? Partly.

**Opinion.** The paper is easy to read at the level of motivation and task format (A12). It is hard to trust at the level of results, because the text and tables disagree. §5 reports Sonnet 4 at 16.3% and GPT-4o at 3.9%, while Table 1 gives 17.6% and 4.9% (R2). §6.2 calls Qwen's 42.0% the highest tool-error rate, but Table 3 implies 44.1% for Qwen and 61.6% for GPT-5 (R15). Table 3's totals exceed the evaluated set (R1). The columns of Table 3 are never defined against the judge's ten categories (R14), and the citations for SWE-Bench and SWE-Bench Verified point to the wrong entries (R21). The framing also overreaches: the paper is titled "long-horizon", yet it evaluates only the setting where requirements and interfaces are handed to the agent (R9). These are revision-level fixes, but at ICLR the paper I read is not yet clear enough to accept.

Decisive: R1 (major), R14 (major), R9 (major), R2 (minor), A12 (holds)

**Scores.**
- Pool position 48 (basis: R1, R14, R9).
- Dimensions: Technical Rigor 50, Clarity 50, Novelty 56, Significance 64, Experimental Validation 50, Reproducibility 58, Ethics 60.
- Overall 3. Confidence 4.

### T6: Open-science and dataset-documentation reviewer (reproducibility; datasets and benchmarks documentation)

**Reading of the ledger.**
- Holds:
  - A7: the public set is released and the judge prompt is given.
  - A12: the example instance documents the format.
  - A11: limitations are honestly stated.
- Discounts: A10. The held-out set's value to others depends on the authors running it, and nothing about it is reported (R18).
- Grades:
  - R11: major. No datasheet-level documentation of curation for a human-curated benchmark.
  - R8: major. The agent and decoding settings needed to reproduce Table 1 are missing.
  - R20: minor. Environments are promised, not released, and private-set results are unreproducible by design, which is acceptable if disclosed.
  - R23: minor.
  - R18: minor.
  - R12: minor.
  - R24: minor (editorial).
  - R5: minor.

**Contribution check.**
1. What does a reader learn? A usable public suite.
2. Does the setting support the framing? Partly.
3. Conceptual delta or refinement? A refinement with a new sourcing policy.
4. Would it transfer? Yes, to anyone running SWE-Agent-style harnesses.

**Opinion.** The public release is a real plus (A7). The paper is upfront that commercial and held-out results cannot be reproduced externally, which I accept for a benchmark with a private tier. What I cannot accept for a resource paper is how little the curation is documented (R11). There are no funnel counts, no annotator profile or compensation, no agreement figures, and no account of the terms under which startup code was bought and sent to third-party APIs (R23, R5). Reproducing Table 1 also needs temperature, reasoning effort, context and cost limits, which are not given (R8). A datasheet and a configuration release would raise my scores considerably. As submitted, the paper is below the documentation bar I expect for a benchmark at a main-track venue.

Decisive: R11 (major), R8 (major), A7 (holds)

**Scores.**
- Pool position 50 (basis: R11, R8 against A7).
- Dimensions: Technical Rigor 54, Clarity 56, Novelty 56, Significance 65, Experimental Validation 52, Reproducibility 50, Ethics 54.
- Overall 3. Confidence 4.

### T7: Code-generation benchmark and program-synthesis researcher (novelty; code-generation benchmarks)

**Reading of the ledger.**
- Holds:
  - A2: licence-based sourcing and a purchased private tier are new for issue-resolution benchmarks.
  - A4: the scale is solid.
  - A13: the commercial tier is distinctive.
  - A3: the tasks are larger than prior suites.
- Discounts: A1. Headroom alone is not novelty, since many concurrent suites also have it.
- Grades:
  - R16: major. The recipe is SWE-bench's, the contamination-resistant and multilingual alternatives are not compared, and "first to systematically apply" is unsupported.
  - R9: major. The framing goes beyond what is new.
  - R4: major. The novel part, contamination resistance, is the untested part.
  - R19: minor.
  - R6: minor.
  - R21: minor.
  - R17: minor.

**Contribution check.**
1. What does a reader learn? That bigger, private-sourced tasks are harder. That is expected.
2. Does the setting support the framing? Partly (R9).
3. Conceptual delta or refinement? It extends SWE-bench/SWE-Bench Verified (commit-pair mining, fail2pass and pass2pass, human verification) with a new sourcing policy. Moderate novelty.
4. Would it transfer? Yes.

It fails questions 1 and 3 in part, and no accept reason shows a specific new insight, so I place it in the lower half.

**Opinion.** The benchmark sits in a crowded line: SWE-bench, SWE-Bench Verified, Multi-SWE-bench [24], SWE-bench-Live [25], and other live or freelance-derived suites such as SWE-rebench [verify], SWE-Lancer, and LiveCodeBench for function-level code. The paper cites some of these but never compares itself on size, languages, patch size or contamination strategy. The claim to be "the first to systematically apply such a methodology" goes unexamined (R16). What is actually new is the sourcing policy (A2), and that is exactly what the paper does not test (R4). The remaining construction follows SWE-bench closely. A comparison table and a measured contamination result would make the novelty case. Without them, this is a solid dataset paper with moderate novelty.

Decisive: R16 (major), R4 (major), A2 (holds), R9 (major)

**Scores.**
- Pool position 47 (basis: R16, R4, R9 against A2).
- Dimensions: Technical Rigor 54, Clarity 58, Novelty 50, Significance 64, Experimental Validation 52, Reproducibility 58, Ethics 60.
- Overall 3. Confidence 4.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P13 | T1 (minor) vs T2, T6 (major) on R8 | Does the paper show that GPT-5's non-submissions (63.1% of its failures, 97.6% of them tool-use) reflect the model and not the harness? | Confirmed, the paper does not show it. §5 states only "We use the same prompt for all models" and native tool use where possible. §6.2 says only "GPT-5 indicates potential differences in effective-tool-use", with no analysis of the 446 tool-use failures (Table 3). T1's assumption that the harness had been checked has no support in the paper. | T1: R8 updated after P13, minor → major. R8 is not among T1's decisive items, so T1's scores are unchanged. |

Value splits stay as they are: R9 (T1 minor vs T3, T5, T7 major), R4 (T3 minor vs T1, T2, T4, T7 major), R6 (T1, T4, T7 minor vs T2, T5 major), R12 (T1, T6 minor vs T2, T3 major).

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 SWE-agent benchmark specialist | significance | 0.215 | 66 | 4 | 4 |
| T2 Evaluation methodologist | experimental_validation | 0.195 | 40 | 3 | 4 |
| T3 Empirical SE researcher | technical_rigor | 0.088 | 44 | 3 | 4 |
| T4 Data-contamination researcher | technical_rigor | 0.088 | 45 | 3 | 4 |
| T5 LLM-agent researcher | clarity | 0.161 | 48 | 3 | 4 |
| T6 Open-science reviewer | reproducibility | 0.146 | 50 | 3 | 4 |
| T7 Code-benchmark researcher | novelty | 0.107 | 47 | 3 | 4 |

- **Aspect-weighted rating:** 3.215 → **final rating 3 (Borderline Reject)**. In ICLR 2026 terms that is **4 on {0, 2, 4, 6, 8, 10}** (5 on the earlier {1, 3, 5, 6, 8, 10} scale), with sub-scores Soundness 2, Presentation 2, Contribution 2. The ICLR scale's verification status is *secondary*: recent forms use this scale, so verify it against the current form.
- Weighted pool position 49.9; plain mean 3.14; spread 1 (4 − 3).
- Uncovered aspects and warnings: ethics (4%) has no type and is renormalized away; the script reported no warnings.
- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

**Paper type**: benchmark  
**Weights**: Technical Rigor 0.15, Clarity & Presentation 0.15, Novelty & Originality 0.10, Significance & Impact 0.20, Experimental Validation 0.20, Reproducibility 0.15, Ethical Compliance 0.05

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| T1 (SWE-agent and code-LLM benchmark specialist) | 4 | 0.85 | 1.00 | 14% |
| T2 (Evaluation and measurement methodologist) | 4 | 0.85 | 1.00 | 14% |
| T3 (Empirical software-engineering researcher (mining repositories, test adequacy)) | 4 | 0.85 | 1.00 | 14% |
| T4 (Data-contamination and training-data researcher) | 4 | 0.85 | 1.00 | 14% |
| T5 (LLM-agent researcher, general ICLR reviewer) | 4 | 0.85 | 1.00 | 14% |
| T6 (Open-science and dataset-documentation reviewer) | 4 | 0.85 | 1.00 | 14% |
| T7 (Code-generation benchmark and program-synthesis researcher) | 4 | 0.85 | 1.00 | 14% |

*No EIC quality weights given yet: the EIC assessment uses confidence only. Add `eic_weight` (0.5-1.5) per reviewer after the EIC's meta-review.*

#### Official scores and EIC assessment

| Dimension | T1 (SWE-agent and code-LLM benchmark specialist) | T2 (Evaluation and measurement methodologist) | T3 (Empirical software-engineering researcher (mining repositories, test adequacy)) | T4 (Data-contamination and training-data researcher) | T5 (LLM-agent researcher, general ICLR reviewer) | T6 (Open-science and dataset-documentation reviewer) | T7 (Code-generation benchmark and program-synthesis researcher) | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 58 | 48 | 46 | 45 | 50 | 54 | 54 | 50.7 | 50.7 | 13 |
| Clarity & Presentation | 60 | 54 | 55 | 56 | 50 | 56 | 58 | 55.6 | 55.6 | 10 |
| Novelty & Originality | 60 | 55 | 54 | 58 | 56 | 56 | 50 | 55.6 | 55.6 | 10 |
| Significance & Impact | 72 | 62 | 63 | 64 | 64 | 65 | 64 | 64.9 | 64.9 | 10 |
| Experimental Validation | 58 | 42 | 50 | 50 | 50 | 52 | 52 | 50.6 | 50.6 | 16 |
| Reproducibility | 64 | 58 | 54 | 55 | 58 | 50 | 58 | 56.7 | 56.7 | 14 |
| Ethical Compliance | 62 | 60 | 58 | 56 | 60 | 54 | 60 | 58.6 | 58.6 | 8 |
| **Composite** | 62.4 | 53.3 | 54.1 | 54.8 | 55.1 | 55.7 | 56.7 | **56.0** | **56.0** | |
| Pool position (P%) | 66 | 40 | 44 | 45 | 48 | 50 | 47 | | | |

#### Ratings (the decision's starting point)

**Official reviewer ratings (Overall 1-6)**: T1 (SWE-agent and code-LLM benchmark specialist) 4, T2 (Evaluation and measurement methodologist) 3, T3 (Empirical software-engineering researcher (mining repositories, test adequacy)) 3, T4 (Data-contamination and training-data researcher) 3, T5 (LLM-agent researcher, general ICLR reviewer) 3, T6 (Open-science and dataset-documentation reviewer) 3, T7 (Code-generation benchmark and program-synthesis researcher) 3 → official mean **3.14**  
**EIC-weighted rating** (internal): **3.14** (+0.00 vs. official) → starting point **3 (Borderline Reject)**

⚠ = spread > 20 points: discuss this disagreement in the decision.

**Composite cross-check (0-100)**: official 56.0 → 3 · EIC-weighted 56.0 → 3 (+0.0 vs. official)  
**Decision ceiling**: none (no upheld DA-CRITICAL issue). The EIC's decision starts from the EIC-weighted rating and may depart from it in either direction, with a written reason.
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (SWE-agent and code-LLM benchmark specialist) | significance | 21% | 0.215 |
| T2 (Evaluation and measurement methodologist) | experimental_validation | 19% | 0.195 |
| T3 (Empirical software-engineering researcher (mining repositories, test adequacy)) | technical_rigor | 17% | 0.088 |
| T4 (Data-contamination and training-data researcher) | technical_rigor | 17% | 0.088 |
| T5 (LLM-agent researcher, general ICLR reviewer) | clarity | 15% | 0.161 |
| T6 (Open-science and dataset-documentation reviewer) | reproducibility | 14% | 0.146 |
| T7 (Code-generation benchmark and program-synthesis researcher) | novelty | 10% | 0.107 |

**Final rating (aspect-weighted mean)**: **3.21** → **3 (Borderline Reject)** · plain mean 3.14 · weighted pool position 49.9
### Cross-Venue Outlook

| Venue | Venue-weighted composite | Bar offset | Venue shift | Band → with DA cap | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|---|
| ICLR (2026) | 56.0 | +0 | +0 | 3 → 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) | Soundness 2, Presentation 2, Contribution 2 | secondary |

Emphasis weights are this skill's heuristics, not official venue weights. Scale status: official / confirmed / secondary / assumed / unpublished (see references/venue_profiles.md). Upheld DA-CRITICAL caps apply to every venue.

- **ICLR**: Soundness/Presentation/Contribution 1-4 and Confidence 1-5 are long-standing. Overall rating reported as {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}. Both are shown.

</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| A1 | 4 of 7 | T1 held, T2 discounted, T5 held, T7 discounted |
| A2 | 3 of 7 | T1 held, T4 held, T7 held |
| A3 | 4 of 7 | T1 held, T2 held, T3 held, T7 held |
| A4 | 2 of 7 | T1 held, T7 held |
| A5 | 2 of 7 | T1 held, T3 held |
| A6 | 2 of 7 | T2 held, T3 held |
| A7 | 1 of 7 | T6 held |
| A8 | 2 of 7 | T1 held, T2 held |
| A9 | 3 of 7 | T1 discounted, T2 discounted, T5 discounted |
| A10 | 3 of 7 | T1 held, T4 held, T6 discounted |
| A11 | 1 of 7 | T6 held |
| A12 | 3 of 7 | T3 discounted, T5 held, T6 held |
| A13 | 3 of 7 | T1 held, T4 held, T7 held |
| R1 | 4 of 7 | T1 minor, T2 major, T3 major, T5 major |
| R2 | 3 of 7 | T2 minor, T3 minor, T5 minor |
| R3 | 2 of 7 | T3 major, T4 minor |
| R4 | 5 of 7 | T1 major, T2 major, T3 minor, T4 major, T7 major |
| R5 | 3 of 7 | T1 minor, T4 minor, T6 minor |
| R6 | 5 of 7 | T1 minor, T2 major, T4 minor, T5 major, T7 minor |
| R7 | 2 of 7 | T1 minor, T2 major |
| R8 | 3 of 7 | T1 major, T2 major, T6 major |
| R9 | 4 of 7 | T1 minor, T3 major, T5 major, T7 major |
| R10 | 3 of 7 | T1 minor, T2 major, T3 major |
| R11 | 2 of 7 | T3 major, T6 major |
| R12 | 4 of 7 | T1 minor, T2 major, T3 major, T6 minor |
| R13 | 3 of 7 | T1 minor, T2 minor, T4 minor |
| R14 | 3 of 7 | T1 minor, T2 major, T5 major |
| R15 | 2 of 7 | T2 minor, T5 minor |
| R16 | 3 of 7 | T1 minor, T4 minor, T7 major |
| R17 | 3 of 7 | T1 minor, T2 major, T7 minor |
| R18 | 3 of 7 | T2 minor, T4 minor, T6 minor |
| R19 | 2 of 7 | T1 minor, T7 minor |
| R20 | 1 of 7 | T6 minor |
| R21 | 3 of 7 | T4 minor, T5 minor, T7 minor |
| R22 | 2 of 7 | T3 minor, T5 minor |
| R23 | 1 of 7 | T6 minor |
| R24 | 2 of 7 | T5 minor, T6 minor |
| R25 | 2 of 7 | T3 minor, T5 minor |
| R26 | 2 of 7 | T2 minor, T3 minor |
| R27 | 1 of 7 | T4 major |
| R28 | 2 of 7 | T3 minor, T5 minor |

### Key strengths

- A3: much larger, multi-file tasks than SWE-Bench Verified (107.4 LOC over 4.1 files on average). Held by 4 of 7 types.
- A2: contamination-mitigation design built on copyleft and purchased private code with three access tiers. Held by 3 of 7 types.
- A1: restores headroom after SWE-Bench Verified saturation. Held by 2 of 7 and discounted by 2, who agree the headroom exists but not that its size relative to Verified is established.
- A13, A10: the commercial and held-out sets. Each held by 2-3 types.

### Top concerns (at most five)

1. **R4:** the contamination-resistance claim is argued from licensing, not measured. The held-out set exists but no public vs held-out comparison is reported (§3.1, §3.3, §5). Fix: report public vs held-out resolve rates for 2-3 models and a memorization probe on public repositories; about one GPU-week plus API cost. Graded major by 4 of 7 types.
2. **R1:** Table 3 failure counts exceed both N = 731 and each model's number of unresolved instances (Opus 920 vs 565 expected), so the failure analysis cannot be interpreted (Table 3, §6.2). Fix: state the unit and recompute on the unresolved public instances; hours. Major for 3 of 7.
3. **R8:** harness parity is not established. Open-weight models use parsed tool calls, GPT-5 fails to submit on 63.1% of its failures (97.6% tool-use), and decoding and agent settings are missing (§5, Table 3). Fix: report every setting, diagnose the GPT-5 non-submissions, rerun with a fixed tool interface; days. Major for 3 of 7 (one after P13).
4. **R9:** the long-horizon, hours-to-days framing is not operationalized. There is no solve-time measurement, and the evaluated setting supplies requirements and interfaces that name files and functions (Abstract, §5 Issue Ambiguity, App. A.2-A.3). Fix: measure expert solve time on a sample, or reframe; report median task size. Major for 3 of 7.
5. **R6:** the gap with SWE-Bench Verified compares a reported >70% under other scaffolds with this paper's single SWE-Agent configuration (§1, Figure 2 caption). Fix: run the same harness on Verified; one to two API-days. Major for 2 of 7.

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R4 | Measure contamination: public vs held-out resolve rates; memorization/completion probe on public repos; temporal analysis (see R27) | ~1 GPU-week + API |
| 2 | R1 | State the unit of Table 3; recompute on unresolved public instances | hours |
| 2 | R8 | Report temperature, reasoning effort, context and cost limits; diagnose GPT-5 non-submissions; unify the tool interface | days |
| 2 | R9 | Expert solve-time study on a sample, or narrow the long-horizon and hours-to-days wording; give median LOC and files | 1-3 weeks, or a rewrite |
| 2 | R6 | Run the identical SWE-Agent configuration on SWE-Bench Verified | 1-2 API-days |
| 2 | R10 | Ablate requirements and interface (statement-only; +requirements) for 2-3 models | 1-2 API-days |
| 2 | R12 | Human solves of a random sample; false-negative audit of ~100 failed patches | 1-2 weeks |
| 2 | R14 | Human-labelled validation of the judge on this data; a judge not under evaluation; category mapping | days |
| 2 | R11 | Datasheet: funnel counts, annotator profile, time, agreement, QA | days |
| 2 | R7 | 3 runs or bootstrap CIs; soften ranking language | 1-3 API-days |
| 2 | R17 | Commercial-set statistics; size/language-matched public vs commercial comparison | a day |
| 2 | R3 | Per-repository counts for all subsets; correct the 50-100 claim | hours |
| 2 | R27 | Commit-date distributions vs model cutoffs; before/after-cutoff resolve rates | hours |
| 2 | R16 | Comparison table vs prior SWE benchmarks; narrow the "first" claim | a day |
| 3 | R2, R15, R21, R22, R25, R28 | Fix text/table mismatches and citations; define Table 3 columns; report LOC median and quartiles; describe what requirements may specify | a day |
| 3 | R13 | State every task filter, and whether models were used to select tasks | minutes |
| 3 | R5, R23, R24 | Data-governance and API data-retention statement; remove identifying text | hours |
| 3 | R18, R20, R26 | Held-out statistics; release environments and configs; Agentless numbers | hours to days |
| 3 | R19 | Narrow the diversity wording, or add languages | wording now; months for data |

Priority 1 contains only R4: no reason was graded fatal, and R4 is the only one graded major by at least half of all types (4 of 7).

---

## 8. Integrity signals and limitations

- **Integrity signals:**
  - `integrity_scan.py` found no reviewer-directed text or hidden characters, and no out-of-place instructions turned up in reading.
  - Anonymization: §4.1 contains "startups founded by Scale employees", which names the submitting organization in a double-blind venue (R24). This is flagged for the editor as a policy matter and is not graded as a scientific weakness.
  - These signals never change a score.
- **Limitations:**
  - Figures 1-4 were not available, so claims about Figure 3 distributions and Figure 4 per-language and per-repository rates were judged from captions and text only.
  - The literature check did not run (no network). The novelty judgment R16 rests on memory, and recommended works are listed with [verify] where unsure: LiveCodeBench (Jain et al., 2024); SWE-Lancer (Miserendino et al., 2025); SWE-rebench (Badertdinov et al., 2025) [verify]; SWE-PolyBench (Rashid et al., 2025) [verify]; SWE-smith (Yang et al., 2025), which the paper evaluates but does not cite; memorization probes in the style of "Time Travel in LLMs: Tracing Data Contamination in Large Language Models" (Golchin and Surdeanu, ICLR 2024).
  - All seven types share one context, and their agreement is not independent confirmation.
  - The reviewing model recognized this paper from prior knowledge. The review uses only the manuscript, not anything about its later reception.
