# Academic Paper Review: "Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling"

Mode: full · Target venue: ICLR (user-stated) · Literature check: strict, cutoff 2025-09-24 · Date: 2026-11-10
Reviewers are fictional personas. The five passes were run one after another in a single model context, so they are perspectives from a shared context, not independent agents. The outcome is a simulation of how a careful panel might see this draft, not a prediction.

Runtime notes (disclosed): figures are not available (text extraction only), so every figure-dependent statement rests on captions and prose. Appendix C appears in the extracted text as a bare heading with no content, so anything it was meant to hold is unverified. `integrity_scan.py` was not run because the evaluation restricted the tools to file reads and the aggregation script. Instead the full text was read for reviewer-directed text and none was found.

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling |
| Primary Discipline | ML theory → inference-time scaling / test-time selection for LLMs |
| Secondary Discipline(s) | Offline RL (pessimism, single-policy coverage), reward-model-guided decoding, learning theory (minimax lower bounds) |
| Paper Type | Theoretical (composite weights: theoretical): theorems and matching bounds, plus a small empirical section |
| Core Technique(s) | Best-of-N, (weighted) majority voting, frequency-thresholded reranking (BoM), L1 coverage coefficient C*, averaging-hammer lower bounds, Chernoff and union bounds |
| Target Venue | ICLR (stated); profile key `iclr` |
| Venue-Specific Notes | None (no contribution-type declaration). ICLR form: Soundness / Presentation / Contribution, Rating, Confidence. |
| Paper Maturity | Submission-ready (complete theory); the empirical section is thin and Appendix C is empty in the extraction |
| Ethics-Relevant Content | None (no human subjects, data collection, or misuse surface beyond standard LLM inference) |

### Claimed Contributions (as stated by the authors; Section 1, contribution list)
- **C1** (problem/result): a minimax lower bound Ω(ε_opt + √(C*ε²_RM/k)) for any Pass@k inference strategy (Section 1; Theorem 6.1).
- **C2** (method/result): BoM, with regret O(ε_opt + √(C*ε²_RM/k)) at sample budget N = Θ̃(C*), matching the lower bound, hence "minimax optimal" (Theorem 5.1; Table 1).
- **C3** (result): (weighted) majority voting and BoN are not scaling-monotonic, while BoM is (Theorems 4.1, 4.2; Corollary 5.2).
- **C4** (empirical): BoM beats majority voting and BoN on GSM8K, MATH-500 and AIME24 with two Qwen models and one reward model; the experiments "verify the scaling monotonic properties" (Section 7).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Single prompt x; reference policy π_ref; true reward r*∈[0,1]; imperfect reward r̂. Assumption 3.1 is an L2 error bound under π_ref. Assumption 3.2 gives a unique y* with r*(y*)=1 and |r*−r̂|(y*)=ε_opt. C*(x)=1/π_ref(y*|x) (Eq. 3.2–3.3). Regret is Eq. 3.1. Scaling-monotonicity is Definition 3.4.
- **Experiments (Section 7).** Models: Qwen3-4B-Instruct-2507 and Qwen2.5-Math-1.5B-Instruct as π_ref; reward model AceMath-7B-RM. Data: GSM8K, MATH-500, AIME24. N=2000 for GSM8K/Qwen3-4B, otherwise N=500. k∈{1,2,3,5,10}. Fig. 3 varies N from 100 to 2000 on AIME24/Qwen3-4B at k=1,3,5, with α=0.005 except α=0.015 at N=100. Group reward = mean of trajectory rewards within an answer group. Splits, seeds, variance, compute, α-selection protocol and code: **not stated** after search (terms searched: test set, validation, held-out, select, tune, hyperparameter, seed, split, checkpoint).
- **Headline claims.** The "the first minimax-optimal Pass@k inference strategy" (Table 1 caption); "its performance does not degrade when increasing N" (abstract); "BoM outperforming both majority voting and BoN" (abstract).
- **Appendix.** A: proof of Theorem 5.1 (Lemma A.1, Eq. A.1–A.10). B: lower bounds (B.1 Lemma B.1; B.2 Thm 4.1; B.3 Thm 4.2; B.4 Thm 6.1/B.2). C: heading only, no content in the extraction.
- **Unverifiable.** Figures 1–3 (curves not readable from text). Several equations are garbled by extraction (exact exponents in A.1, A.6 and B.1 are readable but fragile).

### Integrity signals
No reviewer-directed or hidden text found in a full read of the extracted text. Literature-check similarity (cosine 0.255; 4 shared 8-grams) with Wu et al. 2024b flags only the paper's own sentence describing that work's strategy list (Section 2). That is a cited description, not an integrity concern.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valdsen, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / statistical learning theory, bandits and offline RL, area chair at ML venues
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Counts what is proved versus what is claimed; accepts clean theory with honest scope, distrusts headline wording

### Reviewer 1 (Methodology): Dr. Oyelaran Veckstrom, industrial research lab (Western Europe)
- **Seniority / Expertise**: Senior industry scientist / concentration inequalities and lower-bound constructions; LLM evaluation protocols (pass@k, reward-model-guided selection)
- **Review Focus**: Proof correctness, assumptions, experimental design, reproducibility
- **Style**: Rechecks constants and conditions line by line; wants every regime stated

### Reviewer 2 (Domain): Prof. Mirela Tsankov-Rey, public university theory group (Eastern Europe)
- **Seniority / Expertise**: Senior faculty / inference-time alignment theory; pessimism and single-policy coverage in offline RL
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Compares every claimed novelty with the closest prior abstract

### Reviewer 3 (Perspective): Dr. Haruto Delacroix-Nwosu, applied-statistics and decision-theory group (East Asia / West Africa collaboration)
- **Seniority / Expertise**: Mid-career / ranking and selection, best-arm identification, code-generation pipelines with unit-test verifiers
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions
- **Style**: Constructive, expansive; names bridges to other fields

### Reviewer 4 (Generalist): Dr. Selin Karahanova, ML group at a research university (Middle East)
- **Seniority / Expertise**: Mid-career / LLM reasoning and RL post-training (not theory)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads like a typical PC member; asks whether a non-theorist can use the result

### Devil's Advocate: Dr. Matteo Ibarra-Quill, evaluation-methodology group (South America)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, overclaiming in scaling-law papers
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Fair but exact about what a theorem does and does not say

*Personas are fictional. Proceeding with the stated assumptions.*

## Literature check (Phase 1.5, strict, cutoff 2025-09-24)
Run after the five reports were drafted. Mode: strict. Queries by purpose: claim ×4 (C1 ×2, C2, C3), expansion ×1; one query returned no parseable output (rate limit) and was not retried. Gaps left open: the benchmark/baseline scout was not run (GSM8K, MATH-500 and AIME24 serve as testbeds, not leaderboard comparisons) and `novelty` was not run, so the per-claim verdicts below are hand-assigned from kept abstracts only. Similarity: closest prior works are Wu et al. 2024b (arXiv 2408.00724, prior arXiv-only; cosine 0.255), Brown et al. 2024 (arXiv 2407.21787; 0.185), Stroebl et al. 2024 (arXiv 2411.17501; 0.144). All three are cited by the paper. Huang et al. 2025 (arXiv 2503.21878) is labelled **recent preprint** relative to the cutoff (March 2025, under six months): worth discussing, not a required comparison, and the paper already cites and builds on it.

---

# Phase 1: Reviewer Reports

---

# Peer Review Report

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Reviewer: Dr. Oyelaran Veckstrom, Reviewer 1 (Methodology) (industrial research lab, Western Europe; fictional persona)
## Expertise: lower-bound constructions and concentration inequalities; evaluation protocols for reward-model-guided selection
## Date: 2026-11-10

## Summary
The paper formalizes "Pass@k inference": draw N samples from a reference policy, then submit k of them. Regret is measured against the unique optimal response under an imperfect reward model. For fixed prompt x it proves lower bounds for majority voting (Thm 4.1) and Best-of-N (Thm 4.2). It proposes BoM, which keeps responses whose empirical frequency is at least α and then takes the top-k by reward, and proves an upper bound O(ε_opt + √(C*ε²_RM/k)) (Thm 5.1). A general lower bound (Thm 6.1) matches it. Section 7 runs three methods on three math datasets with two Qwen models and one reward model.

## Strengths
### S1: A clean, self-contained formal setting with matching bounds (Sections 3, 5, 6)
Assumptions 3.1–3.2 are stated explicitly, the quantities (C*, ε_RM, ε_opt) are interpretable, and the upper and lower bounds have the same functional form. The k-dependence is the part that is new relative to the k=1 sample-and-evaluate framework (Remark 3.3).

### S2: The main upper-bound proof is correct in structure (Appendix A, Eq. A.8–A.10)
I rechecked the chain. For every submitted ỹ_i, r*(y*)−r*(ỹ_i) ≤ ε_opt + Δ_i once y* is not submitted but is in Ŷ_α. The minimum of the Δ_i is at most the root of their average. π_ref(ỹ_i) ≥ 1/(4C*) under event E lets Σπ_refΔ² be bounded by ε²_RM. The N threshold N ≥ 16C* log(kC*/ε²_RM) is consistent with the final union bound: 5C*e^{−N/(32C*)} ≤ 5√(C*ε²_RM/k).

### S3: The "bins" argument for the unknown-cardinality tail (Lemma A.1, Eq. A.3–A.7)
Partitioning Y∖Y_{1/(4C*)} into ≤4C* groups of π_ref-mass ≤1/(2C*) is a correct way to avoid a union bound over an unknown number of responses. The main upper-bound argument is correct up to constants.

### S4: Averaging-hammer lower bounds are properly constructed (Lemma B.1, Theorem B.2)
In Theorem B.2, ε²_RM = (M−1)δ²/C and the regret ≥ ((M−k)/M)·δ check out. The negative-association argument in Theorem 4.2 (Eq. B.2–B.4) is sound.

## Weaknesses
### W1: The guarantee is for an algorithm that needs the unknown C*, and the experiments tune α without a stated protocol (Theorem 5.1; Section 7.1–7.2)
Theorem 5.1 sets "the threshold is α = 3/(4C ∗ (x))". C*(x)=1/π_ref(y*|x) depends on the unknown correct answer, and varies per prompt. Section 7.1 says only "we set a threshold α", and Section 7.2 reports "we use α = 0.005 in all other settings" with 0.015 at N=100. No value is given for the k-sweeps in Figures 1–2. There is no validation split, no sensitivity sweep, and no statement of how α was chosen. A single global α cannot equal 3/(4C*(x)) across prompts whose C*(x) range from about 1 to ≫100. Prompts with C*(x)>1/α have their correct answer filtered out by construction. Whether α was chosen on the reported test sets is not stated (a question, not an accusation).
- **Suggested Fix**: Give an adaptive or data-driven α rule (for example α tied to N, or a held-out calibration) and state the selection split. Show an α-sweep on all three datasets. Report accuracy stratified by estimated difficulty (π̂ of the final answer). Cost: about 3 α values × 3 datasets × 2 models with existing samples, so no new generation.

### W2: Experiments cannot support the "verify the scaling monotonic properties" and "optimal scaling" claims (Section 1, Section 7, Figures 1–3)
Section 1 says the experiments "verify the scaling monotonic properties of three algorithms". Definition 3.4 is a worst-case, vanishing-ε statement. A single run on one instance cannot verify it. Figure 3 uses one dataset (AIME24, 30 problems), one model, and 4–5 values of N. No seeds, variance, or confidence intervals appear anywhere in Section 7 (not stated after search). The headline theoretical object, the √(1/k) rate, is never fit or plotted; Figures 1–2 plot accuracy against k only. The Figure 1 caption itself says BoM "matches the performance of baselines in other settings", and Section 7.2 concludes only "a better overall performance over baselines when k is small".
- **Suggested Fix**: Add ≥5 resampled runs (bootstrap over problems and over the N samples) with intervals. Plot regret against k on log-log axes with a √(1/k) reference. Cost: bootstrap on stored samples is negligible; fresh seeds ≈ 20–40 GPU-hours.

### W3: Baselines omit the natural competitor the paper itself defines (Algorithm 1 vs Section 7.1)
Algorithm 1 defines reward-weighted majority voting, and Section 4.1 says it was "shown to achieve better performance than the unweighted version (Wu et al., 2024b)". Section 7.1 evaluates only unweighted majority ("we directly select k answers (up to mathematical equivalence) with highest frequency"). No pessimistic or regularized BoN variant from the cited literature is run. "BoN" in Section 7.1 ranks answer groups by group-mean reward, which differs from Algorithm 2 (individual responses).
- **Suggested Fix**: Add weighted voting (sum of rewards per answer group) and a minimum-support BoN variant. Cost: zero new generation.

### W4: Regime mismatch between the theory and the experiments (Theorem 6.1; Section 7)
Theorem 6.1 assumes "C∗(x) ≥ 2k", i.e. π_ref(y*|x) ≤ 1/(2k). For k up to 10, this is only the hardest prompts. On GSM8K and MATH-500 with a 4B model, most prompts have π_ref(y*|x) near or above 1/2, so C*<2k and neither bound applies. Also, with α=3/(4C*), |Ŷ_α| ≤ 4C*/3, so for k ≥ ~4C*/3 BoM returns y* whenever E holds, regardless of ε. The statement that ε_opt "does not diminish as the number of candidates k increases" (Section 6) therefore holds only in the regime k ≤ C*/2.
- **Suggested Fix**: State the regime in Theorems 5.1/6.1 and in the abstract, and report experimental results restricted to prompts with 2k ≤ Ĉ* (estimated from π̂).

### W5: Appendix constants contain slips (Appendix B.2, B.3, Error Log ERR-1, ERR-2)
These do not change any qualitative conclusion; see the Error Log.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5 | Abstract vs Table 1 vs Theorem 4.2 | "prove that neither majority voting nor BoN exhibits the desirable scaling with k and the sampling budget" | Table 1 lists BoN under "Optimal k-scaling" as Unknown, and Table 1's caption says "BoN lacks the regret upper bound". Section 4.2 says the BoN lower bound at N=Θ̃(C*) "aligns with the general lower bound". Remark 4.3 only conjectures impossibility. So no k-scaling deficiency of BoN is proved. | Cross-referenced Abstract, Table 1, Section 4.2, Remark 4.3 | High | MAJOR | Say that BoN is not scaling-monotonic and that its k-scaling is open |
| ERR-2 | E6 | Algorithm 3 line 5 vs Section 5 "Computational Complexity" | "BoM only queries the reward model for a filtered subset of candidates" | Algorithm 3 line 5 is "Query reward labels" for all N responses, before the |Ŷ_α| test. The efficiency claim contradicts the algorithm as written, and Section 7.1 evaluates all N trajectories. | Cross-referenced Algorithm 3 and Section 5 | High | MAJOR (claim untested) | Move the query after the filter, or drop the claim |
| ERR-3 | E2 | Appendix B.2, Eq. B.1 | "N ≥ 9C ∗ (x) log(2k + 2)" (Theorem 4.1) | (B.1) states P[N*/N ≥ 3/(2C*)] ≤ exp(−N/(9C*)) and P[N_i/N ≤ 3η/(4C*)] ≤ exp(−Nη/(4C*)). For the first, the optimal Chernoff exponent is μ(1.5 ln 1.5 −0.5)=0.108μ, which is below the stated 1/9=0.111. For the second, the exponent is μ(0.75 ln 0.75+0.25)≈0.034μ versus the stated 0.25μ. Constants are too strong, so the threshold 9C* log(2k+2) is not implied. | Recomputed with KL(a‖p) | Medium (exponents read off a garbled extraction) | MINOR | Re-derive constants; the qualitative result stands |
| ERR-4 | E2 | Appendix B.3, final display of the improved analysis | "≥ 0.004" | With ε_RM/(2√p), p=4k/N, and the two factors (1−e^{−1/12})(1−e^{−1/8}) ≈ 0.080×0.1175, the constant is ≈0.0094/4≈0.0024, not 0.004. The text also writes "1 − e8" for 1−e^{−1/8}. | Recomputed | Medium | MINOR | Fix constants |
| ERR-5 | E5 | Section 5, after Theorem 5.1 | "the second term dominates, and consequently the overall regret" | The second term is √(C*ε²/k). It dominates only when ε_opt ≪ √(C*ε²/k), not when ε_opt ≪ √(C*ε²) as written. Otherwise regret floors at ε_opt as k grows. | Derived from Theorem 5.1 | High | MINOR | Correct the condition |

Minor: "GSK8K" typo (Section 7.2); "(1 − C∗ e^{…})" in (A.2) and (A.7) should be a plain product bound; A(x) in the definition of Y_α(x) (Appendix A) is undefined; "regret and the sampling budget k" (Section 4 intro) conflates k with N; Section 3 sentence "Different from the settings where the model is allowed to generate and submit k candidate responses" contradicts the next clause and should be rewritten.

## Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Minimax lower bound Ω(ε_opt+√(C*ε²/k)) | Sec 1, Thm 6.1 | Lemma B.1, Thm B.2 | Supported for non-binary r* and 2k ≤ C*; regime and class not stated (see W4, Q3) |
| C2 | BoM achieves the matching upper bound | Thm 5.1 | Appendix A | Supported given known C* (W1) |
| C3 | MV and BoN not scaling-monotonic, BoM is | Thm 4.1, 4.2, Cor 5.2 | Appendix B.2–B.3 | MV and BoN supported; BoN "k-scaling" claim unsupported (ERR-1) |
| C4 | BoM beats baselines; experiments verify monotonicity | Sec 7, Fig 1–3 | Captions and prose | Partially supported; no variance; verification claim unsupported (W2) |

## Missing References
Not my role; see Reviewer 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Proofs are mostly correct, but α is unknown in practice and the experiments are thin |
| Clarity | 3 | Well organized; some garbled definitions in Section 3 |
| Significance | 2 | Narrow setting (known-C* thresholding), k-submission tasks only |
| Originality | 2 | Extension of the single-policy-coverage pessimism line to k>1 |

## Dimension Scores (0–100)
**Pool position:** better than about 58% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: sound theory with a tight k-dependence, but an unimplementable-as-stated algorithm, no variance in the experiments and an overclaiming abstract place it just below the borderline for this reviewer.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 66 | Competent | Main proofs correct; constant slips; regime and class conditions omitted |
| Clarity & Presentation | 62 | Competent | Clear structure; empty Appendix C; several loose statements |
| Novelty & Originality | 58 | Competent (low) | k-dependence and bins argument are new; the algorithm is frequency-filtered BoN |
| Significance & Impact | 58 | Competent (low) | Useful framing; practicality limited by C* |
| Experimental Validation | 44 | Developing | One run, 3 saturated-to-small datasets, missing baselines, no theory-driven measurements |
| Reproducibility | 50 | Developing | α-selection, seeds and code not stated |
| Ethical Compliance | 65 | Competent | Nothing at stake; limitations not discussed |

## Questions for Authors
1. How was α chosen for the k-sweeps (Figures 1–2) and for N=100 versus N≥200 (Section 7.2)? On which split? If a held-out validation split gives the same ranking, my Experimental Validation score rises about 10 points.
2. What do the empirical Ĉ*(x) and ε̂_RM(x) look like on each dataset, and for what share of prompts does 2k ≤ C*(x) hold? If it is small, the theory covers little of what is plotted.
3. Do the Lemma B.1 and Theorem B.2 instances belong to the same class with exactly the same ε_opt, given that Assumption 3.2 is stated with equality?
4. Appendix C is referenced (footnote 1) but empty in my copy. What does it contain?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. There is no limitations discussion; the known-C* requirement, the binary-reward case and the per-prompt nature of the bounds are not discussed.

## Ethics Review Flag
**No**: nothing at stake.

## Overall Score
**3**: Sound theory with a tight k-dependence, but the algorithm as proven needs C*, the experiments do not test the central claims, and the abstract overstates what is proved about BoN.

## Confidence
**4**: I rechecked the proofs line by line; the figures were not available.

---

# Peer Review Report

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Reviewer: Prof. Mirela Tsankov-Rey, Reviewer 2 (Domain) (public university theory group, Eastern Europe; fictional persona)
## Expertise: inference-time alignment theory; pessimism and single-policy coverage in offline RL
## Date: 2026-11-10

## Summary
The paper adapts the coverage-based analysis of Best-of-N from Huang et al. (2025) to a setting where k responses are submitted. It shows that frequency-based filtering plus reward ranking (BoM) attains a regret rate with the right k-dependence, and that this rate is unimprovable in the worst case. It also shows that majority voting has constant worst-case regret and that BoN's regret lower bound grows with N.

## Strengths
### S1: A genuinely new axis, k, on top of coverage-based inference-time theory (Remark 3.3; Theorem 6.1)
Prior coverage-based analyses (Huang et al. 2024, 2025; Verdun et al. 2025) treat k=1. A lower bound exhibiting 1/√k and an algorithm attaining it is a real addition.

### S2: Honest positioning relative to the closest prior work (Sections 1, 4.2, Remark 4.3)
The paper credits Huang et al. (2025) for scaling-monotonicity, the coverage coefficient and the BoN k=1 bound, and explains why their proof does not extend (the auxiliary rejection-sampling distribution, Remark 4.3).

### S3: Theoretically principled design (Section 5)
Pessimism is used for a clear reason: the reward model is trustworthy only where π_ref has mass. The frequency filter is the minimal operationalization of that.

## Weaknesses
### W1: The claim of a new Pass@k theory and the boundary with known results needs care (Section 2; Table 1 caption)
Section 2 says "the theoretical Pass@k inference framework is novel and remains unexplored in the existing literature". The BoN non-monotonicity part of C3 is the degradation phenomenon already shown by Huang et al. (2025) for k=1 (their abstract notes that naively scaling Best-of-N can degrade performance through reward hacking). Stroebl et al. (2024), which the paper cites only for overoptimization (Section 4.2), analyzes resampling with imperfect verifiers, which is close in spirit. I rate the claims: C1 (k-dependent lower bound) high novelty; C2 (BoM bound) medium (frequency-filtered pessimism plus a k-averaging step); C3 (MV not monotone) medium but technically light (Appendix B.2); C3 (BoN not monotone) incremental, since Huang et al. 2025 covers k=1 and this paper extends it to k>1. This is a MAJOR-at-most claim-level finding: differentiate more sharply.
- **Suggested Fix**: A delta table versus Huang et al. (2025) in the main text: what changes in the algorithm, the assumptions, and the proof (the proof's key new step is (A.9), min ≤ average over k).

### W2: The minimax-optimality label covers only a class that includes non-binary rewards (Theorems 4.1, 4.2, 6.1; Section 3)
The motivating case is binary r* (Section 3: "the ground-truth reward model r∗ functions as a binary verifier"). Every hard instance, however, uses graded rewards: r*(y_i)=1/2 in Theorem 4.1, r*(y_i)=1−ε/(2√p) in Theorem 4.2, and 1−δ in Theorem B.2. With binary r* the regret is the probability that y* is not submitted, and the lower bound as constructed no longer applies. So minimax optimality for Pass@k is established for the graded-reward class, not for the binary Pass@k metric that motivates it.
- **Suggested Fix**: State the class explicitly in the abstract and Table 1; add a binary-reward lower bound or say it is open.

### W3: Related work and citation accuracy (Sections 1–2)
Brown et al. (2024) is described as having conducted "empirical studies on this inference framework" where an algorithm selects k of N. As I read the abstract, that work measures coverage (whether any of N samples solves the problem), not selection of k out of N, so the characterization may be loose (a question, not an error; I can see only the abstract). The origin of the metric is attributed to Li et al. (2022) (AlphaCode), whereas the standard reference for the pass@k metric and estimator is the Codex paper (see Missing References).
- **Suggested Fix**: Re-describe Brown et al. precisely; cite the metric's source.

### W4: Practical grounding of the reward-model assumption (Assumption 3.1, Section 7.1)
Assumption 3.1 is an L2 error under π_ref over answers. The experiments score trajectories and average within an answer group, a reward the theory does not define. How Assumption 3.1 maps onto AceMath-7B-RM outputs is never discussed.
- **Suggested Fix**: A short section mapping the answer-level r̂ to the group-mean construction, ideally with an empirical ε̂_RM.

## Literature-check addendum (strict, cutoff 2025-09-24)
Per-claim novelty (hand-assigned from kept abstracts; the `novelty` script was not run, so verdicts are provisional):

| Claim | Dimension | Novelty | Top prior work (link, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------|-----------|
| C1: k-dependent minimax lower bound | result | high | none covers k>1: Huang et al. 2025, arxiv.org/abs/2503.21878 (recent preprint; cited) is k=1 | no close prior work found in the kept results (arXiv only) |
| C2: BoM bound matching the lower bound | method | medium | Huang et al. 2025 (pessimistic algorithm, k=1; cited) | level 3: same mechanism class, different setting and bound |
| C3a: MV not scaling-monotone | result | medium | Wu et al. 2024b, arxiv.org/abs/2408.00724 (prior arXiv-only; cited; empirical); Chen et al. 2024, arxiv.org/abs/2403.02419 (cited; Filter-Vote non-monotonicity) | level 3: empirical analyses, no worst-case bound |
| C3b: BoN not scaling-monotone | result | incremental | Huang et al. 2025 | level 4: reward-hacking degradation shown at k=1 |
| C4: empirical superiority | result | n/a | — | evaluated in Reviewer 1's report |

Novelty delta (closest prior works):

| Contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|--------------|--------------------|----------------------|------------------|---------------------------|
| BoM / pessimism | Huang et al. 2025 | pessimistic inference-time alignment with coverage guarantees (k=1) | k-submission, frequency threshold, 1/√k rate | cited; differentiated in Remark 4.3 and Section 5 |
| Scaling with N | Wu et al. 2024b; Chen et al. 2024; Stroebl et al. 2024 | empirical scaling laws and a limits-of-resampling analysis | worst-case lower bounds in the k-submission setting | cited; Stroebl et al. only for overoptimization |

Baseline scout: not run (benchmarks are testbeds, not SOTA comparisons). Field snapshot: before the cutoff, test-time scaling theory moved from empirical scaling laws (2024: Wu et al., Brown et al., Snell et al.) to coverage-based guarantees for BoN and pessimism (2025: Huang et al.), with open questions on optimal use of verifiers and on k>1. A significant contribution now is a tight, interpretable bound that explains reward-hacking degradation; a log-factor refinement is incremental. I used this to score Novelty at the incremental-to-clearly-novel boundary, not higher.

## Missing References
*(Verified via `related_search.py verify` unless marked `[verify]`.)*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Chen, M., Tworek, J., Jun, H., et al. (2021). Evaluating Large Language Models Trained on Code. arXiv:2107.03374 (found: arxiv.org/abs/2107.03374) | Standard source of pass@k and its estimator; the paper credits Li et al. (2022) for the metric |
| Important | Setlur, A., Rajaraman, N., Levine, S., Kumar, A. (2025). Scaling Test-Time Compute Without Verification or RL is Suboptimal. arXiv:2502.12118 (found: arxiv.org/abs/2502.12118) | Theory of when verifier-based selection beats verifier-free scaling; related to the role of the reward model |
| Helpful | Wang, P., Li, L., Shao, Z., et al. (2024). Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. ACL 2024 (found: arxiv.org/abs/2312.08935) | Reward-weighted voting with a process reward model, the natural stronger baseline for weighted voting |
| Helpful | Rashidinejad, P., Zhu, B., Ma, C., Jiao, J., Russell, S. (2021). Bridging Offline Reinforcement Learning and Imitation Learning: A Tale of Pessimism. NeurIPS 2021 `[verify]` | Single-policy-coverage pessimism, the lineage behind Section 5 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Correct core proofs, tight bounds |
| Clarity | 3 | Clear framing, minor slips |
| Significance | 3 | Relevant to test-time scaling theory |
| Originality | 2 | Extends known coverage/pessimism analyses to k>1 |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a new, well-defined k-axis with matching bounds, but novelty over Huang et al. (2025) is incremental in method and the graded-reward scope is narrower than the title suggests.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 72 | Competent (high) | Correct proofs, honest scope in Remark 4.3 |
| Clarity & Presentation | 66 | Competent | Clear problem statement, loose wording in places |
| Novelty & Originality | 60 | Competent | New k-axis, incremental method |
| Significance & Impact | 62 | Competent | Useful for theory of test-time scaling |
| Experimental Validation | 52 | Developing (high) | Small, single-run |
| Reproducibility | 55 | Competent (low) | α and seeds missing |
| Ethical Compliance | 68 | Competent | Nothing at stake |

## Questions for Authors
1. Can you state a binary-reward lower bound or say it is open? A binary result would raise my Novelty score.
2. What exactly differs from the pessimistic algorithm of Huang et al. (2025) at k=1, and does BoM recover it?
3. Does Theorem 4.1 cover weight functions with w(1/2)=0 (a hard reward threshold)? The condition "C ∗ (x) ≥ 1 + 2kw(1)/w(1/2)" is vacuous there.

## Limitations Assessment
**Partially**: Remark 4.3 is candid about BoN's open k-scaling; no dedicated limitations section.

## Ethics Review Flag
**No**: nothing at stake.

## Overall Score
**4**: A real new axis with tight bounds from a sound extension of the coverage framework; incremental in method, narrow in experiments.

## Confidence
**4**: I know this literature well; I judged prior work from abstracts only.

---

# Peer Review Report

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Reviewer: Dr. Haruto Delacroix-Nwosu, Reviewer 3 (Perspective) (applied-statistics and decision-theory group; fictional persona)
## Expertise: ranking and selection, best-arm identification, unit-test-verified code generation
## Date: 2026-11-10

## Summary
The paper studies what to submit when an LLM may submit k of N sampled answers and a noisy reward model is available. It argues that voting ignores the reward model while Best-of-N trusts it where it should not, and offers a filter-then-rank rule with matching upper and lower bounds. It illustrates the rule on math reasoning.

## Strengths
### S1: Connects to a familiar decision problem (Sections 3, 5)
Selecting k candidates under a noisy score is a subset-selection problem (ranking and selection, top-k identification), and the lower-bound construction in Theorem B.2 is the classic k-of-M indistinguishable arms argument. This lends the result credibility and suggests links to that literature.

### S2: Pessimism as an engineering principle (Section 5)
Trusting the reward model only where the reference policy has support is easy to apply, and BoM is one line on top of BoN.

### S3: Immediately relevant to tasks with cheap verifiers (Section 3 on Pass@k)
Code generation with unit tests and formal theorem proving are settings where k submissions are natural. The paper's framework gives them a vocabulary.

### S4: The negative result on majority voting is a useful caution (Theorem 4.1)
It is a clean illustration that frequency is a poor proxy for correctness when many distinct wrong answers share mass.

## Weaknesses
### W1: Deployment gap: unknown C* and per-prompt thresholds (Theorem 5.1)
In practice a pipeline will have one α for all prompts. A per-prompt adaptive rule, such as an α that tracks the empirical concentration of the top answers, would match the theory more closely and could be explored.
- **Suggested Fix**: Offer an empirical-Bayes or two-stage rule; report how sensitive accuracy is to α.

### W2: Assumption audit (Assumptions 3.1–3.2)
Three assumptions are implicit: (i) a unique correct answer, which fails for proofs and code (many correct programs); (ii) a stationary reward error under π_ref, whereas a reward model is often wrong exactly on the rare, fluent-but-wrong answers; (iii) a prompt-by-prompt analysis, while deployment cares about average accuracy, where heterogeneity of C*(x) matters.
- **Suggested Fix**: Discuss (i) as a limitation, and add one experiment on a task with multiple correct answers (code with unit tests) to show the framework's reach.

### W3: Cost accounting (Section 5, "Computational Complexity")
The paper says BoM can reduce reward evaluations and adds no generation cost (Section 5: "without incurring additional generation cost"). I take the efficiency point as plausible but could not see how the reward-model budget was counted in Section 7. Test-time cost versus accuracy curves (equal total compute) would make the practical story concrete.
- **Suggested Fix**: Plot accuracy against total generated tokens plus reward calls.

### W4: Broader cross-field ideas (constructive)
Top-k identification with a fixed budget, "pessimistic" lower-confidence-bound ranking, and conformal selection offer ready-made tools: for instance, confidence-bound ranking of answer groups instead of a hard frequency cut.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound theory; experiments illustrative |
| Clarity | 3 | Readable for a non-theorist |
| Significance | 3 | Relevant for verifier-based k-submission tasks |
| Originality | 3 | Fresh framing of a k-axis |

## Dimension Scores (0–100)
**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean formalization with a matching lower bound and a one-line algorithm, of interest to a broad test-time-scaling audience.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 70 | Competent (high) | Standard but correct tools |
| Clarity & Presentation | 68 | Competent | Easy to follow |
| Novelty & Originality | 64 | Competent | New axis |
| Significance & Impact | 66 | Competent | Broad relevance |
| Experimental Validation | 55 | Competent (low) | Illustrative |
| Reproducibility | 58 | Competent | Setup described, α unclear |
| Ethical Compliance | 70 | Competent | Nothing at stake |

## Questions for Authors
1. Does BoM help on code with unit tests, where r* is binary and several programs are correct? A positive result would raise my Significance score.
2. Can α be set per prompt from the empirical frequency profile?
3. What is the total compute (generation plus reward-model calls) at the settings in Figures 1–3?

## Limitations Assessment
**Partially**: no explicit limitations discussion; the unique-answer assumption is not flagged.

## Ethics Review Flag
**No**: nothing at stake.

## Overall Score
**4**: A tidy, broadly relevant formalization with a practical one-line rule, held back by thin experiments.

## Confidence
**3**: I am a non-specialist in LLM-inference theory, and I did not check the proofs in detail.

---

# Peer Review Report

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Reviewer: Dr. Selin Karahanova, Reviewer 4 (Generalist) (ML group at a research university, Middle East; fictional persona)
## Expertise: LLM reasoning, RL post-training
## Date: 2026-11-10

## Summary
The paper asks how best to pick k answers out of N samples from an LLM, given an imperfect reward model. It shows that majority voting and Best-of-N each fail in some worst cases, introduces a filter-then-rank method (BoM), and proves matching upper and lower bounds on regret. Experiments on three math benchmarks show BoM is competitive or better for small k.

## Strengths
### S1: A clear one-sentence contribution (Section 1)
BoM = drop low-frequency answers, then take the top-k by reward. The paper states what it adds and why (Table 1).

### S2: Table 1 is an efficient summary
It conveys worst-case regret, monotonicity and k-scaling for four rows in one place, and honestly marks BoN's k-scaling "Unknown".

### S3: Theory and experiments are both present, and the experiments are simple to follow (Section 7)
Three datasets, two model sizes, and a monotone-in-N study in Figure 3.

### S4: Venue fit (ICLR)
Learning-theory for LLM inference is in scope for ICLR; ICLR also welcomes theory with small-scale experiments.

## Weaknesses
### W1: Presentation of the setting hinders a non-theorist (Section 3)
The sentence "Different from the settings where the model is allowed to generate and submit k candidate responses, our goal is to maximize the highest ground-truth reward of the k samples" appears to contradict itself, and k is called the "sampling budget" in Section 4's introduction. The reader must infer that responses are answers, that r̂ is a function of the answer, and that N is the number of samples. I could not find where these identifications are made explicit.
- **Suggested Fix**: A short plain-language problem paragraph and a notation table.

### W2: Claims in the abstract run ahead of what is shown (Abstract; Table 1; Section 7)
"prove that neither majority voting nor BoN exhibits the desirable scaling with k" is not what Table 1 says for BoN (Unknown). "its performance does not degrade when increasing N" is shown theoretically only under N≥threshold, and empirically in one figure.
- **Suggested Fix**: Align the abstract with Table 1.

### W3: Experiment reporting (Section 7)
The text says BoM "consistently outperforms" on MATH-500 (Figure 1 caption), but with no variance the reader cannot tell a one-problem difference from a real gap, especially on AIME24 (a small set). Appendix C ("Additional Experiments") is empty in my copy, although footnote 1 sends the reader there for additional models.
- **Suggested Fix**: Add intervals, fill Appendix C, and state α.

### W4: No limitations or future-work discussion beyond one sentence (Section 8)
The conclusion lists only a post-training direction.
- **Suggested Fix**: A short Limitations paragraph (known C*, unique-answer assumption, graded-reward lower bounds).

Minor: "GSK8K" (Section 7.2), grammar in Section 3 ("Since the training of the reward model extensively studied").

## Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness of claims | Partly (theory sound; abstract overclaims on BoN; experiments illustrative) | Abstract, Thm 4.2, Table 1 |
| Presentation | Partly | Section 3, Appendix C |
| Contribution (significance, novelty) | Partly | Sections 5–6, Remark 4.3 |
| Reproducibility | Partly (α and seeds missing) | Section 7 |
| Relevance to ICLR audience | Met | Section 1 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound theory, thin experiments |
| Clarity | 2 | Section 3 wording, empty Appendix C |
| Significance | 3 | Of interest to the test-time scaling community |
| Originality | 3 | New axis |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear contribution with matching bounds and a plausible audience, though polish and experiments are below what accepted theory papers usually show.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 68 | Competent | Theory looks sound; I did not check every constant |
| Clarity & Presentation | 60 | Competent (low) | Section 3, abstract-versus-Table 1 mismatch, empty Appendix C |
| Novelty & Originality | 62 | Competent | New k-axis |
| Significance & Impact | 62 | Competent | Test-time scaling is a hot area |
| Experimental Validation | 50 | Developing (high) | No variance; few baselines |
| Reproducibility | 56 | Competent (low) | α unspecified, no code statement |
| Ethical Compliance | 68 | Competent | Nothing at stake |

## Questions for Authors
1. What does Appendix C contain, and which "additional models" does it cover?
2. Where in the paper are the identifications of a response with a final answer and of r̂ as an answer-level function stated?
3. Would you add weighted voting to Figures 1–2?

## Limitations Assessment
**No**: no limitations section.

## Ethics Review Flag
**No**: nothing at stake.

## Overall Score
**4**: A clear, relevant theoretical contribution that the community would benefit from seeing, if the abstract is aligned with Table 1 and the experiments are tightened.

## Confidence
**4**: Confident on venue fit and presentation; I did not verify every derivation.

---

# Devil's Advocate Report

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Reviewer: Dr. Matteo Ibarra-Quill (evaluation-methodology group, South America; fictional persona)

---

## Steelman
The paper gives the first k-dependent worst-case analysis of selecting k of N samples with an imperfect reward model, with an upper bound that matches a lower bound. It explains, with explicit hard instances, why voting and Best-of-N each break, and a one-line filter repairs the problem in theory and in a small experiment.

---

## Core Argument Chain
1. Pass@k inference with an imperfect reward is formalized by Eq. 3.1 with Assumptions 3.1–3.2.
2. Majority voting has constant regret (Theorem 4.1) and BoN has regret growing with N (Theorem 4.2), so neither is scaling-monotonic.
3. BoM attains O(ε_opt+√(C*ε²/k)) for N ≳ C* (Theorem 5.1); a general lower bound matches (Theorem 6.1).
4. Therefore BoM is minimax optimal and scaling-monotonic.
5. Experiments on math datasets show BoM outperforming both baselines and monotonicity verification monotonicity.
∴ BoM is the preferable inference strategy and the optimal one for Pass@k.

---

## Strongest Counter-Argument
The central premise is that BoM is the optimal Pass@k strategy, but what is proved is narrower in three ways that compound. First, the algorithm that attains the bound sets "the threshold is α = 3/(4C ∗ (x))". The threshold requires C*(x)=1/π_ref(y*|x), a property of the unknown correct answer. The optimality result is therefore for an oracle-parameterized rule, and the practical rule (one global α, 0.005 or 0.015, Section 7.2) is a different algorithm that carries no guarantee. Prompts with C*(x)>1/α have y* removed by construction, and these are exactly the hard prompts that matter for Pass@k.

Second, the lower bound is for a class that includes graded rewards (Theorem 6.1 requires "C ∗ (x) ≥ 2k" and instances with r*=1−δ), not for the binary verifier setting that the paper uses to motivate Pass@k (Section 3). For binary r*, no matching lower bound is shown, so "minimax optimal for Pass@k" is not established for the metric in the title. The regime 2k ≤ C*(x) is also only the hardest prompts when k is as large as 10.

Third, the discriminating evidence for the headline claim, that BoM keeps improving as N grows while BoN degrades, is one figure on one dataset with 30 problems, a single model, and no variance (Figure 3). The text concludes "BoM has a more consistent performance". A hard threshold on frequency also degenerates for small N (α·N<1 keeps everything, so BoM equals BoN), and practitioners rarely sample N=500–2000. How would the authors answer a reader who says: "At N=64, k=5, on a prompt with C*=100, what does BoM do that BoN does not" A paper that proves optimality of an oracle-tuned rule and illustrates it with a globally tuned one has not yet shown that the optimal rule is usable.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The evidence supports a narrower claim: the proofs I checked hold, no test-set selection is stated, and the problems are fixable by narrowing wording and adding analyses.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Scope / Logic | Theorem 5.1; Section 7.2 | Optimality is for α=3/(4C*(x)) (needs unknown C*); experiments use a global α with no stated selection protocol (α=0.005, 0.015). The two are different algorithms. | Adaptive α with a guarantee, or an explicit statement that the guarantee is oracle-parameterized; α-sweep and validation split |
| DA-M2 | Overclaim (E5) | Abstract; Table 1; Section 5 intro; Thm 4.2; Remark 4.3 | "neither majority voting nor BoN exhibits the desirable scaling with k" is contradicted by the paper's own Table 1 ("Unknown"), Section 4.2 ("aligns with the general lower bound") and Remark 4.3 (only a conjecture) | Narrow the abstract to what is proved |
| DA-M3 | Scope | Section 3; Theorems 4.1, 4.2, 6.1 | Hard instances use graded rewards (r*=1/2, 1−ε/(2√p), 1−δ); motivating Pass@k case is binary | State the class; prove or flag the binary case as open |
| DA-M4 | Evidence | Section 1; Section 7.2; Figure 3 | "verify the scaling monotonic properties" and the claim that majority voting's low accuracy "aligns with Theorem 4.1" are not tests of a worst-case statement. A single instance cannot verify Definition 3.4. Majority voting's flat curve is also what any saturating estimator would show. | Replace with "consistent with"; add variance and several datasets |
| DA-M5 | Alternative explanation | Section 7.1; Algorithm 1; Algorithm 2 | BoM's gain over "BoN" may come from a minimum-support rule on group-mean rewards, which single-sample answer groups (with noisy rewards) violate. Reward-weighted voting and a min-support BoN are not run, so the benefit of the frequency threshold specifically is not isolated. | Add the two baselines |
| DA-M6 | Logic | Definition 3.4 vs Section 3 text | The text says scaling-monotonicity "guarantees that the performance of the algorithm does not degrade when increasing N". Definition 3.4 is an asymptotic condition (regret ≤ δ for N ≥ N0 when ε_RM ≤ ε0); it does not imply non-degradation for a fixed ε, and Theorem 5.1 is vacuous below N≈16C* log(kC*/ε²_RM) | Reword the interpretation |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Algorithm 3 line 5; Section 5 | "BoM only queries the reward model for a filtered subset" conflicts with line 5, which queries all N |
| DA-m2 | Correctness | Appendix B.2 (B.1); B.3 | Chernoff constants (1/9, η/4) and "0.004" do not follow from the stated bounds; qualitative results unaffected |
| DA-m3 | Completeness | Theorem 6.1 / Theorem B.2 | δ=√(Cε²/(M−1)) must be ≤1; the condition C*ε²_RM ≲ k is missing from the statement |
| DA-m4 | Completeness | Footnote 1; Appendix C | Referenced additional-model results are empty in the provided text (unverifiable) |
| DA-m5 | Scope | Theorem 4.1 | Condition "C ∗ (x) ≥ 1 + 2kw(1)/w(1/2)" excludes w(1/2)=0 (hard threshold), so weighted voting with a sharp reward cut is not covered |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Chernoff exponent, upper tail at 1.5μ (Appendix B.2, B.1) | exp(−N/(9C*)) i.e. exponent μ/9≈0.111μ | μ(1.5 ln 1.5−0.5)=0.108μ | No (constants only) |
| Chernoff exponent, lower tail at 0.75μ (B.1) | exp(−Nη/(4C*)) i.e. 0.25μ | μ(0.75 ln 0.75+0.25)=0.034μ | No (constants only) |
| Constant in B.3 final display | ≥ 0.004 | 0.0800×0.1175×(1/4)≈0.0024 | No |
| Final N condition vs Lemma A.1 (Theorem 5.1) | N ≥ 16C* log(kC*/ε²) | 5C*e^{−N/(32C*)} ≤ 5√(C*ε²/k) | Yes |
| Group-count bound (A.5) | M ≤ 4C* | bins of capacity 1/(2C*), pairs sum > 1/(2C*), so M ≤ 4C*+1 | Approximately (off by one) |

## Ignored Alternative Explanations
- BoM's frequency threshold acts as a minimum-support filter on a noisy per-group reward; any variance-aware ranking (lower confidence bound on the group mean) may give the same gain.
- Majority voting's flat curves in Figure 3 are consistent with ordinary saturation of voting accuracy; they are not specific evidence for Theorem 4.1's constant-regret construction.
- BoN's decline with N is the known reward-hacking effect (Gao et al.; Stroebl et al., both cited), so it is not new evidence for the paper's theory.

## Missing Stakeholder Perspectives
Practitioners with a single global threshold and small N (8–64) are not represented. Tasks with several correct answers (code, proofs) are not represented either.

## Observations (Non-Defects)
- The proof structure of Theorem 5.1 and the averaging-hammer lower bounds are correct and cleanly arranged.
- Remark 4.3 is a candid statement of what the technique cannot yet do for BoN.
- Table 1 marks BoN's k-scaling "Unknown", so the paper is more careful than its abstract.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 58 | Proofs sound; oracle α; regime and class gaps |
| Clarity & Presentation | 60 | Abstract/Table 1 mismatch; Section 3 wording |
| Novelty & Originality | 54 | Incremental method; new axis |
| Significance & Impact | 54 | Practicality limited |
| Experimental Validation | 42 | Cannot test the headline claims |
| Reproducibility | 48 | α, seeds, code |
| Ethical Compliance | 66 | Nothing at stake |

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: oracle-parameterized optimality plus an untested practical rule and an overclaiming abstract put it at the upper end of the typical rejected band.

## Overall: 3 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Each weakness was checked for specificity, whether the paper already answers it, consistency with the paper, and actionability.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (α unknown / unstated) | kept | The paper contains no α-selection statement after search; the C* dependence is Theorem 5.1 itself |
| R1 | W2 (experiments cannot verify) | kept | Quote and Figure 3 caption checked |
| R1 | W3 (baselines) | kept | Algorithm 1 vs Section 7.1 checked |
| R1 | W4 (regime) | kept | Theorem 6.1's "C ∗ (x) ≥ 2k" checked |
| R1 | W5 (constants) | moved to Minor line (ERR-3/4 stay in the log) | Cosmetic for the conclusion |
| R2 | W1 (novelty vs Huang et al.) | rewritten | Stated as claim-level and MAJOR at most; the paper cites Huang et al. |
| R2 | W3 (Brown et al. wording) | rewritten as a question | Only the abstract was read, so it cannot be an error |
| R3 | W3 (cost accounting) | rewritten | The statement that there is no additional generation cost is in Section 5; the reviewer's own reading of the reward-call count is uncertain |
| R4 | W1 ("sampling budget k") | kept | Section 4 intro wording checked |
| R4 | W3 (Appendix C empty) | kept as unverifiable | Appendix C is a bare heading in the extraction |
| DA | DA-M4 | kept | Quotes verified in Section 1 and Section 7.2 |
| DA | numerical-check row row on (A.5) | moved to Minor | Off by one only |
| R3 | S3 relevance to code tasks | kept | No claim about the paper's content |

Scores were not changed.

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer Part A: Package for the EIC

**Official score (before the EIC; no weights, no DA-CRITICAL issues).** Ratings R1 3, R2 4, R3 4, R4 4, DA 3: mean 3.60 · official composite 61.6 · before-overall 4.

**Master issue list and classes.**

| Issue | Sources | Class |
|-------|---------|-------|
| Oracle α (needs C*); α selection unstated; one global α | R1-W1, R3-W1, DA-M1, DA-Q | CONSENSUS-3 |
| Experiments thin: single run, no variance, the monotonicity-verification claim overclaim | R1-W2, R4-W3, DA-M4 | CONSENSUS-3 |
| Abstract overclaims BoN k-scaling (vs Table 1/Thm 4.2/Remark 4.3) | R1-ERR-1, R4-W2, DA-M2 | CONSENSUS-3 (hinges) |
| Missing baselines (weighted voting, min-support BoN) | R1-W3, DA-M5 | CONSENSUS-2 |
| Class of rewards / binary case; regime 2k ≤ C* | R1-W4, R2-W2, DA-M3 | CONSENSUS-3 (hinges) |
| Novelty incremental over Huang et al. 2025 | R2-W1 | SOLO |
| Algorithm 3 line 5 vs "filtered subset" efficiency claim | R1-ERR-2, DA-m1 (R3 repeats the claim in W3) | CONSENSUS-2 |
| Presentation of Section 3; empty Appendix C; no Limitations | R4-W1, R4-W3, R4-W4, R1-Q4 | CONSENSUS-2 |
| Chernoff constants | R1-ERR-3/4, DA-m2 | CONSENSUS-2 (minor) |
| Unique-answer assumption, multiple correct answers | R3-W2 | SOLO |

DA-CRITICAL: none. SPLIT: none explicit (R3 and R4 are more positive on significance). Outcome may hinge on: the BoN overclaim, the oracle-α gap, and the regime/class point. Warnings from the script: none.

## EIC Meta-Review (Prof. Ingrid Valdsen)

### The Case For and Against
- **For acceptance:** A clean new axis (k) in coverage-based test-time theory, with an upper bound that matches an information-theoretic lower bound, correct proofs, and a candid Remark 4.3. A simple filter-then-rank algorithm that is easy to adopt, and an audience (test-time scaling theory) that ICLR serves.
- **Against acceptance:** The optimal rule requires the unknown C*, and the practical α is tuned with no stated protocol. The abstract claims more than is proved about BoN. The lower bound is for a graded-reward class and for 2k ≤ C*, not for the binary Pass@k setting that motivates the paper. The experiments are small, single-run and untested against the theory's central rate, and the method is incremental over Huang et al. (2025).

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Abstract claims BoN lacks desirable k-scaling, but Table 1 says "Unknown" | R1-ERR-1, R4-W2, DA-M2 | Abstract; Table 1; Section 4.2; Remark 4.3 | Verified | Quotes found; Section 5 intro repeats the claim ("neither demonstrates the desirable scaling with k") |
| Optimal α=3/(4C*(x)) needs unknown C*; experiments use fixed α with no selection protocol | R1-W1, DA-M1, R3-W1 | Theorem 5.1; Section 7.1–7.2 | Verified | Searched the text for split/selection terms: nothing stated about how α was chosen |
| Algorithm 3 line 5 queries all N rewards but Section 5 claims only a filtered subset | R1-ERR-2, DA-m1 | Algorithm 3; Section 5 | Verified | R3 repeated the authors' claim without checking |
| Lower-bound instances are graded-reward | R1-W4, R2-W2, DA-M3 | Theorem 4.1 (r*=1/2); Theorem 4.2; Theorem B.2 (1−δ) | Verified | Binary-r* case not covered |
| Theorem 6.1 requires C*≥2k, so ε_opt "does not diminish" only for k ≤ C*/2 | R1-W4, DA | Theorem 6.1; Section 6 | Verified | Also |Ŷ_α| ≤ 4C*/3 under α=3/(4C*) |
| Main proof of Theorem 5.1 | R1-S2/S3 | Appendix A (A.8–A.10, Lemma A.1) | Verified | N condition consistent with Lemma A.1's tail |
| Chernoff constants in B.1/B.3 | R1-ERR-3/4, DA | Appendix B.2, B.3 | Partly correct | Recomputed: exponent 0.108μ vs 1/9 holds; the second exponent and 0.004 depend on garbled extraction; qualitative results unaffected |
| "second term dominates" condition | R1-ERR-5 | Section 5 | Verified | Condition should include 1/k |
| Novelty incremental vs Huang et al. 2025 | R2-W1 | Remark 4.3; Section 5 | Partly correct | Huang et al. is k=1 and a recent preprint at the cutoff; cited and differentiated; I do not treat it as a required comparison |
| Text overlap with Wu et al. 2024b | similarity script | Section 2 | Not an issue | It is the paper's own description of that work |
| Experiments monotonicity verification monotonicity | R1-W2, DA-M4 | Section 1; Figure 3 | Verified | Captions say BoM "outperforms baselines with larger N"; no variance |
| Brown et al. characterization | R2-W3 | Section 1 | Unverified | R2 saw the abstract only; kept as a question |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error log entries ERR-1, 2, 5 verified at their locations; regime point verified; minor over-weighting of constants |
| R2 (Domain) | 4 | 4 | 1.0 | Sound, typical; novelty judged from abstracts, one point (Brown) unverified |
| R3 (Perspective) | 4 | 3 | 0.75 | Repeated the authors' reward-evaluation efficiency claim, which Algorithm 3 contradicts; largely generic suggestions |
| R4 (Generalist) | 4 | 4 | 1.0 | Venue fit and the abstract/Table 1 mismatch are right; did not check derivations |
| DA | 3 | 4 | 1.0 | Counter-argument and DA-M1/M2/M3 verified; DA-M5 is a hypothesis, DA-M6 partly a matter of reading |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

I considered whether the oracle-α gap or the BoN overclaim reached criterion 1 or 2: the theorems stand as stated, and the fixes are narrower claims and analyses on existing data, so they are MAJOR.

### Final Decision and Justification
The EIC-weighted rating (R1 1.25, R2 1.0, R3 0.75, R4 1.0, DA 1.0, each multiplied by its confidence weight) is 3.54, which rounds to a **starting point of 4**; the official mean is 3.60 and the composite cross-check (61.5, band 4) agrees, so there is no band disagreement to explain. I keep the starting point. The deciding evidence points to the acceptance side of the borderline, narrowly. The contribution is a correct, tight, interpretable bound with a new k-axis, and its weaknesses (single run, thin baselines, overclaimed wording, oracle parameter) are of the kind accepted theory papers at ICLR often carry. The verified weaknesses are fixable by narrowing claims and adding analyses on stored samples; none concerns correctness of the main theorem. My own pool position is **66** (better than about 66% of ICLR submissions), at the lower edge of what I would call a typical accepted paper. The reviewers' pool positions range 52–70, a spread under 30 points, so no ruling on the disagreement is needed. No DA-CRITICAL issue was raised, so there is no ceiling (none). The decision is **Borderline Accept (4)**, and it is a simulation of how a careful panel might see this draft, not a prediction.

---

# Editorial Decision

## Paper: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling
## Submission ID: iclr26-a6CVQpjbXq
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: theoretical
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Ingrid Valdsen; R1 Methodology Dr. Oyelaran Veckstrom, R2 Domain Prof. Mirela Tsankov-Rey, R3 Perspective Dr. Haruto Delacroix-Nwosu, R4 Generalist Dr. Selin Karahanova, DA Dr. Matteo Ibarra-Quill

---

## Decision: Borderline Accept (4)

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60 · official composite 61.6
**EIC assessment** (internal): weighted rating 3.54 → starting point 4 · weighted composite 61.2 → band 4 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 4
ICLR rating label for 4: "6 on {0,2,4,6,8,10}" (secondary scale status).

## Score Summary

See the aggregation output (`aggregate.json`) for the final numbers; the table below is filled from it.

### Official Scores and EIC Assessment (from `aggregate.json`, `--venue iclr --final 4`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 66 | 72 | 70 | 68 | 58 | 66.8 | 66.5 | 14 |
| Clarity & Presentation | 62 | 66 | 68 | 60 | 60 | 63.2 | 62.8 | 8 |
| Novelty & Originality | 58 | 60 | 64 | 62 | 54 | 59.6 | 59.2 | 10 |
| Significance & Impact | 58 | 62 | 66 | 62 | 54 | 60.4 | 59.8 | 12 |
| Experimental Validation | 44 | 52 | 55 | 50 | 42 | 48.6 | 47.9 | 13 |
| Reproducibility | 50 | 55 | 58 | 56 | 48 | 53.4 | 52.9 | 10 |
| Ethical Compliance | 65 | 68 | 70 | 68 | 66 | 67.4 | 67.1 | 5 |
| **Composite** | 59.7 | 64.2 | 65.9 | 62.7 | 55.5 | **61.6 (before)** | **61.2 (after)** | |

Reviewer weights (confidence × EIC weight, share of the EIC assessment): R1 0.257, R2 0.205, R3 0.127, R4 0.205, DA 0.205. Official rating (plain mean) 3.60; EIC-weighted rating 3.54; composite band 4; no cross-check disagreement; no script warnings; DA ceiling none.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| ICLR rating for the final Overall 4 | 6 on {0,2,4,6,8,10} (6 on {1,3,5,6,8,10}); labels are secondary, not official wording |
| ICLR venue composite | 61.3 (band 4) |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling" to ICLR. Selecting k answers from N samples under an imperfect reward model is a timely problem, and the k-dependence you analyze is a real addition to coverage-based test-time theory.

**Overall Assessment:** The panel found the main proof sound and the matching lower bound well constructed. It also found that the abstract and the experiments claim more than the theory and the data show. The panel's view is mixed but leans toward acceptance, on the condition that claims are narrowed and the empirical section is strengthened.

**Key Strengths Identified by Reviewers:**
1. A new k-axis with matching upper and lower bounds and a correct core proof (R1, R2, R3).
2. A clear, minimal algorithm, and an honest Table 1 and Remark 4.3 (R2, R4).
3. A formal setting that connects to subset selection and to tasks with cheap verifiers (R3, R4).

**Key Concerns Requiring Attention:**
1. The optimal rule needs the unknown C*, and the α used in Section 7 has no stated selection protocol (CONSENSUS-3: R1, R3, DA).
2. The abstract claims BoN lacks the desirable k-scaling, which Table 1, Section 4.2 and Remark 4.3 do not support (CONSENSUS-3: R1, R4, DA).
3. The lower bounds are for graded rewards and 2k ≤ C*, not the binary Pass@k setting (CONSENSUS-3: R1, R2, DA).
4. Experiments: single run, no variance, no weighted-voting baseline, the monotonicity-verification claim overclaim (CONSENSUS-3).

**Decision: Borderline Accept (4).** The balance tips toward acceptance because the theory is correct and the new axis is of interest. The weaknesses are of the kind that can be addressed with revised wording and analyses on stored samples. A revision that fixes the Priority 1 items below would move the paper clearly to the accept side; leaving the abstract overclaim in place or leaving α unexplained would move it the other way.

Please refer to the Revision Roadmap below for prioritized guidance.

Sincerely,
Prof. Ingrid Valdsen
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Oracle α / α protocol unstated | R1, R3, DA | CONSENSUS-3 |
| Thin experiments, no variance, monotonicity-verification overclaim | R1, R4, DA | CONSENSUS-3 |
| Abstract overclaims BoN's k-scaling | R1, R4, DA | CONSENSUS-3 |
| Reward class / regime of the lower bound | R1, R2, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Significance of the result | R3, R4 (broad relevance) | R1, DA (limited by oracle α) | EIC: both are true; significance is moderate and depends on whether α can be set adaptively |
| Reward evaluations reduced by BoM | R3 (repeats the claim) | R1, DA (Algorithm 3 line 5) | EIC: Algorithm 3 queries all N; claim not supported as written |

### Score Spread Discussion
No dimension has a spread above 20 points (largest: Technical Rigor, 14). The lowest scores sit with R1 and the DA on Experimental Validation (44, 42); the EIC adopts that view, since the experiments cannot test the central claims.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Oracle α vs tuned α | Yes (R1, R3) | n/a | n/a |
| DA-M2 | MAJOR | BoN k-scaling overclaim | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Graded-reward class | Yes (R1, R2) | n/a | n/a |
| DA-M4 | MAJOR | Experiments monotonicity verification a worst-case property | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Frequency threshold not isolated | Partly (R1-W3) | n/a | n/a |
| DA-M6 | MAJOR | Scaling-monotonicity wording | No | EIC: partly a matter of reading; kept as a wording fix | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Abstract and Section 5 intro overclaim BoN's k-scaling | R1-ERR-1, R4-W2, DA-M2 | Abstract; Table 1; Section 4.2; Remark 4.3 | Rewrite: say that BoN is not scaling-monotonic and that its k-scaling is open | Low | Yes |
| R2 | α requires unknown C*; α selection protocol unstated | R1-W1, R3-W1, DA-M1 | Theorem 5.1; Section 7.1–7.2 | State that the guarantee is oracle-parameterized or give an adaptive rule; add α-sweep and validation-split protocol | Medium; no new generation | Yes |
| R3 | Lower-bound class and regime are not stated (graded rewards; 2k ≤ C*; δ ≤ 1) | R1-W4, R2-W2, DA-M3, DA-m3 | Section 3; Theorems 4.1, 4.2, 6.1; Section 6 | State the class and regime in the abstract and theorems; say binary is open or prove it | Low–Medium | Yes (wording); binary result is research |
| R4 | Experiments do not support monotonicity-verification claims; no variance | R1-W2, R4-W3, DA-M4 | Section 1; Section 7; Figures 1–3 | Replace monotonicity verification with "consistent with"; bootstrap intervals; regret-vs-k plot with √(1/k) reference | Low (stored samples) | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Missing baselines: reward-weighted voting, min-support BoN | R1-W3, DA-M5 | Add both on stored samples | Low | Yes |
| S2 | Algorithm 3 line 5 contradicts the efficiency claim | R1-ERR-2, DA-m1, R3-W3 | Move the reward query after the filter or drop the claim; report reward-call counts | Low | Yes |
| S3 | Differentiate from Huang et al. (2025); correct Brown et al. description; cite the pass@k source | R2-W1, R2-W3 | Delta table in the main text; cite Chen et al. 2021 | Low | Yes |
| S4 | Empirical Ĉ* and ε̂_RM; share of prompts with 2k ≤ C* | R1-Q2, R2-W4 | Estimate from π̂ and the reward model; stratify accuracy by difficulty | Low–Medium | Yes |
| S5 | Fill or remove Appendix C; add a Limitations section | R4-W3/W4, R1-Q4 | Provide content | Low | Yes |
| S6 | Constants and typos in Appendix B and (A.2) | R1-ERR-3/4, DA-m2 | Re-derive the Chernoff constants | Low | Yes |
| S7 | Scaling-monotonicity wording and "second term dominates" condition | DA-M6, R1-ERR-5 | Reword | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Unique-answer assumption; code-with-unit-tests experiment | R3-W2 | One experiment on a multiple-correct-answer task |
| N2 | Cost-versus-accuracy plot | R3-W3 | Total tokens plus reward calls |
| N3 | Lower-confidence-bound ranking as an alternative to a hard cut | R3-W4 | Discuss or test |
| N4 | Weighted voting with w(1/2)=0 not covered by Theorem 4.1 | R2-Q3, DA-m5 | Note in Theorem 4.1 |
| N5 | Helpful references (Math-Shepherd; Rashidinejad et al. `[verify]`) | R2 | Add if relevant |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 2–4 days (mostly rewriting plus analyses on stored samples; no new generation required).
- Priority 2: 7 items, roughly 3–5 days (baselines and α-sweep reuse stored samples).
- Priority 3: 5 items.
- **Total estimated revision time**: about 1–2 weeks of work for a careful revision.
