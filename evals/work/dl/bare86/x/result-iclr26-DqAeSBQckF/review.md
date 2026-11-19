# Review: BLISS — A Lightweight Bilevel Influence Scoring Method for Data Selection in LM Pretraining

(Based on the main text and captions only; figures were unavailable. I read pages 1–10 and the reference list. I did not read the appendix material in detail.)

## Summary
The paper proposes BLISS, a data selection method for LM pretraining that avoids external pretrained "oracle" models. A small proxy LM is trained on training data weighted by a softmax over a small score model's outputs. The lower-level loss is weighted CE + γ·KL(proxy‖LLM) + weight decay. The score model is the upper-level variable and is trained on validation loss (LAMBADA) via a hypergradient. This uses a 3-step GD solve of the Hessian linear system and a stochastic approximation of the softmax normalizer. The score model then scores the shard and the top 20% is selected. The target LLM is trained in rounds (5 rounds × 10k steps, 25B tokens). The proxy is reset each round and the score model is carried over. Experiments pretrain Pythia-410M/1B on C4, plus 2.8B and LLaMA-0.5B in smaller setups. The main tables compare only with Random and MATES. Claimed results: +0.2 avg accuracy over MATES at 410M, +0.4 at 1B (47.9 vs 47.5), a "1.7× speedup" to reach MATES' accuracy at 1B, and +1.4 at 2.8B after three rounds. BLISS also uses slightly fewer total FLOPs than MATES at 1B.

## Strengths
- Reasonable motivation: selection that is self-contained (no GPT-style raters, no legal or dependency issues) and that targets the converged proxy's validation loss rather than a one-step influence.
- The bilevel formulation is clean. The KL term tying the proxy to the target LLM is sensible and has an ablation.
- The cost accounting (Table 4) includes warm-up, selection and inference, which is more honest than reporting selection cost alone. The setup is end-to-end multi-round pretraining at several model sizes, plus a second architecture (LLaMA).
- Standard errors are reported, and there are ablations (bilevel vs single-level, softmax, KL, proxy size, validation set).

## Weaknesses
1. **The gains are small relative to the noise, and there is no seed variance.** In Table 1 the 410M average gain over MATES is 0.2 points (45.9 vs 45.7), while per-task standard errors are 1.0–2.1 points and the average's s.e. is ~1.3. At 1B the gain is 0.4. BLISS is worse than MATES and/or Random on several tasks (ARC-C, LogiQA, BoolQ at 1B; ARC-C, OBQA, BoolQ at 410M). The 2.8B (49.0 vs 47.6) and LLaMA (45.65 vs 45.01) gaps are also single-run and close to the reported s.e. Differences of 0.2–0.6 points of average accuracy on tasks near chance (ARC-C, LogiQA, WinoGrande) cannot support "consistently outperforms". Multiple seeds or paired significance tests are needed.
2. **The "1.7× speedup" claim comes from curves with tiny separation and is not rigorously defined.** It is read off Figure 2 on a ~1 point accuracy axis, from a single run, with no confidence band, against one baseline (MATES). It is a speedup in LLM training steps/FLOPs, not total cost, and is only claimed at 1B.
3. **Inconsistencies in the reported numbers.** In Table 1 the 1B BLISS row lists FLOPs "8.08", which is the 410M figure; Table 4 gives 19.53. The text says "2.8B" while Section 5.2 says 2.5B parameters. In Table 2 the "Round 1 (Random)" rows differ (MATES 45.9 vs BLISS 45.2) although both are random warm-ups. That implies run-to-run variation of ~0.7 points, as large as many claimed improvements. In Table 5 the BLISS row has a different per-task profile from Table 1 (HellaSwag 36.0, below both ablations), and its 0.5–1.1 average gaps are again within noise. The "9.3% boost on LogiQA" from KL needs context against s.e. 1.7.
4. **The baseline framing is questionable.** The paper argues that existing methods "require external pretrained models", but MATES, the main baseline, also trains from scratch with an oracle influence from the current LLM and does not use external LLM raters. The novelty then reduces mostly to "long-term" vs "one-step" influence, and the paper does not show that this is the source of the gain. The proxy is trained for ~3,000 steps on 0.1% of a shard, so "trained to convergence" is not literally satisfied; Figures 6–7 reportedly show losses rising again. DsDm, LESS, QuRating, DSIR and SemDeDup are named as baselines, but Tables 1–3 report only Random and MATES. QuRating would be the natural comparison for the "external model" claim.
5. **The validation signal overlaps with the evaluation tasks.** Selection is tuned on LAMBADA (and ARC-E/SQuAD/PIQA in ablations), while evaluation includes ARC-E and PIQA. Leakage or overfitting to the evaluation tasks is not discussed in the main text. The method is "from scratch" only with respect to the model; it still uses downstream-aligned validation data, which is its own kind of oracle.
6. **The method is under-specified and loosely justified.** The softmax denominator over N samples is replaced by a partial sum over a subset (details only in the appendix), which changes the objective and the hypergradient. Equation (5) and line 11 of Algorithm 1 are different approximations, with single/multi-step proxy updates depending on model size and only 3 GD steps for the Hessian-inverse term. The algorithm run is therefore not the one analyzed, and there are no convergence statements or empirical checks of hypergradient quality. The lower-level problem is non-convex, so the implicit-gradient formula does not apply as stated. Nor is there any analysis of what is selected (domain, length, perplexity, duplication), so it is unclear whether the score model captures "influence" or simple surface features.
7. **Compute fairness.** BLISS inference over the dataset (1.53) exceeds MATES' (1.46). At 410M total FLOPs are essentially equal (8.08 vs 8.11), so "fewer FLOPs" holds only at 1B, and depends on MATES' oracle-collection settings. Wall-clock or GPU-hours are not reported. A cheap baseline using the same proxy (e.g., perplexity- or loss-based selection) is missing.
8. **Scale and scope.** The largest run is 2.8B with 15B tokens on data selected for a 1B model. Only C4 and top-20% selection are used, evaluation is zero-shot near chance for these sizes, and no held-out perplexity or other corpora (e.g., FineWeb/DCLM) are shown. "State-of-the-art" is overstated.

## Questions
1. Can you report mean ± std over at least 3 seeds for BLISS and MATES, with a significance test? What causes the 0.7-point round-1 gap in Table 2?
2. How exactly was the 1.7× computed? Please give the end-point accuracy at 50k steps, the interpolation and uncertainty. Does it hold at 410M?
3. Please add QuRating, DSIR, DsDm, LESS, SemDeDup and a same-proxy loss-based baseline under identical FLOPs accounting.
4. Is the benefit due to long-term bilevel optimization or just a learned scorer trained on validation loss? An ablation on the number of lower-level steps (including one step) within BLISS would help.
5. How sensitive are results to the validation set, in particular one with no overlap with any evaluation task? Please report all nine tasks.
6. What does the partial-softmax approximation do to the objective (subset size, γ, top-20% ratio, reset schedule)?
7. Please fix and explain the 1B FLOPs entry in Table 1, 2.5B vs 2.8B, and Table 5 vs Table 1 per-task values.
8. What does the selected data look like, and how does it differ from MATES' selection?

## Ratings
- Soundness: 2 (the idea is plausible, but the evidence is within noise and the algorithm is loosely tied to the formulation)
- Presentation: 2 (numerical inconsistencies, key details in the appendix, overclaiming wording)
- Contribution: 2 (incremental relative to MATES and bilevel reweighting work; modest empirical gain)

**Rating: 4** (marginally below the acceptance threshold)
**Confidence: 4**
