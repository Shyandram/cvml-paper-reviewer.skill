# Academic Paper Review — "The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation" (DC-CoT)

*Simulation of how a careful ICLR panel would likely see this draft; not a prediction of the real outcome. Date: 2026-11-10. Mode: full, confirmation skipped. Literature check: strict, cutoff 2025-09-24. Figures were not available (text extraction only): Figures 1–6 are judged from captions and surrounding text. The five reviewer passes were run one after another in one shared model context (no subagents), each working from its role file, the paper text and the paper memory; they share a context and are not independent agents.*

---

## Phase 0 — Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation |
| Primary Discipline | Machine learning → LLM reasoning, chain-of-thought (CoT) distillation, synthetic-data curation |
| Secondary Discipline(s) | Agent evaluation (WebArena), vision-language reasoning (Visual-CoT, OK-VQA), data-centric AI |
| Paper Type | Benchmark (composite weights: benchmark) — an empirical comparison of existing methods; no new method or new test set |
| Core Technique(s) | Teacher-generated CoT; LoRA SFT of 0.5–8B students; augmentation (question rephrasing, question augmentation, answer augmentation, reverse thinking), selection (teacher-correct, student-error, LLM judge), mixing (length, teacher) |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | None. Submission is public and the PDF can be revised during discussion, so fixable vs. fundamental issues are separated in the Roadmap |
| Paper Maturity | Submission-ready in form ("Preprint. Under review."), but numbers and text disagree in several places (see R1 Error Log) |
| Ethics-Relevant Content | Outputs of proprietary teacher APIs used to train student models and released as a dataset; NC-licensed source data (Table 6: ANLI, e-SNLI "CC BY-NC 4.0"); no human subjects |
| Integrity scan | `integrity_scan.py` on the full text: "No reviewer-directed text or hidden characters found." No instructions addressed to reviewers or AI systems were seen while reading. The `--redact` copy was not written (shell file creation was not permitted in this run); since the scan found nothing, the reviewers read the original text, which is equivalent to the redacted copy. |

### Claimed Contributions (as stated by the authors)
1. **C1** — "DC-CoT, the first data-centric benchmark that investigates data manipulation in chain-of-thought (CoT) distillation from method, model and data perspectives" (Abstract; §1 contribution ①).
2. **C2** — "extensive experiments across diverse teacher–student pairs, tasks, and datasets, offering the first large-scale empirical overview of CoT distillation" (§1 ②).
3. **C3** — "actionable guidelines — e.g., which augmentation boosts generalization, which filtering criterion balances quality and coverage, and when heterogeneous teacher mixtures help" (§1 ③).
4. Findings F1–F3 (§1, §4): F1 augmentation is "generally the most effective approach"; F2 "compatibility and learnability" matter for teacher–student pairs; F3 "distinct scaling behaviors" and generalization across datasets.

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Teachers (§4.1): Gemini-1.5-Pro, GPT-4, Claude-3.5 Sonnet, GPT-4.1 mini, o4 mini; judges: LLama-2-70B (text), GPT-4o-mini (agentic), GPT-4/4.1-mini (visual). Students (§4.1): Llama-3.1-8B, Llama-3.1-8B-R1 Distilled, Mistral-7B, Gemma-7B, Qwen-2.5-7B; Qwen-2.5 0.5–7B (§4.3.2, Fig. 5); Qwen-2.5-VL-3B (Table 3). Whether students are base or instruct models: not stated after search. Training (App. C.1): LoRA rank 32, alpha 64; text tasks "10 epochs for each dataset"; agentic 5 epochs, lr 5e-5, context 10,000; visual 1 epoch, lr 5e-5; LLaMA-Factory; 8×A100 + 16×A6000. Text-task learning rate, batch size, seeds: not stated. Splits (Table 6): Train (Original), Train (Filtered), Test only — no validation split; e.g. SQA test 229, Date test 169 (train 200), ANLI r3 test 1,200 with 883 filtered train examples, Visual-CoT "Train (Original) 132,000 / Train (Filtered) 943,000". Runs: Table 1 "mean of three independent runs" (textual); Table 2 "three-run averages"; no standard deviations anywhere.
- **Headline numbers.** Table 1 (Llama-3.1-8B): textual averages Vanilla CoT 41.81, Reverse Thinking 66.45, Teacher-correct filtering 44.73, Judge 41.04, Teacher mixing 41.97, Length mixing 41.43, "No Selection/No Mixing" 42.80; Q1 text: "24.64%↑" for Reverse. Table 2: teacher × student textual averages 51.24–66.45. Table 3: WebArena and Visual-CoT by teacher. Table 4: seed-data 25/50/75/100%. Table 5: zero-shot vs OOD accuracy for ten source→target pairs. Fig. 5–6: size and data-volume curves (not readable here).
- **Appendix.** A Limitations (budget; "GPT-o4" not included); B Broader Impact (positive only); C training/inference; D related work; E one WebArena prompt/response example; F Table 6 dataset statistics. No prompts for rephrasing/augmentation/judging, no values for L, τ, α.
- **Unverifiable.** Figures 1–6; dataset/code links ("The dataset can be found here", links removed in the blinded text).

### Literature check (Phase 1.5; strict; arXiv only; cutoff 2025-09-24)
Fingerprint written; 7 queries run (3 claim queries C1–C3 + 1 claim-C2 selection query, 1 expansion, 2 baseline/benchmark), 12 allowed; the `benchmarks`, `scout` and `coverage` subcommands were not run (budget), and the two baseline-purpose queries (WebArena trajectories, GSM8K/MATH distillation) returned no abstracts reporting comparable numbers, so no baseline scout table can be built. `similarity` flagged only the paper's own source of Reverse Thinking (cosine 0.313; cited as [6]) with 0 shared 8-grams; no text-overlap flags. Novelty profile (`novelty`): C1 **high** (no prior data-centric CoT-distillation benchmark found in this arXiv-only search; at most medium by the rule that an empty search is not evidence); C2 **medium**; C3 **incremental** (learnability gap already reported by a prior, cited work). "Worth discussing" only: OpenThoughts (recent preprint) and MiCoTA (recent preprint).

### Review Team (fictional personas)

**EIC (meta-reviewer): Prof. Amara Lindqvist-Osei**, large public research university (Northern Europe). Senior faculty; LLM post-training and evaluation. Role: reads all five reports, checks decisive points against the paper, weights reviewers, rules on DA-CRITICAL, decides. Style: weighs contribution against the venue's accepted-paper weaknesses; dislikes text-table mismatches.

**Reviewer 1 (Methodology): Dr. Kenji Aldermoor**, industrial research lab (East Asia). Senior scientist; SFT/LoRA training protocols, synthetic-data evaluation. Focus: design, statistics, fairness of comparison, reproducibility. Style: recomputes every table average, insists on matched compute/data budgets.

**Reviewer 2 (Domain): Prof. Rosalind Ekwueme**, private research university (North America). Senior faculty; knowledge distillation and reasoning in LLMs. Focus: literature, positioning, domain contribution. Style: reads cited abstracts against the claims made about them.

**Reviewer 3 (Perspective): Dr. Mateus Valderrama**, applied-ML lab at a public university (Latin America). Mid-career; learning sciences (curriculum design) and efficient on-device ML. Focus: cross-disciplinary links, deployment, assumptions, broader impact. Style: constructive, looks for what the work could become.

**Reviewer 4 (Generalist): Dr. Priya Raghunathan-Holt**, academic group (South Asia). Postdoc; NLP generalist. Focus: contribution clarity, venue fit, presentation. Style: the typical program-committee member; wants a clear take-home message.

**Devil's Advocate: Prof. Henrik Soleimani**, evaluation-methodology group (Western Europe). Senior faculty; causal inference and experimental design for ML. Focus: core-argument challenges, logic, overclaiming. Style: rigorous, never hostile.

*Personas are fictional.*

---

# Phase 1 — Independent Reports

---

# Peer Review Report — Reviewer 1 (Methodology)

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Reviewer: Dr. Kenji Aldermoor, Methodology (industrial research lab, East Asia; fictional persona)
## Expertise: LoRA/SFT training protocols; synthetic-data evaluation; statistical reporting
## Date: 2026-11-10

### Protocol sweep (search of the whole text, appendix included)
Statements on splits and selection: Table 6 lists only "Train (Original)", "Train (Filtered)" and "Test" — no validation split for any dataset; App. C.1: "For Textual tasks, we train for 10 epochs for each dataset." — one fixed budget regardless of dataset size; no hyper-parameter search is described anywhere; §4.3.1: "For textual reasoning tasks, we utilize the best-performing augmentation approach, Reverse" (the choice of Reverse is made from the Table 1 test accuracies); §3.1.2 threshold τ for the LLM judge, §3.1.3 mixing ratio α and §3.1.1 sample count L: values not stated after search. Which split is used for training/tuning/selection: tuning not described; selection of the method carried into Tables 2/4/Fig. 5 is on the reported test split (consequence discussed under W5).

## Summary
The paper assembles DC-CoT, a set of experiments that compare three families of data manipulation for distilling teacher chain-of-thought into 0.5–8B students: four augmentations (question rephrasing, question augmentation, answer augmentation, reverse thinking), three selection rules (teacher correctness, student error, LLM judge) and two mixing schemes (length, teacher). Students are fine-tuned with LoRA on seven text tasks, WebArena and Visual-CoT, and evaluated in-distribution and on ten source→target pairs. The reported take-aways are that augmentation, and reverse thinking in particular, gives the largest gains, that teacher–student compatibility matters, and that more data does not always help.

## Strengths
### S1: Broad, practically relevant factorial design
The method × teacher × student × data-volume × transfer layout (§4.2–§4.4, Tables 1–5) covers text, agentic and visual tasks with one training recipe, which is rare for distillation studies and gives a useful common reference point. The inclusion of negative results (mixing does not help on average, §4.2 Q2; Vanilla CoT degrades with more data, Table 4) is valuable and honest.
### S2: Mostly internally arithmetic-consistent tables
I recomputed the textual averages in Tables 1 and 2 and Table 4's AVG column; they match to rounding (e.g., Table 1 Reverse: (72.49+78.46+82.17+35.52+76.35+49.75+70.41)/7 = 66.45; Table 2 Llama/GPT-4: 451.51/7 = 64.50). Reported test sizes (Table 6) are consistent with the reported percentages (e.g., Date 70.41% = 119/169).
### S3: Training and inference settings are partly disclosed
App. C.1–C.2 give LoRA rank/alpha, epochs and learning rates for agentic/visual runs, hardware, and the vLLM inference stack; App. E shows a WebArena example.

## Weaknesses

### W1: Augmentation gains are confounded with training-set size and optimisation budget
Rephrasing, question augmentation and answer augmentation produce L extra samples per seed item (§3.1.1 ❶–❸), and reverse thinking adds a backward question and reasoning per item (§3.1.1 ❹); selection removes data (Table 6: ANLI 100,459 → 883). The authors train every configuration for "10 epochs for each dataset" (App. C.1), so augmented runs see several times more gradient steps and tokens than Vanilla CoT. The headline conclusion — "data augmentation offers the most substantial performance gains by enriching reasoning trace diversity and complexity" (§5) — attributes the gain to diversity, but no experiment holds the number of examples/tokens/steps fixed, and the post-augmentation training-set sizes are not reported anywhere (Table 6 has only "Train (Filtered)"). The same confound applies in reverse to selection (fewer examples, same epochs).
- **Suggested Fix**: add a matched-budget arm (same number of training examples/steps for Vanilla, Answer-Aug and Reverse; e.g., subsample the augmented pool to |D_source|) and report post-manipulation dataset sizes in Table 6. Cost: ≈ 4 methods × 7 text tasks × 3 seeds ≈ 84 LoRA runs on an 8B student ≈ 100–150 A100-hours.

### W2: Baselines in Table 1 are inconsistent and some are implausible, which inflates or distorts the deltas
(a) The "No Selection" and "No Mixing" rows reuse the "No CoT" textual numbers (59.89, 65.36, 60.41, 7.39, 20.74, 35.42, 50.37; average 42.80), while their WebArena value (22.78) is Vanilla CoT's and their Visual-CoT value (44.52) is Zero-Shot CoT's. The reference for the selection and mixing comparisons is therefore a hybrid that is not the unfiltered-CoT baseline the text describes. Against Vanilla CoT (41.81, which *is* the unfiltered teacher-CoT run) the effects are: Teacher-correct +2.92, Student-error +2.06, Judge −0.77, Length mixing −0.38, Teacher mixing +0.16 (my recomputation). (b) Vanilla CoT distillation is worse than fine-tuning without CoT on the textual average (41.81 vs 42.80), on WebArena (22.78 vs 30.05) and on Visual-CoT (45.44 vs 46.66); MATH after Vanilla CoT is 4.38, below zero-shot 9.32; ANLI after Vanilla CoT is 23.92, below the 33.83 zero-shot and below the 33% chance level of a three-way task. These patterns suggest an under-tuned or mis-parsed vanilla baseline (e.g., 10 epochs of LoRA overfitting, answer-extraction failures), which makes the large Reverse/Answer-Augmentation "gains" over Vanilla (+24.64 and +15.77 points) partly gains over a weak reference. The paper never discusses why CoT distillation hurts on agentic/visual tasks (No CoT average 38.36 vs Vanilla CoT 34.11).
- **Suggested Fix**: correct the Table 1 rows, report each selector/mixer against the same Vanilla-CoT run, add a tuned (LR/epochs on a validation split) Vanilla baseline, and document the answer-extraction procedure; check ANLI/MATH outputs for format failures.

### W3: No variance, no significance tests, small test sets
Table 1's caption says textual scores are "the mean of three independent runs" but no standard deviation is given in Tables 1–5 and the agentic/visual and size/volume results (Table 3, Fig. 5–6) do not state the number of runs. With test sets of 229 (SQA) and 169 (Date) items (Table 6) the binomial standard error is ≈ 3.2 and ≈ 3.8 points (my computation, p ≈ 0.6/0.5), which is as large as most differences the text interprets: teacher comparisons in Table 2 are mostly ≤ 2 points (e.g., Llama-3.1-8B-R1: 62.74 vs 63.11), Table 3 differs by 0.24 (45.44 vs 45.20) between GPT-4-mini and o4-mini, and selector differences per column are 1–3 points (Table 1).
- **Suggested Fix**: report mean ± std over seeds for all tables, paired bootstrap CIs on the test items for the key contrasts, and avoid ranking teachers/selectors whose difference is within noise.

### W4: Several stated findings are contradicted by the paper's own tables
(i) §4.2 Q2: "LLM-as-a-Judge filtering is highly effective, often surpassing simpler heuristics" — Table 1 gives the Judge the lowest textual average of the three selectors (41.04 vs 44.73 and 43.87), below No Selection (42.80), and WebArena drops from 22.78 to 15.64; §5 nevertheless says selection "using methods such as LLM-as-a-Judge ... is crucial". (ii) §4.2 Q1 reports Teacher-correct as "+1.93↑ over Vanilla CoT" and Teacher mixing as "a marginal decrease of 0.83%↓ over Vanilla CoT": both use the 42.80 reference (+1.93 = 44.73 − 42.80; −0.83 = 41.97 − 42.80); against Vanilla CoT (41.81) they are +2.92 and +0.16. (iii) §4.2 Q3 advises that "combining effective augmentation with suitable filtering or mixing can yield further improvements", but no combined configuration is run anywhere (Tables 1–5 vary one axis at a time). (iv) §4.4.2 Q11: "Table 5 consistently shows..." substantial OOD gains, while 3 of the 10 pairs show no gain or a loss (GSM8K→MATH 9.32→8.75; Visual-CoT→OK-VQA 42.10→38.90; OK-VQA→Visual-CoT 44.52→44.62, +0.10, described as "improves").
- **Suggested Fix**: rewrite Q1–Q3, §5 and contribution ③ to what the tables show, or run the combined pipelines.

### W5: Protocol — no validation split, method choice made on test, hyper-parameters unspecified
Table 6 has no validation split; the recommended per-task strategies (§4.2 Q3) and the choice of Reverse for Table 2, Table 4 and Fig. 5 ("we utilize the best-performing augmentation approach, Reverse") come from the same test accuracies on which they are reported. Because Reverse also wins at nearly every setting in Table 1 and the Table 2/4 numbers are re-used Table 1 cells, I rate this MAJOR rather than fatal (the main comparison would not change), but a held-out check is needed. Critical hyper-parameters are missing: L, τ, α, prompts for rephrasing/augmentation/judging, the sampling temperature, text-task learning rate/batch size, whether students are base or instruct, and the number of items retained after consistency filtering. Table 4's non-monotone Vanilla curve (Llama-3.1-8B: 64.48 at 25% → 49.28 at 100%; GSM8K 42.99 → 24.30) is explained as "noise" in the data (§4.4.1) but equally fits a fixed-epoch over-training artifact; no alternative is tested.
- **Suggested Fix**: carve a validation split from each train set, select methods and epochs there, report the full hyper-parameter table and prompts in an appendix.

### W6: Out-of-distribution protocol cannot isolate transferable reasoning (Table 5)
The comparison is zero-shot vs. fine-tuned on a source task. Fine-tuning also teaches the output/answer format, so gains such as SQA→BoolQ (54.75→64.16) or ANLI→e-SNLI (49.74→59.75) may be format adaptation. There is no control (fine-tuning on an unrelated dataset, a no-CoT fine-tune on the source, or in-distribution training on the target for reference). One row is hard to reconcile with Table 1: training on MATH gives 80.74 on GSM8K (zero-shot 19.64), above the in-distribution GSM8K results for the same student (Vanilla CoT 24.30, Reverse 76.35, Table 1), although the same student reaches only 4.38–36.84 on MATH itself. The teacher/augmentation used for Table 5 is not stated.
- **Suggested Fix**: state the exact training configuration for each pair, add no-CoT and in-domain controls, and explain the MATH→GSM8K value.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1/E4 | Table 1 rows "No Selection", "No Mixing" | "No Selection" | Textual cells equal the "No CoT" row (42.80 avg); WebArena 22.78 = Vanilla CoT; Visual-CoT 44.52 = Zero Shot CoT | Cross-referenced row values within Table 1 | High | MAJOR | Use Vanilla CoT (41.81) as the reference or re-run |
| ERR-2 | E1/E5 | §4.2 Q1 | "Filtering with Teacher Correctness (Textual Average: 44.7%) improves by +1.93↑ over Vanilla CoT" | 44.73 − 41.81 = 2.92; 1.93 is vs the 42.80 row; likewise "decrease of 0.83%↓ over Vanilla CoT" is +0.16 vs Vanilla | Recomputed from Table 1 | High | MAJOR | Correct reference and sign |
| ERR-3 | E5 | §4.2 Q2 and §5 | "LLM-as-a-Judge filtering is highly effective, often surpassing simpler heuristics" | Table 1 Judge textual avg 41.04 < 43.87 < 44.73 and < 42.80 (No Selection); WebArena 15.64 < 22.78 | Cross-referenced Q2/§5 with Table 1 | High | MAJOR | Narrow the claim |
| ERR-4 | E5 | §4.2 Q1 | "Reverse improves average accuracy on all eight tasks by 24.64%" | Reverse is reported on seven textual tasks only ("-" for WebArena/Visual); 24.64 is absolute points (66.45 − 41.81), not % | Recomputed; cross-referenced Table 1 | High | MINOR | "seven textual tasks, +24.64 points" |
| ERR-5 | E6 | Table 1 caption vs Table 3 | "Accuracy of augmentation, selection and mixing strategies on Llama-3.1-8B" | Table 1 Visual-CoT Vanilla CoT is 45.44, identical to Table 3 Qwen-2.5-VL-3B / GPT-4-mini (45.44); Llama-3.1-8B is a text-only LLM | Cross-referenced two tables | Medium | MAJOR | State the visual student and teacher actually used |
| ERR-6 | E6 | Table 4 vs Table 1 | "Vanilla CoT" (Llama-3.1-8B, 100%) | Table 4 ARC 55.34 and Date 59.41 vs Table 1 ARC 55.63 and Date 57.02 for the same configuration (SQA 58.08 and GSM8K 24.30 agree) | Cross-referenced | High | MINOR | Reconcile runs |
| ERR-7 | E6 | §4.1 vs Table 3 vs §4.3.1 Q5 vs App. A | "Due to budget constraints, models like GPT-o4 were not included in our experiments." | §4.1 lists "o4 mini" as a teacher and Table 3 reports "o4-mini"; Table 3 uses "GPT-4o"/"GPT-4-mini" not in §4.1; Q5 names "o1-mini" | Cross-referenced | High | MINOR | Harmonise the teacher inventory |
| ERR-8 | E1/E6 | Table 5 vs Table 1 | "MATH ... GSM8K" row (Zero-Shot 19.64, OOD 80.74) | MATH-trained student scores above the in-domain GSM8K student (Vanilla 24.30; Reverse 76.35), unexplained | Cross-referenced; configuration not stated | Medium | MAJOR | Explain or re-run |

## Claim-to-evidence map (key claims)
| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|-------------|----------|---------|
| C1 | "the first data-centric benchmark" | Abstract, §1 | Table 1–5 are experiments; no protocol, leaderboard or fixed splits/budgets defined; release links unverifiable | Partially (a study, not yet a benchmark) |
| F1 | Augmentation is the most effective family | §1, §4.2 Q1, §5 | Table 1 (Llama-3.1-8B, textual) | Partially: holds vs a weak, size-unmatched baseline; Q7 shows Reverse hurts ARC/GSM8K on Qwen |
| C3 | Selection/mixing guidelines, "when heterogeneous teacher mixtures help" | §1 ③, §4.2 Q3 | Teacher mixing 41.97 vs 41.81 | Unsupported / contradicted for Judge |
| F2 | Compatibility and learnability gap | §4.3 | Table 2/3, Fig. 5 | Partially: 0.24–2.5-point differences, no variance |
| F3 | Distinct scaling; OOD transfer | §4.4 | Table 4, Table 5 | Partially |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Confounded comparisons, inconsistent baselines, no variance |
| Clarity | 2 | Numerous table/text mismatches; missing parameters |
| Significance | 2 | Useful topic, but conclusions not yet reliable |
| Originality | 2 | All methods are prior work; contribution is the study |

## Dimension Scores (0–100)
**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: flawed protocol (size-unmatched comparison, inconsistent baseline rows) and conclusions contradicted by the paper's own Table 1.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | W1, W2, W5 |
| Clarity & Presentation | 55 | Competent | Readable structure, but ERR-1…ERR-8 |
| Novelty & Originality | 45 | Developing | Benchmark of existing methods |
| Significance & Impact | 50 | Developing | Relevant question; 2023-era teachers/tasks (see R2) |
| Experimental Validation | 38 | Developing | W1–W3, W6 |
| Reproducibility | 45 | Developing | Missing L, τ, α, prompts; links unverifiable; API teachers |
| Ethical Compliance | 55 | Competent | Limitations short; no ToS/licensing discussion |

## Questions for Authors
1. Were Vanilla CoT, Answer Aug and Reverse trained on the same number of examples/steps? If not, what are the dataset sizes after augmentation? (A matched-budget result showing Reverse still wins would raise my score; a loss of the margin would lower it.)
2. How were MATH 4.38 and ANLI 23.92 (below zero-shot and below chance) obtained — what answer-extraction rule is used? Would the Vanilla baseline change with tuned epochs?
3. Which teacher and augmentation produced the Table 5 runs, and why does MATH→GSM8K reach 80.74?
4. Is the Visual-CoT column of Table 1 from Llama-3.1-8B or from Qwen-2.5-VL-3B? (Table 1's 45.44 equals Table 3's.)
5. Table 6 lists GSM8K as 7,379 train / 1,339 test; the commonly used split is, to my recollection, 7,473 / 1,319 [verify] — which split was used?

## Limitations Assessment
**Partially.** App. A cites budget and hardware; it omits the missing variance, the single recipe (LoRA only, one learning rate), data contamination of public test sets with teacher/student pretraining data, and the lack of any validation protocol.

## Ethics Review Flag
**No.**

## Overall Score
**2 (Reject).** The study is broad and the topic is worthwhile, but the central ranking of manipulation families rests on size-unmatched, single-recipe runs against an inconsistent baseline, and several written conclusions contradict Table 1.

## Confidence
**4**: I recomputed all averages and cross-checked Tables 1–5; I could not see the figures or the supplementary code.

---

# Peer Review Report — Reviewer 2 (Domain)

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Reviewer: Prof. Rosalind Ekwueme, Domain (private research university, North America; fictional persona)
## Expertise: knowledge distillation for LLM reasoning; synthetic reasoning data
## Date: 2026-11-10

## Summary
DC-CoT evaluates existing data manipulation recipes — MetaMath-style rephrasing and answer augmentation, reverse thinking, three selectors, two mixers — for distilling CoT from proprietary teachers into small open students across text, web-agent and visual tasks. The authors summarise that augmentation helps most, that stronger teachers are not always better (learnability gap), and that data volume effects are non-linear. The value proposition is a controlled, unified comparison of methods that have previously been reported with different setups.

## Strengths
### S1: A real gap in the literature is targeted
Individual recipes (MetaMath [75], Reverse Thinking [6], Distilling Step-by-Step [21], teacher/length mixing [35]) were each introduced with their own models and tasks; a unified comparison across augmentation, selection and mixing (§3.1, Table 1) is useful, and the questions in §1 (❶–❸) are well organised.
### S2: Coverage beyond math (agentic and visual)
Including WebArena [84] and Visual-CoT [51] (§3.2, Tables 1, 3) goes beyond the usual math/commonsense scope of CoT-distillation studies, and App. E documents the agentic format.
### S3: Related work is organised around the right concepts
§2 and App. D separate CoT prompting, long-CoT and distillation, and cite the main distillation prior work (Ho et al. [20], Hsieh et al. [21], Li et al. [33], Mukherjee et al. [45], Fu et al. [13], Magister et al. [41]).

## Weaknesses

### W1: The benchmark's scope is dated relative to the 2025 field
The teachers are GPT-4, Gemini-1.5-Pro, Claude-3.5 (§4.1), the datasets are SQA, CSQA, ARC, ANLI, Date, GSM8K, MATH (§4.1, Table 6) and the CoTs are short; the distillation conversation in 2025 centred on long-CoT traces from reasoning models. The paper itself uses "Llama-3.1-8B-R1 Distilled" as a student (§4.1, Table 2), yet no long-CoT teacher (R1-style outputs) is a source of data, and o4-mini appears only in a visual table (Table 3). In the Field snapshot from the literature check, what counts as significant now is data recipes for long-CoT SFT with verified selection and teacher choice at scale; a result on 200 Date training items or 883 ANLI items (Table 6) will be read as small-scale. Findings such as "more data degrades Vanilla CoT" (Table 4) may be artifacts of short-trace, small-dataset training.
- **Suggested Fix**: add at least one long-CoT teacher (e.g., a reasoning model) and one modern math benchmark with larger training pools, or scope the claims to short-CoT, small-data distillation.

### W2: "First" and "benchmark" are stronger than the evidence; closest prior work is under-positioned
The literature check found no prior data-centric CoT-distillation benchmark (novelty verdict for C1: high on the arXiv-only evidence; at most medium given the search limits), but two nearby lines are not engaged: the learnability-gap finding is already reported in Li et al. ("Small Models Struggle to Learn from Strong Reasoners", arXiv 2502.12143, cited as [35]) which also proposes mixed-length distillation, so F2 ("we confirm the roles of compatibility and learnability", §1) is a replication, verdict incremental; and a recent large-scale study of data recipes for reasoning SFT (OpenThoughts: Data Recipes for Reasoning Models, arXiv 2506.04178, a recent preprint — worth discussing, not a required comparison) examines selection, teacher choice and data scale. The text calls the paper "the first large-scale empirical overview of CoT distillation" (§1 ②) although App. D itself lists many prior studies. In practice the contribution is a study of existing methods with no new protocol, splits, metric or leaderboard that makes it reusable as a "benchmark" (§3 defines manipulations, not an evaluation protocol).
- **Suggested Fix**: replace "first ... overview" by a precise scope statement, add a paragraph contrasting with the learnability-gap and data-recipe work, and define the benchmark artefact (fixed splits, budgets, scoring scripts, released CoT sets).

### W3: Descriptions of methods and prior work contain inaccuracies
§3.1.2 ❷ defines student-error filtering as Dtarget = {(Qi, Ri, Ai) | Âi ≠ A*i}, i.e., the student's answer is wrong, but does not require the teacher's rationale to be correct, so wrong teacher traces can enter the set (the answer in the tuple is the teacher's). §3.1.2 ❸ writes the judged set as Dsource rather than Dtarget (a typo-level slip), and §3.1 writes "Dsource to the target dataset Dsource" (the target should be Dtarget). §4.3.1 Q5 attributes the improvement to "GPT-4-mini and o1-mini" while Table 3 lists "GPT-4-mini" and "o4-mini"; "GPT-4-mini" is not a model named in §4.1 (which lists GPT-4.1 mini). The choice of LLama-2-70B as the judge for rationales produced by Gemini-1.5-Pro (§4.1) is unusual (a weaker, older model than the teacher) and not validated.
- **Suggested Fix**: correct the definitions, name the teacher models consistently, validate the judge against ground truth or a stronger judge.

### W4: Explanations of the results are asserted, not tested
"It likely fosters a deeper understanding by teaching bi-directional reasoning" (§4.2 Q2), "CoTs from very large models like GPT-4 might be overly complex" (§4.3.1 Q5) and "prior distillation history ... can hinder learning" (Q6 point 3) are plausible hypotheses with no measurement of trace length/complexity, perplexity under the student, or consistency with the learnability-gap literature's controls (matched teacher family, varying strength). In Q5 the comparison mixes GPT-4 with two different, newer small/reasoning models, so teacher family and date are confounded with size.
- **Suggested Fix**: add trace statistics (length, step count, student perplexity) by teacher, or soften to hypotheses.

### Missing References
*(Literature check strict, cutoff 2025-09-24; each entry verified with `related_search.py verify`/search unless marked.)*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Yuetai Li et al., "Small Models Struggle to Learn from Strong Reasoners", arXiv 2502.12143 (2025) — prior (arXiv-only); already cited as [35], but its learnability-gap finding should be credited as the source of F2 rather than "confirmed" | Positions F2 and the mixing baselines |
| Important | Toshniwal et al., "OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset", NeurIPS 2024 Datasets & Benchmarks (arXiv 2402.10176; labelled peer-reviewed by the search) | Large-scale teacher-generated, selected math SFT data; evaluates what kind of synthetic data helps |
| Helpful | Xiang Yue et al., "MAmmoTH2: Scaling Instructions from the Web", arXiv 2405.03548 (2024) | Scaling and filtering of synthetic instruction data |
| Helpful (worth discussing; recent preprint) | OpenThoughts: "Data Recipes for Reasoning Models", arXiv 2506.04178 (2025) | Systematic data-recipe study for reasoning SFT |
| Helpful (worth discussing; recent preprint) | MiCoTA: "Bridging the Learnability Gap with Intermediate CoT and Teacher Assistants", arXiv 2507.01887 (2025) | Builds on the same learnability gap |
| Helpful | Ye et al., "LIMO: Less is More for Reasoning", arXiv 2502.03387 (2025) | Small, curated data for reasoning; relevant to Table 4's "more data hurts" |
| Helpful | Yeo et al., "Demystifying Long Chain-of-Thought Reasoning in LLMs", arXiv 2502.03373 (2025) | Controlled study of CoT SFT data and length |

### Literature-check addendum
**Novelty delta table (closest prior works).**
| Claimed contribution | Closest prior work (link) | What that work already does | What is actually new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 data-centric benchmark | OpenThoughts (arXiv 2506.04178, recent preprint) | Systematic data-recipe study for reasoning SFT | A unified comparison across augmentation/selection/mixing on 3 modalities | Not cited; discuss only |
| C2 augmentation is best | Reverse Thinking Makes LLMs Stronger Reasoners (arXiv 2411.19865, peer-reviewed label) | Introduces reverse augmentation; shows gains | Comparison with other augmentations/selectors on small students | Cited [6]; differentiated as a source |
| F2/C3 learnability gap, mixing | Small Models Struggle to Learn from Strong Reasoners (arXiv 2502.12143) | Reports the learnability gap and mixed-length distillation | Replication across more teachers/students | Cited [35] as source of length mixing; not credited for the gap |

**Per-claim novelty:** C1 high (one-claim "no close prior found", arXiv only → at most medium), C2 medium, C3/F2 incremental. No claim is "known"; no criterion-7 candidate. **Baseline scout:** not constructible — no prior arXiv abstracts reporting comparable numbers on these exact configurations were returned (searches for GSM8K/MATH distillation and WebArena trajectories returned data-set/system papers with different settings). **Field snapshot:** until 2023 CoT distillation meant sampling short rationales from GPT-class teachers (SCoTD, Distilling Step-by-Step, Orca); 2024 brought synthetic-math recipes (MetaMath, OpenMathInstruct); 2025 is dominated by long-CoT distillation from reasoning models and data-recipe studies (R1-distilled students, OpenThoughts, LIMO). Open problems stated by recent work: which teacher for which student (learnability gap), which traces to select, and how much data. A contribution is significant when it gives a controlled finding on these questions at long-CoT scale; a +X-point gain on short-CoT 7-task suites is incremental. This calibrates my Significance score.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence is thin for several claims |
| Clarity | 3 | Organised by research questions |
| Significance | 2 | Dated scope; useful as a starting point |
| Originality | 2 | Replication/combination of known recipes |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: relevant unified comparison and broad scope, but the benchmark artefact is thin, the field has moved to long-CoT, and F2 is largely known.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | See R1; method definitions inaccurate (W3) |
| Clarity & Presentation | 58 | Competent | |
| Novelty & Originality | 45 | Developing | C1 high only for the framing; findings incremental |
| Significance & Impact | 52 | Developing | Field snapshot above |
| Experimental Validation | 45 | Developing | Dated teachers/datasets, no long-CoT |
| Reproducibility | 50 | Competent (low) | Deprecated API teachers; released data would help |
| Ethical Compliance | 58 | Competent | |

## Questions for Authors
1. Does the main ranking (augmentation > selection > mixing) hold for a long-CoT teacher on a larger math training set? (Yes would raise my score.)
2. What is DC-CoT as an artefact: fixed splits, scoring scripts, released traces? Will the traces be released given the teachers' terms of use?
3. How does F2 go beyond Li et al. [35]?

## Limitations Assessment
**Partially** (App. A mentions budget/hardware only).

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject).** A useful unified study, but positioned as the "first" benchmark while the artefact is thin, one finding replicates a cited work, and the scope lags the field.

## Confidence
**4.**

---

# Peer Review Report — Reviewer 3 (Perspective)

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Reviewer: Dr. Mateus Valderrama, Perspective (applied-ML lab, public university, Latin America; fictional persona)
## Expertise: curriculum design and learning sciences; efficient/on-device ML; dataset engineering
## Date: 2026-11-10

## Summary
The paper asks how data should be prepared to teach small models to reason from a large model's explanations, comparing re-writing, filtering and mixing recipes on many tasks. Its practical promise is cheaper, more accessible reasoning models. I read it as an early "recipe book" for distillation practitioners, with several observations (diminishing returns of data, student-dependent best teacher, mixed transfer) that matter for deployment.

## Strengths
### S1: Questions practitioners actually ask
Which teacher, how much data, what filter, and does it transfer? (§1 ❶–❸, §4.2–§4.4.) The data-volume study (Table 4, Q9–Q10) and size sweep (Fig. 5, Q7–Q8) address cost/benefit directly.
### S2: A useful analogy with curriculum learning
Length mixing (§3.1.3 ❶, "balanced curriculum") and the learnability-gap discussion (Q5–Q6) connect to curriculum and scaffolding ideas from education research, where matching the difficulty of explanations to learner capacity is central; this framing supports the paper's most interesting observation (Table 3, Table 2).
### S3: Cross-modality scope
Applying the same recipes to agentic web tasks and visual reasoning (Table 1, Table 3) is a good step towards general guidance for small agents.

## Weaknesses

### W1: The learner's side is not examined, so the "learnability" story is speculative
Whether a trace is "digestible" is a property of the student: a curriculum view would measure the student's loss/perplexity on traces, step count, or vocabulary overlap, and would sequence data from easy to hard rather than mixing at a fixed ratio α. The paper explains teacher effects by narrative ("might be overly complex", §4.3.1 Q5) and tests only two or three teacher points (Table 2, Table 3).
- **Suggested Fix**: report student-side diagnostics (token-level loss on teacher traces, trace length) and try an easy-to-hard schedule against random mixing.

### W2: Deployment assumptions are not stated
Students are trained with LoRA (rank 32, App. C.1), evaluated by accuracy only; no inference cost, latency or trace-length cost is reported although the title and Broader Impact claim "efficient reasoning" and "reducing the computational footprint". Longer reverse/answer-augmented traces increase tokens per answer at test time; WebArena results (812 test tasks, Table 6) come with no stated number of runs. The conclusions may not transfer to full fine-tuning or to production API-teacher settings where teachers are deprecated.
- **Suggested Fix**: report output-token counts and latency per method, and one full-fine-tuning check.

### W3: Data-governance and misuse aspects are absent
The benchmark releases teacher outputs from proprietary APIs (GPT-4, Claude-3.5, Gemini; §4.1) and derived training sets built on NC-licensed data (ANLI and e-SNLI, "CC BY-NC 4.0", Table 6); neither provider terms-of-service nor license compatibility is discussed, and Appendix B lists only benefits (democratisation, education, finance, healthcare). Public test sets (GSM8K, MATH, ARC, CSQA) may overlap with teacher/student pretraining data; contamination is not mentioned, and it interacts with the "reverse thinking" gains because the teacher may have memorised the answers.
- **Suggested Fix**: add a licensing/ToS paragraph, a contamination check (e.g., against newer or perturbed test sets), and a limitations entry on smaller, unreliable students deployed in education/health settings.

### W4: Other fields suggest controls the paper lacks
Cycle-consistency (the idea behind reverse thinking's consistency filter, §3.1.1 ❹) and data-augmentation/noise-robustness work from vision and speech distinguish "more data" from "more diverse data" using matched-size controls; likewise, active-learning style selection would compare the student-error filter against uncertainty-based selection. These baselines would give the selection results a reference.
- **Suggested Fix**: add a random-subset selection baseline and a size-matched augmentation baseline.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See R1: confounds, no variance |
| Clarity | 3 | Question-based structure is easy to follow |
| Significance | 3 | Practitioner-relevant questions |
| Originality | 2 | Known recipes, new unified comparison |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: relevant, practical question with broad coverage, but the evidence is not yet at the level of a reliable guide.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound pipeline, confounded comparisons |
| Clarity & Presentation | 58 | Competent | |
| Novelty & Originality | 50 | Developing | |
| Significance & Impact | 58 | Competent | Practitioners would use well-supported guidance |
| Experimental Validation | 48 | Developing | |
| Reproducibility | 52 | Competent | Training settings partly given |
| Ethical Compliance | 50 | Developing | ToS/licensing and contamination not discussed; positive-only Broader Impact (App. B) |

## Questions for Authors
1. Do outputs-per-answer token counts differ between Vanilla and Reverse students? (A large increase would lower the "efficient" claim.)
2. Can the teacher outputs be released under the providers' terms, and what licence will the derived ANLI/e-SNLI data carry?
3. Has any test set been checked for overlap with teacher/student pretraining data?

## Limitations Assessment
**Partially.** Budget/hardware limitations only (App. A).

## Ethics Review Flag
**No** (licensing/ToS issue noted for the editor, not a flagged violation).

## Overall Score
**3 (Borderline Reject).** An interesting and practical direction with potential, but the evidence base needs matched controls, student-side measurements and governance discussion.

## Confidence
**3.**

---

# Peer Review Report — Reviewer 4 (Generalist)

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Reviewer: Dr. Priya Raghunathan-Holt, Generalist (academic group, South Asia; fictional persona)
## Expertise: NLP and representation learning (not distillation specifically)
## Date: 2026-11-10

## Summary
The paper presents DC-CoT, a benchmark-style study of how to prepare chain-of-thought data (augment, select, mix) when distilling large proprietary teachers into small open students, with results on text, web-agent and visual tasks. It reports that augmentation, especially reverse thinking, helps most, that teacher–student pairing is nuanced, that more data is not always better, and that fine-tuning transfers across related tasks to a degree.

**Contribution in one paragraph (my words).** A catalogue of existing CoT-data recipes evaluated under one training pipeline, with take-aways for practitioners who want a small reasoner.

## Strengths
### S1: Clear organisation around research questions
§1 poses three perspectives and §4 answers twelve numbered questions (Q1–Q12), so a reader can find each take-away quickly.
### S2: Breadth and effort
Five teachers, five 7–8B students plus a 0.5–7B family, ten task datasets and ten transfer pairs (§4.1, Tables 1–5) represent a considerable compute and API effort, acknowledged in App. A.
### S3: Honest negative findings
The paper reports that mixing does not beat the baseline on average (§4.2 Q2) and that the "more data is better" assumption fails for Vanilla CoT (§4.4.1 Q10).

## Weaknesses

### W1: "Benchmark" framing vs. a one-off study; venue fit
ICLR rewards benchmarks that others can run and that expose something new. DC-CoT is described in §3 as a list of manipulations and in §4 as experiments; there is no statement of the benchmark's protocol (fixed splits, budgets, metric aggregation), no leaderboard-style result table with all methods on all students, and the dataset/code links are given only as "here" (Abstract; unverifiable in this copy). A reader cannot tell what a future method must do to be "on DC-CoT".
- **Suggested Fix**: add a "Benchmark protocol" subsection and a single master table (method × student × task) with the release plan.

### W2: Key conclusions are hard to trust because text and tables disagree
Examples: "LLM-as-a-Judge filtering is highly effective" (§4.2 Q2) vs Judge having the lowest selector average in Table 1 (41.04); "Reverse improves average accuracy on all eight tasks" (Q1) while Table 1 gives Reverse for seven text tasks; Table 1 states Llama-3.1-8B for all columns yet the Visual-CoT number equals Table 3's Qwen-2.5-VL-3B number (45.44). Verified against Table 1 (R1 ERR-1…ERR-8 are independent of my reading; I re-checked the Judge and Q1 items myself). A paper whose take-aways are the product should have them match the tables.
- **Suggested Fix**: a consistency pass, then a short "key findings" table listing each finding with the exact numbers.

### W3: Presentation of the method definitions and setup
§3.1 and §3.1.2 contain notation slips (Dsource written for the target set), "GPT-4-mini" vs "GPT-4.1 mini" vs "o4 mini" vs "o1-mini" (§4.1, §4.3.1 Q5, Table 3), and the agentic task statement says both the student π_θ and "A large LLM (ML) selects actions" (§3.2) without saying which model acts at test time. Figure 5/6 captions are minimal and, without seeing the plots, the text must carry all numbers. Appendix E is a single WebArena example and does not show the augmentation prompts the benchmark depends on.
- **Suggested Fix**: define notation once, name each model once, state who acts in WebArena, and add prompts.

### W4: Limited actionable guidance
Contribution ③ promises "actionable guidelines" but §4.2 Q3 lists per-task recipes (e.g., "Reverse Thinking excels ... filter ... then Length Mixing can be applied") that are never run together; Q6 gives three "principles" from two or three observations. A practitioner cannot tell whether the recommended pipeline beats Reverse alone.
- **Suggested Fix**: run the recommended per-task pipeline and report it against Reverse alone.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | §4.2 Q1–Q3 vs Table 1 |
| Soundness: fair/controlled comparisons | Not met | §3.1.1, App. C.1 (unmatched data/steps) |
| Presentation: clear, consistent | Partly | text–table mismatches; notation slips |
| Contribution: new knowledge for the community | Partly | Table 2, Table 4 observations; thin benchmark artefact |
| Reproducibility/release | Partly | App. C.1; no prompts, L, τ, α |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Controls missing |
| Clarity | 2 | Mismatches and notation slips |
| Significance | 3 | Topical and useful |
| Originality | 2 | Known methods |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a typical PC member would see a useful but unfinished study whose headline text does not match its tables.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | |
| Clarity & Presentation | 52 | Developing | W2, W3 |
| Novelty & Originality | 48 | Developing | |
| Significance & Impact | 55 | Competent | |
| Experimental Validation | 46 | Developing | |
| Reproducibility | 50 | Developing | |
| Ethical Compliance | 55 | Competent | |

## Questions for Authors
1. Which three findings would you stand behind after a consistency pass, and with which numbers?
2. What is the minimum a new method must do to be added to DC-CoT?
3. Will the dataset/code be released with the generated traces and prompts?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject).** The topic fits ICLR and the effort is large, but at present the paper reads as a draft: take-aways are not yet reliable and the benchmark is not defined as an artefact.

## Confidence
**4.**

---

# Devil's Advocate Report

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Reviewer: Prof. Henrik Soleimani, Devil's Advocate (evaluation-methodology group, Western Europe; fictional persona)

## Steelman
A single, uniform LoRA pipeline applied to many teachers, students and recipes is the right way to compare data-centric methods, and a broad study is more informative than the one-method papers it builds on. The headline pattern — answer/reverse augmentation >> selection ≈ mixing, with student- and task-dependent teacher effects — is consistent with the intuition that rationale diversity matters for small students.

## Core Argument Chain
1. Under one fixed recipe (LoRA, 10 epochs on text, §App. C.1), augmentation lifts the textual average from 41.81 to 66.45 (Table 1).
2. Selection and mixing change the average by ≤ 3 points (Table 1, as read by the authors).
3. Hence data augmentation is the most effective data-centric manipulation, "by enriching reasoning trace diversity and complexity" (§5).
4. Teacher/student/data-volume/transfer experiments reveal compatibility, learnability and scaling regularities (§4.3–§4.4).
∴ DC-CoT yields "actionable guidelines" and "best practices" for CoT distillation (Abstract, §1 ③).

## Strongest Counter-Argument
Even if every number is right, the experiment does not isolate what the paper says it isolates. The augmented arms are not just "more diverse"; they are two- to L-fold *larger* (reverse thinking adds a second question–reasoning pair per item; answer augmentation adds L rationales; §3.1.1), trained for the same fixed 10 epochs (App. C.1), against a Vanilla-CoT baseline that is *worse than fine-tuning without CoT at all* on the text average (41.81 vs 42.80, Table 1), scores 4.38 on MATH (zero-shot 9.32) and 23.92 on ANLI (zero-shot 33.83, chance ≈ 33%). A baseline that damages the student is a weak reference, and the paper's own scaling experiment (Table 4: Vanilla CoT on Llama-3.1-8B falls from 64.48 at 25% to 49.28 at 100%, GSM8K 42.99 → 24.30) shows that the pipeline is unstable in the amount of data/steps — exactly the variable on which augmentation differs from the baseline. So the +24.64-point headline is compatible with "more tokens and steps on an over-trained baseline" rather than "better rationales." The selection/mixing comparisons are worse off: their reference row ("No Selection"/"No Mixing") is a hybrid of the no-CoT, Vanilla and Zero-Shot-CoT runs (ERR-1), and the written conclusions on selection ("LLM-as-a-Judge ... highly effective", "crucial") contradict the table the authors print (Judge 41.04 < Vanilla 41.81). The guidelines (Q3) then recommend pipelines that were never executed. The fix is cheap — matched-budget arms, a tuned baseline, a table-text audit — but until it is done the paper has not shown that its ranking of data-centric families is a property of the data rather than of the training budget and baseline, and the "best practices" claim has no evidence behind it. This is a narrowing-the-claim problem, not a fatal one; the authors would need to answer it in the rebuttal.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core finding (Reverse > Vanilla on the text average) survives in a weaker form; the problems above can be repaired by narrowing claims and adding controls, none of which makes the work unpublishable by itself, and the selection of Reverse on the reported test split (§4.3.1 "we utilize the best-performing augmentation approach, Reverse") falls in the "affects secondary results / the main comparison holds across the sweep" rows of the criterion-3 table (Reverse is also best or near-best at the other settings in Table 1), i.e. MAJOR.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (alternative explanation) | §3.1.1, App. C.1, Table 1/6, §5 | Augmentation gain confounded with data size/steps; post-augmentation sizes not reported; evidence supports "augmented-and-larger beats vanilla", not "diversity" | Matched-size/token arm; report sizes |
| DA-M2 | Evidence (claim distortion, E5) | §4.2 Q1–Q2, §5, Table 1 | Selection/mixing conclusions contradicted or measured against the wrong row (ERR-1…3): Judge 41.04 < 41.81; "+1.93 over Vanilla" is +2.92 | Fix reference rows; rewrite conclusions |
| DA-M3 | Evidence (baseline validity) | Table 1 (Vanilla/No CoT/Zero-shot rows) | Vanilla CoT below No-CoT and below zero-shot on MATH and ANLI; suggests extraction/overfitting issues | Tuned baseline on validation split; document parsing |
| DA-M4 | Logic / Scope | §4.2 Q3, §1 ③, §5 | "combining effective augmentation with suitable filtering or mixing can yield further improvements" and "best practices": no combined run exists | Run combined pipelines or delete the claim |
| DA-M5 | Evidence (reliability) | Tables 2–5, Fig. 5–6 | No variance; test sets of 169–229 items (Table 6) give SE ≈ 3–4 points; teacher "learnability gap" evidence = differences of 0.24–2.5 points (Table 3) | Seeds, bootstrap CIs, restrict claims |
| DA-M6 | Logic (overgeneralisation) | §4.3.2 Q7 vs §4.2 Q1, §1 F1 | On Qwen-2.5, Reverse "markedly degraded performance on ARC and GSM8K", while Table 1 (Llama) shows +26.5 and +52.1 points; "generally the most effective" does not hold across students | Report Reverse vs Vanilla for every student in Table 2; qualify F1 |
| DA-M7 | Evidence (OOD design) | §4.4.2, Table 5 | Zero-shot vs fine-tuned comparison confounds format learning with transfer; MATH→GSM8K 80.74 exceeds in-domain results; 3/10 pairs show no gain though "consistently" is claimed | Controls; explain; restate |
| DA-M8 | Evidence (protocol) | §4.3.1; Table 6 | No validation split; per-task recipes and Reverse selected on reported test accuracy | Hold-out validation for selection |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity-of-description | §4.1, Table 3, Q5, App. A | Teacher list inconsistent (o4-mini, GPT-4o, GPT-4-mini, o1-mini; "GPT-o4 not included") |
| DA-m2 | Scope | Table 6 | "Train (Filtered)" larger than "Train (Original)" for Visual-CoT (943,000 vs 132,000) and OK-VQA (9,009 vs 5,046); column semantics unclear |
| DA-m3 | Reliability | Table 2 | Date = 70.41 in both Llama-3.1-8B/Gemini and Llama-3.1-8B-R1/Gemini rows (119/169 for both); possible coincidence, worth confirming |
| DA-m4 | Judge validity | §4.1 | LLama-2-70B judge weaker than the Gemini teacher; no validation of the judge |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Reverse vs Vanilla (text average) | 24.64 | 66.45 − 41.81 = 24.64 | Yes (but "eight tasks"; seven; absolute points) |
| Teacher-correct filtering vs Vanilla | +1.93 | 44.73 − 41.81 = 2.92 (1.93 is vs No Selection 42.80) | No (label) |
| Teacher mixing vs Vanilla | −0.83 | 41.97 − 41.81 = +0.16 (−0.83 is vs No Mixing 42.80) | No (label) |
| Length mixing vs No Mixing | −1.37 | 41.43 − 42.80 = −1.37 | Yes (vs No Mixing) |
| Table 1 Reverse average | 66.45 | 465.15/7 = 66.45 | Yes |
| Table 4 Llama Vanilla 100% | 49.28 | (58.08+55.34+24.30+59.41)/4 = 49.28 | Yes (but ARC/Date differ from Table 1) |
| Visual-CoT Vanilla (Table 1) vs Qwen-VL/GPT-4-mini (Table 3) | 45.44 vs 45.44 | identical value for different students | Inconsistent with caption |

## Ignored Alternative Explanations
Data size/steps (above); answer-format learning rather than reasoning transfer (Table 5); teacher family/date rather than size (Table 3); public-test-set contamination (GSM8K, MATH, ARC, CSQA) in teachers and students (Qwen-2.5, Llama-3.1); over-training with 10 epochs on small sets (Date 200 train, Table 6); LoRA-specific behaviour; judge weakness (LLama-2-70B) rather than "LLM judging" in general.

## Missing Stakeholder Perspectives
Practitioners following the "best practices" with proprietary-API teachers (terms of service, deprecation of GPT-4/Gemini-1.5-Pro-001); maintainers of the NC-licensed source datasets (ANLI, e-SNLI) whose licences apply to derived data; educators/health users of small reasoners whose errors on commonsense/Date tasks are not analysed (Appendix B lists benefits only).

## Observations (Non-Defects)
The paper reports negative results (mixing, Vanilla degradation) rather than hiding them; averages are arithmetically consistent with their rows; a single uniform pipeline across teachers/students is a design choice that makes cross-recipe comparison possible once the confounds are removed.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 40 | DA-M1–M3, M8 |
| Clarity & Presentation | 52 | text–table mismatches |
| Novelty & Originality | 45 | existing methods; learnability gap known |
| Significance & Impact | 48 | useful if repaired |
| Experimental Validation | 36 | confounds, no variance, weak baseline |
| Reproducibility | 45 | missing L, τ, α, prompts |
| Ethical Compliance | 55 | limited limitations discussion |

## Overall: 2 | Confidence: 4

---

# Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept | Each has a location and a fix; appendix searched (App. C.1 states the fixed 10 epochs and no tuning) |
| R1 | Question 5 (GSM8K split sizes) | kept as Question only | Recollection of the standard split, marked `[verify]`; not a Weakness |
| R2 | W3 (method-definition slips) | rewritten | The "Dsource written for target" point is typo-level; moved into one Minor sentence; the student-error-filter point kept (§3.1.2 ❷) |
| R2 | W2 "learnability gap is known" | kept | Matches the cited work's abstract ("Small Models Struggle to Learn from Strong Reasoners" reports the learnability gap); the paper does cite it as [35] |
| R3 | W4 (other fields' controls) | moved to Minor/P3 | Expansion suggestion, not a defect |
| R3 | W3 contamination | rewritten as question-framed | Contamination is not claimed to have occurred, only not discussed |
| R4 | W3 (notation and naming) | moved to Minor | Cosmetic apart from the "who acts in WebArena" point (kept) |
| DA | DA-m3 (identical Date value) | kept under Minor / question | Low-confidence suspicion (can be a coincidence); not an error |
| All | Paper-answered points | none dropped | The appendix gives no validation protocol, prompts or sizes, so no omission was already answered |

---

# Phase 2 — Synthesizer Part A: package for the EIC

**Consensus map.**
| Issue | Sources | Class |
|-------|---------|-------|
| Augmentation/size/step confound; no matched control | R1-W1, R3-W4, DA-M1 | CONSENSUS-3 |
| Table/text contradictions (Judge, +1.93, "eight tasks", Visual column) | R1-W4, R1 ERR-1…8, R4-W2, DA-M2 | CONSENSUS-3 |
| No variance/significance | R1-W3, DA-M5 (R4-W2 partially) | CONSENSUS-2 |
| Weak/inconsistent baselines | R1-W2, DA-M3 | CONSENSUS-2 |
| No combined-pipeline evidence for guidelines | R1-W4(iii), R4-W4, DA-M4 | CONSENSUS-3 |
| Benchmark is a thin artefact; "first" overclaim | R2-W2, R4-W1 | CONSENSUS-2 |
| Dated teachers/tasks, no long-CoT | R2-W1 | SOLO |
| OOD design (Table 5) | R1-W6, DA-M7 | CONSENSUS-2 |
| Governance/ToS/licensing/contamination | R3-W3, DA stakeholder note | CONSENSUS-2 |
| Learnability explanations untested | R2-W4, R3-W1, DA-M5 | CONSENSUS-3 |
| Test-split selection/no validation | R1-W5, DA-M8 | CONSENSUS-2 |
| SPLIT | none: all five reviewers lean negative; R3 is the most positive | — |
| DA-CRITICAL | none raised | — |

Issues the outcome may hinge on: the Table 1 reference-row problem (ERR-1/ERR-2), the Judge-filter contradiction (ERR-3), the size-matching confound, the Table 5 anomaly (ERR-8), the Visual column provenance (ERR-5), and test-split selection (R1-W5/DA-M8).

**BEFORE (no `eic_weight`, `da_critical: []`):** official mean 2.60 (R1 2, R2 3, R3 3, R4 3, DA 2); official composite 49.0; confidence-only weighted rating 2.59 → 3; composite band 2 (⚠ differs from the rating); no consistency warnings; ICLR 4 on {0,2,4,6,8,10}.

---

# Phase 2 — EIC Meta-Review (Prof. Amara Lindqvist-Osei)

## The Case For and Against
- **For acceptance:** A broad, uniform study of how data manipulation affects small-model CoT distillation across text, agentic and visual tasks, with several useful negative findings; the question is of clear practical interest to the ICLR community, and the authors state their API/hardware limitations honestly.
- **Against acceptance:** The headline ranking of data-centric families rests on size-unmatched runs against an internally inconsistent and sometimes implausible baseline (Table 1), no variance on small test sets, and conclusions on selection, mixing and "guidelines" that the printed tables contradict or never test; the "benchmark" is not specified as a reusable artefact.

## Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "No Selection/No Mixing" textual row = "No CoT" row; WebArena 22.78 = Vanilla; Visual 44.52 = Zero-Shot CoT | R1 ERR-1, DA-M2 | Table 1 | **Verified** | Textual cells 59.89/65.36/60.41/7.39/20.74/35.42/50.37 identical to No CoT; avg 42.80 |
| "+1.93 over Vanilla CoT" and "−0.83 over Vanilla CoT" use the 42.80 reference | R1 ERR-2, DA numeric check | §4.2 Q1, Table 1 | **Verified** | 44.73 − 41.81 = 2.92; 41.97 − 41.81 = +0.16 |
| Judge filtering "highly effective" vs table | R1 ERR-3, R4-W2, DA-M2 | §4.2 Q2, §5, Table 1 | **Verified** | Judge 41.04 vs Teacher 44.73, Student 43.87, No Selection 42.80, Vanilla 41.81; Judge is best selector only on ANLI, Date and Visual-CoT |
| "all eight tasks" | R1 ERR-4 | §4.2 Q1 | **Verified** (minor) | Seven textual tasks; Reverse is "-" on WebArena/Visual |
| Augmentation gain confounded with data size/steps | R1-W1, DA-M1 | §3.1.1, App. C.1, Table 6 | **Partly correct** | Method text says L samples and a backward pair per item; post-augmentation sizes are indeed not reported; the paper does not state that sizes are unmatched, so this is an inference from the described procedure and the fixed 10-epoch rule — a strong, well-founded concern but not a documented fact |
| Vanilla CoT below No-CoT / zero-shot (MATH 4.38 < 9.32; ANLI 23.92 < 33.83) | R1-W2, DA-M3 | Table 1 | **Verified** (numbers); cause **unverifiable** | Whether it is extraction failure or over-training cannot be determined from the paper |
| Table 1 Visual column vs caption | R1 ERR-5 | Table 1, Table 3 | **Partly correct** | 45.44 appears in both; consistent with Qwen-2.5-VL-3B and GPT-4-mini; but §4.2 says teacher for visual was "GPT-4-mini" which fits; the caption is wrong or misleading, but the table value may be right |
| Table 4 vs Table 1 Vanilla ARC/Date | R1 ERR-6 | Tables 1, 4 | **Verified** (minor) | 55.34/59.41 vs 55.63/57.02 |
| Table 5 MATH→GSM8K 80.74 | R1 ERR-8, DA-M7 | Table 5 vs Table 1 | **Verified** (as unexplained) | Configuration for Table 5 not stated |
| Table 5 "consistently" (3/10 pairs no gain) | R1-W4(iv), DA-M7 | §4.4.2 Q11 | **Verified** | 9.32→8.75; 42.10→38.90; 44.52→44.62 |
| No combined pipeline run | R1-W4(iii), R4-W4, DA-M4 | §4.2 Q3, Tables 1–5 | **Verified** | Search of Tables/text found only single-axis runs |
| Selection of Reverse on test split | R1-W5, DA-M8 | §4.3.1; Table 6 | **Verified** | "we utilize the best-performing augmentation approach, Reverse"; no validation split in Table 6 |
| Reverse hurts ARC/GSM8K on Qwen | DA-M6 | §4.3.2 Q7 | **Verified** (text); figure unavailable | Numbers in Fig. 5 not readable |
| Learnability gap = "strong support" from Table 3 | R2-W4, R3-W1, DA-M5 | §4.3.1 Q5, Table 3 | **Overstated** (by the paper) | 45.44/45.20 vs 42.92; one student, single run, teachers differ in family |
| Learnability gap already reported by cited [35] | R2-W2 | §1, §4.3 | **Verified** | Search result abstract for arXiv 2502.12143 (prior) |
| Dated scope / no long-CoT teacher | R2-W1 | §4.1, Table 6 | **Verified** | Teachers in §4.1 are all non-long-CoT as used; R1-distilled only as a student |
| ToS/licence/contamination not discussed | R3-W3 | App. A, B, Table 6 | **Verified** | Not found in the text |

## Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | **1.25** | Every Error Log entry was checked at its location and holds (ERR-1–4, 6, 8 fully; ERR-5 partly); decisive for the outcome; slightly harsh on pool position but calibrated to the evidence |
| R2 (Domain) | 3 | 4 | 1.0 | Literature points verified against search abstracts; field-snapshot calibration reasonable; no point moved the weight |
| R3 (Perspective) | 3 | 3 | 1.0 | Constructive; governance/contamination points verified as absent; no verified error |
| R4 (Generalist) | 3 | 4 | 1.0 | Sound, typical review; text–table points verified |
| DA | 2 | 4 | 1.0 | Confounding argument is partly inference (see verification row 5) so its scores count at full weight but not more; no CRITICAL raised |

## DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so none to rule on (`da_critical: []`; DA ceiling: none). I also checked the criterion-3 question independently: the paper selects Reverse (§4.3.1) and the per-task recipes (§4.2 Q3) on test accuracy because there is no validation split (Table 6). Applying the decision table: Reverse is the best-scoring option, but the main comparison (Reverse vs Vanilla/other augmentations) holds across the settings in Table 1, and the selected configuration affects follow-up analyses (Tables 2, 4, Fig. 5) rather than a headline number fixed in advance — **MAJOR, not CRITICAL** ("main claim holds at every other value in the sweep"; "affects only ablations or secondary results"). It stays in the Roadmap (P1: hold-out check).

## Official ratings → EIC assessment → Final decision
- **Official** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean **2.60**; official composite **49.0**.
- **EIC assessment** (internal; weights above): weighted rating **2.56** → starting point **3 (Borderline Reject)**; weighted composite **48.7** → band 2 (Reject) — the ⚠ cross-check differs by one step.
- **Composite cross-check.** The rating (2.56) and composite (48.7, 1.3 points under the 50 edge) sit at band boundaries; the script's flag is a one-step disagreement near an edge, which by itself is not a reason to depart. I name no verified issue that the ratings failed to account for: the reviewers' own texts already include ERR-1–8 and the confound. I trust the ratings.
- **Final decision: Borderline Reject (3).** The DA ceiling does not bind. The ICLR scale value is reported below. Why not 2: the contribution is real (a broad, honest, practically relevant comparison with some robust findings, e.g., Reverse vs Vanilla on Llama-3.1-8B text is large in absolute terms), every major defect is repairable with existing infrastructure within a revision (matched-budget arms, corrected rows, seeds, rewritten conclusions), and weaknesses such as single runs and API-teacher dependence are typical of accepted benchmark papers. Why not 4: the defects are not typical-accepted-paper weaknesses — the stated conclusions on selection contradict Table 1, the selection/mixing reference row is wrong, the guidelines are untested, and the benchmark is not defined as an artefact — so the reasons to reject outweigh those to accept in the current draft. **EIC pool position: better than about 38% of ICLR submissions** (accepted share ≈ 27%). Deciding evidence: a verified internal inconsistency in the main results table plus a confound that is plausibly the whole headline effect.

---

# Editorial Decision

## Paper: The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation
## Submission ID: iclr26-Dud8FtScW7 (evaluation ID)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: benchmark
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Amara Lindqvist-Osei; R1 Methodology Dr. Kenji Aldermoor, R2 Domain Prof. Rosalind Ekwueme, R3 Perspective Dr. Mateus Valderrama, R4 Generalist Dr. Priya Raghunathan-Holt, DA Prof. Henrik Soleimani

## Decision: **Borderline Reject (3)**

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60 · official composite 49.0
**EIC assessment** (internal): weighted rating 2.56 → starting point 3 · weighted composite 48.7 → band 2 (cross-check; one-step difference near the edge, not a reason to depart) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR translation** (scale status: secondary; run with `--venue iclr --final 3`): rating **4 on {0, 2, 4, 6, 8, 10}** (5 on the earlier {1, 3, 5, 6, 8, 10} scale), Soundness 1, Presentation 2, Contribution 2 (1–4). Labels follow the internal decision, not an official wording.

## Score Summary

### Official Scores and EIC Assessment (script output, with EIC weights)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 42 | 50 | 52 | 50 | 40 | 46.8 | 46.4 | 12 |
| Clarity & Presentation | 55 | 58 | 58 | 52 | 52 | 55.0 | 54.9 | 6 |
| Novelty & Originality | 45 | 45 | 50 | 48 | 45 | 46.6 | 46.4 | 5 |
| Significance & Impact | 50 | 52 | 58 | 55 | 48 | 52.6 | 52.3 | 10 |
| Experimental Validation | 38 | 45 | 48 | 46 | 36 | 42.6 | 42.2 | 12 |
| Reproducibility | 45 | 50 | 52 | 50 | 45 | 48.4 | 48.1 | 7 |
| Ethical Compliance | 55 | 58 | 50 | 55 | 55 | 54.6 | 54.8 | 8 |
| **Composite** | 46.1 | 50.5 | 53.0 | 50.6 | 44.6 | **49.0 (before)** | **48.7 (after)** | |
| Pool position (P%) | 30 | 42 | 50 | 44 | 32 | | | |

No dimension spread exceeds 20 points; no consistency warnings.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 1 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation" to ICLR. Controlled comparisons of how teacher reasoning traces are augmented, filtered and mixed for small students are of real interest, and the amount of work behind the study is evident.

**Overall Assessment:** The panel found the question important and the breadth (five teachers, several students, text/agentic/visual tasks, data-volume and transfer analyses) valuable, and appreciated the reporting of negative results. The panel was also concerned that the study's central ranking and several written conclusions are not yet supported by the evidence as presented. This is how a careful panel would likely see this draft, not a prediction of any real outcome.

**Key Strengths Identified by Reviewers:**
1. A uniform pipeline across methods, teachers, students and modalities (R1-S1, R2-S2, R4-S2).
2. Practitioner-relevant questions, including data volume and teacher–student pairing (R3-S1, R4-S1).
3. Honest negative findings and arithmetic that is largely consistent within tables (R1-S2, R4-S3, DA Observations).

**Key Concerns Requiring Attention:**
1. Augmentation vs baseline comparison is not size-/step-matched and the reference rows in Table 1 are inconsistent (CONSENSUS-3).
2. Written conclusions contradict or are not tested by the tables: LLM-judge filtering, "+1.93 over Vanilla CoT", untested combined pipelines and "best practices" (CONSENSUS-3).
3. No variance on small test sets; weak or implausible baselines; unexplained Table 5 results (CONSENSUS-2).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection — that the headline gain may reflect more training data and steps relative to an over-trained baseline — is a MAJOR issue that the authors can answer with a matched-budget experiment.

**Decision: Borderline Reject (3).** In its current form the reasons to reject outweigh the reasons to accept; the conclusions must be re-grounded in matched controls and a corrected baseline, which requires new experiments, before the contribution can be judged. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Amara Lindqvist-Osei
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Augmentation gain not isolated from data size/steps | R1, R3, DA | CONSENSUS-3 |
| Text–table contradictions and inconsistent rows | R1, R4, DA | CONSENSUS-3 |
| Guidelines/"best practices" not tested (no combined pipeline) | R1, R4, DA | CONSENSUS-3 |
| Learnability/teacher explanations untested | R2, R3, DA | CONSENSUS-3 |

(CONSENSUS-2: no variance — R1, DA; weak baselines — R1, DA; benchmark artefact thin — R2, R4; OOD design — R1, DA; governance/contamination — R3, DA; selection on test split — R1, DA.)

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| How severe: Reject vs Borderline Reject | R1, DA (2) | R2, R3, R4 (3) | The defects are repairable with existing resources and the topic is valuable; EIC sides with 3 (weighted rating 2.56 rounds to 3) |

### Score Spread Discussion
No dimension has a spread above 20; the widest (Technical Rigor and Experimental Validation, 12) separates R1/DA (36–42) from R3 (48–52): R1/DA weight the verified baseline and confound issues more heavily, which the EIC verified, but the issues are fixable, so the official mean stays in the typical-rejected band.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Augmentation confounded with data size/steps | Yes (R1-W1, R3-W4) | n/a | n/a |
| DA-M2 | MAJOR | Selection/mixing conclusions vs Table 1 | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Vanilla baseline below No-CoT/zero-shot | Yes (R1-W2) | n/a | n/a |
| DA-M4 | MAJOR | Guidelines untested | Yes (R1, R4) | n/a | n/a |
| DA-M5…M8 | MAJOR | Variance, student-dependence of Reverse, OOD design, test-split selection | Partly (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Augmentation vs baseline not matched in data size/steps; post-augmentation sizes unreported | R1-W1, DA-M1, R3-W4 | §3.1.1, App. C.1, Table 1, Table 6 | Matched-budget arms (same #examples/steps) for Vanilla, Answer-Aug, Reverse; report sizes | High; ≈100–150 A100-h | Partly (one task/student) |
| P1-2 | Table 1 reference rows wrong/inconsistent; Vanilla baseline implausible (below No-CoT, below zero-shot on MATH/ANLI) | R1 ERR-1/2/5, R1-W2, DA-M2/M3 | Table 1, §4.2 Q1 | Re-base selection/mixing on the Vanilla-CoT run; fix labels; document answer extraction; tuned Vanilla baseline | Medium; ≈30–60 A100-h | Yes |
| P1-3 | Conclusions contradicting or not backed by tables (Judge filtering "highly effective", "crucial"; guidelines; "consistently" in Q11) | R1-W4, R4-W4, DA-M2/M4 | §4.2 Q1–Q3, §4.4.2 Q11, §5, §1 ③ | Rewrite to the numbers, or run the recommended combined pipelines against Reverse alone | Low (rewrite) / Medium (runs) | Yes (rewrite) |
| P1-4 | No variance, no significance on 169–229-item test sets | R1-W3, DA-M5 | Tables 1–5, Fig. 5–6, Table 6 | Seeds, mean ± std, paired bootstrap CIs; drop ranking of within-noise differences | Medium | Partly |
| P1-5 | Method selection on the reported test split; no validation split; hyper-parameters, L, τ, α, prompts missing | R1-W5, DA-M8 | Table 6, §4.3.1, App. C | Validation splits; selection/epochs on validation; full hyper-parameter/prompt appendix | Medium | Yes (appendix) / Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| P2-1 | Table 5 OOD design and MATH→GSM8K anomaly | R1-W6, ERR-8, DA-M7 | State configs; add no-CoT/in-domain controls; explain 80.74 | Medium | Yes |
| P2-2 | Reverse's student dependence (Qwen vs Llama) not reflected in F1 | DA-M6 | Report Reverse vs Vanilla for every student; qualify claim | Medium | Yes |
| P2-3 | Benchmark not specified as an artefact; "first" overclaim | R2-W2, R4-W1 | Protocol section, master table, release plan; scope statement; cite Li et al. (2502.12143) as source of the learnability gap; discuss OpenThoughts (arXiv 2506.04178) and OpenMathInstruct-1 (arXiv 2402.10176) | Low–Medium | Yes |
| P2-4 | Dated scope (no long-CoT teacher) | R2-W1 | Add one reasoning-model teacher and a larger math set, or scope claims | High | No |
| P2-5 | Learnability/teacher explanations untested | R2-W4, R3-W1, DA-M5 | Student-side diagnostics (loss/perplexity on traces, trace length) | Medium | Partly |
| P2-6 | Governance: provider ToS, NC licences (ANLI/e-SNLI), contamination, positive-only Broader Impact | R3-W3, DA stakeholders | Add paragraphs and a contamination check | Low–Medium | Yes |
| P2-7 | Table/text consistency items (ERR-4, 6, 7; Table 1 caption; teacher names; WebArena actor) | R1 Error Log, R4-W3 | Consistency pass | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| P3-1 | Inference cost/token-length per method; one full-fine-tuning check | R3-W2 | Report output tokens and latency |
| P3-2 | Easy-to-hard curriculum vs fixed-ratio mixing; random-selection baseline | R3-W1, W4 | Add as extra arms |
| P3-3 | Student-error filter definition (teacher rationale not required to be correct); judge validation; Date duplicate cell; Table 6 "Filtered > Original" semantics | R2-W3, DA-m2–m4 | Clarify |
| P3-4 | Helpful references (MAmmoTH2, LIMO, Demystifying Long CoT; MiCoTA) | R2 | Cite as context (MiCoTA, OpenThoughts: recent preprints, discussion only) |

## Estimated Revision Effort
- Priority 1: 5 items, ≈ 2–3 weeks including ≈ 150–250 A100-hours of new runs (can be partly shown in a one-week rebuttal on a single student and 3–4 tasks).
- Priority 2: 7 items, ≈ 1–2 weeks (P2-4 is the expensive one).
- Priority 3: 4 items.
- **Total estimated revision time**: ≈ 4–5 weeks.

*No Post-Review Analysis (Gap Scout) was requested and none was run.*
