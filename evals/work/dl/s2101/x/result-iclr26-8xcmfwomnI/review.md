# Simulated Review: "Principled Out-of-Distribution Generalization via Simplicity"

Date: 2026-11-05 · Request: full review, target venue ICLR, skip confirmation, literature check strict (cutoff 2025-09-24).
Run notes: the five reviewer passes shared one model context and were done one after another (no subagents). Figures were not available; figure-dependent claims are judged from captions and text only (E9 not checked). The appendix was read in full for the experimental details (App. A–B) and the Theorem 4.1 proof structure (App. C.1, through Lemma C.3). For Theorem 4.2 (App. C.2) only the set-up, the constants and the places where Assumption C.3 is used were read, not every lemma. This is a simulation of how a careful panel would likely see this draft, not a prediction.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Principled Out-of-Distribution Generalization via Simplicity |
| Primary Discipline | Machine learning theory → statistical learning under covariate shift |
| Secondary Discipline(s) | Generative models (diffusion, compositional generalization); implicit/explicit regularization |
| Paper Type | Theoretical (composite weights: theoretical) |
| Core Technique(s) | Regularized MLE, non-asymptotic excess-risk bounds, Fisher-information geometry, toy MLP and small diffusion experiments |
| Target Venue | ICLR (stated); profile key `iclr` |
| Venue-Specific Notes | none |
| Paper Maturity | Submission-ready (full proofs in appendix; short conclusion with an explicit limitation discussion) |
| Ethics-Relevant Content | none (synthetic data only) |
| Integrity scan | `integrity_scan.py`: "No reviewer-directed text or hidden characters found." No injected instructions seen while reading. |

### Claimed Contributions (as stated by the authors, §1)
- **C1** Simplicity, "measured by a well-defined complexity metric", is a reliable indicator of OOD generalization; grounded in "a carefully designed experiment" on diffusion models (§1, §3).
- **C2** Constant-gap regime: regularized MLE recovers the true model at excess-risk rate Õ(1/n) (Thm 4.1, §4.2).
- **C3** Vanishing-gap regime: rate Õ(n^{-1+2/(3τ)}), approaching Õ(1/n) as τ→∞ (Thm 4.2, §4.3).
- Framing claim (abstract, §1, §5): the results give "a principled explanation for how modern foundation models can perform robustly outside their training distribution", with "the first sharp sample complexity guarantees".

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Diffusion (§3.1, App. A): 28×28 circles, 3 binary attributes, 4 of 8 classes for training, 200,000 images (50,000 per class), text-conditioned U-Net, Adam lr 1e-4, batch 64, 400 epochs, 500 denoising steps; evaluation on 2,000 images per held-out class (App. A.1, A.3). Number of diffusion runs: not stated. MLP (§3.2, App. B): 2-layer ReLU MLP, hidden 128, Adam lr 5×10⁻⁵, "40, 000 training epochs" (B.1), 100 samples per source class (400 total), 20 test samples per target class; 10 independent runs per trial; 80 uniform-map trials, 20 permutation-map trials, 1 flipped map + 10 interpolations. Compute: A6000 GPU / 8-CPU PC, "a few hours" (A.4, B.6).
- **Protocol sweep.** No hyper-parameter selection, validation split or checkpoint selection is described anywhere (searched: test set, validation, held-out, selected, tuned, hyperparameter). Learning rate and epochs are stated as fixed. No test-set selection issue exists. Code availability: not stated after search.
- **Headline numbers.** Rates Õ(1/n) (Thm 4.1), Õ(n^{-1+2/(3τ)}) (Thm 4.2, requires τ ≥ 9 in Assumption C.3). Empirical: Fig 2 (norms), Fig 3 (diffusion losses), Fig 4 (identity-MLP losses: train 6.02663e-4; test 3.60000e-3, 9.82313e-3, 5.24610e-3, 1.55543e-2).
- **Appendix content.** A: diffusion details; B: MLP details; C: proofs of Thm 4.1 and 4.2 (thresholds N*, N′ in (22) and (41)).
- **Unverifiable.** All figures (1, 2, 3, 4, 5, 6, 7) are unavailable; the garbled formula layout in Thm 4.1/4.2 and A.1 is an extraction artifact and is read from the surrounding text.

### Literature check (strict, cutoff 2025-09-24)
Run with `related_search.py` (arXiv API; reviewer never searched for the paper itself). 4 queries kept in the ledger by purpose: claim C1 ×2 ("simplicity bias generalization theory", "diffusion compositional generalization theory"), claim C2 ×1 ("covariate shift maximum likelihood"), expansion ×1 (one query refused for 5 concept words, not counted). No external benchmark exists (theory paper), so no baseline scout. `similarity`: closest prior work = Ge et al. 2023 (cosine 0.267, cited and differentiated by the paper), then Swing-by Dynamics (0.235, cited), then a spectral-bias paper (0.164); **no text overlap** (0 shared 8-grams). `novelty`: C1 medium (top prior: Shah et al. 2020, level 3, not cited), C2 medium (Ge et al., level 3, cited); reading "no central claim fully covered by prior work". Gaps left open: the arXiv-only search is thin for statistics-journal literature (covariate shift, Tikhonov-type selection); noted as a limit, not as evidence of novelty. One result (a concurrent 2025-09-19 preprint on local mechanisms of compositional generalization in conditional diffusion) is "worth discussing" only and plays no role in any score.

## Review Team (fictional personas)

### EIC (meta-reviewer): Helena Okonkwo-Reyes, public research university (Europe)
- **Seniority / Expertise**: Senior faculty / statistical learning theory, distribution shift
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Area chair who reads the assumptions before the theorem

### Reviewer 1 (Methodology): Kwabena Aryeetey-Lund, statistics department, large university (North America)
- **Seniority / Expertise**: Mid-career / M-estimation, non-asymptotic risk bounds, proof techniques
- **Review Focus**: Assumptions, proof correctness, fairness of the empirical test of the hypothesis
- **Style**: Reads proofs line by line; checks every assumption against the paper's own examples

### Reviewer 2 (Domain): Mei-Lin Draycott, ML theory group (East Asia)
- **Seniority / Expertise**: Senior faculty / generalization theory, implicit bias, covariate shift
- **Style**: Positions each theorem against the closest known bound

### Reviewer 3 (Perspective): Soledad Marchetti-Ibarra, computational neuroscience institute (Latin America)
- **Seniority / Expertise**: Mid-career / Occam-type priors, compositional generalization in brains and models
- **Style**: Constructive, looks for connections, most positive voice on the panel

### Reviewer 4 (Generalist): Piotr Hallgrimsson, industrial research lab (Europe)
- **Seniority / Expertise**: Senior industry scientist / generative models, representation learning
- **Style**: Typical program-committee member; asks whether the abstract matches the content

### Devil's Advocate: Oluwaseun Brandvold, evaluation-methodology group (Africa/Europe)
- **Seniority / Expertise**: Mid-career / causal inference, evaluation methodology
- **Style**: Rigorous, never hostile; steelmans first

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Reports

# Peer Review Report
## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Reviewer: Kwabena Aryeetey-Lund, Reviewer 1 / Methodology (statistics department, North America; fictional persona)
## Expertise: M-estimation and non-asymptotic risk bounds; proof techniques for regularized estimators
## Date: 2026-11-05

## Summary
The paper posits that, among all source-domain minimizers, the model that generalizes under covariate shift is the one minimizing a convex, smooth "simplicity" function R. A 2-layer MLP toy (§3.2) is used to argue that "generalizable" models have smaller weight norm than hand-built "non-generalizable" ones. Under a well-specified parametric model, the paper then bounds the excess risk of the regularized MLE with λR(β) added: Õ(1/n) when the true model is separated from all other source minimizers by a constant simplicity gap (Thm 4.1), and Õ(n^{-1+2/(3τ)}) when near-minimal R implies parameter proximity (Thm 4.2).

## Strengths
### S1: A clean, readable non-asymptotic bound for non-unique source minimizers
Thm 4.1 explicitly decomposes the excess risk into the Ge et al. term Tr(I_T I_S⁻¹)/n and a regularization term scaling as 1/∆² (§4.2). I followed the proof structure in App. C.1 (Prop. C.1, Lemma C.2, Lemma C.3): the localization argument (global minimizers vs. spurious local minima via A.3, then the gap ∆ via convexity of R) is coherent.
### S2: Honest limitation discussion
The Conclusion states that the −β* symmetry violates Assumption C.3 and defers the quotient-space extension: "We leave a formal development of this extension to future work." This is the right kind of candor.
### S3: Sufficient experimental detail for the toy
App. B gives architecture, optimizer, trial counts (80/20/1+10 trials, 10 runs each) and compute, so the MLP experiment is rerunnable in principle.

## Weaknesses
### W1: Assumption C.3 with τ ≥ 9 is incompatible with a positive-dimensional solution set, so Thm 4.2 has no non-trivial instance (error ERR-1)
Assumption C.1 makes B_S a compact C¹ manifold of dimension d_S, C.2 allows d_S ≥ 1, and A.4(3) makes R L-smooth with R(0)=0 and R ≥ 0 (hence ∇R(0)=0 and ‖∇R(β)‖ ≤ L‖β‖). For β0 ∈ B_S at distance δ = ‖β0−β*‖, this gives ∆ = R(β0)−R(β*) ≤ L(B_S δ + δ²/2) ≤ L′δ. C.3 requires δ ≤ ∆^τ ≤ (L′δ)^τ, i.e. δ^{τ−1} ≥ L′^{-τ}, which is false for small δ when τ ≥ 9 (τ > 1 suffices). If d_S ≥ 1 there are points of B_S arbitrarily close to β*, so C.3 fails; and if B_S is zero-dimensional, Thm 4.2 collapses to the constant-gap setting of Thm 4.1 with a worse rate. The proof really uses C.3 at small ∆ (App. C.2, Case 2: "By Assumption C.3, we have ‖β0 − β*‖ ≤ n^{-ϵτ}"). If β* is the minimizer of R on a smooth manifold, the tangential gradient vanishes and ∆ ~ δ², so one would need τ ≤ 1/2, where the stated rate n^{-1+2/(3τ)} does not decay. The regime that motivates §4.3 ("they may form a continuum, such as a low-dimensional surface") is therefore excluded by the theorem's own hypotheses.
- **Suggested Fix**: State and prove the vanishing-gap result for a condition that can hold on a continuum (e.g., ‖β0−β*‖ ≤ c·∆^{τ} with τ ≤ 1/2 under local quadratic growth, and re-derive the rate), or give a concrete example with d_S ≥ 1 and τ ≥ 9 satisfying C.1–C.3. Effort: High (re-derivation of the C.2 proofs).
### W2: The empirical comparison in §3.2 does not test the simplicity hypothesis (E4)
"Each such model is trained on 400 identity samples from S, along with 400 modified samples from T." The "non-generalizable" networks therefore see target-domain inputs with deliberately corrupted labels (800 vs. 400 samples), whereas the "generalizable" one is trained on S only. A larger weight norm for a function that must additionally map T to shifted/permuted/flipped outputs (Fig 2a–c) is the expected outcome and does not show that, among functions fitting S only, the true one has the smallest norm. The hypothesis "β* = argmin R over B_S" is never tested; no model fit on S alone with a competing, non-identity extension on T is constructed. The diffusion model of §3.1 is not measured for simplicity at all.
- **Suggested Fix**: Compare, at matched training sets, source-only models that extrapolate differently (e.g., different initializations/seeds, weight decay on/off) and report norm vs. target error across them; measure the norm of the diffusion model for source-only vs. a source+corrupted-target variant. Effort: Low–Medium (≈ a few CPU-hours for the MLP).
### W3: Several assumptions exclude the paper's own examples (E3)
B.1 (positive-definite Hessian at every source minimizer) and B.2 (∆ > 0) fail for any MLP with hidden-unit permutation symmetry, since permuted copies have identical loss and R: this affects the 2-layer MLP of §3.2 and the U-Net of §3.1. The paper's discussion of equivalence classes concedes this for −β*. A.1 as written needs |ℓ_n(β) − E ℓ_n(β)| ≤ B0 √(log n/n) uniformly over all β ∈ ℝ^d with B0 independent of β; the remark says this is "commonly satisfied when the loss function, its gradient, and its Hessian are uniformly bounded", but squared-error/Gaussian NLL (App. B.1 uses MSE) is unbounded in β (ERR-2, medium confidence).
- **Suggested Fix**: State a reduced example (e.g., a linear or small-nonlinear model without symmetries) where A.1–A.4, B/C are verified, and say clearly that the MLP/diffusion setting is outside the theory until the quotient extension is proved. Effort: Medium.
### W4: λ in Thms 4.1/4.2 depends on unknown quantities, and optimization is assumed away
λ = 8B0/∆·√(log n/n) (Thm 4.1) requires the unknown gap ∆ and constant B0; β̂_λ is a global minimizer of a non-convex objective (Eq. 1). No data-driven choice of λ or computational guarantee is discussed, so "sample complexity" is not an algorithmic guarantee, and the burn-in N* is a polynomial in ∆⁻¹, α⁻¹, G⁻¹, … (§4.2) that is never evaluated, so the "fast rate" may only apply for impractically large n.
- **Suggested Fix**: Give an adaptive/validation-based λ or state the oracle nature explicitly; evaluate N* on the toy to show the regime of validity. Effort: Medium.
### W5: "Sharp" is supported only for the n-dependence of the constant-gap bound (E5)
The paper's justification is "this rate is minimax optimal, meaning that our bound is tight in the worst case" (§4.2), which follows from the Ge et al. lower bound on the ∆=∞ subclass. No lower bound exists for the ∆⁻² dependence or for the vanishing-gap exponent −1+2/(3τ), so "the first sharp sample complexity guarantees" (abstract) is overstated for both regimes jointly.
- **Suggested Fix**: Say "rate-optimal in n for the constant-gap regime" and drop "sharp" for the rest, or add a lower bound. Effort: Low.

**Minor:** the intro states the vanishing-gap condition "for some τ > 0" while C.3 requires τ ≥ 9 (ERR-3); Fig 4 caption says "after all 20, 000 epochs" while B.1 says "40, 000 training epochs" (ERR-4); the permutation map is "randomly assigned to a different center" (§3.2) while App. B.4 draws r_j ∼ U({0,1}³), which can equal t (ERR-5); no code-availability statement.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E3 | Assumption C.3 vs C.1, C.2, A.4(3); App. C.2 Case 2 | "There exists τ ≥ 9 and ∆max < 1 such that for all ∆ ≤ ∆max" | With L-smooth R, ∆ ≤ L′δ, so δ ≤ ∆^τ cannot hold for small δ; B_S with d_S ≥ 1 contains such points | Derived by hand from A.4 and C.1; used at small ∆ in proof | High | MAJOR (DA: CRITICAL) | See W1 |
| ERR-2 | E3 | Assumption A.1 and its remark | "commonly satisfied when the loss function, its gradient, and its Hessian are uniformly bounded" | Uniform-in-β ℝ^d bound with β-independent B0 fails for unbounded (squared/Gaussian-NLL) losses | Derived; interpretation-dependent | Medium | MAJOR | See W3 |
| ERR-3 | E6 | §1 vs Assumption C.3 | "for some τ > 0" | Theorem needs τ ≥ 9; for τ ≤ 2/3 the stated rate does not decay | Cross-referenced (§1, §4.3, C.3) | High | MAJOR | State τ ≥ 9 in the contribution |
| ERR-4 | E6 | Fig 4 caption vs App. B.1 | "The final test losses after all 20, 000 epochs" | B.1 states 40,000 epochs for all experiments | Cross-referenced | High | MINOR | Fix |
| ERR-5 | E6 | §3.2 vs App. B.4 | "randomly assigned to a different center" | U({0,1}³) can return t itself | Cross-referenced | Medium | MINOR | Fix |

### Claim-to-evidence map (compressed)
| ID | Claim | Evidence | Verdict |
|----|-------|----------|---------|
| C1 | Simplicity drives OOD generalization | §3.1 (qualitative, Fig 1b), §3.2/Fig 2 (confounded), no test of argmin-R hypothesis | Partially / weakly supported |
| C2 | Õ(1/n) rate, constant gap | Thm 4.1, App. C.1 (proof structure checked) | Supported under strong assumptions |
| C3 | Õ(n^{-1+2/(3τ)}), vanishing gap | Thm 4.2; assumption set contradictory for d_S ≥ 1 | Unsupported as stated |
| Framing | Explains foundation models | §1.1 states the scope is "covariate shift in the underparameterized regime" | Not supported |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Thm 4.1 plausible; Thm 4.2 hypotheses inconsistent; experiments confounded |
| Clarity | 3 | Well organized, intuition after each theorem |
| Significance | 2 | Hypothesis assumed, link to practice not shown |
| Originality | 2 | Extension of the Ge et al. analysis to non-unique minimizers |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a sound constant-gap theorem, but a vacuous second theorem and an experiment that cannot test the hypothesis, in a paper framed far beyond its scope.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | ERR-1, ERR-2, assumption set excludes NNs |
| Clarity & Presentation | 68 | Competent | Clear exposition; τ and epoch inconsistencies |
| Novelty & Originality | 52 | Developing | Incremental over Ge et al. (2023) |
| Significance & Impact | 46 | Developing | Principle assumed rather than shown |
| Experimental Validation | 36 | Developing | Confounded toy (W2); no quantitative diffusion measure |
| Reproducibility | 58 | Competent | Details in App. A–B; no code statement |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations partly discussed |

## Questions for Authors
1. Can you exhibit an example with d_S ≥ 1 satisfying C.1–C.3 with τ ≥ 9? A concrete one would raise my score; an admission that C.3 needs revising would keep it low.
2. In Fig 2, what are the norms of source-only MLPs trained with different seeds or initializations that extrapolate differently on T?
3. Is A.1 verified for any model in the paper (even the linear one)?

## Limitations Assessment
**Partially.** The symmetry limitation is acknowledged; the underparameterized/strong-convexity scope and the oracle λ are not carried into the abstract.

## Ethics Review Flag
**No**: synthetic data only.

## Overall Score
**3**: Borderline Reject. Thm 4.1 is a legitimate but modest extension; Thm 4.2 and the empirical support do not hold up.

## Confidence
**4**: Confident; I rechecked the C.3 argument by hand, and read App. C.1 but not every lemma of C.2.

---

# Peer Review Report
## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Reviewer: Mei-Lin Draycott, Reviewer 2 / Domain (ML theory group, East Asia; fictional persona)
## Expertise: generalization theory, implicit bias, covariate shift
## Date: 2026-11-05

## Summary
The authors study a stylized version of compositional generalization: a parametric model whose source-domain risk has many minimizers, only one of which (β*) is also correct on the target, and which they assume has minimal R. They show that regularizing the MLE with R recovers β* in excess risk, at the optimal 1/n rate under a constant gap, and at a slower rate when the gap vanishes smoothly. They motivate this with a text-conditioned diffusion model and a toy MLP.

## Strengths
### S1: Relevant and well-motivated question
Why over-expressive models extrapolate in the "human-expected" way is a central question; the circles dataset (§3.1, App. A.1) is an appropriate sandbox, following Okawa et al. (2023).
### S2: Correct and fair positioning against the closest bound
§1.1 identifies Ge et al. (2023) as the key prior result ("their analysis assumes a unique global minimizer") and correctly shows that Thm 4.1 reduces to their Thm 3.1 when ∆ = ∞ (§4.2).
### S3: Transparent about scope in the covariate-shift literature
The paper separates the underparameterized setting from overparameterized and non-parametric work (§1.1), which keeps the technical claims honest even though the abstract does not.

## Weaknesses
### W1: The "simplicity principle" is neither new nor shown to be the explanation
That small-norm solutions generalize is the premise of weight decay and of the implicit-bias literature. The paper assumes "We posit that this true parameter corresponds to the" simplest source minimizer (§4.1); the theorem is then a statement that regularization finds an assumed argmin-R point. The uncited literature argues both for and against such a principle: Valle-Pérez et al. (simplicity bias of the parameter-function map), Shah et al. (simplicity bias can *hurt* robustness/OOD behaviour), Abbe et al. (min-degree interpolators for generalization on the unseen). The paper must say what is gained over these, especially the negative evidence.
- **Suggested Fix**: Add a "simplicity and OOD" paragraph with these works; state which part of the argument is new (the finite-sample rate with non-unique minimizers).
### W2: Incremental theory over Ge et al. (2023)
Thm 4.1 adds a regularizer, a gap ∆ and a bias term to the Ge et al. analysis; the first term is theirs. This is a worthwhile but incremental extension (literature check: C2 "medium", closest prior Ge et al. at coverage level 3). The "vanishing-gap" extension is where novelty would lie, but see R1-W1 (assumption C.3 appears unsatisfiable for continua); I could not find an example in the paper that satisfies it with d_S ≥ 1.
- **Suggested Fix**: Provide the worked example and compare the resulting rates with the known min-norm interpolation results under covariate shift the paper already cites (Mallinar et al., 2024).
### W3: Scope vs. claims
The abstract opens with foundation-model OOD generalization and the conclusion states the results "provide a principled explanation for how modern foundation models can perform robustly outside their training distribution", whereas §1.1 states the focus is "covariate shift in the underparameterized regime" and the theory needs strong-convexity at the minimizers (B.1/C.2). Foundation models are heavily overparameterized.
- **Suggested Fix**: Retitle/reword: "a theory of simplicity-based selection among source minimizers under covariate shift".
### W4: Citation hygiene (E7)
The text cites "Saharia et al., 2022" for text-to-image generation from novel attribute combinations (§1), while the bibliography entry is "Image super-resolution via iterative refinement". Dhariwal & Nichol (2021a/b) and Ho et al. (2020a/b) appear twice (medium confidence on the first; the duplicates are certain).

## Missing References (all verified with `related_search.py verify` unless noted)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Shah, Tamuly, Raghunathan, Jain, Netrapalli. *The Pitfalls of Simplicity Bias in Neural Networks.* NeurIPS 2020 (arxiv.org/abs/2006.07710) | Peer-reviewed, prior; argues simplicity bias can harm robustness/OOD behaviour, directly relevant to C1 |
| Important | Valle-Pérez, Camargo, Louis. *Deep learning generalizes because the parameter-function map is biased towards simple functions.* ICLR 2019 (arxiv.org/abs/1805.08522) | Canonical simplicity-explains-generalization account |
| Important | Abbe, Bengio, Lotfi, Rizk. *Generalization on the Unseen, Logic Reasoning and Degree Curriculum.* ICML 2023 (arxiv.org/abs/2301.13105) | Min-degree interpolator as the selected solution on the unseen domain |
| Important | Liang et al. *How Diffusion Models Learn to Factorize and Compose.* NeurIPS 2024 (found in the search) | Compositional generalization of diffusion models on synthetic data |
| Helpful | Soudry, Hoffer, Nacson, Gunasekar, Srebro. *The Implicit Bias of Gradient Descent on Separable Data.* JMLR 2018 (arxiv.org/abs/1710.10345) | Optimization-driven selection among interpolators |

Novelty delta (closest prior work): Ge et al. 2023 does well-specified covariate shift with a unique source minimizer and proves minimax-optimal MLE; this paper adds non-unique minimizers selected by a convex smooth R; cited and differentiated. No work covering all central claims was found.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Hypotheses of Thm 4.2 doubtful (see R1) |
| Clarity | 3 | Clear |
| Significance | 2 | Principle assumed, limited applicability |
| Originality | 2 | Medium novelty per claim-level profile |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: incremental theory over one prior bound, with the novelty-bearing second regime in doubt.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Proof structure of Thm 4.1 is sound; scope assumptions strong |
| Clarity & Presentation | 70 | Competent | Clean writing |
| Novelty & Originality | 52 | Developing | Medium novelty per claim, incremental over Ge et al. |
| Significance & Impact | 48 | Developing | Limited to strongly convex, low-dimensional setting |
| Experimental Validation | 38 | Developing | Illustrative only |
| Reproducibility | 62 | Competent | Details in appendix |
| Ethical Compliance | 66 | Competent | n/a |

## Questions for Authors
1. What does Thm 4.1 show about *which* R is right? In the paper R is given; how would the result change if R were misspecified (e.g., ℓ₁ instead of ℓ₂²)?
2. How do your conditions relate to Shah et al.'s setting where simplicity bias causes OOD failure?
3. Does Thm 4.1 reduce to known Tikhonov/min-norm selection results when the model is linear?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**.

## Overall Score
**3**: Borderline Reject. Incremental theoretical contribution with an overclaimed framing and missing positioning against the simplicity-bias literature.

## Confidence
**3**: Fairly confident; I did not check the proofs in detail.

---

# Peer Review Report
## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Reviewer: Soledad Marchetti-Ibarra, Reviewer 3 / Perspective (computational neuroscience institute, Latin America; fictional persona)
## Expertise: Occam-type priors and compositional generalization in brains and models
## Date: 2026-11-05

## Summary
This is an interesting attempt to give a statistical-learning account of why models extrapolate compositionally: among the many solutions consistent with training data, the one a human would expect is the simplest. The paper shows this with a diffusion model on a clean synthetic dataset, a small MLP in which norms of "good" and "bad" extensions differ, and two theorems on regularized MLE.

## Strengths
### S1: A crisp conceptual story that connects to Occam / minimum-description-length thinking
The "simplest consistent with data" idea (abstract; §4.1) echoes Bayesian Occam priors in cognitive science, and the paper turns it into a testable estimator (Eq. 1).
### S2: A well-chosen controllable testbed
The 3-bit circles dataset (§3.1) lets compositional generalization be isolated, and the held-out combinations in T are sharply defined. Fig 1b is described as showing "high-quality, semantically accurate images for all target classes" (caption-level judgment only; figure unavailable).
### S3: A graded family of counter-examples
Uniform, permutation and flipped/interpolated maps (§3.2) give a continuum from "true" to "wrong" extensions, which is the right structure for a dose–response test.

## Weaknesses
### W1: The empirical link between the diffusion observation and the theory is thin
The diffusion results (§3.1, Fig 3) report loss curves and a qualitative figure; there is no simplicity measurement for the diffusion model, and generalization is judged by eye. The bridge is the MLP toy, which the theory itself (strong convexity, no symmetries) does not cover. A neuroscience-style analysis would ask for a *dose–response relation*: does complexity predict target error across many source-only models, rather than across models given different target labels?
- **Suggested Fix**: Train many source-only networks (seeds, widths, weight decay) on the circles data and plot target error against a complexity proxy; add a quantitative attribute classifier on generated images.
### W2: Assumption audit: who supplies R, and why would the human-aligned model be minimal in it?
The central assumption β* = argmin R over B_S (§1, §4.1) imports the human notion of "expected" into R. Human-expected compositionality is plausibly a statement about *structure* (factorization), not norm; norms are architecture-dependent, and many functions are simple under different metrics. The paper offers weight norm and says "other valid examples include the squared group ℓ2,1 norm", but gives no way to tell which R applies in a given domain.
- **Suggested Fix**: Discuss factorized/structural simplicity and show, in the toy, a case where ℓ₂ norm picks the wrong extension.
### W3: Scale and deployment
The theory holds for fixed d, n→∞ with Hessians bounded below at all source minimizers; the paper does not discuss when this approximates large models. No broader-impact issues arise (synthetic data), but the foundation-model framing in the conclusion should be softened.
- **Suggested Fix**: Add a short "scope" paragraph.

**Minor:** typos ("minimizes" for "minimizers", §4.1; "chadrasekaran" in the Bubeck entry).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Careful theorem 4.1, toy experiments illustrate the story |
| Clarity | 3 | Clear |
| Significance | 3 | Principle is attractive; link to practice is future work |
| Originality | 3 | Framing and extension are fresh enough |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: a clear conceptual framing with a rigorous first theorem and honest limitations; weaknesses are of the ordinary kind (thin experiments, scope).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Theorem and proof structure appear careful |
| Clarity & Presentation | 72 | Competent | Intuition after each theorem |
| Novelty & Originality | 62 | Competent | Fresh framing |
| Significance & Impact | 62 | Competent | Could shape how people think about OOD |
| Experimental Validation | 50 | Developing | Illustrative only |
| Reproducibility | 62 | Competent | Appendix detail |
| Ethical Compliance | 70 | Competent | Limitations honestly discussed |

## Questions for Authors
1. Would the same norm ordering hold for a network trained on a *different* factorization of the 8 classes (e.g., a different choice of S)? A negative answer would lower my score.
2. How do you see the quotient-space extension handling hidden-unit permutations?
3. Is there any evidence the diffusion model's weights are smaller in the generalizing run?

## Limitations Assessment
**Yes, partially**: the equivalence-class discussion is welcome; scope limitations could go earlier.

## Ethics Review Flag
**No**.

## Overall Score
**4**: Borderline Accept. A clear framing and a solid first theorem outweigh the thin empirical link, in my reading.

## Confidence
**3**: Fairly confident; I did not examine the proofs.

---

# Peer Review Report
## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Reviewer: Piotr Hallgrimsson, Reviewer 4 / Generalist (industrial research lab, Europe; fictional persona)
## Expertise: generative models, representation learning
## Date: 2026-11-05

## Summary
The paper argues that out-of-distribution generalization can be understood as selecting the simplest model among those that fit the training data, and proves finite-sample excess-risk bounds for a regularized maximum-likelihood estimator in two regimes (constant and vanishing simplicity gap). The motivation comes from a diffusion model and an MLP toy.

## Strengths
### S1: Clear contribution statement and good organization
The two contributions are stated up front (§1), the theorem statements are followed by plain-language readings (§4.2, §4.3), and the proofs are in a well-organized appendix.
### S2: Honest limitation section
The Conclusion's equivalence-class discussion is a real limitation, openly flagged.
### S3: Fits ICLR's theory/foundations track
A learning-theory result about generalization under distribution shift is within scope for ICLR; the question is the size of the advance.

## Weaknesses
### W1: Title and abstract promise more than the paper delivers
"Principled Out-of-Distribution Generalization via Simplicity" and "Modern foundation models exhibit remarkable out-of-distribution (OOD) generalization" frame a result about a low-dimensional, well-specified, strongly convex-at-minimizers parametric model under covariate shift. A reader from the foundation-model community would expect a result about large networks. Also "the first sharp sample complexity guarantees" needs qualification (R1-W5).
- **Suggested Fix**: Retitle and rewrite the abstract's first and last sentences to match §1.1's scope.
### W2: The empirical section is a narrative, not a test
Fig 2 shows weight norms for models trained on different labelings; Fig 1b shows a generated image grid. Neither quantifies "generalization" (§3.1 says the model "generates high-quality, semantically accurate images" by inspection) and §3.2 says an MLP "reliably generalizes", while App. Fig 4 reports test MSE of 3.6e-3 to 1.55e-2 against a training MSE of 6.03e-4 (derived ratios ≈ 6× to ≈ 26×) with no threshold defining "generalizes".
- **Suggested Fix**: Define a generalization criterion (target MSE vs. a reference noise floor) and show distributions over runs for the generalizable model as well as the others.
### W3: Related work reads as a list in places
§1.1 lists many LLM papers for "compositional generalization" but does not engage with the simplicity-bias literature the paper's own thesis relies on (see R2).
- **Suggested Fix**: Trim the LLM list and add the simplicity-bias and min-norm-selection lines of work.

**Minor:** duplicated bibliography entries (Dhariwal & Nichol 2021a/b; Ho et al. 2020a/b); "minimizes" typo in §4.1; the Fig 4 caption/B.1 epoch inconsistency.

## Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly | Thm 4.1 yes; Thm 4.2 unclear; §3 weak |
| Presentation | Met | §4 |
| Contribution significant to community | Partly | §1, §5 |
| Reproducibility | Partly | App. A–B; no code statement |
| Honest limitations | Met | §5 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Experiments don't test the claim; assumptions strong |
| Clarity | 3 | Well written |
| Significance | 2 | Scope narrower than framing |
| Originality | 2 | Moderate novelty |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: clear writing and a real theorem, but a claim/scope mismatch and illustrative-only experiments, typical of rejected submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Theory plausible; scope limited |
| Clarity & Presentation | 74 | Competent | Good structure |
| Novelty & Originality | 52 | Developing | Incremental |
| Significance & Impact | 52 | Developing | Limited reach |
| Experimental Validation | 40 | Developing | Illustrative |
| Reproducibility | 60 | Competent | Details present |
| Ethical Compliance | 68 | Competent | n/a |

## Questions for Authors
1. Would you accept a title that names the setting (covariate shift, well-specified, low dimension)? Yes would raise my score.
2. What is the quantitative generalization criterion for Fig 1b?
3. What would a falsification of your principle look like in the MLP?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**.

## Overall Score
**3**: Borderline Reject. Useful but modest theory and an overclaimed frame; I'd welcome a re-scoped version.

## Confidence
**3**.

---

# Devil's Advocate Report
## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Reviewer: Oluwaseun Brandvold, evaluation-methodology group (fictional persona)

## Steelman
Over-expressive models fit the source domain in many ways, and only some extrapolate sensibly. If the sensible extension is the minimum of a convex smooth complexity measure among source minimizers, then a regularized MLE recovers it at near-parametric rates, even when source minimizers are non-unique; this extends Ge et al.'s clean covariate-shift analysis and gives a formal home to the intuition behind weight decay.

## Core Argument Chain
1. P1: Diffusion models generalize compositionally on a 3-attribute synthetic task (§3.1).
2. P2: In an MLP abstraction, "generalizable" solutions have smaller weight norm than "non-generalizable" ones (§3.2, Fig 2).
3. P3: Therefore the true model is the simplest among source minimizers (assumption, §4.1).
4. P4: Under assumptions A–C, regularized MLE recovers it at Õ(1/n) / Õ(n^{-1+2/(3τ)}) (Thm 4.1/4.2).
∴ Simplicity "provides a principled explanation" for foundation-model OOD generalization.

## Strongest Counter-Argument
The argument has a gap at each link. P1 → P2: the diffusion model is never measured for simplicity, and the MLP "non-generalizable" models are trained on 800 samples *including labelled target points* (§3.2), so a larger norm is just the cost of fitting extra, more complicated labels; it says nothing about which solution a source-only learner selects. P2 → P3: the simplicity hypothesis is an assumption in the theory, not a finding, and the paper never constructs a source-fitting model that is simpler than the truth but wrong. P3 → P4: the vanishing-gap theorem requires τ ≥ 9 in Assumption C.3, but with R smooth (A.4(3)) and B_S a manifold of positive dimension (C.1, C.2) the condition ‖β0−β*‖ ≤ ∆^τ cannot hold for β0 near β*, because ∆ ≤ L′‖β0−β*‖; so the only non-vacuous case of Thm 4.2 is the isolated-minimizer case already covered by Thm 4.1. The remaining theorem (4.1) needs a known R, an oracle λ ∝ B0/∆, global optimization of a non-convex objective, strong convexity at every source minimizer, and a uniform concentration bound over all of ℝ^d (A.1). Neural networks violate B.1/B.2 through hidden-unit permutation symmetry, which the Conclusion concedes for −β*. P4 → conclusion: the explanation of "foundation models" is a leap across overparameterization, optimization and the choice of R. Each step may be repairable, but together the paper delivers a modest extension of a known bound dressed as an explanation of foundation-model generalization.

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Logic/Evidence | Assumption C.3 with C.1, C.2, A.4(3); Thm 4.2; App. C.2 Case 2 | C.3 ("There exists τ ≥ 9 and ∆max < 1 such that for all ∆ ≤ ∆max …") together with L-smoothness of R implies δ^{τ−1} ≥ L′^{-τ} for every β0 ∈ B_S at distance δ from β*, so no point of B_S can lie within a fixed distance of β*; hence for d_S ≥ 1 the hypotheses of Thm 4.2 are unsatisfiable, and for d_S = 0 Thm 4.2 only restates Thm 4.1 with a slower rate. Contribution 2(b) and the "vanishing-gap regime" narrative of the abstract have no non-trivial instance. This is a failure of the theorem's hypotheses to describe the regime it claims (evidence contradicts claim C3), re-derived by me from the paper's text; it also appears as R1 ERR-1. | State and prove the vanishing-gap theorem under a hypothesis that can hold on a continuum (e.g., a local quadratic-growth condition with τ ≤ 1/2) with re-derived rates, or give a concrete example with d_S ≥ 1 and τ ≥ 9 | New analysis/redesign of Assumption C.3 and re-proof of the rates |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §3.2 "Non-generalizable Alternatives", Fig 2 | Norm comparison confounded: "trained on 400 identity samples from S, along with 400 modified samples from T" vs. source-only for the generalizable model; the hypothesis argmin-R is not tested | Matched source-only comparison (see R1-W2) |
| DA-M2 | Scope/Overclaim (E5) | Abstract, §5 | "a principled explanation for how modern foundation models can perform robustly outside their training distribution" vs. §1.1 scope "covariate shift in the underparameterized regime"; "first sharp" supported only for the n-rate of constant gap (§4.2) | Narrow wording |
| DA-M3 | Assumptions | A.1, B.1, B.2, C.2; §5 equivalence classes | Symmetries make B.2 (∆>0) and B.1 fail for the paper's own MLP/U-Net; deferred to "future work" | Verified example; scope statement |
| DA-M4 | Practicality | Thm 4.1 λ; Eq. (1) | λ depends on unknown ∆ and B0; global minimizer of non-convex objective assumed | Adaptive λ; discuss optimization |
| DA-M5 | Evidence | §3.1, Fig 1b, Fig 3 | Diffusion generalization is shown by a qualitative figure and losses; simplicity of the diffusion model is never measured; number of runs not stated | Quantitative metric and several seeds |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Fig 4 caption vs App. B.1 | "20, 000 epochs" vs "40, 000 training epochs" |
| DA-m2 | Consistency | §1 vs C.3 | "for some τ > 0" vs τ ≥ 9 |
| DA-m3 | Citation | §1, bibliography | "Saharia et al., 2022" entry is the super-resolution paper; duplicated Dhariwal–Nichol and Ho entries |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Training set size, diffusion | 200,000 (50,000 per class × 4) | 4 × 50,000 = 200,000 | Yes |
| MLP training size | 400 (100 × 4) | 400 | Yes |
| Non-generalizable training size | 400 + 400 | 800 | Yes (confound) |
| Rate at τ = 9 | n^{-1+2/(3τ)} | exponent = −1 + 2/27 ≈ −0.926 | Derived |
| Test/train MSE, identity MLP (Fig 4) | train 6.02663e-4; test 3.60000e-3 … 1.55543e-2 | ratios ≈ 6.0 and ≈ 25.8 | Derived; "reliably generalizes" has no threshold |
| Epoch count | 40, 000 (B.1) | 20, 000 in Fig 4 caption | No |

## Ignored Alternative Explanations
- Larger norm of "non-generalizable" MLPs is explained by fitting more complicated target labels, not by simplicity as a selection principle (DA-M1).
- Compositional generalization on the circles data may be driven by the factorized, additive structure of the attributes (and affine independence of the four source points in ℝ³: the identity on S determines the affine map uniquely), not by weight norm.
- Weight decay, initialization scale and architecture can each produce the same norm ordering with no causal role in extrapolation.

## Missing Stakeholder Perspectives
Practitioners training with weight decay on large models would want to know which R and λ matter; no discussion of failure cases (Shah et al., 2020, shows simplicity bias hurting OOD robustness). Synthetic data only, so no harms at stake.

## Observations (Non-Defects)
Thm 4.1's proof structure (localization via A.3, gap argument via convexity of R, Lemma C.3) is coherent; the authors flag the equivalence-class limitation themselves; no test-set selection or tuning appears (protocol sweep found none); the literature check found no text overlap and no uncited prior work covering all central claims.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | C.3 unsatisfiable; A.1 strong |
| Clarity & Presentation | 66 | Clear but inconsistencies |
| Novelty & Originality | 48 | Incremental over Ge et al. |
| Significance & Impact | 44 | Hypothesis assumed |
| Experimental Validation | 36 | Confounded toy |
| Reproducibility | 55 | Details present; no code statement |
| Ethical Compliance | 62 | Nothing at stake |

## Overall: 2 | Confidence: 4
Pool position: better than about 35% of submissions to ICLR.

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "no code-availability statement" | moved to Minor | Reproducibility detail present in App. A–B; not a weakness on its own |
| R2 | "reference list padded / duplicates" | moved to Minor (kept the Saharia mismatch as a medium-confidence note) | Cosmetic |
| R3 | "no broader-impact discussion" | dropped | Synthetic data, nothing at stake; already covered by the Ethics flag |
| R4 | "typos" | moved to Minor | Presentation, does not hide the contribution |
| R4-W2 | "no quantitative generalization criterion" | kept, rewritten with locations (§3.1, Fig 4) | Was vague; the paper does not define "reliably" (§3.2) |
| DA | "diffusion model run count not stated" | rewritten as a question inside DA-M5 | Not stated after search; may be in the supplement |
| R2-W1 | "simplicity principle is not new" | rewritten | The paper's own contribution claim is the finite-sample theory and the framing; stated as positioning weakness with references |
| All | Weaknesses referring to Figures 2–7 | marked "judged from captions and text only" | Figures unavailable |

---

# Phase 2: Editorial Decision

# Editorial Decision

## Paper: Principled Out-of-Distribution Generalization via Simplicity
## Submission ID: iclr26-8xcmfwomnI (blinded)
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: Theoretical
## Review Team (fictional personas): EIC (meta-reviewer) Helena Okonkwo-Reyes; R1 Methodology Kwabena Aryeetey-Lund, R2 Domain Mei-Lin Draycott, R3 Perspective Soledad Marchetti-Ibarra, R4 Generalist Piotr Hallgrimsson, DA Oluwaseun Brandvold

---

## Decision: Borderline Reject (3), ICLR rating "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" (scale status: secondary)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 54.8
**EIC assessment** (internal): weighted rating 2.87 → starting point 3 · weighted composite 53.7 → band 3 (cross-check agrees) · **DA ceiling**: 3 · **Final (EIC)**: 3

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A clear, readable non-asymptotic theory that extends the Ge et al. covariate-shift analysis to non-unique source minimizers (Thm 4.1), a candid limitation discussion, and an attractive conceptual frame with a controllable testbed. The weaknesses of the experiments (single-seed diffusion, toy MLP) are ordinary for a theory paper.
- **Against acceptance:** The second theorem's hypotheses are unsatisfiable in the very regime it targets, the experiment meant to ground the "simplicity hypothesis" is confounded, the assumptions exclude the networks used in the experiments, and the framing ("foundation models", "first sharp") greatly exceeds the proven scope. The remaining contribution (Thm 4.1) is a modest extension.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| C.3 with τ ≥ 9 is unsatisfiable when d_S ≥ 1 | R1-W1/ERR-1, DA-C1, R2-W2 | Assumptions A.4(3), C.1, C.2, C.3; App. C.2 Case 2 | **Verified** | I re-derived: R(0)=0, convex, L-smooth ⇒ ‖∇R(β)‖ ≤ L‖β‖; ∆ ≤ L′δ; δ ≤ ∆^τ fails for small δ. The proof applies C.3 at small ∆ (Case 2). The intuition "τ→∞ recovers the constant gap" (§4.3) matches the direction of the exponent, so this is not an extraction slip. |
| Norm comparison confounded by 800 vs 400 samples | R1-W2, DA-M1 | §3.2 | **Verified** | Quote located: "trained on 400 identity samples from S, along with 400 modified samples from T" |
| Diffusion experiment shows simplicity at work | Paper C1 (§1, contribution 1); credited in R3-S2 | §3.1, Fig 3 | **Overstated** | §3.1 reports no complexity measure for the diffusion model; Fig 2 is MLP only |
| Symmetries break B.1/B.2 for NNs | R1-W3, DA-M3 | §5 equivalence-class discussion | **Verified** | Paper concedes for −β*; "We leave a formal development … to future work" |
| A.1 uniform bound fails for unbounded losses | R1-ERR-2 | A.1 and remark | **Partly correct** | The remark ties it to bounded losses; for MSE/Gaussian NLL uniformity over ℝ^d with β-independent B0 is doubtful, but I did not find a place where the paper claims it for MSE |
| "Sharp" unsupported beyond n-rate | R1-W5, R4-W1, DA-M2 | Abstract, §4.2 | **Partly correct** | Minimax optimality in n for the ∆=∞ subclass is stated in §4.2; no lower bound for ∆-dependence or τ-dependence |
| Intro "τ > 0" vs C.3 "τ ≥ 9" | R1-ERR-3, DA-m2 | §1 vs C.3 | **Verified** | |
| Fig 4 "20, 000" vs B.1 "40, 000" epochs | R1-ERR-4, DA-m1 | Fig 4, B.1 | **Verified** (minor) | |
| Missing references (Shah; Valle-Pérez; Abbe; Liang) | R2 | §1.1 | **Verified** | Each found by `verify`; prior and peer-reviewed or verified on arXiv; not cited; none is a required comparison for a theory paper, but Shah is important for positioning |
| Theorem 4.1 is routine | R2-W2 | §4.2 | **Partly correct** | The gap-based bias term and the multi-minimizer localization (App. C.1) are new relative to Ge et al.; still modest |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Main points verified (C.3, confound, symmetries); one point (A.1) interpretation-dependent |
| R2 (Domain) | 3 | 3 | 1.0 | Positioning and references verified; "routine" slightly overstated |
| R3 (Perspective) | 4 | 3 | 0.75 | Lenient for the venue: rating 4 / pool 65 sits above the report's own W1–W3 (thin empirical link, unexplained R, scope gap), and it credits Fig 1b as support for the principle, which §3.1 does not measure; it also missed the assumption problems |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound and calibrated; scope-vs-claims point verified |
| DA | 2 | 4 | 1.25 | Its CRITICAL and four of five MAJOR issues survived my check |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes: it removes contribution 2(b) (half of the stated theoretical contribution and the abstract's second regime), the hypotheses contradict the regime claimed, and what remains is a modest extension of a known bound with a confounded empirical story. Strict criterion 1 (evidence contradicts the claim as stated) met. | **Upheld** | New data/experiments or redesign (new assumption and re-derived rates), not clarification |

### Final Decision and Justification
The EIC-weighted rating is 2.87, giving a starting point of 3; the composite cross-check (53.7, band 3) agrees, so I keep the starting point. The upheld DA-C1 needs a redesigned assumption and re-proof, so the ceiling is 3, which the decision meets and does not exceed. **Pool position (EIC): about 42%.** Deciding evidence: a typical rejected submission, namely a modest but valid Thm 4.1, an unsatisfiable second regime, a confounded experiment and a framing beyond the proven scope; the paper does not show the "clear idea … that the field didn't have" with evidence across settings. I do not go to 2 because the constant-gap theorem and the writing are of real value and the fixes are well-defined. No integrity concerns were found (clean scan, no text overlap). This is how a careful panel would likely see this draft, not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 50 | 56 | 62 | 55 | 44 | 53.4 | 51.9 | 18 |
| Clarity & Presentation | 68 | 70 | 72 | 74 | 66 | 70.0 | 69.4 | 8 |
| Novelty & Originality | 52 | 52 | 62 | 52 | 48 | 53.2 | 52.2 | 14 |
| Significance & Impact | 46 | 48 | 62 | 52 | 44 | 50.4 | 48.9 | 18 |
| Experimental Validation | 36 | 38 | 50 | 40 | 36 | 40.0 | 38.9 | 14 |
| Reproducibility | 58 | 62 | 62 | 60 | 55 | 59.4 | 58.8 | 7 |
| Ethical Compliance | 66 | 66 | 70 | 68 | 62 | 66.4 | 65.8 | 8 |
| **Composite** | 52.2 | 54.9 | 62.6 | 55.9 | 48.6 | **54.8 (before)** | **53.7 (after)** | |

No dimension has a spread above 20, so no ⚠ flags. Composite before EIC weights (provisional DA-C1 upheld): 54.8; after: 53.7.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Principled Out-of-Distribution Generalization via Simplicity" to ICLR.

The paper tackles a central question, why over-parameterized models extrapolate in human-expected ways, and offers a formal route through simplicity-based selection among source-domain minimizers.

**Overall Assessment:** Reviewers found the exposition clear and the constant-gap result a legitimate extension of prior covariate-shift analysis, but they were not convinced that the empirical section tests the simplicity hypothesis, that the vanishing-gap theorem is applicable, or that the framing about foundation models follows from the results.

**Key Strengths Identified by Reviewers:**
1. A clean non-asymptotic bound with non-unique source minimizers and a clear bias–variance reading (R1, R2, R4).
2. Candid discussion of the equivalence-class limitation (R1, R4, R3).
3. A controllable synthetic testbed and a graded family of counter-examples (R3, R2).

**Key Concerns Requiring Attention:**
1. Assumption C.3 (τ ≥ 9) is incompatible with a positive-dimensional solution set (R1, DA, R2; CONSENSUS-3 in substance).
2. The §3.2 comparison is confounded and the diffusion model is not measured for simplicity (R1, R3, R4, DA; CONSENSUS-4).
3. The framing ("foundation models", "first sharp") exceeds the proven scope (R1, R2, R4, DA, R3 mildly; CONSENSUS-5).

**Critical Challenge (Devil's Advocate):** DA-C1 states that Thm 4.2's hypotheses cannot hold for d_S ≥ 1. I checked it against Assumptions A.4(3), C.1–C.3 and the proof's use of C.3 and uphold it.

**Decision: Borderline Reject (3).** The theory has a solid core, but half of the stated theoretical contribution does not stand as written, and the empirical support for the principle is not yet a test. Fixing the vanishing-gap assumption, adding a matched source-only experiment and re-scoping the claims would put a stronger paper in front of a future panel. Please refer to the Revision Roadmap below.

Sincerely,
Helena Okonkwo-Reyes
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Framing exceeds scope (foundation models; "sharp") | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Empirical support thin or confounded (§3.1–3.2) | R1, R3, R4, DA | CONSENSUS-4 |
| Assumption C.3/vanishing-gap theorem problem | R1, R2, DA | CONSENSUS-3 |
| Assumptions exclude NNs (symmetry, strong convexity) | R1, R3, DA | CONSENSUS-3 |
| Incremental over Ge et al. | R2, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the evidence adequate to support the conceptual principle? | R3 (borderline accept) | R1, R2, R4, DA | Not adequate; the diffusion run is unmeasured and the MLP comparison confounded (verified) |

### Score Spread Discussion
No dimension exceeded the 20-point spread; R3's higher pool position (65 vs 35–50 for the others) sits above its own listed weaknesses and credits an empirical story I found overstated, hence its lower weight.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | C.3 unsatisfiable for d_S ≥ 1 | Yes: R1 (ERR-1), R2 (W2, hedged) | Upheld | New analysis/redesign |
| DA-M1 | MAJOR | Confounded norm comparison | Yes: R1 | n/a | n/a |
| DA-M2 | MAJOR | Overclaim ("foundation models", "sharp") | Yes: R1, R2, R4 | n/a | n/a |
| DA-M3 | MAJOR | Symmetries violate B.1/B.2 | Yes: R1 | n/a | n/a |
| DA-M4 | MAJOR | Oracle λ and global optimization | Yes: R1 | n/a | n/a |
| DA-M5 | MAJOR | Diffusion generalization qualitative only | Partly: R3, R4 | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Assumption C.3 (τ ≥ 9) cannot hold when d_S ≥ 1; Thm 4.2 has no non-trivial instance | DA-C1, R1-W1/ERR-1, R2-W2 | §4.3, Assumption C.3, App. C.2 | Replace C.3 with a condition valid on a continuum (e.g., local quadratic growth, τ ≤ 1/2), re-derive the rate, or give an explicit example with d_S ≥ 1 | High (days–weeks of proof work; 0 GPU-h) | No |
| R2 | Source-only vs. source+corrupted-target confound; hypothesis not tested | R1-W2, DA-M1, R3-W1 | §3.2, Fig 2 | Matched source-only models with different extrapolations; report target error against norm; measure the diffusion model's norm | Medium (≈ 10–20 CPU-h MLP; ≈ 20–40 GPU-h diffusion) | Partly (MLP only) |
| R3 | Claims exceed scope: "foundation models", "first sharp", τ>0 in the intro | R1-W5/ERR-3, R2-W3, R4-W1, DA-M2 | Abstract, §1, §5 | Re-scope title/abstract/conclusion to the setting actually covered; state τ ≥ 9 | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Assumptions exclude the paper's networks (symmetry; A.1 uniform bound) | R1-W3, DA-M3 | Give a verified example model; state that NNs are outside the theory until the quotient extension is proved | Medium | Partly |
| S2 | Oracle λ, unknown ∆, B0; non-convex global minimizer; N* never evaluated | R1-W4, DA-M4 | Adaptive/validation-based λ or explicit oracle caveat; evaluate N* on the toy | Medium | Partly |
| S3 | Diffusion claim is qualitative; run count not stated | DA-M5, R4-W2 | Quantitative attribute classifier, multiple seeds, a generalization criterion for "reliably" | Medium (≈ 30 GPU-h) | Partly |
| S4 | Positioning against simplicity-bias literature | R2-W1, Missing References | Cite and discuss Shah et al. (2020), Valle-Pérez et al. (2019), Abbe et al. (2023), Liang et al. (2024) | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Fig 4 vs B.1 epoch count; permutation-map text vs App. B.4 | R1 | Correct |
| N2 | Duplicate bibliography entries; Saharia et al. entry | R2, R4, DA | Fix; ensure the cited paper matches the claim |
| N3 | Which R, and structural vs. norm simplicity | R3 | Short discussion with a toy example where ℓ₂ picks the wrong extension |
| N4 | Code-availability statement | R1 | Add |

## Estimated Revision Effort
- Priority 1: 3 items, roughly 2–4 weeks (dominated by the re-derivation of Thm 4.2).
- Priority 2: 4 items, roughly 1–2 weeks.
- Priority 3: 4 items, 1–2 days.
- **Total estimated revision time**: about 1–2 months.
