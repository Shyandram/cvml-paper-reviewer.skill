# Academic Paper Review — Forget-It-All (FIA): Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking

*Simulated panel review (full mode, skip confirmation, literature check: strict, cutoff 2025-09-24). The outcome is a simulation of how a careful panel would likely see this draft, not a prediction. Figures were not available (text extraction only): figure-dependent claims (Figs. 3, 4, 5, 6, 7–10) are judged from captions and text and marked unverifiable where it matters. All five reviewer passes were performed sequentially by one model context; they are role-based passes, not independent agents.*

---

## Phase 0 — Field Analysis and Reviewer Configuration

### 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking |
| Primary Discipline | Computer Vision / ML → text-to-image diffusion models → concept erasure (machine unlearning) |
| Secondary Discipline(s) | Neural-network pruning / sparsity; AI safety and copyright compliance |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Training-free unstructured weight masking of Stable Diffusion FFN layers; activation-and-weight saliency; prompt-contrast (concept vs base prompts); mask fusion |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle) |
| Venue-Specific Notes | Public OpenReview process; revised PDF possible during discussion; base rate ≈ 27% accepted |
| Paper Maturity | Submission-ready (appendix with ablations; code promised, not yet released) |
| Ethics-Relevant Content | Generative model safety (NSFW erasure, I2P prompts), artist-style removal (copyright), dual-use (the same machinery could also be used to censor); no human subjects |

### Claimed Contributions (as stated by the authors, §1)
1. **C1** — "first work to explore multi-concept unlearning through unstructured neuron masking" (a sparsity perspective; each concept a neuron mask).
2. **C2** — A training-free, plug-and-play framework (Contrastive Concept Saliency, Eqs. 1–2; Concept-Sensitive Neurons, Eqs. 3–6; mask fusion preserving Concept-Agnostic Neurons, Eqs. 7–8).
3. **C3** — State-of-the-art unlearning across multi-object, multi-style and explicit-content tasks "at under 0.3% overall sparsity".

### Paper memory (factual record shared with all reviewers)
- **Setup:** Stable Diffusion v1.5 (SD v1.4 additionally for explicit content, §4.1); Imagenette (10 classes) scored by a pretrained ResNet-50 (§4.2); I2P with NudeNet at confidence 0.6 (§4.3); 5 artists × 200 titles with CLIP-based CLIPa and FSR (§4.4, Eq. 9); MS COCO-30K for FID/CLIP (§4.1); 50 denoising steps; one RTX A6000 (§4.1).
- **Splits / selection:** no train/validation/test notion; hyperparameters r1, r2, α are set per task or per concept (Table 8, App. B.2), selected by observing forgetting accuracy ("easy-to-forget / hard-to-forget", App. B.2). Number of generated images per class, evaluation prompt templates, and seeds are **not stated after search** (only "seed to 0" for the 50-class run, Table 21 caption; "same random seed" for paired FSR images, §4.4).
- **Baselines:** official code, "recommended configurations unless otherwise specified" (App. F); SA and MACE partly copied from their papers (Table 3 dagger).
- **Headline numbers:** Avg forgetting accuracy 1.9% (Table 1; SD v1.5 90.34); CLIP 29.56 (Table 1; SD 31.42); Overall Score 86.0 (Table 2); NudeNet total 743 → 32 on SD v1.4 (Table 3), FID 14.02, CLIP 31.18; artist average rank 2.5, CLIPa 27.45, FSR 83.4 (Table 4); "under 0.3%" sparsity (§1, §5), Table 9 shows ≈ 0.06% pruned.
- **Appendix adds:** prompt templates (Tables 6–7), hyperparameters (Tables 8–9), ablations on α / layer / granularity (Tables 10–14), attack robustness (Table 15), SD v1.5 NudeNet (Table 16), runtime/memory (Table 17), ±std tables (18–20), a 50-class extension (Table 21, Fig. 6).
- **Unverifiable:** all figures (3–10), including the 50-class curves in Fig. 6 and the α curves in Fig. 5; the PDF-extracted Tables may have lost bolding.

### Integrity scan
`scripts/integrity_scan.py` found one hidden character (a soft hyphen). No text addressed to reviewers or AI systems. Nothing to report to the EIC beyond that. The reviewers read the redacted copy.

### 👥 Review Team (fictional personas)

**EIC (meta-reviewer): Prof. Adaeze Okonkwo-Lindqvist**, large public research university (Northern Europe). Senior faculty / generative models and trustworthy ML. Reads all five reports, checks decisive points, weights, decides. Style: AC who asks "would I reject on this alone?" and calibrates to what ICLR actually accepts.

**Reviewer 1 (Methodology): Dr. Soo-min Verhaegen**, industrial research lab (East Asia). Mid-career industry scientist / diffusion-model evaluation, unlearning benchmarks. Style: recomputes every table, insists on equal tuning effort for baselines.

**Reviewer 2 (Domain): Prof. Lucía Ferrandiz-Okoye**, vision and generative-modeling group, public university (South America). Senior faculty / concept erasure, network pruning literature. Style: reads the cited abstracts before accepting a novelty claim.

**Reviewer 3 (Perspective): Dr. Rajiv Thornbury**, security and signal-processing group, research university (North America). Mid-career / adversarial robustness of generative models, media forensics, content policy. Style: constructive, looks for deployment and misuse angles.

**Reviewer 4 (Generalist): Dr. Mei-Ling Aaberg**, computer vision group, technical university (Northern Europe). Postdoc/early-career faculty / typical program-committee member, not an unlearning specialist. Style: asks whether a non-specialist can follow and whether the venue's audience cares.

**Devil's Advocate: Prof. Emeka Dalgaard**, statistics and evaluation-methodology department, university (Oceania). Senior faculty / evaluation validity, causal reasoning. Style: rigorous skeptic; steelman first.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1 — Independent Reports

# Peer Review Report (Reviewer 1 — Methodology)

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Reviewer: Dr. Soo-min Verhaegen, Methodology Reviewer (industrial research lab, East Asia; fictional persona)
## Expertise: diffusion-model evaluation; concept-erasure benchmarks; generative metrics
## Date: 2026-11-10

### Protocol sweep (searched the full text and appendix)
- Selection statements: "if pruning the target concept causes a significant drop in the model’s forgetting accuracy to that concept, the concept is deemed easy-to-forget" and "requiring only a few iterations to select the optimal α for each task" (App. B.2). Per-concept r2 values in Table 8 (3.0 for parachute, golf ball, gas pump; 0.7 for the rest).
- Evaluation set: no separate validation notion; the number of generated images per class, evaluation prompt templates and seeds are **not stated** after search (Sec. 4.2 says only "using the same evaluation setup as the baselines").
- Baseline protocol: "report all baseline results using the recommended configurations unless otherwise specified" (App. F).

### Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | first multi-concept unlearning via unstructured neuron masking | §1 | related work (CP, MS cited) | Partially (ConceptPrune already prunes neurons; see R2) |
| C2 | training-free, "minimal hyperparameter tuning", plug-and-play | Abstract, §1 | Table 8, App. B.2 | Partially: three hyperparameters set per task/concept using the evaluation metric |
| C3a | best forgetting while "maintaining semantic fidelity and image quality" | Abstract | Tables 1–5 | Partially: forgetting yes; quality drop is real (CLIP 31.42 → 29.56, Table 1) |
| C3b | SOTA at "under 0.3% overall sparsity" | §1, §5 | Table 9 | Unclear: Table 9 shows ≈ 0.06%; the 0.3% figure is not derived anywhere |
| C3c | robustness (App. D) | App. D | Table 15 | Partially (metrics undefined; 4 baselines absent) |

## Summary
The paper proposes FIA, a training-free method that scores weight connections in Stable Diffusion by comparing activations under concept prompts and bare-context prompts, aggregates scores over denoising timesteps, selects top fractions per channel and per layer, and removes the union of concept masks except for connections shared by at least a fraction α of the concepts. It evaluates multi-object (Imagenette), nudity (I2P) and five-artist erasure against eight to nine baselines, reporting the lowest forgetting accuracy in most settings and competitive FID/CLIP.

## Strengths
### S1: Broad evaluation across three task families with many baselines
Tables 1–5 compare against 8–9 methods on objects, explicit content and styles, plus runtime (Table 17), robustness (Table 15) and a 50-class extension (Table 21/Fig. 6). This breadth is above the norm for unlearning papers.
### S2: Informative ablations of the fusion step and the pruned layer
Table 12 isolates the effect of keeping concept-agnostic neurons (naive 1.6% forgetting at CLIP 28.32 vs α = 0.6: 1.9% at 29.46). Table 13 shows pruning location matters sharply (FFN2 1.9% vs cross-attention value 73.4%).
### S3: Cost reporting and honest limitation
Table 17 reports ≈ 11 s per concept and flat memory (≈ 2.95–2.99 GB); §5 admits quality drops for hundreds of concepts.
### S4: Careful pairing in the Overall Score of Table 2
The authors explicitly decline to bold preserving accuracy because "high values may result from failing to forget any concepts" (Table 2 caption) and use a harmonic mean.

## Weaknesses

### W1 (MAJOR): Hyperparameters are tuned per concept/task on the reported metric; baselines are not
App. B.2 states a concept is "hard-to-forget" when forgetting accuracy does not drop at the default and then uses r2 = 3 instead of 0.7 (Table 8: parachute, golf ball, gas pump); α is chosen per task from forgetting curves (Fig. 5) and "a few iterations to select the optimal α". These values produce the headline numbers (Tables 1, 2, 4). Baselines use "recommended configurations" (App. F) that were not designed for 10-concept or 5-style erasure. This contradicts "minimal hyperparameter tuning" (Abstract) and gives FIA a tuning advantage. The text is also internally inconsistent: App. B.2 says r2 = 1 is "sufficient in most cases", Table 8 lists 0.7 and 3.0 (no 1.0 for objects).
- **Suggested Fix:** fix one global (r1, r2, α) before looking at the evaluation classifier, report FIA at it for all tasks; tune on held-out concepts/prompts (e.g., a different Imagenette-like class set) and evaluate on the original ones; give each baseline a comparable small search (e.g., ESD/SalUn strength, MACE LoRA rank). Cost ≈ 10–20 GPU-hours.

### W2 (MAJOR): Headline components are not ablated; only α, layer and granularity are
Contributions list Contrastive Concept Saliency (Eqs. 1–2) and time-integrated sensitivity (Eq. 3) as novel, yet App. C ablates only α (Table 12), pruned layer (Tables 10, 13) and granularity (Tables 11, 14). Missing: |W|·‖X‖ alone (a magnitude-times-activation score), dropping the cosine factor in Eq. 1, dropping −σb in Eq. 2, using the mean-only or frequency-only term in Eq. 3, and a no-base-prompt variant. Eq. 3 adds a mean saliency (arbitrary scale) to a frequency in [0, 1] with "equal weight"; without ablation it is unclear that the second term contributes.
- **Suggested Fix:** add a component-removal table on Imagenette 10 and I2P (about 6 variants × 2 tasks, a few GPU-hours since the method is training-free).

### W3 (MAJOR): Quality and preservation claims are stronger than the evidence
(i) Table 1: FIA CLIP 29.56 vs SD 31.42; six of eight baselines are higher (AC 31.58, MACE 31.05, SPM 30.77, FMN 30.56, ESD 30.12, SalUn 29.93). §4.2 calls these "marginally higher CLIP scores"; the largest gap (AC, 2.02) exceeds FIA's own loss to SD (1.86). No FID is reported for the 10-class setting in the main paper. (ii) Table 2 has no SD v1.5 column; from Table 1 the original model's mean accuracy on the preserved classes 6–10 is (93.5 + 98.2 + 86.9 + 98.4 + 94.7)/5 = 94.3, so FIA's preserving accuracy of 76.7 (recomputed 76.4, see Error Log) is an ≈ 18-point loss, in line with SalUn (77.4) and SPM (76.5), not "high preservation quality". (iii) Style and explicit tasks measure preservation only on COCO; no non-target artists or other body-related prompts are tested.
- **Suggested Fix:** add the SD v1.5 row to Table 2; report FID and a second text-alignment metric on Imagenette prompts for non-target classes; add retained-artist and retained-person/clothed-body prompts.

### W4 (MAJOR): Single run, "± 0.0" for FIA; evaluation protocol under-specified
Tables 18–20 add ± std "to reflect the rigor", but FIA, CP and UCE rows show "± 0.0" everywhere (e.g., Table 18, FIA Avg Acc "1.9 ± 0.0"), i.e., FIA has no measured variance; Table 21 fixes "seed to 0". Differences between FIA and CP in Table 4 (CLIPa 27.45 vs 27.90) and FID in Table 3 (14.02 vs SD 14.04, i.e., below the unmodified model) are within the scale at which FID/CLIP vary with seed. Number of images per class, evaluation prompts and classifier thresholds are not stated (Sec. 4.2).
- **Suggested Fix:** 3–5 generation seeds for all methods on Tables 1–4 (generation-only, ≈ 5 GPU-hours per seed on COCO-30K), state images/class and prompts.

### W5 (MAJOR): Forgetting metrics can be satisfied by degraded rather than unlearned generation
Forgetting accuracy (Table 1; 0.0% for three classes) and CLIPa/FSR (Eq. 9: success "whenever the edited image yields a lower CLIP score than the original") reward any image change. FSR counts a success for a blur as much as for an erasure; CLIPa as defined cannot distinguish "style removed" from "prompt ignored". Table 3's "Genitalia (M)" for FIA (8) is above unmodified SD v1.4 (7).
- **Suggested Fix:** add a human or classifier-based check that target prompts still yield coherent images of the *base context* (the paper's own "base prompt"), and a style classifier for artists.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E1 | Table 2 / Table 19, SalUn "Forgetting Acc [1–5]" | "22.3" | Row values 7.2, 16.9, 43.1, 1.3, 8.1 sum to 76.6, mean 15.3, not 22.3; the SalUn Overall Score then becomes ≈ 80.9, not 77.5 | Recomputed from the 5 rows | High | MAJOR (changes a reported baseline, not the ranking) | Correct Table 2/19 |
| ERR-2 | E1 | Table 2 / Table 19, "Preserving Acc [6–10]" | "76.7" (FIA), "71.9" (UCE), "52.4" (CP), "76.5" (SPM) | Row means are 76.4, 72.9, 53.7, 76.8. UCE Overall becomes ≈ 82.3 (reported 81.7), FIA ≈ 85.8 (reported 86.0); FIA lead over UCE shrinks from 4.3 to ≈ 3.5 | Recomputed | High | MINOR–MAJOR (ranking unchanged) | Recompute all aggregates |
| ERR-3 | E6 | Table 1 vs Tables 12/13/14 | "29.56" vs "29.46" | Same α = 0.6 / FFN2 / "Both" configuration reports CLIP 29.56 in Table 1 but 29.46 in Tables 12–14; gas pump forgetting 5.0 (Tables 1, 13) vs 5.4 (Table 12) | Cross-reference | High | MINOR | Reconcile or explain |
| ERR-4 | E6 | Table 3 vs Tables 10, 11 | "31.18" vs "31.38" | FIA total 32 detections has CLIP 31.18 in Table 3 and Table 10 (FFN2) but 31.38 for "Both" in Table 11 (same total 32) | Cross-reference | High | MINOR | Reconcile |
| ERR-5 | E1 | Table 5 vs Table 4 | "27.90" (CP) | Table 5 per-artist values 27.94, 25.33, 28.01, 28.15, 29.67 average 27.82; Table 14 "Layer" mean 2.88 printed as 2.8 | Recomputed | High | MINOR | Fix |
| ERR-6 | E6 | App. B.2 vs Table 8 | "setting the sparsity ratio r2 = 1 and the concept-agnostic ratio α = 0.6 is sufficient in most cases" | Table 8 lists r2 = 0.7 or 3.0 for all ten objects, never 1.0 | Cross-reference | High | MINOR | State actual rule |
| ERR-7 | E6 | Table 9 | "0.061581" etc. | Implied total weight count differs by row (e.g., 1348/0.000325% ≈ 4.1e8 vs 6014/0.001937% ≈ 3.1e8), so the percentage columns cannot all be consistent; unit (percent vs fraction) not stated | Derived | Medium | MINOR | Clarify units |

### Minor
Table 10 header reads "Imagenette classes" but contains I2P body-part rows; "neurons" denotes individual weight connections (Eq. 1) which is non-standard; Eq. 3's T is "the total number of denoising steps" while App. B.2 speaks of "the first 10 unlearning steps" (unclear which timesteps enter Eq. 3).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Method sound in outline; tuning asymmetry and unablated components |
| Clarity | 3 | Readable; layer choice only in App. C |
| Significance | 2 | Useful practical tool; evidence short of a convincing gain |
| Originality | 2 | Incremental over neuron pruning for erasure |

## Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: baselines at default configurations vs FIA tuned per concept on the evaluation metric; headline components unablated; single run with "± 0.0".

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Protocol asymmetry, uncontrolled selection, aggregate errors in Table 2 |
| Clarity & Presentation | 62 | Competent | Clear writing; inconsistent hyperparameter statements |
| Novelty & Originality | 52 | Developing | See R2; closest prior CP |
| Significance & Impact | 55 | Competent | Practical, but narrow evidence |
| Experimental Validation | 48 | Developing | Broad but not controlled; no variance; metric validity |
| Reproducibility | 50 | Developing | Code "in the near future" (§7); per-concept settings; eval images/prompts unstated |
| Ethical Compliance | 62 | Competent | Brief statement; no dual-use discussion |

## Questions for Authors
1. Were the evaluation prompts (classifier-scored generations) different from the Appendix B.1 mask-identification prompts (e.g., "a golf ball in a clubhouse")? Overlap would raise concerns; disjoint prompts would lower them.
2. How would FIA at fixed r2 = 0.7 and α = 0.6 for all ten objects score in Table 1? A flat result would raise my score.
3. How were single-concept baselines (FMN, AC, ESD, SalUn, CP) extended to ten concepts: sequentially, merged, or jointly?
4. What is the SD v1.5 row of Table 2, and the FID of Table 1 methods?
5. Why are FIA's, CP's and UCE's stds exactly 0.0?

## Limitations Assessment
**Partially.** §5 acknowledges degradation at hundreds of concepts; it does not discuss tuning cost, preservation loss (~18 points on retained classes), or reliance on a single evaluation classifier.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a plausible, cheap method with encouraging numbers, but the tuning asymmetry, missing component ablations and uncontrolled quality claims leave the central "SOTA" claim only partly supported.

## Confidence
**4**: Confident; re-computed tables, but figures were unavailable.

---

# Peer Review Report (Reviewer 2 — Domain)

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Reviewer: Prof. Lucía Ferrandiz-Okoye, Domain Reviewer (public university, South America; fictional persona)
## Expertise: concept erasure in diffusion models; neural network pruning
## Date: 2026-11-10

## Summary
FIA reframes multi-concept erasure as constructing and fusing sparse binary masks over Stable Diffusion's FFN weights, derived from activation-weighted saliency under concept versus context prompts. The paper positions itself against fine-tuning erasers (ESD, FMN, AC, SalUn, SA, SPM, MACE) and training-free methods (UCE, ConceptPrune) and claims state-of-the-art forgetting at very low sparsity.

## Strengths
### S1: Sensible multi-concept mechanism (Sec. 3.3)
Counting how many concept masks a connection appears in (Eq. 8) and keeping connections shared by ≥ ⌈αC⌉ concepts is a simple, interpretable rule, and Table 12 shows it recovers ≈ 1.1 CLIP points over the naive union.
### S2: Appropriate baseline family
Table 1 includes both fine-tuning and training-free methods, and the closest neuron-level work (CP, Chavhan et al., 2024) is both cited (§2) and compared empirically (Tables 1, 3, 4, 15).
### S3: Useful extra evidence for the sparsity view
Table 13 (FFN2 vs attention) and Table 9 (≈ 0.06% pruned) support the claim that very few connections matter, a result of independent interest.

## Weaknesses

### W1 (MAJOR): Novelty is incremental over ConceptPrune and the pruning literature; claim "first" is overstated
§1 states "first work to explore multi-concept unlearning through unstructured neuron masking". ConceptPrune (Chavhan et al., 2024) already identifies and prunes concept-specific FFN neurons without training; §2 dismisses it with "handling multiple concepts is difficult due to complex neuron interactions", but no experiment isolates this (Table 1 shows CP at 7.34% forgetting and the *lowest* CLIP, 27.93). Model Sparsity (Jia et al., 2023; cited as MS) already connects sparsity and unlearning. The saliency in Eq. 1 starts from |W|·‖X‖₂, the activation-aware pruning score of Wanda (Sun et al., ICLR 2024), which is not cited. The genuine delta (multi-concept fusion with concept-agnostic preservation; prompt-contrast with −σb; temporal aggregation) is real but each piece is a modest variant. Claim-level profile below: C1 incremental, C2 medium, C3 medium.
- **Suggested Fix:** narrow C1 to "multi-concept fusion for neuron-level erasure", cite and ablate Wanda-style scoring, and compare against a CP baseline given the same prompts and multi-concept union/fusion.

### W2 (MAJOR): Missing comparisons with prior (pre-cutoff) robust and scalable erasers
The baselines stop at 2024 CVPR/ICCV-era methods. Verified prior work is absent: SPEED (scalable, precise, efficient erasure; arXiv Mar 2025), AdvUnlearn (NeurIPS 2024) and Receler (ECCV 2024) for the robustness claims of App. D, SAFREE (ICLR 2025, a training-free competitor on I2P), and FADE (CVPR 2025), which evaluates on Imagenette and I2P (the same benchmarks). Per the literature rules these are at most MAJOR missing baselines, not grounds for rejection on their own.
- **Suggested Fix:** add SPEED and SAFREE to Tables 1/3/16, AdvUnlearn and Receler to Table 15; at minimum discuss them.

### W3 (MAJOR): Related-work descriptions and citations contain errors
§1 (Introduction) says "ESD (Gandikota et al., 2023) removes concept combinations via an LLM-derived concept graph", which describes a different method (the concept-graph approach of §2's "COGFD (Gandikota et al., 2023)"), while §2 describes ESD correctly as negative-guidance fine-tuning. §2's list for machine unlearning, "Jang et al., 2022; Podell et al., 2023; Vatter et al., 2023", includes SDXL (Podell) and a survey on distributed systems for graph neural networks (Vatter) as MU references per the bibliography. Tsai et al. 2023, Yang et al. 2024 and Zhang et al. 2024b (App. D) are absent from the reference list. COGFD has no bibliography entry.
- **Suggested Fix:** repair attributions; add missing entries.

### W4 (MINOR–MAJOR): The "multi-concept" claim is tested mostly on object classes
Explicit content uses two words and "a single concept … is sufficient" (Table 8 caption); styles use five artists. Only Imagenette (10, up to 50 in Fig. 6/Table 21) stresses the mechanism, and the 50-class result relies on a ResNet-50 that "can reliably identify" the classes (App. E). Celebrity/identity erasure, a standard MACE setting, is missing.
- **Suggested Fix:** add an identity-erasure or 100-concept style experiment.

## Literature-check addendum (strict mode, cutoff 2025-09-24)
7 queries (claim 3, baseline 2, expansion 2) via `related_search.py`, plus `similarity`, `scout`, `coverage`, `novelty`, `verify`; gap left open: no 2021–22 prior work (field started 2023). Similarity: closest prior works are SepME (cos 0.23), "Fantastic Targets for Concept Erasure" (0.22) and Receler (0.19); none above the 0.30 threshold; no text overlap (0 shared 8-grams).

| Claim | Dimension | Novelty | Top prior work (level, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------|-----------|
| C1 first neuron-masking multi-concept | method | incremental | ConceptPrune (4; prior arXiv-only; cited) | Same mechanism (training-free FFN neuron pruning for concepts); multi-concept scaling is the delta |
| C2 FIA framework | method | medium | ConceptPrune (3; cited) | Saliency, temporal/spatial selection and concept-agnostic fusion differ in detail |
| C3 SOTA multi-concept results | result | medium | SPEED (3; prior; not cited) | Claims only comparable on shared benchmarks; SPEED not compared |

Closest prior work as a whole: ConceptPrune (cited and differentiated, weakly).

**Novelty delta table**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| neuron masking for erasure | ConceptPrune (arXiv 2405.19237) | training-free FFN neuron pruning per concept | multi-concept fusion, saliency redesign | cited; differentiated by one unsupported sentence (§2) |
| sparsity ↔ unlearning | Model Sparsity Can Simplify Machine Unlearning (Jia et al., NeurIPS 2023) | sparsity as aid to unlearning | training-free masks for T2I | cited, one line |
| activation-weight saliency | Wanda (Sun et al., ICLR 2024) | |W|·‖X‖ score for pruning LLMs | + cosine term, prompt contrast | not cited |

**Baseline scout (I2P / Imagenette)**
| Benchmark | Prior method (label) | Reported in abstract | Compared? | Note |
|---|---|---|---|---|
| I2P, Imagenette | FADE, "Fine-Grained Erasure…" (CVPR 2025; prior peer-reviewed) | "at least a 12% improvement in retention performance" (retention, not forgetting) | No | settings differ; discuss |
| I2P | TRACE (recent preprint) | none | No | discuss only |
| I2P | SAEmnesia (concurrent) | none | No | discuss only |

**Field snapshot (as of the cutoff).** Around 2023 the dominant approach was fine-tuning (ESD, AC, FMN) per concept; 2024 brought scalable multi-concept editors (UCE closed-form; MACE; SPM adapters) and a robustness turn (adversarial attacks such as Ring-A-Bell and UnlearnDiffAtk; adversarial-training defences such as AdvUnlearn). Training-free guards (SAFREE and similar) and neuron- or feature-level methods (ConceptPrune, sparse-autoencoder approaches) emerged in 2024–25. Open problems: erasure that survives paraphrase and white-box attacks, preserving neighbouring concepts, and scaling to hundreds of concepts. A significant contribution now is a method that is robust to attacks *and* scales without quality loss, evaluated beyond CLIP and a single classifier; a lower forgetting number on Imagenette alone is incremental.

## Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | "SPEED: Scalable, Precise, and Efficient Concept Erasure for Diffusion Models", arXiv 2503.07392, 2025 (authors [verify]) | Directly addresses scalable multi-concept erasure; prior, found via `verify` |
| Important | Y. Zhang et al., "Defensive Unlearning with Adversarial Training for Robust Concept Erasure in Diffusion Models" (AdvUnlearn), NeurIPS 2024 | Robustness baseline for App. D |
| Important | C.-P. Huang et al., "Receler: Reliable Concept Erasing of Text-to-Image Diffusion Models via Lightweight Erasers", ECCV 2024 | Robust eraser; found via `verify` |
| Important | J. Yoon, S. Yu, V. Patil, H. Yao, M. Bansal, "SAFREE: Training-Free and Adaptive Guard for Safe Text-to-Image And Video Generation", ICLR 2025 | Training-free I2P competitor; found via `verify` |
| Important | M. Sun, Z. Liu, A. Bair, J. Z. Kolter, "A Simple and Effective Pruning Approach for Large Language Models" (Wanda), ICLR 2024 | Precedent for the |W|·‖X‖ score in Eq. 1 |
| Helpful | "Fine-Grained Erasure in Text-to-Image Diffusion-based Foundation Models" (FADE), CVPR 2025 (authors [verify]) | Evaluates on Imagenette and I2P |
| Helpful | "RECE: Reliable and Efficient Concept Erasure of Text-to-Image Diffusion Models" [verify] (not found on arXiv by title) | Closed-form competitor |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good coverage; missing newer baselines |
| Clarity | 3 | Understandable positioning but citation errors |
| Significance | 2 | Moderate |
| Originality | 2 | Incremental over ConceptPrune |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the core mechanism (training-free neuron pruning) exists in ConceptPrune and the gains are measured on a narrow, self-tuned protocol; the fusion rule is a real but modest advance.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Method coherent; selection/ablation gaps (see R1) |
| Clarity & Presentation | 64 | Competent | Clear exposition; reference errors |
| Novelty & Originality | 50 | Developing | Incremental claim-level profile |
| Significance & Impact | 56 | Competent | Practical; no robustness leap |
| Experimental Validation | 52 | Developing | Baselines stop short of 2025 methods |
| Reproducibility | 52 | Developing | Code promised, not released |
| Ethical Compliance | 65 | Competent | Brief statement adequate for no-human-data paper |

## Questions for Authors
1. What exactly fails when ConceptPrune is applied with FIA's prompts and the same ten concepts (the claim in §2)? A matched experiment would raise my Novelty score.
2. How does FIA differ empirically from SPEED and SAFREE on I2P/Imagenette?
3. Is the Eq. 1 score a deliberate extension of Wanda's? Why not simply |W|·‖X‖?

## Limitations Assessment
**Partially.** Positioning relative to neuron-pruning for concept removal needs candid discussion.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: reasonable, incremental method whose novelty and relative performance claims are not established against the closest prior work.

## Confidence
**4**: Confident on the erasure literature; verified abstracts via the literature check.

---

# Peer Review Report (Reviewer 3 — Perspective)

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Reviewer: Dr. Rajiv Thornbury, Perspective Reviewer (security/signal-processing group, North America; fictional persona)
## Expertise: robustness of generative models; content moderation; pruning as signal selection
## Date: 2026-11-10

## Summary
FIA offers an operator-friendly route to remove a list of unwanted concepts from a deployed T2I model without retraining: compute saliency masks per concept, fuse, prune. The paper argues this enables regulation-compliant, plug-and-play deployment, and shows lower nudity counts, lower object recognizability and lower artist-style similarity than competing methods.

## Strengths
### S1: Deployment-friendly cost profile
Table 17 shows ≈ 11 s per concept and ≈ 3 GB peak memory regardless of concept count on one A6000; a practitioner with a takedown list can use the method without GPU clusters.
### S2: Adversarial evaluation is included
App. D / Table 15 evaluates Ring-A-Bell, MMA and UnlearnDiffAtk, which many unlearning papers omit; FIA obtains 87.9 / 96.8 on the first two and 61.7 on the third, the best of six methods.
### S3: Link to sparsity is conceptually attractive
Concept-specific connections being a tiny set (≈ 0.06%, Table 9) resonates with network-compression and neuroscience-style "sparse coding of concepts" views and suggests auditability: masks are explicit, storable, reversible artefacts (a mask can be re-applied to the original weights).

## Weaknesses

### W1 (MAJOR): Robustness claim needs definitions and a fuller comparison
Table 15 columns are marked "↑ ↑ ↓" with no definition of the metrics (presumably defence rate or attack success) and omits MACE, SPM, SalUn and AC from Table 15. If UnlearnDiffAtk "↓" is attack success, FIA still has 61.7%, only 3.1 points below CP (64.8): a white-box attacker largely recovers the concept. "Consistently achieves the best robustness" (App. D) overstates this.
- **Suggested Fix:** define metrics and thresholds; include all Table 1 baselines; report the attack success rate on FIA when the attacker knows the mask (adaptive attack).

### W2 (MAJOR): Real-world assumptions: concept lists, synonyms and re-learning
The method assumes the operator can name each target and supply five contextual placeholders (App. B.1; Table 6, 7). Erased concepts are tested only with template prompts; paraphrases, translations, and related concepts ("sexual" vs "nude", "French horn" vs "brass instrument") are not evaluated. Because masks are fixed binary edits on shared weights, a fine-tuner can restore them (the paper does not test fine-tuning recovery, relevant to open weights).
- **Suggested Fix:** add a paraphrase/synonym test set and a few-step fine-tuning recovery test.

### W3 (MINOR–MAJOR): Societal framing is thin
§6 states "this work does not raise ethical concerns" and does not discuss dual use (censorship of legitimate concepts such as artist styles or cultural content), fairness (do nudity masks disproportionately degrade images of particular body types or skin tones?), or the practical copyright question (removing a style is not removing training-data influence).
- **Suggested Fix:** add a short paragraph and a quick demographic-spread check on the I2P outputs.

### W4 (MINOR): Related fields
Sparse-autoencoder feature steering and activation steering are neighbours the paper never mentions (the literature search found 2025 work in this line); these suggest evaluating whether masks transfer across SD versions.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid breadth |
| Clarity | 3 | Clear |
| Significance | 3 | Practical |
| Originality | 3 | Mildly novel |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: broad, cheap, and appealing from a deployment view with some robustness evidence, offset by thin societal and generalization analysis.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound approach |
| Clarity & Presentation | 68 | Competent | Clear |
| Novelty & Originality | 62 | Competent | New recombination |
| Significance & Impact | 66 | Competent | Useful to practitioners |
| Experimental Validation | 60 | Competent | Wide, shallow in places |
| Reproducibility | 58 | Competent | Code promised |
| Ethical Compliance | 58 | Competent | Thin dual-use treatment |

## Questions for Authors
1. What do the three Table 15 metrics measure and with which thresholds? Clarity could raise my Significance score.
2. Does a mask survive a short LoRA fine-tune that re-teaches the concept?
3. Do masks computed on SD v1.5 transfer to SD v1.4/SDXL?

## Limitations Assessment
**Partially.** Scaling is discussed (§5); misuse, circumvention and recovery are not.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: a practical, inexpensive erasure tool with encouraging robustness evidence; I lean accept because the weaknesses (definitions, framing) are fixable.

## Confidence
**3**: Fairly confident; not an unlearning specialist.

---

# Peer Review Report (Reviewer 4 — Generalist)

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Reviewer: Dr. Mei-Ling Aaberg, Generalist Reviewer (computer vision group, Northern Europe; fictional persona)
## Expertise: image generation and recognition (not unlearning specifically)
## Date: 2026-11-10

## Summary (contribution in one paragraph)
The paper presents FIA, a way to remove several concepts from Stable Diffusion at once by zeroing a tiny set of weights found by contrasting responses to "a golf ball in a clubhouse" against "a clubhouse", with a rule to spare weights that many concepts share so that general image quality survives. Reported results show far lower recognizability of removed objects, fewer nudity detections and lower artist similarity than eight baselines at similar image quality, without training.

## Strengths
### S1: Clear problem and narrative (Sec. 1)
The motivation — single-concept erasers degrade or re-acquire concepts when stacked — is plain, and the two-type neuron story (sensitive vs agnostic) is easy to hold in mind.
### S2: Strong headline numbers across three standard tasks
Table 1 average forgetting 1.9% vs the best baseline 7.34% (CP); Table 3 total detections 32 vs 111–838 for baselines; Table 4 best average rank (2.5 vs 3.75).
### S3: Good appendix and practical cost reporting
Appendix B–E provide prompts, hyperparameters, ablations (Tables 8–14) and cost (Table 17).
### S4: Fits ICLR's audience
Safety and unlearning for generative models are active ICLR topics; the method is simple, which the venue values.

## Weaknesses

### W1 (MAJOR): Key design choices live only in the appendix, with conflicting statements
The main text (Sec. 3) defines everything for "a linear layer ℓ", but the method only prunes the second FFN projection (App. C, Table 13); which U-Net layers are processed, how Eq. 3's T relates to "the first 10 unlearning steps" (App. B.2), and how many prompts feed μc/μb (five placeholders per concept, App. B.1) are not in Sec. 3. App. B.2 says r2 = 1 while Table 8 says 0.7/3.0. A non-specialist cannot tell what "FIA" is from Sec. 3 alone.
- **Suggested Fix:** add a short algorithm box listing layers, prompts, and the exact defaults used per task; reconcile B.2 and Table 8.

### W2 (MAJOR): Claims in the abstract and conclusion outrun the evidence
"this work resolves the core trade-off between effective concept unlearning and generation quality" (§5) sits beside Table 1 (CLIP 29.56 vs 31.42 for SD), Table 4 (FID 16.7 vs 14.5 for SD) and the stated degradation for hundreds of concepts (§5). "FIA consistently outperforms state-of-the-art approaches across a range of unlearning tasks" (§1) is true for forgetting, not for quality (FIA is 5th of 8 in CLIP in Table 4 and below six of eight baselines in Table 1).
- **Suggested Fix:** tone down to "improves forgetting at a modest quality cost".

### W3 (MINOR–MAJOR): Figures carry the qualitative evidence but can't be verified from captions
Figures 3, 7–10 are central to judging whether target prompts yield sensible alternatives, and Figure 9 uses author-added masks; the paper doesn't state how prompts/seeds were chosen. *(Figures unavailable in this review.)*
- **Suggested Fix:** state selection (random seeds/prompts) and provide failure cases.

### W4 (MINOR): Presentation slips
Table 10's header "Imagenette classes" is wrong for explicit content; "neuron" for individual weight entries; Table 2 caption's best-value policy changes between tables.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Good experiments; some gaps |
| Clarity | 3 | Mostly clear |
| Significance | 3 | Moderate |
| Originality | 3 | Fine |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: consistent, large wins on three standard benchmarks with a simple method; tempered by overclaiming and under-described protocol.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound enough |
| Clarity & Presentation | 66 | Competent | Appendix-dependent |
| Novelty & Originality | 60 | Competent | Simple, new combination |
| Significance & Impact | 64 | Competent | Topical |
| Experimental Validation | 62 | Competent | Broad |
| Reproducibility | 56 | Competent | Code "in the near future" (§7) |
| Ethical Compliance | 62 | Competent | Brief |

## Questions for Authors
1. Which layers does FIA edit exactly? A clear answer in the main text would improve Clarity.
2. Why report CLIP as "marginally" lower given a 2-point gap?
3. Are the qualitative samples random?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: topical, simple and well-evaluated at first glance; presentation and claim calibration fixable, so reasons to accept marginally outweigh.

## Confidence
**3**: Fairly confident; I did not recompute the tables (see R1).

---

# Devil's Advocate Report

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Reviewer: Prof. Emeka Dalgaard, Devil's Advocate (statistics/evaluation methodology department, Oceania; fictional persona)

## Steelman
FIA is a cheap, training-free editor whose prompt-contrast saliency finds a very small set of FFN weights per concept; a sensible fusion rule spares weights shared across concepts. On three standard setups it achieves lower forgetting than most baselines while keeping COCO FID/CLIP in the same range as many of them, and it keeps working on 50 object classes.

## Core Argument Chain
1. Prompt-contrast saliency (Eqs. 1–3) isolates weights specific to a concept.
2. Removing them (with agnostic weights spared) erases the concept but not other capabilities.
3. Forgetting accuracy, CLIPa/FSR and NudeNet counts measure erasure; COCO FID/CLIP measures retained quality.
4. FIA beats baselines on those measures at < 0.3% sparsity without hyperparameter burden.
∴ FIA achieves reliable multi-concept unlearning with preserved quality and minimal tuning.

## Strongest Counter-Argument
The evidence supports "FIA, tuned per concept on the evaluation metric, reduces what the evaluation classifier or detector sees", but not "FIA erases concepts while preserving quality, with minimal tuning". First, all three erasure metrics are *detector-relative* and monotone in image damage: a ResNet-50 score of 0.0% (Table 1: cassette player, tench, church), a CLIP score that merely has to drop (Eq. 9, "we count a success whenever the edited image yields a lower CLIP score than the original"), and NudeNet counts can all be reduced by corrupting the images generated from the target prompts rather than by removing the concept. Only COCO prompts and five preserved Imagenette classes test the other side, and there FIA loses ≈ 18 points of recognition on preserved classes relative to the unmodified model (derived from Table 1 vs Table 2: 94.3 → 76.7), comparable to the baselines FIA is said to beat on "balance", and it loses 1.86 CLIP and 2.2 FID points (Table 1; Table 4). The Overall Score of Table 2 hides this by rating only against other edited models and by using a harmonic mean in which a nearly zero forgetting rate dominates. Second, the "hard-to-forget" rule (App. B.2) and α selection (Fig. 5) use the evaluation outcome to set r2 and α per concept/task, while baselines run at defaults (App. F). Third, there is no variance and no non-target-style or retained-concept test for styles and nudity. A skeptic would conclude that the paper has shown a strong *targeted-degradation* effect, with unlearning-specificity and tuning-free claims unproven.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim (lower detected forgetting) survives, and the selection of r2 per concept does not meet the held-out-test-selection criterion cleanly: no separate validation/test split exists, the selected α (0.6) is not the best-scoring option in Table 12 (0.8 gives 1.7%, naive 1.6% vs 1.9%) and was chosen on a quality trade-off (decision-table row 1), and the r2 rule is a stated procedure whose effect on the headline is untested (see DA-M1, rated MAJOR).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence/Protocol | App. B.2, Table 8, Fig. 5, App. F | r2 chosen per concept (3.0 for the hardest three) after observing forgetting accuracy ("deemed easy-to-forget"); α chosen per task from forgetting curves; baselines at "recommended configurations". Quote: "requiring only a few iterations to select the optimal α for each task". Headline Table 1 uses these values. Whether evaluation prompts overlap App. B.1 prompts is unstated. | Fixed global settings; held-out concepts/prompts; matched tuning for baselines |
| DA-M2 | Logic/Evidence | Tables 1, 2, 4; Eq. 9 | Forgetting metrics cannot distinguish erasure from damage; preservation tested on five classes only; ≈ 18-point preservation loss unlisted in Table 2 (no SD column) | SD row in Table 2; preservation sets for styles and NSFW; non-CLIP style classifier; human check |
| DA-M3 | Claim distortion (E5) | §5, Abstract, §4.2 | "this work resolves the core trade-off…"; "marginally higher CLIP scores" (gaps up to 2.02, Table 1); "minimal hyperparameter tuning" vs per-concept settings; "under 0.3%" vs Table 9 ≈ 0.06% | Reword; derive the 0.3% figure |
| DA-M4 | Scope | Table 8 caption, §4.3 | The explicit-content task uses two words, so "multi-concept" is shown only on objects (≤ 10, 50 in App. E) and 5 styles | Add identity/100-concept test |
| DA-M5 | Robustness | Table 15, App. D | FIA attack numbers: UnlearnDiffAtk 61.7 vs CP 64.8; baselines missing; metrics undefined; "consistently best" overstated | Define metrics; add all baselines |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of reporting | Tables 18–20 | "± 0.0" for FIA/CP/UCE while text says std added "to reflect the rigor" |
| DA-m2 | Consistency | Tables 1, 12–14 | CLIP 29.56 vs 29.46 for the same configuration |
| DA-m3 | Citation | §1, §2 | ESD misdescribed; Podell and Vatter as MU references; missing entries for Tsai, Yang, Zhang 2024b, COGFD |
| DA-m4 | Table arithmetic | Tables 2, 5, 14, 19 | See R1 Error Log ERR-1/2/5 (re-checked) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Table 1 FIA average | 1.9 | (0.5 + 0 + 0 + 1.7 + 1.8 + 1.9 + 4.8 + 0 + 2.9 + 5.0)/10 = 1.86 | Yes |
| Table 1 SD average | 90.34 | 903.4/10 | Yes |
| Table 2 FIA preserving | 76.7 | 382.1/5 = 76.42 | No (small) |
| Table 2 SalUn forgetting | 22.3 | 76.6/5 = 15.32 | **No** |
| Table 2 UCE Overall | 81.7 | HM(72.86, 94.46) ≈ 82.3 | No (small) |
| Table 4 FIA avg rank | 2.5 | ranks 1, 1, 3, 5 → 2.5 | Yes |
| Table 3 FIA total | 32 | 6 + 2 + 7 + 2 + 6 + 0 + 1 + 8 | Yes |
| Table 5 CP mean | 27.90 | 139.10/5 = 27.82 | No (0.08) |

## Ignored Alternative Explanations
- Image degradation on target prompts vs genuine concept removal (needs "base-context fidelity" checks).
- Prompt overlap between mask-estimation templates (App. B.1) and evaluation prompts.
- Per-concept r2 tuning explaining the gap to baselines run at defaults.
- A simple |W|·‖X‖ (Wanda-style) mask, or CP with the same prompts, may explain most of the gain.

## Missing Stakeholder Perspectives
Artists whose styles are removed vs those whose are retained; users of the edited model whose legitimate prompts hit shared weights (e.g., body-related prompts for medical or art-education use).

## Observations (Non-Defects)
Reporting ± std for baselines, the explicit refusal to bold preservation accuracy in Table 2, and the §5 scaling caveat are good practice. The ablations for layer and α are informative.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Metrics do not isolate erasure; tuning asymmetry |
| Clarity & Presentation | 58 | Clear but inconsistent |
| Novelty & Originality | 52 | Incremental |
| Significance & Impact | 54 | Limited by evidence |
| Experimental Validation | 44 | No variance; narrow preservation tests |
| Reproducibility | 50 | Code not released |
| Ethical Compliance | 60 | Minimal |

Pool position: better than about 50% of submissions to ICLR. Deciding evidence: validity of forgetting metrics and tuning asymmetry offset by consistent, large gaps.

## Overall: 3 | Confidence: 4

---

## Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 tuning | kept | Specific, quoted, not answered in appendix |
| R1 | W3 (ii) preservation ~18 pts | kept | Derived from Tables 1–2; checked |
| R1 | Error Log ERR-3…ERR-7 | moved to Minor line (not weaknesses) | Cosmetic/small; ERR-1/2 kept as E1 entries |
| R2 | W2 missing baselines | rewritten | Marked "at most MAJOR"; recent/concurrent works (TRACE, SAEmnesia, ACE) removed from requirements |
| R2 | W4 | kept as MINOR–MAJOR | Paper's own Table 8 caption supports |
| R3 | W4 related fields | moved to Minor | Suggestion only |
| R3 | W1 "Table 15 omits baselines" | kept | Verified in Table 15 |
| R4 | W3 figures | kept as question | Figures unavailable; cannot be an error |
| R4 | W4 | moved to Minor | Cosmetic |
| DA | CRITICAL none | n/a | Ruled in report |
| DA | DA-M3 "minimal tuning" | kept | Duplicates R1-W1 in part; merged in Phase 2 |

---

## Phase 2 — EIC Meta-Review and Decision

### Synthesizer, Part A — issue map
| Issue | Sources | Class |
|-------|---------|-------|
| Per-concept/per-task tuning on the evaluation metric; baselines at defaults | R1-W1, DA-M1, DA-M3 | CONSENSUS-2 (decisive) |
| Components (Eqs. 1–3) not ablated | R1-W2, R2-W1 (Wanda/CP) | CONSENSUS-2 |
| Quality/preservation overclaimed; ~18-pt preservation loss | R1-W3, R4-W2, DA-M2, DA-M3 | CONSENSUS-3 |
| Single run, "± 0.0" | R1-W4, DA-m1 | CONSENSUS-2 |
| Metric validity (erasure vs damage) | R1-W5, DA-M2 | CONSENSUS-2 |
| Novelty incremental vs ConceptPrune; Wanda | R2-W1, R4 (implicit) | SOLO |
| Missing prior baselines (SPEED, SAFREE, AdvUnlearn, Receler) | R2-W2, R3-W1 (robustness) | CONSENSUS-2 |
| Robustness metrics undefined | R3-W1, DA-M5 | CONSENSUS-2 |
| Citation errors | R2-W3, DA-m3 | CONSENSUS-2 |
| Layer choice / inconsistent hyperparameters in main text | R4-W1, R1-ERR-6 | CONSENSUS-2 |
| Multi-concept only shown on objects | R2-W4, DA-M4 | CONSENSUS-2 |
| Societal/dual-use framing thin | R3-W3 | SOLO |
| SPLIT: strength of evidence — R3/R4 "strong headline numbers" vs R1/DA "metric validity" | | SPLIT |
| DA-CRITICAL | none | n/a |

Official score (before EIC weights): computed with `aggregate_scores.py` (see Score Summary).

### EIC read of the paper
I read the abstract, contributions, Sections 3–4, App. B–E and recomputed Tables 1, 2, 4, 5, 10–14.

# Editorial Decision

## Paper: Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
## Submission ID: iclr26-UsWTBvkTwf (blinded)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Adaeze Okonkwo-Lindqvist; R1 Dr. Soo-min Verhaegen, R2 Prof. Lucía Ferrandiz-Okoye, R3 Dr. Rajiv Thornbury, R4 Dr. Mei-Ling Aaberg, DA Prof. Emeka Dalgaard

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40
**EIC assessment** (internal): weighted rating 3.31 → starting point 3 · **DA ceiling**: none · **Final (EIC)**: 3
Official composite 56.7 (BEFORE run, no EIC weights) · EIC-weighted composite 55.9 → band 3 (cross-check agrees, no ⚠) · ICLR target-venue translation of the final decision 3: **4 on {0,2,4,6,8,10}** (5 on {1,3,5,6,8,10}; scale status: secondary), Soundness 2 / Presentation 3 / Contribution 2. All from `aggregate_scores.py` (`before.json`, `aggregate.json`).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A cheap, training-free editor that, on three standard setups, gives markedly lower detected forgetting (Table 1: 1.9% vs 7.34% for the best baseline; Table 3: 32 vs 111–838 detections) with FID/CLIP in a usable range, scales to dozens of concepts (Table 17, Fig. 6) and reports an adversarial evaluation (Table 15). The topic is timely for ICLR and the method is simple.
- **Against acceptance:** The mechanism is an incremental step over ConceptPrune; the headline gains come from per-concept/per-task hyperparameters selected by the reported metric while baselines run at defaults; the erasure metrics cannot separate unlearning from damage, preservation loses ≈ 18 points on retained classes, key components are unablated, there is no variance, and several tables contain arithmetic or cross-table inconsistencies.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Per-concept r2 / per-task α selected using forgetting accuracy; baselines at recommended configs | R1-W1, DA-M1 | App. B.2, Table 8, App. F | **Verified** | Quotes present ("deemed easy-to-forget"; "recommended configurations"). Overlap with evaluation prompts is unstated, so the *size* of the effect is unknown |
| Table 2 aggregates wrong (SalUn 22.3→15.3, preserving means) | R1 ERR-1/2, DA | Tables 2, 19 | **Verified** | Recomputed; ranking of FIA first survives (FIA ≈ 85.8, UCE ≈ 82.3, SalUn ≈ 80.9) |
| ≈ 18-pt preservation loss, no SD column in Table 2 | R1-W3, DA-M2 | Tables 1, 2 | **Verified** | SD classes 6–10 mean 94.3 vs FIA 76.4–76.7 |
| "marginally higher CLIP" | R1-W3, R4-W2 | §4.2, Table 1 | **Verified** (authors' wording overstated) | gap up to 2.02 |
| Components of Eqs. 1–3 not ablated | R1-W2 | App. C | **Verified** | Only α, layer, granularity |
| Novelty incremental over ConceptPrune; Wanda uncited | R2-W1 | §1–2, Eq. 1 | **Verified** | CP is cited, compared, and differentiated only by one sentence |
| Citation errors (ESD description, Podell/Vatter, missing entries) | R2-W3, DA-m3 | §1, §2, App. D, References | **Verified** | |
| Robustness "consistently best" overstated | R3-W1, DA-M5 | Table 15 | **Partly correct** | FIA is numerically best on all three; margins small; metric undefined |
| Metrics reward damage (erasure vs degradation) | R1-W5, DA-M2 | Eq. 9, Tables 1, 4 | **Partly correct** | Mechanism plausible; no evidence in the paper of degradation (figures unavailable), so a concern, not a finding |
| Table 3 male-genitalia count above SD | R1-W5 | Table 3 | **Verified (minor)** | 8 vs 7 |
| Writing "clear"; layer choice in appendix only | R4-W1 | §3 vs App. C | **Verified** | |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC weight | Reason |
|----------|---------|------------|------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Errors verified by recomputation; decisive points correct; well calibrated |
| R2 (Domain) | 3 | 4 | 1.0 | Sound, mostly verified; novelty verdict matches claim-level profile |
| R3 (Perspective) | 4 | 3 | 0.85 | One overstated point ("consistently best" robustness) and fewer verified specifics; otherwise sound |
| R4 (Generalist) | 4 | 3 | 1.0 | Presentation points verified; did not check tables, as stated |
| DA | 3 | 4 | 1.1 | Core objections survive; "no CRITICAL" ruling is appropriate; counter-argument on metric validity only partly evidenced |

### DA-CRITICAL Rulings
None raised (DA-M1 is the closest: the AC test fails because no cleanly held-out split exists, α is not the best-scoring option in Table 12, and the fix is a rerun with fixed settings; I treat it as a major issue that weighs on the decision).

### Final Decision and Justification
The EIC-weighted rating is 3.31, so the starting point is Borderline Reject (3); the composite cross-check lands in the same band (see Score Summary). I keep 3. The paper is a competent, topical contribution whose reported margins are probably real in direction, but its weaknesses go beyond what typical accepted ICLR papers carry: the comparison is not equal-effort (tuned vs default), the two headline components are untested, quality loss is understated, and the arithmetic errors in Table 2/19 and the cross-table inconsistencies reduce trust. None is fatal, and all are fixable in a revision (fixed global settings, component ablation, SD row and variance, narrower claims), so this is a near-miss rather than a clear reject. No DA ceiling applies. Pool position (EIC): better than about 52% of ICLR submissions, on the reject side of the bar. A revised PDF with the fixes above, plus SPEED/SAFREE comparisons, could reasonably move it to Borderline Accept.

---

## Score Summary

Official scores and the EIC assessment: see `aggregate.json` / the script output (run twice: BEFORE without `eic_weight`, AFTER with the weights above and `--final 3`).

| Dimension | R1 | R2 | R3 | R4 | DA |
|-----------|----|----|----|----|----|
| Technical Rigor | 50 | 55 | 62 | 62 | 48 |
| Clarity & Presentation | 62 | 64 | 68 | 66 | 58 |
| Novelty & Originality | 52 | 50 | 62 | 60 | 52 |
| Significance & Impact | 55 | 56 | 66 | 64 | 54 |
| Experimental Validation | 48 | 52 | 60 | 62 | 44 |
| Reproducibility | 50 | 52 | 58 | 56 | 50 |
| Ethical Compliance | 62 | 65 | 58 | 62 | 60 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking" to ICLR. Removing several concepts from a deployed text-to-image model without retraining is a practical problem, and a training-free approach is attractive.

**Overall Assessment:** Reviewers agree the method is simple, cheap and shows much lower detected forgetting than most baselines on three standard tasks, and that the appendix is informative. They are divided on how much of the gain survives equal tuning effort and on whether the metrics isolate erasure from image damage.

**Key Strengths:** (1) breadth of tasks and baselines with runtime/memory reporting (R1, R3, R4); (2) a simple, interpretable fusion rule shown to help in Table 12 (R1, R2); (3) an adversarial robustness evaluation (R3).

**Key Concerns Requiring Attention:** (1) per-concept and per-task hyperparameters selected on the evaluation metric against default-configured baselines (CONSENSUS-2); (2) unablated headline components, no variance, and quality/preservation loss understated (CONSENSUS-3); (3) novelty relative to ConceptPrune and missing prior baselines (SPEED, SAFREE, AdvUnlearn, Receler).

**Decision: Borderline Reject (3).** The weaknesses are fixable and the direction is promising; what would change the decision is a fixed-hyperparameter result, component ablations, an SD v1.5 row and variance, and narrower claims.

Sincerely,
Prof. Adaeze Okonkwo-Lindqvist, Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Quality/preservation overclaimed | R1, R4, DA | CONSENSUS-3 |
| Tuning asymmetry | R1, DA | CONSENSUS-2 |
| Missing prior baselines / robustness completeness | R2, R3 | CONSENSUS-2 |
| Citation errors | R2, DA | CONSENSUS-2 |
| Layer choice and hyperparameter statements unclear | R1, R4 | CONSENSUS-2 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Do the numbers show a real gain? | R3, R4 (strong headline numbers) | R1, DA (protocol asymmetry, metric validity) | R1/DA verified specific problems; R3/R4 did not recompute. Direction of effect plausible, magnitude uncertain |

### Score Spread Discussion
Spreads > 20 points occur in Technical Rigor/Experimental Validation between R1/DA (44–50) and R3/R4 (60–62). The editor adopts the lower view because R1's and the DA's points were verified in text and arithmetic.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Tuning on evaluation metric, baselines at defaults | Yes (R1-W1) | n/a | New experiments |
| DA-M2 | MAJOR | Metrics reward damage; preservation loss | Yes (R1-W3, W5) | n/a | New experiments/analyses |
| DA-M3 | MAJOR | Claim distortion | Yes (R4-W2) | n/a | Clarification |
| DA-M4 | MAJOR | Multi-concept only on objects | Yes (R2-W4) | n/a | New experiments |
| DA-M5 | MAJOR | Robustness claim | Yes (R3-W1) | n/a | Minor additions |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Per-concept/per-task tuning against evaluation metric; unequal tuning | R1-W1, DA-M1 | App. B.2, Table 8, App. F | Fixed global (r1, r2, α); tuning on held-out concepts/prompts; small matched search for baselines | Medium; 10–20 GPU-h | Partly |
| R2 | Unablated core components (Eqs. 1–3), including Wanda-style and ConceptPrune-with-same-prompts controls | R1-W2, R2-W1 | Eqs. 1–3, App. C | Component-removal table on Imagenette-10 and I2P | Low–Medium; few GPU-h | Yes |
| R3 | Quality/preservation not fully reported and overclaimed; SD row and FID in Tables 1–2; non-target retention for styles/NSFW | R1-W3, DA-M2, DA-M3, R4-W2 | Tables 1, 2, 4; §4.2, §5 | Add SD row, FID, retained-concept tests; reword claims | Medium | Yes |
| R4 | No variance; "± 0.0" rows; evaluation protocol undefined | R1-W4, DA-m1 | Tables 18–20 | 3–5 seeds; state images/class and prompts | Medium; ~15 GPU-h | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Metric validity (erasure vs damage); style classifier or human study | R1-W5, DA-M2 | Add non-CLIP style/base-context checks | Medium | Partly |
| S2 | Missing prior baselines (SPEED, SAFREE, AdvUnlearn, Receler); FADE discussion | R2-W2 | Compare or discuss | Medium | Partly |
| S3 | Robustness metric definitions, all baselines in Table 15, adaptive attack | R3-W1, DA-M5 | Define and extend | Low–Medium | Yes |
| S4 | Table arithmetic and cross-table errors (ERR-1…7), Table 10 header | R1 Error Log | Recompute and reconcile | Low | Yes |
| S5 | Citation errors (ESD description, Podell/Vatter, missing Tsai/Yang/Zhang 2024b/COGFD) | R2-W3, DA-m3 | Repair | Low | Yes |
| S6 | Layer choice and defaults in main text; B.2 vs Table 8 | R4-W1, ERR-6 | Add algorithm box | Low | Yes |
| S7 | Multi-concept beyond objects (identity, many styles) | R2-W4, DA-M4 | Add one experiment | Medium | Partly |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Dual-use, fairness, recovery under fine-tuning, synonym/paraphrase test | R3-W2, W3 | Short analysis |
| N2 | "0.3%" vs 0.06% sparsity | R1, DA-M3 | Derive or correct |
| N3 | Related fields (SAE steering, activation steering) | R3-W4 | Mention |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 1–2 weeks (≈ 40 GPU-hours)
- Priority 2: 7 items, ≈ 1 week
- Priority 3: 3 items
- **Total estimated revision time**: ≈ 2–3 weeks
