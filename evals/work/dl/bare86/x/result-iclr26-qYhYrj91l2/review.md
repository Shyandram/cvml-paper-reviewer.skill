# Review: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos

Note: figures were not available. Figure-dependent claims are judged from captions and text only. The paper's central evidence is video, which I could not see either.

## Summary
The paper fine-tunes pretrained text-to-video diffusion models (CogVideoX-5B for text-based camera control, AC3D for trajectory-based control) to follow "unconventional" camera motions. The training data are simple low-poly Unity scenes with scripted camera motions. Several components are meant to keep the synthetic appearance out of the generated videos:
- A dual-adaptation scheme in the style of AnimateDiff. An appearance LoRA is trained on static-camera synthetic videos and frozen, a camera LoRA or trajectory encoder is trained on moving-camera videos, and the appearance LoRA is discarded at inference.
- A "virtual" style tag, `<VIRTUAL>`, appended to training prompts and dropped at test time.
- An "optical-flow" loss that matches frame-to-frame differences of the predicted x0 to those of the ground truth.

Evaluation uses 100 prompts per category (simple, composed, complex). Metrics are TransErr, RotErr and FVD, plus an MTurk study (Action Correctness and Realism, 0–2 scale) and CLIP similarity. The authors claim better camera-motion precision than CameraCtrl, CogVideoX and AC3D, with realism comparable to the baselines.

## Strengths
- The problem is well motivated. Camera motions that are rare in real data (search-then-focus, shake, 180° rotation) are a real gap, and the baselines' failures on them in Figs. 2, 7 and 8 are plausible.
- The data pipeline is cheap and practical. The scenes are low-poly, the motion scripts are about 10 lines of code and can be written by an LLM, and about 500 videos are used. If the claims hold, this is attractive.
- The same recipe is applied to two different control paradigms (text-conditioned LoRA and a trajectory encoder).
- Quantitatively, VividCam improves TransErr in most categories. The gains are largest for composed and complex motion (e.g. composed TransErr 0.51→0.22 for CogVideoX→VividCam-Cog, and complex RotErr 0.59→0.36 for AC3D→VividCam-AC3D). The human study agrees in direction on complex motion.
- The ablation (Fig. 5, Table 4) shows that removing the appearance LoRA hurts realism visibly. Table 5 reports a comparison with mixed real data.
- The paper is clearly written and easy to follow.

## Weaknesses
1. **The central generalization claim is not tested.**
   - The title and abstract promise learning "unconventional" motions. The evaluation motions (Table 1) are exactly the motion types the authors script in Unity and train on. Test prompts are template-like variants of the training motions.
   - The experiments therefore show that a model trained on motion X follows motion X better than models that never saw X. They do not show generalization to new unconventional motions, or composition beyond the trained set.
   - There is no held-out-motion test (e.g. train on a subset of motions and test on unseen ones, or on novel combinations).

2. **The baselines are not matched in data exposure.**
   - The obvious controls are missing: AC3D or CogVideoX LoRA fine-tuned directly on the same synthetic videos with no disentanglement, and fine-tuning on a small number of real or other-source videos with the same motions.
   - Without these, the paper cannot separate "any fine-tuning on the target motions helps" from "the disentanglement design helps." Only the realism side is ablated.
   - The comparison with real data (Table 5) uses RealEstate10K, which the authors admit lacks these motions. That test cannot show whether synthetic data is as good as real data for unconventional motions. Table 5 also uses only 500+500 videos and one trajectory model, so the claim of realism "comparable to models trained on real footage" is weakly supported.

3. **The optical-flow loss is neither optical flow nor ablated.**
   - Eq. 5 is an L1 loss on differences of consecutive predicted and ground-truth frames. This is a frame-difference (temporal gradient) loss and is appearance-dependent. It is not appearance-invariant supervision as claimed, since it constrains the synthetic content's pixel changes.
   - It is presented as a key component ("appearance-invariant supervision"), but no ablation or λ value is given, and Eq. 5 operates on reconstructed X̂0 from a latent diffusion model. It is unclear whether the loss is computed in latent or pixel space. The paper does not say whether it helps, or whether it hurts realism by pushing synthetic motion statistics into the model.

4. **The metrics are weak or unreliable.**
   - FVD values of 1500–2500 on 100 prompts per category are far from a regime where FVD is meaningful. FVD at this sample size is very noisy. The reference set for FVD is never stated.
   - TransErr and RotErr require camera-pose estimation from generated videos. The estimator (COLMAP, etc.), the ground-truth trajectory source for the text-based setting, and the scale handling are not described in the main text. The authors themselves note these metrics are "potentially unfair" for the text-based setting, yet Table 2 includes VividCam-Cog and CogVideoX.
   - Pose-estimation failures on shake and rotation motions probably dominate the complex-category numbers.
   - In Table 2, VividCam is not uniformly better. CogVideoX has better RotErr on simple and composed motions (0.0297 vs 0.0407 on simple), VividCam-AC3D has worse RotErr than AC3D on simple motion, and FVD is worse than baselines in several cells (complex Cog: 1866 vs 1488). The text glosses over these.
   - The "realism comparable to baselines" claim therefore rests mainly on the MTurk study.

5. **The human study is small and has no statistics.**
   - 25 prompts × 2 repeats per category, rated 0–2, with $0.03 per question. There are no confidence intervals, no inter-rater agreement, no significance tests, and no attention checks are reported.
   - Many of the claimed differences are 0.01–0.05 (e.g. Realism 0.74 vs 0.74, 0.68 vs 0.68, 0.78 vs 0.72), and VividCam-AC3D is equal to AC3D on simple Action Correctness. Claims such as "consistently generates more precise camera motion" cannot be judged without variance.
   - It is unclear whether raters were blind to method and whether the order was randomized.
   - Table 4 shows w/o S-Prompt has identical Action Correctness (0.93) and only a 0.09 difference in Realism. The evidence that the style-aligned prompt matters is thin given the noise level.

6. **The ablations are limited.** There are no ablations on:
   - the number or diversity of synthetic videos;
   - scene complexity, even though the paper's own premise is that simple scenes suffice (no comparison with richer or realistic synthetic scenes such as the ones it cites);
   - LoRA rank;
   - the single-LoRA multi-motion design;
   - appearance leakage in the trajectory setting, where the appearance LoRA sits on the diffusion model but only the encoder is trained.

   There is also no quantitative measure of residual synthetic-style leakage (e.g. a classifier or FID against low-poly renders). Leakage is only shown qualitatively.

7. **Scope and robustness are unclear.**
   - Only one base model family (CogVideoX-5B and AC3D on top) is used, so it is unclear whether the method transfers to other backbones.
   - Camera motion learned from low-poly scenes with simple, mostly static geometry may couple with scene content. There is no analysis of whether the learned motion transfers to content far from the training scenes (large dynamic scenes, humans, indoor scenes).
   - Failure cases are not shown, and the limitations discussion is missing.
   - Prompts like "pan around searching for X, then lock focus" depend on a semantic target, and the Unity data contain no such semantic target. It is unclear what is actually learned (a motion pattern vs. a prompt-conditioned behavior), and whether the model finds the object or just replays a fixed motion.

8. **Novelty is moderate.** The appearance/motion split follows AnimateDiff, and training on synthetic data for camera control is already done (Fu et al., Shuai et al.). The contribution is mostly the application of these techniques plus a style tag. The disentanglement claim is also not accompanied by analysis of why it works, e.g. why discarding a LoRA suffices when the camera LoRA is trained on top of it and could still carry style.

9. **Presentation.**
   - The text-based and trajectory-based setups are described in parallel with notation that is hard to follow (θ_d, Δθ_c^d, Δθ_c^e).
   - Eq. 1–2 are missing the squared or norm operator.
   - Several listed motions (dolly zoom, explosive shake, rotation) have no dedicated quantitative breakdown.
   - Key results are only in videos on a webpage, which I could not evaluate.

## Questions
1. Can you show generalization to motions or compositions not present in the training set (held-out motion types)? What is the text-based model's behavior when given a novel camera instruction?
2. What are the results for AC3D or CogVideoX fine-tuned on the same synthetic data without the appearance LoRA, style prompt and flow loss, with realism measured? Table 4 only partially covers this (no A-LoRA, no S-Prompt).
3. What is the effect of L_flow (ablation, λ)? Is it computed in pixel space? Why is it called optical flow?
4. How are TransErr and RotErr computed for generated videos, and what is the ground truth for the text-based setting? How many generated videos fail pose estimation? What is the FVD reference set?
5. Please give confidence intervals and significance tests for Tables 2–5, inter-rater agreement for the human study, and whether raters were blind to method.
6. Does the learned "seek then focus" motion actually depend on object location in the generated scene, or is it a fixed motion pattern?
7. How does performance vary with the number of synthetic videos, scene richness, and different base models?

## Ratings
- **Soundness: 2/4.** The qualitative results look promising, but the evidence is noisy, the key controls are missing, and the generalization claim is untested.
- **Presentation: 3/4.**
- **Contribution: 2/4.** A useful practical recipe, but the components are mostly known and the evaluation does not establish the headline claim.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**
