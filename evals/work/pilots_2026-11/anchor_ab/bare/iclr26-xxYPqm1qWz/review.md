# Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

*Note: I reviewed the PDF text extraction only. I could not see figures (Fig. 1-12, including the loss curves and the Figure 5/6 bar charts). Where a claim depends on a figure, I used the caption and the numbers stated in the text and tables.*

## Summary

The paper proposes VideoAgentTrek, a pipeline that mines computer-use trajectories from screen-recorded YouTube tutorials. It has four parts:

1. **Video collection.** Seed-keyword search is followed by channel-level expansion: a channel is accepted when at least 80% of sampled videos pass. This yields 55.6k videos, about 10k hours.
2. **ScreenFilter.** A YOLOv8 cursor detector keeps segments with a visible cursor, about 7.4k hours.
3. **Video2Action, an "inverse dynamics module".** It has two parts, both fine-tuned from Qwen2.5-VL-7B on OpenCUA screen recordings with logged input events:
   - a dense action-event detector that outputs (type, t_start, t_end);
   - an action-parameter recognizer that outputs click coordinates, typed text, and so on.
4. **Inner monologues.** GPT-5 generates a first-person thought for each step from keyframes, the action, and ASR context.

Applied to 39k videos, the pipeline yields about 1.52M steps (about 26B tokens). A Qwen2.5-VL-7B agent is continued-pretrained on this data (Stage 1), then SFT'd on about 8B tokens of human trajectories from OpenCUA/AGUVIS (Stage 2). Results:

- **OSWorld-Verified:** Stage-2-only reaches 9.3%. Stage 1+2 reaches 14.1% (20 steps, mean of 3 runs) and 15.8% (50 steps, single run).
- **AgentNetBench step SR:** 64.1% rises to 69.3%.
- **Data scaling:** using 0/50/100% of the video tokens shows a monotone trend.
- **IDM evaluation:** the detector scores F1 0.78 on a 23-hour held-out set. The parameterizer scores 65.8% accuracy in a 500-sample manual study.

## Strengths

- **Important problem and scalable data source.** Data scarcity is a central bottleneck for computer-use agents. Turning abundant passive tutorial videos into action-labelled trajectories is a natural and well-motivated idea, in the spirit of VPT, for the GUI domain. Recovering both the timing and the parameters of actions goes beyond earlier tutorial-mining work such as AgentTrek, which replays text tutorials.
- **Substantial engineering and scale.** The work covers 55k videos, 1.52M steps and 26B tokens. Channel-coherence-based discovery is a sensible, cheap way to scale recall. The ScreenFilter throughput (about 840 h per GPU-day) is practical. The authors say they will release ScreenFilter and Video2Action, which would be useful to the community.
- **Consistent downstream gains in a controlled comparison.** Stage-2 is held fixed, and adding Stage 1 improves OSWorld-Verified 20-step SR from about 9.3% to about 14.1%. That gap is clearly larger than the run-to-run spread reported in Table 4 (9.13-9.42 vs 13.57-14.68). AgentNetBench improves by +5.2 points.
- **Data-scaling ablation.** The 0/50/100% ablation shows a monotone trend on both benchmarks. This is at least suggestive that more video data helps.
- **Honest component-level evaluation.** The paper reports per-type precision/recall for the detector and per-type accuracy for the parameterizer, including weak categories (press: recall 0.08; drag/press accuracy about 0.36). This makes the noise level of the mined data visible.
- **Long trajectories.** The mined trajectories average about 39 steps, much longer than existing corpora, which is potentially valuable for long-horizon training.

## Weaknesses

1. **No compute- or token-matched control, so the cause of the gain is unclear.** The only comparison is Stage-2-only vs Stage 1 (26B extra tokens) + Stage 2. Several alternative explanations are not ruled out:
   - **Extra compute and GUI-image exposure.** The 26B extra tokens may help regardless of whether the action labels are correct.
   - **GPT-5 reasoning distillation.** GPT-5 monologues cover 1.52M steps.
   - **Grounding data.** Stage 1 includes "a small number" of OSWorld-G grounding pairs, and it is unclear whether Stage-2-only also sees them.

   Missing ablations that would isolate the contribution of the IDM labels:
   - (a) Stage 1 on the same frames with captions or monologues only, without action labels;
   - (b) Stage 1 without inner monologues;
   - (c) Stage 1 with deliberately degraded labels, such as random coordinates or a weaker IDM;
   - (d) a token-matched baseline with more human or synthetic trajectories, or upsampled Stage-2 data.

   Without these, the claim that "passive internet videos can be transformed into high-quality supervision" is not established. A broad "GUI-video continued pretraining helps" claim would be more defensible.
2. **Weak baselines and low absolute performance.** All comparisons are internal to one 7B backbone. There is no comparison with other data-generation methods:
   - AgentTrek-style tutorial replay;
   - OS-Genesis-style synthesis;
   - VPT-style IDM labelling with a simpler IDM.

   There is also no comparison with contemporary open 7B computer-use agents trained on similar human data, such as OpenCUA-7B or UI-TARS-7B. The final 15.8% on OSWorld-Verified appears well below what published 7B agents trained on OpenCUA-like data report. This makes it hard to judge whether the video data helps a competitive recipe or only a weak Stage-2 baseline. At minimum, the authors should explain why their Stage-2-only model (9.3%) is weaker than published models trained on similar data.
3. **The headline numbers mix protocols.** The abstract and contributions use 15.8%, a single 50-step run, and compute the "70% relative improvement" against a 20-step-averaged baseline. The more reliable 20-step mean is 14.1% (+52%).
   - The test-time-scaling claim (14.13 to 15.78) rests on one 50-step run. The 1.65-point gain is comparable to the spread across the three 20-step runs (13.57-14.68). Section 4.2's interpretation ("teaches the model to decompose complex tasks into subgoals, persist through intermediate failures...") is not supported by any analysis.
   - The scaling study's "SR@50" numbers (13.3, 15.7) also appear to be single runs.
4. **The IDM is overclaimed and the label quality is modest.**
   - **"Unsupervised" / "without manual annotation".** The IDM is trained on OpenCUA's human-collected interaction logs (154 h for the detector, 512k clips for the recognizer). The pipeline is weakly or self-supervised at deployment, not unsupervised.
   - **"Millisecond-precision temporal localization".** This is never measured. The detector runs on 4 fps video with a temporal patch of 2 frames, and the hit criterion is "any temporal overlap" with matching type, which is very lenient. Please report boundary error and IoU-thresholded metrics.
   - **Held-out evaluation is in-distribution.** It is held-out OpenCUA data. The in-the-wild check covers only 10 YouTube videos and reports a single "~70% recovery" figure, with no annotator count or agreement statistic.
   - **Parameterizer accuracy.** It is 65.8% overall, judged by a lenient "plausibly produces the observed transition" criterion. Combined with 0.70 detection recall, a large fraction of steps are missing or mislabelled. The paper never quantifies the end-to-end quality of mined trajectories, for example the per-trajectory step-error rate on a manually annotated subset of YouTube videos.
5. **No contamination analysis.** The corpus is mined from tutorials on Ubuntu, Chrome, LibreOffice, GIMP, VS Code, VLC and similar apps, which are exactly the OSWorld application buckets. Many OSWorld tasks are derived from common how-to queries. A decontamination check, for example task-instruction overlap with video titles or transcripts, is needed before attributing the OSWorld gains to generalization. AgentNetBench is drawn from the same AgentNet/OpenCUA distribution as the Stage-2 data and the IDM training data, so its gains are in-distribution.
6. **Long-horizon claims are weakly grounded.**
   - **Trajectory definition.** A "trajectory" here appears to be all detected actions in a video, not a goal-directed task, so the average of 39 steps is not comparable to the task-level step counts of other datasets in Table 9.
   - **Estimated average.** The average is "estimated from a 5,416-trajectory sample", even though all 39k trajectories are available.
   - **Missing task-level structure.** It is unclear how task instructions are created for Stage-1 trajectories, or whether any exist.
7. **Inconsistencies and presentation problems.**
   - **Recall.** The text says recall 0.71, but Table 1 says 0.70.
   - **Table 8 shares.** Mouse move (8,441) and drag (6,372) are listed as 0.1% each, but they are about 0.5% and 0.4%.
   - **Table 6.** The rows sum to 53,375, not 55,603.
   - **Table 3.** moveTo and dragTo have identical counts (32,840).
   - **Figure references.** Section 4.2 cites "Figure 10" for the step distribution, but Figure 10 shows training-data formats (Table 10 is meant).
   - **Appendix D.**
     - It calls the recognizer "our dense detector".
     - It has a dangling "Figure" reference.
     - Its frame-rate policy says it "caps at 20" but the formula caps at 30.
   - **Table 5.** "terminate" accuracy drops sharply after Stage 1 (0.588 to 0.237), which is unexplained and might matter for OSWorld.
   - **Writing.** Section 2.3 says "Agent Traing". The appendices are thin: the training configurations live only in figures, and the Stage-1 data mixture is not specified quantitatively.
8. **Ethics, licensing and reproducibility.** The paper scrapes and trains on 55k YouTube videos, with narration transcripts passed to GPT-5. The appendix gives only one line on "license/PII checks". It does not discuss copyright or ToS compliance, consent, or whether the mined dataset (as opposed to the tools) will be released. Reproducing Stage 1 also depends on GPT-5 annotations.

## Questions

1. Can you provide a token-matched control for Stage 1? For example, the same frames with (i) no action labels, or (ii) no GPT-5 monologues, or (iii) the same token budget of additional human or synthetic trajectories. Does the Stage-2-only baseline receive the OSWorld-G grounding pairs?
2. How do your Stage-2-only and Stage 1+2 models compare with published 7B agents trained on OpenCUA/AgentNet data, under the same OSWorld-Verified step budget? Why is the Stage-2-only baseline at 9.3%?
3. Can you report multiple 50-step runs (and 100-step if feasible) for both models, with confidence intervals, so the test-time-scaling claim can be assessed?
4. What is the end-to-end error rate of mined trajectories on a manually annotated YouTube subset, combining missed detections, spurious detections and wrong parameters? How sensitive is downstream performance to label quality?
5. What temporal boundary error does the detector achieve, given that the paper claims millisecond precision at 4 fps?
6. Did you check overlap between the YouTube corpus (titles, transcripts, apps) and OSWorld tasks?
7. How are Stage-1 trajectories framed: is there a task instruction, or are they goal-free action sequences? How is a 39-step "trajectory" segmented from a video?
8. Why does terminate accuracy on AgentNetBench drop from 0.588 to 0.237 after Stage 1?
9. Will you release the mined dataset, and how were copyright and PII handled?

## Ratings

- **Soundness:** 2. The core gain is plausible and larger than the run-to-run spread, but it lacks controls that isolate the contribution of the IDM labels. The test-time-scaling and long-horizon claims are under-supported, and the IDM precision claims are not measured.
- **Presentation:** 2. The structure is clear, but there are numerous numerical inconsistencies, broken references, overclaiming ("unsupervised", "millisecond precision", the "70%" headline) and thin appendices.
- **Contribution:** 3. A useful, scalable data pipeline and tools for an important problem, with some evidence that it helps. Its significance is limited by weak baselines and low absolute performance.

**Rating:** 6 (marginally above the acceptance threshold). The idea and scale are valuable, and the controlled Stage-1 ablation gives a consistent signal. To be confidently accepted, the paper needs token-matched controls, external baselines, a contamination analysis and corrected or toned-down claims.

**Confidence:** 4
