# Simulated Panel Review — "Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization"

*Skill: academic-paper-reviewer v2.10.1 · Mode: full · Target venue: ICLR (stated) · Literature check requested: strict, cutoff 2025-09-24 · Date: 2026-11-10.*
*The five reviewer passes were performed sequentially by one model in a shared context (no subagents); independence is by role and by reading order only. This is a simulation of how a careful panel would likely see this draft, not a prediction. Figures were not available (text extraction only): figure-dependent claims are judged from captions and surrounding text and flagged where it matters.*

---

# Phase 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization |
| Primary Discipline | Machine learning → generalization of deep networks / training dynamics |
| Secondary Discipline(s) | Stochastic optimization (SGD noise, SDE view), representation similarity, applied probability (TV-distance bounds) |
| Paper Type | Analysis / Insight (composite weights: analysis). It also contains an informal theory section, but the contribution is empirical-phenomenological. |
| Core Technique(s) | "Composite networks" pairing shallow layers from checkpoint t1 with deep layers from checkpoint t2; prediction-agreement "consistency"; one-step SGD feature-perturbation covariance; sphericity test; TV-distance generalization bound |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle; scale status: secondary) |
| Venue-Specific Notes | none; ICLR form = Soundness / Presentation / Contribution (1–4), Rating, Confidence |
| Paper Maturity | Early draft / submission with conceptual (non-computable) theory |
| Ethics-Relevant Content | none (public image benchmarks; no human data). LLM-use disclosure present (§9). |

### Claimed Contributions (as stated by the authors, §1)
1. **C1 (method/framing):** "New lens on generalization": depth-decomposed framing where feature dynamics act as implicit, structured augmentations, operationalized via composite networks and temporal-consistency metrics.
2. **C2 (result):** "Robust empirical phenomena": temporal consistency is "tightly coupled with generalization", holds on unseen and corrupted data, collapses under random labels.
3. **C3 (result/mechanism):** "Mechanistic link to SGD": SGD injects anisotropic noise "aligned with feature dynamics".
4. **C4 (theory):** A "conceptual bridge" (Theorem 1, informal; App. G) bounding the class-wise generalization gap by a TV distance plus δ; no computable version.

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Datasets: MNIST, CIFAR, SVHN, STL-10 (§4.1); main-text experiments are ResNet-20 on CIFAR-10 with d "at second basic block" (Figs. 2, 5 captions); Experiment 3 is an MLP 28×28→100→2→10 on MNIST (App. H). Architectures for the other datasets: *not stated after search*. Optimizers (Table 2, App. H): SGD (MNIST, CIFAR-10/100, lr 0.01/0.1, momentum 0.9), Adam (SVHN, STL-10, lr 0.001). Total epochs for Experiments 1–2: not stated (checkpoints up to t=1000 appear in Fig. 4). LR schedule: "the learning rate was reduced at specific epochs during training", values deferred to external code links. Seeds / number of runs / error bars: *not stated after search*; no figure caption mentions them. Compute: RTX 4090 GPUs, "a few hours" (App. H). Splits: standard CIFAR train/test implied; no validation or selection protocol stated (nothing is tuned or selected; t1, t2 are swept). Own code: not mentioned (only third-party repositories acknowledged).
- **Headline numbers.** Composite accuracy ">98%" and near-zero CE for t1 ≥ 150 (§4.2, Fig. 2); relative parameter drift ‖θ300−θ150‖₂/‖θ300‖₂ ≈ 0.07 (§4.2); t2 ≤ 500 composite accuracy ">98%" (§4.4, Fig. 5); reinit/retrain test accuracy 92.0% → 91.2% (first block kept) / 91.5% (first two blocks) and mCE 0.316 → 0.326 / 0.329 (App. F.A); Welch p-values in Table 1 (App. E); isotropy p-values "typically < 0.001" (App. E).
- **Appendix adds:** Itô derivation of feature dynamics (App. A), classification-region definition and pushforward measures (A.C–A.D), extra datasets/depths for memory, forgetting and transfer curves (Figs. 10–13), CIFAR-10 "induction" with PCA (Fig. 14), epochs 50/150 spectra (Fig. 15), all 15 CIFAR-10C corruptions (Figs. 16–17), explanation of memory (App. C), NTK argument (App. D), hypothesis tests (App. E), reinit and freeze experiments (App. F), definitions and proofs of Theorems 1–3 (App. G), training settings (App. H).
- **Unverifiable:** all figures (1–19); garbled equations in extraction (e.g., Fig. 3 caption symbols, Theorem 1 display); external code links (removed).

### Integrity signals
`scripts/integrity_scan.py` on the paper text: "No reviewer-directed text or hidden characters found." The reviewers read the redacted copy (identical to the original here). No injected instructions were noticed while reading.

### Literature check status (strict, cutoff 2025-09-24)
Fingerprint written (title, method-like terms, two distinctive phrases, cutoff). Three `related_search.py search` attempts (claim queries for C1 and C3) failed: the arXiv API returned HTTP 429 twice and timed out once. **No results were kept; no baseline scout, similarity or novelty profile could be produced.** Per the skill, the check falls back to `literature check: off`: novelty verdicts and missing references below come from the reviewers' knowledge, every recommended reference is marked `[verify]`, and none was confirmed through `verify`.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Lucía Varnhagen-Okoro, large public research university (Europe)
- **Seniority / Expertise**: senior faculty / statistical learning theory, optimization dynamics, empirical ML methodology
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Area chair who asks "which claim does this experiment actually test?" and rewards honest, narrowly scoped findings.

### Reviewer 1 (Methodology): Dr. Anselm Kuroda-Reyes, industrial research lab (North America)
- **Seniority / Expertise**: mid-career industry scientist / training-dynamics experiments, checkpoint analysis, evaluation protocols for generalization
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on controls, seeds and chance baselines; recomputes every number.

### Reviewer 2 (Domain): Prof. Ioana Delacroix-Nwosu, public research university (Europe)
- **Seniority / Expertise**: senior faculty / generalization theory, SGD as a stochastic process, implicit regularization
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads proofs line by line; checks that cited work supports the sentence citing it.

### Reviewer 3 (Perspective): Dr. Priyanka Vestergaard-Alamu, interdisciplinary research institute (South Asia)
- **Seniority / Expertise**: mid-career researcher / dynamical systems and statistical physics of learning, representational drift in neuroscience
- **Review Focus**: Cross-disciplinary connections, assumptions, practical impact, broader impact
- **Style**: Constructive and expansive; "interesting, and could be stronger if…".

### Reviewer 4 (Generalist): Dr. Jae-won Strand-Ibarra, university vision and representation-learning group (East Asia)
- **Seniority / Expertise**: mid-career faculty / representation learning, image classification robustness
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted ICLR papers usually contain.

### Devil's Advocate: Prof. Rafael Oyelaran-Kowalczyk, university statistics and causal-inference group (Oceania)
- **Seniority / Expertise**: senior faculty / causal inference, evaluation methodology, robustness
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks what the experiment would look like if the claim were false.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1 — Independent Reports

# Peer Review Report

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Reviewer: Dr. Anselm Kuroda-Reyes, Methodology Reviewer (industrial research lab, North America; fictional persona)
## Expertise: training-dynamics experiments; checkpoint analysis; generalization evaluation protocols
## Date: 2026-11-10

---

## Summary
The paper splits a network at depth d and builds "composite networks" that combine shallow layers from one training checkpoint with deep layers from another. It observes that predictions of such composites agree with the reference network over a window of epochs (§4), that the agreement distribution on CIFAR-10 test and CIFAR-10C inputs is concentrated near 1 with clean labels and develops a long tail with 40% label noise (§5, Fig. 7), and that one-step SGD feature perturbations have a strongly non-spherical covariance (§6, Fig. 8). From these observations it argues that shallow-feature drift acts as "implicit structured augmentation" for deeper layers, and sketches a total-variation generalization bound (§7, App. G).

## Strengths
### S1: A simple, well-defined probe
Composite networks (§3, Fig. 1) and point-/dataset-level consistency (§4.1) are precisely defined, cheap to compute from saved checkpoints, and apply to any architecture. Memory, transfer and forgetting are separated into Experiments 1–3 with clear protocols.

### S2: Honest reporting of where the effect is absent
App. B states that for MNIST and STL-10 "accuracy remains largely unchanged as t1 varies", and the Conclusion calls the framing "still conceptual". The authors do not hide the null cases.

### S3: Attempts at interventions, not only observation
The noisy-label contrast (Fig. 7), reinitialising deep layers (App. F.A) and freezing shallow layers (App. F.B) are the right kinds of experiments to begin separating mechanisms, even though they are under-powered (see W1).

### S4: Reasonable breadth of appendix curves
Figs. 10–13 repeat the memory/forgetting/transfer curves for several datasets and several depths d, and App. H discloses optimizer settings per dataset (Table 2).

## Weaknesses

### W1: The central causal claim (C1/C2) is not tested by any controlled experiment
The title and §4.2 claim that shallow-feature drift is an implicit augmentation that "supports generalization" (§4.2: "This expanding consistency offers direct evidence that shallow layers act as structured augmenters"). The evidence is the observation that composites remain accurate, which is equally predicted by "features drift slowly and the classifier is locally insensitive". The two interventions that could separate the stories are small and uncontrolled: App. F.A reports test accuracy 92.0% → 91.2% / 91.5% and mCE 0.316 → 0.326 / 0.329 from one run each (no seeds), differences of the size typically seen between seeds for ResNet-20 on CIFAR-10 (general knowledge, not from the paper); and the freeze experiment (App. F.B, Fig. 18) removes trainable capacity as well as drift, so "slightly lower and less stable test accuracy" cannot be attributed to loss of augmentation. No experiment adds or removes temporal feature variability with everything else fixed, and no experiment relates the size of the consistency window to the generalization gap across runs.
- **Suggested Fix**: (a) Train the deep part on shallow features from a single frozen checkpoint versus features sampled from a window of checkpoints (the literal augmentation intervention). (b) Add matched-norm random perturbations of the shallow weights/features as a null for "structured" drift. (c) Report the correlation between window length and test gap across ≥ 10 runs varying LR, batch size, weight decay, and explicit augmentation. (d) Use ≥ 3–5 seeds. Cost: ResNet-20/CIFAR-10 runs are ≈ 1–2 GPU-h on a 4090 (the paper states "a few hours"), so ≈ 30–60 GPU-h in total.

### W2: Consistency is largely implied by accuracy, has no chance baseline, and is mostly measured on the training set
Consistency (§4.1) is agreement between predictions, and the label y does not enter the definition. If two networks are both ≥ 98% accurate on the training set (§4.2, "over 98% accuracy"), they must agree on at least 1 − (0.02 + 0.02) = 96% of samples; "tightly concentrated around 1.0" (§4.2, Fig. 2c) is therefore expected for any two late checkpoints, with or without augmentation-like behaviour. Figs. 2, 4, 5 are explicitly on the training set. Under distribution shift (Fig. 16, CIFAR-10C severity 5) agreement counts equally when both networks are wrong, so it cannot show that "temporal augmentation remains effective" (App. Fig. 16 caption). No reference level is given for what consistency a *non*-augmenting solution would show (e.g., composites from independent seeds, or from weights perturbed by the same relative norm as the observed 7% drift).
- **Suggested Fix**: Report label-aware composite accuracy on test and corrupted data next to agreement; add chance/null baselines (independent-seed shallow part; matched-norm perturbed shallow part); normalise the window length by the null. Low cost (inference only, plus a few extra training runs).

### W3: The "not a convergence artifact" argument does not rule out ordinary slow drift
§4.2 argues that accuracy decays with |t2 − t1| and that ‖θ300 − θ150‖₂/‖θ300‖₂ ≈ 0.07 "contradicting the behavior expected under a stationary solution". A slowly moving iterate under a stepped learning-rate schedule produces exactly this decay; a 7% parameter-norm change says little about functional change in a network with batch normalisation and weight decay. The LR schedule is not given (App. H: "the learning rate was reduced at specific epochs"), yet the windows (150–300, up to 1000) can straddle LR drops that dominate the drift.
- **Suggested Fix**: State total epochs and LR drop epochs; repeat Experiments 1–2 with constant and cosine schedules; measure functional drift (e.g., representation similarity between checkpoints) rather than parameter norm.

### W4: The SGD-noise analysis (C3) tests a straw-man null, and two claimed results are not shown
(i) §6/App. E reject a *spherical* covariance for Δz. Since Δz is the Jacobian of the shallow layers applied to a gradient step, a rapidly decaying spectrum is expected from the Jacobian alone; the comparison to "isotropic Gaussian perturbations of the same scale" (Fig. 8) is not informative about SGD specifically. (ii) §1 states "the strength of this anisotropy correlates with temporal consistency and memory-window length", and the contribution list says SGD noise is "aligned with feature dynamics". A text search of the whole manuscript finds no correlation analysis and no alignment measurement (e.g., overlap between top eigenvectors of the Δz covariance and the inter-epoch feature displacement). (iii) Fig. 8's caption does not give model, dataset or batch size; the number of bootstrap replicates B, sample count N and dimension d for the test are not stated (p < 0.001 requires B ≥ 1000), and "across epochs and data points" implies many tests without correction.
- **Suggested Fix**: Use a structured null (isotropic Δθ pushed through the same Jacobian; shuffled-label gradients); quantify subspace alignment with principal angles; vary batch size/LR and report the claimed correlation, or delete both claims; state B, N, d and correct for multiplicity.

### W5: "Across datasets and architectures" is not supported by what is reported, and there are no seeds or error bars
The §1 contribution list says "Across datasets and architectures, we show that temporal consistency is tightly coupled with generalization" (and §4 repeats "Across datasets and architectures, three patterns consistently emerge"). Main-text evidence is ResNet-20 on CIFAR-10 plus a 2-D-bottleneck MLP on MNIST; architectures for the other datasets are not stated. SVHN and STL-10 use Adam (Table 2), so the SGD-noise narrative does not apply to them. No figure caption or text reports seeds, repeated runs or confidence bands, which at CIFAR scale is a real weakness (3–5 seeds expected). Table 1 uses Welch's t-test on per-sample consistency values; samples from one network are not independent draws of an experiment, and neither n nor effect size is given.
- **Suggested Fix**: Add 3–5 seeds with bands for Figs. 2–5 and 7; list architecture per dataset; add at least one non-residual and one transformer-style model; test differences across seeds/runs with effect sizes (or a rank test on per-run summaries).

### W6: The NTK "forgetting" argument (App. D, §4.2) does not follow
The paper states that under NTK linearization "partial parameter freezing would not reverse monotonic loss decrease" and concludes the loss of the composite is ≤ Loss(f(θ_t1)). The composite pairs θ_t1 (shallow) with θ_t2 (deep) where *both* blocks were trained jointly from t1 to t2. It is not the iterate of gradient flow with the shallow block frozen, so monotonicity of that other trajectory says nothing about the loss at the mixed point; with any coupling between blocks the mixed point can have higher loss even in a convex linearized model. Moreover ResNet-20 at lr 0.1 is far from the lazy regime that NTK describes, so "cannot be explained by NTK" is not informative.
- **Suggested Fix**: Give a two-block quadratic counterexample or a correct derivation, or drop the claim.

**Minor**: duplicated heading "4.3/4.4 TRANSFERABILIY" (typo in both); appendix letters collide (sub-sections A–D of Appendix A vs. top-level B–H), so cross-references such as "Appendix 14" (§4.5) and "Appendix A" (§3 vs. §5) are ambiguous; d denotes both split depth and parameter dimension (§3); App. D writes f[d:n] while the main text uses f[d+1:n].

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | App. F.A | "This corresponds to a 3–4% accuracy drop under corruptions" | mCE (= average error) rises 0.316 → 0.326 / 0.329, i.e., +1.0 / +1.3 accuracy points absolute; 3.2% / 4.1% is the *relative* error increase | Recomputed from the three printed mCE values | High | MINOR | State absolute and relative changes separately |
| ERR-2 | E2 | §4.2 and App. D | "partial parameter freezing would not reverse monotonic loss decrease" | The composite is not reached by training with frozen shallow layers, so monotonic decrease on that other trajectory does not bound its loss | Derived (trajectory vs. mixed point), see W6 | Medium | MAJOR (side claim) | Correct or remove |
| ERR-3 | E5 | §1 | "the strength of this anisotropy correlates with temporal consistency and memory-window length" | No correlation result appears in §6, App. E or elsewhere | Full-text search for "correlat" (only §1, related-work and a bibliography entry) and read of §6/App. E | High | MAJOR | Provide the analysis or delete the claim |
| ERR-4 | E1/E6 | Table 1 | "Depth 1 5.46244 × 10−06 … Depth 3 5.46244 × 10−06" | Different depths give identical p-values to six digits while Depth 2 gives 2.02578 × 10−14: likely a copy error or a shared test | Cross-referenced rows of one table | Medium | MINOR | Check and re-report |
| ERR-5 | E5 | §1 (contributions), §4 | "Across datasets and architectures, we show that temporal consistency is tightly coupled with generalization" | Main text evidence: ResNet-20/CIFAR-10 and a toy MLP; architectures for other datasets not stated | Cross-referenced §4.1, Fig. 2/5 captions, App. H | High | MAJOR | Narrow the wording or add models |

### Claim-to-Evidence Map
| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|--------------|---------------------|---------|
| C1 | Feature drift acts as implicit, structured augmentation | Title, §1, §4.2 | Fig. 2–5 composites; App. F | Partially (stability shown; mechanism untested) |
| C2 | Temporal consistency is "tightly coupled with generalization"; collapses with random labels | §1, §5, Fig. 7 | Test/CIFAR-10C agreement; 40% noisy-label contrast | Partially / Unsupported (agreement, not generalization; 40% noise ≠ random labels) |
| C3 | SGD noise is anisotropic, aligned with feature dynamics, correlated with consistency | §1, §6, App. E | Fig. 8 spectra; sphericity test | Anisotropy supported against a weak null; alignment and correlation Unsupported |
| C4 | Generalization gap bounded via TV of augmented feature distribution | §7, App. G | Proof of an informal bound; no computation | Proof correct as stated; empirical content Unsupported |

**Protocol sweep.** I searched for `test set`, `validation`, `select`, `early stopping`, `best`, `tuned` and similar. The manuscript states no training, tuning or selection on a held-out test set; t1/t2 are swept and curves reported, not selected. No leakage concern.

## Dimension Scores (0–100)

**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline mechanism is not isolated by any control, and the key metric is nearly implied by accuracy; evidence is single-run on one small setting.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | W1, W3, W6 and ERR-2/3: untested mechanism, an invalid side argument, unsupported claims |
| Clarity & Presentation | 55 | Competent | Definitions clear; heading/appendix/notation slips |
| Novelty & Originality | 45 | Developing | Cross-checkpoint composites are a reasonable probe; the rest is an interpretation |
| Significance & Impact | 40 | Developing | Without a tested mechanism, little to build on |
| Experimental Validation | 32 | Developing | Single runs, train-set metrics, no null baselines, one setting |
| Reproducibility | 42 | Developing | Epochs/LR schedule/seeds not stated; code external |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations only partly discussed |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Mean of rigor/validation ≈ 36 (< 45) |
| Clarity | 2 | 55 |
| Significance | 1 | 40 (< 45) |
| Originality | 2 | 45 |

## Questions for Authors
1. What are the total epochs and LR drop epochs, and do the windows in Figs. 2–5 lie inside one LR stage? A constant-LR repeat showing the same window would raise my score.
2. What consistency do composites from an independent-seed or norm-matched perturbed shallow part show? If it is also ≈ 1, W2 stands.
3. What is the unit and n in Table 1, and why are the Depth 1 and Depth 3 p-values identical?
4. Can you show the claimed correlation between anisotropy strength and window length (§1)? If not, will the sentence be removed?

## Limitations Assessment
**Partially.** §7 and §8 acknowledge that the theory is conceptual and not computable. There is no discussion of the single-setting evidence, the missing causal controls, or the absence of seeds.

## Ethics Review Flag
**No**: public benchmarks, no human data.

## Overall Score
**2 (Reject)**: An interesting probe, but the paper's main interpretation is untested and the main metric cannot discriminate it from ordinary convergence; several stated results are absent from the paper.

## Confidence
**4**: Careful read of text, appendix and proofs; figures could not be inspected.

---

# Peer Review Report

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Reviewer: Prof. Ioana Delacroix-Nwosu, Domain Reviewer (public research university, Europe; fictional persona)
## Expertise: generalization theory; SGD as a stochastic process; implicit regularization
## Date: 2026-11-10

---

## Summary
The paper proposes to view the shallow part of a network as an "implicit augmenter" for the deep part: because shallow features change during training, the deep classifier sees a distribution of feature variants per input. It supports this with checkpoint-mixing experiments, a noisy-label contrast, a sphericity test for SGD feature noise, and an informal TV-distance generalization bound. The authors position it against capacity-based theory, flat-minima/stability analyses, neural collapse and "phenomenon-driven" work (§1, §2).

## Strengths
### S1: A fresh angle on a hard question
Looking at *time-evolution of internal features* rather than final parameters or input–output behaviour is a different perspective from the capacity and flatness literature the paper reviews (§2.1), and the intuition from straight-line feature trajectories in residual networks (§1, citing Gai & Zhang; Li & Papyan; Aubry et al.) is a reasonable starting point.

### S2: Correct, readable elementary proofs
I checked Theorem 2 (App. G.A) and the decomposition behind Theorem 1/3 (App. G.B). Theorem 2(2) is a correct Markov-type argument; the Theorem 1 inequality follows from the triangle inequality and the sup-definition of TV as written. The proofs contain no algebraic errors.

### S3: Clear definitions of memory and transferability
Definition 2 (App. G.A) separates particle-level from empirical-level memory, and the empirical consistency metric in §4.1 matches it (reference network at the later epoch).

### S4: Candid framing of the theory
§7 says the framework "remains theoretical due to two intractable components", which sets expectations correctly.

## Weaknesses

### W1: Closest prior work on the same objects is not discussed, so the delta is unclear
The experiment pairs shallow layers from one checkpoint with deep layers from another; this is model stitching across time. Related lines that the paper does not cite or differentiate, all from my knowledge (literature check unavailable; all `[verify]`): representation convergence "from the bottom up" during training (SVCCA, Raghu et al., NeurIPS 2017), model stitching (Lenc & Vedaldi, CVPR 2015; Bansal, Nakkiran & Barak, NeurIPS 2021), linear mode connectivity across training (Frankle et al., ICML 2020), and iterate averaging/checkpoint ensembling (SWA, Izmailov et al., UAI 2018). The simplest competing explanation for the composite results (shallow layers settle early; deep layers adapt to them) is exactly the SVCCA observation, and the paper never engages it.
- **Suggested Fix**: Add a related-work paragraph and a table stating what composite networks reveal beyond layer-wise convergence and stitching results.

### W2: The SGD-noise result (C3) restates something well established, and the SDE background is mis-sourced
That SGD gradient noise is highly anisotropic and concentrated in few directions is a long-standing finding (e.g., Zhu et al., ICML 2019; Gur-Ari et al., 2018 [verify]); showing it for Δz against a spherical null (§6) is not new. The SDE model in §3 and App. A (dθ = −∇L dt + √Σ dB, with no learning-rate factor) is attributed to Chen et al. (2022) and Chaudhari & Soatto (2018). The bibliography title for Chen et al. is "Revisiting the acceleration phenomenon via high-resolution differential equations"; from the title it concerns acceleration ODEs, not SGD diffusions (Medium confidence; cannot confirm from an abstract here, so I list it as a question below).
- **Suggested Fix**: Cite the SGD-SDE literature that derives the √(ηΣ) diffusion (e.g., Li, Tai & E, ICML 2017 [verify]) and position C3 relative to prior noise-structure results.

### W3: Theorem 1 is correct but may carry no information
The bound is TV(Ω^(i)_{t′,Δt}, f_#(μ_i)) + δ. Ω^(i) is a mixture of finitely many feature points (training samples × integer epochs, §7), while f_#(μ_i) is the pushforward of the true class distribution. Unless held-out features coincide with training-time features, two such measures are mutually singular and TV = 1, making the bound trivial (the bound is always ≤ 1 + δ). The first step of the proof (App. G.B, (1)) is the generic TV bound for any classifier and any substituted measure; the memory assumption only pays the δ for replacing the empirical pushforward by Ω. The statement "small prediction thresholds (δ) often correspond to large time windows (Δt), suggesting a broader generalizable region than conventional analyses imply" (§7) is not backed by any computed δ, Δt or TV. Theorem 2 is Markov's inequality.
- **Suggested Fix**: Use a smoothed/kernelized distance (MMD, Wasserstein as the authors suggest) on a small model and report values; or state explicitly that Theorem 1 is illustrative and remove it from the contribution list.

### W4: The NTK foil is not a meaningful comparator
App. D argues forgetting is incompatible with NTK linearization, but (a) the argument is flawed (see R1-W6) and (b) no one expects a lr-0.1 ResNet-20 to be in the lazy regime; the contrast does not support the paper's own mechanism.
- **Suggested Fix**: Compare with relevant alternatives (layer-wise convergence, SWA-type averaging), not with NTK.

### Missing References *(all `[verify]`: literature check unavailable)*
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Raghu, Gilmer, Yosinski, Sohl-Dickstein. SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability. NeurIPS 2017 `[verify]` | Layers converge bottom-up during training; the simplest alternative explanation for composite stability |
| Critical | Bansal, Nakkiran, Barak. Revisiting Model Stitching to Compare Neural Representations. NeurIPS 2021 `[verify]` | Composite networks are stitching across time |
| Important | Lenc, Vedaldi. Understanding image representations by measuring their equivariance and equivalence. CVPR 2015 `[verify]` | Origin of stitching-based comparison |
| Important | Frankle, Dziugaite, Roy, Carbin. Linear Mode Connectivity and the Lottery Ticket Hypothesis. ICML 2020 `[verify]` | Stability of checkpoints along a training path |
| Important | Izmailov, Podoprikhin, Garipov, Vetrov, Wilson. Averaging Weights Leads to Wider Optima and Better Generalization. UAI 2018 `[verify]` | Temporal averaging as a generalization mechanism; natural baseline |
| Important | Zhu, Wu, Yu, Wu, Ma. The Anisotropic Noise in Stochastic Gradient Descent: Its Behavior of Escaping from Sharp Minima and Regularization Effects. ICML 2019 `[verify]` | Anisotropic SGD noise is already characterised |
| Important | Gur-Ari, Roberts, Dyer. Gradient Descent Happens in a Tiny Subspace. arXiv 2018 `[verify]` | Low-dimensional structure of gradients |
| Helpful | Li, Tai, E. Stochastic Modified Equations and Adaptive Stochastic Gradient Algorithms. ICML 2017 `[verify]` | Proper SDE approximations of SGD |
| Helpful | Smith, Dherin, Barrett, De. On the Origin of Implicit Regularization in Stochastic Gradient Descent. ICLR 2021 `[verify]` | Implicit-regularization view of SGD trajectories |
| Helpful | Kornblith, Norouzi, Lee, Hinton. Similarity of Neural Network Representations Revisited. ICML 2019 `[verify]` | Measure of functional drift between checkpoints |

### Novelty by claim (knowledge only; no search ran; at most "medium" where uncertain)
| Claim | Dimension | Novelty | Closest prior work (not verified) | Reasoning |
|-------|-----------|---------|-----------------------------------|-----------|
| C1 | method/framing | medium | Model stitching; SVCCA | Cross-checkpoint composites and the augmentation interpretation are a new framing, but the probe is stitching |
| C2 | result | incremental | Layer-wise convergence; noisy-label memorization dynamics | Stability within a window is predicted by earlier work; the link to generalization is not shown |
| C3 | result | known `[verify]` | Anisotropic SGD noise (Zhu et al. 2019) | Established; the new part (feature space, alignment) is unshown |
| C4 | theory | incremental | Generic TV/Wasserstein generalization bounds | Elementary and possibly vacuous |

### Citation check (E7)
| Citation | Concern | Confidence |
|----------|---------|-----------|
| Chen et al. (2022) as source of SGD SDE (§3, App. A) | Bibliography title concerns acceleration via high-resolution ODEs | Medium → Question |
| Zhang et al. (2016) in §2.1 ("showed that neural networks can generalize well even when their parameter count far exceeds the number of training samples") | The cited paper's headline is that networks fit random labels; wording is loose | Low → Question |

## Dimension Scores (0–100)

**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: novelty rests on framing, positioned against none of the closest prior work; the theory is elementary and possibly vacuous.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 45 | Developing | Proofs correct; NTK argument flawed; bound uninformative |
| Clarity & Presentation | 55 | Competent | Readable; positioning missing |
| Novelty & Originality | 45 | Developing | New framing, probe close to stitching, SGD result known |
| Significance & Impact | 42 | Developing | Interest depends on the untested mechanism |
| Experimental Validation | 40 | Developing | Observational; no controls |
| Reproducibility | 45 | Developing | Details external |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Rigor 45 / validation 40 average ≈ 43 → 1, raised one step because proofs are correct |
| Clarity | 2 | 55 |
| Significance | 1 | 42 |
| Originality | 2 | 45 |

## Questions for Authors
1. How do the composite results differ from what bottom-up layer convergence (SVCCA) already predicts? Evidence that they do would raise my score.
2. Can you compute any version of Theorem 1 (kernel-smoothed or MMD) on a small model and show it is non-vacuous?
3. Is Chen et al. (2022) the source of the SDE used in §3? If not, please cite the correct derivation.

## Limitations Assessment
**Partially.** The theory's intractability is stated; positioning limits and the lack of controls are not.

## Ethics Review Flag
**No**.

## Overall Score
**2 (Reject)**: A new vocabulary around a known set of observations; the positioning, the SGD result and the bound do not yet deliver a contribution at the ICLR bar.

## Confidence
**4**: Familiar with the area; references recalled from knowledge and unverified.

---

# Peer Review Report

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Reviewer: Dr. Priyanka Vestergaard-Alamu, Perspective Reviewer (interdisciplinary research institute, South Asia; fictional persona)
## Expertise: dynamical systems and statistical physics of learning; representational drift in neuroscience
## Date: 2026-11-10

---

## Summary
The paper asks whether a network's own training trajectory can act as an augmentation mechanism. It shows that late checkpoints' deep layers still classify features from earlier (and, to a lesser degree, later) checkpoints' shallow layers, argues this is more than convergence, and links it to SGD noise structure and a conceptual TV-style bound.

## Strengths
### S1: A question with natural links to other fields
The picture of a readout (deep layers) tolerating drift in an upstream code (shallow layers) parallels "representational drift" in neuroscience and the stability–plasticity trade-off in continual learning; the paper's vocabulary ("memory", "forgetting") invites those connections.

### S2: Empirical hooks that others can reuse
Composite networks and consistency windows are easy to compute on any checkpointed model and could become a diagnostic (§4.1).

### S3: Self-aware, forward-looking conclusion
§7–§8 flag tractable surrogates (MMD, Wasserstein) as the next step; this is a sensible research agenda.

### S4: No ethical or societal red flags
Public image benchmarks, small models, compute disclosed (App. H); an LLM-use disclosure is included (§9).

## Weaknesses

### W1: "Augmentation" is read passively; the paper never shows the deep layers are *trained on* varied features
At time t, deep layers θ_t see only z_t(x). Features from other times were presented to *earlier* deep parameters, not the current ones. The observed stability of f(θ_t2)∘f_{1:d}(θ_t1) shows that the classifier is insensitive to small shallow-feature shifts (an assumption of locally smooth readout), not that exposure to varied features regularised it. In a dynamical-systems view the time-average ω_{x,t′,Δt} (§7) is an ergodic average over a non-stationary process; the paper assumes that sampling uniformly over a time window mimics the distribution of *unseen* inputs' features, which is not checked.
- **Suggested Fix**: Test the ergodicity-type assumption directly: compare the distribution of ω_{x,t′,Δt} with the features of held-out points of the same class (e.g., via MMD at depth d). This is also the missing link for Theorem 1.

### W2: Agreement is used as a stand-in for generalization
In §5 and App. Figs. 16–17, consistency on CIFAR-10C is read as "demonstrating the structured nature of the augmentation mechanism". Agreement between two checkpoints on corrupted data tells us nothing about accuracy on that data; a practitioner would want composite *accuracy* on test/OOD data and its relation to the generalization gap. The noisy-label collapse (40% labels randomized, not "random labels" as in the abstract) could equally reflect that networks that memorize are less stable in their predictions.
- **Suggested Fix**: Report accuracy-based composites on test/OOD data and add a control separating memorization from "lack of semantic structure" (e.g., label noise at several rates; pure random labels).

### W3: Scale and practical use are untested
All headline evidence is ResNet-20 on CIFAR-10. The Introduction cites transformers (Aubry et al.), but no transformer or non-residual convolutional network appears. No practical use of the window is shown, e.g., predicting the test gap, choosing checkpoints, or comparing with known generalization measures.
- **Suggested Fix**: Add one larger/different architecture and one practical demonstration (e.g., rank hyperparameter settings by window length vs. test accuracy).

### W4: No limitations section
The theory's intractability is discussed (§7), but the paper has no limitations discussion of its single-setting, single-run empirical base or of its causal interpretation.
- **Suggested Fix**: Add a short Limitations section.

## Dimension Scores (0–100)

**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting perspective with a reusable probe, but the evidence for the perspective is thin; I place it at the upper end of the typical rejected band.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Passive-robustness reading, missing links |
| Clarity & Presentation | 58 | Competent | Clear narrative |
| Novelty & Originality | 55 | Competent | New framing |
| Significance & Impact | 50 | Developing | Potential if validated |
| Experimental Validation | 42 | Developing | One setting; agreement metric |
| Reproducibility | 50 | Developing | Details external |
| Ethical Compliance | 65 | Competent | Nothing at stake; limitations partial |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Rigor/validation ≈ 46 |
| Clarity | 2 | 58 |
| Significance | 2 | 50 |
| Originality | 2 | 55 |

## Questions for Authors
1. Is the distribution of features across checkpoints close to the feature distribution of held-out same-class points at depth d? A positive answer would raise my score; a negative one would undermine C4.
2. Does window length predict test accuracy across hyperparameter settings better than simple measures?
3. Does the effect survive in a non-residual network?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**.

## Overall Score
**3 (Borderline Reject)**: A thought-provoking perspective and reusable probe; the evidence does not yet reach the claim.

## Confidence
**3**: Fairly confident; I am from an adjacent field and did not check every derivation.

---

# Peer Review Report

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Reviewer: Dr. Jae-won Strand-Ibarra, Generalist Reviewer (university vision and representation-learning group, East Asia; fictional persona)
## Expertise: representation learning; image-classification robustness
## Date: 2026-11-10

---

## Summary
The paper investigates whether feature changes during training play the role of a data augmentation. It builds hybrid networks from different checkpoints, reports that predictions stay stable across a window, contrasts clean and 40%-noisy-label training, analyses the covariance of one-step SGD feature updates, and offers an informal TV-based generalization bound. Its stated message is a "conceptual perspective" linking feature dynamics and generalization.

**Venue-criteria checklist (ICLR).** (1) Soundness: claims supported by evidence — *not met* (mechanism untested, §4–§5). (2) Contribution: significance of finding — *partly* (a clean phenomenon, interpretation not established). (3) Presentation: clear writing and organization — *partly* (readable; structural slips, Minor line). (4) Empirical breadth appropriate to claim — *not met* (§1 "across datasets and architectures" vs. ResNet-20/CIFAR-10 main text). (5) Reproducibility — *partly* (App. H; epochs, schedule, seeds missing). (6) Venue fit — *met* (generalization and training dynamics are core ICLR topics; phenomenological studies are welcome when well controlled).

## Strengths
### S1: Engaging, motivated question
The Introduction builds from a concrete observation (straight-line trajectories in residual nets, §1) to a testable question about generalization to "the region surrounding these lines".

### S2: A compact, intuitive probe
Fig. 1 and the consistency definitions (§4.1) make the experimental idea easy to grasp, and Experiments 1–3 map to three named regularities.

### S3: Appendix breadth and candour
Extra datasets/depths (Figs. 10–13), CIFAR-10C across 15 corruptions (Figs. 16–17), and the Conclusion's "still conceptual" framing.

### S4: Fair-minded handling of null results
App. B notes MNIST/STL-10 do not show forgetting.

## Weaknesses

### W1: Claims outrun the evidence in wording
The paper uses "direct evidence" (§4.2), "demonstrate" (§1), "These findings establish…" (§6), and "rigorous statistical evidence" (§6) for observational or weak-null results. The abstract says consistency "disappears when the training supervision lacks semantic structure (e.g., random labels)", but §5 uses 40% randomized labels. A reader will leave with a causal story the experiments do not support.
- **Suggested Fix**: Rephrase as hypotheses or "consistent with"; use "40% noisy labels" throughout.

### W2: Core definitions and organization hide the key evidence
The Fig. 3 caption's reference network differs from the §4.1 definition (cannot be fully verified from the extracted symbols: see Questions); the empirical definitions in §4.1 use y but never use the label; Sections 4.3 and 4.4 share a heading; appendices are lettered inconsistently (sub-sections A–D within Appendix A, then B–H), so references like "Appendix 14" and "Appendix A" are ambiguous; d is overloaded (§3). The most important controls (App. F reinit/freeze) are buried in a "Supporting evidence" appendix with no table or error bars.
- **Suggested Fix**: Move the reinit/freeze results into the main text with seeds; fix numbering and notation.

### W3: The theory section is a contribution on paper but not in substance
§7 titles itself "A Conceptual Theory Bridge", Theorem 1 is "Informal", the TV term is "intractable", and no value of δ, Δt or TV is reported, yet C4/§1 present it as a contribution ("suggesting computable surrogates such as MMD or Wasserstein distances", §1). It reads as a motivation paragraph rather than a result.
- **Suggested Fix**: Either demonstrate a computable surrogate on one setting or move the theorem to a discussion section.

### W4: The "across datasets" evidence is qualitative and left to figures in the appendix
No table summarizes, per dataset and architecture, the window length or the effect; conclusions rely on curves whose seeds and variability are not shown.
- **Suggested Fix**: Add a summary table with mean ± std over seeds.

**Minor**: duplicate heading "TRANSFERABILIY"; typos ("phemenon"); Fig. 8/16/17 captions omit model and dataset in places.

## Dimension Scores (0–100)

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a readable, promising observation, but the paper's main claim rests on observational, single-run evidence and an uninformative theory section — typical of rejected submissions at ICLR.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 45 | Developing | Claims not tested |
| Clarity & Presentation | 52 | Competent→Developing | Readable but disorganized appendix, overclaiming |
| Novelty & Originality | 50 | Developing | New framing |
| Significance & Impact | 45 | Developing | Depends on validation |
| Experimental Validation | 40 | Developing | One setting, no seeds |
| Reproducibility | 48 | Developing | Epochs/LR/seeds missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | ≈ 43 |
| Clarity | 2 | 52 |
| Significance | 2 | 45 |
| Originality | 2 | 50 |

## Questions for Authors
1. Is the reference network in the Fig. 3 caption (θ_t1) the one intended, or the later one as in §4.1? (The caption symbols are garbled in extraction.)
2. Can the central evidence (reinit/freeze, Fig. 18) be reported with seeds in the main text?
3. Do the conclusions hold for pure random labels rather than 40% noise?

## Limitations Assessment
**Partially**: no dedicated Limitations section; theory limits are acknowledged in §7–§8.

## Ethics Review Flag
**No**.

## Overall Score
**3 (Borderline Reject)**: A thoughtful probe and a promising direction, but the contribution as claimed is not established; the weaknesses are of the kind that most rejected submissions share rather than accepted ones.

## Confidence
**4**: Confident on venue fit and presentation; did not re-derive all proofs.

---

# Devil's Advocate Report

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Reviewer: Prof. Rafael Oyelaran-Kowalczyk, Devil's Advocate (university statistics and causal-inference group, Oceania; fictional persona)

---

## Steelman
Composite checkpoints reveal a robust, quantifiable property: deep layers at late epochs are insensitive to the drift their shallow layers underwent. That property disappears under noisy labels, so it is not a trivial feature of any training run. If one accepts the reading that this insensitivity is acquired from exposure to drifting features, it supplies a training-dynamics account of generalization that parameter-space theories lack.

## Core Argument Chain
1. P1: Under SGD, hidden features of a fixed input form a distribution over training time (§3, Itô expansion).
2. P2: Deep layers at a late epoch classify features from nearby epochs with high agreement (memory/transfer; §4).
3. P3: This stability is not a convergence artifact (§4.2: drift ≈ 0.07; accuracy decays with gap).
4. P4: Stability persists on test and corrupted inputs with clean labels and collapses with 40% noisy labels (§5).
5. P5: SGD feature noise is anisotropic (§6).
6. P6: If the classifier is stable within a window, a TV bound controls the class-wise generalization gap (§7).
∴ Feature dynamics act as implicit structured augmentation that supports generalization (title, abstract).

## Strongest Counter-Argument
Suppose the claim were false: the deep layers are merely a slowly changing function of slowly changing shallow features. What would the paper's experiments look like? Exactly as reported. Late checkpoints of any converging run will have shallow features that move little between neighbouring epochs and a classifier that is locally insensitive to small moves; composites mixing nearby checkpoints then agree with the reference, agreement decays with the gap, and agreement is near 1 whenever both networks are accurate (§4.2 reports > 98% accuracy, which already forces agreement ≥ 96% on the training set). Networks trained on 40% noisy labels keep fitting and memorising throughout the window, so their predictions move more and agreement collapses. None of this involves augmentation or generalization. To distinguish the stories one needs an intervention that removes or adds temporal variation of shallow features while holding the optimizer trajectory otherwise fixed, a matched-norm non-structured perturbation control, and a measure of generalization (test accuracy or gap) rather than prediction agreement. The paper has none of these in its main text; the only attempts (App. F) are single-run, differ by 0.5–0.8 accuracy points, and confound drift with trainable capacity (freezing) or with training length (reinitialisation and retraining). The paper's own App. C concedes that its gradient-balance explanation "is specific to the training set". The SGD-noise section adds anisotropy, which is expected from the Jacobian structure of Δz, and the claimed alignment and correlation with memory windows are not shown. The theory bound relies on a TV distance between a finite mixture of training-trajectory points and the true feature distribution, which may be trivially 1 and is never computed. The step from "stable under checkpoint mixing" to "implicit augmentation supports generalization" is therefore an interpretation, not a finding, yet it is the title and the first contribution.

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence (criterion 2: experiment cannot test the claim) | §4–§5, Figs. 2, 4, 5, 7; App. F; title | The claim "temporal feature variation acts as implicit augmentation that supports generalization" is tested only by train-set composite metrics (Figs. 2, 4, 5: "training set"), and by label-free prediction agreement on test/corrupted data (§5), a metric that cannot measure generalization (both networks may be wrong and agree). No experiment manipulates temporal variation with other factors fixed. | Add intervention + null experiments (single vs. window-sampled shallow features; matched-norm perturbation), report accuracy/gap and seeds | New data/experiments/redesign |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Claim distortion (E5) | Abstract, §1, §4.2, §6 | "direct evidence", "demonstrate", "These findings establish…", "rigorous statistical evidence"; "random labels" (abstract) vs. 40% noisy labels (§5); "Across datasets and architectures" vs. ResNet-20/CIFAR-10 main text. Evidence supports a weaker claim. | Narrow wording; say "40% noisy labels"; add architectures |
| DA-M2 | Logic / theory | §7, App. G | Theorem 1 holds but the TV term compares an atomic training-trajectory mixture with the true class feature distribution and is uncomputed; it may equal 1 (bound ≤ 1 + δ, trivial). Theorem 2 is Markov's inequality. No δ, Δt or TV value is reported, yet §7 claims "a broader generalizable region than conventional analyses imply". | Compute a smoothed surrogate on a small model or demote the theorem |
| DA-M3 | Logic | §4.2, App. D | The NTK argument compares the loss at a mixed-parameter point to loss along a frozen-shallow trajectory; it does not follow. | Correct or remove |
| DA-M4 | Evidence | §1, §6, App. E | Spherical null is weak; "correlates with temporal consistency and memory-window length" and "aligned with feature dynamics" have no supporting analysis; B, N, d and multiplicity handling not stated. | Structured null; subspace alignment; vary batch size/LR |
| DA-M5 | Alternative explanations | §4.2 | "Not a convergence artifact" relies on 7% parameter-norm drift and decay with gap, both expected for slow drift with a stepped LR schedule that is not reported. | Report schedule, functional drift; constant-LR repeat |
| DA-M6 | Statistics | App. E Table 1; all figures | No seeds anywhere; Welch's t-test on per-sample bounded consistency values with unstated n; identical p-values for Depth 1 and 3. | Seeds, effect sizes, rank-based tests on per-run summaries |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | §4.3/4.4 | Duplicate heading "TRANSFERABILIY" |
| DA-m2 | Presentation | Appendices | Lettering collisions; ambiguous cross-references ("Appendix 14", "Appendix A") |
| DA-m3 | Notation | §3, App. D | d used for dimension and split depth; f[d:n] vs. f[d+1:n] |
| DA-m4 | Reporting | App. F.A | "3–4% accuracy drop" is a relative error increase (see numeric check) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Accuracy drop under corruption (App. F.A) | "3–4% accuracy drop" | (0.326 − 0.316) = 0.010 and (0.329 − 0.316) = 0.013 absolute; 0.010/0.316 = 3.2%, 0.013/0.316 = 4.1% relative error increase | No (absolute accuracy drop is 1.0–1.3 points) |
| Clean accuracy after reinit/retrain | 92.0 → 91.2 / 91.5 | −0.8 / −0.5 points; note 2-block retention (91.5) beats 1-block (91.2) on accuracy but is worse on mCE (0.329 vs. 0.326) | Consistent arithmetic; non-monotone trend |
| Agreement implied by accuracy (§4.2) | ">98% accuracy", consistency ≈ 1.0 | Two classifiers each ≥ 98% accurate agree on ≥ 1 − 0.02 − 0.02 = 96% | Trivially satisfied |
| Table 1 p-values | Depth 1: 5.46244 × 10⁻⁶; Depth 3: 5.46244 × 10⁻⁶ | Identical to 6 digits for different depths | Suspicious (Question) |
| Theorem 2(2) | "more than 1 − 1/q" | From 1 − δ < 1 − qδ(1 − p) ⇒ p > 1 − 1/q | Match (Markov) |

## Ignored Alternative Explanations
- Slow, converging drift of shallow features plus a locally insensitive classifier (no augmentation needed).
- Bottom-up layer convergence: shallow layers settle early; deep layers adapt (SVCCA-type observation, `[verify]`).
- Near-identity residual blocks in ResNet-20 making feature changes small by construction (only residual nets in main text).
- Memorisation under 40% noise reduces prediction stability, independent of "semantic structure".
- Composite accuracy depends on batch-norm statistics mixed across checkpoints (not discussed).

## Missing Stakeholder Perspectives
No deployment or societal stakeholder is implicated by this work. The relevant omitted audience is practitioners who would want a usable generalization predictor; none is offered.

## Observations (Non-Defects)
- The composite-network probe is a good idea and cheap to adopt.
- The authors disclose null cases (App. B) and LLM use (§9), and label the theory "conceptual".
- The proofs of Theorems 2–3 contain no algebraic errors.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 35 | Mechanism untested; NTK argument invalid; bound uninformative |
| Clarity & Presentation | 52 | Readable; overclaiming wording; organization slips |
| Novelty & Originality | 42 | Framing new; results largely expected |
| Significance & Impact | 38 | Without a tested mechanism |
| Experimental Validation | 30 | Train-set metrics, no controls, no seeds |
| Reproducibility | 42 | Schedule/epochs/seeds missing |
| Ethical Compliance | 60 | Nothing at stake; limitations partial |

**Pool position:** better than about 28% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central claim is not tested by the reported experiments.

## Overall: 2 | Confidence: 4

---

# Phase 1.5 — Literature Check

Not completed: see *Literature check status* in Phase 0 (arXiv API HTTP 429 ×2, timeout ×1; 0 results kept; 3 of the 12-query budget attempted, none counted as results). No novelty profile, baseline scout or similarity run. All references above are from the reviewers' knowledge and marked `[verify]`. No newer/concurrent work was used against the paper.

# Phase 1.6 — Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept (ordered by severity) | Each has a location, a concrete check and a fix; none answered in the appendix (searched for seeds, correlation, schedule) |
| R1 | Minor line | moved to Minor | Heading/appendix/notation slips are cosmetic |
| R2 | W2 (SDE source) | rewritten | The Chen et al. mismatch is inferred from the bibliography title only; moved to a Question and Citation-check table, not a weakness |
| R2 | W2 (SGD noise "known") | rewritten | Based on knowledge without a verified abstract: claim-level finding, MAJOR at most, not "known" for the whole paper |
| R2 | W3 (Theorem 1 vacuous) | rewritten | Stated as "may be vacuous (TV = 1 unless features coincide)" since TV is not computed by either side |
| R2 | W1/Missing references | kept | All marked `[verify]`; none is "newer" work; none required as a comparison |
| R3 | W1–W4 | kept | Specific, constructive; W4 reworded: §7–§8 do acknowledge theory limits, so "no Limitations section" instead of "no limitations" |
| R4 | W1–W4 | kept | W2 includes a symbol-level point (Fig. 3 caption) that depends on garbled extraction → moved to Questions, not an error |
| DA | DA-C1 | kept as CRITICAL for the EIC | |
| DA | DA-M2 | rewritten | Same caution as R2-W3 |
| DA | DA-m4 | kept | Mirrors R1 ERR-1 |
Scores unchanged.

# Phase 2 — Synthesizer Package (Part A)

**Merged issues and consensus classes**

| ID | Issue | Sources | Class | May hinge? |
|----|-------|---------|-------|------------|
| I1 | Central mechanism/causal claim ("implicit augmentation supports generalization") not tested | R1-W1, R3-W1, R4-W1, DA-C1, DA-M5 (R2-W3 relates) | CONSENSUS-4 | Yes |
| I2 | Consistency metric: implied by accuracy, no null baseline, agreement ≠ generalization, train-set evidence | R1-W2, R3-W2, DA-C1 | CONSENSUS-3 | Yes |
| I3 | Theory (Theorem 1) uninformative/uncomputed; contribution only conceptual | R2-W3, R4-W3, DA-M2 | CONSENSUS-3 | Yes |
| I4 | SGD-noise result: weak null, known, claimed alignment/correlation absent | R1-W4, R2-W2, DA-M4 | CONSENSUS-3 | No |
| I5 | Limited breadth; no seeds/statistics | R1-W5, R3-W3, R4-W4, DA-M6 | CONSENSUS-4 | No |
| I6 | NTK argument flawed | R1-W6, R2-W4, DA-M3 | CONSENSUS-3 | No |
| I7 | Overclaiming wording | R4-W1, DA-M1, R1 ERR-5 | CONSENSUS-3 | No |
| I8 | Missing related work (stitching, layer convergence, SWA, LMC) | R2-W1, R3 (comments) | CONSENSUS-2 | No |
| I9 | Convergence/LR-schedule alternative explanation | R1-W3, DA-M5 | CONSENSUS-2 | No |
| I10 | Organization/notation | R4-W2, R1 Minor, DA-m1–m3 | CONSENSUS-3 (cosmetic) | No |
| S1 | Value of the conceptual theory bridge (R3 sees a promising agenda; R2/DA see no content) | R3-S3 vs. R2-W3, DA-M2 | SPLIT | No |

**DA-CRITICAL:** DA-C1 (needs new experiments if upheld). **Integrity-scan findings:** none. **Error Logs:** R1 ERR-1…5.

**Official output (before EIC weights, DA-C1 provisionally upheld):** official mean rating 2.40; composite 45.2; provisional ceiling 3 (cap reason: DA-C1 needs new experiments); no warnings; spreads all ≤ 15.

---

# Phase 2 — Editorial Decision

# Editorial Decision

## Paper: Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization
## Submission ID: iclr26-FaNWaj1Zk2 (evaluation id)
## Date: 2026-11-10
## Target Venue: ICLR (key `iclr`) | Paper Type: analysis
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Lucía Varnhagen-Okoro; R1 Methodology Dr. Anselm Kuroda-Reyes, R2 Domain Prof. Ioana Delacroix-Nwosu, R3 Perspective Dr. Priyanka Vestergaard-Alamu, R4 Generalist Dr. Jae-won Strand-Ibarra, DA Prof. Rafael Oyelaran-Kowalczyk

---

## Decision: Reject (2) — ICLR label: 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10})

**Official ratings** (shown to authors): R1 2, R2 2, R3 3, R4 3, DA 2 → mean 2.40 · official composite 45.2
**EIC assessment** (internal): weighted rating 2.38 → starting point 2 · weighted composite 45.1 → band 2 (cross-check agrees) · **DA ceiling**: none (DA-C1 downgraded) · **Final (EIC)**: 2

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The paper offers a cheap, reusable probe (composite networks across checkpoints) and an inviting reading of training dynamics as implicit augmentation. It is candid that the theory is conceptual (§7–§8) and reports null cases (App. B). If the authors showed that the effect is not a generic consequence of convergence, this could be an interesting ICLR phenomenology paper.
- **Against acceptance:** The headline interpretation is not tested: no experiment manipulates temporal feature variation, the main metric is almost implied by accuracy and has no null baseline, evidence is single-run and essentially ResNet-20/CIFAR-10, the SGD-noise claims of "alignment" and "correlation" are not shown, the TV bound is uncomputed and possibly vacuous, and the NTK argument is invalid. These are weaknesses typical of rejected submissions, not of accepted papers, because they concern whether the central claim is measured at all.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Mechanism untested; only observational + small single-run interventions | R1-W1, R3-W1, R4-W1, DA-C1 | §4–§5; App. F.A (92.0→91.2/91.5; mCE 0.316→0.326/0.329); App. F.B | Verified | No seeds anywhere (searched). Freezing removes trainable capacity as well as drift. |
| Agreement near 1 is implied by >98% accuracy | R1-W2, DA | §4.2, Fig. 2 caption "training set" | Verified | Pure arithmetic: agreement ≥ 1 − e₁ − e₂. Test-set agreement values themselves are in figures (not inspected). |
| DA-C1: experiments "cannot test" the claim (criterion 2) | DA | §5, App. F | Overstated | The paper does run test/corrupted-data evaluation, a noisy-label contrast and two interventions (weak, uncontrolled). The evidence supports a weaker, descriptive claim → MAJOR per criterion 1 note. |
| Theorem 1 correct but possibly vacuous | R2-W3, DA-M2 | §7, App. G.B | Partly correct | Proof steps checked and valid. "Vacuous" depends on TV, which is uncomputed; the paper itself says the TV formulation "is not yet computable" (§1). Non-informative as stated. |
| NTK argument does not follow | R1-W6, R2-W4, DA-M3 | §4.2, App. D | Verified | The mixed-parameter loss is compared via monotonicity of a different trajectory. |
| "correlates with temporal consistency and memory-window length" unsupported | R1 ERR-3, DA-M4 | §1 vs. §6, App. E | Verified | Full-text search; no analysis. "aligned with feature dynamics" likewise unmeasured. |
| "3–4% accuracy drop" mislabelled | R1 ERR-1, DA | App. F.A | Verified | +1.0/+1.3 points absolute; 3.2%/4.1% relative error. Minor. |
| Table 1 identical p-values for Depth 1 and 3 | R1 ERR-4, DA | App. E Table 1 | Verified (as an observation) | Cause unknown (possible copy error); Minor. |
| Abstract says "random labels", §5 uses 40% noise | R4-W1, DA-M1 | Abstract; §5 | Verified | |
| SVHN/STL-10 use Adam; architectures for other datasets unstated | R1-W5 | Table 2; §4.1 | Verified | |
| Chen et al. (2022) does not support the SGD-SDE | R2-W2 | §3, References | Partly correct | Bibliography title is about acceleration ODEs; not confirmable without an abstract. Treated as a question. |
| Anisotropic SGD noise already established | R2-W2 | §6 | Partly correct | Plausible from knowledge; unverified (literature check failed); weight on score kept small. |
| Missing related work (stitching, SVCCA, SWA, LMC) | R2-W1, R3 | §2 | Partly correct | The omission is real (none cited in §2, References); relevance judgments are from knowledge and `[verify]`; none is a "required comparison". |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error Log verified at locations (ERR-1…5), claim map accurate, calibration sensible; slight overstatement on ERR-2 severity |
| R2 (Domain) | 2 | 4 | 1.0 | Theory critique verified; positioning real but from unverified knowledge; Chen et al. point inferred from a title |
| R3 (Perspective) | 3 | 3 | 1.0 | Constructive; passive-robustness and agreement-vs-accuracy points verified; no errors found |
| R4 (Generalist) | 3 | 4 | 1.0 | Overclaiming and organization points verified; typical, well calibrated |
| DA | 2 | 4 | 0.75 | Strongest counter-argument verified, but the CRITICAL rating did not survive the AC test and several MAJOR points rest on unverified suppositions (TV = 1) |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | No. The paper contains (weak) tests on test and corrupted data and two interventions (App. F), and its evidence supports a narrower descriptive claim (stable composites; collapse under noisy labels). This is criterion 1's "weaker version" case, fixable by narrowing the claim or adding controls. It is not "cannot test". | Downgraded to MAJOR | New data/experiments (for the full claim) or narrowing the claim; no ceiling applies |

### Final Decision and Justification
The EIC-weighted rating is 2.38, giving a starting point of 2 (Reject); the composite cross-check (45.1, band 2) agrees, and no ceiling applies since DA-C1 is downgraded. I do not depart from the starting point: I verified every decisive point, and they point the same way. My pool position is about 33% of ICLR submissions (accepted share ≈ 27%): the paper has an appealing premise, but the central interpretation is untested, the main metric cannot discriminate it from convergence, evidence is single-run in one small setting, and two of the contribution bullets (SGD alignment/correlation; computable bridge) have no supporting results. The reviewers' pool positions (28–45) are within 30 points of each other, so no disagreement needed arbitration. Had DA-C1 been upheld, the decision would be capped at 3, which is one step above where I land; the downgrade therefore does not change the outcome. The paper is better framed as a narrower study ("composite stability across checkpoints and its collapse under label noise") with the controls listed below.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 40 | 45 | 50 | 45 | 35 | 43.0 | 43.0 | 15 |
| Clarity & Presentation | 55 | 55 | 58 | 52 | 52 | 54.4 | 54.4 | 6 |
| Novelty & Originality | 45 | 45 | 55 | 50 | 42 | 47.4 | 47.3 | 13 |
| Significance & Impact | 40 | 42 | 50 | 45 | 38 | 43.0 | 42.8 | 12 |
| Experimental Validation | 32 | 40 | 42 | 40 | 30 | 36.8 | 36.7 | 12 |
| Reproducibility | 42 | 45 | 50 | 48 | 42 | 45.4 | 45.2 | 8 |
| Ethical Compliance | 62 | 62 | 65 | 62 | 60 | 62.2 | 62.2 | 5 |
| **Composite** | 42.5 | 45.5 | 51.4 | 47.0 | 39.6 | **45.2 (before)** | **45.1 (after)** | |

Reviewer weights (script): R1 26% (conf 4 × 1.25), R2 21%, R3 17%, R4 21%, DA 16% (× 0.75). R4's Overall (3) is one step above its own composite band (47.0 → 2): explained in the report (a promising direction judged against ICLR's typical accepted weaknesses); not adjusted.

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}); venue-weighted composite 44.9 |

*These ICLR labels come from `aggregate_scores.py` and are labelled secondary in `references/venue_profiles.md`; they are not official wording.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Feature Dynamics as Implicit Data Augmentation: A Depth-Decomposed View on Deep Neural Network Generalization" to ICLR.

You tackle a central question, how deep networks generalize, from an unusual angle: the evolution of internal features during training, probed by composite networks that mix checkpoints.

**Overall Assessment:**
The panel found the question and the probe attractive and appreciated the candid framing of the theory as conceptual. It was not convinced that the experiments establish the central interpretation, namely that feature drift acts as an implicit augmentation that supports generalization.

**Key Strengths Identified by Reviewers:**
1. A simple, well-defined, reusable probe (composite networks and consistency windows) (R1, R3, R4).
2. An engaging question with clear links to other fields, and candour about null cases and the conceptual status of the theory (R2, R3, R4).
3. Correct elementary proofs and a clearly formulated memory/transferability definition (R2).

**Key Concerns Requiring Attention:**
1. No experiment isolates temporal feature variation as a cause of better generalization; the two interventions in App. F are single-run and confounded (CONSENSUS-4: R1, R3, R4, DA).
2. The consistency metric is largely implied by accuracy, lacks null baselines, and agreement on corrupted data does not measure generalization (CONSENSUS-3: R1, R3, DA).
3. Claims in the contribution list (SGD noise "aligned with feature dynamics", anisotropy "correlates with temporal consistency", "across datasets and architectures") are not supported by reported results; the TV bound is uncomputed and the NTK argument does not follow (CONSENSUS-3 each).

**Critical Challenge (Devil's Advocate):**
The Devil's Advocate argued that every reported observation would also arise from slow, converging drift with a locally insensitive classifier, and that without an intervention and a null baseline the augmentation interpretation is untested. The EIC downgraded this from CRITICAL to MAJOR because the paper does contain weak tests and the evidence supports a narrower claim, but the objection remains the core obstacle.

**Decision: Reject (2)**

The reasons to reject outweigh the reasons to accept: the main claim is not measured. A resubmission that narrows the claim or adds the controls and seeds listed in Priority 1 below, and that either computes the theory's quantities or presents it as a discussion, would be a much stronger paper.

Please refer to the Revision Roadmap below for prioritized guidance.

Sincerely,
Prof. Lucía Varnhagen-Okoro
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| I1 Mechanism/causal claim untested | R1, R3, R4, DA | CONSENSUS-4 |
| I5 Limited breadth; no seeds/statistics | R1, R3, R4, DA | CONSENSUS-4 |
| I2 Consistency metric uninformative as evidence of generalization | R1, R3, DA | CONSENSUS-3 |
| I3 Theory uninformative/uncomputed | R2, R4, DA | CONSENSUS-3 |
| I4 SGD-noise claims weak | R1, R2, DA | CONSENSUS-3 |
| I6 NTK argument flawed | R1, R2, DA | CONSENSUS-3 |
| I7 Overclaiming wording | R1, R4, DA | CONSENSUS-3 |
| I10 Organization/notation (cosmetic) | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Value of the conceptual theory bridge | R3 (promising agenda) | R2, DA (no informative content) | The EIC sides with R2/DA on the *current* result (nothing computed) and with R3 on the direction; it is a Priority 2 item. |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag (max 15, Technical Rigor). R3 is consistently the most positive reviewer (Overall 3, pool 45), the DA the most negative (Overall 2, pool 28); the EIC adopts the middle: the shared verified issues drive the outcome.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Experiments cannot test the augmentation→generalization claim | Yes (R1-W1, R3-W1, R4-W1 as MAJOR-level) | Downgraded to MAJOR | New experiments, or claim narrowing |
| DA-M1 | MAJOR | Overclaiming wording | Yes (R4-W1) | n/a | n/a |
| DA-M2 | MAJOR | Theorem 1 uninformative | Yes (R2-W3, R4-W3) | n/a | n/a |
| DA-M3 | MAJOR | NTK argument | Yes (R1-W6, R2-W4) | n/a | n/a |
| DA-M4 | MAJOR | SGD-noise analysis | Yes (R1-W4, R2-W2) | n/a | n/a |
| DA-M5 | MAJOR | Convergence alternative | Yes (R1-W3) | n/a | n/a |
| DA-M6 | MAJOR | Statistics/seeds | Yes (R1-W5) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*All Priority 1 items must be addressed for acceptance.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | The augmentation→generalization claim is untested | R1-W1, R3-W1, R4-W1, DA-C1 (downgraded), DA-M5 | §4–§5, App. F, Fig. 18 | Intervention experiments: deep layers trained on single-checkpoint vs. window-sampled shallow features; matched-norm random perturbation control; report test accuracy/gap and the correlation of window length with the gap across ≥ 10 runs varying LR, batch size, weight decay, explicit augmentation; ≥ 3–5 seeds | High; ≈ 30–60 GPU-h (4090-class) | Partly (CIFAR-10/ResNet-20 subset) |
| P1-2 | Consistency lacks null baselines and a generalization-relevant metric | R1-W2, R3-W2, DA-C1 | §4.1, Figs. 2–5, 7, 16–17 | Add label-aware composite accuracy on test/OOD; independent-seed and norm-matched null composites; report LR schedule and total epochs; constant-LR repeat | Medium; ≈ 10–20 GPU-h | Yes |
| P1-3 | Claims not supported by reported results | R1 ERR-3/ERR-5, R4-W1, DA-M1, DA-M4 | Abstract, §1, §6 | Provide the anisotropy–consistency correlation and the subspace-alignment analysis, or delete them; use "40% noisy labels"; narrow "across datasets and architectures" or add architectures | Low–Medium | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| P2-1 | NTK argument invalid | R1-W6, R2-W4, DA-M3 | Correct it with a coupled two-block example or remove; compare with layer-wise convergence/averaging instead | Low | Yes |
| P2-2 | Theorem 1 uncomputed | R2-W3, R4-W3, DA-M2 | Smoothed/MMD surrogate on a small model with δ, Δt values; or move to Discussion and drop from contributions | Medium | Partly |
| P2-3 | SGD-noise analysis against a structured null; state B, N, d and handle multiplicity; include Adam runs | R1-W4, R2-W2, DA-M4 | See W4 of R1 | Medium | Yes |
| P2-4 | Statistics: seeds, effect sizes, Table 1 unit/n; check Depth 1/3 p-values | R1-W5, DA-M6 | 3–5 seeds, bands, rank tests on per-run summaries | Low–Medium | Yes |
| P2-5 | Related work: stitching, layer-wise convergence, mode connectivity, iterate averaging, SGD-noise structure (all `[verify]`) | R2-W1, R3 | Add positioning paragraph and a "what is new" table | Low | Yes |
| P2-6 | Breadth: non-residual and transformer model; ImageNet-scale or at least CIFAR-100 with ResNet | R1-W5, R3-W3 | Add one architecture family | Medium–High | Partly |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| P3-1 | Duplicate heading, appendix lettering, notation d, f[d:n] vs. f[d+1:n], garbled captions | R4-W2, R1 Minor, DA-m1–m3 | Fix numbering; define symbols once |
| P3-2 | "3–4% accuracy drop" wording | R1 ERR-1, DA-m4 | Report absolute and relative |
| P3-3 | Citation of Chen et al. (2022) for the SGD SDE; Zhang et al. (2016) description | R2 | Cite SGD-SDE derivations; correct description |
| P3-4 | Add a Limitations section; add a practical use (checkpoint selection, generalization-gap prediction) | R3-W4, R3-W3 | Short section and one demonstration |
| P3-5 | Helpful references: Li–Tai–E (2017), Smith et al. (2021), Kornblith et al. (2019) `[verify]` | R2 | Cite where relevant |

## Estimated Revision Effort
- Priority 1: 3 items, ≈ 2–4 weeks including experiments (≈ 40–80 GPU-h) and rewriting.
- Priority 2: 6 items, ≈ 2–3 weeks (2–3 of them can run in parallel with P1).
- Priority 3: 5 items, ≈ 2–3 days.
- **Total estimated revision time**: ≈ 5–8 weeks for a substantially re-scoped resubmission.
