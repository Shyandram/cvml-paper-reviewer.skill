# Review: Circuit Insights: Towards Interpretability Beyond Activations (ICLR 2026)

## Summary
The paper builds on transcoders, which split feature attributions into an input-dependent activation and an input-invariant weight connection. It proposes two methods.
- **WeightLens** describes a transcoder feature from weights alone. It projects the encoder vector through the embedding matrix and through earlier-layer decoders, and takes z-score outlier tokens. It keeps only tokens that actually activate the feature in a forward pass. It optionally adds outlier tokens from the decoder-to-unembedding projection, and lemmatizes the result.
- **CircuitLens** uses transcoder and attention-head attributions (Jacobian-corrected, following Ameisen et al.). It masks inputs down to the tokens that contribute to the activation. It clusters sampled activations by Jaccard similarity of their contributor sets (frequency filter plus DBSCAN). It then has GPT-4o-mini describe each cluster and merge the descriptions. It also uses inverse-frequency quantile sampling over the whole activation distribution instead of top-k examples.

Evaluation uses the FADE metrics (Clarity, Responsiveness, Purity, Faithfulness) on about 250 features in each of 4 layers of Gemma-2-2b transcoders, against Neuronpedia and MaxAct* descriptions. The paper reports that:
- WeightLens matches or beats the baselines on Clarity and Responsiveness, but not on Purity.
- 25–59% of features receive a validated token-based description.
- CircuitLens gives mixed gains over the baselines, with its clearest gains in Clarity at layers 12 and 21.

## Strengths
- The motivation is good. Auto-interp pipelines depend on explainer LLMs and large datasets, and use only activations. Using transcoder weights and circuit attributions to reduce that dependence is a worthwhile direction.
- WeightLens is simple, cheap and needs no LLM. The finding that a lemmatized token list can match LLM descriptions on some FADE metrics is interesting and informative. It is also a useful diagnostic of how much of the feature space is token-level.
- The layer-wise analysis is informative: token-based coverage differs by depth and by model (Fig. 3), and the circuit-cluster counts per layer are reported (Fig. 8).
- Circuit-based clustering and masking to attention-contributing tokens is a sensible, new way to attack the "vague description" problem. The qualitative examples (L12F619, L21F91) are suggestive.
- The paper is candid that Faithfulness is uniformly low and that Purity favours baselines.

## Weaknesses
1. **The headline claims are stronger than Tables 1 and 2 support.**
   - "Matches or exceeds" holds only for Clarity and Responsiveness. Purity is clearly worse for WeightLens in layers 0–12 (0.02–0.03 vs 0.07–0.10 in Table 1). Faithfulness is about 0 for every method.
   - Clarity is the only metric where WeightLens clearly wins, and no variance is reported. The gaps are small in layers 0–12 and look larger only at layers 12 and 21 (the latter having a much higher Responsiveness baseline).
   - In Table 2, CircuitLens on the full-distribution sample is below the baselines in some places. Clarity at layer 7 is 0.39–0.44 vs 0.44–0.48, and Responsiveness is lower in 3 of 4 layers.
   - The strongest CircuitLens results are the "(top)" variants, which use the same top-activation sampling as the baselines. This undercuts the central argument that full-distribution sampling is better. The paper itself says full-distribution sampling gave worse numbers.
   - The text says the circuit approach "uncovers complex patterns invisible to activation-only methods", but the quantitative evidence is modest and mostly in Clarity.
2. **Evaluation scale and rigor are thin.**
   - There are ~250 features per layer, 4 layers, and one model (Gemma-2-2b) for the main metrics. GPT-2 and Llama are used only for coverage statistics.
   - There are no confidence intervals, seeds or significance tests. Differences of 0.01–0.05 are discussed as meaningful.
   - It is unclear how features are selected. They may be random, or they may include dead features.
   - The FADE metrics are LLM-in-the-loop (the evaluator generates synthetic data from descriptions). The method is therefore not LLM-free in evaluation, and the evaluator's behaviour on a token list vs a sentence may favour one form. No human evaluation is included.
3. **Selection bias in the WeightLens comparison.**
   - WeightLens describes only features that pass validation (25–59%). It is unclear whether Table 1 compares baselines on the same subset or on all ~250 features.
   - If the comparison is on the validated subset, which is the easy, token-like set, then "matches or exceeds on context-independent features" is close to circular. Baselines would be expected to do well there too.
   - Conversely, if the baselines are scored on all features and WeightLens only on its subset, the comparison is unfair. This needs to be stated precisely, and results on the covered and uncovered subsets should be reported separately. Fig. 4 suggests the baselines are also poor on non-token features, which does not show that weights add value there.
4. **Methodological justification is weak.**
   - Assumptions 1 and 2 are asserted, not tested. A z-score outlier threshold (its value, and its sensitivity) is not justified for non-Gaussian projections.
   - The "validation" step (keep a token only if it activates the feature in a forward pass) reintroduces dataset or activation dependence. This weakens the claim of needing no data.
   - The "semantically aligned" part of Assumption 2 is not operationalised.
   - The RoPE explanation for the mid-layer drop in token-based features is speculative and untested. For example, no ablation compares models, positional schemes or transcoder training choices.
   - Attention attributions treat the attention pattern as frozen, but the ones used here are linear approximations. There is no check that the selected head–token pairs are causally important (e.g. ablation or patching). The "circuit" claims are therefore purely attributional.
5. **Circuit-clustering is under-evaluated.**
   - There is no evaluation of cluster quality: no comparison with embedding-based clustering (which the paper dismisses without experiments), no human judgement, no ablation of ρ, DBSCAN parameters or the number of samples.
   - Fig. 8 shows cluster counts, but not whether more clusters correspond to real polysemanticity, as opposed to noise or hyperparameters. The authors admit layer 12 needs "more careful hyperparameter tuning".
   - Combining WeightLens and CircuitLens is described as improving robustness, but the gains are small and again lack variance.
   - Attributing the improvement to the method vs to the GPT-4o-mini prompt change (supplying masked patterns rather than activations) is not separated. A prompt-matched baseline is missing.
6. **Faithfulness and output analysis.**
   - Faithfulness is about 0.00–0.04 everywhere, so it provides no discrimination. The explanation (distributed concepts) is plausible but untested.
   - The output-centric component is costly, and the paper itself drops it from the circuit experiments. Its benefit is shown only anecdotally.
   - The proposal to modify the metric for circuits is not carried out.
7. **Baselines are limited.** There is no comparison with other weight-based or logit-lens-style interpretability (e.g. direct vocab projection of decoder vectors in SAE/transcoder auto-interp, Gur-Arieh et al.'s output-centric method, or TWERA). The claims about scalability and efficiency are never quantified (compute, tokens, time or cost vs baselines). The 24M-token vs large-corpus comparison confounds method with dataset.
8. **Presentation.** The paper is generally readable, but it has typos (e.g. "WeigthLens", Table 1 "0.7" for purity at layer 12, which is presumably 0.07). The bolding promised in the captions is not visible in the extracted text. Much of the key evidence is in the appendix. Figure-dependent claims (Figs. 3–8) could not be checked from the text extraction. I judged them from captions and prose.

## Questions
1. Are Table 1 features the same set for all methods? Are baselines scored on all ~250 features, or only on features that WeightLens validated? Please report the covered and uncovered subsets separately.
2. What are the variances or bootstrap confidence intervals, and the number of features per cell? Which differences are significant?
3. How sensitive are the results to the z-score threshold, ρ, DBSCAN eps/min_samples, N=100, α=0.9 and B=20? Were they tuned using the evaluation features?
4. Can you show that the head–token pairs picked by CircuitLens are causally relevant (ablation or patching)? Does the masked-input description predict activation better than a top-k description?
5. How does CircuitLens compare to a baseline that uses the same explainer LLM and prompt format but gives it top-k activations and the same masking heuristics, to isolate the circuit-based clustering effect?
6. What is the actual compute cost (forward/backward passes, tokens, LLM calls) relative to MaxAct*/Neuronpedia? The scalability claim needs numbers.
7. Do the findings hold for other layers and for the GPT-2 and Llama transcoders, and for CLTs or skip-transcoders?

## Scores
- **Soundness:** 2 (the claims are partly supported, but with selection effects, no uncertainty estimates and confounded comparisons)
- **Presentation:** 3
- **Contribution:** 2 (useful ideas, a modest and incremental empirical gain, and a narrow evaluation)

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 3**
