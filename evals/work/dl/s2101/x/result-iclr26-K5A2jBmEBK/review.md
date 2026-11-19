# Simulated Panel Review: DeepCompress (ICLR, full mode)

*Date: 2026-11-10. Simulation of how a careful panel would likely see this draft; not a prediction of any real outcome. Personas are fictional. The five reviewers were run as separate role-based passes in one shared model context (no subagents), so they are not independent agents. Figures were not available: Figures 1–4 are judged from captions and surrounding text only, and the numeric labels of Figure 3 are garbled in the text extraction.*

**Run settings:** target venue ICLR (stated), literature check `strict` with cutoff 2025-09-24, confirmation skipped.

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains |
| Primary Discipline | Machine learning → RL post-training of large language models for efficient mathematical reasoning |
| Secondary Discipline(s) | Exploration in RL (policy entropy), curriculum and adaptive computation |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Zero-RL with DAPO/GRPO-style rollouts, rule-based verifier reward, length reward shaping (sigmoid of within-group standardized length), difficulty from group pass ratio vs. EMA batch pass ratio |
| Target Venue | ICLR 2026, top-tier ML conference (stated by user); profile key `iclr` |
| Venue-Specific Notes | none |
| Paper Maturity | Submission-ready |
| Ethics-Relevant Content | none (math benchmarks, no human data); no broader-impact statement |

### Claimed Contributions (as stated by the authors)
1. **C1** (Sec. 3, Fig. 1, Sec. 1): longer responses cover a wider range of correct solutions than shorter ones for the same problem (pass@32 rises with length while pass@1 falls).
2. **C2** (Sec. 4.2, Eqs. 3–5): a dual length reward that favours shorter responses on "Simple" questions and longer responses on "Hard" questions.
3. **C3** (Sec. 4.3–4.4, Eqs. 6–11): a model-aware difficulty signal, β_i = P_g(x_i) − P_b, with a correctness-conditioned length reward and an EMA-smoothed batch pass ratio.
4. **C4** (Sec. 5.2, Table 1, Fig. 3): new SOTA among Zero-RL models on seven math benchmarks (+2.0 avg for 3B, +2.7 for 7B) with 57.9% / 16.6% shorter responses.
5. **C5** (Secs. 5.3–5.4, Fig. 4, Table 2): the gains arise from higher policy entropy, exploration and more effective reflection.

### Paper memory (factual record, shared with all reviewers)
- **Setup facts.** Base models Qwen2.5-3B and Qwen2.5-7B, trained with DAPO following the DeepMath recipe (Sec. 4.1, Sec. 5.1); training data for DeepCompress not named explicitly (DeepMath-103K is named only for the DeepMath-Zero baselines, Sec. 3.1). Table 3 (App. B): lr 1e-6, KL 0, train batch 512, rollout.n 32, max response length 10K, 500 steps, α 0.2, λ 0.99. Evaluation: 16 samples per question, T 0.6, top-p 0.95, max tokens 32,768 (Sec. 5.1). Checkpoint selected on a validation set of 60 MATH and 60 AIME 2022–2023 questions (Sec. 5.1). Baselines are re-evaluated by the authors (Sec. 5.1). Seeds, number of training runs, compute, and code release: not stated after search (link footnotes were removed from the blinded text).
- **Headline numbers.** Table 1: DeepCompress-Zero-3B avg 36.6 vs DeepMath-Zero-3B 34.6; 7B 48.7 vs 46.0; AIME24 7B 23.5 vs 19.4; AIME25 7B 19.6 vs 13.1. Sec. 5.2 text: length reduced 57.9% (3B) and 16.6% (7B) on average (Fig. 3). Table 2: hard-question pass@1 and reflection counts.
- **Appendix.** A: GPT-4o prompt for behaviours. B: training configuration (Table 3). No extra experiments.
- **Unverifiable.** Figures 1–4 (not available); Fig. 3 bar values garbled.
- **Integrity scan:** `integrity_scan.py` found no reviewer-directed text or hidden characters. The reviewers read the (unchanged) redacted copy.
- **Literature check:** run in `strict` mode (cutoff 2025-09-24): 7 queries in total (4 claim: C1×2, C2, C3; 1 baseline; 2 expansion) of 12 allowed. Gaps left open: no peer-reviewed prior work from 2021–2024 was kept (arXiv-only search); the benchmark scout returned no benchmark list, so the baseline scout table could not be built.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ottoline Reyes-Baptiste, senior faculty, large public research university (Southern Europe)
- **Seniority / Expertise**: Senior faculty / reinforcement learning, language-model post-training, evaluation practice
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what the venue actually accepts; weights reviewers by what they got right.

### Reviewer 1 (Methodology): Dr. Marit Halvorsen-Adeyemi, industrial research lab (Northern Europe)
- **Seniority / Expertise**: Senior industry scientist / RLVR training pipelines (GRPO/DAPO), reasoning-model evaluation, pass@k estimation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched training budgets and control runs; recomputes tables.

### Reviewer 2 (Domain): Prof. Wen-Hui Takeda-Marsh, NLP group, large public research university (East Asia)
- **Seniority / Expertise**: Senior faculty / efficient reasoning, chain-of-thought compression, length-reward shaping
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Positions every method against its nearest neighbour.

### Reviewer 3 (Perspective): Dr. Soledad Ibarrondo-Nkemelu, operations research and cognitive science department, research university (Latin America)
- **Seniority / Expertise**: Mid-career / adaptive computation, bandit resource allocation, metacognition
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive, points toward extensions.

### Reviewer 4 (Generalist): Dr. Priyanka Vendramin, machine-learning group, mid-size university (South Asia)
- **Seniority / Expertise**: Mid-career / deep learning for language and vision
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical programme-committee member; weighs weaknesses against typical accepted ICLR papers.

### Devil's Advocate: Prof. Gideon Altamirano-Sze, statistics and evaluation methodology group, research university (North America)
- **Seniority / Expertise**: Senior faculty / causal inference, evaluation methodology
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks what else explains the result.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

# Peer Review Report

## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Reviewer: Dr. Marit Halvorsen-Adeyemi, Methodology (industrial research lab, Northern Europe; fictional persona)
## Expertise: RLVR training pipelines; reasoning-model evaluation; pass@k estimation
## Date: 2026-11-10

## Summary
The paper adds a length reward to Zero-RL training of Qwen2.5-3B/7B. Within each rollout group, a response's length is standardized (Eq. 3) and passed through a sigmoid whose sign is set by β_i, the group pass ratio minus an EMA-smoothed batch pass ratio (Eqs. 6–8, 11). Questions easier than the batch average thus reward shorter correct answers, and harder ones reward longer correct answers (Eq. 10). The authors report higher average accuracy than DeepMath-Zero and shorter outputs on seven math benchmarks (Table 1, Fig. 3), and argue the mechanism works through entropy and reflection (Sec. 5.3–5.4).

## Strengths
### S1: Simple, cheap mechanism that is easy to reproduce
The method is a few lines on top of the verifier reward: Eqs. 3–5, 8, 10, 11 fully specify the reward, and Table 3 lists the optimizer, rollout and reward hyperparameters. Training costs no more than ordinary DAPO.

### S2: Baselines were re-evaluated under one protocol
Sec. 5.1 states that all baselines were re-evaluated "under our precise evaluation settings" with a fixed decoding configuration (T 0.6, top-p 0.95, 16 samples, 32,768 max tokens), so Table 1 is not a mix of copied numbers.

### S3: Arithmetic in the headline table is correct
I recomputed Table 1's averages: DeepCompress-3B (75.3+49.4+39.3+32.7+16.7+7.1+35.8)/7 = 36.6; DeepMath-3B 242.1/7 = 34.6; 7B 341.2/7 = 48.7 vs 322.1/7 = 46.0. The stated deltas (+2.0, +2.7, +4.1 on AIME24, +6.5 on AIME25) hold. The 3B/7B length reductions in Table 2 (11,222 → 4,853, i.e. −56.8%; 7,180 → 5,942, −17.2%) are consistent with the text's 57.9% and 16.6%.

### S4: Training dynamics are inspected rather than only final numbers
Fig. 4 (per the text) tracks entropy, training length and test pass@1 for fixed-β variants, which exposes how the length reward changes optimization.

## Weaknesses

### W1: The main comparison is not matched in training recipe, so the gain cannot be attributed to the dual length reward (Table 1, Sec. 5.1, Table 3, Sec. 6)
DeepCompress is trained from the Qwen base with DAPO, a 10K response cap and a 2K overlong buffer for 500 steps (Table 3), and the authors list the 10K cap as a limitation ("we capped the maximum generation length at 10k tokens", Sec. 6). The DeepMath-Zero baselines are released checkpoints whose cap, steps and chat template are never stated, and the paper changed the chat template ("we adjusted the chat template", Sec. 5.1). DAPO's overlong shaping itself penalizes long responses, so the cap alone could explain much of the 57.9% length reduction for 3B, where a Fig. 3 label of 14,128 tokens appears for DeepMath-Zero-3B (as extracted; the figure labels are garbled). No row trains the same recipe (same data, cap, template, 500 steps) *without* the length reward.
- **Suggested Fix:** Add "DAPO, same recipe, no length reward" (3B and 7B) to Table 1 and Fig. 3, and report the baseline's cap and step count. Cost: about one extra run per size, comparable to the main runs (order of 10²–10³ GPU-hours depending on the 7B setup).

### W2: No component ablation and no ablation of the "robustness" additions (Secs. 4.3, 4.4, 5.3)
Sec. 5.3 compares only fixed-β variants (β = ±1) against DeepCompress. There is no ablation of Eq. 10 (correctness conditioning), Eq. 11 (EMA smoothing), α, λ, or of the *direction* of the signal (e.g., reversed assignment, random assignment, or Simple-only penalty). Because Eq. 11 initializes P_b at 1.0 with λ = 0.99, P_{b,t} ≥ 0.99^t (derived: ≥ 0.61 at step 50, ≥ 0.37 at step 100). During the first ~100 steps nearly every question has P_g < P_b and is labelled "Hard", so training starts with a long-response bonus phase regardless of actual difficulty. The "initial increase then controlled reduction" in length (Sec. 5.3) could therefore be a schedule produced by the EMA initialization rather than difficulty-aware allocation.
- **Suggested Fix:** Report DeepCompress without Eq. 10, without Eq. 11, with a hand-set length schedule (bonus then penalty, no difficulty), and with difficulty labels reversed or shuffled. At least the 7B runs on the validation split suffice.

### W3: The central mechanism (adaptive allocation, broader exploration on hard problems) is not measured (Sec. 4.2, 5.2, 5.4)
The text asserts "this strategy increases the probability of generating at least one correct solution for difficult problems" (Sec. 4.2), but no pass@k of the *trained* models is reported anywhere; Table 1 reports pass@1 only. Nor is response length reported by difficulty bucket: Table 2 shows hard-question responses become 57% shorter for 3B and 17% shorter for 7B, which is the opposite of "extending CoT for under-learned cases" relative to the baseline. Also by Eq. 10 the length bonus applies only to correct responses, so a group with zero correct samples (P_g = 0) receives no length signal; the bonus can only reshape length among already-correct samples and cannot by itself raise the chance of finding a first correct one.
- **Suggested Fix:** Report pass@k (k up to 32/64) for DeepMath-Zero, DAPO-control and DeepCompress, and mean length per difficulty bucket (using the DeepMath difficulty labels or fixed pass-rate bins).

### W4: Efficiency claims are untested against any efficiency baseline (Table 1, Sec. 5.2, Sec. 2)
The introduction positions the work against length-penalty RL (Team et al., Luo et al., Aggarwal & Welleck, Liu et al.) and says they trade accuracy for brevity. Table 1 contains no such method; DeepMath-Zero is an accuracy-oriented Zero-RL model, not a compression method. "Improves efficiency" is thus only shown relative to a model that was never trained to be short. The fixed-β=+1 "Length Penalty" variant is the only efficiency control, and its final accuracy on the seven benchmarks is not tabulated.
- **Suggested Fix:** Add at least one length-RL baseline (e.g., a plain length penalty and one adaptive-penalty method) in the same recipe, and tabulate β = ±1 variants on all seven benchmarks with length.

### W5: Single training run, noisy selection, small test sets (Sec. 5.1, Table 1)
No seeds or variance are reported. AIME24/25 have 30 problems each, so +4.1 points avg@16 is about 1.2 problems and +6.5 about 2 problems (derived). On MATH-500 at 7B the result is a tie (85.6 vs 85.6). Checkpoints are selected by pass@1 on a 120-question validation set, which is itself noisy; whether the baselines received comparable checkpoint selection is not stated. Gains on the larger sets (+2.0 on OlympiadBench and Minerva at 7B) are plausible but unquantified.
- **Suggested Fix:** Report ≥3 training seeds for 7B (or bootstrap CIs over questions and samples, plus seed variance on a smaller proxy); state how baselines' checkpoints were chosen.

### W6†: Pass@k-by-length analysis (Sec. 3, Fig. 1) cannot be assessed from the text (rewritten as a question after Phase 1.6)
Bins are of uniform width in z, so sample counts per bin are uneven, and the pass@32 estimator in Eq. 1 needs n ≥ 32 per problem per bin. For fixed n, pass@32 is a monotone function of the bin's accuracy, so the reported divergence between pass@1 (falling) and pass@32 (rising) must come from averaging across problems with different bin occupancy. This is a question for the authors (see Q1), not an error claim: Fig. 1 was unavailable.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | Sec. 1 vs Sec. 4.1 | "With Group Relative Policy Optimization (GRPO, Shao et al., 2024) as our basic RL algorithm" / "utilize DAPO (Yu et al., 2025a) as our RL algorithm" | The RL algorithm is stated as GRPO in the intro and DAPO in Sec. 4.1/5.1; DAPO's dynamic sampling changes which groups reach Eq. 8 | Cross-referenced (two locations) | High | MINOR | State one algorithm; say whether dynamic sampling filters P_g ∈ {0,1} groups before P_b (Eq. 7) is computed |
| ERR-2 | E5/E1 | Sec. 5.2 vs Table 1 | "consistently outperforms all existing Zero RL baselines across all seven mathematical reasoning benchmarks" | Table 1, MATH-500 at 7B: DeepCompress 85.6 = DeepMath-Zero-7B 85.6 (tie) | Cross-referenced | High | MINOR | Say "matches or exceeds" |
| ERR-3 | E6 | Sec. 5.4 vs App. A | "track the emergence of four cognitive behaviors" | Table 2 reports one "Reflect" column; the Appendix A prompt lists backtracking, verification, subgoal setting, enumeration, none named "reflection" | Cross-referenced | High | MINOR | Define "Reflect" and report all four behaviours |
| ERR-4 | E5 | Sec. 5.3 | "achieving simultaneous optimality in both dimensions" | Same section: "length bonus variant exhibits higher performance compared to other methods" and "length penalty variants produce remarkably shorter responses" | Cross-referenced (text only; Fig. 4 unavailable) | Medium | MINOR | Remove "optimality"; tabulate the Pareto trade-off |

## Missing References
*(Domain Reviewer's role; none added here.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gain attribution is unresolved (W1, W2) and mechanism untested (W3). |
| Clarity | 3 | Method is fully specified; minor inconsistencies (ERR-1, ERR-3). |
| Significance | 2 | Modest average gains; efficiency unbenchmarked. |
| Originality | 2 | Difficulty-adaptive length shaping is a crowded area; sign flip is the delta. |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison is confounded by an unmatched recipe and 10K cap (W1), and the efficiency claim has no efficiency baseline (W4); these are signals of a typical rejected submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Mechanism unmeasured, no ablations of the added components. |
| Clarity & Presentation | 62 | Competent | Reward fully defined; GRPO/DAPO and which reward form is trained are unclear. |
| Novelty & Originality | 52 | Developing | Incremental over difficulty-adaptive length rewards; see R2. |
| Significance & Impact | 56 | Competent | Useful if confirmed; unconfirmed. |
| Experimental Validation | 44 | Developing | No matched control, no efficiency baselines, single run. |
| Reproducibility | 60 | Competent | Table 3 hyperparameters present; code, data for training, baseline settings unverified. |
| Ethical Compliance | 62 | Competent | Limitations paragraph present; nothing at stake. |

## Questions for Authors
1. For Fig. 1: how many samples n fall in each of the 16 bins per problem, and how is pass@32 averaged across problems when n differs? Is "8,192 responses per problem" correct (it implies ~4.1M generations per model on MATH-500 alone)? A bin-size-matched analysis would raise my Quality score.
2. What max response length, number of steps and chat template did DeepMath-Zero use, and what does DAPO with your recipe but no length reward score and weigh in at in length?
3. Does the headline model use Eq. 10 (Fig. 2 shows the length reward on incorrect responses, Eq. 9)? Does dynamic sampling remove P_g ∈ {0, 1} groups before β is computed?
4. Are the 60 "MATH" validation questions disjoint from MATH-500?
5. What are the final accuracies and lengths of the β = ±1 variants on all seven benchmarks?

## Limitations Assessment
**Partially.** Sec. 6 acknowledges reliance on within-group length variation and the 10K cap, but not the single-run evidence, math-only/Qwen-only scope, or the cap's interaction with the length results.

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): An easily reproduced idea with plausible results, but the central attribution is not controlled and the efficiency claim has no efficiency baseline.

## Confidence
**4**: I checked the equations, tables and appendix; Figures were unavailable.

---

# Peer Review Report

## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Reviewer: Prof. Wen-Hui Takeda-Marsh, Domain (NLP group, large public research university, East Asia; fictional persona)
## Expertise: efficient reasoning; CoT compression; length-reward shaping
## Date: 2026-11-10

## Summary
The paper argues that RL methods that always shorten reasoning chains may limit the model's reasoning boundary, and proposes to shorten chains only for questions the model currently finds easy, while rewarding longer chains for questions it finds hard. Difficulty is defined online as the group pass ratio relative to a batch-level pass ratio. On Qwen2.5-3B/7B with a DeepMath-style Zero-RL recipe, it reports modest accuracy gains and shorter outputs than DeepMath-Zero (Table 1, Fig. 3).

## Strengths
### S1: Well-motivated question
The tension between shortening for efficiency and keeping exploratory length for hard problems is real and clearly framed (Sec. 1, Sec. 3). The observation that pass@1 falls with length while pass@32 rises (Sec. 3.2, per its text) is a useful hypothesis for RL practitioners.

### S2: Difficulty is obtained for free from rollouts
Using P_g and P_b (Eqs. 6–8) avoids external difficulty labels and tracks the evolving model (Sec. 4.3). This is a practical design.

### S3: The "bonus for hard questions" direction is the distinctive element
Related work cited by the paper mostly penalizes length (Sec. 2). Reversing the sign for relatively hard questions is the clearest delta from that literature.

### S4: Related work is organized sensibly
Sec. 2 separates prompting, SFT and RL families and acknowledges difficulty-calibrated methods (Cheng et al., 2025; Yu et al., 2025b).

## Weaknesses

### W1: Difficulty-adaptive length shaping already exists; the paper does not differentiate from it empirically or in text (Sec. 2, Sec. 4.3)
Sec. 2 itself says Cheng et al. (2025) calibrate "the length penalty based on task difficulty" and Yu et al. (2025b) adapt the reasoning budget to difficulty, yet neither is compared against or contrasted in Sec. 4. Per my literature check (strict mode, arXiv abstracts), the closest prior peer-reviewed work is GRPO-LEAD (difficulty-aware RL with length-regularized rewards for concise math reasoning, 2025), and recent preprints Adaptive Length Penalty (ALP; per-prompt online solve rate scales the length penalty, "hard prompts remain unhindered"), Su & Cardie (adapts the accuracy–length trade-off to model performance) and AdaCtrl (difficulty-aware budgeting). The recent preprints are "worth discussing" only and not a basis for score reduction; the peer-reviewed GRPO-LEAD covers parts of C2/C3 at partial level. Net: the Simple half and the online-solve-rate signal are not new; the Hard-side bonus and the P_g − P_b form are the contribution. This is a Novelty weakness (MAJOR at most), not a "known results" case.
- **Suggested Fix:** Add a paragraph and a table row contrasting with an online-solve-rate penalty (e.g., ALP-style) and with Cheng et al./Yu et al.; state exactly what the signed β adds.

### W2: Motivation (C1) is stated as established while the supporting analysis is thin and not tied to the method (Sec. 3.2, Sec. 4.2)
The evidence that "longer responses contain a wider coverage of potentially correct solutions" is a within-model pass@k-versus-length plot on two models trained by others. The leap from "long-bin responses have higher pass@32" to "rewarding length on hard questions broadens the reasoning boundary" is not checked for the trained models. The related question of whether RL expands or merely sharpens the base model's pass@k boundary is not engaged (see Missing References), which would sharpen what "reasoning boundary" means here.
- **Suggested Fix:** Report pass@k for trained models and cite/discuss the RL-boundary literature.

### W3: Characterization of cited prior work is partly inconsistent (Sec. 1, Sec. 2) [E7, low confidence → Question]
Liu et al. (2025) is cited among "token-length reward functions" (Sec. 1) and as "self-supervised optimal length signals" (Sec. 2). The arXiv abstract of the cited paper (2505.15612) describes length-based reward shaping with a step reward controlled by a target length. I cannot tell from the abstract alone whether the Sec. 2 label fits, so I ask rather than assert (Q2).

### W4: "New state-of-the-art" is scoped too broadly (Sec. 5.2, Sec. 6)
Table 1 contains three 7B Zero-RL baselines and one 3B Zero-RL baseline. The SOTA claim should be limited to this baseline set and model sizes; other recent Zero-RL recipes for Qwen2.5-7B are not included.
- **Suggested Fix:** Narrow the wording, and add one more recent Zero-RL 7B baseline if available.

## Literature-check addendum (strict, cutoff 2025-09-24)
**Per-claim novelty (claim-level profile; `related_search.py novelty`):**

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 longer responses cover more correct solutions | result | no close prior work found in 8 results (at most medium) | none above level 2; Su et al., "Between Underthinking and Overthinking" (arXiv 2505.00127, recent preprint, shared topic) | arXiv-only search; this is a limit of the search, not evidence of novelty |
| C2 dual length reward | method | medium | GRPO-LEAD (level 3, https://arxiv.org/abs/2504.09696, prior peer-reviewed, not cited) | Difficulty-aware and length-regularized rewards exist; the signed Hard-side bonus is new in the retrieved set. Worth discussing: ALP (arXiv 2506.05256, recent preprint) |
| C3 model-aware difficulty (P_g vs EMA P_b) | method | medium | GRPO-LEAD (level 3, same link, not cited) | Difficulty-aware reweighting exists; online solve rate used by recent preprints. Worth discussing: Su & Cardie (arXiv 2505.18298, recent preprint) |

Script reading: "no central claim fully covered by prior work"; attribution (closest to the paper as a whole): GRPO-LEAD. One missing prior-peer-reviewed comparison is MAJOR at most, and here only a differentiation request.

**Novelty delta table:**

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| Dual length reward | GRPO-LEAD (prior); ALP (recent preprint) | Length-regularized, difficulty-aware rewards; penalty scaled by per-prompt solve rate | Length *bonus* for relatively hard questions; relative-to-batch sign | Not cited |
| Model-aware difficulty | GRPO-LEAD; Su & Cardie (recent preprint) | Difficulty-aware reweighting; accuracy-conditioned length trade-off | P_g − P_b with EMA, used as signed coefficient | Not cited |

**Baseline scout:** `related_search.py benchmarks` returned no benchmark list for this paper, so no baseline scout table was built and no under-reported baseline could be checked. All baselines in Table 1 are re-evaluated by the authors, so under-reporting against copied numbers does not arise.

**Field snapshot (as of the cutoff, from kept abstracts).** By late 2024 efficient reasoning meant prompting and SFT on shortened chains (e.g., the overthinking work cited as Chen et al., 2024). Early 2025 moved to RL with length-based rewards, and by May–June 2025 several preprints made the penalty adaptive to difficulty or accuracy (ALP, Su & Cardie, AdaCtrl, AALC), several reporting roughly 50% token reductions on math benchmarks with maintained accuracy. Open problems stated in the retrieved abstracts: calibrating length to difficulty, and models "underthinking" harder problems. In this sub-field, a >50% token cut at equal accuracy is now common and not a distinguishing result; a clear Pareto gain over strong length-RL baselines, or direct evidence that a length bonus on hard problems raises the pass@k boundary, would count as significant. I used this to score Novelty (50) and Significance (58): modest gains plus a distinctive direction, with the efficiency side unbenchmarked.

## Missing References
*Verified with `related_search.py verify`; unverified entries are marked `[verify]`.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | none (no verified prior-peer-reviewed work is a required comparison) | |
| Important | Zhang & Zuo, "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models" (arXiv 2504.09696, 2025; found, labelled peer-reviewed) | Difficulty-aware, length-regularized GRPO for math: closest prior work. |
| Important | Liu et al., "Understanding R1-Zero-Like Training: A Critical Perspective" (arXiv 2503.20783, 2025; title found by `verify`; content description from my knowledge, `[verify]`) | A critical analysis of R1-Zero-like training, relevant to the Zero-RL baselines and to length dynamics. |
| Important | Yue et al., "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" (arXiv 2504.13837, 2025; title found by `verify`; content description from my knowledge, `[verify]`) | Discusses the pass@k view of the reasoning boundary that C1 invokes. |
| Important (worth discussing, recent preprint) | Xiang et al., "Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning" (arXiv 2506.05256; found) | Online per-prompt solve rate scales the length penalty. |
| Important (worth discussing, recent preprint) | Su & Cardie, "Thinking Fast and Right: Balancing Accuracy and Reasoning Length with Adaptive Rewards" (arXiv 2505.18298; found) | Adapts reward trade-off to model performance. |
| Helpful (recent preprint) | Huang et al., "AdaCtrl: Towards Adaptive and Controllable Reasoning via Difficulty-Aware Budgeting" (arXiv 2505.18822; found) | Difficulty-aware reasoning budget. |
| Helpful (recent preprint) | Su et al., "Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs" (arXiv 2505.00127; found) | Empirical length–correctness study relevant to C1. |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mechanism evidence thin. |
| Clarity | 3 | Clear exposition. |
| Significance | 2 | Moderate in a crowded sub-field. |
| Originality | 2 | Incremental over difficulty-adaptive rewards; signed bonus is the delta. |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper has a distinctive, intuitive idea and a decent table, but the novelty delta is narrow in a crowded 2025 sub-field and the closest neighbours are neither cited nor compared.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Reasonable design; the justification relies on an untested step from Fig. 1 to training. |
| Clarity & Presentation | 64 | Competent | Positioning is listed rather than argued. |
| Novelty & Originality | 50 | Developing | Medium per-claim verdicts; narrow delta. |
| Significance & Impact | 58 | Competent | Relevant, practical topic; modest evidence. |
| Experimental Validation | 50 | Developing | No comparison with difficulty-adaptive or length-RL methods. |
| Reproducibility | 62 | Competent | Reward definitions explicit. |
| Ethical Compliance | 62 | Competent | Nothing at stake. |

## Questions for Authors
1. What exactly does the signed β add over an online-solve-rate-scaled length penalty (ALP-style) and over GRPO-LEAD's difficulty-aware reward? An experiment answering this could raise Novelty.
2. Is the Sec. 2 label "self-supervised optimal length signals" for Liu et al. (2025) accurate for LASER-style step rewards?
3. Do trained models actually show larger pass@k on hard problems than the DAPO control?

## Limitations Assessment
**Partially.** Sec. 6 is short and does not discuss overlap with difficulty-adaptive methods or the single-domain scope.

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): A distinctive direction with a narrow novelty delta in a crowded area and no comparison with the nearest neighbours.

## Confidence
**4**: I know this sub-field; the literature check supports but arXiv covers only part of it.

---

# Peer Review Report

## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Reviewer: Dr. Soledad Ibarrondo-Nkemelu, Perspective (operations research and cognitive science, research university, Latin America; fictional persona)
## Expertise: adaptive computation; bandit resource allocation; metacognition
## Date: 2026-11-10

## Summary
The paper treats reasoning length as a resource that should be allocated by problem difficulty, as humans and adaptive-compute systems do: spend less on mastered problems, more on hard ones. It implements this as an RL reward whose sign depends on whether a question is solved more or less often than the batch average, and reports accuracy gains with shorter responses on math benchmarks.

## Strengths
### S1: A principled framing of test-time compute allocation
Allocating effort by difficulty is the same structure as adaptive computation time and budgeted bandits. The idea that a *relative* difficulty signal (P_g − P_b, Eq. 8) keeps the policy pressure meaningful as the model improves is appealing, and is a self-calibrating alternative to fixed difficulty labels (Sec. 4.3).

### S2: Practical stakes are clear
Fewer tokens per response (Fig. 3, Table 2) matter to anyone serving reasoning models, and the paper's headline is that this need not cost accuracy.

### S3: Entropy diagnostics give a window into exploration
Reporting entropy next to length and accuracy (Fig. 4, per its text) connects the method to the RL exploration literature, even though the causal reading needs more support.

### S4: The method does not need extra models or labels
No judge, teacher or difficulty annotation is required (Sec. 4.3), which makes it easy to adopt.

## Weaknesses

### W1: Tokens are used as a proxy for cost, and difficulty as a proxy for need (Sec. 5.2, Fig. 3)
Only response length in tokens is reported. Wall-clock latency or throughput on a serving stack is not, and the authors' own recipe caps training at 10K tokens (Table 3) while evaluating at 32,768 (Sec. 5.1). For deployment users the relevant outcomes include truncation rate, latency, and behaviour on queries longer than the training cap.
- **Suggested Fix:** Report the fraction of responses hitting max length for every model, and one latency/throughput number on fixed hardware.

### W2: Unexamined assumptions behind the relative-difficulty rule (Sec. 4.3)
(a) "Hard" is defined relative to the batch mean, so a question solved 90% of the time in a batch with mean 95% is still "Hard" and receives a length bonus; the label says nothing about absolute difficulty. (b) The signal's scale is small: with α = 0.2 and, e.g., β = 0.2, the sigmoid term varies by only ~0.04 reward units between z = −2 and z = +2 (derived), versus the ±1 outcome reward (Eq. 2), so the effective push depends heavily on |β| = |P_g − P_b|, whose distribution during training is never shown. (c) The EMA initialized at 1.0 (Eq. 11) makes early training a "Hard-everywhere" phase (derived: P_{b,t} ≥ 0.99^t). Together these suggest the dynamics could be driven by the schedule and the cap rather than by difficulty-awareness.
- **Suggested Fix:** Plot the distribution of β and the fraction of "Simple"/"Hard" questions over training; compare labels with the DeepMath difficulty annotations the paper mentions (Sec. 4.3).

### W3: Scope and generality (Sec. 5.1, Sec. 6)
Only math, only Qwen2.5 base models at 3B and 7B, one recipe. The claim that the framework "enhances both the accuracy and efficiency of LRMs" (abstract) is general; the evidence is for this setting.
- **Suggested Fix:** Narrow the wording, or add a second model family or a non-math task (e.g., code with unit-test verifiers).

### W4: No broader-impact or limitations depth (Sec. 6)
The limitations paragraph is short. Shorter reasoning could reduce transparency for hard problems (less visible chain-of-thought), and quicker answers on problems judged "Simple" by a noisy online signal could increase confident errors on edge cases. These are minor here but worth a sentence.
- **Suggested Fix:** Add two sentences on these trade-offs.

## Extensions I would like to see
Connections that could strengthen the work: adaptive computation time and PonderNet-style halting (Graves, "Adaptive Computation Time for Recurrent Neural Networks", 2016; Banino et al., "PonderNet", 2021), bandit-style allocation of rollouts across prompts, and prioritized/curriculum sampling by solve rate as an alternative to shaping length. A comparison of length shaping with simply allocating more rollouts to hard prompts would show whether the benefit lies in length or in extra samples.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound design, evidence still thin. |
| Clarity | 3 | Clear. |
| Significance | 3 | Practical, timely. |
| Originality | 3 | Fresh framing of a known reward family. |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the topic is timely and the idea is clean and adoptable, which puts it above the median submission; I place it just below the typical accepted paper because the evidence for the mechanism is thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Design sound; assumptions unexamined. |
| Clarity & Presentation | 70 | Competent | Easy to follow. |
| Novelty & Originality | 62 | Competent | Useful framing. |
| Significance & Impact | 68 | Competent | Practical value if confirmed. |
| Experimental Validation | 58 | Competent | Adequate for a first look; lacks controls. |
| Reproducibility | 66 | Competent | Hyperparameters and equations given. |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations present. |

## Questions for Authors
1. How do the "Simple"/"Hard" proportions and |β| evolve during training? Evidence that they are well spread would raise my score.
2. What is the truncation rate at 10K in training and at 32,768 at evaluation for each model?
3. Would giving hard prompts more rollouts (instead of rewarding length) achieve similar gains?

## Limitations Assessment
**Partially.** See W4.

## Ethics Review Flag
**No.**: Math benchmarks, no human data or misuse potential.

## Overall Score
**4** (Borderline Accept): A clean, timely idea whose practical value is plausible; the evidence is thinner than I would like.

## Confidence
**3**: I am from a neighbouring field and did not verify implementation details of the RL stack.

---

# Peer Review Report

## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Reviewer: Dr. Priyanka Vendramin, Generalist (machine-learning group, mid-size university, South Asia; fictional persona)
## Expertise: deep learning for language and vision
## Date: 2026-11-10

## Summary
The paper proposes rewarding shorter reasoning for questions a model finds easy and longer reasoning for those it finds hard, with "easy/hard" decided on the fly from rollout pass rates. Trained from Qwen2.5 base models, it outperforms a prior Zero-RL model on seven math benchmarks by about 2–3 points on average, with notably shorter responses, and offers entropy and reflection analyses as an explanation.

## Strengths
### S1: Clear problem, clear idea
The paper is easy to read, the equations are short, and the "Mechanism of β" box (Sec. 4.3) explains the sign and magnitude of the control in plain language.

### S2: Good venue fit
RL for reasoning and efficient inference is a core ICLR topic, and the method is adoptable by others.

### S3: Gains on the hardest benchmarks are the largest
Table 1 shows the largest gains at 7B on AIME24 (+4.1) and AIME25 (+6.5), which is where the method's motivation predicts improvement (subject to the noise caveat on 30-question sets).

### S4: Honest limitation statement
Sec. 6 states that the method relies on within-group length variation and that training used a 10K cap.

## Venue Criteria Checklist (ICLR: soundness, presentation, contribution)
| Item | Grade | Location |
|------|-------|----------|
| Claims supported by evidence (Soundness) | Partly | Table 1 supports the headline numbers; mechanism claims (Sec. 5.3–5.4) are weaker |
| Experiments appropriate and controlled | Partly | No matched no-length-reward control (Table 1, Table 3) |
| Significance of contribution | Partly | Modest average gain; crowded area |
| Presentation | Met | Secs. 3–4 clear; minor wording issues |
| Positioning in related work | Partly | Difficulty-adaptive neighbours cited in Sec. 2 but not compared |
| Limitations and reproducibility information | Partly | Sec. 6 and Table 3 present; baseline settings and code not visible |

## Weaknesses

### W1: The headline claim of simultaneous accuracy and efficiency gain rests on one comparison point (Table 1, Fig. 3)
Everything in Sec. 5.2 is relative to DeepMath-Zero. A reader cannot tell what part of the gain and the shortening comes from the length reward versus the training recipe (10K cap, steps, chat template; Sec. 5.1, Table 3). This is the most likely objection from other reviewers and is typical of papers that nevertheless get accepted when answered by one control run.
- **Suggested Fix:** Add a same-recipe DAPO control without the length reward.

### W2: Explanatory claims go beyond what Tables/Figures show (Sec. 5.3, Sec. 5.4, Table 2, Sec. 1)
The contribution list says the method "encourag[es] high policy entropy" (Sec. 1), but per Sec. 5.3 the length-bonus variant has the higher entropy and DeepCompress sits between. Table 2 shows a 7B reflection count of 2.64 vs 2.59 for the baseline (+0.05), described as "reflects more often", and the count comes from GPT-4o with a prompt that asks the judge to "actively identify and emphasize beneficial behaviors" (App. A) and no human validation. Entropy→performance is correlational.
- **Suggested Fix:** Soften the language, validate the GPT-4o tagger on a human-labelled sample, and report all four behaviours.

### W3: Related work is listed, not positioned (Sec. 2)
Sec. 2 enumerates methods and ends with "limited accuracy improvements" but never states how the signed difficulty reward differs from the difficulty-calibrated methods it just cited (Cheng et al., Yu et al.).
- **Suggested Fix:** Add a short "differences" paragraph and a comparison row.

**Minor:** typographical errors ("infeasbile", "diffifulty", "indenpendent", "Lentgh", "fluatuate", "accross", "Specfically"); "Easy" in the contributions bullet vs "Simple" elsewhere (Sec. 1); Fig. 2 shows the length reward on incorrect responses while Eq. 10 removes it (clarify which is trained).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Control missing. |
| Clarity | 3 | Clear. |
| Significance | 2 | Moderate. |
| Originality | 2 | Incremental. |

## Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, readable paper with decent numbers sits above the median, but the missing control and untested mechanism are weaknesses that typical rejected submissions share; I put it at the top of the rejected band rather than at borderline.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound reward; unverified attribution. |
| Clarity & Presentation | 64 | Competent | Clear with small inconsistencies. |
| Novelty & Originality | 54 | Developing | Incremental. |
| Significance & Impact | 60 | Competent | Relevant. |
| Experimental Validation | 52 | Developing | One baseline family. |
| Reproducibility | 62 | Competent | Table 3. |
| Ethical Compliance | 64 | Competent | Limitations noted. |

## Questions for Authors
1. What does the DAPO control with no length reward achieve, in accuracy and length? A result near DeepMath-Zero would raise my score.
2. Could you add the fixed-β variants to Table 1?
3. How was the GPT-4o behaviour tagger validated?

## Limitations Assessment
**Partially.** Sec. 6 is honest but short.

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): A readable paper with a reasonable idea; one control and some claim-softening would move it to the other side.

## Confidence
**4**: Read in full; did not check the RL internals.

---

# Devil's Advocate Report

## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Reviewer: Prof. Gideon Altamirano-Sze (statistics and evaluation methodology group, research university, North America; fictional persona)

---

## Steelman
Existing length-penalty methods compress reasoning uniformly and lose accuracy on hard problems. A reward that penalizes length only where the model is already reliable, and rewards it where it is not, should keep the exploratory capacity that hard problems need. The paper shows that this recipe gives higher average accuracy and much shorter responses than a strong Zero-RL model across seven benchmarks, with training curves consistent with an initial exploration phase followed by compression.

---

## Core Argument Chain
1. Longer responses have higher pass@32 even though pass@1 falls with length (Sec. 3.2, Fig. 1).
2. Hence always shortening responses restricts the reasoning boundary (Sec. 1, Sec. 3.2).
3. A length reward that is signed by relative difficulty (P_g − P_b) shortens easy and lengthens hard responses (Sec. 4.2–4.3).
4. This reward, applied to correct responses only and with an EMA-smoothed P_b (Sec. 4.4), trains Qwen2.5 bases that beat DeepMath-Zero in accuracy and length (Table 1, Fig. 3).
5. The improvement is due to the dual reward through higher entropy and more effective reflection (Sec. 5.3–5.4).
∴ Dynamically exploring and compressing reasoning chains improves both accuracy and efficiency.

---

## Strongest Counter-Argument
Even if every number in Table 1 is right, the paper does not show that the *dual, difficulty-aware* mechanism is what produced them. A simpler account fits the evidence better. DeepCompress is a fresh Zero-RL run with a 10K response cap, a 2K overlong buffer, 500 steps and a modified chat template (Sec. 5.1, Table 3), while its main comparator is a released checkpoint with unknown cap and schedule. Both the cap and DAPO's overlong shaping push toward shorter outputs; the paper's own Fig. 1 narrative says pass@1 *falls* with length, so any procedure that removes rambling raises pass@1, especially for a 3B baseline whose Table 2 hard-set responses average 11,222 tokens under a 32,768 limit. On top of this, the "Hard" side of the mechanism is not shown to operate. By Eq. 10 the length bonus applies only to correct responses, so for questions with no correct sample it does nothing, and the paper's own Table 2 shows that responses to *hard* questions also shrink by 57% (3B) and 17% (7B) relative to the baseline, not grow. The training-time "initial lengthening" in Fig. 4b may then come from the EMA initialized at 1.0 with λ = 0.99 (Eq. 11), where P_{b,t} ≥ 0.99^t is high for the first ~100 steps and almost every question is labelled "Hard": a length-bonus-then-penalty schedule, not difficulty-awareness. The motivating claim about pass@k and the reasoning boundary is never tested on the trained models. Finally, the efficiency claim is made against models never trained to be short, while the methods the paper says trade accuracy for brevity are absent from every table. The authors need a same-recipe control, a schedule-only control, pass@k of the trained models, and at least one length-RL baseline before the causal story and the "new SOTA, better and shorter" headline can be accepted.

---

## Issue List

### CRITICAL Issues
**No CRITICAL issues found.** The headline numbers are internally consistent, no tuning or selection on the reported test benchmarks is stated (checkpoints are chosen on a separate 120-question validation set, Sec. 5.1), and the confounds above are fixable by additional controls and narrower claims.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / Alternative explanation | Table 1, Sec. 5.1, Table 3, Sec. 6 | Unmatched recipe (10K cap, overlong buffer, 500 steps, template change) vs. released baselines; no same-recipe no-length-reward control. Evidence supports "DeepCompress recipe > DeepMath-Zero", not "dual reward > no length reward". Narrowing-the-claim case. | DAPO control, same cap/steps/template; report baseline's cap/steps |
| DA-M2 | Logic | Sec. 4.2, Eq. 10, Table 2, Fig. 4 | Mechanism untested: no pass@k for trained models; hard-question responses also shrink (Table 2); bonus applies only to correct responses so P_g = 0 groups get none; no length-by-difficulty analysis. | pass@k up to 64; length by difficulty bucket; fraction of groups with P_g = 0 |
| DA-M3 | Alternative explanation | Eq. 11, Table 3, Sec. 5.3 | EMA init 1.0 with λ = 0.99 yields a long "Hard-everywhere" phase (P_{b,t} ≥ 0.99^t: ≥ 0.61 at step 50, ≥ 0.37 at step 100); no ablation of Eq. 10, Eq. 11, α, λ or of reversed/shuffled difficulty. | Schedule-only and shuffled-difficulty controls; ablate Eq. 10, 11 |
| DA-M4 | Scope / Cherry-picking | Table 1, Sec. 2, Sec. 5.2 | Efficiency claim has no efficiency baseline; the methods said to lose accuracy are not run. β = ±1 variants only appear as plots. | Add at least one length-RL baseline and a tabulated β ablation |
| DA-M5 | Overclaim (E5) | Sec. 5.2, Sec. 5.3, Sec. 1, Sec. 5.4 | "across all seven" (MATH-500 7B is a tie, 85.6 vs 85.6); "simultaneous optimality" while the text says the length-bonus variant is higher in accuracy and the penalty variant shorter; "encouraging high policy entropy" while the bonus variant has higher entropy; "reflects more often" with +0.05 at 7B. Each survives in weaker form. | Rewrite claims to match |
| DA-M6 | Measurement validity | Sec. 5.4, Table 2, App. A | Reflection counts from an unvalidated GPT-4o tagger with a prompt that asks it to "actively identify and emphasize" behaviours; the hard set is defined by base-model failure; one of four behaviours reported. | Human-validate tagger on a sample; report all behaviours; neutral prompt |
| DA-M7 | Noise | Sec. 5.1, Table 1 | Single training run; AIME sets have 30 problems (+4.1 avg@16 ≈ 1.2 problems; +6.5 ≈ 2 problems, derived); checkpoint chosen on 120 questions; baseline checkpoints chosen by others. | Seeds or CIs; state baseline selection |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Clarity | Sec. 1 vs Sec. 4.1 | GRPO vs DAPO as the base algorithm; role of dynamic sampling in computing P_b unspecified. |
| DA-m2 | Clarity | Fig. 2, Eq. 9 vs Eq. 10 | Figure shows length reward on incorrect responses; text says it is removed. |
| DA-m3 | Protocol | Sec. 5.1 | Whether the 60 "MATH" validation questions are disjoint from MATH-500 is unstated. |
| DA-m4 | Clarity | Sec. 3.1 | "8,192 responses for a given problem" implies ~4.1M generations per model on MATH-500; confirm. |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Avg acc 3B DeepCompress (Table 1) | 36.6 | 256.3/7 = 36.6 | Yes |
| Avg acc 3B DeepMath-Zero | 34.6 | 242.1/7 = 34.6 | Yes |
| Avg acc 7B DeepCompress | 48.7 | 341.2/7 = 48.7 | Yes |
| Avg acc 7B DeepMath-Zero | 46.0 | 322.1/7 = 46.0 | Yes |
| AIME24 / AIME25 gains at 7B | +4.1 / +6.5 | 23.5−19.4 = 4.1; 19.6−13.1 = 6.5 | Yes |
| AIME24 gain at 3B | +5.2 | 16.7−11.5 = 5.2 | Yes |
| Hard-question length reduction (Table 2), 3B / 7B | text: 57.9% / 16.6% (all benchmarks) | (11,222−4,853)/11,222 = 56.8%; (7,180−5,942)/7,180 = 17.2% | Consistent (different sets; Fig. 3 unreadable) |
| "across all seven benchmarks" | all seven better | MATH-500, 7B: 85.6 vs 85.6 | No (tie) |

## Ignored Alternative Explanations
- Training cap and DAPO overlong shaping, rather than difficulty-aware shaping, shortening outputs (DA-M1).
- EMA initialization producing a lengthen-then-shorten schedule (DA-M3).
- Removal of rambling and truncated outputs raising pass@1, independent of exploration.
- Extra gains from checkpoint selection on a validation set that baselines did not receive.
- Changed chat template (Sec. 5.1) affecting both accuracy and length.
- More rollouts on hard prompts (curriculum/oversampling) giving similar gains.

## Missing Stakeholder Perspectives
Practitioners serving long-tail hard queries (shorter chains on hard problems may reduce answers' inspectability and accuracy off the benchmarks), and users of non-math domains where difficulty from pass rate is unavailable or noisy.

## Observations (Non-Defects)
The method is simple and fully specified; averages in Table 1 are arithmetically right; baselines were re-run under a single decoding protocol; the paper discloses its 10K cap and its dependence on within-group length variation; the quantity P_g − P_b is a neat, label-free self-calibrating difficulty signal.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Mechanism untested; ablations missing. |
| Clarity & Presentation | 60 | Clear; several internal inconsistencies. |
| Novelty & Originality | 50 | Narrow delta. |
| Significance & Impact | 54 | Modest if confounds persist. |
| Experimental Validation | 42 | No matched control or efficiency baseline; single run. |
| Reproducibility | 58 | Hyperparameters present; baselines' settings unknown. |
| Ethical Compliance | 60 | Nothing at stake. |

**Pool position:** better than about 44% of submissions to ICLR. Deciding evidence: unmatched comparison and untested mechanism (DA-M1, DA-M2).

## Overall: 3 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Weaknesses were tested for Specific / Not already answered / Consistent with the paper / Actionable. Reports above are shown as drafted; the EIC reads the post-check versions described here. Scores unchanged.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W6 (Fig. 1 estimator) | rewritten as a question | Figure unavailable; cannot be asserted as an error (Hard Rule 10) |
| R1 | Error-log ERR-4 (Sec. 5.3 "optimality") | kept, confidence Medium | Quote and cross-reference exist; relies on text, not figure |
| R2 | W3 (Liu et al. characterization) | rewritten as a question | Only the abstract was seen; low confidence |
| R2 | W1 (difficulty-adaptive methods exist) | rewritten | Recent preprints (ALP, Su & Cardie, AdaCtrl) are "worth discussing" only; the weakness rests on the peer-reviewed GRPO-LEAD and on the paper's own Sec. 2 sentences |
| R3 | W4 (broader impact) | moved to Minor | Cosmetic for a math-only benchmark paper |
| R3 | W2(b) magnitude point | kept | Derived from Eqs. 4–5 and Table 3 α; shown to be arithmetic |
| R4 | "Easy"/"Simple" naming, typos, Fig. 2 vs Eq. 10 | moved to one Minor line | Cosmetic |
| DA | M6 (hard set defined by base-model failure) | kept, shortened | Paper states definition in Sec. 5.4 |
| All | "No code release" | dropped | Link footnotes removed in the blinded text; unverifiable |

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer Part A: Package

**Master issue list (deduplicated):**

| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Unmatched recipe / no same-recipe no-length-reward control (10K cap, steps, template) | R1-W1, R4-W1, DA-M1 | CONSENSUS-3 |
| I2 | Mechanism (adaptive allocation, pass@k on hard problems) not measured | R1-W3, R3-W2, R2-W2, DA-M2 | CONSENSUS-4 |
| I3 | No ablation of Eq. 10 / Eq. 11 / α / λ; EMA init schedule | R1-W2, R3-W2, DA-M3 | CONSENSUS-3 |
| I4 | No efficiency baseline; β = ±1 only plotted | R1-W4, R2-W1, R4-W3, DA-M4 | CONSENSUS-4 |
| I5 | Overclaiming (all seven, optimality, entropy, reflection) | R1 ERR-2/4, R4-W2, DA-M5 | CONSENSUS-3 |
| I6 | Single run; noisy small test sets; noisy checkpoint selection | R1-W5, DA-M7 | CONSENSUS-2 |
| I7 | Novelty delta narrow vs difficulty-adaptive length rewards | R2-W1, R4-W3 | CONSENSUS-2 |
| I8 | Reflection analysis validity (GPT-4o tagger) | R4-W2, DA-M6 | CONSENSUS-2 |
| I9 | Deployment: tokens as cost proxy, truncation, latency | R3-W1 | SOLO |
| I10 | Scope: math-only, Qwen-only | R3-W3, R2-W4 | CONSENSUS-2 |
| I11 | Positive-leaning dissent: R3 rates Overall 4, views evidence as adequate for a timely idea | R3 vs R1/R2/R4/DA | SPLIT |

**DA-CRITICAL issues:** none raised. **SPLIT:** I11. **Hinge:** I1, I2, I3.
**Integrity signals:** none (scan clean; no text overlap flagged by `similarity`; closest prior work GRPO-LEAD cosine 0.144, 0 shared 8-grams).
**Official output (pre-EIC, from `scores_before.json`):** official mean rating 3.20, official composite 56.3, starting point 3. No warnings.

## EIC Meta-Review (Prof. Ottoline Reyes-Baptiste)

### The Case For and Against
- **For acceptance:** A simple, label-free, adoptable reward with a fresh sign choice (length bonus for relatively hard questions), clear writing, correct headline arithmetic, a consistent accuracy gain plus shorter outputs on seven benchmarks, and the largest gains on AIME at 7B. Weaknesses are those many accepted ICLR papers share (single run, one baseline family).
- **Against acceptance:** The comparison is not recipe-matched, so the attribution to the dual reward is unproven; the claimed mechanism (hard-side exploration) is never measured and the paper's own Table 2 shows hard responses shrinking; the efficiency claim has no efficiency baseline; the novelty delta over difficulty-adaptive length rewards is narrow and undifferentiated.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| 10K cap, overlong buffer, 500 steps for DeepCompress; baseline's cap/steps not stated | R1-W1, DA-M1 | Table 3, Sec. 6, Sec. 5.1 | **Verified** | Searched the text: baseline training settings appear nowhere. Whether the cap explains the shortening is an open question, not a verified fact |
| No no-length-reward control and no efficiency baseline in Table 1 | R1-W1/W4, DA-M4 | Table 1 | **Verified** | Rows: Qwen bases, SimpleRL-Zoo-style, Open-Reasoner-Zero, DeepMath-Zero only |
| No pass@k of trained models | R1-W3, DA-M2 | Sec. 5, Table 1 | **Verified** | Only pass@1 reported |
| Hard-question responses shorter than baseline | R1-W3, DA-M2 | Table 2 (11,222→4,853; 7,180→5,942) | **Verified** | Hard set is defined by base-model failure, so it is not identical to "hard for the trained model" |
| Length bonus applies only to correct responses (P_g = 0 gets none) | R1-W3, DA-M2 | Eq. 10 | **Verified** | Which reward form (Eq. 9 vs 10) produced Table 1 is not stated; Fig. 2 depicts the Eq. 9 form |
| EMA init 1.0, λ = 0.99 ⇒ P_{b,t} ≥ 0.99^t, "Hard-everywhere" early phase | R1-W2, R3-W2, DA-M3 | Eq. 11, Table 3 | **Verified (derived)** | Arithmetic holds; that it *explains* Fig. 4b is a hypothesis (figure unavailable) |
| Length-reward magnitude small (≈0.04 between z = ±2 at β = 0.2, α = 0.2) | R3-W2 | Eqs. 4–5, Table 3 | **Verified (derived)** | β distribution unreported |
| "across all seven benchmarks" false at 7B MATH-500 (tie) | R1 ERR-2, DA-M5 | Table 1, Sec. 5.2 | **Verified** | Minor overclaim |
| GRPO vs DAPO inconsistency | R1 ERR-1, DA-m1 | Sec. 1, 4.1, 5.1 | **Verified** | Minor, but dynamic-sampling interaction matters |
| Length-bonus variant has higher accuracy than DeepCompress (Fig. 4c) | R1 ERR-4, DA-M5 | Sec. 5.3 text | **Partly correct** | The sentence says "higher performance compared to other methods"; I cannot see Fig. 4, so which methods are included is unclear; Table 2 hard-set pass@1 favours DeepCompress (13.81 vs 11.89) |
| Reflection +0.05 at 7B called "more often" | R4-W2, DA-M6 | Table 2, Sec. 5.4 | **Verified** | 2.64 vs 2.59 |
| Pass@k-bin estimator concern | R1-W6 | Eq. 1, Sec. 3.1 | **Not decidable** | Needs per-bin n; treated as a question |
| ALP/Su & Cardie as "same mechanism" | R2-W1 | Literature check | **Overstated if used as a weakness** | Recent preprints (June / May 2025): worth discussing only. GRPO-LEAD (peer-reviewed, level 3) gives partial overlap: Novelty weakness MAJOR at most |
| Liu et al. (2025) mislabelled | R2-W3 | Sec. 2 | **Not decidable** | Only the abstract was seen; kept as question |
| Table 1 arithmetic | R1-S3, DA | Table 1 | **Verified** | All averages and deltas recomputed |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points (W1, W3, W5, ERR-1/2/3) verified; one point (ERR-4) depends on text only; calibrated to the venue |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; the strongest "same mechanism" argument rests on recent preprints, but R2 correctly labelled them worth discussing |
| R3 (Perspective) | 4 | 3 | 1.0 | Verified derivations (EMA, magnitude); lenient pool position of 66 given the evidence, but role-appropriate |
| R4 (Generalist) | 3 | 4 | 1.0 | Typical, calibrated; points verified |
| DA | 3 | 4 | 1.25 | Counter-argument survived my check (Eq. 10, Table 2, Eq. 11); no CRITICAL inflation; correct restraint |

### DA-CRITICAL Rulings
The Devil's Advocate raised no CRITICAL issue. I checked criterion 3: the checkpoint is selected on a separate validation set (60 MATH + 60 AIME 2022–2023, Sec. 5.1); the reported test benchmarks are not used for selection. Whether the 60 MATH questions overlap MATH-500 is unstated; this is a question (DA-m3), not leakage evidence. The upheld count is 0 and there is no ceiling.

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
Official ratings are 3, 3, 4, 3, 3 (mean 3.20); the EIC-weighted rating is 3.15, so the starting point is **3 (Borderline Reject)**. The composite cross-check (EIC-weighted 55.7) falls in the same band (3), so there is no disagreement to arbitrate. I do not depart from the starting point. My own pool position is **48**: the idea is clear and timely and the paper is well written, which puts it above clearly weak submissions, but the three issues that hinge the outcome (I1 recipe mismatch, I2 mechanism not measured, I3 no ablation of the added components) are all of the kind that typical rejected submissions share, and the efficiency half of the headline claim (I4) has no efficiency baseline. The reviewers' pool positions range from 42 to 66; the 24-point gap comes from R3's more generous reading of evidence, which my verification does not support (Table 2 and Eq. 10 point the other way on the mechanism). I do not count the literature-check items on recent preprints against the paper. All outstanding problems can be fixed with additional runs (a same-recipe control, schedule-only and shuffled-difficulty controls, pass@k, one length-RL baseline), which is why the paper is a plausible accept after revision, but as submitted the evidence does not support the claim that the dual difficulty-aware reward is responsible. No DA ceiling applies. **Final (EIC): 3.** On the ICLR scale this corresponds to a rating of 4 on {0, 2, 4, 6, 8, 10} (5 on the older {1, 3, 5, 6, 8, 10}), scale status secondary.

---

## Score Summary

### Official Scores and EIC Assessment

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 19% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 19% |
| DA | 4 | 0.85 | 1.25 | 24% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 54 | 60 | 56 | 48 | 53.6 | 53.0 | 12 |
| Clarity & Presentation | 62 | 64 | 70 | 64 | 60 | 64.0 | 63.5 | 10 |
| Novelty & Originality | 52 | 50 | 62 | 54 | 50 | 53.6 | 53.1 | 12 |
| Significance & Impact | 56 | 58 | 68 | 60 | 54 | 59.2 | 58.5 | 14 |
| Experimental Validation | 44 | 50 | 58 | 52 | 42 | 49.2 | 48.3 | 16 |
| Reproducibility | 60 | 62 | 66 | 62 | 58 | 61.6 | 61.2 | 8 |
| Ethical Compliance | 62 | 62 | 66 | 64 | 60 | 62.8 | 62.5 | 6 |
| **Composite** | 53.4 | 55.8 | 63.3 | 57.7 | 51.4 | **56.3 (before)** | **55.7 (after)** | |
| Pool position (P%) | 42 | 48 | 66 | 54 | 44 | | | |

**Official reviewer ratings (Overall 1–6):** R1 3, R2 3, R3 4, R4 3, DA 3 → official mean **3.20**. **EIC-weighted rating:** **3.15** → starting point **3 (Borderline Reject)**. No spread above 20 points. **Composite cross-check:** official 56.3 → band 3; EIC-weighted 55.7 → band 3. **Decision ceiling:** none.

### Target-Venue Scores (ICLR 2026, scale status: secondary; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); skill Overall 3 (Borderline Reject) |

---

## Editorial Decision

# Editorial Decision
## Paper: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains
## Submission ID: iclr26-K5A2jBmEBK | Date: 2026-11-10
## Target Venue: ICLR | Paper Type: Empirical
## Review Team (fictional personas): EIC Prof. Reyes-Baptiste; R1 Halvorsen-Adeyemi (Methodology), R2 Takeda-Marsh (Domain), R3 Ibarrondo-Nkemelu (Perspective), R4 Vendramin (Generalist), DA Altamirano-Sze

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean 3.20 · official composite 56.3
**EIC assessment** (internal): weighted rating 3.15 → starting point 3 · weighted composite 55.7 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3

### Editorial Decision Letter

Dear Authors,

Thank you for submitting "DeepCompress" to ICLR. The topic, reasoning efficiency without losing accuracy, is timely and important.

**Overall Assessment:** The panel found a clear, simple and practical idea: a label-free, online difficulty signal that flips the sign of a length reward. The paper is well written and the headline arithmetic is correct. The panel's concern is attribution: the evidence does not yet show that the dual difficulty-aware reward, rather than the training recipe, produces the reported accuracy and length changes.

**Key Strengths Identified by Reviewers:**
1. Simple, fully specified, easily adopted reward (R1, R3, R4).
2. Consistent gains with shorter outputs on seven benchmarks, largest on AIME at 7B, with baselines re-evaluated under one protocol (R1, R4).
3. A thoughtful framing of length as a resource allocated by difficulty (R2, R3).

**Key Concerns Requiring Attention:**
1. No same-recipe control without the length reward; the 10K cap, overlong buffer, step count and chat template differ from or are unspecified for the baselines (CONSENSUS-3).
2. The mechanism, extra exploration on hard problems, is not measured: no pass@k for trained models, hard-question responses also shrink (Table 2), and the bonus applies only to correct responses (CONSENSUS-4).
3. No ablation of the correctness conditioning, EMA smoothing, α, λ, or of the direction of the signal; the EMA initialization may itself produce the early lengthening (CONSENSUS-3).
4. The efficiency claim has no efficiency baseline (CONSENSUS-4); novelty versus difficulty-adaptive length rewards is not differentiated (CONSENSUS-2).

No Devil's Advocate CRITICAL issue was raised.

**Decision: Borderline Reject (3).** The core idea is sound and the issues are fixable with additional experiments and narrower wording. With a same-recipe control, schedule-only and shuffled-difficulty controls, pass@k for the trained models, and at least one length-RL baseline, the decision could move to the accept side. This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome.

Sincerely,
Prof. Ottoline Reyes-Baptiste
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Mechanism not measured (I2) | R1, R2, R3, DA | CONSENSUS-4 |
| No efficiency baseline (I4) | R1, R2, R4, DA | CONSENSUS-4 |
| Unmatched recipe / control missing (I1) | R1, R4, DA | CONSENSUS-3 |
| No component ablations / EMA schedule (I3) | R1, R3, DA | CONSENSUS-3 |
| Overclaiming (I5) | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the evidence adequate for a timely, practical idea (Overall 4 vs 3)? | R3 | R1, R2, R4, DA | R3's derived points (EMA, reward magnitude) were verified and argue *against* its own score; adopting the majority view with weights 1.25 on R1 and DA |

### Score Spread Discussion
No dimension is flagged (all spreads ≤ 16). The widest, Experimental Validation (42–58), reflects R3's more lenient reading; the EIC adopts the lower view because of I1 and I4.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Unmatched recipe, no control | Yes: R1, R4 | n/a | n/a |
| DA-M2 | MAJOR | Mechanism untested | Yes: R1, R2, R3 | n/a | n/a |
| DA-M3 | MAJOR | EMA schedule, no ablations | Yes: R1, R3 | n/a | n/a |
| DA-M4 | MAJOR | No efficiency baseline | Yes: R1, R2, R4 | n/a | n/a |
| DA-M5 | MAJOR | Overclaiming | Yes: R1, R4 | n/a | n/a |
| DA-M6 | MAJOR | Reflection analysis validity | Yes: R4 | n/a | n/a |
| DA-M7 | MAJOR | Noise, single run | Yes: R1 | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (must fix)
*No upheld DA-CRITICAL issues. These are the issues the EIC verified as undermining the main attribution claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | No same-recipe no-length-reward control; unmatched cap/steps/template | R1-W1, R4-W1, DA-M1 | Table 1, Table 3, Sec. 5.1, Sec. 6 | Train DAPO with identical data, 10K cap, 500 steps, template; report baseline's cap/steps; add to Table 1 and Fig. 3 | High; 1 run per size (3B, 7B) at main-run cost | Partly (one 3B run) |
| P1-2 | Mechanism unmeasured | R1-W3, R2-W2, R3-W2, DA-M2 | Secs. 4.2, 5, Table 2 | pass@k (to 64) for DeepMath-Zero, control and DeepCompress; length by difficulty bucket; fraction of P_g = 0 groups | Medium; inference only (≈ same as Table 1 evaluation × larger k) | Yes |
| P1-3 | No ablation of Eq. 10, Eq. 11, α, λ; EMA-schedule explanation | R1-W2, R3-W2, DA-M3 | Secs. 4.3, 4.4, 5.3 | Ablate each; add schedule-only and shuffled/reversed-difficulty controls; plot β distribution and Simple/Hard share | High; ≥4 additional 7B runs (or shorter proxy runs) | Partly |
| P1-4 | Efficiency claim lacks an efficiency baseline | R1-W4, R2-W1, R4-W3, DA-M4 | Table 1, Sec. 2, Sec. 5.2 | Add a plain length penalty and one adaptive-penalty method in the same recipe; tabulate β = ±1 variants on all seven benchmarks with length | High; 2–3 additional runs | Partly |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Overclaiming wording ("all seven", "optimality", "high entropy", "reflects more often", "new SOTA") | R1 ERR-2/4, R4-W2, R2-W4, DA-M5 | Rewrite to match tables | Low | Yes |
| S2 | Single run, small test sets, noisy selection | R1-W5, DA-M7 | ≥3 seeds at 7B or bootstrap CIs; state baseline checkpoint selection | High (seeds) / Low (CIs) | Partly |
| S3 | Differentiate from difficulty-adaptive length rewards (GRPO-LEAD; Cheng et al.; Yu et al.; discuss ALP, Su & Cardie, AdaCtrl as recent work) | R2-W1, R4-W3 | Add positioning paragraph and comparison | Low–Medium | Yes |
| S4 | Reflection analysis validity | R4-W2, DA-M6 | Human-validate tagger; neutral prompt; report all four behaviours | Low–Medium | Yes |
| S5 | Cite and discuss Liu et al. ("Understanding R1-Zero-Like Training"), Yue et al. (pass@k boundary) | R2 Missing References | Add to related work | Low | Yes |
| S6 | Clarify RL algorithm (GRPO vs DAPO), dynamic-sampling interaction with P_b, Eq. 9 vs Eq. 10 in the trained model, validation split disjointness | R1 ERR-1, DA-m1/m2/m3 | State explicitly | Low | Yes |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Truncation rate and latency/throughput | R3-W1 | Report max-length hit rate and one latency number |
| N2 | Scope: math-only, Qwen-only | R3-W3 | Add a second family or task, or narrow wording |
| N3 | More rollouts on hard prompts as an alternative to length reward | R3 | Comparison would clarify where the benefit lies |
| N4 | Typos; Easy/Simple naming; two sentences on broader trade-offs | R4, R3-W4 | Edit |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 2–3 weeks of compute and analysis (several full-recipe runs per model size)
- Priority 2: 6 items, about 1 week (mostly writing; seeds optional)
- Priority 3: 4 items
- **Total estimated revision time**: about 3–4 weeks

*Post-Review Analysis (Gap Scout): not requested; not run.*
