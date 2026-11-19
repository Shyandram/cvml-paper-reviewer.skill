# Review: Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling

(Text-only review. Figures were not available, so the empirical claims are judged from captions and prose.)

## Summary
The paper studies "Pass@k inference". Given N samples from a reference policy, an imperfect reward model r̂ and a budget of k submissions, the goal is to minimise regret against the best of the k submitted responses. It makes three theoretical claims.
- (Weighted) majority voting has constant regret on some hard instances (Thm 4.1).
- Best-of-N has regret Ω(min{1, √(Nε²_RM/k)}) on some instances (Thm 4.2), so neither method is "scaling-monotonic".
- The proposed Best-of-Majority (BoM) first drops responses whose empirical frequency is below α ≈ 3/(4C*), then takes the top-k by r̂. For N ≳ C* log(kC*/ε²_RM) it achieves regret ε_opt + O(√(C*ε²_RM/k)) (Thm 5.1). A matching lower bound is given for C* ≥ 2k (Thm 6.1).

Experiments use Qwen3-4B and Qwen2.5-Math-1.5B with the AceMath-7B-RM reward model on GSM8K, MATH-500 and AIME24. BoM is reported to be better than or equal to majority voting and BoN for small k, and more stable as N grows.

## Strengths
- The Pass@k selection problem is natural and relevant to current practice. Prior theory (Huang et al. 2025) covers only k = 1, so adding k as a parameter is a sensible extension.
- BoM is simple and well motivated by pessimism: trust r̂ only where π_ref has enough mass. The upper-bound proof is clean. Eq. 5.1 turns the on-policy L2 reward error into a bound on the minimum error over the k selections, with a 1/√k gain.
- The binning argument for the lower side of the sandwich event E is a neat way to avoid depending on |Y|. I checked the constants for P(¬E) at the stated N and they work out (5C*e^{-N/(32C*)} ≤ 5√(C*ε²/k)).
- Upper and lower bounds have the same form in (C*, ε_RM, k, ε_opt). The hard instances for majority voting and BoN are explicit and show the failure modes clearly: many mid-probability wrong answers hurt voting, and over-optimisation of r̂ hurts BoN.
- The experiments directionally support the theory. BoN degrades with N, and BoM is more stable.

## Weaknesses
1. **The 1/√k "scaling" is limited in scope and partly trivial.**
   - Under Assumption 3.2, C* = 1/π_ref(y*), and the filtered set Ŷ_α contains at most about 4C*/3 responses (α = 3/(4C*)). Once k ≳ C*, BoM returns the whole filtered set, which contains y* with high probability and has zero regret, with no reward model needed.
   - The lower bound requires C* ≥ 2k. So the 1/√k law only concerns k < C*. The paper does not say that outside this window the problem reduces to covering.
   - The bound √(C*ε²_RM/k) is also vacuous whenever C*ε²_RM ≥ k, which is common when C* is large (hard problems, the stated motivation).
   - "Minimax optimal" is therefore a statement about one worst-case family, up to constants and log factors. The N requirement in Thm 5.1 (N ≳ C* log(kC*/ε²)) is not matched by a sample-complexity lower bound. Calling the scheme "optimal scaling with N" is too strong.
2. **The assumptions are strong and far from LLM practice.**
   - They assume a unique y* with r* = 1, and ε_RM is measured on-policy under π_ref, with the coverage C* = 1/π_ref(y*) equal to the inverse probability of the single correct response. For math, "responses" are only meaningful after clustering final answers, which the experiments do and the theory does not model.
   - Assumption 3.2 makes ε_opt a free additive term. The lower-bound Ω(ε_opt) is nearly definitional.
   - BoM needs α ∝ 1/C*, which is unknown per prompt. No procedure for estimating or adapting it is given. The experiments simply use α = 0.005 or 0.015 (with N = 100, 500 or 2000), so the "theory-derived threshold" is not what is used.
3. **The scaling-monotonicity definition does not support the claims made about it.** Definition 3.4 says only that regret ≤ δ for N ≥ N0 when ε_RM is small enough. It does not say that performance never degrades as N grows, yet the abstract and Section 3 state that BoM's "performance does not degrade when increasing N". An upper bound that holds for N ≥ N0 is not monotonicity in N. The "No" entries for majority voting and BoN in Table 1 rest on single constructed instances. The table's "Unknown" for BoN's k-scaling shows the BoN analysis is incomplete: the gap to the lower bound is 1/√k, and the paper itself only conjectures that BoN cannot match BoM.
4. **Technical novelty is modest.** The proof is the pessimism filter plus Chernoff and a union bound over bins, plus Cauchy–Schwarz as in Huang et al. 2025. The lower bound is a standard two-point/multi-hypothesis construction. I did not see the proof of Thm 6.1 in the provided text, only its statement, so I cannot verify it. Appendix typos such as "≤ 1 − |Y|e^{…}" in (A.2) suggest the proofs need a cleanup.
5. **The empirical evaluation is thin and does not clearly validate the theory.**
   - There are no confidence intervals, seeds or repeated resamplings of the N trajectories. AIME24 has only 30 problems, so differences of a few points are within noise.
   - α appears tuned per setting, with no sensitivity analysis and no statement of whether it was tuned on the test sets.
   - The caption of Fig. 1 itself concedes that BoM only "matches" the baselines for larger k and on GSM8K. On Qwen2.5-1.5B, majority voting seems competitive for larger k. Claims such as "consistently outperforms" are overstated.
   - Baselines are weak. Weighted majority voting, which Thm 4.1 covers, is not evaluated. Aggregating rewards over answer groups by sum or max, rather than the mean used here, is not compared. Both are standard and cheap. Simple variants of BoN, such as the pessimistic or smoothed versions the paper cites, are also missing. Without them it is unclear that the frequency filter is what helps.
   - "Majority voting remains low, consistent with Thm 4.1" confuses a worst-case lower bound with an empirical observation. Majority voting's low top-k accuracy for k > 1 is expected for any method that picks near-duplicate-probability answers, and does not demonstrate constant regret. Likewise, BoN's degradation with N is attributed to reward over-optimisation, but this is not tested (e.g. with a reward model of varying quality).
   - Pass@k for k ≤ 10 on a handful of benchmarks with one reward model is a narrow test.
6. **Practical relevance of the setting is unclear.** The Pass@k "submission" assumes a verifier-free selection of k answers to be judged by an oracle, which is not the usual deployment. The cost analysis ("fewer reward evaluations") is asserted but not measured, and the paper does not discuss when k distinct answers are available at all (AIME-style problems often yield fewer than k distinct clusters).
7. **Presentation.** Section 3 says that "different from the settings where the model is allowed to generate and submit k candidate responses", which reads backwards. Table 1 mixes worst-case instance lower bounds (majority voting, BoN) with upper bounds (BoM), which is not a like-for-like comparison. There are several typos.

## Questions
1. What happens to the result when k ≳ C*? Please state explicitly that BoM is then reward-free, and whether the √(C*ε²/k) term matters in any non-trivial regime where it is below 1.
2. How should α be chosen without knowing C*? Please show sensitivity of the experimental results to α, and say how it was selected (held-out prompts?).
3. Can you add error bars and multiple sample resamplings, plus weighted majority voting and sum/max-aggregated BoN baselines?
4. Can you give a BoN upper bound for Pass@k, or a lower bound that really separates BoN from BoM at N = Θ̃(C*)? Currently the only BoN separation comes from large N.
5. How do the results extend when the answer space is continuous or semantic (code, open-ended generation), where the empirical frequency of an exact response is useless?
6. Please give a proof or sketch for Thm 6.1 in the main text, and clarify the regime of N in which the lower bound holds.

## Ratings
- Soundness: 3
- Presentation: 2
- Contribution: 2

**Rating: 4** (borderline reject)

**Confidence: 3**

The idea is clean and the upper bound is correct as far as I checked. Even so, the claimed optimality and monotonicity are narrower than advertised, the theoretical novelty over Huang et al. 2025 is incremental, and the empirical evidence is weak and noisy.
