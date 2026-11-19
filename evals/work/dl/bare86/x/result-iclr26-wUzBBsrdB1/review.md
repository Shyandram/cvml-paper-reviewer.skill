# Review: "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders"

(Figures were not available. I judged figure-based claims from captions and text only.)

## Summary
The paper argues that L0 is not a free hyperparameter for sparse autoencoders (SAEs). It makes three claims.

1. **Toy model.** The setting is 50 orthogonal ground-truth features in R^100 with correlated firing. A BatchTopK SAE recovers the features only when its L0 equals the true L0 (11).
   - Too-low L0 makes the SAE mix correlated features. At L0=5 a ground-truth dictionary has worse MSE (4.88) than the mixed learned one (2.73), so MSE rewards the wrong solution.
   - Too-high L0 gives degenerate mixtures.
2. **A metric for the "correct" L0.** The paper proposes the "Nth decoder projection score" s_n^dec. It is the n·b-th largest value of (x−b_dec)W_dec^T over a batch. It is minimized at the true L0 in the toy model. A sketch of an automatic L0-tuning procedure is in Appendix A.4, and it reportedly needs heavy tuning on LLMs.
3. **LLM experiment.** On Gemma-2-2b layer 12, with 32k-latent BatchTopK SAEs trained at many L0 values, s_n^dec is minimized around L0≈200–250. Sparse-probing F1 (k=1, 16) also peaks there. The authors conclude that most public SAEs (L0 < 100) have L0 that is too low.

## Strengths
- The question is important and timely. The claim that the sparsity–reconstruction tradeoff can be misleading is stated clearly and is practically relevant. It is consistent with feature hedging and absorption.
- The toy-model demonstration is clean. The comparison between a ground-truth SAE and a learned SAE at low L0 (Appendix A.2, Figs. 6/7) is a compelling illustration that MSE can prefer wrong dictionaries.
- The asymmetry finding is interesting. Too-high L0 leaves many correct latents, while too-low L0 corrupts all of them. The L0 schedule experiment (A.3) suggests low L0 early in training may be hard to recover from, which gives practical advice: start high and anneal down.
- The paper is short and honest about limitations (A.4, A.6). The LLM sweep over L0 (10 to 2500) is substantial.

## Weaknesses
1. **The toy model is very favorable, and the "true L0" is well-defined only by construction.**
   - Features are exactly orthogonal (50 in 100 dimensions), so there is no superposition, even though SAEs exist to handle superposition. Magnitudes are nearly constant (N(1, 0.15)), and the correlation matrix is random.
   - A single toy configuration is used: one seed, one correlation matrix, one frequency profile, one true L0. Per-sample L0 is random, so BatchTopK is "correct" only on average.
   - Recovery is shown only through cosine-similarity heatmaps, with no quantitative summary (e.g., mean max-cosine) and no error bars over seeds. It is not shown that the result survives non-orthogonal features, heavy-tailed magnitudes, or other correlation structures.
2. **The central metric s_n^dec is under-motivated and not shown to be robust.**
   - The justification is heuristic ("latents should have near-zero projection on arbitrary inputs"). There is no theory and no ablation against alternative diagnostics.
   - It depends on a free parameter n. The paper says n must be "sufficiently larger than a reasonable guess at the correct L0" and that "up to about h/2 works well". That presupposes knowing the answer, and no principled rule for choosing n is given.
   - The minimum is described as flat for L0 slightly above the optimum. The LLM sweep is coarse beyond L0=250, and "200–250" is a wide band. It is unclear how precisely the correct L0 is determined, or how one would locate it without training a full sweep of SAEs.
   - In the LLM there is no ground truth, so the metric is validated only against another proxy (sparse probing). Sensitivity to width, learning rate and training length is not examined.
3. **The LLM evidence for "correct L0" is thin and partly circular.**
   - Everything is on one model (Gemma-2-2b), one layer (12), one width (32k) and one architecture (BatchTopK). The abstract and discussion nonetheless say "most commonly used SAEs have an L0 that is too low". The correct L0 plausibly depends on width, since wider SAEs split features, and on layer and model, as the authors acknowledge. The Neuronpedia SAEs in Fig. 9 differ in model, layer, width and architecture.
   - Sparse-probing F1 peaks near L0 200–250, but the variation is small (read from the axes: roughly 0.74–0.76 for k=1 and 0.77–0.83 for k=16). There are no error bars, seeds, or significance tests. Agreement within a wide band between one noisy proxy and a heuristic metric is weak evidence. Prior work [11] already reports that low L0 hurts probing.
   - There is no evidence that features at L0≈200–250 are more "correct": no absorption or hedging measurements, no autointerp, no SAEBench, no example latents. The abstract's "finds the true L0" claim is not supported for LLMs beyond the proxy agreement.
   - The introduction says the toy-model decoder patterns "manifest in LLM SAEs", but the only LLM evidence shown is the s_n^dec curve, not decoder patterns.
   - A single "true L0" in a real LLM is assumed. Real activations have variable numbers of active concepts, hierarchical features, and multiple granularities.
4. **Over-claiming relative to evidence.**
   - L1 and JumpReLU SAEs are not tested. The limitations say the authors "do not expect" different results, but they behave differently from fixed-L0 BatchTopK.
   - The statement that the sparsity–reconstruction tradeoff is "a misleading metric" overreaches. In the toy model, when the SAE is allowed fewer active latents than true features, the best-MSE solution is naturally not the true dictionary. That does not show that comparing algorithms at matched L0, as prior work does, is misleading.
   - The remark that the metric may give "hints as to the true number of firing features in superposition" is speculative.
5. **Limited novelty.** The low-L0 failure is essentially feature hedging [6], as the paper says. Low L0 hurting downstream tasks was already known [11, 4]. The new parts are the toy L0 sweep, the s_n^dec heuristic and the Gemma sweep, and the latter two are weakly supported. There is no comparison to other ways of selecting L0.
6. **Presentation and consistency.**
   - The Fig. 2 caption says N=12 and N=20, but the text says n=18 and n=22.
   - The definition z↓[n·b] is confusing, and figure legends say "k" while the text says "N".
   - The high-L0 "degenerate solution" is described only qualitatively. The local-minimum explanation in A.3 is speculation without an experiment.
   - Appendix A.4's automatic method has no results shown. The practical takeaway ("practitioners must set L0 correctly") therefore offers no procedure short of a full sweep of trained SAEs.
   - Many details are missing: toy SAE width, learning rate and steps, and normalization of MSE and variance explained.
7. **Statistics.** No seeds or error bars appear anywhere. All curves are single runs.

## Questions
1. What is the toy SAE width? Do the results hold with wider SAEs, non-orthogonal true features, other correlation structures, and across seeds? Please report a quantitative recovery metric with error bars.
2. How do you choose n for s_n^dec without already knowing the true L0? Is there any argument for why the minimum is n-independent?
3. Does the minimum persist with heavy-tailed magnitudes or high per-sample variance in L0?
4. Do Gemma SAEs at L0≈200–250 show lower absorption or hedging, or better autointerp or SAEBench scores, than SAEs at L0≈50? Can you show LLM latents mixing features at low L0?
5. Do the conclusions hold at other widths, layers, models, and for JumpReLU and L1 SAEs? How do you reconcile a width-dependent "correct" L0 with the idea that it is a property of the activations?
6. Please provide seeds or error bars for the probing curves, and the F1 gap between L0≈250 and L0≈50–100.
7. Can you show results for the automatic L0 method in A.4?
8. Please reconcile the n values in Fig. 2 and the text.

## Scores
- **Soundness:** 2 / 4. The toy result is sound within a narrow setting. The LLM claims rest on a heuristic metric and one noisy proxy, with no replication.
- **Presentation:** 2 / 4. The outline is clear, but the paper has inconsistencies and missing details.
- **Contribution:** 2 / 4. The message is useful, but it extends prior hedging work with limited evidence and no usable method.

## Rating: 4 (marginally below the acceptance threshold)
The point that L0 must be set carefully is valuable, and the toy illustration is neat. But the generalization to real SAEs rests on one model, layer and width, with an untheorized, n-dependent metric validated only by a noisy proxy and no seeds. The "most SAEs" conclusion is over-claimed. I would raise my score given experiments across widths, layers and architectures, quantitative feature-quality evaluations at the identified L0, a more realistic toy setting, and results for the automatic procedure.

## Confidence: 4
