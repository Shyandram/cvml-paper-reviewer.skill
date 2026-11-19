# Academic Paper Review: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos

*Simulated panel review (full mode), target venue ICLR, literature check strict (cutoff 2025-09-24). Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction. All five reviewers and the EIC are fictional personas; the five reports were produced in five separate role passes that share one model context (no independent agents ran). Figures were not available: figure-dependent claims are judged from captions and text only (Figures 1–6, 8, 11, 12 and the loss curves / learning rates inside them are unverified).*

---

## Phase 0: Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos |
| Primary Discipline | Machine learning → GUI / computer-use agents (data-centric pretraining) |
| Secondary Discipline(s) | Computer vision (temporal event detection, video VLMs); imitation learning from observation (inverse dynamics) |
| Paper Type | Empirical (composite weights: empirical). It also has System/Dataset flavour (pipeline + 1.52M-step corpus), but the central evidence is a method-style benchmark comparison, so the default empirical weights apply. |
| Core Technique(s) | Qwen2.5-VL-7B fine-tuned as a dense event detector and an action parameterizer (inverse dynamics); YOLOv8x cursor filter (ScreenFilter); GPT-5 / GPT-4.1 for inner monologues and video classification; two-stage continued pretraining + SFT |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (ICLR form: Soundness, Presentation, Contribution, Rating, Confidence) |
| Paper Maturity | Submission-ready draft with visible editing slips (cross-references, appendix labels) |
| Ethics-Relevant Content | Web-scraped YouTube videos (copyright / terms of service, creator consent); on-screen personal data and typed text (PII, possible credentials); no limitations or broader-impact section |

**Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters found. The reviewers read the (identical) redacted copy.

**Literature check:** mode strict; 6 queries (3 claim, 1 benchmark/baseline, 2 expansion) plus 4 title verifications; `similarity`, `scout` and `novelty` run; `coverage` not run (budget spent on verification instead). Gaps left open: no dedicated query for AgentNetBench (no hits expected: it is introduced in a cited paper); the search covers arXiv only.

### Claimed Contributions (as stated by the authors; claim IDs used throughout)
- **C1** (method/resource): VideoAgentTrek, "an unsupervised approach to training computer-use agents" that mines trajectories from unlabeled screen-recorded videos "eliminating the need for manual annotation" (Abstract, §1 bullet 1); 1.52M steps from 39,000 YouTube videos (§2.3.1).
- **C2** (method): Video2Action, an inverse dynamics module with dense action-event detection and action parameterization, with "millisecond-precision temporal localization" and "high fidelity" parameter extraction (Abstract, §1 bullet 2, §2.2).
- **C3** (result): continued pretraining + SFT lifts OSWorld-Verified from 9.3% to 15.8% ("70% relative") and AgentNetBench step accuracy from 64.1% to 69.3% (Abstract, §1 bullet 3, §3.1, Fig. 5).
- **C4** (claims of mechanism/scaling): consistent data scaling (§4.1, Fig. 6), improved long-horizon planning and "true test-time scaling" (§3.1.2, §4.2).
- **C5** (resource): open-source release of ScreenFilter and Video2Action (§1 bullet 4); promised, not available for review.

### Paper memory (factual record shared with all reviewers)
- **Splits / setup:** Base Qwen2.5-VL-7B-Instruct (§2.3.2). Stage 1: one epoch over 26B tokens of mined trajectories plus a small number of grounding pairs; 32× H100, ~60 h, global batch 512, 6,500 iterations (Fig. 11). Stage 2: 8B tokens of human-annotated trajectories (OpenCUA, AGUVIS), 64× H100, ~16 h, 3,000 iterations (Fig. 12). Grounding pairs from OSWorld-G, ~1B tokens (§2.3.1). Event detector: 154 h of OpenCUA video with logs (App. C); parameterizer: "512,000 screen-capture clips" (App. D); detector test set: 23 h, 20,282 events, source not stated (§3.2.1). Parameterizer evaluated by manual review of 500 in-the-wild predictions (§3.2.2). ScreenFilter: 15,000 synthetic images, F1 89.58% (App. B).
- **Evaluation:** OSWorld-Verified, 20-step budget: three runs, average reported; 50-step budget: single run (App. G). AgentNetBench: 100 tasks, offline step success (§3.1.1). Learning rates, optimizer, seeds: not stated in the extracted text (may sit in unavailable Figs. 8, 11, 12).
- **Data:** 55,603 videos from "50+ channels", ~10,000 h → 7,377 h after ScreenFilter (§2.1.1–2.1.3, App. H); 39,000 videos processed, ~39 steps each, ~26B tokens (§2.3.1); how 39,000 of 55,603 were chosen is not stated.
- **Headline numbers:** 9.3→15.8 OSWorld-Verified (Abstract; Fig. 5; Table 4: 9.27 vs 15.78 at 50 steps, 9.3 vs 14.13 at 20 steps); 64.1→69.3 AgentNetBench (Table 5: 0.641 / 0.693); base 4.5 / 38.5.
- **Appendix adds:** prompt for monologues (App. E), data formats (Figs. 9–10), full per-app OSWorld counts (Table 4), per-action AgentNetBench (Table 5), corpus statistics (Tables 6–10).
- **Unverifiable:** all figures; hyperparameters inside figures.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Marguerite Okonkwo-Lindqvist, large public research university (Northern Europe)
- **Seniority / Expertise**: senior faculty / agent learning from demonstrations, evaluation of foundation-model agents
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what the venue actually accepts; weights reviewers by what they got right.

### Reviewer 1 (Methodology): Dr. Anh-Khoa Vuong, industrial research lab (Southeast Asia)
- **Seniority / Expertise**: mid-career industry scientist / VLM post-training, OSWorld-style online agent evaluation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on token- and compute-matched controls; recomputes every table.

### Reviewer 2 (Domain): Prof. Leandro Castellanos-Ruiz, large public university (South America)
- **Seniority / Expertise**: senior faculty / GUI agent data synthesis, imitation from observation (VPT-style inverse dynamics)
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work against the actual abstracts; asks for delta tables.

### Reviewer 3 (Perspective): Dr. Siobhan Adeyemi-Park, human–computer interaction group, research institute (West Africa / North America)
- **Seniority / Expertise**: mid-career / HCI, robotic process automation and workflow mining, privacy of screen data
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for what the work could become.

### Reviewer 4 (Generalist): Dr. Hana Lindgren-Oyelaran, university lab (Central Europe)
- **Seniority / Expertise**: postdoc-to-early-faculty / multimodal learning and video understanding (not agents)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical programme-committee member; weighs weaknesses against accepted-paper norms.

### Devil's Advocate: Dr. Rafael Bjornsson-Haddad, independent evaluation-methodology researcher (Iceland)
- **Seniority / Expertise**: senior researcher / causal attribution in ML experiments, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reports

# Peer Review Report (Reviewer 1: Methodology)

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Reviewer: Dr. Anh-Khoa Vuong, Methodology (industrial research lab; fictional persona)
## Expertise: VLM post-training; online computer-use agent evaluation; data-scaling ablations
## Date: 2026-11-10

### Summary
The paper builds a pipeline that crawls screen-recorded tutorials from YouTube, filters them with a cursor detector, recovers timestamped actions with two Qwen2.5-VL-7B models (event detection, parameterization), adds GPT-5-written inner monologues, and yields ~1.52M steps / 26B tokens. A Qwen2.5-VL-7B agent is first trained on these tokens (Stage 1) and then on 8B tokens of human trajectories (Stage 2). Compared with Stage 2 only, success on OSWorld-Verified rises from 9.3% to 14.13% (20 steps) / 15.78% (50 steps), and AgentNetBench step accuracy from 64.1% to 69.3%.

### Protocol sweep
Searched the full text for split/selection statements. **Found:** "For the 20-step budget, we conduct three independent runs per model and report the average Task SR. For the 50-step budget, we perform a single run." (App. G). The detector test set is "a held-out" 23 h set (§3.2.1) with no source stated. **Not stated after search:** whether the 100 AgentNetBench tasks (built from the AgentNet dataset, §3.1.1) are excluded from the OpenCUA/AgentNet logs used to train the detector, the parameterizer and Stage 2; no checkpoint or hyperparameter selection on a reported split is described (no "selected / best / tuned" statements about evaluation).

### Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | "unsupervised", "eliminating the need for manual annotation" | Abstract, §1 | IDM trained on 154 h of human-logged OpenCUA video (App. C); Stage 2 is "human-annotated" (§2.3.2) | Partially supported (the *video corpus* is unlabeled; the pipeline and recipe still rest on human labels and proprietary LLMs) |
| C2 | accurate extraction, "millisecond-precision", "high fidelity" | Abstract, §1 | Table 1 (overlap-based P/R), Table 2 (65.8% manual accuracy) | Partially supported / precision claim unsupported |
| C3 | 9.3→15.8 OSWorld-Verified; 64.1→69.3 AgentNetBench | Abstract, Fig. 5, Tables 4–5 | Table 4 (3 runs at 20 steps), Table 5 | Supported as a measured gain over the authors' own Stage-2-only model; attribution to *video-derived* supervision not isolated |
| C4a | "clear relationship" between data size and performance | §4.1 | Fig. 6: three points, single runs | Partially supported |
| C4b | "true test-time scaling", teaches "decompose complex tasks into subgoals" | §3.1.2, §4.2 | 14.13 (mean of 3) → 15.78 (one run); no analysis of subgoals | Mechanism unsupported |

### Weaknesses

**W1 (most severe). The headline gain is not isolated to video-mined supervision.** Stage 1 adds 26B video tokens plus ~1B grounding tokens (§2.3.1–2.3.2), while "stage2 only" sees 8B tokens (§2.3.2, Fig. 12). The "SFT-only baseline" therefore differs from the full model in tokens, compute (Stage 1 alone is ~32 GPUs × 60 h ≈ 1,920 GPU-h, Fig. 11), data type (GPT-5-written reasoning text, §2.2.3) and domain exposure at the same time. No control uses an equal budget of another source (for example the same 8B human tokens repeated to a matched count, or tutorial-derived data produced by a simpler non-IDM pipeline). Without it, §4.1 shows that *more tokens help*, not that *video supervision* helps, and the title claim ("Pretraining from Unlabeled Videos") is untested against "more in-domain GUI tokens". **Fix:** one token-matched control (≈1,920 + 1,024 GPU-h from Figs. 11–12), plus an ablation that removes or replaces the GPT-5 monologues (the thoughts are the part most plausibly distilled from a stronger model).

**W2. Label quality is measured in ways that cannot support the precision claims.** (i) A detection is a hit if "its interval has any temporal overlap with a ground-truth event" (§3.2.1), so no boundary error is measured, although the contributions claim "millisecond-precision temporal localization" (§1) and "tight" bounds (§2.2.1). (ii) Parameterization has no automatic metric: "Because ground-truth object boxes are unavailable, we evaluate only on unseen web tutorials via blinded manual review" (§2.2.2), yet OpenCUA logs contain click coordinates and typed text and could give a pixel-error / exact-match score on held-out logs. (iii) The manual review uses a plausibility criterion ("plausibly produce the observed on-screen transition", §3.2.2) on 500 samples, and still gives 65.8% overall, 71.3% for click, 36.6% drag, 36.2% press (Table 2). (iv) Recall is 0.70 overall and 0.08 for `press` (Table 1), so roughly 30% of actions are missing from each trajectory. About a third of parameter labels are wrong and a third of steps are absent, yet the abstract says "high fidelity", and the paper does not study how this noise affects training (no filtered-subset ablation). **Fix:** held-out pixel-error and exact-match metrics, IoU-based boundary scores, and a training run on the highest-confidence subset (~1 Stage-1 run on a 25% subset ≈ 500 GPU-h).

**W3. Statistical reliability of the claims about long horizons and scaling.** The 50-step results are single runs (App. G). The "test-time scaling" claim rests on 15.78% (one run) vs 14.13% (mean of runs ranging 13.57–14.68, Table 4): +1.65 points, about 6 of ~361 tasks, and 1.1 points above the best 20-step run. The data-scaling curve (Fig. 6) is three single-run points; the second step is small on AgentNetBench (+4.0 then +1.2). The 20-step effect itself is robust: Stage-2-only 9.13–9.42 vs 13.57–14.68 across three runs. **Fix:** three runs at 50 steps for both models and for the 50% variant (OSWorld-Verified evaluation only; no retraining).

**W4. No external reference point.** The only comparison is the authors' own Stage-2-only model (9.3%). The paper cites OpenCUA, AGUVIS and UI-TARS (§1, §2.3) and uses their human data, but reports no number for their released 7B-scale agents on the same benchmarks, nor any other benchmark (e.g., an offline grounding or mobile benchmark, although §2.3.1 claims the grounding data "strengthen pointer–target alignment" and App. G that pretraining "notably strengthens grounding"). It is therefore unclear whether 15.8% is competitive or whether the Stage-2-only baseline is simply weak. **Fix:** add the published numbers of comparable open agents (stating budget and setting), and one grounding benchmark.

**W5. Reporting inconsistencies that affect trust in the tables** (see Error Log): Table 1 total predictions, Table 4 denominators, Stage-2-only 50-step value, Table 8 and Table 6 totals.

**W6. Selective reading of Table 5.** The text says pretraining "notably strengthens grounding and multi-action control" (App. G), but `terminate` accuracy falls from 0.588 (stage2 only) to 0.237 (stage1+2) and `scroll` (0.600) is below the base model (0.615). Termination accuracy matters for online success; the regression is not discussed. **Fix:** report and discuss, e.g., whether Stage 1 teaches the agent never to stop.

**Minor:** text says recall 0.71 (§3.2.1) vs Table 1 0.70; Fig. 6 shows 15.7 vs 15.78/15.8 elsewhere; §3.1.2 says "(see Section 4.1)" for the flat SFT-only curve, which is in §4.2; §4.2 cites "Figure 10" for the step histogram, which is "Table 10"; App. D calls the parameterizer a "dense detector"; Fig. 1 label "Agent Traing"; "AgentNetBench is an offline benchmark is based on".

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E1 | Table 1, "Total" row | "Total 17,298" | Preds rows: 12,222+971+177+1,448+1,480 = 16,298; GT column sums to 20,282 correctly; micro-precision on 16,298 is 0.874 (0.87), not 0.88 | Recomputed sums, and TP = P×Preds per row (sum 14,247 → recall 0.7025 ✓) | High | MINOR | Correct total and precision |
| ERR-2 | E6 | Table 4 headers vs §3.1.1 | "includes 369 human-crafted Ubuntu desktop tasks" | Header denominators sum to 359 (46+46+26+23+23+15+24+47+92+17); reported rates match 361 (e.g., 53/361 = 14.68%, 57/361 = 15.79%), so the evaluated task set is unclear | Recomputed | High | MINOR | State the exact task list (e.g., exclusions) |
| ERR-3 | E1 | Table 4 vs Fig. 5 / App. G | "stage2 only" turn4 (50): 9.27 | Row counts sum to 33 solved tasks (1+12+2+3+2+2+2+4+4+1); 33 gives 9.14% (/361), 9.19% (/359), 8.94% (/369), never 9.27 | Recomputed | High | MINOR | Correct the count or the rate |
| ERR-4 | E1 | Table 8 | "Total 1,547,092" | Rows sum to 1,560,464; the text elsewhere gives "approximately 1.52 million" (39,000 × 39) | Recomputed | High | MINOR | Reconcile the three totals |
| ERR-5 | E1 | Table 6 | "High (1080p+) 2,322 / Standard 49,589 / Low 1,464" | Sums to 53,375, not the 55,603 videos stated in App. H; "97% are 720p or higher" matches 53,375 (97.3%), not 55,603 (93.4%) | Recomputed | High | MINOR | Explain the 2,228 missing videos |
| ERR-6 | E5 | §1 bullet 2 vs §3.2.1 | "millisecond-precision temporal localization" | Evaluation counts any temporal overlap as a hit; no boundary error reported | Cross-referenced two locations | High | MAJOR | Report boundary error or soften the claim |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central causal claim (video-derived supervision, not extra tokens, drives the gain) is confounded, with no external baselines and weakly validated labels, which are signals of a typical rejected submission; offset by a large, three-run-robust gain on OSWorld-Verified and real engineering scale.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Sound pipeline; attribution confound, lenient metrics, table errors |
| Clarity & Presentation | 60 | Competent | Readable method; many cross-reference and labeling slips |
| Novelty & Originality | 55 | Competent | See R2 |
| Significance & Impact | 58 | Competent | Useful if the data effect is isolated |
| Experimental Validation | 48 | Developing | Two benchmarks, one base model, own baseline only, no matched control |
| Reproducibility | 56 | Competent | Hardware/iterations stated; LR/optimizer unverified (figures); data-selection steps unclear; release promised only |
| Ethical Compliance | 55 | Competent | Licensing/PII mentioned in one sentence only |

### NeurIPS-style: Quality 2, Clarity 2, Significance 2, Originality 2.

### Questions for Authors
1. Is there a token-matched control with non-video data? An answer showing Stage-1 video data beats an equal-token control would move me to Overall 4.
2. Were the 100 AgentNetBench tasks (or their source trajectories) excluded from the IDM training logs and Stage 2 data? A "no" would change Experimental Validation substantially.
3. What is the held-out pixel error of click coordinates and the exact-match rate for typed text on OpenCUA logs?
4. How were 39,000 of the 55,603 downloaded videos chosen, and what is the exact OSWorld-Verified task list behind Table 4?
5. Why does `terminate` accuracy drop from 0.588 to 0.237 (Table 5)?

### Limitations Assessment: **No.** There is no limitations section; label noise (§2.3.2 mentions "residual noise" once) and OS mismatch (videos vs Ubuntu OSWorld) are not discussed.
### Ethics Review Flag: **No** (from my angle; see R3).
### Overall: **3 (Borderline Reject)**. A promising data recipe whose central causal claim is not isolated and whose label quality is weakly measured.
### Confidence: **4**

---

# Peer Review Report (Reviewer 2: Domain)

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Reviewer: Prof. Leandro Castellanos-Ruiz, Domain (large public university; fictional persona)
## Expertise: GUI-agent trajectory synthesis; imitation from observation
## Date: 2026-11-10

### Summary
The paper applies the VPT recipe (an inverse-dynamics model labels unlabeled video, then behaviour cloning) to desktop screen-recorded tutorials. The IDM is a fine-tuned video VLM that outputs typed action spans and their parameters; a proprietary LLM adds rationales. The mined corpus is used for continued pretraining of a 7B VLM before SFT, improving OSWorld-Verified and AgentNetBench.

### Strengths
**S1: Right problem, right moment.** Trajectory scarcity is the acknowledged bottleneck for computer-use agents (§1), and tutorial video is an under-used source. Converting it with a learned IDM rather than replay or LLM-guessing is a natural and defensible extension of VPT (Baker et al., 2022; §5).
**S2: Scale and engineering.** 55,603 videos, 7,377 verified GUI hours (§2.1.2), 26B tokens, detector precision 0.88 for click/scroll (Table 1) is a substantial pipeline; the ScreenFilter details (App. B) are useful.
**S3: Honest breakdowns.** Per-application OSWorld counts over three runs (Table 4) and per-action AgentNetBench (Table 5) let readers see where the gain occurs (chrome, thunderbird, writer).
**S4: Principled structure.** Separating event detection from parameterization, and conditioning the latter on the former (§2.2.2), is sensible.

### Weaknesses
**W1. Closest prior work is missing and positioning is thin.** §5 has three short paragraphs. A verified, peer-reviewed prior work that also turns web tutorials, *including videos*, into GUI trajectories for training generalized GUI agents (TongUI; arXiv Apr 2025, AAAI 2026 per the search record) is not cited, while AgentTrek and Jang et al. (2025) are. The related-work statement that web-scale mining "typically lacks precise temporal boundaries or action parameters (Xu et al., 2025a; Jang et al., 2025)" is not substantiated, and I could not check Jang et al. against its abstract (a question, not a finding). Why it matters: the novelty of C1 hinges on the delta against tutorial-to-trajectory work. **Fix:** cite and differentiate TongUI, Synatra and the latent-action line (below); say what is gained over replay-based (AgentTrek) and LLM-extraction pipelines, ideally empirically.

**W2. Novelty is application-level.** The mechanism (IDM + behaviour cloning on web video) is VPT's; what is new is its instantiation for desktop GUIs with a VLM backbone, the detector/parameterizer split, and scale. This is respectable engineering but not a new concept; ICLR typically asks for an insight (why does video help, which parts of the pipeline matter). No component ablation (event detection vs parameterization quality; thoughts vs actions; ScreenFilter on/off) is given.

**W3. Alternatives to a supervised IDM are not discussed.** Latent-action methods learn actions from video without any action labels (cited only as Ye et al. 2025 in §5); the paper trains its IDM on 154 h of logged human data (App. C), so "unsupervised" (§1 bullet 1) is a terminology stretch that the Domain context makes visible: VPT's IDM also uses a small labelled set, but VPT states that explicitly.

**W4. Comparison with the field's open agents is absent.** OpenCUA, AGUVIS and UI-TARS are cited as sources of data/ideas but not as numerical reference points (see R1-W4). In the OSWorld literature, results are only comparable under stated budgets and observation settings; the paper gives its own (up to five screenshots, 20/50 steps, App. G) but no table against peers.

**W5. Claim calibration.** "hundreds of applications across Windows, macOS, and web platforms" (§1) is not supported by any application-level statistic (only six coarse categories from a GPT-4.1 title/transcript classifier, Fig. 3, App. H), and all videos come from "50+ channels" (§2.1.3). OSWorld is Ubuntu-only (§3.1.1); the OS composition of the mined videos is not given.

### Novelty claim profile (literature check, strict)
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 | method | medium | TongUI, level 3, https://arxiv.org/abs/2504.12679v4, prior (peer-reviewed), **not cited**; AgentTrek level 3, https://arxiv.org/abs/2412.09605v2, prior (peer-reviewed), cited | Both convert tutorials into trajectories; differences (learned IDM on screen video, 1.52M steps) are real but not argued |
| C2 | method | high (no close prior found in 6 queries; arXiv only, so at most medium in confidence) | TongUI, level 2 | VPT (cited) is the ancestor; no desktop-GUI VLM-IDM found |
| C3 | result | high | OSWorld, level 1 | Numbers are the paper's own |
Script reading: "no central claim fully covered by prior work". **Attribution:** closest to the whole paper is TongUI (cosine 0.17, shared 8-grams 0; no text overlap flagged). No integrity flag.

### Novelty delta table
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| Mining tutorials into trajectories (C1) | TongUI (arXiv 2504.12679) | Crawls GUI tutorials ("videos and articles") and processes them into trajectories for GUI agents (abstract) | Learned video IDM with timestamps; desktop screen recordings; larger step count | No (TongUI); AgentTrek cited, differentiated by one sentence in §5 |
| IDM on screen video (C2) | VPT (Baker et al., 2022) | IDM auto-labels unlabeled web video for behaviour cloning | VLM-based typed-span detection + parameterization for GUIs | Yes (§5), briefly |

### Baseline scout (OSWorld, success rate; kept results only)
| Benchmark | Prior method (link, label) | Reported number (abstract) | Compared? | Note |
|-----------|----------------------------|----------------------------|-----------|------|
| OSWorld | Agent S, arXiv 2410.08164, prior (arXiv-only, 6+ months) | "9.37%" absolute gain, 83.6% relative | No | Closed-model agentic framework: different setting, not a required baseline |
| OSWorld | Agent S2, arXiv 2504.00906, recent preprint | 18.9% / 32.7% relative gains at 15/50 steps | No | Worth discussing only |
| OSWorld | LiteCUA, arXiv 2505.18829, recent preprint | 14.66% | No | Different system (API-based), worth discussing only |
No under-reported baselines. The numbers of open 7B-scale agents (OpenCUA, UI-TARS, AGUVIS) are the relevant comparators; I give none from memory.

### Field snapshot
Three to five years ago, GUI agents were mostly evaluated on simulated or web-only environments with small human-labelled sets. Since OSWorld (2024) established a live-desktop benchmark, results have come from two directions: compositional, closed-model agent frameworks (Agent S, Agent S2) and open data-centric training with trajectory synthesis (AgentTrek, OS-Genesis, TongUI, all in the kept results). The common open problems are trajectory scarcity, grounding accuracy and long-horizon planning. At this moment a significant contribution in the open-data line is a data recipe that raises a *fixed* open model by a large margin against a *matched-data* alternative, or that is shown to generalize across benchmarks or model sizes; a gain over one's own smaller-data baseline is expected rather than distinctive. This calibrates Significance: I score the scale and the 20-step effect as real, the attribution as not yet shown.

### Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Zhang et al., "TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents", arXiv 2504.12679 (AAAI 2026 per search record); https://arxiv.org/abs/2504.12679v4 | Same source (web tutorials incl. video) and goal (trajectories for GUI agents) as C1 |
| Important | Ou et al., "Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale", arXiv 2409.15637; https://arxiv.org/abs/2409.15637v2 | Converts indirect knowledge (including tutorials) into demonstrations; relevant to the annotation-free framing |
| Important | Wu et al., "OS-Atlas: A Foundation Action Model for Generalist GUI Agents", arXiv 2410.23218; https://arxiv.org/abs/2410.23218v1 | Large-scale GUI grounding data and action-model pretraining: a direct comparator for the Stage-1 grounding claims |
| Helpful | Schmidt & Jiang, "Learning to Act without Actions", arXiv 2312.10812; https://arxiv.org/abs/2312.10812v2 | Label-free latent-action alternative to a supervised IDM |
All four were found by `related_search.py verify`; venue details beyond the TongUI record are not asserted.

### Dimension Scores (0–100)
**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: sound, useful application of a known recipe at scale, but uncited closest work, no component ablations and no comparator numbers keep it on the reject side of the bar.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Standard, correctly applied; lenient evaluation of the IDM |
| Clarity & Presentation | 62 | Competent | Clear positioning of the pipeline; thin related work |
| Novelty & Originality | 55 | Competent | New application of VPT-style IDM; medium vs TongUI |
| Significance & Impact | 60 | Competent | Useful for the open-data line if the effect holds up |
| Experimental Validation | 52 | Developing/Competent | No peers, no ablations |
| Reproducibility | 56 | Competent | Details present; release promised only |
| Ethical Compliance | 58 | Competent | Limited discussion of licensing |

### NeurIPS-style: Quality 2, Clarity 3, Significance 2, Originality 2.

### Questions for Authors
1. How does C1 differ from TongUI and Synatra, and can you show an empirical delta? (A concrete delta would raise Novelty.)
2. What is "unsupervised" in your pipeline, given the IDM is trained on 154 h of logged human data?
3. How does Jang et al. (2025) fail to provide "precise temporal boundaries or action parameters" (§5)?
4. What are the OS and application distributions of the mined videos?

### Limitations Assessment: **No** (no section; no discussion of OS shift or noise).
### Ethics Review Flag: **No** (see R3).
### Overall: **3 (Borderline Reject)**. Useful engineering with thin positioning and unisolated attribution.
### Confidence: **4**

---

# Peer Review Report (Reviewer 3: Perspective)

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Reviewer: Dr. Siobhan Adeyemi-Park, Perspective (HCI research institute; fictional persona)
## Expertise: RPA / workflow mining; privacy of screen recordings; human tutorials
## Date: 2026-11-10

### Summary
This work treats the large body of screen-recorded tutorials as implicit demonstrations of computer use and shows that a pipeline that detects and parameterizes actions can convert them into training data that improves a 7B computer-use agent, especially on live OSWorld tasks.

### Strengths
**S1: A powerful reframing.** Tutorials are demonstrations produced by people who explain intent aloud. Using ASR context (§2.2.3, App. E) to ground rationales mirrors how task-mining and process-mining systems in RPA use narration and event logs, and it is a genuinely interdisciplinary idea.
**S2: Evidence of a real effect on a live environment.** Three-run 20-step averages separate cleanly (Table 4: 9.13–9.42 vs 13.57–14.68), which matters more to practitioners than offline step accuracy.
**S3: Open tooling.** The promise to release ScreenFilter and Video2Action (§1) can help a community that lacks data.
**S4: Useful transparency.** Appendix tables on resolution, content classes and action distribution (Tables 6–8) are good practice for data papers.

### Weaknesses
**W1. Privacy, licensing and consent are essentially unaddressed.** The corpus is scraped YouTube video; the only statement is that "Final training sets are still screened by cursor gating, license/PII checks, and downstream detectors" (App. H), with no description of the licence filter, the PII procedure or whether the 1.52M-step corpus will be released. Tutorials show on-screen e-mails, file names and typed text, and the extracted `type` parameters are stored verbatim (e.g., Fig. 9 shows a typed string "lilybloom123."; whether it is real is unknowable). Creator consent and YouTube terms are not mentioned. **Fix:** a data statement (licence filter, PII redaction rate, takedown route) and, if the data are released, a licence analysis.

**W2. Unexamined assumptions.** (a) Tutorial demonstrators are near-optimal and rarely err, so the mined data contain few recoveries; yet §4.2 argues the data teach the agent to "persist through intermediate failures" and recover. (b) The visual-evidence assumption: keystroke-only actions are barely recoverable (`press` recall 0.08, Table 1), so the corpus under-represents keyboard-heavy workflows (Table 8: key 9.4%, hotkeys absent). (c) Distribution shift: OSWorld is Ubuntu (§3.1.1); the video corpus is a mixture whose OS composition is not reported. (d) Scale: all data come from "50+ channels", so scaling in *videos* may be scaling within a few creators' styles.

**W3. Deployment realism.** 15.78% task success (Table 4) means the agent fails ~84% of OSWorld tasks; the abstract calls the result "high-quality supervision". The Conclusion calls the pipeline "cost-effective" (§6), but no cost accounting (video storage, ScreenFilter at ~840 h per GPU-day (App. B), IDM inference, 1.52M GPT-5 calls, vs human annotation cost) is given. **Fix:** a cost table.

**W4. No limitations / broader-impact discussion.** Computer-use agents that execute typed input and clicks have misuse potential (credential entry, automation of abuse); none of this is discussed.

### Cross-disciplinary suggestions
Process/task mining from event logs (RPA literature) offers alignment and noise-handling ideas for matching narration to steps; speech-recognition-aware filtering could be used to drop segments where narration disagrees with the detected action; HCI evaluations (task completion with human-in-the-loop correction) would show practical value beyond autonomous success. Future directions: error-recovery mining (videos of tutorial mistakes), cross-OS adaptation, and learned confidence for label filtering.

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the practical value of an open pipeline plus a robust 20-step effect on a live benchmark outweighs typical-for-accepted-papers weaknesses; the ethics and attribution gaps keep it below the typical-accepted band.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound; see R1 for details |
| Clarity & Presentation | 62 | Competent | Clear story |
| Novelty & Originality | 64 | Competent | New instantiation, good reframing |
| Significance & Impact | 70 | Competent (upper) | Directly relevant to open agent data scarcity |
| Experimental Validation | 56 | Competent (lower) | Limited baselines/benchmarks |
| Reproducibility | 58 | Competent | Promised release |
| Ethical Compliance | 52 | Developing | No limitations or data-rights discussion |

### NeurIPS-style: Quality 2, Clarity 3, Significance 3, Originality 3.

### Questions for Authors
1. What licence and PII filters exactly were applied, and will the corpus be released? (A concrete protocol would raise Ethical Compliance.)
2. What fraction of mined steps are error/recovery behaviours, and does that support §4.2?
3. What are the OS and app distributions?

### Limitations Assessment: **No.**
### Ethics Review Flag: **Yes**: scraped YouTube content (copyright, terms of service, creator consent) and on-screen personal data / typed strings in a corpus intended for release as a pipeline; the paper's only treatment is one sentence in App. H.
### Overall: **4 (Borderline Accept)**. Valuable direction and robust live-benchmark effect; ethics and attribution gaps are fixable.
### Confidence: **3**

---

# Peer Review Report (Reviewer 4: Generalist)

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Reviewer: Dr. Hana Lindgren-Oyelaran, Generalist (university lab; fictional persona)
## Expertise: multimodal and video learning
## Date: 2026-11-10

### Summary
The paper proposes a three-part system (video collection with ScreenFilter, Video2Action IDM, two-stage agent training) that turns tutorials into ~1.52M training steps, and reports gains for a 7B agent on OSWorld-Verified and AgentNetBench. In my own words: "you can bootstrap computer-use training data from YouTube if you can label actions from pixels, and doing so before SFT helps".

### Venue fit and criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | Gain measured (Table 4) but attribution unisolated (§2.3.2) |
| Soundness: fair comparison | Partly | Only own baseline, token budgets differ (Fig. 11–12) |
| Presentation | Partly | Clear story; editing slips (§3.1.2, §4.2, App. D, Fig. 1) |
| Contribution: new insight beyond leaderboard | Partly | Data recipe; no analysis of why it works |
| Reproducibility / release | Partly | Hardware given, release promised, LR unverified |
| Limitations stated | Not met | None |

### Strengths
**S1: Clear, well-motivated problem and pipeline figure** (§1, Fig. 1/2/4), easy to follow for a non-specialist.
**S2: A measurable and large effect.** 14.13 vs 9.3 at 20 steps over three runs is well outside the run range (Table 4).
**S3: Useful appendices.** Training configurations (Figs. 11–12), prompts (App. E) and corpus statistics (Tables 6–10) make the work more concrete than most pipeline papers.
**S4: Practical value.** Open ScreenFilter / Video2Action, if released, is a community resource.

### Weaknesses
**W1. Contribution is a recipe without an explanation.** The paper shows that adding 26B tokens of mined data helps (§4.1), but does not say which part matters: actions, rationales, grounding pairs or sheer token volume. ICLR reviewers will want one controlled analysis. **Fix:** a small ablation grid (with/without monologue, with/without Stage-1 grounding pairs, token-matched control).
**W2. Claims run ahead of evidence.** "unsupervised" and "eliminating the need for manual annotation" (Abstract/§1) vs a supervised IDM and a human-annotated Stage 2; "high fidelity" vs 65.8% manual accuracy (Table 2); "true test-time scaling" from one run (§4.2). **Fix:** narrow the wording ("annotation-light", "mined from unlabeled video using a detector trained on 154 h of logged data").
**W3. Presentation slips reduce trust.** Mislabelled cross-references ("Figure 10" for the step histogram, "Section 4.1" for the budget analysis), "Figure 1 … Agent Traing", the unfinished sentence "We visualize the data sample in Figure" (App. D), inconsistent names ("SFT-only", "stage2 only"), duplicated 15.7 / 15.78 / 15.8, and arithmetic slips in Tables 1, 4, 6, 8. **Fix:** a careful pass; one consistent name for each model.
**W4. Thin related work and no limitations section** (§5 spans three short paragraphs; no section lists limitations).

**Minor:** typographical issues (see R1).

### Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a large, replicable effect at scale and clear writing of the pipeline place it near a typical accepted data-centric paper; the missing controls and overclaims are common among accepted papers but here touch the central claim.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Sound pipeline; gaps in controls |
| Clarity & Presentation | 58 | Competent | Understandable; many slips |
| Novelty & Originality | 60 | Competent | Application-level novelty |
| Significance & Impact | 66 | Competent | Of interest to many ICLR attendees working on agents |
| Experimental Validation | 57 | Competent | Adequate for the main claim, not comprehensive |
| Reproducibility | 60 | Competent | Details present; promised release capped |
| Ethical Compliance | 58 | Competent | Brief |

### NeurIPS-style: Quality 2, Clarity 2, Significance 3, Originality 2.

### Questions for Authors
1. Which ingredient of Stage 1 matters (actions, thoughts, grounding, token volume)? A clean answer would move me up.
2. Why does the abstract use the 50-step single-run number while §3.1.2 emphasizes 20-step averages?
3. Will the mined corpus, not only the tools, be released?

### Limitations Assessment: **No.**
### Ethics Review Flag: **No** (defer to R3).
### Overall: **4 (Borderline Accept)**. Clear, useful, large measured gain; I lean accept despite attribution gaps, which are typical of this kind of paper.
### Confidence: **3**

---

# Devil's Advocate Report

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Reviewer: Dr. Rafael Bjornsson-Haddad, independent evaluation-methodology researcher (fictional persona)

## Steelman
A tutorial video contains the same information a human annotator would produce: where the pointer goes, what is typed, why. A good IDM can recover this, and tutorials exist at web scale. Training a 7B agent on 26B tokens of such data before SFT lifts live-desktop success from 9.3% to ~14–16%, an effect that survives three runs at 20 steps.

## Core Argument Chain
1. Tutorial videos contain implicit GUI demonstrations (§1).
2. Video2Action recovers actions and parameters accurately enough (§3.2, Tables 1–2).
3. The recovered steps (plus GPT-5 rationales) form useful training data (§2.3).
4. Training on them before SFT improves OSWorld-Verified and AgentNetBench (Tables 4–5).
5. More video tokens → more gain (§4.1) and better long-horizon behaviour (§4.2).
∴ Passive internet video is a scalable, annotation-free, cost-effective source of supervision for computer-use agents (§6).

## Strongest Counter-Argument
Step 4 is real; the inference from 4 to the conclusion is not. The comparison is "8B human tokens" vs "26B mined tokens + 1B grounding + the same 8B" (§2.3.2, Figs. 11–12): three times the compute and an entirely different kind of text (GPT-5-written, first-person rationales conditioned on narration, §2.2.3). That is a confound that would raise performance for many data sources, including no video at all. The paper then reads the result as evidence about *video*, about *inverse dynamics*, about *long-horizon planning*, and about *annotation cost*. None of these is tested: no equal-token non-video control; no run with noisy labels removed; no comparison with simpler or existing tutorial-mining methods; no cost accounting. What *is* measured about the IDM is weak: any temporal overlap counts as a detection (§3.2.1) and a plausibility-based manual check gives 65.8% accuracy on 500 samples (Table 2), with 0.08 `press` recall (Table 1). If a third of parameters are wrong and a third of steps missing, an alternative explanation is simply that the agent benefits from a large amount of in-domain GUI-formatted text and screenshots *despite* the noise, which is much less interesting than "video supervision works", and would be reproduced by a text/synthetic pipeline. And the "annotation-free" framing is undercut by the pipeline's own dependencies: an IDM trained on 154 h of logged human data (App. C), a Stage 2 of human-annotated trajectories (§2.3.2), and proprietary GPT-5 and GPT-4.1 labelling (§2.2.3, App. H). The authors can answer by adding a token-matched control and narrowing the claims; until then the evidence supports "adding in-domain tokens built from mined videos helps a 7B model", not the headline thesis.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core measured gain is real (Table 4, three runs), and the weaknesses below are fixable by controls or by narrowing claims; none contradicts the main claim or makes the experiment unable to test it, and there is no test-set selection (no selection statement found in the protocol sweep).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (confound) | §2.3.2, Figs. 11–12, §4.1 | Stage-1+2 vs Stage-2-only differs by ~27B tokens and ~3× compute and by GPT-5-generated text; attribution to video is untested (evidence supports a weaker claim) | Token-matched non-video control; ablate monologues |
| DA-M2 | Scope / claim distortion (E5) | Abstract; §1 bullet 1 ("an unsupervised approach to training computer-use agents"); App. C; §2.3.2 | "Unsupervised / eliminating manual annotation" vs supervised IDM (154 h human logs), human-annotated Stage 2, proprietary LLM labelling | Reword; report a variant with less human data |
| DA-M3 | Logic (mechanism) | §4.2; §3.1.2 | "demonstrates true test-time scaling" and "teaches the model to decompose complex tasks into subgoals": one 50-step run, no analysis of behaviours; long trajectories reflect long videos, not harder tasks (Table 9 compares a video-level trajectory against task-level benchmarks; avg 39.25 estimated from 5,416 samples) | 3 runs at 50 steps; trajectory-level analysis (recovery, subgoal) or soften |
| DA-M4 | Evidence (label quality) | §3.2, Tables 1–2 | Overlap-only detection criterion; 65.8% plausible-accuracy; no coordinate error; impact on training untested | Held-out pixel error; filtered-subset training |
| DA-M5 | Scope (diversity/scale) | §1 ("hundreds of applications"); §2.1.3 ("50+ channels"); Fig. 3 | Diversity and "web-scale" claims unsupported by app/OS statistics; 55,603 videos from ~50 channels | Report app/OS/channel distributions; channel-held-out analysis |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Reporting | Tables 1, 4, 6, 8 | Totals and denominators do not reconcile (see R1 Error Log) |
| DA-m2 | Reporting | Table 5 / App. G | `terminate` regression (0.588 → 0.237) not discussed |
| DA-m3 | Ethics | App. H, Fig. 9 | Licence/PII handling one sentence; typed strings stored verbatim |
| DA-m4 | Clarity | §2.2 vs Fig. 4 | Unclear whether Stage-1 inputs are video clips or single screenshots, and how a task goal is supplied for mined trajectories (the tuple R has no instruction, §2) |
| DA-m5 | Cost claim | §6 | "cost-effective" with no cost figures |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| 70% relative improvement (50 steps) | 15.8 vs 9.3 | 15.78/9.27 = 1.702 (70.2%); vs 9.3: 69.7% | ✓ |
| +52% at 20 steps | +4.83 pts | 14.13 − 9.3 = 4.83; 4.83/9.3 = 51.9% | ✓ |
| Test-time scaling +11.7% | 14.13 → 15.78 | 1.65/14.13 = 11.7% | ✓ (single run vs mean of 3) |
| AgentNetBench +5.2 / +30.8 | 69.3 vs 64.1 / 38.5 | 5.2 / 30.8 | ✓ |
| Table 1 total preds | 17,298 | 16,298 | ✗ |
| Table 1 overall recall | 0.70 (text 0.71) | 14,247/20,282 = 0.7025 | ✓ table, ✗ text |
| Table 4 stage2-only 50-step | 9.27% | 33 tasks → 9.14% (/361) | ✗ |
| Table 4 denominators | 369 tasks | sum 359 | ✗ |
| Table 8 total | 1,547,092 | rows sum 1,560,464 | ✗ |
| Table 6 total | 55,603 | rows sum 53,375 | ✗ |
| Steps | 39,000 × 39 ≈ 1.52M | 1.521M | ✓ |
| Table 2 overall | 0.658 | weighted by sample sizes 0.660 | ✓ (rounding) |

## Ignored Alternative Explanations
(1) Token count / compute; (2) GPT-5 distillation of reasoning text; (3) pseudo-labelling of an OpenCUA-like distribution by a model trained on OpenCUA, which brings the Stage-1 data close to Stage-2 and to AgentNetBench's source (leakage possibility is an open question, not a finding); (4) run-to-run variance at 50 steps; (5) chrome and thunderbird tasks drive most of the difference (Table 4), pointing to domain overlap with common tutorials rather than general ability.

## Missing Stakeholder Perspectives
Video creators whose content is scraped (consent, licence, credit); people whose data appear on screen; downstream users of an agent that might type credentials.

## Observations (Non-Defects)
The three-run 20-step comparison is cleanly separated and properly reported per app (Table 4). The authors disclose that the 50-step budget was one run, report flat Stage-2-only behaviour honestly, and publish training configurations. The data-scale curve points in the expected direction.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Confound, lenient IDM evaluation |
| Clarity & Presentation | 58 | Readable; slips |
| Novelty & Originality | 52 | Application of VPT recipe, uncited closest work |
| Significance & Impact | 56 | Conditional on the effect being video-driven |
| Experimental Validation | 44 | No matched control, no peers, single-run claims |
| Reproducibility | 54 | Release promised; selection steps unclear |
| Ethical Compliance | 52 | Data-rights gap |

**Pool position:** better than about 48% of submissions to ICLR. Deciding evidence: the central attribution is untested and several headline words are not backed.

## Overall: 3 | Confidence: 4

---

## Phase 1.5 / 1.6: Literature Addendum and Report Check

Literature check: strict, cutoff 2025-09-24, 6 queries (claims C1–C3, one OSWorld baseline query, two expansion queries) and 4 verifications; kept results used as above. Results labelled recent preprint / concurrent are "worth discussing" only and lowered no score.

### Report-check table (Synthesizer, Step 0)
| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | W1 statement that related work "typically lacks precise temporal boundaries" is unsupported (Jang et al.) | Rewritten as a question | Cannot check the abstract of Jang et al. |
| R3 | W1 "typed string looks like a credential" | Rewritten: noted as example whose real status is unknowable | Hard Rule 10 |
| R1 | Leakage into AgentNetBench | Moved to Questions (it is in Protocol sweep as "not stated") | Suspicion, not error |
| R4 | W4 (no limitations section) merged with thin related work | Kept, merged | Verified: no limitations section exists |
| DA | DA-M3 "long trajectories reflect long videos" | Kept, tone adjusted | Table 9 compares video-level and task-level trajectories (paper's own footnote) |
| R1/R4 | Typographical items | Moved to one Minor line each | Cosmetic |
No weakness was dropped as already answered in the appendix.

---

## Phase 2: EIC Meta-Review and Editorial Decision

# Editorial Decision

## Paper: VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos
## Submission ID: iclr26-xxYPqm1qWz
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Marguerite Okonkwo-Lindqvist; R1 Methodology (Dr. Vuong), R2 Domain (Prof. Castellanos-Ruiz), R3 Perspective (Dr. Adeyemi-Park), R4 Generalist (Dr. Lindgren-Oyelaran), DA (Dr. Bjornsson-Haddad)

---

## Decision: Borderline Reject (3), ICLR label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})", scale status: secondary

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40** · official composite **56.7**
**EIC assessment** (internal): weighted rating **3.34** → starting point **3** · weighted composite **56.4** → band 3 (cross-check agrees, no ⚠) · **DA ceiling**: none · **Final (EIC)**: **3**

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A large, practical pipeline that, over three runs at 20 steps, moves a 7B agent from ~9.3% to ~14.1% on live OSWorld-Verified (Table 4), with open tools promised and an informative appendix. The direction (tutorial video as agent data) is timely and the effect is not noise.
- **Against acceptance:** The central claim (video-mined supervision, rather than 27B more in-domain tokens including GPT-5 rationales, drives the gain) is untested; IDM labels are weakly validated (65.8% plausible-accuracy, overlap-only detection); no comparison with any other agent, one base model, two benchmarks; several headline words are unbacked ("unsupervised", "millisecond-precision", "true test-time scaling"); uncited closest work; no limitations or data-rights discussion.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Stage-1+2 vs stage-2-only differs by ~27B tokens, no matched control | R1-W1, DA-M1, R4-W1 | §2.3.1–2.3.2, Figs. 11–12 | **Verified** | The only baseline is stage2-only; no equal-token run is reported |
| "Unsupervised / no manual annotation" vs supervised IDM and human Stage 2 | DA-M2, R1 map C1, R2-W3 | Abstract; §1; App. C; §2.3.2 | **Verified** (partly semantic) | The *videos* are unlabeled; the recipe is not annotation-free |
| "millisecond-precision" vs overlap criterion | R1-W2/ERR-6 | §1 bullet 2; §3.2.1 | **Verified** | |
| Table 2 gives 65.8% manual accuracy; Table 1 `press` recall 0.08 | R1-W2, DA-M4 | Tables 1–2 | **Verified** | The plausibility criterion is lenient, so the figure may understate or overstate true coordinate error: unknown |
| 50-step results are single runs; scaling claim rests on +1.65 | R1-W3, DA-M3 | App. G, Table 4, §4.2 | **Verified** | The 20-step effect is robust across three runs |
| Table 1 total preds 17,298 vs rows 16,298 | R1 ERR-1 | Table 1 | **Verified** | |
| Table 4 denominators sum 359; stage2-only 50-step 33 tasks vs 9.27% | R1 ERR-2/3 | Table 4 | **Verified** | |
| Tables 6 and 8 totals | R1 ERR-4/5 | App. H | **Verified** | |
| `terminate` accuracy 0.588 → 0.237 | R1-W6, DA-m2 | Table 5 | **Verified** | Not discussed in the text |
| TongUI uncited; overlaps C1 | R2-W1 | Reference list, kept abstract | **Partly correct** | Task (tutorials→trajectories) matches; the mechanism differs and the abstract excerpt is truncated; no DA criterion-7 case |
| "hundreds of applications" unsupported | R2-W5, DA-M5 | §1, Fig. 3 | **Verified** | Only six categories reported |
| No limitations / broader-impact section | R3-W4, R4-W4 | whole paper | **Verified** | |
| Typed string in Fig. 9 may be credential | R3-W1 | Fig. 9 | **Partly correct** | Example exists; real status unknowable |
| AgentNetBench task overlap with training logs | R1 Q2 | §3.1.1, App. C | **Not verifiable** | Not stated; kept as a question |
| Figure-based claims (Figs. 5, 6, 10) | all | captions | **Not checked** | Figures unavailable |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Every numeric finding in the Error Log checked out; central confound well grounded |
| R2 (Domain) | 3 | 4 | 1.0 | TongUI point verified but slightly overstated; a sound, typical review |
| R3 (Perspective) | 4 | 3 | 1.0 | Mostly verified; one speculative item (credentials) hedged |
| R4 (Generalist) | 4 | 3 | 1.0 | Sound; leans lenient given its own dimension scores (implied Overall 3) but not wrong |
| DA | 3 | 4 | 1.0 | Strongest counter-argument verified; "annotation-free" point partly semantic |

### DA-CRITICAL Rulings
The Devil's Advocate raised no CRITICAL issue ("No CRITICAL issues found"). I checked the possible criterion 1/2 reading (the experiment cannot test the claim): the experiment tests whether the full recipe beats Stage-2-only (it does), so a missing control is MAJOR under the "partly controlled confound" exception. No selection on a reported split is described (protocol sweep). **DA ceiling: none.**

### Final Decision and Justification
The official ratings (3, 3, 4, 4, 3; mean 3.40) and the EIC-weighted rating (3.34) both round to 3; the composite cross-check (56.4, band 3) agrees, with no ⚠, so I keep the starting point and depart from nothing. My pool position is **57**: the decisive evidence is that the headline attribution (to video-derived supervision) is confounded by token count and GPT-5-written reasoning and is not tested by any control, the labels are weakly validated, and no reference point from other agents is given, which are signals of a typical rejected submission; the 20-step effect (three runs, 4.8 points), the scale of the pipeline and the timeliness are real positives that keep the paper near the line and make a revision (adding the token-matched control, boundary and coordinate metrics, peer numbers and a data statement) plausibly acceptable. This is "how a careful panel would likely see this draft", not a prediction. The decision does not exceed the DA ceiling (none).

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate_scores.py --venue iclr --final 3`, with EIC weights; BEFORE = no EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 55 | 58 | 62 | 60 | 50 | 57.0 | 56.6 | 12 |
| Clarity & Presentation | 60 | 62 | 62 | 58 | 58 | 60.0 | 60.0 | 4 |
| Novelty & Originality | 55 | 55 | 64 | 60 | 52 | 57.2 | 56.7 | 12 |
| Significance & Impact | 58 | 60 | 70 | 66 | 56 | 62.0 | 61.4 | 14 |
| Experimental Validation | 48 | 52 | 56 | 57 | 44 | 51.4 | 50.9 | 13 |
| Reproducibility | 56 | 56 | 58 | 60 | 54 | 56.8 | 56.6 | 6 |
| Ethical Compliance | 55 | 58 | 52 | 58 | 52 | 55.0 | 55.0 | 6 |
| **Composite** | 54.6 | 56.9 | 60.9 | 59.9 | 51.4 | **56.7 (before)** | **56.4 (after)** | |

Official Overall mean 3.40; EIC-weighted rating 3.34 (weights: R1 1.25, others 1.0). Pool positions: R1 50, R2 55, R3 66, R4 65, DA 48; EIC 57. No consistency warnings. (R4's own composite 59.9 implies Overall 3; R4 gave 4: a one-step gap explained in its report.)

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Venue-weighted composite | 56.5 (band 3) |
| Rating (label from the script) | **4 on {0,2,4,6,8,10}** (5 on {1,3,5,6,8,10}); skill-internal 3 Borderline Reject |
| Confidence | mean 3.6 |

*Recent analyses report the {0,2,4,6,8,10} scale for ICLR 2026; verify against the current form.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "VideoAgentTrek: Computer-Use Pretraining from Unlabeled Videos" to ICLR. Converting the large stock of screen-recorded tutorials into training data for computer-use agents is a worthwhile and timely goal.

**Overall Assessment:** The reviewers appreciated the scale and practicality of the pipeline and the clear improvement on live OSWorld-Verified over three runs. They were less convinced that the improvement can be attributed to video-derived supervision rather than to additional in-domain tokens and LLM-written rationales, that the extracted labels are as accurate as described, and that the stated claims (annotation-free, millisecond precision, test-time scaling) are supported.

**Key Strengths Identified by Reviewers:**
1. A large, realistic pipeline with robust gains at 20 steps across three runs (R1, R3, R4, DA).
2. A useful reframing of tutorials as demonstrations, with open tools promised (R2, R3, R4).
3. Transparent appendices (training configurations, prompts, per-app and per-action tables) (R2, R3, R4, DA).

**Key Concerns Requiring Attention:**
1. No token- or compute-matched non-video control; GPT-5 rationales not ablated (R1, R4, DA; CONSENSUS-3).
2. Weak validation of label quality; precision wording unsupported (R1, DA, R2; CONSENSUS-3).
3. No comparison with released agents or other benchmarks; positioning omits closest work (R1, R2; CONSENSUS-2).
4. Overclaims: "unsupervised", "eliminating manual annotation", "true test-time scaling" (R1, R2, R4, DA; CONSENSUS-4).
5. Data rights, PII and limitations (R3, R4, DA; CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** The DA argued that the measured gain is real but is compatible with a token-count / reasoning-distillation explanation that would hold with no video at all. This was not rated CRITICAL, but it is what a revision must address first.

**Decision: Borderline Reject (3)**

In its present form, the paper's central causal claim is not isolated by the experiments, and several claims go beyond the evidence. These are fixable with experiments that are within a rebuttal-plus-revision effort (a token-matched control, boundary / coordinate metrics, peer numbers, three runs at 50 steps) and with narrowing of wording. If the control confirms that video-derived supervision helps beyond an equal-token alternative, the paper would be a solid accept-level data contribution. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Marguerite Okonkwo-Lindqvist
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| Unsupported or overstated claims ("unsupervised", "high fidelity", "true test-time scaling") | R1, R2, R4, DA | CONSENSUS-4 |
| Attribution not isolated (token/compute/GPT-5 confound; no ablation) | R1, R4, DA | CONSENSUS-3 |
| Label quality weakly measured | R1, DA, R2 (via claim calibration) | CONSENSUS-3 |
| No limitations / data-rights discussion | R3, R4, DA | CONSENSUS-3 |
| Missing peer comparison; thin positioning | R1, R2 | CONSENSUS-2 |
| Reporting inconsistencies | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall level | R3, R4 (4) | R1, R2, DA (3) | The 4s rest on practical significance and the robust 20-step effect, which I credit; the 3s rest on the unisolated attribution, which is the more decisive verified issue (see weights) |

### Score Spread Discussion
No dimension exceeds the 20-point spread; the widest is Significance (56–70), where R3 values the open-data direction and R1/DA discount it until attribution is shown. I adopt the weighted value (61.4).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Token/GPT-5 confound | Yes (R1-W1, R4-W1) | n/a | New experiments |
| DA-M2 | MAJOR | "Unsupervised / annotation-free" | Yes (R1, R2, R4) | n/a | Clarification (rewording) |
| DA-M3 | MAJOR | Test-time scaling / subgoal mechanism | Yes (R1-W3) | n/a | Re-running 50-step evaluation |
| DA-M4 | MAJOR | IDM label quality | Yes (R1-W2) | n/a | New measurements on existing held-out logs |
| DA-M5 | MAJOR | Diversity/scale claims | Partly (R2-W5, R3-W2) | n/a | Statistics on existing data |
(No DA-CRITICAL issue.)

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Attribution confound (tokens, compute, GPT-5 rationales) | R1-W1, DA-M1, R4-W1 | §2.3.2, Figs. 11–12, §4.1 | Token-matched non-video control (same 26B tokens from repeated human data or a simpler pipeline); ablate monologues and grounding pairs | High; ≈1,920 GPU-h for Stage 1 + 1,024 for Stage 2 per control | Partly (one control feasible; full grid not) |
| P1-2 | Unsupported headline wording | DA-M2, R1 (C1/C2), R2-W3, R4-W2 | Abstract; §1; §6 | Replace "unsupervised / eliminating manual annotation / millisecond-precision / high fidelity / cost-effective" with supported statements, or add evidence | Low | Yes |
| P1-3 | IDM label quality not measured adequately | R1-W2, DA-M4 | §3.2, Tables 1–2 | Pixel error for clicks, exact match for typing on held-out OpenCUA logs; IoU/boundary metrics; confidence-filtered training run | Medium; ~500 GPU-h | Partly |
| P1-4 | Single-run 50-step and scaling claims | R1-W3, DA-M3 | App. G, §4.2, Fig. 6 | Three runs at 50 steps (both models, and the 50% variant); soften mechanism claims | Medium (evaluation only) | Yes |

### Priority 2: Strongly Suggested
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No external reference points; one base model/benchmark pair | R1-W4, R2-W4 | Add published numbers of open agents under stated budgets; one more benchmark | Medium | Yes |
| S2 | Closest prior work uncited (TongUI, Synatra, OS-Atlas, LAPO) | R2-W1, R2 refs | Cite and differentiate; one empirical delta if possible | Low–Medium | Yes |
| S3 | Reporting inconsistencies (Tables 1, 4, 6, 8; text 0.71; Fig. 6 vs Fig. 5) | R1 Error Log, DA-m1 | Reconcile; state the OSWorld task list | Low | Yes |
| S4 | AgentNetBench / training-log overlap | R1 Q2 | State exclusion protocol | Low | Yes |
| S5 | Diversity claims, OS/app distribution, channel concentration | DA-M5, R2-W5, R3-W2 | Report statistics; temper "hundreds of applications" | Low | Yes |
| S6 | Data rights, PII, limitations | R3-W1, R3-W4, R4-W4, DA-m3 | Data statement; limitations section; release plan | Low | Yes |
| S7 | `terminate` regression | R1-W6, DA-m2 | Analyse and discuss | Low | Yes |

### Priority 3: Nice to Fix
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Cross-reference and labeling slips (Figure 10/Table 10, Section 4.1/4.2, App. D "dense detector", "Agent Traing") | R1, R4 | Copy-edit |
| N2 | Cost accounting | R3-W3, DA-m5 | Cost table |
| N3 | Error-recovery mining, narration-aware filtering | R3 | Future work |
| N4 | Clarify Stage-1 input form and task-goal conditioning | DA-m4 | One paragraph |

## Estimated Revision Effort
- Priority 1: 4 items, ~2–3 weeks (about 3,500–5,000 GPU-h, mostly the matched control)
- Priority 2: 7 items, ~1 week (mostly text and small analyses)
- Priority 3: 4 items, ~1 day
- **Total estimated revision time**: about 3–4 weeks

*Gap Scout (optional post-review analysis) was not run.*
