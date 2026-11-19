# Review: DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains

(Figures were not available. Figure-based claims are judged from captions and text only.)

## Summary
The paper proposes a length-shaping reward for RL with verifiable rewards (DAPO on Qwen2.5-3B/7B, following the DeepMath-Zero recipe). The motivation is a preliminary study. Within a problem, pass@1 falls as response length grows, but pass@32 rises for longer responses. The authors conclude that length-minimizing rewards may shrink the reasoning boundary.

The method works as follows:
- Response length is standardized within each rollout group (z).
- The length reward is α·sigmoid(−β z), with β = P_g(x) − P_b. P_g is the group pass ratio and P_b is an EMA of the batch pass ratio, initialized at 1.0.
- Problems easier than the batch average (β > 0) reward shorter responses. Harder ones (β < 0) reward longer responses.
- The length reward is applied only to correct responses.

On seven math benchmarks, DeepCompress-Zero-3B and -7B are reported to beat DeepMath-Zero by +2.0 and +2.7 average points. Average response length is reported to fall by 57.9% (3B) and 16.6% (7B). Ablations with fixed β = ±1, entropy curves and a GPT-4o-based reflection analysis are offered as support.

## Strengths
- The problem is timely: efficiency without accuracy loss, and avoiding blanket length penalties.
- The idea is simple and cheap. It needs no extra rollouts or annotations, because difficulty comes from statistics GRPO/DAPO already computes. It is easy to reproduce, and the hyperparameters are listed (α = 0.2, λ = 0.99).
- Accuracy and length move in the favorable direction together. The 7B gains on AIME24/25 are sizeable. The training and test dynamics (Fig. 4) are informative.
- The difficulty signal is relative and model-aware, so it needs no fixed labels. The EMA smoothing and the correctness-gated length reward are sensible design choices.
- The limitations paragraph honestly notes the 10k training cap.

## Weaknesses
1. **The gains are not attributed to the proposed reward.**
   - The only reference is the DeepMath-Zero checkpoint. DeepCompress is trained with a 10K max response length and a 2K overlong buffer, and evaluated at 32K. The paper does not say what cap or step budget the DeepMath-Zero baseline used.
   - A model trained under a hard cap with an overlong penalty may get shorter by itself. The essential control is missing: the same DAPO run (10K cap, 500 steps, same checkpoint selection, same chat template) with no length reward.
   - Without it, neither the compression nor the accuracy gain can be credited to the dual reward.
2. **No comparison with efficiency baselines.**
   - The paper positions itself against length-penalty RL (Kimi 1.5, L1, Arora & Zanette, etc.) and SFT-based compression. None of these is run.
   - Open-Reasoner-Zero and SimpleRL-Zoo are accuracy baselines only. The "new SOTA" and "outperforms all baselines across all seven benchmarks" claims rest on one non-efficiency baseline.
   - The second claim is also not literally true: 7B on MATH-500 is a tie (85.6 vs 85.6).
   - Efficiency is shown only against DeepMath-Zero, not as accuracy-vs-length trade-off curves against other methods.
3. **Statistical rigor.**
   - There is a single run per model and no seeds or confidence intervals. Many gains are 1–2 points, within the usual noise of AIME (30 problems) and other small benchmarks.
   - The checkpoint is chosen from 500 steps using a 120-question validation set that includes AIME 2022–23. It is unclear whether baselines got the same selection, which would favor DeepCompress.
4. **The ablations are thin and partly contradict the framing.**
   - The fixed Length Bonus variant has higher test pass@1 than DeepCompress (Fig. 4c, per the text). In Table 2 it has lower pass@1 on the hard set (11.89 vs 13.81), so the two analyses point in different directions and neither is explained.
   - Ablations are on 7B only. The paper reports no test of the Hard/Simple assignment (e.g., random or flipped sign), unconditional vs conditional reward, EMA vs raw P_b, or sensitivity to α and λ.
   - The "robustness" motivations in Section 4.4 are therefore untested.
5. **The preliminary study is weak.**
   - Pass@32 is computed within bins of within-problem standardized length. This conflates truncation and looping in the long tail, uneven per-problem contributions, and a conditional-subset effect. It does not show that long responses "contain a wider coverage" of solutions, and it is not the pass@k of any policy.
   - The trend fails on 7B AIME25 and is rescued post hoc with k=64. No bin sample sizes or CIs are given.
   - The jump to "length-penalty RL restricts the reasoning boundary" is untested. The paper never reports pass@k at large k for the final models.
6. **Mechanism concerns in the design.**
   - "Hard" is relative to the batch mean, so about half of every batch is always "Hard" regardless of absolute difficulty.
   - With P_b initialized at 1.0 and λ = 0.99 (time constant about 100 steps), P_b stays far above the true value early on. Nearly all problems get β < 0, which is effectively a length-bonus phase. This probably produces the "initial increase" in length and is partly an artifact of the schedule.
   - |β| = |P_g − P_b| is typically small and α = 0.2, against outcome rewards of ±1. The paper shows no distribution of β or realized R_l, so it is unclear how such a small term produces a 58% length reduction. This again suggests the cap or overlong penalty is the driver.
   - The length reward is applied only to correct responses, and hard problems have few of them. The "exploration" signal acts on very few samples.
   - The central claim, that the model allocates length by difficulty, is never measured. A plot of length vs. problem difficulty (MATH level, DeepMath difficulty) against the baseline is missing. Fig. 3 suggests compression across all benchmarks, including AIME.
7. **Overreaching mechanistic claims.**
   - "Encourages high policy entropy, leading to superior performance" is correlational. The paper itself notes that the bonus variant has higher entropy.
   - The reflection analysis uses an unvalidated GPT-4o judge whose prompt asks it to "actively identify and emphasize" behaviors. Differences are tiny (2.64 vs 2.59 for 7B) and have no variance.
   - The hard set is defined by base-model failures. Only the Reflect count is reported although four behaviors were tracked.
   - "Smarter thinking" is not supported.
8. **Scope.** The study covers math only, Qwen2.5 base models only, 3B and 7B only, and one RL algorithm and data recipe. It includes no larger models, other families, code or science tasks, or distilled reasoning models (the main setting of efficiency work). Behavior beyond the 10K training cap is not analyzed, and efficiency is measured only as mean response length.
9. **Presentation.**
   - The text has many typos ("infeasbile", "diffifulty", "Lentgh") and inconsistent Simple/Easy wording.
   - β is both a hyperparameter and a per-sample quantity, and R_z/R_l are overloaded.
   - The language is overstated ("perfectly", "intelligently", "simultaneous optimality").
   - Key details are missing: baseline training budget, how the bins were formed, and exact length tables.

## Questions
1. What does the same DAPO recipe give with the same 10K cap, overlong buffer, 500 steps and checkpoint selection, but no length reward? What cap and steps did DeepMath-Zero use?
2. How does DeepCompress compare, at matched budget and as accuracy-vs-length curves, with at least two published length-penalty RL methods?
3. What are the distributions of β and the realized R_l over training? How do results change with λ = 0 or 0.9, or with P_b initialized from the first batch?
4. Can you ablate each component (conditional reward, EMA, β sign, α) and include the 3B model?
5. Does the model use more tokens on harder problems than on easier ones at test time, compared with the baseline?
6. Does DeepCompress improve pass@k at large k (e.g., 256 on AIME) over DeepMath-Zero? That is the claimed boundary expansion.
7. Can you report standard deviations over seeds? Was validation-based checkpoint selection applied identically to all baselines?
8. Why does the Length Bonus variant reach higher test pass@1 than DeepCompress, and what is the accuracy-length trade-off between them?

## Ratings
- **Soundness: 2.** The attribution of gains is not controlled, there is a single seed, and the mechanistic claims are not directly tested.
- **Presentation: 2.** The paper is understandable but has many typos, overstated language and missing details.
- **Contribution: 2.** The idea is simple and of modest novelty, and the evaluation scope is small.

**Rating: 4** (marginally below the acceptance threshold). The idea is reasonable and the results are encouraging. The key controls are missing: a no-length-reward baseline with the same cap, comparisons with existing length-penalty methods, component ablations, and seeds. As a result the main claims are not established. Those claims are that the dual reward is what improves both accuracy and efficiency, and that it adapts length to difficulty.

**Confidence: 4**
