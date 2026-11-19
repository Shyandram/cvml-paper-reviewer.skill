# Review: Discounted Online Convex Optimization: Uniform Regret Across a Continuous Interval

(Text-only review; the figures are schematic diagrams and I judged them from captions and text.)

## Summary
The paper studies λ-discounted regret in OCO when λ is unknown. It makes three contributions:
1. It shows that OGD with step size η ∝ √(1−λ) achieves discounted regret O(1/√(1−λ)) (Thm 1). This matches Zhang et al. (2024) up to constants.
2. It extends the analysis of DNP-cu (Kapralov & Panigrahy; Zhang et al. 2022a) to discounted payoffs (Thm 2). The bound (13) holds for any η ≥ ρ, while (14) is the ρ-discounted bound.
3. It runs the "Smoothed OGD" (SOGD) construction of Zhang et al. (2022a): a chain of OGD experts on a geometric grid of λ's, combined sequentially by DNP-cu in descending λ order. It obtains a bound of O(√(log T/(1−λ))) that holds simultaneously for all λ ∈ [1−1/τ, 1−1/T] (Thm 3). The extension from the grid to the continuum uses Lemma 20 of Kapralov & Panigrahy.

This answers an open question left by Zhang et al. (2024).

## Strengths
- The question is clean and well motivated, and the open problem is stated explicitly in prior work.
- The central observation is neat. Because (13) holds for any η ≥ ρ, one DNP-cu with parameter ρ controls payoff under all larger discount factors. This is what lets one chain experts whose performance measures differ, and it explains why the descending ordering matters.
- The main proof skeleton is correct. I checked the following steps and found them right: Theorem 1 including constants; the decomposition (32) into α_k, β and γ; the signs in (17)/(18) and (33)/(35); the grid-to-continuum argument via Lemma 2 and (37).
- The authors are upfront that the idea comes from Kapralov & Panigrahy and that SOGD comes from Zhang et al. (2022a).
- The paper is short and readable.

## Weaknesses
1. **Novelty and significance are limited, and a simpler route appears to give the same bound.**
   - The paper itself notes that adaptive regret plays an analogous role. In fact, strongly adaptive regret seems to imply uniform discounted regret by a short Abel-summation argument. Write s_t = f_t(w_t) − f_t(w) and S_k = Σ_{t≥k} s_t. Then Σ_t λ^{T−t} s_t = λ^{T−1} S_1 + Σ_{k≥2} (λ^{T−k} − λ^{T−k+1}) S_k.
   - All coefficients are nonnegative and sum to at most 1. If an algorithm has adaptive regret O(√(|I| log T)) on every interval I, which SOGD already provides (Zhang et al. 2022a; also Daniely et al. 2015 and Jun et al. 2017 up to logs), then each S_k is O(√((T−k+1) log T)). Averaging against the geometric weights gives O(√(log T/(1−λ))) for all λ simultaneously. No grid, no Lemma 2 and no new DNP analysis is needed.
   - If this reduction is right, Theorem 3 is a corollary of known results. The paper's "technical challenge" claim (§1.1) that existing adaptive-regret machinery cannot handle an unknown λ is then too strong.
   - The authors must either show why this reduction fails or compare against it. The claimed novelty would otherwise reduce to "a self-contained discounted analysis".
2. **Proof gap in Lemma 1 (Section 4.5).** The final step bounds g(U(n)−8) ≤ e^{(64−16U)/(16n)} ≤ e^{(64−16U)/512}, "due to n ≥ 32". This inequality goes the wrong way. Since 64−16U < 0, a larger n makes e^{(64−16U)/(16n)} larger, so the bound is valid for n ≤ 32, not n ≥ 32. The constant 1.4648 is computed at n = 32 and does not follow for larger n. The lemma is probably salvageable, because U(n)(1−g) grows with n through U ~ √(n log(1/Z)). But the proof as written is invalid, and it is the paper's claimed "novel and complete" replacement for a gap in prior work. The paper's own claim that earlier proofs had "gaps and inaccuracies" makes this more significant.
3. **Sloppy constants and conditions.**
   - Lemma 1 assumes U(n) ≥ 20 while Theorem 2 assumes U(n) ≥ 22.
   - (31) writes "min 1/(1−λ_i) = N" where T/2^N is meant.
   - The step "U(n) ≥ 4√32" uses n ≥ 32, but the stated conditions only give n ≥ 8e ≈ 21.7.
   - The grid depends on T, while the bound is applied at prefixes j ≤ T in the continuum extension. This is fine but should be said.
   - The abstract states the bound as O(√(log T)/(1−λ)); the correct form is O(√(log T/(1−λ))).
   - Section 4.1 writes ‖f_t(w_t)‖ where ‖∇f_t(w_t)‖ is meant.
   These are individually minor but together reduce confidence in the Theorem 2 / Lemma 1 machinery, which is where the claimed novelty lies.
4. **The proofs of Theorems 2 and 4 are largely inherited.** They adapt Zhang et al. (2022a) and import (28), (38), (39) and (24)/(25) by citation. A reader cannot verify the new analysis without the earlier paper. The genuinely new content is the step (41) → (42), which is short.
5. **Restricted scope and no optimality discussion.**
   - There is no lower bound or discussion of whether the √(log T) price of adaptivity is necessary.
   - The range [1−1/τ, 1−1/T] needs τ = Ω(log T), so very short effective windows are excluded.
   - The losses are assumed bounded in [0, GD]. The algorithm needs T in advance (the grid and Z = 1/T depend on T), and an anytime version is not discussed.
   - The cost is O(log T) OGD experts plus O(log T) DNP-cu instances per round. Per-round cost and memory are not discussed.
6. **No empirical evidence.** There are no experiments, even though the stock-prediction motivation is never evaluated. A small simulation comparing SOGD to OGD with a misspecified λ would help. For ICLR a purely theoretical paper is acceptable only if the contribution is strong, and here it is incremental.
7. **Related work is thin.** The paper does not compare to the strongly-adaptive reduction above, or to universal methods (MetaGrad, Zhang et al. 2022b) that could in principle track λ.

## Questions
1. Does the Abel-summation reduction from strongly adaptive regret of SOGD to uniform discounted regret (Weakness 1) hold? If so, what does Theorem 3 add beyond a self-contained proof?
2. Can you fix the n-direction error in Lemma 1 (Weakness 2)? Which constants change?
3. Is the √(log T) factor necessary? Is there a matching lower bound for unknown discount?
4. Can the T-dependence be removed (anytime), and can τ be taken below log T?
5. Does the result extend to gradient-adaptive bounds as in Zhang et al. (2024), or to exp-concave and strongly convex losses?

## Ratings
- **Soundness: 2.** The core argument is largely right, but there is an invalid step in Lemma 1 and several inconsistent constants.
- **Presentation: 3.** The paper is clear but has typos and imports many steps by citation.
- **Contribution: 2.** It is incremental over Zhang et al. (2022a) and Kapralov & Panigrahy, and possibly a corollary of adaptive-regret results.
- **Rating: 4** (marginally below the acceptance threshold).
- **Confidence: 4.**
