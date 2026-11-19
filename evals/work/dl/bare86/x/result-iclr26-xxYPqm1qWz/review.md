# Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

(Based on text only. Figures were not available, so I judged figure-dependent claims from captions and text.)

## Summary
The paper proposes a pipeline that mines computer-use trajectories from screen-recorded YouTube tutorials.
1. Video collection uses seed keywords, channel expansion and a YOLOv8-based cursor detector (ScreenFilter).
2. Video2Action is an inverse-dynamics module made of two fine-tuned Qwen2.5-VL-7B models. One does dense, typed temporal event detection. The other does action parameterization (click coordinates, typed text). Both are trained on OpenCUA logs. GPT-5 then writes an "inner monologue" for each step.
3. About 39k videos yield 1.52M steps and 26B tokens. A Qwen2.5-VL-7B agent is trained in two stages: one epoch on the mined data, then 8B tokens of human trajectories (OpenCUA/AGUVIS).

The reported results are OSWorld-Verified 9.3% (stage-2 only) → 14.1% (20 steps) / 15.8% (50 steps), and AgentNetBench 64.1% → 69.3%. The authors also report data-scaling (0/50/100% of stage-1 tokens) and a "test-time scaling" observation. Video2Action is evaluated by detector P/R/F1 on a 23-hour held-out set (F1 0.78) and by manual review of 500 predictions in the wild (65.8% accuracy).

## Strengths
- The problem matters and is timely. Computer-use data is scarce, and turning abundant tutorial videos into (screenshot, action, parameters) supervision is a sensible, VPT-style idea at a useful scale (about 10k hours of raw video, 7.4k hours after filtering).
- The system is complete end to end: collection, filtering, IDM, thought generation, training. The authors plan to release ScreenFilter and Video2Action.
- The monotone trend with 0/50/100% of stage-1 data (OSWorld 9.3 → 13.3 → 15.7; AgentNetBench 64.1 → 68.1 → 69.3) suggests that the mined data helps.
- The IDM is evaluated honestly in places. Per-type results are reported, including weak ones (press and drag), and the in-the-wild manual accuracy of 65.8% is disclosed.
- The mined trajectories are longer than those in existing corpora (average 39 steps), which is a practically useful property.

## Weaknesses
1. **The headline claim (70% relative improvement, 9.3 → 15.8) is not a like-for-like comparison.**
   - 15.8% is the 50-step-budget number, and the 14.13% at 20 steps is a 52% relative gain (Sec. 3.1.2 shows both).
   - The abstract and conclusion use the more favorable number.
   - The stage-2-only baseline is reported as exactly 9.3% at both budgets, but no run-to-run variance is given for any number.
   - OSWorld-Verified has 369 tasks, so 1 task is about 0.27 points. The 20→50 step gain of 1.65 points is about 6 tasks. With a single seed and no confidence intervals, the "test-time scaling" claim rests on very thin evidence.
2. **There is no compute- or data-matched control.**
   - Stage 1 adds 26B tokens of extra training, on top of the 8B stage-2 tokens. The baseline never sees them.
   - It is not shown that the gain comes from video-derived trajectories. It could come from extra training on any GUI-related data, such as more OpenCUA-like data, synthetic or noisy labels, or the generic effect of a longer curriculum and the GPT-5 reasoning text.
   - Useful controls would be (a) stage 1 on the same tokens with shuffled or corrupted actions, (b) stage 1 on the human-annotated data repeated or at matched token count, (c) stage 1 without inner monologues, and (d) a naive pseudo-labeling baseline (heuristic cursor/OCR labels).
   - The paper's central question is whether the IDM-mined labels add value, and none of these ablations isolates it.
3. **Weak external comparison.**
   - No comparison is given with other 7B open agents (OpenCUA-7B, UI-TARS-7B, AGUVIS, AgentTrek). It is not even clear whether the stage-2-only baseline reproduces OpenCUA-7B's published results.
   - 15.8% on OSWorld is low in absolute terms. It is unclear where the system stands relative to published methods that use the same human data.
   - The "SFT-only baseline" is the authors' own, and its 9.3% is hard to calibrate.
4. **Train/test overlap and in-domain evaluation.**
   - The IDM is trained on OpenCUA logs, and stage 2 also uses OpenCUA data.
   - AgentNetBench comes from the AgentNet/OpenCUA distribution, so the offline benchmark is in-domain for stage 2. The 5.2-point gain there is modest and again unreplicated.
   - The 23-hour "held-out" IDM test set is said to come from the "source corpus". Its split (by video, by user, by app) is not described.
   - OSWorld is Ubuntu-only. The mined videos are mostly Windows/macOS/web (by the authors' account), so the claim of cross-platform transfer is untested. Mismatch is not analyzed.
5. **Data quality of the mined labels is poor and its effect is not analyzed.**
   - Detector recall is only 0.70 overall (press 0.08, drag 0.52). Missed actions create trajectories with gaps, so the "steps" are not contiguous, and the paper does not discuss how this affects state-action consistency.
   - Parameterization accuracy is only 65.8% (click 71%, drag 37%, press 36%). So roughly a third of the mined parameters are wrong or judged not "plausibly" correct.
   - The click accuracy criterion is "plausibly produces the observed transition", which is lenient. It is not coordinate precision, so the "high fidelity" and "millisecond-precision" claims in the abstract and contributions are not supported.
   - There is no analysis of noise versus downstream performance, such as filtering by confidence or training on the subset with correct labels.
   - The in-the-wild evaluations are tiny: 10 videos for detection and 500 manually judged predictions, with no inter-annotator agreement reported.
   - The detector's "hit" criterion is any temporal overlap with matching type, which is very loose and inflates precision and recall. No IoU thresholds are used, which sits oddly with the "tight temporal boundaries" claim.
6. **Evaluation text/table inconsistencies.** Recall is 0.70 in Table 1 but 0.71 in the text. The text says action types are "reliably localized", yet drag recall is 0.52 and press is 0.08.
7. **Attribution of the long-horizon and test-time-scaling claims is speculative.**
   - Sec. 4.2 asserts that video pretraining "teaches the model to decompose tasks into subgoals, persist through failures, and leverage additional budget". This is not backed by any trajectory analysis.
   - Examples would be success rate by task horizon, error analyses, or failure modes.
   - The statement that the baseline "cannot plan beyond its training horizon" is an interpretation of one flat number.
8. **Methodological gaps and reproducibility.**
   - Cursor-based filtering (80% of frames contain a cursor for at least 6 s) will bias the data toward mouse-driven interaction and against keyboard-only interaction. It is validated only on synthetic cursor composites (F1 0.90).
   - The inner monologues come from GPT-5 given the post-action state and ±1-minute ASR. This creates hindsight leakage: the thought is conditioned on the outcome, but at test time the agent has no such information. Its effect is not ablated.
   - There are no stage-1 hyperparameters or learning-rate details for the agent in the main text.
   - The 39k videos used versus the 55k candidates is not explained.
   - There is no discussion of YouTube licensing, ToS, privacy (screen recordings can contain personal data), or data release. The data is described as "publicly available", but the paper does not say whether the trajectories will be released.
9. **Novelty is moderate.** The idea is the VPT inverse-dynamics recipe applied to GUI videos, using an off-the-shelf VLM fine-tuned on OpenCUA logs. Related work such as AgentTrek (tutorial-guided replay), Jang et al. (video-to-dataset) and VPT is cited, but there is no empirical comparison against alternatives such as AgentTrek-style synthesis. The related-work comparison is largely qualitative. Figures 5/6 compare only the authors' own variants.
10. **Presentation.** Some sections are written in a promotional register ("striking", "true test-time scaling"). Appendix D mislabels the parameterization model as the "dense detector". Some figure references are broken ("Figure" with no number). The Figure 1 caption/text is hard to follow.

## Questions
1. What are the OSWorld results (mean ± std over several seeds or runs) for stage-2-only and stage1+2 at both 20 and 50 steps? Does the stage-2-only model really not change at all with 50 steps?
2. Can you provide a compute/token-matched control, for example stage 1 on mined data with randomized actions, or on additional human-annotated data? What does stage 1 do with inner monologues removed?
3. How does the model compare with the published OpenCUA-7B, UI-TARS-7B and AGUVIS on the same benchmark and protocol?
4. How does downstream performance change if only high-confidence mined steps are kept? Can you quantify noise tolerance, or how much of the gain comes from the 30–35% incorrect parameters versus the correct ones?
5. What is the IDM evaluation under IoU-based temporal matching and coordinate-error metrics (e.g., click within the target element)? How was the 23-hour held-out set split relative to the training logs?
6. Are there OSWorld gains for task categories where tutorial content should help (office/Excel)? Are there per-domain breakdowns? Given the Windows/macOS-heavy videos, why does it transfer to Ubuntu?
7. Will the mined trajectories (not just the tools) be released? What is the legal and privacy position for redistribution?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 3
- Rating: 4
- Confidence: 4

**Rating justification.** The direction is valuable and the system is substantial. However, the central causal claim (that IDM-mined video labels give the improvement) lacks controls, uses a favorable-budget headline number, rests on single-run results on a 369-task benchmark, and the underlying label quality is demonstrably modest (65.8% parameter accuracy, 0.70 recall). With the controls, variance estimates and baseline comparisons above, this could become a solid paper. In its current form it falls below the acceptance threshold.
