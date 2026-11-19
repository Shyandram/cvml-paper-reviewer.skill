# Academic Paper Review: *Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding* (DAIR)

*Simulated panel review (full mode), 2026-11-10. User request: "Review this paper. Target venue: ICLR. Full review, skip confirmation, literature check: strict, cutoff date 2025-09-24." All five reviewers are fictional personas and were run as five separate role-based passes in **one shared model context**; they are not independent agents. Figures were not available (text extraction only): figure-dependent claims (Fig. 1, 3–6, 7–14) are judged from captions and text. The text extraction garbles Table 4 layout slightly; values below were read carefully but remain "as extracted".*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding |
| Primary Discipline | Computer Vision → low-level vision → all-in-one image restoration (AIR) |
| Secondary Discipline(s) | Generative latent-variable models (VAE), efficient architectures, image-quality assessment, object detection (downstream) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | VAE-style multi-scale latent encoder with supervised-contrastive regularizer; luminance/chrominance dual-branch U-Net; FFT-based degradation map; FiLM-style bottleneck modulation; element-wise sigmoid-gated decoder ("3WD") |
| Target Venue | ICLR (2026 cycle) (stated by the user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none (ICLR: Soundness/Presentation/Contribution 1–4, rating on {0,2,4,6,8,10}; public reviews; revised PDF possible during discussion) |
| Paper Maturity | Submission-ready in form, but with unresolved protocol and consistency issues |
| Ethics-Relevant Content | New annotated detection test set (3,000 images, App. B.4) with no stated license/annotation protocol; medical images (App. C.4–C.5); otherwise none |

### Claimed Contributions (as stated by the authors)
1. **C1** Reframe AIR as learning latent degradation priors directly from the corrupted image, "eliminating the need for external manual prompts (MP)" (Abstract; §1 contribution 1).
2. **C2** A "which–where–what" reasoning paradigm: latent prior encoding (LPE, Eq. 2–3), a learnable spatial Degradation Map (DM, Eq. 4–7), and latent fusion (LF, Eq. 8–9) (§1 contribution 2, §3.1).
3. **C3** A decoder, 3WD, with "linear complexity" performing "explicit spatial reasoning" (Eq. 10, §3.2, §4.6, Table 5).
4. **C4** "Consistently outperforms SOTA" on six common, five compound and unseen degradations, "average 1.68 dB PSNR gain", "three times more efficient", and up to "7.40 mAP" detection gain (Abstract; §1 contribution 3; Tables 1–4, 9, 10).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Common-degradation tasks: dehazing SOTS, deraining Rain100L, desnowing CCD, deblurring GoPro, denoising DIV2K with random σ∈[0,50], low-light LSD (§4.1). Compound: CDD, five types in Table 3; haze+snow and low-light+rain held out as "unseen" (§4.1, Table 4). Ablations use four tasks (§4.1, Table 6). Latent encoder pre-trained "for 200,000 steps" on six single + five compound degradations with L1 + KL + "discriminative latent regularizer" (§4.1); Algorithm 1 gives T1 = 300K, T2 = 100K, β_max = 0.3, λ_con = 0.01 and takes degradation labels y_i as input (App. A.4); SupCon loss uses same-label positives (Eq. 17). Main network "trained for 100,000 to 500,000 steps, depending on task complexity" and "tune[d] ... for TS settings" (§4.1). Adam, lr 1e-4, batch 4, 256×256 crops, one RTX 3060. Baselines "trained using their official implementations and suggested hyperparameters" (§4.1). Splits (train/val/test), seeds, number of runs, model selection rule, code/data release, licenses: **not stated** after text search for "test set, validation, held-out, select, tuned, checkpoint, seed, code, release, licen, consent".
- **Headline numbers.** 1.68 dB average (Abstract; not a table entry: equals the mean of the three average gains +2.78 [Table 1], +0.78 [Table 3], +1.47 [Table 4]); "three times more efficient" (Abstract; Table 1 GFLOPs 45.65 vs ADAIR 147.18; Table 9); 6-task average 28.15 dB / 0.8829 (Table 1); compound average 22.61 / 0.8277 (Table 3); unseen average 20.97 / 0.8415 (Table 4); 3WD vs SA/CA +7.72 dB (Table 5); ablation 26.90 / 0.8565 (Table 6); detection AP 34.9 vs 31.7 (Table 10); "up to 7.40 mAP" (§1; source not found in text).
- **Appendix adds.** VAE and loss details (A.2), architecture and training algorithm (A.3–A.4), low-light breakdown (Table 7), denoising on BSD100/Urban100 (Table 8), inference benchmark (Table 9), a self-built detection benchmark (Table 10), no-reference-metric results on five out-of-distribution domains with no baselines (Tables 11–15), failure cases (Fig. 14, App. D).
- **Unverifiable.** All figures (1–14), including the t-SNE (Fig. 5b), the Degradation Map visualizations (Fig. 6) and qualitative comparisons; Table 4 row alignment is slightly garbled by extraction.

### Integrity signals
`scripts/integrity_scan.py` on the paper text: **0 findings** (no text addressed to reviewers or AI systems, no hidden characters). Reviewers read the (identical) redacted copy.

### Literature-check setup
Mode: **strict**, cutoff **2025-09-24**. Fingerprint written (method names DAIR, 3WD, DAEB, LPE; cutoff date); used only to exclude the paper. Results are reported in the Phase 1.5 addendum.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ingrid Valdemar, senior researcher at an industrial vision lab (Northern Europe)
- **Seniority / Expertise**: Senior scientist, repeat area chair / Image restoration, evaluation methodology, efficient vision models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights reviewers, makes the final decision
- **Style**: Calibrated to what ICLR accepts; checks numbers herself and gives little credit to rhetoric.

### Reviewer 1 (Methodology): Dr. Kaveh Marandi, mid-career faculty, vision group at a large public research university (Middle East)
- **Seniority / Expertise**: Mid-career / Low-level vision benchmarking, PSNR/SSIM protocols, training-budget matching for AIR methods
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table and insists on matched training budgets.

### Reviewer 2 (Domain): Prof. Naledi Dube, senior faculty, imaging lab at a research university (Southern Africa)
- **Seniority / Expertise**: Senior / All-in-one restoration, degradation representation learning, prompt-based restoration
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work closely, asks what is actually new relative to the closest method.

### Reviewer 3 (Perspective): Dr. Mateo Ferreira-Lund, computational photography researcher, camera-systems group at an industrial lab (South America / Europe)
- **Seniority / Expertise**: Senior industry scientist / ISP pipelines, signal processing, edge deployment, detection under adverse conditions
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive, looks for what would make the work useful in a real pipeline.

### Reviewer 4 (Generalist): Dr. Hana Ishikura-Moore, assistant professor, machine-learning group at a research university (East Asia)
- **Seniority / Expertise**: Early-career faculty / Representation learning and generative models, not restoration specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; wants the contribution stated plainly and supported.

### Devil's Advocate: Prof. Dmitri Aksoy, senior faculty, statistics and ML-evaluation group at a research university (Central Asia / Europe)
- **Seniority / Expertise**: Senior / Evaluation methodology, causal attribution of gains, shortcut learning
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; attacks only after stating the strongest version of the case.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Five Reviewer Reports

---

# Peer Review Report (Reviewer 1)

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Reviewer: Dr. Kaveh Marandi, Methodology Reviewer (vision group, large public research university; fictional persona)
## Expertise: low-level vision benchmarking; PSNR/SSIM protocols; matched-budget comparison of AIR methods
## Date: 2026-11-10

## Summary
The paper proposes DAIR, a U-Net-style restoration network conditioned on features from a separately pre-trained, frozen, VAE-like encoder whose bottleneck is regularized with a supervised contrastive loss over degradation labels. The encoder features modulate attention values (Eq. 2), feed a learned one-channel "degradation map" (Eq. 4–7) and a FiLM-like bottleneck fusion (Eq. 8–9), and the decoder uses a sigmoid-gated element-wise product ("3WD", Eq. 10). The authors report gains over six AIR baselines on a six-task mixture (Table 1), five CDD compound settings (Table 3), two held-out compound settings (Table 4), plus ablations, a speed table and a detection test.

## Strengths
### S1: Broad evaluation scope
Six single-degradation tasks, five compound types and two held-out compound types are reported, with both PSNR and SSIM and with params/FLOPs next to quality (Table 1). Breadth is above that of many AIR papers.

### S2: Efficiency is reported next to quality
Table 1 lists 18.08M parameters and 45.65 GFLOPs at 256×256, and Table 9 gives latency, FPS and throughput on a stated GPU (RTX 3060, FP32) at three resolutions. This is the right way to support an efficiency claim, even though the text overstates it (W3).

### S3: Frozen-encoder protocol and honest failure cases
The encoder is trained once and frozen for all experiments (§4.1, App. A.4), so the same prior serves every setting; failure cases and the limitation of tests on modest hardware are stated (App. D, Fig. 14).

### S4: Component ablation exists
Table 6 ablates LP/LF/DM/3WD progressively and includes a "w/o Latent Prior" row, which allows the central claim to be checked (see W2).

## Weaknesses

### W1: Baseline training protocol is unspecified and appears unmatched; baseline numbers look anomalous
§4.1 says baselines were "trained using their official implementations and suggested hyperparameters", while DAIR uses a 200K–300K-step supervised pre-training stage with degradation labels (App. A.4), then a main network trained "for 100,000 to 500,000 steps, depending on task complexity" and tuned "for TS settings". It is not stated (a) whether Table 1 is one all-in-one DAIR model or per-task models (the sentence "We only tune the main network for TS settings" suggests the latter), (b) the step/epoch/batch budget of each baseline (all training here uses batch 4 on one RTX 3060, far below typical AIR schedules), (c) whether baselines were trained on the same data mixture, including the exclusion of the held-out compound types in Table 4, (d) how "100K–500K" was chosen and on which split. Baseline numbers are strikingly low or erratic: Restormer denoising 20.41 dB (Table 1) and 16.62 dB at σ=50 on DIV2K (Table 8); DFPIR, a CVPR 2025 method, is the weakest of the recent prompt/frequency AIR methods in Tables 1, 3 and 4 (average 24.46 in Table 1: only 0.12 dB above Uformer's 24.34 and below PromptIR 25.37 and ADAIR 25.35; 18.78 in Table 3, below Uformer's 20.68) and sits at ≈21.5 dB across σ = 15/25/50 on BSD100 and Urban100 (Table 8), i.e. flat in noise level. These patterns point to under-trained or mis-configured baselines, so the headline gains cannot be attributed to the method.
- **Suggested Fix**: State the protocol in a table (steps, batch, data, single model vs per-task, pre-training for each method). Train all methods under one identical budget (including DAIR without the extra encoder pre-training budget counted), and show baselines at their published checkpoints/numbers on at least one benchmark they were originally reported on (e.g., the CDD numbers from the OneRestore paper). Cost: ~6 methods × 1 re-run ≈ 100–200 GPU-h on an RTX-3060-class card.

### W2: The ablation does not support latent priors as the source of the gain, and shows an implausible interaction
Table 6: adding LP to the base model changes the 4-task average from 20.22 to 20.49 dB (+0.27 dB; desnowing and deraining PSNR actually drop: 20.76→20.75, 22.70→22.46), and Base+LP+LF+DM reaches 21.77. "DAIR w/o Latent Prior" (✗ LP, ✗ LF, ✓ DM, ✓ 3WD) scores 22.67, yet adding LP+LF to it yields 26.90 (+4.23 dB). So LP+LF are worth ≈0.9 dB without 3WD (Base 20.22 → Base+LP+LF 21.08) but ≈4.2 dB with 3WD, and 3WD adds +5.13 dB on top of Base+LP+LF+DM (21.77→26.90). A +4–5 dB jump from a sigmoid gate is far outside what such modules usually contribute and suggests that the rows were trained under different budgets or configurations. It is also unclear how DM (which takes x_ℓ as K/V, Eq. 5) and 3WD operate when "LP" is removed. The text's claim that removing latent priors "highlight[s] its critical role" (§4.7) rests on a row that also removes LF.
- **Suggested Fix**: Specify what replaces x_ℓ in each ablated row; re-run all rows with identical seeds/steps; add rows "3WD only", "LP via plain autoencoder (no KL, no SupCon)", and "LP with labels shuffled". Cost: ~8 runs × 4 tasks.

### W3: Efficiency and "linear complexity" claims are not supported as worded
Abstract: "three times more efficient". Table 1 supports ≈3.2× fewer FLOPs than ADAIR only, but DAIR has more FLOPs than Uformer (45.65 vs 43.86 G). Table 9 shows DAIR at 20.55/55.20/220.92 ms for 128²/256²/512² versus Uformer 31.07/58.08/203.83 ms: at 512×512 DAIR is slower, with lower FPS (4.53 vs 4.91) and throughput (1.19 vs 1.29 MP/s). The text ("consistently achieves the fastest processing times, highest FPS, and superior throughput across various image sizes", App. B.3) is contradicted by its own table. Table 9 also omits Restormer, AIRNet and DiffUIR, and it is not stated whether params/FLOPs/latency include the frozen VAE encoder that must run at inference (the VAE decoder is unused). §4.6 claims "85-257× speedup and 76-89% memory reduction" for 3WD vs SA/CA, but Table 5 contains no speed or memory numbers, and §3.2 (O(HW)) and §4.6 (O(d²×H×W)) state different complexities; the implementation of the SA/CA baselines is not stated: dense attention over 256×256 = 65,536 tokens is very expensive on a single RTX 3060, so what was actually run (windowed? downsampled? transposed?) is a question I cannot resolve from the text.
- **Suggested Fix**: Report params/FLOPs/latency for the complete inference pipeline including the encoder; include all baselines in Table 9; narrow the abstract claim to what is measured; give the Table 5 speed/memory numbers and the exact SA/CA implementation (windowed? downsampled? transposed?).

### W4: No variance, no significance, many small margins
All results are single runs without seeds or intervals. Margins in the compound table are small: +0.37, +0.35, +0.44 dB in three of five columns (Table 3), +0.25 dB denoising (Table 1), +0.04 to +0.28 dB on DIV2K/BSD100/Urban100 (Table 8). With batch 4 on a small GPU run-to-run noise could be of this order. At this scale of training (small crops, one GPU) 3 seeds are feasible.
- **Suggested Fix**: 3 seeds on Tables 3 and 8 and mean±std; paired bootstrap over test images for the ≤0.5 dB cells. ≈ 3× the cost of those rows.

### W5: Protocol and split reporting missing; "unseen" test is narrower than claimed
No statement of train/val/test splits, checkpoint selection, or which split chooses the 100K–500K step count (protocol sweep found none). DIV2K is used for both training and the "denoising" test of Table 1; which DIV2K images are test is not stated. The "unseen degradations" of §4.4/Table 4 are two CDD combinations whose components (haze, snow, low-light, rain) are all in the labelled pre-training set; the unseen out-of-domain results (App. C, Tables 11–15) report input vs output no-reference metrics with no baselines.
- **Suggested Fix**: Give a split table; state selection rule; add baselines to Tables 11–15 or drop "generalizes" wording; test one genuinely new degradation (e.g., motion + noise at unseen level, JPEG, lens flare) against baselines.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 8 vs App. B.1.2 text | "improvements of up to +2.2 dB PSNR at high noise levels" | Table 8 Improvement row: max +0.28 dB (BSD100 σ=15); three cells are negative (−0.16 BSD100 σ=50, −0.18 and −0.16 Urban100 σ=25/50). "consistently achieved higher scores" is also contradicted. | Cross-referenced text with Table 8 improvement row; recomputed e.g. 31.83−31.99=−0.16 | High | MAJOR | Correct the text; state that AIRNet is better in 3 of 9 cells |
| ERR-2 | E1/E9 | Table 8, BSD100 columns | "33.28/0.9219" (Uformer, σ=15 and σ=50) | Identical PSNR/SSIM at σ=15 and σ=50 is implausible; further identical pairs across methods: DiffUIR BSD100 σ=50 "31.99/0.9122" = DAIR BSD100 σ=25; Restormer BSD100 σ=50 "31.59/0.8937" = ADAIR BSD100 σ=25; PromptIR σ=25 "27.03/0.7007" ≈ AIRNet σ=50 "27.03/0.7006". The BSD100 σ=50 column looks mis-assembled (ADAIR 14.07 vs 26.80 on DIV2K, DiffUIR 31.99 vs 14.34). | Cross-referenced cells (two locations each) | High | MAJOR | Re-generate and re-check Table 8; release raw per-image results |
| ERR-3 | E1 | Table 9 vs App. B.3 text | "consistently achieves the fastest processing times, highest FPS, and superior throughput" | At 512×512 Uformer is faster (203.83 vs 220.92 ms), higher FPS (4.91 vs 4.53) and throughput (1.29 vs 1.19). | Read two rows of Table 9 | High | MAJOR | Narrow the claim |
| ERR-4 | E1 | §4.2.1 vs Table 1 | "+5.64 PSNR and +0.0758 SSIM in desnowing" | Table 1 improvement row gives +4.42/+0.0401 (31.50−27.08 vs best baseline PromptIR); 5.64/0.0758 are gains over ADAIR (25.86/0.8812), not over the best method. | Recomputed from Table 1 | High | MINOR | Report gain vs best baseline |
| ERR-5 | E1 | Table 7 Improvement row | "+1.06/+0.0059 ... +0.87/+0.0469" (Lowlight Outdoor PSNR +0.87) | DAIR 14.77 vs best baseline DFPIR 14.74 → +0.03, not +0.87 (0.87 is vs Restormer 13.90). The text "consistently outperforms others" is a tie in this cell. | Recomputed from Table 7 | High | MINOR | Correct the cell |
| ERR-6 | E1 | §4.4 vs Table 4 | "average gains of +1.47 dB PSNR and +0.0412 SSIM" | Table 4 improvement row gives +0.0523 SSIM (0.8415−0.7892 vs PromptIR); 0.0412 is vs ADAIR (0.8003). PSNR figure is vs PromptIR, so the two numbers use different baselines. | Recomputed from Table 4 | High | MINOR | Use one reference baseline |
| ERR-7 | E6 | §4.1 vs App. A.4 Algorithm 1 | "pre-train our latent encoder for 200,000 steps" | Algorithm 1 sets "T1 = 300K" for the same VAE pre-training stage. | Cross-referenced | High | MINOR | Reconcile |
| ERR-8 | E6 | §3.2 vs §4.6 | "achieves linear computational complexity" | §3.2 states O(HW) per stage; §4.6 states "linear complexity O(d2"×H×W; Table 5 lists O(HW). Projections W_Q,W_K,W_V cost O(C²HW), so "exactly HW × C operations" is not the full cost. | Cross-referenced | High | MINOR | State one complexity with channel dimension |
| ERR-9 | E6 | App. C.1 | "Table. 8 and Figure 9 illustrate the performance of the proposed method on real-world noisy images" | Real-world denoising numbers are in Table 11; Table 8 is BSD100/Urban100 synthetic denoising. | Cross-referenced | High | MINOR | Fix reference |
| ERR-10 | E1 | Table 14 vs Table 11 | "Improvement −4.26 ... −0.16" | Sign convention flips: NIQE improvement is shown positive in Tables 11/12/13/15 (+1.33, +0.05, +0.33, +4.35) but negative here for an equally lower-is-better gain (13.94→9.68). LPIPS rises 0.63→0.79 yet is called an improvement row. | Cross-referenced tables | High | MINOR | Harmonize and explain the LPIPS reference |

*Questions rather than errors (Low confidence/unverifiable):* the "up to 7.40 mAP" gain in §1 is not reproduced by Table 10 (largest gap to a listed method is 7.0 AP vs DFPIR on AP[.5:.95], 7.3 at IoU 0.50); it may come from Fig. 1, which is unavailable.

*Omission sweep:* split/selection protocol, seeds/variance, baseline budget, code/data, licenses: **not stated after search**. Compute: present (single RTX 3060, §4.1; training time not stated). Hyperparameters: present for optimizer, crop, β, λ (§4.1, A.2) but not for DM/3WD module widths or how step counts were chosen. Failure cases/limitations: present (App. D).

**Minor:** typos ("Restformer", "Refrenece", "We propose reframe"); duplicated "deblurring" dataset entry in §4.1; Fig. 2 text says F_µ = γ⊙[L3+C3]+β (§3) while Eq. 9 uses (1+γ) and F_LC.

## Claim-to-evidence map (compressed)

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Latent priors replace manual prompts | Abstract, §1 | Tables 1, 3, 4; labelled SupCon pre-training (Eq. 17, Alg. 1) | Partially: no prompts at inference, but supervised by degradation labels in pre-training |
| C2 | which/where/what reasoning is what yields the gain | §3.1, Table 6 | LP alone +0.27 dB; large gains only with 3WD | Partially supported / ablation inconsistent |
| C3 | 3WD is linear-complexity and better than SA/CA | §3.2, §4.6, Table 5 | Table 5 quality only; no speed/memory numbers | Quality shown (implausibly large), efficiency unsupported |
| C4 | Consistently outperforms SOTA, 3× efficient | Abstract | Tables 1–4, 8, 9 | Partially: gains real in tables but baseline protocol unverifiable; efficiency overstated |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Unmatched/undocumented baseline training; ablation inconsistent; table errors |
| Clarity | 2 | Protocol and ablation rows underspecified; multiple text–table mismatches |
| Significance | 2 | Useful if gains hold; unverified |
| Originality | 2 | Assembly of known components (see R2) |

## Dimension Scores (0–100)

**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main comparison rests on authors-retrained baselines with an unstated, apparently unmatched protocol and anomalous numbers, and the ablation contradicts the central "latent prior" narrative.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | Fairness and protocol gaps; several text–table contradictions |
| Clarity & Presentation | 50 | Developing | Method readable, but experimental protocol and tables inconsistent |
| Novelty & Originality | 45 | Developing | Mostly known building blocks |
| Significance & Impact | 48 | Developing | Gains would matter if reproducible |
| Experimental Validation | 38 | Developing | Breadth good, depth/fairness poor |
| Reproducibility | 40 | Developing | No code, no splits, no seeds, undefined SA/CA baselines |
| Ethical Compliance | 55 | Developing | Limitations discussed; new annotated set without documentation |

## Questions for Authors
1. Is Table 1 a single all-in-one DAIR model or per-task models, and what exactly were the step/batch/data budgets of each baseline? (A matched-budget result with DAIR ≤ baseline budgets would raise my score to 3–4; an unmatched protocol keeps it at 2.)
2. Do reported Params/FLOPs/latency include the frozen VAE encoder at inference?
3. In Table 6, what replaces x_ℓ in the DM and 3WD when LP is removed, and were all rows trained for equal steps?
4. How is "100K–500K steps depending on task complexity" chosen, and on which split?
5. What produced the "up to 7.40 mAP" figure in §1?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. App. D lists failure cases and the absence of edge-hardware tests, but not the label supervision of the prior, the baseline-protocol caveats or data/annotation documentation.

## Ethics Review Flag
**No.** (Documentation of the new annotated set and of medical-image use is a minor issue, see R3.)

## Overall Score
**2**: Promising breadth and a reasonable design, but the central comparison cannot be trusted as reported, and the paper's own ablation and tables contradict several claims.

## Confidence
**4**: Recomputed all tables; could not see figures or the supplement code.

---

# Peer Review Report (Reviewer 2)

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Reviewer: Prof. Naledi Dube, Domain Reviewer (imaging lab, research university; fictional persona)
## Expertise: all-in-one restoration; degradation representation learning; prompt-based restoration
## Date: 2026-11-10

## Summary
DAIR argues that existing AIR methods either need manually specified prompts or hard-code frequency heuristics, and offers instead a pre-trained VAE-like latent encoder whose multi-scale features and bottleneck code condition a restoration U-Net, plus a degradation map and a gated decoder. The contribution is positioned as new in "reframing AIR as latent prior inference" and in a "which–where–what" decomposition. Reported results beat six baselines on common, compound and held-out compound degradations and on a downstream detection test.

## Strengths
### S1: Clear gap statement and sensible structure
The paper states a gap (blind restoration without prompts, §1) and organizes the method around three questions, which makes the pipeline easy to map to Fig. 2.

### S2: Combines several useful ingredients
Luminance/chrominance dual branches, a degradation-conditioned spatial map and bottleneck modulation are reasonable choices for mixed degradations, and the bottleneck FiLM-style modulation conditioned on a learned code is well motivated (§3.1.3).

### S3: Evaluation includes compound and held-out compound cases
Using CDD (Guo et al., 2024) and holding out two combinations (§4.1, Table 4) is a step toward testing compositional generalization.

### S4: Useful downstream-task angle
Testing detection on restored images (App. B.4, Table 10) is a relevant, rarely reported axis for AIR.

## Weaknesses

### W1: The problem framing mischaracterizes prior work, so the claimed gap is overstated
§1 sorts prior work into (1) hand-crafted frequency/architectural priors (ADAIR, AirNet) and (2) methods that "rely on explicit, manually provided prompts" (PromptIR, DFPIR). §2.2 says PromptIR "integrates text-based prompts" and Table 1 marks PromptIR and DFPIR with MP ✓. As I understand it, PromptIR is a *blind* method whose prompts are learned, input-conditioned modules that need no user text [verify against the cited paper's abstract; see addendum]. AirNet (cited in §2.1 as using "contrastive learning to extract degradation representations") already learns an implicit degradation embedding from the input alone, which is the paper's own C1 mechanism; DAIR's SupCon regularizer with degradation labels (Eq. 17, App. A.2) is the AirNet-style idea. And DAIR itself uses an FFT magnitude/phase branch (Eq. 4), i.e., a hand-crafted frequency cue of the very kind criticized in the abstract ("embed hand-crafted architectural priors (e.g., frequency heuristics)"). The "chicken-and-egg" motivation therefore does not separate DAIR from the closest blind baselines.
- **Suggested Fix**: Reframe against AirNet-style learned degradation embeddings and blind prompt-learning methods; correct the MP column; compare explicitly with latent/embedding-conditioned AIR methods.

### W2: Novelty relative to learned-degradation-embedding AIR is modest and not isolated
The method is (i) a pre-trained autoencoder-like encoder with KL (β=0.3) and SupCon (λ=0.01) used as a feature conditioner, (ii) value-modulation of attention (Eq. 2), (iii) a one-channel gate from FFT features (Eq. 4–7), (iv) FiLM-style fusion (Eq. 8–9), (v) a sigmoid gate in the decoder (Eq. 10). Each is a known building block, and Table 6 shows that the "latent prior" alone contributes +0.27 dB (20.22→20.49). The novelty claim is therefore the combination, and its worth must be shown against an AirNet-like encoder (contrastive, no VAE) plugged into the same network; this control is absent. The VAE reconstruction objective reconstructs the *degraded* input (Eq. 15), so nothing in the objective makes x_ℓ degradation-specific beyond the weak SupCon term at the bottleneck (λ=0.01); the statement that this multi-objective training "ensures that hierarchical features" capture degradation-specific representations at multiple scales (§3.1) is asserted, not tested.
- **Suggested Fix**: Add "AirNet encoder in DAIR" and "plain autoencoder (no KL, no labels)" controls; probe x_ℓ (linear probe for degradation type, mutual information with labels) per scale.

### W3: "Unseen" and "reasoning" language is not backed by the experiments
Unseen = two CDD combinations of seen components (Table 4) and out-of-domain images evaluated with no-reference scores and no competing methods (Tables 11–15), where several gains are negligible (underwater NIQE 3.83→3.78, LPIPS +0.00, Table 12; LSD-U MUSIQ 62.33→62.51, Table 13). The "reasoning paradigm" is a naming scheme for existing skip/gating components; "explicit spatial reasoning" (§1) describes a sigmoid-gated product.
- **Suggested Fix**: Tone down; add baselines to Tables 11–15; define "unseen" as unseen primitive types.

### W4: Positioning against compound-degradation baselines
OneRestore (Guo et al., 2024), the source of CDD and a method designed for compound degradations, is cited (§2.2) but is not a baseline in Table 3 or 4; all compared methods are re-trained by the authors. Beyond the listed baselines, other recent blind/learned-embedding and prompt-learning AIR methods are not discussed (see addendum).
- **Suggested Fix**: Add OneRestore and 2–3 recent blind AIR methods; report them at their official numbers where the protocol matches.

### Citation check (E7)
The paper's argument leans on: PromptIR (§1, §2.2, Table 1 "MP ✓"), DFPIR (§1, §2.2, "CLIP-encoded text prompts"), ADAIR (§1 "hand-crafted frequency priors"), AirNet (§1, §2.1), UHD-Processor (§2.2, "VAE-based framework"). Results of checking against kept abstracts are in the literature-check addendum below. Also, two attributions look wrong (E7, Medium confidence): "Guo et al. (2023)", whose title is "Letting go of self-domain awareness: Multi-source domain-adversarial generalization via dynamic domain-weighted contrastive transfer learning", is cited as the source of the supervised-contrastive loss (§4.1, App. A.2); and DFPIR ("Tian et al. (2025a)") is cited for multi-head self-attention at the VAE bottleneck (App. A.2), where Vaswani et al. (2017) is the natural source. The authors should confirm both.

**Minor:** the "Related Works" subsection title "Image-to-Image Translation" covers restoration generally.

## Missing References
*See the Phase 1.5 literature-check addendum below for the verified list (this report is completed there).*

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See R1; claims partly unsupported |
| Clarity | 2 | Gap framing inaccurate |
| Significance | 2 | Moderate, if gains hold |
| Originality | 2 | Combination of known parts |

## Dimension Scores (0–100)

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: modest, unisolated novelty plus a framing that misdescribes the closest blind methods; offset by consistently positive tables and a sensible architecture.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Method understandable, claims about latent features untested |
| Clarity & Presentation | 52 | Competent (low) | Readable structure, inaccurate prior-work description |
| Novelty & Originality | 42 | Developing | Known blocks; no control against AirNet-style embeddings |
| Significance & Impact | 50 | Developing | Useful sub-area result |
| Experimental Validation | 45 | Developing | Missing key baseline (OneRestore) and controls |
| Reproducibility | 45 | Developing | Details partly given; no code |
| Ethical Compliance | 58 | Competent (low) | Limitations discussed |

## Questions for Authors
1. In what concrete sense is PromptIR's prompt "manual"? (A clear answer with evidence could raise Originality; otherwise the MP column should be corrected.)
2. How does DAIR differ from AirNet's contrastive degradation encoder plugged into the same network?
3. What does the x_ℓ of each scale encode (probe results)?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (App. D covers failure cases but not the label-supervised prior or framing).

## Ethics Review Flag
**No.**

## Overall Score
**3**: A reasonable design with positive tables, but the novelty is a combination of known parts, the framing overstates the gap, and key controls and baselines are missing.

## Confidence
**4**: Know the AIR literature well; relied on the paper's text for training details.

---

# Peer Review Report (Reviewer 3)

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Reviewer: Dr. Mateo Ferreira-Lund, Perspective Reviewer (camera-systems group, industrial lab; fictional persona)
## Expertise: ISP pipelines; signal processing; edge deployment; detection under adverse conditions
## Date: 2026-11-10

## Summary
The paper presents a restoration network that infers a degradation code from the input and uses it to route features, locate degraded regions and modulate fusion, aiming at a single prompt-free model for weather, low-light and noise. It adds a small benchmark showing that restored images improve YOLOv12-L detection and a set of out-of-domain visual examples. For a practitioner the proposition is attractive: one blind model that is cheaper than recent prompt-based restorers.

## Strengths
### S1: A deployment-relevant objective
A prompt-free, single-model restorer with ~18M parameters and ~46 GFLOPs at 256² (Table 1) is closer to what an ISP or robotics perception stack could host than 30M+ models or a 4,400 GFLOPs diffusion model (Table 1, DiffUIR).

### S2: Downstream-task evaluation
App. B.4 (Table 10) tests whether restoration helps detection, which is the real purpose in autonomous or surveillance settings, and reports AP by object size.

### S3: Frequency-domain cue links to classical signal processing
The FFT magnitude/phase branch in the degradation map (Eq. 4) connects to classical spectral degradation analysis and is cheap.

### S4: Failure cases and hardware candour
App. D reports artifacts in extreme low light (<5 lux) and over-enhancement underwater, and notes the absence of edge-hardware tests.

## Weaknesses

### W1: The detection result lacks the baselines that make it interpretable
Table 10 compares restorers only against each other. Missing: the detector on the **unrestored degraded input** and on **clean references**; without them one cannot tell whether any restorer helps (Uformer 28.0 and DFPIR 27.9 may be below the degraded input). The test set (3,000 annotated images, annotations transferred from clean references, App. B.4) is described in two sentences: no class list, box counts, annotator process or license; and the "first quantitative assessment" claim is not supported by a literature review. Detector retraining/fine-tuning on restored outputs, the standard alternative, is not tried.
- **Suggested Fix**: Add the degraded-input and clean-reference rows; document and release the annotations; temper "first".

### W2: Real-world robustness and hardware claims are thinly supported
Real-world and out-of-domain results (Tables 11–15) compare "Input" vs "Enhanced (Our)" with NIQE/MUSIQ/LPIPS and no other method. LPIPS is a full-reference metric, so its "Input" values (0.63–0.82) have no defined reference; gains in Tables 12 and 13 are negligible (e.g., MUSIQ 62.33→62.51), and in Table 14 LPIPS worsens 0.63→0.79. Efficiency is measured on a desktop RTX 3060 in FP32 only (Table 9); the latency advantage over Uformer disappears at 512×512, which is closer to real camera resolutions; mobile/edge numbers and memory are absent (App. D defers them).
- **Suggested Fix**: Run baselines on the same real images with no-reference metrics and a small user preference study; report peak memory and latency at ≥1080p with tiling; clarify the LPIPS reference.

### W3: An implicit assumption: the degradation types at test time are a small closed set
The latent prior is supervised with labels for six single and five compound types (Eq. 17, Alg. 1), and the held-out "unseen" cases are combinations of the same primitives. Real camera pipelines also have degradations that are not on this list (sensor noise with ISP interactions, JPEG/HEVC compression, lens flare, motion plus defocus). The paper does not show behaviour when the inferred code is wrong (e.g., a degradation type confusion), whether the model silently "over-enhances", or whether the frozen encoder is calibrated (the t-SNE in Fig. 5b is figure-only and cannot be checked here).
- **Suggested Fix**: Evaluate on RAW-to-sRGB noise, compression and flare cases; test with adversarially mismatched codes; report a confusion analysis of the latent prior.

### W4: Societal and data-documentation gaps
Medical images (App. C.4–C.5) are processed with a model not designed or validated for diagnostic use, with phrases such as "diagnostically relevant textures" (App. C.5) and "healthcare imaging" as an application (§4.2.1), but no caution that perceptual enhancement can alter clinically relevant content. There is no broader-impact statement, and the new annotated set has no license.
- **Suggested Fix**: Add a short impact/limitations note and datasheet; avoid clinical suggestions without clinician-validated metrics.

**Minor:** the title of Table 1 column "MP" is not defined in the caption.

## Missing References
Optional; no additional entries beyond R2's. Cross-disciplinary pointers (named methods only): attention-gate skip connections from medical segmentation, and spectral-domain restoration literature, are conceptually close to the "degradation map" and "3WD" gating and should be discussed as related lines of work.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Detection/real-world evidence incomplete |
| Clarity | 2 | Appendix claims exceed evidence |
| Significance | 3 | Practical objective is relevant |
| Originality | 2 | See R2 |

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically relevant objective with positive headline numbers on many tasks; held back by missing no-restoration detection baselines, weak real-world evidence and a closed-set assumption.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent (low) | Reasonable design; gaps in evidence |
| Clarity & Presentation | 58 | Competent | Understandable |
| Novelty & Originality | 52 | Developing | Combination of known blocks |
| Significance & Impact | 58 | Competent | Practical relevance if results hold |
| Experimental Validation | 52 | Developing | Breadth with missing controls |
| Reproducibility | 50 | Developing | No code or splits |
| Ethical Compliance | 48 | Developing | No impact statement; medical framing; undocumented new set |

## Questions for Authors
1. What is detection AP on the unrestored degraded images and on the clean references? (If restoration by DAIR clearly beats the degraded input, I would raise Significance; if several restorers fall below it, the benchmark says little.)
2. What are peak memory and latency at 1080p on a mobile-class device?
3. What happens when the latent code is mismatched to the true degradation?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No.** (Recommend adding documentation for the new annotated data and a caution about medical use; no serious violation.)

## Overall Score
**3**: Practically relevant and cheaper than recent baselines, but the downstream and real-world evidence is not yet decisive.

## Confidence
**3**: Fairly confident; outside my usual sub-area for the model-design details.

---

# Peer Review Report (Reviewer 4)

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Reviewer: Dr. Hana Ishikura-Moore, Generalist Reviewer (machine-learning group, research university; fictional persona)
## Expertise: representation learning; generative models; not specialized in restoration
## Date: 2026-11-10

## Summary
The paper tackles all-in-one restoration without user prompts. It pre-trains an encoder in a VAE-like fashion with a contrastive term, freezes it, and uses its multi-scale features and bottleneck code to guide a restoration network through feature modulation, a learned degradation map and a light gated decoder. Across three groups of experiments (six common tasks, compound degradations, held-out compound degradations) it reports higher PSNR/SSIM than the compared methods at lower cost, with additional detection and out-of-domain demonstrations.

## Strengths
### S1: Plain, well-motivated goal
Prompt-free blind restoration with a single model is a recognizable problem; Fig. 1 and §1 frame it clearly.

### S2: The structure of the method section is easy to follow
Section 3 maps each module to a question (which/where/what) and Fig. 2 mirrors it; equations are mostly complete (Eq. 2–10).

### S3: Many tables with consistent metric pairs
PSNR/SSIM with params/FLOPs in Table 1, and ablation in Table 6, give readers the main numbers at a glance.

### S4: Appendix includes algorithm, loss details and limitations
App. A.2–A.4 gives the pre-training objective, hyperparameters (β=0.3, λ_con=0.01, τ=0.1) and Algorithm 1.

## Weaknesses

### W1: The central claim is stated more strongly than the evidence and is partly contradicted by the paper's own ablation
The contribution list attributes the gains to latent priors that need "no explicit task cues" (§1, Abstract), yet pre-training uses degradation labels (Eq. 17; Alg. 1 takes labels y_i), and Table 6 shows LP alone adds +0.27 dB, with most of the gain appearing only when 3WD is present. A reader cannot tell what produces the 2.78 dB average gain in Table 1. For ICLR the question "what do we learn?" is unanswered.
- **Suggested Fix**: State the label supervision in the abstract; add a clean "gain attribution" figure/table; drop "without explicit cues" unless shown for a label-free variant.

### W2: Experimental protocol is under-specified for a venue that expects reproducibility
Single vs multi-task training, baseline budgets, splits and selection are not stated (see R1 W1/W5). Numerous text–table slips (R1 Error Log) erode trust: the abstract's 1.68 dB average is not a table entry (it equals the mean of three different average gains), the Table 8 text claims "+2.2 dB" where the table shows ≤+0.28 dB, and App. B.3 says DAIR is fastest at all sizes where Table 9 says otherwise.
- **Suggested Fix**: Define each headline number and where it comes from; add a reproducibility table; release code.

### W3: Overstated and loosely defined terminology
"Reasoning paradigm", "explicit spatial reasoning", "linear complexity attention" and "unseen degradations" are used for a gated U-Net, a sigmoid-gated product, and two held-out combinations of known degradations. The "attention" in Eq. 5–6 and Eq. 10 is a sigmoid gate with no token mixing, so a comparison against full SA/CA (Table 5) is not comparing like with like.
- **Suggested Fix**: Use descriptive terms; compare 3WD with gated skip connections, channel (transposed) attention and windowed attention, which are the realistic alternatives.

### W4: Venue fit
A well-executed AIR system paper can fit ICLR, but ICLR reviewers typically want either a new principle with evidence or exceptionally careful empirical work. Here the principle is not isolated and the empirical work has loose ends.
- **Suggested Fix**: Add a controlled study showing that a label-free prior (and not a stronger decoder) is responsible for generalization to new degradation types.

**Minor:** typographical issues ("We propose reframe AIR", "Restformer", "Refrenece"), the undefined acronym TS in captions, Table 1 improvement row for Params/GFLOPs measured against different baselines per column.

### Venue criteria checklist (ICLR)
| Item | Grade | Location |
|------|-------|----------|
| Soundness: claims supported | Partly | Tables 5–6 vs §1 claims |
| Soundness: fair baselines | Not met / unverifiable | §4.1 |
| Presentation: clear structure | Met | §3, Fig. 2 |
| Contribution: new insight beyond SOTA table | Partly | Table 6 |
| Reproducibility statement/code | Not met | §4.1, App. A.4 |

## Missing References
Optional; deferred to R2.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence does not isolate the claimed contribution |
| Clarity | 3 | Method readable; protocol missing |
| Significance | 2 | Moderate |
| Originality | 2 | Combination of known parts |

## Dimension Scores (0–100)

**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear problem and readable method with consistent positive tables, but the main claim is neither isolated nor verifiably fair.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Reasonable design, inconsistent evidence |
| Clarity & Presentation | 52 | Developing | Clear method, unclear protocol, text–table slips |
| Novelty & Originality | 48 | Developing | Mostly known blocks |
| Significance & Impact | 52 | Developing | Moderate |
| Experimental Validation | 50 | Developing | Broad but uncontrolled |
| Reproducibility | 45 | Developing | No code, no splits, no seeds |
| Ethical Compliance | 60 | Competent | Limitations section present |

## Questions for Authors
1. Which single experiment would you point to as isolating the benefit of the label-free prior from that of 3WD?
2. Is the abstract's "1.68 dB" the mean of the three average gains in Tables 1, 3 and 4?
3. Will code and the detection annotations be released?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No.**

## Overall Score
**3**: The idea is reasonable and the results are positive on paper, but the paper does not yet show why it works nor that the comparisons are fair.

## Confidence
**4**: Confident about venue norms; not deep in restoration details.

---

# Devil's Advocate Report

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Reviewer: Prof. Dmitri Aksoy, Devil's Advocate (evaluation-methodology group, research university; fictional persona)

---

## Steelman
A prompt-free, single-model restorer with ~18M parameters that beats six recent AIR methods across six single tasks, five compound degradations and two held-out compound combinations, at about a third of ADAIR's FLOPs, and that also benefits a downstream detector, would be a useful practical advance. The frozen, label-supervised latent encoder is a clean way to inject degradation awareness without text prompts at test time.

---

## Core Argument Chain
1. Existing AIR methods need prompts or hand-crafted priors, which limits generalization (§1).
2. A VAE-style latent encoder yields degradation-aware features ("which"), the DM yields "where", fusion yields "what" (§3).
3. A gated linear decoder (3WD) exploits these cues efficiently (§3.2).
4. DAIR beats SOTA AIR methods on common, compound, unseen degradations and downstream detection, at lower cost (Tables 1–4, 9, 10).
5. The ablation shows each component, especially latent priors, is critical (Table 6).
∴ Learned latent priors are the cause of DAIR's superior generalization and efficiency.

---

## Strongest Counter-Argument
The paper reports large gains but never establishes what causes them. Three observations from the paper's own tables suggest the gains come from the experimental protocol and the decoder gate rather than from the "latent priors": (1) In Table 6, Base+LP improves the four-task average by only +0.27 dB (20.22→20.49), with desnowing and deraining slightly *worse*; the 4.23 dB "latent-prior" effect appears only in the presence of 3WD and LF, a super-additive interaction (LP+LF ≈ +0.9 dB without 3WD, ≈ +4.2 dB with it) that normally signals unmatched training budgets across rows. (2) In Table 5 the DAIR+SA (19.18) and DAIR+CA (17.71) variants fall below even the Table 6 Base Model (20.22), i.e., replacing the 3WD gate with standard attention is worse than having no module at all; this implies the SA/CA variants were mis-trained or infeasible at full resolution (65,536 tokens at 256×256), so the headline "+7.72 dB" tells us nothing about 3WD. (3) The retrained baselines are erratic in a way published AIR methods are not: Restormer denoises σ=50 on DIV2K at 16.62 dB (Table 8), DFPIR is flat at ≈21.5 dB across σ=15/25/50 on BSD100/Urban100 (Table 8) and is only 0.12 dB above Uformer on the Table 1 average (24.46 vs 24.34), and Table 8 contains duplicated cells that suggest assembly errors. When baselines are trained by the authors, for an unspecified budget on one RTX 3060 at batch 4, while the proposed model receives extra supervised pre-training (200–300K steps, labels, Eq. 17) and per-task step counts "depending on task complexity" (§4.1), an advantage of 2–4 dB on tasks such as desnowing (+4.42 dB, Table 1) and dehazing (+3.67 dB) is more plausibly a protocol artifact than a property of latent priors. Finally, the "without explicit task cues" premise is itself only true at inference: pre-training uses degradation-type labels (Alg. 1), the held-out "unseen" classes are combinations of labelled primitives (§4.1), and the paper's own decoder adds a hand-crafted FFT branch (Eq. 4), the thing the abstract criticizes. Authors must show, under one identical budget, that a label-free prior beats an AirNet-style encoder and a no-prior decoder.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main claim is weakened and its attribution is unproven, but every problem I found can be answered by narrowing claims, matching training budgets and re-running controls; the paper's own tables do not contradict the headline comparison, no test-set selection is stated (protocol sweep found no selection or tuning statement), and I see no concrete evidence of fabrication (duplicated table cells in Table 8 are more plausibly assembly errors and are reported as MAJOR).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §4.1, Tables 1, 3, 4, 8 | Baselines trained by the authors with unspecified, apparently unmatched budgets; numbers are anomalous (Restormer 16.62 dB at σ=50, DFPIR flat ≈21.5 dB, Table 8). "Fairness" asserted in one sentence. | Matched-budget retraining, official-checkpoint sanity check, protocol table |
| DA-M2 | Logic | Table 6, §4.7 | Latent prior alone +0.27 dB; super-additive interaction with 3WD; attribution to LP unproven (partly contradicted). | Equal-budget ablation, plus AirNet-encoder and plain-autoencoder controls |
| DA-M3 | Evidence | Table 5, §4.6 | SA/CA variants below the no-module base (19.18/17.71 vs 20.22); speed/memory claims ("85-257×", "76-89%") have no data; implementation undefined. | Give implementation and numbers; use gated/channel/windowed-attention baselines |
| DA-M4 | Scope | §1, Abstract, Alg. 1, Eq. 17 | "Without explicit task cues" (abstract) and the claimed elimination of manual degradation hints hold only at inference; training uses degradation labels, and the "manual prompt" characterization of PromptIR/DFPIR (MP ✓) is questionable [verify; could not be checked against abstracts]. | Narrow the wording; add label-free variant |
| DA-M5 | Evidence | Table 8, App. B.1.2 | Text claims "+2.2 dB" and "consistently higher" where the table shows ≤+0.28 dB and three negative cells; duplicated cells (BSD100). | Correct and regenerate the table |
| DA-M6 | Scope | Abstract, Table 9, App. B.3 | "three times more efficient" and "fastest ... across various image sizes" contradicted at 512² (Uformer faster). | Narrow to measured claims; full-pipeline cost |
| DA-M7 | Scope | §4.4, App. C, Tables 11–15 | "Unseen"/"strong cross-domain generalization": two compound combinations of seen primitives; out-of-domain results lack baselines; LPIPS undefined without reference; negligible gains (Tables 12–13). | Baselines on OOD, true unseen types |
| DA-M8 | Evidence | App. B.4, Table 10 | No unrestored-input or clean-reference detection rows; undocumented annotation; "first quantitative assessment" claim. | Add rows, document data |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Logic | §3.1.3 | µ is called a "global descriptor" but is a 320-channel spatial map at H/8×W/8 (App. A.2), and Eq. 8 outputs γ,β of spatial size. |
| DA-m2 | Scope | Table 6 | "Improvement" row is relative to the Base Model (e.g., 29.11−23.42 = 5.69), whereas the caption says "over the best performing method". |
| DA-m3 | Evidence | Abstract | The "1.68 dB" headline is the mean of three different average gains (2.78, 0.78, 1.47), against different best baselines, and is not a table entry. |
| DA-m4 | Evidence | Eq. 2–3, §3.1.1 | If DAEB uses softmax(QK^T/√d) at full resolution it is quadratic, in tension with 45.65 GFLOPs at 256²; the attention form is not specified (a question). |
| DA-m5 | Presentation | Table 10 text | "average improvement of 3.2 percentage points over SOTA methods" — gaps are against the best listed method only. |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Table 1 DAIR average PSNR | 28.15 | (16.87+34.08+29.12+31.50+26.82+30.51)/6 = 28.15 | Yes |
| Table 1 avg gain over best (PromptIR 25.37) | +2.78 | 28.15−25.37 = 2.78 | Yes |
| §4.2.1 desnowing gain | +5.64 PSNR / +0.0758 SSIM | vs best baseline: 31.50−27.08 = 4.42 / 0.9570−0.9169 = 0.0401 | No (text uses ADAIR as reference) |
| Table 3 DAIR average PSNR | 22.61 | (25.25+23.15+22.03+20.81+21.79)/5 = 22.606 | Yes |
| Abstract: average PSNR gain | 1.68 dB | (2.78+0.78+1.47)/3 = 1.677 (mean of three averages); coincides with Table 3 Haze+Rain +1.68 | Derivable, not a table entry |
| §4.4 unseen avg SSIM gain | +0.0412 | Table 4 row +0.0523 (vs PromptIR); 0.0412 only vs ADAIR | No (inconsistent reference) |
| App. B.1.2 denoising gain | "up to +2.2 dB" | max of Table 8 improvement row = +0.28 | No |
| Table 7 Lowlight-Outdoor PSNR gain | +0.87 | 14.77−14.74 (DFPIR) = +0.03 | No |
| Table 9: "fastest across sizes" | DAIR best | 512²: Uformer 203.83 ms vs DAIR 220.92 ms | No |
| Table 5 avg gain | +7.72 | 26.90−19.18 = 7.72 | Yes (but SA/CA below base model) |
| Table 6 DAIR vs w/o LP | −4.23 / −0.0876 | 26.90−22.67 = 4.23; 0.8565−0.7689 = 0.0876 | Yes |
| Table 10 gain | +3.2 AP | 34.9−31.7 = 3.2 | Yes |
| §1 detection "up to 7.40 mAP" | 7.40 | max gap in Table 10: 34.9−27.9 = 7.0 (AP[.5:.95]) | Not reproduced (Fig. 1 unavailable) |

## Ignored Alternative Explanations
- Training-budget and protocol advantage (200–300K extra supervised pre-training steps; task-dependent step counts; unspecified baseline budgets).
- A stronger decoder or extra skip-path capacity, rather than a prior, explains Table 6: 3WD alone is worth +5.13 dB.
- Label supervision during pre-training makes the encoder a degradation-type classifier; the benefit may be router-like, not a general "prior".
- "Unseen" test sets share all primitives with training.
- Under-trained baselines inflate every margin in Tables 1, 3, 4, 8.

## Missing Stakeholder Perspectives
Practitioners deploying on cameras and phones (no edge, memory or high-resolution numbers); clinicians when medical images are used (App. C.4–C.5); annotators and data users of the new detection set (no documentation).

## Observations (Non-Defects)
- Table averages are internally consistent with their rows (Tables 1, 3, 4, 5, 6).
- The authors disclose failure cases and hardware limits (App. D).
- Using the same frozen encoder across experiments is a good discipline.
- Reporting efficiency numbers next to quality is a strong choice.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 38 | Attribution unproven; ablation and SA/CA baselines implausible |
| Clarity & Presentation | 50 | Method readable; many text–table mismatches |
| Novelty & Originality | 42 | Known blocks; AirNet-like idea |
| Significance & Impact | 45 | Useful if real |
| Experimental Validation | 36 | Unverifiable baselines; no controls |
| Reproducibility | 40 | No code, splits, seeds, baseline budgets |
| Ethical Compliance | 55 | Limitations present; new data undocumented |

**Pool position:** better than about 32% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline gains cannot be attributed (Tables 5–6) and the baseline protocol is unverifiable.

## Overall: 2 | Confidence: 4

---

# Phase 1.5: Literature Check (strict, cutoff 2025-09-24) — **not completed: arXiv API unreachable**

Mode requested: `strict`, cutoff 2025-09-24. The fingerprint was written (method names DAIR, 3WD, DAEB, LPE; cutoff date) and the integrity scan found nothing. Queries: 3 attempts were refused by the script before counting (more than 4 concept words, not charged to the budget); 1 search query ("image restoration degradation embedding", claim C1) and 1 `verify` call (PromptIR title) both failed with **"arXiv API unreachable (HTTP Error 429)"** or timed out. No results were kept, so `scout`, `coverage`, `similarity` and `novelty` were not run, there is no baseline-scout table, no similarity or text-overlap result, and no verified link. Per `references/literature_search.md`, the check falls back to `literature check: off`: the addendum below relies on the Domain Reviewer's knowledge, every uncertain item is marked `[verify]`, and **no novelty verdict below is script-derived**. Coverage gaps left open: all claims (C1–C4), all benchmarks.

## Domain Reviewer addendum (R2, completes the report above)

**Per-claim novelty (knowledge-based, `[verify]`; not from `related_search.py novelty`):**

| Claim | Dimension | Novelty | Closest prior work in the paper's own related work (cited?) | Reasoning |
|-------|-----------|---------|------------------------------------------------------------|-----------|
| C1 prompt-free latent prior | method | incremental `[verify]` | AirNet (Li et al., CVPR 2022; cited) learns a degradation embedding from the input by contrastive learning; ADAIR and PromptIR are also blind at inference `[verify]` | The no-prompt-at-inference property is shared with several cited methods; what differs is the VAE-style multi-scale features and SupCon with labels |
| C2 which/where/what | method | medium | Attention-gate skip connections and FiLM conditioning (Perez et al., 2018; cited) | Each module is known; the combination is the novelty; not isolated by controls |
| C3 3WD linear decoder | method | incremental | Sigmoid gating and channel attention (Hu et al., 2018; cited); Restormer's transposed attention (cited) is already linear in HW | "Attention" here is a gate; novelty is in wiring, not mechanism |
| C4 empirical SOTA | result | not assessable | OneRestore (cited, CDD source, not compared) | Result claims depend on baseline protocol (R1-W1) |

**Novelty delta (own related work):** no uncited prior work with the same task and core mechanism was identified, so no "known results presented as new" candidate (DA criterion 7) is raised; AirNet is cited and differentiated only weakly (§2.1), which is a Novelty weakness (MAJOR at most), as in R2-W1/W2.

**Field snapshot (from knowledge `[verify]`; no reception of the reviewed paper mentioned):** AIR moved from per-task networks to single blind models (AirNet-style degradation embeddings), then to learned-prompt (PromptIR-style) and frequency-modulated (ADAIR-style) designs, with recent work adding mixture-of-experts routing, text/CLIP guidance and diffusion priors. Typical evaluations are 3-task (denoise/derain/dehaze) and 5-task protocols, and compound-degradation settings such as CDD. A +0.3–0.5 dB average gain at equal budget is incremental; a clear gain at equal training budget with an isolated, explained mechanism or a substantial efficiency gain at equal accuracy is significant. I use this only to calibrate Significance and Novelty.

**Citation check (E7), now finalized:** because the abstracts could not be retrieved, the claims that PromptIR "integrates text-based prompts" (§2.2) and that PromptIR/DFPIR "rely on explicit, manually provided prompts" (§1, Table 1 MP ✓) are **unverified**: they are Questions to the authors, not errors. The two attribution oddities (Guo et al. 2023 for the SupCon loss; DFPIR for multi-head self-attention in App. A.2) are verifiable from the manuscript's own citation contexts (§4.1, App. A.2) and stand as Medium-confidence points.

**Missing References** (none verifiable by script; marked `[verify]` unless I am confident the entry exists as described; none of these is a *required* comparison, since no entry is confirmed as prior peer-reviewed work by the tool)

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | OneRestore (Guo et al., ECCV 2024), already in the bibliography: **add as a baseline on CDD** (Tables 3–4) | Method designed for the dataset used for compound/unseen tests |
| Important | Luo et al., "Controlling Vision-Language Model for Universal Image Restoration" (DA-CLIP), ICLR 2024 `[verify]` | A widely cited learned degradation-aware universal restorer, relevant to the prompt/prior contrast |
| Important | Zamfir et al., "Complexity Experts are Task-Discriminative Learners for Any Image Restoration" (MoCE-IR), CVPR 2025 `[verify]` | Recent all-in-one method with input-driven routing, close to the "which features to route" framing |
| Important | Zhang et al., "Perceive-IR: Learning to Perceive Degradation Better for All-in-One Image Restoration" (2024/2025) `[verify]` | Learned degradation perception for AIR, close to C1/C2 |
| Helpful | Oktay et al., "Attention U-Net: Learning Where to Look for the Pancreas", MIDL 2018 | Gated skip connections that tell the decoder where to look: the conceptual ancestor of the Degradation Map + 3WD gate |
| Helpful | Line of work: contrastive degradation encoders for blind restoration (beyond AirNet) | Control for the "latent prior" claim |

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (baseline protocol) | kept; one clause corrected | An earlier draft misstated DFPIR vs Uformer (24.46 vs 24.34); corrected before the EIC saw it; consistent with Table 1 |
| R1 | W2 (ablation) | kept; numbers corrected | "≈1.5 dB without 3WD" corrected to 0.86 (Base 20.22 → Base+LP+LF 21.08) |
| R1 | W3 (efficiency) | rewritten | The claim that SA/CA "cannot have been dense attention" was speculation; now a question about the implementation |
| R1 | W4 (variance) | kept | Specific, actionable |
| R1 | W5 (splits, "unseen") | kept | Paper does not answer it (protocol sweep) |
| R1 | ERR-1…ERR-10 | kept | Each has location, quote and recomputation; ERR-4/6 are MINOR |
| R2 | W1 (framing) | rewritten | PromptIR/DFPIR characterization could not be verified; stated as a question with `[verify]` |
| R2 | W2, W3, W4 | kept | Specific; tied to Table 6, §4.4, Tables 3–4 |
| R2 | Citation note | rewritten | Garbled sentence replaced with two concrete, locatable attribution points |
| R3 | W1–W4 | kept | W4 rewritten to avoid implying clinical claims the paper does not make beyond "diagnostically relevant textures" (App. C.5) |
| R4 | W4 (venue fit) | rewritten | Generic; tied to Table 6 and the missing controls |
| R4 | Minor items | moved to Minor | Typos, undefined acronym |
| DA | M4 | rewritten | PromptIR/DFPIR characterization marked `[verify]` |
| DA | M1–M8, m1–m5 | kept | Located and actionable |

Scores unchanged. Overlap among reports is preserved for the EIC.

---

# Phase 2: Synthesizer Part A and EIC Meta-Review

## Synthesizer package (for the EIC)

**Official score (script, BEFORE run):** official ratings R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60; official composite 47.7; confidence-only weighted rating 2.59 → starting point 3; composite band 2 (⚠ cross-check disagrees with the rating-based starting point). No DA-CRITICAL issue raised. No integrity-scan findings. No spreads above 20 (largest: Technical Rigor 17, Experimental Validation 16).

**Merged issue list**

| # | Issue | Source IDs | Class | Hinge? |
|---|-------|-----------|-------|--------|
| 1 | Baseline training protocol unspecified/unmatched; anomalous baseline numbers | R1-W1, DA-M1, R4-W2 | CONSENSUS-3 | **Yes** |
| 2 | Latent prior's contribution not isolated; Table 6 interaction implausible | R1-W2, R2-W2, R4-W1, DA-M2 | CONSENSUS-4 | **Yes** |
| 3 | Efficiency/"linear complexity"/speedup claims overstated; Table 9 contradicts text | R1-W3, R3-W2, R4-W3, DA-M3, DA-M6 | CONSENSUS-4 | Yes |
| 4 | Splits/selection not stated; "unseen" narrower than claimed; OOD without baselines | R1-W5, R2-W3, R3-W2, R3-W3, DA-M7 | CONSENSUS-4 | Yes |
| 5 | Text–table contradictions and duplicated Table 8 cells | R1 ERR-1…10, R4-W2, DA-M5 | CONSENSUS-3 | Yes |
| 6 | Framing/novelty relative to AirNet-style blind methods; label supervision | R2-W1, R2-W2, DA-M4, R4-W1 | CONSENSUS-3 (partly) | No |
| 7 | Detection benchmark lacks no-restoration/clean rows; undocumented set | R3-W1, DA-M8 | CONSENSUS-2 | No |
| 8 | Single runs, small margins | R1-W4 | SOLO | No |
| 9 | Missing baseline OneRestore / recent AIR methods | R2-W4 | SOLO | No |
| 10 | Ethics/data documentation, medical framing | R3-W4 | SOLO | No |

SPLIT: none explicit (R3 rates Significance higher than R1/DA, but nobody disputes a specific fact).

## Editorial Decision

# Editorial Decision

## Paper: Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding
## Submission ID: iclr26-4fhbxglvYs
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Ingrid Valdemar; R1 Methodology Dr. Kaveh Marandi, R2 Domain Prof. Naledi Dube, R3 Perspective Dr. Mateo Ferreira-Lund, R4 Generalist Dr. Hana Ishikura-Moore, DA Prof. Dmitri Aksoy

*This is a simulation of how a careful panel would likely see this draft, not a prediction of a real outcome.*

---

## Decision: Borderline Reject (3)  (ICLR rating label: **4 on {0,2,4,6,8,10}**, i.e., 5 on the earlier {1,3,5,6,8,10} scale; scale status: secondary, not official wording)

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean **2.60** · official composite **47.7**
**EIC assessment** (internal): weighted rating **2.56** → starting point **3** · weighted composite **47.3** → band 2 (cross-check) · **DA ceiling**: none · **Final (EIC)**: **3**
**Journal recommendation:** not applicable (conference target).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A prompt-free single model with 18M parameters and 45.65 GFLOPs reports higher PSNR/SSIM than six recent AIR methods on six single tasks, five compound degradations and two held-out compound combinations (Tables 1, 3, 4); table averages and improvement rows are internally consistent (recomputed). The evaluation is broad, includes a detection test, shows failure cases (App. D), and the architecture is sensible.
- **Against acceptance:** The comparison is against baselines retrained by the authors under an unstated, apparently unmatched protocol, with erratic baseline numbers (Table 8) and several text–table contradictions; the paper's own ablation shows the latent prior alone adds +0.27 dB (Table 6) while a gating decoder variant accounts for most of the gain, and the SA/CA comparison (Table 5) is below the no-module base. Novelty is a combination of known blocks, and the "unseen", "reasoning" and "efficiency" claims exceed the evidence. No code, splits or seeds.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Baselines trained under unspecified, unmatched budgets | R1-W1, DA-M1, R4-W2 | §4.1 | Partly correct | Quotes verified ("trained using their official implementations and suggested hyperparameters"; DAIR "100,000 to 500,000 steps, depending on task complexity"); that baselines are *unmatched/under-trained* is an inference from anomalies, not stated |
| Baseline anomalies (Restormer 16.62 dB at σ=50; DFPIR flat ≈21.5 dB) | R1-W1, DA | Table 8 | Verified | Values read directly; cause not established |
| Latent prior alone +0.27 dB; super-additive with 3WD | R1-W2, DA-M2, R2-W2 | Table 6 | Verified | 20.22→20.49; 21.77→26.90 (+5.13) with 3WD; w/o-LP row 22.67 vs 26.90 |
| SA/CA variants below the base model | DA-M3, R1-W3 | Tables 5, 6 | Verified | 19.18 and 17.71 vs 20.22 (same four tasks); "mis-trained" is inference |
| "Fastest ... across various image sizes" contradicted | R1 ERR-3, DA-M6 | Table 9, App. B.3 | Verified | 512²: Uformer 203.83 ms vs DAIR 220.92 ms |
| "+2.2 dB" and "consistently higher" vs table | R1 ERR-1, DA-M5 | App. B.1.2, Table 8 | Verified | Max +0.28; three negative cells |
| Duplicated cells in Table 8 BSD100 | R1 ERR-2 | Table 8 | Verified | Four cross-referenced duplicate/near-duplicate pairs; consistent with assembly error, not evidence of manipulation |
| Abstract 1.68 dB not a table entry | R4, DA-m3 | Abstract; Tables 1, 3, 4 | Verified (derived) | = mean of +2.78, +0.78, +1.47 |
| Table 7 Lowlight-Outdoor +0.87 should be +0.03 | R1 ERR-5 | Table 7 | Verified | DFPIR 14.74 |
| Text SSIM gains use different reference (+5.64; +0.0412) | R1 ERR-4, ERR-6 | §4.2.1, §4.4 | Verified | Minor |
| "Without explicit task cues" contradicted by label use | DA, R4-W1 | Abstract; Eq. 17; Alg. 1 | Overstated | Labels are used in pre-training; at inference no cues are needed. Narrow wording; not a flaw in the claim as an inference-time property |
| Frequency heuristics criticized yet FFT branch used | R2-W1, DA | Abstract; Eq. 4 | Partly correct | Real tension but FFT features are learned-projected inside the module |
| PromptIR/DFPIR "manual prompt" mischaracterized | R2-W1, DA-M4 | §1, §2.2, Table 1 | Not verifiable | Literature check unavailable; treat as a question |
| "Unseen" = combinations of seen primitives | R1-W5, R2-W3, DA-M7 | §4.1, §4.4 | Verified | Held-out haze+snow, low-light+rain; the single degradations are in pre-training |
| Detection table lacks unrestored and clean rows | R3-W1, DA-M8 | Table 10 | Verified | |
| Mis-attributed citations (SupCon source; MHSA via DFPIR) | R2 | §4.1, App. A.2 | Partly correct | Contexts verified; whether Guo et al. 2023 contains the loss unverified |
| "Up to 7.40 mAP" not reproduced | R1 | §1; Table 10 | Not verifiable | Max gap in Table 10 is 7.0 AP; Fig. 1 unavailable |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | **1.25** | Every Error Log entry checked and held at its location (ERR-1…ERR-10); two draft slips were fixed before review; one inference (unmatched baselines) is plausible but not proven |
| R2 (Domain) | 3 | 4 | 1.0 | Sound novelty analysis; the headline prior-work mischaracterization point could not be verified (no literature check) |
| R3 (Perspective) | 3 | 3 | 1.0 | Verified detection-baseline and LPIPS points; perspective role, calibrated |
| R4 (Generalist) | 3 | 4 | 1.0 | Balanced and verified; mostly overlaps R1/DA |
| DA | 2 | 4 | 1.0 | Arithmetic verified; the "protocol artifact" attribution is an inference, so no upweighting |

### DA-CRITICAL Rulings

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised ("No CRITICAL issues found") | n/a | EIC concurs: no test-set selection is stated (protocol sweep), no evidence the main claim is contradicted, and the Table 8 irregularities look like assembly errors | n/a |

### Final Decision and Justification
The EIC-weighted rating is 2.56, which rounds to **3** (starting point); the 0–100 composite (47.3) falls in band 2, and the script flags the disagreement. The rating sits within 0.1 of the 2.5 boundary and the composite is 2.7 points below the band edge of 50, so I treat the two signals as a borderline pair rather than a conflict. I could name verified issues the three "3" ratings do not mention (Table 8 contradictions and duplicated cells, Table 9 vs text, Table 5 below the base model), but R1 and the DA, who gave 2, already rest on exactly these, and none of the "3" ratings rests on a point I found incorrect. I therefore keep the starting point. Why not 4: the central attribution to latent priors is unproven and partly contradicted by Table 6, and the comparison protocol is unverifiable. Why not 2: Tables 1, 3 and 4 are internally consistent on recomputation, the gains appear across many settings and a lower compute class, no leakage or fabrication evidence exists, and most problems are fixable by documentation and controlled re-runs (several are rebuttal-feasible). **EIC pool position: better than about 40% of ICLR submissions (a typical rejected submission); deciding evidence: unverifiable baseline fairness plus an ablation that does not support the paper's main explanation.** No DA ceiling applies; the decision does not exceed it.

---

## Score Summary

### Official Scores and EIC Assessment (script output, with EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 40 | 48 | 55 | 50 | 38 | 46.2 | 45.6 | 17 |
| Clarity & Presentation | 50 | 52 | 58 | 52 | 50 | 52.4 | 52.1 | 8 |
| Novelty & Originality | 45 | 42 | 52 | 48 | 42 | 45.8 | 45.5 | 10 |
| Significance & Impact | 48 | 50 | 58 | 52 | 45 | 50.6 | 50.2 | 13 |
| Experimental Validation | 38 | 45 | 52 | 50 | 36 | 44.2 | 43.6 | 16 |
| Reproducibility | 40 | 45 | 50 | 45 | 40 | 44.0 | 43.6 | 10 |
| Ethical Compliance | 55 | 58 | 48 | 60 | 55 | 55.2 | 55.4 | 12 |
| **Composite** | 44.0 | 47.9 | 53.5 | 50.7 | 42.4 | **47.7 (before)** | **47.3 (after)** | |
| Pool position (%) | 33 | 42 | 52 | 46 | 32 | | | |

No dimension has a spread above 20 points, so there are no ⚠ disagreements to arbitrate. Reviewer weights (confidence × EIC weight) give R1 25%, R2 20%, R3 16%, R4 20%, DA 20%.

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating (final = EIC decision 3) | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); both scales are shown by the script and neither is official wording |
| Venue-weighted composite | 47.1 (band 3, no shift) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding" to ICLR.

Prompt-free, single-model restoration of mixed weather, low-light and noise degradations is a practically important problem, and your paper reports results across six single, five compound and two held-out compound settings.

**Overall Assessment:** The panel found the goal clear, the architecture sensible, and the table averages internally consistent. The panel was not convinced that the reported gains can be attributed to the proposed latent priors or that the comparisons are fair, and it found several statements in the text that the paper's own tables contradict.

**Key Strengths Identified by Reviewers:**
1. A broad evaluation (single, compound, held-out compound, detection, out-of-domain examples) with efficiency numbers reported next to quality (R1, R3, R4).
2. A clear structure for the method and a sensible combination of luminance/chrominance branches, a degradation map and a light decoder (R2, R4).
3. Honest failure cases and a frozen-encoder protocol (R1, R3).

**Key Concerns Requiring Attention:**
1. The baseline training protocol is unspecified and apparently unmatched, and several baseline numbers are anomalous (R1, R4, DA; CONSENSUS-3).
2. The ablation does not isolate the latent prior (Base+LP = +0.27 dB) and shows a super-additive interaction with the decoder; the SA/CA comparison scores below the no-module base (R1, R2, R4, DA; CONSENSUS-4).
3. Efficiency, "linear complexity", "unseen" and "generalization" claims exceed the evidence; Table 9 contradicts the text at 512×512; Table 8 text overstates gains and the table has duplicated cells (R1, R3, R4, DA; CONSENSUS-4).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection is that the gains are more plausibly explained by the training protocol and the decoder gate than by latent priors; this must be answered with equal-budget controls.

**Decision: Borderline Reject (3).** The topic and the results are promising, but the evidence does not yet show why the method works or that the comparison is fair. A revised version that documents the protocol, retrains all methods under one budget, reruns the ablations at equal budget with an AirNet-style-encoder control, and corrects the contradictions listed below would be judged on a stronger footing. This is a simulated assessment of how a careful panel would likely see this draft.

Please refer to the Revision Roadmap below.

Sincerely,
Dr. Ingrid Valdemar
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Latent prior not isolated; ablation implausible | R1, R2, R4, DA | CONSENSUS-4 |
| Efficiency/complexity claims overstated | R1, R3, R4, DA | CONSENSUS-4 |
| Splits/selection absent, "unseen" narrow, OOD weak | R1, R2, R3, DA | CONSENSUS-4 |
| Baseline protocol unmatched/anomalous | R1, R4, DA | CONSENSUS-3 |
| Text–table contradictions | R1, R4, DA | CONSENSUS-3 |
| Framing/novelty vs AirNet-style blind methods | R2, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Significance of the practical contribution | R3 (58) | R1 (48), DA (45) | No factual dispute; R3's score assumes the gains hold, which the EIC cannot confirm; weights unchanged |
| "No explicit task cues" is a flaw | DA, R4 | (paper: inference-time property) | Overstated as a flaw; keep as a wording fix |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. The largest spread (Technical Rigor, 17) is between R3 (55) and the DA (38); the EIC adopts the lower region because R3 did not examine Tables 5–8 in detail (verified issues there).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| (no DA-C) | — | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Baselines unmatched, anomalous | Yes (R1, R4) | n/a | n/a |
| DA-M2 | MAJOR | Latent-prior attribution unproven | Yes (R1, R2, R4) | n/a | n/a |
| DA-M3 | MAJOR | SA/CA below base; speed numbers absent | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | "Without explicit cues"; MP characterization | Yes (R2, R4) | n/a | n/a |
| DA-M5 | MAJOR | Table 8 text/duplicates | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR | Efficiency claim vs Table 9 | Yes (R1, R3) | n/a | n/a |
| DA-M7 | MAJOR | "Unseen" and OOD claims | Yes (R1, R2, R3) | n/a | n/a |
| DA-M8 | MAJOR | Detection table lacks baselines | Yes (R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*Issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Baseline protocol undocumented/unmatched; anomalous baselines | R1-W1, DA-M1, R4-W2 | §4.1; Tables 1, 3, 4, 8 | Protocol table; retrain all methods under one budget and data mixture (single model vs per-task stated); sanity-check against official checkpoints | High; ≈100–200 GPU-h (RTX-3060 class) | Partly (documentation yes; full retraining maybe) |
| R2 | Latent prior not isolated; implausible interactions | R1-W2, R2-W2, R4-W1, DA-M2 | Table 6; §4.7 | Equal-budget re-run of every row; add AirNet-style contrastive encoder, plain autoencoder, label-shuffled controls; specify what replaces x_ℓ without LP | Medium; ≈60–100 GPU-h | Partly |
| R3 | Text–table contradictions and duplicated Table 8 cells | R1 ERR-1…ERR-10, DA-M5, DA-M6, R4-W2 | App. B.1.2, Table 8, Table 9/App. B.3, §4.2.1, §4.4, Table 7, Abstract | Regenerate Table 8 from raw results; correct each statement; define the "1.68 dB" headline; narrow efficiency wording | Low; ≈1–2 days | Yes |
| R4 | 3WD vs SA/CA comparison and efficiency evidence | R1-W3, DA-M3 | Table 5; §3.2; §4.6 | State SA/CA implementations; add speed/memory numbers; compare with gated/channel/windowed-attention baselines; report full-pipeline params/FLOPs/latency including the frozen encoder | Medium; ≈20–40 GPU-h | Yes |

### Priority 2 — Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Splits/selection not stated; "unseen" narrow; OOD evidence without baselines; LPIPS undefined | R1-W5, R2-W3, R3-W2/W3, DA-M7 | Split table and selection rule; unseen primitive degradations; baselines on OOD data; clarify LPIPS reference | Medium | Partly |
| S2 | Single runs, small margins (+0.04…+0.5 dB cells) | R1-W4 | 3 seeds and paired bootstrap on Tables 3 and 8 | Medium; ≈3× those rows | Partly |
| S3 | Framing/novelty relative to AirNet-style methods; MP column; label supervision wording | R2-W1, DA-M4, R4-W1 | Reposition, verify and correct the MP column, state label supervision in the abstract | Low | Yes |
| S4 | Missing baselines and references | R2-W4; Missing References | Add OneRestore on CDD and 2–3 recent blind AIR methods; cite the listed works (verify first) | Medium | Partly |
| S5 | Detection benchmark rows and documentation | R3-W1, DA-M8 | Add degraded-input and clean-reference rows; datasheet; release annotations; support or drop "first" | Low–Medium | Yes |
| S6 | No code, seeds, compute details | R1, R4 | Release code and checkpoints; report training time | Low | Yes |

### Priority 3 — Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Ethics/data documentation and medical framing | R3-W4 | Short impact note; avoid clinical suggestions |
| N2 | Terminology ("reasoning", "attention" for a gate, "global descriptor" for a spatial map) | R4-W3, DA-m1 | Use descriptive terms |
| N3 | DAEB attention form unspecified | DA-m4 | State whether spatial or channel attention |
| N4 | Table 6 improvement-row reference; different baselines per column in Table 1 | DA-m2, R4 | Label the reference baseline |
| N5 | Typos, undefined acronyms, wrong cross-reference (Table. 8 → Table 11) | R1, R4 | Proofread |
| N6 | Real-world, edge-device, ≥1080p latency and memory | R3 | Add tiling-based numbers |

---

## Estimated Revision Effort
- Priority 1: 4 items, ≈2–4 weeks including retraining (≈200–350 GPU-h on an RTX-3060-class card)
- Priority 2: 6 items, ≈1–2 weeks
- Priority 3: 6 items, ≈2–3 days
- **Total estimated revision time**: ≈4–6 weeks

*No Gap Scout analysis was requested; none was run.*
