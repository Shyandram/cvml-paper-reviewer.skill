# Simulated Review — "Mitty: Diffusion-based Human-To-Robot Video Generation"

*Full mode · target venue ICLR · literature check: strict (cutoff 2025-09-24) · date 2026-11-05. This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome. The panel is five role-based passes sharing one model context (no independent agents ran). Figures were not available: figure-dependent claims are judged from captions and text only.*

---

# PHASE 0 — Paper Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Mitty: Diffusion-based Human-To-Robot Video Generation |
| Primary Discipline | Computer Vision → conditional video generation (video diffusion transformers) |
| Secondary Discipline(s) | Robotics → learning from human demonstrations; egocentric video; data synthesis |
| Paper Type | Empirical (composite weights: empirical). It also builds a synthetic paired dataset, but the main contribution is a method evaluated on benchmarks |
| Core Technique(s) | Wan 2.2 video DiT (TI2V-5B, 14B MoE) with LoRA; clean human-latent tokens concatenated with noisy robot-latent tokens ("in-context learning", "bidirectional attention"); hand-pose → IK → robot-arm rendering pipeline for synthetic pairs |
| Target Venue | ICLR (top-tier ML conference; stated by the user); profile key `iclr` (2026 cycle, scale status *secondary*) |
| Venue-Specific Notes | None. ICLR submissions and reviews are public; revised PDFs allowed during discussion |
| Paper Maturity | Submission-ready draft with notable rough edges (naming and table inconsistencies, a stray GPT mention in the supplement) |
| Ethics-Relevant Content | Re-use of egocentric datasets (EPIC-Kitchens, Ego4D) under their licences; videos sent to commercial editing APIs (Kling, Runway Aleph); human preference and expert studies with no stated protocol approval; generated video of robot arms (low misuse potential) |

**Input notes.** Text extraction from a two-column PDF; tables are readable, equations partly garbled (Eq. 4–5 notation is legible enough to read). No figures. The supplement (A–D) is included. No code link (the project page URL is removed). The file shows author names; they were ignored. The integrity scan (`integrity_scan.py`) found **no reviewer-directed text or hidden characters**; the five reviewers read the redacted copy (identical to the original). The text cites items dated after the 2025-09-24 cutoff (e.g., [54] arXiv:2512.04537, [45] arXiv:2511.19861, "Accessed: 2025-11-08" on [21], [37]), so the provided text is a later revision than a submission-deadline version. This is noted for the editor only and changes no score.

### Claimed Contributions (as stated by the authors, §1)
1. **C1** — "the first end-to-end Human2Robot" video generation framework built upon a video diffusion transformer (no intermediate keypoints/trajectories/depth).
2. **C2** — in-context learning gives appearance, scene and action consistency, "significantly improving cross-task" generalization.
3. **C3** — an efficient data synthesis strategy combined with existing datasets for mixed training, which "markedly enhances the model" generalization on unseen tasks and environments (§1, contribution 3).

### Paper memory (factual record, shared with all reviewers)
- **Setup facts.** Backbone Wan 2.2 TI2V-5B (dense) as default; "T2V 14B"/"TI2V-14B MoE" as larger model (§4.1, Table 1, §4.5). LoRA rank 96, lr 1e-4, effective batch 4, 416×224, 8 FPS, 41-frame clips, 2 H200 GPUs; 5B: 20k steps; 14B: 10k steps (§4.1, §4.2). **Seeds/runs, code/data release, GPU-hours, checkpoint selection, validation split: not stated after search.**
- **Data.** Human2Robot (H2R): 11,788 clips after filtering, 500 test (§4.2); the public H2R set has "2,600 video pairs" across nine tasks (§1). EPIC-Kitchens-synthetic: 34,820 clips, 200 test = 100 seen + 100 unseen scenes (§4.2); "over 6,000 high-quality synthetic" human–robot paired videos (Fig. 3 caption). How train/test clips are split (by episode/video or by clip) is **not stated** for H2R; for EPIC only the seen/unseen scene division is given.
- **Metrics.** FVD, PSNR, MSE, SSIM; task success rate (SR) judged by three domain experts with consensus ("Three domain experts independently review all" generated videos) (§4.3, Suppl. A.2); Embodiment Consistency (CLIP image score + DreamSim + human evaluation, normalized; §4.3); human preference with "20 valid survey responses" (§4.3). FVD feature extractor/sample count not stated.
- **Headline numbers.** Table 1: 5B w/ 1st frame — H2R SR 91, EPIC seen 88, unseen 86; 14B — 93/90/89. Table 3: Ours SR 84.5, preference 68.0%, embodiment consistency 92.6 (Masquerade 96.5).
- **Appendix adds.** SR definition (A.1), expert protocol (A.2), Masquerade failure modes (B, Fig. 7), more qualitative results (C, Figs. 8–9), Mitty failure analysis (D, Fig. 10: erasing failures, arm structural distortion — "most frequent failure mode on the EPIC-Kitchens dataset" — and unreasonable interaction).
- **Unverifiable.** All figures; Eq. 4 only partly checkable (see R1).

### Literature check summary (Phase 1.5, run after the five reports were drafted)
Mode `strict`, cutoff 2025-09-24; 6 of 12 queries used (claim queries C1×2, C2, C3; baseline queries ×2); 49 kept results; no coverage gaps flagged. Closest prior works: Phantom, Human2Robot, Robotic Telekinesis (cosine 0.27/0.27/0.26; no text overlap). Details in R2's addendum.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Adaeze Brandvold, public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / generative video models, evaluation of generative systems
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Weighs evidence over head-count; knows that ICLR accepts papers with ordinary weaknesses but not with unsupported central claims.

### Reviewer 1 (Methodology): Dr. Joon-ho Pellegrino, industrial research lab (East Asia)
- **Seniority / Expertise**: Mid-career industry scientist / diffusion-model fine-tuning; FVD and human-evaluation design for video generation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table delta; insists on matched training budgets and variance on small test sets.

### Reviewer 2 (Domain): Prof. Samira Valtteri, robotics and vision group, large public university (North America)
- **Seniority / Expertise**: Senior faculty / robot learning from human video; cross-embodiment transfer; egocentric datasets
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks the closest prior work abstract by abstract; separates new methods from newly applied ones.

### Reviewer 3 (Perspective): Dr. Tomasz Okafor-Lindgren, graphics and HCI institute (Central Europe)
- **Seniority / Expertise**: Mid-career researcher / video editing and compositing, VFX pipelines, human-robot interaction
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; sees potential and says what would unlock it.

### Reviewer 4 (Generalist): Dr. Mei-Lin Auerbach, vision group, public university (Oceania)
- **Seniority / Expertise**: Mid-career / vision and multimodal learning (not robotics)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical programme-committee member; asks whether an ML audience would learn something.

### Devil's Advocate: Prof. Rafael Dunmore-Aziz, statistics and evaluation methodology department (South America)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, causal reasoning about benchmarks
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first.

*Personas are fictional. Assumptions: venue ICLR (stated), paper type empirical.*

---

# PHASE 1 — Independent Reviews

---

# Peer Review Report — Reviewer 1 (Methodology)

## Paper: Mitty: Diffusion-based Human-To-Robot Video Generation
## Reviewer: Dr. Joon-ho Pellegrino, Methodology Reviewer (industrial research lab, East Asia; fictional persona)
## Expertise: diffusion fine-tuning; video-generation metrics; human-evaluation design
## Date: 2026-11-05

### Summary
The paper fine-tunes Wan 2.2 with LoRA so that a clean latent of a human demonstration video conditions the denoising of a robot-execution video. Training data are the public Human2Robot (H2R) clips and a synthetic set made by running a hand-pose → robot-rendering pipeline over EPIC-Kitchens, filtered by humans. Results are reported with FVD/PSNR/SSIM/MSE, a binary expert "task success" rate, a small preference study and a comparison with Masquerade and three off-the-shelf video-editing systems. The paper concludes that the model beats rendering- and editing-based alternatives and generalizes to unseen environments.

### Protocol sweep (Step 0)
Searched the full text and supplement for split/selection statements. Found: all quantitative results are "reported on these" held-out splits (§4.2); H2R "of which 500 are used for testing"; EPIC "200 form the test set, evenly divided into 100" seen and 100 unseen scenes. **Not stated after search:** a validation split, checkpoint selection, how clips were assigned to train/test (by episode/video or by clip), seeds, number of runs. No statement says anything was tuned or selected on the test set; I therefore raise no leakage issue, but the missing split protocol is a validity question (Q1).

### Claim-to-evidence map
| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|--------------|----------|---------|
| C1 | First end-to-end H2R video generation, bypassing intermediate representations | §1, Abstract, §6 | Table 3 vs. Masquerade/editing baselines; no model trained on keypoint/trajectory conditioning with the same data | Partially: the comparison does not isolate the absence of an intermediate representation (W2) |
| C2 | In-context learning gives appearance/action consistency and "significantly improving cross-task" generalization | §1, §3.2 | Table 2 "w/o ref vid." ablation; Table 1/2 EPIC unseen split | Consistency: supported (SR 65→91 on H2R). Cross-task generalization: **unsupported** — no held-out-task split (W3) |
| C3 | Mixed training with synthetic data "markedly enhances" generalization to unseen tasks/environments | §1 contribution 3, §6 | Table 2 mixed vs. separate | **Contradicted** by the paper's own table (W1) |
| — | "state-of-the-art results" | Abstract | Table 3 (zero-shot editing baselines + Masquerade) | Partially: baselines are not trained on the paired data (W2) |

### Strengths
**S1: A clean, sensible conditioning recipe on a strong open backbone.** Clean human latents plus noisy robot latents in one sequence (Fig. 2, §3.1) is a simple design that inherits Wan 2.2 priors. Training budget is modest (LoRA, two H200s, §4.1), which makes the approach accessible.

**S2: The ablation on the human reference video is informative.** Removing the reference video drops SR from 91 to 65 on H2R and from 88 to 75 on EPIC-seen (Table 2), a large effect that supports the claim that the model actually uses the demonstration rather than only the first frame and text.

**S3: Honest failure analysis and limitations.** Supplement D and Fig. 10 report concrete failure modes of Mitty (arm distortion most frequent on EPIC), and §5 states that success is judged on generated videos, not on physical rollouts.

**S4: A definition of "task success" and an anonymized, shuffled expert protocol** (Suppl. A.1–A.2) is more than most video-generation papers provide.

### Weaknesses (ordered by severity)
**W1: The mixed-training claim is contradicted by Table 2, and the text and conclusion disagree with each other.** §1 says combining datasets for mixed training "markedly enhances the model" generalization on unseen tasks and environments; §4.6 says the separately trained model "outperforms mixed training"; §6 credits ablations with showing the "effectiveness of in-context conditioning and mixed training". Table 2 shows mixed training is far worse on H2R (PSNR 16.63 vs 21.70 dB; SR 72 vs 91) and mixed on EPIC-unseen is better on SR (86 vs 81), PSNR and MSE but worse on FVD and SSIM. No experiment compares training with vs. without the synthetic EPIC data on H2R or on unseen tasks, so the data-synthesis contribution (C3) has no controlled test.
- **Suggested Fix**: Add ablations: (a) H2R-only vs H2R + synthetic EPIC, tested on H2R and on held-out tasks; (b) EPIC-only. Rewrite §1/§6 to match Table 2. ≈ 2 extra 5B runs ≈ 2×(20k steps) on 2 GPUs.

**W2: The headline comparison does not test the central claim that bypassing intermediate representations helps.** Table 3 compares Mitty (trained on in-domain paired data) with Masquerade (a non-learned multi-stage pipeline) and with three zero-shot editing systems that see one robot reference image. No baseline trained on the same paired data with an explicit intermediate representation (e.g., a rendered keypoint/arm-skeleton video as condition) or with another conditioning mechanism (e.g., fine-tuning an existing video-to-video controllable model such as the cited VACE [18] on the same pairs). "State-of-the-art" in the Abstract is therefore relative to systems with a large information and training-data disadvantage. Human2Robot [51], whose method generates robot videos from human video, is cited but not compared.
- **Suggested Fix**: Add one matched-data baseline (VACE-style or channel-concat conditioning fine-tuned on the same 11.8k/34.8k clips) and one keypoint-conditioned variant; or narrow the claim to outperforming rendering and zero-shot editing pipelines. ≈ 2 fine-tunes ≈ 40 GPU-h.

**W3: Cross-task generalization is claimed but the test splits cannot show it.** C2 claims "significantly improving cross-task" generalization and the Abstract claims strong generalization to unseen environments. The only "unseen" split is 100 EPIC clips from unseen scenes (§4.2). H2R has nine tasks; no held-out-task evaluation is reported, and how H2R clips are split is not stated. Clips are cut at equal intervals from the same videos (§3.3, last paragraph), so clips from one episode may land in both train and test, in particular for "seen" EPIC scenes.
- **Suggested Fix**: State the split unit; report H2R with leave-one-task-out (even 2–3 tasks), and EPIC with episode-level splits. No new training of the method beyond 3 runs.

**W4: Evidence is single-run on very small test sets, and several reported differences are inside sampling noise.** With n=100 clips (EPIC seen/unseen), the binomial 95% interval of an SR near 85% is about ±7 points (recomputed: SE = √(0.86·0.14/100) ≈ 3.5 points); for H2R n=500 at 91% it is about ±2.5 points. Differences quoted as meaningful include 14B vs 5B on H2R (93 vs 91), mixed vs separate on EPIC-unseen (86 vs 81) and with vs. without first frame on EPIC-seen (88 vs 84). No seeds, intervals or paired tests are given. FVD is computed on 100–500 videos with an unspecified feature extractor; the reported FVD values (6.5–12.3) cannot be interpreted without it.
- **Suggested Fix**: Report Wilson/bootstrap CIs for SR, a paired test (McNemar) between configurations on the same clips, FVD protocol, and 3 seeds for the 5B model on H2R (≈ 3×20k steps).

**W5: Table 1 and Table 2 disagree, and the prose misdescribes Table 1.** See Error Log ERR-1 to ERR-3.

**W6: The 5B vs 14B "scaling" comparison is confounded.** 14B is trained for 10k steps and 5B for 20k (§4.1); the 14B row is named "T2V 14B" in Table 1 and §4.5, but "TI2V-14B MoE" in §4.1, and it is not stated whether the 14B model receives the first frame (a T2V model has no image input). Any claim that the larger model "achieves the best overall performance" cannot be attributed to scale.
- **Suggested Fix**: State exactly which checkpoint, conditioning and step count each row uses; match steps or report both.

**W7: The human studies are under-specified.** SR is a binary consensus judgment by three unnamed "domain experts" with no agreement statistic (§4.3, A.2); preference is based on "20 valid survey responses" with no number of items, raters per item, or tie option; Embodiment Consistency mixes CLIP, DreamSim and human scores into a normalized average without the normalization or weights (§4.3). It is not stated whether the experts are the authors or whether they could identify the methods (Mitty outputs resemble ground truth; Masquerade has black frames).
- **Suggested Fix**: Report Fleiss/Cohen κ before consensus, rater/item counts, sign-test p-values on preference, and the exact formula for Embodiment Consistency.

**Minor:** section titles swapped in §4.5 ("Quantitative Evaluation" introduces Fig. 4 qualitative results, "Qualitative Results" introduces Table 1); "Datasets ad Benchmark"; inconsistent decimals (21.7 vs 21.42 in Table 2); Fig. 3 caption says "Segment Anything [36]" but [36] is SAM 2; Suppl. D refers to a GPT-based approach ("failure cases of our GPT" followed by a hyphen break), which does not describe Mitty; no GPU-hours reported.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | §4.5 vs Table 1 | "adding the first-frame condition consistently" (reduces FVD/MSE while slightly increasing PSNR, SSIM and SR) | Table 1: EPIC-seen SSIM 0.630→0.617, EPIC-unseen SSIM 0.670→0.627 and PSNR 13.30→13.29 all go down with the first frame | Recomputed from Table 1 rows "w/o 1st f" vs "w 1st f" | High | MAJOR | Correct text; discuss SSIM drop (−0.043 unseen) |
| ERR-2 | E6 | Table 1 vs Table 2 | EPIC-unseen "TI2V 5B (w 1st f)" SR 86 vs "Full (Sep. train.)" SR 81 | Same model/config; the other four metrics are identical (9.48, 13.29, 0.627, 0.0493) but SR differs by 5 points. Table 3's Ours SR of 84.5 equals the mean of Table 2's 88 and 81 (derived), supporting 81 | Cross-referenced (two locations) and recomputed | High | MAJOR | Reconcile; state which clips Table 3 uses |
| ERR-3 | E5/E1 | §4.6 vs §6 vs §1 | "outperforms mixed training"; "effectiveness of in-context conditioning and mixed training" | Table 2 shows mixed < separate on H2R by 19 SR points; the conclusion claims the opposite | Cross-referenced (§1, §4.6, §6, Table 2) | High | MAJOR | Align claims with data (W1) |
| ERR-4 | E6 | Suppl. D | "failure cases of our GPT" | Mitty is a Wan 2.2 diffusion model; no GPT component exists elsewhere | Searched full text for "GPT" (single hit) | Medium | MINOR | Fix wording; confirm Fig. 10 shows Mitty |
| ERR-5 | E6 | §4.1 vs §4.5/Table 1 | "Wan 2.2 TI2V-14B MoE" vs "T2V 14B" | Same model named two ways; first-frame conditioning on a T2V model undefined | Cross-referenced | Medium | MINOR | State the exact checkpoint |

### Reproducibility checklist
| Item | Present? | Location |
|------|----------|----------|
| Architecture details | Partly (concatenation described; Eq. 4 vs Fig. 2 ambiguity, see Q2) | §3.1–3.2, Fig. 2 |
| Optimizer/LR/batch/steps | Yes (AdamW not stated) | §4.1 |
| Hyperparameter search and tuning split | Not stated after search | — |
| Hardware and compute | Hardware yes; GPU-hours no | §4.1 |
| Seeds | Not stated | — |
| Code/data/checkpoints | Not stated (project page link removed) | Abstract |
| Synthetic-data filtering rate/criteria | Not stated ("human-in-the-loop filtering mechanism") | §3.3 |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sensible method; unsupported/contradicted secondary claims; no variance, no matched baselines |
| Clarity | 2 | Eq. 4 vs Fig. 2, naming and table inconsistencies |
| Significance | 2 | Useful direction, but only video plausibility is shown |
| Originality | 2 | Known conditioning recipe applied to a new task; data pipeline inherited |

### Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central comparison lacks a matched-data baseline and a controlled test of the data-synthesis claim, and Tables 1–2 contradict each other and the prose.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | Method is plausible; Eq. 4/Fig. 2 mismatch; confounded 5B/14B; inconsistent tables |
| Clarity & Presentation | 54 | Competent | Readable but with swapped headings, naming drift, stray "GPT" |
| Novelty & Originality | 48 | Developing | Task application of existing in-context conditioning |
| Significance & Impact | 52 | Competent | Valuable direction; evidence limited to generated-video plausibility |
| Experimental Validation | 40 | Developing | n=100–500, single runs, no matched baselines, no held-out-task test |
| Reproducibility | 50 | Developing | No code/seeds/filtering criteria; hyperparameters present |
| Ethical Compliance | 60 | Competent | Limitations honest; licence/API-upload and human-study details missing |

### Questions for Authors
1. How were H2R and EPIC train/test clips split (by episode, video, or clip)? If clips of the same episode appear in both, which of the seen-split numbers survive an episode-level split? (A clean episode-level split would raise my Experimental Validation score.)
2. Eq. 4 defines a projection-free cross-attention between C and D whose outputs are concatenated, while Fig. 2 and §1 describe concatenating tokens inside the DiT self-attention with LoRA on QKV. Which is implemented? Is there an ablation against plain concatenation with ordinary self-attention? (An ablation showing a gain would raise the Technical Rigor score.)
3. Eqs. 1–5 are written for DDPM ε-prediction; to my knowledge Wan 2.x is trained with a flow-matching objective [verify]. Which objective and sampler were used for fine-tuning and inference?
4. What are the Table 1 vs Table 2 SR values for EPIC-unseen, and which clips does Table 3 use?
5. What fraction of Masquerade-rendered clips survived human filtering, and how was Masquerade's 31.5% SR measured (raw or filtered clips)?

### Limitations Assessment
**Partially.** §5 and Suppl. D are candid about the lack of closed-loop evaluation and about failure modes. Missing: the unmeasured effect of the data-synthesis pipeline on generalization, the filtering yield, and the negative transfer visible in mixed training.

### Ethics Review Flag
**No.** Minor: dataset licences (EPIC-Kitchens, Ego4D) and upload of dataset frames to commercial APIs should be stated.

### Overall Score
**3 (Borderline Reject)**: A sensible, accessible recipe on a hot topic, but the paper's own tables contradict one of its three contributions, the key claim (end-to-end beats intermediate representations) is not tested against a matched-data alternative, and the evidence is single-run on small test sets.

### Confidence
**4**: Tables were recomputed; figures could not be inspected and Eq. 4 may be shorthand.

---

# Peer Review Report — Reviewer 2 (Domain)

## Paper: Mitty: Diffusion-based Human-To-Robot Video Generation
## Reviewer: Prof. Samira Valtteri, Domain Reviewer (robotics and vision group, large public university, North America; fictional persona)
## Expertise: robot learning from human video; cross-embodiment transfer; egocentric data
## Date: 2026-11-05

### Summary
Mitty generates a robot-arm execution video from a human demonstration video by conditioning a pretrained video diffusion transformer on the demonstration, and trains it on an existing paired dataset plus a synthetic set made from egocentric videos with a published rendering pipeline. It is positioned as the first end-to-end alternative to keypoint/trajectory pipelines. The experiments compare against a rendering pipeline and general video editors on video-level metrics.

### Strengths
**S1: A relevant, timely problem.** Turning human demonstrations into embodiment-specific visual targets is a live question in learning from human video (§2.2), and a diffusion-based direct translator is a natural next step beyond inpaint-and-render approaches such as the cited Masquerade [23].

**S2: Honest attribution of the data pipeline.** §3.3 states "we build upon the data rendering approach" of Masquerade [23] and lists each off-the-shelf stage (Detectron2, SAM 2, E2FGVI, robosuite), so what is new in the data side is clear (filtering and scale).

**S3: Practical evaluation breadth for a new task.** Two datasets (a real paired set and a synthetic egocentric one with seen/unseen scenes), several video metrics, expert success judgements, and a comparison with commercial editors give a multi-angle picture for a task with no standard benchmark.

**S4: Useful negative information about editors.** Fig. 6/§4.8 show that generic editors with a single robot reference image distort the arm, a fair data point that the task needs paired supervision.

### Weaknesses
**W1: "First end-to-end Human2Robot video generation framework" (C1) is overstated, and the closest prior work is not differentiated.** Human2Robot [51] (cited, but only in a citation list in §2.2 and as the source of the dataset in §1) is described in its own abstract as treating human–robot alignment "as a conditional video generation problem" and "generating robot videos from human input". The idea of translating a human demonstration video into a robot video at pixel level also predates it (AVID, below, via image translation). The paper's genuine delta is a larger pretrained video DiT, a different conditioning, and added synthetic data; this should be framed as such and [51]'s video model should be compared or explicitly differentiated.
- **Suggested Fix**: Replace "first" by a precise delta statement; add [51] to the related work discussion and, if its video model is available, to Table 3.

**W2: The methodological delta against in-context conditioning for video DiTs is small and not ablated.** Concatenating clean condition tokens with noisy target tokens for joint attention is the in-context conditioning recipe already used for video DiTs and for the cited VACE [18], In-Context LoRA [15] and Video ICL [56]. The paper does not show whether "bidirectional attention" (Eq. 4) adds anything over plain concatenation, so the technical contribution reduces to applying a known recipe to human→robot data.
- **Suggested Fix**: Ablate Eq. 4 vs plain token concatenation; discuss the relation to uncited video-DiT in-context work (see addendum).

**W3: The bypass-of-intermediate-representations narrative is inconsistent with the paper's own data.** §1 says of the synthesis approach that it "passes traditional intermediate representations" (sic: the word is split across a line break), yet §3.3 builds the EPIC training targets from HaMeR hand meshes → keypoints → end-effector poses (thumb–index midpoint, plane normal, thresholded gripper) → robosuite rendering, i.e., exactly the intermediate-representation pipeline criticized in the Abstract. Mitty is end-to-end only at inference; its EPIC "ground truth" is the output of that pipeline, so its fidelity is bounded by the teacher's pose estimates, and EPIC PSNR/SSIM measure agreement with a rendering, not with a physically correct robot video.
- **Suggested Fix**: Say this explicitly; add an evaluation on real (not rendered) robot ground truth for at least the H2R set separately from EPIC aggregates; discuss teacher-student bounds.

**W4: Positioning against the recent human-to-robot video-translation line is thin.** Phantom [22], Masquerade [23], EgoMimic [19] and MimicDreamer [24] are cited as a list, but the paper does not state which of their capabilities (e.g., kinematic reachability, policy training, closed-loop execution) Mitty lacks or has. HaMeR, the hand estimator actually used (§3.3), has no bibliography entry.
- **Suggested Fix**: A short comparison table (input, output, needs depth/keypoints, evaluated on robot?, trained on) and a citation for HaMeR.

### Missing References (verified with `related_search.py`, strict mode; links in the addendum)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Smith, Dhawan, Zhang, Abbeel, Levine. *AVID: Learning Multi-Stage Tasks via Pixel-Level Translation of Human Videos.* RSS 2020 (https://arxiv.org/abs/1912.04443v3) | Prior pixel-level translation of human demonstration videos into robot videos (CycleGAN); bears on the "first" claim |
| Important | Fei, Qiu, Li, Yu, Fan. *Video Diffusion Transformers are In-Context Learners.* arXiv 2412.10783, 2024 (https://arxiv.org/abs/2412.10783v3) | Same in-context conditioning mechanism in video DiTs; needed to position C2 |
| Helpful | Xiong, Li, Chen, Bharadhwaj, Sinha, Garg. *Learning by Watching: Physical Imitation of Manipulation Skills from Human Videos.* IROS 2021 (https://arxiv.org/abs/2101.07241v2) | Unsupervised human-to-robot translation from a single video |
| Helpful | Liu, Gupta, Abbeel, Levine. *Imitation from Observation: Learning to Imitate Behaviors from Raw Video via Context Translation.* ICRA 2018 (https://arxiv.org/abs/1707.03374v2) | Early context translation from human video |
| Worth discussing (recent preprint, not required) | He, Liu, Ye, et al. *FullDiT2: Efficient In-Context Conditioning for Video Diffusion Transformers.* arXiv 2506.04213, 2025 | In-context conditioning by concatenation with noisy latents |
| Worth discussing (recent preprint, not required) | *RoboSwap: A GAN-driven Video Diffusion Framework For Unsupervised Robot Arm Swapping.* arXiv 2506.08632, 2025 [authors: see arXiv listing, verify] | Robot-arm swapping in video with diffusion refinement |

### Literature-check addendum (strict, cutoff 2025-09-24; 6 queries)
**Per-claim novelty (claim-level profile; `related_search.py novelty`).**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 first end-to-end H2R video gen | problem | incremental | Human2Robot (4; https://arxiv.org/abs/2502.16587v4; prior arXiv-only; **cited**) | Generates robot videos from human video as conditional video generation; Mitty differs in backbone, conditioning and data |
| C2 in-context conditioning | method | incremental | Video DiTs are In-Context Learners (4; https://arxiv.org/abs/2412.10783v3; prior arXiv-only; not cited) | Concatenation of conditioning video and target for joint attention; Mitty adds Eq. 4 attention (untested) |
| C3 synthetic paired data | resource | incremental | Phantom (4; https://arxiv.org/abs/2503.00779v2; prior peer-reviewed; **cited**) | Inpaint human arm and overlay rendered robot; the paper builds on Masquerade explicitly |

Script reading: "no central claim fully covered by prior work". Attribution: Phantom. One claim-level finding (C1) is MAJOR at most; the paper is not "known". No close prior work was found in these results for the *combination* of a video DiT with human-demonstration conditioning on EPIC-style data (arXiv only, so not evidence of novelty).

**Novelty delta table.**
| Claimed contribution | Closest prior work | Already done | What is new | Cited and differentiated? |
|---|---|---|---|---|
| C1 | Human2Robot (Xie et al., 2025) | Conditional video generation of robot video from human video, with a paired dataset | Pretrained Wan 2.2 backbone, in-context conditioning, EPIC synthetic data, video-level evaluation | Cited ([51]); not differentiated or compared |
| C2 | Video DiTs are In-Context Learners | In-context concatenation for video DiTs | Application to human→robot; Eq. 4 attention | Related family cited ([15],[18],[56]); this work not cited |
| C3 | Phantom; Masquerade (arXiv:2508.09976, found, Aug 2025) | Inpaint/overlay pipelines for paired data | Scale, human-in-loop filtering, using the output as supervision | Cited and attributed |

**Baseline scout.** No external benchmark with published video-metric numbers for this task was found: `scout` for EPIC-Kitchens returned only unrelated work, and the H2R dataset paper reports robot-policy results, not FVD/PSNR/SR on the paper's splits. No under-reported baseline can be established; settings differ. Missing required comparisons from *prior* work: Human2Robot's video model (MAJOR at most). Phantom, Masquerade and X-Humanoid-like works are not directly comparable video baselines.

**Field snapshot.** Five years ago, learning from human video relied on CycleGAN-style translation (AVID) or hand-pose retargeting to robot actions; by 2024–2025 the dominant moves are keypoint/track-conditioned policies, inpaint-and-render data editing (Phantom, Masquerade) and large video models used for planning or as data engines. Open problems stated by recent work: embodiment gaps, scarce paired data, and bridging generated video to executable actions. A significant contribution in this sub-field now shows that generated video improves downstream robot performance or enables a new capability with controlled evidence (matched data, real-robot or closed-loop tests); a better-looking translated video on a rendered benchmark is incremental. This calibrates my Significance (54) and Novelty (44) scores.

**Citation check (E7).** [23] Masquerade is correctly described and verified; [51] Human2Robot is cited as the dataset source and listed in §2.2 but its video-generation model is not discussed; [5] HandDiff is cited for 3D hand pose estimation, while the estimator actually used (HaMeR, §3.3) is uncited — an omission, not a mismatch; Fig. 3's "[36]" is SAM 2, labelled "Segment Anything".

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims outrun controlled evidence |
| Clarity | 2 | Positioning thin; naming drift |
| Significance | 2 | Useful direction, only video-level evidence |
| Originality | 2 | Incremental on all three claims |

### Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: all three contributions have close prior work with only partial differentiation, and the gain over the closest prior approach is not demonstrated empirically.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound recipe; Eq. 4 untested; theory not the point |
| Clarity & Presentation | 56 | Competent | Related work lists rather than positions |
| Novelty & Originality | 44 | Developing | Incremental on all claims at claim level |
| Significance & Impact | 54 | Competent | Timely, narrow evidence |
| Experimental Validation | 46 | Developing | No matched/closest-prior comparison |
| Reproducibility | 52 | Competent | Details partly present; no code |
| Ethical Compliance | 60 | Competent | Honest limitations |

### Questions for Authors
1. How does Mitty differ, technically and empirically, from Human2Robot's video model [51]? A head-to-head on the H2R test clips would raise my Novelty and Experimental scores.
2. Does Eq. 4 outperform plain concatenation in the DiT's own self-attention?
3. How much of Mitty's EPIC performance is bounded by hand-pose errors in the rendering teacher (what fraction of test clips has erroneous GT)?

### Limitations Assessment
**Partially.** Closed-loop absence is acknowledged; teacher-bound and prior-work overlap are not.

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject)**: A reasonable application of in-context video conditioning to a new task, but the "first" claim is overstated, the delta to the closest prior work is not shown, and the data contribution is attributed-but-incremental.

### Confidence
**4**

---

# Peer Review Report — Reviewer 3 (Perspective)

## Paper: Mitty: Diffusion-based Human-To-Robot Video Generation
## Reviewer: Dr. Tomasz Okafor-Lindgren, Perspective Reviewer (graphics and HCI institute, Central Europe; fictional persona)
## Expertise: video editing and compositing; VFX pipelines; human-robot interaction
## Date: 2026-11-05

### Summary
The paper turns a human demonstration into a robot-arm video by letting a video diffusion model "read" the demonstration while it generates the robot video. For training it builds paired data by erasing hands from egocentric footage and compositing rendered robot arms. The authors present this as a stepping stone toward learning robot policies from human video, without yet producing actions.

### Strengths
**S1: A compelling visual-effects-style reframing.** Treating embodiment transfer as video replacement rather than as pose retargeting connects the work to the video-compositing literature; Fig. 1 and Fig. 6 show why generic editing fails (the arm's structure drifts), which is exactly what a compositing artist would expect from a single reference image.

**S2: Data-engine thinking.** Using a cheap rendering pipeline as a teacher to create supervision at scale (§3.3), then distilling it into a model that tolerates its failures, is a pragmatic idea that could transfer to other embodiments or to humanoid targets (§2.2 mentions humanoids).

**S3: Honest scope.** §5 states the model is "not yet a complete Video Policy pipeline" and that success is judged from videos; this keeps the contribution from being mistaken for a policy.

**S4: Low barrier.** LoRA fine-tuning on two GPUs (§4.1) means labs can reuse the approach.

### Weaknesses
**W1: The "task success rate" is a visual-plausibility judgement, so it says little about usefulness for robots.** §4.3 defines failure as artifacts, discontinuities or incorrect arm motion; Suppl. A.1 ignores "small geometric distortions". A video that looks right can encode a kinematically infeasible or collision-prone trajectory; Masquerade's failures in Suppl. B (reachability, arm collisions) are exactly such cases, and nothing shows Mitty avoids them except qualitative figures. The Abstract's "new insights for scalable robot learning" and Fig. 1's "achieves high task success rates" read as robotics claims.
- **Suggested Fix**: Add a cheap physical proxy: extract the rendered arm's pose from generated frames (e.g., with the same rendering/pose tools) and test reachability/self-collision rates, or run a small simulation replay for 20–50 clips; reword the metric as video-level task success.

**W2: Assumptions about embodiment and viewpoint are unexamined.** Both datasets are fixed viewpoint (H2R third-person) or head-mounted (EPIC) and use a specific robot model rendered with robosuite; the pipeline maps thumb–index pinch to a gripper. Dexterous or non-pinch grasps (cutting, writing in Fig. 4) are mapped to the same gripper abstraction. It is not discussed whether the model can generate a *different* robot arm without retraining, which is the practical need in cross-embodiment learning.
- **Suggested Fix**: Show one or two embodiment swaps (e.g., another robosuite arm) using the same pipeline, or state the single-embodiment limit.

**W3: Robustness and temporal scope.** Clips are 41 frames at 8 FPS, 416×224 (§4.1–4.2): about five seconds at low resolution. Real demonstrations are longer, and the paper does not show long-horizon chaining or the effect of resolution. Camera motion on EPIC is cited as the main difficulty (§4.5), yet no analysis by camera-motion level is provided.
- **Suggested Fix**: Report per-difficulty breakdowns (static vs moving camera; one vs two hands) and a chained-clip example; discuss resolution effects.

**W4: Provenance and licensing of source footage.** EPIC-Kitchens and Ego4D have specific licences (non-commercial/consented use) and the footage is sent to commercial editing APIs (Kling, Aleph) in §4.8; the paper states neither terms nor safeguards. Generated robot videos of real kitchens retain scene layout and possibly identifiable surroundings.
- **Suggested Fix**: Add a data-licence and API-use statement.

**Minor:** the term "paradoxical in-context learning" in Fig. 1's caption is unexplained.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sensible design; limited controls |
| Clarity | 3 | Mostly clear |
| Significance | 3 | Promising direction for data engines |
| Originality | 3 | New use of a known recipe |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a topical, visually convincing translation system with an honest scope statement; I weigh the direction and the data-engine idea above the evidence gaps, which the other reviewers cover.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasonable design and ablation on the reference video |
| Clarity & Presentation | 66 | Competent | Clear narrative |
| Novelty & Originality | 60 | Competent | Application novelty; useful framing |
| Significance & Impact | 70 | Competent | Relevant to video world models and human-video learning |
| Experimental Validation | 58 | Competent | Several datasets and baselines; limited statistics |
| Reproducibility | 58 | Competent | Setup given; no code |
| Ethical Compliance | 66 | Competent | Limitations honest; licences missing |

### Questions for Authors
1. Can the generated arm trajectories be checked for reachability and self-collision? A positive check would raise my Significance score.
2. Can the model be retargeted to a second robot with a small amount of data?
3. What is the failure rate by camera motion (static vs moving)?

### Limitations Assessment
**Yes, mostly.** §5 and Suppl. D are candid; add embodiment/viewpoint limits.

### Ethics Review Flag
**No.** Low misuse potential; dataset licensing to be stated.

### Overall Score
**4 (Borderline Accept)**: An interesting, accessible step toward using human video for robot learning with honest scope; evidence gaps are real but typical of a first paper on a new task.

### Confidence
**3**: Not a robotics-learning specialist; could not inspect the figures.

---

# Peer Review Report — Reviewer 4 (Generalist)

## Paper: Mitty: Diffusion-based Human-To-Robot Video Generation
## Reviewer: Dr. Mei-Lin Auerbach, Generalist Reviewer (vision group, public university, Oceania; fictional persona)
## Expertise: vision and multimodal learning (not robotics)
## Date: 2026-11-05

### Summary
The paper presents a LoRA-fine-tuned video diffusion model that converts a human manipulation video into a robot-arm execution video, trained on a real paired dataset and a large synthetic set built by rendering robot arms into egocentric videos. It reports video-quality metrics, expert-judged success rates and a preference study, and positions the model as a foundation for future video-to-policy methods. In my words: a data-plus-recipe paper showing that a strong video backbone can learn embodiment translation when given paired data.

### Strengths
**S1: Clear problem statement and motivation** (§1): the three challenges (appearance/scene consistency, action alignment, data scarcity) map neatly onto the three contributions and the experiments.

**S2: Appropriate venue topic.** Conditional video generation and learning from human video are in scope for an ICLR audience, and the paper is accessible to non-roboticists.

**S3: Illustrative figures and an ablation table** (Fig. 2 architecture, Fig. 4 results, Table 2) make the main message — the reference video matters — easy to follow.

**S4: Candid limitations section** (§5).

### Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Claims supported by evidence (Soundness) | Partly — C3 contradicted, C2 generalization unsupported | Table 2, §1 |
| Clarity of presentation | Partly | §3.2 vs Fig. 2, §4.5 headings |
| Contribution significance | Partly — first-paper-on-a-task value but modest ML insight | §1, §6 |
| Reproducibility | Partly — no code, seeds | §4.1 |
| Fair comparison | Not met for the SOTA claim | Table 3 |

### Weaknesses
**W1: The ML take-away is thin.** Beyond conditioning on the demonstration by in-context concatenation, the paper provides no analysis of why the model works (what is attended, how it handles the mismatch in embodiment) and the sole architectural novelty (Eq. 4) is not ablated. For an ICLR audience the paper currently reads as an application report with strong visuals.
- **Suggested Fix**: Add one analysis (attention maps from the robot tokens onto human tokens; effect of conditioning length) and the Eq. 4 ablation.

**W2: Several claims in the text do not match the tables.** The mixed-training claims (§1 vs §4.6 vs §6), the statement that the first frame "consistently" improves PSNR/SSIM (EPIC SSIM falls in Table 1), and the Table 1 vs Table 2 SR discrepancy for EPIC-unseen (86 vs 81) make the results hard to trust until reconciled.
- **Suggested Fix**: Re-derive the tables from raw logs and align the text.

**W3: The method section is hard to implement from the text.** Eq. 4 defines a projection-free pair of cross-attentions whose outputs are "concatenated along the token" dimension (§3.2), whereas §3.1 says tokens are concatenated "along the temporal dimension" and Fig. 2 shows self-attention with LoRA on QKV. Eqs. 1–5 describe a DDPM-style process for a backbone whose objective is not stated. A reader cannot tell what exactly was trained.
- **Suggested Fix**: Give the exact attention computation in the DiT block, the training objective and the position-embedding handling of the two streams; state if Eq. 4 is illustrative.

**W4: The paper's own framing "in-context learning" over-promises.** The model is conditioned on a demonstration at test time, but no new task is learned from a handful of examples; it is video-to-video translation. The claim "ICL can predict robot actions to achieve novel tasks" (§1) is not demonstrated: no actions are predicted and no novel-task split is used.
- **Suggested Fix**: Call it demonstration-conditioned generation, or test on held-out tasks.

**Minor:** headings in §4.5 swapped; typos ("Datasets ad Benchmark"); Table 2 decimals inconsistent; "paradoxical in-context learning" (Fig. 1); stray GPT mention in Suppl. D; naming of the 14B model.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims exceed evidence in several places |
| Clarity | 2 | Method details and table/text mismatches |
| Significance | 3 | Timely task |
| Originality | 2 | Incremental recipe |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a topical application with good visuals but contradictory tables, limited ML insight and an unsupported "SOTA" framing keep it on the rejected side of the bar.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Reasonable, partly untested |
| Clarity & Presentation | 56 | Competent | Narrative clear; method unclear |
| Novelty & Originality | 50 | Developing | Application novelty |
| Significance & Impact | 58 | Competent | Timely first-paper value |
| Experimental Validation | 50 | Developing | Small sets, single runs |
| Reproducibility | 54 | Competent | Training config present |
| Ethical Compliance | 62 | Competent | Honest limitations |

### Questions for Authors
1. Which attention is implemented — Eq. 4 or ordinary self-attention over concatenated tokens? (A clear answer plus ablation would raise the Technical Rigor score.)
2. Can you give held-out-task results for H2R?
3. Why does mixed training hurt H2R so much? Is it negative transfer from dual- vs single-arm data?

### Limitations Assessment
**Partially.** Good on closed-loop absence; silent on mixed-training negative transfer.

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject)**: A topical paper with promising qualitative results whose strongest claims (SOTA, generalization, mixed-training benefit) are not backed by controlled evidence; fixable but not by a rebuttal-length edit alone.

### Confidence
**4**

---

# Devil's Advocate Report

## Paper: Mitty: Diffusion-based Human-To-Robot Video Generation
## Reviewer: Prof. Rafael Dunmore-Aziz, Devil's Advocate (statistics and evaluation methodology department, South America; fictional persona)

## Steelman
A strong open video backbone, given paired human–robot supervision, can translate a human demonstration into a temporally coherent robot video far better than a stage-wise rendering pipeline or zero-shot editors. The reference-video ablation (SR 91 vs 65 on H2R, Table 2) shows the demonstration is used, and the failure analysis is honest about limits.

## Core Argument Chain
1. Rendering pipelines accumulate errors across stages and lose information (§1, §4.7).
2. A video DiT conditioned directly on the demonstration avoids this (§3.2).
3. A synthetic-data pipeline supplies enough paired data for generalization (§3.3, §4.2).
4. Mitty beats Masquerade and generic editors on expert-judged success and preference (Table 3).
5. Mitty generalizes to unseen environments and tasks (Table 1/2, EPIC unseen).
∴ End-to-end in-context video generation is the better route to scalable human-to-robot translation.

## Strongest Counter-Argument
The comparison that carries the conclusion is not a comparison of *routes* but of *amounts of supervision*. Mitty is trained on the paired data; Masquerade is evaluated as a non-learned pipeline on raw output, and the editors are zero-shot with a single reference image. Mitty's own training targets on EPIC are Masquerade renders that humans filtered (§3.3, §4.7), so Mitty is a student of the pipeline it beats, evaluated against that pipeline's filtered output as ground truth (Fig. 4 caption: the third row "shows the ground-truth robot execution" videos). Under such a design, higher SR than the raw teacher is expected: it measures the filter's value, which Mitty inherits, not the superiority of bypassing intermediate representations. The experiment that would test the claim — the same filtered data used to train a model conditioned on the intermediate representation (rendered arm/keypoint video) versus the human video — is absent. Further, "task success" is determined by three experts viewing generated video (§4.3), with a 100-clip test set for the unseen split, so a 5-point SR difference is inside sampling noise, and the one internal comparison that would speak to the data contribution (Table 2 mixed vs separate) points in different directions across datasets and is described in opposite ways in §4.6 and §6. What the evidence supports is a weaker, still useful claim: a video DiT fine-tuned on filtered paired clips yields visually plausible robot videos that look better than zero-shot editors and unfiltered rendering. The authors can survive this objection by narrowing the claim and adding a matched-data baseline, so the issue is MAJOR, not CRITICAL.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim in its weaker form (a fine-tuned video DiT produces plausible robot videos that beat rendering and zero-shot editing) survives: the evidence supports it, no result is selected or tuned on a reported test set (no such statement after the protocol sweep), and the contradicted statements concern secondary claims.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic/Evidence | Table 3, §4.7, §3.3 | Teacher–student circularity: Mitty's EPIC training targets and "GT" are filtered Masquerade renders, then Mitty is compared with raw Masquerade. Evidence supports only the weaker claim (not contradicted) | Evaluate Masquerade with the same filtering; add a matched-data intermediate-representation baseline; include real robot ground truth only (H2R) |
| DA-M2 | Evidence | Table 2, §1, §4.6, §6 | Mixed training claim: §1 "markedly enhances", §4.6 separate is better, §6 "effectiveness of ... mixed training"; H2R SR 72 vs 91 under mixed. Evidence contradicts contribution 3 (a secondary claim) | Add a with/without-synthetic-data ablation; rewrite |
| DA-M3 | Scope | §1, C2, §4.2 | "Cross-task generalization" claimed; no held-out-task test; clip split unit unstated (§3.3 last paragraph) | Leave-task-out evaluation; episode-level splits |
| DA-M4 | Evidence | Table 1 vs 2 vs 3, §4.5 | Numeric inconsistencies (SR 86 vs 81; first frame said to consistently improve PSNR/SSIM) | Reconcile; derive from logs |
| DA-M5 | Evidence | §4.3, Suppl. A.2, Table 3 | Human-judged SR with no agreement stat, 20 survey responses, undefined normalized "Embodiment Consistency"; n=100 per EIC split makes ±7-point intervals | Report κ, CIs, formula; more raters/items |
| DA-M6 | Logic | §1 vs §3.3 | §1 says the synthesis approach by-passes traditional intermediate representations, while the data pipeline is built from them | Reword; discuss bounds |
| DA-M7 | Scope | Abstract, Fig. 1, §6 | "new insights for scalable robot learning" and "achieves high task success rates" imply robot-level evidence; none exists (§5) | Qualify as video-level; add a proxy |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Clarity | §3.2 vs Fig. 2 | Eq. 4 vs described architecture; DDPM equations vs backbone objective |
| DA-m2 | Clarity | §4.1 vs §4.5 | 14B naming and step-count (10k vs 20k) |
| DA-m3 | Integrity-neutral | Suppl. D | A GPT-based approach is mentioned once ("failure cases of our GPT"); likely leftover wording |
| DA-m4 | Clarity | §4.5 | Swapped subsection headings |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Human preference shares sum to 100% (Table 3) | 20.0+4.8+4.0+3.2+68.0 | 100.0 | Yes |
| "Ours" SR in Table 3 | 84.5 | (88+81)/2 = 84.5 using Table 2 EPIC seen/unseen separate-training SR; Table 1 gives 86 for unseen, which would give 87 | Matches Table 2 only |
| First frame improves PSNR/SSIM "consistently" (§4.5) | Stated | EPIC-seen SSIM 0.630→0.617; unseen SSIM 0.670→0.627; unseen PSNR 13.30→13.29 | **No** |
| 14B vs 5B FVD on H2R | 7.40→6.48 | −12.4% relative | Yes (small SR gain: 91→93) |
| Task description: removing it "causes only" minor changes (§4.6) | Stated | EPIC-seen FVD 7.23→9.43 (+30%); SR 88→83 | Overstated for EPIC |
| SR binomial interval, n=100 at 86% | — | ±6.8 points (95%) | n/a |

## Ignored Alternative Explanations
- Higher SR than the teacher may reflect the human filter rather than end-to-end modelling.
- EPIC PSNR/SSIM near 13 dB/0.6 may mainly reflect moving camera and rendering mismatch, not robot-arm correctness.
- The "reference video" ablation drops SR by removing the only source of task information beyond the first frame and text; a conditioning-by-keypoints variant would show whether the human video's raw pixels (vs its pose) matter.
- Clips from the same videos in train and test may inflate "seen" results.
- Different step counts for 5B and 14B may mask scaling effects.

## Missing Stakeholder Perspectives
Robot practitioners who would want guarantees of kinematic feasibility; owners and participants of the egocentric footage (licences, privacy); evaluators outside the author group for the success judgement.

## Observations (Non-Defects)
The paper discloses that success is judged on video, includes failure cases, and attributes the data pipeline to its source. The reference-video ablation is a large effect. The comparison with generic editors (§4.8) is informative.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Contradicted secondary claims, untested Eq. 4, confounded scaling |
| Clarity & Presentation | 52 | Inconsistent tables/text |
| Novelty & Originality | 42 | Incremental on all three claims; "first" overstated |
| Significance & Impact | 50 | Video-level evidence only |
| Experimental Validation | 38 | No matched baseline; small n; single run; no held-out tasks |
| Reproducibility | 48 | No code, seeds, filtering yield |
| Ethical Compliance | 60 | Honest limitations; licence gaps |

**Pool position:** better than about 36% of submissions (accepted share ≈ 27%).

## Overall: 3 | Confidence: 4

---

# PHASE 1.6 — Report Check (Synthesizer, Step 0)

Each weakness was checked for specificity, whether the paper already answers it, consistency with the paper, and actionability.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W4, W6–W7 | kept | Located, quote or recomputation available |
| R1 | W5 (Table 1/2 mismatches) | kept, made a pointer to the Error Log | Duplicate of ERR-1/2/3 |
| R1 | missing GPU-hours | moved to Minor | Cosmetic reproducibility note |
| R2 | W3 (bypass-of-intermediate-representations narrative) | kept | Verified: §1 and §3.3 wording quoted |
| R2 | W4 (HaMeR uncited) | rewritten | Narrowed to a factual omission (HaMeR absent from the bibliography); checked [5] is a different paper |
| R2 | Novelty statements about Human2Robot | kept | Matches the abstract of [51]; cited in the paper, so the point is not differentiated rather than uncited |
| R3 | W3 (robustness) | rewritten | Made specific (41 frames, 8 FPS, 416×224; per-camera-motion breakdown) |
| R3 | W4 (licensing) | kept | Actionable; low severity |
| R4 | W4 ("in-context learning" framing) | kept | Quote from §1 verified |
| R4 | typos and heading swaps | moved to Minor | Presentation issue that does not hide the contribution |
| DA | DA-M2 | kept | Verified in Table 2/§4.6/§6; classified as contradiction of a secondary claim, hence MAJOR |
| DA | DA-m3 (GPT mention) | kept as MINOR | Verified: one hit in Suppl. D |

No scores were changed. Nothing was dropped as already answered by the appendix: the supplement adds evaluation protocol and failure cases but not the split protocol, seeds, filtering yield or the Eq. 4 clarification.

---

# PHASE 2 — Synthesizer Package, EIC Meta-Review and Decision

## Synthesizer, Part A: merged issue list and official score

| Merged issue | Source IDs | Class | Hinges on outcome? |
|--------------|------------|-------|--------------------|
| No matched-data / intermediate-representation baseline; "SOTA" vs zero-shot editors and non-learned Masquerade | R1-W2, R2-W1, R4-W1, DA-M1 | CONSENSUS-4 | **Yes** |
| Mixed-training/data-synthesis claim contradicted by Table 2; text/conclusion disagree | R1-W1, R4-W2, DA-M2 | CONSENSUS-3 | **Yes** |
| Cross-task generalization untested; split unit unstated | R1-W3, DA-M3, R4-Q2 | CONSENSUS-3 | Yes |
| Table/text inconsistencies (ERR-1–3) | R1-W5, R4-W2, DA-M4 | CONSENSUS-3 | Moderate |
| Single run, small n, no CIs | R1-W4, DA-M5 | CONSENSUS-2 | Moderate |
| "First", incremental novelty vs Human2Robot / in-context video DiTs | R2-W1, R2-W2, R4-W1 | CONSENSUS-2 | Yes |
| Human studies under-specified | R1-W7, DA-M5 | CONSENSUS-2 | Low |
| Task success is video-level, not robot-level | R3-W1, DA-M7, R1 (limits) | CONSENSUS-3 | Moderate |
| Bypass-of-intermediate-representations narrative vs data pipeline | R2-W3, DA-M6 | CONSENSUS-2 | Moderate |
| Method ambiguity (Eq. 4 vs Fig. 2; DDPM vs backbone objective) | R1-Q2/Q3, R4-W3, DA-m1 | CONSENSUS-3 | Low–moderate |
| 5B/14B confound | R1-W6, DA-m2 | CONSENSUS-2 | Low |
| Licensing/ethics statement | R3-W4, R1 (ethics) | CONSENSUS-2 | Low |
| Embodiment/viewpoint assumptions; resolution/duration | R3-W2, R3-W3 | SOLO | Low |
| DA-CRITICAL | none raised | — | — |
| SPLIT | R3 rates 4, others 3 (pool 66 vs 36–50) | SPLIT on overall merit | Discussed below |

**Official score** (`aggregate_scores.py`, before EIC weights, DA-critical list empty): official mean rating **3.20**, official composite **52.4** (band 3). Pool positions: 38, 42, 66, 50, 36.

## EIC Meta-Review (Prof. Adaeze Brandvold)

### The Case For and Against
- **For acceptance:** The task is topical, the recipe is simple and effective on a strong open backbone, and the reference-video ablation shows the demonstration is truly used. The authors are candid about the lack of closed-loop evaluation, and a new paired, synthetic dataset plus qualitative evidence against generic editors is a reasonable first paper on the task.
- **Against acceptance:** The three contributions are each incremental relative to close prior work (Human2Robot, in-context video DiTs, Masquerade/Phantom); the key comparison does not control for training data or representation; one contribution (mixed training on synthetic data) is contradicted by the paper's own Table 2; cross-task generalization is claimed but untested; tables and prose disagree; and the evidence is single-run, small-n, video-level judgements.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Mixed training worse on H2R (PSNR 16.63 vs 21.7; SR 72 vs 91) and §1/§6 claim benefit | R1-W1, DA-M2 | Table 2, §1, §4.6, §6 | **Verified** | §1: "markedly enhances"; §4.6: separate "outperforms mixed training" |
| First frame "consistently" increases PSNR/SSIM | ERR-1, DA | §4.5, Table 1 | **Verified** | EPIC SSIM 0.630→0.617 and 0.670→0.627 |
| SR 86 vs 81 for EPIC-unseen | ERR-2, DA | Table 1, Table 2, Table 3 | **Verified** | Table 3 84.5 = (88+81)/2 |
| Comparison lacks matched-data baseline | R1-W2, DA-M1 | Table 3, §4.4 | **Verified** | Baselines are zero-shot editors and Masquerade; "state-of-the-art" in the Abstract |
| Teacher–student circularity | DA-M1 | §3.3, §4.7, Fig. 4 | **Partly correct** | EPIC targets are filtered Masquerade renders (§3.3, §4.7); but H2R GT is real robot data and Mitty's H2R SR (91) is not subject to this; the gap vs raw Masquerade is on EPIC only; Table 3's test set is not stated |
| Cross-task generalization untested; split not stated | R1-W3, DA-M3 | §4.2, §3.3 | **Verified** | No held-out-task split; split unit not stated |
| "First" claim overstated | R2-W1 | §1; [51] | **Partly correct** | [51]'s abstract describes generating robot videos from human input with a decoupled action decoder; a DiT-based end-to-end variant may still be new, but the unqualified framing is overstated |
| Eq. 4 vs Fig. 2 mismatch | R1-Q2, R4-W3 | §3.2, Fig. 2 | **Verified (ambiguity)** | Not scored as an error; Eq. 4 may be shorthand |
| Bypass narrative vs data pipeline | R2-W3, DA-M6 | §1, §3.3 | **Verified** | The training targets are built from keypoints/poses |
| Stray GPT mention | ERR-4 | Suppl. D | **Verified** | Single occurrence; minor |
| R3's positive rating relies on the generalization and visual quality the paper claims (R3 treats the generalization claim as largely established in S1–S2) | R3 | §4.5, Table 1 | **Overstated** | Unseen split is 100 clips from unseen scenes only |

No integrity signals beyond the neutral note that the provided text cites items dated after 2025-09-24 and shows author names; no reviewer-directed text was found. These change no score.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error Log items ERR-1–3 and the Table 2 contradiction all verified; calibrated to the venue |
| R2 (Domain) | 3 | 4 | 1.0 | Literature points verified against retrieved abstracts; "first" slightly overstated by one clause |
| R3 (Perspective) | 4 | 3 | 0.75 | Pool position 66 rests on strong generalization and visual quality that the EIC found overstated; the weaknesses it lists are sound but the rating is not reconciled with them |
| R4 (Generalist) | 3 | 4 | 1.0 | Sound, typical review |
| DA (Devil's Advocate) | 3 | 4 | 1.0 | Strong counter-argument partly correct (circularity affects EPIC only); no inflated CRITICAL |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised (0 DA-CRITICAL) | n/a | n/a | n/a |

I checked that none of the MAJOR items meets the strict criteria for CRITICAL: no selection on a reported test split is stated (protocol sweep found no tuning/selection sentence), the main claim in its narrowed form is supported rather than contradicted, and the contradicted statement concerns a secondary contribution.

### Final Decision and Justification
The official ratings are 3, 3, 4, 3, 3 (mean 3.20); the EIC-weighted rating is 3.13, giving a starting point of **3 (Borderline Reject)**, and the composite cross-check (official 52.4, EIC-weighted 51.4) is also band 3, so the two signals agree. There is no DA ceiling. I do not depart from the starting point. The pool-position spread (36–66) is driven by R3's lenient 66; ruling on the evidence behind that gap, the points that decide it are the contradicted mixed-training contribution, the unsupported cross-task claim and the absence of a matched baseline for the bypass-intermediate-representations claim, each verified in the paper. Against that, the task value, the simple effective recipe and the honest limitations keep this from a Reject (2): these are fixable with additional experiments (a matched-data baseline, a with/without-synthetic-data ablation, a held-out-task split, CIs) and claim-narrowing, which are plausibly within a discussion period but not trivial. At ICLR the accepted-paper pool contains papers with single runs and small gaps, but not with a central contribution contradicted by the paper's own ablation and with the main comparison not isolating the claimed mechanism. My own pool position: better than about 45% of submissions (accepted share ≈ 27%). Final Overall (EIC): **3 — ICLR rating 4 on {0,2,4,6,8,10}** (5 on the earlier {1,3,5,6,8,10} scale); Soundness 2, Presentation 2, Contribution 2 (secondary scale status).

---

## Score Summary

### Official Scores and EIC Assessment
(From `aggregate_scores.py scores.json --venue iclr --final 3`.)

#### Reviewer weights (EIC, internal)
| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 26% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 0.75 | 13% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 46 | 52 | 60 | 52 | 44 | 50.8 | 49.8 | 16 |
| Clarity & Presentation | 54 | 56 | 66 | 56 | 52 | 56.8 | 55.9 | 14 |
| Novelty & Originality | 48 | 44 | 60 | 50 | 42 | 48.8 | 47.9 | 18 |
| Significance & Impact | 52 | 54 | 70 | 58 | 50 | 56.8 | 55.5 | 20 |
| Experimental Validation | 40 | 46 | 58 | 50 | 38 | 46.4 | 45.2 | 20 |
| Reproducibility | 50 | 52 | 58 | 54 | 48 | 52.4 | 51.8 | 10 |
| Ethical Compliance | 60 | 60 | 66 | 62 | 60 | 61.6 | 61.2 | 6 |
| **Composite** | 48.6 | 51.1 | 62.1 | 53.8 | 46.2 | **52.4 (before)** | **51.4 (after)** | |
| Pool position (P%) | 38 | 42 | 66 | 50 | 36 | | | |

No dimension spread exceeds 20 (Significance and Experimental Validation sit at exactly 20): the divergence is R3's more generous view of Significance (70) and Experimental Validation (58); the editor adopts the view that a first paper on a new task earns moderate Significance but that the evidence supports Experimental Validation in the mid-40s.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) — "Borderline Reject (3)" internal |
| Venue-weighted composite | 51.2, band 3 |

*Official rating mean 3.20; EIC-weighted rating 3.13; before composite 52.4; after composite 51.4. Emphasis weights are heuristics, not official ICLR weights.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Mitty: Diffusion-based Human-To-Robot Video Generation" to ICLR. Converting a human demonstration into an embodiment-specific video with a large pretrained video model is a timely idea, and the paper is a reasonable first step.

**Overall Assessment:** The panel found a simple, effective conditioning recipe on a strong open backbone and an honest account of its limits, and was positive about the reference-video ablation and the failure analysis. It also found that the strongest claims — state-of-the-art, cross-task generalization and a benefit from mixed training — are not backed by controlled evidence and, for mixed training, are contradicted by Table 2.

**Key Strengths Identified by Reviewers:**
1. A relevant task and a simple, accessible recipe (R1, R2, R3, R4).
2. A large, clearly informative effect of the human reference video (Table 2; R1, DA).
3. Candid limitations and failure analysis (§5, Suppl. D; R1, R3, R4, DA).

**Key Concerns Requiring Attention:**
1. No matched-data or intermediate-representation baseline; the SOTA comparison involves zero-shot editors and a non-learned pipeline (CONSENSUS-4).
2. The data-synthesis/mixed-training contribution is contradicted by Table 2 and described in conflicting ways (CONSENSUS-3).
3. Cross-task generalization is untested and the train/test split unit is unstated (CONSENSUS-3); table and text inconsistencies (CONSENSUS-3); single-run, small-n evidence (CONSENSUS-2).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest challenge is that Mitty's EPIC training targets are filtered Masquerade renders, so beating raw Masquerade measures the filter rather than the benefit of bypassing intermediate representations; this must be addressed with a matched-data baseline or a narrower claim.

**Decision: Borderline Reject (3)** — ICLR rating 4 on {0,2,4,6,8,10}.

This draft is borderline-reject because the unsupported and contradicted claims weigh more than the task value. A revision that adds a matched-data baseline, the with/without-synthetic-data ablation, a held-out-task evaluation, uncertainty estimates and reconciled tables, and narrows the claims to what is shown, would likely change how a panel sees it. This is a simulation of how a careful panel would likely see this draft, not a prediction.

Sincerely,
Prof. Adaeze Brandvold (fictional persona)
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No matched-data baseline; SOTA framing | R1, R2, R4, DA | CONSENSUS-4 |
| Mixed-training claim contradicted | R1, R4, DA | CONSENSUS-3 |
| Cross-task generalization untested | R1, R4, DA | CONSENSUS-3 |
| Table/text inconsistencies | R1, R4, DA | CONSENSUS-3 |
| Method ambiguity (Eq. 4/Fig. 2/objective) | R1, R4, DA | CONSENSUS-3 |
| Success is video-level, not robot-level | R3, DA, R1 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall merit (3 vs 4) | R3 (4, pool 66) | R1, R2, R4, DA (3; pools 36–50) | Rule on evidence: the contradicted contribution, untested generalization and missing matched baseline were verified; R3 does not rebut them. Weighted toward 3 |
| Novelty of "first" claim | R2: overstated | R3/R4 implicitly accept | Partly correct: "first end-to-end DiT" may stand, "first end-to-end H2R video generation" does not in this form |
| Teacher–student circularity | DA | — | Partly correct: affects EPIC, not H2R |

### Score Spread Discussion
Significance and Experimental Validation reach 20 (not above): R3 is more generous on both; see above. Novelty (18) and Technical Rigor (16) are below the flag threshold.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Teacher–student circularity; no matched-data baseline | Yes (R1-W2, R2) | n/a | New experiments |
| DA-M2 | MAJOR | Mixed-training contradiction | Yes (R1-W1, R4) | n/a | Experiments + rewording |
| DA-M3 | MAJOR | Cross-task generalization untested | Yes (R1-W3) | n/a | New evaluation split |
| DA-M4 | MAJOR | Numeric inconsistencies | Yes (R1, R4) | n/a | Clarification |
| DA-M5 | MAJOR | Human study under-specified; small n | Yes (R1-W7) | n/a | Additional reporting |
| DA-M6 | MAJOR | Bypass-of-intermediate-representations wording | Yes (R2-W3) | n/a | Rewording |
| DA-M7 | MAJOR | Robot-level claims without robot-level evidence | Yes (R3-W1) | n/a | Rewording/proxy |
| (no DA-CRITICAL raised) | | | | | |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*Issues the EIC verified as undermining a main claim or secondary contribution. No upheld DA-CRITICAL issue.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Mixed-training/data-synthesis claim contradicted; no with/without-synthetic-data ablation | R1-W1, R4-W2, DA-M2 | §1, §4.6, §6, Table 2 | Ablation (H2R-only vs H2R+EPIC-synthetic vs EPIC-only; test on H2R and held-out tasks); rewrite §1/§6 | Medium; ≈ 40 GPU-h | Yes (partly) |
| R2 | No matched-data baseline for end-to-end vs intermediate representation; SOTA wording | R1-W2, R2-W1, R4-W1, DA-M1 | Table 3, §4.4, Abstract | Fine-tune a VACE-style/channel-concat conditioner and a keypoint/arm-render-conditioned variant on the same pairs; or narrow the claim to outperforming rendering and zero-shot editing | High; ≈ 40–80 GPU-h | Partly |
| R3 | Cross-task generalization untested; split unit not stated | R1-W3, DA-M3 | §4.2, §3.3, C2 | Leave-task-out on H2R; episode-level splits; state split protocol | Medium | Yes |
| R4 | Table/text inconsistencies (SR 86 vs 81; first frame said to consistently improve PSNR/SSIM) | R1-ERR-1/2/3, DA-M4 | §4.5, Tables 1–3 | Re-derive tables from logs; align text; state Table 3's test set | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Uncertainty and statistics: CIs for SR, paired tests, FVD protocol, 3 seeds for 5B | R1-W4, DA-M5 | Wilson/bootstrap CIs, McNemar, FVD details | Low–Medium; ≈ 60 GPU-h for seeds | Yes |
| S2 | Human-study protocol: κ, rater/item counts, Embodiment Consistency formula | R1-W7, DA-M5 | Report in appendix | Low | Yes |
| S3 | Position against Human2Robot [51] and in-context video DiTs; ablate Eq. 4 vs plain concatenation | R2-W1, R2-W2 | Differentiate/compare; Eq. 4 ablation; cite AVID, "Video Diffusion Transformers are In-Context Learners" | Medium | Yes |
| S4 | Bypass-narrative wording and teacher-bound discussion; real-GT-only evaluation on H2R | R2-W3, DA-M1/M6 | Reword; separate real vs rendered GT | Low | Yes |
| S5 | Robot-level claims: qualify "task success"; add a reachability/collision proxy | R3-W1, DA-M7 | Reword; proxy on 20–50 clips | Medium | Partly |
| S6 | Method clarity: Eq. 4 vs Fig. 2, training objective, 14B naming/steps, step-count confound | R1-W6, R4-W3 | Exact attention definition; objective; matched or reported steps | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Licence/API-use statement | R3-W4 | Add paragraph on EPIC/Ego4D licences and API uploads |
| N2 | Embodiment retargeting; chained clips; difficulty breakdown | R3-W2/W3 | One additional robot arm; camera-motion breakdown |
| N3 | HaMeR citation; section-title swap; typos; decimals; GPT mention; "paradoxical in-context learning" | R1, R2, R4, DA | Copy-edit |
| N4 | Worth discussing: FullDiT2, RoboSwap (recent preprints, not required) | R2 | Mention in related work |
| N5 | Helpful references | R2 | AVID, Learning by Watching (IROS 2021), Imitation from Observation (ICRA 2018) |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 1–2 weeks (≈ 80–150 GPU-hours plus writing)
- Priority 2: 6 items, roughly 1 week
- Priority 3: 5 items, 1–2 days
- **Total estimated revision time**: about 2–3 weeks; the Priority 1 experiments are only partly feasible in a one-week rebuttal window.
