# Review: Wavelet-Stereo (ICLR 2026 submission)

*Figures were not available. Figure-dependent claims (Fig. 1 convergence curves, qualitative results) are judged from captions and text only.*

## Summary
The paper observes that RAFT-Stereo's EPE converges differently in "high-frequency" regions (edges and thin structures) than in "low-frequency" regions. The authors take this as the reason iterative stereo methods lose fine detail. They propose Wavelet-Stereo, with three parts:
- A 3-level Haar DWT of the left image. The LH/HL/HH sub-bands go to a U-shaped high-frequency extractor, and the LL band goes to the RAFT context encoder.
- A "high-frequency preservation update" (HPU) operator. It combines an iterative frequency adapter (IFA), which alternates channel/spatial attention between the high-frequency features and the hidden state, with an LSTM whose cell state is the high-frequency feature.
- Plug-in versions for RAFT-Stereo and MonSter.

Wavelet-MonSter is reported to reach first place on KITTI 2012 and 2015 for most metrics. It also reports small gains on ETH3D and a Scene Flow EPE of 0.36 versus MonSter's 0.37.

## Strengths
- The problem is relevant. Thin structures and edges are a known weakness of recurrent stereo.
- The idea of feeding an explicit, fixed wavelet decomposition into the update operator is simple, and it plugs into two different baselines (RAFT-Stereo and MonSter).
- The method gives consistent, if small, gains over a very strong MonSter baseline on the KITTI and ETH3D leaderboards. The authors submitted to the public benchmarks.
- The paper has a per-region (Canny edge / non-edge) EPE analysis, an ablation of DWT levels, a runtime/memory breakdown, and a failure-case and limitations section.

## Weaknesses
1. **The central diagnostic claim is weakly supported.**
   - "Frequency convergence inconsistency" is shown only in Fig. 1, on a few ETH3D scenes for RAFT-Stereo, and I could not see it.
   - The claim that joint optimization of all frequencies is the *underlying reason* for the degradation is asserted, not tested. Edge pixels have larger error simply because of depth discontinuities, occlusion and label ambiguity. Higher EPE at edges and different convergence rates there are expected without any frequency-specific mechanism.
   - "High-frequency region" is defined by Canny edges on the ground-truth disparity (App. B.2). That is a *disparity-discontinuity* mask, not an image-frequency one. The paper never links image-domain wavelet high-frequency content to disparity-edge error. The text mixes "image" and "disparity" frequency.
   - No experiment shows that the proposed model converges more consistently across regions. Fig. 1(b) is claimed but not quantified in the text.
2. **Numerical inconsistencies across tables.** These undermine confidence in the ablations.
   - RAFT-Stereo's Scene Flow EPE is 0.53 in Table 1 but 0.62 in Table 4. The "simplified training" explanation was not backed by a matched comparison. Table 6 gives 0.53 at 32 iterations.
   - Wavelet-RAFT's EPE is 0.46 (Table 1), 0.52 (Tables 4 and 6), 0.467 (Table 7) and 0.53 (Table 5).
   - Table 5 has EPE of about 0.37 for all rounds, a different number again.
   - Table 6 shows RAFT-Stereo EPE of 0.53 at 32 iterations, 0.63 at 16 and 0.53 at 12. That is non-monotonic and looks like an error.
   - Table 7 lists the HPU-only model at 0.563 with 0.55M parameters, but the full model at 5.5M.
   - The "38.6% runtime reduction" appears to compare Wavelet-RAFT at 8 iterations (0.27 s) with RAFT-Stereo at 32 iterations (0.44 s). By Table 6 itself, RAFT-Stereo at 12 iterations gets the same EPE (0.53) in 0.22 s, which is *faster* than Wavelet-RAFT's 8 iterations. The "accelerates convergence" claim is therefore not supported. At equal iterations Wavelet-RAFT is about 1.8x slower, and the runtime in Table 8 (about 490 ms for 16 iterations) differs from Table 6 (0.45 s).
   - The text states 25.89% and 10.3% gains over Selective-IGEV and DLNR in high-frequency regions. Table 3 gives 26.10 → 23.42, which is about 10% over Selective-IGEV, and 31.6 → 23.42, which is about 26% over DLNR. The percentages look swapped or miscomputed. The claim of a 22% gain over the baseline for Wavelet-RAFT (34.00 → 26.48) is the only one that checks out.
3. **Gains over the state of the art are marginal, and no variance is reported.**
   - The Table 1 improvement is 0.01 px (0.37 → 0.36).
   - Table 2 improvements over MonSter are 0.01–0.04 on most metrics, for example D1-all 1.33 → 1.31 and Out-3 all 1.09 → 1.07. KITTI D1-fg Noc is worse than DEFOM-Stereo.
   - There are no seeds, no confidence intervals and no significance tests. The method is heavier (more parameters, about 1.8x runtime) than the baselines. The "rank 1 for almost all metrics" claim is the headline but rests on differences that are plausibly within run-to-run noise.
   - Zero-shot generalization is claimed from qualitative figures only. No quantitative zero-shot table (KITTI, Middlebury, ETH3D) is given, even though the appendix describes the evaluation.
4. **Ablations are limited and partly confounded.**
   - Table 4 compares RAFT's GRU with an LSTM-based HPU. The gain could come from the LSTM, from extra parameters, or from the extra input. It is not isolated from the DLNR-style LSTM.
   - Table 4 contains no experiment that replaces DWT sub-bands with a learned or Sobel/Laplacian high-pass, or with a plain extra image-feature branch of the same capacity. The central claim that *explicit wavelet* decomposition matters is untested.
   - There is no ablation of IFA versus no IFA, or of the LSA/HSA design.
   - Parameter-matched controls are missing. The extractor adds about 5M parameters (Table 7).
   - The 0.77M additional parameters stated in the text does not match Table 7 (4.36 → 5.5M).
   - Ablations are on RAFT-Stereo only, not on MonSter, which produced the headline results.
5. **Method description is unclear and partly inconsistent.**
   - Eq. (1)–(2) define alternating attention updates of F_h and F_l, but the notation (i, j, k) is confusing. Whether the IFA runs inside each of the n_k updates, and with what weights shared across iterations, is not clear.
   - The statement F_h^{i,0,k} = F_h^{i,0,k-1} is hard to interpret.
   - Eq. (10) puts F_h in the LSTM cell state in place of c_{t-1} (c_t = f_t * F_h + i_t * g_t). That is an unusual choice with no analysis. It also means the cell state is never carried across iterations, which seems to contradict the "preservation across iterations" motivation.
   - The LL-band is used as the input to the context encoder, but the cost volume uses full-resolution features. Why the low-frequency branch should be better than the original RGB is unexplained.
   - The "same hidden state F_l" is called "low-frequency", but nothing constrains it to be low-frequency.
   - Citation [31] for the Haar wavelet is a wavelet diffusion paper, and [41] and [42] are duplicate references. The IFA description in the text (alternating) differs from Fig. 5's description of "bidirectional".
6. **Novelty is moderate.**
   - Frequency-aware stereo (Selective-Stereo, DLNR) already exists. Wavelet feature branches, HiLo-style attention and CBAM-style channel/spatial attention are all established.
   - The contribution is a combination of known components, and the main new element is a fixed Haar front-end. The paper's criticism that prior methods "lack interpretability" is not backed by a comparison.
7. **Presentation.** Many typos and inconsistent names (Wavelet-Raft / Wavelet-RAFT, "r=4" versus "j"). It is unclear which model each table uses. "Plug-and-play into multiple iterative methods" is shown for only two methods. The failure-case figure's caption says the method extracts "task-irrelevant information", which suggests it adds noise in some scenes, but there is no analysis. Code is promised, not provided.

## Questions
1. Can you show the convergence plots (EPE per iteration, edge vs non-edge) for Wavelet-Stereo as well as RAFT-Stereo, over many scenes and datasets? Does your method actually remove the inconsistency?
2. Please reconcile the baseline and own-model numbers across Tables 1, 4, 5, 6 and 7. Which table is correct, and are the baselines trained with the same schedule?
3. How do runtime and accuracy compare with RAFT-Stereo and MonSter at *matched* runtime or parameter count? Does Wavelet-RAFT at 8 iterations really beat RAFT-Stereo at 12 iterations?
4. What happens if you replace the Haar DWT with a learned high-pass, a Sobel/Laplacian filter, or simply a second RGB-based feature branch with the same architecture? What is the effect of IFA alone and of putting F_h in the cell state?
5. Do you have results over multiple seeds on Scene Flow and on the KITTI/ETH3D training splits, and quantitative zero-shot numbers?
6. Why use Canny on ground-truth disparity as the "high-frequency" mask? How do the results change with a mask based on image gradients, or excluding occluded pixels?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- **Rating: 4** (marginally below the acceptance threshold)
- Confidence: 4

The leaderboard result is real but incremental. The motivating analysis and the "faster convergence" claim are not convincingly supported, the numbers are inconsistent across tables, and the ablations do not isolate the contribution of the wavelet decomposition.
