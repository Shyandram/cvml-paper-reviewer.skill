# Academic Paper Review: "A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency"

*Simulated panel review (skill v2.10.1, full mode, target venue ICLR, literature check: strict, cutoff 2025-09-24). Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction of any real decision. The five reviewer passes were run one after another in a single model context (not independent agents); Phase 1 reports were written without reference to one another. Figures were not available: figure-dependent claims are judged from captions and text only and marked as such.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency |
| Primary Discipline | Computer Vision → stereo matching / disparity estimation (iterative, RAFT-style) |
| Secondary Discipline(s) | Signal processing (wavelet / frequency decomposition), recurrent architectures |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Haar DWT of the left image; U-shaped high-frequency feature extractor; attention-based iterative frequency adapter (IFA); LSTM-style update operator (HP-LSTM); plugged into RAFT-Stereo and MonSter |
| Target Venue | ICLR 2026 (stated by user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | None. ICLR: ~27% accepted share of submissions; public reviews; revised PDF possible in discussion |
| Paper Maturity | Submission-ready draft with visible rough edges (reference errors, inconsistent tables) |
| Ethics-Relevant Content | None (public synthetic and driving benchmarks) |
| Input limits | Text extracted from PDF; **figures (Fig. 1–13) not available**; table colour marks (best / second best) not extractable |

### Claimed Contributions (as stated by the authors)
1. **C1 (finding / problem).** EPE of RAFT-Stereo "converge inconsistently in the low and high frequency regions", causing high-frequency degradation (Abstract; §1; Fig. 1(a); App. B.2; Table 3).
2. **C2 (explanation).** The cause is that the single GRU "optimizes all frequency components together without distinguishing between high and low frequencies" (Abstract; §1).
3. **C3 (method).** Wavelet-Stereo: explicit Haar-DWT decomposition, two multi-scale frequency feature extractors, and a High-frequency Preservation Update operator (HPU = IFA + HP-LSTM) (§3.2–3.4; Eq. 1–4, 10).
4. **C4 (efficiency / convergence).** The framework can "significantly accelerate the speed of network convergence": 8 iterations beat RAFT-Stereo, "reducing runtime by 38.6%" (§4.3, Table 6).
5. **C5 (result).** Plug-and-play on iterative methods; new SOTA on Scene Flow; rank 1st on KITTI 2012 / 2015 leaderboards "for almost all metrics" (§4.2, Tables 1–2).

## Paper memory (shared with all reviewers; factual, not judgment)

- **Setup facts.** Train: Scene Flow pretrain, batch 8, 200k iterations, crop 320×736, 2×A6000, AdamW (§4.1); "Adam" in App. B.1. Ablations: batch 6, 100k steps (§4.1). Iterations 22 train / 32 eval (§4.1). Haar DWT with n_i = 3 levels (§3.2). IFA rounds n_j: not stated for headline models (Table 5 sweeps 1–6). ETH3D finetune: 300k + 90k steps on a mixture (§4.2); KITTI finetune: KITTI 2012+2015 mix, batch 8, 50k steps (§4.2). Seeds / runs: not stated after search. Hyperparameter selection split: not stated after search; ablations run on "Scene Flow test set" (Table 4 caption). Code: "will provide" (Abstract). Compute: App. Table 8 (batch 1, 16 iterations, A6000).
- **Headline numbers and sources.** Scene Flow EPE 0.46 (Wavelet-RAFT) / 0.36 (Wavelet-MonSter) vs 0.53 / 0.37 baselines (Table 1). Table 3 region EPE (Wavelet-RAFT 26.48 / 0.56; Wavelet-MonSter 23.42 / 0.44). ETH3D Bad1.0 Noc 0.44 vs MonSter 0.46 ("4.4%"). KITTI leaderboard numbers (Table 2). "38.6%" runtime reduction (Table 6).
- **Appendix adds.** Dataset and metric definitions (A); Canny region protocol for Table 3 (B.2: Canny lower=100, upper=200 "on ground truth (GT) images"); LSA/HSA and HP-LSTM equations (B.3, Eq. 8–10); DWT-level ablation Table 7; per-stage cost Table 8; qualitative figures incl. failure cases (Figs. 8–13); limitations (E).
- **Unverifiable.** All figures, including Fig. 1(a) (the only direct evidence for C1/C2); table colour marks; any garbled symbols in Eq. 1–2.

## Integrity scan (Hard Rule 9)

`scripts/integrity_scan.py --paper … --redact reviewer_copy.txt`: **no reviewer-directed text or hidden characters found.** No injected instructions were noticed while reading. Nothing to report to the EIC. The reviewers read the (identical) redacted copy.

## Literature check status (Phase 1.5)

Mode: **strict, cutoff 2025-09-24**. Fingerprint written. Query attempts: 3 (one refused by the self-exclusion filter for containing the method name; two claim queries, `--tag C2` and `--tag C3`, were executed). **Both executed queries failed with "arXiv API unreachable (HTTP 429)"; 0 results kept, 0 scouted, `similarity` and `novelty` not runnable.** Per `references/literature_search.md`, the check falls back to *off*: missing references below come from the reviewer's knowledge and are marked `[verify]`; no novelty verdict is "known", and "no close prior work found" cannot be claimed from this search. Gaps left open: all claims, benchmark scouting (KITTI), expansion round.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Leona Marchetti-Adeyemi, senior faculty, vision and learning group, large public university (Europe)
- **Seniority / Expertise**: senior / dense prediction, geometry-aware learning, area-chair experience
- **Role**: reads all five reviews, checks decisive points against the paper, weights reviewers, decides
- **Style**: trusts verified arithmetic over rhetoric; asks whether the contribution outweighs ordinary weaknesses

### Reviewer 1 (Methodology): Dr. Mei-Lan Pereira, industrial perception lab, autonomous driving (East Asia)
- **Seniority / Expertise**: senior industry scientist / stereo and optical-flow evaluation, recurrent refinement networks
- **Style**: recomputes every table; insists on matched compute and same-protocol numbers

### Reviewer 2 (Domain): Prof. Rashid Tolonen, vision lab, large public university (Northern Europe)
- **Seniority / Expertise**: senior faculty / stereo matching literature (cost volumes, iterative methods, foundation-model priors)
- **Style**: positions every claim against the nearest prior method; reads the bibliography

### Reviewer 3 (Perspective): Dr. Sunita Azevedo-Brandt, computational imaging group, public university (South Asia)
- **Seniority / Expertise**: mid-career / wavelets and multiresolution analysis, embedded vision
- **Style**: constructive; looks for connections to signal processing and deployment realities

### Reviewer 4 (Generalist): Dr. Jonas Whitcombe, representation-learning lab, private university (North America)
- **Seniority / Expertise**: mid-career / general deep learning for vision, not stereo specialist
- **Style**: typical program-committee member; asks whether a non-specialist can follow

### Devil's Advocate: Dr. Oluwaseun Ferreira-Nakamura, evaluation-methodology group, industry lab (Africa / Latin America)
- **Seniority / Expertise**: senior / evaluation methodology, causal attribution in ablations
- **Style**: rigorous, never hostile; tests whether the evidence proves the stated cause

*Personas are fictional. Assumptions: venue ICLR (stated), paper type empirical.*

---

# Phase 1: Independent Reports

---

# Peer Review Report (Reviewer 1: Methodology)

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Reviewer: Dr. Mei-Lan Pereira, Methodology Reviewer (industrial perception lab, East Asia; fictional persona)
## Expertise: stereo / flow evaluation protocols; recurrent refinement; compute-matched comparison
## Date: 2026-11-10

## Summary
The paper argues that RAFT-style stereo networks refine edge (high-frequency) and smooth (low-frequency) regions at different rates, and attributes this to a single GRU updating all frequencies jointly. It adds a Haar-DWT branch on the left image, a U-shaped high-frequency feature extractor, an attention-based adapter (IFA) and an LSTM-style update (HP-LSTM). It reports gains on Scene Flow, ETH3D and first place on the KITTI leaderboards when the module is added to MonSter, plus faster convergence when added to RAFT-Stereo.

**Protocol sweep.** Searched for test / validation / held-out / selected / tuned / best / checkpoint terms in the full text and appendix. Findings: Table 4 caption: "Ablation study of the effectiveness of proposed modules on Scene Flow test set."; §4.3 selects "a clear peak at r=4 iterations" (Table 5); Table 7 marks 3-level DWT as "(Ours)". No validation split is mentioned anywhere; the split used for choosing n_j, n_i and the Canny thresholds is **not stated after search**, and the evidence points to the Scene Flow test split.

## Claim-to-evidence map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | EPE converges inconsistently in high / low frequency regions | Abstract, §1 | Fig. 1(a) (unavailable); Table 3 final EPE only; no per-iteration data in text | Unverifiable from text; Table 3 not reconcilable with Table 1 (ERR-1) |
| C2 | Joint optimisation by one GRU is *the* reason | Abstract, §1 | None beyond the method working; no control separating "frequency separation" from "more context capacity" | Unsupported (mechanism asserted, not tested) |
| C3 | Wavelet decomposition + HPU helps | §4.3 Tables 4–5, 7 | Ablations on Scene Flow, single runs; key controls missing | Partially supported |
| C4 | Faster convergence, 38.6% less runtime | §4.3 Table 6 | Compares 8-iter Wavelet-RAFT to 32-iter RAFT-Stereo only | Overstated (ERR-4) |
| C5 | SOTA; plug-and-play | Tables 1–2 | Margins over MonSter of 0.01 EPE / 0.02–0.04 on KITTI; two backbones | Partially supported |

## Strengths

### S1: Strong headline leaderboard result
Table 2 places Wavelet-MonSter at or above every listed method on most KITTI 2012 / 2015 and ETH3D columns, e.g. KITTI 2012 Out-3 All 1.07 vs 1.09 for MonSter and 1.18 for DEFOM-Stereo. Leaderboard submissions are externally evaluated, which removes a class of test-set concerns for these numbers.

### S2: Method applied to two different backbones
Table 1 reports the module on RAFT-Stereo (0.53 → 0.46) and MonSter (0.37 → 0.36), supporting the generality claim in part; the RAFT-Stereo gain is not small.

### S3: Useful ablation structure and cost disclosure
Table 4 (modules), Table 5 (IFA rounds), Table 7 (DWT levels) and App. Table 8 (per-stage memory / params / ms) are the right kinds of analyses; the limitations section (App. E) honestly states the compute overhead, and Fig. 13 shows failure cases.

### S4: Simple, interpretable preprocessing
A parameter-free Haar DWT (§3.2, n_i = 3) is cheap (33.31 ms, Table 8) and gives a clear definition of "high-frequency" input, in contrast to learned frequency selection.

## Weaknesses

### W1: The motivating diagnosis (C1/C2) is not supported by comparable, reproducible measurements
(a) Table 3 reports EPE of 34.00 (high-frequency region) and 0.72 (low) for RAFT-Stereo, but Table 1 gives 0.53 overall for the same model. If the two masks partition the image and EPE is averaged over each mask, the overall EPE must lie between 0.72 and 34.00; 0.53 is outside that range. The same holds for MonSter (low 0.47 vs overall 0.37) and Wavelet-MonSter (0.44 vs 0.36). Under Eq. 6–7 (`EPE_high = M ⊙ EPE_total`) the normalisation is not defined. So the region numbers must come from a different protocol (e.g. different disparity cap, occlusion handling, edge dilation) that is not stated. (b) Edge pixels have larger EPE for geometric reasons (disparity discontinuities, occlusion) independent of any "frequency convergence"; a Canny mask on ground truth "images" (App. B.2; disparity or RGB is not specified) cannot separate these. (c) The convergence claim needs EPE-vs-iteration curves for both regions; the text contains none (Fig. 1 is unavailable and judged by caption only).
- **Suggested Fix**: State the mask source (GT disparity or RGB), normalisation, disparity cap and occlusion handling; report region EPE with the Table 1 protocol so numbers reconcile; add per-iteration region-EPE curves for RAFT-Stereo and Wavelet-RAFT on Scene Flow (≈ 1 GPU-hour of inference), and a control with masks of equal area on non-edge pixels with large disparity.

### W2: Ablations do not isolate wavelet decomposition from added capacity
Table 4 compares against GRU with concatenated features and against a "simple two-layer convolutional network" for Fh (§4.3). Missing controls: (i) the same U-shaped extractor + HPU fed with the raw left image (no DWT) or with a learned high-pass; (ii) IFA on/off (Table 5 starts at j=1, so j=0 is absent); (iii) HP-LSTM vs DLNR's LSTM vs GRU with the same extra features; (iv) Haar vs other decompositions (Laplacian pyramid, Sobel/edge map). Without (i) a skeptic can attribute the gain to a ~7M-parameter extra context path (Table 8: 7.01M for high-frequency extraction) rather than to frequency separation.
- **Suggested Fix**: Add (i)–(iv) on the 100k-step ablation schedule: ≈ 4 runs × ~2 GPU-days each on 2×A6000 (to be confirmed by the authors).

### W3: Numbers for the same model disagree across tables, so ablations cannot be trusted as a set
Wavelet-RAFT EPE is 0.46 (Table 1), 0.52 (Table 4 "Full model"), 0.46 at 32 iterations (Table 6), 0.467 (Table 7, "HPU + HAM3 (Ours)") and 0.367 at j=4 (Table 5). The paper says the ablation setting is "simplified" (§4.3), which would explain Table 4's 0.52 > 0.46, but then Table 5's 0.367 would be a *shorter-trained* model that is far better than the fully trained one and better than every non-MonSter method in Table 1; Table 5's 0.790 s equals Table 6's 32-iteration runtime. Table 7's D1 (6.21) matches Table 4, but its EPE (0.467) does not match (0.52). In Table 7 the text claims "0.77M additional parameters while achieving 2.3% improvements (EPE decreases from 0.483 to 0.472)", but 0.77M is the HAM2→HAM3 step (4.73 → 5.5 M), whose EPE change is 0.472 → 0.467 (1.1%). The RAFT-Stereo baseline also varies (0.62 in Table 4, 0.53 in Tables 1 and 6).
- **Suggested Fix**: Add a table mapping each reported run to (model, schedule, iterations, split, metric) and correct or explain Table 5 / Table 7.

### W4: The speed claim (C4) rests on a favourable baseline row
Table 6: RAFT-Stereo at 12 iterations has EPE 0.53 at 0.22 s; Wavelet-RAFT at 8 iterations has EPE 0.52 at 0.27 s. The "38.6%" is relative to RAFT-Stereo at 32 iterations (0.44 → 0.27 s, recomputed 38.6%). At matched runtime RAFT-Stereo is as good or better, and at 32 iterations Wavelet-RAFT is 1.8× slower (0.79 vs 0.44 s). RAFT-Stereo's EPE is also non-monotonic in iterations (0.53 at 32, 0.63 at 16, 0.53 at 12), which suggests a typo or an unstable measurement. The text calls it "significantly" faster convergence.
- **Suggested Fix**: Plot EPE vs. wall-clock for both models at several iteration counts with the same hardware / batch / precision; correct the 16-iteration row.

### W5: Single-run results with very small margins on the headline model
Wavelet-MonSter vs MonSter: Scene Flow 0.36 vs 0.37 EPE (Table 1); KITTI 2015 D1-all All 1.38 vs 1.41; KITTI 2012 Out-3 Noc 0.83 vs 0.84 (Table 2). No seeds or variance anywhere (omission sweep: not stated). For Scene Flow (4,370 test pairs) a 0.01 EPE difference may be within run-to-run variation; leaderboard gains of 0.01–0.04 are typical of SOTA claims but are not shown to exceed noise. Field norms accept single runs on large benchmarks, so this is MAJOR rather than disqualifying.
- **Suggested Fix**: 3 seeds for Wavelet-MonSter and MonSter on Scene Flow (2 × 3 × 200k iterations; ~ 2× the original cost, verify with authors) or a paired bootstrap over test images.

### W6: Headline model is not described and zero-shot generalisation is claimed without numbers
Wavelet-MonSter produces all leaderboard results, but §3 describes only Wavelet-RAFT (§3.1); how HPU attaches to MonSter's mono-depth branch, its parameters and its runtime are not given. Generalisation: App. A and App. D claim "zero-shot generalization" improvements but only qualitative figures (Figs. 8–11) are shown, no table of Scene Flow → KITTI / Middlebury / ETH3D errors, although Middlebury is described in App. A.
- **Suggested Fix**: Add a Wavelet-MonSter architecture / integration paragraph and params / runtime; add the standard zero-shot table (Scene Flow-trained → KITTI 2012/2015, Middlebury, ETH3D) for RAFT-Stereo vs Wavelet-RAFT and MonSter vs Wavelet-MonSter.

### W7: Hyperparameters chosen on the reported split
Table 5 selects j = 4 and Table 7 selects 3 DWT levels on the Scene Flow test split (Table 4 caption), with no validation split. Both selected values are best-scoring in their tables. The comparison with baselines holds at every swept value in Table 5 (all entries 0.367–0.394 below every baseline EPE in Tables 4/6), so this is a protocol disclosure and not a validity threat to the conclusion.
- **Suggested Fix**: State the split; hold out a slice of the Scene Flow training set (or use FlyingThings subset) for selecting n_j and n_i.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 3 vs Table 1 | "High-frequency region Low-frequency region" (Table 3 header); RAFT-Stereo 34.00 / 0.72; Table 1 RAFT-Stereo 0.53 | Overall EPE lower than the EPE of the low-frequency region alone; impossible if both are averages over a partition of the same pixels | Cross-referenced Tables 1, 3 (also MonSter 0.47 vs 0.37; Wavelet-MonSter 0.44 vs 0.36) | High | MAJOR | State and unify the protocol |
| ERR-2 | E1 | §4.2 | "them by 25.89% and 10.3% in high-frequency regions" | Text order is Selective-IGEV then DLNR; Table 3 gives Selective-IGEV 26.10→23.42 = 10.3% and DLNR 31.60→23.42 = 25.89%. Low-frequency: 13.7% is Selective-IGEV, 30.2% is DLNR | Recomputed | High | MINOR | Swap attribution |
| ERR-3 | E1 / E6 | Table 5 vs Tables 1, 4, 6, 7 | "performance exhibits a clear peak at r=4 iterations" | Table 5 EPE 0.367 at j=4 (0.790 s) vs 0.46 (Table 6, 32 it, 0.79 s), 0.52 (Table 4), 0.467 (Table 7) for the same configuration | Cross-referenced | High | MAJOR | Reconcile or state differing settings |
| ERR-4 | E5 | §4.3 | "Our Wavelet-RAFT need only 8 iterations to surpass the performance of RAFT-Stereo while reducing runtime by 38.6%." | 38.6% holds only vs 32-iteration RAFT-Stereo; RAFT-Stereo at 12 iterations has equal EPE (0.53 vs 0.52, a 0.01 gap) in 0.22 s vs 0.27 s | Recomputed (0.44→0.27 = 38.6%) and cross-referenced Table 6 | High | MAJOR | Report matched-time comparison |
| ERR-5 | E1 | Appendix C | "adds just 0.77M additional parameters while achieving 2.3% improvements" | 2.3% = (0.483−0.472)/0.483 is HAM1→HAM2 (+0.37M); the 0.77M step is HAM2→HAM3 with EPE 0.472→0.467 (1.1%) | Recomputed from Table 7 | High | MINOR | Correct text |
| ERR-6 | E6 | §4.1 vs App. B.1 | "we use the AdamW [26] optimizer" / "all models are trained with the Adam optimizer" | Optimizer defined differently in two places | Cross-referenced | High | MINOR | Unify |
| ERR-7 | E6 | App. A vs §4.2 | "All models in this work are trained exclusively on the SceneFlow training dataset." | §4.2 fine-tunes on ETH3D / KITTI mixtures for leaderboard models | Cross-referenced | High | MINOR | Qualify the sentence |
| ERR-8 | E2 | App. B.3 Eq. 8–9 | "Global Max Pooling (GMP) and Global Average Pooling (GAP) along spatial dimensions" | After global spatial pooling the map is 1×1, so the 7×7 conv in HSA ("processes them through a 7×7 convolutional layer W3 to capture") has no spatial extent to act on | Derived from Eq. 8–9 | Medium | MAJOR (clarity of a core module) | Clarify whether pooling is over channels (CBAM-style) |
| ERR-9 | E8 | Table 6 | RAFT-Stereo row at 16 iterations: EPE 0.63, runtime 0.26 | EPE 0.63 at 16 iterations is worse than at 12 (0.53) and 32 (0.53) | Cross-referenced within Table 6 | Medium | MINOR (possible typo) | Verify the row |

### Minor
Eq. 5 sums over k but the exponent uses i; Table 6 cites RAFT-Stereo as [44] (the ACVNet TPAMI paper) rather than [25]; §4.2 says "GMStereo [37]" but [37] is Selective-Stereo; references [41] and [42] are the same ACVNet entry; "Haar wavelet [31]" cites a diffusion paper; Table 8 caption promises "equivalent FPS" but no FPS column; Table 8 stage times sum to 489.1 ms vs 0.45 s for 16 iterations in Table 6; "r=4" vs "j" notation in §4.3; "VKITTI" appears in Fig. 10 but not in App. A.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Real leaderboard gains, but inconsistent tables and missing controls |
| Clarity | 2 | Headline model undescribed; module equations ambiguous |
| Significance | 2 | Narrow, incremental SOTA margins |
| Originality | 2 | Known pieces (DWT, attention, LSTM update) in a new combination |

## Dimension Scores (0–100)

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central diagnostic claim unverified and internally inconsistent tables; headline gain over the closest prior (MonSter) is 0.01–0.04 on single runs.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Untested causal claim; ERR-1/3/4; ambiguous module equations |
| Clarity & Presentation | 52 | Developing | Reference and notation errors; headline model undescribed |
| Novelty & Originality | 48 | Developing | Assembly of known components; weak differentiation from Selective-Stereo / DLNR |
| Significance & Impact | 52 | Developing | Leaderboard #1 is genuine but margins are tiny |
| Experimental Validation | 44 | Developing | Missing controls, no variance, no zero-shot numbers, speed claim cherry-picked |
| Reproducibility | 50 | Developing | Code "will be provided"; n_j, U-Net layout, MonSter integration missing |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations section present but short |

## Questions for Authors
1. What exactly are the masks and normalisation behind Table 3, and why is RAFT-Stereo's low-frequency EPE (0.72) above its overall EPE (0.53)? A reconciled table would raise my Experimental Validation score.
2. What configuration produces Table 5's 0.367 at j=4, and why does it differ from 0.46 (Table 6, 32 iterations)?
3. Does the gain survive when the same U-shaped extractor is fed the raw RGB left image instead of DWT sub-bands? A negative answer would lower my Novelty score substantially.
4. Is the 16-iteration RAFT-Stereo row of Table 6 correct?
5. How many parameters / how much runtime does Wavelet-MonSter add to MonSter?

## Limitations Assessment
**Partially.** App. E acknowledges compute overhead and shows failure cases (Fig. 13 caption: "Examples of failure cases for the proposed method."), which is commendable. Missing: sensitivity to non-depth texture edges (acknowledged only via the failure-case caption), absence of variance, and dependence on a mono-depth foundation prior in the MonSter variant.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A real leaderboard-level result with a plausible, cheap idea, but the diagnostic motivation is unverified, the tables disagree with one another, and key controls are missing; these are fixable but need new experiments.

## Confidence
**4**: Recomputed all headline deltas and cross-referenced Tables 1, 3–8; figures unavailable.

---

# Peer Review Report (Reviewer 2: Domain)

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Reviewer: Prof. Rashid Tolonen, Domain Reviewer (vision lab, large public university, Northern Europe; fictional persona)
## Expertise: stereo matching literature; iterative / RAFT-based methods; foundation-model priors
## Date: 2026-11-10

## Summary
The submission proposes injecting wavelet-derived high-frequency context into the update operator of RAFT-style stereo networks, and reports state-of-the-art KITTI / ETH3D results when combined with MonSter. Its positioning is against two prior frequency-motivated iterative methods: Selective-Stereo (selective receptive fields in the GRU) and DLNR (LSTM decoupling of the hidden state).

## Strengths

### S1: A clear, physically interpretable alternative to learned frequency selection
§2 criticises Selective-Stereo-style methods because they "lack interpretability in their learned decomposition patterns" and DLNR for a hidden state with no "clear physical definition"; replacing these with an explicit Haar DWT (§3.2) is a well-motivated, simple direction.

### S2: Comparison set includes the right recent iterative methods
Table 2 covers IGEV, Selective-IGEV, NMRF-Stereo, LoS, DEFOM-Stereo and MonSter (CVPR 2024–2025), and Table 3 compares directly with Selective-RAFT / Selective-IGEV / DLNR on a frequency-split analysis, which is the right closest-prior comparison.

### S3: Practical value in a competitive sub-field
Reaching first place on two KITTI leaderboards against a very strong 2025 baseline is meaningful for stereo practitioners, and the module is a modest 6–7M-parameter addition (Table 8).

### S4: Positioning around a nameable problem
Defining "frequency convergence inconsistency" gives a testable lens on RAFT-style refinement even though the evidence (C1) needs strengthening.

## Weaknesses

### W1: Novelty over Selective-Stereo and DLNR is modest and weakly differentiated
The three ingredients (separating a high-frequency stream; attention gating of features; an LSTM-type update to preserve detail) are each present in the cited work: DLNR already "replaces the GRU with an LSTM to retain more high-frequency information" (§1), and Selective-Stereo already routes frequency-selective features into the update. What is new is the *source* of the high-frequency signal (Haar sub-bands of the left image) and the IFA alternation (Eq. 1–2). Table 3 shows Selective-IGEV (26.10) and MonSter (26.08) almost tie in high-frequency EPE, so the frequency claim is not unique to the proposed module. The differentiation is asserted ("lacks a clear physical definition") rather than tested.
- **Suggested Fix**: A table isolating the three differences (frequency source; adapter; LSTM) against Selective-Stereo and DLNR under identical backbones; state clearly which claim is new.

### W2: Missing related work on wavelet / frequency decomposition in stereo and low-level vision
The related-work paragraph on frequency methods (§2) cites octave convolution, HiLo attention and learning-in-frequency-domain works, but not prior wavelet-based stereo (see Missing References) nor wavelet CNNs from restoration where DWT-branch / feature-fusion designs are well studied. The claim "its utilization in the field of stereo matching remains relatively limited" needs checking against that line of work.
- **Suggested Fix**: Add and differentiate (see list); soften "limited".

### W3: Baseline table is incomplete for the claim "best among all published approaches"
§4.2: "achieves the best performance among all published approaches to date". Table 2 omits IGEV++ (TPAMI 2025, same group as IGEV/Selective-Stereo) and foundation-model stereo methods (see Missing References); and on KITTI D1-fg (Noc / All) DEFOM-Stereo scores 2.24 / 2.23 against 2.60 / 2.60 for Wavelet-MonSter. Foreground is where thin / fine objects would show the claimed benefit, so the one metric closest to the thesis is *not* a win. Scene Flow Table 1 omits Selective-IGEV and DLNR, which the paper itself evaluates in Table 3 (Selective-IGEV's reported Scene Flow EPE is lower than Wavelet-RAFT's 0.46, to my recollection [verify]).
- **Suggested Fix**: Add rows and temper the wording to "best on most metrics".

### W4: Generalisation claim directed at prior work is unsupported
§2 states Selective-Stereo "demonstrate limited generalization capability across diverse datasets" without evidence or citation; the paper then claims its own "zero-shot generalization" improvement only qualitatively (Figs. 8–11).
- **Suggested Fix**: Provide the zero-shot table or delete both claims.

### W5: Citation errors weaken the positioning
Table 6 cites RAFT-Stereo as [44] (ACVNet, TPAMI); §4.2 "GMStereo [37]" points to Selective-Stereo; [41] and [42] duplicate ACVNet; "Haar wavelet [31]" cites a diffusion-model paper rather than a DWT source; MonSter and DEFOM-Stereo are cited as arXiv preprints [6], [20] but labelled "CVPR 2025" in Table 2 (that label is plausible from my knowledge but the bibliography does not support it).
- **Suggested Fix**: Audit the bibliography.

### Missing References
*Literature check unavailable (arXiv API HTTP 429; no results kept). All entries come from knowledge and are marked `[verify]`; none is a required comparison on the strength of this search alone.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | M. Yang, F. Wu, W. Li. "WaveletStereo: Learning Wavelet Coefficients of Disparity Map in Stereo Matching." CVPR 2020 `[verify]` | Wavelet-based stereo network (predicts wavelet coefficients of disparity); different mechanism, but the paper's statement that wavelets in stereo are rare should address it |
| Important | G. Xu, X. Wang, Z. Zhang, J. Cheng, C. Liao, X. Yang. "IGEV++: Iterative Multi-range Geometry Encoding Volumes for Stereo Matching." IEEE TPAMI 2025 `[verify]` | Strongest follow-up of IGEV from the same line as Selective-Stereo; relevant to "best among all published" |
| Helpful | B. Wen, M. Trepte, J. Aribido, J. Kautz, O. Gallo, S. Birchfield. "FoundationStereo: Zero-Shot Stereo Matching." CVPR 2025 `[verify]` | Foundation-model stereo; relevant to zero-shot / generalisation framing |
| Helpful | L. Bartolomei, F. Tosi, M. Poggi, S. Mattoccia. "Stereo Anywhere: Robust Zero-Shot Deep Stereo Matching Even Where Either Stereo or Mono Fail." CVPR 2025 `[verify]` | Mono-prior stereo, related to the MonSter backbone choice |

### Novelty delta table (from the paper's own related work and knowledge; no literature check)

| Claimed contribution | Closest prior work | What it already does | What is actually new | Cited and differentiated? |
|----------------------|--------------------|----------------------|----------------------|---------------------------|
| C3 high-frequency stream into the update operator | Selective-Stereo [37]; DLNR [51] | Frequency-aware GRU / LSTM-decoupled hidden state | Haar sub-band input + IFA alternating attention | Cited; differentiated by assertion (§2) |
| C3 wavelets in stereo | WaveletStereo (CVPR 2020) `[verify]` | Wavelet representation of disparity | Wavelets on image side for context | Not cited |
| C1 frequency convergence diagnosis | None identified (no search result; arXiv-only search failed) | n/a | Region-wise EPE view of iterative methods | n/a (verdict at most *medium*) |

*Per-claim novelty (typed from the Methodology Reviewer's map; search unavailable):* C1 problem/finding: medium (no close prior work known to me; not a search result). C3 method: incremental (assembly of cited mechanisms). C5 result: result-type claim, attribute-value (KITTI ranks) not "known".

**Baseline scout (not runnable).** Benchmark KITTI scouted by knowledge only: the missing comparison candidates are listed above; neither is a required baseline on this search.

**Field snapshot (knowledge, ≤ cutoff).** Iterative stereo (RAFT-Stereo 2021 → IGEV 2023 → Selective / DLNR 2023–24) has saturated KITTI at D1-all ≈ 1.3–1.5%; the recent step changes came from priors (monocular depth / foundation models: MonSter, DEFOM-Stereo, FoundationStereo) rather than refinement operators. A +0.03 D1 gain on KITTI is incremental; what counts as significant now is a new capability (robust zero-shot, thin structures at range) or a large efficiency gain at equal accuracy. This calibrates Significance to *moderate* and Novelty to *incremental*.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good SOTA table; inconsistent ablations |
| Clarity | 2 | Positioning partly asserted; citation errors |
| Significance | 3 | Leaderboard result matters to the sub-field |
| Originality | 2 | Combination of known mechanisms |

## Dimension Scores (0–100)

**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental novelty over Selective-Stereo / DLNR and tiny margins over MonSter, partly offset by a genuine KITTI #1 in a competitive sub-field.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Sound idea; unclear module description |
| Clarity & Presentation | 54 | Developing | Positioning partly asserted; bibliography errors |
| Novelty & Originality | 50 | Developing | Incremental assembly |
| Significance & Impact | 56 | Competent | Real leaderboard result; narrow margins |
| Experimental Validation | 50 | Developing | Missing baselines / zero-shot numbers |
| Reproducibility | 52 | Developing | Promised code only |
| Ethical Compliance | 62 | Competent | No issues |

## Questions for Authors
1. How does the method differ, empirically, from Selective-Stereo and DLNR at the same backbone? (A table with matched settings would raise Novelty.)
2. Is prior wavelet-based stereo work relevant to your claim that frequency-domain use in stereo is limited?
3. Why is DEFOM-Stereo better on D1-fg if the method targets thin / fine structures?
4. Can you report Selective-IGEV / DLNR in Table 1?

## Limitations Assessment
**Partially.** Overhead acknowledged (App. E); the dependence of the headline model on MonSter's mono-depth prior and the narrow margin over it are not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A competent engineering contribution in a mature sub-field; novelty is incremental and differentiation from the two nearest methods is asserted, not shown.

## Confidence
**4**: Know the stereo literature well; literature check could not be run, so some references are `[verify]`.

---

# Peer Review Report (Reviewer 3: Perspective)

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Reviewer: Dr. Sunita Azevedo-Brandt, Perspective Reviewer (computational imaging group, public university, South Asia; fictional persona)
## Expertise: wavelets and multiresolution analysis; embedded vision
## Date: 2026-11-10

## Summary
The paper brings multiresolution signal analysis into recurrent stereo matching: a Haar decomposition separates edge-bearing sub-bands from the smooth approximation, and the update operator is conditioned on adaptively refined high-frequency features. The result is competitive-to-leading on KITTI and Scene Flow at a modest parameter cost.

## Strengths

### S1: A principled link to classic multiresolution analysis
Using a fixed Haar DWT (§3.2, 3 levels) rather than learned filters gives an invertible, parameter-free split and ties the work to decades of wavelet theory; it is cheap (33.31 ms in Table 8).

### S2: Plug-in nature fits deployment pipelines
The module attaches to RAFT-Stereo and MonSter without changing the correlation volume (Alg. 1 vs 2), which is attractive for practitioners who already run these models, and the authors measure runtime and memory per stage (Table 8).

### S3: The edge / smooth-region framing is practically relevant
Thin structures at range matter in driving and robotics (§1 motivates with autonomous driving [48] and manipulation [18]); the Canny-split evaluation (App. B.2) is a useful idea for diagnosing where iterative refinement fails, even if the protocol needs tightening.

### S4: The iteration-efficiency result is a real engineering benefit
Table 6 indicates Wavelet-RAFT reaches comparable EPE with fewer iterations (8 vs 32), and the authors promise a real-time variant.

## Weaknesses

### W1: "Frequency" is used loosely; image high-frequency ≠ disparity edges
The method decomposes only the *left RGB image* (§3.2) and the failure-case caption (Fig. 13) attributes failures to "extraction of task-irrelevant information" (texture edges that are not depth edges). The evaluation masks are Canny edges on ground truth (App. B.2), i.e. depth-discontinuity regions, while the method feeds image-texture frequencies; the two coincide only partly. A signal-processing reading would also expect the *right* image or the correlation volume to be decomposed, since matching ambiguity arises there.
- **Suggested Fix**: Report region analysis for texture-edge vs. depth-edge pixels separately; try decomposing the cost volume / both images; discuss aliasing and Haar's limited directional selectivity (alternatives: shearlets, steerable pyramids `[verify]` as lines of work).

### W2: Deployment realism: real-time and memory
Wavelet-RAFT at 32 iterations takes 0.79 s vs 0.44 s (Table 6); the headline Wavelet-MonSter runtime / memory is not reported, and the promise of a "real-time version" is future work (§5). For driving and robotics claims (§1) a measured latency at KITTI resolution on embedded hardware is the key number.
- **Suggested Fix**: Report params / FLOPs / latency for Wavelet-MonSter and a lighter variant; add an accuracy-vs-latency Pareto plot.

### W3: Robustness beyond benchmarks is untested
Benchmarks are KITTI, ETH3D (gray-scale) and Scene Flow; there is no evaluation under noise, blur, weather or other sensor shift, where high-frequency features are expected to be *most* fragile (noise lives in high-frequency sub-bands).
- **Suggested Fix**: Evaluate with synthetic corruptions (noise, blur, JPEG) on KITTI-train and report degradation for baseline vs. proposed.

### Missing connections (suggestions; entries `[verify]`)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Helpful | P. Liu, H. Zhang, K. Zhang, L. Lin, W. Zuo. "Multi-level Wavelet-CNN for Image Restoration." CVPR Workshops 2018 `[verify]` | DWT as a lossless downsampling / feature-fusion layer; informs the multi-level design |
| Helpful | S. E. Finder, R. Amoyal, E. Treister, O. Freifeld. "Wavelet Convolutions for Large Receptive Fields." ECCV 2024 `[verify]` | Wavelet-domain convolutions as an efficient architecture block |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid evidence on benchmarks; some loose ends |
| Clarity | 3 | Readable method; notation rough |
| Significance | 3 | Useful to stereo practitioners |
| Originality | 3 | Fresh combination for the stereo setting |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a well-motivated plug-in with benchmark-leading KITTI numbers; offset by loose frequency definitions and no deployment numbers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 61 | Competent | Sound approach; weak diagnostics |
| Clarity & Presentation | 60 | Competent | Understandable with effort |
| Novelty & Originality | 60 | Competent | Meaningful transfer of wavelets to recurrent stereo |
| Significance & Impact | 65 | Competent | Practical value; benchmark-leading |
| Experimental Validation | 60 | Competent | Standard benchmarks and ablations; gaps |
| Reproducibility | 56 | Competent | Code promised, not released |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations stated |

## Questions for Authors
1. Is the benefit concentrated on depth-edge pixels or on texture-edge pixels? (An answer showing depth-edge gains would raise my score.)
2. What is the latency of Wavelet-MonSter at KITTI resolution?
3. Does the module help under noise / blur?

## Limitations Assessment
**Partially.** App. E notes the compute overhead; robustness and sensor shift are not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: A principled, useful plug-in with leaderboard-level results; weaknesses (loose frequency definition, no deployment numbers) are typical of papers at the borderline.

## Confidence
**3**: Strong on wavelet analysis, less on stereo-specific protocols; did not check every table.

---

# Peer Review Report (Reviewer 4: Generalist)

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Reviewer: Dr. Jonas Whitcombe, Generalist Reviewer (representation-learning lab, private university, North America; fictional persona)
## Expertise: general deep learning for vision
## Date: 2026-11-10

## Summary
The paper claims iterative stereo networks lose high-frequency (edge, thin-object) accuracy during refinement because a single GRU treats all frequencies alike. It decomposes the left image with a Haar wavelet, extracts high- and low-frequency features separately, and conditions an LSTM-style update on adaptively gated high-frequency features. It reports leading results on KITTI 2012/2015 and ETH3D (with MonSter as the base), better Scene Flow EPE and faster convergence on RAFT-Stereo.

## Venue criteria checklist (ICLR: Soundness, Presentation, Contribution)
| Criterion | Status | Location |
|-----------|--------|----------|
| Claims supported by evidence | Partly: leaderboard claims supported, causal diagnosis not | §1 vs Table 3; Fig. 1 (unavailable) |
| Soundness of method description | Partly: Wavelet-MonSter undescribed; Eq. 8–9 unclear | §3, App. B.3 |
| Presentation | Partly: many reference/notation errors | References [31], [41]/[42], [44]; Eq. 5 |
| Contribution to ICLR audience | Partly: a specialised vision application with limited broader insight | §5 |
| Reproducibility | Not met: code promised only | Abstract |

## Strengths

### S1: Clear, well-motivated storyline
§1 builds a readable narrative (the problem in RAFT-style updates → two prior fixes → the explicit frequency split), and Algorithms 1–2 make the change to a standard iterative pipeline easy to see.

### S2: Strong headline numbers
Table 2 shows Wavelet-MonSter ahead of 12 listed methods on most columns, and Table 1 gives new best Scene Flow EPE (0.36).

### S3: Honest cost and failure disclosure
App. Table 8 and App. E acknowledge that DWT, multi-scale extraction and IFA add overhead; Fig. 13 provides failure cases (caption only judged).

### S4: Reasonable ablation set
Tables 4, 5 and 7 test modules, IFA rounds and DWT levels.

## Weaknesses

### W1: The main method is hard to follow in several places
(i) Eq. 1–2 alternate which stream is updated by index parity of j, yet it is not said which F_l (before or after IFA) enters the LSTM in Eq. 3, and Eq. 3 uses `F_h^{k-1}` while §3.4 says `F_h^{i,0,k} = F_h^{i,0,k-1}`. (ii) In Eq. 10 the cell state is replaced by F_h (`ct = ft ∗ Fh + it ∗ gt`), so it is unclear how information is "preserved" across iterations. (iii) §3.4 uses j and §4.3 uses r for the same count. (iv) Fig. 5(e) / Fig. 3 are the only description of the multi-level structure and were not available to me; this is noted as a limitation of my reading, not a flaw in the paper. (v) The headline Wavelet-MonSter is never described.
- **Suggested Fix**: A per-iteration pseudo-code of HPU with tensor shapes, and a paragraph on the MonSter integration.

### W2: Presentation errors that distract from the contribution
References: Table 6 cites RAFT-Stereo as [44]; "GMStereo [37]" is Selective-Stereo; [41] = [42]; Haar wavelet cited to a diffusion paper [31]. Numbers: §4.2 swaps which percentage belongs to Selective-IGEV and DLNR (25.89% is DLNR, 10.3% is Selective-IGEV; recomputed from Table 3). These do not hide the contribution but reduce confidence in the numbers.
- **Suggested Fix**: Audit references and recompute all percentages.

### W3: Contribution is narrow for ICLR's general audience
The paper is a stereo-specific architecture tweak; its broader message (separating frequency components in recurrent refinement) is not tested beyond two stereo backbones, and no other iterative task (optical flow, e.g. the same RAFT family) is tried despite "plug-and-play into multiple iterative-based methods".
- **Suggested Fix**: Show one non-stereo recurrent task (optical flow) or one more stereo backbone (IGEV), or reframe the claim narrowly.

### W4: Efficiency framing is selective
The headline "38.6%" (Table 6) compares 8-iteration Wavelet-RAFT to 32-iteration RAFT-Stereo; RAFT-Stereo at 12 iterations has the same EPE (0.53 vs 0.52) at 0.22 s vs 0.27 s. A generalist reader would take the statement at face value.
- **Suggested Fix**: Add a matched-time comparison.

### Minor
Typos ("franework", "show in Fig.2", "Traditional terative framework", "resulting high frequency degradation"); Table 5 "0.865s" units inconsistent with other rows; Fig. 10 mentions VKITTI not described in App. A; Table 2 colour marks are not recoverable in text.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Strong benchmark but internal inconsistencies |
| Clarity | 2 | Method details and bibliography need work |
| Significance | 2 | Narrow audience |
| Originality | 2 | Incremental recombination |

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: solid leaderboard result but a specialised, incremental contribution presented with several visible errors; presentation is at the weaker end of ICLR submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Method plausible; some details unclear |
| Clarity & Presentation | 48 | Developing | Many errors; undefined integration |
| Novelty & Originality | 52 | Developing | Incremental |
| Significance & Impact | 56 | Competent | Good results for the sub-field |
| Experimental Validation | 52 | Developing | Benchmarks fine; no variance / zero-shot numbers |
| Reproducibility | 50 | Developing | Code promised |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. What does the HPU look like inside MonSter, and what is its added cost?
2. Does the idea transfer to optical flow (RAFT) or IGEV?
3. Which of the Table 3 numbers uses the same protocol as Table 1?

## Limitations Assessment
**Partially.** App. E is honest but brief.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A good empirical result in a narrow area, presented with enough errors and missing detail that I would not champion it; rewrite and extra controls could move it to Borderline Accept.

## Confidence
**4**: Read the whole paper; not a stereo specialist.

---

# Devil's Advocate Report

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Reviewer: Dr. Oluwaseun Ferreira-Nakamura, Devil's Advocate (evaluation-methodology group, industry lab; fictional persona)

---

## Steelman
RAFT-style stereo refines a hidden state that increasingly encodes global, low-frequency structure; edges and thin objects suffer. Injecting an explicit, parameter-free wavelet decomposition of the image into the update step gives the network a dedicated path for fine detail. The module improves two different backbones and ends with first place on both KITTI leaderboards, which is hard to dismiss.

---

## Core Argument Chain
1. P1: In RAFT-Stereo, EPE in high-frequency regions converges differently from low-frequency regions (Fig. 1(a); Table 3).
2. P2: The cause is a single update operator optimising all frequencies jointly (Abstract; §1).
3. P3: Therefore giving the update operator explicit high-frequency features (DWT + IFA + HP-LSTM) removes the inconsistency.
4. P4: The resulting model improves accuracy on benchmarks and converges faster (Tables 1, 2, 4, 6).
∴ The inconsistency is the underlying reason for limited iterative performance, and the proposed framework solves it.

---

## Strongest Counter-Argument
Even if every benchmark number is taken at face value, the paper does not show P1→P2→P3. The only evidence that "frequency convergence inconsistency" exists is a figure (not available here) and Table 3, whose region EPEs cannot be reconciled with Table 1: RAFT-Stereo's low-frequency EPE (0.72) exceeds its overall EPE (0.53), which is arithmetically impossible if both are means over a partition of the same pixels. Edge pixels naturally carry larger error (depth discontinuities, occlusions), so a higher EPE at edges is not by itself "inconsistent convergence". No experiment tracks region EPE across iterations for the baseline and the proposed model; P2 (cause) is never tested by an intervention that changes *only* the frequency separation. The gains are equally explained by a simpler hypothesis: an additional ~7M-parameter, U-shaped context branch (Table 8) with extra high-resolution detail (a 3-level wavelet pyramid of the left image) helps any RAFT-style update, frequency-specific or not. The decisive control — feed the same branch the raw image or a non-wavelet high-pass — is absent (Table 4 only replaces it with a two-layer conv). The same applies to the speed claim: Table 6 shows plain RAFT-Stereo at 12 iterations matching the "faster" model's EPE (0.53 vs 0.52) in less time (0.22 vs 0.27 s). If the gains come from capacity and a strong mono-depth prior (the leaderboard model builds on MonSter), the paper's explanatory framing, and its title, claim more than the evidence shows. The authors should either supply the control and the per-iteration analysis or reframe the work as "an extra high-frequency context branch improves iterative stereo".

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main empirical claim (best-in-table KITTI / ETH3D results with Wavelet-MonSter, Table 2) survives, and the unsupported parts (the causal diagnosis; the speed claim) are weaker-claim cases that can be narrowed rather than contradicted outright by the paper's own evidence.

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / Logic | Abstract; §1; Table 3; Fig. 1(a); App. B.2 | The causal claim ("underlying reason") is asserted, not tested; region EPEs (Table 3) cannot be reconciled with Table 1 (RAFT-Stereo low-frequency 0.72 > overall 0.53); no per-iteration analysis in text. Evidence supports a weaker claim (the module helps), does not contradict it | Narrow the wording or add per-iteration region curves and a reconciled protocol |
| DA-M2 | Alternative explanation | Table 4; §4.3 | No control separating wavelet-based frequency separation from added extractor capacity / U-Net context; Fh ablation replaces it with a two-layer conv only | Same extractor on RGB; learned high-pass; param-matched baseline |
| DA-M3 | Overclaiming (E5) | §4.3 "Our Wavelet-RAFT need only 8 iterations…"; Table 6 | Speed claim holds only against 32-iteration RAFT-Stereo; 12-iteration RAFT-Stereo gives 0.53 at 0.22 s vs 0.52 at 0.27 s; non-monotonic RAFT row (0.63 at 16 it.) | Matched-time curve; correct row |
| DA-M4 | Overclaiming (E5) | Abstract; §4.2 "ranks 1st on both the KITTI 2015 and KITTI 2012 leaderboards for almost all metrics" | Table 2: DEFOM-Stereo beats Wavelet-MonSter on D1-fg (2.24 / 2.23 vs 2.60 / 2.60) — the metric closest to the thesis; wording "best performance among all published approaches to date" ignores IGEV++ and foundation-model stereo not in the table `[verify]` | Narrow wording; add rows |
| DA-M5 | Evidence / Consistency | Tables 1, 4, 5, 6, 7 | Wavelet-RAFT EPE: 0.46, 0.52, 0.46, 0.467, 0.367 across tables; Table 5's best (0.367, 0.790 s) conflicts with Table 6's 32-iteration result (0.46, 0.79 s) | Provide a run-to-table mapping; explain |
| DA-M6 | Protocol | Table 4 caption, Tables 5 and 7 | Hyperparameters (j = 4, 3 DWT levels) are selected as best-scoring on the Scene Flow test split, which has no validation split. Because every value in Table 5 (0.367–0.394) beats every baseline, the main comparison holds regardless of the selected value: MAJOR, not criterion 3 (decision-table row: main claim holds at every other swept value) | Select on a held-out part of the training set; state the protocol |
| DA-M7 | Scope | §1; §3.1; App. B.3 | Headline model Wavelet-MonSter (all leaderboard results) is never described; the module's integration with MonSter's mono branch and its added cost are unknown | Add description, params, runtime |
| DA-M8 | Evidence | §2; App. A, D | Claims that prior work generalises poorly and that Wavelet-RAFT shows superior zero-shot generalisation have no quantitative support | Add zero-shot table or remove |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §4.2 | Percent attributions for Selective-IGEV and DLNR are swapped (recomputed from Table 3) |
| DA-m2 | Consistency | §4.1 vs App. B.1 | AdamW vs Adam |
| DA-m3 | Consistency | App. A | "All models … trained exclusively on SceneFlow" vs fine-tuning in §4.2 |
| DA-m4 | Citation | Table 6; §4.2; refs [31], [41]/[42], [44] | Wrong or duplicated reference targets |
| DA-m5 | Reporting | Table 8 | Per-stage times sum to 489.1 ms vs 0.45 s for 16 iterations (Table 6); "equivalent FPS" promised, absent |
| DA-m6 | Math | Eq. 5, App. B.3 Eq. 8–9 | Loss index mismatch (i vs k); global pooling followed by a 7×7 conv |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Runtime reduction vs RAFT-Stereo (Table 6) | 38.6% | (0.44 − 0.27)/0.44 = 38.6% | Yes (but vs the 32-iteration row only) |
| Gain over RAFT-Stereo, high-frequency EPE (Table 3) | 22% | (34.00 − 26.48)/34.00 = 22.1% | Yes |
| vs Selective-IGEV, high-frequency | "25.89%" (first-named) | (26.10 − 23.42)/26.10 = 10.3% | **No (attribution swapped; 25.89% is DLNR)** |
| vs DLNR, high-frequency | "10.3%" | (31.60 − 23.42)/31.60 = 25.9% | **No (swapped)** |
| vs Selective-IGEV / DLNR low-frequency | "30.2% and 13.7%" | Selective-IGEV (0.51 → 0.44) = 13.7%; DLNR (0.63 → 0.44) = 30.2% | **No (swapped)** |
| ETH3D Bad1.0 Noc vs MonSter | 4.4% | (0.46 − 0.44)/0.46 = 4.3% | Yes (rounding) |
| DWT-level gain (App. C) | "2.3%" with "0.77M" | (0.483 − 0.472)/0.483 = 2.3% (HAM1→HAM2, +0.37M); 0.77M step gives 1.1% | **Partly** |
| Table 3 vs Table 1 consistency | n/a | Low-frequency EPE 0.72 > overall 0.53 | **No (impossible for a partition)** |
| Table 8 sum vs Table 6 | 0.45 s at 16 it. | 33.31 + 10.65 + 5.44 + 70.54 + 369.16 = 489.1 ms | Roughly (9% gap) |

## Ignored Alternative Explanations
- Extra capacity and a strong mono-depth prior in the MonSter-based leaderboard model explain the gains more simply than frequency separation.
- Higher EPE at Canny edges is expected from occlusion and discontinuities independent of any iterative "convergence" effect.
- Table 6's gain is partly a choice of the reference iteration count (32) and of reporting EPE only.
- Different training schedules for baselines vs proposed in the ablations: baseline retrained at 100k steps (0.62) vs reported 0.53 elsewhere.

## Missing Stakeholder Perspectives
Practitioners with latency budgets (driving, robotics): the headline model's runtime is not reported. Reviewers cannot see the authors' code (promised only).

## Observations (Non-Defects)
- The Haar-DWT front end is cheap and interpretable; the authors disclose overhead and failure cases.
- Leaderboard evaluation is external; the KITTI results do not depend on the authors' own protocol.
- The IFA ablation (Table 5) and DWT-level ablation (Table 7) are the right shapes of experiment, once reconciled.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Untested causal claim; inconsistent tables; no control for capacity |
| Clarity & Presentation | 52 | Readable but error-prone |
| Novelty & Originality | 48 | Incremental |
| Significance & Impact | 50 | Real but narrow |
| Experimental Validation | 42 | Missing controls, variance and zero-shot numbers |
| Reproducibility | 50 | Code promised; key integration details missing |
| Ethical Compliance | 60 | Nothing at stake |

**Pool position:** better than about 38% of submissions to ICLR. Deciding evidence: causal framing unsupported and tables mutually inconsistent, offset only by a leaderboard result with small margins.

## Overall: 3 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W7 (hyperparameters on test split) | Rewritten | Stated as a disclosure issue at MAJOR; the Scene Flow test is the field's usual reporting split, and conclusions hold across the sweep |
| R1 | ERR-8 (HSA 7×7 conv after global pooling) | Kept, but flagged as interpretation-dependent (Medium confidence) | A loose description is possible; the EIC treats it as a question about clarity |
| R1 | ERR-9 | Moved to Minor | Possible typo, Medium confidence |
| R2 | W3 "Selective-IGEV's Scene Flow EPE lower than 0.46" | Rewritten as a `[verify]` question | From recollection only; not checkable in paper |
| R2 | W5 "MonSter / DEFOM labelled CVPR 2025 in Table 2 but bibliography says arXiv" | Moved to Minor | Citation formatting |
| R3 | W1 "decompose right image / cost volume" | Kept (suggestion) | Constructive, labelled as suggestion |
| R3 | S4 (speed benefit) | Noted | Contradicted in part by Table 6 (12-iteration RAFT-Stereo); reflected in the EIC's weight |
| R4 | W1(iv) figures unavailable | Dropped | Not a weakness of the paper; a limitation of the read |
| R4 | W2 | Merged | Same issue as R1 Minor / DA-m1, DA-m4 |
| DA | DA-M6 | Kept at MAJOR | Table 5 lists all swept values beating every baseline |
| All | "Typos" lines | Moved to Minor | Cosmetic |

Scores were not changed.

---

# Phase 2: Synthesizer Package, Part A

## Official score (before EIC weights; DA-CRITICAL list empty)

`aggregate_scores.py scores_before.json --venue iclr` → official ratings R1 3, R2 3, R3 4, R4 3, DA 3, **mean 3.20**; official composite **53.4**; confidence-only EIC rating 3.17 → 3; composite band 3. No warnings.

## Merged issue list (classification)

| Merged issue | Sources | Class | May decide outcome? |
|--------------|---------|-------|---------------------|
| Causal diagnosis (C1/C2) untested; Table 3 not reconcilable with Table 1 | R1-W1/ERR-1, R3-W1 (partly), DA-M1 | CONSENSUS-3 | Yes |
| Missing controls separating wavelet from capacity | R1-W2, R2-W1, DA-M2 | CONSENSUS-3 | Yes |
| Speed claim relies on 32-iteration baseline | R1-W4/ERR-4, R4-W4, DA-M3 | CONSENSUS-3 | Yes |
| Cross-table EPE inconsistency (Table 5 vs others) | R1-W3/ERR-3, DA-M5 | CONSENSUS-2 | Yes |
| Headline Wavelet-MonSter not described; no zero-shot numbers | R1-W6, R4-W1, DA-M7, DA-M8, R2-W4 | CONSENSUS-4 | Moderate |
| Single run / small margins | R1-W5, R2 (Intro of W3), DA-M4 | CONSENSUS-2 | Moderate |
| Incremental novelty over Selective-Stereo / DLNR; missing related work | R2-W1/W2, R4-W3 | CONSENSUS-2 | Moderate |
| Baselines incomplete / D1-fg not best | R2-W3, DA-M4 | CONSENSUS-2 | Moderate |
| Reference errors; percentage swap | R1-Minor, R2-W5, R4-W2, DA-m1/m4 | CONSENSUS-4 | No |
| Deployment latency / robustness | R3-W2/W3 | SOLO | No |
| Hyperparameters chosen on test split | R1-W7, DA-M6 | CONSENSUS-2 | No |
| DA-CRITICAL | none | — | — |
| SPLIT | R3 rates significance and technical soundness higher; R3 treats the speed gain as a strength, R1/R4/DA contest it | SPLIT | Yes |

---

# Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency
## Submission ID: iclr26-SHAmQVifzK (blinded)
## Date: 2026-11-10
## Target Venue: ICLR (2026 cycle; scale status secondary) | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Leona Marchetti-Adeyemi; R1 Methodology Dr. Mei-Lan Pereira; R2 Domain Prof. Rashid Tolonen; R3 Perspective Dr. Sunita Azevedo-Brandt; R4 Generalist Dr. Jonas Whitcombe; DA Dr. Oluwaseun Ferreira-Nakamura

---

## Decision: Borderline Reject (3), ICLR label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean **3.20** · official composite **53.4**
**EIC assessment** (internal): weighted rating **3.13** → starting point **3** · weighted composite **52.6** → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: **3**
**Pool position (EIC):** better than about 45% of ICLR submissions.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The module is simple, cheap in parameters, plausible, and combined with MonSter it reaches first place on both KITTI leaderboards, an externally verified result in a very competitive sub-field. Ablations (Tables 4, 5, 7) and a compute breakdown (Table 8) exist, and failure cases and limitations are disclosed.
- **Against acceptance:** The paper's central scientific claim (that "frequency convergence inconsistency" is the underlying reason for limited iterative performance) is not tested; the region-wise EPE table cannot be reconciled with the main table; ablation numbers for the same model disagree across five tables; the speed claim holds only against a favourable baseline row; no control separates wavelet decomposition from extra capacity; the headline model is not described; margins over MonSter are 0.01–0.04 on single runs.

### Verification of Decisive Points (EIC read of the paper: abstract, contributions, §3 method, Tables 1–8, App. B–E)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 3 region EPEs inconsistent with Table 1 (low-frequency 0.72 > overall 0.53) | R1 ERR-1, DA-M1 | Tables 1, 3; App. B.2 | **Verified** | Mask normalisation undefined in Eq. 6–7; a partition cannot give an overall mean below its smaller-region mean. Possible protocol difference is unstated by the authors |
| Wavelet-RAFT EPE differs across tables; Table 5 (0.367) vs Table 6 (0.46) at same runtime | R1 ERR-3, DA-M5 | Tables 1, 4, 5, 6, 7 | **Verified** | Five different values; only Table 4 is explained by the stated "simplified training" |
| Speed claim valid only vs 32-iteration RAFT-Stereo | R1 ERR-4, R4-W4, DA-M3 | Table 6; §4.3 | **Verified** | 12-iteration RAFT-Stereo EPE 0.53 at 0.22 s vs 0.52 at 0.27 s; 38.6% recomputed correctly |
| No control separating wavelets from capacity | R1-W2, DA-M2 | Table 4, §4.3 | **Verified** | Only the two-layer-conv replacement of Fh and the GRU+concat replacement of HPU exist |
| §4.2 percentage attribution swapped | R1 ERR-2, R4-W2, DA | §4.2; Table 3 | **Verified** | 25.89% belongs to DLNR, 10.3% to Selective-IGEV |
| D1-fg not best; "almost all metrics" wording | R2-W3, DA-M4 | Table 2 | **Verified** | DEFOM-Stereo 2.24 / 2.23 vs 2.60 / 2.60; "for almost all metrics" is arguably accurate for rankings but "best performance among all published approaches" is overstated |
| Headline Wavelet-MonSter not described | R1-W6, R4-W1, DA-M7 | §3.1, §4.2 | **Verified** | §3.1 describes Wavelet-RAFT only |
| HSA 7×7 conv after global pooling (ERR-8) | R1 | App. B.3 Eq. 8–9 | **Partly correct** | Text says pooling "along spatial dimensions", conv then has nothing to act on; may be a loose description (e.g. CBAM-style channel pooling); treated as a question |
| Zero-shot generalisation claimed without numbers | R1-W6, R2-W4, DA-M8 | §2; App. A, D | **Verified** | Only Figs. 8–11 (qualitative); figures not viewed |
| Hyperparameters selected on the Scene Flow test split | R1-W7, DA-M6 | Table 4 caption; Tables 5, 7 | **Verified** (MAJOR, row 2 of the decision table) | Selected values are best-scoring, but all swept values beat every baseline; not criterion 3 |
| R3: speed gain is a strength; benefit "indicates comparable EPE with fewer iterations" | R3-S4 | Table 6 | **Overstated** | True against 32-iteration baseline only |
| R2: "Selective-IGEV's reported Scene Flow EPE is lower than 0.46" | R2-W3 | Table 1 | **Unverifiable** | From recollection; marked `[verify]`; not used in the decision |
| R1 ERR-9 (non-monotonic RAFT-Stereo row) | R1 | Table 6 | **Verified (as an anomaly)** | Probably a typo; not decisive |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Every MAJOR error-log entry I re-checked (ERR-1, 3, 4, 5, 6, 7) holds; ERR-8 is interpretation-dependent but flagged Medium; decisive for the outcome |
| R2 (Domain) | 3 | 4 | **1.0** | Sound; the one unverifiable claim (Selective-IGEV EPE) was marked `[verify]`; literature check unavailable so Critical missing references could not be established |
| R3 (Perspective) | 4 | 3 | **0.75** | Treats the 38.6% speed benefit and "iteration efficiency" as a strength (Overstated, Table 6) and did not catch the table inconsistencies; calibration slightly lenient (pool position 66 with several verified issues unmentioned); useful signal-processing points kept |
| R4 (Generalist) | 3 | 4 | **1.0** | Accurate, balanced; one point (figure-dependent) rightly not counted |
| DA | 3 | 4 | **1.0** | Arguments largely survive the check (M1–M5, M7); DA-M6 correctly kept at MAJOR; no overreach to CRITICAL |

### DA-CRITICAL Rulings

No DA-CRITICAL issues were raised ("No CRITICAL issues found."). Table is empty. I independently considered whether any verified issue meets the strict criteria: (1) *evidence contradicts the main claim*, no: the leaderboard result stands and the diagnostic claim is unsupported, not contradicted (narrowing fixes it); (3) *leakage*, no: Table 5 / 7 selections are best-scoring but the comparison holds at every swept value, so row 2 of the decision table applies (MAJOR); the leaderboard numbers are externally evaluated; (6) *method cannot be understood*: Wavelet-Stereo's core (Eq. 1–4, 10) is understandable, Wavelet-MonSter is under-described (MAJOR). Ceiling: none.

### Final Decision and Justification

The EIC-weighted rating is 3.13, so the starting point is **3 (Borderline Reject)**; the composite cross-check (52.6, band 3) agrees, so I do not depart. The decision rests on verified issues, each with a location: (a) the motivating claim (§1, Table 3) is not reconcilable with Table 1 and has no per-iteration evidence; (b) the same model's EPE takes five different values across Tables 1, 4, 5, 6 and 7; (c) the speed claim (Table 6) is true only against the 32-iteration baseline, while RAFT-Stereo at 12 iterations is equal at lower cost; (d) no experiment separates wavelet decomposition from the extra ~7M-parameter context path (Table 4, Table 8). These issues are mostly fixable, but they need new experiments rather than rewording, and they bear on the paper's own framing (title and abstract). Against that, the leaderboard-level KITTI result is real and the idea is sensible, but the margin over the closest prior model (MonSter) is 0.01–0.04 on single runs, and on the foreground metric closest to the thesis (D1-fg) a competing method is better. Judged against ICLR submissions, I place the paper at about the 45th percentile: a typical rejected submission with a stronger-than-typical empirical headline. A revised version that adds the capacity control, per-iteration region curves, reconciled tables and a described Wavelet-MonSter would plausibly be a Borderline Accept. The decision does not exceed any DA ceiling (none applies).

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate_scores.py scores.json --venue iclr --final 3`)

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
| Technical Rigor | 50 | 54 | 61 | 54 | 46 | 53.0 | 52.2 | 15 |
| Clarity & Presentation | 52 | 54 | 60 | 48 | 52 | 53.2 | 52.6 | 12 |
| Novelty & Originality | 48 | 50 | 60 | 52 | 48 | 51.6 | 50.8 | 12 |
| Significance & Impact | 52 | 56 | 65 | 56 | 50 | 55.8 | 54.9 | 15 |
| Experimental Validation | 44 | 50 | 60 | 52 | 42 | 49.6 | 48.5 | 18 |
| Reproducibility | 50 | 52 | 56 | 50 | 50 | 51.6 | 51.2 | 6 |
| Ethical Compliance | 62 | 62 | 66 | 62 | 60 | 62.4 | 62.1 | 6 |
| **Composite** | 50.2 | 53.5 | 61.2 | 53.4 | 48.5 | **53.4 (before)** | **52.6 (after)** | |
| Pool position (P%) | 40 | 45 | 66 | 48 | 38 | | | |

No dimension spread exceeds 20 points; no script warnings. **Official rating 3.20 → EIC-weighted rating 3.13 → starting point 3 → final 3.**

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating (script label for final Overall 3) | **4 on {0,2,4,6,8,10}** (5 on {1,3,5,6,8,10} for earlier cycles) |
| Venue-weighted composite | 52.4 (band 3, no shift, no DA cap) |

Present these as recent-form labels (secondary status); not official wording. Cross-venue outlook was not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "A Wavelet-based Stereo Matching Framework for Solving Frequency Convergence Inconsistency" to ICLR. The work targets a real weakness of iterative stereo (fine structures and thin objects) with an explicit multiresolution input.

**Overall Assessment:** The panel found a simple, interpretable and inexpensive idea with an externally verified, leaderboard-level result on KITTI. Its scientific framing is, however, ahead of its evidence, and several numbers in the paper do not agree with one another.

**Key Strengths Identified by Reviewers:**
1. Leading KITTI 2012 / 2015 and ETH3D results when combined with MonSter, plus gains on RAFT-Stereo (R1, R2, R4).
2. Parameter-free Haar decomposition that is interpretable and cheap; honest cost disclosure and failure cases (R1, R3, R4).
3. Well-chosen ablation structure and a practical plug-in design (R1, R3, R4).

**Key Concerns Requiring Attention:**
1. The "frequency convergence inconsistency" diagnosis and its stated cause are not tested; the Canny-region EPEs in Table 3 cannot be reconciled with Table 1 (R1, R3, DA; CONSENSUS-3).
2. No control separates wavelet decomposition from added extractor capacity; the same model's EPE differs across Tables 1, 4, 5, 6 and 7 (R1, R2, DA; CONSENSUS-3 and -2).
3. The speed claim compares against a 32-iteration baseline; 12-iteration RAFT-Stereo matches Wavelet-RAFT's 8-iteration accuracy at lower cost (R1, R4, DA; CONSENSUS-3).
4. The headline Wavelet-MonSter is not described, there are no zero-shot numbers, no variance, and margins over MonSter are small (R1, R4, DA, R2).

**Decision: Borderline Reject (3)**

The contribution is plausible and the leaderboard result is notable, but the fixes needed (a capacity-matched control, per-iteration region analysis, reconciled tables, a description and cost of the MonSter variant) require new experiments rather than rewording. We would expect a revised paper with these additions to be competitive at a future submission. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Leona Marchetti-Adeyemi
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Reference / notation errors; swapped percentages | R1, R2, R4, DA | CONSENSUS-4 |
| Headline Wavelet-MonSter not described; zero-shot claim lacks numbers | R1, R2, R4, DA | CONSENSUS-4 |
| Causal diagnosis untested; Table 3 not reconcilable | R1, R3 (partly), DA | CONSENSUS-3 |
| Missing capacity control | R1, R2, DA | CONSENSUS-3 |
| Speed claim relies on a favourable baseline | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the speed benefit a strength? | R3 | R1, R4, DA | Against: Table 6 at 12 iterations (verified) |
| Does the paper clear the ICLR bar? | R3 (4) | R1, R2, R4, DA (3) | Sided with the majority on verified issues; R3's weight reduced to 0.75 |

### Score Spread Discussion
No dimension is flagged (all spreads ≤ 18). Widest: Experimental Validation (R3 60 vs DA 42), because R3 did not weigh the missing controls and inconsistent tables; the editor adopts the lower view.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| (none) | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Causal claim untested; Table 3 vs Table 1 | Yes (R1) | n/a | n/a |
| DA-M2 | MAJOR | No capacity control | Yes (R1, R2) | n/a | n/a |
| DA-M3 | MAJOR | Speed claim vs 12-iteration baseline | Yes (R1, R4) | n/a | n/a |
| DA-M6 | MAJOR | Hyperparameters chosen on test split (non-leakage row) | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Issues the EIC verified as undermining a main claim (no upheld DA-CRITICAL issue).*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Diagnostic claim untested; region EPEs not reconcilable with main table | R1-W1/ERR-1, DA-M1, R3-W1 | Abstract, §1, Table 3, App. B.2, Fig. 1 | State mask source / normalisation; recompute Table 3 with the Table 1 protocol; add per-iteration region-EPE curves for RAFT-Stereo and Wavelet-RAFT; or narrow the claim | Medium (≈ 1–2 GPU-h inference + text) | Yes |
| R2 | No control separating wavelet decomposition from added capacity | R1-W2, DA-M2, R2-W1 | Table 4, §4.3 | Same extractor on raw RGB / learned high-pass; IFA on/off; HP-LSTM vs DLNR LSTM; param-matched baseline | High (≈ 4 runs × 100k steps) | Partly |
| R3 | Inconsistent EPE for the same model across tables | R1-W3/ERR-3, DA-M5 | Tables 1, 4, 5, 6, 7; App. C text | Provide run-to-table map; correct or re-run Table 5 / 7; fix the "2.3% / 0.77M" sentence | Low–Medium | Yes |
| R4 | Speed / convergence claim against favourable baseline | R1-W4/ERR-4, R4-W4, DA-M3, R3-S4 | Table 6, §4.3 | Matched wall-clock EPE curves for both models; verify 16-iteration row | Low | Yes |
| R5 | Headline model undescribed; zero-shot generalisation unquantified | R1-W6, R4-W1, DA-M7/M8, R2-W4 | §3.1, §4.2, App. A, D | Describe the Wavelet-MonSter integration with params / runtime; add the Scene Flow→KITTI/Middlebury/ETH3D zero-shot table | Medium–High | Partly |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Single runs with 0.01–0.04 margins | R1-W5, DA-M4 | 3 seeds on Scene Flow for MonSter vs Wavelet-MonSter or paired bootstrap | High (≈ 6 × 200k-step runs) | No |
| S2 | Incremental novelty vs Selective-Stereo / DLNR not tested; related work gaps | R2-W1/W2 | Matched-backbone comparison; discuss WaveletStereo `[verify]`, wavelet-CNN restoration work `[verify]` | Medium | Partly |
| S3 | Overclaimed best-among-all-published wording (D1-fg; IGEV++ `[verify]`; foundation stereo `[verify]`) | R2-W3, DA-M4 | Add rows / narrow wording; add Selective-IGEV and DLNR to Table 1 | Low | Yes |
| S4 | Hyperparameters chosen on the Scene Flow test split | R1-W7, DA-M6 | Hold-out selection; state protocol | Medium | Partly |
| S5 | Latency / memory of the headline model; robustness | R3-W2/W3 | Params / FLOPs / ms for Wavelet-MonSter; corruption tests | Medium | Partly |
| S6 | Unclear module equations (Eq. 1–3, 8–10) | R4-W1, R1-ERR-8 | Pseudo-code with shapes; clarify pooling vs 7×7 conv | Low | Yes |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Reference errors ([31], [41]=[42], [44], "GMStereo [37]") | R1, R2, R4, DA | Audit the bibliography |
| N2 | AdamW vs Adam; "trained exclusively on SceneFlow"; Eq. 5 index; Table 8 sum and FPS column; typos | R1, R4, DA | Fix text |
| N3 | Show one non-stereo recurrent task or another backbone (IGEV) | R4-W3 | Support the "plug-and-play" claim |
| N4 | Texture-edge vs depth-edge region analysis; alternate decompositions | R3-W1 | Extend the analysis |

---

## Estimated Revision Effort
- Priority 1: 5 items, ≈ 2–3 weeks (about 1–2 GPU-weeks on the authors' 2×A6000 setup; estimate, to be confirmed by the authors)
- Priority 2: 6 items, ≈ 2–3 weeks (seed runs dominate)
- Priority 3: 4 items, ≈ 2–3 days
- **Total estimated revision time**: ≈ 4–6 weeks

*Literature check note: mode strict, cutoff 2025-09-24; 3 query attempts (1 refused by the self-exclusion filter, 2 executed and failed with HTTP 429), 0 kept results; claim, baseline and expansion rounds not completed. Every recommended reference above is marked `[verify]`.*
