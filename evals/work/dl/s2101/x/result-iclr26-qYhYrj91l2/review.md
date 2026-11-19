# Academic Paper Review: VividCam (ICLR, full mode)

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated; profile key `iclr`, 2026 cycle, scale status *secondary*) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped.

*Disclosure: the five reviewers were run as five separate role-based passes by one model in one context (no delegation). They are not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only. The simulation describes how a careful panel would likely see this draft; it does not predict a real outcome.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos |
| Primary Discipline | Computer Vision → controllable video generation (camera control) |
| Secondary Discipline(s) | Computer graphics / virtual production (game-engine rendering); sim-to-real domain adaptation |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Text-to-video diffusion (CogVideoX-5B, AC3D), LoRA fine-tuning, synthetic data from Unity, frame-difference loss, virtual-style prompt token |
| Target Venue | ICLR, top-tier ML conference (stated); profile key `iclr` |
| Venue-Specific Notes | none (ICLR: Soundness / Presentation / Contribution, public reviews, revised PDF allowed during discussion) |
| Paper Maturity | Submission-ready draft, thin on evaluation (no limitations section) |
| Ethics-Relevant Content | Generative video model (misuse potential, not discussed); crowdsourced human study on Amazon Mechanical Turk (compensation, consent/IRB not stated); synthetic data only, no personal data |

### Claimed Contributions (as stated by the authors, §1 end)
1. **C1**: "a novel framework for generating realistic videos with diverse camera motions by leveraging synthetic data efficiently rendered from engines like Unity" (VividCam).
2. **C2**: VividCam "effectively mitigates artifacts present in low-quality synthetic videos and focuses on learning their complex camera motions" (appearance LoRA §4.3, static-camera set X_a §4.2, style-aligned prompt §4.3, flow loss Eq. 5).
3. **C3**: "a wide range of camera motions with precise, consistent control and high visual quality" (Tables 2–3, Figs. 4, 6–8).
Further strong claims: realism "comparable to models trained on real footage" (§1, §6), "releasing the reliance on collecting realistic training videos" (Abstract), an "appearance-invariant" flow loss (§1), "cost-efficient training paradigm" (§5.4).

### Paper memory (factual record shared with all reviewers)
- **Setup:** base CogVideoX-5B, frozen (App. C); text-based control: appearance LoRA rank 128 and camera LoRA rank 512 (§5.1, Table 6), lr 1e-4 / 3e-4; trajectory-based control: full fine-tuning of the AC3D camera encoder, lr 1e-4 (§4.3, App. C, Table 6). 49 frames, 720×480 (App. C). Training data: Unity low-poly scenes (App. A), "500 synthetic training videos" per motion type (App. C); static-camera set X_a count not stated. Splits/selection protocol, seeds, steps, batch size, λ of Eq. 5, GPU hours, code release: **not stated after search**.
- **Evaluation:** 3 categories (simple/composed/complex) × 100 prompts (§5.3); FVD, TransErr, RotErr (Table 2); human study on MTurk, 88 workers, 25 prompts × 2 repeats per category, 0–2 scale (App. E, Table 3); CLIP similarity (App. F, Table 7); ablations (Tables 4–5). Baselines: CameraCtrl, CogVideoX, AC3D with official checkpoints (§5.3).
- **Headline numbers:** Table 2 (e.g., composed TransErr 0.2208 vs 0.5107 for CogVideoX), Table 3 (complex Action Correctness 0.77/0.81 vs 0.61–0.68), Table 4 (full 0.93/0.74), Table 5 (0.88/0.75 mixed vs 0.91/0.72 virtual).
- **Appendix adds:** Unity scene options (A), prompt format examples (B), hyperparameters (Table 6, C), qualitative figures 6–8 (D), MTurk protocol (E), CLIP (F).
- **Unverifiable:** all figures (images unavailable); Eq. 1–2 norm symbols (extraction shows no norm bars, treated as an extraction artifact).

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. No instruction-like text was found while reading. Reviewers read the redacted copy (identical to the paper here).

### Literature check log (Phase 1.5)
Mode strict (cutoff 2025-09-24), 8 of 12 queries used (6 claim, 2 expansion), arXiv API. `benchmarks` returned no external benchmark (the evaluation is the authors' own prompt set; RealEstate10K is only a training-data ablation), so no baseline query/scout was run: gap left open. `similarity`: closest prior works AC3D (cosine 0.253), MoTrans (0.238), Collaborative Video Diffusion (0.230); no high-overlap or text-overlap flag. Claim-level `novelty`: C1 medium, C2 medium, C3 medium; paper reading "no central claim fully covered by prior work" (attribution: Free-Form Motion Control, Shuai et al.).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Marit Solheim-Adeyemi, public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / generative models, video diffusion, evaluation of generative models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Area-chair mindset: asks whether the contribution outweighs ordinary weaknesses; distrusts unverified quotes

### Reviewer 1 (Methodology): Dr. Joaquín Aldermere, industrial research lab (North America)
- **Seniority / Expertise**: Mid-career / FVD and human-evaluation design for video generation; LoRA fine-tuning protocols
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched baselines, variance, and a stated protocol for every number

### Reviewer 2 (Domain): Prof. Wen-Li Brandvold, large public university (East Asia)
- **Seniority / Expertise**: Senior faculty / camera-controllable video diffusion; motion customization and domain adaptation
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads bibliographies against text; separates "new application" from "new mechanism"

### Reviewer 3 (Perspective): Dr. Amara Tessendorf, graphics and virtual-production research institute (Europe)
- **Seniority / Expertise**: Senior researcher / real-time rendering, cinematography, sim-to-real
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what filmmakers and game-engine users would need

### Reviewer 4 (Generalist): Dr. Rafael Kowalczyk-Nair, university vision group (South America)
- **Seniority / Expertise**: Mid-career / general computer vision, not video generation specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against contribution

### Devil's Advocate: Prof. Selin Haverford-Duarte, university statistics and ML department (Middle East)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, causal inference, confound analysis
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reviews

# Peer Review Report: Reviewer 1 (Methodology)

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Reviewer: Dr. Joaquín Aldermere, Methodology Reviewer (industrial research lab, North America; fictional persona)
## Expertise: video-generation evaluation (FVD, human studies); LoRA fine-tuning protocols
## Date: 2026-11-10

### Protocol sweep
Searched the whole text for split/selection terms. **Present:** none of "validation", "held-out", "selected", "checkpoint", "best", "early stopping" occur as a protocol statement. The paper states no train/val/test protocol for the evaluation prompts, no checkpoint selection rule, and no tuning split. **Not stated after search:** seeds, number of training steps/epochs, batch size, λ (§4.3, "where λ > 0 balances two losses"), compute. Evaluation uses 100 prompts per category (§5.3) and is generation-only, so there is no labelled test split to leak; the open question is whether the checkpoint/hyperparameters were chosen by looking at these same prompts (question Q1).

### Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Framework learns camera motions from synthetic Unity videos | Abstract, §1 | Tables 2–3, Figs. 4, 6 | Partially: shown for a fixed list of scripted motions (Table 1) that are also the test motions |
| C2 | Disentangles appearance: A-LoRA + style prompt + flow loss | §1, §4.3 | Table 4 (A-LoRA, S-Prompt only), Fig. 5 | Partially: **no ablation of L_flow**; Table 4 setting unstated |
| C3 | Precise control and high visual quality | §1, §5.3 | Tables 2–3 | Partially: strong on composed motions; weak/mixed on complex motions (see W1) |
| C4 | Realism "comparable to models trained on real footage" | §1, §6 | Table 5 (RealEstate10K only) | Partially: real-data control is a low-diversity indoor dataset |
| C5 | "appearance-invariant supervision" from the flow loss | §1 | Eq. 5 | Unsupported: Eq. 5 is a frame difference |

### Strengths
**S1: A simple, well-motivated recipe with a sensible domain-gap design.** §4.3 separates a static-camera appearance set X_a from a moving-camera set X_c, freezes the appearance LoRA while training the camera module, and discards it at inference. The experimental question (can very low-quality synthetic videos teach camera motion?) is crisp, and the Unity setup (App. A) is cheap and described concretely.

**S2: A relevant evaluation target and a non-trivial motion set.** Table 1 and §5.1 define simple, composed and complex categories, and the complex ones (handheld shake, rotation, object seeking) are exactly where CogVideoX and AC3D degrade (Table 3: baseline complex Action Correctness 0.61–0.68).

**S3: The ablation directly probes the main disentanglement mechanisms and the data-source question.** Table 4 isolates the appearance LoRA (Realism 0.74 → 0.60 without it) and the style prompt (0.74 → 0.65); Table 5 asks whether real data helps. Reporting FVD-based and human-based metrics together (Tables 2–3) and CLIP in App. F is more honest than a single metric.

**S4: Honest reporting of an unfavourable number.** §5.3 states that vanilla CogVideoX has the best RotErr for simple and composed motions and explains why; this is a claim-versus-evidence discussion many papers omit.

### Weaknesses

**W1: On the complex ("unconventional") motions, the automatic evidence is weak and the quality metric goes the wrong way; the claim rests on a small crowd study.** In Table 2 (complex), VividCam-Cog improves over CogVideoX by only 0.4327 → 0.4011 TransErr (−7.3%, derived) and 0.5067 → 0.5013 RotErr (−1.1%, derived), while FVD worsens 1488.36 → 1866.40 (+25.4%, derived), the worst FVD of all five methods in that block. §5.3 calls this "the small FVD difference compared to the vanilla". The large TransErr gains are on composed motions (0.5107 → 0.2208, −56.8%, derived), which are the *least* unconventional. For VividCam-AC3D, RotErr is slightly *worse* than AC3D on simple (0.1162 vs 0.0973) and composed (0.1968 vs 0.1958). The unconventional-motion claim therefore depends on Table 3 (complex Action Correctness 0.77/0.81 vs 0.61–0.68).
- **Suggested Fix:** Report all categories with paired confidence intervals; add an honest paragraph on complex-motion FVD; add a motion metric that works for non-rigid camera motions (e.g., flow-based motion statistics, VBench-style motion smoothness). Cost: analysis only, plus ~100 extra videos per method.

**W2: The human study is under-specified and unqualified by variance, and carries the decisive claims.** App. E: 25 prompts × 2 repeats = "50 videos per camera motion category and a total of 150 videos" (is that per method? 150 across five methods cannot be 50 per category per method), "Each question is awarded $0.03", 88 workers, ratings 0–2. Missing: number of ratings per video, whether method identity/order was blinded and randomized, attention checks and worker qualification, inter-rater agreement, confidence intervals or tests. Many differences that the text reads as findings are small: simple Realism 0.77 vs 0.74 (VividCam-Cog vs CogVideoX); Table 5, 0.91/0.72 vs 0.88/0.75. VividCam-AC3D simple Action Correctness (0.74) equals AC3D (0.74) and is below CogVideoX (0.80) and CameraCtrl (0.79).
- **Suggested Fix:** Describe sampling and blinding, report per-video rating counts, bootstrap CIs over prompts and raters, Krippendorff's α, and paired sign tests for the headline comparisons. Cost: no new generation; ~1 day of analysis (rerun a small batch if raw ratings were not kept).

**W3: The optical-flow loss (Eq. 5) is neither optical flow nor shown to matter.** §1 says it provides "appearance-invariant supervision". Eq. 5 compares frame-to-frame *pixel differences* of the predicted clean video with those of the ground truth. Frame differences depend directly on texture and edges, so they are not appearance-invariant, and the ground truth here is the synthetic video whose appearance the method wants to discard. It is applied to an x̂₀ reconstructed from a noisy X_t (timestep weighting not stated), and λ is never given. No ablation of L_flow exists (Table 4 covers only A-LoRA and S-Prompt), although it is listed among the two "complementary components" (§1). I recompute: Eq. 5 contains no flow estimator.
- **Suggested Fix:** Add rows "w/o L_flow" and λ sweep (text-based, one camera LoRA each: roughly 3 trainings, a few GPU-hours each on a 5B model with LoRA); either rename to "frame-difference loss" or use a real flow estimator (e.g., RAFT) on x̂₀ and discuss timestep weighting.

**W4: The baselines are not comparable on architecture, resolution and training data, and there is no "naive synthetic fine-tuning" or "small real-data" baseline for the main tables.** §5.3 uses "the official implementations and checkpoints": CameraCtrl is a U-Net model, CogVideoX/AC3D are DiTs. Resolution, frame count and sampler for CameraCtrl are not stated, and FVD across such models is not comparable. VividCam is *fine-tuned on the test motion types* (§4.2: "We consider diverse simple and complex motions listed in Table 1"), whereas the baselines never saw them, so Table 2/3 measure "fine-tuned vs. not fine-tuned" rather than "synthetic vs. alternative data". The informative baselines are: (a) fine-tuning CogVideoX camera LoRA on the same Unity videos without the disentanglement (Table 4 "w/o A-LoRA" is only reported with human ratings and with an unstated setting), (b) fine-tuning on a modest set of real clips of the same motions, (c) a motion-customization baseline.
- **Suggested Fix:** Add (a) and (b) to Tables 2–3; report resolution/frames for every baseline and, if not equal, re-render FVD at a common size. Cost: ~2 extra fine-tunings per motion set; real clips (e.g., 100 per motion) are a small collection effort for most Table 1 motions.

**W5: FVD with 100 videos per category is unreliable and its reference set is not stated.** §5.3 gives "Each category consists of 100 input prompts", and FVD values range 1488–2577 (Table 2); FVD with ~100 samples is strongly biased by sample size and the reference real set is not given. Differences of 10–50 points (e.g., simple: 1781.90 vs 1808.30) are not interpretable without a variance estimate.
- **Suggested Fix:** State the reference set; report FVD with multiple generation seeds (3 seeds × 100 prompts) and a bootstrap interval; or use a more sample-efficient metric.

**W6: Evaluation of text-based models with trajectory metrics is not defined.** §5.3 says the text model "does not have access to the ground-truth trajectory, making these metrics potentially unfair", yet Table 2 reports TransErr/RotErr for CogVideoX and VividCam-Cog. The pose estimator, the reference trajectory for each text prompt, and how reference trajectories exist for handheld shake or explosive shake are not described.
- **Suggested Fix:** Specify the pose-estimation pipeline (and its failure rate on generated videos), the reference trajectory per prompt, and the scale alignment used for TransErr.

**W7: Reproducibility details are incomplete.** λ, steps, batch size, GPU hours, seeds, the number of X_a videos, the full 100×3 prompt lists (App. B shows examples only) and a code/data release statement are missing (Table 6 has no such entries). §5.1 says the LoRA rank is "128 and 512 for appearance and camera learning" while App. C says "with the LoRA rank fixed at 128".
- **Suggested Fix:** Add the missing hyperparameters, release the Unity scripts and prompt lists, and fix the rank statement.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | §5.1 vs App. C vs Table 6 | "the LoRA rank is 128 and 512 for appearance and camera learning" / "with the LoRA rank fixed at 128" | Camera LoRA rank is 512 in §5.1 and Table 6 but "fixed at 128" in App. C | Cross-referenced three locations | High | MINOR | Correct App. C |
| ERR-2 | E5/E1 | §5.3 vs Table 2 (complex FVD) | "our method preserves video quality, as evidenced by the small FVD difference compared to the vanilla" | Complex FVD 1866.40 vs 1488.36 (+378.04, +25.4%); worst of five methods in that block | Recomputed from Table 2 | High | MAJOR | Qualify the sentence per category |
| ERR-3 | E5/E6 | §1, §4.3, Eq. 5 | "providing appearance-invariant supervision that stabilizes motion learning and strengthens disentanglement" | Eq. 5 is an L1 distance between frame differences, not an optical-flow quantity, and is not appearance-invariant | Read Eq. 5 against the text; no flow estimator defined | High | MAJOR | Rename, justify, or ablate |
| ERR-4 | E8 | §5.4, Table 4 caption | "We conduct a human evaluation and show results in Table 4" | Motion category and model (text/trajectory) for Table 4 not stated; the full row (0.93/0.74) equals the VividCam-Cog Composed row of Table 3 | Cross-referenced Tables 3 and 4 | Medium | MINOR | State the setting |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea but evaluation does not isolate components or control baselines |
| Clarity | 3 | Clear writing; protocol details missing |
| Significance | 2 | Useful for creative control, evidence narrow |
| Originality | 2 | Domain-adapter recipe applied to a new source of data |

### Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim (unconventional motions, realism comparable to real data) is tested with 100-prompt FVD, an unqualified crowd study, no L_flow ablation and uncontrolled baselines; these are signals of a typical rejected submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Unablated loss, misnamed Eq. 5, train-inference LoRA mismatch not examined |
| Clarity & Presentation | 66 | Competent | Readable; protocol and Table 4 setting missing |
| Novelty & Originality | 52 | Developing | Primarily reuse of AnimateDiff-style domain adaptation |
| Significance & Impact | 55 | Borderline | Practical, but evidence narrow |
| Experimental Validation | 42 | Developing | See W1–W6 |
| Reproducibility | 45 | Developing | No code statement, no λ/steps/compute |
| Ethical Compliance | 55 | Competent | No limitations section; $0.03/question |

### Questions for Authors
1. Were checkpoints, λ and LoRA ranks chosen using the 100 evaluation prompts per category? (A held-out prompt set that confirms the Table 2/3 ordering would raise my score.)
2. What is the effect of removing L_flow, and which λ was used? (A clear, non-negative effect would raise my Technical Rigor score; no effect would shift the contribution to A-LoRA and the style prompt.)
3. How many ratings per video and per method were collected, were methods blinded and randomized, and what is inter-rater agreement?
4. Are the test camera motions disjoint from the 500 training videos' motions or the same types?

### Limitations Assessment
**Partially.** There is no limitations section. Suggest adding failure cases (motions that fail), complex-motion FVD degradation, and dependence on simple Unity scenes.

### Ethics Review Flag
**No**, with a note on crowdsourcing compensation (see R3).

### Overall Score
**3 (Borderline Reject)**: A useful, cleanly described recipe, but the evidence for the unconventional-motion and real-data-parity claims is thin and unqualified, and a core component is unablated.

### Confidence
**4**: Confident; figures could not be viewed.

---

# Peer Review Report: Reviewer 2 (Domain)

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Reviewer: Prof. Wen-Li Brandvold, Domain Reviewer (large public university, East Asia; fictional persona)
## Expertise: camera-controllable video diffusion; motion customization
## Date: 2026-11-10

### Summary
The paper proposes VividCam, which fine-tunes CogVideoX-5B (text control) or the AC3D camera encoder (trajectory control) on videos rendered in simple low-poly Unity scenes, using a separately trained appearance LoRA on static-camera renders, a virtual-style prompt token, and a frame-difference loss, then discards the appearance module at inference. It reports improved camera accuracy and human-rated action correctness for composed and complex camera motions at roughly unchanged realism.

### Strengths
**S1: Addresses a real data bottleneck in camera control.** §2.2 correctly notes that annotated datasets are scarce and limited in motion diversity; using programmatic rendering for exact trajectories is a sound idea with a clear route to scaling (App. A: scripts "typically no more than 10 lines").

**S2: Well-chosen contrast with prior synthetic-data work.** §2.3 positions against Fu et al. 2024 and Shuai et al. 2025 (heavy scene design) and against modifying real trajectories (Bai et al. 2025); the low-poly angle is a clear, if narrow, differentiator.

**S3: Covers both text-conditioned and trajectory-conditioned paradigms** (§4.1, Tables 2–3), showing the idea is not tied to one conditioning scheme.

**S4: Practical finding that the style gap can be partly absorbed by a droppable LoRA** (Table 4, Fig. 5 caption), which is a useful negative-result-aware engineering lesson.

### Weaknesses

**W1: The disentanglement mechanism is largely the AnimateDiff domain-adapter idea, and the related work on motion/appearance separation is not engaged.** §4.3 says the scheme was "inspired by AnimateDiff (Guo et al., 2023)" and the paper concedes the technique "has only been used to bridge minor appearance gaps". The bibliography has no motion-customization work that trains separate appearance and motion adapters (MotionDirector, Customize-A-Video, "Separate Motion from Appearance", all prior and verified below), nor flow-guided camera-control training (FloVD). The delta for C2 is therefore: (i) a much larger domain gap, (ii) static-camera renders X_a for the appearance adapter, (iii) a style token, (iv) a frame-difference loss. Each is modest, and none is individually ablated beyond (i)–(iii) in Table 4.
- **Suggested Fix:** Add a related-work paragraph and at least one empirical comparison with a motion-customization pipeline using the same Unity data; state precisely what is new relative to those.

**W2: Positioning against synthetic-data camera control is incomplete.** Free-Form Motion Control (Shuai et al., 2025) and HumanVid (Wang et al., 2024b) are cited as "require substantial manual effort", but no experiment shows that low-poly data is *as good* as high-quality synthetic data, which is the implicit selling point ("synthetic videos do not need to be realistic at all", §6). Without a comparison with training on a higher-fidelity synthetic subset or on those released datasets, "simple suffices" is untested.
- **Suggested Fix:** Train the same pipeline on a subset of an existing synthetic camera dataset and compare; or reduce the claim.

**W3: The "unconventional" label is partly a framing issue.** Table 1 lists push in, tilt up, orbit, handheld shake, dolly zoom, camera rotation; these are standard cinematography vocabulary, and §5.3 shows that the base CogVideoX already handles several (simple RotErr 0.0297). The motivating Dolly zoom (§1) does not appear in any figure caption (Figs. 4, 6, 7, 8) or table. What is shown is *learning prescribed, scripted motions*, not generalization to unseen unconventional motions or to compositions never seen in training.
- **Suggested Fix:** Add a held-out-motion test (train without X, test on X, or on novel compositions) and show Dolly zoom; otherwise retitle the claim as "learning scripted motions from synthetic data".

**W4: The comparison set omits the closest ways of getting the same capability.** No comparison with CameraCtrl II (He et al., 2025, cited in §2.2), ReCamMaster (Bai et al., 2025, cited), or the cited synthetic-data methods; baseline results come from three methods with different architectures (§5.3).
- **Suggested Fix:** Add at least one DiT-based, recent, camera-controlled baseline trained on real data with the same base model.

### Literature-check addendum (strict, cutoff 2025-09-24; 8 queries; arXiv only)

**Per-claim novelty (claim-level profile, `related_search.py novelty`):**
| Claim | Dimension | Novelty | Top prior work (level, label, cited?) | Reasoning |
|-------|-----------|---------|----------------------------------------|-----------|
| C1 synthetic Unity data → camera motion | method | medium | Free-Form Motion Control, Shuai et al. (3, prior peer-reviewed, cited) | Prior work already uses rendered videos for camera/object control; low-poly + disentangle is the delta |
| C2 appearance LoRA + virtual token + frame-difference loss | method | medium | MotionDirector (3, prior arXiv-only, **not cited**); Separate Motion from Appearance (3, **not cited**); FloVD (2, not cited) | Dual-path appearance/motion adapters and flow-guided camera control exist; the combination for a large synthetic gap is the delta |
| C3 precise realistic motion from simple synthetic data | result | medium | Free-Form Motion Control (3, cited) | No prior low-poly result found in 8 queries (arXiv only: a limit of the search, not evidence of novelty) |

Paper reading: no central claim is fully covered by a prior work; one-claim findings are MAJOR at most. Attribution (closest overall): Free-Form Motion Control (arXiv 2501.01425, cited). No text-overlap flag. Baseline scout: no external benchmark in the paper (see Phase 0 log), so no baseline table.

**Novelty delta table:**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited/differentiated? |
|----------------------|--------------------|----------------------|------------------|-----------------------|
| C1 | Free-Form Motion Control (Shuai et al.) | Synthetic videos with controllable camera and object motion for video generation | Very simple low-poly scenes plus appearance disentanglement | Cited, differentiated by "manual effort" only |
| C2 | MotionDirector; Customize-A-Video; Separate Motion from Appearance | Separate appearance and motion adapters for T2V | Static-camera set, virtual token, large synthetic→real gap | Not cited |
| C2 (loss) | FloVD | Optical-flow-guided camera-controlled generation | Frame-difference loss as training signal | Not cited |

**Field snapshot (as of 2025-09):** camera control moved from fine-tuned U-Net adapters (CameraCtrl, MotionCtrl, 2023–24) to DiT-based trajectory conditioning (AC3D, VD3D, CameraCtrl II, 2024–25), with growing use of synthetic and re-rendered data (HumanVid, Free-Form Motion Control, ReCamMaster). Standard metrics remain TransErr/RotErr/FVD on RealEstate10K-style trajectories, with human studies for text-conditioned motion. Open problems stated by the field: complex, non-rigid and long compound motions, dynamic scenes, and scarce annotated data. A significant contribution here is a new capability on motions existing models fail at, demonstrated with controlled baselines, or a clear data-efficiency gain; small gains on RealEstate10K trajectories are incremental. This calibrates Significance below the accepted-paper band unless the complex-motion capability is backed by controlled evidence.

### Missing References (follow the citation-integrity rule; `verify` run with arXiv search)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Zhao et al., "MotionDirector: Motion Customization of Text-to-Video Diffusion Models", arXiv 2023 (found by search, 2023-10) | Separate appearance and motion adapters (dual-path LoRA) for video diffusion: the closest mechanism to the dual adaptation of §4.3 |
| Important | Ren et al., "Customize-A-Video: One-Shot Motion Customization of Text-to-Video Diffusion Models", 2024 (found by search, 2024-02; evidence of peer review in the search record) | Motion adaptation with appearance disentanglement |
| Important | "Separate Motion from Appearance: Customizing Motion via Customizing Text-to-Video Diffusion Models", arXiv 2025-01 (found by search; author list not recalled) | Same decomposition, directly relevant to C2 |
| Important | Jin et al., "FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis", 2025 (found; peer-reviewed per search record) | Optical-flow-based camera-controlled generation: relevant to the flow loss and a possible baseline |
| Helpful | Greff et al., "Kubric: A scalable dataset generator", CVPR 2022 (found, arXiv 2022-03) | Procedurally generated synthetic video data for learning motion; a precedent for sim-to-real training |
| Helpful | Van Hoorick et al., "Generative Camera Dolly: Extreme Monocular Dynamic Novel View Synthesis", ECCV 2024 (found, arXiv) | Synthetic data for learning camera-controlled video generation |
| Helpful | "Learning Camera Movement Control from Real-World Drone Videos", arXiv 2024-12 (found; authors not recalled) | A real-footage alternative for complex camera moves; supports a real-vs-synthetic comparison |
*Worth discussing only (recent preprints, never required):* FlowLoss (arXiv 2025-04), CamCloneMaster (arXiv 2025-06).

**Citation check (E7):** the three citations the argument leans on, AC3D (Bahmani et al., 2025), Free-Form Motion Control (Shuai et al., 2025) and AnimateDiff, match their bibliography entries and are described accurately in §2.3/§4.3. One small slip: §4.1 says the videos are "rendered by a physics engine" while §4.2/App. A use Unity as a rendering engine. "ArtistT2V." (§1) is a bare URL citation without authors.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation does not isolate the contributions |
| Clarity | 3 | Clear overall |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Application of known adapter ideas to a new data source |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful idea with medium novelty against uncited motion-customization work, and gains not demonstrated against controlled baselines.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Approach sound in outline; train/inference mismatch unexamined |
| Clarity & Presentation | 66 | Competent | Clear positioning against synthetic-data work, silent on adapters |
| Novelty & Originality | 52 | Developing | C1–C3 all "medium" in the claim profile |
| Significance & Impact | 58 | Competent | Practical for creators, narrow evidence |
| Experimental Validation | 48 | Developing | Few, non-matched baselines |
| Reproducibility | 50 | Developing | Hyperparameters partial |
| Ethical Compliance | 60 | Competent | Nothing at stake except crowd study |

### Questions for Authors
1. What is the empirical difference from training MotionDirector-style dual LoRAs on the same Unity videos? (A matching or better result would raise Novelty.)
2. Do the test motions of Table 1 occur in the training set? How does the method behave on a held-out motion type?
3. How does low-poly data compare with higher-fidelity synthetic data from an existing dataset?

### Limitations Assessment
**No.** There is no limitations discussion; the narrow scene diversity and simple objects should be discussed.

### Ethics Review Flag
**No**

### Overall Score
**3 (Borderline Reject)**: Interesting use of synthetic data, with medium novelty, uncited motion-customization neighbours, and thin comparisons.

### Confidence
**4**

---

# Peer Review Report: Reviewer 3 (Perspective)

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Reviewer: Dr. Amara Tessendorf, Perspective Reviewer (graphics and virtual-production research institute, Europe; fictional persona)
## Expertise: real-time rendering, cinematography, sim-to-real transfer
## Date: 2026-11-10

### Summary
The paper argues that creative camera moves are rare in real video corpora, so it trains camera control from scripted game-engine renders of cheap low-poly worlds, relying on a droppable appearance adapter and prompt tricks to keep outputs photorealistic. The result is a controllable text-to-video model for moves such as orbits, searches, shakes and rotations, evaluated with automatic metrics and a crowd study.

### Strengths
**S1: A bridge between graphics and generative video that suits production workflows.** A virtual-production practitioner can script a camera move in a few lines (App. A) and get a training set; the idea of treating the engine as a "motion data generator" rather than an image generator is practical and under-explored.

**S2: The finding that appearance can be separated at the weight level is interesting beyond this task.** §4.3 ("the camera control learning no longer needs to learn the same information") suggests a general recipe for any synthetic-to-real transfer where the label (motion) is cheap but the pixels are cheap-looking.

**S3: The motion taxonomy (Table 1) ties each move to a filmmaking purpose** ("Emphasize an object", "Disorient viewer, mark transition"), which makes the evaluation intelligible to creative users.

**S4: Results span both conditioning paradigms and show many qualitative cases** (Figs. 4, 6–8 captions list diverse content prompts); I could not view the images, so I judge only from captions.

### Weaknesses (framed as opportunities)

**W1: Camera semantics that are not extrinsics are not represented.** "Dolly zoom", "zoom in", and "locks focus" (§1, Fig. 4, Fig. 6 prompts) involve changing focal length and depth of field, not only camera pose. The trajectory branch uses Plücker embeddings of poses (§3); how focal-length change and focus pulls are encoded, rendered in Unity, and learned from low-poly scenes with no depth-of-field is not explained. 
- **Suggested Fix:** State how intrinsics and focus are handled; add dolly-zoom (a classic, easily checked motion) and a field-of-view trace as a quantitative test.

**W2: Assumption that motion is separable from scene content and scale.** Camera speed and extent in low-poly scenes with a few cubes and spheres (App. A) may not transfer to scenes with people or large depth ranges; "pushes in" at constant speed in Fig. 4 row 1 is read from a stone's apparent size. A test with scale- and depth-varying real scenes and dynamic subjects would establish the assumption.
- **Suggested Fix:** Evaluate on prompts with varying depth/scale and with strong object motion, and report failures.

**W3: Crowdsourcing and misuse not discussed.** App. E states "Each question is awarded $0.03" with 88 workers; the time per question and effective hourly wage are not given, and no consent/IRB or exemption statement is made. The paper has no limitations or broader-impact text, though better camera control for generative video also benefits deepfake and misleading-footage production.
- **Suggested Fix:** Report time per question and effective wage; add a short limitations and impact paragraph.

**W4: No real-world-user or practitioner evaluation of "creative" value.** The motivation is artistic originality (§1), but all judgments come from anonymous crowd ratings of short clips.
- **Suggested Fix:** A small study with video editors or cinematographers, or at least a comparison to professional-footage references for complex moves.

### Cross-disciplinary suggestions
Procedural content generation and domain randomization (sim-to-real in robotics) are the natural lens: randomizing scene textures, lighting and object categories, and measuring leakage with a synthetic-style classifier, would make "disentanglement" measurable. Virtual-production previsualization tools could supply richer yet still cheap scene variation. A reference like Kubric (procedural synthetic video) is a precedent. Future directions: camera-aware 3D consistency checks with SfM, and mixing in a few real shake/zoom clips.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound recipe, partly under-tested |
| Clarity | 3 | Clear |
| Significance | 3 | Useful for creators |
| Originality | 3 | New use of engine data for camera control |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean, practically useful finding for a popular area (camera control in video generation) and a clear idea, offset by thin evidence.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Reasonable design |
| Clarity & Presentation | 70 | Competent | Readable and well organized |
| Novelty & Originality | 62 | Competent | Useful combination in a new setting |
| Significance & Impact | 68 | Competent | Practical creative-tool value |
| Experimental Validation | 56 | Competent | Adequate but not controlled |
| Reproducibility | 55 | Competent | Engine scripts easy to recreate; code not promised |
| Ethical Compliance | 52 | Developing | No limitations/impact text; $0.03/question |

### Questions for Authors
1. How are focal length and focus changes represented in X_c and in the trajectory encoder? 
2. What is the hourly wage implied by the $0.03 payment and observed task times, and was ethics review obtained or waived?
3. Could you show failure cases on dynamic, large-depth scenes?

### Limitations Assessment
**No.** Add a limitations section.

### Ethics Review Flag
**No**: but worker compensation should be clarified (see W3). 

### Overall Score
**4 (Borderline Accept)**: Appealing and practical idea in a popular area; weaknesses are addressable by analysis and added controls.

### Confidence
**3**: Not a video-diffusion specialist; figures not viewed.

---

# Peer Review Report: Reviewer 4 (Generalist)

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Reviewer: Dr. Rafael Kowalczyk-Nair, Generalist Reviewer (university vision group, South America; fictional persona)
## Expertise: general computer vision
## Date: 2026-11-10

### Summary
VividCam fine-tunes pretrained text-to-video diffusion models for camera control using cheaply rendered synthetic videos. To stop the model from inheriting the synthetic look, it trains an appearance LoRA on static-camera renders first, then a camera module on moving-camera renders, drops the appearance LoRA at inference, and adds a virtual-style prompt token and a frame-difference loss. It reports better camera accuracy and human-rated correctness on composed and complex motions than CameraCtrl, CogVideoX and AC3D, with realism roughly maintained.

### Venue fit and criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported by the evidence | Partly | Tables 2–5; complex FVD, Table 5 control dataset |
| Presentation: clear, organized | Met | §§1, 4, 5 |
| Contribution: significance and novelty for the audience | Partly | §1 contributions; medium novelty |
| Reproducibility signals | Partly | App. C, Table 6; no code statement |
| Limitations stated | Not met | no section |

### Strengths
**S1: A clear, memorable idea and a well-motivated problem.** The "paradox" between data-hungry training and creative camera control (§1) is stated crisply and the answer, learn motion from cheap synthetic data, is easy to understand and to re-implement.

**S2: Good organization.** Notation in §3–4 is introduced once; Fig. 3 captions summarize the pipeline; Table 1 organizes the motions; the appendix has hyperparameters (Table 6) and prompts (App. B).

**S3: Pragmatic and surprising result.** That clips of "basic geometries within a low-poly 3D scene" (Abstract) suffice to teach a 5B video model to follow compound motions is of interest to this venue's audience.

**S4: Reasonable mix of evidence:** automatic metrics, human study, CLIP (App. F), ablations (Tables 4–5), and qualitative comparisons (Figs. 7–8).

### Weaknesses

**W1: The headline claims are phrased more broadly than the evidence.** "Comparable to models trained on real footage" (§1) rests on Table 5, where the "real" data are RealEstate10K clips whose motions the authors describe as of "limited diversity" (§5.4), and the differences (0.91/0.72 vs 0.88/0.75) are given without variance. "Notably, we show that synthetic videos do not need to be realistic at all" (§6) is not tested against a realistic synthetic alternative.
- **Suggested Fix:** Narrow the wording to what Table 5 shows, or add a real-data comparison on the unconventional motions.

**W2: The evaluation is hard to follow and tables are weakly connected to claims.** Table 4 and Table 5 do not state which motion category/model/prompts they use, and App. E ("150 videos") does not say whether this covers all methods. A reader cannot tell which numbers support which claim; the contribution bullets (§1, items 2–3) are result statements rather than separable contributions.
- **Suggested Fix:** Add a one-line setting to each table caption; restate contributions as method / finding / evidence.

**W3: Missing limitations and failure analysis.** No failure cases are shown (e.g., motions where VividCam is not better: Table 2 simple RotErr 0.0407 vs 0.0297 for CogVideoX; Table 3 VividCam-AC3D simple Action Correctness 0.74 = AC3D) and no limitations section exists; a venue audience expects it.
- **Suggested Fix:** Add a limitations paragraph and a small failure-case figure.

*Minor:* "wepresent" (§4), "Mechinical" (Fig. 9), "ArtistT2V." bare reference, "physics engine" (§4.1) vs rendering engine.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound recipe, partial controls |
| Clarity | 3 | Clear |
| Significance | 3 | Useful |
| Originality | 3 | New application |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea with an interesting finding, offset by some overclaiming and a thin evaluation; weaknesses are of a kind accepted papers also have.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Standard but sound approach |
| Clarity & Presentation | 72 | Competent | Well organized; table settings missing |
| Novelty & Originality | 62 | Competent | Novel combination |
| Significance & Impact | 66 | Competent | Useful for creators |
| Experimental Validation | 54 | Developing/Competent | Limited baselines/controls |
| Reproducibility | 55 | Competent | Partial |
| Ethical Compliance | 58 | Competent | Limited discussion |

### Questions for Authors
1. Which category, model and prompts does Table 4 use? Confirm whether the full row equals the VividCam-Cog Composed row of Table 3.
2. In Table 5, how many videos form "Virtual data" (500 or 1000)? If more than "Mixed", is data size controlled?
3. Would you narrow "comparable to real footage" to the RealEstate10K setting?

### Limitations Assessment
**No.**

### Ethics Review Flag
**No**

### Overall Score
**4 (Borderline Accept)**: A clear and interesting idea whose evidence is adequate but not strong; I lean to accept because the weaknesses are fixable and typical.

### Confidence
**3**

---

# Devil's Advocate Report

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Reviewer: Prof. Selin Haverford-Duarte, Devil's Advocate (university statistics/ML department, Middle East; fictional persona)

## Steelman
Camera-control methods are bounded by the motions present in annotated real data. VividCam shows that a few hundred programmatically rendered, visually crude clips, plus a droppable appearance adapter, can add new camera behaviours to a frozen 5B video model without visibly harming realism, a cheap and general recipe supported by automatic and human evaluation.

## Core Argument Chain
1. Real data lack unconventional camera motions (§1, "infeasible" to collect).
2. Synthetic engines can render arbitrary motions cheaply (§4.2, App. A).
3. Training on synthetic videos hurts realism, but an appearance LoRA, a style token and a flow loss remove the synthetic look (§4.3).
4. Fine-tuned models follow complex motions better than baselines (Tables 2–3) at comparable realism (Tables 3–5).
∴ Unconventional camera motions can be learned without real training videos, and realism need not suffer.

## Strongest Counter-Argument
The paper's causal story is that the appearance LoRA *absorbs* synthetic appearance so the camera module learns only motion. The evidence does not isolate that story. First, the comparison conflates two things: VividCam models are fine-tuned on the very motion types (Table 1) they are then tested on, whereas the baselines never saw them. A gain on "composed" motions (TransErr −56.8%, derived) is what any fine-tuning on those motions would produce and says nothing about synthetic versus real data; the one real-data control (Table 5) uses RealEstate10K, which the authors themselves say has "limited diversity of camera motions", so it cannot show that synthetic data is *as good as* real data for unconventional motions. Second, on the category the paper cares about most, complex motions, automatic evidence is weak: TransErr −7.3% and RotErr −1.1% against vanilla CogVideoX, with FVD 25% worse (Table 2). The claim then hinges on a crowd study (0–2 ratings, $0.03 per question, no variance, no agreement) where realism for VividCam-AC3D equals AC3D (0.65 vs 0.65). Third, the loss said to provide "appearance-invariant supervision" is a frame difference that is not appearance-invariant and is not ablated, and the appearance adapter is removed at inference after the camera module was trained on top of it, a train/test weight mismatch not examined. A simpler explanation for the results is that any brief fine-tuning on scripted trajectories improves following of those trajectories, and that the style token and LoRA reduce, but are not shown to remove, leakage; leakage is never measured directly. The authors need a matched real-data or high-fidelity-synthetic control and a leakage measurement to support the title claim.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main claim is weakened (not contradicted) by the evidence: Table 2/3 still favour VividCam on composed and complex motions by human rating, no protocol selection on a labelled test set is stated, and the issues above can be fixed by narrowing claims and adding controls.

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| (none) | | | | | |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence/Scope | §4.2, §5.3, Table 2–3 | Test motions equal training motion types; baselines never fine-tuned on them; gains reflect fine-tuning, not synthetic-versus-real data. No generalization to unseen motions | Add held-out-motion test and a real-clip or high-fidelity-synthetic fine-tuning baseline |
| DA-M2 | Evidence | Table 2 (complex), §5.3 | Complex-motion FVD +25.4% vs CogVideoX described as "small"; metric gains of 7.3% (TransErr) and 1.1% (RotErr) | Per-category honest statement, CIs, better metric |
| DA-M3 | Logic | §1, §4.3, Eq. 5 | "appearance-invariant" claim for a frame-difference loss; no L_flow ablation; λ unknown | Ablate, rename, justify |
| DA-M4 | Evidence | §5.4, Table 5 | "Comparable to real footage" tested only on RealEstate10K; no variance; differences of 0.03 | Narrow claim; add real unconventional-motion data |
| DA-M5 | Method validity | §4.3 (Eq. 4), Inference | Camera module is trained in the presence of a frozen appearance LoRA but deployed without it; train/test mismatch; leakage never measured (no style classifier, no distribution metric) | Test inference with/without A-LoRA; measure style leakage |
| DA-M6 | Evidence | App. E, Table 3 | Crowd study unqualified (no variance, blinding, agreement, rating counts, 150-video ambiguity) | Full protocol and statistics |
| DA-M7 | Overclaim | Abstract, §1, §6 | "releasing the reliance on collecting realistic training videos"; "cost-efficient" — no cost numbers; no real-data baseline on target motions | Quantify engineering hours; narrow wording |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §5.1 vs App. C | Camera LoRA rank 512 vs "fixed at 128" |
| DA-m2 | Reporting | §5.3, Table 2 | RotErr/TransErr for text-only models with no defined reference trajectory (and "potentially unfair" by the authors' own admission) |
| DA-m3 | Reporting | Table 4 | Setting unstated; the full-model row equals a Table 3 row |
| DA-m4 | Motivation | §1, Figs. 4, 6–8 | Dolly zoom, the motivating example, is not in any caption or table |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Complex FVD, VividCam-Cog vs CogVideoX (§5.3 "small FVD difference") | 1866.40 vs 1488.36 | +378.04 (+25.4%) | No ("small" is not supported) |
| Composed TransErr, VividCam-Cog vs CogVideoX | 0.2208 vs 0.5107 | −0.2899 (−56.8%) | Large gain, as the table shows |
| Complex TransErr, VividCam-Cog vs CogVideoX | 0.4011 vs 0.4327 | −0.0316 (−7.3%) | Small gain |
| Complex RotErr, VividCam-Cog vs CogVideoX | 0.5013 vs 0.5067 | −0.0054 (−1.1%) | Negligible |
| Complex TransErr, VividCam-AC3D vs AC3D | 0.3376 vs 0.4271 | −0.0895 (−21.0%) | Solid gain |
| Table 4 full row vs Table 3 VividCam-Cog Composed | 0.93/0.74 vs 0.93/0.74 | identical | Setting unstated |
| Abstract/§1 claims vs tables | no numeric claim in abstract | n/a | — |

## Ignored Alternative Explanations
- Fine-tuning on any scripted trajectories for these specific motions would improve trajectory adherence regardless of the data source.
- The CogVideoX baseline's low Action Correctness on composed motions (0.53) may reflect prompt-format brittleness rather than missing capability; a prompt-engineering control is absent.
- Realism ratings may be insensitive to residual low-poly style because raters judge short 49-frame clips at 720×480 on a 0–2 scale.
- Observed FVD differences may be sample-size noise at n = 100.

## Missing Stakeholder Perspectives
Professional cinematographers and editors (value of "unconventional" motions); crowd workers (compensation); people affected by easier synthetic-footage production.

## Observations (Non-Defects)
The authors openly report that CogVideoX is better on simple/composed RotErr (§5.3); they ablate the two principal disentanglement tools; the task framing is crisp; a single LoRA and a single encoder serve all motions (§5.1), which is a point in favour of generality.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Unablated, misnamed loss; train/test LoRA mismatch |
| Clarity & Presentation | 66 | Clear; missing settings |
| Novelty & Originality | 50 | Known adapter ideas, medium novelty per claim profile |
| Significance & Impact | 55 | Useful, narrowly shown |
| Experimental Validation | 42 | Confounded comparison; weak variance reporting |
| Reproducibility | 45 | Key hyperparameters and release missing |
| Ethical Compliance | 52 | No limitations, low pay unexplained |

## Overall: 3 | Confidence: 4

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 complex-motion evidence | kept | Numbers recomputed from Table 2 |
| R1 | W2 human study | kept | App. E confirms the gaps; checked that no variance/agreement/blinding statement exists |
| R1 | W3 flow loss | kept | Eq. 5 read; no ablation in §5.4 |
| R1 | W4 baselines | rewritten | Narrowed to what the paper states (§5.3 "official implementations"); resolution of baselines is a question, not an error |
| R1 | W5 FVD | kept | Table 2 values and §5.3 sample count |
| R1 | W6 trajectory metrics for text models | kept | §5.3 says metrics "potentially unfair"; protocol absent after search |
| R1 | W7 reproducibility | kept (reordered last) | λ, steps, compute absent after search |
| R1 | ERR-1, ERR-4 | moved to Minor | Cosmetic/omission, low impact |
| R2 | W1 adapters not cited | kept | Bibliography checked: MotionDirector, Customize-A-Video, FloVD absent |
| R2 | W3 "unconventional" | rewritten | Dolly zoom absence judged from captions only (figures unavailable) |
| R3 | W1 intrinsics/focus | rewritten as question | Cannot verify how intrinsics are encoded; paper silent |
| R3 | W3 crowd compensation | kept | App. E quote verified |
| R4 | W2 table settings | kept | Table 4/5 captions checked |
| R4 | Typos | moved to Minor | cosmetic |
| DA | M1–M7 | kept | All located; DA-M5 phrased as a method question (mismatch is stated in §4.3/Inference) |

No weakness was dropped as already answered by the appendix. Scores unchanged.

---

## Phase 2: EIC Meta-Review and Decision

### Synthesizer, Part A: issue map and official score

**Master issue list (classification):**
| Issue | Sources | Class |
|-------|---------|-------|
| Complex-motion evidence weak; FVD worse; reliance on crowd study | R1-W1, DA-M2, R4-W3 | CONSENSUS-3 |
| Human study under-specified (variance/blinding/agreement); low pay | R1-W2, DA-M6, R3-W3 | CONSENSUS-3 |
| No ablation of L_flow; misnamed/not appearance-invariant; λ missing | R1-W3, DA-M3, R2-W1 (partly) | CONSENSUS-3 |
| Confounded baselines; test motions = training motions; no matched real/synthetic control | R1-W4, R2-W3/W4, DA-M1, DA-M4, R4-W1 | CONSENSUS-4 |
| Missing/unspecified protocol for text models' trajectory metrics; FVD reliability | R1-W5/W6, DA-m2 | CONSENSUS-2 |
| Uncited motion-customization and flow-guided camera-control work; medium novelty | R2-W1/W2 + addendum, R3 (suggestions) | SOLO (R2) |
| Intrinsics/focus handling; scale/depth transfer | R3-W1/W2 | SOLO |
| No limitations section / broader impact | R3-W3, R4-W3, R1 | CONSENSUS-3 |
| Reproducibility gaps | R1-W7, DA | CONSENSUS-2 |
| Overclaim "comparable to real footage" / "cost-efficient" | R4-W1, DA-M4, DA-M7 | CONSENSUS-2 |
| Train/inference LoRA mismatch; leakage unmeasured | DA-M5 | SOLO |
| SPLIT | R3/R4 (Overall 4: fixable, typical) vs R1/R2/DA (Overall 3: evidence insufficient) | SPLIT on overall |

**DA-CRITICAL issues:** none. **Hinge issues:** evidence on complex motions and the Table 5 real-data control.
**Official score:** plain mean rating 3.40, composite 55.5 (see score tables below). Consistency warnings: none flagged (spread ≤ 14 on all dimensions).

### EIC Meta-Review (Prof. Marit Solheim-Adeyemi)

### The Case For and Against
- **For acceptance:** A clear, practical and somewhat surprising idea: very simple rendered clips plus a droppable appearance adapter let a frozen 5B video model follow scripted camera moves, with strong gains on composed motions and a human-rated advantage on complex ones. The paper reads well, covers two conditioning paradigms and ablates the disentanglement components. The weaknesses (single configuration, crowd-study details) are common among accepted papers.
- **Against acceptance:** The headline claims (unconventional motions, parity with real data, an appearance-invariant loss) are stronger than the evidence: complex-motion automatic metrics barely move while FVD worsens by 25%, the real-data control is a low-diversity indoor dataset, one of three "components" (the loss) has no ablation, baselines are architecture-mismatched and not trained on the test motions, and variance/protocol for the human study are absent.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Complex FVD 1866.40 vs 1488.36 called "small difference" | R1-ERR-2, DA-M2 | Table 2; §5.3 | **Verified** | Recomputed +378.04 (+25.4%); worst of five in the block. The phrase quoted exists in §5.3 |
| Complex TransErr −7.3%, RotErr −1.1% for Cog; composed TransErr −56.8% | R1-W1, DA | Table 2 | **Verified** | Arithmetic reproduced |
| VividCam-AC3D RotErr worse than AC3D on simple and composed | R1-W1 | Table 2 | **Verified** | 0.1162 vs 0.0973; 0.1968 vs 0.1958 (the second gap is tiny) |
| No ablation of the flow loss | R1-W3, DA-M3 | §5.4, Tables 4–5 | **Verified** | Searched "flow" in §5.4: only §4.3/Eq. 5 and the introduction |
| Eq. 5 is a frame difference, not "appearance-invariant" | R1-ERR-3, DA-M3 | Eq. 5, §1 | **Verified** (appearance-invariance is a reasoned inference, Medium-High) | Text says "aligning frame-to-frame differences between predictions and ground truth" |
| LoRA rank 128 vs 512 inconsistency | R1-ERR-1 | §5.1, App. C, Table 6 | **Verified** | Minor |
| Table 4 setting unstated; full row equals Table 3 composed row | R1-ERR-4, R4-Q1 | Tables 3–4 | **Verified** | Cannot confirm it is the same setting |
| Table 5 "real" data is RealEstate10K, "limited diversity" | R4-W1, DA-M4 | §5.4 | **Verified** | The authors' own hypothesis sentence |
| Test motions equal training motion types | DA-M1, R2-W3 | §4.2, §5.1 | **Partly correct** | §4.2 says training uses "diverse simple and complex motions listed in Table 1" and §5.1 evaluates the same categories; whether specific test trajectories are disjoint from training ones is not stated |
| Dolly zoom absent from results | R2-W3, DA-m4 | Figs. 4, 6–8; Table 1 | **Partly correct** | Absent from the captions and text; figures not visible, so images are unverified |
| Trajectory metrics for text-only models undefined | R1-W6 | §5.3, Table 2 | **Verified** | §5.3 admits the limitation, supplies no protocol |
| Human-study details missing (blinding, agreement, ratings per video) | R1-W2, DA-M6 | App. E | **Verified** | Searched App. E; none present. "150 videos" ambiguity real |
| Missing motion-customization citations | R2-W1 | Reference list | **Verified** | Not in the bibliography; mechanism similarity is **Partly correct** (it is a related mechanism for separating motion/appearance, not the same task) |
| Camera module deployed without the adapter it was trained with | DA-M5 | §4.3 Inference | **Verified** as a design fact; its harm is unmeasured (hypothesis) | Raise as a question |
| Crowd pay $0.03/question | R3-W3 | App. E | **Verified** | Time per question unknown; hourly wage unverifiable |
| Missing limitations section | R3, R4 | Whole paper | **Verified** | |

Literature-check points: R2's missing references are all prior (peer-reviewed or arXiv-only 6+ months) and found by `verify`/search, so they stay Important at most. Recent preprints (FlowLoss, CamCloneMaster) are discussion-only and did not lower any score. No claim is "known"; no criterion-7 issue.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log item I rechecked reproduced (complex FVD, Eq. 5, rank mismatch); decisive points verified; well calibrated to ICLR |
| R2 (Domain) | 3 | 4 | 1.0 | Citation gaps verified; mechanism-overlap framing slightly strong but within bounds |
| R3 (Perspective) | 4 | 3 | 1.0 | Accurate points (compensation, limitations); rating less informed by the numeric evidence but not overstated |
| R4 (Generalist) | 4 | 3 | 1.0 | Sound, flags the overclaim; no verified error either way |
| DA | 3 | 4 | 1.0 | Argument largely survives my check; DA-M5 and "frame difference is not appearance-invariant" are plausible but not measured, so no upweighting |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

I independently checked the criteria: no evidence contradicts the main claim (VividCam does beat baselines on composed motions and on human-rated complex motions); the experiments can test the claim in a weaker form; no test-set selection is stated (protocol not stated: a question, MAJOR at most); no fabrication/ethics violation signal. No ceiling applies.

### Final Decision and Justification
The EIC-weighted rating is 3.34, so the starting point is **3 (Borderline Reject)**; the plain mean is 3.40, and the 0–100 composite (54.9) falls in the same band, so both signals agree. I do not depart from the starting point: no verified issue is missing from the ratings, and I found no reviewer rating that rests on an incorrect or overstated claim. The decisive evidence is on the paper's own central terms. (1) The "unconventional-motion" win is concentrated in composed motions, while for complex ones the automatic metrics barely improve and FVD is 25% worse (Table 2). (2) The realism-parity claim has one control, on RealEstate10K, which the authors say lacks motion diversity (§5.4), so it cannot test the title claim. (3) One of the two training components (the loss) is unablated and misdescribed, and the comparison conflates fine-tuning on the test motions with the use of synthetic data. My pool position is **52**: better than about half of ICLR submissions, a typical-rejected-submission position just below the 55–69 borderline band. R3 and R4 (66) weigh the neat idea and the writing more heavily; the disagreement with R1/R2/DA (45–50) is 21 points at most (below the 30-point threshold), and the evidence behind it (items 1–3 above) is verified. The decision does not exceed any DA ceiling (none exists). The weaknesses are fixable (an L_flow ablation, a real-clip/high-fidelity-synthetic baseline, per-category intervals, honest claims), so this is a *borderline* reject, and a revised version with those controls would plausibly be a competitive submission.

---

## Score Summary

### Official Scores and EIC Assessment

*Output of `aggregate_scores.py scores.json --venue iclr --final 3` (with the EIC's `eic_weight` values).*

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 56 | 62 | 60 | 48 | 55.2 | 54.5 | 14 |
| Clarity & Presentation | 66 | 66 | 70 | 72 | 66 | 68.0 | 67.7 | 6 |
| Novelty & Originality | 52 | 52 | 62 | 62 | 50 | 55.6 | 55.0 | 12 |
| Significance & Impact | 55 | 58 | 68 | 66 | 55 | 60.4 | 59.6 | 13 |
| Experimental Validation | 42 | 48 | 56 | 54 | 42 | 48.4 | 47.6 | 14 |
| Reproducibility | 45 | 50 | 55 | 55 | 45 | 50.0 | 49.4 | 10 |
| Ethical Compliance | 55 | 60 | 52 | 58 | 52 | 55.4 | 55.4 | 8 |
| **Composite** | 51.0 | 54.9 | 60.8 | 60.5 | 50.1 | **55.5 (before)** | **54.9 (after)** | |
| Pool position (P%) | 45 | 50 | 66 | 66 | 45 | | | |

Official ratings: R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40**. EIC-weighted rating (R1 weight 1.25, others 1.0): **3.34** → starting point 3. Before-run (no EIC weights) EIC-weighted rating 3.35 and composite 55.1.

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); skill Overall 3 (Borderline Reject) |
| Confidence (1–5) | 3–4 (reviewer range) |

*Scale labels are the skill's translation of the internal Overall; the ICLR scale is `secondary`, so treat the wording as unverified against the current form.*

---

## Editorial Decision

## Paper: VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: Empirical
## Review Team (fictional personas): EIC Prof. Marit Solheim-Adeyemi; R1 Dr. Joaquín Aldermere; R2 Prof. Wen-Li Brandvold; R3 Dr. Amara Tessendorf; R4 Dr. Rafael Kowalczyk-Nair; DA Prof. Selin Haverford-Duarte

## Decision: Borderline Reject (3), ICLR rating 4 on {0,2,4,6,8,10}

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 55.5
**EIC assessment** (internal): weighted rating 3.34 → starting point 3 · weighted composite 54.9 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3

### Editorial Decision Letter

Dear Authors,

Thank you for submitting "VividCam: Learning Unconventional Camera Motions from Virtual Synthetic Videos" to ICLR. The question of whether cheap, programmatically rendered videos can teach a video diffusion model new camera behaviour is a timely and interesting one.

**Overall Assessment:** The panel found a clear, practical idea that is easy to understand and presented well, and was split between a lean to accept (R3, R4) and a lean to reject (R1, R2, DA). The reasons to reject concern how the central claims are tested, not whether the idea is sound.

**Key Strengths Identified by Reviewers:**
1. A simple, well-motivated disentanglement recipe (appearance adapter on static-camera renders, discarded at inference) with a cheap data pipeline (R1, R2, R3, R4).
2. Clear gains on composed motions and a human-rated advantage on complex ones, across both text and trajectory control (R1, R4, DA).
3. Clear writing, motion taxonomy tied to filmmaking purposes, and openness about unfavourable numbers (R3, R4, R1).

**Key Concerns Requiring Attention:**
1. The baselines and controls do not isolate "synthetic data" from "fine-tuning on the test motions"; a real-clip or high-fidelity-synthetic comparison on the unconventional motions is needed, and the real-data control (RealEstate10K, Table 5) is low-diversity (CONSENSUS-4).
2. On complex motions, automatic metrics barely improve (TransErr −7.3%, RotErr −1.1% vs CogVideoX) and FVD is 25% worse, described as "small"; the claim rests on a crowd study without variance, blinding or agreement (CONSENSUS-3).
3. The frame-difference loss (Eq. 5) is described as optical-flow based and appearance-invariant, has no ablation, and its weight λ is unreported (CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The strongest challenge is that the results could be explained by fine-tuning on scripted trajectories regardless of data source, and that style leakage is never measured; this must be addressed in any revision.

**Decision: Borderline Reject (3)**

Our judgment is that the contribution is real but the evidence does not yet support the stated claims at ICLR's bar. A revision with an L_flow ablation, controlled real/synthetic baselines on the complex motions, per-category intervals for the metrics and the human study, narrowed wording, and a limitations section would address the gap. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Marit Solheim-Adeyemi
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Confounded baselines; fine-tuned on test motion types; no matched real/synthetic control; overclaim of real-data parity | R1, R2, R4, DA | CONSENSUS-4 |
| Weak complex-motion evidence, FVD worse | R1, R4, DA | CONSENSUS-3 |
| Human study under-specified; compensation | R1, R3, DA | CONSENSUS-3 |
| Flow loss unablated and misdescribed | R1, R2, DA | CONSENSUS-3 |
| No limitations section | R1, R3, R4 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall lean | R3, R4 (4: idea and writing outweigh fixable gaps) | R1, R2, DA (3: evidence insufficient) | The verified evidence points to the lower side; all weaknesses named are about the central claims, not polish |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag (max 14, Technical Rigor/Experimental Validation). The upper reviewers (R3, R4) score Experimental Validation 54–56 vs R1/DA 42; I adopt the lower view because the verified complex-motion numbers and missing controls match it.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Test motions = training motions; no matched control | Yes (R1-W4, R2-W3/W4) | n/a | n/a |
| DA-M2 | MAJOR | Complex-motion FVD "small" | Yes (R1-W1) | n/a | n/a |
| DA-M3 | MAJOR | Flow loss claim, no ablation | Yes (R1-W3) | n/a | n/a |
| DA-M4 | MAJOR | Real-data parity claim | Yes (R4-W1) | n/a | n/a |
| DA-M5 | MAJOR | Adapter train/inference mismatch, leakage unmeasured | No | n/a | n/a |
| DA-M6 | MAJOR | Human study protocol | Yes (R1-W2, R3-W3) | n/a | n/a |
| DA-M7 | MAJOR | "Cost-efficient"/"releasing the reliance" overclaim | Partly (R4-W1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Verified issues that undermine a main claim (no upheld DA-CRITICAL issue).*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Controls do not isolate synthetic data from fine-tuning on the test motions; no real-clip or high-fidelity-synthetic baseline; real-data control (RealEstate10K) low-diversity | R1-W4, R2-W2/W3/W4, R4-W1, DA-M1, DA-M4 | §5.3–5.4, Tables 2–3, 5 | Add fine-tuning baselines on (a) real clips of the Table 1 motions, (b) a subset of an existing synthetic camera dataset, (c) naive synthetic fine-tuning; add a held-out-motion test; narrow "comparable to real footage" | High; ~10–30 GPU-hours (LoRA fine-tuning of a 5B model, 3–5 runs) plus data gathering | Partly (a small set is feasible in a week) |
| R2 | Complex-motion evidence: FVD +25.4%, metric gains of 7.3% / 1.1% vs CogVideoX, described as "small" | R1-W1/ERR-2, DA-M2 | §5.3, Table 2 | Per-category honest statement; paired bootstrap CIs; motion metric suited to shakes/rotations; reword the sentence | Low–Medium; analysis plus ~100 videos per method | Yes |
| R3 | Flow loss (Eq. 5) misdescribed and unablated; λ unknown | R1-W3/ERR-3, DA-M3 | §1, §4.3, Eq. 5, Table 4 | Ablate L_flow and sweep λ; rename or use a real flow estimator; state timestep weighting | Medium; ~3 trainings (a few GPU-hours each) | Yes |
| R4 | Human study protocol and statistics (carries the complex-motion claim) | R1-W2, DA-M6, R3-W3 | App. E, Table 3 | Per-method counts, ratings per video, blinding/randomization, agreement, CIs, paired tests, effective hourly wage and ethics status | Low–Medium; analysis of existing ratings | Yes (if raw ratings kept) |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Comparison fairness: baseline architecture/resolution/frame count differ; FVD with 100 videos and unstated reference set | R1-W4/W5, DA-M2 | Common-size re-rendering, multi-seed FVD with intervals; state reference set | Medium | Yes |
| S2 | Trajectory metrics for text-based models undefined | R1-W6, DA-m2 | Specify pose estimator, reference trajectories, alignment; failure rate | Low | Yes |
| S3 | Adapter train/inference mismatch; style leakage unmeasured | DA-M5 | Test inference with/without A-LoRA; leakage metric (style classifier or feature-distribution distance) | Medium | Partly |
| S4 | Literature: motion/appearance adapters and flow-guided camera control | R2-W1, addendum | Cite and discuss MotionDirector, Customize-A-Video, Separate Motion from Appearance, FloVD; one empirical comparison | Medium | Partly |
| S5 | Intrinsics/focus handling, dolly zoom not shown | R3-W1, R2-W3, DA-m4 | State encoding; add dolly zoom with an FOV trace | Medium | Partly |
| S6 | Reproducibility: λ, steps, batch size, compute, seeds, X_a size, full prompt lists, code/data release; rank inconsistency (§5.1 vs App. C) | R1-W7/ERR-1, DA-m1 | Add and release Unity scripts and prompts | Low | Yes |
| S7 | Limitations, failure cases and broader impact missing | R3-W3, R4-W3 | Add a section with failure cases and misuse discussion | Low | Yes |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Table 4/5 settings unstated; Table 4 full row equals Table 3 composed row | R1-ERR-4, R4-W2 | Add the setting to each caption |
| N2 | "Unconventional" framing; motions are standard cinematography | R2-W3 | Reword, or add truly novel motions |
| N3 | Scale/depth transfer and dynamic scenes | R3-W2 | Evaluate varied depth and strong object motion |
| N4 | Practitioner study | R3-W4 | A small study with editors/cinematographers |
| N5 | Cross-disciplinary suggestions (domain randomization, procedural generation) | R3 | Discuss in future work; cite Kubric |
| N6 | Typos, bare URL citation, "physics engine" wording | R4, R2 | Fix |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–3 weeks (new fine-tunings plus a real-clip set; 10–30 GPU-hours of fine-tuning plus analysis).
- Priority 2: 7 items, about 1 week.
- Priority 3: 6 items, a few days.
- **Total estimated revision time**: about 3–4 weeks.

---

*Simulation notice: this is how a careful panel would likely see this draft, not a prediction of any real outcome.*
