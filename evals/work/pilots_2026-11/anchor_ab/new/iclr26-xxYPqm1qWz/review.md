# Peer Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | empirical (method + data pipeline, evaluated on agent benchmarks) |
| Field, sub-area | machine learning / multimodal agents; computer-use (GUI) agents, learning from unlabeled video |
| Task | Computer-use / GUI agents trained from mined video demonstrations. Not a row of `references/task_neighbors.md`; adapted from "Vision–language models, multimodal LLMs" (main claim), with "Video understanding, tracking" (the event detector) and "Reinforcement learning" (inverse dynamics, behaviour cloning) as secondary rows |
| Neighboring fields | (1) learning from observation / imitation learning and robotics (VPT-style inverse-dynamics labelling) [added beyond the file]; (2) temporal action localization and dense video event detection; (3) VLM/LLM pretraining and data scaling; (4) web and LLM agents and their evaluation; (5) responsible web-data collection, copyright and privacy [added beyond the file]; (6) HCI / UI understanding [added beyond the file] |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | technical_rigor 23%, experimental_validation 19%, novelty 16%, significance 16%, clarity 10%, reproducibility 9%, ethics 8% (`aggregate_scores.py ratio --paper-type empirical --venue iclr`) |
| Literature check | off: no network access in this run. Novelty is judged against the paper's own related work and recalled literature; uncertain recalled entries are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

The reviewers' copy came from `integrity_scan.py --redact`. The scan found no text addressed to reviewers and no hidden characters. It redacted one venue/acceptance mark in a reference entry. The figures were not available: figure content is judged from captions and surrounding text only, and this is stated where it matters (Figures 5, 6, 10 are read through Table 4, Table 5 and the text).

---

## 1. Paper memory

**Claims.**
- C1: Video2Action, an inverse-dynamics module (dense action-event detector + action parameterizer, both fine-tuned Qwen2.5-VL-7B), accurately recovers GUI actions and their parameters from raw video (Abstract; §1 bullet 2, which claims "millisecond-" precision localization; §2.2; §3.2).
- C2: The pipeline turns 39,000 YouTube videos into 1.52M interaction steps (≈26B tokens) "without manual annotation". The data are diverse ("hundreds of applications across Windows, macOS, and web platforms") and long-horizon (39.25 steps on average) (Abstract; §1; §2.3.1; §4.2; Table 9).
- C3: Continued pretraining on this data, followed by SFT, raises OSWorld-Verified task success from 9.3% to 15.8% ("a 70% relative improvement") and AgentNetBench step success from 64.1% to 69.3% (Abstract; §3.1.2; Figure 5; Tables 4–5).
- C4: Performance grows with the amount of video pretraining data: 0%, 50% and 100% give 64.1/68.1/69.3 on AgentNetBench and 9.3/13.3/15.7 SR@50 on OSWorld (§4.1, Figure 6).
- C5: Video pretraining enables test-time scaling and long-horizon planning. The model goes from 14.13% at 20 steps to 15.78% at 50, while the SFT-only model stays flat (§3.1.2, §4.2).
- C6: A reproducible pipeline. ScreenFilter and Video2Action are released as open-source tools (§1 bullet 4; §6).

**Setup facts.**
- Base model: Qwen2.5-VL-7B (§2.3.2).
- Stage 1: one epoch over 26B tokens of VideoAgentTrek trajectories, "with a small number of GUI grounding pairs". 32× H100, 6,500 iterations, global batch 512, ≈60 h (§2.3.2; Figure 11).
- Stage 2: 8B tokens of human trajectories from OpenCUA and AGUVIS. 64× H100, 3,000 iterations, batch 512, ≈16 h (§2.3.1–2.3.2; Figure 12). Grounding data: ≈1B tokens from OSWorld-G (§2.3.1). Whether the Stage-2-only baseline also sees the grounding data: not stated.
- Event detector: trained on 154 h of OpenCUA video with interaction logs (App. C; Table 3: 771,945 events). Videos are downsampled to 4 fps in 10 s clips with a temporal patch of 2 frames (App. C). 32× H100, ≈15 h (Figure 8).
- Parameterizer: trained on 512,000 clips from OpenCUA logs, with a dynamic frame rate (App. D).
- Inner monologue: GPT-5 Medium, given the action, the parameters, before/after keyframes and ±60 s of ASR (§2.2.3; App. E).
- ScreenFilter: YOLOv8x trained on 15,000 synthetic cursor composites; F1 89.58% (App. B). It keeps 7,377 h of 10,000 h (§2.1.2).
- Corpus: 55,603 videos from "50+ channels" (§2.1.3; App. H). Categories come from GPT-4.1 run on titles and descriptions (Tables 6–7, Figure 3).
- Evaluation: OSWorld-Verified with a 5-screenshot history. At 20 steps, three runs are averaged; at 50 steps, a single run. Inference settings are identical across models (App. G). AgentNetBench has 100 tasks (§3.1.1).
- Not stated: training seeds, learning rate and optimizer settings (Figures 8, 11, 12 list framework, batch size and iterations only); exclusion of benchmark tasks from the training data; the source of the 23 h held-out detector test set beyond "a small curated subset from the source corpus" (§2.2.1); whether the dataset or the trained agent is released; the license, consent and PII procedure.

**Headline numbers.**
- OSWorld-Verified: 4.5 (base), 9.3 (Stage 2 only), 14.13 (Stage 1+2, 20 steps, mean of 3 runs), 15.78 (50 steps, single run) (Figure 5; Table 4).
- AgentNetBench: 38.5 / 64.1 / 69.3 (Figure 5; Table 5).
- Detector: P 0.88 / R 0.70 / F1 0.78 (Table 1). Parameterizer: 0.658 accuracy on 500 manual samples (Table 2).
- Corpus: 1.52M steps from 39,000 videos (§2.3.1); 1,547,092 actions (Table 8).

**Could not be read.**
- Figures 1–12 as images: the bar values in Figures 5 and 6 come only from the extracted labels, and Figure 10 / Table 10 (step-length distribution) are garbled.
- The loss curves in Figures 8, 11 and 12.
- Appendix H promises "Detailed data statistics and examples", but only Tables 6–10 are present.
- No supplement or code was provided.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | Attacks the main bottleneck of computer-use agents, the scarcity of labelled trajectories, with a passive and abundant source: screen-recorded tutorials. If it works, the source scales far beyond human annotation | Abstract; §1 ("Training these agents requires extensive trajectories…"); §2.1: 55k videos, ≈10,000 h | strong | the mined labels being good enough (R7, R8) |
| A2 | empirical strength | A large, controlled gain on an online benchmark. At a matched 20-step budget, Stage 1+2 averages 14.13% against 9.32% for Stage 2 only over three evaluation runs each, and the per-run ranges do not overlap (13.57–14.68 vs 9.13–9.42) | Table 4; App. G "we conduct three independent runs per model" | strong (moderate after P1) | the gain being due to the video data rather than extra compute or grounding data (R1, R4) |
| A3 | empirical strength | At a matched 50-step budget the headline ratio holds: 15.78 / 9.27 = 1.70, i.e. 70% relative | Table 4 turn4 rows; Abstract | moderate | the single 50-step run being representative (R9, R10) |
| A4 | empirical strength | The offline benchmark improves too: AgentNetBench step SR goes from 64.1 to 69.3 (+5.2 pp), with gains on most action types (click 0.671→0.767, moveTo 0.300→0.502, rClick 0.214→0.417) | §3.1.2; Table 5 | moderate | no overlap between the AgentNetBench tasks and the Stage-2 data (R11); 100 tasks, no CI (R10) |
| A5 | empirical strength / significance | A data-scaling trend: 0%, 50% and 100% of the video tokens, each followed by identical Stage 2, give monotone gains on both benchmarks (64.1→68.1→69.3; 9.3→13.3→15.7) | §4.1; Figure 6 | moderate | three points, single runs (R10); compute grows with the data (R1) |
| A6 | resource / significance | A large, long-horizon corpus: 1.52M steps, 26B tokens, 39.25 steps per trajectory on average against 18.6 for AgentNet and 12.1 for AgentTrek | §2.3.1; Table 9 | moderate | the corpus being released (R13); the label quality (R8) |
| A7 | soundness | A clean two-stage IDM formulation: prompt-free dense typed-span detection f_θ(v)→{(a_k, ts_k, te_k)}, then per-segment parameterization h_φ(v_k)→(â_k, π_k). It is evaluated on 20,282 held-out events with per-type P/R/F1 (overall P 0.88, R 0.70) | §2.2.1–2.2.2; Table 1 | moderate | the held-out set being representative of YouTube video and the matching criterion being meaningful (R5, R7) |
| A8 | clarity / honesty | Weak spots are reported honestly: press recall 0.08, drag F1 0.62, drag/press parameter accuracy ≈0.36, and the limits of the metadata classifier | Table 1; Table 2; App. H "Limitations. Metadata-only classification can mislabel borderline cases" | moderate | — |
| A9 | novelty | A disclosed and argued transfer of VPT-style inverse-dynamics labelling from games/robotics to desktop GUIs. The transfer needed structured parameters (coordinates, literal text), dense typed spans and reasoning traces. This differs from AgentTrek's tutorial-guided replay and from instrumented annotation | §2.2 ("Following insights from robotics where inverse dynamics recovers actions from observations"); §5 (Baker et al., 2022; Xu et al., 2025a) | moderate | the delta over Jang et al. (2025) and VPT being shown (R14) |
| A10 | reproducibility | Many details are given: the video quality standards (App. A), the ScreenFilter thresholds (80% cursor frames, ≥6 s, 2 s merge; App. B), the frame-rate rule (App. D), the full monologue prompt (App. E), and the training configurations (Figures 8, 11, 12). The tools are released | Apps A–G; §1 bullet 4; §6 | moderate | the release actually happening; missing optimizer details (R13) |
| A11 | soundness | The ablation design isolates Stage 1. The variants share an identical Stage-2 SFT (§4.1) and identical inference settings and executors (App. G) | §4.1; App. G "inference settings and action executors; no manual interventions are allowed during evaluation" | moderate | Stage 2 only not lacking the grounding data that Stage 1 has (R4) |
| A12 | empirical strength | Budget sensitivity: with Stage 1, extra steps add solved tasks (14.13→15.78), while Stage 2 only stays flat (9.3→9.27) | §3.1.2; §4.2; Table 4 | weak (after P3) | the difference exceeding run-to-run noise (R9) |
| A13 | efficiency / soundness | ScreenFilter is cheap and accurate enough to run at scale: F1 89.58%, ≈840 h of video per GPU-day | App. B | weak | test images are synthetic composites, like the training data |
| A14 | clarity | The pipeline and the two IDM tasks are formally specified (trajectory tuple R={(I_k, r_k, a_k, π_k)}, the detection set S, h_φ). Per-domain and per-action breakdowns are given | §2; §2.2.1–2.2.2; Tables 4–5 | moderate | — (figures not seen) |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | experimental validation / soundness | The gain is confounded with extra training compute. Stage 1 adds one epoch over 26B tokens (6,500 iterations × 512, ≈60 h on 32 H100), and the baseline gets nothing in its place. No control spends the same tokens on non-video data (e.g., more epochs of the human/grounding data, or video frames with zero-shot VLM labels). So the gain cannot be attributed to the mined actions specifically | §2.3.2; Figure 11; §4.1 (the 0% point is Stage 2 only); App. G | gap | major | A compute-matched Stage-1 control on non-video or weakly labelled data; ≈60 h × 32 H100 per run |
| R2 | experimental validation | No external baselines. The only comparisons are the paper's own base and SFT-only models. No published computer-use agent (e.g., the OpenCUA or UI-TARS models the paper cites and whose data it uses) is reported on OSWorld-Verified or AgentNetBench. The reader cannot place 15.8% at 7B, and no other data source (AgentTrek-style tutorial replay, Jang et al. 2025) is compared at equal tokens | §3.1.2; Figure 5; Table 4 (only "stage2 only" and "stage1 + stage2"); §5 | gap | major | Add a table with published 7B agents under the same protocol, and an equal-token comparison against an alternative mined-data source; a few evaluation days, plus one Stage-1 run for the data comparison |
| R3 | soundness | No ablation of the pipeline's components. There is no test of the effect of the GPT-5 inner monologue, of ScreenFilter, or of IDM label quality (e.g., a weaker detector, or zero-shot VLM labelling instead of the trained IDM), and no ablation of the ASR context. The monologue quality is never evaluated, although GPT-5 receives ±60 s of ASR and may invent intent | §2.2.3; App. E; §4 (only data scale is ablated) | gap | major | Stage-1 runs without monologues, and with zero-shot-labelled actions, on a 25–50% token subset; plus a human rating of ≈200 monologues |
| R4 | soundness | Does the Stage-2-only baseline include the OSWorld-G grounding data? §2.3.2 adds grounding pairs to Stage 1 ("with a small number of GUI grounding pairs"), while Stage 2 is "a curated set of clean, human-annotated trajectories". If the grounding data appear only in Stage 1, part of the gain is grounding data, not video | §2.3.1 ("contributes roughly 1B tokens"); §2.3.2; §4.1 | question | major | State the data mixture of every arm; rerun the 0% arm with the same grounding pairs |
| R5 | soundness / claim accuracy | "Millisecond" precision is claimed but never measured. §1 bullet 2 claims millisecond-precision temporal localization, and §5 claims "millisecond-level precision and parameter extraction". But the detector sees 4 fps video with a 2-frame temporal patch (0.5 s per temporal token; App. C), and a hit is "any temporal overlap" (§3.2.1). No boundary error or tIoU is reported | §1 bullet 2; §5; App. C "we downsample videos to 4 fps", "patch size of 2 frames for modeling efficiency"; §3.2.1 | error | major | Reword; report boundary error (ms) and tIoU-thresholded P/R; no new training |
| R6 | claim accuracy | "Eliminating the need for manual annotation" and "an unsupervised approach" overstate the method. The IDM is trained on human demonstration logs (154 h; 512,000 clips; App. C–D). Stage 2 requires "clean, human-annotated trajectories" (§2.3.2). Collection uses "human-in-the-loop screening" (§2), and Stage 2 alone already gives 9.3 of the 15.8. The method reduces annotation; it does not eliminate it | Abstract; §1 bullet 1 "an unsupervised approach to training computer-use agents"; §2; §2.3.2; App. C–D | error | minor | Reword as "with little additional annotation", and state the human data each stage needs |
| R7 | soundness / evaluation | The IDM evaluation is weak where it matters. The held-out set (23 h) is "a small curated subset from the source corpus", likely in-domain with the OpenCUA training logs. The in-the-wild detector check uses only 10 YouTube videos and reports "∼70%" with no counts. The parameterizer is judged by whether an action "would plausibly produce the observed on-screen transition", on 500 samples with no inter-annotator agreement | §2.2.1; §3.2.1; §3.2.2; Table 2 | gap | major | Annotate ≥50 diverse YouTube videos with exact event logs (or re-record them); report strict coordinate/text-match metrics and agreement |
| R8 | soundness / data quality | The label noise is large and its effect is not characterized. Detection recall is 0.70 and parameter accuracy 0.658, so roughly half of the true actions are missed or wrong. Keystroke actions are nearly absent (press recall 0.08), which skews the data toward clicks (left click 67.1% in Table 8). The claim of "high-quality supervision" (Abstract) is not tested against these rates | Table 1; Table 2; Table 8; Abstract "passive internet videos can be transformed into high-quality supervision" | gap | major | A noise-injection or filtering study (e.g., train on confidence-filtered subsets); report per-type label error in the final corpus |
| R9 | claim accuracy | The test-time-scaling claim and its mechanism go beyond the evidence. The 50-step number is a single run ("For the 50-step budget, we perform a single run"). It solves 57 tasks against 53/49/51 in the three 20-step runs (Table 4, recomputed with a 361-task denominator), and the 20-step runs themselves span 4 tasks. The mechanism ("teaches the model to decompose complex tasks into subgoals, persist through intermediate failures") is never tested. Table 5 offers an untested alternative: terminate accuracy falls from 0.588 to 0.237, so the Stage-1 model may simply stop less often | §3.1.2; §4.2 "the agent demonstrates true test-time scaling"; App. G; Table 4; Table 5 | error | major | 3+ runs at 50 and 100 steps for both arms; analyse early-termination rates; drop the mechanism language or test it |
| R10 | statistics | No training-seed variance. AgentNetBench results (100 tasks) and the scaling points of Figure 6 are single numbers with no CI. Three data-scale points are called "a clear relationship between pretraining data size and computer-use agent performance" | §4.1; Figure 6; Table 5; App. G | gap | minor | Bootstrap CIs over tasks; a second Stage-2 seed; one more data-scale point |
| R11 | evaluation validity | Possible leakage, unchecked. AgentNetBench is "based on 100 representative tasks from the AgentNet dataset", while Stage 2 samples OpenCUA (AgentNet) trajectories and the IDM is trained on OpenCUA logs. There is no statement that the benchmark tasks are excluded. The YouTube corpus covers Ubuntu, Chrome, GIMP and LibreOffice tutorials, but there is no decontamination against the OSWorld instructions | §3.1.1; §2.3.1; App. C–D; §2.1 | question | major | State the exclusion; run an n-gram or embedding overlap check between OSWorld/AgentNetBench instructions and the video titles/ASR |
| R12 | ethics / legal | Large-scale scraping of YouTube screen recordings raises copyright, terms-of-service and privacy questions (emails, names and credentials visible on screen; the Figure 9 example types a password-like string "lilybloom123."). The only mention is "license/PII checks" in a limitations bullet of App. H, with no procedure, and there is no ethics or broader-impact statement | App. H; Figure 9; App. A; §2.1 | gap | major | Describe the licence/ToS basis, the PII detection and redaction, and the takedown process; add an impact statement |
| R13 | reproducibility | The reproducibility claim outruns what is released. Only the tools are promised ("open-source release of our ScreenFilter and Video2Action tools"). Not stated: release of the 1.52M-step dataset, the video ID list, the seed keywords/channels, or the trained agent. Learning rate, optimizer, warmup and data mixture ratios are absent from Figures 8/11/12. Labelling depends on proprietary GPT-5 and GPT-4.1 | §1 bullet 4; §6; Figures 8, 11, 12; §2.2.3; App. H | gap | major | Release the video IDs and mined trajectories (or a script with fixed IDs), full hyperparameters and the checkpoints |
| R14 | novelty | The delta over the closest prior work is a transfer and scale-up, not a new idea. VPT (Baker et al., 2022) introduced IDM pseudo-labelling of unlabeled video for behaviour cloning. AgentTrek (Xu et al., 2025a) already mined web tutorials for trajectories. Jang et al. (2025) generate datasets from videos for mobile agents. The paper's argument against prior mining ("typically lacks precise temporal boundaries or action parameters", §5) is asserted, with no empirical comparison | §5; §2.2; Table 9 | judgment (basis: Baker et al. 2022; Xu et al. 2025a; Jang et al. 2025, all cited) | major | Position explicitly against VPT and Jang et al.; compare data quality and downstream effect at equal tokens |
| R15 | claim accuracy | The diversity claim is unsupported. §1 says the trajectories span "hundreds of applications across Windows, macOS, and web platforms", but no application- or OS-level statistics are given (Figure 3 gives only coarse categories). The corpus comes from "50+ channels" (≈1,000 videos per channel), which suggests limited creator diversity. The evaluation covers only Ubuntu (OSWorld) and Windows/macOS (AgentNetBench) | §1; §2.1.3; Figure 3; App. H | gap | minor | Report app/OS counts and per-channel shares; analyse channel concentration |
| R16 | clarity / numbers | Several numeric inconsistencies (all checked by recomputation): Table 1 Preds column sums to 16,298, not the printed 17,298; Table 8 counts sum to 1,560,464, not 1,547,092, and mouse move/drag shares print 0.1% where the counts give 0.55%/0.41%; Table 6 buckets sum to 53,375 of 55,603 videos; Table 4 header denominators sum to 359 while §3.1.1 says 369 tasks, and the success rates match 361 (e.g., 57/361 = 15.79%); recall is 0.71 in the text vs 0.70 in Table 1 | Tables 1, 4, 6, 8; §3.1.1; §3.2.1 | error | minor | Correct the tables; state the OSWorld-Verified task count used |
| R17 | clarity | Presentation slips. App. D (Action Identification) opens "Our dense detector is trained on 512,000 screen-capture clips". "We visualize the data sample in Figure" has no figure number. §2.3.1 says statistics "will be provided in the Appendix H". Figure 5 reports base 4.5% "on OSWorld (Xie et al., 2024)" in §2.3.2 but plots it under OSWorld-Verified | App. D; §2.3.1; §2.3.2; Figure 5 | error | minor | Copy-edit pass |
| R18 | significance / transfer | One weak starting point. All results use one 7B base model whose SFT-only agent reaches 9.3% on OSWorld-Verified. Nothing shows that the video pretraining still helps a stronger SFT recipe (more human data, RL) or a larger model, which is the regime practitioners use (contribution check, question 4) | §2.3.2 "which makes it a proper starting point"; Figure 5; Table 4 | judgment (basis: single base model and weak baseline) | major | Apply Stage 1 to a stronger SFT mixture, or to a second base model or size; 1–2 extra training runs |

### Answered

- "The 70% relative headline compares a 50-step run against a 20-step baseline." Answered at Table 4: at a matched 50-step budget, 15.78/9.27 = 1.70. The 20-step comparison (14.13 vs 9.3, +52%) is also reported in §3.1.2.
- "The main OSWorld gain may be evaluation noise." Answered at App. G and Table 4: three independent 20-step runs per model, ranges 9.13–9.42 vs 13.57–14.68, non-overlapping.
- "The agents may be evaluated with different settings or with human help." Answered at App. G: "inference settings and action executors; no manual interventions are allowed during evaluation" (identical across models)

### Aspect coverage

- novelty: A9, R14
- soundness / technical rigor: A7, A11, R1, R3, R4, R5, R7, R8
- empirical strength / experimental validation: A2, A3, A4, A5, A12, R2, R9, R10, R11
- significance: A1, A5, A6, R18
- clarity / claim accuracy: A8, A14, R6, R15, R16, R17
- reproducibility: A10, R13
- ethics, licence, privacy: R12 (A8 honesty)
- efficiency / compute reporting: A13; training compute given (Figures 8, 11, 12), and its role as a confound is R1
- statistics: R10 (A2 for the evaluation runs)
- human-study design: R7 (manual validation without agreement)
- considered, no reason: theory (no theoretical claims are made); figure integrity (E9, figures not available)

### Pairs

- A2 ↔ R1, R4: is the OSWorld gain due to the mined video data?
- A3 / A12 ↔ R9: the 50-step and test-time-scaling claims.
- A4 ↔ R11: AgentNetBench validity.
- A5 ↔ R1, R10: the scaling trend versus a compute and seed confound.
- A6 ↔ R8, R13: corpus value versus label quality and availability.
- A7 ↔ R5, R7, R8: IDM accuracy.
- A9 ↔ R14: novelty of the transfer.
- A1 ↔ R6, R18: significance versus the annotation still required and transfer to stronger agents.
- A10 ↔ R13: reproducibility.

---

## 3. Reorganized ledger and probes

### By claim

**C1 (IDM accuracy):** A7 (checked after P4/P6, moderate) ↔ R5 (checked, error), R7 (checked, high swing), R8 (checked, high swing); A8 (checked); A13 (open, low swing).

**C2 (scale, diversity, no manual annotation):** A6 (checked: Table 9; values recomputed, 39,000 × 39 ≈ 1.52M) ↔ R6 (checked, error), R15 (open, low swing), R16 (checked); A1 (checked).

**C3 (downstream gains):** A2 (checked; moderate after P1) ↔ R1 (checked after P1, high swing, decides the pair), R4 (open after P2, unsettled question, high swing); A3 (checked); A4 ↔ R11 (open after P8, unsettled question); R2 (checked after P9, high swing); R18 (checked, judgment); A11 (checked, conditional on R4).

**C4 (data scaling):** A5 (checked) ↔ R10 (checked), R1.

**C5 (test-time scaling, long horizon):** A12 ↔ R9 (checked after P3, error).

**C6 (reproducible, released):** A10 (checked) ↔ R13 (checked after P11).

**General:** A9 ↔ R14 (checked after P9, judgment); R3 (checked after P1/P9: no component ablation exists); R12 (checked after P10); R17 (checked); A14 (checked).

Merged duplicates: an early "monologue quality unevaluated" reason was merged into R3, and a "scaling claim on three single-run points" reason into R10. No IDs were assigned to the merged reasons.

Swing ranking (highest first): R1, R4, R2, R9, R7/R8, R11, R14, R18, R3, R5, R12, R13; then low swing: R6, R10, R15, R16, R17.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R1 ↔ A2, A5 | Does any experiment hold Stage-1 training compute fixed while removing the video-derived actions? | Re-read §2.3.2, §3.1, §4.1, App. F–G, Figures 10–12 | confirmed: the only Stage-1 variants are 0%, 50% and 100% of the video tokens (§4.1), and 0% equals Stage 2 only. No equal-token non-video control exists | R1 open → checked (gap); A2 strong → moderate (the gain is real, its attribution unsettled); A5 depends on R1 |
| P2 | R4 ↔ A11 | Does the Stage-2-only arm receive the OSWorld-G grounding pairs? | Re-read §2.3.1 ("contributes roughly 1B tokens"), §2.3.2 ("augmented with a small number of GUI grounding pairs"; Stage 2 "a curated set of clean, human-annotated trajectories"), §4.1, App. F | cannot be settled from the paper: the grounding data are named only for Stage 1, and the Stage-2 mixture is described as human trajectories | R4 stays an open `question` (no type may grade it above minor); A11 conditional |
| P3 | R9 ↔ A12, A3 | Does the 50-step gain exceed the 20-step run-to-run variation? | Recomputed solved counts from Table 4. Per-domain sums are 34/33/34/33 for Stage 2 only and 53/49/51/57 for Stage 1+2; the SRs match a 361-task denominator (57/361 = 15.79%, 53/361 = 14.68%). Checked App. G (single 50-step run) and Table 5 (terminate 0.588 → 0.237) | partly: the 50-step run is +4 tasks over the best 20-step run and +6 over the mean, while the 20-step runs span 4 tasks, so the increase is plausible but within ≈1.5× the run spread, from one run. The mechanism is not tested, and the lower terminate accuracy is an untested alternative explanation | R9 open → checked, kind error (claim distortion on the mechanism and "true test-time scaling"); A12 moderate → weak; A3 stays moderate |
| P4 | R5 ↔ A7 | Is any temporal precision finer than the input sampling reported or achievable? | Re-read App. C ("we downsample videos to 4 fps", "patch size of 2 frames for modeling efficiency"), §3.2.1 ("any temporal overlap"), Tables 1–2 | confirmed: 4 fps with a 2-frame temporal patch gives 0.5 s per temporal token (derived). The metric needs only overlap, and no boundary error is reported anywhere | R5 open → checked, kind error |
| P5 | R6 | Does the pipeline depend on human-labelled data? | Re-read App. C (154 h of OpenCUA logs), App. D (512,000 clips), §2 ("human-in-the-loop screening"), §2.3.2 (Stage 2 on human trajectories), Figure 5 (Stage 2 alone gives 9.3 of 15.8) | confirmed | R6 checked, kind error |
| P6 | R7 ↔ A7 | Where do the held-out detector test data come from, and how large is the in-the-wild check? | Re-read §2.2.1 ("a small curated subset from the source corpus"), §3.2.1 (23 h held out; "On 10 unseen YouTube tutorials"; "∼70%"), §3.2.2 (500 predictions; "plausibly produce"; disagreements resolved by second pass; no agreement statistic) | partly: the in-the-wild evaluation is small and lenient as stated; the exact source of the 23 h set is not named, but it has logged ground truth, so it comes from instrumented recordings, not YouTube | R7 checked; A7 stays moderate |
| P7 | R16 | Do the table totals and percentages match their rows? | Recomputed all of them in python | confirmed: Table 1 Preds sum 16,298 ≠ 17,298, and precision 0.874 is consistent with 16,298; Table 8 sum 1,560,464 ≠ 1,547,092; shares of mouse move/drag are 0.55%/0.41%, not 0.1%; Table 6 sums to 53,375 ≠ 55,603; the Table 4 denominators sum to 359 vs "369 tasks", and the SRs match 361. Checks that passed: Table 2 samples sum to 500, overall 0.660 vs 0.658 printed (rounding); Table 3 sums to 771,945; Table 7 sums to 55,603; the Table 1 F1 values are consistent | R16 checked (error, minor); A2–A4 unaffected (the Table 4 SRs are internally consistent) |
| P8 | R11 ↔ A4 | Does the paper state that the AgentNetBench tasks or OSWorld instructions are excluded from the training data? | Text search for "exclud", "overlap", "decontam" and re-read §2.3.1, §3.1.1, App. G | cannot be settled from the paper: no exclusion statement. Both arms share the Stage-2 data, so a leak would inflate both, not the difference | R11 stays an open `question` (≤ minor for every type) |
| P9 | R2, R14 ↔ A9 | Does the paper compare empirically with any external agent or alternative mined-data source (AgentTrek, Jang et al. 2025, VPT-style labelling)? | Re-read §3, §4, §5, Table 9 (step counts only); no literature query (no network) | confirmed: no external agent numbers and no data-source comparison; Table 9 compares only reported step lengths | R2 checked (gap); R14 checked (judgment, basis: the paper's own citations); A9 moderate, depends on R14 |
| P10 | R12 | Does the paper describe a licence, consent, ToS or PII procedure, or an ethics statement? | Text search for "licen", "PII", "consent", "privacy", "copyright", "ethic" | confirmed: one mention only, "license/PII checks" in an App. H limitations bullet, with no procedure; no ethics or impact statement | R12 checked |

---

## 4. Reviewer roster

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Computer-use / GUI-agent specialist | experimental_validation | the task (VLM-based GUI agents) | builds and evaluates OSWorld-style desktop and web agents | online benchmark gains under standard protocol; placement against published agents; data that transfers | in-house-only baselines; weak starting points; benchmark overlap | A2, A3, A4, A6, R2, R1, R18, R11, R15 | high |
| T2 Agent-evaluation and experimental-design methodologist | technical_rigor | neighbor: evaluation science for LLM/web agents | designs controlled ablations and agent-evaluation protocols | matched controls; variance; claims sized to the evidence | compute confounds; single runs; mechanism stories without tests | A2, A11, A12, R1, R3, R4, R9, R10, R16, R6 | high |
| T3 Learning-from-observation / inverse-dynamics researcher | novelty | neighbor: imitation learning from video, robotics (VPT line) | IDM pseudo-labelling, behaviour cloning from observation, latent-action models | a clear delta over VPT-style labelling; evidence that label quality matters | "first" claims for known recipes; no comparison with simpler labellers | A9, A7, R14, R3, R8, R6, R2 | medium |
| T4 Temporal action localization / video-grounding researcher | technical_rigor | neighbor: video understanding (dense event detection) | temporal localization metrics (tIoU, boundary error), dense video captioning | strict localization metrics; in-domain vs in-the-wild evaluation | lenient overlap criteria; unmeasured precision claims; tiny manual studies | A7, A8, A13, A14, R5, R7, R8, R16, R17 | medium |
| T5 VLM pretraining and data-scaling researcher | significance | neighbor: VLM/LLM pretraining and data curation | continued pretraining, data mixtures, scaling studies | new data sources that scale; data-size trends; impact on practice | gains that vanish at a stronger baseline; tokens vs data-quality confounds | A1, A5, A6, A2, R1, R18, R8, R13, R6, R14 | high |
| T6 Responsible data-collection and data-governance researcher | ethics | neighbor: data ethics, copyright and privacy of web data [added beyond the file] | web-scraped datasets, datasheets, PII and licensing | documented provenance, consent/ToS basis, PII handling, release plans | scraping without a stated basis; credentials on screen; "checks" without procedure | A8, A10, R12, R13, R6, R15 | low–medium |

All aspects with ≥12% of the ratio (technical_rigor, experimental_validation, novelty, significance) have a type, and technical_rigor has two because it raises distinct questions (experimental design vs. localization metrics). Clarity (10%) and reproducibility (9%) have no type of their own. Their reasons (R16, R17, A14, R13, A10) sit in T2's, T4's and T6's "Weighs most", and the script renormalizes those shares away. Ethics (8%) gets T6 because the paper raises distinct questions there (R12). Every ledger item appears in some type's "Weighs most".

---

## 5. Reviews

### T1: Computer-use / GUI-agent specialist (experimental_validation; the task)

**Reading of the ledger.**
- Holds: A2. Three runs per arm, non-overlapping ranges, same executor: a real gain over the paper's own SFT model. A4: the offline gains are broad across action types. A6: 39 steps on average is genuinely longer than AgentNet's 18.6.
- Discounts: A3, a single run. A5: three single-run points with compute growing alongside. A12, given P3.
- R2: major. Without a single published agent under the same protocol, I cannot tell whether 15.8% at 7B is competitive or whether the data merely lift a weak model.
- R1: major. 26B extra tokens with no matched control. The video data may be helping, but the paper does not show it is the actions that matter.
- R18: major. A 9.3% SFT-only starting point is low for this task, and gains at that level often shrink with a stronger recipe.
- R4: minor (unsettled question).
- R11: minor (unsettled question; it affects both arms).
- R9: minor (a secondary claim for me).
- R15: minor. R10: minor.

**Opinion.** This is the kind of data source the field needs. The OSWorld-Verified gain is not an artefact of evaluation noise: Table 4's three runs per arm settle that. But as a GUI-agent reviewer, my first question is where this places the agent, and the paper never says. Every comparison is internal: base, SFT-only, SFT plus video. The SFT-only model reaches only 9.3%, and the extra stage adds 26B tokens of training without a compute-matched control. So the paper shows that adding a large video-derived corpus to a weak recipe helps. It does not show that mined actions beat other uses of the same compute, or that they help an agent near the current state of the art. I would move to accept with (i) a table of published 7B agents under this protocol, (ii) a Stage-1 control of equal tokens on non-video or weakly labelled data, and (iii) Stage 1 applied on top of a stronger SFT recipe. Without these, it is a promising pipeline with an under-controlled downstream claim.

Decisive: R2 (major), R1 (major), R18 (major), A2 (holds).

**Scores.** Bracket: above C (A2: something that was not shown before is shown working, the downstream benefit of IDM-mined desktop video, with controlled repeated evaluation, which C's ranking-only conclusions lack); below D (R2, R1: D measured its mechanism and placed itself against prior work; here neither attribution nor placement is shown). Pool position 56 (basis: A2, A4 vs R2, R1, R18). Technical Rigor 55, Clarity 60, Novelty 58, Significance 62, Experimental Validation 54, Reproducibility 60, Ethics 55. Overall 3. Confidence 4.

### T2: Agent-evaluation and experimental-design methodologist (technical_rigor; evaluation science)

**Reading of the ledger.**
- Holds: A2 (the evaluation-side variance is handled properly). A11 (identical Stage 2 and inference), conditional on R4.
- Discounts: A5 (compute and data are confounded, single runs). A12 (P3: within ≈1.5× the run spread, one run).
- R1: major. The central causal claim, that video-mined actions improve agents, has no compute-matched control.
- R9: major. "True test-time scaling" and the subgoal/persistence mechanism rest on one 50-step run, and Table 5's terminate drop (0.588 → 0.237) is a simpler, untested explanation.
- R3: major. No component ablation, so no part of the pipeline is shown to matter.
- R4: minor (unsettled question; potentially major).
- R10: minor. R11: minor (question). R16: minor (checked slips, conclusions unaffected). R6: minor.

**Opinion.** The evaluation of the final models is better than usual: three runs, identical executors, non-overlapping ranges. What is missing is the experimental design that would let the gain be attributed. Stage 1 is "more training"; to credit the video actions, the paper needs an arm with the same tokens and no mined actions, or with zero-shot labels. The grounding data's placement (R4) could also account for part of the difference, and the text does not say. The secondary claims are written well beyond their evidence. A single 50-step run is presented as "true test-time scaling" and explained by subgoal decomposition, which is never measured. A three-point scaling curve becomes "a clear relationship". I also found several table totals that do not add up (R16). None changes a conclusion, but together they suggest the numbers were not cross-checked. My score would rise with a compute-matched control, an explicit statement of the data mixture of each arm, and repeated 50-step runs with termination statistics.

Decisive: R1 (major), R9 (major), R3 (major), A2 (holds).

**Scores.** Bracket: above B (A2: the evidence is connected to the claimed setting, unlike B's toy proxy); below C (R1, R3: C's conclusions were at least well controlled, while here the headline causal attribution is not). Pool position 46 (basis: R1, R3, R9 vs A2). Technical Rigor 46, Clarity 56, Novelty 55, Significance 56, Experimental Validation 48, Reproducibility 56, Ethics 55. Overall 3. Confidence 4.

### T3: Learning-from-observation / inverse-dynamics researcher (novelty; imitation learning, robotics)

**Reading of the ledger.**
- Holds: A9 (moderate). The paper discloses the VPT lineage and the transfer required real work: typed dense spans, structured parameters, rationales. A7: the decomposition into detection and parameterization is sensible.
- Discounts: A6. Scale is effort, not novelty.
- R14: major. Relative to VPT (IDM pseudo-labelling plus behaviour cloning), AgentTrek (tutorials → trajectories) and Jang et al. 2025 (video → dataset for mobile agents), the delta is the domain and the scale, and the claimed advantage over prior mining is asserted, not shown.
- R3: major. In VPT-style work, the key question is how IDM quality maps to policy quality, and the paper never varies it.
- R8: minor. Noisy labels are expected with an IDM; what matters is R3's missing study.
- R6: minor. R2: minor (for novelty, comparing data sources matters more than comparing agents).

**Opinion.** I read this as a competent, large-scale application of inverse-dynamics labelling to desktop GUIs. Contribution check: Q1, what a reader learns: that VPT-style labelling of desktop tutorials yields usable pretraining data for a 7B GUI agent. That is useful, but close to what one would predict from VPT and from AgentTrek. Q3: the delta is a refinement and transfer (VPT's recipe; AgentTrek's and Jang et al.'s data source), not a new mechanism. Q2: the framing ("unsupervised", "eliminating manual annotation") overstates a pipeline that needs human logs at both ends (R6). The insight that would make this a strong ICLR paper is missing: how label noise, monologues or IDM accuracy trade against data volume. The paper could produce it cheaply with its own components (R3). A comparison with a zero-shot VLM labeller and with the AgentTrek-style replay data at equal tokens would show whether the trained IDM is the reason for the gain.

Decisive: R14 (major), R3 (major), A9 (holds, moderate).

**Scores.** Bracket: above B (A9, A2: the transfer is disclosed and works on the real target benchmark); at C (R14, R3: competent and useful but without an insight into why it works, failing contribution questions 1 and 3; no ledger item shows a mechanism, so the accept line is not crossed). Pool position 50 (basis: R14, R3 vs A9). Technical Rigor 52, Clarity 60, Novelty 50, Significance 56, Experimental Validation 52, Reproducibility 58, Ethics 55. Overall 3. Confidence 4.

### T4: Temporal action localization / video-grounding researcher (technical_rigor; video understanding)

**Reading of the ledger.**
- Holds: A8 (per-type failures are reported plainly).
- Discounts: A7, partly. The formulation is fine, but the metric (any overlap) is far looser than the localization literature uses. A13: synthetic test data. A14 holds (the task definitions are precise), but it does not offset R5.
- R5: major. A contribution bullet claims millisecond precision from a model that sees 0.5 s temporal tokens (P4), and precision is never measured.
- R7: major. The in-the-wild evidence is 10 videos and a "plausibly produce" judgment, with no agreement statistic.
- R8: major. Recall 0.70 and press recall 0.08 mean the corpus systematically under-represents keyboard actions, and the paper treats the output as "high-quality".
- R16: minor (the Table 1 Preds total is off by 1,000). R17: minor.

**Opinion.** From a temporal-localization viewpoint, the IDM is the paper's technical core, and it is evaluated more weakly than any detection paper in my field would be. A hit requires only "any temporal overlap" with a same-type ground-truth event. With click events lasting a fraction of a second and 10 s clips, that criterion says little about the boundaries, yet the paper claims millisecond-level precision. The held-out set comes from instrumented recordings, not YouTube, so the domain gap the pipeline must bridge (zooms, overlays, varied cursors) is tested only on 10 videos, with a single approximate number. The parameterizer's 65.8% "plausible" accuracy, combined with 70% recall, puts the label error near half of all true actions, so I want either a strict evaluation or evidence that the noise does not matter. My score would rise with tIoU-thresholded results, boundary error in milliseconds, and a properly sized in-the-wild set with agreement statistics.

Decisive: R7 (major), R5 (major), R8 (major), A8 (holds).

**Scores.** Bracket: above B (A7, A8: the IDM is evaluated on a large held-out set, with honest per-type numbers); below C (R5, R7, R8: the component that produces the data is not measured to the standard its claims require). Pool position 47 (basis: R7, R5, R8 vs A7). Technical Rigor 46, Clarity 55, Novelty 55, Significance 56, Experimental Validation 50, Reproducibility 56, Ethics 55. Overall 3. Confidence 4.

### T5: VLM pretraining and data-scaling researcher (significance; VLM/LLM pretraining)

**Reading of the ledger.**
- Holds: A1. Unlabeled video is the one GUI data source that scales by orders of magnitude. A5: monotone gains from 0% to 50% to 100% on two benchmarks is the signal a data-scaling researcher looks for first. A6: a 26B-token, long-horizon corpus. A2.
- Discounts: A3 (single run).
- R1: major. In pretraining, "more tokens helps" is the null hypothesis; I need an equal-token control to call this a data-quality result.
- R18: major. Contribution check Q4: one base model, with a weak SFT baseline.
- R8: minor. The scaling trend suggests the noise is tolerated at this scale.
- R13: minor, assuming the mined corpus is part of the "reproducible pipeline". Updated after P11: minor → major.
- R6: minor. R14: minor (for significance the transfer to GUIs matters more than its originality).

**Opinion.** I am more positive than the other types. The question this paper answers, whether passively recorded tutorials can be turned into pretraining signal for GUI agents at scale, matters for the field. The answer is a qualified yes: a monotone data curve and a large gain on OSWorld-Verified. Contribution check: Q1, a reader learns that IDM-mined video improves a GUI agent and that the benefit grows with data, which was not shown for desktop agents before. Q2: "web scale" and "hundreds of applications" are stronger than 39k videos from 50+ channels supports (R15). Q3: the delta is a transfer (moderate). Q4 is my main reservation. The baseline is weak and only one base model is used, so I cannot tell whether the curve continues once the SFT recipe is strong. The missing compute-matched control (R1) keeps "more tokens" as a live explanation. Still, the data curve and the size of the gain place it at the borderline, leaning accept. A stronger-recipe run and an equal-token control would move me firmly to accept.

Decisive: A1 (strong), A5 (holds), R1 (major), R18 (major).

**Scores.** Bracket: above C (A5, A2: the paper shows something new working and how it scales with the data, beyond C's ranking); below D (R1, R18: unlike D, the mechanism, mined actions rather than extra tokens, is not measured, and it is shown on one base model only). Pool position 64 (basis: A1, A5, A2 vs R1, R18). Technical Rigor 58, Clarity 62, Novelty 60, Significance 66, Experimental Validation 60, Reproducibility 60, Ethics 56. Overall 4. Confidence 3. (Significance sits above the 55–61 band as my best dimension; R13's later update was not among my decisive items, so the scores stand.)

### T6: Responsible data-collection and data-governance researcher (ethics; data ethics and privacy)

**Reading of the ledger.**
- Holds: A8 (honest limitation statements about the classifier). A10 (the selection criteria are documented in App. A).
- R12: major. 55k scraped YouTube videos, screen content that can expose personal data (the Figure 9 example types a password-like string), and a single unexplained mention of "license/PII checks". There is no ethics statement.
- R13: major. Without a statement on the corpus's release or on video IDs, the dataset can be neither audited nor reproduced. The labelling also relies on proprietary GPT-5 and GPT-4.1.
- R6: minor. R15: minor (channel concentration is also a representational question).

**Opinion.** The research question is legitimate, and nothing here suggests bad faith. But a paper whose contribution is a web-scale data pipeline must document its data governance, and this one does not. The paper does not say on what legal basis the videos were downloaded and used for training, whether creators' terms permit it, how personal information visible on screen (emails, documents, typed credentials) is detected and removed before training or release, or whether a takedown process exists. "license/PII checks" in a limitations bullet is not a procedure. The release plan covers tools but not the data, so outside auditing is impossible. These are fixable in revision: a datasheet, a PII-redaction description with an error rate, and an impact statement would bring this to the norm for dataset-driven ICLR papers. As it stands, the ethics dimension is below what I would expect of an accepted paper.

Decisive: R12 (major), R13 (major), A8 (holds).

**Scores.** Bracket: above B (A8, A10: careful documentation of the selection criteria); below C (R12, R13: C released its artifacts and had nothing comparable at stake). Pool position 48 (basis: R12, R13). Technical Rigor 54, Clarity 58, Novelty 56, Significance 58, Experimental Validation 54, Reproducibility 52, Ethics 42. Overall 3. Confidence 3.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P11 | T5 (R13 minor) vs T6 (R13 major) | Does the paper state that the mined dataset, the video IDs or the trained agent will be released? | Re-read §1 bullet 4, §6, App. H. Confirmed: only "ScreenFilter … and Video2Action … as open-source tools" are promised; nothing about data, video IDs or checkpoints | T5: R13 minor → major (updated after P11). Not among T5's decisive items, so T5's scores are unchanged |

Value splits that stay:
- R8: T4 major vs T3 and T5 minor. They disagree on how much label noise matters given the scaling trend.
- R9: T2 major vs T1 minor. They disagree on how central the test-time-scaling claim is.
- R14: T3 major vs T5 minor. They disagree on whether the transfer's originality matters to the contribution.

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 Computer-use / GUI-agent specialist | experimental_validation | 0.235 | 56 | 3 | 4 |
| T2 Agent-evaluation methodologist | technical_rigor | 0.141 | 46 | 3 | 4 |
| T3 Learning-from-observation / IDM researcher | novelty | 0.194 | 50 | 3 | 4 |
| T4 Temporal localization researcher | technical_rigor | 0.141 | 47 | 3 | 4 |
| T5 VLM pretraining / data-scaling researcher | significance | 0.194 | 64 | 4 | 3 |
| T6 Data-governance researcher | ethics | 0.094 | 48 | 3 | 3 |

- **Aspect-weighted rating:** 3.194 → **final rating 3 (Borderline Reject)**. On the ICLR scale this is **4 on {0, 2, 4, 6, 8, 10}** (5 on the earlier {1, 3, 5, 6, 8, 10} scale). The ICLR scale is `secondary`: recent forms use it; verify against the current form. ICLR sub-scores: Soundness 2, Presentation 2, Contribution 2.
- Weighted pool position 53.0; plain mean 3.17; spread 1 (max 4 − min 3).
- Uncovered aspects and warnings: none from the script. Clarity (10%) and reproducibility (9%) have no type of their own and are renormalized away, as the procedure allows.
- No override is applied, and likelihood and confidence do not weight the rating.

<details><summary>Aggregation output</summary>

```
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Computer-use / GUI-agent specialist) | experimental_validation | 19% | 0.235 |
| T2 (Agent-evaluation and experimental-design methodologist) | technical_rigor | 23% | 0.141 |
| T3 (Learning-from-observation / inverse-dynamics researcher) | novelty | 16% | 0.194 |
| T4 (Temporal action localization / video-grounding researcher) | technical_rigor | 23% | 0.141 |
| T5 (VLM pretraining and data-scaling researcher) | significance | 16% | 0.194 |
| T6 (Responsible data-collection and data-governance researcher) | ethics | 8% | 0.094 |

Final rating (aspect-weighted mean): 3.19 → 3 (Borderline Reject) · plain mean 3.17 · weighted pool position 53.0

Per-type composites: T1 57.3, T2 52.2, T3 54.0, T4 52.5, T5 60.3, T6 53.9 (each implied Overall = stated Overall)
Composite cross-check: 55.0 → 3
ICLR (2026): venue-weighted composite 54.9, band 3 → 3; recommendation 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10});
Soundness 2, Presentation 2, Contribution 2; scale status secondary
```

The full output is in `aggregate.json` and `aggregate_output.md`.

</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| A1 | 1 of 6 | T5 held |
| A2 | 4 of 6 | T1 held, T2 held, T3 held (as part of the bracket), T5 held |
| A3 | 2 of 6 | T1 discounted, T5 discounted |
| A4 | 1 of 6 | T1 held |
| A5 | 2 of 6 | T5 held, T2 discounted |
| A6 | 3 of 6 | T1 held, T5 held, T3 discounted |
| A7 | 2 of 6 | T3 held, T4 discounted (partly) |
| A8 | 2 of 6 | T4 held, T6 held |
| A9 | 1 of 6 | T3 held (moderate) |
| A10 | 1 of 6 | T6 held |
| A11 | 1 of 6 | T2 held (conditional on R4) |
| A12 | 2 of 6 | T1 discounted, T2 discounted |
| A13 | 1 of 6 | T4 discounted |
| A14 | 1 of 6 | T4 held |
| R1 | 3 of 6 | T1 major, T2 major, T5 major |
| R2 | 2 of 6 | T1 major, T3 minor |
| R3 | 2 of 6 | T2 major, T3 major |
| R4 | 2 of 6 | T1 minor, T2 minor (unsettled question) |
| R5 | 1 of 6 | T4 major |
| R6 | 4 of 6 | T2 minor, T3 minor, T5 minor, T6 minor |
| R7 | 1 of 6 | T4 major |
| R8 | 3 of 6 | T4 major, T3 minor, T5 minor (value split) |
| R9 | 2 of 6 | T2 major, T1 minor (value split) |
| R10 | 2 of 6 | T1 minor, T2 minor |
| R11 | 2 of 6 | T1 minor, T2 minor (unsettled question) |
| R12 | 1 of 6 | T6 major |
| R13 | 2 of 6 | T6 major, T5 major (updated after P11) |
| R14 | 2 of 6 | T3 major, T5 minor (value split) |
| R15 | 2 of 6 | T1 minor, T6 minor |
| R16 | 2 of 6 | T2 minor, T4 minor |
| R17 | 1 of 6 | T4 minor |
| R18 | 2 of 6 | T1 major, T5 major |

### Key strengths

- A2: a controlled, repeated-evaluation OSWorld-Verified gain (9.3 → 14.13 at 20 steps, three runs per arm, non-overlapping ranges). Held by 4 of 6 types.
- A6: a large, long-horizon corpus (1.52M steps, 39.25 steps per trajectory). Held by 2 of 6.
- A1 / A5: a scalable data source with a monotone data-scaling curve. Held by T5; A5 discounted by T2.
- A8: honest per-type reporting of the IDM's weak classes. Held by 2 of 6.

### Top concerns (at most five)

1. **R1**: The gain is not separated from 26B tokens of extra training compute (§2.3.2, Figure 11, §4.1). Fix: an equal-token Stage-1 control on non-video or zero-shot-labelled data; ≈60 h on 32 H100.
2. **R3**: No ablation of the IDM quality, monologues or ScreenFilter, and no comparison with simpler labelling (§2.2–2.3, §4). Fix: Stage-1 runs without monologues and with zero-shot labels on a token subset, plus a human rating of the monologues; 2–3 reduced runs.
3. **R18**: One base model with a weak SFT-only baseline (9.3%) (§2.3.2, Table 4). Fix: apply Stage 1 to a stronger SFT recipe or a second base model; 1–2 training runs.
4. **R13**: Only the tools are promised. Not stated: the dataset, video IDs, checkpoints, and full optimizer settings (§1, §6, Figures 8/11/12). Fix: release the video IDs, the trajectories and the configurations; low compute.
5. **R2**: No external agents and no alternative data source compared (§3.1.2, Figure 5, Table 4). Fix: a table of published 7B agents under the same protocol, and an equal-token comparison with tutorial-replay data; evaluation days plus one run.

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R1 | Compute-matched Stage-1 control (same tokens, no mined actions or zero-shot labels); state every arm's data mixture (also resolves R4) | ≈60 h × 32 H100 per run |
| 2 | R3 | Component ablations: monologues, IDM quality / zero-shot labeller, ScreenFilter, ASR context; rate monologue quality | 2–3 reduced Stage-1 runs; ≈1 annotator-day |
| 2 | R18 | Stage 1 on top of a stronger SFT recipe or a second base model or size | 1–2 training runs |
| 2 | R2 | Published 7B agents under the same protocol; equal-token comparison with AgentTrek-style or Jang et al. 2025 data | evaluation days; one Stage-1 run |
| 2 | R13 | Release the video IDs, trajectories and checkpoints; list LR, optimizer, warmup and mixture ratios | low |
| 2 | R12 | Licence/ToS basis, PII detection and redaction with an error rate, takedown process, impact statement, datasheet | low–moderate |
| 2 | R9 | ≥3 runs at 50 and 100 steps for both arms; termination analysis; drop or test the mechanism language | ≈2–3 evaluation days |
| 2 | R7 | ≥50 annotated in-the-wild videos with exact event logs; strict coordinate/text metrics; inter-annotator agreement | ≈1–2 annotator-weeks |
| 2 | R8 | Noise characterization: per-type label error in the final corpus; confidence-filtered training subsets | 1–2 reduced runs |
| 2 | R5 | Remove the "millisecond" claim or measure boundary error; tIoU-thresholded P/R | no training |
| 2 | R14 | Explicit positioning against VPT, AgentTrek and Jang et al. 2025, with the data comparison of R2 | writing + R2 |
| 3 | R4 | (Covered by R1) state whether Stage 2 only sees the OSWorld-G pairs | writing |
| 3 | R6 | Reword "unsupervised" / "eliminating manual annotation"; quantify the human data used | writing |
| 3 | R10 | Bootstrap CIs on AgentNetBench and OSWorld; a second training seed; one more scaling point | evaluation + one run |
| 3 | R11 | Exclusion statement and overlap check against the AgentNetBench and OSWorld instructions | low |
| 3 | R15 | App/OS statistics and channel-concentration analysis | low |
| 3 | R16, R17 | Correct the table totals and shares and the OSWorld task count; copy-edit App. D and the missing figure reference | writing |

Priority 1 holds only R1, the one reason graded major by at least half of all types (3 of 6). No reason was graded fatal.

Missing related work the authors could position against, beyond the works they already cite:
- Learning from observation: "Behavioral Cloning from Observation" (Torabi, Warnell, Stone, IJCAI 2018); "Learning to Act without Actions" (Schmidt, Jiang, ICLR 2024).
- Video-derived GUI data and benchmarks: "VideoGUI: A Benchmark for GUI Automation from Instructional Videos" (Lin et al., 2024) [verify]; "GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents" (Chen et al., 2024) [verify]; "TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials" (2025) [verify].

---

## 8. Integrity signals and limitations

- **Integrity signals:** none found. `integrity_scan.py` reported no reviewer-directed text or hidden characters. The redacted copy replaced one venue/acceptance mark in the ReAct reference, which is not a manipulation signal. No out-of-place instructions were seen while reading. The numeric inconsistencies in R16 look like copy-editing errors, not signs of fabrication: the Table 4 success rates are internally consistent with a 361-task denominator. They never change a score.
- **Limitations:**
  - Figures were not available. Figure 5 and Figure 6 values were taken from their extracted labels and cross-checked against Table 4/5 and §4.1. Figure 10 and Table 10 are garbled, and the loss curves (Figures 8, 11, 12) were not seen. Figure integrity (E9) was not checked.
  - The literature check did not run (no network). The novelty judgment R14 rests on works the paper itself cites, and recalled references not certain are marked [verify].
  - No supplement or code was provided.
  - All six types share one context and one reading; their agreement is not independent confirmation.
