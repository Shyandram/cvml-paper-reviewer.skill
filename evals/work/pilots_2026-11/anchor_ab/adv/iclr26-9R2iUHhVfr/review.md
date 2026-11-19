# Peer Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | benchmark |
| Field, sub-area | machine learning; LLM agents for software engineering, code benchmarks |
| Task | Repository-level software-engineering benchmark for LLM agents (adapted from the "LLMs, NLP" row of `references/task_neighbors.md`; no listed row fits) |
| Neighboring fields | LLM evaluation and data contamination (row "LLMs, NLP"); evaluation science / benchmark methodology (row "LLMs, NLP"); empirical software engineering and mining software repositories (*added*); software testing and automated program repair (*added*); datasets-and-benchmarks / open science (*added*); human annotation and crowdsourcing quality control (*added*) |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | `aggregate_scores.py ratio --paper-type benchmark --venue iclr`: significance 21%, experimental validation 19%, technical rigor 17%, clarity 15%, reproducibility 14%, novelty 10%, ethics 4% |
| Literature check | off (no network access in this run); novelty reasons resting on memory are marked [verify] where relevant |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Input note: the review uses the text extracted from the PDF. Figures 1-4 were not available; claims that rest on them (Figure 3 distributions, Figure 4 per-language and per-repository rates) are judged from their captions and the text only.

---

## 1. Paper memory

**Claims.**
- C1: SWE-Bench Pro is "substantially more challenging"; under a unified scaffold, frontier models stay "below 25% (Pass@1), with GPT-5 achieving the highest score to date at 23.3%" (Abstract; Table 1; Figure 2 caption).
- C2: The benchmark is "contamination-resistant" by design: copyleft (GPL) public and held-out sets plus a private commercial set; "the first to systematically apply such a methodology" (Abstract; Section 1; Section 3.1).
- C3: The tasks are realistic, enterprise-level, diverse and "long-horizon ... may require hours to days" for a professional engineer; reference solutions average 107.4 lines across 4.1 files (Title; Abstract; Section 1; Section 3.1).
- C4: Human augmentation (problem statement, requirements, interface) and verification ensure resolvability and avoid false negatives (Abstract; Section 1; Sections 3.2, 4.2-4.3; Appendix A).
- C5: The public-to-commercial drop shows "the greater complexity of enterprise codebases" (Section 1; Section 5; Table 2).
- C6: An LLM-as-judge analysis shows that large models fail on semantic or algorithmic correctness, small models on syntax, tool use and context management (Section 1; Section 6.2; Table 3).

**Setup facts.**
- Subsets: public 731 tasks / 11 repositories; commercial 276 / 18; held-out 858 / 12; total 1,865 (Abstract; Section 3.3). Languages: Python, Go, JavaScript, TypeScript (Section 3.2 Environments; Section 7.1).
- Construction: consecutive commit pairs with fail2pass tests (Section 4.1); edits of 1-10 lines excluded (Section 1); human-written problem statement, requirements and optional interface (Sections 3.2, 4.2); Docker environments by professional engineers, tests run 3 times, human filtering of fail2pass tests (Sections 3.2, 4.3).
- Evaluation: SWE-Agent scaffold, same basic prompt, max 200 turns, model versions "as of September 18th, 2025", open-weight models served with vLLM on 8 H100s, tool use via syntax parsing for open-weight models; Pass@1 (Section 5). Fully specified setting, no ambiguity (Section 5 Issue Ambiguity).
- Seeds / number of runs / confidence intervals: not stated after search. Decoding temperature, token or cost budget: not stated. Annotator numbers, agreement, drop counts: not stated. Human solve times: not stated. Held-out set results: none ("for future analysis", Section 5).
- Failure analysis: GPT-5 as judge on the last 20 turns of unresolved trajectories, one category per instance; human agreement cited from prior work (87%) (Section 6.2; Appendix B.1).

**Headline numbers.** Public set: GPT-5 23.3, Claude Opus 4.1 22.7, Claude Sonnet 4 17.6, Gemini 2.5 Pro Preview 13.5, SWE-Smith-32B 6.8, GPT-4o 4.9, Qwen-3 32B 3.4 (Table 1). Commercial set: Opus 4.1 17.8, GPT-5 14.9, Gemini 10.1, Sonnet 4 9.1, GPT-4o 3.6 (Table 2). ">70%" on SWE-Bench Verified (Section 1, citing [15]; Figure 2 caption). 107.4 lines / 4.1 files average (Section 1).

**Appendix summary.** Appendix A: one full worked instance (Open Library: problem statement, requirements, interface) and Table 4 (original commit message vs rewritten issue). Appendix B.1: the full LLM-judge prompt with ten categories. No additional experiments.

**Could not be read.** Figures 1-4 (images). Table 1 and Table 2 were merged side by side in extraction but are readable. No supplement was provided.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | Fills a real need: SWE-Bench Verified is near saturation (>70% reported) while the strongest agents resolve at most 23.3% here, leaving headroom to track progress | Abstract; Section 1 ('In the next 6 - 12 months, there will be diminishing feedback from SWE-Bench-Verified'); Table 1 (GPT-5 23.3) | strong | R4, R26 not upheld |
| A2 | novelty | A three-tier access design for contamination resistance: copyleft-licensed public and held-out sets plus a private commercial set, which the paper argues has not been applied systematically to a research benchmark | Section 1 ('exclusively selecting repositories distributed under strong copyleft licenses (GPL)'); Section 3.1; Section 3.3 | moderate | R1 (resistance actually holds) |
| A3 | significance | Tasks are larger than in SWE-Bench Verified: reference solutions average 107.4 lines across 4.1 files, every task changes at least 10 lines | Section 1 ('On average, the reference solutions span 107.4 lines of code across 4.1 files'); Figure 3 caption | moderate | R17 (which subset); R10 |
| A4 | technical_rigor | Human augmentation adds a problem statement, requirements and an interface specification so that agents are not failed for misnaming functions or missing information (fewer false negatives) | Section 3.2 (Requirements, Interface); Section 4.2; Appendix A.2-A.3; Table 4 | moderate | R11, R12 |
| A5 | technical_rigor | Environment and test verification: Dockerfiles built by professional engineers, tests run 3 times to remove flaky tests, human filtering of irrelevant or too-broad fail2pass tests | Section 3.2 ('we run each set of tests 3 times'); Section 4.3 | moderate | R25 |
| A6 | experimental_validation | Uniform evaluation protocol: one scaffold (SWE-Agent), the same prompt, a 200-turn cap and a fixed model-version date for all seven models | Section 5 ('We use the same prompt for all models'; 'latest versions as of September 18th, 2025') | moderate | R3 (scaffold not decisive) |
| A7 | significance | A private commercial set gives an enterprise-code evaluation that public benchmarks cannot offer, and the paper reports results on it (best 17.8%) | Section 3.3; Table 2 (Claude Opus 4.1 17.8, GPT-5 14.9) | moderate | R13 |
| A8 | experimental_validation | Diagnostic analyses beyond a leaderboard: breakdowns by language and repository and a trajectory failure-mode taxonomy, with the judge prompt released | Section 6.1; Figure 4; Section 6.2; Table 3; Appendix B.1 | moderate | R5, R6, R8, R9 |
| A9 | reproducibility | The public set (731 tasks) is released with pre-built Docker images and evaluation code, and the agent-judge prompt is given | Section 3.3 ('We release 731 instances openly on HuggingFace'); Section 3.2 ('All environments will be released as pre-built docker images'); data/code links on p.1 | strong | release as promised; R16 |
| A10 | significance | Breadth: 41 actively maintained repositories across consumer apps, B2B services and developer tools, with a per-repository cap to prevent one repo dominating | Abstract; Section 1 ('strict cap of 100 instances'); Section 3.1 | moderate | R14 |
| A11 | clarity | The task format is clearly specified and illustrated with a full worked instance and an original-vs-rewritten issue comparison | Section 3.2; Appendix A.1-A.3; Table 4 | moderate | — |
| A12 | ethics | Candid limitations: language coverage, dependence on test suites, and the reduced ambiguity introduced by augmentation are acknowledged | Section 7.1 | moderate | — |
| A13 | significance | A held-out set from separate repositories is retained to detect future overfitting to the public set | Section 3.3 ('We keep this set private to test for overfitting in the future') | weak | the held-out set is eventually evaluated |
| A14 | significance | Multi-language coverage (Python, Go, JavaScript, TypeScript) beyond the Python-only SWE-bench, with per-language results | Section 6.1; Figure 4 (left); Section 7.1 | weak | R23 |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | technical_rigor | The contamination-resistance claim is never tested. The 'legal barriers' of GPL are asserted, not shown; no memorization probe, no commit-date vs training-cutoff analysis, and the held-out set built for this purpose is never evaluated | Section 3.1 ('creates legal barriers to their inclusion in commercial training corpora'); Section 5 ('we keep the private set held-out for future analysis'); Abstract ('contamination-resistant testbed') | gap | major | Evaluate the held-out set and compare with the public set; add a commit-date vs cutoff analysis or a memorization probe; or soften to 'designed to reduce contamination'. Cost: a few agent runs (days of API budget) |
| R2 | experimental_validation | Single run Pass@1 without confidence intervals. With N=731 the binomial standard error near 23% is about 1.6 points, so GPT-5 (23.3) vs Opus 4.1 (22.7) is not separable, yet the abstract calls GPT-5 'the highest score to date' | Table 1; Abstract ('GPT-5 achieving the highest score to date at 23.3%'); derived SE = sqrt(0.233*0.767/731) = 1.56 pp | gap | major | Report binomial or bootstrap 95% CIs (free from existing runs) and, ideally, 3 runs for the top models; soften ranking claims. Cost: none to moderate |
| R3 | experimental_validation | Results rest on one scaffold with a 200-turn cap. The scaffold-model fit visibly drives outcomes (GPT-5 does not submit on 63.1% of its failures, 97.6% of those tool-use errors), and Agentless is dismissed without numbers | Section 5 ('we find that Agentless has difficulty in multi-file editing'; 'maximum of 200 turns'); Table 3 (GPT-5 Not-Submitted 63.1%, Tool-Use 97.6%) | gap | major | Report the Agentless numbers already run; add a second agent scaffold (e.g., OpenHands) for the top models; report turn-limit sensitivity. Cost: moderate API budget |
| R4 | technical_rigor | The headline contrast with '>70% on SWE-Bench Verified' is not a controlled comparison: Verified numbers come from vendor reports with other scaffolds, not the paper's SWE-Agent configuration, so the difficulty gap is confounded with scaffold and settings | Figure 2 caption ('score >70% of SWE-Bench Verified but less than 25%'); Section 1 ('over 70% pass rate on SWE-Bench-Verified [15]') | gap | major | Run the same SWE-Agent configuration on SWE-Bench Verified for the same models. Cost: low-moderate API budget |
| R5 | experimental_validation | Error (E1): Table 3 trajectory counts exceed the size of the set analysed. Section 6.2 filters 'to only unresolved instances' of the public set (N=731), but Opus 4.1 has 681+239=920 classified failures and Gemini 915; with a 22.7% resolve rate Opus should have about 565 unresolved | Table 3 (Opus 4.1 (681), (239); Gemini (491), (424)); Section 6.2 ('programmatically filter to only unresolved instances'); Table 1 (N=731). Recomputed: 731 x (1-0.227) = 565 | error | major | Explain what the denominators are (multiple runs? commercial set? resolved trajectories?) and recompute Table 3 on the stated population. Cost: low |
| R6 | clarity | Error (E1): 'Qwen 3 32B ... exhibits the highest tool error rate (42.0%)' does not match Table 3: Qwen's tool-use share of all failures is 51.3% x 86.0% = 44.1%, and GPT-5's is 63.1% x 97.6% = 61.6% | Section 6.2 ('exhibits the highest tool error rate (42.0%)'); Table 3. Recomputed from table percentages and counts (349/792 = 44.1%) | error | minor | Correct the number and the ranking. Cost: trivial |
| R7 | clarity | Error (E1): the text contradicts Table 1: 'Claude 4 Sonnet also achieves a 16.3% resolve rate' (Table 1: 17.6) and GPT-4o '3.9%' (Table 1: 4.9); Qwen-3 32B is called 'DeepSeek Qwen-3 32B' | Section 5 Results ('also achieves a 16.3% resolve rate'; 'at 3.4% and 3.9% respectively'); Table 1 | error | minor | Align text and table. Cost: trivial |
| R8 | technical_rigor | Error (E5, claim distortion): the introduction says smaller models such as Qwen 3 32B 'more frequently fail due to issues in syntax and formatting', but by Table 3 syntax errors are 24.2% of Opus 4.1 failures vs 23.2% of Qwen's; the text also reads 24.2% syntax errors as 'strong technical execution' | Section 1 ('smaller models (e.g., Qwen 3 32B) more frequently fail due to issues in syntax and formatting'); Section 6.2 ('suggesting strong technical execution'); Table 3 (Opus 74.0% x 32.7% = 24.2%; Qwen 48.7% x 47.7% = 23.2%) | error | major | Restate the failure-mode conclusions to match Table 3 (or report rates on a common denominator). Cost: low |
| R9 | technical_rigor | The LLM-judge failure analysis is not validated on this benchmark: GPT-5 judges its own and its competitors' trajectories, agreement with humans is borrowed from another paper (87%), the '20 turns' human comparison gives no numbers, and 'Other' absorbs 63.4% of Sonnet 4's submitted failures | Section 6.2 ('utilizing GPT-5 as the judge'; 'demonstrate 87% alignment'; 'We determined 20 turns to have the highest correspondence'); Table 3 (Sonnet 4 Other 63.4%) | gap | major | Report human-judge agreement (kappa) on a labelled sample for each model, use a second judge to check self-preference, refine the 'Other' bucket. Cost: a few annotator-days |
| R10 | significance | The 'long-horizon' framing (title) and 'tasks that may require hours to days for a professional software engineer' are not operationalized: no human solve-time estimates, no agent trajectory-length or turn statistics; only lines and files changed are measured | Title; Abstract ('may require hours to days for a professional software engineer to complete'); Section 1; Figure 3 caption | judgment | major | Report annotator time estimates or measured human solve times on a sample, and trajectory length/turn distributions; otherwise drop 'long-horizon'. Cost: low-moderate |
| R11 | technical_rigor | The human-written requirements and interface are derived from the tests and gold patch, so the benchmark measures implementing a precise specification rather than resolving an issue; the paper asserts they 'don’t leak solutions' but runs no ablation without requirements/interface | Section 3.2 ('These requirements are grounded on the unit tests'); Appendix A.2 ('Requirements never include specific code implementation and don’t leak solutions'); Section 5 Issue Ambiguity; Section 7.1 Reduction in Ambiguity | gap | major | Ablate on the public set: problem statement only vs + requirements vs + interface; audit a sample of requirements for solution leakage. Cost: moderate API budget plus annotation |
| R12 | technical_rigor | Quality control of the human pipeline is unreported: number and expertise of annotators, agreement, how many candidate tasks/tests were dropped at each stage, and whether any human independently solved tasks; so 'All tasks are human-verified ... to ensure resolvability' is unsupported | Abstract ('All tasks are human-verified and augmented with sufficient context to ensure resolvability'); Sections 4.2-4.3 (no counts or agreement); not stated after search | gap | major | Add a pipeline funnel table (candidates -> kept at each stage), annotator details, agreement, and a human-solvability check on a sample. Cost: low for reporting, moderate for a solvability study |
| R13 | experimental_validation | The public-vs-commercial gap is attributed to 'greater complexity of enterprise codebases' without any complexity statistics for the commercial set; the sets differ in repositories, languages and tasks per repository, and model order changes (Sonnet 4: 17.6 -> 9.1) | Section 1 ('underscoring the greater complexity of enterprise codebases'); Section 5; Tables 1-2 | gap | major | Report LOC, files, language mix and repo sizes for the commercial set and compare at matched task size. Cost: low |
| R14 | clarity | Error (E6): the per-repository count claim does not hold for the commercial set: 'Each repository contributes between 50 and 100 instances' but 276 commercial tasks over 18 repositories average 15.3 per repository; Section 3.1 also says '50-100+' against the 'strict cap of 100' | Section 1 ('Each repository contributes between 50 and 100 instances, with a strict cap of 100'); Section 3.1 ('contribute 50-100+ instances'); Abstract (18 commercial repositories); Section 3.3 (276 problems). Recomputed 276/18 = 15.3 | error | minor | State the rule per subset and report per-repo counts. Cost: trivial |
| R15 | reproducibility | Two of three subsets are private: commercial results cannot be reproduced by others, and no statistics of the held-out or commercial sets are given | Section 3.3; Section 5 ('For all analysis, we use the public set') | judgment | minor | Publish aggregate statistics of both private sets and a submission protocol for third-party evaluation. Cost: low |
| R16 | reproducibility | Evaluation details needed to reproduce Table 1 are missing: exact model identifiers, decoding temperature, context and token/cost budgets, how syntax-parsed tool use works for open-weight models, and per-run cost; SWE-Smith-32B is used without a citation | Section 5 Evaluation settings ('All models use the latest versions as of September 18th, 2025'; 'we use syntax parsing to enable tool-use'); Table 1 (SWE-Smith-32B); reference list (no SWE-smith entry) | gap | major | Add a configuration table per model and release run configs and trajectories. Cost: low |
| R17 | clarity | Dataset statistics are thin and partly unclear: which subset the 107.4 LOC / 4.1 files average covers is not stated, and 'over 100 tasks demand more than 100 lines' sits oddly with a mean of 107.4 unless the tail is heavy; distributions exist only in Figure 3 (not readable here) | Section 1 ('over 100 tasks demand more than 100 lines of modification'); Figure 3 caption ('Distributions in the public set') | question | minor | Give a statistics table per subset (median/IQR LOC, files, hunks, tests) in text. Cost: trivial |
| R18 | clarity | Minor inconsistencies: 'exclude trivial edits (1-10 lines)' vs 'at least 10 lines'; the Figure 4 caption mentions '10+ files and 500+ LOC' categories not described in the text; Table 3 columns do not map one-to-one onto the 10 judge categories in Appendix B.1 (e.g., 'endless file reading' in the text) | Section 1; Figure 4 caption; Table 3; Section 6.2 ('endless file reading behaviors (17.0%)'); Appendix B.1 category list | error | minor | Fix wording and add a category mapping. Cost: trivial |
| R19 | clarity | Citation errors (E7): the abstract's 'best practices of SWE-Bench [25]' points to 'Swe-bench goes live!'; 'social media posts [1, 25]' points to two arXiv papers | Abstract ('builds upon the best practices of SWE-Bench [25]'); Section 1 ('social media posts [1, 25]'); References [1], [13], [25] | error | minor | Correct the reference numbers. Cost: trivial |
| R20 | novelty | The construction is a refinement of the SWE-bench recipe: the commit-pair / fail2pass sourcing (Section 4.1) follows SWE-bench [13], human verification follows SWE-Bench Verified [15], multi-language follows Multi-SWE-bench [24], contamination freshness is addressed by SWE-bench-Live [25]; the new parts are copyleft/commercial sourcing and requirements/interface augmentation | Section 4.1; Section 3.1 ('Similar to SWE-Bench Verified'); Section 2.1; Section 1 ('to the best of our knowledge, this work is the first') | judgment | major | Position the delta explicitly with a comparison table against SWE-bench, Verified, Multi-SWE-bench, SWE-bench-Live (size, languages, LOC, files, contamination strategy). Cost: low |
| R21 | novelty | Related work omits closely related benchmarks and contamination strategies, e.g., freelance-task SWE evaluation (Miserendino et al., 'SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?', 2025), executable training environments (Pan et al., 'Training Software Engineering Agents and Verifiers with SWE-Gym', 2024; Yang et al., 'SWE-smith: Scaling Data for Software Engineering Agents', 2025), and time-based contamination control (Jain et al., 'LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code', 2024) | Section 2.1-2.2 (none of these discussed) | gap | minor | Add and position these works. Cost: trivial |
| R22 | ethics | Sourcing and consent of commercial code are described inconsistently and incompletely: 'purchased their engineering repos' (Section 3.1) vs 'formal partnership agreements' (Abstract) vs internal assets incl. acquired companies and employee-founded startups (Section 4.1); no statement on secrets/PII scrubbing, licence terms of the GPL derivative, or annotator compensation | Abstract; Section 3.1 ('we contacted the company and purchased their engineering repos'); Section 4.1 ('including companies acquired through mergers and acquisitions') | gap | minor | Add a data statement: sourcing agreements, PII/secret scrubbing, licences, annotator pay; disclose any affiliation of commercial-set sources. Cost: low |
| R23 | significance | Language coverage is narrow for a benchmark framed as 'diverse': Python, Go, JavaScript, TypeScript only; Java, C++, Rust absent (acknowledged) | Section 7.1 ('some widely-used languages like Java, C++, and Rust are underrepresented'); Abstract ('diverse set of 41 actively maintained repositories') | judgment | minor | Scope the claim; plan expansion. Cost: none for wording |
| R24 | experimental_validation | Model coverage is thin for a benchmark paper: only two open-weight models (Qwen-3 32B, SWE-Smith-32B), no strong open coding agents; no analysis of resolve rate vs task size in text | Table 1; Section 6.1; Figure 4 caption | gap | minor | Add 2-3 strong open-weight coding models and a resolve-rate vs LOC/files plot. Cost: moderate GPU budget |
| R25 | technical_rigor | Test validity is not measured in either direction: no estimate of false negatives (valid alternative solutions failing the tests; acknowledged) and no audit of resolved patches for false positives passing weak tests | Section 7.1 Dependency on Test Suite; Section 4.3; not stated after search | gap | major | Manually audit a sample of resolved and unresolved patches per model and report FP/FN rates. Cost: a few engineer-days |
| R26 | experimental_validation | Figure 1's caption lists 'difficulty filtering', but Section 4 describes only size-based exclusion; if tasks were also filtered by model failure, the low resolve rates would be partly by construction | Figure 1 caption ('difficulty filtering'); Section 1 ('we exclude trivial edits (1-10 lines of code)'); Section 3.1 ('problems are naturally challenging') | question | major | State all filtering criteria and whether any model was used to select tasks. Cost: trivial |
| R27 | clarity | Found by P5. The '>70% on SWE-Bench-Verified' claim cites [15], OpenAI's 2024 Verified announcement, which cannot report the 2025 models (GPT-5, Opus 4.1) used in the Figure 2 contrast; the cited source does not support the claim (E7) | Section 1 ('state-of-the-art agents have reported over 70% pass rate on SWE-Bench-Verified [15]'); Figure 2 caption; Reference [15] ('OpenAI, 2024') | error | minor | Cite the actual sources of the >70% numbers with their scaffolds. Cost: trivial |

### Answered

- Flaky or non-deterministic tests make evaluation noisy — answered at Section 3.2 ('we run each set of tests 3 times and filter out any test that doesn't pass consistently'); Section 4.3 Environment verification.
- Agents are failed for misnaming classes or functions the hidden tests expect — answered at Section 3.2 Interface; Appendix A.3.
- One repository could dominate the public set — answered at Section 1 (cap of 100 per repository); public set 731 tasks over 11 repositories = 66.5 per repository (derived).
- The evaluation setting (fully specified vs ambiguous) is not disclosed — answered at Section 5 Issue Ambiguity ('Models are evaluated in the setting without any ambiguity'); Section 7.1 Reduction in Ambiguity.

### Aspect coverage

- significance: A1, A3, A7, A10, A13, A14; R10, R23
- experimental validation: A6, A8; R2, R3, R5, R13, R24, R26
- technical rigor (soundness of the benchmark): A4, A5; R1, R4, R8, R9, R11, R12, R25
- clarity: A11; R6, R7, R14, R17, R18, R19, R27
- reproducibility: A9; R15, R16
- novelty: A2; R20, R21
- ethics: A12; R22
- statistical reporting: R2 (no other statistical tests apply)
- anonymity / venue compliance: considered; see Section 8 (not a scientific reason)
- societal impact (automation of software work): considered, no reason (the paper makes no deployment claim)

Omission sweep (`references/error_audit.md` Section 4): splits — present (public / commercial / held-out, Section 3.3; no tuning involved); seeds, runs, variance — not stated after search (R2); baseline settings — partly present (Section 5), decoding and budgets not stated (R16); hyperparameters — turn cap only (R16); compute — 8 H100 node for open models (Section 5), cost not stated (R16); data licence and consent — partly present (GPL, purchased code), consent and PII not stated (R22); failure cases and limitations — present (Section 6.2, Section 7.1); code and data availability — present for the public set (Section 3.3, p.1 links).

### Pairs

- A1 ↔ R4, R26: is the difficulty gap real and not an artifact of scaffold or selection? (C1)
- A2, A13 ↔ R1: is the benchmark actually contamination-resistant? (C2)
- A3 ↔ R10, R17: does task size support "long-horizon" and "enterprise-level"? (C3)
- A4 ↔ R11, R12: does augmentation produce resolvable tasks without turning them into spec-following? (C4)
- A5 ↔ R25: are the tests valid verifiers? (C4)
- A6 ↔ R2, R3: is the uniform protocol enough to rank models? (C1)
- A7 ↔ R13: what does the commercial gap show? (C5)
- A8 ↔ R5, R6, R8, R9: is the failure analysis reliable? (C6)
- A9 ↔ R15, R16: what can others reproduce? (general)
- A10 ↔ R14, R23: how diverse is it, per subset? (C3)

---

## 3. Reorganized ledger and probes

No duplicates were merged (R6 and R8 bear on the same table but report different errors; R19 and R27 are separate citation problems).

### By claim

**C1: much harder benchmark; frontier models < 25%**
- A1 (checked; holds on Table 1 alone), A6 (checked) ↔ R2 (checked, high swing), R3 (checked, high swing), R4 (checked, high swing), R26 (open, question, unsettled by P1), R7 (checked), R24 (checked), R27 (checked, found by P5)

**C2: contamination-resistant**
- A2 (checked after P4), A13 (checked) ↔ R1 (checked, high swing; decides the pair)

**C3: realistic, long-horizon, diverse**
- A3 (open on subset; see R17), A10 (checked), A14 (checked) ↔ R10 (checked, high swing), R14 (checked), R17 (open, question), R23 (checked)

**C4: augmentation and verification ensure resolvability**
- A4 (checked), A5 (checked) ↔ R11 (checked, high swing; decides the pair), R12 (checked, high swing), R25 (checked)

**C5: commercial gap reflects enterprise complexity**
- A7 (checked) ↔ R13 (checked, medium swing)

**C6: failure modes differ by model size**
- A8 (checked; weakened by R5, R8) ↔ R5 (checked, error), R6 (checked, error), R8 (checked, error), R9 (checked)

**General**
- A9, A11, A12 (checked) ↔ R15, R16, R18, R19, R20 (judgment, high swing for novelty types), R21, R22

Swing ranking (highest first): R11, R1, R4, R3, R2, R5, R12, R10, R20, R26, R9, R13, R25, R8, R16; the rest are low swing.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R26 | Does the paper use any model-based difficulty filter when selecting tasks, beyond excluding 1-10 line edits? | Re-read Sections 1, 3.1, 4.1-4.3 and searched the text for 'filter' and 'difficulty' | unsettled — Figure 1 caption ('difficulty filtering'); Section 1 ('we exclude trivial edits'); no other mention | R26 stays question (open); no type may grade it above minor |
| P2 | R5 | Do the Table 3 counts match the number of unresolved public-set instances? | Recomputed totals from Table 3 counts and expected unresolved = 731 x (1 - resolve rate) | confirmed — Table 3; Table 1; Section 6.2 | R5 question -> error (Opus 920 vs ~565; Gemini 915 vs ~632; GPT-4o 789 vs ~695; Qwen 792 vs ~706) |
| P3 | R6, R8 | Do the failure-mode rates quoted in Sections 1 and 6.2 follow from Table 3? | Recomputed overall shares = column share x Submitted/Not-Submitted share for every model | confirmed — Section 6.2; Table 3 | Opus 35.9/24.2, Sonnet 35.6/17.1, Gemini 38.9/30.6/18.0 reproduce; Qwen tool 44.1 not 42.0 and GPT-5 61.6 is higher -> R6 error; Opus syntax 24.2 vs Qwen 23.2 -> R8 error |
| P4 | R1, A2, A13 | Is any contamination analysis or held-out evaluation reported? | Searched for 'contamina', 'held-out', 'cutoff'; re-read Sections 3.1, 3.3, 5 | confirmed — Section 5 ('we keep the private set held-out for future analysis') | R1 checked (gap confirmed); A2 depends on R1 -> moderate stays, now checked; A13 weak, checked |
| P5 | R4, A1 | Are the >70% SWE-Bench Verified numbers produced under the paper's SWE-Agent configuration? | Traced Figure 2 caption and Section 1 to reference [15] | confirmed — Figure 2 caption; Section 1; Reference [15] 'OpenAI, 2024' | R4 checked; new R27 (citation does not support the claim) found by P5; A1 holds on Table 1 alone |
| P6 | R11, R12 | Does the paper report an ablation without requirements/interface, or annotation QC statistics? | Searched for 'annotat', 'agreement', 'ablation', 'drop'; re-read Sections 3.2, 4.2, 4.3, 5, 7.1, Appendix A | confirmed — Sections 4.2-4.3 (drop rules, no counts); Section 5 Issue Ambiguity | R11, R12 checked (gaps confirmed) |
| P7 | R10, A3 | Is 'hours to days' or 'long-horizon' measured anywhere (human time, turns, trajectory length)? | Searched for 'hours', 'time', 'turn', 'horizon' | confirmed — Abstract only; Section 5 gives only a 200-turn cap | R10 checked; A3 holds for size (LOC/files) only, open on subset (see R17) -> stays moderate |
| P8 | R3, A6 | Are Agentless numbers reported, and how large is the not-submitted share driven by tool errors? | Re-read Section 5 Scaffold; recomputed Table 3 not-submitted tool-use shares | confirmed — Section 5 (no Agentless numbers); Table 3 (GPT-5 63.1% x 97.6% = 61.6% of failures are tool-use non-submissions) | R3 checked; A6 holds (uniform protocol) but uniformity does not remove scaffold dependence |
| P9 | R14, A10 | Does the 50-100 instances per repository rule hold for every subset? | Recomputed 731/11, 276/18, 858/12 | confirmed — Section 1; Section 3.3; Abstract | R14 error (commercial 15.3 per repo); A10 holds for public and held-out (66.5, 71.5) |
| P10 | R2 | Are the top-model differences in Table 1 larger than sampling error? | Binomial SE at p=0.233, N=731; and at p=0.178, N=276 | confirmed — Table 1, Table 2 | R2 checked: SE 1.56 pp (public) and 2.30 pp (commercial); GPT-5 vs Opus gap 0.6 pp |
| P11 | R17 | Can the 107.4 LOC mean be reconciled with 'over 100 tasks' exceeding 100 lines, and which subset is it? | Re-read Section 1 and Figure 3 caption; figure itself unavailable | unsettled — Section 1; Figure 3 caption | R17 stays question (open) |
| P12 | R11 | Do the requirements in the worked example prescribe solution structure (file, symbol, exact values), contrary to 'don’t leak solutions'? (split: T1/T2/T6 major vs T3 minor) | Re-read Appendix A.2 example line by line against the Appendix A.3 interface | partly — Appendix A.2 ('The tuple `STAGED_SOURCES` in `openlibrary/core/imports.py` must include "google_books"'; 'a function named `stage_from_google_books` must') | R11: requirements specify files, symbols and literal values, not the algorithm; T3 grade minor -> major (post-review) |

---

## 4. Reviewer roster

Aspects with at least 12% of the ratio: significance, experimental validation, technical rigor, clarity, reproducibility. Each has a type. Novelty (10%) gets a type because the paper raises a distinct novelty question (R20, the "first" claim of C2). Ethics (4%) has no type; R22 sits in T3's and T4's "Weighs most".

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 SWE-agent benchmark specialist | experimental_validation | the task | builds and evaluates repository-level code benchmarks and agent scaffolds | headroom, controlled comparisons, reliable verifiers | single-scaffold leaderboards, uncontrolled cross-benchmark contrasts, filtering that manufactures difficulty | R2, R3, R4, R11, R13, R24, R26, R7, R17, R25; A1, A3, A6, A10, A8 | high |
| T2 Evaluation and benchmark methodologist | technical_rigor | evaluation science | measurement validity, annotation protocols, LLM-judge validation | claims backed by measurement; reported QC | untested design claims (contamination), unreported annotation pipelines, unvalidated judges, numbers that don't add up | R1, R12, R9, R5, R2, R11, R6, R8, R13, R27; A5, A2, A4, A8 | high |
| T3 Empirical software-engineering (MSR) researcher | significance | empirical SE / mining software repositories | studies real-world change complexity and industrial practice | realism of tasks, industrial relevance, honest framing | "long-horizon" or "enterprise" labels without measures, narrow language mix, commit-derived tasks that are not real issues | R10, R13, R23, R22, R20, R11, R15; A1, A7, A3, A10, A14 | medium |
| T4 Open-benchmark and reproducibility reviewer | reproducibility | datasets-and-benchmarks / open science | maintains public benchmarks and leaderboards | released data, environments, configs; documentation | private test sets with no statistics, missing run configs, undocumented data sourcing | R15, R16, R22, R19, R12; A9, A5, A11, A7 | medium |
| T5 LLM-agents generalist (presentation and claims) | clarity | LLM agents / NLP | broad ML reader who checks that text, tables and claims agree | precise, self-consistent reporting | text-table mismatches, overstated conclusions, unclear statistics | R5, R6, R7, R8, R14, R17, R18, R19, R27, R10; A11, A12, A8 | high |
| T6 Software testing and program-repair researcher | technical_rigor | software testing / automated program repair | test adequacy, patch correctness, overfitting patches | verifiers that accept all and only correct patches | test-suite overfitting, plausible-but-wrong patches, specs that leak the fix | R25, R11, R12, R14, R17, R26; A5, A4 | medium |
| T7 Data-contamination and LLM-evaluation researcher | novelty | LLM evaluation / data contamination (*added*) | contamination detection and contamination-resistant benchmark design | demonstrated, not asserted, contamination resistance; positioning against prior strategies | licence-based arguments without evidence, "first" claims, missing related strategies | R1, R20, R21, R15, R4; A2, A13, A14 | medium |
| TA advocate | significance | the task | a well-informed champion of this benchmark | what the community gains if answerable issues are fixed | — | all reasons graded major by another type | high |

---

## 5. Reviews

### T1: SWE-agent benchmark specialist (experimental_validation; the task)

**Reading of the ledger.**
- Holds: A1 (Table 1 shows real headroom whatever the cause), A3 (4.1 files and 107.4 lines is a meaningful step up from one-to-two-line fixes), A6 (one scaffold, one prompt and one cut-off date is a clean protocol), A10 (41 repositories with a cap). Discounts: A8 (the breakdowns are useful, but Table 3's denominators do not add up, R5).
- R3: major (with GPT-5 abandoning 63.1% of failures on tool-use errors, the ranking measures scaffold fit as much as capability). R4: major (the ">70% vs <25%" contrast is the paper's main selling point and is not run under the same configuration). R2: major (the abstract ranks models 0.6 points apart). R11: major (the specification-heavy task definition changes what the score means; no ablation). R13: minor (interesting but secondary). R24: minor. R26: minor (question; P1 found no model-based filter). R7: minor. R17: minor (question). R25: minor (standard for this benchmark family). R27: minor (the >70% citation does not support the claim).

**Opinion.** As someone who builds these benchmarks, I want this artifact to exist: SWE-Bench Verified no longer separates frontier agents, and a set of multi-file, 100-line tasks in four languages with working Docker environments is exactly what the field needs next (A1, A3). But the paper's evidence for what the numbers mean is thinner than the artifact deserves. Every result comes from one scaffold with a 200-turn cap, and Table 3 shows that scaffold interaction dominates some models' failures (R3). The headline contrast with SWE-Bench Verified compares the paper's own runs with vendor-reported numbers under other scaffolds (R4, R27), so I cannot tell how much of the 70-to-23 drop is task difficulty. Rankings are made from single runs without intervals (R2). And because requirements and interfaces are written from the tests, the benchmark may be measuring specification-following more than issue resolution (R11). Each of these is fixable with runs the authors can afford: Agentless numbers they already have, SWE-Agent on Verified, a requirements ablation, and CIs. With those I would move to accept.

Decisive: R3 (major), R4 (major), R2 (major), A1 (strong).

**Scores.** Pool position 56 (basis: A1 holds; R3, R4, R2 unresolved). Technical Rigor 55, Clarity 64, Novelty 56, Significance 66, Experimental Validation 50, Reproducibility 66, Ethics 60. Overall 3. Confidence 4.

### T2: Evaluation and benchmark methodologist (technical_rigor; evaluation science)

**Reading of the ledger.**
- Holds: A5 (flaky-test removal and human test filtering are the right controls). Discounts: A2 (a design intention, untested; see R1), A4 (the intent is right, but the process that implements it is unmeasured, R12), A8 (R5, R9).
- R1: major (the abstract's central adjective is never measured, and the held-out set built to measure it is unused). R12: major ("human-verified ... to ensure resolvability" needs a funnel, annotator details and agreement). R9: major (a judge that is also a subject, with borrowed validation and a 63.4% "Other" bucket). R5: major (an analysis whose counts exceed its population cannot be interpreted). R2: major. R11: major (construct validity). R6: minor. R8: minor (for me a symptom of R9). R13: minor. R27: minor.

**Opinion.** A benchmark paper's core contribution is a measurement instrument, and I judge it by whether the paper shows the instrument measures what it says. Here the design is sensible but almost every validity claim is asserted rather than demonstrated. "Contamination-resistant" rests on a legal argument about GPL (R1); no experiment compares public and held-out performance, though the held-out set exists for exactly that. "Human-verified and augmented ... to ensure resolvability" comes with no counts of what was dropped, who annotated, or whether anyone solved the tasks (R12). The requirements are derived from the tests, and the paper's own example shows they fix file paths, symbol names and literal values (R11; Appendix A.2), so construct validity needs an ablation. The failure-mode analysis has a judge that grades its own trajectories, no in-domain human agreement, and counts larger than the set (R5, R9). None of this makes the benchmark wrong, but as written the paper reads like a release note. A funnel table, a held-out evaluation and a requirements ablation would change my view.

Decisive: R1 (major), R12 (major), R11 (major), R5 (major).

**Scores.** Pool position 45 (basis: R1, R12, R11, R5). Technical Rigor 44, Clarity 58, Novelty 52, Significance 60, Experimental Validation 48, Reproducibility 60, Ethics 56. Overall 3. Confidence 4.

### T3: Empirical software-engineering (MSR) researcher (significance; empirical SE)

**Reading of the ledger.**
- Holds: A1 (headroom matters for the next year of agent work), A7 (private industrial code is rare and valuable), A3 (multi-file changes are where real maintenance effort lies), A10. Discounts: A14 (four languages, Java and C++ absent).
- R10: major (in SE, "long-horizon" and "hours to days" are measurable; the paper measures only diff size). R13: major (the enterprise-complexity explanation is a claim about the codebases with no statistics on them). R11: minor → **major after P12** (I first took Appendix A.2's "don’t leak solutions" at face value; the example names files, symbols and literals). R23: minor (acknowledged). R22: minor. R20: minor (in my field, a better-constructed dataset is itself the contribution). R15: minor.

**Opinion.** From an empirical-SE viewpoint this is a valuable dataset: commit-derived, multi-file changes from maintained projects, plus a rare private set of industrial code (A7). That is closer to real maintenance work than most agent benchmarks (A3). My concerns are about the claims attached to it. The title and abstract promise "long-horizon" tasks that take "hours to days", but the paper reports only lines and files changed; diff size is a weak proxy for effort, and annotator time estimates would have been cheap to collect (R10). The commercial drop is explained by "greater complexity of enterprise codebases", but the commercial set is never characterized (R13), and with about 15 tasks per repository the per-repo variance alone could explain much of it. I would accept a version that either measures these properties or words the claims to match the evidence. The dataset itself would stand.

Decisive: A1 (strong), A7 (moderate), R10 (major), R13 (major).

**Scores.** Pool position 66 (basis: A1, A7 hold; R10, R13 answerable by measurement or rewording). Technical Rigor 58, Clarity 64, Novelty 60, Significance 68, Experimental Validation 56, Reproducibility 64, Ethics 58. Overall 4. Confidence 4.

### T4: Open-benchmark and reproducibility reviewer (reproducibility; datasets-and-benchmarks)

**Reading of the ledger.**
- Holds: A9 (731 tasks with pre-built Docker images and code is the most useful part of the paper), A5, A11 (the worked instance makes the format reproducible). Discounts: A7 (results on a private set cannot be checked by anyone).
- R16: major (Table 1 cannot be reproduced without model IDs, temperature, budgets and the open-weight tool-parsing method). R15: minor (private sets are inherent to the design, but their statistics should be published). R22: minor. R19: minor. R12: minor (I care that the funnel is documented for maintainers).

**Opinion.** For a benchmark the release matters most, and the public release here is solid: tasks on a public hub, containerized environments built by engineers, flaky-test filtering, and a fully worked example (A9, A5, A11). That is better than many benchmark submissions. Two gaps keep me from a stronger score. First, the evaluation configuration is under-specified (R16): "latest versions as of September 18th, 2025" is not a model identifier, decoding parameters and budgets are missing, and SWE-Smith-32B is not even cited. Without these the leaderboard numbers cannot be reproduced, which matters because the paper's main empirical claim is the leaderboard. Second, two of the three subsets are private, and no statistics are given for them (R15); a held-out set nobody can see is only useful if its properties are documented. Both are documentation fixes, so I lean accept.

Decisive: A9 (strong), A5 (moderate), R16 (major).

**Scores.** Pool position 66 (basis: A9, A5; R16 fixable). Technical Rigor 58, Clarity 64, Novelty 58, Significance 64, Experimental Validation 56, Reproducibility 70, Ethics 60. Overall 4. Confidence 4.

### T5: LLM-agents generalist (clarity; LLM agents / NLP)

**Reading of the ledger.**
- Holds: A11 (the task format and example are clear), A12 (honest limitations). Discounts: A8 (I cannot trust Table 3's narrative given R5, R6, R8).
- R5: major (the analysis table's populations are inconsistent with the set sizes). R8: minor (from a presentation view: the conclusion stated in the introduction does not follow from the table). R6, R7, R14, R18, R19, R27: minor each (individually trivial; together they show the text was not checked against the tables). R17: minor. R10: minor (framing).

**Opinion.** The paper is easy to read at the level of ideas: the motivation, the three subsets and the task format are clear, and the appendix example helps (A11). The problem is precision. I checked every number in the text against the tables and many do not match: Sonnet 4 is 16.3 in the text and 17.6 in Table 1, GPT-4o 3.9 vs 4.9 (R7); Qwen's "highest tool error rate (42.0%)" is 44.1% by the table and not the highest (R6); the introduction's "smaller models fail on syntax" contradicts Table 3, where Opus 4.1 has a slightly larger syntax-error share than Qwen (R8); the per-repository rule fails for the commercial set (R14); and Table 3's counts exceed the set size (R5). Citations are misnumbered (R19, R27). Each is small, but in a benchmark paper whose value is trustworthy numbers they add up. A careful consistency pass and a statistics table would raise my score.

Decisive: R5 (major), R8 (minor), A11 (moderate).

**Scores.** Pool position 56 (basis: R5 and the cluster R6-R8, R14, R19; A11 holds). Technical Rigor 54, Clarity 58, Novelty 56, Significance 62, Experimental Validation 54, Reproducibility 64, Ethics 60. Overall 3. Confidence 3.

### T6: Software testing and program-repair researcher (technical_rigor; software testing / APR)

**Reading of the ledger.**
- Holds: A5 (re-running tests three times and dropping broad tests is standard good practice), A4 (interfaces do prevent a known class of false negatives).
- R25: major (program repair learned long ago that test-passing patches are often wrong; the paper audits neither false positives nor false negatives). R11: major (a specification naming the symbols and values the tests check narrows the patch space). R12: minor. R14: minor. R17: minor. R26: minor (question).

**Opinion.** The test pipeline is carefully engineered (A5), and the interface field solves a real false-negative problem (A4). But the benchmark's verdict on each patch is only as good as its tests, and the paper never measures that. The automated program-repair literature has shown repeatedly that test-suite-passing patches can be incorrect, and that alternative correct patches can fail tests written for the gold patch; the paper acknowledges the second (Section 7.1) but quantifies neither (R25). Combined with requirements that tell the agent which file, symbol and string the tests check (R11; Appendix A.2), I suspect resolve rates measure the ability to satisfy a precise test-derived specification. That is a legitimate thing to measure, but it should be named and its validity shown with a manual patch audit.

Decisive: R25 (major), R11 (major), A5 (moderate).

**Scores.** Pool position 50 (basis: R25, R11; A5 holds). Technical Rigor 48, Clarity 60, Novelty 55, Significance 62, Experimental Validation 50, Reproducibility 62, Ethics 58. Overall 3. Confidence 3.

### T7: Data-contamination and LLM-evaluation researcher (novelty; LLM evaluation / contamination, added)

**Reading of the ledger.**
- Holds: A2 (licence-based plus private sourcing is a distinct strategy from the temporal freshness of live benchmarks), A13 (a held-out mirror is the right instrument). Discounts: A14 (multi-language SWE evaluation already exists, Multi-SWE-bench [24]).
- R1: major (the novel part of the design is exactly the part that is not tested; GPL code is public on GitHub, and a licence does not stop a crawler). R20: major (the rest of the construction follows the SWE-bench recipe). R21: minor (time-based contamination control, e.g. LiveCodeBench, should be discussed). R15: minor. R4: minor. R10: minor (framing; T3's field judges it).

**Opinion.** The paper's claimed novelty is its contamination strategy (A2): copyleft licensing for the public and held-out sets, and private commercial code. The private set is genuinely contamination-resistant by construction. The copyleft argument is weaker: GPL repositories are public, and whether training corpora exclude them is a policy question the paper does not examine (R1). The paper also has the instrument to test it, a held-out set mirroring the public one, and leaves it for "future analysis". Beyond that, the construction is a careful refinement of SWE-bench, Verified, Multi-SWE-bench and SWE-bench-Live (R20), so the conceptual delta is moderate. Contribution check: the reader learns that frontier agents resolve about a quarter of larger, specification-augmented tasks; the delta is a refinement of an existing benchmark (question 3 fails); the framing ("long-horizon", "contamination-resistant") outruns the setting (question 2 fails, R1, R10). A public-vs-held-out comparison would substantively raise my view.

Decisive: R1 (major), R20 (major), A2 (moderate).

**Scores.** Pool position 50 (basis: R1, R20; A2 partly holds). Technical Rigor 50, Clarity 62, Novelty 50, Significance 60, Experimental Validation 52, Reproducibility 62, Ethics 58. Overall 3. Confidence 3.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P12 | T1, T2, T6 (major) vs T3 (minor) on R11 | Do the Appendix A.2 requirements prescribe solution structure, contrary to "don’t leak solutions"? | partly — the example fixes the file (`openlibrary/core/imports.py`), the tuple and its new literal (`"google_books"`), the function name `stage_from_google_books`, the URL format and the fallback condition; it does not give the algorithm | T3: R11 minor → major (updated after P12; not among T3's decisive items, so its scores are unchanged) |

Other splits rest on values (R20, R13, R10, R1) and stay; see the consensus map. One round only.

### TA: advocate (significance; the task)

**Reading of the ledger.** Sorting every reason another type graded major:
- Answerable (graded minor here): R2 (CIs from existing runs; soften one sentence), R3 (Agentless numbers already run, per Section 5), R4 (tone down or add one run on Verified), R1 (reword "contamination-resistant" to "designed to reduce contamination" and publish the held-out comparison when run), R9 (report the human-validation numbers the authors say they used to choose 20 turns), R10 (drop "hours to days" or add annotator estimates), R11 (state that the benchmark measures specification-guided resolution; the setting is already disclosed in Section 5 and Section 7.1), R12 (a funnel table from records the pipeline already has), R13 (statistics of the commercial set), R16 (a configuration table), R25 (an audit sample of existing patches), R8 (rewording to match Table 3).
- Blocking (grade kept): R5 (an error, never answerable: major), R20 (the delta over SWE-bench is what it is: major).
- Holds: A1 (strong), A9 (strong), A7, A2 (the private commercial set is contamination-resistant by construction, even if the GPL argument is untested). Discounts: A8 (until R5 is fixed).

**Opinion.** An area chair should want this paper for one reason: it gives the community the next SWE-bench, at the moment the current one stops discriminating (A1), with a public release that others can run (A9), and with a private industrial set no other public benchmark offers (A7). A reader at ICLR gains a harder, multi-language, containerized benchmark and a first map of where frontier agents fail. Nearly everything the other types object to is about how the paper argues for the artifact, not about the artifact: missing intervals, a second scaffold, softer adjectives, a funnel table, configuration details. A camera-ready revision can answer these. Two things cannot be argued away. The failure-analysis table has an unexplained population error (R5), and the construction is a refinement of SWE-bench rather than a new idea (R20). With those, I place the paper just above the accept line, not well above it.

Decisive: A1 (strong), A9 (strong), R5 (major), R20 (major).

**Scores.** Pool position 70 (basis: A1, A9, A7; answerable reasons answered; R5, R20 remain). Technical Rigor 62, Clarity 66, Novelty 62, Significance 72, Experimental Validation 60, Reproducibility 70, Ethics 62. Overall 4. Confidence 3.


---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 (SWE-agent benchmark specialist) | experimental_validation | 0.195 | 56 | 3 | 4 |
| T2 (Evaluation and benchmark methodologist) | technical_rigor | 0.088 | 45 | 3 | 4 |
| T3 (Empirical software-engineering (MSR) researcher) | significance | 0.107 | 66 | 4 | 4 |
| T4 (Open-benchmark and reproducibility reviewer) | reproducibility | 0.146 | 66 | 4 | 4 |
| T5 (LLM-agents generalist (presentation and claims)) | clarity | 0.161 | 56 | 3 | 3 |
| T6 (Software testing and program-repair researcher) | technical_rigor | 0.088 | 50 | 3 | 3 |
| T7 (Data-contamination and LLM-evaluation researcher) | novelty | 0.107 | 50 | 3 | 3 |
| TA (advocate) | significance | 0.107 | 70 | 4 | 3 |

- **Aspect-weighted rating:** 3.361 → **final rating 3 (Borderline Reject)**; ICLR's own label for the same number: **4 on {0, 2, 4, 6, 8, 10}** (5 on the earlier {1, 3, 5, 6, 8, 10} scale). Scale status: secondary ("recent forms use…; verify against the current form").
- ICLR sub-scores from the script: Soundness 2, Presentation 3, Contribution 2.
- Weighted pool position 57.9; plain mean 3.38; spread 1 (3 to 4).
- Uncovered aspects and warnings: ethics (4%) has no type of its own and is renormalized away; the script reported no warnings.
- The rating is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

**Paper type**: benchmark  
**Weights**: Technical Rigor 0.15, Clarity & Presentation 0.15, Novelty & Originality 0.10, Significance & Impact 0.20, Experimental Validation 0.20, Reproducibility 0.15, Ethical Compliance 0.05

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| T1 (SWE-agent benchmark specialist) | 4 | 0.85 | 1.00 | 14% |
| T2 (Evaluation and benchmark methodologist) | 4 | 0.85 | 1.00 | 14% |
| T3 (Empirical software-engineering (MSR) researcher) | 4 | 0.85 | 1.00 | 14% |
| T4 (Open-benchmark and reproducibility reviewer) | 4 | 0.85 | 1.00 | 14% |
| T5 (LLM-agents generalist (presentation and claims)) | 3 | 0.70 | 1.00 | 11% |
| T6 (Software testing and program-repair researcher) | 3 | 0.70 | 1.00 | 11% |
| T7 (Data-contamination and LLM-evaluation researcher) | 3 | 0.70 | 1.00 | 11% |
| TA (advocate) | 3 | 0.70 | 1.00 | 11% |

*No EIC quality weights given yet: the EIC assessment uses confidence only. Add `eic_weight` (0.5-1.5) per reviewer after the EIC's meta-review.*

#### Official scores and EIC assessment

| Dimension | T1 (SWE-agent benchmark specialist) | T2 (Evaluation and benchmark methodologist) | T3 (Empirical software-engineering (MSR) researcher) | T4 (Open-benchmark and reproducibility reviewer) | T5 (LLM-agents generalist (presentation and claims)) | T6 (Software testing and program-repair researcher) | T7 (Data-contamination and LLM-evaluation researcher) | TA (advocate) | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 55 | 44 | 58 | 58 | 54 | 48 | 50 | 62 | 53.6 | 53.6 | 18 |
| Clarity & Presentation | 64 | 58 | 64 | 64 | 58 | 60 | 62 | 66 | 62.0 | 62.0 | 8 |
| Novelty & Originality | 56 | 52 | 60 | 58 | 56 | 55 | 50 | 62 | 56.1 | 56.2 | 12 |
| Significance & Impact | 66 | 60 | 68 | 64 | 62 | 62 | 60 | 72 | 64.2 | 64.3 | 12 |
| Experimental Validation | 50 | 48 | 56 | 56 | 54 | 50 | 52 | 60 | 53.2 | 53.2 | 12 |
| Reproducibility | 66 | 60 | 64 | 70 | 64 | 62 | 62 | 70 | 64.8 | 64.8 | 10 |
| Ethical Compliance | 60 | 56 | 58 | 60 | 60 | 58 | 58 | 62 | 59.0 | 59.0 | 6 |
| **Composite** | 59.6 | 53.9 | 61.6 | 61.6 | 58.2 | 56.3 | 56.4 | 65.4 | **59.1** | **59.1** | |
| Pool position (P%) | 56 | 45 | 66 | 66 | 56 | 50 | 50 | 70 | | | |

#### Ratings (the decision's starting point)

**Official reviewer ratings (Overall 1-6)**: T1 (SWE-agent benchmark specialist) 3, T2 (Evaluation and benchmark methodologist) 3, T3 (Empirical software-engineering (MSR) researcher) 4, T4 (Open-benchmark and reproducibility reviewer) 4, T5 (LLM-agents generalist (presentation and claims)) 3, T6 (Software testing and program-repair researcher) 3, T7 (Data-contamination and LLM-evaluation researcher) 3, TA (advocate) 4 → official mean **3.38**  
**EIC-weighted rating** (internal): **3.39** (+0.01 vs. official) → starting point **3 (Borderline Reject)**

⚠ = spread > 20 points: discuss this disagreement in the decision.

**Composite cross-check (0-100)**: official 59.1 → 3 · EIC-weighted 59.1 → 3 (+0.0 vs. official)  
**Decision ceiling**: none (no upheld DA-CRITICAL issue). The EIC's decision starts from the EIC-weighted rating and may depart from it in either direction, with a written reason.
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (SWE-agent benchmark specialist) | experimental_validation | 19% | 0.195 |
| T2 (Evaluation and benchmark methodologist) | technical_rigor | 17% | 0.088 |
| T3 (Empirical software-engineering (MSR) researcher) | significance | 21% | 0.107 |
| T4 (Open-benchmark and reproducibility reviewer) | reproducibility | 14% | 0.146 |
| T5 (LLM-agents generalist (presentation and claims)) | clarity | 15% | 0.161 |
| T6 (Software testing and program-repair researcher) | technical_rigor | 17% | 0.088 |
| T7 (Data-contamination and LLM-evaluation researcher) | novelty | 10% | 0.107 |
| TA (advocate) | significance | 21% | 0.107 |

**Final rating (aspect-weighted mean)**: **3.36** → **3 (Borderline Reject)** · plain mean 3.38 · weighted pool position 57.9
### Cross-Venue Outlook

| Venue | Venue-weighted composite | Bar offset | Venue shift | Band → with DA cap | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|---|
| ICLR (2026) | 59.1 | +0 | +0 | 3 → 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) | Soundness 2, Presentation 3, Contribution 2 | secondary |

Emphasis weights are this skill's heuristics, not official venue weights. Scale status: official / confirmed / secondary / assumed / unpublished (see references/venue_profiles.md). Upheld DA-CRITICAL caps apply to every venue.

- **ICLR**: Soundness/Presentation/Contribution 1-4 and Confidence 1-5 are long-standing. Overall rating reported as {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}. Both are shown.


</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| A1 | 3 of 8 | held: T1, T3, TA; discounted: — |
| A2 | 3 of 8 | held: T7, TA; discounted: T2 |
| A3 | 2 of 8 | held: T1, T3; discounted: — |
| A4 | 2 of 8 | held: T6; discounted: T2 |
| A5 | 3 of 8 | held: T2, T4, T6; discounted: — |
| A6 | 1 of 8 | held: T1; discounted: — |
| A7 | 3 of 8 | held: T3, TA; discounted: T4 |
| A8 | 4 of 8 | held: —; discounted: T1, T2, T5, TA |
| A9 | 2 of 8 | held: T4, TA; discounted: — |
| A10 | 2 of 8 | held: T1, T3; discounted: — |
| A11 | 2 of 8 | held: T4, T5; discounted: — |
| A12 | 1 of 8 | held: T5; discounted: — |
| A13 | 1 of 8 | held: T7; discounted: — |
| A14 | 2 of 8 | held: —; discounted: T3, T7 |
| R1 | 3 of 8 | T2 major, T7 major, TA minor |
| R2 | 3 of 8 | T1 major, T2 major, TA minor |
| R3 | 2 of 8 | T1 major, TA minor |
| R4 | 3 of 8 | T1 major, T7 minor, TA minor |
| R5 | 3 of 8 | T2 major, T5 major, TA major |
| R6 | 2 of 8 | T2 minor, T5 minor |
| R7 | 2 of 8 | T1 minor, T5 minor |
| R8 | 3 of 8 | T2 minor, T5 minor, TA minor |
| R9 | 2 of 8 | T2 major, TA minor |
| R10 | 4 of 8 | T3 major, T5 minor, T7 minor, TA minor |
| R11 | 5 of 8 | T1 major, T2 major, T3 major, T6 major, TA minor |
| R12 | 4 of 8 | T2 major, T4 minor, T6 minor, TA minor |
| R13 | 4 of 8 | T1 minor, T2 minor, T3 major, TA minor |
| R14 | 2 of 8 | T5 minor, T6 minor |
| R15 | 3 of 8 | T3 minor, T4 minor, T7 minor |
| R16 | 2 of 8 | T4 major, TA minor |
| R17 | 3 of 8 | T1 minor, T5 minor, T6 minor |
| R18 | 1 of 8 | T5 minor |
| R19 | 2 of 8 | T4 minor, T5 minor |
| R20 | 3 of 8 | T3 minor, T7 major, TA major |
| R21 | 1 of 8 | T7 minor |
| R22 | 2 of 8 | T3 minor, T4 minor |
| R23 | 1 of 8 | T3 minor |
| R24 | 1 of 8 | T1 minor |
| R25 | 3 of 8 | T1 minor, T6 major, TA minor |
| R26 | 2 of 8 | T1 minor, T6 minor |
| R27 | 3 of 8 | T1 minor, T2 minor, T5 minor |

Value splits that remain (not settled by a probe, by design): R20 (T7 and TA major vs T3 minor: how much a refinement of the SWE-bench recipe matters), R13 (T3 major vs T1 and T2 minor), R10 (T3 major vs T5, T7 and TA minor), R1 (T2 and T7 major vs TA minor as answerable by rewording).

### Key strengths

- A1: a benchmark with real headroom where SWE-Bench Verified is saturating (Table 1) — held by 3 of 8 types (T1, T3, TA), discounted by none.
- A5: careful environment and test verification (Sections 3.2, 4.3) — held by 3 of 8 (T2, T4, T6).
- A9: public release of 731 tasks with Docker environments (Section 3.3) — held by T4 and TA.
- A7: a private enterprise-code set with reported results (Table 2) — held by T3 and TA.
- A3 / A10: larger, multi-file tasks across 41 repositories (Section 1) — held by T1 and T3.

### Top concerns (at most five)

1. R11: requirements and interfaces are derived from the tests and gold patch and prescribe files, symbols and literal values (Appendix A.2; Section 3.2), with no ablation of their effect. Fix: ablate statement-only vs + requirements vs + interface on the public set; audit a sample for leakage (moderate API budget plus annotation).
2. R5: Table 3 classifies more failed trajectories than the public set has instances (Opus 4.1 920 vs about 565 unresolved; Section 6.2, Table 3). Fix: state the population and recompute (low cost).
3. R1: contamination resistance is asserted, not tested; the held-out set is never evaluated (Section 3.1; Section 5). Fix: evaluate the held-out set against the public set and add a commit-date or memorization analysis, or soften the claim (days of API budget).
4. R2: single-run Pass@1 without intervals; GPT-5 vs Opus 4.1 differ by 0.6 points against an SE of about 1.6 (Table 1; Abstract). Fix: report CIs from existing runs; repeat top models (none to moderate).
5. R20: the construction refines the SWE-bench recipe (Section 4.1; Section 3.1); the paper does not position its delta against SWE-bench, Verified, Multi-SWE-bench and SWE-bench-Live. Fix: a comparison table (low cost).

### Revision Roadmap

Priority 1 is R11 only: graded major by 4 of 8 types (T1, T2, T6, T3 after P12); no reason was graded fatal.

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R11 | Ablate requirements and interface (statement only / + requirements / + interface) on the public set for 2-3 models; audit 50 requirements for solution leakage; reframe the task as specification-guided issue resolution if the gap is large | moderate API budget, ~2 annotator-days |
| 2 | R5 | Define the population of Table 3 and recompute | low |
| 2 | R1 | Evaluate the held-out set; commit-date vs model-cutoff analysis; or soften "contamination-resistant" | days of API budget |
| 2 | R2 | Binomial/bootstrap 95% CIs for Tables 1-2; 3 runs for the top models; soften "highest score to date" | none to moderate |
| 2 | R20 | Comparison table vs SWE-bench, SWE-Bench Verified, Multi-SWE-bench, SWE-bench-Live | low |
| 2 | R3 | Report the Agentless numbers; add a second scaffold for the top models; turn-limit sensitivity | moderate API budget |
| 2 | R4 | Run the same SWE-Agent configuration on SWE-Bench Verified for the same models | low-moderate API budget |
| 2 | R9 | Human-judge agreement per model on a labelled sample; a second judge model; refine "Other" | a few annotator-days |
| 2 | R10 | Human solve-time estimates and trajectory-length statistics, or drop "long-horizon" / "hours to days" | low-moderate |
| 2 | R12 | Pipeline funnel table, annotator details and agreement, human-solvability check on a sample | low to moderate |
| 2 | R13 | Complexity statistics for the commercial set; matched-size comparison | low |
| 2 | R16 | Per-model configuration table (IDs, temperature, budgets, tool parsing); release trajectories; cite SWE-smith | low |
| 2 | R25 | Manual audit of resolved and unresolved patches for false positives and negatives | a few engineer-days |
| 3 | R6, R7, R8, R14, R18, R19, R27 | Correct text-table mismatches, failure-mode statements, per-repo rule, captions, category mapping and citations | trivial to low |
| 3 | R15, R17, R21, R22, R23, R24, R26 | Private-set statistics and submission protocol; per-subset statistics table; related work (SWE-Lancer, SWE-Gym, SWE-smith, LiveCodeBench); data statement; scope "diverse"; more open-weight models; state all filtering criteria | low to moderate |

---

## 8. Integrity signals and limitations

- **Integrity signals:** `integrity_scan.py` found no reviewer-directed text or hidden characters, and none was seen while reading. These never change a score.
- **Anonymity (for the editor, not a scientific reason):** the blinded copy still names an organization in Section 4.1 (p. 6), in the sentence on private-repository sourcing, right after a removed affiliation. The name is not repeated here. It may be a residue of the blinding step rather than of the submission. It was ignored for scoring.
- **Recognition:** the reviewer recognized this benchmark from prior knowledge. Nothing about its later reception was used; novelty and significance were judged from the manuscript alone.
- **Limitations:** Figures 1-4 were not readable (Figure 3 statistics and Figure 4 breakdowns judged from captions; R17 and R26 stay questions partly for this reason). No literature check ran (no network); the related-work gaps in R21 come from memory, with confidence that the named works exist. The types share one context, so their agreement is not independent confirmation.
