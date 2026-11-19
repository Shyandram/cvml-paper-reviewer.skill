# Academic Paper Review: "Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents"

**Date:** 2026-11-10 · **Mode:** full · **Target venue:** ICLR (stated by the user) · **Literature check:** strict, cutoff 2025-09-24 · **Skill version:** 2.10.1

*Disclosure.* The five reviewer reports were written as five sequential role-based passes in a single model context. No independent agents ran. The simulated outcome is "how a careful panel would likely see this draft", not a prediction. The paper text was extracted from the PDF, so **figures were not viewable**. Figure-dependent statements (Figures 2–7) are judged from captions and text only, and every such place is marked.

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents |
| Primary Discipline | Machine learning for science → neural operators / PDE surrogates |
| Secondary Discipline(s) | Physical oceanography (surface currents); climate-data downscaling and super-resolution |
| Paper Type | Empirical (composite weights: empirical). It proposes model variants and benchmarks them. |
| Core Technique(s) | Fourier neural operators (FNO) with a downscaling front end (DFNO, after Yang et al. 2023), U-shaped operator variant (DUNO), residual operator (SpecDFNO), diffusion upsampling (SpecDFNODiff), Sobel-gradient variants (MetaGradDFNO, MultiGradDFNO), temporal variants |
| Target Venue | ICLR 2026 main-track standard (stated by the user); profile key `iclr` (scale status: secondary). The manuscript footer reads "ICML 2025 Workshop. Copyright 2025 by the author(s)." |
| Venue-Specific Notes | No ICLR-specific contribution type. The manuscript is a short workshop paper (about six pages of main text, then references and a four-page appendix). It is judged against the ICLR main-track pool, as the user requested. |
| Paper Maturity | Early draft / workshop-stage. |
| Ethics-Relevant Content | None (no human data). Dual-use is minimal. Possible safety relevance: hallucinated currents in oil-spill or search-and-rescue use (Sec. 5.1, Sec. 5.2.3). |

### Claimed Contributions (as stated by the authors, Sec. 1)
1. **C1:** "We benchmark multiple models for arbitrary-resolution downscaling and apply them to physical observations" (Copernicus ocean currents). Resource/benchmark claim.
2. **C2:** "We develop a surrogate model capable of predicting PDE solutions at arbitrary resolutions-independent of the input resolution." Method claim, with the priority statement "this is the first work to present a neural surrogate capable of accurate, resolution-agnostic prediction".

### Paper memory (factual record; shared with all reviewers)
- **Setup facts.**
  - Navier–Stokes (NS): 10,000 simulations at 64×64, 50 steps, ν = 1e-4, split 7,000/2,000/1,000 (Sec. 3.1). Coarse grids 32×32 and 16×16 are made by average pooling. Input is 5 frames at 16×16, output is the next 5 frames at 16×16 and 32×32. Zero-shot evaluation is at 64×64 from the 16×16 input (Sec. 3.4).
  - Copernicus: global surface velocities at 0.08°. "Regional subsets" (not named), 128×128 patches, split 800/200/100 (Sec. 3.1). Inputs are average-pooled to 2×, 4× and 8× coarsening (Sec. 4.2).
  - Appendix: Adam, lr 1e-3, 600 epochs, batch 16 (A.1). Z-score per velocity component and "a 70%/15%/15% ratio" split (A.2).
  - Not stated after search: model sizes and Fourier modes, number of parameters, seeds, runtime or hardware, code, how patches/regions/dates were chosen, which split Tables 1–4 report on, which scale factors each model was trained on, PSNR/SSIM definitions, land-mask handling.
- **Headline numbers.** "MAE improvement of 30×" (Sec. 5.2.2, from Table 2). DFNO-2/DFNO-4 comparison numbers in Table 1 are copied from Yang et al. (2023).
- **Appendix adds.** Optimizer and preprocessing, plus Figures 4–7 (qualitative panels). It adds no ablations, no variance and no metric definitions.
- **Unverifiable.** Figures 1–7 (extraction only) and equation typesetting. Equations 1–4 are the standard NS vorticity form, with no unusual content.
- **Integrity scan.** `scripts/integrity_scan.py`: "No reviewer-directed text or hidden characters found." Nothing was redacted. No other out-of-place instructions were seen while reading.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Halvard Mbeki-Lindqvist, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty, area chair at ML and ML-for-science venues / scientific ML, evaluation of surrogate models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Wants the headline claim tested by the experiments. Tolerant of small scale if the evidence is clean.

### Reviewer 1 (Methodology): Soo-ah Tanvirov, industrial research lab (Central Asia / Europe)
- **Seniority / Expertise**: Mid-career industry scientist / neural operators, evaluation protocols for PDE surrogates, super-resolution metrics
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; insists on matched baselines and seeds.

### Reviewer 2 (Domain): Camille Odhiambo-Reyes, climate-data group, national research institute (Western Europe)
- **Seniority / Expertise**: Senior researcher / statistical and deep-learning downscaling of climate fields, FNO literature, operational ocean products
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks that prior work is described as its own abstract describes it.

### Reviewer 3 (Perspective): Ravindra Kalinowski, geophysical fluid dynamics department, public university (South Asia)
- **Seniority / Expertise**: Associate professor / ocean turbulence and spectral diagnostics, data assimilation, implicit neural representations (graphics)
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what a practising oceanographer would need to trust the output.

### Reviewer 4 (Generalist): Ximena Aldous-Park, machine-learning group, mid-size university (South America)
- **Seniority / Expertise**: Mid-career faculty / deep learning broadly (generative models, representation learning)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: A typical program-committee member; reads the whole paper but not every derivation.

### Devil's Advocate: Dmitri Fenwick-Osei, evaluation-methodology and statistics group, research institute (North America)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, causal inference, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews (each reviewer used the reviewer copy, which is identical to the paper because the scan redacted nothing, plus the paper memory; none saw another reviewer's report)

## Reviewer 1: Methodology

# Peer Review Report
## Paper: Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents
## Reviewer: Soo-ah Tanvirov, Methodology (industrial research lab; fictional persona)
## Expertise: neural operators; PDE-surrogate evaluation; super-resolution metrics
## Date: 2026-11-10

### Summary
The paper builds a family of Fourier-neural-operator downscalers following Yang et al.'s DFNO. It adds a U-shaped operator (DUNO), a residual operator (SpecDFNO), a diffusion upsampler (SpecDFNODiff) and two Sobel-gradient variants. It also adds temporal versions (Temp DFNO, Temp SpecDFNO) that predict five future Navier–Stokes frames at 16×16 and 32×32 from five 16×16 inputs, with a zero-shot 64×64 readout (Sec. 3.4, Table 1). Static downscaling from average-pooled Copernicus surface-current patches is compared against two U-Net baselines at 2×, 4× and 8× (Tables 2–4). The authors conclude that the neural operators far outperform CNNs and that the temporal models match DFNO without a numerical solver (Sec. 5.2.1–5.2.2).

### Strengths
**S1: Sensible zero-shot test design for the temporal surrogate.** Training on 16×16 → {16×16, 32×32} and evaluating 16×16 → 64×64 (Sec. 3.4, Table 1) is a real out-of-resolution test, and the 64×64 error rises modestly (MAE 0.0198 vs 0.0174).

**S2: A real observational data stream and a clean train/val/test split by count.** Copernicus velocities (Sec. 3.1, 4.2) are a worthwhile target, and the paper reports 2×, 4× and 8× factors rather than one (Tables 2–4).

**S3: Both L1 and L2 training losses are reported for every model (Tables 2–4)**, which at least exposes loss sensitivity, and limitations at large factors are reported openly (Sec. 5.2.3).

**S4: Transparent use of copied numbers.** The Table 1 caption states that "DFNO-2 and DFNO-4 values are taken from (Yang et al., 2023)", so the provenance of those rows is disclosed.

### Weaknesses

**W1: The CNN baselines look non-functional, so the "30×" headline carries no information.** Table 2 reports CNN 2x MAE 0.424, SSIM 0.105 and PSNR 14.07. Table 3 gives MAE 0.4246 and Table 4 gives 0.424, so MAE is identical to three digits across all three output resolutions and across L1 and L2 training. SSIM stays near 0.1 everywhere. The inputs are average-pooled copies of the target field, so plain bicubic interpolation would be expected to do far better than SSIM 0.1; the DFNO rows reach SSIM 0.97 at 2×. No interpolation baseline, no standard super-resolution network and no generative baseline is reported, so the "(MAE improvement of 30×)" (Sec. 5.2.2; 0.424 / 0.0137 = 30.9, recomputed) says only that a mis-trained or mis-evaluated baseline is bad. The text of Sec. 3.4 also describes odd evaluation (CNN-2 "through model recursion and bicubic interpolation", CNN-4 reduced "through average pooling").
- **Suggested Fix**: add bicubic/nearest, a trained single-scale SR network (e.g., EDSR/SwinIR-class) and the original FNO/DFNO under matched training. Report a sanity check that the CNN reproduces published behaviour on the NS data. About 1–2 GPU-days.

**W2: The arbitrary-resolution claim (C2) is not tested as worded.** Every experiment uses a 16×16 input (Sec. 3.4, Table 1, Sec. 4.2 and 5.2.2: "16×16 → 32×32/64×64/128×128"). The abstract and Sec. 1 claim output resolution "regardless of the input resolution", but no run varies the input resolution (e.g., 32×32 → 64×64, or 8× from a 32×32 input). Only power-of-two factors (2×, 4×, 8×) are tried. No non-integer factor (e.g., 3×) and no grid beyond the data's native resolution is evaluated. "Arbitrary" is therefore an untested extrapolation of three integer factors from a single input size.
- **Suggested Fix**: add a grid of (input, output) resolution pairs, including non-integer factors, and report error against factor. Low cost, since models already exist.

**W3: No variance, a single run, and a 100-patch test set.** There are no seeds, standard deviations or intervals anywhere (searched: "seed", "std", "variance" give no hits). Copernicus has only 100 test patches (Sec. 3.1), and the training set has 800 patches. The ranking claims rest on small gaps: MetaGradDFNO vs MultiGradDFNO MAE 0.01370 vs 0.01380 (Table 2, L2); SpecDFNO vs DFNO at 4× is −10% MAE (Table 3, 0.03653 vs 0.04057, recomputed); Temp SpecDFNO vs Temp DFNO differ by 0.2–0.8% in MAE across Table 1. This is a small-experiment regime where variance is expected (Field-Norm Calibration), so single runs are a real weakness here.
- **Suggested Fix**: 3–5 seeds for the main rows, a paired bootstrap over test patches. About 20–40 GPU-hours for models this size (sizes not stated).

**W4: The Table 1 comparison with DFNO-2/DFNO-4 is not like-for-like, and the text overstates it.** DFNO-2/4 numbers are copied from another paper. DFNO-2/4 downscale solver-generated fields, whereas the temporal models predict five future frames (Sec. 4.1, Sec. 5.2.1). Nothing says the data, normalization or error definition match. Even taken at face value, the results are mixed. At 32×32, Temp DFNO has MAE 0.017426 vs 0.0124 for DFNO-2 (40% worse) and 0.0208 for DFNO-4 (16% better). At 64×64 it has 0.019775 vs 0.0246 (20% better) and 0.0168 (18% worse). The text says the temporal models "not only match, but in some cases outperform" DFNO-2/4. Meanwhile there is no baseline at all for the temporal task: no persistence, no plain FNO-3D at fixed resolution, no numerical-solver cost or accuracy, no rollout beyond five frames.
- **Suggested Fix**: re-train DFNO-2/4 on the paper's own NS set, add persistence and a plain FNO/UNet-forecaster, and report rollout error growth and wall-clock vs the solver.

**W5: Several components are never isolated.** No ablation exists for the meta-upsampling, Sobel preprocessing, residual operator or diffusion block (Sec. 3.2). Parameter counts are never given. SpecDFNO adds a second neural operator (Sec. 3.2), so its gains may be capacity. Temp SpecDFNO vs Temp DFNO differ by ≤0.8% (Table 1). Yet the text says the residual operator is "enhancing the model's ability to capture high-frequency components", and no spectrum or high-frequency metric is shown.
- **Suggested Fix**: parameter-matched ablations and an energy-spectrum plot per model.

**W6: Protocol under-specified and inconsistent (see Error Log ERR-1, ERR-4).** The Copernicus regions, dates, patch extraction and overlap are not given. Adjacent or overlapping patches from the same region and time can leak across the 800/200/100 split. Which split Tables 1–4 report, and which split selected checkpoints/epochs, is not stated after the protocol sweep. The scale factors each model was trained on are not stated either, so "zero-shot 4×" for SpecDFNO (Sec. 5.2.2) cannot be interpreted. I found no statement of tuning on the reported split (searched: test, validation, select, tuned, checkpoint, best model, early stopping), so I raise no leakage finding, only the unanswered question.
- **Suggested Fix**: state regions, dates, patch stride, split rule (spatially/temporally disjoint), the reporting split, and training factors.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E6 | Sec. 3.1 vs App. A.2 | "800 training samples, 200 validation samples, and 100 test samples" vs "split using a 70%/15%/15% ratio" | Copernicus: 800/200/100 of 1,100 is 72.7/18.2/9.1%. NS: 7,000/2,000/1,000 is 70/20/10%. Neither matches 70/15/15. | Recomputed | High | MINOR | State the real split |
| ERR-2 | E1 | Table 3 | Row "DFNO L1 0.04057 0.01749 33.15377 0.85038" | Tables 2 and 4 obey PSNR = 10·log10(P/MSE) with one constant P in each table (P ≈ 4.93 in Table 2, 7.45 in Table 4, constant to ±0.01 over all rows). In Table 3 the implied P ranges from 5.3 (DUNO L1) to 36.2 (DFNO L1) and 6.6 (CNN rows). At least one of the MSE or PSNR columns is wrong, mainly for the DFNO rows. | Recomputed from the printed values | High | MAJOR | Recheck Table 3's MSE/PSNR columns; the "DUNO competitive MSE" statement rests on that column |
| ERR-3 | E1/E5 | Sec. 5.2.2 vs Table 2 | "SpecDFNO shows robust performance across all scales" | At 2× SpecDFNO is worse than plain DFNO: MAE 0.03407 vs 0.02134 (L1, +60%) and 0.02451 vs 0.01822 (L2, +35%). | Recomputed from Table 2 | High | MAJOR | Narrow the claim to 4×, or explain |
| ERR-4 | E8/E6 | Sec. 3.4 | "PSNR and SSIM metrics are also computed (details provided in the Appendix)" | The appendix (A.1, A.2, B.1, B.2) has no metric definitions: no peak value, no SSIM window, no per-sample vs aggregate averaging. | Searched the full text | High | MINOR | Add the definitions |
| ERR-5 | E4 | Table 4 | Rows DFNO, MetaGradDFNO, MultiGradDFNO: MAE ≈ 0.0648, MSE ≈ 0.00936, SSIM ≈ 0.609 | At 8×, six configurations (DFNO L1/L2, MetaGrad L1/L2, MultiGrad L1/L2) have MAE within 0.0002 of 0.0648, SSIM spread < 0.001, and MSE 0.00934–0.00936 in five of the six (0.00894 for MultiGrad L1). Different architectures and losses should not collapse like this. This suggests a shared fallback output, so rankings at 8× are not informative. | Cross-referenced across rows | Medium | MAJOR | Report bicubic at 8× and check outputs are not the interpolated input |
| ERR-6 | E1/E5 | Sec. 5.2.1, Table 1 | "These models not only match, but in some cases outperform the DFNO2 and DFNO4 models" | Mixed results (see W4), and the comparison is across different tasks. | Recomputed from Table 1 | High | MAJOR | Re-run DFNO-2/4 under the paper's protocol |

### Claim-to-Evidence Map
| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|--------------|----------|---------|
| C1 | Benchmark of arbitrary-resolution downscaling models on Copernicus | Sec. 1 | Tables 2–4 | Partially: one weak baseline pair, one run, no interpolation baseline |
| C2a | Surrogate predicts PDE solutions at arbitrary output resolution, independent of input resolution | Abstract, Sec. 1 | Table 1 (16×16 input only) | Partially: three integer factors, one input size |
| C2b | First resolution-agnostic neural surrogate | Sec. 1 | None possible | Unsupported (see R2) |
| C3 | Temporal models "match, and in some cases outperform" DFNO-2/4 and combine the predictive power of a numerical solver | Sec. 5.2.1 | Table 1 | Contradicted for DFNO-2 at 32×32; no solver comparison |
| C4 | Neural operators far beat CNNs | Sec. 5.2.2 | Tables 2–4 | Supported only against a likely broken baseline |
| C5 | Physical conservation is enforced | Sec. 3.2 | None | Unsupported (no diagnostic, mechanism unclear) |

### Omission sweep
Split and tuning split: split present, reporting/selection split **not stated after search**. Seeds/variance: **not stated after search**. Baseline settings: partly (CNN architecture in Sec. 3.4; DFNO settings not stated). Hyperparameters: A.1 present, search procedure not stated. Compute/hardware: **not stated after search**. Licence: Copernicus cited (Copernicus Marine Service, 2025), licence not discussed. Failure cases/limitations: present (Sec. 5.2.3). Code/data availability: **not stated after search**.

**Minor:** inconsistent "~9 km" (Sec. 1) vs "~8 km" (Sec. 3.1) for 0.08°; "DFNO2/DFNO4" vs "DFNO-2/DFNO-4" naming; incomplete reference author lists ("e. a.").

### Questions for Authors
1. What exactly produced the near-constant CNN MAE of 0.424 in Tables 2–4, and what does bicubic interpolation of the same inputs score? (A strong bicubic number would lower my score of the whole empirical section; a sound CNN pipeline would raise it.)
2. Can you show a (32×32 → 64×64) or non-integer-factor result? (This would address W2.)
3. Which split do Tables 1–4 report, and was the epoch/checkpoint chosen on validation?
4. Are the Table 1 DFNO-2/4 numbers on the same NS data and normalization as the Temp models?

### Dimension Scores (0–100)
**Pool position:** better than about 15% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main baseline comparison (Tables 2–4) is uninformative, and the central "arbitrary input-independent resolution" claim is tested at one input size with a single run.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | Inconsistent Table 3, unexplained collapsed rows, untested claim |
| Clarity & Presentation | 52 | Developing | Understandable, but results are in the Discussion and metrics are undefined |
| Novelty & Originality | 35 | Developing | Incremental variants of a published DFNO (see R2) |
| Significance & Impact | 36 | Developing | No evidence the output is usable beyond the 0.08° product |
| Experimental Validation | 30 | Developing | One run, 100 test patches, broken or weak baseline, no ablations |
| Reproducibility | 40 | Developing | Optimizer given, but model sizes, regions, code and seeds absent |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations discussed (Sec. 5.2.3) |

*Consistency note:* Overall 2 against own composite 39.5 (band 2).

### NeurIPS-style: Quality 1 · Clarity 2 · Significance 1 · Originality 1
### Limitations: Partially. Sec. 5.2.3 discusses large-factor degradation but attributes it to "physical reality" without a test.
### Ethics Review Flag: No
### Overall: **2 (Reject).** Confidence: **4**. The reliable results are only the 2× DFNO-family numbers. The main comparative and conceptual claims are not supported by the experiments as reported.

---

## Reviewer 2: Domain

# Peer Review Report
## Reviewer: Camille Odhiambo-Reyes, Domain (national research institute; fictional persona)
## Expertise: statistical and neural downscaling; FNO literature; operational ocean products
## Date: 2026-11-10

### Summary
The submission applies and extends the DFNO of Yang et al. (2023). Its temporal variant predicts Navier–Stokes frames at several resolutions, and its static variants downscale Copernicus surface currents. The authors present this as the first neural surrogate whose output resolution is independent of its input resolution (Sec. 1) and as a benchmark on real ocean data.

### Strengths
**S1: A relevant, under-served application.** Ocean-current downscaling from the 0.08° analysis (Sec. 1, 3.1) is of practical interest, and applying the DFNO idea outside atmospheric fields is a reasonable test of transfer.

**S2: Honest positioning relative to the closest method.** The paper states what Yang et al. (2023) did and what it adds (Sec. 1, 2.3), and it describes DFNO as the base of every variant rather than hiding the lineage.

**S3: Broad family of variants in one framework (Sec. 3.2, Fig. 1 caption)** — spectral residual, gradient, diffusion and U-shaped operator options give the community a quick map of what to try.

### Weaknesses

**W1: The contribution is incremental over the cited DFNO, and the priority claim is overstated.** The strongest prior (Yang et al. 2023, Fourier Neural Operators for Arbitrary Resolution Climate Data Downscaling, ICLR 2023 workshop) already trains on a small upsampling factor and zero-shot downscales to unseen factors. Sec. 3.2 says "the rest of the framework is similar to the DFNO". The new pieces are (i) a time axis in the convolutions (Sec. 3.3), which is a standard way to extend an FNO to spatiotemporal data [verify against Li et al., 2020], and (ii) a set of block swaps without ablation. The sentence "the first work to present a neural surrogate capable of accurate, resolution-agnostic prediction, where the output resolution does not depend on the input resolution" (Sec. 1) is not established. The paper itself describes neural operators as able to "learn resolution-agnostic operators governing PDEs" (Sec. 1), the arbitrary-scale super-resolution literature (below) targets one model for any output size, and the paper evaluates one input size. It also never quantifies "accurate" against any neural-surrogate baseline.
- **Suggested Fix**: narrow the claim to "a temporal extension of DFNO evaluated on NS", add an explicit novelty-delta table vs Yang et al. and arbitrary-scale SR methods.

**W2: Positioning omits the arbitrary-scale super-resolution line and mis-names a component.** Related Work (Sec. 2.3) says CNN downscalers are "limited to fixed input and output sizes". Arbitrary-scale SR networks that take one model to any magnification (Meta-SR; LIIF) are a direct, citable counter-example and a natural static baseline for Tables 2–4. The paper also introduces "a Universal Neural Operator (UNO)" (Sec. 3.2) with no citation. The operator I know under that acronym is the **U-shaped** neural operator (Rahman, Ross and Azizzadenesheli, TMLR 2023) [verify]. The text's expansion looks wrong and uncited, and the claim "UNO generalizes well across different PDE types and is more expressive than the standard FNO" has no source.
- **Suggested Fix**: cite and compare, or correct the name and cite the source.

**W3: Related work on neural operators is described but never used as a baseline.** Transolver, FactFormer and LSM are named as resolution-agnostic operators (Sec. 1, 2.1) but none is evaluated on the NS set or on Copernicus. The temporal task has no neural-operator baseline at all (Table 1 compares only against numbers copied from the DFNO paper). A missing baseline is MAJOR at most. Here it matters because C2 is "a surrogate".
- **Suggested Fix**: add at least FNO-3D/UNO and one transformer-operator on the NS data.

**W4: Domain-relevant evaluation is missing.** For ocean surface currents the field uses kinetic-energy spectra, divergence/vorticity statistics and drifter or HF-radar validation. None appears. The task is downscaling a 0.08° product from an average-pooled copy of itself (Sec. 4.2). It does not test whether the output improves on the 0.08° product, which is the motivation given in the abstract and Sec. 1 ("insufficient for applications requiring detailed local dynamics").
- **Suggested Fix**: add spectra and divergence diagnostics, and a held-out higher-resolution regional model or in situ comparison.

**W5: Citation details to check (E7).** The OceanNet reference is listed as "Oceannet: Surrogate modeling of gulf stream dynamics using fno and predictor–corrector schemes. Advances in Water Resources, 2023". The record I could verify is "OceanNet: A principled neural operator-based digital twin for regional oceans" (Chattopadhyay et al., arXiv 2023); the title and venue should be checked [verify]. Several entries use "e. a." (Daw, Dong, Chattopadhyay). "(Dong, 2015)" is cited for CNN image super-resolution without an author list.

### Literature-check addendum (strict mode, cutoff 2025-09-24)
Five queries ran (claim ×2, baseline ×1, expansion ×2; two more were refused for exceeding 4 concept words and not counted). 42 results were kept: 33 prior, 5 recent preprints, 4 concurrent, none newer (strict). `coverage` showed no gaps. `related_search.py benchmarks` found no public benchmark names; the NS data follows Li et al.'s recipe and Copernicus is a data product, so the baseline `scout` step had nothing to scout. Similarity run: closest prior work **Fourier Neural Operators for Arbitrary Resolution Climate Data Downscaling** (cosine 0.306, "high conceptual overlap: check task and core mechanism"), then Downscaling Neural Network for Coastal Simulations (0.207) and Evaluating Loss Functions and Learning Data Pre-Processing for Climate Downscaling (0.165). No text overlap (0 shared 8-grams).

**Per-claim novelty (`related_search.py novelty`)**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 benchmark on Copernicus | resource | **medium** | Yang et al. 2023 (3; https://arxiv.org/abs/2305.14452v2; prior, peer-reviewed; cited). Coastal-simulation downscaler (2; https://arxiv.org/abs/2408.16553v3; prior arXiv-only; not cited) | DFNO is the same method family on ERA5/NS. The ocean-current data are new for it. |
| C2 resolution-agnostic temporal surrogate | method | **incremental** | Yang et al. 2023 (4; cited). Lütjens et al. 2022 Multiscale Neural Operator (3; https://arxiv.org/abs/2207.11417v1; prior arXiv-only; not cited). Meta-SR (2; https://arxiv.org/abs/1903.00875v4; not cited) | DFNO already gives zero-shot arbitrary-factor output. The delta is the time axis. |

Script paper reading: "no central claim fully covered by prior work", so no criterion-7 candidate. The attribution is Yang et al. 2023, which the paper cites and differentiates, so any novelty deficit is MAJOR at most (insufficient novelty).

**Novelty delta table**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C2 | Yang et al. 2023 (DFNO) | Trains with small upsampling factor, zero-shot downscales to larger factors with a Fourier operator | Convolutions over time, so output is a predicted sequence | Yes, explicitly (Sec. 1, 2.3), though "the rest of the framework is similar to the DFNO" (Sec. 3.2) |
| C2 | Lütjens et al. 2022 | Grid-independent fast PDE surrogate with a learned closure | — | No |
| C1 | Yang et al. 2023 | Downscaling with FNO on climate fields | Surface-ocean-current data, extra variants | Yes |

**Baseline scout.** Not applicable (no external benchmark detected). The only copied baseline numbers are DFNO-2/4 in Table 1 (from Yang et al.). Whether the settings match cannot be checked from the manuscript, so it stays a question, not an under-reported baseline.

**Field snapshot (as of the cutoff).** Roughly 3–5 years ago downscaling meant fixed-factor CNN/GAN super-resolution, and arbitrary-scale one-model approaches had come from computer vision (Meta-SR 2019, LIIF 2021). Neural operators (FNO 2020) then offered grid-independent maps, applied by 2023 to arbitrary-resolution climate downscaling (DFNO) and to Gulf-Stream and global-weather emulation (OceanNet, FourCastNet). Current work in the kept results moves toward generative, scale-adaptive and uncertainty-aware downscaling that does not need retraining per model or climate (e.g., Hess et al. 2024, https://arxiv.org/abs/2403.02774v4) and toward observation-guided arbitrary-resolution fields (2025 preprints). Open problems stated in those abstracts are uncertainty, extrapolation to unseen conditions and fine-scale coastal fidelity. In this sub-field right now, a small MAE gain on a self-degraded product is incremental. A significant contribution would be a new capability tested on real observations at finer-than-product resolution, with strong interpolation/SR/generative baselines, physical diagnostics (spectra, divergence) and calibrated uncertainty. I used this to score Novelty and Significance.

### Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Hu et al., "Meta-SR: A Magnification-Arbitrary Network for Super-Resolution", CVPR 2019 (https://arxiv.org/abs/1903.00875v4, found) | Prior single-model arbitrary-magnification upsampling; bears on the "first" claim and on baselines |
| Critical | Chen, Liu, Wang, "Learning Continuous Image Representation with Local Implicit Image Function" (LIIF), CVPR 2021 (https://arxiv.org/abs/2012.09161v2, found) | Continuous-representation approach to arbitrary-scale SR (per its title and the arbitrary-scale SR search results); natural static baseline |
| Important | Lütjens et al., "Multiscale Neural Operator: Learning Fast and Grid-independent PDE Solvers", ICML AI4Science workshop 2022 (https://arxiv.org/abs/2207.11417v1, found) | Grid-independent surrogate, same goal as C2 |
| Important | Liu et al., "Downscaling Neural Network for Coastal Simulations", 2024 (https://arxiv.org/abs/2408.16553v3, found) | Ocean/coastal downscaling baseline family |
| Important | Rahman, Ross, Azizzadenesheli, "U-NO: U-shaped Neural Operators", TMLR 2023 [verify] (not found by title on arXiv) | Source of the operator the paper calls "UNO" |
| Important | Kovachki et al., "Neural Operator: Learning Maps Between Function Spaces" (https://arxiv.org/abs/2108.08481v6, found) | Theory of resolution-agnostic operators, which the paper leans on without citing |
| Helpful | Pathak et al., "FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators", 2022 (https://arxiv.org/abs/2202.11214v1, found) | FNO-family global emulation |
| Helpful | Hess et al., "Fast, Scale-Adaptive, and Uncertainty-Aware Downscaling of Earth System Model Fields with Generative Machine Learning", 2024 (https://arxiv.org/abs/2403.02774v4, found) | Generative, scale-adaptive downscaling with uncertainty (the paper's own future work, Sec. 5.3) |

All entries were found with `related_search.py verify` or the claim searches, except U-NO, which is marked `[verify]`. Only prior-labelled work is given Critical or Important status. No recent or concurrent preprint is required.

### Questions for Authors
1. What differs, beyond the temporal axis, between Temp DFNO and DFNO-2/4 of Yang et al.? (A clear architectural difference would raise Novelty.)
2. What is the source for "UNO", and how does DUNO differ from a U-NO-based DFNO?
3. Do outputs improve on the native 0.08° product at all (comparison with an independent finer model or in situ data)?

### Dimension Scores (0–100)
**Pool position:** better than about 18% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental lineage from one cited paper, with a priority claim that does not hold, and no ocean-relevant validation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Block swaps unmotivated, "UNO" misdescribed |
| Clarity & Presentation | 52 | Developing | Related work is thin and leaves out SR |
| Novelty & Originality | 33 | Developing | Incremental (script verdict: C2 incremental, C1 medium) |
| Significance & Impact | 40 | Developing | Useful target, unproven benefit |
| Experimental Validation | 35 | Developing | No domain diagnostics, missing neural-operator baselines |
| Reproducibility | 42 | Developing | Optimizer only |
| Ethical Compliance | 60 | Competent | No issues |

### NeurIPS-style: Quality 1 · Clarity 2 · Significance 2 · Originality 1
### Limitations: Partially (Sec. 5.2.3; uncertainty deferred to Sec. 5.3).
### Ethics Review Flag: No
### Overall: **2 (Reject).** Confidence: **4**. The paper is a reasonable workshop-level application note, but it does not clear the ICLR novelty and evidence bar.

---

## Reviewer 3: Perspective

# Peer Review Report
## Reviewer: Ravindra Kalinowski, Perspective (geophysical fluid dynamics department; fictional persona)
## Expertise: ocean turbulence diagnostics; data assimilation; implicit neural representations
## Date: 2026-11-10

### Summary
The paper tries to give oceanographers a learned tool that turns coarse surface-current fields into finer ones at user-chosen resolution, and to give ML practitioners a temporal neural-operator surrogate that can be queried at several resolutions. It tests on a synthetic turbulent flow and on 128×128 patches of the Copernicus surface-current product, and it reports honestly that skill drops at 8×.

### Strengths
**S1: Practical motivation that matters.** Oil-spill trajectories, larval dispersal and sediment transport (Sec. 5.1) depend on fine-scale currents, and a cheap resolution-flexible emulator would be valuable to coastal users.

**S2: The pipeline composes ideas cleanly.** Interpolation-kernel mixing (meta-upsampling), gradient-field processing and diffusion refinement (Sec. 3.2) are the sort of building blocks that classical multigrid, wavelet and implicit-representation methods would recognise, which suggests good transfer potential.

**S3: Candid limits discussion (Sec. 5.2.3).** The authors say outputs "oversmooth" or "hallucinate details" at high factors and propose uncertainty quantification (Sec. 5.3), which is the right instinct for a safety-adjacent application.

### Weaknesses (framed as opportunities)

**W1: The observation model is idealized.** Coarse inputs are average-pooled copies of the same field (Sec. 3.1, 4.2). A real coarse product differs from a pooled fine one: it comes from different model physics, assimilation and altimetry gaps (Sec. 3.1 itself says the product mixes altimetry, in situ data and models). Average pooling also yields a clean low-pass response that a real sensor does not. Skill on the pooled-then-recovered task therefore overstates skill on real coarse data. Opportunity: evaluate on two different products (e.g., a coarse operational model vs a finer regional one) or with a noisy, differently filtered degradation.
- **Suggested Fix**: add a degradation-robustness test (noise, Gaussian blur, subsampling instead of pooling).

**W2: Physical consistency is claimed but not shown.** "Physical conservation laws are softly enforced through a softmax constraint layer" (Sec. 3.2) is not explained. Softmax-type constraints preserve a sum of non-negative quantities, whereas velocity components are signed, and incompressibility (Eq. 2, ∇·u = 0) is a different constraint. No divergence, vorticity or kinetic-energy-spectrum diagnostic appears, and no ablation shows the layer does anything. For oceanographic users the spectra and divergence are what show whether the downscaled field is dynamically plausible.
- **Suggested Fix**: state exactly which quantity is conserved, and plot energy spectra and divergence for each model.

**W3: Assumptions behind the NS surrogate task.** The NS data are a doubly periodic, forced flow at ν = 1e-4 on a 64×64 grid (Sec. 3.1). The 16×16 coarse version removes most of the dynamically active scales, so "prediction" at 16×16 is closer to predicting a smoothed field. The evaluation reports five-step error only (Sec. 3.4, Table 1). Whether the surrogate stays stable over rollouts and conserves enstrophy is unknown. Scale assumption: ocean surface currents are far less turbulent per pixel than this NS setup, so the Copernicus results do not test the same regime.
- **Suggested Fix**: add multi-step rollouts and a regime comparison.

**W4: Hallucination risk in deployment.** Sec. 5.2.3 admits the models "hallucinate details", and Sec. 5.1 motivates search-and-rescue-adjacent uses. Without uncertainty estimates the deployment story is premature. (The authors already list uncertainty quantification as future work in Sec. 5.3, so I treat this as an acknowledged limitation to prioritize, not a hidden flaw.)
- **Suggested Fix**: add ensemble spread or conformal intervals for at least one model, and a coastal-mask handling note (land cells are not discussed).

### Cross-disciplinary connections
Implicit neural representations (LIIF-style) answer "output at any coordinate" without a fixed grid, and could be compared directly. Classical multigrid and wavelet multiresolution analysis give a principled way to relate the 16/32/64/128 hierarchy. Data assimilation would give a proper observation operator. Scale-selective verification (spectral coherence, fractions skill score) from numerical weather prediction is standard for downscaling skill.

### Questions for Authors
1. Would the 2× and 4× rankings survive with subsampling or noise instead of average pooling? (Survival would raise Significance.)
2. What does the "softmax constraint layer" constrain for signed velocity components?
3. How are land points and coastlines treated in the 128×128 patches?

### Dimension Scores (0–100)
**Pool position:** better than about 34% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting, usable-in-principle application with candid limits, but the evidence that it works on real coarse data is thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Physical layer unexplained, no diagnostics |
| Clarity & Presentation | 55 | Competent | Understandable motivation |
| Novelty & Originality | 45 | Developing | Sensible combination, little that is new |
| Significance & Impact | 52 | Developing | Application relevant, evidence thin |
| Experimental Validation | 42 | Developing | One run, idealized observation operator |
| Reproducibility | 45 | Developing | Few details |
| Ethical Compliance | 62 | Competent | Limitations candid; hallucination risk noted |

### NeurIPS-style: Quality 2 · Clarity 2 · Significance 2 · Originality 2
### Limitations: Partially. Good candour, no mitigation yet.
### Ethics Review Flag: No (no human data; hallucination risk is a limitations point, not an ethics-review trigger)
### Overall: **3 (Borderline Reject).** Confidence: **3**. I like the direction, but at ICLR the evidence has to carry more weight than the potential.

---

## Reviewer 4: Generalist

# Peer Review Report
## Reviewer: Ximena Aldous-Park, Generalist (university ML group; fictional persona)
## Expertise: deep learning broadly (generative models, representation learning)
## Date: 2026-11-10

### Summary
**The contribution in one paragraph.** The paper wraps a Fourier-operator downscaler (DFNO) in several variants and tests them on two things. A synthetic Navier–Stokes forecast task checks that a temporal version predicts five frames at 16×16, 32×32 and 64×64. A real ocean-current task checks recovery of fine fields from pooled coarse patches at 2×, 4× and 8×. It reports that the neural operators beat a pair of CNN baselines by a large margin and that all methods degrade at 8×.

### Strengths
**S1: A clear, simple pipeline and an understandable task (Sec. 3.2, Fig. 1).** A reader outside the sub-area can follow what goes in and what comes out.

**S2: Multiple scale factors and both losses reported (Tables 2–4)**, giving a fairly complete picture of how each variant behaves as difficulty increases.

**S3: The limitations section says plainly where things break (Sec. 5.2.3)**, and future work is concrete (Sec. 5.3).

**S4: Real data, with public provenance (Sec. 3.1, reference "Copernicus Marine Service, 2025").**

### Weaknesses

**W1: The main claim is not supported by the evidence presented, and the paper's structure hides this.** The paper is a short workshop paper (footer: "ICML 2025 Workshop"). The comparative evidence is two CNN baselines whose numbers look broken (MAE 0.424 and SSIM ≈ 0.1 in Tables 2–4), no interpolation baseline, one run and 100 test patches. A reader cannot tell whether DFNO variants are good or the CNNs are bad. At ICLR the evaluation has to show that the proposed ideas, not the lineage from DFNO, deliver the gains.
- **Suggested Fix**: strong baselines (bicubic, SR network, FNO, generative), variance, and an ablation table.

**W2: Contribution framing is unclear and overclaimed.** Sec. 1 lists a benchmark and a surrogate, while the abstract also claims a "supervised deep learning framework" that is "arbitrary resolution regardless of the input resolution". Experiments use one input size. "Multiscale" in the title refers to multiple output grids, not to multiscale physics. "To the best of our knowledge, this is the first work…" is not supported (see R2).
- **Suggested Fix**: state one or two precise claims and match each to a table.

**W3: Presentation puts the results in the wrong place and omits definitions.** Sec. 4.2 is two sentences. The real result discussion sits under "5. Discussion" (Sec. 5.2.1–5.2.2). Tables 2–4 do not say which models were trained for which factor, which split they report, or how PSNR/SSIM were computed (Sec. 3.4 points to an appendix that lacks them). Figure 3 appears next to Sec. 4.2 but, from its caption, shows only DFNO predictions, so the Sec. 4.2 statement that DFNO keeps "sharp gradients better than other baselines" has no visual comparison against any baseline (figures not viewable; judged from captions). Figure 1's description of the architecture is a block list without equations or sizes.
- **Suggested Fix**: merge results into Sec. 4, define metrics, add a small protocol table.

### Venue criteria checklist (ICLR: Soundness / Presentation / Contribution)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Claims supported by evidence (Soundness) | Not met | Tables 1–4; see W1 |
| Methods reproducible from the text | Not met | Sec. 3.2 (no sizes), App. A |
| Clear presentation | Partly | Sec. 4–5 structure |
| Significant contribution beyond prior work | Not met | Sec. 1–2; DFNO lineage |
| Relevance to ICLR audience (representation/operator learning for science) | Partly | Sec. 2.1; the ML novelty is slim |
| Honest limitations | Met | Sec. 5.2.3 |

**What the community loses if it is rejected:** little. A cleaner version with strong baselines would be useful as an application note. **Typical-of-accepted?** The weaknesses here (missing strong baselines, one run, no ablations, undefined metrics, unsupported priority claim) occur together and are typical of rejected submissions, not of accepted ones.

**Minor:** typos ("the proposed models has successfully", "standard FNO. the rest of"), "DFNO2/DFNO-2" naming, "∼9 km"/"∼8 km" mismatch.

### Questions for Authors
1. Which single claim do you want the paper judged on? (A scoped claim and an ablation would raise my Contribution score.)
2. Can you state exactly which factors each model was trained on?
3. Can the Copernicus experiments be repeated with bicubic and one SR baseline?

### Dimension Scores (0–100)
**Pool position:** better than about 20% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central empirical comparison is uninformative and the ML contribution is incremental over one cited paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | See W1 |
| Clarity & Presentation | 50 | Developing | Understandable, results misplaced, metrics undefined |
| Novelty & Originality | 36 | Developing | Variants of DFNO |
| Significance & Impact | 40 | Developing | Niche, unproven |
| Experimental Validation | 34 | Developing | Weak baselines, single run |
| Reproducibility | 42 | Developing | Few details |
| Ethical Compliance | 58 | Competent | Nothing at stake |

### NeurIPS-style: Quality 1 · Clarity 2 · Significance 2 · Originality 1
### Limitations: Yes (adequate for a workshop paper).
### Ethics Review Flag: No
### Overall: **2 (Reject).** Confidence: **4**.

---

## Devil's Advocate

# Devil's Advocate Report
## Paper: Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents
## Reviewer: Dmitri Fenwick-Osei, evaluation-methodology group (fictional persona)

## Steelman
Neural operators are resolution-agnostic by design, and extending Yang et al.'s DFNO to a temporal setting lets one trained model forecast PDE fields at several output resolutions without a numerical solver. On a real ocean-current product, DFNO-family models recover fine fields far better than CNNs at 2× and 4×. The authors openly describe the 8× degradation.

## Core Argument Chain
1. P1: FNO-style operators are resolution-agnostic, and DFNO-style up-sampling gives zero-shot arbitrary factors (Sec. 2.1, 2.3).
2. P2: A temporal version predicts NS frames at 16×16, 32×32 and 64×64, "comparable" to DFNO-2/4 (Table 1, Sec. 4.1).
3. P3: On Copernicus patches, DFNO variants beat CNN baselines by ~30× in MAE (Table 2, Sec. 5.2.2).
4. P4: Physical constraints are enforced (Sec. 3.2).
5. P5: Degradation at high factors reflects physics, not the models (Sec. 5.2.3).
∴ A general, resolution-agnostic neural surrogate and a useful ocean downscaler have been demonstrated.

## Strongest Counter-Argument
The paper never establishes that any learned model is better than trivial interpolation, and it never tests that its output resolution is independent of input resolution. Every comparative result on real data is against two CNNs whose numbers are implausible for the task. MAE is 0.424 to three digits in Tables 2, 3 and 4 whatever the output size or loss, with SSIM about 0.1 (Tables 2–4). The inputs are average-pooled copies of the target, so plain bicubic upsampling would score far above that. The "30× improvement" (Sec. 5.2.2) therefore cannot be read as evidence for neural operators or for any new variant. The DFNO family is itself the prior method, so the paper's own variants are separated from DFNO by gaps no larger than a few percent from a single run on 100 test patches. At 4×, SpecDFNO's MAE gain over DFNO is 10% (Table 3), and Temp SpecDFNO differs from Temp DFNO by at most 0.8% (Table 1). At 8× six different configurations return nearly the same numbers (MAE within 0.0002, SSIM spread under 0.001, Table 4), which suggests the models output a common fallback, and the paper explains it as "physical reality" (Sec. 5.2.3) without testing it. On the temporal task the "match DFNO" claim compares against numbers copied from another paper for a different task, and it fails at 32×32 against DFNO-2 (Table 1). Finally, "arbitrary resolution independent of input" is tested at one input size and three power-of-two factors. A reasonable skeptic can say the paper currently shows that a pre-existing method works on a smooth field when the metric is saturated by a broken baseline, and nothing more. The authors need a bicubic and an SR baseline, matched DFNO runs, seeds, and an input-resolution sweep.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The evidence supports a weaker claim (DFNO-type models recover smooth pooled fields at 2×), which is fixable by narrowing claims and adding baselines. I found no test-set selection (protocol sweep: no statement that tuning, checkpointing or selection used the reported split), no contradiction of the main claim by the paper's own results, and no fabrication signal.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Tables 2–4, Sec. 5.2.2 | CNN baselines look non-functional; "30×" is uninformative; no interpolation baseline | Bicubic, SR network, FNO under matched training |
| DA-M2 | Scope | Abstract, Sec. 1, Sec. 3.4 | "Arbitrary resolution regardless of input resolution" tested at one 16×16 input and three integer factors | Input/output grid sweep, non-integer factors |
| DA-M3 | Logic | Sec. 5.2.1, Table 1 | "Match, and in some cases outperform" DFNO-2/4: mixed, different tasks, copied numbers | Re-run DFNO-2/4 on the paper's data; add persistence/FNO baselines |
| DA-M4 | Evidence | Table 4 | Six configurations collapse to the same numbers; explained by "physical reality" untested | Check outputs, add bicubic, show spectra |
| DA-M5 | Integrity of results | Table 3 | Implied peak value varies 5.3–36.2 across rows (PSNR vs MSE inconsistent) | Recheck the MSE/PSNR columns |
| DA-M6 | Overclaiming | Sec. 1, Sec. 5.2.1 | "First" priority claim; "combined the predictive power of a classic numerical solver" with no solver comparison | Remove or support with solver accuracy/runtime |
| DA-M7 | Alternative explanation | Sec. 3.1, 3.4 | Patch-level leakage possible (regions, dates, overlaps not given); no variance | Spatially/temporally disjoint splits; seeds |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Clarity | Sec. 3.2 | SpecDFNO's second operator "predicts the residual between the initial FNO output and the ground truth", unclear at inference |
| DA-m2 | Clarity | Sec. 5.2.2 | "SpecDFNODiff provides marginal improvements" vs a 30–46% MAE reduction at 2× over SpecDFNO (Table 2) and slight worsening with L2 at 4× and 8× (Tables 3–4) |
| DA-m3 | Integrity | Sec. 3.2 | "softly enforced through a softmax constraint layer": mechanism unspecified for signed fields |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| MAE improvement vs CNN (Sec. 5.2.2) | "30×" | 0.424 / 0.0137 = 30.9 | Yes (to a degenerate baseline) |
| Temp DFNO vs DFNO-2, 32×32 MAE (Table 1) | "match/outperform" | 0.017426 / 0.0124 = 1.41 (worse) | No |
| Temp DFNO vs DFNO-4, 64×64 MAE (Table 1) | "match/outperform" | 0.019775 / 0.0168 = 1.18 (worse) | No |
| Split ratio (Sec. 3.1 vs App. A.2) | 70/15/15 | 800/200/100 → 72.7/18.2/9.1; 7000/2000/1000 → 70/20/10 | No |
| PSNR vs MSE consistency (Tables 2, 3, 4) | PSNR = f(MSE) | Constant P in Tables 2 and 4; P from 5.3 to 36.2 in Table 3 | Table 3 No |
| SpecDFNO vs DFNO at 4×, MAE (Table 3) | "most robust" | 0.03653 / 0.04057 − 1 = −10% | Yes, a small gap from one run |

## Ignored Alternative Explanations
1. The CNN gap may come from a broken or mis-evaluated CNN pipeline, not from spectral operators.
2. Bicubic upsampling of average-pooled inputs may already match the DFNO family at 2×.
3. Variant-to-variant differences may be seed noise (single run; 100 test patches).
4. Gains at 4× may reflect added capacity (SpecDFNO has two operators) rather than the residual design.
5. Spatial or temporal autocorrelation between neighbouring patches may inflate skill if splits are random.
6. The 8× collapse may be an optimization or pipeline issue, not an information-content limit.

## Missing Stakeholder Perspectives
Operational oceanographers and coastal responders (who would act on hallucinated structure), and users of coastal areas where land masks and boundary currents make patches non-periodic. Neither is discussed (Sec. 5.1 mentions applications only).

## Observations (Non-Defects)
- The zero-shot 64×64 readout (Sec. 3.4, Table 1) is the right kind of test for the surrogate claim, even though only one input size is used.
- The authors disclose that DFNO-2/4 numbers are copied (Table 1 caption).
- Large-factor failure is reported rather than hidden (Table 4, Sec. 5.2.3).

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 36 | Table 3 inconsistency, collapsed rows, untested claims |
| Clarity & Presentation | 50 | Results misplaced, metrics undefined |
| Novelty & Originality | 32 | Incremental over DFNO |
| Significance & Impact | 34 | Benefit over trivial interpolation unproven |
| Experimental Validation | 28 | Broken/weak baselines, one run |
| Reproducibility | 38 | Few details |
| Ethical Compliance | 56 | Nothing at stake; limitations honest but a hallucination risk is untreated |

**Pool position:** better than about 12% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the baselines that carry the main claim are not credible.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

All weaknesses were checked for specificity, "not already answered" (full-text and appendix search), consistency with the paper, and actionability. Scores were not changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W6 (protocol) | Rewritten | The first draft said "no train/val/test statement". Sec. 3.1 and A.2 do give a split, so it was narrowed to the unstated reporting/selection split and the inconsistent ratios (ERR-1). |
| R1 | Draft point on missing hardware/runtime | Moved to Minor (omission sweep) | Not tied to a claim except the surrogate's speed, which is covered in W4. |
| R2 | Draft W: "no comparison with Transolver/FactFormer/LSM is a critical omission" | Rewritten (W3) | The paper only names them as related work. They are published baselines for PDE benchmarks, but a missing baseline is MAJOR at most. |
| R2 | W2 UNO naming | Kept, marked [verify] | The paper's expansion and lack of a citation are verified in the text. The correct name rests on the reviewer's knowledge and could not be confirmed by title search. |
| R2 | W5 OceanNet venue | Rewritten as a check item | Verified title differs from the listed one; correctness of the printed venue not established, so stated as "should be checked". |
| R3 | Draft W: "no uncertainty quantification" | Rewritten (W4) | Sec. 5.3 already lists it as future work, so it is an acknowledged limitation. |
| R3 | Draft W on "no ethics statement" | Dropped | No human data or misuse potential. Sec. 5.1 and 5.2.3 cover applications and limits. |
| R4 | W3 "Fig. 3 lacks baselines" | Rewritten with caption-only caveat | Figures not viewable, so the claim is limited to what captions say. |
| R4 | Typos | Moved to Minor | Cosmetic. |
| DA | DA-m2 "marginal improvements" | Kept as MINOR | Verified against Table 2 (−46% / −30% MAE) but the paper's conclusion does not rely on it. |

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer, Part A: package for the EIC

**Official score** (`aggregate_scores.py`, before EIC weights, DA-CRITICAL list empty): ratings R1 2, R2 2, R3 3, R4 2, DA 2 → mean **2.20**; official composite **41.7**; no spread above 20 points (largest: Significance, 18); the script printed no consistency warnings (R3's Overall 3 sits one step above its composite band 2).

**Merged issues and classes**
| Issue | Sources | Class |
|-------|---------|-------|
| CNN baselines look broken; no interpolation or SR baseline; "30×" uninformative | R1-W1, R4-W1, DA-M1, R2-W3 (baselines) | CONSENSUS-4 |
| Single run, tiny test set, differences within noise | R1-W3, R4-W1, DA-M7, DA counter-argument | CONSENSUS-3 |
| "Arbitrary resolution regardless of input" untested | R1-W2, R4-W2, DA-M2 | CONSENSUS-3 |
| Priority claim and incrementality over DFNO | R2-W1, R4-W2, DA-M6 | CONSENSUS-3 |
| Table 1 comparison with copied DFNO-2/4 numbers | R1-W4, DA-M3 | CONSENSUS-2 |
| Protocol and reproducibility gaps (regions, splits, factors, metrics, code) | R1-W6, R4-W3, DA-M7 | CONSENSUS-3 |
| No ablations or parameter counts | R1-W5, DA-m1 | CONSENSUS-2 |
| Physical-consistency claim unsupported | R3-W2, DA-m3, R1 C5 | CONSENSUS-3 |
| Table 3 MSE/PSNR inconsistency | R1 ERR-2, DA-M5 | CONSENSUS-2 |
| Idealized observation operator (pooling) | R3-W1, R2-W4 | CONSENSUS-2 |
| Misnamed/uncited UNO | R2-W2 | SOLO |
| Table 4 collapse | R1 ERR-5, DA-M4 | CONSENSUS-2 |

**SPLIT:** R3's Overall 3 and Significance 52 against four reviewers at Overall 2 and Significance 34–40. **DA-CRITICAL:** none. **Outcome could hinge on:** the CNN baseline issue, the input-resolution claim, and Table 3.

## EIC Meta-Review (Halvard Mbeki-Lindqvist)

### The Case For and Against
- **For acceptance:** The paper addresses a useful application (ocean-current downscaling from a global product) with an architecture that is, in principle, resolution-flexible. The temporal extension and zero-shot 64×64 readout are a reasonable idea, and the authors describe the failure at 8× openly. A cleaned-up version would make a sensible application note.
- **Against acceptance:** The main empirical comparison is against CNN baselines whose numbers are implausible and unchanged across tables. The central "arbitrary resolution regardless of input resolution" claim is tested at one input size. The ML contribution is a few uncontrasted variants of a cited prior (DFNO). There is a single run on 100 test patches, a numerically inconsistent Table 3, and no ablation, physical diagnostic or comparison with simple interpolation. The short workshop paper is far from ICLR's bar.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| CNN MAE ≈ 0.424 identical across Tables 2–4 and L1/L2; SSIM ≈ 0.1 | R1-W1, DA-M1, R4-W1 | Tables 2–4 | **Verified** (numbers) / **Partly correct** (cause) | Numbers are as printed. "Mis-trained or mis-evaluated" is an inference; the absence of a bicubic baseline row is verified ("bicubic" appears only as an upsampling option in Sec. 3.2 and Fig. 1 and inside the CNN evaluation description in Sec. 3.4) |
| "30×" = 0.424/0.0137 | R1-W1 | Sec. 5.2.2, Table 2 | **Verified** | 30.9, recomputed |
| Every experiment uses a 16×16 input and integer power-of-two factors | R1-W2, DA-M2, R4-W2 | Sec. 3.4, 4.2, 5.2.2; Tables 1–4 | **Verified** | The "regardless of input resolution" wording is in the abstract and Sec. 1 |
| Table 3 PSNR/MSE inconsistent (implied P 5.3–36.2) | R1 ERR-2, DA-M5 | Table 3 | **Verified** | Recomputed rows (e.g., DFNO L1 0.01749/33.15 → P = 36.2; DUNO L1 0.0032/32.19 → P = 5.3). Tables 2 and 4 are consistent |
| Table 1: Temp DFNO not "match/outperform" DFNO-2 at 32×32 | R1-W4, DA-M3 | Table 1, Sec. 5.2.1 | **Verified** | 0.017426 vs 0.0124 MAE; 0.000573 vs 0.0004 MSE. It is better than DFNO-4 there |
| Table 1 comparison is across different tasks and copied numbers | R1-W4 | Table 1 caption, Sec. 4.1 | **Partly correct** | Copying is disclosed. Whether the data match is unverifiable (Yang et al. not provided). The paper does not state it either |
| Split ratios inconsistent | R1 ERR-1 | Sec. 3.1 vs App. A.2 | **Verified** | |
| PSNR/SSIM details "provided in the Appendix" are absent | R1 ERR-4, R4-W3 | Sec. 3.4, App. A | **Verified** | |
| Table 4 rows collapse to nearly the same numbers | R1 ERR-5, DA-M4 | Table 4 | **Verified** (numbers) / **Partly correct** (collapse to "fallback" is an inference) | MAE within 0.0002, SSIM spread < 0.001; MultiGrad L1 MSE 0.00894 is the one outlier. The paper's own explanation (Sec. 5.2.3) is untested |
| SpecDFNO "robust across all scales" | R1 ERR-3 | Sec. 5.2.2, Table 2 | **Verified** | +60% / +35% MAE vs DFNO at 2× |
| "First" priority claim | R2-W1, DA-M6 | Sec. 1 | **Partly correct** | The sentence is narrow ("neural surrogate", temporal), so not strictly contradicted. It rests on no comparison and ignores the cited FNO/DFNO resolution invariance |
| "UNO" is mis-named/uncited | R2-W2 | Sec. 3.2 | **Partly correct** | Lack of citation and the expansion are in the text. The correct name rests on R2's knowledge and is marked [verify] |
| Softmax constraint layer unexplained | R3-W2, DA-m3 | Sec. 3.2 | **Verified** (unexplained) | The suitability for signed fields is the reviewers' reasoning, not checked against Harder et al. text |
| "SpecDFNODiff provides marginal improvements" | DA-m2 | Sec. 5.2.2, Table 2 | **Verified** | Mixed: −46%/−30% MAE at 2×, +6–7% worse with L2 at 4× and 8× |
| Fig. 3 shows only DFNO | R4-W3 | Fig. 3 caption | **Partly correct** | Judged from the caption only; figures not viewable |
| Literature: DFNO is the closest prior work | R2 | Sec. 1, 2.3 | **Verified** | The paper cites and differentiates it; script flags it (cosine 0.306) |

No leakage evidence: searches for "test set", "selected", "tuned", "checkpoint", "early stopping", "seed", "variance" found no statement of selection on the reported split.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | **1.25** | Every numerical claim checked out (ERR-1 to ERR-6); the error log found the Table 3 inconsistency; minor overreach only in interpreting Table 4 and the CNN cause |
| R2 (Domain) | 2 | 4 | **1.0** | Sound and calibrated; one item (UNO name) is unverified from the paper alone; literature addendum accurate to the kept abstracts |
| R3 (Perspective) | 3 | 3 | **1.0** | Role-appropriate and consistent with the paper; Overall 3 is somewhat generous but within its stated pool position (34) |
| R4 (Generalist) | 2 | 4 | **1.0** | Calibrated; the caption-only figure claim is correctly caveated |
| DA | 2 | 4 | **1.0** | All major arguments survived the check; no CRITICAL raised, which was correct |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so there is nothing to uphold or downgrade, and **the DA ceiling is none**.

### Final Decision and Justification
The EIC-weighted rating is **2.16**, giving a starting point of **2 (Reject)**. The official mean is 2.20. The composite cross-check agrees (EIC-weighted 41.4, official 41.7: band 2). I keep the starting point: no verified issue was missed by the lower ratings and no low rating rests on a point the paper answers. The one SPLIT (R3: Overall 3) rests on potential and application relevance, which I weigh, but the verified evidence problems (CNN baseline numbers, the untested "regardless of input resolution" claim, an inconsistent Table 3, no variance, no ablation, a priority claim that is not established) are things R3's own weaknesses also list. **My pool position: better than about 18% of ICLR submissions.** The deciding evidence is that the central comparison (Tables 2–4) is uninformative and the headline conceptual claim is tested at one input size. A typical rejected submission shows these signals (weak or missing baselines, claim not tested, known idea presented as new), and an accepted paper would show a clear capability or finding, which the paper does not yet establish. The paper is not treated as a new-task paper: the task (arbitrary-resolution downscaling) is established and DFNO already exists. The decision does not exceed the DA ceiling (none). Fixing the issues requires new experiments, so a rebuttal-window recovery to acceptance is unlikely.

**Final (EIC): 2 (Reject).** ICLR rating (script): 2 on {0,2,4,6,8,10} (3 on the older {1,3,5,6,8,10} scale).

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate_scores.py --venue iclr`, with EIC weights R1 1.25, others 1.0)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 38 | 42 | 48 | 42 | 36 | 41.2 | 40.8 | 12 |
| Clarity & Presentation | 52 | 52 | 55 | 50 | 50 | 51.8 | 51.7 | 5 |
| Novelty & Originality | 35 | 33 | 45 | 36 | 32 | 36.2 | 35.8 | 13 |
| Significance & Impact | 36 | 40 | 52 | 40 | 34 | 40.4 | 39.8 | 18 |
| Experimental Validation | 30 | 35 | 42 | 34 | 28 | 33.8 | 33.3 | 14 |
| Reproducibility | 40 | 42 | 45 | 42 | 38 | 41.4 | 41.2 | 7 |
| Ethical Compliance | 60 | 60 | 62 | 58 | 56 | 59.2 | 59.1 | 6 |
| **Composite** | 39.5 | 41.8 | 48.8 | 41.6 | 37.1 | **41.7 (before)** | **41.4 (after)** | |
| Pool position (P%) | 15 | 18 | 34 | 20 | 12 | | | |

**Official ratings:** R1 2, R2 2, R3 3, R4 2, DA 2 → mean **2.20** · official composite **41.7**. **EIC assessment (internal):** weighted rating **2.16** → starting point **2** · weighted composite **41.4** → band 2 · **DA ceiling:** none · **Final (EIC): 2**. No dimension is flagged ⚠ (spread > 20).

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 1 |
| Rating | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) |
| Venue-weighted composite | 41.0 (band 2, no DA cap) |

The ICLR scale is not official wording ("secondary": recent analyses). Emphasis weights are the skill's heuristics.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Multiscale Neural PDE Surrogates for Prediction and Downscaling: Application to Ocean Currents" to ICLR.

The paper tackles a worthwhile problem: producing finer ocean-current fields than a global 0.08° product offers. It does so by extending a Fourier-neural-operator downscaler to time-dependent and several static variants.

**Overall Assessment:** The panel found the application relevant and the pipeline easy to follow, and valued your plain account of where skill drops at 8×. It judged that the evidence does not yet support the headline claims, and that the machine-learning contribution is a modest extension of the cited DFNO.

**Key Strengths Identified by Reviewers:**
1. A relevant real-data application and a zero-shot 64×64 evaluation of the temporal surrogate (R1-S1, R2-S1, R3-S1).
2. Reporting of several scale factors, both losses, and the failure regime (R1-S2/S3, R4-S2/S3, R3-S3).
3. Clear lineage and positioning relative to DFNO (R2-S2).

**Key Concerns Requiring Attention:**
1. The CNN baselines in Tables 2–4 have implausible, near-constant numbers (MAE 0.424, SSIM ≈ 0.1) and no interpolation or super-resolution baseline, so the "30×" gain is uninformative (R1, R4, DA; CONSENSUS-4).
2. "Arbitrary resolution regardless of the input resolution" is tested with one 16×16 input and three power-of-two factors, and the priority claim ("first") is not established against FNO/DFNO and arbitrary-scale super-resolution work (R1, R2, R4, DA; CONSENSUS-3).
3. Single runs, 100 test patches, no ablations, undefined metrics, an inconsistent Table 3 (MSE vs PSNR) and unexplained identical results at 8× in Table 4 (R1, DA).

**Critical Challenge (Devil's Advocate):** none rated CRITICAL. The DA's strongest objection is that the paper does not show any learned model beating plain interpolation, or that output resolution is independent of input resolution, and that the variants are separated from DFNO by gaps within what one run can produce. The authors need to address this directly.

**Decision: Reject (2).** The decision follows the EIC-weighted rating (2.16) and the composite cross-check (41.4). Resolving the issues needs new experiments rather than rewording.

**Path forward:** A resubmission with matched strong baselines (bicubic, an SR network, FNO and DFNO under the same protocol), seeds and variance, an input/output-resolution sweep including non-integer factors, ablations, spectral and divergence diagnostics, and a precisely scoped novelty claim would be a substantially different paper and would be assessed on its merits. This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome.

Sincerely,
Halvard Mbeki-Lindqvist
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| CNN baselines non-functional, no interpolation/SR baseline | R1, R2, R4, DA | CONSENSUS-4 |
| Single run / tiny test set / noise-level differences | R1, R4, DA | CONSENSUS-3 |
| Arbitrary-resolution claim untested | R1, R4, DA | CONSENSUS-3 |
| Incrementality and priority claim over DFNO | R2, R4, DA | CONSENSUS-3 |
| Protocol and reproducibility gaps | R1, R4, DA | CONSENSUS-3 |
| Physical-consistency claim unsupported | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the paper is a borderline application contribution | R3 (Overall 3) | R1, R2, R4, DA (Overall 2) | Evidence problems R3 itself lists (W1–W3) outweigh potential; EIC keeps the starting point 2 |

### Score Spread Discussion
No dimension exceeds the 20-point flag (largest spread: Significance, 18, with R3 the high scorer at 52). R3 is the only reviewer in the 30–54 pool band (34). The others sit below 30. The EIC adopts the majority view because R3's own weaknesses imply a lower position.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| (no CRITICAL) | — | — | — | n/a | n/a |
| DA-M1 | MAJOR | CNN baselines broken, no interpolation baseline | Yes: R1-W1, R4-W1, R2-W3 | n/a | n/a |
| DA-M2 | MAJOR | Input-independence untested | Yes: R1-W2, R4-W2 | n/a | n/a |
| DA-M3 | MAJOR | Table 1 claim vs copied numbers | Yes: R1-W4 | n/a | n/a |
| DA-M4 | MAJOR | Table 4 collapse | Yes: R1 ERR-5 | n/a | n/a |
| DA-M5 | MAJOR | Table 3 PSNR/MSE inconsistent | Yes: R1 ERR-2 | n/a | n/a |
| DA-M6 | MAJOR | "First" and "predictive power of a numerical solver" overclaims | Partly: R2-W1 | n/a | n/a |
| DA-M7 | MAJOR | Possible patch leakage, no variance | Partly: R1-W3/W6 | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix). Verified as undermining a main claim
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | CNN baselines non-functional; no interpolation or SR baseline | R1-W1, R4-W1, DA-M1, R2-W3 | Tables 2–4, Sec. 3.4, 5.2.2 | Add bicubic, trained SR net (single-scale and arbitrary-scale, e.g., LIIF-style), plain FNO and DFNO under matched training; show a sanity check of the CNN pipeline | Med; ~30–60 GPU-h | Partly (interpolation: Yes; trained baselines: tight) |
| P1-2 | "Arbitrary resolution regardless of input resolution" untested | R1-W2, R4-W2, DA-M2 | Abstract, Sec. 1, 3.4, Table 1 | Sweep (input, output) pairs, add non-integer factors, plot error vs factor | Low–Med; ~10 GPU-h | Yes |
| P1-3 | Table 1 comparison to copied DFNO-2/4 and no temporal-task baselines | R1-W4, DA-M3 | Table 1, Sec. 4.1, 5.2.1 | Re-train DFNO-2/4 on the paper's NS data; add persistence, FNO-3D/UNet forecaster, solver cost, multi-step rollout | Med–High; ~40 GPU-h | Partly |
| P1-4 | Single runs; unreliable rankings | R1-W3, DA-M7 | Tables 1–4 | 3–5 seeds, paired bootstrap, spatially/temporally disjoint split | Med; ~20–40 GPU-h | Partly |
| P1-5 | Table 3 MSE/PSNR inconsistent; Table 4 identical rows | R1 ERR-2, ERR-5, DA-M4, DA-M5 | Tables 3, 4 | Recheck and re-run, define metrics, add bicubic at 8×, verify outputs differ from interpolated input | Low–Med | Yes |
| P1-6 | Priority claim and incrementality over DFNO | R2-W1, R4-W2, DA-M6 | Sec. 1, 3.2 | Remove "first"; add a novelty-delta table vs Yang et al., Lütjens et al., arbitrary-scale SR | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| P2-1 | No ablations or parameter counts | R1-W5 | Parameter-matched ablations of meta-upsampling, Sobel, residual operator, diffusion | Med; ~30 GPU-h | Partly |
| P2-2 | Physical constraint unexplained, no diagnostics | R3-W2, DA-m3 | State the constraint; add energy spectra, divergence, vorticity | Low–Med | Yes |
| P2-3 | Idealized observation operator; no real coarse product | R3-W1, R2-W4 | Test other degradations; compare with an independent finer model or in situ data | Med–High | No |
| P2-4 | Protocol gaps: regions, dates, patches, reporting split, training factors, metrics | R1-W6, R4-W3, ERR-1, ERR-4 | Add a protocol table and appendix definitions; fix split ratios | Low | Yes |
| P2-5 | Missing references and component naming | R2-W2, W5 | Add Meta-SR, LIIF, Lütjens et al., Liu et al., Kovachki et al.; fix/cite U-NO [verify]; check the OceanNet entry | Low | Yes |
| P2-6 | Text–table mismatches (SpecDFNO "all scales", Diff "marginal") | ERR-3, DA-m2 | Rewrite Sec. 5.2.2 from the tables | Low | Yes |
| P2-7 | Hallucination risk, no uncertainty | R3-W4 | Ensemble/conformal intervals for one model | Med | Partly |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Move results from Sec. 5 into Sec. 4; fix typos and naming | R4 | Restructure |
| N2 | Helpful references (FourCastNet; Hess et al.) | R2 | Cite as context |
| N3 | Cross-disciplinary comparisons (implicit neural representations, multigrid, fractions skill score) | R3 | Discuss in related work |
| N4 | "~9 km" vs "~8 km"; "e. a." author lists | R1, R2 | Fix |

## Estimated Revision Effort
- Priority 1: 6 items, about 3–5 weeks (roughly 100–200 GPU-hours).
- Priority 2: 7 items, about 2–3 weeks.
- Priority 3: 4 items, a few days.
- **Total estimated revision time:** about 6–8 weeks for a substantially new submission.

*Literature check ran in strict mode (5 of 12 queries: claim 2, baseline 1, expansion 2; no gaps left). Recent and concurrent preprints were listed only as "worth discussing" and none were required. U-NO is marked `[verify]`.*
