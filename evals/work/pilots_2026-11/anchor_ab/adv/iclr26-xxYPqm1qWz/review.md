# Peer Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | empirical (a data-generation pipeline judged by downstream agent training) |
| Field, sub-area | multimodal ML / vision–language agents; computer-use (GUI) agents, learning from unlabeled video |
| Task | Vision–language models, multimodal LLMs (row of `task_neighbors.md`, specialised to GUI/computer-use agents); secondary: Video understanding, tracking (temporal event detection) |
| Neighboring fields | GUI/computer-use agents and agent benchmarks (from the VLM row); temporal action localization and dense video grounding (from the video row); learning from observation / inverse dynamics in robotics and games (*generated beyond the file*: VPT, latent-action pretraining); foundation-model continued pretraining and data scaling (*generated*); web-data curation, copyright and PII in scraped video (*generated*); agent evaluation science (contamination, variance, budget matching) |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | technical rigor 23%, experimental validation 19%, novelty 16%, significance 16%, clarity 10%, reproducibility 9%, ethics 8% (`aggregate_scores.py ratio --paper-type empirical --venue iclr`) |
| Literature check | off (no network); novelty reasons resting on memory are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Figures are not available (text extraction only). Figures 1–12 were judged from captions and the extracted text fragments; the bar values of Figures 5 and 6 are read from the extracted labels and cross-checked against Table 4 and the text.

---

## 1. Paper memory

**Claims.**
- C1: A pipeline that "automatically mines training data from publicly available screen-recorded videos at web scale, eliminating the need for manual annotation" (Abstract; §1 bullet 1: "an unsupervised approach").
- C2: VIDEO2ACTION, an inverse dynamics module (dense action-event detection + action parameterization), "with millisecond-precision temporal localization", enabling "accurate reconstruction of GUI interactions ... without ground-truth labels" (§1 bullet 2; §2.2; §3.2; Tables 1–2).
- C3: Stage-1 continued pretraining on the mined data improves OSWorld-Verified task success from 9.3% (SFT-only) to 15.8% ("a 70% relative improvement") and AgentNetBench step accuracy from 64.1% to 69.3% (Abstract; §3.1.2; Figure 5; Tables 4–5).
- C4: Performance "scales consistently" with Stage-1 video data (0/50/100%) (§4.1; Figure 6).
- C5: Video pretraining yields long-horizon planning / "true test-time scaling" (14.13% at 20 steps → 15.78% at 50 steps, SFT-only flat at 9.3%) (§3.1.2; §4.2; Table 9).
- C6: A reproducible pipeline, with ScreenFilter and Video2Action released as open-source tools (§1 bullet 4; §6).

**Setup facts.**
- Corpus: 55,603 videos (~10,000 h) from 50+ channels (§2.1.3; App. H); ScreenFilter keeps 7,377 h (§2.1.2); 39,000 videos processed into ~1.52M steps, ~26B tokens (§2.3.1). How the 39,000 were selected from the 55,603: not stated.
- ScreenFilter: YOLOv8x cursor detector trained on 15,000 synthetic composites; F1 89.58% on its held-out set (App. B).
- Event detector: Qwen2.5-VL-7B-Instruct, full FT on 154 h of OpenCUA recordings with logged events, 4 fps, 10 s clips, temporal patch 2 frames (§2.2.1; App. C; Table 3).
- Action parameterizer: Qwen2.5-VL-7B, full FT on 512,000 OpenCUA clips (App. D; that paragraph is headed "Action Identification" but says "Our dense detector is trained on 512,000...").
- Inner monologue: GPT-5 Medium with action, parameters, keyframes and ±60 s ASR (§2.2.3; App. E).
- Agent: Qwen2.5-VL-7B; Stage 1 = 26B tokens of mined trajectories "augmented with a small number of GUI grounding pairs" (OSWorld-G, ~1B tokens), 6,500 iterations, batch 512, 32×H100, ~60 h; Stage 2 = 8B tokens of human trajectories from OpenCUA and AGUVIS, 3,000 iterations, 64×H100, ~16 h (§2.3.1–2.3.2; Figs. 11–12).
- Evaluation: OSWorld-Verified (Ubuntu; stated "369" tasks; Table 4 headers sum to 359; row percentages imply 361), 20-step budget with three runs, 50-step budget with one run, five-screenshot history (App. G); AgentNetBench, 100 offline tasks from the AgentNet dataset (§3.1.1). Seeds: not stated. Learning rate, optimizer, warmup: not stated. Baseline: Stage-2-only model with the same Stage 2 (§3.1.2).
- Data licence, consent, PII handling: one clause, "license/PII checks" (App. H, Limitations bullet); no ethics statement.

**Headline numbers.** OSWorld-Verified 9.3 → 15.8 (Abstract; Figure 5; Table 4 turn4: 9.27 vs 15.78); 20-step: 9.3 → 14.13 (+4.83 pp, +52%) (§3.1.2; Table 4 turns 1–3); AgentNetBench 38.5 → 64.1 → 69.3 (Figure 5; Table 5); scaling 9.3/13.3/15.7 and 64.1/68.1/69.3 (Figure 6); detector P 0.88 / R 0.70 / F1 0.78 (Table 1); parameterizer accuracy 0.658 on 500 samples (Table 2); 39.25 average steps (Table 9).

**Appendix summary.** A: video quality standards. B: ScreenFilter. C–D: detector and parameterizer data. E: monologue prompt. F: training configs. G: evaluation protocol plus Tables 4–5. H: corpus statistics (Tables 6–10).

**Could not be read.** All figures as images. That includes the loss curves in Figs. 8, 11 and 12, the training-sample visualisations in Figs. 7, 9 and 10, and the Table 10 step histogram, which survives only as axis fragments. The "Proportion" column of Table 9 is merged with Table 10 in extraction. No supplement or code was provided.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | Targets the real bottleneck of computer-use agents (annotated trajectories) with an abundant, passive source; turns 39k public tutorials into 1.52M steps / 26B tokens, far beyond human-annotated corpora | §1; §2.3.1 "approximately 1.52 million ReAct steps overall, and about 26 billion training tokens" | strong | data quality adequate (R10) |
| A2 | empirical strength | A controlled comparison with an identical Stage 2: adding Stage 1 lifts OSWorld-Verified 9.3 → 14.13 (20 steps) and 9.27 → 15.78 (50 steps), and AgentNetBench 64.1 → 69.3 | §3.1.2; Figure 5; Tables 4–5 | moderate | the gain is due to the video data, not extra compute or grounding data (R1, R2) |
| A3 | statistical robustness | At 20 steps, three runs per model; the spreads (9.13–9.42 vs 13.57–14.68) do not overlap, and the 4.8 pp gap is >4× either spread | App. G "we conduct three independent runs per model"; Table 4 | strong | — |
| A4 | empirical strength | Monotone data scaling: 0/50/100% of video tokens gives 9.3/13.3/15.7 (OSWorld) and 64.1/68.1/69.3 (AgentNetBench) | §4.1; Figure 6 | moderate | R21 (three points, single runs) |
| A5 | soundness of the IDM | The IDM is evaluated quantitatively on 20,282 held-out events, per type, plus a 500-sample in-the-wild manual check, and weak action types are reported honestly (press recall 0.08) | Tables 1–2; §3.2 | moderate | R10 (in-domain test set, thin wild evaluation) |
| A6 | novelty | Transfers VPT-style inverse-dynamics auto-labeling from games and robotics to desktop GUI video. The transfer is disclosed and argued, and the IDM is decomposed into dense temporal event detection plus per-segment parameterization, both trained on logged demonstrations | §2.2 "Following insights from robotics..."; §5 (VPT, Baker et al., 2022) | moderate | R17 |
| A7 | empirical breadth | The gains are spread over apps: chrome 8 → 12–15, writer 2 → 5–7, thunderbird 2–3 → 6, os 2 → 3–4 solved | Table 4 | moderate | R9 (no contamination check) |
| A8 | resource | The mined trajectories are long: 39.25 steps on average, 42.1% above 20 steps and 14.5% at 50 or more | §4.2; Table 9 | weak | R20 (per-video vs per-task) |
| A9 | reproducibility | Training configs (framework, GPUs, TP/PP, batch, iterations, wall-clock) for all three models; the full monologue prompt; ScreenFilter thresholds; the frame-rate policy | Figs. 8, 11, 12; App. B, D, E | moderate | R15 |
| A10 | resource | Promises to release ScreenFilter and Video2Action as open-source tools | §1 bullet 4; §6 | weak | release actually happens |
| A11 | clarity | The three-stage pipeline (collection → IDM → training) is clearly structured, with formal task definitions for detection ($f_\theta(v)\to S$) and parameterization ($h_\phi(v_k)$) | §2; §2.2.1–2.2.2; Figs. 1, 2, 4 | moderate | — |
| A12 | efficiency / practicality | A cheap curation front end: channel-coherence expansion needs "minimal human oversight", and ScreenFilter processes ~840 h of video per GPU-day | §2.1.1; App. B | moderate | — |
| A13 | honesty | States the limitations of metadata-only classification, and the lower accuracy on keystroke, drag and press actions | App. H "Limitations"; §3.2.1; §3.2.2 | weak | — |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | rigor / validation | Compute and token confound. The treated model gets 26B extra tokens of Stage-1 training (~60 h on 32 H100s) that the baseline never gets. With no equal-compute control (Stage 1 on non-video data, on video frames with ASR text but no IDM actions, or longer Stage 2), the gain cannot be attributed to the mined action labels | §2.3.2 "We train for one epoch over 26B tokens"; Fig. 11; §3.1.2 compares only with "SFT-only" | gap | major | Add 1–2 matched-token controls (≈60 h on 32 H100s each) |
| R2 | rigor / validation | Data-mixture confound. OSWorld-G grounding pairs (~1B tokens) are added only in Stage 1, so the Stage-2-only baseline lacks them. Grounding data built for the same Ubuntu application ecosystem as OSWorld could explain part of the OSWorld gain | §2.3.1 "GUI Grounding Data ... OSWorld-G"; §2.3.2 Stage 1 "augmented with a small number of GUI grounding pairs"; Stage 2 "curated set of clean, human-annotated trajectories" | gap | major | Run Stage-2-only + grounding pairs, or Stage 1 without them (~16–60 GPU-node-hours) |
| R3 | validation | No external comparison: no other 7B computer-use agents and no other trajectory-synthesis or mining methods (AgentTrek, OS-Genesis, video-to-dataset; all cited in §5) are compared, so 15.8% cannot be placed against the state of the art | Figure 5 and Table 4 contain only base / stage2-only / stage1+2 | gap | major | Add published numbers of comparable 7B agents under the same protocol; one same-budget comparison with an alternative data source |
| R4 | validation | No ablation of any pipeline component: GPT-5 inner monologue, ScreenFilter, channel expansion, IDM quality, or label-noise level. Roughly 0.88 × 0.658 ≈ 58% of steps are correct end to end (derived), yet how noise affects training is never measured | §2.2.3; Tables 1–2; §4 has only the data-scale ablation | gap | major | Ablate monologue on/off and IDM-confidence filtering at 50% data (~2–3 Stage-1 runs) |
| R5 | claim accuracy | "millisecond-precision temporal localization" is not supported. Detector inputs are 4 fps with a 2-frame temporal patch (0.5 s granularity, derived), and a hit needs only "any temporal overlap"; no boundary error or tIoU metric is reported | §1 bullet 2; App. C "downsample videos to 4 fps ... temporal patch size of 2 frames"; §3.2.1 | error (derived: 2 frames / 4 fps = 0.5 s) | major | Remove the claim, or report boundary error and tIoU-thresholded metrics, as in standard temporal action localization |
| R6 | claim accuracy | "unsupervised" / "eliminating the need for manual annotation" / "without ground-truth labels" is overstated. The IDM is trained on human demonstration logs (154 h; 512k clips), Stage 2 uses 8B tokens of human-annotated trajectories, and collection uses "human-in-the-loop screening" | Abstract; §1 bullets 1–2; App. C; App. D; §2.3.1; §2 bullet 1 | error (cross-referenced) | major | Reword to "without annotating the mined videos"; quantify the human data used (text only) |
| R7 | validation / claims | The test-time-scaling and long-horizon claim (C5) rests on one 50-step run per model. 15.78 vs the 20-step mean of 14.13 is +1.65 pp, while the 20-step runs alone span 1.11 pp (13.57–14.68). The stated mechanism ("teaches the model to decompose complex tasks into subgoals, persist through intermediate failures") is never tested | §4.2; App. G "For the 50-step budget, we perform a single run"; Table 4 | gap | major | Three 50-step runs (and 100 steps) per model; per-task analysis of where extra steps help; tone down the mechanism |
| R8 | validation | AgentNetBench is built from AgentNet tasks, and Stage 2 (human data from OpenCUA) and both IDM components are trained on OpenCUA data. The paper does not say whether benchmark tasks are held out of training; single run, no variance | §3.1.1; §2.3.1; App. C–D | question | major | State the train/benchmark separation; report variance |
| R9 | validation | Possible contamination: the mined video domains (OS ~36%, seeds "How to use Ubuntu", office apps) overlap the OSWorld application set (chrome, gimp, vscode, writer, impress, thunderbird, vlc), and no overlap or deduplication check against benchmark task instructions is reported | Figure 3; Figure 2 seeds; Table 4 headers; no "contamination" or "dedup" in the text | question | major | Retrieve videos whose titles/ASR match OSWorld task instructions; report results with them removed |
| R10 | soundness of the IDM | IDM evaluation is thin for an unlabeled-web claim. The held-out set is the "source corpus" (in-domain recordings), the wild detector check covers 10 videos with "∼70%" by human review, and parameterization uses a lenient "plausibly produce" criterion on 500 samples. Annotator count and agreement are not given | §2.2.1 "small curated subset from the source corpus"; §3.2.1; §3.2.2; Table 2 | gap | major | Label 2–3 h of YouTube video with event timestamps; report agreement (≈1–2 annotator-weeks) |
| R11 | correctness | Table 1 Total row: Preds printed 17,298, but the rows sum to 16,298. With 16,298 the implied precision is 0.874 (matches 0.88); with 17,298 it would be 0.824. The text says recall "0.71", the table 0.70. "micro/macro aggregates" are promised but only one Total row is given | Table 1; §3.2.1 "solid recall (0.71)" | error (recomputed) | minor | Correct the total; report both aggregates |
| R12 | correctness | Table 8 counts sum to 1,560,464, not the printed 1,547,092. mouse move and drag shares are printed 0.1% but compute to 0.55% and 0.41% | Table 8 | error (recomputed) | minor | Correct the table |
| R13 | correctness | Small numeric inconsistencies. Table 6 buckets sum to 53,375 vs 55,603 downloaded. Table 2 Drag 0.366 is not attainable with 22 samples (8/22 = 0.364), and per-type counts give 330/500 = 0.660 vs 0.658. Table 4 stage2-only turn4 counts sum to 33 (9.14% at the 361-task denominator the other rows imply) vs 9.27% printed; the stated "369 human-crafted ... tasks" vs 359 in the headers | Tables 2, 4, 6; §3.1.1 | error (recomputed) | minor | Reconcile; state the OSWorld-Verified task count and any partial-credit scoring |
| R14 | ethics | 55k scraped YouTube videos with no discussion of copyright or ToS, creator consent, or PII in screen recordings (emails, account names, typed passwords). Only "license/PII checks" in one clause; no ethics or limitations section. Figure 9's sample types "lilybloom123.", which reads like a credential | App. H Limitations bullet; Figure 9; App. A | gap | major | Add an ethics statement: licence basis, PII redaction procedure and its recall, release terms |
| R15 | reproducibility | Release covers tools only: no statement that the mined trajectories, the video ID list, or the trained agent will be released. Learning rate, optimizer and warmup are absent from Figs. 8, 11 and 12. Monologue and classification depend on closed GPT-5 / GPT-4.1 | §1 bullet 4; §6; Figs. 8, 11, 12 | gap | major | Release video IDs plus trajectories (or a subset); give full optimizer settings |
| R16 | clarity | Cross-reference and copy errors: §3.1.2 "see Section 4.1" (content is in §4.2); §4.2 "As illustrated in Figure 10" (Fig. 10 shows training samples; the histogram is Table 10); App. D "Our dense detector is trained on 512,000" under Action Identification; "We visualize the data sample in Figure" (no number); §2.3.1 "will be provided in the Appendix H"; Fig. 1 "Agent Traing" | as quoted | error (cross-referenced) | minor | Copy-edit |
| R17 | novelty | The conceptual delta over VPT (inverse-dynamics auto-labeling of web video, Baker et al., 2022) is a domain transfer. Mining tutorials for GUI trajectories exists in AgentTrek (Xu et al., 2025a) and video-to-dataset for mobile agents (Jang et al., 2025), plus concurrent tutorial-mining work [verify]. §5 distinguishes them in one sentence ("typically lacks precise temporal boundaries or action parameters") without empirical comparison | §5 "Generating agent trajectories"; §5 "Learning from unlabeled video" | judgment (basis: VPT; AgentTrek; Jang et al. 2025) | major | Sharpen the delta; compare against one tutorial-derived alternative at matched tokens |
| R19 | significance | One base model (Qwen2.5-VL-7B) at one scale; absolute OSWorld-Verified success stays low (15.8%). Whether video pretraining still helps stronger or larger agents, or after heavier SFT, is untested | §2.3.2 "Foundation Qwen2.5-VL-7B"; Figure 5 | gap | major | Repeat on one stronger or larger base (cost ≈ the Stage-1 run) |
| R20 | validation | Table 9 compares average steps per video (39.25, estimated from a 5,416-trajectory sample) with average steps per task in other datasets. A tutorial may contain several tasks, so "substantially longer trajectories" is not like-for-like | Table 9 † note; §4.2 | judgment | minor | Segment videos into tasks, or caveat the comparison |
| R21 | validation | "a clear relationship between pretraining data size and ... performance" rests on three points, single runs (the 50% point is not in Table 4) | §4.1; Figure 6 | gap | minor | Add a 25% point and seeds, or soften |
| R22 | validation | AgentNetBench `terminate` accuracy drops from 0.588 (stage2-only) to 0.237 with Stage 1, which is unexplained: video pretraining may harm stop decisions, since videos do not end at task completion. stage2-only `press` is missing ("—") | Table 5 | gap | minor | Discuss; add terminate-token handling |
| R23 | clarity / data | The selection chain is unclear: 55,603 downloaded → 7,377 h after ScreenFilter → "39,000 videos" processed. Whether these are the 38,700 "A tutorial" label (Table 7) is not stated, and App. H says that label is "not ... a hard accept/reject gate" | §2.1.2; §2.3.1; Table 7; App. H | gap | minor | State the funnel with counts |
| R24 | significance (added in T3 review) | No analysis of *what* the video data teaches: which action types or app domains benefit, and whether gains track domain coverage (Figure 3 vs Table 4). The paper reports that it helps, not why or when | Tables 4–5 are reported without such analysis; §4 | judgment | major | Correlate per-app gains with per-app video hours; per-action error analysis (text plus existing runs) |

### Answered

- R18 (question: the abstract's "70% relative improvement" compares a 50-step run with a 20-step baseline). Answered by P5: at matched 50-step budgets, 15.78 / 9.27 = 1.70 (Table 4 turn4). The single-run concern remains under R7.
- "OSWorld results are single runs": answered for the 20-step budget at App. G ("three independent runs per model") and Table 4.
- "Compute and hardware not reported": answered at Figs. 8, 11, 12 (GPUs, iterations, wall-clock).
- "Base-model reference missing": answered at Figure 5 and Table 5 (4.5% OSWorld; 0.385 AgentNetBench).
- "Inner-monologue prompt unspecified": answered at App. E.
- "Video quality criteria unspecified": answered at App. A.

### Aspect coverage

- technical rigor: A2, A5, R1, R2, R5, R6
- experimental validation: A2, A3, A4, A7, R3, R4, R7, R8, R9, R10, R20, R21, R22
- novelty: A6, R17
- significance: A1, A8, R19, R24
- clarity: A11, R16, R23
- reproducibility: A9, A10, R15
- ethics: A13, R14
- correctness of numbers (E1): R11, R12, R13
- efficiency: A12
- statistical reporting: A3, R7, R8, R21

### Pairs

- A2 ↔ R1, R2: is the OSWorld/AgentNetBench gain caused by the mined video labels?
- A3 ↔ R7: variance is controlled at 20 steps but not at 50 steps.
- A4 ↔ R21: data-scaling strength.
- A5 ↔ R10, R5, R11: IDM quality.
- A6 ↔ R17: novelty of the transfer.
- A8 ↔ R20: long-horizon data.
- A1 ↔ R6, R14: scalable "no annotation" pipeline vs. its hidden human data and legal/ethical cost.
- A9/A10 ↔ R15: reproducibility.

---

## 3. Reorganized ledger and probes

### By claim

**C1 (pipeline without manual annotation):** A1 (checked), A12 (checked), R6 (checked by P4, high swing), R23 (checked), R12 (checked by P6)
**C2 (accurate IDM, millisecond precision):** A5 (checked; weakened by P9), R5 (checked by P3), R10 (checked by P9, high swing), R11 (checked by P6), R13 (checked by P6)
**C3 (downstream gains):** A2 ↔ R1, R2 (checked by P1, P2; decides the pair, highest swing), A3 (checked by recomputation), A7 (checked), R3 (checked: Fig. 5 / Tables 4–5 re-read), R4 (checked), R8 (open: P7 cannot settle), R9 (open: P8 cannot settle), R19 (checked), R22 (checked), R24 (checked; added in T3 review)
**C4 (data scaling):** A4 ↔ R21 (checked)
**C5 (long horizon / test-time scaling):** A8 ↔ R20 (checked), A3 ↔ R7 (checked by P5; R18 merged into P5 and moved to Answered)
**C6 (release and reproducibility):** A9 (checked), A10 (open: a promise), R15 (checked by P12, after reviews)
**General:** A6 ↔ R17 (checked by P10 against the paper's own §5; the literature itself unchecked, no network), A11, A13, R14 (checked by P11), R16 (checked)

Swing order: R1/R2 (decide A2) > R3 > R17 > R4 > R6 > R7 > R10 > R8/R9 > R5 > R14 > R19 > rest.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R2 (↔ A2) | Are the OSWorld-G grounding pairs also in the Stage-2-only baseline? | Re-read §2.3.1, §2.3.2, §4.1, Fig. 6 caption | partly. The text places them only in Stage 1 ("augmented with a small number of GUI grounding pairs"); Stage 2 is "a curated set of clean, human-annotated trajectories". Whether the "0%" variant of §4.1 keeps them is not stated | R2 open → checked (the confound exists as written); A2 depends on it |
| P2 | R1 (↔ A2) | Does any experiment match Stage-1 compute without the mined labels? | Search §3–4 and App. F–G for any alternative Stage 1 | confirmed: only 0/50/100% of video tokens (§4.1); no non-video or label-free Stage-1 control | R1 checked; A2 strong → moderate |
| P3 | R5 | What temporal resolution can the detector have? | Derivation from App. C (4 fps, temporal patch 2 frames) and the §3.2.1 metric | confirmed: 2 / 4 fps = 0.5 s per temporal token; the metric counts any overlap; no boundary error reported | R5 question → error |
| P4 | R6 | How much human-labeled data does the pipeline use? | Trace §2, §2.2.1–2.2.2, App. C–D, §2.3.1 | confirmed: 154 h logged demonstrations (detector), 512,000 clips (parameterizer), 8B tokens human trajectories (Stage 2), human-in-the-loop screening (§2) | R6 judgment → error (claim distortion, cross-referenced) |
| P5 | R7, R18 | Is the 70% headline budget-matched, and is the 50-step gain beyond run-to-run spread? | Recompute from Table 4 | R18 refuted: 15.78 / 9.27 = 1.70 at 50 steps. R7 confirmed: 50-step results are single runs (App. G); 20-step means 9.32 and 14.13; the 20-step spread for stage1+2 is 1.11 pp vs a +1.65 pp 50-step gain | R18 → Answered; R7 checked |
| P6 | R11, R12, R13 | Do the table totals add up? | Recompute sums and ratios (python) | confirmed: Table 1 Preds sum 16,298 (printed 17,298); Table 8 sum 1,560,464 (printed 1,547,092); Table 6 sum 53,375; Table 2 counts give 0.660; Table 4 row counts sum to 34/33/34/33 and 53/49/51/57, matching the printed % at a denominator of 361 except stage2 turn4 (9.14 vs 9.27). Per-type precision and recall in Table 1 are internally consistent | all three → error (minor) |
| P7 | R8 | Are AgentNetBench tasks excluded from the Stage-2 and IDM training data? | Re-read §3.1.1, §2.3.1, App. C–D, G | cannot be settled from the paper: no statement of separation | stays question (graded ≤ minor) |
| P8 | R9 | Is any overlap between mined videos and OSWorld tasks checked? | Text search for contamination/overlap/dedup/benchmark | cannot be settled: no such analysis; "overlap" occurs only in the detector metric | stays question |
| P9 | R10 (↔ A5) | Where does the held-out detector set come from, and how many annotators judged the wild sets? | Re-read §2.2.1, §3.2.1–3.2.2, App. C | confirmed: the held-out set is a "small curated subset from the source corpus" (i.e., in-domain); 10 wild videos; annotator count and agreement not given | R10 checked; A5 moderate (unchanged), its "Depends on" partly fails |
| P10 | R17 (↔ A6) | How does the paper itself distinguish its work from VPT, AgentTrek and Jang et al. (2025)? | Re-read §5, §2.2 | confirmed: one sentence on web mining ("typically lacks precise temporal boundaries or action parameters") and an explicit VPT lineage; no empirical comparison. No external literature query (no network) | R17 checked (paper-internal basis); concurrent-work claims marked [verify] |
| P11 | R14 | Does the paper discuss licence, consent or PII? | Text search for licence/PII/copyright/consent/ethic/privacy | confirmed: only "license/PII checks" (App. H Limitations); no procedure | R14 checked |

---

## 4. Reviewer roster

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Computer-use / GUI agent specialist | experimental_validation | the task (GUI agents) | builds and evaluates desktop/web agents on OSWorld-style benchmarks | gains on live benchmarks against strong agents; transfer across apps | internal-only baselines; low absolute numbers; benchmark-specific data | A2, A3, A7, A8, R1, R2, R3, R8, R19, R20, R22 | high |
| T2 Agent evaluation and experimental-design methodologist | technical_rigor | agent evaluation science (neighbor) | controlled comparisons, variance, contamination, budget matching | causal attribution of gains; matched controls; correct numbers | confounded ablations; single runs; overclaimed mechanisms | A3, A4, R1, R2, R6, R7, R9, R11, R12, R13, R21 | high |
| T3 Learning-from-observation / video-pretraining-for-control researcher | novelty | robotics & games: inverse dynamics, VPT, latent-action pretraining (generated neighbor) | IDM auto-labeling, behaviour cloning from video | a clear delta over VPT-style pipelines; insight into what video teaches | "first" claims for known recipes; no analysis of the transfer | A1, A6, R4, R6, R10, R17, R24 | medium |
| T4 Temporal video grounding / action localization researcher | technical_rigor | video understanding (neighbor) | dense event detection, temporal boundaries, tIoU metrics | standard localization metrics; out-of-domain tests | lenient hit criteria; precision claims beyond the frame rate | A5, A11, R5, R10, R11, R13, R16 | medium |
| T5 Foundation-model pretraining and data-scaling researcher | significance | continued pretraining and data scaling (generated neighbor) | data mixtures, token budgets, scaling studies | scalable data sources that move the frontier | token/compute confounds; one base model; three-point "scaling laws" | A1, A2, A3, A4, A12, R1, R2, R7, R15, R19, R21 | medium |
| T6 Web-data curation and responsible-data researcher | reproducibility | web-data curation, copyright and PII (generated neighbor) | large scraped corpora, datasheets, release practice | documented funnels; releasable artifacts; PII handling | scraping without licence analysis; unreleased data; closed-model labeling | A9, A10, A13, R12, R14, R15, R16, R23 | medium |
| TA advocate | significance | the task | champion of the paper's best case | what the paper is worth once answerable issues are answered | — | A1, A3, A6, A11, all reasons graded major by others | (always) |

Every aspect with ≥ 12% of the ratio (rigor 23%, validation 19%, novelty 16%, significance 16%) has a type. Clarity (10%) and ethics (8%) have no type of their own. Their reasons sit with T4/TA (clarity) and T6 (ethics), and the script renormalizes their shares away.

---

## 5. Reviews

### T1: Computer-use / GUI agent specialist (experimental_validation; the task)

**Reading of the ledger.**
- Holds: A2 (the same Stage 2 on both sides makes this a cleaner comparison than most CUA data papers), A3 (non-overlapping three-run spreads at 20 steps), A7 (gains in chrome, writer and thunderbird, not one app). Discounts: A8 (per-video length is not task length, R20).
- R1: major (26B extra tokens with no matched control). R2: major (OSWorld-G grounding data only on the treated side, for the same app ecosystem). R3: major (15.8% means nothing to me without a single external 7B agent or alternative data source in the table). R4: minor (from an agent's view, the downstream number matters more than component ablations). R8: minor (unsettled question). R19: minor. R22: minor (terminate collapse is worrying for live use but does not show on OSWorld). R7: minor.

**Opinion.** I want this to work. Tutorial video is the obvious untapped source for computer-use data, and this is a serious, at-scale attempt. The comparison design (identical Stage 2, three runs at 20 steps) is better than the norm. But as an agent builder, I cannot tell from this paper whether I should use the pipeline. The only baseline is the authors' own SFT model, and the treated model also received 26B more tokens (R1) plus grounding pairs from OSWorld-G that the baseline did not get (R2). That is exactly the kind of data that moves OSWorld. No external agent or competing data source is reported (R3), so 15.8% on OSWorld-Verified cannot be placed. A single table comparing against published 7B agents under the same protocol, and one control giving the baseline the grounding pairs, would change my mind substantially. As it stands, the evidence shows that "more data, some of it relevant, helps a weak 7B model", not that IDM-mined video labels are the cause.

Decisive: R1 (major), R2 (major), R3 (major), A2 ↔ R1/R2 (A2 holds only partly), A3 (strong)

**Scores.** Pool position 50 (basis: R1, R2, R3 against A2, A3). Technical Rigor 50, Clarity 62, Novelty 56, Significance 62, Experimental Validation 46, Reproducibility 55, Ethics 50. Overall 3. Confidence 4.

### T2: Agent evaluation and experimental-design methodologist (technical_rigor; evaluation science)

**Reading of the ledger.**
- Holds: A3 (the 20-step design with three runs is the paper's best methodological feature). Discounts: A4 (three single-run points do not establish "a clear relationship", R21), and A2 to moderate until R1/R2 are controlled.
- R1: major. R2: major (the treatment differs from the control in two ways at once; that is a confounded ablation, not a minor gap). R6: major (the title-level framing "unsupervised" contradicts App. C–D and Stage 2; checked by P4). R7: major (C5 is a headline section, built on single runs and an untested mechanism). R9: minor (question; but the paper should run the check). R8: minor (question). R11: minor. R12: minor. R13: minor. R21: minor.

**Opinion.** The paper's causal claim is that video-mined supervision causes the gains. The experiment that would show this is absent. Treatment = 26B tokens of mined trajectories + OSWorld-G grounding pairs + 60 GPU-node-hours; control = none of those. Both confounds (R1, R2) point the same way, and neither is discussed. The secondary claims are weaker still. The long-horizon story (C5, §4.2) attributes subgoal decomposition and error recovery to a +1.65 pp difference between single runs, when the 20-step runs of the same model already vary by 1.11 pp (P5). The "unsupervised" framing (R6) contradicts the paper's own appendices. I also found several arithmetic slips (R11–R13). None is serious alone, but together they suggest the tables were not cross-checked. What would change my mind: (i) Stage-2-only + grounding pairs; (ii) a token-matched Stage 1 on non-video data or on unlabeled video frames; (iii) three seeds at 50 steps. If the gain survives (i) and (ii), this is a good paper.

Decisive: R1 (major), R2 (major), R7 (major), R6 (major), A3 (strong)

**Scores.** Pool position 42 (basis: R1, R2, R7, R6). Technical Rigor 44, Clarity 58, Novelty 55, Significance 58, Experimental Validation 45, Reproducibility 52, Ethics 50. Overall 3. Confidence 4.

### T3: Learning-from-observation / video-pretraining-for-control researcher (novelty; robotics and games)

**Reading of the ledger.**
- Holds: A6 (the VPT lineage is disclosed and the GUI-specific decomposition into dense event detection + parameterization is reasonable), A1. Discounts: none beyond that.
- R17: major (as a recipe, this is VPT on a new domain; the tutorial-mining delta over AgentTrek and video-to-dataset work is asserted in one sentence, not shown). R4: major (in VPT-style work, the interesting result is what the IDM needs and how much label noise the policy tolerates; neither is measured). R24 (added in this review): major (see below). R6: minor (wording; I care less than T2 about the label). R10: minor.
- **New reason R24** (added in T3 review): the paper never asks what the video data teaches. Tables 4 and 5 give per-app and per-action numbers, but no analysis relates gains to video coverage per domain (Figure 3) or explains the terminate drop (R22).

**Contribution check.**
1. *What does a reader learn?* That IDM-labeled GUI tutorials help a 7B VLM agent, by about 5 pp on OSWorld-Verified. Given VPT and LAPA, this was the expected result. The why and when (R24, R4) are missing.
2. *Does the setting support the framing?* "Web scale" is 39k videos from 50+ channels. "Long-horizon" rests on single runs (R7) and per-video lengths (R20). Partly.
3. *Conceptual or refinement?* A refinement and transfer of the VPT recipe to GUIs (R17); a moderate delta, with real engineering effort.
4. *Would the conclusions transfer?* Untested beyond one 7B base model (R19).

Questions 1 and 3 fail, so novelty is in the lower half of the pool.

**Opinion.** The paper is a competent, large-scale port of inverse-dynamics auto-labeling to screen recordings, and it says so honestly in §2.2 and §5. That honesty earns the transfer credit (A6), but the paper does not show what the transfer required. There is no ablation of the two-stage IDM against a single-stage alternative, no study of label quality versus downstream gain, and no analysis of which skills the video teaches. VPT's own contribution included exactly such analyses (IDM data size, fine-tuning effects). Here the scientific content beyond "it helps" is thin. A label-noise study (filtering by IDM confidence at fixed tokens) and a per-domain gain analysis would lift my view of the novelty considerably.

Decisive: R17 (major), R4 (major), R24 (major), A6 (moderate, holds)

**Scores.** Pool position 52 (basis: R17, R4, R24 against A6, A1). Technical Rigor 54, Clarity 62, Novelty 50, Significance 60, Experimental Validation 52, Reproducibility 55, Ethics 50. Overall 3. Confidence 3.

### T4: Temporal video grounding / action localization researcher (technical_rigor; video understanding)

**Reading of the ledger.**
- Holds: A5 (per-type P/R/F1 on 20k events is more than many pipelines report), A11. Discounts: A5's "Depends on" partly fails (P9: the test set is in-domain).
- R5: major (an error by derivation; "millisecond-precision" is impossible at 4 fps with a 2-frame patch, and the any-overlap criterion would not measure it anyway). R10: major (10 wild videos and a lenient "plausibly produce" criterion are not an evaluation of web-scale labeling). R11: minor. R13: minor. R16: minor.

**Opinion.** From a temporal-localization standpoint, the detector is a reasonable VLM fine-tune, but its evaluation does not meet the field's norms. A hit is any temporal overlap with the same type. That is far looser than tIoU-thresholded mAP, so the reported 0.88 precision says little about boundaries, which are exactly what the paper's "millisecond-precision" claim (§1) is about. The claim is not merely unsupported: at 0.5 s temporal tokens (P3) it cannot be true of the model's output. The test set comes from the same OpenCUA-style recordings as training, while the target domain (YouTube tutorials, with zoom, overlays and compression) gets 10 videos and a "∼70%" human estimate. The keystroke failure (press recall 0.08) means the pipeline mainly mines clicks, consistent with Table 8 (67% left click). I would want tIoU@{0.3, 0.5, 0.7} on a labeled YouTube subset, and the precision claim removed.

Decisive: R5 (major), R10 (major), A5 (moderate, partly holds)

**Scores.** Pool position 45 (basis: R5, R10). Technical Rigor 46, Clarity 58, Novelty 56, Significance 58, Experimental Validation 48, Reproducibility 52, Ethics 50. Overall 3. Confidence 3.

### T5: Foundation-model pretraining and data-scaling researcher (significance; continued pretraining)

**Reading of the ledger.**
- Holds: A1 (strong: a new, cheap and abundant data source for an important agent capability), A3, A4 (the direction is right, if thin), A12. A2 holds as moderate.
- R1: major (a token budget is the first thing to match in a data paper). R2: major (the mixture differs). R19: major (one 7B base at 15.8% absolute; data that helps a weak model often washes out on stronger ones). R21: minor. R7: minor (the long-horizon story is secondary to me). R15: minor (I read §1's "reproducible pipeline" as covering the data; **updated after P12: minor → major**).

**Contribution check.**
1. *What does a reader learn?* That a passive video corpus is a viable Stage-1 source for computer-use pretraining, with monotone returns over 0–26B tokens. Useful, though the confounds (R1, R2) blur it.
2. *Does the setting support the framing?* "Web scale" is moderate (39k videos); one base model.
3. *Conceptual or refinement?* A new data source for this task. Moderate.
4. *Would it transfer?* Unknown for stronger bases (R19).

**Opinion.** This is the kind of data-source paper the agent community needs. The pipeline is cheap (ScreenFilter at 840 h per GPU-day), the source is effectively unbounded, and the 0/50/100% curve has not obviously saturated. That gives a plausible path to far more pretraining data than human annotation can supply, which is why I place it above the median. The paper still falls short of a clear accept for me, for two reasons. It does not match token budgets or data mixtures (R1, R2), the standard controls in any data-mixture paper. And it tests one 7B base whose absolute numbers are far from where practitioners operate (R19). If a token-matched control and one stronger base reproduce the gain, the paper becomes a solid accept.

Decisive: A1 (strong), A3 (strong), R1 (major), R19 (major)

**Scores.** Pool position 66 (basis: A1, A3, A4 against R1, R19). Technical Rigor 60, Clarity 66, Novelty 62, Significance 70, Experimental Validation 62, Reproducibility 60, Ethics 52. Overall 4. Confidence 3.

### T6: Web-data curation and responsible-data researcher (reproducibility; web data)

**Reading of the ledger.**
- Holds: A9 (configs are fuller than usual), A13. Discounts: A10 (a promise of tools, not of data).
- R15: major (the scientific artifact is the mined dataset, and its release is not mentioned; optimizer settings are missing; labeling relies on closed GPT-5/GPT-4.1). R14: major (55k scraped videos, screen recordings full of personal data, and one clause on "license/PII checks"). R23: minor. R12: minor. R16: minor.

**Opinion.** Reproducibility here hinges on the data, not the tools. A reader cannot rebuild the corpus without the video IDs and the channel lists. The paper states neither, nor whether the trajectories will be released (R15). The funnel from 55,603 videos to 39,000 is not documented (R23), and the corpus tables do not add up (R12, Table 6 in R13). On ethics: screen recordings routinely show email addresses, account names and typed credentials (the Figure 9 sample types a password-like string). The paper must say what PII detection was done, with what recall, and on what legal basis YouTube content is used for training and possibly redistributed (R14). These are fixable with a datasheet and an ethics statement, but as submitted they weigh on the paper. I would move to borderline-positive with a released ID list, a datasheet and a concrete PII procedure.

Decisive: R15 (major), R14 (major), A9 (moderate)

**Scores.** Pool position 45 (basis: R15, R14, R23). Technical Rigor 54, Clarity 58, Novelty 56, Significance 58, Experimental Validation 52, Reproducibility 50, Ethics 40. Overall 3. Confidence 3.

### TA: advocate (significance; the task)

**Blocking vs answerable**, for each reason another type graded major:

| Reason | Graded major by | Advocate's call | Advocate grade |
|---|---|---|---|
| R1 compute confound | T1, T2, T5 | blocking: needs new runs | major |
| R2 grounding-data confound | T1, T2, T5 | blocking: needs a new run; the text places the data in Stage 1 only | major |
| R3 no external baselines | T1 | answerable: published 7B numbers in one table | minor |
| R4 no component ablations | T3 | blocking: needs new runs | major |
| R5 millisecond claim | T4 | answerable: delete the phrase (an error in wording, not a result) | minor |
| R6 "unsupervised" | T2 | answerable: reword | minor |
| R7 single-run test-time scaling | T2 | answerable: tone down C5 and present it as preliminary | minor |
| R10 thin IDM evaluation | T4 | answerable in part: report annotator count and agreement; the core numbers stand | minor |
| R14 ethics | T6 | answerable: ethics statement and PII procedure | minor |
| R15 data release | T6, T5 | answerable: commit to release IDs and trajectories | minor |
| R17 novelty delta | T3 | not answerable by revision (a judgment) | major |
| R19 one base model | T5 | blocking: needs a new base | major |
| R24 what video teaches | T3 | answerable in part from existing runs (per-app analysis of Table 4) | minor |

**Accept case.** A1 and A3. The paper opens a cheap, effectively unbounded data source for computer-use agents, and shows with a cleanly repeated 20-step evaluation (three runs per model, non-overlapping spreads) that adding it to a fixed Stage 2 raises OSWorld-Verified success by half. An ICLR reader would gain a working recipe and tools (A10, A12) for mining their own corpora.

**Opinion.** Answer what can be answered: the claims toned down (R5, R6, R7), the published baselines tabulated (R3), the ethics and release commitments made (R14, R15). What remains is a paper with one large, robust effect whose cause is not yet isolated (R1, R2), no component analysis (R4), and one base model (R19). That paper sits just above the borderline. The data-source idea is valuable, but two blocking confounds sit on the central claim. I would argue for it in discussion only if the authors' response shows the grounding pairs are small relative to the effect, for example with a Stage-2-plus-grounding run.

Decisive: A1 (strong), A3 (strong), R1 (major, blocking), R2 (major, blocking)

**Scores.** Pool position 65 (basis: A1, A3 with answerable reasons answered; R1, R2, R4, R19 remain). Technical Rigor 60, Clarity 68, Novelty 62, Significance 72, Experimental Validation 62, Reproducibility 62, Ethics 55. Overall 4. Confidence 3.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P12 | T6 (major) vs T5 (minor) on R15 | Does the paper state that the mined trajectories or video list will be released? | confirmed not stated. §1 bullet 4: "we release SCREENFILTER for efficient GUI filtering and VIDEO2ACTION for action extraction as open-source tools"; §6 likewise; no mention of data, IDs or trained agents | T5: R15 minor → major (not among T5's decisive items; scores unchanged) |

Splits on values that stay: R4 (T1 minor vs T3 major: how much component ablations matter), R6 (T2 major vs T3 minor), R7 (T2 major vs T1/T5 minor), R17 (T3 major vs TA's acceptance of the transfer as a contribution, still graded major).

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 Computer-use / GUI agent specialist | experimental_validation | 0.230 | 50 | 3 | 4 |
| T2 Agent evaluation methodologist | technical_rigor | 0.138 | 42 | 3 | 4 |
| T3 Learning-from-observation researcher | novelty | 0.190 | 52 | 3 | 3 |
| T4 Temporal video grounding researcher | technical_rigor | 0.138 | 45 | 3 | 3 |
| T5 Pretraining and data-scaling researcher | significance | 0.095 | 66 | 4 | 3 |
| T6 Web-data curation / responsible-data researcher | reproducibility | 0.115 | 45 | 3 | 3 |
| TA advocate | significance | 0.095 | 65 | 4 | 3 |

- **Aspect-weighted rating:** 3.19 → **final rating 3 (Borderline Reject)**. ICLR label: "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})". The ICLR scale status is *secondary*: recent forms use {0,2,4,6,8,10}; verify against the current form. ICLR sub-scores from the script: Soundness 2, Presentation 2, Contribution 2.
- Weighted pool position 51.0; plain mean 3.29; spread 1 (3–4).
- Uncovered aspects and warnings: none from the script. Clarity (10%) and ethics (8%) have no type and are renormalized away; neither is above 12%.
- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

```
Ledger mode: aspect-weighted average (iclr)
| Reviewer type | Aspect | Aspect share | Weight |
| T1 (Computer-use / GUI agent specialist) | experimental_validation | 19% | 0.230 |
| T2 (Agent evaluation and experimental-design methodologist) | technical_rigor | 23% | 0.138 |
| T3 (Learning-from-observation / video-pretraining-for-control researcher) | novelty | 16% | 0.190 |
| T4 (Temporal video grounding / action localization researcher) | technical_rigor | 23% | 0.138 |
| T5 (Foundation-model pretraining and data-scaling researcher) | significance | 16% | 0.095 |
| T6 (Web-data curation and responsible-data researcher) | reproducibility | 9% | 0.115 |
| TA (advocate) | significance | 16% | 0.095 |
Final rating (aspect-weighted mean): 3.19 -> 3 (Borderline Reject) · plain mean 3.29 · weighted pool position 51.0
Composites: T1 53.6, T2 50.8, T3 54.4, T4 51.9, T5 62.0, T6 53.1, TA 63.0; official composite 55.5 -> band 3
ICLR (2026, secondary): composite 55.5, band 3 -> 3; "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"; Soundness 2, Presentation 2, Contribution 2
Warnings: none
```
</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R1 | 4 of 7 | T1 major, T2 major, T5 major, TA major |
| R2 | 4 of 7 | T1 major, T2 major, T5 major, TA major |
| R3 | 2 of 7 | T1 major, TA minor |
| R4 | 3 of 7 | T1 minor, T3 major, TA major |
| R5 | 2 of 7 | T4 major, TA minor |
| R6 | 3 of 7 | T2 major, T3 minor, TA minor |
| R7 | 4 of 7 | T1 minor, T2 major, T5 minor, TA minor |
| R8 | 2 of 7 | T1 minor, T2 minor (question) |
| R9 | 1 of 7 | T2 minor (question) |
| R10 | 3 of 7 | T3 minor, T4 major, TA minor |
| R11 | 2 of 7 | T2 minor, T4 minor |
| R12 | 2 of 7 | T2 minor, T6 minor |
| R13 | 2 of 7 | T2 minor, T4 minor |
| R14 | 2 of 7 | T6 major, TA minor |
| R15 | 3 of 7 | T5 major (after P12), T6 major, TA minor |
| R16 | 2 of 7 | T4 minor, T6 minor |
| R17 | 2 of 7 | T3 major, TA major |
| R19 | 3 of 7 | T1 minor, T5 major, TA major |
| R20 | 1 of 7 | T1 minor |
| R21 | 2 of 7 | T2 minor, T5 minor |
| R22 | 1 of 7 | T1 minor |
| R23 | 1 of 7 | T6 minor |
| R24 | 2 of 7 | T3 major, TA minor |
| A1 | 3 of 7 | held by T3, T5, TA |
| A2 | 2 of 7 | held by T1 and T5 (moderate); T2 discounts it until R1 and R2 are settled |
| A3 | 4 of 7 | held by T1, T2, T5, TA |
| A4 | 2 of 7 | T5 held; T2 discounted |
| A5 | 1 of 7 | T4 held (partly) |
| A6 | 2 of 7 | T3 held, TA held |
| A7 | 1 of 7 | T1 held |
| A8 | 1 of 7 | T1 discounted |
| A9 | 1 of 7 | T6 held |
| A10 | 1 of 7 | T6 discounted |
| A11 | 2 of 7 | T4 held, TA held |
| A12 | 1 of 7 | T5 held |
| A13 | 1 of 7 | T6 held |

### Key strengths

- A3: a repeated, non-overlapping 20-step OSWorld-Verified comparison (9.13–9.42 vs 13.57–14.68). Held by 4 of 7 types.
- A1: an abundant, cheap new data source for computer-use agents (39k videos → 1.52M steps). Held by 3 of 7.
- A2: an identical Stage 2 on both sides gives +4.8 pp OSWorld (20 steps) and +5.2 pp AgentNetBench. Held as moderate by T1 and T5, pending R1/R2.
- A6: a disclosed, argued transfer of inverse-dynamics labeling from robotics to GUIs. Held by T3 and TA.

### Top concerns (at most five)

1. R1: the treated model gets 26B extra Stage-1 tokens with no equal-compute control (§2.3.2; Fig. 11). Fix: a token-matched Stage 1 on non-video data and on unlabeled video, ≈60 h on 32 H100s each.
2. R2: OSWorld-G grounding pairs are only on the treated side (§2.3.1–2.3.2). Fix: Stage-2-only + grounding pairs, ≈16 h on 64 H100s.
3. R4: no ablation of the monologue, filtering or IDM noise, though an estimated ~58% of steps are correct end to end (Tables 1–2; §4). Fix: 2–3 half-scale Stage-1 runs.
4. R19: one 7B base model at 15.8% absolute (§2.3.2; Fig. 5). Fix: repeat on a stronger or larger base.
5. R17: the delta over VPT, AgentTrek and video-to-dataset work is asserted, not shown (§5). Fix: one matched-token comparison with a tutorial-derived alternative, and a sharper related-work delta.
(R15 ties with R4, R17 and R19 at two major grades; it is in the Roadmap at Priority 2.)

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R1 | Token- and compute-matched Stage-1 controls (non-video data; video frames + ASR without IDM actions) | ≈ 1–2 × 60 h on 32 H100s |
| 1 | R2 | Stage-2-only + OSWorld-G grounding pairs baseline (or Stage 1 without them) | ≈ 16–60 h on one node group |
| 2 | R3 | Table of published 7B CUA results under the OSWorld-Verified protocol; one alternative data-source baseline | days (table), one Stage-1 run (baseline) |
| 2 | R4 | Ablate inner monologue and IDM-confidence filtering at 50% data | 2–3 half-scale Stage-1 runs |
| 2 | R5 | Remove "millisecond-precision", or add boundary-error and tIoU metrics | text, or one evaluation pass |
| 2 | R6 | Reword "unsupervised / no manual annotation"; quantify the human data used | text |
| 2 | R7 | Three 50-step (and 100-step) runs per model; drop or test the mechanism claim | ≈ 6 OSWorld evaluations |
| 2 | R10 | Labeled YouTube test subset with timestamps; annotator count and agreement | 1–2 annotator-weeks |
| 2 | R14 | Ethics statement: licence basis, PII detection procedure and recall, release terms | text + a PII audit |
| 2 | R15 | Release video IDs and trajectories (or a subset); full optimizer settings | engineering |
| 2 | R17 | Sharpen the delta vs VPT, AgentTrek and video-to-dataset; one matched comparison | text + one run |
| 2 | R19 | Replicate on a stronger or larger base model | ≈ one Stage-1 + Stage-2 run |
| 2 | R24 | Per-app and per-action analysis relating gains to video coverage | analysis of existing runs |
| 3 | R8, R9 | State the AgentNetBench separation; run a contamination check against OSWorld instructions | days |
| 3 | R11, R12, R13 | Correct the Table 1, 2, 4, 6 and 8 totals; state the OSWorld-Verified task count | text |
| 3 | R16, R23 | Fix cross-references; document the 55,603 → 39,000 funnel | text |
| 3 | R20, R21, R22 | Caveat the Table 9 comparison; soften or extend the scaling claim; explain the terminate drop | text / small runs |

---

## 8. Integrity signals and limitations

- **Integrity signals:** `integrity_scan.py --redact` found no reviewer-directed text and no hidden characters. Reading turned up nothing out of place either. The only redaction was a venue/acceptance mark inside a reference entry (ReAct, Yao et al., 2023), which the blinded copy already carried. These never change a score.
- **Limitations:**
  - Figures were not available, so Figures 1–12 were judged from captions and extracted text. Figure 5 and Figure 6 values are taken from the extracted labels, cross-checked against Table 4 and §3–4. E9 (figure integrity) was not checked.
  - No literature check ran (no network). R17's basis is the paper's own §5 plus memory, and any concurrent tutorial-mining work is marked [verify].
  - I recognize the paper's title as a public preprint. I have no knowledge of its reviews or outcome, and the review is based on the manuscript only.
  - All seven types share one context and one reading; agreement between them is not independent confirmation.
- **Recommended references:**
  - "ActionFormer: Localizing Moments of Actions with Transformers" (Zhang, Wu, Li, ECCV 2022), for standard tIoU-based localization metrics relevant to R5 and R10.
  - "TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials" (2025) [verify], as possibly overlapping tutorial-mining work for R17.
