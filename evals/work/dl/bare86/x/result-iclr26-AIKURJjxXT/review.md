# Review: EFRame — Exploration-Filter-Replay RL for deeper reasoning

(Figures are not available in the extracted text; figure-dependent claims are judged from captions and prose only.)

## Summary
The paper augments GRPO for RLVR on a multimodal LLM (Qwen2.5-VL-7B-Instruct) with three components.
1. **Additional rollout.** For prompts where all G1=5 regular rollouts fail, it samples G2=20 more at temperature 1.2.
2. **Online filtering.** It drops zero-advantage samples. In the additional rollout it keeps only positive samples, so over 95% of the extra samples are discarded.
3. **Replay buffer.** Samples with |advantage| > 1 are stored (size 5120) and replayed every 5 steps.

An entropy-dynamics argument (the natural-policy-gradient covariance result) motivates the design: rare high-advantage samples raise entropy, and replay lowers it again. The paper reports gains over GRPO and DAPO on Geometry3K (55.24 vs 50.75 and 49.09). On four out-of-domain math benchmarks the average gain over GRPO is +0.94 (55.13 vs 54.19). It also proposes a three-way taxonomy of samples (regular, high-quality, low-quality).

## Strengths
- The problem is well motivated: advantage vanishing on hard prompts, late-stage collapse in GRPO, and the cost of simply raising G.
- The method is simple, built on EasyR1/veRL, and code is said to be released.
- It reports wall-clock cost (Table 2: 1.35x GRPO per step), which is more candid than many comparable papers.
- The ablations (Fig. 5) ask a sensible question: is each of the three components needed? The finding that removing replay drops performance below vanilla GRPO is interesting if it holds up.
- Entropy, response-length and gradient-norm curves give some insight into training dynamics.

## Weaknesses
1. **Statistical rigor is absent.**
   - All results appear to be single runs, with no seeds, variances or confidence intervals.
   - The out-of-domain gain over GRPO is +0.94 on average, and over DAPO +0.68. On MathVision, GRPO (29.11) beats the proposed method (28.82). On MathVerse the margin over DAPO is 0.33.
   - These differences are within typical noise for RL fine-tuning and benchmark evaluation. The paper says GRPO and DAPO "occasionally" collapse, which makes single-run comparisons less reliable still.
   - The headline "36.5%" is a relative advantage over GRPO's *gain* (16.80 vs 12.31), not over GRPO's accuracy. "19.9% over GRPO" is likewise a ratio of gains over the base model. This framing inflates the effect: the absolute margin is about 4.5 points on Geo3K and under 1 point on average out of domain.
2. **Compute confound and missing baselines.**
   - The method costs 1.35x time per step. It also samples 20 extra responses on hard prompts (25 in total) and does replay updates.
   - There is no compute-matched baseline, such as GRPO with G=8–10 or GRPO at matched wall-clock or sample budget.
   - Fig. 1 compares only G=5 and G=20 to argue that larger G is inefficient. This is not the right comparison, because the method uses a large G only on hard prompts.
   - Baselines that attack the same issues are missing. These include DAPO dynamic sampling (which resamples when advantage is zero), difficulty-based curricula, LUFFY and other off-policy-guidance methods, and simple positive-sample or prioritized replay. Several are cited but not compared against.
   - The DAPO baseline appears to be a partial configuration (clip-higher plus a length penalty, with no mention of dynamic sampling).
3. **Narrow and unclear evaluation.**
   - Only one 7B model is used, and training is mostly on Geo3K. A "6k out-of-domain" training set is mentioned, but it is unclear which training data produced the "Ours" row in Table 1.
   - GRPO and DAPO rows are presumably the authors' own runs. The other 7B baselines are taken from other papers with different data and evaluation settings. The evaluation protocol (judge, prompts, decoding) is unspecified.
   - A maximum response length of 2048 is short for "deeper reasoning". Growth in response length is presented as improved reasoning without evidence.
   - The claim of "access to deeper reasoning capabilities that remain unattainable under vanilla GRPO" is not tested. There is no pass@k analysis, which is what the cited Yue et al. concern would call for. There is also no analysis of whether hard training prompts become solved, and no qualitative examples.
   - The title and abstract refer to LLMs, but there are no text-only experiments. The appendix concedes that gains on Math are "less pronounced".
4. **The theory is heuristic and partly misapplied.**
   - Theorem 4.5 is a tabular softmax NPG result taken from a blog post (Zhihu). The second citation renders as "?". It is applied to a transformer trained with clipped PPO-style updates. The qualitative extension is plausible but unverified, and the covariance term is never measured.
   - The explanation is internally awkward. High-advantage low-probability samples raise entropy, and replay lowers it. Yet Fig. 4 reportedly shows entropy rising later in training, and the paper presents this as desirable. Both entropy increase and entropy decrease are framed as beneficial, with no falsifiable prediction.
   - "Theorem 4.4" (advantages sum to zero) is trivial. As stated for the O_H and O_L subsets, it holds only before positive-only filtering.
   - The claim that high-advantage, low-probability samples "are more likely to have their gradients clipped" is asserted rather than measured.
5. **Correctness and bias issues in the replay and filtering design are not discussed.**
   - Training on positives only for hard prompts removes the negative gradient. The cited Zhu et al. argue that negatives are valuable. Claim 2 (negatives "mislead optimization") rests on train-versus-test curves from one run in Fig. 5. That reading is correlational and conflates "negatives from hard prompts" with "removing all filtering".
   - Replayed samples are off-policy but are used with ratios and clipping. It is not specified how the importance ratio is computed for them.
   - Sampling at temperature 1.2 changes the behaviour policy. The PPO ratio is presumably computed as if the samples came from temperature 1.0. This mismatch is not addressed.
   - With G2=20, a single positive has Â≈4.4, so the |Â|>1 criterion stores essentially every positive from hard prompts. The criterion is therefore not selective.
   - Geo3K's training set is small, so repeated replay of a limited set of hard problems could overfit. The in-domain gains may partly reflect this. No held-out analysis is given.
   - Definition 4.1 labels a prompt difficult after 5 failures. A prompt with pass rate 0.3 fails all 5 with probability about 17%, so the category mixes truly unsolvable and moderately hard prompts. The paper does not report what fraction of prompts triggers exploration, or how often it yields positives.
6. **Hyperparameter sensitivity and shallow ablations.**
   - Appendix B admits sensitivity to clip-higher, buffer size and replay frequency, saying the gradients must be "just perfect". No sensitivity study is shown.
   - Ablations are on one dataset and shown only as curves. There is no table, no pairwise combinations (e.g. exploration + replay without filtering), no replay-only variant, and no ablation of G2 or temperature.
   - "Without replay is below GRPO" suggests that the exploration module on its own is harmful, which also points to fragile tuning.
   - EFRame uses asymmetric clipping (ε_high) as DAPO does, but the GRPO baseline uses symmetric 0.2. The baseline is therefore not matched on a setting that the appendix calls important.
7. **Presentation.**
   - There is much promotional language ("systematic", "principled", "aha state", "reinforcement lottery"), and some typos ("distorb", "challanging", "avail able").
   - There are unresolved references ("?"), a duplicated DPO entry, and a blog post as the key theoretical source.
   - The sample taxonomy is billed as an analytical contribution, but it restates difficulty- and sign-based splits and is not analysed beyond the ablation curves.
   - Related-work coverage is thin.

## Questions
1. Can you provide at least 3 seeds with mean ± std for Geo3K and Table 1, and say whether GRPO/DAPO collapse occurs in all seeds?
2. How does EFRame compare with compute- or sample-matched baselines: GRPO with larger G or longer training, DAPO with dynamic sampling, and a simple positive-sample replay?
3. How are importance ratios computed for replayed samples and for temperature-1.2 samples? Is any off-policy correction applied?
4. What fraction of prompts is labelled difficult over training, what fraction yields positives, and how do these change as the policy improves?
5. Is there pass@k evidence (k up to 64 or more) that EFRame expands the set of solvable problems beyond the base model and beyond GRPO?
6. Can you measure the covariance term in Theorem 4.5 empirically, to test the entropy explanation?
7. Can you add results on another model family or scale, and on text-only math (e.g. MATH500, AIME)? What explains the weaker gains on Math?
8. How many unique hard prompts are in the replay buffer, and is there overfitting to them? What do held-out Geo3K results show?
9. How were the Table 1 numbers for the non-reproduced baselines obtained, and under what evaluation settings?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- **Rating: 4** (marginally below the acceptance threshold)
- Confidence: 4

The idea is reasonable and the practical recipe may be useful. But the evidence is thin: single runs, small out-of-domain margins, no compute-matched or strong baselines, and heuristic theory. As a result, the claims of "deeper reasoning" and improved stability are not established.
