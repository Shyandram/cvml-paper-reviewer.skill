# Simulated Peer Review — SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

*Full-mode simulation, target venue ICLR (2026 cycle). Date: 2026-11-05. The outcome is a simulation of how a careful panel might see this draft, not a prediction. Literature check: strict, cutoff 2025-09-24. All five reviewer passes were performed by one model in sequence and share one context (no independent agents). Figures were not available: figure-dependent claims are judged from captions and text only.*

---

# Phase 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? |
| Primary Discipline | Machine learning → evaluation of LLM coding agents (issue-resolution benchmarks) |
| Secondary Discipline(s) | Software engineering (mining repositories, test-based verification); data licensing and IP |
| Paper Type | Benchmark (dataset + evaluation of existing models); composite weights: benchmark |
| Core Technique(s) | Commit-pair task mining, human augmentation of task descriptions, containerised fail2pass/pass2pass evaluation, SWE-Agent scaffold, LLM-as-judge failure clustering |
| Target Venue | ICLR (stated by user); profile key `iclr` |
| Venue-Specific Notes | None (no ECCV/ACM MM/TPAMI rules). Public submissions and reviews; authors may upload a revised PDF during discussion |
| Paper Maturity | Submission-ready draft with evident gaps in documentation and in internal consistency of numbers |
| Ethics-Relevant Content | Purchased proprietary startup codebases (consent/licence scope, secrets/PII, code sent to third-party model APIs); copyleft-licensed public code; annotator labour (not described) |

### Claimed Contributions (as stated by the authors)
1. **C1** — A data-collection strategy to mitigate contamination: GPL/copyleft public repositories (public + held-out sets) and private commercial codebases (§1, §3.1, §4.1).
2. **C2** — Challenging, diverse, industrially relevant tasks: 1,865 problems, 41 repositories, multi-file, avg. 107.4 lines over 4.1 files (§1, §3.1, §3.3).
3. **C3** — A human-in-the-loop augmentation and verification workflow (problem statement, requirements, interface, test filtering) to ensure resolvability (§1, §3.2, §4.2–4.3).
4. **C4** — Evaluation: frontier models ≤23.3% (public, N=731) and ≤17.8% (commercial, N=276), plus an LLM-judge failure-mode analysis (§5, §6, Tables 1–3).

### Paper memory (shared factual record)
- **Splits:** public 731 (HuggingFace), commercial 276 (private, results only), held-out 858 (private, no results); 731+276+858 = 1,865 ✓; 11+18+12 = 41 repos ✓ (Abstract, §3.3).
- **Setup:** SWE-Agent scaffold only (Agentless tried, "low" scores, not reported, §5); max 200 turns; one shared basic prompt; open models served by vLLM on 8×H100; "latest versions as of September 18th, 2025" (§5). Number of runs/seeds, temperature, reasoning effort, context limit, cost: **not stated after search**.
- **Headline numbers:** GPT-5 23.3 / Opus 4.1 22.7 / Sonnet 4 17.6 / Gemini 2.5 Pro Preview 13.5 / SWE-Smith-32B 6.8 / GPT-4o 4.9 / Qwen3-32B 3.4 (Table 1); commercial Opus 17.8 / GPT-5 14.9 / Gemini 10.1 / Sonnet 9.1 / GPT-4o 3.6 (Table 2); failure clusters (Table 3).
- **Appendix adds:** one worked example (Open Library, A.1–A.3, Table 4 original-vs-rewritten statement) and the judge prompt (B.1). It does **not** add: repository list, per-repo/language counts, annotator statistics, inter-annotator agreement, human-time estimates, contamination probes.
- **Unverifiable:** Figures 1–4 (not available), data/code links (removed), the supplement (none referenced).
- **Integrity scan:** `integrity_scan.py` found no reviewer-directed text or hidden characters. No injection found.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Elena Marchetti-Voss, large public research university (Southern Europe)
- **Seniority / Expertise**: Senior faculty, area chair at ML venues / evaluation of foundation models, dataset and benchmark quality
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Wants every headline claim tied to a table; accepts ordinary weaknesses if the resource is clearly useful

### Reviewer 1 (Methodology): Dr. Anika Sundaram, industrial research lab (South Asia)
- **Seniority / Expertise**: Senior industry scientist / agent evaluation protocols, statistical reporting for LLM benchmarks
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every number; insists on confidence intervals and matched harnesses

### Reviewer 2 (Domain): Prof. Lars Eidevall, public university software-engineering and NLP group (Northern Europe)
- **Seniority / Expertise**: Senior faculty / code LLM benchmarks, issue-resolution literature, contamination studies
- **Review Focus**: Literature, positioning, domain contribution
- **Style**: Reads the closest prior abstracts before judging novelty

### Reviewer 3 (Perspective): Dr. Camila Restrepo-Fuentes, empirical software-engineering and technology-law group (Latin America)
- **Seniority / Expertise**: Mid-career / mining software repositories, open-source licensing, human–AI programming workflows
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive; asks what real engineering teams would do with the benchmark

### Reviewer 4 (Generalist): Dr. Hyun-woo Baek, industrial research lab (East Asia)
- **Seniority / Expertise**: Mid-career / LLM post-training and general ML evaluation
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs flaws against usefulness

### Devil's Advocate: Dr. Oluwaseun Adeyemi-Park, evaluation-methodology group, university (North America)
- **Seniority / Expertise**: Mid-career / benchmark validity, construct validity, causal inference for evaluation
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; asks whether the numbers mean what the title says

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1 — Independent Reviews

---

# Peer Review Report

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Reviewer: Dr. Anika Sundaram, Methodology Reviewer (industrial research lab, South Asia; fictional persona)
## Expertise: agent evaluation protocols; statistical reporting for LLM benchmarks
## Date: 2026-11-05

---

## Summary
The paper presents a benchmark of 1,865 issue-resolution tasks drawn from 41 repositories, split into a public set (731), a private commercial set (276) and a private held-out set (858). Tasks are mined from commit pairs, filtered to multi-file changes of at least 10 lines, rewritten by humans with requirements and interface specifications, and verified through fail2pass/pass2pass tests in Docker. Seven models are run under SWE-Agent. The best Pass@1 is 23.3% on the public set and 17.8% on the commercial set. A GPT-5 judge clusters failure trajectories.

---

## Strengths

### S1: Scale and a sound evaluation backbone
Containerised tasks with fail2pass and pass2pass tests, plus a 3× rerun to drop flaky tests (§3.2 Tests, §4.3), give an executable, automatically gradable benchmark of useful size (§3.3, 731 public tasks).

### S2: A tiered release design
Public, held-out and commercial subsets (§3.3) give a sensible structure for later overfitting checks, and the per-repository cap (§1) limits any single repository's weight.

### S3: Candid limitations on test dependence and prescriptiveness
§7.1 ("Dependency on Test Suite", "Reduction in Ambiguity") names the two main validity threats of the design, and the "no ambiguity" setting is stated explicitly (§5, Issue Ambiguity).

### S4: Open evaluation details for the judge
The full judge prompt is given (App. B.1), which makes the failure analysis at least inspectable.

---

## Weaknesses

### W1: Table 3 is internally inconsistent and the text misreads it (E1, MAJOR)
Row totals in Table 3 (Submitted + Not-Submitted) are 920 (Opus 4.1), 724 (GPT-5), 699 (Sonnet 4), 915 (Gemini 2.5), 789 (GPT-4o) and 792 (Qwen3-32B). The table is said to cover *unresolved* instances of the N=731 public set (§6.2: "filter to only unresolved instances"), so each row should total at most 731 minus resolved tasks (e.g., ≈565 for Opus at 22.7%, ≈561 for GPT-5 at 23.3%). Four of six rows exceed 731 outright. The text also states that Qwen3-32B "exhibits the highest tool error rate (42.0%)", but the table gives 349/792 = 44.1% for Qwen against 446/724 = 61.6% for GPT-5, so Qwen is not highest. The 17.0% "endless file reading" for Sonnet 4 is the "Stuck in Loop" column (119/699), not "Incorrect File" or a reading category.
- **Suggested Fix**: Explain what the denominators are (runs? multiple attempts? both sets?), correct the table or the text, and state the mapping from the ten judge categories in App. B.1 to the nine columns of Table 3. Cost: low (re-tabulate existing data).

### W2: Single run, single scaffold, no intervals, and rankings are within noise (MAJOR)
Results are one Pass@1 per model under one scaffold (§5), with no seeds, temperatures or reasoning-effort settings stated. With N=731, a 23.3% rate has a normal-approximation 95% CI of about ±3.1 pp, so GPT-5 (23.3) vs Opus 4.1 (22.7) is not a ranking. On the commercial set (N=276) the ±4.2–4.5 pp intervals contain the 2.9 pp gap between Opus (17.8) and GPT-5 (14.9), and the order flips between Table 1 and Table 2 without comment. The abstract nevertheless says GPT-5 achieves "the highest score to date".
- **Suggested Fix**: Report 95% CIs (paired bootstrap over tasks), at least 3 runs for the top models on the public set, and soften "highest score to date" to "highest among evaluated models". Cost: roughly 3 × 7 models × 731 tasks of agent rollouts, on the order of a few thousand GPU-/API-hours.

### W3: The headline numbers are confounded by harness failures (MAJOR)
Table 3 shows 63.1% of GPT-5 trajectories and 57.8% of Sonnet 4 trajectories end as "Not-Submitted", with 97.6% of GPT-5's non-submissions attributed to tool-use errors and 61.6% of Sonnet 4's to long-context overflow. GPT-4o's non-submissions are 100% tool-use. These point at scaffold–model mismatch (a 200-turn cap, no context management, a basic shared prompt, §5) as much as at capability. The paper says Agentless "has difficulty in multi-file editing" (§5) but shows no numbers, and uses no second harness (e.g., a model's native agent loop or another open scaffold).
- **Suggested Fix**: Report results under at least one additional scaffold, or show a harness-robustness ablation (turn cap, context truncation) for the top-3 models, and report the share of failures that are harness-caused. Cost: medium.

### W4: No evidence that the tasks are valid and resolvable beyond "human-verified" (MAJOR)
The abstract says all tasks are "human-verified and augmented with sufficient context to ensure resolvability", yet the paper reports no annotator count, training, time per task, inter-annotator agreement, funnel (candidates → kept at each stage, §4.1–4.3), second-pass audit, or solvability check by an independent human or a test-oracle run. Since requirements are written to match the tests (§4.2: "grounded in the gold patch and test expectations"), it is also unclear how many valid alternative solutions fail the tests, which §7.1 concedes.
- **Suggested Fix**: Add the filtering funnel, annotation protocol and agreement statistics; audit ~100 failing trajectories by hand for false negatives. Cost: medium (annotator time).

### W5: "Difficulty" and "long-horizon" claims are not measured (MAJOR)
The Abstract claims tasks that "may require hours to days for a professional software engineer", but no human time estimates are given. Figure 1's caption lists "difficulty filtering" among the design principles, yet §4 does not describe any difficulty filter beyond the 1–10-line exclusion in §1. The statement "over 100 tasks demand more than 100 lines" (§1) is compatible with a mean of 107.4 lines only if the distribution is heavy-tailed, and no median, percentiles or comparison with SWE-Bench Verified statistics (other than "161 out of 500" trivial tasks) are given. Without an ablation of the requirements/interface text (§3.1 says the no-requirements setting is "potentially interesting"), the 23% cannot be attributed to length or enterprise realism rather than to spec/test coupling.
- **Suggested Fix**: Add a statistics table against SWE-Bench Verified (lines, files, median), measured trajectory length (turns used vs. the 200 cap), a human-time sample, and a with/without-requirements ablation on a subset. Cost: low–medium.

### W6: Contamination resistance is asserted, not tested (see also DA-M1)
Resistance rests on the licence argument "the nature of these licenses creates legal barriers to their inclusion in commercial training corpora" (§3.1). No membership or memorisation probe, no comparison of pre- and post-cutoff commits, and no evidence about the held-out set is provided, and the held-out set has no reported results. For the commercial set, the proprietary models in Table 2 were presumably served through vendor APIs, which exposes the "private" code to those vendors (the paper does not say how it was run).
- **Suggested Fix**: Add a simple contamination probe (e.g., verbatim-completion/membership tests on gold patches; performance split by commit date relative to model cutoffs), report held-out results for at least two models, and state how commercial tasks were served. Cost: low–medium.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 3 vs §5/Table 1 (N=731) | "We use LLM-as-a-judge to classify failing trajectories into buckets" | Row totals 920, 724, 699, 915, 789, 792 vs ≤731 minus resolved | Recomputed from printed counts | High | MAJOR | Explain denominators or correct |
| ERR-2 | E1 | §5 Results vs Table 1 | "also achieves a 16.3% resolve rate" | Table 1 gives 17.6 for Sonnet 4 | Cross-referenced | High | MINOR | Fix text |
| ERR-3 | E1 | §5 Results vs Table 1 | "considerably lower performance at 3.4% and 3.9% respectively" | Table 1 gives 4.9 for GPT-4o | Cross-referenced | High | MINOR | Fix text |
| ERR-4 | E1/E5 | §6.2 vs Table 3 | "exhibits the highest tool error rate (42.0%)" | Table 3: Qwen 349/792 = 44.1%; GPT-5 446/724 = 61.6% | Recomputed | High | MAJOR | Correct claim |
| ERR-5 | E6 | §1 vs §3.1 vs §3.3 | "Each repository contributes between 50 and 100 instances" | 276/18 ≈ 15 average per commercial repo; §3.1 says "50-100+" while §1 says a "strict cap of 100" | Derived from §3.3 and Abstract counts | High | MINOR | State per-set counts |

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | contamination-resistant | Abstract, §1, §3.1 | Licence argument only | Unsupported (untested) |
| C2 | challenging, enterprise-level, long-horizon | Abstract, §1 | 107.4 lines / 4.1 files; ≤23.3% | Partially (difficulty shown, "long-horizon"/"enterprise" not measured) |
| C3 | verified, resolvable | Abstract, §4 | Process description; no agreement or audit | Partially |
| C4 | models ≤23.3%/≤17.8%; failure modes | §5–6 | Tables 1–3 | Partially (one run; Table 3 inconsistent) |

**Minor:** Fig. 4 caption mentions "10+ files and 500+ LOC" categories not discussed in §6.1; "DeepSeek Qwen-3 32B" (§5) mislabels Qwen3; `Table 4` is referenced before the appendix table appears.

### Protocol sweep
Searched for split/selection statements: no tuning of hyperparameters or selection on the reported tasks is described; "We determined 20 turns to have the highest correspondence with human validations" (§6.2) is a judge-configuration choice made against an unreported human sample. Not criterion-3 leakage (the benchmark is the evaluation target, not a trained model).

### Omission sweep
Splits: present (§3.3). Seeds/runs/variance: not stated after search. Baseline settings (model versions/prompts/decoding): partly (§5; no decoding, no reasoning effort). Compute: partly (hardware yes, cost no). Licence/consent: partly (copyleft rationale; no consent/licence statement for commercial data). Failure cases: present (§6.2). Code/data: public set on HuggingFace (link removed); Docker images "will be released".

---

## Missing References
*(Domain Reviewer's responsibility; none added here.)*

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Useful design but unsupported claims, an inconsistent Table 3, and no variance |
| Clarity | 2 | Readable, but key protocol details and denominators are missing |
| Significance | 3 | A harder, executable SWE benchmark is of clear community value |
| Originality | 2 | Incremental over issue-resolution benchmarks; licence/commercial angle is new |

---

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the resource is useful, but its central claims (contamination resistance, long-horizon difficulty, resolvability) are untested and Table 3 does not reconcile with N.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Sound executable pipeline, but untested central claims and internal numerical inconsistencies |
| Clarity & Presentation | 58 | Competent | Readable; table/text mismatches and missing denominators |
| Novelty & Originality | 52 | Developing | Mostly incremental on the SWE-bench family; copyleft+commercial split is the new element |
| Significance & Impact | 68 | Competent | Strong demand for post-saturation SWE benchmarks |
| Experimental Validation | 46 | Developing | One run, one scaffold, no intervals; harness failures dominate several rows |
| Reproducibility | 48 | Developing | Two of three subsets unreleased by design; images "will be released"; runs/decoding not specified |
| Ethical Compliance | 55 | Competent-low | Limitations section exists; purchased-code consent/licence and API exposure not discussed |

---

## Questions for Authors

1. What are the denominators in Table 3 (runs, attempts, or sets)? A reconciliation with N=731 would remove my main numerical concern.
2. How many candidates survived each stage in §4.1–4.3, and what was inter-annotator agreement? Reasonable agreement would raise my Technical Rigor score.
3. How do GPT-5 and Sonnet 4 perform if tool-use and context failures are mitigated (second scaffold or native harness)? A large change would lower my confidence in the ranking.
4. How were proprietary models run on the commercial set, and under what data-retention terms?
5. Does the held-out set show a similar ordering of models to the public set? Reported results would address the overfitting claim.

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially.
§7.1 is candid about languages, scope, test dependence and prescriptiveness, but it does not mention single-run variance, harness sensitivity, unverified contamination resistance, or the unreleased commercial and held-out sets.

---

## Ethics Review Flag

**No**: no flag, but the licence/consent scope for purchased codebases and the vendor-API exposure should be stated.

---

## Overall Score

**3**: A useful resource whose central claims and secondary analysis are not yet supported to the standard of an ICLR benchmark paper; fixable, but with several open items. Mapped from composite 54.1.

## Confidence

**4**: Read the full paper and recomputed the tables; figures unavailable.

---

# Peer Review Report

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Reviewer: Prof. Lars Eidevall, Domain Reviewer (public university SE/NLP group, Northern Europe; fictional persona)
## Expertise: code LLM benchmarks; issue-resolution literature; contamination
## Date: 2026-11-05

---

## Summary
The paper proposes a benchmark meant to succeed SWE-Bench Verified, mixing GPL-licensed public repositories with purchased private startup codebases. It argues that licensing and private data limit contamination, that multi-file, longer patches better reflect professional work, and that human-written requirements and interfaces keep tasks resolvable. It evaluates seven models and reports below 25% for all of them.

---

## Strengths

### S1: A well-timed response to saturation
The motivation (§1: SWE-Bench Verified above 70%, noted 161/500 trivial tasks) is concrete and matches where the field is moving; the benchmark targets a real gap in headroom.

### S2: A genuinely uncommon data-source strategy
Using strong-copyleft public repositories plus purchased private codebases (§3.1, §4.1) differs from the time-window freshness used by contamination-oriented code benchmarks, and a private commercial test set with public result reporting is rare in this literature.

### S3: A useful structural design for monitoring overfitting
The public/held-out pair drawn from separate repository sets (§3.3) is a sound way to detect overfitting if the held-out results are later released.

### S4: A broad related-work sweep of agents and benchmarks
§2 covers function-level, repository-level and agent literature in a short space and positions the work against SWE-bench, Multi-SWE-bench and SWE-bench Multimodal.

---

## Weaknesses

### W1: Positioning against the closest prior work is thin, and key neighbours are uncited (MAJOR)
The literature check (see addendum) found prior work that tackles the same sub-problems and is not cited: SWE-rebench (decontaminated, continuously refreshed SWE evaluation, peer-reviewed), SWE-Lancer (real-world freelance SWE tasks with triple-verified end-to-end tests and a private/public split), OmniGIRL and SWE-PolyBench (multilingual issue resolution). §2 lists benchmarks but never states what SWE-Bench Pro does that these do not, and "to the best of our knowledge, this work is the first to systematically apply such a methodology" (§1) is not argued against them. The licence-plus-private-data mechanism is plausibly new, so this is a positioning gap rather than a novelty failure.
- **Suggested Fix**: Add a comparison table (source, contamination mechanism, task size, verification, private split, languages) against SWE-bench Verified, SWE-rebench, SWE-Lancer, Multi-SWE-bench and SWE-bench-Live; narrow "first".

### W2: The copyleft contamination argument is a legal premise, not a finding (MAJOR)
§3.1 argues licence terms "create legal barriers to their inclusion in commercial training corpora". Copyleft repositories are publicly hosted and crawlable, and whether any given training pipeline filtered by licence is not known; issues and PR discussions, which §4.2 draws from, are public text. The domain standard for contamination claims is an empirical probe or a temporal split (the contamination-free code benchmarks that window by date, and decontamination analyses against SWE-bench Verified in the literature). The appendix's own example (Open Library, App. A.1.1) is a heavily visible open-source project.
- **Suggested Fix**: Add empirical evidence (verbatim completion, date-split performance, or a held-out vs public comparison) or recast the claim as "reduced risk" and drop "contamination-resistant" from the abstract.

### W3: The "enterprise-level" and "long-horizon" framing is not established by the data (MAJOR)
The commercial repositories come from startups (§3.1, §4.1), not from large enterprise systems, and their per-repo instance counts (≈15 on average, derived from 276/18) differ from the public sets. "Long-horizon" is not measured by trajectory length, time or step count. The citations used to motivate enterprise change size ([9, 16] in §1) concern code-change complexity and maintenance time, which do not directly support "multi-file modifications spanning hundreds of lines" in enterprise settings.
- **Suggested Fix**: Quantify horizon (turns, tool calls, median patch size) and say "startup codebases"; cite work that actually characterises enterprise change sizes or drop the claim.

### W4: The failure analysis is unvalidated and not positioned (MAJOR)
§6.2 relies on a GPT-5 judge looking at the last 20 turns, validated by an unreported human sample, and cites "87% alignment" from the SWE-agent paper [22] for a different taxonomy and judge. GPT-5 also judges its own failures. The LLM-as-judge literature recommends human agreement reporting and self-preference checks.
- **Suggested Fix**: Report a human-labelled sample (n≥100), per-category agreement, and a second judge family; cite judge-validation work.

### W5: Citation accuracy (E7, MINOR/MAJOR)
The abstract's "SWE-Bench [25]" points to SWE-bench Goes Live, not to SWE-bench ([13]). §1 calls [1, 25] "social media posts", but both entries are arXiv papers (SWE-bench+ and SWE-bench Goes Live). "SWE-Bench Verified [13]" in §1 cites the original SWE-bench rather than the Verified release ([15]). The §2.1 sentence "Da et al. [6] shows that these instances can be used for RL training" attributes to an Agent-RLVR paper a claim about Multi-SWE-bench instances.
- **Suggested Fix**: Audit the bibliography against in-text claims.

### Error Log (citations)
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-D1 | E7 | Abstract vs refs | "builds upon the best practices of SWE-Bench [25]" | [25] is "Swe-bench goes live!" | Cross-referenced with reference list | High | MINOR | Cite [13] |
| ERR-D2 | E7 | §1 vs refs | "recent works [5, 7, 21] and social media posts [1, 25]" | [1], [25] are arXiv papers | Cross-referenced | High | MINOR | Correct the description |
| ERR-D3 | E7 | §1 vs refs | "SWE-Bench-Verified [15]" / "SWE-Bench Verified [13]" | Two different citations for the same object ([13] is original SWE-bench) | Cross-referenced | High | MINOR | Use [15] consistently |

---

## Literature-check addendum

*Literature check run: strict mode, cutoff 2025-09-24, arXiv search only. 9 counted queries (claim 5 [C1, C2×2, C3, C4], baseline 1, expansion 2) of 12 allowed, plus `coverage`, `scout`, `similarity`, `novelty`, and 5 `verify` calls. Gaps left open: no prior work retained from 2022–2023 (field began in late 2023); search is arXiv-only, so non-arXiv venues are not covered. `benchmarks` returned no external benchmark tables (the paper has none of its own comparisons to baselines in other benchmarks).*

### Per-claim novelty
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|-----------------------------------------------|-----------|
| C1 contamination-resistant data collection | method | medium | SWE-rebench (3) https://arxiv.org/abs/2505.20411 · prior (peer-reviewed) · not cited | Prior work attacks contamination by freshness and decontamination; none of the abstracts read uses licence selection or purchased private data. Worth discussing: SWE-bench Goes Live (recent preprint, cited as [25]) |
| C2 challenging multi-file industrial tasks | resource | medium | SWE-Lancer (3) https://arxiv.org/abs/2502.12115 · prior (arXiv-only, 6+ months) · not cited | Real-world freelance tasks with end-to-end tests and a held-out split already exist; SWE-Bench Pro's size, multi-language and private repository sourcing differ |
| C3 human augmentation/verification | method | medium | SWE-Lancer (3); Multi-SWE-bench (recent preprint, cited as [24]) worth discussing | Verification by experts is common (SWE-bench Verified is the obvious precedent and is cited); requirement/interface augmentation tied to the tests is the specific addition |
| C4 results and failure analysis | result | high | SWE-Lancer (2) | New numbers on a new benchmark; failure-cluster analysis follows the SWE-agent style |

Script reading: "no central claim fully covered by prior work"; attribution (closest prior work): SWE-Lancer; most similar by text: SWE-rebench (cosine 0.30). **Text-overlap flag (for the editor):** the similarity script reports 5 shared verbatim 8-grams with the abstract of Multi-SWE-bench ("covering Java, TypeScript, JavaScript, Go, Rust, C, and C++"); this is the language list in a sentence that describes and cites Multi-SWE-bench [24] (§2.1), so it is explained by correct citation. No integrity concern raised.

### Novelty delta table
| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| Contamination-resistant benchmark | SWE-rebench (2025) | Continuously extracts fresh SWE tasks to decontaminate evaluation | Licence-based public set, purchased private set | No |
| Realistic, hard, real-world tasks with private evaluation | SWE-Lancer (2025) | Real freelance tasks, triple-verified end-to-end tests, public subset | Repo-level patches from commit history in 41 repos; multi-language; mixed access tiers | No |
| Multilingual repository-level issue tasks | OmniGIRL (ISSTA'25), SWE-bench-java | Multi-language, multi-domain issue resolution | Larger multi-file patches, private tiers | No |
| Expert verification of tasks | Multi-SWE-bench ("68 expert annotators", cited) | Annotator-verified instances | Added requirements/interface text | Cited, not differentiated |

### Baseline scout
No external benchmark with comparable published baseline numbers is used by the paper (its results are on its own benchmark), so there are no under-reported-baseline checks. For the paper's reference benchmark (SWE-bench Verified) the scout returned abstract-level mentions only and no comparable numeric rows; the ">70%" figure is cited to a blog [15] and is not reproduced under the paper's own scaffold (Figure 2 caption compares the two benchmarks under different conditions).

### Field snapshot (as of the cutoff)
Three to four years ago, function-level benchmarks (HumanEval, MBPP, APPS) dominated. Repository-level issue resolution (SWE-bench, 2023–24) became the central agent benchmark, followed by multilingual (Multi-SWE-bench, SWE-bench-java, OmniGIRL, SWE-PolyBench), multimodal, live/decontaminated (SWE-bench-Live, SWE-rebench) and economically grounded (SWE-Lancer) variants in 2025. Frontier models exceed 70% on SWE-bench Verified in vendor reports, so headroom, contamination and false-negative tests are the open problems. What counts as significant now: a new SWE benchmark is significant if it (a) retains clear headroom, (b) provides an evidence-based contamination or validity argument, and (c) is gradable reproducibly. A new large set with lower scores is expected; the discriminating contribution is validity evidence.

### Verified missing references
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Badertdinov et al. (2025), "SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents", arXiv:2505.20411 (verified, prior peer-reviewed label) | Same contamination goal and the same task type; must be contrasted with the licence-based strategy |
| Important | Miserendino et al. (2025), "SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?", arXiv:2502.12115 (verified, prior) | Real-world task benchmark with verified tests and a held-out split |
| Important | Rashid et al. (2025), "SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents", arXiv:2504.08703 (verified found on arXiv; publication status not confirmed, treat as `[verify]` for venue) | Multilingual repository-level benchmark with task complexity metrics |
| Important | Guo et al. (2025), "OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution", ISSTA 2025, arXiv:2505.04606 (verified, prior peer-reviewed) | Multilingual/multi-domain issue resolution; closest in language scope `[authors verify]` |
| Helpful | Jain et al. (2024), "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code", arXiv:2403.07974 (verified, prior) | Temporal-window contamination control, a baseline for the contamination discussion |
| Helpful | Zheng et al. (2023), "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023, arXiv:2306.05685 (verified) | Judge-validation and self-preference considerations for §6.2 |
| Helpful | Wang et al. (2025), "Are 'Solved Issues' in SWE-bench Really Solved Correctly? An Empirical Study", arXiv:2503.15223 (verified) | Evidence on false positives in test-based SWE verification; relevant to the test-dependence limitation |

*Author lists above are from memory and marked for confirmation; titles and links were verified by `related_search.py verify`.*

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound pipeline, but contamination claim untested |
| Clarity | 3 | Readable and organised |
| Significance | 3 | High demand for harder SWE benchmarks |
| Originality | 3 | New data strategy over a crowded benchmark family |

---

## Dimension Scores (0–100)

**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful, timely resource with a distinctive data-source idea, offset by thin positioning and untested contamination claims — typical of accepted benchmark papers with real weaknesses.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasonable construction; claims outrun evidence |
| Clarity & Presentation | 62 | Competent | Clear narrative; positioning thin |
| Novelty & Originality | 60 | Competent | Medium per-claim novelty (C1, C2, C3) |
| Significance & Impact | 72 | Competent-high | Fills headroom gap; likely to be used |
| Experimental Validation | 56 | Competent-low | Seven models, one harness |
| Reproducibility | 56 | Competent-low | Partial release by design |
| Ethical Compliance | 62 | Competent | Limitations candid; IP/consent unstated |

---

## Questions for Authors

1. What distinguishes SWE-Bench Pro from SWE-rebench and SWE-Lancer beyond licence-based sourcing? A table would raise my Novelty score.
2. Do you have any empirical contamination evidence (e.g., split by commit date vs. model cutoffs)? Results contradicting the premise would lower my score.
3. How were the 41 repositories chosen ("similarity to professional programs", §4.1), and which are they? A list would help judge diversity.

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially. §7 is honest, but it omits the contamination and external validity limitations of the licensing strategy.

---

## Ethics Review Flag

**No**.

---

## Overall Score

**4**: A timely, useful benchmark with a distinctive sourcing idea and medium per-claim novelty; positioning and contamination evidence need work but are fixable. Composite 61.4.

## Confidence

**4**: Familiar with the benchmark family; search was arXiv-only.

---

# Peer Review Report

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Reviewer: Dr. Camila Restrepo-Fuentes, Perspective Reviewer (empirical SE and technology-law group, Latin America; fictional persona)
## Expertise: mining software repositories; open-source licensing; human–AI programming workflows
## Date: 2026-11-05

---

## Summary
The paper introduces a benchmark of real-repository engineering tasks designed to remain hard for current coding agents. It mixes GPL repositories with purchased private startup code, rewrites issues into structured problem statements, requirements and interfaces, and reports that the best frontier models solve about a fifth of the tasks. A trajectory analysis suggests different failure profiles for larger and smaller models.

---

## Strengths

### S1: Bringing proprietary-style code into evaluation
The commercial set (§3.3, Table 2) addresses a real blind spot: public open-source repositories are unrepresentative of what companies write, and reporting results on private code is a thoughtful compromise between realism and secrecy.

### S2: Task framing close to industrial practice
Issue-style statements with templates preserved (App. A.1, "the same default issue templates") plus explicit requirements and interfaces (§3.2) mirror how teams specify work, and Table 4 shows concretely how a bare commit message becomes a usable issue.

### S3: Honest reflection on the realism–verifiability trade-off
§3.1 and §7.1 acknowledge that real tasks are under-specified and that augmentation may make problems "too prescriptive", which is the key tension in benchmarking SWE agents.

### S4: Failure analysis that connects to practitioners' concerns
The taxonomy (context overflow, tool-use, wrong solution; Table 3) maps onto what developers observe with agents, even though its numbers need repair.

---

## Weaknesses

### W1: "Enterprise-level" is asserted but the sources are startups and a "no-ambiguity" setup (MAJOR)
Practitioner tasks start from vague tickets, discussions and screenshots; §4.2 acknowledges this ("often including screenshots, links, or other media"), then removes it. Because requirements are "grounded on the unit tests" (§3.2) and name functions and routes (App. A.2), many tasks look like specification-to-code rather than issue triage. Startup repositories (§3.1) are typically small teams with short histories, not the "layered dependencies" of large enterprises (§4.1).
- **Suggested Fix**: Report a with/without-requirements split on a subset (the authors themselves suggest this, §3.1) and describe commercial repositories by size, age, team size and language.

### W2: The commercial set raises IP, consent and leakage questions the paper does not address (MAJOR)
The paper says it "contacted the company and purchased their engineering repos" (§3.1) while §4.1 says sources include "companies acquired through mergers and acquisitions, startups founded by Scale employees", and the Abstract says "formal partnership agreements". It is unclear what rights cover redistribution of results, derivative analysis, or sending code to third-party model APIs (Table 2 includes GPT-5, Claude and Gemini models) where retention and training policies differ. Code can also contain secrets or personal data. Selection of commercial partners by the benchmark creators is a potential bias that should be disclosed.
- **Suggested Fix**: State licence terms, consent scope, secret/PII scanning, how closed models were accessed (zero-retention endpoints?) and how partner repos were chosen.

### W3: The GPL premise mixes legal, technical and practical questions (MAJOR)
Copyleft status describes obligations on redistribution of derivatives, not technical access; an AI developer could include or exclude such code regardless. The paper offers no legal reference (§3.1) and does not say that "legal barriers" is a contested interpretation. Cross-disciplinary evidence from licence-compliance studies would help; as written, the argument is likely to be read as overreaching.
- **Suggested Fix**: Reframe as an assumption, cite licence analysis, and complement with empirical tests.

### W4: Evaluation assumes tests as the oracle of correctness
In SE research the oracle problem is well known: passing tests written for one implementation penalises valid alternatives, and the paper's own interface section (§3.2, App. A.3) shows tests tied to function names. The metric is thus construct-valid for "reproduce the reference patch's interface and behaviour", which is narrower than "professional-level" engineering (Abstract, Conclusion).
- **Suggested Fix**: Add a small human review of near-miss failures and, as future work, rubric or review-based grading (§7.2 gestures at this).

### W5: No discussion of broader impact
There is no statement on labour-market, automation or security implications of agents solving repository tasks, nor on the safety of executing agent-generated code in containers (§3.2 Environments). A short impact paragraph and a note on sandboxing would help.
- **Suggested Fix**: Add 1–2 paragraphs.

**Minor:** Provide per-repository metadata (domain, size, language) in the appendix.

---

## Missing References
*(None added; see Domain Reviewer.)* Cross-disciplinary lines of work worth citing without specific titles: software-testing literature on the test-oracle problem; psychometric (item-response) analyses of benchmark difficulty; empirical studies of open-source licence compliance in model training data `[verify]`.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Pipeline sensible; claims about enterprise realism overreach |
| Clarity | 3 | Clear |
| Significance | 3 | Practitioner-relevant benchmark (a 4 if validity evidence existed) |
| Originality | 3 | Commercial set is new |

---

## Dimension Scores (0–100)

**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: practical relevance and a private commercial split give clear community value, with ordinary weaknesses for this class of paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound design with gaps |
| Clarity & Presentation | 64 | Competent | Readable |
| Novelty & Originality | 62 | Competent | Commercial tier is new |
| Significance & Impact | 76 | Strong | Real need for post-saturation, private-code evaluation |
| Experimental Validation | 58 | Competent-low | Limited harness and no intervals |
| Reproducibility | 58 | Competent-low | Partial, intentional |
| Ethical Compliance | 58 | Competent-low | IP/consent/API exposure not discussed |

---

## Questions for Authors

1. Under what terms were closed-model APIs used on the commercial code? A zero-retention answer would raise my Ethics score.
2. How many commercial tasks have tests that depend on names given in the Interface field?
3. What do the commercial repositories look like (size, age, languages, team size)?
4. Would you release anonymised aggregate metadata for the held-out and commercial sets?

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially. §7.1 is candid on scope; missing are IP/consent, API exposure and impact.

---

## Ethics Review Flag

**No**: no flag. I recommend that the editor ask for an IP/consent statement for the purchased code and for how it was sent to model providers.

---

## Overall Score

**4**: A useful, practitioner-relevant benchmark with ordinary weaknesses for the genre; the commercial set and IP questions should be tightened. Composite 63.5.

## Confidence

**3**: Fairly confident on the SE and licensing aspects; less on ML benchmark norms.

---

# Peer Review Report

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Reviewer: Dr. Hyun-woo Baek, Generalist Reviewer (industrial research lab, East Asia; fictional persona)
## Expertise: LLM post-training; general ML evaluation
## Date: 2026-11-05

---

## Summary
SWE-Bench Pro is a new issue-resolution benchmark of 1,865 multi-file tasks from 41 repositories, with a public set, a private commercial set and a private held-out set. Tasks come with human-written requirements and interfaces and are verified with tests in containers. Under a single scaffold, no evaluated model exceeds 23.3% on the public set, and an LLM-judge analysis categorises failures. The authors position it as the successor to SWE-Bench Verified.

---

## Strengths

### S1: Clear, well-motivated problem
§1 states the motivation (saturation, trivial tasks, contamination) in a way a non-specialist can follow, and the three contributions are easy to find.

### S2: Resource of useful scale with a thoughtful release policy
731 public tasks (§3.3) with Docker environments "released as pre-built docker images" (§3.2) and private tiers for monitoring is a sensible structure that the community can use.

### S3: Concrete appendix example
App. A walks through one full instance (problem statement, requirements, interface) and Table 4 shows the rewrite, which makes the augmentation process tangible.

### S4: Candid limitations
§7.1 lists language coverage, test dependence and reduced ambiguity, which is more honest than most benchmark papers.

---

## Weaknesses

### W1: Contribution claims outrun the evidence, and the key evidence is thin (MAJOR)
The three headline properties — contamination resistance, "long-horizon" difficulty, resolvability — are asserted in the abstract and conclusion ("robust, contamination-resistant testbed", §8) but are not supported by experiments. The ICLR audience will expect at least a contamination probe, a human-time or step-count measure and an annotation-quality report. Results are single-run (§5), and some top-line comparisons (GPT-5 vs Opus 4.1: 23.3 vs 22.7) are inside any reasonable noise.
- **Suggested Fix**: Add the three missing measurements and CIs, or narrow the claims.

### W2: Result presentation has inconsistencies that undermine trust (MAJOR)
Text and tables disagree (§5 gives 16.3% for Sonnet 4 and 3.9% for GPT-4o; Table 1 gives 17.6 and 4.9), the "highest tool error rate (42.0%)" sentence in §6.2 does not match Table 3, and Table 3's row totals exceed N=731 (e.g., Opus 681+239 = 920). A reader cannot tell what Table 3 counts. Table 3's columns also do not match the judge's categories in App. B.1.
- **Suggested Fix**: Re-tabulate Table 3 with explicit denominators and align the text; give the category mapping.

### W3: Important details are missing from the main text (MAJOR)
No list of the 41 repositories, per-language/per-repo counts, annotator numbers, or funnel statistics; "difficulty filtering" appears only in the Figure 1 caption; the Figure 4 caption refers to "10+ files and 500+ LOC" categories absent from §6.1. §3.1 ("50-100+") and §1 ("strict cap of 100") describe the per-repo limit differently, and the commercial set averages about 15 tasks per repository.
- **Suggested Fix**: Add a dataset-statistics table and a datasheet in the appendix; make the caption/text consistent.

**Minor:** "DeepSeek Qwen-3 32B" mislabel (§5); citations to [25] for SWE-bench (Abstract) and to [1, 25] as "social media posts" (§1); Section 3.1 repeats the introduction; section titles do not match each other (§3 vs §4); the acknowledgements and §4.1 name individuals and an organisation, which breaks double-blind anonymisation.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly | Contamination/long-horizon unsupported (§3.1, Abstract) |
| Soundness: evaluation protocol | Partly | Single run/scaffold (§5); Table 3 inconsistent |
| Presentation: clear and complete | Partly | Missing stats; text–table mismatches |
| Contribution: significance | Met | Benchmark succeeds saturated SWE-Bench Verified (§1) |
| Contribution: new insight | Partly | Failure modes (§6.2) interesting but unvalidated |
| Reproducibility/ethics statements | Partly | Public set released; licence/consent for commercial data not stated |

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in validation |
| Clarity | 2 | Inconsistent numbers and missing details |
| Significance | 3 | Useful resource |
| Originality | 3 | New data-source idea |

---

## Dimension Scores (0–100)

**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: benchmark utility and timeliness are above the median submission; the weaknesses are typical for accepted benchmark papers, though the numerical inconsistencies are above typical.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound core, unsupported claims |
| Clarity & Presentation | 58 | Competent | Clear motivation; inconsistent numbers/missing tables |
| Novelty & Originality | 58 | Competent | Incremental, one new idea |
| Significance & Impact | 72 | Competent-high | Timely, usable |
| Experimental Validation | 56 | Competent-low | Single harness, no variance |
| Reproducibility | 55 | Competent-low | Partial release |
| Ethical Compliance | 62 | Competent | Limitations candid |

---

## Questions for Authors

1. Can you reconcile Table 3 with N=731? A clean table would raise my Clarity score.
2. What is the median patch size and file count, versus SWE-Bench Verified?
3. Will the held-out results for at least two models be released during discussion?

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially (§7.1).

---

## Ethics Review Flag

**No**.

---

## Overall Score

**4**: A useful, timely benchmark whose weaknesses are fixable and typical of accepted benchmark papers, though the inconsistencies must be repaired. Composite 60.1.

## Confidence

**4**: Read the full paper; judged figures from captions.

---

# Devil's Advocate Report

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Reviewer: Dr. Oluwaseun Adeyemi-Park, Devil's Advocate (evaluation-methodology group, university, North America; fictional persona)

---

## Steelman
SWE-Bench Verified is near saturation, and a benchmark with larger multi-file changes, human-verified specifications, private and licence-restricted data, and visible headroom is exactly what the field needs. The authors tie each design choice to a known weakness of SWE-bench and are open about the main limitations.

---

## Core Argument Chain
1. SWE-Bench Verified exceeds 70% and has many trivial tasks (§1).
2. SWE-Bench Pro keeps only multi-file changes of ≥10 lines from actively maintained repositories (§1, §3.1).
3. GPL-licensed public repositories and purchased private repositories are unlikely to be in training data (§3.1).
4. Human augmentation and test filtering make every task resolvable (§4.2–4.3).
5. Models score below 25% (Tables 1–2), with failure modes characterised by an LLM judge (§6.2).
∴ SWE-Bench Pro is a contamination-resistant, rigorous measure of progress toward professional-level, long-horizon software engineering agents (Abstract, §8).

---

## Strongest Counter-Argument
Low pass rates are offered as evidence of difficulty ("long-horizon", "enterprise-level"), but the paper cannot distinguish that reading from three alternatives. First, **harness failure**: for GPT-5, 63.1% of failing trajectories never submit and 97.6% of those are tool-use errors; for Sonnet 4, 61.6% of non-submissions are context overflow (Table 3). A score of 23.3% under a single, shared 200-turn SWE-Agent prompt (§5) may be a measure of scaffold fit. Second, **specification–test coupling**: requirements are "grounded in the gold patch and test expectations" (§4.2) and name functions and routes (App. A.2–A.3). A task can then fail because a valid implementation differs from the reference interface, a false-negative risk the authors concede in §7.1 ("Dependency on Test Suite") but never measure. Third, **selection effects**: tasks survive only if they have ≥10 changed lines, multiple files and a clean fail2pass transition, plus unreported human filtering whose funnel is missing, so the benchmark may select for test-brittle instances, not for hard but fair ones. Meanwhile "contamination-resistant" rests on an untested legal premise (§3.1) and the held-out set has no results to show it works. The comparison with ">70% on SWE-Bench Verified" (Figure 2 caption, §8) mixes a different harness, spec style, and task set, and so cannot support "a critical gap between current agent capabilities and the demands of real-world development" (§8). The authors need to show that a failing frontier model's patch is genuinely wrong, and that a competent engineer solves the task, before the numbers can be read as capability gaps.

*This supports a weaker claim (a harder, richer benchmark), not the opposite of the stated claim, so it is MAJOR, not CRITICAL.*

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim that the benchmark is hard and useful survives in a narrower form (a harder, executable benchmark whose validity evidence is still missing); each weakness below can be repaired by narrowing the wording or adding analyses, and none shows that the evidence contradicts the claim or that leakage occurred.

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence/Scope | §3.1; Abstract "contamination-resistant testbed" | Contamination resistance rests on a legal premise ("the nature of these licenses creates legal barriers…"); no probe; held-out set has no results; closed models were presumably run on private code through vendor APIs | Add empirical contamination evidence and held-out results, or say "reduced risk" |
| DA-M2 | Evidence (E1) | Table 3 vs §6.2, §5 | Row totals 920/724/699/915/789/792 vs N=731; "highest tool error rate (42.0%)" vs 349/792=44.1% and GPT-5 446/724=61.6%; text figures 16.3%/3.9% vs Table 1's 17.6/4.9 | Reconcile or correct; state category mapping |
| DA-M3 | Logic | §5, Table 3 | Low scores confounded by harness failures; one scaffold; Agentless numbers not reported | Add a second harness and a harness-failure share |
| DA-M4 | Scope (E5) | Abstract, Fig. 1 caption | "hours to days", "long-horizon", "difficulty filtering" are unmeasured/undescribed | Measure or remove |
| DA-M5 | Logic | Fig. 2 caption, §8 | The 23% vs >70% comparison mixes harness, spec and task set | Report SWE-Bench Verified under the same scaffold and prompt |
| DA-M6 | Evidence | Tables 1–2 | No CIs; GPT-5 vs Opus 4.1 and the public/commercial flip are within noise; "highest score to date" | Report CIs; soften wording |
| DA-M7 | Integrity-adjacent | §3.1, §4.1, Abstract | Provenance of commercial repos (purchased vs M&A vs employees' startups vs "formal partnership agreements") is described inconsistently; selection of partners unspecified | Describe selection and independence; disclose rights |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Citations | Abstract, §1 | [25] cited for SWE-Bench; [1, 25] called "social media posts"; [13] vs [15] for Verified |
| DA-m2 | Consistency | §1 vs §3.1 | "strict cap of 100" vs "50-100+"; commercial repos average ≈15 tasks |
| DA-m3 | Labels | §5 | "DeepSeek Qwen-3 32B" |
| DA-m4 | Judge | §6.2 | "87% alignment" borrowed from [22] for another taxonomy and judge; own human agreement not reported |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Subset sizes | 731 + 276 + 858 = 1,865 (§3.3) | 1,865 | Yes |
| Repositories | 11 + 12 + 18 = 41 (Abstract) | 41 | Yes |
| Sonnet 4 public resolve rate | 16.3% (§5) | 17.6% (Table 1) | No |
| GPT-4o public resolve rate | 3.9% (§5) | 4.9% (Table 1) | No |
| Qwen3-32B tool-error rate | 42.0% (§6.2) | 349/792 = 44.1% (Table 3) | No |
| "Highest" tool error rate | Qwen (§6.2) | GPT-5: 446/724 = 61.6% | No |
| Opus failure total | 681 + 239 = 920 (Table 3) | Unresolved ≈ 731 × (1 − 0.227) = 565 | No |
| Opus "wrong solution" share | 35.9% (§6.2) | 330/920 = 35.9% | Yes (but uses the 920 base) |
| 95% CI, GPT-5 public | not reported | 23.3 ± 3.1 pp (N=731, normal approx.) | n/a |
| Commercial per-repo size | "50 and 100" (§1) | 276/18 ≈ 15.3 average | No |

## Ignored Alternative Explanations
- Harness/scaffold mismatch (Table 3's tool-use and context-overflow shares) rather than capability.
- Test brittleness and interface coupling (valid alternative implementations fail).
- Repository familiarity: high-profile GPL projects (e.g., Open Library, App. A.1.1) may be better known than the paper assumes, through issues, forums and mirrors.
- Selection on fail2pass cleanliness favouring particular repo types, and difference between Python/Go and JS/TS driven by test infrastructure, not by language difficulty (§6.1).

## Missing Stakeholder Perspectives
- Companies whose code is used and vendors that receive it during API evaluation; annotators (compensation and conditions not described); maintainers of the GPL projects.

## Observations (Non-Defects)
- The split design (public/held-out/commercial) is a strong, rare idea; the limitations section pre-empts several objections; the judge prompt is disclosed; stated subset counts add up.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Untested central claims; inconsistent Table 3 |
| Clarity & Presentation | 56 | Readable but with mismatches and missing details |
| Novelty & Originality | 52 | Incremental over SWE-bench family; sourcing idea new |
| Significance & Impact | 62 | Useful, but validity of "gap" claims unproven |
| Experimental Validation | 42 | One run, one harness, no CIs |
| Reproducibility | 50 | Partial release, missing run details |
| Ethical Compliance | 55 | IP/consent and API exposure unaddressed |

## Overall: 3 | Confidence: 4
(Pool position: better than about 50% of submissions; composite 51.5.)

---

# Phase 1.6 — Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 Table 3 inconsistency | kept | Specific, verified by recomputation, has a fix |
| R1 | Draft point "no limitations section" | dropped | §7.1 exists and covers language, scope, test dependence, ambiguity |
| R1 | Fig. 4 caption mismatch | moved to Minor | Cosmetic/figures unavailable |
| R2 | W1 positioning vs SWE-rebench etc. | rewritten | Novelty statements now match the abstracts retrieved by the literature check (mechanism differs; no "known" claim) |
| R2 | W5 citation errors | kept (MINOR) | Verified against the bibliography |
| R3 | W5 broader impact | kept, flagged as low weight | Specific but speculative; §7.2 gestures at future work |
| R3 | "Language coverage narrow" draft point | dropped | Answered by §7.1 "Limited Language Coverage" |
| R3 | W2 API exposure | rewritten as a question-backed weakness | Paper does not say how models were served; inference, not a stated error |
| R4 | "No discussion of reduced ambiguity" draft | dropped/rewritten | §7.1 discusses it; rewritten as "no ablation" under R1-W5/R3-W1 |
| DA | DA-M5 comparison with SWE-Bench Verified | kept | Specific to Fig. 2 caption and §8 |
| DA | "No inter-annotator agreement" within M-list | kept in R1-W4/DA text | Not stated after search |

Scores were not changed in this step.

---

# Phase 2 — EIC Meta-Review and Decision

*Synthesizer package (Part A):* official mean rating 3.60; official composite 58.1; spread >20 on no dimension (max 16); no consistency warnings; no integrity flags; no DA-CRITICAL.

**Merged issue list (classification):**
| Issue | Sources | Class |
|-------|---------|-------|
| Contamination resistance untested | R1-W6, R2-W2, R3-W3, R4-W1, DA-M1 | CONSENSUS-4/5 |
| Table 3/text/numbers inconsistent | R1-W1, R4-W2, DA-M2 | CONSENSUS-3 |
| Single run/no CIs, within-noise rankings | R1-W2, R4-W1, DA-M6 | CONSENSUS-3 |
| Harness confound | R1-W3, DA-M3 | CONSENSUS-2 |
| Validity/resolvability not evidenced (agreement, funnel, false negatives) | R1-W4, R3-W4, DA-counter-argument | CONSENSUS-3 |
| "Long-horizon/enterprise" unmeasured | R1-W5, R2-W3, R3-W1, DA-M4 | CONSENSUS-4/5 |
| Commercial set rights/provenance/API exposure | R1-W6, R3-W2, DA-M7 | CONSENSUS-3 |
| Positioning vs SWE-rebench/SWE-Lancer | R2-W1 | SOLO |
| Citation errors | R2-W5, R4-minor, DA-m1 | CONSENSUS-3 (minor) |
| Judge validity | R2-W4, DA-m4 | CONSENSUS-2 |

# Editorial Decision

## Paper: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
## Submission ID: iclr26-9R2iUHhVfr
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: benchmark
## Review Team (fictional personas): EIC Prof. Elena Marchetti-Voss; R1 Methodology Dr. Anika Sundaram, R2 Domain Prof. Lars Eidevall, R3 Perspective Dr. Camila Restrepo-Fuentes, R4 Generalist Dr. Hyun-woo Baek, DA Dr. Oluwaseun Adeyemi-Park

---

## Decision: Borderline Accept (4) — ICLR rating label "6" on {0,2,4,6,8,10} (also "6" on {1,3,5,6,8,10}); scale status: secondary

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60 · official composite 58.1
**EIC assessment** (internal): weighted rating 3.56 → starting point 4 · weighted composite 57.8 → band 3 (cross-check) · **DA ceiling**: none · **Final (EIC)**: 4

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely, executable, large benchmark for a topic the community needs after SWE-Bench Verified saturation. The licence-restricted public set, a private commercial set with public result reporting, and a held-out split are a distinctive release design, and results show real headroom (≤23.3% and ≤17.8%). The authors are candid about the main limitations, and every substantive issue can be fixed in a revision (narrowing claims, adding CIs, re-tabulating Table 3, adding validity audits).
- **Against acceptance:** The three headline properties (contamination resistance, long-horizon difficulty, resolvability) are asserted and not measured, and Table 3 does not reconcile with N=731. Results are a single run under a single scaffold in which harness failures dominate several rows, so rankings and the 23%-vs-70% "gap" are not interpretable as capability differences. The commercial set raises unaddressed IP/consent and API-exposure questions.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 3 row totals exceed N=731 (920, 915, 789, 792) | R1-W1, R4-W2, DA-M2 | Table 3, §6.2 | Verified | Recomputed: 681+239=920, 491+424=915, 569+220=789, 386+406=792; all > 731 |
| Text 16.3%/3.9% vs Table 1 17.6/4.9 | R1 ERR-2/3, R4, DA | §5 "Results", Table 1 | Verified | Quoted text vs table |
| "Qwen has the highest tool error rate (42.0%)" | R1 ERR-4, DA-M2 | §6.2, Table 3 | Verified (claim incorrect) | 349/792 = 44.1%; GPT-5 446/724 = 61.6% |
| Contamination resistance is not tested | R1-W6, R2-W2, DA-M1 | §3.1 | Verified | Only a licence argument; held-out set has no results |
| "Hours to days" and "long-horizon" unmeasured | R1-W5, DA-M4 | Abstract, §1 | Verified | No human-time or trajectory-length data |
| "Difficulty filtering" undescribed | R1-W5, R4-W3, DA-M4 | Figure 1 caption, §4 | Partly correct | §1 states the exclusion of 1–10-line edits, which may be what is meant; no model-based filter is described in §4 |
| GPT-5 63.1% not submitted, 97.6% tool-use | R1-W3, DA | Table 3 | Partly correct | Numbers verified; reading them as scaffold mismatch is an inference the paper does not test |
| Commercial set averages ≈15 tasks per repo vs "50 and 100" | R1 ERR-5, R4, R2 | §1, §3.3, Abstract | Verified | 276/18 = 15.3 (average), so at least some repositories are below 50 |
| Public/commercial ranking flip GPT-5 vs Opus 4.1 | R1-W2, DA-M6 | Tables 1–2 | Verified | 23.3 vs 22.7 (public); 14.9 vs 17.8 (commercial) |
| No CI/seed information | R1-W2 | §5 | Verified | Not stated after search |
| Citation errors ([25] for SWE-Bench; [1, 25] as "social media posts") | R2-W5, DA-m1 | Abstract, §1, refs | Verified | Both are arXiv papers per the reference list |
| Requirements are "grounded" in tests/gold patch (spec–test coupling) | DA, R3-W1 | §4.2, App. A.2 | Verified | Direct quote in §4.2 |
| Commercial-set provenance inconsistent | DA-M7, R3-W2 | Abstract, §3.1, §4.1 | Partly correct | Three descriptions (partnerships, purchase, M&A/employee startups) are compatible but unreconciled; no contradiction proven |
| Uncited SWE-rebench, SWE-Lancer | R2-W1 | refs; literature check | Verified | Not in bibliography; labelled prior; mechanism differs, so "positioning gap", not "known result" |
| Proprietary models run via vendor APIs on private code | R1-W6, R3-W2 | Table 2, §5 | Partly correct | API models appear in Table 2; the access route and retention terms are not stated, so exposure is an inference |

**Missing-comparison check against ledger labels:** R2's missing references SWE-rebench (prior, peer-reviewed label), SWE-Lancer (prior arXiv-only 6+ months), OmniGIRL (prior, peer-reviewed) are eligible as required discussions (positioning, not baselines, since no shared evaluation exists). SWE-bench Goes Live and Multi-SWE-bench carry the "recent preprint" label and are cited; they are not grounds for lowering any score. The text-overlap flag with Multi-SWE-bench is a correctly cited description (integrity concern: none). No integrity-scan findings; no injection.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log entry verified at its location; well calibrated; minor overreach on the compute-cost estimate |
| R2 (Domain) | 4 | 4 | 1.0 | Literature claims verified against retrieved abstracts; sound, typical review |
| R3 (Perspective) | 4 | 3 | 1.0 | Sensible practitioner angle; API-exposure point is an inference, but stated as a question; not penalised for role |
| R4 (Generalist) | 4 | 4 | 1.0 | Verified presentation points; calibrated |
| DA | 3 | 4 | 1.0 | Arguments mostly verified; strongest counter-argument is partly inferential, so default weight |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | n/a | n/a |

I considered whether the contamination claim (DA-M1) should be promoted: it is not criterion 3 (no leakage into a tuned model is shown), does not show evidence contradicting the claim, and the benchmark remains useful if the claim is narrowed. It stays MAJOR.

### Final Decision and Justification
The EIC-weighted rating is 3.56, rounding half-up to 4 (Borderline Accept), within 0.06 of the 3.5 boundary; the 0–100 composite (57.8) falls in band 3. A one-step disagreement near a band boundary is a borderline signal, not a reason to depart, and I cannot name a verified issue that the reviewers' ratings failed to account for: R1 and the DA already priced in the Table 3 and validity problems, and R2–R4 explicitly weigh them against usefulness. I keep the starting point, 4. My own pool position is **65**: better than about 65% of ICLR submissions. The deciding evidence is that a large, executable benchmark for a high-demand problem, with a distinctive release design and visible headroom, is the kind of resource accepted at ICLR despite real weaknesses (single harness, missing intervals, overclaimed wording), whereas the unverified central claims and the Table 3 inconsistencies keep it close to the line. There is no DA ceiling, so the decision does not exceed any cap. Acceptance should be conditional in spirit on narrowing the contamination, long-horizon and "gap" wording, fixing Table 3, adding CIs, and describing the filtering funnel; if those cannot be done the paper would be Borderline Reject.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 60 | 62 | 58 | 46 | 55.2 | 54.7 | 16 |
| Clarity & Presentation | 58 | 62 | 64 | 58 | 56 | 59.6 | 59.4 | 8 |
| Novelty & Originality | 52 | 60 | 62 | 58 | 52 | 56.8 | 56.4 | 10 |
| Significance & Impact | 68 | 72 | 76 | 72 | 62 | 70.0 | 69.7 | 14 |
| Experimental Validation | 46 | 56 | 58 | 56 | 42 | 51.6 | 51.1 | 16 |
| Reproducibility | 48 | 56 | 58 | 55 | 50 | 53.4 | 53.0 | 10 |
| Ethical Compliance | 55 | 62 | 58 | 62 | 55 | 58.4 | 58.2 | 7 |
| **Composite** | 54.1 | 61.4 | 63.5 | 60.1 | 51.5 | **58.1 (before)** | **57.8 (after)** | |
| Pool position | 52 | 65 | 70 | 65 | 50 | | EIC: 65 | |

Reviewer weights (EIC): R1 1.25, R2 1.0, R3 1.0, R4 1.0, DA 1.0 (confidence weights 0.85/0.85/0.70/0.85/0.85).

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 3 |
| Rating (final = 4 on the skill's scale) | 6 on {0,2,4,6,8,10} (6 on {1,3,5,6,8,10}); label from the script, not official wording |
| Venue-weighted composite | 57.9 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?" to ICLR.

Your paper targets a timely need: a benchmark with headroom for coding agents once SWE-Bench Verified saturates.

**Overall Assessment:**
The reviewers saw a large, executable and practically relevant benchmark with an unusual release design. They also found that several of its central claims are asserted rather than measured, and that parts of the results analysis do not yet reconcile with the reported setup. The panel's view, as a simulation of how a careful panel might see this draft, is borderline, leaning toward acceptance.

**Key Strengths Identified by Reviewers:**
1. A well-motivated, executable benchmark of useful size with clear headroom (R1, R2, R3, R4).
2. A distinctive public/held-out/commercial release design and licence-based sourcing idea (R2, R3, DA observation).
3. Candid limitations and a tangible worked example (R1, R3, R4).

**Key Concerns Requiring Attention:**
1. Contamination resistance, "long-horizon" difficulty and resolvability are not backed by measurements (CONSENSUS-4/5).
2. Table 3 does not reconcile with N=731, and several text statements contradict Tables 1 and 3 (CONSENSUS-3).
3. Single-run, single-scaffold results without intervals, with harness failures dominating several rows; rankings are within noise (CONSENSUS-3).
4. Rights, consent and API exposure for the commercial set are not described (CONSENSUS-3).

**Decision: Borderline Accept (4)**

The balance tipped on usefulness and fixability: each concern above can be addressed by narrowing claims and adding analyses on existing data. Please see the Revision Roadmap below.

Sincerely,
Prof. Elena Marchetti-Voss
Editor-in-Chief (meta-reviewer, fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Contamination resistance untested | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Long-horizon/enterprise claim unmeasured | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Table 3 and text-number inconsistencies | R1, R4, DA | CONSENSUS-3 |
| Single run, no CIs | R1, R4, DA | CONSENSUS-3 |
| Validity/resolvability not evidenced | R1, R3, DA | CONSENSUS-3 |
| Commercial set rights and exposure | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall recommendation | R2, R3, R4 (4) | R1, DA (3) | The rating-based starting point is 4 (3.56); the dissenters' evidence is verified, but the accept-leaning reviewers weigh it against significance; kept at 4 as a borderline call |
| Severity of the missing-literature point | R2 | R1, R3, R4 (not raised) | SOLO issue; positioning gap only; MAJOR at most |

### Score Spread Discussion
No dimension spreads by more than 20 points (maximum: Technical Rigor and Experimental Validation, 16). Composite band (3) differs from the rating-based start (4); treated as a borderline signal near a band boundary.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Contamination untested | Yes (R1, R2, R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | Table 3/text inconsistencies | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Harness confound | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Unmeasured "long-horizon" | Yes (R1, R2, R3) | n/a | n/a |
| DA-M5 | MAJOR | 23% vs >70% comparison not like-for-like | No | n/a | n/a |
| DA-M6 | MAJOR | No CIs; rankings within noise | Yes (R1, R4) | n/a | n/a |
| DA-M7 | MAJOR | Commercial provenance/rights | Yes (R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld. The items below are those the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Contamination resistance is untested | R1-W6, R2-W2, R3-W3, R4-W1, DA-M1 | §3.1, Abstract | Add a contamination probe (date-split performance, verbatim completion), report held-out results for ≥2 models, or reword to "reduced risk" | Medium; ~100–200 API-hours | Yes (partially) |
| R2 | Table 3 irreconcilable with N=731; text contradicts tables | R1-W1, R4-W2, DA-M2 | Table 3, §5, §6.2 | Define denominators, re-tabulate, fix 16.3/3.9/42.0 statements, give category mapping | Low | Yes |
| R3 | "Long-horizon", "hours to days", "difficulty filtering" unmeasured | R1-W5, R2-W3, DA-M4 | Abstract, Fig. 1 caption, §1 | Report median patch size/files vs SWE-Bench Verified, turns used, human-time sample; describe or remove the difficulty filter | Low–Medium | Yes |
| R4 | No CIs; single run; "highest score to date" | R1-W2, DA-M6 | Tables 1–2, Abstract | Paired-bootstrap CIs; ≥3 runs for top models; soften wording | Medium; few thousand GPU/API-hours | Partly |
| R5 | Resolvability/validity unevidenced | R1-W4, R3-W4, DA | §4.1–4.3, §7.1 | Add the filtering funnel, annotator count and agreement; audit ~100 failures for false negatives | Medium | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Harness confound (tool-use/context failures) | R1-W3, DA-M3 | Second scaffold or harness ablation for top 3 models | Medium–High | Partly |
| S2 | Like-for-like comparison with SWE-Bench Verified | DA-M5 | Run Verified under the same scaffold/prompt for 2–3 models | Medium | Partly |
| S3 | Commercial set rights, consent, API access, partner selection | R3-W2, DA-M7, R1-W6 | Add licence/consent/PII scanning statement and API retention terms | Low | Yes |
| S4 | Positioning against SWE-rebench, SWE-Lancer, OmniGIRL, SWE-PolyBench | R2-W1 | Add comparison table; narrow "first" | Low | Yes |
| S5 | Judge validation | R2-W4, DA-m4 | Human-labelled sample (n≥100), per-category agreement, second judge | Medium | Partly |
| S6 | With/without requirements ablation | R1-W5, R3-W1 | Subset ablation | Medium | Partly |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Citation errors ([25], [1, 25], [13]/[15]) | R2-W5, DA-m1 | Audit bibliography |
| N2 | Per-repo count wording (§1 vs §3.1; commercial ≈15 per repo) | R1 ERR-5, DA-m2 | State per-set statistics |
| N3 | Repository list and datasheet in appendix | R3, R4 | Add |
| N4 | Fig. 4 caption mentions categories not in §6.1; "DeepSeek Qwen-3" label | R1, R4 | Fix |
| N5 | Broader-impact and sandboxing paragraph | R3-W5 | Add |
| N6 | Anonymity: §4.1 and acknowledgements identify organisation/individuals | R4 | Anonymise |

---

## Estimated Revision Effort
- Priority 1: 5 items, roughly 1–2 weeks (re-tabulation and wording are hours; probes, CIs and audits are days).
- Priority 2: 6 items, roughly 1–2 weeks (harness and Verified comparison are the largest).
- Priority 3: 6 items, 1–2 days.
- **Total estimated revision time**: about 2–3 weeks of work for one team; the rebuttal window can cover the low-effort items and part of the medium ones.
