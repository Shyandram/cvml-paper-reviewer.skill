# Review: PixNerd: Pixel Neural Field Diffusion (ICLR 2026)

*Based on extracted text only. Figures were unavailable, so I judged figure-dependent claims (Figs. 2–8, ablation curves) from captions and text.*

## Summary
The paper proposes PixNerd, a single-stage, single-scale, VAE-free pixel-space diffusion transformer. The transformer operates on 16×16 pixel patches, which keeps the token count equal to a latent DiT with patch size 2 on an f8 VAE. The usual linear patch-decoding head is replaced by a patch-wise implicit neural field. Each patch's last hidden state predicts the weights of a small 2-layer MLP, with row-wise normalisation. The MLP takes DCT-basis coordinate encodings of the in-patch position, concatenated with the noisy pixel value, and outputs the velocity per pixel. Training is flow matching with several modern additions: SwiGLU, RMSNorm, RoPE, lognorm timestep sampling, and a REPA loss against DINOv2-B.

Reported results:
- ImageNet 256: FID 2.15 (XL/16, Euler-100, 160 epochs).
- ImageNet 512: FID 2.84, fine-tuned from the 256 model.
- Text-to-image (45M images, Qwen3-1.7B text encoder): GenEval 0.73 and DPG 80.9 at 512².
- Training-free arbitrary-resolution sampling by interpolating the neural-field coordinates.

Efficiency is argued through a latency and memory table. Ablations cover normalisation, width, depth, positional encoding, CFG interval and solver.

## Strengths
- The idea is simple and well motivated. Large-patch pixel diffusion struggles because a linear head cannot decode 16×16×3 values, so a per-patch, content-conditioned decoder is a natural fix. The design is single-stage with no cascade.
- The results are strong for pixel-space models. On ImageNet-256, FID 2.15 and sFID 4.55 at 160 epochs are competitive with or better than PixelFlow, RDM, ADM and FractalMAR, at a lower token count and with a single scale. The 512² result is well ahead of earlier pixel-space numbers (ADM-U, SimpleDiffusion, RIN). The text-to-image results (GenEval 0.73) are reasonable for 45M images.
- The ablations cover the main design choices (normalisation, width, depth, coordinate encoding, solver, guidance interval). The L/16 comparison against a baseline that differs only in the head (22 vs 24 layers to match compute) is the right experiment in principle.
- Coordinate interpolation gives training-free multi-resolution sampling, a practical benefit of the neural-field formulation (quality not verifiable from text).
- Engineering details (solver choice, interval guidance, training setup) are reported, which makes the work useful as a data point for the community.

## Weaknesses
1. **The head-only comparison is thin.** The central claim is that the neural field is what makes large-patch pixel diffusion work. The evidence is one baseline (Baseline-L/16 with a linear head), loss curves, and a qualitative figure (Fig. 5) at 400k steps. There is no FID table for Baseline vs PixNerd at matched steps.
   - Other cheap decoders at the same compute are missing: a conv or small-transformer head, a shared (non-hypernetwork) per-pixel MLP, a DDT-style decoder, or a pixel-level refinement stage.
   - A single linear layer vs a hypernetwork MLP does not show that per-patch weights, rather than extra decoder capacity and nonlinearity, are the key ingredient.
   - Lower flow-matching loss does not imply better samples.
2. **"VAE-free" and "simple, end-to-end" are partly overstated.** Training uses a REPA loss against frozen DINOv2-B. This is an external pretrained encoder doing much of the work the VAE's auxiliary supervision does. There is no ablation without REPA, so we do not know how much of the 2.15 FID depends on it. The text-to-image model also relies on a frozen Qwen3 encoder and Qwen2.5-VL recaptioning.
3. **The comparison protocol is not fully fair or clear.**
   - Table 2's headline numbers use Euler-100 (or Adams2) with interval guidance, and CFG is tuned on FID-10k (Fig. 7e). The baselines' sampling steps, guidance settings and training budgets vary and are not stated.
   - The paper says "comparable to latent diffusion" at "similar computation", but clearly stronger latent models (REPA 1.42, DDT 1.26) are in the same table.
   - sFID 4.55–5.25 is not better than many latent models (4.33–4.70). The "significantly better sFID" claim holds only against pixel models.
4. **Efficiency claims are inconsistent and loosely controlled.**
   - Table 1 lists PixNerd-L/16 at 0.010s per step against 0.097s for the baseline, while the total per-image latency is 0.51s vs 0.48s. This is arithmetically inconsistent (50 × 0.010 ≠ 0.51), and looks like a typo.
   - Training memory is higher for PixNerd (22–34 GB vs 18 GB), which is not discussed.
   - The "nearly 8× faster" claim is not clearly supported (4.21s vs 0.65s is ~6.5×). Hardware, batch size and compilation settings for ADM-G and PixelFlow are not stated.
   - Whether the latent baseline's training speed includes VAE encoding is unclear. With pre-extracted latents it would be faster.
5. **Reproducibility and writing issues.**
   - The 512² fine-tuning schedule is given as "abc steps", a placeholder left in the text.
   - Sec. 4.5 says DPG "0.82 overall score" while Table 5 says 80.9. The abstract says GenEval 0.73 and the intro says 73.0. The name alternates between PixNerd and PixelNerd.
   - The preliminaries contain sloppy or incorrect expressions (the definition of g(t), "v = dx/dt = x_real − ε").
   - Eq. (12) is under-specified (range of k, number of bases). The neural-field dimensions D1 and D2 and the cost of generating the weights are unclear. Sec. 4.2 says the default normalises the output features, but Eq. (10) normalises only the weights.
   - All FIDs appear to be single runs, with no variance, and no code release is mentioned.
6. **The text-to-image evaluation is weak.**
   - Table 4 has few baselines, some old and several with blank entries. Recent models of similar scale (SANA, PixArt-Σ, Lumina, BLIP3-o, SD3.5, Flux) and recent pixel-space T2I models are missing. Parameter counts are reported inconsistently.
   - The GenEval "Position" score of 0.71, against 0.40–0.43 for other models, is not discussed. It is surprising for this model size and may reflect the BLIP-3o SFT data, which resembles GenEval-style prompts. Overlap is not examined, and pre-SFT results are not given.
   - Qualitative claims rest on author-chosen prompts, with no FID/CLIP or aesthetic or human evaluation. The authors acknowledge blur and artifacts.
7. **Limited analysis of the mechanism.**
   - Each patch has independent weights and no pixel-level cross-patch conditioning. Patch-boundary seams at 16-pixel intervals are plausible and not examined, especially for the arbitrary-resolution claims in Fig. 4.
   - Only patch size 16 is studied. The claim of "exploring the performance upper bound" of large patches is not tested against patch sizes 8 or 32.
   - Arbitrary-resolution generation is qualitative only. The method resamples the noisy image to the training token grid and interpolates coordinates, so it may behave like upsampling of a low-resolution generation. No FID at 1024² and no comparison with simple upsampling is given.
8. **Novelty is moderate.** Coordinate-based and hypernetwork decoders for generation are established (INRFlow, PatchDiffusion, DDMI, DenoisedWeights, INR-GANs). The positioning is a discussion paragraph rather than an empirical comparison. The contribution is an effective engineering design (a dynamic 2-layer MLP head) rather than a conceptual advance.

## Questions
1. Can you give a matched FID table (at several step counts and at the end of training) for the linear-head baseline vs PixNerd, plus alternative equal-FLOPs heads (a shared MLP, a conv head), with and without REPA?
2. How much of the final FID comes from REPA, and from Euler-100 vs Euler-50 and interval guidance?
3. Please fix and explain Table 1: the 0.010s/step figure is inconsistent with 0.51s per image. Why is training memory higher? On what hardware and settings were the competing methods measured?
4. How many steps was the 512² fine-tuning ("abc steps"), and what is the total GPU-hour cost relative to REPA/DiT-type training?
5. Are there visible 16-pixel boundary artifacts? Do you have quantitative results for arbitrary-resolution generation?
6. Why is the GenEval Position score so high? Does the SFT data overlap with GenEval-style prompts, and what are the pre-SFT numbers?
7. How does PixNerd behave with other patch sizes (8/32) and larger model sizes?
8. Will code and checkpoints be released? Do you have seed variance for the FID numbers?

## Ratings
- **Soundness:** 3 (the method is plausible and the main results credible, but there are no controlled head ablations, REPA dependence is untested, and the efficiency numbers are inconsistent)
- **Presentation:** 2 (placeholder text, inconsistent numbers, notation errors, under-specified method details)
- **Contribution:** 3 (strong pixel-space results from a simple, effective design, but moderate novelty and a remaining gap to latent models)

**Rating: 6** (marginally above the acceptance threshold)

**Confidence: 4**

The recommendation rests on strong empirical results for a simple and effective pixel-space design. It is held back by thin controlled evidence for the claimed mechanism, the unablated REPA dependence, the inconsistent efficiency and writing, and the remaining gap to latent models.
