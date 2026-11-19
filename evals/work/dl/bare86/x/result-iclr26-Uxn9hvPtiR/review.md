# Review: Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents

(Text-only review; figures were not available and are judged from captions only.)

## Summary
The paper builds on the DFNO of Yang et al. (2023), an FNO-based arbitrary-resolution downscaler. It proposes several variants: DUNO (UNO backbone), SpecDFNO (a second operator predicting a residual), SpecDFNODiff (diffusion-based upsampling), MetaGradDFNO and MultiGradDFNO (Sobel gradient inputs with learned or multiscale upsampling), and Temp DFNO / Temp SpecDFNO (temporal convolutions). It evaluates them on two datasets:
- Synthetic 2D Navier–Stokes (64×64, 5 input steps → 5 output steps, with zero-shot evaluation at 64×64). Here the paper claims it removes the dependence on a numerical solver.
- Static downscaling of Copernicus (CMEMS) ocean surface velocity (2×, 4×, 8×), against two U-Net baselines.

The paper claims to be the "first neural surrogate capable of resolution-agnostic prediction where output resolution does not depend on input resolution".

## Strengths
- Downscaling ocean currents is a practically relevant problem. Applying neural operators to real CMEMS data is a reasonable direction.
- The paper tries a range of architectural variants and reports four metrics (MAE, MSE, PSNR, SSIM) with both L1 and L2 training losses.
- The paper is honest that performance degrades at 8× and that outputs oversmooth or hallucinate.

## Weaknesses
1. **Novelty is thin and the central claim is overstated.**
   - The method is DFNO plus incremental add-ons. The temporal version is a straightforward extension of the convolutions to a time axis.
   - FNO-type surrogates already predict at different resolutions (zero-shot super-resolution is a standard FNO property), and many resolution-agnostic neural operators exist. "First … resolution-agnostic prediction" is not supported. Related work on neural fields, implicit arbitrary-scale super-resolution (LIIF-type), and operator-learning super-resolution is not discussed.
   - Related work on neural-operator ocean and weather models is thin beyond OceanNet and one other citation.
2. **The Navier–Stokes comparison is not valid.** Table 1 sets Temp DFNO and Temp SpecDFNO against DFNO-2 and DFNO-4 numbers copied from Yang et al. (2023).
   - The tasks are different. Yang et al. do downscaling of solver outputs; this paper does 5→5 temporal prediction. Data generation, normalization, horizon and metrics may all differ.
   - Claims such as "match, and in some cases outperform" and "combined the predictive power of a classic numerical solver" are therefore unsupported.
   - Comparisons against a standard FNO or other neural PDE surrogates (Transolver, FactFormer, LSM, which the paper cites) trained on the same data are missing. No baselines were run for the surrogate task, and no long-rollout or error-growth evaluation is shown.
   - The Table 1 errors are essentially identical for Temp DFNO and Temp SpecDFNO. No seeds or error bars are given.
3. **The real-data downscaling baselines look broken.**
   - CNN 2x/4x reach MAE ≈ 0.4, MSE ≈ 0.19 and SSIM ≈ 0.1 on z-scored data. That is close to predicting a constant, which is implausible for a trained U-Net, and bicubic interpolation alone would almost certainly do far better.
   - The CNN rows are nearly constant across tables and loss functions, which suggests failed training or an evaluation bug. The reported "30× MAE improvement" is therefore uninformative.
   - Simple baselines are missing: bicubic/bilinear interpolation, an unmodified FNO, and standard SR (SRCNN, EDSR, SwinIR, or a LIIF-style arbitrary-scale method). The CNN baselines are also evaluated through a convoluted recursion/average-pooling protocol.
4. **The downscaling set-up is a synthetic degradation.** Inputs are average-pooled versions of the same 0.08° product, which is itself a model/assimilation output.
   - Pooling-based degradation does not match real coarse observations or models. There is no evaluation against independent observations (drifters, HF radar).
   - Physically meaningful metrics are absent: kinetic energy spectra, divergence, vorticity statistics, and extremes.
   - The abstract motivates the work by saying the Copernicus product lacks granularity. Yet the experiments only reconstruct the same product's native 128×128 patches from pooled copies, so they never produce anything finer than the product.
5. **Very small data and no statistical rigor.**
   - The real dataset is 800/200/100 patches of 128×128 from unspecified "regional subsets". Region, dates, and whether train and test overlap spatially or temporally (leakage) are not stated. The appendix's 70/15/15 split is inconsistent with the main text (800/200/100).
   - Single runs, no seeds, no variance. Many differences between variants are small and inconsistent across tables. Rankings reverse between resolutions and between L1/L2.
   - Metrics are computed at different resolutions and are not directly comparable across tables. For example, DFNO's MSE in Table 3 (0.0164–0.0175) is larger than in Table 4 (0.0094), despite the easier 4× task.
6. **Inconsistent or implausible results and text.**
   - Table 2 reports MetaGradDFNO as best at 2×, but in Tables 3 and 4 the same architecture is worse than or identical to the others. In Table 4 nearly all neural operator variants are identical to about three digits (MAE ≈ 0.0649, MSE ≈ 0.00936, SSIM ≈ 0.609), which suggests the models collapse to the same output (e.g. an interpolation of the input). This is not discussed.
   - The text says "SpecDFNO excels at zero-shot 4× downscaling" while Table 3 shows DFNO/DUNO with better MSE and MAE in several cases. The text says gradient models "excel at moderate" factors, yet they are the worst at 4×.
   - It is unclear which results are truly zero-shot (trained at one factor, tested at another) and which are trained per factor.
7. **Unclear or incorrect method description.**
   - A "softmax constraint layer" is mentioned in passing, and "softly enforced" conflicts with the hard-constraint reference. The conserved quantity for ocean surface currents is unspecified (is the surface flow even mass-conserving?).
   - The diffusion model is described in one paragraph: no architecture, sampler, steps, or conditioning details, no compute cost, and no probabilistic evaluation (CRPS, spectra). A diffusion upsampler is evaluated with deterministic pixel metrics only, and the claimed "increased overhead" is not quantified.
   - For the spectral residual, it is unclear how the second operator is trained and applied at test time (the ground truth is not available at inference). No ablations isolate each component. No parameter counts or runtimes are given, even though speed is a main motivation for surrogates.
   - "Arbitrary resolution" is tested only at 2–3 discrete factors.
8. **Presentation.** The paper reads as a short workshop paper (the footer is "ICML 2025 Workshop"). Several sections are thin or misplaced: "Discussion" holds the results, and Section 4.2 opens with a stray sentence. Metric definitions are said to be in an appendix but are not there. There is no code or data release information. Some references are incomplete or inaccurate (Dong et al. is in TPAMI 2016, "e. a." author lists). The claim that degradation at 8× "reflects physical reality" is speculation without analysis.

## Questions
1. Why do the CNN baselines sit at MSE ≈ 0.19, nearly constant across scales and losses? What do bicubic interpolation and a plain FNO achieve on the identical split and metrics?
2. Can you provide Navier–Stokes baselines (FNO, Transolver, etc.) trained on your data, and longer rollouts, rather than numbers copied from a different task?
3. Why are all neural operators identical in Table 4 to about three digits? Are they outputting the interpolated input?
4. Which regions and time periods form train/val/test in CMEMS? Is there spatial or temporal overlap?
5. What is the "softmax constraint", and which physical quantity is conserved? Please add an ablation with and without it.
6. Please provide spectra, divergence, and vorticity diagnostics, plus seeds or confidence intervals.
7. What is the exact difference between your approach and standard FNO zero-shot resolution transfer that makes this a "first"?

## Ratings
- Soundness: 1
- Presentation: 2
- Contribution: 1
- **Rating: 2**
- Confidence: 4
