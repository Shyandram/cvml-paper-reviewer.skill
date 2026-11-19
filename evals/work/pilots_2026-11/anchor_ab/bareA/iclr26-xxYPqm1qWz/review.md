# Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

Note: I worked from extracted PDF text only. Figures (loss curves, the pipeline diagrams, the Figure 5/6 bar charts) were judged from captions, the numbers in the text and the appendix tables.

## Summary

The paper describes a pipeline that turns YouTube screen-recorded tutorials into training data for computer-use agents (CUAs). It has three parts:
1. Video collection: seed-keyword search, then channel and tag expansion, gives 55k videos (about 10k hours). A YOLOv8 cursor detector (ScreenFilter) keeps about 7.4k hours of GUI footage.
2. Video2Action, an inverse dynamics module (IDM). It has (a) a Qwen2.5-VL-7B dense action-event detector, giving action type plus start/end time, and (b) a Qwen2.5-VL-7B action parameterizer, giving click coordinates, typed text and so on. Both are trained on OpenCUA screen recordings with logged input events. GPT-5 then writes an inner-monologue rationale for each step from keyframes and ASR transcripts.
3. Agent training. Stage 1 is continued pretraining of Qwen2.5-VL-7B on 26B tokens of mined trajectories (39k videos, 1.52M steps). Stage 2 is SFT on 8B tokens of OpenCUA/AGUVIS human trajectories.

Results against the Stage-2-only baseline:
- OSWorld-Verified: 9.3% to 14.1% at a 20-step budget (mean of 3 runs) and 15.8% at 50 steps (single run).
- AgentNetBench step SR: 64.1% to 69.3%.
- A three-point data-scaling curve (0/50/100% of the Stage-1 tokens) and a test-time step-budget analysis support claims about scaling and long-horizon planning.

## Strengths

- **S1. Important, well-motivated problem and a natural idea, executed at scale.** Annotating CUA trajectories is expensive, while tutorial videos are plentiful. Carrying VPT-style inverse-dynamics labelling over to GUI video, with recognition of structured parameters (coordinates, typed text), is a sensible and timely direction. The scale (1.52M steps, 39 steps per trajectory on average) is large compared with existing CUA corpora (Table 9).
- **S2. The downstream gain is real and consistent within the controlled comparison.** With the same Stage-2 SFT, adding Stage 1 improves OSWorld-Verified in all three 20-step runs: 13.6–14.7% against 9.1–9.4%, with low variance (Table 4). It also improves AgentNetBench overall and on most action types (Table 5). The gain spreads across several app buckets (chrome, writer, thunderbird, os, impress).
- **S3. Monotonic data-scaling trend.** At 0/50/100% of the Stage-1 tokens, performance rises on both benchmarks (Figure 6). This suggests the mined data is not saturating.
- **S4. Component-level evaluation of the IDM is reported, including failure modes.** Detector P/R/F1 by action type on a 23-hour held-out set (Table 1), and a 500-sample blinded manual check of the parameterizer (Table 2). The paper is candid that press/drag are weak.
- **S5. Practical artifacts.** The paper promises to release ScreenFilter and Video2Action. The appendices give collection criteria, prompts and training configurations, which help reproduction.

## Weaknesses

- **W1. No compute- or token-matched control: the gain cannot be credited to the video-mined data.** The treatment model gets 26B extra tokens of Stage-1 training. The baseline goes straight from Qwen2.5-VL-7B-Instruct to 8B tokens of SFT. Any extra in-domain training (more epochs over OpenCUA/AGUVIS, GUI grounding data, or synthetic trajectories) might give a similar gain. The paper needs at least one baseline with the same Stage-1 budget on alternative data, such as the human data repeated or the grounding data alone. The 0/50/100% scaling curve has the same confound: token count and data source change together.
- **W2. Ablations of the pipeline components are missing.** The paper claims the gains come from IDM-recovered actions and long trajectories. Yet the Stage-1 text also contains GPT-5-generated rationales and action descriptions, conditioned on ASR and keyframes. Without ablations it is unclear how much of the gain comes from distilled GPT-5 reasoning text and how much from the recovered actions and coordinates. The missing ablations are:
  - with and without inner monologue;
  - with and without action parameters (for example, actions without coordinates);
  - noisy labels against filtered labels;
  - with and without the small amount of grounding data mixed into Stage 1.

  Without them, the paper's core claim, that passive videos turned into actions through learned inverse dynamics give effective supervision, is not isolated.
- **W3. Weak absolute performance, and no comparison with existing open CUAs.** The final 7B model reaches 14.1% (20 steps) or 15.8% (50 steps) on OSWorld-Verified. The paper does not report OpenCUA-7B, UI-TARS(-1.5)-7B, AGUVIS-7B or similar models under the same protocol. Several of these are trained on the same human data used in Stage 2 and, to my knowledge, report clearly higher OSWorld numbers. The Stage-2-only baseline at 9.3% looks under-tuned relative to such models. This raises two concerns:
  - the improvement may partly reflect a weak baseline;
  - it is unknown whether the video data helps a competitive recipe.

  The conclusion that the data is "high-quality supervision" and a "viable alternative to manual annotation" is also not tested. Every result still depends on human SFT data, and there is no video-only (Stage 1 alone) agent result on OSWorld.
- **W4. Statistical support for the long-horizon / test-time-scaling claim is thin.**
  - The 50-step numbers are single runs. The 20-step treatment runs already span 13.57–14.68%, so a single 50-step run at 15.78% (about 2–4 tasks more than the 20-step runs) is not clearly above noise.
  - Section 4.2 attributes the effect to learning to "decompose complex tasks into subgoals, persist through intermediate failures" (from Section 4.2), but no analysis supports this mechanism: no trajectory analysis, no error-recovery measurement, and no control with matched trajectory length.
  - The headline "70% relative improvement" compares a single 50-step run (15.78) against a 20-step average (9.3). The baseline's own 50-step run is 9.27, so the comparison happens to be similar, but the presentation is inconsistent with the 20-step averages in Section 3.1.2 (+52%).
- **W5. IDM label quality is modest, and its effect is unquantified.**
  - Overall detector recall is 0.70, and recall for press is 0.08.
  - The parameterizer is correct on only 65.8% of 500 sampled actions (drag 37%, press 36%). Roughly a third of mined steps may therefore carry wrong parameters.
  - The hit criterion, "any temporal overlap", is very lenient and conflicts with the claimed "millisecond-precision temporal localization".
  - The in-the-wild detector check uses only 10 videos.
  - The paper does not study how label noise affects downstream performance, or whether confidence filtering helps.
- **W6. Possible overlap between IDM/SFT training data and the AgentNetBench evaluation.** The IDM is trained on OpenCUA raw recordings, Stage 2 uses OpenCUA trajectories, and AgentNetBench is built from AgentNet tasks. The paper should state explicitly that the AgentNetBench tasks and recordings are excluded from all training sources.
- **W7. Claims of "without manual annotation" / "unsupervised" are overstated.** The IDM needs 154 hours of human-recorded, event-logged demonstrations. Collection includes human-in-the-loop seed validation. Labelling also depends on GPT-4.1 and GPT-5. The real claim is that a modest amount of instrumented data is amplified, which is fine, but it should be framed that way. The cost trade-off should be quantified: how many labelled hours of OpenCUA data are worth one IDM-labelled hour.
- **W8. Novelty relative to close prior work is under-discussed.** Related work is brief. The paper should position itself more concretely against:
  - VPT (the same IDM-then-pretrain recipe in Minecraft);
  - AgentTrek (web tutorials guiding trajectory synthesis);
  - Jang et al. 2025 (video-to-dataset for mobile agents);
  - other recent tutorial-video GUI corpora.

  The technical novelty lies mainly in engineering (a fine-tuned Qwen2.5-VL for dense detection and parameterization). Nothing new is learned about why video pretraining helps.
- **W9. Presentation problems and internal inconsistencies.**
  - Recall is 0.70 in Table 1 and 0.71 in the text; 15.78 appears elsewhere as 15.7.
  - Appendix D says "our dense detector is trained on 512,000 clips". This is presumably the parameterizer.
  - The frame-rate text says frames are capped at 20, but the formula gives min{30,·}.
  - Table 3 gives identical counts for moveTo and dragTo (32,840).
  - Table 8 lists mouse move at 8,441 = 0.1% and drag at 6,372 = 0.1%; these should be about 0.5% and 0.4%.
  - 55k videos from "50+ channels" seems inconsistent with keyword-search collection.
  - A stage-2 entry in Table 5 is "—".
  - A dangling "Figure" reference appears in Appendix D, and Appendix H is promised but thin.
  - Stage-1 trajectories have no stated task instruction, and the paper does not say how this is handled.
- **W10. Data ethics and licensing.** Mining and redistributing YouTube content (frames, ASR, typed text, which may include PII such as the "lilybloom123." password-like example in Figure 9) needs a clearer discussion of terms of service, consent, PII scrubbing and what exactly is released. Appendix H mentions "license/PII checks" (from Appendix H) only in passing.

## Questions

1. Can you add a Stage-1 control with the same token budget on non-video data (for example, OpenCUA/AGUVIS repeated, or grounding data only), so the gain can be credited to the video-mined trajectories?
2. What is the effect of removing the GPT-5 inner monologues from Stage 1? What if action parameters are kept but the monologues are replaced by templated text?
3. How does your Stage-2-only baseline compare with OpenCUA-7B and UI-TARS-7B under your OSWorld-Verified protocol? Does Stage 1 still help when added to a competitive recipe?
4. Can you report several runs at the 50-step budget for both models, with confidence intervals?
5. Are any AgentNetBench tasks or recordings, or their sources, in the IDM training data or the Stage-2 SFT data?
6. What does Stage-1 data look like without a task instruction? Is a pseudo-instruction generated per video? If so, how?
7. Have you tried filtering mined steps by IDM confidence? How does downstream performance change with label accuracy?
8. What exactly will be released (models, mined trajectories, video IDs)? How are YouTube ToS and PII handled?

## Scores

- Soundness: 2. The core comparison lacks a compute-matched control and component ablations. The test-time-scaling claim rests on single runs.
- Presentation: 2. The paper is readable, but has many numerical and copy-paste inconsistencies and a thin related-work section.
- Contribution: 3. A useful, scalable data source with a positive signal and planned tool release, but the source of the gain is unclear and absolute results are well below current open models.

## Calibration bracket

- **Above anchor C (careful study without insight, ~50).** This paper shows something new working rather than benchmarking known methods. Web tutorial videos, auto-labelled by a learned GUI IDM, improve a CUA in a controlled same-SFT comparison: consistent across three runs (S2), with a monotonic scaling trend (S3) and component-level IDM measurements (S4). That is a contribution of the "new data source that works" kind, which C lacks.
- **Below anchor D (clear contribution with ordinary weaknesses, ~72).** D measured the mechanism behind its gain and compared against competitive systems. Here:
  - the gain is not credited to the video data, because there is no token-matched control (W1) and no ablation of the GPT-5 monologue or the parameters (W2);
  - absolute numbers are not compared with existing open 7B CUAs, and the baseline appears under-tuned (W3);
  - the long-horizon mechanism claim rests on single runs and speculation (W4).

  These weaknesses go beyond D's ordinary ones, because they touch the central attribution claim.
- **Placement.** About 58 in the pool: just above C and well below D, because the central attribution is unverified. This corresponds to rating 4 (marginally below the acceptance threshold). Convincing answers to Q1–Q4 could move it to 6.

## Rating

4 (marginally below the acceptance threshold)

## Confidence

4
