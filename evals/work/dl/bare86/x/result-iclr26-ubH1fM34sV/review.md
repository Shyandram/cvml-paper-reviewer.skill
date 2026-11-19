# Review: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping (ICLR 2026)

Note: the text was extracted from the PDF and the figures were not available. Figures 1–4 are judged from their captions and the text only. Figure 3 numbers came through as OCR residue.

## Summary
The paper targets GUI grounding in which a VLM emits pixel coordinates as text tokens. The authors argue that the bottleneck is an implicit mapping from patch positional embeddings to numeric tokens, and that this mapping breaks at resolutions unseen in training. They make two proposals.

1. **RULER tokens.** These are auxiliary tokens inserted before the image. Each carries, as its token value, the pixel coordinate of an image patch. Each shares the position IDs of that patch. They are placed every s patches (s=8 by default). The model can then "copy" the coordinate of the nearest RULER token and add a bounded offset (b = s·p).
2. **I-MRoPE.** This interleaves the frequency bands among the spatial axes instead of assigning contiguous bands to t/h/w, as MRoPE does. The paper notes that Qwen3-VL independently introduced the same idea.

Experiments use two settings. In the first, LLaVA-NeXT (SigLIP + Qwen2.5-7B) is trained from scratch on UGround web data. In the second, Qwen2.5-VL-7B is fine-tuned with RULER. Evaluation is on ScreenSpot, ScreenSpot-V2 and ScreenSpot-Pro. The reported gains:
- Fine-tuning with RULER raises ScreenSpot-Pro from 34.6 to 37.2, ScreenSpot from 86.8 to 87.7 and ScreenSpot-V2 from 88.2 to 89.0.
- From scratch, I-MRoPE + RULER gives 32.1 on ScreenSpot-Pro against 29.2 for MRoPE.

## Strengths
- The idea is simple and easy to implement. It is cheap in tokens (under 1% overhead on desktop-size screens). It keeps the autoregressive text-coordinate interface, so it is compatible with standard VLM usage. This is a real advantage over architectural alternatives such as GUI-Actor's attention head.
- The motivation is intuitive: an induction-head-style retrieve-then-offset mechanism that decouples the output from absolute resolution. Coordinate regression from positional embeddings is a plausible failure source for high-resolution extrapolation.
- The from-scratch setting is a controlled comparison (LLaVA PE → MRoPE → I-MRoPE → +RULER) with the same data. The fine-tuning setting shows applicability to a strong pretrained model.
- The interval ablation and token-overhead analysis are useful, and the limitation on mobile screens is honestly noted.

## Weaknesses
1. **The central mechanistic claim is untested.** The paper asserts that RULER turns "regression into retrieval/copy + bounded arithmetic" and that this explains the resolution generalization. There is no direct evidence of this.
   - There is no attention analysis showing that the model attends to the nearest RULER token.
   - There is no error analysis, for example of error versus distance to the nearest RULER, or of digit-level errors.
   - There is no controlled resolution-extrapolation experiment, such as training at low resolution and testing at several larger scales, or ScreenSpot-Pro downscaled and upscaled.
   - ScreenSpot-Pro differs from the training data in domain as well as resolution (professional apps, small icons). Larger gains there therefore do not isolate resolution generalization. The claim that RULER "enables reliable GUI automation across diverse resolutions" is overstated.
2. **The gains are small and statistical support is absent.** There is a single run per configuration, with no seeds, confidence intervals or significance tests. ScreenSpot-Pro has ~1.6k items and ScreenSpot has ~1.3k. Many reported differences are within plausible noise.
   - Fine-tuned ScreenSpot: +0.9, with D-Text going down (94.6→93.6).
   - Fine-tuned ScreenSpot-V2: +0.8, with D-Icon going down.
   - From scratch on ScreenSpot, I-MRoPE → +RULER is +0.3, with M-Icon and D-Icon flat or down. The same step on ScreenSpot-V2 is +1.1, with D-Text down.
   - The I-MRoPE vs MRoPE differences on ScreenSpot-Pro are +0.2 (29.2→29.4), and +0.5/+0.5 on ScreenSpot and V2.
   The "largest gain on high-resolution" narrative rests mainly on ScreenSpot-Pro (+2.6 fine-tuned, +2.9 from scratch), without variance estimates.
3. **The fine-tuning baseline is unclear.** The paper does not say whether "Qwen2.5-VL" in the tables is the off-the-shelf model or the same model fine-tuned on UGround without RULER.
   - If it is off-the-shelf, the RULER gain is confounded with fine-tuning on UGround (with raw-pixel coordinates), and the comparison is invalid.
   - If it is fine-tuned, this must be stated, together with the number of steps and the hyperparameters, which are only in an appendix I cannot verify.
   - The introduction compares 31.1 (UGround-V1) to 37.2 "through fine-tuning alone". That compares different base models and data.
   - A further problem is that RULER is introduced at fine-tuning time into a model never trained with it. Any distribution-shift cost is not examined.
4. **There are no baselines against alternative explicit-coordinate designs.** The paper should compare against a few obvious options:
   - normalized/relative coordinates, which are already resolution-invariant, or a fixed 0–1000 grid as in other grounding models;
   - textual grid or coordinate overlays on the image (set-of-mark-style rulers drawn on the screenshot);
   - Phi-Ground's distance-weighted label smoothing;
   - GUI-Actor's coordinate-free patch selection under identical data and base model.
   Without these, "explicit position-to-coordinate mapping is the key" is not isolated. A related ablation is also missing: RULER tokens with shuffled or wrong values, or with position IDs unaligned to patches. That would show that alignment, not extra tokens or extra context, is responsible.
5. **I-MRoPE novelty and evidence are limited.** The authors acknowledge that Qwen3-VL has the identical design (concurrent). The evidence that frequency imbalance "degrades grounding" is a +0.2 to +0.5 point change with no variance estimate. The claim of "a previously overlooked issue" is overclaimed given Resonance RoPE and related frequency-allocation work. The 2D variant (Eq. 8) alternates "h" and "t", which is confusing notation for a height/width split and should be fixed. The I-MRoPE contribution is also not tested in the fine-tuning setting (it is deliberately not used there), so it is never shown to help a strong pretrained model.
6. **The comparison to the SOTA is weak.** The best results are well below UI-TARS-7B and GUI-Actor-7B on all benchmarks (e.g., 37.2 vs 44.2 on ScreenSpot-Pro). The authors attribute this to data. That is plausible, but it means the work does not show that RULER helps in a competitive training regime (more data, RL, mixed platforms). Whether the gain survives with stronger data, or on a model already trained on large mixes, remains open. Baseline numbers are partly copied and partly reproduced, with "appropriate transformations" for normalized coordinates left unspecified. Table 1 mixes the two sources.
7. **The scope is narrow.** Only 7B models and two training setups were tested, with web-only training data. ScreenSpot-Pro is the only high-resolution benchmark. There is no agentic end-to-end evaluation (e.g., OSWorld, AndroidWorld). There is no check that general VLM capability is preserved, although the paper claims this ("without compromising general vision-language capabilities") and the claim is unsupported.
8. **Design limitations are not discussed.**
   - Because RULER assumes square patches and a shared h/w mapping, aspect-ratio handling and non-square-patch encoders are out of scope.
   - Values are limited to the initial pixel of each patch, and with s=8 a residual offset of tens to over a hundred pixels must be estimated. This does not obviously fit "simple bounded arithmetic" for small icons.
   - Multi-image and multi-turn behavior is only briefly mentioned.
   - Inference latency (prefix length, KV cache) is only reported in token ratios, not wall-clock.
9. **The interval analysis is inconclusive.** Section 5.2 states that s does not yield significant or consistent differences, and the best s varies by setting. The mobile case shows that fewer than 2 tokens can hurt. This weakens the argument that the number of explicit references matters, and it is consistent with the possibility that most of the gain is a generic effect of extra tokens/fine-tuning.
10. **Presentation problems.**
    - The efficiency analysis says "p=8" where it means s.
    - The claim of "less than 1%" is contradicted by 1.9–2.8% for mobile in Figure 4, although the text partly notes this.
    - The ScreenSpot description ("1,272 instructions each on mobile, desktop, web") is garbled.
    - The abstract's "consistent gains" glosses over the sub-split regressions.
    - Hyperparameters are only in the appendix, which was not in the provided text.

## Questions
1. In the fine-tuning rows, is "Qwen2.5-VL" the off-the-shelf checkpoint or the same model fine-tuned on UGround without RULER, for the same number of steps and with the same coordinate format? Please report both.
2. Can you provide multi-seed results or bootstrap confidence intervals for Tables 1–3?
3. Can you run a controlled resolution-extrapolation study, for example training at ≤1080p and testing the same screenshots upsampled to 2K/4K/8K, with and without RULER? Can you also report accuracy as a function of the screenshot's original resolution within ScreenSpot-Pro?
4. Can you show mechanistic evidence, such as attention to the nearest RULER token, accuracy versus offset to the nearest RULER, or a corrupted-RULER ablation (shuffled values or misaligned position IDs)?
5. How does RULER compare with (a) a normalized-coordinate output format, (b) Phi-Ground-style label smoothing and (c) overlaid pixel rulers/grids, with the same base and data?
6. Does the gain persist when starting from a stronger grounding model (UI-TARS, GUI-Actor backbones) or with a larger mixed-platform dataset?
7. Does RULER affect the general VLM benchmarks that the paper's compatibility claim implies?
8. What are the wall-clock overheads, and how does the method handle non-square patches or dynamic aspect ratios?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- Rating: 4
- Confidence: 4

Overall: the idea is neat, cheap and plausible, but the evidence is thin. Gains are small, single-seed and in part possibly confounded. The mechanism is unverified, important baselines are missing, and the I-MRoPE contribution is concurrent with Qwen3-VL and marginal. I lean towards borderline reject. With a clean baseline, variance estimates and a real resolution-generalization study, this could become a solid paper.
