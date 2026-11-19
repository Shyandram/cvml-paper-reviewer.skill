# Full Review — "SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing"

*Simulated panel review (mode: full; target venue ICLR; literature check: strict, cutoff 2025-09-24). The five reviewer passes were run one after another in one shared model context; they are role-based perspectives, not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only. This is a simulation of how a careful panel would likely see this draft, not a prediction of any outcome.*
*Date: 2026-11-05*

---

# PHASE 0 — Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing |
| Primary Discipline | Machine learning → self-supervised representation learning for multimodal sensor time series (IoT) |
| Secondary Discipline(s) | Cyber-physical / IoT sensing; seismology (earthquake localization); wearable activity recognition; information theory (analysis) |
| Paper Type | Empirical (method + benchmark evaluation); composite weights: empirical |
| Core Technique(s) | Masked autoencoding with a ViT backbone; continuous spatial positional embedding; learnable per-node "structural" embedding; a second (spatial-position) decoder; frozen-encoder fine-tuning of light heads |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence) |
| Paper Maturity | Submission-ready draft ("Preprint. Under review."), main text 9 pages, 18 pages of appendix and tables |
| Ethics-Relevant Content | Outdoor audio (16 kHz microphones) and vehicle GPS from smartphones (M3N-VC); border-defense "intruder" detection used as a motivating example (§1); no ethics or broader-impact statement |
| Integrity signals | `integrity_scan.py`: 0 findings. No text addressed to reviewers or AI systems was found. Reviewers read the original text (no redaction needed). |

### Claimed Contributions (as stated by the authors, §1)
1. **C1** — SPAR, "a novel IoT pretraining framework that explicitly models spatial layouts and node-specific characteristics", built on spatial positional embeddings, structural positional embeddings and dual reconstruction objectives (§1, §3.1–3.2).
2. **C2** — "theoretical analyses from information theory and occlusion-invariant representation learning" offering insight into the design (Prop. 3.1, Prop. 3.2, §3.3, App. B).
3. **C3** — "extensive experiments on three real-world datasets" demonstrating "superior generalizability and robustness" across modalities, placements, tasks and spatial scales (Abstract, §4, App. D).

### Paper memory (factual record shared with all reviewers)
- **Setup (located):** same ViT backbone and identical heads for all methods, same number of epochs (number not stated), three seeds (§4, first paragraph). Frozen encoder at fine-tuning (Fig. 1 caption; §3.2). Default mask ratio 0.75 (App. D.1).
- **Splits:** M3N-VC "official temporal split for training and validation (approximately 3:1)" and pretraining "on all six scenes" (App. C.2); downstream tasks use scene H24 (single vehicle) and I22 (multi-vehicle). Ridgecrest: 22,360 train / 9,092 "validation" events, temporal (App. C.3). RealWorld-HAR: first 10 participants train, last 5 "validation" (App. C.4). **No separate test split on any dataset; the reported numbers are on the "validation" splits. How hyperparameters/checkpoints were chosen: not stated after search.**
- **Not stated after search:** model size/depth/width, patch size, optimizer, learning rate, batch size, epochs, GPU type/hours, parameter counts/FLOPs, code link, how baselines ingest multi-node multimodal input, loss weighting between the two terms of Eq. 5.
- **Headline numbers and sources:** M3N-VC single-vehicle localization MSE 12.98 / dist. err 4.20 m (Table 1); multi-vehicle mAP@4m 41.57 (Table 2); Ridgecrest MSE 23.46 / 5.37 km, HAR 89.63 acc / 90.45 F1 (Table 3).
- **Appendix adds:** proofs (App. B), dataset settings (App. C), single-vehicle classification (Table 5), message-drop (Table 6), unseen placement (Table 7), ablations and masking variants (Table 8), qualitative figures (Figs. 3–7), limitations (App. E).
- **Unverifiable:** Figures 1–7 (not available); equations in the extracted text are partly garbled (Eq. 3/4 argument grouping read from context).

### Literature check (Phase 1.5; mode strict, cutoff 2025-09-24)
8 queries (claim 5: C1×3, C2×1, C3×1; baseline 2; expansion 1) against arXiv, 66 unique kept results; no query touched the paper's title, method name or authors; self-exclusion filter active. `similarity`: no high conceptual overlap (top cosine 0.15 against a 0.30 flag) and **no text overlap** (0 shared 8-grams). `scout` on RealWorld-HAR returned no rows; `benchmarks` listed none. **No close prior work was found in this search (arXiv only); that is a limit of the search, not evidence of novelty.** Gaps left open: no query for the multi-node vehicle-localization benchmark beyond one baseline query (the dataset itself is recent); no per-claim `novelty` profile file was written because no kept result reached entailment level 3 for any claim.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Imani Rautavaara, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / self-supervised learning, multimodal sensing
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Judges against what the venue actually accepts; weights verified evidence over rhetoric

### Reviewer 1 (Methodology): Dr. Tomasz Reinholt, industrial research lab (Central Europe)
- **Seniority / Expertise**: Senior industry scientist / masked-autoencoder pretraining protocols, frozen-encoder evaluation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every headline delta; insists on matched protocols

### Reviewer 2 (Domain): Prof. Aiko Fernsby, sensing and ubiquitous-computing group, public university (East Asia)
- **Seniority / Expertise**: Senior faculty / sensor-based activity recognition, time-series foundation models, multimodal contrastive learning
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks that related work is characterized the way the cited papers describe themselves

### Reviewer 3 (Perspective): Dr. Lucía Montenegro-Bell, geophysics and signal-processing institute (South America)
- **Seniority / Expertise**: Mid-career / array signal processing, seismic source location, sensor-network deployment
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what physics and classical methods would add

### Reviewer 4 (Generalist): Dr. Kwabena Osei-Lindgren, vision and learning lab, public university (West Africa / Europe)
- **Seniority / Expertise**: Mid-career / representation learning in general (not sensing)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs contribution against ordinary weaknesses

### Devil's Advocate: Dr. Priyanka Haldenwang, evaluation-methodology group, research institute (South Asia / Europe)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, ablation design, causal attribution of gains
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; attacks only after steel-manning

*Personas are fictional. Proceeding with the stated assumptions.*

---

# PHASE 1 — Independent Reviews

---

# Peer Review Report — Reviewer 1

## Paper: SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing
## Reviewer: Dr. Tomasz Reinholt, Methodology Reviewer (industrial research lab; fictional persona)
## Expertise: masked-autoencoder pretraining protocols; frozen-encoder evaluation; evaluation statistics
## Date: 2026-11-05

## Summary
The paper proposes SPAR, a masked-autoencoder pretraining scheme for multi-node, multimodal sensor data. Each node's signal tokens receive an added embedding of its (per-sample normalized, randomly rotated/translated) continuous coordinates and an added learnable per-node vector ("structural position"); a second decoder reconstructs masked spatial positions in addition to masked signals (Eqs. 1–5). Two propositions are offered as theory. SPAR is compared with eight pretraining baselines on three datasets (vehicle localization/classification, earthquake localization, activity recognition) with frozen encoders and light heads, reporting mean ± std over three seeds. SPAR has the best mean on every reported table, with very large margins on M3N-VC localization and small ones elsewhere.

## Strengths
### S1: Consistent protocol statement and variance reporting
All Tables 1–8 report mean ± std over three seeds, and §4 states that all methods share the ViT backbone, heads and number of epochs. For this scale of experiment (small heads on frozen encoders) that is the right reporting practice and lets the reader see which gaps exceed noise.
### S2: Informative ablation on the learned node embedding
Table 8 isolates four components plus masking variants on the same task. The jump from 12.98 to 22.55 MSE when the structural embedding is removed is large and well separated from the seed std (±2.98), which is a useful and honest result.
### S3: Several useful stress tests on one benchmark
Label-ratio sweep (Table 1), node-level message drop (Table 6) and a held-out placement (Table 7, scene H08/H24 excluded from pretraining, App. C.2) go beyond a single headline table; the multi-vehicle mAP@r task with a DETR-style head (Table 2) is a demanding evaluation.
### S4: Dataset statistics and temporal/subject splits are described
App. C gives sample counts (21,694 / 31,452 / 13,351), temporal and subject-disjoint splits, and the data-loss exclusion for the forearm sensor.

## Claim-to-evidence map (key claims)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | SPAR beats eight baselines | §4, Tables 1–3 | Tables 1, 2 large margins on M3N-VC; Table 3 margins ≤0.45 pts | Supported on M3N-VC; Not distinguishable from noise on HAR and Ridgecrest distance error |
| C1 | Each component contributes ("synergistic") | App. D.1 | Table 8, no interaction runs | Partially (components help individually; "synergy" untested) |
| C2 | Theory explains the design | §3.3, App. B | No empirical link | Unsupported as a *reason* for performance |
| C3 | "Resilience to scarce supervision" | §4.1 | Table 1 | Partially: SPAR degrades more than the best baseline in relative terms (W2) |
| C3 | "Robustness to missing data" | §4.1, Table 6 | Table 6 | Partially (W3) |
| C3 | Generalizes to unseen placements / "arbitrary placement" | Abstract, §2, Table 7 | One scene, random embedding reuse | Partially (W4) |

## Weaknesses
### W1: The headline advantage is attributable to a per-node learned embedding, and the paper never shows baselines get comparable node identity
Table 8 shows SPAR without the structural embedding at 22.55 ± 2.98 MSE and 5.08 m — no better than AudioMAE (22.36, 5.40) and worse than CAV-MAE (18.85, 5.06) in Table 1 at label ratio 1.0. Yet §4 says only that baselines "use the same ViT backbone architecture", and App. C.1 gives one-line descriptions. How baselines ingest several nodes and two modalities, how (or whether) they know which node a token came from, and whether they receive coordinates are not stated. Localization is hardly possible without node identity, so either the baselines have an unreported equivalent or they are handicapped. The comparison therefore cannot separate "placement-aware pretraining" from "node-ID embedding that the baselines lack".
- **Suggested Fix**: Describe the baseline input pipeline; add (i) CAV-MAE and AudioMAE with the same learned node embedding and with coordinate embeddings and (ii) a plain MAE on the SPAR architecture (no decoder 2, no coordinates). ≈ 3 baselines × 3 seeds on one dataset ≈ 30–40 GPU-hours.
### W2: Several robustness and generalization claims are worded more strongly than Tables 1, 6 and 7 show
(a) "notable resilience to scarce supervision" (§4.1): recomputed from Table 1, SPAR's MSE rises from 12.98 to 21.36 (+64.6%) between label ratios 1.0 and 0.2, whereas CAV-MAE rises from 18.85 to 24.84 (+31.8%); SPAR's lead over CAV-MAE shrinks from 31.1% to 14.0%. SPAR is still best, but it is *less* label-robust than the strongest baseline. (b) Table 6: SPAR at drop rate 0.2 gives 14.56 ± 2.47 versus CAV-MAE 15.98 ± 1.67 — a 1.42 gap inside one std; and every method's MSE at drop 0.05–0.1 is *lower* than in Table 1 (e.g., SPAR 12.65/12.48 vs 12.98; CAV-MAE 16.28/15.85 vs 18.85), which is unexplained and suggests drop is applied in a way (training-time? test-time?) that the text does not say. (c) Table 7: baselines barely degrade (FreqMAE 5.36→5.51 m) while SPAR goes 4.20→5.09 m, so the distance margin over the best baseline falls from 17.0% (vs CAV-MAE, Table 1) to 7.6% (vs FreqMAE).
- **Suggested Fix**: Report relative degradation, not only absolute values; state where message drop is applied; reword the claims.
### W3: Gains are within seed noise on two of three datasets, yet the text reads as a uniform win
Table 3 HAR: accuracy 89.63 ± 0.57 vs AudioMAE 89.18 ± 0.32 (+0.45); F1 90.45 ± 0.63 vs 90.11 ± 0.53 (+0.34). Table 3 Ridgecrest distance error 5.37 ± 0.24 vs CAV-MAE 5.48 ± 0.37 (−2.0%, MSE −25.7% is larger). Table 5 classification 99.27 ± 0.07 vs AudioMAE 99.06 ± 0.23. §4.2 says SPAR "achieves the best overall performance"; §4.3 says it underscores effectiveness "in handling heterogeneous sensor characteristics". With n = 3 seeds, none of these margins is supported by a test.
- **Suggested Fix**: Paired bootstrap over validation events/windows (cheap, no retraining) and an honest "comparable to AudioMAE/CAV-MAE" wording; add seeds to 5.
### W4: Evaluation protocol is under-specified: no test split, undisclosed selection, and pretraining on the evaluation scenes
Reported numbers come from the "validation" splits (App. C.2–C.4); the paper never says how hyperparameters, checkpoints or the mask ratio were chosen, nor on which split. For M3N-VC, models are pretrained "on all six scenes" and "on the full dataset" (§4.1, App. C.2) — it is not stated whether unlabeled clips from the later (validation) period of H24/I22 are in the pretraining set. If they are, pretraining is transductive on the evaluation clips for every method; if the node embedding is per scene, it also memorizes the evaluation nodes. This does not by itself bias the *ranking* (all methods see the same data) but it matters for the claims about generalization.
- **Suggested Fix**: State the selection protocol; hold out a test period/participants/events never used for selection; pretrain with the validation period excluded and report the delta.
### W5: Reproducibility is very low
No model size, optimizer, learning rate, batch size, number of epochs, compute, parameter counts or code link anywhere in the main text or App. A–E (full-text search). The two-decoder joint-encoder SPAR has more parameters and compute than single-decoder baselines; with no budget table, "same number of epochs" is not a compute-matched comparison.
- **Suggested Fix**: Add a hyperparameter table, params/FLOPs/wall-clock for pretraining and fine-tuning, and release code (anonymized).
### W6: Missing reference points for the earthquake and localization tasks
All comparisons are among SSL methods. There is no supervised-from-scratch model with the same head (so the value of pretraining at label ratio 1.0 is unknown) and no trivial predictor (e.g., event-centroid) to calibrate 5.4 km on Ridgecrest, where CMC/Cosmo/SimCLR sit at ~10.3–10.4 km. No domain method is compared although [54] (a supervised multi-station location network) is cited for data processing.
- **Suggested Fix**: Add supervised-from-scratch, centroid and one domain locator row to Tables 1 and 3.

**Minor:** Table 2 caption "{2,4,6,8} meters" vs columns 4/6/8/10 m; §4.3 "(e.g., wrist, ankle, chest)" vs App. C.4 "chest, forearm, head, shin, thigh, upper arm, and waist"; PhyMask is not assigned to either baseline family in §4; "MSE" is not defined (see ERR-2).

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E6 | Table 2 caption vs column headers | "r is the distance threshold varying across {2,4,6,8} meters" | Columns are mAP@4m, @6m, @8m, @10m; no 2 m column | Cross-referenced caption and header row | High | MINOR | Correct caption (or add the 2 m column) |
| ERR-2 | E6 | Tables 1, 3; §4 | "MSE (m²)" next to "Dist. Err. (m)" | If MSE were mean squared Euclidean distance, Jensen gives MSE ≥ (Dist. Err.)²; SPAR 12.98 < 4.20² = 17.64 (and 23.46 < 5.37² = 28.84). So MSE is per-coordinate or otherwise normalized, undefined in the paper | Derived | Medium | MINOR | Define MSE and the distance error |
| ERR-3 | E6/E1 | App. C.3 | "magnitudes ranging from -0.5 to 900.0 and depths between -5 km and 30,000 km" | Physically impossible values (depth > Earth radius); inconsistent with "M > -0.5" in the same sentence and with a reported MSE of 23.46 km². Typo or uncleaned labels | Cross-referenced within C.3 and Table 3 | Medium | MAJOR if labels were not cleaned, else MINOR | Clarify units/cleaning; state the label range actually used |
| ERR-4 | E5 | §4.1 | "notable resilience to scarce supervision" | Table 1: SPAR +64.6% MSE from ratio 1.0→0.2 vs CAV-MAE +31.8% | Recomputed | High | MAJOR (claim wording) | Reword; report relative degradation |

## Missing References
*Not this reviewer's focus; see Reviewer 2.*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Large gain on one benchmark, but baseline pipeline and protocol undisclosed; the structural-embedding confound |
| Clarity | 3 | Readable; missing protocol details and caption inconsistency |
| Significance | 2 | Niche task family; margins small on two of three datasets |
| Originality | 2 | Positional embeddings + node embedding + extra decoder |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main gain is confounded by an unmatched node-identity input and the protocol lacks hyperparameters, a test split and a supervised reference; typical rejected submissions share these.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound basic design; theory decorative; evaluation confound (W1) |
| Clarity & Presentation | 60 | Competent | Clear flow; omitted setup details |
| Novelty & Originality | 50 | Developing | See Reviewer 2 |
| Significance & Impact | 52 | Developing | Real problem, modest demonstrated advance beyond M3N-VC |
| Experimental Validation | 50 | Developing | Three seeds and ablations, but baselines unmatched, no test split, gains within noise on 2 of 3 datasets |
| Reproducibility | 36 | Developing | No hyperparameters, compute or code |
| Ethical Compliance | 62 | Competent | Licence stated (CC BY 4.0, App. C.2); limitations section exists; dual-use/privacy not discussed |

## Questions for Authors
1. How do the baselines receive multi-node, two-modality input, and do they get node identity or coordinates? If they do not, would CAV-MAE with the same learned node embedding close the gap? (A positive answer for SPAR would raise my score; a gap closing would lower it.)
2. Were validation-period clips of H24/I22, and the Ridgecrest 2022–2024 and HAR participants 11–15 waveforms, part of the pretraining set?
3. How were hyperparameters/checkpoints selected and on which split?
4. Where is message drop applied (pretraining, fine-tuning, test), and why does moderate drop *improve* MSE for all methods in Table 6?
5. Were the three seeds applied to pretraining as well as to the head? SPAR's std (±0.11 MSE, Table 1) is much smaller than that of most baselines.

## Limitations Assessment
**Partially.** App. E discusses only side-information for structural embeddings. Missing: dependence on known, accurate coordinates; scene-specific embeddings; centralized joint encoding.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. A real gain on the main benchmark is plausible, but the comparison does not isolate placement-aware pretraining from a node-identity input, and the protocol is not reproducible from the paper.

## Confidence
**4**: I checked all tables and the appendix, but figures were unavailable.

---

# Peer Review Report — Reviewer 2

## Paper: SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing
## Reviewer: Prof. Aiko Fernsby, Domain Reviewer (sensing/ubiquitous-computing group; fictional persona)
## Expertise: sensor-based activity recognition; time-series foundation models; multimodal contrastive learning
## Date: 2026-11-05

## Summary
The paper argues that IoT pretraining ignores the physical placement of sensors and proposes SPAR, a masked autoencoder that adds continuous coordinate embeddings, a learnable per-node vector and a position-reconstruction decoder, with an information-theoretic and a "contrastive view" analysis. It is evaluated on vehicle monitoring, earthquake localization and activity recognition against eight pretraining baselines drawn mostly from the authors' sub-community and from audio/vision.

## Strengths
### S1: Well-motivated problem framing
§1 and the "Different Notions of Spatial Context" paragraph in §2 clearly separate pixel-grid, symbolic-entity and continuous-coordinate notions of "spatial", and the placement-aware framing of multi-node sensing is a useful articulation.
### S2: Breadth of positional-reconstruction related work
§2 ("Pretraining via Positional Reconstruction Objectives") assembles jigsaw, relative-position and absolute-position prediction in vision and NLP, plus GeoMAE and LEGO, giving the reader a good map.
### S3: Domain-diverse evaluation
Using vehicle acoustics/seismics, regional seismology and body-worn IMUs spans three different physical regimes and two to three spatial scales (meters to tens of km).
### S4: Baselines include recent sensing-specific MAEs
FreqMAE [28] and PhyMask [27] (2024) and FOCAL [41] are the current sensing-specific contrastive/MAE methods, which is more than many application papers include.

## Weaknesses
### W1: The closest prior art is cited but not compared, and the novelty statement is partly contradicted by the paper itself
The paper cites methods that already feed sensor or electrode identity/geometry into masked-autoencoder pretraining — [15] Gao et al., [43] Miao et al. (multi-device wearable HAR, directly relevant to Table 3), [70] ("geometry-aware" EEG), [59] GeoMAE — and sets them aside in §2 as using "discrete symbolic entities". None is a baseline in §4. In addition, §2 claims "our approach integrates continuous physical coordinates of nodes" as the distinction and says prior positional-reconstruction works "typically operate on discrete, domain-specific positional targets", while the same paragraph says "LEGO [56] recovers perturbed molecular geometries" (continuous coordinates), and §1 cites NeRF [44], whose continuous-coordinate encodings contradict "making classical positional embedding strategies unsuitable" (§3.1). Whether [70] is correctly characterized cannot be checked here: its bibliography title ("…geometry-aware modeling") suggests it uses electrode geometry — see Question 1.
- **Suggested Fix**: Add the closest family as baselines (at minimum MAE with continuous-coordinate/Fourier encodings and a sensor-ID embedding à la [15]/[43]) and rewrite the §2/§3.1 distinctions.
### W2: Per-claim novelty is modest: C1 combines known ingredients, C2 restates known results
*(Literature check strict; no close prior work found on arXiv in 8 queries — at most "medium" per the search limit.)* C1: adding a continuous coordinate embedding and a learned per-node vector to MAE tokens, plus a second reconstruction head, is a combination of known components (position embeddings, node/ID embeddings, auxiliary regression). The structural position as defined is mathematically a learned per-node embedding, projected linearly (§3.1: "the weight matrix of F_st_embed can be understood as a learned set of basis vectors") — i.e., a node-ID embedding in a low-rank parameterization (d_R ≪ d). C2: Prop. 3.1 is the standard variational lower bound I(X;Z) ≥ H(X) − E[−log q(X|Z)] applied with conditioning; Prop. 3.2 begins "As shown by Kong et al. [31]" and relabels the same argument with extra context. Verdicts: C1 (method) **medium**; C2 (method/analysis) **incremental**; C3 (result) **not assessable** (benchmark is recent, no external numbers).
- **Suggested Fix**: State the delta to node-ID and coordinate-embedding MAEs explicitly and drop the novelty emphasis ("significantly advances" in the abstract).
### W3: The theory does not establish what the text says it establishes
Prop. 3.1 gives *lower bounds* on two different quantities (I(X;Z̃) for MAE, conditional sums for SPAR); neither bound is shown to be larger, tighter, or related to downstream performance. The statement "under certain assumptions" does not list them; the proof (App. B.1, Eq. 11 onward) assumes the latent preserves the unmasked signal and treats masked-only loss as equal to full loss. The prose conclusion — SPAR "avoid[s] memorizing redundant information" (after Prop. 3.1) — does not follow from a lower bound. Prop. 3.2's spatial pair, Eq. 10, has positions that are broadcast along tokens (§3.1), so the two "complementary masked views" of the position carry the same node coordinates whenever each node keeps at least one token in each view; the contrastive reading is then vacuous for that branch. §3 calls this "solid theoretical foundations" and "deep insights".
- **Suggested Fix**: State assumptions in the propositions, label them as interpretations, or add an empirical test (e.g., estimate position information in Z̃ with and without the second decoder).
### W4: Baselines and benchmarks are not tied to published reference numbers
The benchmark scout found no prior-work numbers to compare (no query hit RealWorld-HAR or M3N-VC results; arXiv only). All numbers are the authors' own runs. For RealWorld-HAR with six positions and a custom subject split (App. C.4) no published figure is comparable, so the 89–90% range cannot be calibrated. Under-reported baselines cannot be checked.
- **Suggested Fix**: Add a published-protocol RealWorld-HAR split or one result with numbers from an earlier paper.
### W5: Citation/characterization checks
Of the five citations the argument leans on, [31] (Kong & Zhang) is used consistently with the paper's use; [18] CAV-MAE is described correctly in App. C.1 (audio-visual contrastive+MAE) but applied to non-audio-visual sensor data without describing the adaptation; [70] is a question (above).

## Missing References
*Citation-integrity rule applied; every title below was checked with `related_search.py verify` unless marked `[verify]`. All are prior to the cutoff.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | S. Zaidi, M. Schaarschmidt, J. Martens, H. Kim, Y. W. Teh, A. Sanchez-Gonzalez, P. Battaglia, R. Pascanu, J. Godwin. "Pre-training via Denoising for Molecular Property Prediction", ICLR 2023 (found, https://arxiv.org/abs/2206.00133) | Continuous 3D-coordinate reconstruction/denoising as pretraining: bears on the claim that positional-reconstruction objectives use only discrete targets |
| Important | J. Münchmeyer et al. "Earthquake magnitude and location estimation from real time seismic waveforms with a transformer network", Geophysical Journal International 2021 (found, https://arxiv.org/abs/2101.02010) | Supervised multi-station transformer for earthquake location: a domain baseline for Table 3 |
| Helpful | R. Pan, F. Xiao, H. Zhang, M. Shen. "Kriformer: A Novel Spatiotemporal Kriging Approach Based on Graph Transformers", 2024 (found, https://arxiv.org/abs/2409.14906) | Sensor-network estimation at unobserved locations; relevant to "arbitrary placement" |
| Helpful | Y. Pang et al. "Masked Autoencoders for Point Cloud Self-supervised Learning" (Point-MAE), ECCV 2022 `[verify]` | MAE over unordered tokens with continuous 3D coordinates as positional input |

*Line of work (no specific reference): coordinate/Fourier-feature encodings from neural fields, as used for continuous inputs.*

## Literature-check addendum (Domain Reviewer)
**Per-claim novelty (claim-level profile; prior labels only):**

| Claim | Dimension | Novelty | Top prior work (level, label, cited?) | Reasoning |
|-------|-----------|---------|----------------------------------------|-----------|
| C1 | method | medium | Related-work items in the paper itself ([15], [43], [70], [59]), level 3 by my reading of their descriptions in the paper; none from the search above level 2 | Combination of known ingredients; no kept abstract covers it |
| C2 | method/analysis | incremental | Kong & Zhang [31] (cited), level 4 for Prop. 3.2; local-contrastive view of MAE (arXiv 2310.01994, found, not cited, level 3) | Prop. 3.2 restates [31] with extra context |
| C3 | result | no close prior work found in 8 queries (arXiv only) | – | Not "novel": search limit |

**Novelty delta table (closest prior works)**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| Continuous coordinates as MAE input | Fus-MAE/MAESTRO-type multi-source MAEs; GeoMAE [59]; point-cloud MAEs | Positional input to MAE for geometric data | Applied to multi-node, multi-modal sensor tokens | Partly ([59] cited; weakly differentiated) |
| Learned per-node vector | [15], [43] | Sensor identity in masked pretraining | Low-rank learned vector, per-node | Cited, differentiated by wording only |
| Position reconstruction | MP3 [71], LOCA [7], LEGO [56], molecular denoising (above) | Position targets (some continuous) | Node coordinates as targets | Cited; "discrete" claim is contradicted by [56] |

**Baseline scout:** empty for RealWorld-HAR; M3N-VC and the Ridgecrest catalog are not benchmarked in kept results.

**Field snapshot (150–250 words).** Three to five years ago sensor pretraining was dominated by contrastive multimodal alignment (CMC-style, Cosmo, COCOA, FOCAL) on small wearable datasets. Masked reconstruction (AudioMAE-style, then frequency- and physics-aware masking such as FreqMAE and PhyMask) became the strong default, and time-series foundation models and LLM-based sensing followed. The current state of the art on each benchmark in this paper is not defined, because M3N-VC, the Ridgecrest setup and the custom HAR split are used mainly by one sub-community. Open problems stated by recent work include cross-placement and cross-device generalization, missing-modality robustness and labeled-data scarcity. In this sub-field a significant contribution is a method that transfers to an unseen layout or device set without retraining, or a unified model across heterogeneous deployments, with gains beyond seed variance; a consistent +0.3–0.5 points on a small HAR benchmark is incremental. I used this to hold Novelty at 48 and Significance at 55: the idea is relevant and sensible but not demonstrated to deliver cross-layout transfer.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims exceed evidence in places; theory decorative |
| Clarity | 3 | Well organized |
| Significance | 2 | Niche, modest outside one benchmark |
| Originality | 2 | Known components recombined |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is an incremental recombination whose nearest sensing/geometry-aware relatives are cited but neither compared nor convincingly differentiated.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Sound method; proofs follow standard lines; the interpretation is overreaching |
| Clarity & Presentation | 60 | Competent | Clear, with inflated wording |
| Novelty & Originality | 48 | Developing | Medium for the method, incremental for the theory |
| Significance & Impact | 55 | Competent | Meaningful sub-area, modest gains outside M3N-VC |
| Experimental Validation | 52 | Developing | See Reviewer 1 |
| Reproducibility | 40 | Developing | Missing hyperparameters, no code |
| Ethical Compliance | 62 | Competent | Basic compliance |

## Questions for Authors
1. How does [70] (the paper's own bibliography title: "…geometry-aware modeling") use electrode geometry, and why is it classed as "discrete symbolic entities" while SPAR's coordinates are "continuous"? `[verify]` A clear difference would raise my Novelty score.
2. What is the empirical gap between SPAR and MAE with Fourier-feature coordinate embeddings plus a learned sensor-ID embedding, i.e., the combination of [43]/[15] and [59]?
3. What additional evidence beyond Table 7 shows generalization to unseen layouts, as claimed in §2 ("generalization to unseen spatial configurations")?

## Limitations Assessment
**Partially.** Related-work limits and assumptions on known coordinates are missing.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. A relevant problem and a sensible recipe, but novelty is modest and positioning against the closest prior art (cited, not compared) is not convincing.

## Confidence
**4**: Know the sensing literature well; did not check proofs line by line beyond the main steps.

---

# Peer Review Report — Reviewer 3

## Paper: SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing
## Reviewer: Dr. Lucía Montenegro-Bell, Perspective Reviewer (geophysics and signal-processing institute; fictional persona)
## Expertise: array signal processing; seismic source location; sensor-network deployment
## Date: 2026-11-05

## Summary
SPAR learns representations of multi-node signals by telling the encoder where each sensor is (coordinates plus a learned per-node vector) and asking a second decoder to recover masked positions. The authors argue this lets a single pretrained model serve tasks that depend on geometry — locating vehicles or earthquakes, recognizing body-worn activity — and that it copes with lossy links and new placements. It is an appealing way to bring something that array processing has always known (location and geometry matter) into learned representations.

## Strengths
### S1: Brings geometry into learned sensor representations
In array processing and seismic location the geometry of the stations is central. Encoding it into the representation (§3.1) is a principled move that the ML-for-IoT literature has under-used. §1's examples (seismic/acoustic choke points, on-body IMUs) are well chosen.
### S2: Spans three physically different regimes
Meters-scale vehicle tracking (Table 1/2), tens-of-kilometers regional seismology (Table 3, §4.2) and body-scale IMUs (§4.3) make the framework's generality plausible. The Ridgecrest data (20.38% naturally missing stations, §4.2) is a realistic partial-observation setting.
### S3: Practical handling of missing nodes
Zero-padding missing entries and masking them out of the loss (end of §3.2) is simple and deployment-friendly; the message-drop study (Table 6) is the right kind of test.
### S4: Honest qualitative figures
Failure cases in App. D.1 (Fig. 4, bottom row: false positives and negatives) are shown, which is not universal.

## Weaknesses
### W1: Centralized joint encoding clashes with the "distributed sensing" premise
Eq. 2 applies a joint transformer over the concatenated latents of all modalities and nodes, so all nodes' data must reach one place; there is no discussion of communication, energy or latency, and attention scales with total tokens (nodes × tokens, 6–16 nodes here, App. C). The title and abstract position SPAR as "distributed sensing" without addressing how it would run on constrained or intermittently connected nodes.
- **Suggested Fix**: Report params/FLOPs, per-node cost and a bandwidth-limited variant (e.g., early fusion on a gateway), or scope the claim.
### W2: Key physical assumptions are implicit and untested
(i) Known, accurate coordinates: in HAR, coordinates are "manually assign[ed]… based on standard anatomical placement" (App. C.4), so the spatial branch is exercised with synthetic, constant positions; on M3N-VC GPS is 1 Hz and noisy. (ii) Per-sample normalization to zero mean and unit variance (§3.1) removes absolute scale and location: how can one model separate a parking lot from a 50 km network, as claimed ("spatial scales"), and how are predictions mapped back to meters/km? (iii) Time synchronization across nodes is assumed but not stated. (iv) The effect of signal propagation (distance attenuation, velocity models) is left to be learned.
- **Suggested Fix**: Add a coordinate-noise sweep (perturb S by 1–10 m), an experiment without normalization or with scale as an input, and a statement on synchronization.
### W3: Classical and physics-based references are missing from the evaluation
Seismic location has standard travel-time/inversion locators and supervised multi-station networks (cited as [54], not compared); for acoustic/seismic vehicle localization, time-difference-of-arrival and beamforming are standard. A reader from those fields cannot tell whether 5.4 km (Table 3) or 4.2 m (Table 1) is useful. A supervised-from-scratch run and a classical baseline would show where SPAR sits.
- **Suggested Fix**: One classical locator per task, even coarse; report the label-free pretraining gain against a supervised model.
### W4: Dual-use and privacy are not discussed
§1's lead example is detecting and typing "potential intruders (e.g., humans, vehicles, stray animals)" at a border choke point; M3N-VC uses 16 kHz microphones and smartphone GPS traces. No broader-impact or ethics statement exists, and the HAR data involves 15 participants (App. C.4).
- **Suggested Fix**: Add a short impact paragraph and a statement on data consent/licensing for the audio and GPS data.
**Minor:** Figure 3/6 map credits are good practice; define "mAP@r" thresholds in the caption of Table 2.

## Missing References
*Optional for this reviewer.* Named methods only: beamforming and time-difference-of-arrival localization for acoustic arrays; travel-time-based earthquake location; Gaussian-process/kriging interpolation for sensor networks; permutation-invariant set encoders (Set Transformer, Perceiver-style cross-attention) for variable node sets.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Reasonable design and testing |
| Clarity | 3 | Clear |
| Significance | 3 | Fits a real need |
| Originality | 3 | A useful transfer of an old idea |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a well-motivated geometry-aware pretraining scheme with the best mean on every table, tempered by missing deployment and physics reference points.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Design is plausible; assumptions implicit |
| Clarity & Presentation | 66 | Competent | Clear structure |
| Novelty & Originality | 62 | Competent | New for sensor pretraining; known in neighboring areas |
| Significance & Impact | 68 | Competent | Broad application relevance |
| Experimental Validation | 60 | Competent | Multi-dataset but missing references |
| Reproducibility | 50 | Developing | Details missing (deferred to the reader) |
| Ethical Compliance | 58 | Developing | Surveillance/privacy unaddressed |

## Questions for Authors
1. Can SPAR run when the node set at test time differs in size from pretraining? What happens with 3 or 12 nodes instead of 6–8?
2. How sensitive are results to coordinate noise? A flat curve to ~5 m would raise my Significance score; a steep one would lower it.
3. How is the per-sample normalization inverted for the localization heads?

## Limitations Assessment
**Partially.** App. E covers metadata only; deployment and privacy limits are absent.

## Ethics Review Flag
**No.** A short impact statement would be advisable for the surveillance-adjacent motivating example; no concrete violation visible.

## Overall Score
**4**: Borderline Accept. An interesting, physically grounded idea with consistent mean gains across three regimes; weaknesses are the ordinary ones of an application paper, but the practical story is incomplete.

## Confidence
**3**: Outside the ML-methods core; did not check the proofs in detail.

---

# Peer Review Report — Reviewer 4

## Paper: SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing
## Reviewer: Dr. Kwabena Osei-Lindgren, Generalist Reviewer (vision and learning lab; fictional persona)
## Expertise: representation learning, masked autoencoders (not sensing)
## Date: 2026-11-05

## Summary
The paper proposes a masked-autoencoder-style pretraining scheme for sensor networks in which each token carries both its signal and the (continuous) location and a learned identity of the node it came from, and a second decoder reconstructs masked locations. It is evaluated on three sensing datasets with frozen encoders and small heads and compared with eight pretraining baselines; the method is best on average on all of them. A theory section explains the design from information-theoretic and contrastive viewpoints.

## Strengths
### S1: The contribution fits in one sentence, and the design is simple
Reading §1 and §3 I can state what is new: add coordinates and per-node vectors to the tokens, and reconstruct positions as well as signals. The method is a small extension of MAE and easy to adopt (§3.1–3.2).
### S2: Experiments are broad enough for an application-oriented ICLR paper
Three datasets, eight baselines, label-ratio and message-drop sweeps, an unseen-placement test, ablations and masking variants (Tables 1–8) are more than the median application submission.
### S3: Standard error bars throughout
Mean ± std over three seeds in every table lets me see where gaps are meaningful (e.g., Table 1) and where they are not (e.g., Table 3).
### S4: Clear related-work positioning on "what spatial means"
The distinction between grids, symbolic entities and continuous coordinates (§2) is a helpful framing for a reader outside sensing.

## Weaknesses
### W1: Important implementation details are missing, so I cannot judge fairness
I cannot find the model size, epochs, optimizer, learning rate, batch size, compute or code, and the paper does not say how baselines read multi-node input (§4, App. C.1). For a reader from outside sensing this is the main obstacle to trusting Table 1–3.
- **Suggested Fix**: A hyperparameter and compute table; a short description of each baseline's input pipeline; code.
### W2: The abstract and intro claim more than the experiments show
"The work significantly advances self-supervised model pretraining" (Abstract), "SPAR is grounded in solid theoretical foundations" (§3), "demonstrating a synergistic effect" (App. D.1) and "arbitrary placement" (Abstract) outrun what Tables 3, 7 and 8 show: the HAR gain is +0.45 accuracy against a 0.57 std; the unseen-placement test is one scene with embeddings reused from other nodes (App. D.1); "synergy" has no interaction experiment. The paper would be stronger, not weaker, with plainer wording.
- **Suggested Fix**: Rewrite the abstract/intro claims to match Tables 1–8.
### W3: The main text pushes the most informative results to the appendix
Five of the eight experiment sets (classification, message drop, unseen placement, ablations, masking) are described in a few lines in §4.1 and live in App. D; the ablations that decide whether the idea works (Table 8) are not in the main paper. For ICLR's presentation criterion, the key ablation and the unseen-placement table belong in the body, and the proof sketches can move out.
- **Suggested Fix**: Move Tables 7–8 into §4 and shorten §3.3.
### W4: The theory section is long relative to what it delivers
§3.3 occupies a page and a half, uses "under certain assumptions" without stating them (Prop. 3.1), and Prop. 3.2 opens with a result from another paper. The reader leaves without a testable prediction. I would rather see one experiment that verifies a theoretical claim.
- **Suggested Fix**: State assumptions; connect theory to a measurable quantity or shorten.

## Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported by evidence | Partly | Tables 1–8; HAR and Ridgecrest within noise; theory not linked to results |
| Presentation | Partly | Clear text; key tables in appendix; Table 2 caption wrong |
| Contribution significance | Partly | New application of position-aware MAE; strong on one benchmark |
| Reproducibility | Not met | No hyperparameters or code anywhere |
| Fit to ICLR (representation learning) | Met | Pretraining with analysis; applied |

## Missing References
*Optional; see Reviewer 2.*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound recipe, with gaps |
| Clarity | 3 | Readable |
| Significance | 3 | Moderate |
| Originality | 2 | Small extension of MAE |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, simple idea with consistent gains and ablations, in an application niche; the omissions are typical of weaker accepted papers but not of strong ones.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Sound basics; missing details |
| Clarity & Presentation | 66 | Competent | Easy to follow; key content in the appendix |
| Novelty & Originality | 58 | Competent | Incremental extension |
| Significance & Impact | 62 | Competent | Useful sub-area |
| Experimental Validation | 60 | Competent | Broad, with gaps |
| Reproducibility | 48 | Developing | Nothing to reproduce from |
| Ethical Compliance | 62 | Competent | Basic |

## Questions for Authors
1. Can you move Table 8 and Table 7 to the main text and add the baseline-input description? (Doing so would raise Clarity.)
2. What is the parameter count and pretraining time of SPAR relative to AudioMAE and CAV-MAE?
3. Could the claims about "arbitrary placement" be narrowed to what Table 7 shows?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. I lean toward accepting a clear, simple idea with consistent gains, provided the missing implementation details and claim wording are fixed; the reasons to accept narrowly outweigh the reasons to reject.

## Confidence
**4**: Confident on the ML side; limited sensing background.

---

# Devil's Advocate Report

## Paper: SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing
## Reviewer: Dr. Priyanka Haldenwang (evaluation-methodology group; fictional persona)

## Steelman
SPAR is the first sensing-specific masked-autoencoder recipe to treat sensor geometry as a first-class input and to ask the model to recover it. On the largest benchmark it gives gains over a strong field of baselines that are far beyond seed variance (Table 1: 12.98 vs 18.85 MSE; Table 2: 41.57 vs 22.12 mAP@4m), and a clean ablation (Table 8) shows each design element matters.

## Core Argument Chain
1. P1: Sensor placement shapes the signals and is ignored by current IoT pretraining (§1).
2. P2: Adding spatial and structural embeddings plus reconstructing positions makes the encoder placement-aware (§3).
3. P3: The theory shows SPAR's loss keeps more useful, context-aware information than MAE (Prop. 3.1, 3.2).
4. P4: SPAR beats eight baselines under a fair protocol on three datasets (§4).
5. P5: It is robust to scarce labels and missing data and generalizes to unseen placements (§4.1, App. D).
∴ SPAR "significantly advances" placement-aware pretraining and generalizes across modalities, placements, tasks and scales.

## Strongest Counter-Argument
The evidence supports "adding a per-node learned embedding to an MAE helps" much better than it supports "placement-aware pretraining via coordinates and position reconstruction helps". Three observations in the paper's own tables point that way. First, removing the structural (learned per-node) embedding turns SPAR from the best method (12.98 MSE) into an average one (22.55 ± 2.98, Table 8), equal to AudioMAE (22.36, Table 1) and worse than CAV-MAE (18.85); the paper never says whether baselines get any node identity, and localization cannot be done without it. Second, the coordinate and spatial-reconstruction components, which are the paper's stated novelty, contribute the smallest effects (Table 8: 15.12 and 14.73 vs 12.98). Third, the spatial reconstruction target is nearly trivial by construction: positions are broadcast to every token of a node (§3.1), masking is random per token (§3.2, ratio 0.75), so for any node with at least one unmasked token the encoder has already seen the exact coordinates and the spatial decoder can read them back; the one masking variant that makes the task non-trivial — masking whole nodes ("Node-Drop Masking") — *hurts* (17.71, App. D.1/Table 8). The "duality of signals and positions" and the contrastive reading in Prop. 3.2 (Eq. 10: two complementary views of a position that carries identical content) do not describe a mechanism that the experiments exercise. Meanwhile the generalization claims are built on one unseen scene whose nodes are given embeddings "randomly selected from those learned during pretraining" (App. D.1), a protocol with no counterpart for the baselines. If SPAR's win is largely a node-ID effect, the comparison with eight baselines that were possibly given no equivalent is not a test of the paper's thesis. The authors need a node-ID-matched baseline and an experiment in which positions are not recoverable from unmasked tokens.

## Issue List

### CRITICAL Issues
**No CRITICAL issues found.** The central empirical finding (large gain on M3N-VC over every baseline, three seeds) is not contradicted by the paper's evidence; the problems above narrow what it shows, and are fixable by clarification and added controls. The paper does not state test-set selection (protocol sweep: only "validation" splits named, no selection statement), so criterion 3 is a question, not a finding.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Table 8 vs Table 1; §4 "same ViT backbone" | Gain is largely attributable to the learned per-node embedding (22.55 vs 12.98 MSE, +73.7%); baselines' node identity input is undefined, so "placement-aware" is not isolated | Node-ID-matched and coordinate-matched baselines; plain-MAE-on-SPAR row |
| DA-M2 | Logic | §3.1 (broadcast S), §3.2 (random token masking), Table 8 "w/o Reconstructing Spatial Positions" 14.73, "+ Node-Drop Masking" 17.71 | Spatial reconstruction is near-trivial under random masking; the dual-objective claim is not exercised | Mask whole nodes for the spatial target, or report reconstruction error vs masking fraction; show spatial loss is non-trivial |
| DA-M3 | Scope | Abstract "allowing arbitrary placement"; App. D.1, Table 7 | Generalization to new placements tested on one scene with embeddings reused from other nodes; baselines don't get this protocol; SPAR's distance margin falls to 7.6% | More scenes, leave-one-scene-out across all six, new node counts; learn embeddings in fine-tuning for baselines |
| DA-M4 | Evidence | Tables 3, 5; §4.2–4.3 | Margins within std on HAR (+0.45 acc), Ridgecrest distance error (−2.0%) and classification (+0.21); text says "best overall performance" | Paired bootstrap; reword |
| DA-M5 | Evidence | Table 2 | Six of eight baselines score ≤ 0.31 mAP@4m and ≤ 6.8 at 10m, whereas their single-vehicle numbers are ordinary (Table 1); this looks like failed head training rather than weak representations, leaving CAV-MAE (22.12) as the only informative baseline | Check baseline heads (loss weights, convergence); report training curves |
| DA-M6 | Logic | §3.3, Prop. 3.1 | Lower bounds on different quantities are presented as showing SPAR is better; "under certain assumptions" never specified | State assumptions; do not claim a ranking |
| DA-M7 | Protocol | App. C.2–C.4; §4.1 | No test split; selection protocol undisclosed; pretraining on "the full dataset" may include evaluation-period clips | State and, if needed, redo with an excluded evaluation period |
| DA-M8 | Evidence | App. C.3 | Impossible label ranges (900.0 magnitude, 30,000 km depth) in the catalog description | Clarify cleaning and units |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Wording | Abstract, §3, App. D.1 | "significantly advances", "solid theoretical foundations", "synergistic effect" |
| DA-m2 | Presentation | Table 2 caption | {2,4,6,8} vs 4/6/8/10 m |
| DA-m3 | Consistency | §4.3 vs App. C.4 | "wrist, ankle, chest" vs "chest, forearm, head, shin, thigh, upper arm, waist" |
| DA-m4 | Evidence | Table 8 | Node-Balanced Masking 12.54 ± 1.63 vs 12.98 ± 0.11 called "slight improvement"; within noise |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| SPAR vs CAV-MAE MSE gap, ratio 1.0 (Table 1) | 12.98 vs 18.85 | (18.85−12.98)/18.85 = 31.1% | n/a (not stated) |
| Same, ratio 0.2 | 21.36 vs 24.84 | 14.0% | Margin shrinks |
| MSE growth 1.0→0.2: SPAR / CAV-MAE | 12.98→21.36 / 18.85→24.84 | +64.6% / +31.8% | Contradicts "notable resilience" relative to the best baseline |
| Removing structural embedding (Table 8) | 22.55 vs 12.98 | +73.7% | Consistent with the text ("more substantial degradation") |
| Table 7 distance margin | 5.09 vs best baseline 5.51 | 7.6% (vs 17.0% in Table 1) | Narrower, as stated by no text |
| HAR accuracy gap (Table 3) | 89.63 vs 89.18 | +0.45; stds 0.57/0.32 | Within noise |
| Ridgecrest distance gap (Table 3) | 5.37 vs 5.48 | −0.11 km (2.0%); stds 0.24/0.37 | Within noise |
| Fig. 7 accuracy from confusion matrix | – (Table 3: 89.63 ± 0.57) | 3890/4311 = 90.2% | Consistent (one run vs. mean) |
| Fig. 5 accuracy | – (Table 5: 99.27 ± 0.07) | 1578/1589 = 99.3% | Consistent |

## Ignored Alternative Explanations
- Node-identity input (any learned node ID) explains most of the gain over baselines with no such input.
- Transductive pretraining on evaluation-scene clips may inflate M3N-VC numbers for all methods and favour methods that store scene-specific node vectors.
- Different effective capacity/compute (two decoders plus joint encoder) rather than the positional idea.
- A weakly trained detection head explains the near-zero mAP of six baselines in Table 2.
- Moderate message drop improves all methods in Table 6, which suggests a regularization effect rather than robustness.

## Missing Stakeholder Perspectives
Operators of sensor deployments (communication and energy budgets); people recorded by outdoor microphones and GPS traces; domain seismologists who would judge 5 km location error against catalog standards.

## Observations (Non-Defects)
- Seeds and std reported everywhere; the largest gains are far outside noise.
- The structural-embedding ablation is honestly reported even though it is unflattering to the "coordinates" story.
- The paper discloses a manual coordinate assignment for HAR and the forearm exclusion.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Confounded attribution; theory not linked |
| Clarity & Presentation | 58 | Readable; overclaiming wording |
| Novelty & Originality | 48 | Recombination; theory is a restatement |
| Significance & Impact | 52 | Problem relevant; demonstrated advance narrower than claimed |
| Experimental Validation | 48 | Missing controls and references |
| Reproducibility | 36 | Nothing to reproduce from |
| Ethical Compliance | 58 | Surveillance/privacy unaddressed |

**Pool position:** better than about 46% of submissions to ICLR. Deciding evidence: the claimed mechanism is not isolated by the experiments, a signal shared by typical rejected submissions.

## Overall: 3 | Confidence: 4

---

# PHASE 1.5 / 1.6 — Report Check

The literature-check addendum is part of Reviewer 2's report (above). Each weakness was tested for specificity, whether the paper already answers it, consistency with the paper, and actionability.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept | Each cites a table/section and a fix; checked against the appendix (no baseline-pipeline description exists) |
| R1 | Minor line (caption, wrist/ankle, PhyMask grouping) | moved to Minor | Cosmetic |
| R2 | W1 ([70] characterization) | rewritten | Its bibliography title is the only evidence available, so the claim was turned into a question with `[verify]`; the LEGO/NeRF contradiction is in the paper's own text and was kept |
| R2 | W4 (no published numbers) | rewritten | Phrased as a limit of the arXiv-only scout, not a missing baseline |
| R2 | W5 | moved to Minor | Citation check found nothing wrong beyond [70] |
| R3 | W1–W4 | kept | W3 rephrased as "reference points", not a required comparison |
| R4 | W3 (main text vs appendix) | kept | Presentation point that affects how the contribution is judged |
| DA | DA-M5 (near-zero baselines) | rewritten | Marked as an inference (suspected under-training), put to the authors as a check, not as an error |
| DA | DA-M8 | kept | Located; quote verified |
| All | Scores | unchanged | Not modified in this step |

---

# PHASE 2 — Synthesizer Package, EIC Meta-Review and Editorial Decision

## Synthesizer, Part A: Master issue list

| Merged issue | Source IDs | Class |
|---|---|---|
| Gain attributable to the learned node embedding; baselines' node input undefined | R1-W1, DA-M1 (R4-W1 on missing details) | CONSENSUS-3 |
| Missing hyperparameters, compute and code | R1-W5, R4-W1, R2 (Repro score), DA | CONSENSUS-4 |
| Overstated claims (resilience, robustness, synergy, "arbitrary placement", "significantly advances") | R1-W2, R4-W2, DA-M3/M4, DA-m1, R2-W2 | CONSENSUS-4 |
| Gains within noise on HAR / Ridgecrest / classification | R1-W3, DA-M4 (R4 mention) | CONSENSUS-2 |
| Theory does not support the stated conclusions | R2-W3, DA-M6, R4-W4 | CONSENSUS-3 |
| Novelty modest; closest priors cited but not compared | R2-W1/W2, R1 (Novelty score), DA | CONSENSUS-3 |
| Unseen-placement evidence is thin | R1-W2c, R3 (Q1), DA-M3 | CONSENSUS-3 |
| Protocol: no test split, selection undisclosed, pretraining on evaluation scenes | R1-W4, DA-M7 | CONSENSUS-2 |
| Spatial reconstruction near-trivial under random masking | DA-M2 (R2-W3 on Eq. 10) | SOLO (+ partial R2) |
| Weak reference points (supervised, centroid, classical) | R1-W6, R3-W3 | CONSENSUS-2 |
| Centralized fusion vs distributed premise; privacy/dual-use | R3-W1, R3-W4 | SOLO |
| Near-zero baselines in Table 2 | DA-M5 | SOLO |
| Impossible catalog ranges, Table 2 caption, HAR positions text | R1 ERR-1/3, DA-M8, DA-m2/m3 | CONSENSUS-2 |
| SPLIT | R3 and R4 (Overall 4) vs R1, R2, DA (Overall 3) on whether the contribution outweighs the gaps | SPLIT |

**DA-CRITICAL issues:** none raised. **Issues the outcome may hinge on:** node-embedding attribution (DA-M1), spatial reconstruction triviality (DA-M2), reproducibility/protocol, noise-level gains.

**Official score (before EIC weights; script run on `scores_before.json`):** official ratings R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40; official composite 55.1; no warnings.

## EIC Meta-Review (Prof. Imani Rautavaara)

### The Case For and Against
- **For acceptance:** The problem (placement-aware pretraining for multi-node sensing) is well defined, the recipe is simple and easy to adopt, and the gains on M3N-VC are far larger than seed noise (Table 1: 12.98 vs 18.85 MSE; Table 2: 41.57 vs 22.12 mAP@4m). Ablations (Table 8), a label-ratio sweep, a message-drop study and a held-out placement test make the evaluation broader than many application papers.
- **Against acceptance:** The decisive ablation shows that the learned per-node embedding carries most of the gain, and the paper never says whether baselines get any node identity. The novelty attributed to coordinates and position reconstruction (the smaller ablation effects, and a reconstruction target that is nearly trivial under the stated masking) is not demonstrated. Gains are within noise on two of three datasets, nothing needed to reproduce the work is given (no hyperparameters, compute or code), no test split or selection protocol is stated, and the theory does not support the claims it is attached to.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Removing structural embedding collapses SPAR to AudioMAE/CAV-MAE level | R1-W1, DA-M1 | Table 8 (22.55 ± 2.98) vs Table 1 (22.36, 18.85) | Verified | Numbers match |
| Baselines' node/position input not described | R1-W1, R4-W1, DA-M1 | §4, App. C.1 | Verified | Searched text; only one-line baseline descriptions |
| Spatial reconstruction near-trivial under random masking | DA-M2 | §3.1 (broadcast), §3.2 (token masking), Table 8 | Partly correct | Mechanism follows from the equations and is consistent with Table 8 (14.73; Node-Drop 17.71), but it is an inference; the paper never measures the spatial loss |
| "Resilience to scarce supervision" overstated | R1-W2a, ERR-4 | §4.1, Table 1 | Verified | +64.6% vs +31.8% recomputed; SPAR still best at every ratio |
| Gains within noise on HAR / Ridgecrest distance / Table 5 | R1-W3, DA-M4 | Tables 3, 5 | Verified | 0.45 vs std 0.57; 0.11 vs 0.24–0.37; 0.21 vs 0.23 |
| Message-drop table: unexplained improvement vs no-drop | R1-W2b | Table 6 vs Table 1 | Verified | All methods' MSE lower at 5–10% drop (SPAR 12.65/12.48 vs 12.98) |
| Unseen-placement evidence is one scene with reused embeddings | R1, R3, DA-M3 | App. D.1, Table 7 | Verified | Quote: "randomly selected from those learned during pretraining" |
| No hyperparameters/compute/code | R1-W5, R4-W1 | Full-text search | Verified | None found, including the appendix |
| No test split; selection not stated | R1-W4, DA-M7 | App. C.2–C.4 | Verified | Splits named "validation"; no selection statement found; not criterion 3 on this record |
| Prop. 3.1/3.2 do not support the stated reading | R2-W3, DA-M6, R4-W4 | §3.3, App. B | Partly correct | Derivation of the bounds is standard and follows; the interpretive claims ("avoids memorizing redundant information", "deep insights") do not follow. The vacuity of Eq. 10 holds when each node keeps ≥1 token |
| Table 2 caption vs columns | R1 ERR-1, DA-m2 | Table 2 | Verified | |
| Impossible ranges in Ridgecrest catalog | R1 ERR-3, DA-M8 | App. C.3 | Verified (as printed) | Whether typo or uncleaned labels is unknown; would be MAJOR only if labels were not cleaned |
| Near-zero baselines imply failed heads | DA-M5 | Table 2 | Overstated | Plausible inference; the paper offers no evidence either way. Reasonable to ask for a check |
| [70] mischaracterized as "discrete" | R2-W1 | §2, bibliography | Unverifiable | Only the title is available; stays a question. The LEGO and NeRF inconsistencies in the paper's own text are verified |
| "classical positional embeddings unsuitable" overstated | R2-W1 | §3.1; §1 cites NeRF [44] | Verified | |
| Closest sensing/geometry MAEs cited, not compared | R2-W1 | §2 vs §4 baseline list | Verified | |

*Literature check ledger:* no weakness rests on a recent preprint, concurrent or newer work; the only recommended references (Zaidi et al.; Münchmeyer et al.; Kriformer) are prior to the cutoff and were found by `verify`; Point-MAE stays marked `[verify]`. No text overlap flags, no integrity-scan findings.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Recomputed numbers and ERR-1/3/4 verified; W4/W5 verified; minor overstatement on ERR-3 severity |
| R2 (Domain) | 3 | 4 | 1.0 | W1–W3 verified; the [70] point correctly demoted to a question; novelty slightly harsh but justified |
| R3 (Perspective) | 4 | 3 | 1.0 | Sound deployment and assumption points, partly generic; Overall 4 is slightly lenient given verified protocol gaps, within the role |
| R4 (Generalist) | 4 | 4 | 1.0 | Accurate on missing details and claim wording; calibration a little generous on reproducibility |
| DA | 3 | 4 | 1.25 | Strongest counter-argument survived the check (M1 verified, M2 partly); no inflated CRITICAL; DA-M5 overstated but flagged as inference |

### DA-CRITICAL Rulings
No CRITICAL issue was raised, so there is nothing to uphold or downgrade. I checked the criterion-3 question independently: the paper names only train and "validation" splits, makes no statement of selecting configurations on the reported split (protocol sweep above), so under the decision table it is a MAJOR question about the selection protocol (DA-M7), not leakage. **DA ceiling: none.**

### Final Decision and Justification
**Official ratings** are R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40**; official composite 55.1. **EIC-weighted rating** (script, after weights) is **3.34** → starting point **3 (Borderline Reject)**; EIC-weighted composite 54.4 → band 3, agreeing with the rating, so there is no cross-check disagreement. I keep the starting point and decide **Borderline Reject (3)**. The deciding evidence is specific and located. (1) The headline gain is not isolated: the learned per-node embedding, whose baseline analogue is undefined, accounts for the largest ablation effect (Table 8), and the paper's own claimed novelty (coordinates, position reconstruction) contributes less (Table 8: 15.12, 14.73) with a reconstruction target that is trivially satisfiable under the stated masking. (2) Gains are within noise on HAR, Ridgecrest distance error and Table 5, so the "generalizability across modalities" reading rests chiefly on one benchmark (M3N-VC, scenes H24 and I22). (3) Nothing required to reproduce the work is given (no hyperparameters, compute, code, selection protocol, test split). (4) Theory is decorative and its claims overreach. My pool position is **52**: the paper is above the median submission (a real, large gain on its main benchmark; a clear idea; honest ablations; seeds reported) but below the accepted-paper band, because the central mechanism claim and the generalization claims are not tested by controls an accepted ICLR paper would normally include, and the weaknesses are the kind that typical rejected submissions share. R3's and R4's Overall 4 are respected — their pool positions of 66 and 65 are higher than the evidence I verified supports, mainly because neither weighed the node-embedding attribution — but all four substantive issues are fixable, and this is exactly the kind of paper that moves up if the node-ID-matched baselines and the protocol details show the gain survives. The decision does not exceed any DA ceiling (none applies). The simulated outcome is how a careful panel would likely see this draft, not a prediction.

**Final (EIC): 3.** ICLR rating for this decision: **4 on {0,2,4,6,8,10}** (5 on the earlier {1,3,5,6,8,10} scale).

---

## Score Summary

### Official Scores and EIC Assessment
*Output of `aggregate_scores.py scores.json --venue iclr --final 3` (EIC weights applied).*

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 52 | 55 | 62 | 60 | 50 | 55.8 | 55.1 | 12 |
| Clarity & Presentation | 60 | 60 | 66 | 66 | 58 | 62.0 | 61.6 | 8 |
| Novelty & Originality | 50 | 48 | 62 | 58 | 48 | 53.2 | 52.5 | 14 |
| Significance & Impact | 52 | 55 | 68 | 62 | 52 | 57.8 | 56.9 | 16 |
| Experimental Validation | 50 | 52 | 60 | 60 | 48 | 54.0 | 53.3 | 12 |
| Reproducibility | 36 | 40 | 50 | 48 | 36 | 42.0 | 41.2 | 14 |
| Ethical Compliance | 62 | 62 | 58 | 62 | 58 | 60.4 | 60.4 | 4 |
| **Composite** | 51.5 | 53.0 | 61.3 | 59.6 | 49.8 | **55.1 (before)** | **54.4 (after)** | |
| Pool position (P%) | 48 | 50 | 66 | 65 | 46 | | | |

No dimension spread exceeds 20 points; no consistency warnings.

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "SPAR: Self-supervised Placement-Aware Representation Learning for Distributed Sensing" to ICLR. The question of how sensor placement should enter pretraining is interesting and under-explored, and the paper gives it a clear, simple formulation.

**Overall Assessment:** The panel found the idea clear and the gains on the multi-vehicle and single-vehicle localization benchmark large and well beyond seed noise. The panel was split: two reviewers leaned toward acceptance, three toward rejection. After checking the decisive points against the manuscript, the area chair weighted the concerns about attribution and reproducibility more heavily.

**Key Strengths Identified by Reviewers:**
1. A simple, adoptable recipe addressing a relevant problem, with a clear framing of what "spatial" means for sensing (R2, R3, R4).
2. Three-seed mean ± std in all tables; strong, well-separated gains on M3N-VC (R1, R4, DA).
3. A useful learned-embedding ablation, label-ratio, message-drop and held-out-placement experiments (R1, R4).

**Key Concerns Requiring Attention:**
1. The main gain is largely explained by the learned per-node embedding (Table 8), and baselines' node/position input is undefined; coordinates and position reconstruction contribute less, and the spatial target is nearly trivial under the stated masking (R1, DA, R4 — CONSENSUS-3 for attribution).
2. Reproducibility and protocol: no hyperparameters, compute, code, test split or selection protocol; possible pretraining on evaluation scenes (CONSENSUS-4/2).
3. Claims exceed evidence: "resilience", "robustness", "arbitrary placement", "synergy", and gains within noise on HAR, Ridgecrest distance error and classification (CONSENSUS-4/2).
4. The theory does not support the statements made about it, and the closest sensing/geometry-aware MAE works are cited but not compared (CONSENSUS-3).

**Decision: Borderline Reject (3).**

The deciding issue is that the experiments do not yet isolate what the paper says is new. A revised version that shows the gain survives node-identity-matched baselines, that gives the training and selection protocol, and that narrows the generalization claims would be considered for a different outcome. Please see the Revision Roadmap below.

Sincerely,
Prof. Imani Rautavaara
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Missing hyperparameters, compute, code | R1, R2, R4, DA | CONSENSUS-4 |
| Claims exceed evidence | R1, R2, R4, DA | CONSENSUS-4 |
| Node-embedding attribution / baseline input undefined | R1, R4, DA | CONSENSUS-3 |
| Theory does not support stated conclusions | R2, R4, DA | CONSENSUS-3 |
| Novelty modest, closest priors not compared | R1, R2, DA | CONSENSUS-3 |
| Unseen-placement evidence thin | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Contribution outweighs weaknesses | R3, R4 (Overall 4) | R1, R2, DA (Overall 3) | The weaknesses in R1/DA were verified in the tables; R3/R4 did not weigh the node-embedding attribution. Decision 3 |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. The widest are Significance (16) and Novelty (14), driven by R3 (68/62) versus R1/DA (52/50, 48); I adopt the lower view for Novelty (verified delta to node-ID and coordinate MAEs is not shown) and a middle view for Significance.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| – | CRITICAL | None raised | – | – | – |
| DA-M1 | MAJOR | Gain attributable to learned node embedding; baselines' node input undefined | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Spatial reconstruction near-trivial under random masking | Partly (R2-W3) | n/a | n/a |
| DA-M3 | MAJOR | Unseen placement thinly tested | Yes (R1, R3) | n/a | n/a |
| DA-M4 | MAJOR | Gains within noise on 2 of 3 datasets | Yes (R1-W3) | n/a | n/a |
| DA-M5 | MAJOR | Near-zero baselines in Table 2 | No | n/a | n/a |
| DA-M6 | MAJOR | Theory ranking claim not supported | Yes (R2-W3) | n/a | n/a |
| DA-M7 | MAJOR | No test split; selection and pretraining protocol | Yes (R1-W4) | n/a | n/a |
| DA-M8 | MAJOR | Impossible catalog ranges | Yes (R1 ERR-3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*Issues the EIC verified as undermining a main claim (no upheld DA-CRITICAL issue). All Priority 1 items must be addressed for acceptance.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Gain not isolated from a node-identity input; baseline input pipeline undefined | R1-W1, DA-M1 | §4, App. C.1, Table 8 | Describe baseline inputs; add CAV-MAE/AudioMAE with the same learned node embedding and with coordinate embeddings; add plain MAE on the SPAR architecture | Med; ~30–40 GPU-h | Partly (one dataset) |
| R2 | Reproducibility and protocol: hyperparameters, compute, code, test split, selection, scope of pretraining data | R1-W4/W5, R4-W1, DA-M7 | §4, App. C | Hyperparameter and compute table; state selection split; exclude evaluation-period clips from pretraining and report the delta; release anonymized code | Low–Med; ~20 GPU-h | Yes (table); Partly (rerun) |
| R3 | Claims exceed evidence ("resilience", "robustness", "arbitrary placement", "synergy", "best overall") | R1-W2/W3, R4-W2, DA-M3/M4, ERR-4 | Abstract, §4.1–4.3, App. D.1 | Report relative degradation and paired-bootstrap CIs; reword claims to Tables 1–8 | Low | Yes |
| R4 | Spatial reconstruction objective not shown to be non-trivial or useful | DA-M2, R2-W3 | §3.1–3.2, Table 8 | Node-level masking for the spatial target or report spatial loss vs masking fraction; test removing it with Node-Drop masking | Med; ~15 GPU-h | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Unseen-placement evidence: one scene, reused embeddings | R1-W2c, DA-M3, R3-Q1 | Leave-one-scene-out across six scenes; different node counts; baselines given the same protocol | High; ~60 GPU-h | No |
| S2 | Theory: state assumptions; do not claim a ranking; link to a measurable quantity | R2-W3, DA-M6, R4-W4 | Rewrite propositions as interpretations or add an empirical test | Low | Yes |
| S3 | Closest sensing/geometry MAEs cited but not compared; novelty differentiation; §2/§3.1 contradictions (LEGO, NeRF, [70] `[verify]`) | R2-W1/W2 | Add [15]/[43]/coordinate-encoding MAE baselines; rewrite §2/§3.1 | Med | Partly |
| S4 | Reference points: supervised-from-scratch, centroid, classical/domain locator (e.g., a multi-station transformer for earthquake location, [54] and Münchmeyer et al.) | R1-W6, R3-W3 | Add rows to Tables 1 and 3 | Med | Partly |
| S5 | Table 6 anomaly and Table 2 near-zero baselines | R1-W2b, DA-M5 | State where message drop is applied; check baseline heads and training curves | Low–Med | Yes |
| S6 | Catalog range typos/cleaning (900.0 magnitude, 30,000 km depth); Table 2 caption; HAR sensor positions text | R1 ERR-1/3, DA-M8 | Correct and state cleaning | Low | Yes |
| S7 | Per-sample normalization and scale; coordinate-noise sensitivity; synchronization | R3-W2 | Ablation with scale input and a noise sweep | Med; ~15 GPU-h | Partly |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Move Tables 7–8 to the main text; shorten §3.3 | R4-W3 | Reorganize |
| N2 | Centralized fusion vs distributed premise: cost and bandwidth | R3-W1 | Report params/FLOPs/latency; a gateway-fusion variant |
| N3 | Dual-use/privacy statement for the border-defense example and the audio/GPS data | R3-W4 | Add an impact paragraph and a data-consent note |
| N4 | Node-Balanced Masking called "slight improvement" within noise; PhyMask family label; MSE definition | DA-m4, ERR-2 | Reword; define metrics |
| N5 | Helpful references: Kriformer (arXiv 2409.14906); Point-MAE `[verify]` | R2 | Cite if relevant |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 65–75 GPU-hours plus a week of writing and protocol reporting.
- Priority 2: 7 items, roughly 90–110 GPU-hours (S1 dominates).
- Priority 3: 5 items, a few days of writing.
- **Total estimated revision time**: about 3–4 weeks including the new runs. ICLR allows revised PDFs during the discussion period, so P1 R2/R3 and the writing items can be done in the rebuttal window, and R1/R4 partly.
