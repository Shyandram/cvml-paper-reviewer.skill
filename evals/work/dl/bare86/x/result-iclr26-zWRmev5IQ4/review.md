# Review: DiTraj: Training-free Trajectory Control for Video Diffusion Transformer (ICLR 2026)

Note: figures were not available. Figure-dependent claims are judged from captions and text only.

## Summary
The paper proposes DiTraj, a training-free bounding-box trajectory control method for text-to-video DiTs (demonstrated on Wan2.1-1.3B and CogVideoX-5B). It has three components.
1. **Foreground-background separation guidance.** An LLM (Qwen3) splits the prompt into a foreground prompt and a background prompt. A cross-attention mask makes tokens inside the box attend to the foreground prompt and all other tokens attend to the background prompt. This is applied for the first t_a=30 of 50 steps.
2. **STD-RoPE.** The authors observe that attention in 3D full attention is "diagonal", so tokens with similar RoPE positions attend strongly to each other. For the first t_b=5 steps, the spatial RoPE of foreground (in-box) tokens in every frame is replaced by that of an anchor frame's box, while the temporal RoPE is kept. A self-attention mask blocks attention between foreground tokens and "R-tokens". These are non-foreground tokens that end up with duplicated positions.
3. **3D-aware control.** The anchor is the smallest box, and its position grid is nearest-neighbor upsampled to larger boxes. The "density" of position embeddings is meant to encode depth/closeness.

On 56 prompts × 10 seeds, the paper reports better trajectory metrics (mIoU, CD, AP50) than Peekaboo, TrailBlazer, FreeTraj, Direct-a-Video, LVD and Tora. VBench quality is comparable or better, and a user study with 24 participants favors the method.

## Strengths
- The idea is simple, inference-cheap (+5–6% time) and needs no inversion or optimization. It transfers across two DiT backbones, which supports generality.
- Manipulating RoPE positions of a subset of tokens to strengthen cross-frame attention is a neat, mechanistic idea. It is tied to a plausible observation (Fig. 4) about attention locality under 3D-RoPE.
- The ablation separates SG from STD-RoPE and sweeps t_a/t_b. The gains from STD-RoPE are large in the metrics (mIoU 35.4→47.3, AP50 25.6→50.5).
- The paper is clearly organized and the method is easy to reproduce in principle. The LLM prompt template is given in the appendix.
- The 3D-aware (depth) control via position density is a novel angle, even though it is lightly evaluated.

## Weaknesses
1. **Mechanistic claim is only weakly validated.** The causal story is "similar RoPE → similar rotation → higher attention → better layout". It rests on one qualitative attention-map visualization (block 1, first step, one example), and the paper itself notes that the phenomenon is known (Luo et al. 2025; Wen et al. 2025). There is no quantitative analysis across prompts, blocks, heads or steps. There is no test of alternatives, such as the effect of the cross-attention mask or the foreground prompt itself. The explanation that RoPE rotation similarity yields "more similar feature representations" is loose. RoPE affects q·k through relative offsets, and content features also matter. Assigning identical spatial positions to the foreground tokens is an edit that makes frames look more alike by construction. Whether it improves layout *planning* or simply copies appearance is not separated.
2. **Evaluation is small and potentially biased.**
   - The evaluation uses 56 prompts, many taken from Peekaboo/TrailBlazer and extended by the authors with hand-designed boxes. Prompts are single-object and mostly easy animals or objects.
   - There are no multi-object, occlusion, crossing-trajectory or very small/large box cases. Multiple objects are a standard use case for trajectory control, and the method is only described for a single foreground box.
   - There is no standard benchmark with established trajectory splits, and no confidence intervals or seed variance despite 10 seeds per prompt.
   - The detector (OWL-ViT) is queried with the subject name. A method that duplicates the foreground prompt "close-up shot filling the box" may be advantaged on detector-based metrics. Mask or segmentation-based or tracker-based evaluation would be more convincing.
3. **Unfair or confounded comparisons.**
   - Baselines run on different (older, weaker, U-Net) backbones, so the improvement conflates the base-model strength with the method. Wan2.1 is vastly stronger than the AnimateDiff/ModelScope-class backbones the baselines use. The paper does not adapt any baseline idea (e.g., Peekaboo/TrailBlazer-style attention masks, FreeTraj noise initialization) to the same DiT. The "original" Wan row in Table 3 is only a no-control reference, not a competing control method.
   - The key claim that DiT-specific design is needed is therefore not demonstrated. A simple ported baseline (attention masking on Wan, noise-prior manipulation) is missing.
   - Tora uses a point trajectory (center of the box), so its mIoU/AP is not a like-for-like comparison. Its low AP50 (3.4) with a high Cov (0.95) is probably an artifact of this protocol.
   - The Table 1 comparison against Tora is also done with the CogVideoX variant, where gains are less clear. Ours(CogVideoX) is *worse* than TrailBlazer on the 3 numbers shown (AQ 0.580 < 0.593 LVD, CD 0.14 vs FreeTraj 0.11, AP50 58.8 vs 49.1 OK). Not all "best across all metrics" claims hold. CD is best for FreeTraj among the CogVideoX-comparable methods, and the claim "outperforms ... all metrics" versus training-based methods is false for CD (Direct-a-Video 0.14 equals Ours (CogVideoX); LVD AQ 0.593 > 0.580; Tora MS 0.988 vs 0.990 fine).
   - The abstract/text claim of "best across all metrics" against training-based methods should be corrected. The text also reports improvements "of 2.1%, 15.9%, 18.2%, 2.9%" with unclear definitions (relative vs absolute). For example, the AP50 gap is 50.5 vs 49.1 for TrailBlazer, but on CogVideoX it is 58.8.
4. **Hyperparameters chosen on the test set.** t_a and t_b are selected by ablation on the same evaluation set used for the headline results (Table 5 is the same as the Table 3 rows). t_b is quite sensitive (1→5 doubles AP50, 10–20 degrades quality). This leaves uncertainty about robustness for other models, resolutions, or trajectory lengths. The t_b=5 steps-of-50 setting is applied to Wan with a flow-matching schedule, and it is unclear how it transfers to CogVideoX (the same values are used).
5. **Trade-offs and failure modes are under-analyzed.**
   - Replacing spatial PE for all foreground tokens with a single anchor can distort object shape/pose and make objects look static or rigid. This risk is partly seen in the slight decrease in quality (SC/MS/IQ vs SG alone).
   - The self-attention mask has no ablation. The "R-token" masking is justified qualitatively only. Does removing it matter? The ablation lacks the intermediate "STD-RoPE without R-mask".
   - The "random anchor" in Alg. 1 (k←Random(0,f)) and sensitivity to anchor choice are not studied. The upsampled anchor for 3D-aware control (smallest box) is arbitrary.
   - Large-motion cases (the stated motivation) are not separately quantified; no breakdown by displacement magnitude.
6. **3D-aware control is not validated.** The claim that position-embedding density controls depth/camera distance is supported only by qualitative examples (Fig. 1 right). There is no quantitative evaluation, and no evidence that the effect is genuinely depth rather than apparent size. Bounding-box size already determines apparent size, so what "3D-aware" adds beyond scaling is unclear. No comparison to baselines on size-varying boxes is given.
7. **Dependence on an LLM and prompt engineering.** Foreground/background prompt quality depends on Qwen3 and a very long hand-engineered template (80–100 words each, "close-up shot filling the entire frame"). There is no ablation on LLM choice, template, or non-LLM alternatives, such as using the original prompt for the foreground and a generic background prompt. The extra "semantic expansion" by the LLM may itself improve quality (SG alone raises IQ from 0.608 to 0.691), so the benefit of the separation is confounded with prompt enrichment. Control: use the original prompt with the mask or an enriched prompt without the mask.
8. **Novelty and claims.** "First training-free DiT-specific method" is a timing claim. Contemporary training-free DiT control and attention-manipulation work exists (e.g., on image DiTs, layout control in FLUX, and video DiT motion transfer), and related work is thin on these. The individual ingredients (attention masking by region prompts, RoPE manipulation) have precedents, and the novelty is the combination for video trajectory.
9. **Presentation.**
   - Several statements are overclaimed ("complete alignment with the target trajectory", "significantly surpasses").
   - Quantitative claims are inconsistent with the table in places, as above.
   - The user study (24 participants) reports only percentages with no per-user variance or protocol details. All methods are shown at once, and ordering and video selection are not described.
   - There are no limitations section and no failure cases. The text has minor typos ("Trailbrazer", "blown wings").
   - Table 1 comparisons mix backbones, resolutions and frame counts. This is unstated.

## Questions
1. Can you provide a quantitative version of the Fig. 4 analysis (attention mass between in-box tokens across frames, averaged over prompts/blocks/steps) with and without STD-RoPE?
2. Can you provide a baseline that ports an existing training-free approach (e.g., Peekaboo/TrailBlazer-style attention masks, FreeTraj initialization) onto Wan2.1 or CogVideoX? This would separate the effect of "DiT backbone" from "your method".
3. What happens without the R-token mask, and with the original prompt (no LLM split) used for both foreground and background? What happens with an LLM-enriched prompt but no mask?
4. How sensitive are the results to the choice of anchor frame (random vs. first vs. mid), and to t_a/t_b on held-out prompts or trajectories?
5. Does the method handle multiple objects, crossing/occluding trajectories, or very small boxes? How are multi-object cases supposed to be handled when there is a single "foreground prompt"?
6. How is the 3D-aware control quantified? Does the depth cue (position density) change anything beyond box-size-driven scaling? Provide a user or depth-estimation based evaluation.
7. Can you provide variance across seeds/prompts, and also evaluate with a segmentation/tracking-based metric to reduce reliance on OWL-ViT?
8. Please clarify the "improvements of 2.1%, 15.9%, 18.2%, 2.9%" and the "best across all metrics" claim versus Table 1.

## Ratings
- Soundness: 2
- Presentation: 3
- Contribution: 2
- Rating: 4
- Confidence: 4

Overall: a practical, cheap and apparently effective method with an interesting RoPE-based idea. However, the evidence is thin: a small, self-designed prompt set, backbone-confounded baselines, test-set hyperparameter tuning, a loosely validated mechanism, missing ablations (R-mask, LLM prompt) and unvalidated 3D claims. I lean toward borderline reject, though I would raise the rating if the baselines were ported to the same DiT and the analysis were made quantitative.
