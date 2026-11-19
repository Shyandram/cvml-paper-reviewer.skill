# Simulated Review: "Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval"

*Skill: academic-paper-reviewer v2.10.1, full mode. Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction of the outcome. Personas are fictional. Figures are not available; Figures 1–3 are judged from captions and text only. The five reviewers were run as five separate passes in one model context (no subagents), so they are not independent agents.*

Run notes: the user asked for literature check **strict**, cutoff 2025-09-24. Two arXiv queries timed out (no network), so **Phase 1.5 was skipped**. All literature statements below come from the reviewers' knowledge and are marked `[verify]` where unsure. The integrity scan (`integrity_scan.py`) found no reviewer-directed text or hidden characters; the reviewers read the (unchanged) redacted copy.

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval |
| Primary Discipline | ML → online learning / online convex optimization (regret theory) |
| Secondary Discipline(s) | Prediction with expert advice; non-stationary / adaptive online learning |
| Paper Type | Theoretical (composite weights: theoretical) |
| Core Technique(s) | Online gradient descent, Discounted-Normal-Predictor with conservative updating (DNP-cu), meta-expert aggregation, geometric grid of discount factors |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | None. Reviews are public; ICLR rating on {0,2,4,6,8,10} (secondary-source labels) |
| Paper Maturity | Submission-ready theory paper; 21 pages, no experiments, no appendix or supplement |
| Ethics-Relevant Content | None |

### Claimed Contributions (as stated by the authors)
1. **C1**: OGD with a constant step size η = D√(2(1−λ))/G achieves O(1/√(1−λ)) λ-discounted regret (Thm 1, §3.1).
2. **C2**: A "novel analysis" of DNP-cu under discounted payoff: a guarantee for any η ≥ ρ, enabling aggregation of two experts that operate under different discount factors (Thm 2, Lemma 1, §3.2, §4.2, §4.5).
3. **C3**: SOGD (multiple OGD experts aggregated sequentially by DNP-cu) attains a uniform O(√log T/√(1−λ)) discounted regret for all λ ∈ [1−1/τ, 1−1/T] simultaneously, without knowing λ, answering an open question (Thm 3, §3.2, §4.3).
4. **C4 (framing)**: Reconstructing the Kapralov–Panigrahy argument "addressing the gaps and inaccuracies in their presentation" (§1.2 "Clarification"; Lemma 1 "entirely new and complete analysis", §4.5).

### Paper memory (factual record shared with all reviewers)
- **Setup:** Assumptions 1–3 (convexity, gradient bound G, diameter D) and f_t ∈ [0, GD] (Eq. 4). Grid S of discount factors λ_i = 1 − 2^{i−1}/T (Eq. 11–12), N = log₂(T/τ). Z = 1/T. τ ≥ max{16e, 32 log(1/Z)} (Thm 3). Horizon T is used to build the grid (Eq. 11, Alg. 4).
- **Experiments:** none. Splits, seeds, compute: not applicable. Code: not stated.
- **Headline results:** Thm 1: √2·DG/√(1−λ). Thm 3: (2GD/√(1−λ))(4√log(1/Z) + 2 + √(...)) + GD(N+1)Z/(1−λ) + 2GD (printed form; the √ over 1−λ in the abstract's rate is lost in extraction, see Remark after Thm 3).
- **Imported (not re-derived):** Eq. (24), (25), (28), (38), (39) and the convexity of g come from Zhang et al. (2022a) and Daniely and Mansour (2019); Lemma 2 from Kapralov and Panigrahy (2010, Lemma 20).
- **Appendix/supplement:** none (all proofs are in §4). **Unverifiable here:** Figures 1–3 (captions only); several garbled displays (Thm 3 statement, Lemma 2 coefficients, g definitions).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Renata Valcourt-Imai, public research university (Europe)
- **Seniority / Expertise**: Senior faculty / online learning theory, regret analysis, area chair for ML theory tracks
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Re-derives the key step herself; accepts modest theory contributions if correct and honestly positioned.

### Reviewer 1 (Methodology): Dr. Kaveh Oyelaran, research university (Middle East)
- **Seniority / Expertise**: Mid-career / proof techniques for OCO and expert aggregation; potential-function analyses
- **Review Focus**: Proof correctness, assumptions, tightness, constants, reproducibility of derivations
- **Style**: Reads proofs line by line and recomputes constants.

### Reviewer 2 (Domain): Prof. Elin Marchetti-Ng, public research university (East Asia)
- **Seniority / Expertise**: Senior faculty / adaptive and dynamic regret, universal OCO, switching costs
- **Review Focus**: Literature, novelty against closest prior work, domain contribution
- **Style**: Asks what is actually new relative to the nearest results.

### Reviewer 3 (Perspective): Dr. Sofia Adeyinka-Roth, industrial research lab (North America)
- **Seniority / Expertise**: Senior industry scientist / adaptive filtering, non-stationary control, streaming optimization practice
- **Review Focus**: Cross-field links, deployment assumptions, practical meaning of discounting
- **Style**: Constructive; most positive on the panel.

### Reviewer 4 (Generalist): Dr. Mateus Brandvold, university (South America)
- **Seniority / Expertise**: Mid-career / general machine learning theory and optimization (not online learning specifically)
- **Review Focus**: Contribution clarity, ICLR fit, presentation
- **Style**: Typical program-committee reader; skims derivations, focuses on message.

### Devil's Advocate: Prof. Jun-seo Halloran, university (Oceania)
- **Seniority / Expertise**: Senior faculty / optimization, evaluation methodology, claims-versus-evidence analysis
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans before attacking.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reviews

# Peer Review Report (Reviewer 1)

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Reviewer: Dr. Kaveh Oyelaran, Methodology Reviewer (research university, Middle East; fictional persona)
## Expertise: proof techniques for OCO; expert aggregation; potential-function analysis
## Date: 2026-11-10

---

## Summary
The paper studies λ-discounted regret in OCO. It first re-derives that OGD with a step size proportional to √(1−λ) has discounted regret of order 1/√(1−λ) (Thm 1). For an unknown λ, it builds a geometric grid of discount factors, runs one OGD per grid point, and chains DNP-cu combiners in order of decreasing discount factor (Alg. 3–4). The central technical step is a discounted-payoff guarantee for DNP-cu, Eq. (13)–(14) in Thm 2, which lets one combiner compete simultaneously against an expert at its own discount factor and against a longer-memory expert. The result is a bound of order √log T/√(1−λ) over a range of λ that is extended from the grid to a continuum by a smoothing lemma (Lemma 2).

## Strengths

### S1: The main proof chain is correct as far as I could check
I re-derived Thm 1 (§4.1): D²/η + ηG²/(2(1−λ)) equals √2·DG/√(1−λ) at the stated η. I checked (17)–(19) from convexity, the telescoping decomposition (32), the per-level bounds (34)–(36), and the grid-to-continuum step with (37). The factors are consistent (the paper's 2 in the last display of §4.3 is a valid loosening of √2).

### S2: The ordering requirement is identified and used correctly
The requirement η = λ₁ ≥ ρ = λ₂ in Thm 2 is exactly why Alg. 4 must go in descending discount factors ("in descending order of their associated discount factors", §3.2). The case analysis α_k (λ_i > λ_k) versus β (ρ = λ_i) in §4.3 is clean.

### S3: Honest attribution of what is borrowed
The "Clarification" paragraph (§1.2) and the statements "The proof is similar to that of Zhang et al. (2024, Theorem 6)" (§4.1) and "we directly leverage several intermediate results to avoid redundancy" (§4.4) tell the reader where the proofs lean on earlier work.

### S4: Thm 1 is uniform in time
Thm 1's step size and bound do not depend on T, which is a useful property for an OGD-based baseline.

## Weaknesses

### W1: The "new and complete" proof of Lemma 1 contains an invalid step (MAJOR)
In §4.5 the bound g(U(n)−8) ≤ e^{(64−16U(n))/(16n)} ≤ e^{(64−16U(n))/512} is justified by "the last two steps are due to the definition of U (n) and n ≥ 32". The exponent (64−16U)/(16n) is negative and increases toward 0 as n grows, so replacing n by its lower bound 32 gives a *smaller* quantity, not an upper bound. With U(n) ≈ 4√(n log(1/Z)) from Eq. (15), the first expression tends to 1 for large n, and the required inequality c − U·g(c) ≥ 1 then rests on log(1/Z) being large enough. For Z = 1/T and moderate T this probably still holds (my rough expansion suggests it does once log(1/Z) is about 2 or more), but as stated (Z ≤ 1/e, any n ≥ max{8e, 16 log(1/Z)}) the lemma is not established, and §4.5 itself says the authors regard this as the hard step ("proving (44) remains highly challenging").
- **Suggested Fix:** redo the last step with U(n)/n kept explicit, or restate Lemma 1 for Z = 1/T and T ≥ T₀ with the proof verified numerically. Low effort (1–2 days), rebuttal-feasible.

### W2: Several key inequalities are imported, so the "complete analysis" cannot be checked in this paper (MODERATE)
Eq. (24), (25), (28), (38), (39) and the convexity of g on [0, U(n)] are taken from Zhang et al. (2022a) or Daniely and Mansour (2019). Thm 4's proof also reuses "(70)" and "(74)" of the earlier paper. (39) in particular carries the potential-function argument. This is acceptable practice, but it conflicts with the framing of §4.5 as an "entirely new and complete analysis" and §1.2's criticism of the original sketch.
- **Suggested Fix:** add a short appendix stating each imported inequality with its hypotheses (the rule b_k ≠ b̃_k also appears twice in (24)–(25) as printed). Low effort.

### W3: "Cost of adaptivity" and tightness are asserted, not shown (MODERATE)
The Remark after Thm 3 says the extra O(√log T) factor reflects "the cost of adaptivity to the discount factor". No lower bound, and no argument that the factor is unavoidable, is given. The paper also contains no numerical sanity check of any kind. The constants (τ ≥ 32 log T, 4√log(1/Z) + 2, N+1 additive term) are large enough that a small synthetic experiment (piecewise-stationary linear losses on a ball, comparing SOGD with oracle-λ OGD over several λ) would show whether the bound is informative.
- **Suggested Fix:** either soften the wording ("incurs an additional factor, whose necessity we leave open") or add a lower-bound argument; add a CPU-only simulation (≈1 hour).

### W4: The advertised "uniform over a continuous interval" guarantee has a narrower range than the abstract suggests (MODERATE)
(a) The grid, N and Z all use the horizon T (Eq. 11, Alg. 4), so the method is not anytime; the T-independence remarked after Thm 1 does not carry over to Thm 3. (b) λ is limited to windows 1/(1−λ) ≥ τ, with τ ≥ 32 log T, described as "a minimal window length introduced for technical reasons". By my derivation this restriction costs nothing: the discounted regret is at most GD/(1−λ) = GD·n trivially (Eq. 4), and for n ≤ 32 log T one has GD·n ≤ √32·GD√(n log T), which is below the bound of Thm 3. So the restriction could be removed with a one-line remark, and the authors should say so.
- **Suggested Fix:** state the extension to all λ ≤ 1−1/T and discuss a doubling or anytime variant. Low effort.

### W5: Small inconsistencies in constants (MINOR, see Error Log)
Lemma 1 assumes U(n) ≥ 20 but its proof needs U(n) ≥ 22 (Thm 2 states 22); §4.3 uses n ≥ τ/2 in (31) but "n = τ" when bounding U(n).

**Minor:** §4.1 writes ‖f_t(w_t)‖² where ‖∇f_t(w_t)‖² is meant, and says "Jensen's inequality" where convexity is used; "discounted regret for discounted regret" (§2.2); "g" is defined twice, (6) and (8), with "erf" normalised differently, and Alg. 1 does not say which g it uses.

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | OGD achieves O(1/√(1−λ)) | Abstract, §3.1 | Thm 1, §4.1 | Supported (verified); matches the order of Zhang et al. (2024, Thm 6) |
| C2 | DNP-cu discounted payoff for η ≥ ρ | §3.2 | Thm 2, Thm 4, Lemma 1 | Partially: one proof step invalid (W1); several inputs imported |
| C3 | Uniform √log T/√(1−λ) over [1−1/τ, 1−1/T] | Abstract, §3.2 | Thm 3, §4.3 | Supported given C2; range and T-dependence narrower than the abstract suggests |
| C3′ | Extra factor is "the cost of adaptivity" | Remark after Thm 3 | none | Unsupported |
| C4 | Prior sketch had "gaps and inaccuracies" | §1.2 | none specified | Unsupported as stated |

### Protocol sweep and omission sweep
Searched the full text for test/validation/selection/tuning terms: no experiments, so no split or selection statements exist (not applicable). Omission sweep: seeds/compute (not applicable); limitations section (not stated after search; §5 restates results only); code (not stated, not needed for a proof paper); per-round computation (not stated, see Questions).

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | §4.5, after Fig. 3 | "the last two steps are due to the definition of" | The exponent (64−16U)/(16n) is negative; bounding it by the n = 32 value is a lower, not upper, bound for n > 32 | Derived: monotonicity in n; with U≈4√(n log(1/Z)) exponent → 0 | High (step) / Medium (lemma false at Z near 1/e) | MAJOR | Redo with U/n explicit |
| ERR-2 | E6 | Lemma 1 vs §4.5 end | "U (n) ≥ 20" (Lemma 1) vs. "due to U (n) ≥ 22" | At U = 20: 20(1−e^{−0.5}) − 8 = −0.13 < 1, so the proof does not give the lemma as stated; Thm 2 uses 22 | Recomputed; at 22 the value is 1.464, matching the printed 1.4648 | High | MINOR | State U(n) ≥ 22 |
| ERR-3 | E6 | §4.3 "(31) holds when…" and U(n) bound | "we set Z = 1/T and n = τ ≤ T" | (31) uses n ≥ τ/2, but 4√n ≥ 22 needs n ≥ 30.3; τ ≥ 16e gives only n ≥ 8e ≈ 21.7 and 4√21.7 ≈ 18.6. It holds only via τ ≥ 32 log T with T ≥ 8 | Recomputed | Medium | MINOR | State T ≥ 8 explicitly |
| ERR-4 | E2 | Lemma 2 (§4.3) | "the coefficients on the RHS are nonnegative and sum to 1" | For finite T the printed coefficients sum to less than 1 (the missing weight sits on the empty average s₀ = 0); harmless because the bound in (36) is ≥ 0 | Derived from s_t = (s^{λ₂}_t − λ₂ s^{λ₂}_{t−1})/(1−λ₂) | Medium (depends on the lemma's convention) | MINOR | Add a zero term or state the convention |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Proofs mostly sound, one invalid step in the lemma presented as new; no tightness evidence |
| Clarity | 3 | Well organised; duplicated definitions |
| Significance | 2 | Narrow sub-problem; useful but modest |
| Originality | 2 | Largely assembled from K&P 2010 and Zhang et al. 2022a |

## Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: correct but incremental theory with an invalid step in its flagship lemma and no tightness or empirical evidence; typical accepted theory papers show a sharper result or a lower bound.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Main chain verified; W1 and imported inputs |
| Clarity & Presentation | 64 | Competent | Good flow; notation duplication |
| Novelty & Originality | 50 | Developing | Adaptation of existing machinery |
| Significance & Impact | 52 | Developing | Niche but real |
| Experimental Validation | 38 | Developing | None; theory papers need not, but a sanity check was feasible |
| Reproducibility | 62 | Competent | Proofs in main text; imports from other papers |
| Ethical Compliance | 70 | Competent | Nothing at stake; no limitations section |

## Questions for Authors
1. Can you give a corrected proof of (44) for the full range of Lemma 1, or restrict the lemma? A correct proof would raise my Technical Rigor score.
2. Is the √log T factor necessary? A lower bound would raise Significance; an explicit "open" statement would remove my W3.
3. Does a strongly adaptive regret guarantee of the Daniely et al. / Jun et al. type already imply Thm 3 (see R2)? What does SOGD give beyond it?
4. What are the per-round oracle calls (function values at each expert's point, gradients at N+1 iterates)?

## Limitations Assessment
**Partially.** No limitations or open-problems paragraph (T known, range of λ, no lower bound, oracle model).

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): sound but incremental; the flagship lemma's proof has a real error and the tightness claim is unsupported.

## Confidence
**4**: I verified the main chain and recomputed constants; I did not re-derive the imported inequalities.

---

# Peer Review Report (Reviewer 2)

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Reviewer: Prof. Elin Marchetti-Ng, Domain Reviewer (public research university, East Asia; fictional persona)
## Expertise: adaptive and dynamic regret; universal OCO; meta-expert frameworks
## Date: 2026-11-10

---

## Summary
The paper shows that OGD with a suitably tuned step size has discounted regret of order 1/√(1−λ) and that, for an unknown λ in a range of window lengths, a chain of DNP-cu combiners over a geometric family of OGD experts gives discounted regret of order √log T/√(1−λ) simultaneously. It positions this as the answer to an open question left by a recent paper on discounted adaptive online learning, and as an OCO analogue of Kapralov and Panigrahy's argument for expert advice.

## Strengths

### S1: A clean statement of an interesting question
§1.1 explains why a standard meta-expert framework, where all experts share one performance measure, does not immediately apply when the measure itself (the discount) is the unknown; Fig. 1 contrasts the two settings.

### S2: The discount-ordering idea
The observation that the discounted payoff guarantee (13) holds for every η ≥ ρ, and the use of it in descending discount order (Alg. 4), is a neat way to let one combiner serve two different discounted measures.

### S3: Candid positioning relative to the PEA result
The "Clarification" in §1.2 acknowledges that the idea of uniform discounted regret appears in Kapralov and Panigrahy (2010) for expert advice, and the paper cites the OCO predecessors it builds on (Zhang et al. 2022a, 2024; Daniely and Mansour 2019).

## Weaknesses

### W1: Thm 3 may follow from known strongly adaptive regret by a short reduction, which the paper never addresses (MAJOR)
§1 says adaptive regret "serves a similar purpose to that of discounted regret" and notes that algorithms for it "provide guarantees that hold simultaneously for all intervals", then moves on. But a discounted regret against a fixed comparator w is a positive combination of suffix-interval regrets. Write s_t = f_t(w_t) − f_t(w) and S_k = Σ_{j≤k} s_{T−j+1} (regret on the last k rounds). Abel summation gives

Σ_t λ^{T−t} s_t = Σ_{k<T} (λ^{k−1} − λ^k) S_k + λ^{T−1} S_T.

Every S_k is at most the regret on that interval against its best point, which is at most R(k) for a strongly adaptive algorithm. With R(k) = c√(k log T), the bound of the type known for strongly adaptive regret in the papers cited in §1 (Daniely et al. 2015; Jun et al. 2017; exact log factor `[verify]`), Cauchy–Schwarz gives (1−λ)Σ_k λ^{k−1}√k ≤ 1/√(1−λ), and the boundary term λ^{T−1}√T is also O(1/√(1−λ)). The result is discounted regret O(√(log T)/√(1−λ)) for **every** λ ≤ 1−1/T at once, which is exactly the rate of Thm 3, without a τ restriction and (for anytime strongly adaptive algorithms) without knowing T. I checked the algebra; I am relying on memory for the strongly adaptive rate, and the literature check could not run, so this needs checking by the authors. If correct, C3 is a corollary of known tools and the "open question" has a short answer.
- **Why it matters:** this decides whether Thm 3 is a new capability or an alternative proof of an implied result.
- **Suggested Fix:** add a section comparing with this reduction. Either show where it fails (for example, an SA algorithm that does not give the stated rate in OCO, or a setting where the DNP route gives more: gradient-adaptive bounds, better constants), or reposition SOGD as an alternative proof. Medium effort; rebuttal-feasible as analysis.

### W2: The novelty language outruns the contribution (MAJOR)
Each ingredient has a direct source: the algorithm structure is SOGD (Zhang et al. 2022a, whose Combiner and DNP-cu chain it reuses, Alg. 3–4); the discounted-payoff lemma is "Lemma 18" of Kapralov and Panigrahy (2010) with the η ≥ ρ extension; the grid-to-continuum step is their Lemma 20; Thm 4 reuses intermediate results of the 2022 paper ("we directly leverage several intermediate results to avoid redundancy", §4.4). Thm 1 is, in the paper's words, "similar to that of Zhang et al. (2024, Theorem 6), except that we adopt a different step size" (§4.1), and the result has the same order. Phrases such as "novel analysis" (abstract, §1.2) and "entirely new and complete analysis" (§4.5) are then too strong; the gaps in the 2010 sketch are never listed.
- **Suggested Fix:** list exactly what changed relative to each source (a table), list the specific gaps found in Kapralov–Panigrahy §5, and tone down the wording.

### W3: The "open question" framing needs a quotation (MODERATE)
§1 says Zhang et al. (2024) "explicitly leave this scenario as an important open question in their work", for a paper about time-varying discount factors and gradient-adaptive bounds. It is unclear that their question is the worst-case uniform-in-λ bound studied here; I cannot verify this without the text.
- **Suggested Fix:** quote the sentence, and state which version of the question is answered.

### W4: Related work omits the strongly adaptive and parameter-free lines that are closest in technique (MODERATE)
There is no discussion of black-box reductions to strongly adaptive regret beyond a list of three citations in §1. Cutkosky (2020) is an example of such a line `[verify]`.

### Citation check (E7)
I checked the 3–5 citations the argument rests on against the in-text claims: Zhang et al. 2022a (SOGD, DNP-cu), Zhang et al. 2024 (fixed-λ OGD result, O(1/√(1−λ²))), Kapralov and Panigrahy 2010 (§5 sketch, Lemmas 18, 20, 22), Daniely and Mansour 2019, Freund and Hsu 2008. The in-text descriptions are consistent with what I know of them, but I could not compare them to the abstracts (no literature check). One question rather than a flag: Krichene et al. (2014), on no-regret learning in selfish routing, is cited among the "discounted variants under the framework of tracking the best expert" (§2.2); its relevance should be explained.

## Missing References (no literature check ran; none verified, all marked `[verify]`)
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | none (the strongly adaptive papers central to W1 are already cited: Daniely et al. 2015; Jun et al. 2017) | |
| Important | Ashok Cutkosky, "Parameter-free, Dynamic, and Strongly-Adaptive Online Learning", ICML 2020 `[verify]` | A black-box route to strongly adaptive regret; relevant to W1 |
| Helpful | Omar Besbes, Yonatan Gur, Assaf Zeevi, "Non-stationary stochastic optimization", Operations Research, 2015 `[verify]` | Non-stationarity measured differently; context for the motivation |

### Novelty against the closest prior work (built from the paper and memory, no literature check)
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C1 (OGD, 1/√(1−λ)) | Zhang et al. 2024, Thm 6 | Same order for fixed λ (as quoted in §3.1 Remark) | A different step size | Yes, same order acknowledged |
| C2 (DNP-cu, discounted payoff, η ≥ ρ) | K&P 2010 Lemmas 18, 20, 22; Zhang et al. 2022a Thm 1 | Discounted payoff for PEA; DNP-cu in OCO with standard payoff | Combination (OCO plus discounted payoff plus η ≥ ρ); a new proof of the Lemma 18/22 step | Yes, partially differentiated |
| C3 (uniform over λ in OCO) | K&P 2010 §5 (PEA); strongly adaptive regret reduction (W1) | Uniform discounted regret in PEA; interval-uniform regret in OCO | OCO instantiation | Reduction not discussed |

### Per-claim novelty (knowledge-based, `[verify]`)
C1: incremental. C2: incremental to medium. C3: medium at most, and incremental if the reduction in W1 holds.

### Field snapshot (knowledge only, `[verify]`)
Discounted and strongly adaptive regret are mature topics with several ICML/COLT/NeurIPS papers. At this venue a theory-only paper is expected to show either a result that previous tools cannot give or a clearly simpler or sharper derivation; extending a known meta-algorithm to a new regret measure is usually seen as incremental unless it comes with tightness.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound but see R1 |
| Clarity | 3 | Clear enough |
| Significance | 2 | Depends on W1 |
| Originality | 2 | Built from K&P and Zhang et al. |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main theorem's rate appears recoverable from known strongly adaptive regret results, and the proofs are adaptations; no result that earlier tools cannot give is shown.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Correct modulo R1's finding |
| Clarity & Presentation | 62 | Competent | Positioning of the novelty is unclear |
| Novelty & Originality | 42 | Developing | See W1, W2 |
| Significance & Impact | 46 | Developing | Niche; implied by simpler route if W1 holds |
| Experimental Validation | 38 | Developing | None |
| Reproducibility | 60 | Competent | Self-contained apart from imports |
| Ethical Compliance | 70 | Competent | Nothing at stake |

## Questions for Authors
1. Does the Abel-summation reduction from strongly adaptive regret give Thm 3's bound? If not, which step fails? (A convincing answer would raise Novelty and Significance substantially.)
2. What exactly are the "gaps and inaccuracies" in Kapralov and Panigrahy §5?
3. Can SOGD give something the reduction cannot (anytime guarantee without T, gradient-adaptive terms, smaller constants)?

## Limitations Assessment
**Partially.** No limitations paragraph; relation to adaptive regret is not analysed.

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): technically sound, but the contribution is incremental and the main result may be implied by known tools.

## Confidence
**4**: I checked the reduction algebra myself; the rate of the strongly adaptive results is from memory.

---

# Peer Review Report (Reviewer 3)

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Reviewer: Dr. Sofia Adeyinka-Roth, Perspective Reviewer (industrial research lab, North America; fictional persona)
## Expertise: adaptive filtering; non-stationary streaming optimization; practical use of exponential forgetting
## Date: 2026-11-10

---

## Summary
Exponential forgetting is everywhere in practice (exponential moving averages, forgetting factors in recursive estimators, momentum). The paper asks how a learner can adapt when the right forgetting rate is unknown, and gives an OCO algorithm whose discounted regret scales like √log T/√(1−λ) for all rates in a range. The result is purely theoretical and worst-case.

## Strengths

### S1: A well-chosen abstraction of "forgetting rate selection"
The unknown-discount problem (§1) is the OCO version of choosing a window or decay constant online. Casting it as simultaneous regret guarantees across λ is natural and could inform how EMA rates are chosen in online and streaming systems.

### S2: Assumptions are standard and clearly stated
Assumptions 1–3 and the normalization (4) are the usual ones; the reader can see exactly what is assumed.

### S3: A concrete algorithmic recipe
Fig. 2 and Alg. 4 give an implementable meta-algorithm (a logarithmic number of experts), and the order requirement in §3.2 is easy to follow.

## Weaknesses (framed as opportunities)

### W1: No evidence that the guarantee is practically meaningful (MODERATE)
The motivation (§1: stock prediction, volatile versus stable periods) is not followed by any experiment, and the constants (τ ≥ 32 log T, 4√log(1/Z) + 2) leave unclear when the bound beats the trivial GD/(1−λ). A small simulation with a regime switch would show whether the meta-algorithm picks the right memory.
- **Suggested Fix:** a synthetic experiment plus a plot of regret against 1/(1−λ) for the oracle OGD, SOGD and a fixed-λ OGD.

### W2: Oracle and computational assumptions are implicit (MODERATE)
Alg. 3 line 6 says "Send the loss function" to both experts, and ℓ_t in (19) needs f_t at two different points (the learner plays a convex combination, but the DNP bit uses the experts' function values). Each round therefore needs N+1 gradient evaluations and 2N function evaluations. This is the usual price of meta-expert methods but it matters for streaming practice, and the cost is never stated.
- **Suggested Fix:** state the per-round cost (O(log(T/τ)) experts) and the oracle model; discuss bandit or gradient-only feedback as future work.

### W3: Known horizon and bounded domain (MODERATE)
The grid (11) and Z = 1/T use the horizon; real streams have none. The bounded diameter D and gradient bound G are needed to normalise bits in [−1, 1].
- **Suggested Fix:** discuss a doubling or anytime construction and what breaks if D or G is unknown.

### W4: Links to neighbouring fields are not drawn (OPPORTUNITY)
Forgetting-factor selection is well studied in adaptive filtering (recursive least squares with a forgetting factor; variable forgetting factor schemes), in discounted bandit algorithms for switching environments, and in EMA-based optimisers (the paper cites Ahn et al. 2024 on Adam). A short discussion of what the worst-case result says about these would widen the audience: for instance, whether SOGD's selection of the memory is related to variable forgetting-factor rules, and what the result implies for choosing Adam's β₂ online.

### Fundamental assumption audit
1. *Worst-case adversary and a fixed comparator.* The discounted comparator w is a single point for the whole history; in practice drift often moves the optimum, which discounted regret only partly captures (compare with dynamic regret).
2. *Full-function access.* See W2.
3. *Scale.* Logarithmic overhead is cheap, but each expert runs a full OGD step, so high-dimensional models multiply cost by N+1.

### Future directions
A lower bound for uniform discounted regret; combining with dynamic regret; gradient-adaptive versions (the line begun by Zhang et al. 2024); an anytime algorithm; bandit feedback; an empirical study on non-stationary streams.

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a correct, clearly motivated theoretical result with a clean algorithmic idea, in a topic with a real practical counterpart; the incremental technique and lack of experiments keep it from the accepted-theory band.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 68 | Competent | Chain verified in the main proofs; I did not audit constants |
| Clarity & Presentation | 66 | Competent | Clear structure |
| Novelty & Originality | 58 | Competent | A new combination of known parts |
| Significance & Impact | 62 | Competent | A useful theoretical tool for memory selection |
| Experimental Validation | 45 | Developing | None; a sanity check would help |
| Reproducibility | 64 | Competent | Algorithms fully specified |
| Ethical Compliance | 72 | Competent | No ethical concerns; limitations are thin |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Rigorous but no empirical check |
| Clarity | 3 | Clear |
| Significance | 3 | Useful for a recognisable practical problem |
| Originality | 2 | Combination of known ideas |

## Questions for Authors
1. Is there a regime (short windows, small T) where the explicit constants make Thm 3 informative? What does the bound look like for T = 10⁴?
2. Can the algorithm run with gradient-only access?
3. How should one choose τ in practice?

## Limitations Assessment
**Partially.** Assumptions are stated but their practical consequences are not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**4** (Borderline Accept): sound and clearly motivated, with typical weaknesses for a theory paper; I lean to accept.

## Confidence
**3**: Fairly confident; I am not a specialist in regret proofs and did not audit the technical lemmas.

---

# Peer Review Report (Reviewer 4)

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Reviewer: Dr. Mateus Brandvold, Generalist Reviewer (university, South America; fictional persona)
## Expertise: machine learning theory; convex optimisation (not online learning specifically)
## Date: 2026-11-10

---

## Summary
The paper considers online learning where the loss of old rounds is geometrically discounted, so that recent data matter more. It shows that plain online gradient descent handles a known discount factor and proposes a meta-algorithm built from several gradient-descent runs combined by a prediction-with-advice subroutine, so that one algorithm achieves near-optimal discounted regret for every discount factor in a range, without being told which one applies. The authors regard this as the answer to a question raised in earlier work.

## Strengths

### S1: A clear problem and a readable motivation
The abstract and §1 state the question and the obstacle in plain terms, and Fig. 1 (from the caption: previous work in the upper panel, discounted OCO in the lower panel) makes the difficulty visible.

### S2: Well-organised paper
Preliminaries (§2), main results (§3) and proofs (§4) are cleanly separated; the theorem statements come first and the proofs follow, with a one-paragraph intuition after each theorem.

### S3: Appropriate fit with ICLR's theory audience
Online convex optimisation and regret analysis are within ICLR's learning-theory scope, and the paper is honest about its building blocks.

### S4: Reasonably modest claims in the conclusion
§5 restates what was shown without extra claims.

## Weaknesses

### W1: It is hard to tell what is new (MODERATE)
There is no contribution list. The reader has to piece the claims together from the abstract, §1.2 and the remarks. Much of the machinery (DNP-cu, SOGD, the combiner) comes from earlier papers; §1.2 says so, but the delta is not summarised. The wording "novel analysis" and "entirely new and complete analysis" makes the delta look larger than the text supports.
- **Suggested Fix:** add a bullet list of contributions that separates what is reused from what is new.

### W2: No discussion of tightness, limitations or practical meaning (MODERATE)
§5 restates results. A non-specialist cannot tell whether √log T/√(1−λ) is good, whether a lower bound is expected, or what T-dependent tuning means in practice (see R1, R3).
- **Suggested Fix:** a short "Limitations and open questions" paragraph.

**Minor:** two error-function definitions and two g's (Eq. 6 and 8) with Alg. 1 not saying which; Fig. 2 and Fig. 3 captions are short (judged from captions only); "sequentially aggregation", "the these studies", "discounted regret for discounted regret" (§2.2).

### Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness (claims backed by proofs) | Partly | §4; ERR-level issues flagged by R1 |
| Presentation | Met | §1–§3 |
| Contribution (significance to ICLR audience) | Partly | Niche, incremental |
| Related work positioned | Partly | §1, §2.2–2.3 list prior work but do not explain the delta |
| Limitations stated | Not met | §5 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound as far as a generalist can tell |
| Clarity | 3 | Clear |
| Significance | 2 | Niche |
| Originality | 2 | Built on earlier components |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear question and a correct, well-structured answer from a well-chosen toolkit; typical for a borderline-accepted theory paper, though the delta from earlier work is modest.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 66 | Competent | Appears sound; I did not dig into the derivations |
| Clarity & Presentation | 64 | Competent | Clear, with some duplicated notation |
| Novelty & Originality | 58 | Competent | Incremental |
| Significance & Impact | 60 | Competent | Moderate |
| Experimental Validation | 48 | Developing | None |
| Reproducibility | 62 | Competent | Algorithms specified |
| Ethical Compliance | 70 | Competent | Nothing at stake |

## Questions for Authors
1. Can you give a one-paragraph statement of what is new compared with the earlier SOGD paper?
2. Is the √log T factor unavoidable?
3. What would a practitioner choose for τ?

## Limitations Assessment
**No.** Not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**4** (Borderline Accept): a clear, correct theory paper whose reasons to accept (an explicit question, a clean answer) slightly outweigh its modest novelty.

## Confidence
**3**: Fairly confident as a generalist.

---

# Devil's Advocate Report

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Reviewer: Prof. Jun-seo Halloran, Devil's Advocate (university, Oceania; fictional persona)

---

## Steelman
The paper identifies a real difficulty (experts under different performance measures cannot be combined by Hedge-style aggregators) and shows that DNP-cu's discounted-payoff guarantee, valid for every η ≥ ρ, repairs it. The proofs are explicit, the algorithm is simple, and the resulting bound scales with the natural effective window n = 1/(1−λ) up to √log T.

## Core Argument Chain
1. Standard meta-expert methods need one performance measure for all experts (§1.1).
2. With an unknown discount, experts operate under different measures, so those methods fail (§1.1).
3. DNP-cu satisfies a discounted-payoff guarantee for any η ≥ ρ (Thm 2).
4. Chaining combiners in descending discount order uses this guarantee (Alg. 4, §4.3).
5. Hence SOGD achieves √log T/√(1−λ) uniformly over [1−1/τ, 1−1/T], answering an open question (Thm 3).
∴ Adapting to an unknown discount factor is possible only through this new analysis.

## Strongest Counter-Argument
Premise 2 is not established, and the conclusion "only through this analysis" is false if the following reduction holds. Discounted regret against a fixed comparator is a nonnegative combination of suffix-interval regrets: with S_k the regret on the last k rounds, Σ_t λ^{T−t} s_t = Σ_{k<T}(λ^{k−1} − λ^k) S_k + λ^{T−1} S_T. Any algorithm with strongly adaptive regret R(k) ≈ c√(k log T) on every interval (the guarantee the paper cites in §1 for Daniely et al. 2015 and Jun et al. 2017, exact form `[verify]`) therefore has discounted regret at most (1−λ)Σ_k λ^{k−1} R(k) + λ^{T−1}R(T), and Cauchy–Schwarz bounds the first sum by c√(log T)/√(1−λ); the boundary term is of the same order. That is the rate of Thm 3, for all λ ≤ 1−1/T, with no τ restriction. I checked the algebra and found no gap. Note that the paper's own motivation (§1) says adaptive regret "serves a similar purpose to that of discounted regret" and that SOGD's earlier incarnation already targets adaptive regret (§1.2), yet the text never states why the one does not give the other. If the reduction is right, the "open question" has a short answer and Thm 3's main message is a corollary; the contribution reduces to an alternative proof whose technical content is an extension of Kapralov and Panigrahy's analysis, including a lemma proof (Lemma 1) that, as R1 shows, has a flawed final step. The authors must either show the reduction fails, or say what SOGD gives that it does not (anytime guarantee, gradient-adaptive terms, constants).

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The reduction concerns the paper's novelty rather than its correctness; it rests on a rate I recall rather than quoted from a verified source, and the paper cites the adaptive-regret works and could answer by positioning, so it is MAJOR (criterion 7 requires a verified uncited prior work, which I do not have).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Scope | §1, §3.2 Thm 3 | Possible corollary of strongly adaptive regret via Abel summation (see above); the "open question" framing and C3's significance depend on it | Add a section analysing this reduction; show failure or reposition |
| DA-M2 | Evidence | Remark after Thm 3 | "reflecting the cost of adaptivity to the discount factor" is asserted with no lower bound | Add a lower bound, or write "we do not know whether this factor is necessary" |
| DA-M3 | Evidence | §4.5, Lemma 1 | The proof advertised as "entirely new and complete" has an invalid final step (R1 ERR-1); Lemma 1's stated hypothesis U(n) ≥ 20 is not what the proof needs (ERR-2) | Repair; restate for the regime used (Z = 1/T) |
| DA-M4 | Scope | Abstract, Thm 3, Eq. (11) | "unknown discount factor" is a restricted case: horizon T known, windows ≥ τ ≥ 32 log T; the restriction on windows is vacuous (trivial bound GD/(1−λ) is already below the bound for n ≤ 32 log T), while T-dependence is real and not discussed | State the extension to all λ ≤ 1−1/T; discuss anytime variants |
| DA-M5 | Overclaiming | §1.2 "Clarification", §4.5 | "gaps and inaccuracies" in the earlier sketch are asserted but not enumerated | List them |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | Whole paper | No sanity experiment; constants (e.g., τ ≥ 32 log T) may make the bound vacuous for realistic T |
| DA-m2 | Clarity | Eq. (6), (8), Alg. 1 | Two definitions of g and of erf with different normalisation; Alg. 1 does not say which |
| DA-m3 | Logic | §3.1 Remark | "uniformly over time" holds for OGD (Thm 1), not for SOGD, whose grid uses T |
| DA-m4 | Clarity | §4.1 | ‖f_t(w_t)‖² where ‖∇f_t(w_t)‖² is intended; "Jensen's inequality" where convexity is used |
| DA-m5 | Evidence | §4.3, (31) | n ≥ τ/2 in (31) but n = τ in the U(n) bound (ERR-3) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Thm 1 constant: D²/η + ηG²/(2(1−λ)) at η = D√(2(1−λ))/G | √2·DG/√(1−λ) | 2·DG/√(2(1−λ)) = √2·DG/√(1−λ) | Yes |
| "1−λ < 1−λ² < 2(1−λ)" (Remark after Thm 1) | as stated | (1−λ)(1+λ) with 1+λ ∈ (1, 2) | Yes |
| g(4√n) bound, §4.3 | ≈ 0.8517 | (1/√2)(√π/4)·e = 0.7071 × 0.4431 × 2.7183 = 0.8517 | Yes (origin of the bound not derivable from the garbled display) |
| Lemma 1 end: U(1−e^{(64−16U)/512}) − 8 at U = 22 | ≥ 1.4648 | 22 × (1 − e^{−0.5625}) − 8 = 22 × 0.4302 − 8 = 1.464 | Yes |
| Same expression at U = 20 (Lemma 1's stated hypothesis) | implied ≥ 1 | 20 × (1 − e^{−0.5}) − 8 = −0.13 | No |
| (37): (1−λ_{i+1})/(1−λ_i) | ≤ 2 | 2^i/2^{i−1} = 2 | Yes |
| Last display of §4.3 constant on the main term | 2 | √((1−λ_{i+1})/(1−λ)) ≤ √2 | Yes (the paper's 2 is loose) |

## Ignored Alternative Explanations
1. The same rate may be an artefact of the √(k log T) strongly adaptive rate integrated against the geometric weights (see Strongest Counter-Argument).
2. The additive (N+1)GDZ/(1−λ) term is lower-order only because Z = 1/T and 1−λ ≥ 1/T; the paper does not say so.
3. For windows n ≤ 32 log T the bound is implied by the trivial bound, so the τ restriction is not "technical" but a non-restriction.

## Claim Distortion Check (E5)
| Sentence | Evidence | Supported as worded? |
|----------|----------|----------------------|
| "we affirmatively answer this question" (abstract) | Thm 3 for T-dependent grid, windows ≥ τ | Partly: the question is "adapts to an unknown discount factor"; T must be known |
| "novel analysis" (abstract, §1.2) | §4.2–4.5 reuse Zhang et al. 2022a, K&P 2010 | Overstated |
| "reflecting the cost of adaptivity" (Remark after Thm 3) | none | Unsupported |
| "uniformly over time" (§3.1 Remark) | Thm 1 only | Supported for OGD only |
| "entirely new and complete analysis" (§4.5) | Lemma 1 proof | Overstated: invalid last step |

## Missing Stakeholder Perspectives
Practitioners who tune forgetting rates (adaptive filtering, streaming systems) are named as motivation (§1, stock prediction) but their constraints (oracle access, unknown horizon) are not addressed.

## Observations (Non-Defects)
The proofs of Thm 1, (17)–(19), (32)–(37) are correct; the ordering insight (η ≥ ρ, descending discount factors) is a genuine and nicely used point; attributions to earlier work are generally honest.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 60 | Main chain correct; Lemma 1 proof flawed |
| Clarity & Presentation | 62 | Clear; positioning vague |
| Novelty & Originality | 44 | Extension of known machinery; possible corollary |
| Significance & Impact | 46 | Depends on the reduction |
| Experimental Validation | 36 | None; bound's informativeness untested |
| Reproducibility | 60 | Self-contained apart from imports |
| Ethical Compliance | 70 | Nothing at stake |

**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main theorem's rate appears to be implied by known tools, and the technical novelty is modest.

## Overall: 3 | Confidence: 4

---

## Phase 1.5: Literature Check

Mode requested: **strict**, cutoff 2025-09-24. Two queries were sent to arXiv (claim C1 "discounted regret online learning"; claim C3 "strongly adaptive regret"). Both timed out after 45–100 s (no network). Result: no kept results, no `similarity` or `novelty` run, no baseline scout (the paper has no empirical benchmark). The Domain Reviewer relied on knowledge and marked every recommended reference `[verify]`. Gaps left open: all.

## Phase 1.6: Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 constants inconsistencies | Moved to Minor (kept in Error Log) | MINOR errors that do not change a conclusion |
| R1 | W4 range of λ | Rewritten | The reported restriction is vacuous (derived); text now states so |
| R2 | W3 "open question" framing | Kept as MODERATE, rewritten as a request for the quotation | Cannot be verified against the cited paper |
| R3 | W4 links to other fields | Kept, relabelled "opportunity" | Not a defect of the paper; constructive suggestion |
| R4 | W1 no contribution list | Kept | Verified: no bullet list in §1 |
| R4 | notation duplication | Moved to Minor | Presentation detail |
| DA | DA-m3 "uniformly over time" | Kept | Verified: the Remark after Thm 1 applies to OGD only |
| All | Weakness citing "no experiments" | Kept as MODERATE in R1/R3, MINOR in DA | A theory paper; only matters for the informativeness of the constants |
| All | Reduction claim (R2-W1, DA-M1) | Kept; flagged for EIC verification | Depends on a recalled rate |

Scores were not changed.

---

## Phase 2: Editorial Synthesizer, Part A

### Issue list and classification
| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Possible reduction from strongly adaptive regret; novelty of Thm 3 and "open question" framing | R2-W1, DA-M1 (R1 Q3) | CONSENSUS-2 (hinge) |
| I2 | Lemma 1 proof step invalid / hypothesis mismatch | R1-W1, DA-M3 | CONSENSUS-2 (hinge) |
| I3 | "Cost of adaptivity" and tightness unsupported; no lower bound | R1-W3, DA-M2, R4-W2 | CONSENSUS-3 (hinge) |
| I4 | Overstated novelty language; unnamed gaps in K&P | R2-W2, DA-M5, R4-W1 | CONSENSUS-3 |
| I5 | Known horizon, narrower λ-range than advertised, oracle model | R1-W4, R3-W2/W3, DA-M4 | CONSENSUS-3 |
| I6 | No empirical sanity check | R1-W3, R3-W1, DA-m1 | CONSENSUS-3 |
| I7 | Imported lemmas, "complete analysis" not self-contained | R1-W2, R4-W1 | CONSENSUS-2 |
| I8 | "Open question" quotation | R2-W3 | SOLO |
| I9 | Links to adaptive filtering and EMA optimisers | R3-W4 | SOLO |
| S1 | Significance: R3, R4 positive vs. R2, DA negative | | SPLIT |

**DA-CRITICAL issues:** none raised.

### Official score (BEFORE run, no EIC weights, DA list empty)
`scores_before.json` → `before.json`: official mean rating 3.40 (R1 3, R2 3, R3 4, R4 4, DA 3); official composite 57.2; suggested Overall 3; no warnings; ICLR Soundness 2 / Presentation 3 / Contribution 2.

---

## Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval
## Submission ID: iclr26-65iFtHZ8Cu
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: theoretical
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Renata Valcourt-Imai; R1 Methodology Dr. Kaveh Oyelaran, R2 Domain Prof. Elin Marchetti-Ng, R3 Perspective Dr. Sofia Adeyinka-Roth, R4 Generalist Dr. Mateus Brandvold, DA Prof. Jun-seo Halloran

---

## Decision: Borderline Reject (3), shown on the ICLR scale as 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); ICLR scale status: secondary

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 57.2
**EIC assessment** (internal): weighted rating 3.29 → starting point 3 · weighted composite 56.4 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** about 52 (better than about 52% of ICLR submissions). Deciding evidence: a correct but incremental extension of existing machinery, with a flawed flagship lemma proof, no tightness evidence, and a main rate that appears to follow from known strongly adaptive regret results.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The question is natural and the paper gives an explicit, mostly correct algorithm and proof chain; the descending-discount ordering with η ≥ ρ is a real insight; attribution to predecessors is honest; the weaknesses (no experiments, T known) are common in accepted theory papers.
- **Against acceptance:** The central theorem's rate appears to be a corollary of strongly adaptive regret, which the paper itself cites and never analyses; the technical content is an adaptation of Kapralov–Panigrahy and Zhang et al. (2022a); the proof presented as new and complete contains an invalid step; "cost of adaptivity" and "novel analysis" are asserted without support; there is no lower bound or sanity check.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Discounted regret is a positive combination of suffix-interval regrets, so strongly adaptive regret of order √(k log T) yields √(log T)/√(1−λ) | R2-W1, DA-M1 | §1, Thm 3 | **Verified (algebra)** | I re-derived Abel summation, Cauchy–Schwarz and the boundary term. The SA rate itself is from memory (`[verify]`); the conclusion that the paper must discuss this is solid, but whether Thm 3 is *strictly* implied depends on that rate |
| Invalid final step in Lemma 1's proof | R1-W1 / ERR-1, DA-M3 | §4.5 | **Verified** | The exponent is negative; bounding by the n = 32 value is a lower bound for n > 32. Impact on Thm 3 appears limited (Z = 1/T, moderate T), so **Partly correct** on "lemma fails" |
| Lemma 1 hypothesis U(n) ≥ 20 vs. proof's 22 | R1 ERR-2, DA | Lemma 1, §4.5 | **Verified** | −0.13 at U = 20; 1.464 at U = 22 |
| τ restriction is vacuous | R1-W4, DA-M4 | Thm 3 | **Verified** | Trivial regret ≤ GD/(1−λ) is below the bound for n ≤ 32 log T |
| Known horizon T in the grid; "uniformly over time" holds for OGD only | R1-W4, R3-W3, DA-m3 | Eq. (11), Alg. 4, §3.1 Remark | **Verified** | |
| "Cost of adaptivity" has no support | R1-W3, DA-M2 | Remark after Thm 3 | **Verified** | |
| Unspecified "gaps and inaccuracies" in K&P | R2-W2, DA-M5 | §1.2 | **Verified** | None enumerated |
| Per-round function-value access at several points | R3-W2 | Alg. 3 line 6, Eq. (19) | **Verified** | |
| R4: contribution is a clear answer to an open question | R4 | §1 | **Overstated** | Depends on I1 and on what Zhang et al. (2024) actually left open (unverified) |
| Lemma 2 coefficients sum below 1 | R1 ERR-4 | §4.3 | **Verified, harmless** | The bound is nonnegative |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error log verified at its locations (ERR-1, 2, 4); minor overstatement on whether Lemma 1 fails outright |
| R2 (Domain) | 3 | 4 | 1.25 | The decisive reduction point is verified; the SA rate is recalled and marked `[verify]`, which is appropriate |
| R3 (Perspective) | 4 | 3 | 1.0 | Sound, constructive; points verified; does not weigh the novelty issue |
| R4 (Generalist) | 4 | 3 | 0.75 | Rating rests on the "open question answered" premise that the EIC found overstated; otherwise reasonable and does not hold up the weaknesses it lists |
| DA | 3 | 4 | 1.0 | Counter-argument survived the check, no CRITICAL claimed; full weight but overlaps R2, not independently decisive |

### DA-CRITICAL Rulings
No DA-CRITICAL issues were raised. The DA's strongest counter-argument (DA-M1) was rated MAJOR; the EIC concurs that it is MAJOR (no verified uncited prior work, the paper cites the relevant adaptive-regret papers). **DA ceiling: none.**

### Final Decision and Justification
The EIC-weighted rating is 3.29, so the starting point is 3, and the composite cross-check (56.4, band 3) agrees; the decision does not depart from the starting point and stays below no ceiling. The reasons: the two accept-leaning ratings (R3, R4) rest on the paper being a clear answer to an open question, while the verified points show that the main rate plausibly follows from tools the paper cites (I1), that the proof offered as new contains an invalid step (I2), and that two headline phrases ("novel analysis", "cost of adaptivity") are not supported (I3, I4). These are fixable, and the paper is a correct, honestly attributed extension, but typical accepted theory papers at ICLR show a result earlier tools do not give, a lower bound, or a clearly sharper proof; this draft shows none of them. Pool positions of the reviewers range from 48 to 66; the spread (18 points) is explained by whether the reviewer weighs I1. The EIC's own pool position is 52, on the rejected side of the bar for the reasons above. If the authors can show the reduction fails, or show what SOGD gives that it does not, and repair Lemma 1, the paper would be a borderline accept.

---

## Score Summary

### Official Scores and EIC Assessment
(From `aggregate.json`, run with the EIC weights: R1 1.25, R2 1.25, R3 1.0, R4 0.75, DA 1.0; weight shares R1 .253, R2 .253, R3 .167, R4 .125, DA .202.)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 58 | 58 | 68 | 66 | 60 | 62.0 | 61.1 | 10 |
| Clarity & Presentation | 64 | 62 | 66 | 64 | 62 | 63.6 | 63.4 | 4 |
| Novelty & Originality | 50 | 42 | 58 | 58 | 44 | 50.4 | 49.1 | 16 |
| Significance & Impact | 52 | 46 | 62 | 60 | 46 | 53.2 | 51.9 | 16 |
| Experimental Validation | 38 | 38 | 45 | 48 | 36 | 41.0 | 40.0 | 12 |
| Reproducibility | 62 | 60 | 64 | 62 | 60 | 61.6 | 61.4 | 4 |
| Ethical Compliance | 70 | 70 | 72 | 70 | 70 | 70.4 | 70.3 | 2 |
| **Composite** | 55.5 | 52.7 | 62.8 | 61.7 | 53.5 | **57.2 (before)** | **56.4 (after)** | |

No spread exceeds 20 points; the script raised no warnings.

### Target-Venue Scores (ICLR, scale status: secondary; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 3 / 2 (each 1–4) |
| Venue composite (ICLR emphasis) | 56.2 |
| Rating for the final decision (internal 3) | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval" to ICLR. The question of adapting to an unknown forgetting rate is natural, and the paper gives an explicit algorithm with a readable proof.

**Overall Assessment:**
The panel found the main proof chain correct and the ordering insight (a discounted-payoff guarantee valid for η ≥ ρ, used in descending discount order) elegant and honestly attributed. The panel was split on significance: two reviewers saw a clear, correct answer to a natural question, while two judged the contribution an incremental adaptation whose main rate may follow from existing results.

**Key Strengths Identified by Reviewers:**
1. The proof chain for Thm 1 and Thm 3 is correct as checked (R1, DA).
2. The ordering insight with η ≥ ρ and the explicit meta-algorithm (R1, R2, R3).
3. Clear organisation and honest attribution of building blocks (R3, R4, R2).

**Key Concerns Requiring Attention:**
1. The paper does not analyse whether strongly adaptive regret already implies Thm 3 via Abel summation (R2, DA; CONSENSUS-2, hinge).
2. The proof of Lemma 1, presented as new and complete, has an invalid final step and a hypothesis mismatch (R1, DA; CONSENSUS-2).
3. "Cost of adaptivity" and "novel analysis" are asserted without support (R1, R2, DA, R4; CONSENSUS-3).
4. Known horizon, oracle assumptions, and the vacuous τ restriction are not discussed; no sanity experiment (R1, R3, DA; CONSENSUS-3).

**Critical Challenge (Devil's Advocate):**
The strongest objection (rated MAJOR, no CRITICAL issue was raised) is the reduction above: if it holds, the open question has a short answer from known tools. It must be addressed directly.

**Decision: Borderline Reject (3).** *This is how a careful panel would likely see this draft, not a prediction of the outcome.*

The reasons to reject outweigh the reasons to accept mainly because of concerns 1–3. To change the assessment: show where the reduction fails or what SOGD provides that it does not; repair Lemma 1; give a lower bound or soften the "cost of adaptivity" claim; and enumerate the specific gaps in the earlier sketch. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Renata Valcourt-Imai
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Tightness / "cost of adaptivity" unsupported | R1, DA, R4 | CONSENSUS-3 |
| Overstated novelty language | R2, DA, R4 | CONSENSUS-3 |
| Known horizon, λ-range and oracle assumptions | R1, R3, DA | CONSENSUS-3 |
| No empirical sanity check | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the contribution significant enough? | R3, R4 | R2, DA | The EIC sides with the sceptics: the verified reduction and the incremental technique outweigh the clear question; R4's premise was overstated |

### Score Spread Discussion
No dimension exceeded the 20-point spread. The widest (16 points) are Novelty and Significance, which diverge on whether the reduction (I1) is taken into account; the EIC adopts the weighted view (49.1, 51.9).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Possible reduction from strongly adaptive regret | Yes, R2-W1 (R1 Q3) | n/a | n/a |
| DA-M2 | MAJOR | "Cost of adaptivity" unsupported | Yes, R1-W3 | n/a | n/a |
| DA-M3 | MAJOR | Lemma 1 proof | Yes, R1-W1 | n/a | n/a |
| DA-M4 | MAJOR | Narrower scope than "unknown discount factor" | Yes, R1-W4, R3 | n/a | n/a |
| DA-M5 | MAJOR | Unnamed "gaps and inaccuracies" | Yes, R2-W2 | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are issues the EIC verified as undermining the main claim's novelty or correctness. Ordered by impact on the decision.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Relation to strongly adaptive regret (Abel summation reduction) | R2-W1, DA-M1, R1-Q3 | §1, Thm 3 | Add a section deriving what the reduction gives (rate, range, anytime); show where it fails or say what SOGD adds | Medium (3–5 days, no compute) | Yes |
| R2 | Invalid step in Lemma 1's proof and hypothesis mismatch | R1-W1, ERR-1, ERR-2, DA-M3 | §4.5, Lemma 1 | Redo the final bound with U/n explicit; state the regime (Z = 1/T, T ≥ 8) | Low (1–2 days) | Yes |
| R3 | "Cost of adaptivity" and "novel analysis" unsupported | R1-W3, DA-M2, DA-M5, R2-W2 | Remark after Thm 3, §1.2, §4.5 | Lower bound, or soften; list the specific gaps in K&P §5; table of what is new | Low to High (wording low; lower bound high) | Wording yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Known T, anytime variant, λ-range (remove τ restriction) | R1-W4, R3-W3, DA-M4 | State extension to all λ ≤ 1−1/T; discuss doubling | Low | Yes |
| S2 | Imported inequalities; self-contained appendix | R1-W2, R4-W1 | Appendix with (24), (25), (28), (38), (39) and hypotheses | Low | Yes |
| S3 | Sanity simulation | R1-W3, R3-W1, DA-m1 | Piecewise-stationary experiment; plot regret against 1/(1−λ) | Low (CPU, about 1 hour) | Yes |
| S4 | Oracle model and per-round cost | R3-W2, R1-Q4 | State function-value and gradient calls per round | Low | Yes |
| S5 | Missing references `[verify]` | R2 | Discuss Cutkosky (2020) | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Links to adaptive filtering, discounted bandits, EMA optimisers | R3-W4 | Short discussion |
| N2 | "Open question" quotation | R2-W3 | Quote the sentence from Zhang et al. (2024) |
| N3 | Notation and typos | R4, R1, DA-m2/m4 | One definition of g and erf; ∇f_t; "Jensen"→convexity; typos listed above |
| N4 | Lemma 2 convention | R1 ERR-4 | Add the zero term |
| N5 | Krichene et al. (2014) relevance | R2 | Explain or drop |
| N6 | Limitations paragraph | R1, R4 | Add |

## Estimated Revision Effort
- Priority 1: 3 items, about 1–2 weeks (3–5 days for the reduction analysis, 1–2 days for the lemma)
- Priority 2: 5 items, about 2–3 days
- Priority 3: 6 items, about 1 day
- **Total estimated revision time**: about 2 weeks, with no GPU use
