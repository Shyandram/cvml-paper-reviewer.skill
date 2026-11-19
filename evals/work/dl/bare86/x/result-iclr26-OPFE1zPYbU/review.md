# Review: Rethinking Diffusion Model in High Dimension (ICLR 2026)

Note: figures were not available, so figure-dependent claims (Figs. 5, 14–17) are judged from captions and text only. I read the main text and the appendix up to A.1. I did not read the later appendix material or the coefficient tables.

## Summary
The paper asks whether diffusion models really learn the data distribution. It makes three claims.

1. **Sparsity ("weighted sum degradation").** All three formulations (Markov chain, score, flow matching) reduce to regressing the posterior mean E[x0|xt]. Under the empirical (Dirac-mixture) data distribution, this posterior mean is a softmax-weighted sum of training samples. On ImageNet-256/512 latents (Tables 1–2), the weights are almost one-hot for t below roughly 600. The authors conclude that the regression target "degrades" to a single sample, often the x0 that generated xt. They then interpret training as "predict the clean image from the noisy one", with a frequency-domain story (low frequencies first).
2. **Natural Inference.** DDPM ancestral sampling, DDIM, Euler, DEIS, DPM-Solver and DPM-Solver++ are rewritten as xt ≈ (signal coefficient)·(linear combination of earlier x0-predictions) + (noise combination). The coefficients are tabulated as a lower-triangular "coefficient matrix". A linear combination of earlier predictions is called "Self Guidance", by analogy with CFG and unsharp masking.
3. **Applications.** The framework is used to explain why high-order solvers are fast and why they break at large CFG. It is also used to control sharpness, to hand-tune coefficient matrices that improve FID on CIFAR-10 at 5/10/15 steps, and to describe an "over-enhancement" phenomenon.

## Strengths
- The question (why diffusion models generalize in high dimension) is interesting.
- The coefficient-matrix view of multistep samplers is a clean way to compare solvers. It also suggests a search space: optimized or learned linear combinations of past x0 predictions.
- On CIFAR-10, with a fixed pretrained model and a shared time schedule, the optimized matrices give lower FID at 5 steps (8.66 vs 11.50–15.60).
- The paper is readable, and code is promised.

## Weaknesses

### 1. The central "sparsity" argument does not support its conclusion
- **The statistic describes the empirical optimum, not the learned network.** Section 3 analyses the closed-form posterior under the empirical training distribution. It is well known that this optimal denoiser memorizes: it reproduces training points and cannot generate new samples. Trained networks demonstrably do not collapse to it, because architecture, smoothness and finite training give them inductive biases that generalize. The paper never measures what the network does. It does not compare network outputs to the empirical posterior mean or to the nearest training sample, and it does not test whether generations are training copies.
- **The jump from "the target degenerates" to "the model is unlikely to learn the ideal target" is asserted, not shown.** It conflates the finite-sample fitting target with the population posterior mean. A network that generalizes does not fit the finite-sample target.
- **Missing literature.** The paper does not engage with the work on memorization vs generalization in diffusion models, on the closed-form empirical denoiser, on inductive-bias-driven generalization, or on the low intrinsic dimension of image data. The reference list contains none of it, so the "rethinking" framing overstates novelty.
- **Factual and notation slips.**
  - Sec. 3.1 says the posterior weight of X0^i is "inversely proportional to the distance" to µ. The weight is exp(−d²/2σ²), which is Gaussian in distance, and the paper's own derivation gives that form.
  - Eqs. (18–22) reuse p(x0|xt) for the data prior in places where p(x0) is meant.
  - Eq. (23) integrates over dxt instead of dx0.
  - The reduction of all three formulations to posterior-mean regression (Eqs. 8, 16) is standard (Vincent 2011; Ho et al.), yet it is presented as part of the contribution.
- **The degradation statistic is close to tautological.**
  - It draws X0 from the training set, adds noise, and checks whether the posterior over that same training set is one-hot. In 4096–16384 dimensions at small t, the generating point is trivially the nearest one. The 1.00/1.00 entries at small t only say that the data is sparse relative to the noise.
  - The implementation is under-specified. It is unclear how the softmax over about 1.28M points and the 0.9 threshold are computed, how "t" in 0–1000 maps to flow matching σt, and whether held-out points behave the same.
  - Only ImageNet is analysed. There is no control on low-dimensional or structured data where models are known to generalize, which would be needed to show the statistic discriminates anything.
- **The conclusion is at odds with practice.** If the target were a single training sample for t < 600, the model would be a memorizer at those noise levels. The same models are routinely observed to generate novel content at those noise levels.
- **The "simple understanding" is not new.** "Predict x0 from a noisy x0" is x0-prediction, long known to be equivalent to ε, v and score prediction. The frequency-domain explanation (Sec. 3.3) is informal and leans on a blog post. The claims that low frequencies are prioritized, and that high frequencies are "directly predicted" at small t, are untested. No per-frequency error of a trained network is shown.

### 2. The "unified framework" is nearly trivial and only approximate
- Any deterministic sampler whose update is linear in past network outputs can be unrolled into xt = Σ c·y + Σ b·ε. That DDIM, Euler, DEIS and DPM-Solver can be written this way follows from linearity of the update. It is expected, not a finding.
- The equivalence is numerical and approximate. The paper itself says the equivalent signal coefficient is "almost equal to" √ᾱt and the noise coefficient "approximately" √(1−ᾱt). The evidence is plots (Figs. 8–13). No error bounds or max/mean deviation tables are given. If the coefficients are not exactly the stated values, the framework shows closeness, not unification.
- The claim that Markov-chain and SDE concepts are "not needed" overreaches. The coefficients come from exactly those derivations. The framework tabulates them and does not derive them.
- Coverage is incomplete. UniPC, predictor–corrector samplers and stochastic higher-order samplers are not treated. The DDPM case is shown to need extra noise terms that break the clean structure (the paper concedes the noise matrix differs).
- The linear multistep and exponential-integrator view is already present in the DEIS, DPM-Solver and UniPC literature. Renaming an affine combination of two predictions as "Self Guidance", with Fore/Mid/Back variants by the sign of λ, adds no technical content.
- The claim that Self Guidance "enhances quality" in the way CFG or unsharp masking does is by analogy only. Extrapolating along a trajectory is the standard mechanism of higher-order multistep methods. The analogy is not tested.

### 3. The explanations in Section 5 are speculative and thinly tested
- **5.1.** The chain "negative coefficients ⇒ Fore Self Guidance ⇒ higher quality ⇒ high-order solvers are faster" has no ablation. High-order solvers are faster because truncation error is smaller, and negative weights are a natural consequence of extrapolation. Nothing separates "enhancement" from ordinary higher-order cancellation.
- **5.2.** The large-CFG explanation rests on one example (Fig. 14: three hand-picked combinations on one SD3 image with one prompt). It has no metric, no seeds, and no comparison with the known account of guided sampling leaving the data manifold, which motivated DPM-Solver++. It is also confounded with data-prediction vs noise-prediction parameterization. "Positive coefficients are the key to larger CFG" is not established.
- **5.3.** Sharpness control is one qualitative before/after comparison, with no sharpness metric and no user study.
- **5.5.** "Over-enhancement" is produced by re-applying the denoiser at a fixed t, which is an off-distribution regime. The attribution to a train–test frequency-domain mismatch is a hypothesis. The "verification" (fine-tuning on the model's own outputs, Fig. 17) is a single qualitative experiment with no baseline and no description of the data mixture. Training on a model's own outputs has its own known effects.

### 4. The evidence for "more efficient inference" is thin
- **Single small benchmark.** The only quantitative result is CIFAR-10 (ScoreSDE ddpmpp-continuous VP) at three step budgets, with one FID number each. There are no seeds, confidence intervals or stated sample counts. There is no ImageNet, latent-diffusion or SD3 result, even though the motivation is "high dimension".
- **Tuning asymmetry.** The optimized matrices appear tuned against the same metric on the same model and step counts. The procedure, search budget and number of FID evaluations are not given. The matrix has O(T²) free parameters, against a few hyperparameters for baselines. There is no held-out check (different seeds, models, datasets or metrics), so overfitting to FID cannot be excluded.
- **Missing baselines.** Searched or learned linear solvers are the natural comparison: UniPC, DPM-Solver-v3, iPNDM, and learned or bespoke solvers such as LD3 and AMED. "Better coefficient matrix" is essentially a learned linear multistep solver, and that literature is not cited or compared.
- **The baseline ordering looks unusual.** DEIS beats DPM-Solver and DPM-Solver++ at 10 and 15 steps (3.94/3.55 vs 5.06/4.15 and 4.64/3.92), and DPM-Solver++ is not reported as beating DPM-Solver at 10 steps in the usual way. This suggests baseline configuration issues. NFE accounting across solvers is also unclear.
- **No reusable method is delivered.** Sec. 5.6 concedes the optimum depends on model, step count and discretization. The design principles (shorter tail for few steps, more negative weights) are heuristics drawn from a handful of observations.

### 5. Presentation
- The title and abstract promise an answer to "do diffusion models learn the distribution?". The paper does not analyse generalization, and the sparsity analysis (Sec. 3) has no logical dependency on the inference framework (Sec. 4). The three "conclusions" are loosely connected.
- Numerous typos and inconsistencies:
  - "Table 3.2" is used for two tables.
  - "Self Guidence", "imageget-256", and "ancestor" vs "ancestral" appear.
  - "Figure 14(d)" is cited twice in one sentence.
  - Sec. 5.4 says "higher FID scores" where lower is better.
  - The latent size 16,480 is probably 16,384.

## Questions
1. Does the trained network behave like the empirical posterior mean in the regime where your statistic says the target is one-hot? For example, compare network x0 predictions to the nearest training sample and to the exact empirical denoiser, and check generations for training-set copies. If the network does not collapse, what do Tables 1–2 tell us?
2. How is p(x0|xt) computed over about 1.28M points per sample? How is t mapped between VP and flow matching? Do the numbers change for held-out data?
3. How close are the "equivalent" coefficients to √ᾱt and √(1−ᾱt)? Please give max/mean errors per method and step count, and show numerically that the framework reproduces the original samplers' outputs.
4. How was the optimized coefficient matrix found (objective, algorithm, number of FID evaluations, samples per FID, seeds)? Does it transfer across models, datasets and step counts, and does it beat UniPC and learned-solver baselines?
5. Can you ablate the claim that negative or positive coefficients explain high-order speed-up and CFG robustness, for instance by constraining a fixed-order solver's coefficients to be nonnegative?
6. What evidence beyond the argument supports the frequency-ordering story (e.g. per-frequency prediction error vs t for trained models)?

## Ratings
- **Soundness: 1.** The central inference is unsupported, and the empirical-optimum analysis is never connected to trained networks. The unification is approximate and largely an algebraic restatement.
- **Presentation: 2**
- **Contribution: 2**

**Rating: 2**

**Confidence: 4**
