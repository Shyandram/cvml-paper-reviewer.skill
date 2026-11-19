# Peer Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | empirical (method + mined training corpus) |
| Field, sub-area | machine learning / multimodal agents; computer-use (GUI) agents, learning from video |
| Task | Computer-use / GUI agents. Not listed in `task_neighbors.md`; adapted from "Vision–language models, multimodal LLMs" (main claim), "Video understanding, tracking" (the IDM) and "Reinforcement learning" (imitation from observation) |
| Neighboring fields | VLM/MLLM pretraining and data curation; temporal action localization and video grounding; imitation learning from observation and inverse dynamics (robotics, VPT-style) [added]; LLM/VLM agent evaluation science; web and GUI trajectory synthesis (web agents) [added]; responsible web-scale data collection and privacy [added] |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | (`aggregate_scores.py ratio --paper-type empirical --venue iclr`): technical rigor 23%, experimental validation 19%, novelty 16%, significance 16%, clarity 10%, reproducibility 9%, ethics 8% |
| Literature check | off: no network access. Novelty reasons that rest on memory are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Input note: the review was written from text extracted from the PDF. Figures were not available. Figure-dependent claims (Figs. 5, 6, 10 and the loss curves in Figs. 8, 11 and 12) are judged from their captions, the numbers printed in the extracted text, and the matching tables (Table 4 restates Fig. 5's OSWorld numbers).

---

## 1. Paper memory

**Claims.**
- C1: VideoAgentTrek mines computer-use trajectories from unlabeled public screen recordings at web scale, "eliminating the need for manual annotation": 39,000 videos → 1.52M steps (Abstract; Sec. 2.3.1).
- C2: Video2Action, an inverse dynamics module, detects GUI actions with "millisecond-precision temporal localization" and extracts parameters "with high fidelity" (Abstract; Sec. 1 contributions bullet 2; Sec. 3.2; Tables 1–2).
- C3: Continued pretraining on the mined data improves agents: OSWorld-Verified 9.3% → 15.8% ("70% relative"), AgentNetBench step SR 64.1% → 69.3% (Abstract; Sec. 3.1.2; Fig. 5; Tables 4–5).
- C4: Performance scales with the amount of video pretraining data (Sec. 4.1; Fig. 6).
- C5: Video pretraining enables test-time scaling and long-horizon planning (Sec. 3.1.2; Sec. 4.2).
- C6: A reproducible pipeline, with ScreenFilter and Video2Action released as open source (Sec. 1 contributions bullet 4; Sec. 6).

**Setup facts.**
- Corpus: 55,603 videos (~10,000 h) from 50+ channels (Sec. 2.1.3; App. H). ScreenFilter keeps 7,377 h (Sec. 2.1.2). 39,000 videos are processed, at ~39 steps each (Sec. 2.3.1). How the 39,000 were selected: not stated.
- ScreenFilter: YOLOv8x trained on 15,000 synthetic cursor composites; F1 89.58% on a held-out set (App. B).
- Event detector: Qwen2.5-VL-7B-Instruct, full fine-tuning on 154 h of OpenCUA video with logs (App. C). 4 fps, 10 s clips, temporal patch of 2 frames (App. C). 32×H100, ~15 h (Fig. 8).
- Parameterizer: Qwen2.5-VL-7B, trained on 512,000 OpenCUA clips (App. D).
- Inner monologue: GPT-5 Medium, conditioned on the action, keyframes and ASR (Sec. 2.2.3; App. E).
- Agent: Qwen2.5-VL-7B base. Stage 1: 26B tokens of video trajectories plus GUI grounding pairs (OSWorld-G, ~1B tokens), one epoch (Sec. 2.3.1–2.3.2). Stage 2: 8B tokens of OpenCUA + AGUVIS human trajectories (Sec. 2.3.1–2.3.2). Stage-1 config: 32×H100, batch 512, 6,500 iterations, ~60 h (Fig. 11). Stage-2 config: 64×H100, 3,000 iterations, ~16 h (Fig. 12).
- Optimizer, learning rate, warmup, sequence length: not stated.
- Evaluation: OSWorld-Verified with a 5-screenshot window. Three runs at 20 steps, one run at 50 steps (App. G). AgentNetBench: 100 offline tasks (Sec. 3.1.1), single run.
- Decontamination or overlap checks: not stated.
- Seeds: not stated.

**Headline numbers.**
- OSWorld-Verified: 4.5 (base) / 9.3 (stage2 only) / 14.13 (20 steps) / 15.78 (50 steps) (Fig. 5; Table 4).
- AgentNetBench: 38.5 / 64.1 / 69.3 (Fig. 5; Table 5).
- Detector: P 0.88, R 0.70, F1 0.78 (Table 1).
- Parameterization: accuracy 0.658 (Table 2).
- Scaling: 9.3 / 13.3 / 15.7 on OSWorld and 64.1 / 68.1 / 69.3 on AgentNetBench (Fig. 6, text).
- Average of 39.25 steps per trajectory (Table 9; estimated from a sample of 5,416).

**Appendix summary.**
- A: video quality standards.
- B: ScreenFilter.
- C–D: detector and parameterizer data and training.
- E: monologue prompt.
- F: training formats and configurations.
- G: evaluation protocol and per-run results (Tables 4–5).
- H: corpus statistics (Tables 6–10).

**Could not be read.** Figures 1–12 as images (layouts and loss curves). Fig. 6 and Fig. 10 values come only from text fragments. The equations in Sec. 2.2 are partly garbled by extraction but readable. No supplementary material or code was provided.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | significance | Targets the data bottleneck of computer-use agents with an abundant, unused source: public screen-recorded tutorials | Sec. 1 ¶1–2: "creating such datasets through manual annotation is extraordinarily expensive" | strong | — |
| A2 | resource / scale | Large mined corpus: 39,000 videos, ~1.52M steps, ~26B tokens, long trajectories | Sec. 2.3.1; Table 9: avg 39.25 steps vs 18.6 (AgentNet) | strong | R3 not upheld at fatal level (labels usable) |
| A3 | empirical strength | Stage 1 gives a consistent OSWorld-Verified gain: three 20-step runs 13.57–14.68% vs 9.13–9.42%, non-overlapping | Table 4; App. G | strong | R1 (what causes the gain) |
| A4 | empirical strength | AgentNetBench step SR 64.1 → 69.3, with gains on 8 of 9 comparable action types | Sec. 3.1.2; Table 5 | moderate | R7 (benchmark held out), R14 |
| A5 | empirical / scaling | Monotone data scaling across 0/50/100% of video tokens on both benchmarks | Sec. 4.1; Fig. 6 (text: 9.3 → 13.3 → 15.7) | moderate | the ablation isolates video data (R1) |
| A6 | novelty | Disclosed transfer of VPT-style inverse dynamics to desktop GUIs, with a two-stage design: prompt-free dense event detection, then segment parameterization | Sec. 2.2; Sec. 5 | moderate | R13 (delta over prior GUI mining) |
| A7 | soundness | Detector evaluated on a held-out 23 h set (20,282 events) per type, with weak types reported honestly | Sec. 3.2.1; Table 1: press recall 0.08 | moderate | — |
| A8 | clarity | Pipeline is clearly organized, with overview figures and formal task definitions | Figs. 1, 2, 4; Sec. 2.2.1–2.2.2 | moderate | — |
| A9 | reproducibility | Hardware, batch, iterations and wall-clock for all three models; full monologue prompt; filter thresholds; frame-rate policy | Figs. 8, 11, 12; App. B, D, E | moderate | — |
| A10 | resource | Promised open-source release of ScreenFilter and Video2Action | Sec. 1 bullet 4; Sec. 6 | weak | release actually happens |
| A11 | insight | Budget sensitivity: the video-pretrained agent gains from 20 to 50 steps, while the SFT-only agent is flat (9.27%) | Sec. 4.2; Table 4 | weak (after P2) | R5 |
| A12 | transparency | Per-application and per-action breakdowns show where gains come from | Table 4 (chrome 8 → 13–15 solved); Table 5 | moderate | — |
| A13 | efficiency | Cheap filtering stage | App. B: "approximately 840 hours of video per GPU-day" | weak | — |
| A14 | ethics / honesty | Label noise and classifier limitations acknowledged | Sec. 2.3.2: "inevitably contain residual noise"; App. H "Limitations" | weak | — |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | soundness | The SFT-only baseline skips Stage 1 entirely. It therefore lacks ~26B tokens of extra training (~1,920 H100-h) and the OSWorld-G grounding pairs. No compute- or data-matched control isolates the mined video actions | Sec. 2.3.2: Stage 1 is "augmented with a small number of GUI grounding pairs"; Sec. 2.3.1 (~1B grounding tokens); Fig. 11 | gap | major | Controls at equal Stage-1 tokens: grounding only; human or synthetic trajectories; video frames + ASR without mined actions (~2k H100-h each) |
| R2 | exp. validation | No external agents or alternative data sources are compared. Agents the paper cites as trained on the same OpenCUA/AGUVIS data are not reported, nor is AgentTrek or OS-Genesis-style synthetic data at equal tokens. 15.8% cannot be placed against 7B agents | Fig. 5 / Table 4 show only base, stage2-only and stage1+2; Sec. 5 | gap | major | Report published 7B agents under the same protocol, plus a synthetic-trajectory Stage 1 (1–2 weeks of compute) |
| R3 | soundness | Action parameterization, the source of click coordinates and typed text, is validated only by a lenient manual "plausibly produce" judgment on 500 samples. Accuracy is 0.658 overall, 0.366 for drag and 0.362 for press. It is not evaluated against held-out OpenCUA logs, which do hold exact parameters, and there is no end-to-end trajectory-correctness estimate | Sec. 2.2.2: "Because ground-truth object boxes are unavailable, we evaluate only on unseen web tutorials"; Table 2 | gap | major | Pixel error and text exact-match on held-out OpenCUA clips; audit ~200 full trajectories |
| R4 | claim accuracy | "Millisecond-precision" and "high fidelity" are unsupported. The check: 4 fps sampling and a 2-frame temporal patch give 0.5 s granularity, a hit needs only "any temporal overlap", and no boundary error is reported | Sec. 1 bullet 2; App. C; Sec. 3.2.1 | error | major | Report boundary error or tIoU-thresholded AP, or drop the claim (low cost) |
| R5 | claim accuracy | The test-time-scaling claim is overclaimed. The check: one 50-step run; +1.65 pt over the 20-step mean ≈ 6 of 361 tasks; +1.10 pt over the best 20-step run, against a 1.11 pt spread among the 20-step runs. The mechanism ("teaches the model to decompose complex tasks into subgoals") is untested | Sec. 4.2; Table 4; App. G: "For the 50-step budget, we perform a single run" | error | major | Three 50/100-step runs per model; trajectory analysis, or soften the wording |
| R6 | exp. validation | "Clear relationship" between data and performance rests on 3 points, one run each | Sec. 4.1; Fig. 6 | gap | minor | Add 25%/75% points and repeated runs |
| R7 | validity | Possible overlap of tutorials with OSWorld tasks (LibreOffice, GIMP, Chrome, VLC, Thunderbird are common tutorial topics). AgentNetBench comes from AgentNet, the same OpenCUA corpus used in Stage 2 and for IDM training. No decontamination or split statement | Sec. 3.1.1; Sec. 2.3.1; Sec. 2.2.1 | question | major | Report overlap of titles/ASR with task instructions; confirm the AgentNetBench tasks are excluded |
| R8 | soundness | No ablation of pipeline components: monologue (GPT-5), ScreenFilter, IDM label quality, action labels vs raw interleaved frames | Sec. 4 has only the data-scale ablation | gap | major | Ablations at 25% of the Stage-1 budget (~1–2k H100-h) |
| R9 | presentation accuracy | Numerical inconsistencies (recomputed, P4): Table 1 Preds sum to 16,298, not the printed 17,298, and the text gives recall 0.71 vs 0.70 in the table. Table 2: 330/500 = 0.660, not 0.658, and 0.366 is unattainable with 22 samples. Table 4: the stage2 50-step run solves 33 = 9.14% of 361, but 9.27% is printed, and the bucket denominators sum to 359. Table 6 sums to 53,375, not 55,603. Table 8 counts sum to 1,560,464, not 1,547,092, with mouse move/drag printed as 0.1% (actual ≈0.5/0.4%). Table 3 has moveTo = dragTo = 32,840 | Tables 1, 2, 3, 4, 6, 8; Sec. 3.2.1: "solid recall (0.71)" | error | minor | Correct the tables |
| R10 | clarity | Unclear how stage-1 video trajectories get a task goal, and how 39,000 of 55,603 videos were chosen. App. D says "Our dense detector is trained on 512,000 screen-capture clips" inside the parameterizer section; App. D has a dangling "We visualize the data sample in Figure"; Sec. 4.2 cites "Figure 10" for the step distribution (Table 10) | Sec. 2.3.1–2.3.2; App. D; Sec. 4.2 | gap | minor | Describe the stage-1 sample format and selection; fix the references |
| R11 | ethics | No ethics or legal statement on scraping YouTube (ToS, copyright), consent or PII. Typed-text extraction can capture credentials: the Fig. 9 example types "lilybloom123.". "license/PII checks" is only asserted in App. H Limitations, and data release is unstated | App. H; Fig. 9; App. A | gap | major | Ethics statement; describe the PII/credential scrubbing and licence filtering; release terms |
| R12 | reproducibility | Optimizer, LR, warmup, sequence length, image resolution and coordinate normalization are not stated. Dataset release is not committed (only the tools). Monologue generation depends on closed GPT-5 Medium | Figs. 8, 11, 12 (framework/hardware/batch/iterations only); Sec. 1 bullet 4 | gap | major | Full hyperparameters; dataset or video-ID release |
| R13 | novelty | The core mechanism is VPT's IDM auto-labelling transferred to GUIs. Tutorial mining for agents exists (AgentTrek with text tutorials; Jang et al. 2025, video-to-dataset for mobile agents). The delta vs Jang et al. is one sentence | Sec. 5: "typically lacks precise temporal boundaries or action parameters" | judgment | major | Direct comparison with prior video/tutorial mining pipelines |
| R14 | exp. validation | AgentNetBench is a single run on 100 tasks with no variance. Terminate accuracy drops 0.588 → 0.237, undiscussed, while the text says "This consistent improvement" | Table 5; Sec. 3.1.2 | gap | minor | Variance; discuss the termination regression |
| R15 | significance | Absolute performance is low (15.8%). One base model, one scale, no RL stage; no evidence the gain persists with stronger SFT data or larger models (contribution check Q4) | Abstract; Sec. 2.3.2 "Foundation"; Fig. 5 | judgment | major | A second base model or a stronger SFT mixture |
| R16 | soundness | Manual evaluations are under-specified: the in-the-wild detector check uses 10 videos and reports "∼70%" with no counts; Table 2 gives no annotator count, agreement, or meaning of "blinded" | Sec. 3.2.1 "Manual validation"; Sec. 3.2.2 | gap | minor | Report counts, annotators and agreement |
| R17 | clarity | Inconsistent action taxonomy: 5 types (Table 1), 12 (Table 3), 10 (Table 5), 9 (Table 8), with no mapping | Tables 1, 3, 5, 8 | gap | minor | One taxonomy and its mapping |

### Answered

- "OSWorld results are single runs": answered at App. G ("we conduct three independent runs per model and report the average Task SR" at 20 steps) and Table 4.
- "Scaling variants might get different Stage-2 data": answered at Sec. 4.1 ("then apply identical Stage-2 SFT to each variant").
- "The 70% relative gain compares a 50-step result with a 20-step baseline": answered by Table 4. SFT-only at 50 steps is 9.27%, and 15.78/9.27 = 1.70, so the ratio holds at a matched budget.
- "The detector needs manual labels, contradicting 'no manual annotation'": answered at Sec. 2.2.1 and App. C. It is trained from OpenCUA interaction logs converted automatically; the claim concerns the mined videos.

### Aspect coverage

- Technical rigor / soundness: A7; R1, R3, R4, R5, R8, R16
- Experimental validation: A3, A4, A5, A12; R2, R6, R14, R7
- Novelty: A6; R13
- Significance: A1, A2, A11; R15
- Clarity: A8; R9, R10, R17
- Reproducibility: A9, A10; R12
- Ethics: A14; R11
- Efficiency (raised by the paper): A13. There is no efficiency claim to check beyond this.
- Statistical reporting: A3 (3 runs); R5, R6, R14
- Omission sweep (error_audit §4):
  - split and tuning: present for the detector (Sec. 3.2.1), not stated for the agent or decontamination (R7);
  - seeds and variance: partial (App. G; R5, R14);
  - baseline settings: R1, R2;
  - hyperparameters: R12;
  - compute: present for training (Figs. 8, 11, 12), not stated for mining or GPT-5 cost (R12);
  - licence and consent: R11;
  - failure cases: considered, no reason beyond R14. Per-action weaknesses are reported in Tables 1–2.
- Figure integrity (E9): not checked (no images).

### Pairs

- A3 ↔ R1: does the OSWorld gain come from the mined video actions? (C3)
- A3/A4 ↔ R7: are the benchmarks held out from the training sources? (C3)
- A2 ↔ R3: are the mined labels good enough to count as supervision? (C1, C2)
- A7 ↔ R4/R16: what the detector evaluation does and does not show (C2)
- A5 ↔ R6/R1: does performance scale with video data specifically? (C4)
- A6 ↔ R13: novelty of the IDM transfer (C1, C2)
- A11 ↔ R5: test-time scaling (C5)
- A9/A10 ↔ R12: reproducibility (C6)
- A1 ↔ R15: significance at the tested scale (C3)
- A4 ↔ R14: AgentNetBench gain (C3)

---

## 3. Reorganized ledger and probes

No duplicates were merged. The reasons were written distinct from the start: R3 (parameter accuracy) is kept separate from R4 (temporal-precision wording) and R16 (manual protocol).

### By claim

**C1: mining at scale without manual annotation.** A1 (checked), A2 (checked), A13 (checked); A2 ↔ R3; R13 (checked after P9, judgment; high swing for the novelty types).

**C2: accurate IDM.** A6 (checked), A7 (checked); R3 (checked after P3, high swing, decides A2 ↔ R3); R4 (checked after P3, error); R16 (checked, minor); R17 (checked, minor).

**C3: video pretraining improves agents.** A3 (checked; P7), A4 (checked), A12 (checked); R1 (checked after P1, highest swing, decides A3 ↔ R1); R2 (checked after P6, high swing); R7 (open after P5, unsettled question, high swing); R8 (checked, high swing); R14 (checked, minor); R15 (checked, judgment, high swing).

**C4: data scaling.** A5 (checked after P11, weakened); R6 (checked).

**C5: test-time scaling / long horizon.** A11 (checked after P2, weakened); R5 (checked after P2, error).

**C6: reproducible pipeline and release.** A9 (checked), A10 (checked); R12 (checked after P10).

**General.** A8 (checked), A14 (checked); R9 (checked after P4); R10 (checked); R11 (checked after P8, high swing for ethics).

Swing ranking: R1 > R2 > R3 > R7 > R8 > R5 > R13 > R15 > R11 > R4 > R12 > the rest.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R1, A3 | Does the SFT-only baseline receive the OSWorld-G grounding pairs and a compute-matched Stage 1? | Re-read Sec. 2.3.1–2.3.2, 4.1, App. F; recompute GPU-hours | **confirmed**. Stage 1 is "augmented with a small number of GUI grounding pairs" (Sec. 2.3.2), ~1B tokens (Sec. 2.3.1). Stage 2 is human trajectories only. Stage 1 costs 32 × ~60 h ≈ 1,920 H100-h (Fig. 11), none of which the baseline gets | R1 open → checked (gap confirmed); A3 stays strong for "Stage 1 helps", but not for "mined video actions help" |
| P2 | R5, A11 | Is the 20 → 50-step gain larger than run-to-run variation? | Recompute from Table 4 counts (implied denominator 361) | **confirmed**. 20-step runs: 53, 49, 51 solved (14.68/13.57/14.13%), spread 1.11 pt. 50-step: 57 solved (15.78%), a single run: +1.65 pt over the mean (~6 tasks), +1.10 over the best run | R5 judgment → error (checked); A11 moderate → weak |
| P3 | R4, R3 | What temporal resolution and matching criterion support "millisecond precision"? Is parameterization evaluated against exact logs? | Re-read App. C, App. D, Sec. 3.2 | **confirmed**. "downsample videos to 4 fps", "temporal patch size of 2 frames" (App. C); hit iff "any temporal overlap" (Sec. 3.2.1); parameterization evaluated only by manual review, although the training data are logs with exact events (Sec. 2.2.2) | R4 question → error; R3 open → checked |
| P4 | R9 | Do table totals and shares match their rows? | Recompute in python | **confirmed**. Table 1 Preds Σ = 16,298 (14,247 implied hits / 16,298 = 0.874, consistent with P 0.88, so the 17,298 total is a typo). Table 2: Σ correct = 330 → 0.660. Table 4: 33/361 = 9.14 ≠ 9.27; buckets Σ = 359. Table 6 Σ = 53,375. Table 8 Σ = 1,560,464. Mouse move share = 0.5% | R9 checked, error (minor) |
| P5 | R7 | Is any overlap check between the mined videos or Stage-2 data and the evaluation tasks reported? | Text search: contamination, overlap, held-out, decontam, exclude | **cannot be settled from the paper**: not stated after search | R7 stays an open `question`; no type may grade it above minor |
| P6 | R2 | Is any external agent or alternative data source compared? | Re-read Sec. 3, Fig. 5 caption, App. G, Tables 4–5 | **confirmed**: only base, stage2 only and stage1+stage2 | R2 open → checked |
| P7 | A3 | Do the 20-step run ranges overlap? | Recompute | **refuted** (no overlap): 9.13–9.42 vs 13.57–14.68; means 9.32 vs 14.13, a difference of ≈17 tasks | A3 stays strong, checked |
| P8 | R11 | Does the paper describe licensing, consent or PII handling? | Text search: license, consent, PII, privacy, copyright, ethic | **confirmed**: the only mention is App. H, "screened by cursor gating, license/PII checks, and downstream detectors". Fig. 9 shows typed text "lilybloom123." | R11 open → checked |
| P9 | R13, A6 | How does the paper state its delta over prior tutorial/video mining? | Re-read Sec. 5, Sec. 1; no literature query (no network) | **partly**: one sentence ("typically lacks precise temporal boundaries or action parameters"); no empirical comparison | R13 stays a judgment, checked for what the paper says; prior-work positions marked [verify] |
| P10 | R12 | Are LR, optimizer and sequence length stated anywhere? | Text search: learning rate, lr, optimizer, Adam, warmup, sequence length | **confirmed**: not stated after search | R12 open → checked |

Post-review probe P11 is listed under *Settling factual splits* below.

---

## 4. Reviewer roster

All four aspects with ≥ 12% of the ratio have a type: technical rigor (T2, T3), experimental validation (T1), novelty (T4) and significance (T5). Ethics (8%) gets T6 because the paper raises a distinct question there (R11). Clarity (10%) and reproducibility (9%) have no type of their own. Their reasons sit in T1, T3 and T5, and the script renormalizes their share away.

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Computer-use / GUI agent specialist | experimental_validation | computer-use agents (the task) | builds and evaluates OSWorld-style desktop agents | end-to-end task success against strong published agents; clean protocols | baselines that are only ablations; absolute numbers far from the state of the art | R1, R2, R8, R15, R14, R7, A3, A4, A12, A8, A13 | high |
| T2 Training and evaluation methodologist for VLM agents | technical_rigor | LLM/VLM evaluation science | controlled training comparisons, variance and compute parity | matched-compute controls, multiple seeds, claims sized to evidence | extra-compute confounds; single runs behind headline claims | R1, R5, R6, R8, R9, R12, A3, A9, A5 | high |
| T3 Temporal action localization / video grounding researcher | technical_rigor | video understanding (neighbor) | dense event detection, tIoU metrics | standard localization metrics; boundary accuracy | lenient hit criteria; "precise" claims at low fps | R3, R4, R16, R17, R10, A7, A6, A2 | medium |
| T4 Learning-from-observation / inverse-dynamics researcher | novelty | imitation from observation, robotics, VPT-style (neighbor) | IDM auto-labelling, behaviour cloning from video | a new mechanism or insight beyond the transfer; label-noise analysis | known recipes presented as new; no IDM-quality → policy-quality study | R13, R8, R3, R5, A6, A11 | medium |
| T5 Multimodal foundation-model data and scaling researcher | significance | MLLM pretraining and data curation (neighbor) | web-scale data pipelines, scaling studies | reusable data resources, scaling evidence | gains that vanish at scale; unreleased data | R15, R12, R1, R6, R11, A1, A2, A5, A10 | high |
| T6 Data governance and privacy researcher | ethics | responsible web-scale data collection (neighbor) | PII in scraped data, licensing, consent | documented data provenance and scrubbing | credential/PII leakage; ToS-violating scraping without a statement | R11, R12, R10, A14, A1 | low |

---

## 5. Reviews

### T1: Computer-use / GUI agent specialist (experimental_validation; the task)

**Reading of the ledger.**
- Holds:
  - A1: the data bottleneck is real.
  - A2: a 1.5M-step corpus with long trajectories is unusual.
  - A3: three non-overlapping 20-step runs make the gain over SFT-only robust (P7).
  - A4, A12: per-domain and per-action detail helps.
  - A8: clear pipeline.
  - A13: cheap filtering.
- Discounts:
  - A11: a single 50-step run (P2).
  - A5: three single-run points.
- Grades:
  - R2: major. No published agent is reported, so the reader cannot tell whether 15.8% is competitive at 7B, and the paper cites several 7B agents trained on the same human data.
  - R1: major. The baseline does not get the grounding data or the extra compute.
  - R8: major. Which pipeline step matters is unknown.
  - R15: major. 15.8% is low in absolute terms.
  - R3: minor (to me, downstream success matters more than label accuracy).
  - R5, R6: minor.
  - R7: minor (unsettled question).
  - R14: minor.
  - R9: minor.

**Opinion.** The pipeline is a sensible and timely way to use tutorial videos, and the Stage-1 gain over the same model without Stage 1 is consistent across runs. The evaluation still answers a narrower question than the paper claims. It shows that adding 26B tokens of something, including OSWorld-G grounding pairs, beats adding nothing. It does not show that mined video actions beat equally many tokens of grounding data, synthetic trajectories, or repeated human data. And because no external agent is reported, the 9.3% SFT baseline cannot be judged as strong or weak: Sec. 2.3 calls it a "strong finetuning basis", but nothing in the paper supports that. A compute-matched control and a table placing the model among published 7B agents would move me to borderline accept. A component ablation (monologue, filter, labels) would add further.

Decisive: R2 (major), R1 (major), R8 (major), A3 (strong)

**Scores.** Pool position 45 (basis: R2, R1, R8 against A3). Technical Rigor 50, Clarity 60, Novelty 52, Significance 55, Experimental Validation 44, Reproducibility 52, Ethics 56. Overall 3. Confidence 4.

### T2: Training and evaluation methodologist for VLM agents (technical_rigor; LLM/VLM evaluation science)

**Reading of the ledger.**
- Holds:
  - A3: the 20-step comparison uses three runs, which is better than most agent papers.
  - A9: configs are given.
- Discounts:
  - A5: three single-run points, and the 0% point is the stage2-only model, so compute varies with data.
  - A11: per P2, the gain is within about one run's spread of the best 20-step run.
- Grades:
  - R1: major. It is the central confound: Stage 1 adds ≈1,920 H100-h and grounding data.
  - R5: major. "True test-time scaling" and the subgoal-decomposition mechanism rest on one run and ~6 tasks.
  - R8: major. There is no ablation of the GPT-5 monologues, which may carry much of the signal.
  - R6: minor.
  - R7: minor (unsettled).
  - R9: minor. The inconsistencies are many but individually small; none changes a headline.
  - R12: minor (for rigor).
  - R14: minor.

**Opinion.** Mechanically, the experiments are honest, and the three-run protocol at 20 steps is a plus. But the design cannot attribute the gain to the thing the title names. Stage 1 differs from no Stage 1 in data, compute and grounding pairs at once, and the scaling ablation shares the same 0% anchor. Section 4.2 then turns a single-run +1.65 pt into a causal story about planning that is never tested. I would expect the gain to shrink, not vanish, under a matched control. As written, it supports "continued pretraining with this mixture helps", not "videos are high-quality supervision". A matched-token control and 3-seed 50-step runs would move me up a full point.

Decisive: R1 (major), R5 (major), R8 (major), A3 (strong)

**Scores.** Pool position 42 (basis: R1, R5, R8). Technical Rigor 44, Clarity 58, Novelty 52, Significance 52, Experimental Validation 45, Reproducibility 50, Ethics 56. Overall 3. Confidence 4. *(The composite of 49.8 maps to 2. I keep Overall 3 because A3 is a real, replicated effect and the flaws are fixable by added controls rather than invalidating.)*

### T3: Temporal action localization / video grounding researcher (technical_rigor; video understanding)

**Reading of the ledger.**
- Holds:
  - A7: a held-out 23 h test set with per-type numbers is the right start.
  - A6: the detect-then-parameterize decomposition is reasonable.
- Discounts:
  - A2: scale says nothing about label quality, given R3.
- Grades:
  - R3: major. With ~34% of sampled actions judged wrong under a lenient criterion, and no exact-coordinate evaluation even though OpenCUA logs provide exact labels, label quality is unknown where it matters.
  - R4: major. "Millisecond-precision" at 4 fps with a 0.5 s temporal patch, scored by any-overlap matching, is a claim the evaluation cannot support.
  - R16: minor.
  - R17: minor.
  - R9: minor. The Table 1 total typo is visible to a localization reader.
  - R10: minor.

**Opinion.** As temporal localization, Video2Action is evaluated with a hit criterion that the localization community would not accept as evidence of "tight boundaries". Any overlap counts, and there is no tIoU threshold or boundary error. The parameterizer, which produces the coordinates the agent learns to click, is checked only by human plausibility on 500 samples. That is odd, because the training source has exact logs that could serve as a held-out test with pixel error. The press and drag numbers (recall 0.08, accuracy ~0.36) show real limits that the abstract's "high fidelity" hides. Downstream gains suggest the labels are usable, but the paper cannot say how noisy they are. Standard tIoU-based metrics and an exact-parameter evaluation would address my concerns.

Decisive: R3 (major), R4 (major), A7 (moderate)

**Scores.** Pool position 47 (basis: R3, R4 vs A7). Technical Rigor 46, Clarity 58, Novelty 54, Significance 55, Experimental Validation 50, Reproducibility 52, Ethics 58. Overall 3. Confidence 3.

### T4: Learning-from-observation / inverse-dynamics researcher (novelty; robotics / imitation from observation)

**Reading of the ledger.**
- Holds:
  - A6: the transfer is disclosed (VPT cited, robotics IDM cited), and GUI videos need a parameter extractor that VPT's keyboard/mouse IDM did not need in this form.
  - A2: the scale of the transfer.
- Discounts:
  - A11: the "planning" insight is not shown (P2).
- Grades:
  - R13: major. The recipe is VPT's: train an IDM on a small logged set, label web video, pretrain, fine-tune. Tutorial mining for agents also exists in the paper's own related work. The delta is a new domain plus a two-stage IDM, and it is not compared empirically with prior mining pipelines.
  - R8: major. The one question this line of work most needs answered here, how IDM quality translates into policy quality, is not studied.
  - R3: minor (for novelty).
  - R5: minor.

**Contribution check.**
1. What does a reader learn? That VPT-style auto-labelling works for desktop GUIs and gives +4.8 pt on OSWorld over SFT-only. Given VPT and AgentTrek, that is a confirmation more than a surprise. The why (which part of the signal helps) is missing (R8).
2. Does the setting support the framing? "Web scale" is backed by 39k videos and 26B tokens. "High-quality supervision" is not backed (R3, R4).
3. Is the delta conceptual or a refinement? A refinement and transfer of VPT's IDM paradigm and of tutorial-based trajectory mining (AgentTrek; Jang et al. 2025) (R13).
4. Would the conclusions transfer? Unknown beyond a 7B Qwen2.5-VL with modest SFT (R15).

Questions 1 and 3 fail, and no accept reason shows a specific new insight, so novelty sits in the lower half.

**Opinion.** I like the engineering, and the transfer is honestly attributed. But for a venue weighting novelty, the paper needs to give the field something VPT did not: a finding about IDM noise vs policy gains, about which action types benefit, or about why the termination behaviour degrades (Table 5). Without that, it is a well-executed domain transfer. A study varying IDM quality, and a head-to-head with prior tutorial-mining data, would raise my novelty view.

Decisive: R13 (major), R8 (major), A6 (moderate)

**Scores.** Pool position 46 (basis: R13, R8 vs A6). Technical Rigor 52, Clarity 62, Novelty 46, Significance 52, Experimental Validation 50, Reproducibility 54, Ethics 58. Overall 3. Confidence 4.

### T5: Multimodal foundation-model data and scaling researcher (significance; MLLM pretraining and data curation)

**Reading of the ledger.**
- Holds:
  - A1: the right problem.
  - A2: a big, long-horizon corpus.
  - A3: a replicated gain.
  - A10: tool release is useful.
- Discounts (after P11):
  - A5: it no longer isolates video data.
- Grades:
  - R15: major. One 7B base model and 15.8% absolute: whether the benefit survives stronger SFT mixtures or RL is the significance question, and it is untested.
  - R12: major. Without a committed release of the mined data (or video IDs), the community cannot use the main resource. Only the tools are promised.
  - R1: major (updated after P11, was minor).
  - R6: minor.
  - R11: minor (for significance).

**Contribution check.**
1. The reader learns that mined tutorial actions can be a useful pretraining signal for CUAs, with a positive data trend. This is a modest but real insight.
2. "Web scale" holds for the data. The agent results are at one scale.
3. A transfer and refinement (shared with T4's view, R13).
4. Transfer to production-scale agents is unknown (R15).

**Opinion.** This is the kind of data pipeline the field needs, and I initially read Fig. 6 as clean evidence that more mined video gives more capability. P11 shows that the 0% point is simply the stage2-only model, so the first half of the curve also adds grounding pairs and compute. Only the 50% → 100% step (+2.4 OSWorld, single run; +1.2 AgentNetBench) varies video tokens alone, and it still doubles compute. Combined with the low absolute numbers and no committed data release, the significance is real but modest. A released corpus and a second, stronger base model would make this a clear accept from my perspective.

Decisive: A1 (strong), A2 (strong), R1 (major), R15 (major)

**Scores (updated after P11).** Pool position 57 (basis: A1, A2 vs R1, R15). Technical Rigor 54, Clarity 62, Novelty 56, Significance 60, Experimental Validation 54, Reproducibility 55, Ethics 56. Overall 3. Confidence 4.
*Before P11: R1 minor; pool position 66; TR 60, Cl 64, Nov 60, Sig 68, EV 62, Rep 56, Eth 58; Overall 4.*

### T6: Data governance and privacy researcher (ethics; responsible web-scale data collection)

**Reading of the ledger.**
- Holds:
  - A1: public tutorials are a reasonable source in principle.
  - A14: some limitations are acknowledged.
- Grades:
  - R11: major. The pipeline explicitly extracts typed text from third-party screen recordings, and the paper's own training example (Fig. 9) types a string that looks like a password ("lilybloom123."). Yet there is no ethics statement, no description of the "license/PII checks", and no word on YouTube's terms or creator consent.
  - R12: minor (for ethics). Release terms are unstated.
  - R10: minor. Selection from 55,603 to 39,000 videos is undocumented.

**Opinion.** Learning from public tutorials is defensible, but a paper that scrapes 55k videos and extracts keystrokes needs to document what it does with credentials, e-mail addresses and names visible on screen, and under what licence it will release data. One appendix line is not documentation. These are fixable with an ethics statement and a scrubbing description, so I do not consider this fatal. It does lower the paper's standing at a venue that asks for responsible-data reporting.

Decisive: R11 (major), A1 (strong)

**Scores.** Pool position 46 (basis: R11). Technical Rigor 54, Clarity 60, Novelty 54, Significance 56, Experimental Validation 52, Reproducibility 46, Ethics 40. Overall 3. Confidence 3.

### Settling factual splits

The split on R1: T1 and T2 graded it major, T5 minor. T5's grade rested on a fact, namely whether the Fig. 6 ablation isolates video data.

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P11 | T5 (minor) vs T1, T2 (major) on R1 | Does Fig. 6 hold the grounding pairs and compute fixed while varying video tokens? | **partly**. Sec. 4.1 varies "0%, 50%, and 100% of the video tokens", but the 0% point (64.1 / 9.3) equals the stage2-only model (Fig. 5, Table 4), so 0 → 50% also adds Stage 1, its grounding pairs and compute. Only 50 → 100% varies video alone, and compute changes with it. Whether the grounding pairs are held fixed across 50% and 100% is not stated | T5: R1 minor → major (logged "updated after P11: minor → major"). R1 is among T5's decisive items, so T5's scores were updated: pool 66 → 57, Overall 4 → 3. A5 moderate → weak |

Remaining splits rest on values. T3 grades R3 major and T1/T4 minor, because they weigh label accuracy against downstream gains differently. T1/T5 grade R15 major, while the others do not name it.

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 Computer-use / GUI agent specialist | experimental_validation | 0.235 | 45 | 3 | 4 |
| T2 Training and evaluation methodologist | technical_rigor | 0.141 | 42 | 3 | 4 |
| T3 Temporal localization researcher | technical_rigor | 0.141 | 47 | 3 | 3 |
| T4 Learning-from-observation researcher | novelty | 0.194 | 46 | 3 | 4 |
| T5 Multimodal data and scaling researcher | significance | 0.194 | 57 | 3 | 4 |
| T6 Data governance and privacy researcher | ethics | 0.094 | 46 | 3 | 3 |

- **Aspect-weighted rating:** 3.00 → **final rating 3 (Borderline Reject)**. The ICLR label is "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})", with scale status *secondary*: recent forms use this scale, so verify it against the current form. ICLR sub-scores: Soundness 2, Presentation 2, Contribution 2.
- Weighted pool position 47.5; plain mean 3.00; spread 0 (all types 3 after P11; before P11, T5 gave 4).
- Uncovered aspects and warnings: none. Clarity (10%) and reproducibility (9%) have no type of their own and are renormalized away by the script. T2's composite (49.8) maps to 2 against an Overall of 3; the gap is explained in T2's review.

<details><summary>Aggregation output</summary>

```
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Computer-use / GUI agent specialist) | experimental_validation | 19% | 0.235 |
| T2 (Training and evaluation methodologist for VLM agents) | technical_rigor | 23% | 0.141 |
| T3 (Temporal action localization / video grounding researcher) | technical_rigor | 23% | 0.141 |
| T4 (Learning-from-observation / inverse-dynamics researcher from robotics) | novelty | 16% | 0.194 |
| T5 (Multimodal foundation-model data and scaling researcher) | significance | 16% | 0.194 |
| T6 (Data governance and privacy researcher) | ethics | 8% | 0.094 |

**Final rating (aspect-weighted mean)**: **3.00** → **3 (Borderline Reject)** · plain mean 3.00 · weighted pool position 47.5

| Venue | Venue-weighted composite | Band | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|
| ICLR (2026) | 52.5 | 3 → 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) | Soundness 2, Presentation 2, Contribution 2 | secondary |

Dimension means (official): TR 50.0, Clarity 60.0, Novelty 52.3, Significance 55.0, Exp. Val. 49.2, Repro 51.5, Ethics 54.0; composite 52.5.
```

Full output: `aggregate.json` and `before.json` in this directory.

</details>

This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R1 | 3 of 6 | T1 major, T2 major, T5 major (updated after P11, was minor) |
| R8 | 3 of 6 | T1 major, T2 major, T4 major |
| R15 | 2 of 6 | T1 major, T5 major |
| R3 | 3 of 6 | T3 major, T1 minor, T4 minor (values split) |
| R5 | 3 of 6 | T2 major, T1 minor, T4 minor (values split) |
| R2 | 1 of 6 | T1 major |
| R4 | 1 of 6 | T3 major |
| R13 | 1 of 6 | T4 major |
| R11 | 2 of 6 | T6 major, T5 minor |
| R12 | 3 of 6 | T5 major, T2 minor, T6 minor |
| R6 | 3 of 6 | T1, T2, T5 minor |
| R7 | 2 of 6 | T1, T2 minor (capped: unsettled question) |
| R9 | 3 of 6 | T1, T2, T3 minor |
| R14 | 2 of 6 | T1, T2 minor |
| R10 | 2 of 6 | T3, T6 minor |
| R16, R17 | 1 of 6 | T3 minor |
| A1 | 3 of 6 | held by T1, T5, T6 |
| A2 | 4 of 6 | held by T1, T4, T5; discounted by T3 |
| A3 | 3 of 6 | held by T1, T2, T5 |
| A5 | 3 of 6 | discounted by T1, T2, T5 |
| A6 | 2 of 6 | held by T3, T4 |
| A11 | 3 of 6 | discounted by T1, T2, T4 |
| A7 | 1 of 6 | held by T3 |
| A9 | 1 of 6 | held by T2 |
| A4, A8, A12, A13 | 1 of 6 | held by T1 |
| A10 | 1 of 6 | held by T5 |
| A14 | 1 of 6 | held by T6 |

### Key strengths

- A2: a large mined corpus (39k videos, 1.52M steps, avg 39.25 steps per trajectory). Held by 3 of 6 types.
- A3: a replicated OSWorld-Verified gain over the same model without Stage 1 (non-overlapping 3-run ranges, Table 4). Held by 3 of 6.
- A1: a real bottleneck addressed with an abundant source. Held by 3 of 6.
- A6: a disclosed, sensible transfer of inverse dynamics to GUIs. Held by 2 of 6.

### Top concerns (at most five)

1. R1: the main comparison is confounded by Stage-1 compute (~1,920 H100-h) and OSWorld-G grounding pairs that the SFT-only baseline does not get. The scaling ablation shares the same 0% anchor (Sec. 2.3.1–2.3.2; Fig. 6; P1, P11). Fix: matched-token Stage-1 controls (grounding only; human or synthetic trajectories; frames + ASR without actions), ~2k H100-h each.
2. R8: no ablation of the monologue, ScreenFilter, IDM label quality, or action labels vs raw frames (Sec. 4). Fix: component ablations at a reduced Stage-1 budget, ~1–2k H100-h.
3. R15: low absolute performance (15.8%) with a single 7B base model and no evidence the gain persists with stronger recipes (Abstract; Fig. 5). Fix: a second base model or a stronger SFT mixture.
4. R2: no external agents or alternative data sources are compared (Fig. 5; Table 4; P6). Fix: a table of published 7B agents under the same OSWorld-Verified protocol, plus a synthetic-trajectory Stage 1 at equal tokens.
5. R3: action parameters are validated only by lenient manual plausibility (0.658 overall; drag/press ~0.36), not against the exact held-out logs that exist (Sec. 2.2.2; Table 2; P3). Fix: pixel-error and exact-match evaluation on held-out OpenCUA clips, plus a trajectory audit.

### Revision Roadmap

Priority 1 holds the reasons graded major by at least 3 of 6 types (no type graded any reason fatal).

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R1 | Matched-token Stage-1 controls; state whether grounding pairs are in every Fig. 6 variant | ~2k H100-h per control |
| 1 | R8 | Ablate the monologue, ScreenFilter, label noise, and action labels vs frames only | ~1–2k H100-h total at a reduced budget |
| 2 | R2 | Published 7B agents and a synthetic-data Stage 1 under the same protocol | 1–2 weeks of evaluation and compute |
| 2 | R3 | Exact-parameter evaluation on held-out OpenCUA logs; trajectory audit | days |
| 2 | R4 | Boundary-error / tIoU metrics, or drop "millisecond-precision" and "high fidelity" | low |
| 2 | R5 | 3+ runs at 50 (and 100) steps for both models; trajectory analysis, or soften Sec. 4.2 | ~2–3 days of OSWorld runs |
| 2 | R11 | Ethics statement; PII and credential scrubbing; licence and release terms | low |
| 2 | R12 | Full hyperparameters; commit to a dataset or video-ID release | low |
| 2 | R13 | Positioning against, and ideally an empirical comparison with, prior tutorial/video mining | moderate |
| 2 | R15 | A second base model or a stronger SFT baseline | substantial |
| 3 | R6, R14 | Extra scaling points and variance; AgentNetBench variance; discuss the terminate regression | moderate |
| 3 | R7 | Overlap check of tutorials and Stage-2 data against the benchmarks (unsettled question) | low |
| 3 | R9, R10, R16, R17 | Correct the table totals and shares; clarify stage-1 format and video selection; fix the App. D and Fig. 10 references; report manual-review protocol; unify the action taxonomy | trivial–low |

---

## 8. Integrity signals and limitations

- **Integrity signals:** none found. `integrity_scan.py --redact` reported no reviewer-directed text or hidden characters, and none was seen while reading. The only redaction is a venue/acceptance mark inside the ReAct reference entry, which is not an instruction. The numerical inconsistencies in R9 look like transcription slips (e.g., a 1,000 offset in the Table 1 total), not signs of fabrication; they are noted for the authors only.
- **Limitations:**
  - The review used extracted text without figures. Fig. 6 values come from the text, and the loss curves (Figs. 8, 11, 12) and qualitative examples were not seen. E9 figure integrity was not checked.
  - The literature check did not run (no network). Statements about prior work (Jang et al. 2025; AgentTrek; OpenCUA/Aguvis/UI-TARS results) rest on what the paper cites and are marked [verify] where positioning matters.
  - No reference is recommended as missing.
  - The types share one context, so their agreement is not independent confirmation.
  - The reviewer recognized the paper's title from prior knowledge. It was reviewed on the manuscript alone, without using any knowledge of its reception or outcome.
