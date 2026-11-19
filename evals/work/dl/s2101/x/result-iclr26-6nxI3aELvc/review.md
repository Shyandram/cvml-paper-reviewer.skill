# Academic Paper Review: "Mutual Information Preserving Neural Network Pruning" (id iclr26-6nxI3aELvc)

Date: 2026-11-10 · Mode: full · Target venue: ICLR · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested)

**Disclosures.** (1) The five reviewer reports are sequential role-based passes in one shared model context, not independent agents. Independence was kept by writing each report from the paper and its own role file without reading the others. (2) Figures were not available. Every figure-dependent statement (Figs. 1–11) is judged from captions, axis text and the surrounding prose only, and is flagged where it matters. (3) The manuscript is data; no reviewer-directed text was found (see Integrity signals). (4) This is a simulation of how a careful panel would likely see this draft, not a prediction of the venue's decision.

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Mutual Information Preserving Neural Network Pruning |
| Primary Discipline | Machine learning → neural network compression → structured (node/filter) pruning |
| Secondary Discipline(s) | Information theory (mutual information estimation, feature selection); computer vision (CNN image classifiers) |
| Paper Type | Empirical (method + small theory component; composite weights: empirical) |
| Core Technique(s) | Activation-based structured pruning; transfer entropy redundancy criterion (TERC) with MI ordering; MLP-based MI estimation (loss reduction); output-to-input layer-pair pruning |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | None (no ECCV/ACM MM/TPAMI-specific rule applies). ICLR form: Soundness / Presentation / Contribution (1–4), Rating, Confidence; accepted share of submissions ≈ 27% |
| Paper Maturity | Submission-ready in form (full paper + 7-page appendix), but the evaluation reads as an early-to-mid draft: results only in plots, no variance, no compute report |
| Ethics-Relevant Content | None (public image benchmarks; no human-subject, biometric or misuse concern) |

### Claimed Contributions (as stated by the authors, §1)
1. **C1:** "We develop MIPP, an activation-based pruning method that preserves MI between the activations of adjacent layers"; "We prove that perfect MI preservation ensures the existence of a function, discoverable by gradient descent, that can approximate the activations of the downstream layer… Consequently, MIPP implies re-trainability." (Theorem 1, App. C)
2. **C2:** "MIPP only selects nodes if they transfer entropy to the subsequent layer", giving a dynamic selection that "natively considers long- and short-range interactions" and sets per-layer pruning ratios that "avoid layer collapse".
3. **C3:** "Through comprehensive experimental evaluation, we demonstrate that MIPP can effectively prune networks, whether they are trained or not."
4. **C4 (abstract headline):** "we demonstrate MIPP’s ability to outperform state-of-the-art methods", including a pre-trained ResNet50 on ImageNet.

## Paper memory (factual record shared by all reviewers)

- **Setup facts.** Models/datasets: LeNet5/MNIST and deformed MNIST; VGG11, ResNet18, ResNet34 on CIFAR10; VGG19, ResNet50 on CIFAR100; pre-trained ResNet50 on ImageNet (§5). Baselines: SynFlow, GraSP (unstructured, made structured by L1-normalising node weights), ThiNet, SOSP-H; a "re-initialized" baseline replaces SOSP-H for untrained networks; only ThiNet on ImageNet "due to memory limitations" (§5). Training and re-training schedules: Table 2 (App. D.3.1). MIPP MLPs: three MLPs, two hidden layers of 256 nodes, 1500 initial iterations, 20 (VGG) or 150 (others) re-training iterations, 35 iterations for MI ordering (App. D.3.2). Pruning ratio is swept through a confidence level x%: 20 values per experiment (App. D.1). Filter-to-scalar collapse: L1 chosen among L1/L2/mean/std (App. E.2, Fig. 10, Table 3).
- **Not stated after search (full-text grep):** validation split; random seeds / number of runs / variance (except the "five" MI re-estimates, §4.2.2); GPU type, wall-clock or GPU-hours; FLOPs, parameter counts or latency; top-1 numbers in any table; code (promised "upon publication"); the criterion that defines "layer collapse"; the data used to compute activations for pruning.
- **Headline numbers:** only ImageNet "average PR of 71.1 ±0.81% and 55.6±0.62" for pre-trained / untrained ResNet50 (Fig. 6 caption); sparsity statements "above 95 %" (LeNet5) and "above 90 %" (VGG11) in §5. All accuracy results are in Figs. 1, 2, 3, 6, 8, 9, 10 (figures; not readable here).
- **Appendix adds:** Theorem 1 proof (App. C), pruning-ratio schedule (D.1), augmentation (D.2), hyperparameters (D.3), feature-selection experiment (E.1), collapse-function comparison (E.2), other methods' per-layer PRs (E.3, Fig. 11), baseline characteristics (F, Table 4).
- **Unverifiable:** all plots; garbled equations in the extracted text (Eq. 1 prime marks, Eq. 3–4 of App. C, §4.4 prime marks), Table 3 absolute-value bars.

## Integrity signals
`scripts/integrity_scan.py` on the paper text: "No reviewer-directed text or hidden characters found." No instruction addressed to reviewers or AI systems was seen while reading. Nothing to report to the editor. The reviewers read the redacted copy (identical to the original here).

## Literature check (Phase 1.5): mode strict, cutoff 2025-09-24
Fingerprint written (title, method names MIPP/TERC, 3 distinctive phrases; no authors, anonymous submission). **6 counted queries:** claim C1 ×2 ("information-theoretic filter pruning", "mutual information channel pruning"), claim C2 ×1 ("layer collapse structured pruning"), claim C3 ×1 ("trainability preserving pruning"), baseline ×1 ("ImageNet ResNet50 channel pruning"), expansion ×1 ("provable filter pruning efficient"); one 5-word query was refused and not counted. `similarity` run on the paper's opening text. **Closest prior works:** "Layer Collapse Can be Induced by Unstructured Pruning" (arXiv 2404.16890, cosine 0.14), "Pruning Convolutional Filters via Reinforcement Learning with Entropy Minimization" (arXiv 2312.04918, 0.135); no high conceptual overlap (≥ 0.30) and no text overlap (0 shared 8-grams). **Gaps left open (honest limits):** `benchmarks`, `scout`, `coverage` and the `novelty` scripts were not run, so the baseline scout has no extracted numbers and per-claim verdicts below are my reading of kept titles/abstracts (the abstracts I read in full: Provable Filter Pruning, SCOP, HRank). The search covers arXiv only: "no close prior work found" is a limit of the search, not evidence of novelty.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ilse Varga-Lindqvist, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty, area chair at ML conferences / optimization and generalization of deep networks; model compression
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what the venue actually accepts; verifies before trusting any consensus

### Reviewer 1 (Methodology): Dr. Kwabena Osei-Mintah, industrial research lab (West Africa / Europe)
- **Seniority / Expertise**: Senior industry scientist / pruning evaluation protocols (pruning-at-initialization benchmarks, retraining budgets), estimator validity
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched compute and FLOPs, reads appendices first

### Reviewer 2 (Domain): Prof. Haruka Matsuzawa-Bell, vision and compression group, large public university (East Asia)
- **Seniority / Expertise**: Senior faculty / structured pruning of CNNs, reconstruction-based filter selection, lottery-ticket literature
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Demands a novelty delta against the closest prior method; checks every citation

### Reviewer 3 (Perspective): Dr. Lucía Barrientos-Quill, signal-processing and information-theory department, technical university (Latin America)
- **Seniority / Expertise**: Mid-career / information-theoretic feature selection, sparse approximation, causal and transfer-entropy methods
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive, names the analogous classical technique

### Reviewer 4 (Generalist): Dr. Dmitri Falconer-Yilmaz, ML group, mid-size research university (Central Europe)
- **Seniority / Expertise**: Mid-career / deep-learning generalist (vision classification), not a pruning specialist
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers usually have

### Devil's Advocate: Prof. Saoirse Tanvir-Lund, evaluation-methodology and causal-inference group, research institute (North America)
- **Seniority / Expertise**: Senior faculty / ablation design, confound analysis, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, fair; asks which control would separate the claimed cause from alternatives

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Mutual Information Preserving Neural Network Pruning
## Reviewer: Dr. Kwabena Osei-Mintah, Reviewer 1 (Methodology) (industrial research lab; fictional persona)
## Expertise: pruning evaluation protocols; retraining budgets; MI/entropy estimator validity
## Date: 2026-11-10

### Protocol sweep (full-text search, appendix included)
Searched: test set/split, validation, held-out, selected/select/tuned/tuning/hyperparameter, grid search, cross-validation, early stopping, checkpoint, best model, same split, we choose/select, per task/dataset. Findings: **no validation split, no held-out statement, no checkpoint-selection statement**. Figures 2, 3, 6 report "Training" and "Test" accuracy of the pruned-and-retrained network over a sweep of 20 confidence levels x% (App. D.1), so no single operating point is selected on test data. One design choice is selected from a comparison whose data and split are unstated: "we adopted this function throughout when collapsing convolutions" (App. E.2, after Fig. 10). Share with DA: no statement that anything was trained, tuned or selected on the reported test set; nothing criterion-3-like found.

## Summary
The paper proposes MIPP, a structured pruning method that processes layer pairs from output to input and keeps a node of layer *l* only if removing it measurably hurts an MLP's ability to reconstruct the activations of layer *l+1* (a TERC-style test, with nodes pre-sorted by their individual MI). The mutual information is estimated as the reduction in MLP prediction loss (§4.2.2, Eq. 1); the confidence x% with which a node must "transfer entropy" is the knob that sets sparsity. A theorem (App. C) is offered to link MI preservation to the existence of a reconstruction function, which the authors present as implying re-trainability. Experiments cover LeNet5, VGG, ResNet on MNIST/CIFAR and a pre-trained ResNet50 on ImageNet, against four baselines, with accuracy and a "layer collapse" rate plotted against neuron reduction.

## Strengths

### S1: The pruning criterion is concrete and the layer-collapse question is measured
Fig. 3 plots the fraction of runs that collapse per pruning-level bin for every method and architecture, and Figs. 4, 5, 11 show per-layer ratios for MIPP and the baselines. Few pruning papers instrument collapse this directly; the per-layer plots make the method's behaviour inspectable (§5, "Figure 4 … block-based PRs").

### S2: Hyperparameters of the method itself are largely documented
App. D.3.2 gives MLP size, iteration counts, number of MLPs; Table 2 gives training and re-training schedules; D.2 the augmentation. This is better than the usual "details in code".

### S3: Honest about a failure regime and a design ablation
§5 ("LeNet5 on deformed MNIST") states that MIPP is "inapplicable to models whose input data contains information not relevant for the classification task" when pruning untrained networks, and App. E.2 compares four filter-collapse functions rather than assuming one.

## Weaknesses

### W1: No variance, no seeds, no tables; results cannot be checked or compared
No run count or seed appears anywhere. All accuracy results are plots; §5 itself says "despite noisy results, MIPP generally outperforms baselines" (ResNet50/CIFAR100). In Fig. 3 the unit is "the percentage of runs that lead to layer collapse" per 5% bin, but with 20 x-values per experiment (App. D.1) the number of runs per bin is not given (if each x-value is run once, each bin holds only a few runs and the percentage can only take values like 0/50/100: *derived conjecture, please clarify*). Claims such as "more resistant to layer collapse" therefore rest on a handful of runs.
- **Suggested Fix:** report mean ± std over ≥ 3 seeds for the CIFAR settings (pruning + re-training), the number of runs per bin in Fig. 3, and a table of exact accuracies at matched sparsity. Rough cost: ResNet18/CIFAR10 prune-and-retrain is on the order of an hour per run; 3 seeds × 20 x-values × 4 methods ≈ 240 runs ≈ 200–300 GPU-hours for the small models (estimate).

### W2: Baselines and matching do not support "state of the art"
GraSP and SynFlow are unstructured pruning-at-initialization methods; they are made structured by "L1-normalization to all the weights associated with a node" (§5), a conversion that is not part of those methods. ThiNet receives "a uniform PR across all layers", and every baseline gets MIPP's average neuron reduction "as the global PR". Matching is on average neuron reduction, not on FLOPs or parameters, although MIPP's own per-layer allocation (more nodes kept early, §5) changes FLOPs at equal neuron reduction. The structured methods the paper itself cites and that target the same property are not compared: Trainability Preserving Neural Pruning (Wang & Fu, 2023), CHIP (Sui et al., 2021), HRank (Lin et al., 2020), Provable Filter Pruning (Liebenwein et al., 2020). On ImageNet only ThiNet is run, "due to memory limitations", and the text claims only that "MIPP generally outperforms ThiNet at test time". Re-training schedules for baselines are not stated separately from MIPP's (Table 2 lists one recipe per dataset).
- **Suggested Fix:** report FLOPs/params and compare at matched FLOPs on ResNet50/ImageNet against at least TPP, CHIP/HRank and one recent baseline with a common re-training recipe; state which numbers are re-run versus copied; give the baselines the same anti-collapse safeguard (minimum width per layer). Cost: ImageNet ResNet50 re-training of 75 epochs ≈ 100–200 GPU-hours per configuration; matched-FLOPs runs for 3 baselines ≈ 500+ GPU-hours (estimate); partly feasible via published checkpoints.

### W3: The MI "estimator" compares unequally trained networks and is never validated
§4.3 and App. D.3.2: one MLP is trained for 1500 iterations; after masking a node the MLP is re-trained "not to the same extent as in the first instance" (20 iterations for VGG, 150 for others) and the loss is compared with the original; MI ordering uses only "35 iterations due to time constraints". The keep/prune decision thus depends on MLP capacity (two hidden layers of 256 units predicting layers that are up to 2048 channels wide), on the iteration counts, and on five repetitions used to form a "confidence" x% (§4.2.2) that is swept up to ≈ 100% (App. D.1), a level five samples cannot meaningfully support. No sensitivity study to any of these is given. For convolutional layers each filter is collapsed to a single scalar by an L1 norm (App. E.2), so the quantity being reconstructed is not the layer's activation as Theorem 1 assumes.
- **Suggested Fix:** ablate MLP width/iterations/repeats on one CIFAR model; report agreement of kept sets across repeats; validate the estimator on a synthetic case where the true conditional MI is known. Cost: low (< 20 GPU-hours).

### W4: Protocol and cost omissions that the claims depend on
(i) What data are the activations computed on, and how many samples? Not stated after search. (ii) The motivation (§1) is that iterative structured methods are "computationally impractical for large models", yet MIPP trains three MLPs per layer and re-trains one per candidate node; no wall-clock, GPU-hours or comparison with baselines' pruning time is reported, and the "linear in time" statement (§4.2.1) concerns TERC, not the full procedure. (iii) The collapse function was picked on a comparison (Fig. 10) whose dataset/split is not stated. (iv) "The implementation of MIPP will be made available upon publication"; no code at review time.
- **Suggested Fix:** report data and sample counts for MI estimation, total pruning time per model and per baseline, and the data/split behind Fig. 10; provide anonymized code.

### W5: The "trained or not" claim is only partly supported
C3 says MIPP prunes "networks, whether they are trained or not", but §5 reports that on untrained VGG11 "MIPP remains competitive but is slightly out-performed by both GraSP and reinitialize baselines", the same on VGG19/CIFAR100, and a drop on deformed MNIST (Fig. 1). The "re-initialized" baseline is never defined (re-initialized weights under which architecture: MIPP's per-layer widths, or the original?). Without a control that trains the pruned architecture from scratch, it is unclear how much of any "pruning at initialization" result comes from the selected nodes rather than the resulting layer widths.
- **Suggested Fix:** define the baseline; add (a) the MIPP-derived architecture trained from scratch and (b) a random node choice with MIPP's per-layer widths.

### Claim-to-evidence map (compressed)
| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|--------------|----------|---------|
| C1 | Theorem: MI preservation ⇒ existence of a GD-discoverable reconstruction function ⇒ "MIPP implies re-trainability" | Abstract, §1, §4.1, App. C | Proof in App. C; no re-trainability experiment beyond accuracy curves | Unsupported as worded (existence only; see ERR-1/2) |
| C2 | Node selection accounts for interactions and avoids layer collapse | §1, §4.3, Figs. 3–4 | Fig. 3 (collapse rate), Fig. 4 | Partially supported (figures unavailable; collapse undefined; few runs) |
| C3 | Prunes trained and untrained networks effectively | §1, §5, Figs. 1–2 | Fig. 2 | Partially (competitive, slightly worse on untrained VGG) |
| C4 | Outperforms state of the art incl. ResNet50/ImageNet | Abstract, §5 last paragraph | Fig. 6 (ThiNet only) | Unsupported as worded |

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | App. C, after Eq. 4 | "The only circumstances under which Equation 4 holds is if" | The step from a Donsker–Varadhan identity to f(X′)=X_L is asserted, not derived; the supremum is also attained by X_L plus any constant, so "only if f = X_L" is not literally true; "discoverable by gradient descent" is never proved though §1 states it as proved | Read the proof; cross-referenced with §1 contribution 1 and §4.1. Equations are garbled in extraction, so the algebra itself is partly unverifiable | Medium | MAJOR | State Theorem 1 for discrete variables with a full proof, drop or prove the GD claim |
| ERR-2 | E3 | §4.4, "Theoretical argument" | "these pairs share perfect MI" | I(X_l;X_{l+1})=H(X_{l+1}) holds for discrete variables; for continuous activations related by a deterministic map the MI is infinite/ill-defined, so "preserving MI" has no literal meaning for real-valued ReLU activations. The implemented estimator (MSE reduction) is only an approximation "under certain circumstances" (§4.2.2) that are not specified | Cross-referenced §4.4 with §4.2.2 | Medium-High | MAJOR | State assumptions (discretization, noise model) under which the equivalences hold |
| ERR-3 | E6 | App. D.1 | "where r = 0.5 and x0 = 50" | The recursion x_n = x_0 + Σ(1−x_{i−1})·r only makes sense with x as a fraction; with x_0 = 50 the factor (1−50) is negative. With fractions, x_n = 1−2^−(n+1): x_1 = 75%, x_19 ≈ 99.9999%. Also "20 different values" vs n ∈ [0,20] = 21 values | Recomputed | High | MINOR | Fix units and count |
| ERR-4 | E6 | App. E.2 vs Tables 3, 4 | "please refer to Table 4" | Collapse functions are in Table 3; Table 4 compares baseline characteristics | Cross-referenced | High | MINOR | Correct the reference |

## Dimension Scores (0–100)

**Pool position:** better than about 28% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison is against weak/adapted baselines on small CNN benchmarks with no variance, and the theory claim ("implies re-trainability") is not established.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Theorem/estimator gaps (ERR-1/2), unvalidated estimator (W3), approximation by L1-collapse not covered by theory |
| Clarity & Presentation | 55 | Competent | Readable method description; collapse and baselines under-defined; results only in plots |
| Novelty & Originality | 50 | Developing/Competent | Composition of TERC, loss-based MI estimate and reconstruction pruning; modest differentiation |
| Significance & Impact | 45 | Developing | Small-scale CNNs; no demonstrated gain at the sub-field's standard benchmark |
| Experimental Validation | 38 | Developing | No variance; weak baselines; ImageNet vs ThiNet only; no FLOPs |
| Reproducibility | 40 | Developing | MLP settings given, but data for MI, cost, seeds, code missing |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations partly discussed (§5) |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Avg(TR, EV) = 40 → 1; one step up because the design is coherent and instrumented |
| Clarity | 2 | 55 |
| Significance | 2 | 45 |
| Originality | 2 | 50 |

## Questions for Authors
1. How many runs back each point of Figs. 2–3, and how many runs fall into each 5% bin of Fig. 3? Mean ± std over seeds would change my view of C2.
2. At matched FLOPs, how does MIPP compare with TPP and CHIP/HRank on ResNet50/ImageNet under one re-training recipe? A win there would raise my rating by one step; a loss would lower it.
3. What is the total pruning time for ResNet50/ImageNet versus ThiNet?
4. On which data and how many samples are activations and MIs computed (§4.2.2, App. D.3.2)?
5. Does Algorithm 1 (line 3, which passes the unpruned X_{l+1}) condition on the pruned next layer as §4.4 argues? (§4.4's prime marks are garbled in my copy.)

## Limitations Assessment
**Partially.** §5 discusses the untrained/deformed-MNIST regime. Missing: cost of the procedure, sensitivity to the estimator, restriction to CNNs, the scalar-collapse approximation.

## Ethics Review Flag
**No**

## Overall Score
**2**: Reject. A coherent criterion with an instrumented collapse analysis, but the headline claims (re-trainability guarantee, state of the art) are not supported and the evidence lacks variance, cost and fair structured baselines.

## Confidence
**4**: Confident; figures could not be inspected and proof equations are garbled in extraction.

---

# Peer Review Report

## Paper: Mutual Information Preserving Neural Network Pruning
## Reviewer: Prof. Haruka Matsuzawa-Bell, Reviewer 2 (Domain) (vision and compression group, large public university; fictional persona)
## Expertise: structured pruning of CNNs; reconstruction-based filter selection; pruning at initialization
## Date: 2026-11-10

## Summary
The paper frames structured pruning as selecting nodes such that the next layer's activations remain predictable from the kept nodes of the current layer, measured via mutual information. It adapts TERC (Westphal et al., 2024, a feature-selection method from RL state-variable selection) with a loss-reduction MI estimator, processes layers from output to input, and obtains per-layer pruning ratios automatically. It argues this avoids ranking, layer collapse and loss of re-trainability, and evaluates on CNN classifiers from LeNet5 to ResNet50, with a feature-selection side experiment.

## Strengths

### S1: A principled, easy-to-state selection principle with automatic layer-wise ratios
Selecting nodes by whether they carry information about the next layer (§3, §4.2.1) yields per-layer ratios without a hand-set allocation, a real practical issue in global pruning (§1, Figs. 4, 5). Per-layer plots (Figs. 4, 11) make the allocation interpretable.

### S2: Relevant failure analysis and related-work scope
§2 correctly organises the space into activation-based, layer-wise-ratio and unstructured-to-structured work, and the paper's focus on layer collapse (Lee et al., 2019; Tanaka et al., 2020) is a known, legitimate problem for structured pruning of deep nets.

### S3: Breadth of architectures and a spin-off use
The same criterion is used for filters (App. E.2) and for input-pixel selection (App. E.1), and results span six model/dataset pairs plus ImageNet.

## Weaknesses

### W1: The core mechanism is a composition of existing pieces, and the closest method is not differentiated
§4.2.1 states that "we are able to deploy an out-of-the-box solution" (TERC), the MI estimator is that of Covert et al. (2020) and Gadgil et al. (2024) (§4.2.2), and output-to-input layer-pair processing follows ThiNet "like Luo et al. (2017)" (§4.4). Eq. (1) shows the criterion reduces to "a simple comparison of a loss function with and without a node": keep a node if a learned decoder can no longer reconstruct the next layer without it, which is the reconstruction criterion of ThiNet (§2: "greedily selects nodes if they minimize the error in reconstructing the activations of the next layer") and of Ding et al. (2019), with an MLP decoder and a confidence threshold added. §2 dismisses ThiNet as "too restrictive, as it does not consider the effects of re-training", which is asserted, not shown. The MI vocabulary adds little beyond this reconstruction view. Novelty is therefore real but modest (see the table below).
- **Suggested Fix:** add a method-level comparison table (criterion, decoder class, order, layer-wise ratios) against ThiNet and Ding et al., and an ablation replacing the MLP/TERC criterion by a ThiNet-style linear reconstruction under the same pipeline.

### W2: Positioning contains claims that do not match the cited work's own abstract, and key related lines are missing
(a) §2 says Liebenwein et al. (2020) "developed an activation-based pruning scheme with the ability to establish layer-wise PRs. However, this method is not well adopted as it employs prohibitively expensive iterative re-training", and §1 cites it for structured solutions being "computationally impractical for large models". The abstract of *Provable Filter Pruning for Efficient Neural Networks* (arXiv 1911.07412) describes a sampling-based method that uses "a small batch of input data points to assign a saliency score to each filter" with "provable guarantees on the size and performance of the pruned network"; it does not mention iterative re-training. This also sits uneasily with the abstract's claim that "global pruning methods do not offer any guarantees regarding re-training". I rate this a partly-checked mismatch (I have only the abstract), so the authors should verify and correct the description. (b) Not discussed: information-theoretic compression of networks (variational information bottleneck pruning, Dai et al. 2018), generic structural pruning frameworks (DepGraph), layer-adaptive sparsity allocation (LAMP), and work showing that pruning-at-initialization gains largely reflect layer-wise ratios (Frankle et al., 2021), which bears directly on the "re-initialized" baseline and on contribution 2. (c) The introduction's premise that pruning and re-training beats training a smaller model from scratch (§1, citing LeCun et al., 1989 and others) is contested by Liu et al. (2019).
- **Suggested Fix:** correct the Liebenwein description against the paper itself; add the missing work to §2 and discuss each in one sentence of difference.

### W3: The theoretical contribution is narrower than presented
Theorem 1 states an equivalence between existence of a reconstruction function g (over an unrestricted class F) and MI preservation; it does not concern the function class of the pruned network (an affine map followed by an activation, retrained jointly with the rest of the net), nor end-to-end accuracy. "Discoverable by gradient descent" (§1, §4.1) is not proved. The conclusion that MIPP "ensures re-trainability in a manner that is more rigorous than competing techniques" (§4.1) is unsupported, and the practical method (approximate MI, confidence threshold, scalar collapse of filters) does not achieve "perfect MI preservation" in any case. The domain consequence is that C1 should be stated as "reconstructability of the next layer by a learned decoder".
- **Suggested Fix:** restate C1/§4.1 accordingly, or add a restricted-class statement with proof and an empirical test (does re-training succeed because reconstruction succeeded?).

### W4: Evidence does not reach the sub-field's standard for a significant contribution
Evaluation is on LeNet5/MNIST, VGG/ResNet on CIFAR and one ImageNet ResNet50 run versus a 2017 method. The accepted standard in recent structured-pruning papers is ResNet50/ImageNet top-1 against FLOPs versus several recent baselines; no FLOPs or top-1 numbers are tabulated here (see R1-W2). The abstract's "outperform state-of-the-art" is not met (see literature-check addendum).
- **Suggested Fix:** as in R1-W2; and consider a modern architecture (ViT or a small LLM) or narrow the claim to "small CNN classifiers".

### W5: Citation accuracy (E7), minor
Reference entries that look wrong to me, to be checked by the authors: GraSP ("Picking winning tickets before training by preserving gradient flow", Wang, Zhang, Grosse) is listed "In ICLR’22, 2022", whereas I recall ICLR 2020 [verify]; Liebenwein et al. is listed "In NeurIPS’20", whereas I recall ICLR 2020 [verify]; the author list of "Discrimination-aware channel pruning" is garbled in the bibliography ("Zhuang Liu, Mingxing Tan, Bo Zhuang, …") [verify].

## Literature-check addendum

**Per-claim novelty (claim-level profile; my reading of kept abstracts, `novelty` script not run).**
| Claim | Dimension | Novelty | Top prior work (label, link, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------|-----------|
| C1 MI-preserving layer-pair pruning with re-trainability guarantee | method | medium | ThiNet (ICCV 2017; cited, level ≈ 3: reconstruction of next layer, different criterion); Dai et al. 2018 VIBNet (prior, arXiv 1802.10399, not cited, level 2: information-theoretic compression) | No close prior work found for TERC-based layer-pair pruning in 3 queries (arXiv only); guarantee claim is the weak part |
| C2 Interaction-aware selection with automatic per-layer PR avoiding collapse | method | medium | SynFlow (cited), "Layer Collapse Can be Induced by Unstructured Pruning" (prior, arXiv 2404.16890, not cited, level 2) | Collapse avoidance via iterative scoring is known for unstructured pruning; structured, activation-based version is new |
| C3 Prunes trained and untrained nets | result | incremental | Pruning-at-initialization line (SNIP, GraSP, SynFlow; cited) | Result attribute only competitive with existing methods |
| C4 Beats SOTA incl. ImageNet ResNet50 | result | not established | HRank (arXiv 2002.10179), SCOP (NeurIPS 2020), TPP (ICLR 2023; cited), MDP (2025), GDP (2021) | Not compared |

No claim is established as "known"; no candidate for DA criterion 7. Closest prior work as a whole: ThiNet (Luo et al., 2017, cited) and, by similarity search, arXiv 2404.16890 (cos 0.14, below any overlap threshold).

**Novelty delta table**
| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| Next-layer-informed node selection | ThiNet (Luo et al., 2017) | Greedy filter selection minimising next-layer reconstruction error, output-to-input | Learned MLP decoder + TERC/MI ordering + confidence threshold, automatic ratios | Cited; differentiation weak (§2 "too restrictive") |
| Information-theoretic pruning | Dai et al. 2018 (VIBNet) | Information-bottleneck-regularised compression | Post-hoc MI-preserving selection | Not cited |
| Avoiding collapse | SynFlow (Tanaka et al., 2020) | Iterative scoring conserving flow, no collapse | Structured, data-dependent | Cited |

**Baseline scout table.** Benchmark: ImageNet, ResNet50 (top-1 vs FLOPs). Numbers not extracted (scout not run). Prior-label methods not compared in the paper: TPP (Wang & Fu 2023, cited, peer-reviewed), HRank (arXiv-only prior, cited), CHIP (cited), SCOP (NeurIPS 2020), GDP (peer-reviewed, 2021), MDP (peer-reviewed 2025). A missing baseline from prior work is MAJOR at most; no under-reported baseline could be checked because the paper gives no numbers.

**Field snapshot (as of the cutoff, from kept results and general knowledge).** Structured CNN pruning moved from norm- and Hessian-based scores (Li et al., 2017; SOSP, 2022) to reconstruction- and rank-based criteria (ThiNet, HRank), then to regularisation that targets trainability (TPP, ICLR 2023) and architecture-agnostic dependency handling (DepGraph, CVPR 2023); recent work targets latency-constrained pruning of vision transformers and LLMs (e.g., MDP, 2025). The standard test is ResNet50/ImageNet with top-1 at stated FLOPs against several recent baselines under one re-training recipe. For this sub-field, a +0.3–0.5 point gain on small CIFAR models is incremental; a clear matched-FLOPs gain on ImageNet, a new capability (e.g., a guarantee that is tested), or a 2× cost reduction at equal accuracy is significant. I used this to place Significance at 48 and Novelty at 52.

## Missing References
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical (missing comparison; already cited) | Huan Wang, Yun Fu. "Trainability Preserving Neural Pruning", ICLR 2023 (found, prior peer-reviewed) | Targets the same property (trainability after pruning) in structured pruning; must be compared empirically |
| Important | Bin Dai, Chen Zhu, David Wipf. "Compressing Neural Networks using the Variational Information Bottleneck", ICML 2018 (verified: https://arxiv.org/abs/1802.10399v3) | Information-theoretic structured compression; differentiate from MI-preserving selection |
| Important | Gongfan Fang et al. "DepGraph: Towards Any Structural Pruning", CVPR 2023 (verified: https://arxiv.org/abs/2301.12900v2) | Standard modern structural-pruning framework and benchmark |
| Important | Jaeho Lee, Sejun Park, Sangwoo Mo, Sungsoo Ahn, Jinwoo Shin. "Layer-adaptive Sparsity for the Magnitude-based Pruning", ICLR 2021 (verified: https://arxiv.org/abs/2010.07611v2) | Layer-wise ratio allocation baseline for contribution 2 |
| Important | Jonathan Frankle, Gintare Karolina Dziugaite, Daniel Roy, Michael Carbin. "Pruning Neural Networks at Initialization: Why are We Missing the Mark?", ICLR 2021 (verified: https://arxiv.org/abs/2009.08576v2) | Per-layer widths explain much of pruning-at-init; relevant to the untrained-network claim |
| Important | Zhuang Liu, Mingjie Sun, Tinghui Zhou, Gao Huang, Trevor Darrell. "Rethinking the Value of Network Pruning", ICLR 2019 (verified: https://arxiv.org/abs/1810.05270v2) | Train-from-scratch control for pruned architectures |
| Helpful | Yang He et al. "Filter Pruning via Geometric Median for Deep Convolutional Neural Networks Acceleration", CVPR 2019 (verified: https://arxiv.org/abs/1811.00250v3) | Widely used filter-pruning baseline |
| Helpful | Tao Zhuang et al. "Neuron-level Structured Pruning using Polarization Regularizer", NeurIPS 2020 [verify] (not found on arXiv by title) | Structured baseline with learned layer-wise allocation |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Avg(TR 52, EV 45) = 48.5 |
| Clarity | 2 | 58 |
| Significance | 2 | 48 |
| Originality | 2 | 52 |

## Dimension Scores (0–100)

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a plausible, modestly novel criterion, but the evidence is below the sub-field's bar (no recent structured baselines at matched FLOPs) and the theory claim is overstated.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing/Competent | Sound idea; Theorem 1 narrower than claimed; estimator approximations |
| Clarity & Presentation | 58 | Competent | Related work organised; some descriptions unmatched with cited work |
| Novelty & Originality | 52 | Competent | Composition of TERC + MLP-MI + ThiNet-style reconstruction; automatic ratios |
| Significance & Impact | 48 | Developing | Small CNNs; no standard-benchmark gain demonstrated |
| Experimental Validation | 45 | Developing | Missing recent structured baselines and FLOPs |
| Reproducibility | 50 | Developing/Competent | MLP details given; code only promised |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. How does MIPP differ, in the selected set and in accuracy, from ThiNet with the same output-to-input order and an MLP decoder? A clean ablation would raise my Novelty score.
2. Is the description of Liebenwein et al. (iterative re-training, "prohibitively expensive") taken from that paper's body? Please give the location.
3. Why is TPP, which the paper cites for trainability-preserving structured pruning, not a baseline?
4. Can Theorem 1 be restated for the function class of the pruned layer?

## Limitations Assessment
**Partially.** Missing: restriction to classification CNNs, reliance on scalar collapse of filters, cost of the method.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A reasonable but modestly novel criterion with overstated theory and incomplete positioning; the evidence is below the field's standard for the stated "state of the art" claim.

## Confidence
**4**: Confident on the pruning literature; I read three abstracts in full and cannot see the figures.

---

# Peer Review Report

## Paper: Mutual Information Preserving Neural Network Pruning
## Reviewer: Dr. Lucía Barrientos-Quill, Reviewer 3 (Perspective) (signal-processing and information-theory department, technical university; fictional persona)
## Expertise: information-theoretic feature selection; sparse approximation; transfer entropy
## Date: 2026-11-10

## Summary
MIPP turns pruning into a feature-selection problem between adjacent layers: keep the nodes whose removal reduces the predictability of the next layer. The authors borrow a feature-selection criterion (TERC), estimate mutual information through an MLP loss difference, and run it from the output layer toward the input. They report that this gives layer-wise pruning ratios that avoid layer collapse, on CNNs from LeNet5 to ResNet50, and show the same machinery can select input pixels (App. E.1).

## Strengths

### S1: A useful bridge between feature selection and network pruning
Treating the previous layer as a candidate feature set for the next (§4.2.1) imports a mature literature (mRMR-style selection, Battiti 1994; Peng et al., 2005; cited) into pruning. The side result that the same method selects pixels (App. E.1, Figs. 7–9) is a nice demonstration of the unified view.

### S2: Interpretable by-products
Figs. 4, 5 and 11 show how per-layer ratios follow the ResNet block structure (periodicity of two for ResNet34, of three for ResNet50, §5), which can inform architecture design rather than only produce a pruned model.

### S3: Candid about the regime where it fails
§5 explains that on untrained networks the method can only preserve information already in the inputs and is "inapplicable" when the inputs contain task-irrelevant information. That is a precise, falsifiable scope statement that most pruning papers do not make.

## Weaknesses

### W1: Deployment value is asserted, not measured
The paper motivates pruning by "resource consumption and costs" (Abstract) but reports only "Average Neuron Reduction"; no FLOPs, parameters, latency or memory (searched: none stated). Structured pruning's benefit depends on hardware; narrow, non-uniform layer widths (e.g., early-layer-heavy allocation, §5) can run slower than uniformly pruned nets. Conversely, the cost of the pruning procedure (three MLPs per layer, a retrained MLP per candidate node) may exceed that of the baselines, and no figure is given.
- **Suggested Fix:** report FLOPs and measured latency on a stated device for the ImageNet model, and pruning wall-clock per method.

### W2: Four unexamined assumptions carry the argument
(1) *Information in activations ⇒ usefulness for the task.* MIPP preserves information about the next layer (ending at the logits) but not specifically task-relevant information; §4.4's argument that preserving the outputs' information yields "only the entropy required to reproduce the outputs" does not follow for hidden layers whose entropy includes nuisance variation. (2) *Local layer-pair preservation composes into global performance.* Errors accumulate across pairs, and the next layer used as the target is itself an approximation. (3) *Scalar collapse suffices for filters.* Reducing each filter to its L1 norm (App. E.2) discards spatial structure, yet the theory is for full activations. (4) *Transfer entropy.* The name comes from time-series causality; here there is no temporal structure and the criterion is a conditional-MI test with removal, so the "transfer" framing (§1, §3) is a formal analogy.
- **Suggested Fix:** state these assumptions explicitly in §3–4 and test (2) and (3) empirically, e.g., compare against keeping full filter activations for LeNet5 or a small ResNet.

### W3: Classical analogues are not used for comparison
Choosing a column subset of a layer that preserves the next layer's output is the column subset selection / leverage-score-sampling problem in numerical linear algebra, and the information-bottleneck literature has critiques of the compression-phase story the paper leans on in §4.4 (Tishby & Zaslavsky, 2015; Shwartz-Ziv & Tishby, 2017; critique: Saxe et al., ICLR 2018 [verify]). A cheap spectral/leverage baseline would show whether the information-theoretic machinery is needed.
- **Suggested Fix:** add a column-subset-selection baseline (e.g., leverage-score or pivoted-QR selection of nodes) on one CIFAR model.

### W4: Broader impact is unaddressed
No statement on how compression may change behaviour across classes or subgroups (compressed networks can lose accuracy unevenly; Hooker et al., 2019, "What do compressed deep neural networks forget?" [verify]) and no energy measurement behind the claimed "positive implications".
- **Suggested Fix:** report per-class accuracy changes on CIFAR100 and a short impact paragraph.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Avg(TR 52, EV 46) = 49 |
| Clarity | 2 | 60 |
| Significance | 2 | 52 |
| Originality | 2 | 56 |

## Dimension Scores (0–100)

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting cross-field idea and interpretable by-products, but deployment evidence and key assumptions are missing.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing/Competent | Assumption chain untested |
| Clarity & Presentation | 60 | Competent | Readable; framing borrowed from RL/feature-selection |
| Novelty & Originality | 56 | Competent | Fresh cross-field transfer |
| Significance & Impact | 52 | Competent | Potentially useful; unmeasured |
| Experimental Validation | 46 | Developing | No hardware or cost metrics |
| Reproducibility | 48 | Developing | Cost and code missing |
| Ethical Compliance | 62 | Competent | No human data; limitations partly stated, no impact discussion |

## Questions for Authors
1. What is the measured latency on a stated device for the pruned ResNet50 versus ThiNet's and the unpruned model? A speed-up would raise my Significance score.
2. Does keeping full filter activations (not L1 scalars) change which nodes are kept on a small ResNet?
3. How much does the pruned model's per-class accuracy shift on CIFAR100?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**: nothing at stake beyond a short impact note.

## Overall Score
**3**: Borderline Reject. The cross-field framing and by-products are attractive, but the deployment value and the assumption chain are not demonstrated, and the evidence is thin for ICLR.

## Confidence
**3**: Fairly confident; pruning-specific baselines are outside my main area, and figures were not available.

---

# Peer Review Report

## Paper: Mutual Information Preserving Neural Network Pruning
## Reviewer: Dr. Dmitri Falconer-Yilmaz, Reviewer 4 (Generalist) (ML group, mid-size research university; fictional persona)
## Expertise: deep learning for vision; training and generalization
## Date: 2026-11-10

## Summary
The paper addresses three weaknesses it attributes to global structured pruning (static ranking, layer removal, no re-training guarantee). Its answer, MIPP, keeps a node only if an MLP can no longer reconstruct the next layer without it, estimating mutual information through the MLP's loss and processing layers from the output backwards. A theorem is presented as justifying re-trainability. Experiments on small and mid-size CNNs and ImageNet ResNet50 are summarised in accuracy-versus-neuron-reduction plots and layer-collapse plots.

## Strengths

### S1: Clear problem statement and motivation
§1 names three drawbacks and maps each to a mechanism of MIPP (§4.3 "mechanistic features"), which makes the contribution easy to state.

### S2: Method description is followed by algorithm boxes and appendix hyperparameters
Algorithms 1–2 (App. B), Table 2 and App. D.3 give enough for a reader to understand the pipeline, which is better than many submissions.

### S3: Breadth and honesty
Six model/dataset pairs plus ImageNet, ablation of the collapse function (App. E.2), and an explicit discussion of where the method does not help (§5, deformed MNIST).

## Venue Criteria Checklist (ICLR: soundness, presentation, contribution)
| Item | Status | Location |
|------|--------|----------|
| Claims supported by evidence | Partly | Abstract "outperform state-of-the-art" vs Fig. 6 (ThiNet only); C1 "implies re-trainability" vs App. C |
| Technical soundness of theory | Partly | Theorem 1 (§4.1, App. C) is existence-only |
| Experimental coverage of the standard benchmark | Partly | ImageNet ResNet50 vs one baseline |
| Presentation: terms and figures self-contained | Partly | Layer collapse, "Re-initialized", "Average Neuron Reduction" |
| Reproducibility (code, cost) | Not met | "upon publication"; no cost |
| Contribution significance for the ICLR audience | Partly | Small CNNs; modest novelty |

## Weaknesses

### W1: The main evidence is not presentable as evidence
All quantitative results are in figures (Figs. 2, 3, 6), with panels whose y-axes differ and a text that mostly says "competitive", "generally outperforms" or "noisy". There is no table of numbers, no stated unpruned reference accuracy, and the ImageNet result (Fig. 6) is a single plot with an "average PR of 71.1 ±0.81%". A reader cannot compare with the literature, and the abstract's headline "outperform state-of-the-art methods" and the final sentence of §5 ("surpass state-of-the-art performance when pruning trained NNs") are not backed by a comparison with recent structured methods; §5 itself concedes "SOSP-H does outperform MIPP at test time" for ResNet34 at 80–90%.
- **Suggested Fix:** one main table (model, sparsity/FLOPs, accuracy ± std, methods) and a narrower abstract.

### W2: Key terms and procedure steps are undefined or inconsistent
"Layer collapse" is only characterised in a Fig. 3 caption ("untrainable layer collapse") with no criterion; "sparsity" and "neuron reduction" are used interchangeably (§5); "Re-initialized baseline" is never defined; §1 says "Rather than ranking nodes and selecting the top-k", yet §4.2.1 says "we sort the nodes in the pruning layer in descending order of MI with the target", so MIPP does rank; Algorithm 1 line 3 passes the unpruned X_{l+1} whereas §4.4 argues for conditioning on the pruned layer (the primes are garbled in my copy, so I list this as a question rather than an error); the handling of convolutions, used in every CNN experiment, is relegated to App. E.2.
- **Suggested Fix:** add a short definitions paragraph and move the filter-collapse description to §4.

### W3: Scope for the venue
For ICLR in 2026 the audience will ask whether the idea transfers to transformers or large models; the evaluation is CNN-only and small except one ImageNet run, and the theory does not cover the approximations used. Not fatal: many accepted pruning papers are CNN-only, but those typically show a clear matched-FLOPs ImageNet gain.
- **Suggested Fix:** narrow the claim to CNN classifiers and add the ImageNet comparison, or add a ViT experiment.

### W4: Unsupported explanatory statements
§5: "This is because CNNs are known to generalize better when their remaining nodes are concentrated in the early layers" (no citation), and SOSP-H's behaviour is explained as "due to its ability to establish performant layer-wise PRs", with no test.
- **Suggested Fix:** cite or test, or phrase as hypotheses.

**Minor:** typos ("critereon", "If Figure 10", "tendancy", "textupfL−1", "CCVPR’09"); Table 1 lists notation types with unclear symbols; Fig. 7 selection is described as "significantly stochastic" and "non-intuitive" yet used to claim "state-of-the art test accuracy" (E.1).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Avg(TR 50, EV 46) = 48 |
| Clarity | 2 | 56 |
| Significance | 2 | 50 |
| Originality | 2 | 52 |

## Dimension Scores (0–100)

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea with partly supported claims; the weaknesses (no tables, a single-baseline ImageNet result) are more serious than those typical of accepted pruning papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Theory narrower than claimed |
| Clarity & Presentation | 56 | Competent | Understandable; undefined terms; figure-only results |
| Novelty & Originality | 52 | Competent | Recombination, modest |
| Significance & Impact | 50 | Developing/Competent | Useful if scaled |
| Experimental Validation | 46 | Developing | Thin ImageNet evidence |
| Reproducibility | 46 | Developing | Code promised only |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. Can you provide one table with exact accuracies, FLOPs and std over seeds? That would move me to Overall 4 if the ImageNet comparison holds against a recent baseline.
2. How is a layer defined as "collapsed" in Fig. 3?
3. What is the unpruned accuracy line in Fig. 2/6?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. Clear idea, readable, but claims in the abstract outrun the evidence, and results are not presented in a checkable form.

## Confidence
**4**: Confident on the presentation and venue-fit judgment; less on pruning specifics.

---

# Devil's Advocate Report

## Paper: Mutual Information Preserving Neural Network Pruning
## Reviewer: Prof. Saoirse Tanvir-Lund, Devil's Advocate (evaluation-methodology and causal-inference group, research institute; fictional persona)

---

## Steelman
Pruning a trained network by keeping only the nodes needed to predict the next layer is a sensible, information-grounded criterion; it sets per-layer ratios automatically, and across six model/dataset pairs the authors show it collapses less often than score-ranking baselines at high sparsity while remaining competitive in accuracy, with ImageNet ResNet50 as a proof that it scales.

## Core Argument Chain
1. A node should be kept only if it transfers entropy to the next layer; MI preservation means a decoder exists that reconstructs the next layer (Theorem 1).
2. Reconstructability implies the pruned net is re-trainable (§1, §4.1).
3. Selection per layer pair, from output to input, with a confidence threshold, realises this in practice and yields per-layer ratios.
4. Because each layer keeps what the next needs, layers do not collapse (Fig. 3).
5. Baselines (adapted unstructured methods, ThiNet, SOSP-H) are compared at the pruning level MIPP picks and are worse or equal.
∴ MIPP outperforms the state of the art, trained or not (Abstract, §5).

## Strongest Counter-Argument
The evidence does not isolate MI preservation as the cause of any advantage. What is implemented is not mutual information but the comparison of a briefly re-trained MLP's loss with and without a node (Eq. 1, App. D.3.2), with capacity and iteration counts that set what counts as "information"; sparsity is determined by a confidence knob x% swept over 20 values (App. D.1), not by the information criterion. The resulting per-layer ratios are the most plausible source of any gain: §5 itself attributes better generalisation to "remaining nodes … concentrated in the early layers", and the baselines are run at MIPP's global ratio, with no minimum-width safeguard, ThiNet at uniform ratios, and unstructured methods converted by L1-normalisation (§5). In such a comparison a method that sets layer widths by a reconstruction constraint will naturally avoid layer collapse and look better, regardless of whether the criterion is "mutual information". The decisive control is absent: apply MIPP's per-layer ratios to plain magnitude (L1) or ThiNet-style pruning, or give baselines a guard against empty layers, and see whether the advantage survives. Further, Theorem 1 is an existence statement for an arbitrary function class; the pruned layer must realise the reconstruction with a single affine map and activation and then be re-trained, which Theorem 1 does not address, so "MIPP implies re-trainability" cannot be a reason for any experimental result. Finally, the headline "outperform state-of-the-art" rests on ImageNet comparison with a 2017 method (ThiNet) and on CIFAR/MNIST comparisons against methods not designed for the setting. If the authors answer by narrowing the claim to "competitive layer-collapse-resistant structured pruning of small CNNs" and by adding the control, the paper becomes defensible; as written, the causal story (MI preservation → re-trainability → better pruned nets) is not supported.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core empirical claim (competitive, collapse-resistant structured pruning of small CNNs) survives in weaker form; no test-set selection, contradiction of the main claim, fabrication or ethical issue was found (protocol sweep shared with R1: no tuning on the reported test set).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / claim distortion (E5) | §1 contribution 1; §4.1 ("more rigorous than competing techniques"); App. C | "We prove… discoverable by gradient descent… MIPP implies re-trainability": Theorem 1 shows existence only, with an unrestricted function class, for perfect MI preservation, which the practical method does not achieve; the experiments show accuracy drops after pruning | Narrow to "reconstructability", or prove a restricted-class statement and test it |
| DA-M2 | Evidence vs claim | Abstract; §5 last paragraph; Fig. 6 | "outperform state-of-the-art" and "surpass state-of-the-art performance" vs. ThiNet-only ImageNet comparison and §5's own concession ("SOSP-H does outperform MIPP at test time") | Narrow wording or add TPP/CHIP/HRank at matched FLOPs |
| DA-M3 | Alternative explanation / missing control | §5 "Models, datasets and baselines"; Figs. 3–4 | Baselines forced to MIPP's global ratio, no minimum-width guard, ThiNet uniform; advantage may come from per-layer widths | Transplant MIPP's per-layer ratios to L1/ThiNet; add min-keep guard to baselines |
| DA-M4 | Construct validity | Eq. 1, §4.2.2, App. D.3.2 | The criterion compares a 1500-iteration MLP with a 20/150-iteration re-trained MLP; "confidence" from five repeats swept to ≈ 100%; scalar-collapsed filters | Sensitivity and estimator validation; report agreement across repeats |
| DA-M5 | Statistics | Fig. 3 caption; §5 "noisy results" | Collapse rate per 5% bin with an unstated, probably small number of runs; no seeds | Report runs per bin and seed variance |
| DA-M6 | Overgeneralisation | §5 "This is because CNNs are known to generalize better…"; Contribution 3 | Uncited explanation presented as fact; "whether they are trained or not" vs §5 "slightly out-performed by both GraSP and reinitialize baselines" | Cite/test; narrow C3 |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §1 vs §4.2.1 | "Rather than ranking nodes and selecting the top-k" while nodes are sorted by MI before TERC |
| DA-m2 | Consistency | App. D.1 | x_0 = 50 with (1−x) factor; 20 values vs n ∈ [0,20] |
| DA-m3 | Citation | §2 on Liebenwein et al. | Description vs that paper's abstract (see R2-W2) |
| DA-m4 | Overclaiming | App. E.1 | "state-of-the art test accuracy" for pixel selection, based on 90%/75% scenarios against baselines not designed for pixel selection |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Appendix D.1 ladder from r = 0.5, x_0 = 50 | "20 different values" (n ∈ [0,20]) | With fractions, x_n = 1 − 2^−(n+1): 75%, 87.5%, …, x_19 ≈ 99.9999%; 21 values for n = 0..20; with x_0 = 50 the factor (1−50) is negative | No (units and count inconsistent) |
| Fraction of ImageNet ResNet50 neurons kept | "average PR of 71.1 ±0.81%" (pre-trained) | 100 − 71.1 = 28.9% kept (assuming PR = fraction removed) | Consistent, but no FLOPs/params to interpret it |
| Re-training budget relative to training | Table 2: CIFAR 200 → 120 epochs; ImageNet 90 → 75 epochs | 120/200 = 60%; 75/90 ≈ 83% | Consistent; whether baselines got the same is not stated |
| Abstract/§5 vs figure text | "surpass state-of-the-art" | §5 concedes SOSP-H better at 80–90% on ResNet34 | Partly inconsistent |

## Ignored Alternative Explanations
- Per-layer widths (not the criterion) drive the results; control: MIPP ratios applied to L1/ThiNet; random choice at MIPP widths.
- Output-to-input order and retraining-aware reconstruction, not MI, give the collapse resistance; control: ThiNet with the same order and a min-keep guard.
- Estimator capacity/iteration choices act as a hidden sparsity regulariser.
- For untrained networks, MIPP mostly prunes pixels/neurons that are constant (MNIST borders, §5), which any variance-based criterion also does.

## Missing Stakeholder Perspectives
Practitioners who deploy pruned CNNs (latency, memory, per-class accuracy shifts) and users of pruning toolkits who need the cost of the pruning step; none is addressed.

## Observations (Non-Defects)
The collapse analysis (Figs. 3, 4, 11) is a good instrument and the scope statement on untrained, complex inputs (§5) is exemplary. The method is described with enough detail (App. D.3.2) that a control experiment can be run quickly. The conclusion is modest in tone relative to the abstract.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | DA-M1, DA-M4 |
| Clarity & Presentation | 56 | Readable; overstated abstract |
| Novelty & Originality | 48 | Composition; weak differentiation from ThiNet |
| Significance & Impact | 46 | No demonstrated standard-benchmark gain |
| Experimental Validation | 40 | DA-M2, DA-M3, DA-M5 |
| Reproducibility | 46 | Details of MLP given; code, data for MI, cost missing |
| Ethical Compliance | 60 | Nothing at stake |

## Overall: 2 | Confidence: 4

Pool position: better than about 30% of ICLR submissions. Deciding evidence: central causal claim not isolated by a control; headline "state of the art" unsupported.

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Each weakness in the five reports was checked for specificity, "not already answered in the paper or appendix", consistency with the paper and with cited abstracts, and actionability. Changes made while assembling the reports:

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2-W2 | Liebenwein et al. described as one-shot / not iterative | rewritten | Only the abstract was read; stated as an abstract-vs-claim mismatch to verify, not as a fact about that paper (Hard Rule 2, Domain Step 5) |
| R4-W2 | "Algorithm 1 uses unpruned X_{l+1}, contradicting §4.4" | moved to Question | §4.4 primes are garbled in extraction, so unverifiable (Hard Rule 10) |
| R1 (draft W on missing hyperparameters) | "no hyperparameters given" | dropped | App. D.3 and Table 2 give them; replaced by the narrower W3/W4 on MI-estimation data and sensitivity |
| R3-W2 point 4 | "transfer entropy is misnamed" | rewritten | Reworded as formal analogy; the paper's own usage follows Westphal et al. (2024), and the criticism targets the work, not the authors |
| R2-W5, R4 minor | typos, bibliography slips | moved to Minor / marked [verify] | Cosmetic or recall-based |
| DA draft "baseline numbers differ from original papers" | dropped | No numbers are given in the text and figures are unavailable |

Scores were not changed. R1-W1's per-bin run-count remark is kept as a clarifying question (marked "derived conjecture").

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer package (Part A)

**Issue list and classes.**
| Merged issue | Source IDs | Class |
|--------------|-----------|-------|
| Baselines/ImageNet evidence do not support "state of the art"; no FLOPs; recent structured baselines (TPP, CHIP, HRank) missing | R1-W2, R2-W4, R4-W1/W3, DA-M2 | CONSENSUS-4 |
| Theorem 1 / "implies re-trainability" overclaimed (existence-only; GD claim unproved) | R1-ERR-1/2, R2-W3, R3-W2, DA-M1 | CONSENSUS-4 |
| Estimator validity, sensitivity, scalar collapse of filters | R1-W3, R3-W2, DA-M4 | CONSENSUS-3 |
| No seeds/variance; collapse-rate statistics; no tables | R1-W1, R4-W1, DA-M5 | CONSENSUS-3 |
| Cost of the method / deployment metrics missing | R1-W4, R3-W1 | CONSENSUS-2 |
| Novelty is a composition; ThiNet not differentiated | R2-W1, DA-M3 (partly) | CONSENSUS-2 |
| Untrained-network claim only partly supported; "re-initialized" undefined | R1-W5, DA-M6 | CONSENSUS-2 |
| Missing control: MIPP's per-layer ratios on a simple criterion; baselines lack guard | DA-M3, R1-W5 | SOLO (DA) with partial support |
| Citation/description accuracy (Liebenwein; bibliography) | R2-W2/W5, DA-m3 | CONSENSUS-2 |
| Undefined terms, figure-only results | R4-W2 | SOLO |
| Classical analogues (column subset selection); broader impact | R3-W3/W4 | SOLO |
| SPLIT | none explicit; R3/R2 rate the idea's novelty a bit higher than R1/DA | — |
| DA-CRITICAL | none raised | — |

Issues the outcome may hinge on: the ImageNet/SOTA evidence (R1-W2, DA-M2), Theorem 1 (DA-M1), the missing control (DA-M3), and variance (R1-W1). Official score computed with `scripts/aggregate_scores.py` (BEFORE run, no `eic_weight`, `da_critical` empty): official rating 2.60, official composite 49.6, starting point 3, composite band 2 (⚠ cross-check disagreement). No consistency warnings. No integrity findings.

## EIC Meta-Review (Prof. Ilse Varga-Lindqvist)

### The Case For and Against
- **For acceptance:** A clean and explainable criterion that sets per-layer ratios by itself, a well-instrumented layer-collapse analysis (Figs. 3, 4, 11) across six model/dataset pairs, honest scope statements (§5), and documented MLP settings (App. D.3.2). The weaknesses on its own (no variance, one-baseline ImageNet) are not unusual for a first version.
- **Against acceptance:** The headline claims ("outperform state-of-the-art", "implies re-trainability") are not supported by the paper's own evidence: ImageNet is compared only with ThiNet, adapted unstructured baselines are used at CIFAR scale, the theorem proves existence only, there are no tables, seeds or compute numbers, and the central causal story is not isolated by a control. Novelty is a modest composition of existing parts.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| No seeds/variance/tables; results only as plots | R1-W1, R4-W1, DA-M5 | §5, Figs. 2, 3, 6; full-text search | Verified | "despite noisy results" (§5); no "seed" or run count anywhere; Tables 1–4 are notation, hyperparameters, collapse functions, baseline characteristics |
| ImageNet compared only with ThiNet; "state of the art" in abstract | R1-W2, R2-W4, DA-M2 | Abstract; §5; Fig. 6 | Verified | Wording "due to memory limitations we only compare to ThiNet on larger datasets"; §5 last paragraph repeats the SOTA claim |
| Baselines adapted from unstructured methods; MIPP's ratio imposed on baselines; TPP/CHIP/HRank cited but not compared | R1-W2, DA-M3, R2-W3 | §1, §2, §5 | Verified | TPP, CHIP, HRank appear in references/related work and not in experiments |
| Theorem 1 gives existence only; GD-discoverability unproved | R1-ERR-1, R2-W3, DA-M1 | §1, §4.1, App. C | Verified (prose); proof algebra Partly unverifiable (garbled) | R1's "constant shift" remark is sound in principle but not checkable from the garbled equations |
| MI for deterministic continuous activations ill-defined | R1-ERR-2 | §4.4 vs §4.2.2 | Partly correct | True for exact differential MI; the paper's estimator is a loss-based proxy, which it concedes "under certain circumstances" |
| Estimator compares 1500-iteration vs 20/150-iteration MLP; no sensitivity | R1-W3, DA-M4 | §4.3; App. D.3.2 | Verified | "not to the same extent as in the first instance"; direction of bias not determinable (warm start implied but not stated) |
| No compute/time, FLOPs, latency | R1-W4, R3-W1 | full-text search | Verified | None of GPU, wall-clock, FLOPs, latency found |
| Untrained-network claim only partly supported | R1-W5, DA-M6 | §1 C3; §5 VGG11, VGG19 | Verified | "slightly out-performed by both GraSP and reinitialize baselines" |
| Liebenwein description (iterative re-training) vs that paper's abstract | R2-W2, DA-m3 | §1, §2 | Partly correct | Abstract has no mention of iterative re-training, but I cannot check the body; kept as MINOR |
| Bibliography errors (GraSP year/venue, Liebenwein venue, DCP authors) | R2-W5 | References | Plausible, unverified | Marked [verify]; cosmetic |
| Layer collapse undefined | R4-W2 | Fig. 3 caption | Verified | Only the caption "untrainable layer collapse" |
| Appendix D.1 formula units / count | R1-ERR-3, DA-m2 | App. D.1 | Verified | Recomputed: x_1 = 75%, x_19 ≈ 99.9999% as fractions; 21 vs 20 values |
| "Table 4" mis-reference | R1-ERR-4 | App. E.2 | Verified | Table 3 holds the collapse functions |
| "Rather than ranking" vs MI ordering | DA-m1, R4-W2 | §1 vs §4.2.1 | Verified | Ordering is used to sequence TERC, but nodes are ranked by MI |
| Transfer entropy is a formal analogy, no temporal structure | R3-W2 | §1, §3 | Partly correct | Interpretive; no effect on the decision |
| Control (MIPP ratios on simple criterion) absent | DA-M3 | §5 | Verified | No such experiment in main text or appendix |

Literature ledger check: the missing-comparison weaknesses (TPP, CHIP, HRank) rest on **prior (peer-reviewed or arXiv-only 6+ months)** work, so they stand as MAJOR missing baselines; no weakness rests on a recent preprint, concurrent or newer work, and none was used to lower a score. All recommended references were checked with `verify` except the polarization-regularizer paper, kept as `[verify]`. No work was found that is "known results presented as new" (no criterion-7 candidate); similarity search found no overlap. Reviewer bibliography remarks are recall-based and stay `[verify]`.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Nearly every point verified (W1, W2, W4, W5, ERR-3/4); the ERR-2 point is partly correct; scores are consistent with the text; decisive on the outcome |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly verified; the Liebenwein description rests on an abstract only (partly correct); bibliography remarks unverified |
| R3 (Perspective) | 3 | 3 | 1.0 | Sound but mostly constructive and less decisive; the transfer-entropy remark is interpretive, the rest verified |
| R4 (Generalist) | 3 | 4 | 1.0 | Presentation points verified; calibrated to the venue |
| DA | 2 | 4 | 1.0 | Arguments largely survived the check (DA-M1/M2/M3/M5 verified); no CRITICAL overreach; the alternative-explanation argument is plausible but untested, so no upweight |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so there is nothing to uphold or downgrade. Independent of the DA, I checked criterion 3: the paper reports accuracy over a sweep of 20 x-values, no single configuration chosen on test data; the one selection ("we adopted this function throughout", App. E.2) uses a comparison whose split is not stated, which is a MAJOR question about protocol, not leakage. No ceiling applies.

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| (none raised) | n/a | n/a | n/a |

### Final Decision and Justification
The EIC-weighted rating is 2.56 (official mean 2.60), giving a starting point of 3 (Borderline Reject). The composite cross-check is 49.2 (official 49.6), which is band 2 (Reject), a one-step disagreement within 1 point of the band edge (50); per the rules this is a borderline signal, not a reason to depart, and I name no verified issue that the ratings failed to account for. I therefore keep the rating-based starting point and the final decision is **3 (Borderline Reject)**. My pool position: **better than about 35% of ICLR submissions** (accepted share ≈ 27%), the typical-rejected band: a coherent, instrumented idea of modest novelty whose headline claims (state of the art; re-trainability) are unsupported by ImageNet-versus-ThiNet, adapted-baseline and existence-only theory evidence, with no variance or cost reporting. The decision sits at the low side of 3: the weaknesses concern evidence and wording, all fixable within a revision cycle, which is why it is not 2; nothing in the paper is fatal (no DA ceiling applies). The final number does not exceed any ceiling (none). Mapped to ICLR's form: Soundness 2, Presentation 2, Contribution 2, rating label "4 on {0,2,4,6,8,10}" (scale status secondary), i.e., below the accept threshold. This is a simulation of how a careful panel would likely see this draft.

---

## Score Summary

### Official Scores and EIC Assessment (output of `aggregate_scores.py --venue iclr --final 3`, with `eic_weight` values)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Methodology) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Perspective) | 3 | 0.70 | 1.00 | 16% |
| R4 (Generalist) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 42 | 52 | 52 | 50 | 44 | 48.0 | 47.6 | 10 |
| Clarity & Presentation | 55 | 58 | 60 | 56 | 56 | 57.0 | 56.8 | 5 |
| Novelty & Originality | 50 | 52 | 56 | 52 | 48 | 51.6 | 51.4 | 8 |
| Significance & Impact | 45 | 48 | 52 | 50 | 46 | 48.2 | 47.9 | 7 |
| Experimental Validation | 38 | 45 | 46 | 46 | 40 | 43.0 | 42.6 | 8 |
| Reproducibility | 40 | 50 | 48 | 46 | 46 | 46.0 | 45.6 | 10 |
| Ethical Compliance | 60 | 62 | 62 | 60 | 60 | 60.8 | 60.7 | 2 |
| **Composite** | 45.8 | 51.4 | 52.8 | 50.7 | 47.1 | **49.6 (before)** | **49.2 (after)** | |
| Pool position (P%) | 28 | 38 | 42 | 40 | 30 | | EIC: 35 | |

**Official ratings:** R1 2, R2 3, R3 3, R4 3, DA 2 → mean **2.60**. **EIC-weighted rating:** 2.56 → starting point **3**. **Composite cross-check:** 49.2 → band 2 (⚠ one-step difference, near the band edge). **DA ceiling:** none. **Final (EIC): 3.** No dimension has a spread above 20.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue-weighted composite 49.0; final Overall 3 (Borderline Reject) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Mutual Information Preserving Neural Network Pruning" to ICLR. The topic, structured pruning that avoids layer collapse and keeps a network re-trainable, is a worthwhile one.

**Overall Assessment:** The reviewers found a coherent, interpretable selection principle with a useful collapse analysis, but judged that the headline claims go beyond the evidence and that the evaluation is not yet at the standard of the sub-field. The panel's view is a borderline-reject.

**Key Strengths Identified by Reviewers:**
1. A concrete, explainable criterion that sets per-layer ratios automatically, with instrumented collapse analysis and per-layer plots (R1-S1, R2-S1, R3-S2).
2. Honest scope statements and documented MLP settings (R1-S2/S3, R3-S3, R4-S3).
3. A cross-field bridge from feature selection to pruning, with a pixel-selection spin-off (R3-S1).

**Key Concerns Requiring Attention:**
1. The "state of the art" and ImageNet claims rest on a single 2017 baseline and on converted unstructured baselines; recent structured methods that you cite (TPP, CHIP, HRank) are not compared, and no FLOPs are reported (CONSENSUS-4).
2. Theorem 1 shows existence of a reconstruction function for perfect MI preservation, not "re-trainability", and not for the practical estimator (CONSENSUS-4).
3. No seeds, variance, tables, run counts for the collapse analysis or pruning cost; the estimator is unvalidated (CONSENSUS-3).
4. The advantage may come from per-layer widths rather than MI; a transplant control is missing (DA).

**Decision: Borderline Reject (3)**

The overall merit is real but the claims are ahead of the evidence. A revision that narrows the claims, adds a matched-FLOPs ImageNet comparison with recent structured baselines under one recipe, reports variance and cost, and includes the per-layer-ratio control would put the paper in the accept-leaning range for the panel. Please refer to the Revision Roadmap below for prioritised guidance.

Sincerely,
Prof. Ilse Varga-Lindqvist
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Evidence does not support "state of the art"; recent structured baselines/FLOPs missing | R1, R2, R4, DA | CONSENSUS-4 |
| Theorem 1 overclaimed as re-trainability | R1, R2, R3, DA | CONSENSUS-4 |
| Estimator validity/sensitivity; scalar collapse | R1, R3, DA | CONSENSUS-3 |
| No variance/seeds; figure-only results | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Strength of the novelty | R3 (fresh cross-field transfer, 56) | R1, DA (composition, ≤ 50) | Composition of existing parts with real but modest delta over ThiNet; I side with the 50–52 range |
| Overall verdict 2 vs 3 | R1, DA (2) | R2, R3, R4 (3) | Weighted rating 2.56 → 3; the issues are fixable and no ceiling applies |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. The largest spreads (10) are Technical Rigor (R1 42 versus R2/R3 52) and Reproducibility (R1 40 versus R2 50); R1's view that the estimator and theory are weaker is better supported, so R1 carries a higher weight.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Theorem 1 does not give re-trainability | Yes (R1, R2, R3) | n/a | n/a |
| DA-M2 | MAJOR | SOTA claim vs ThiNet-only ImageNet | Yes (R1, R2, R4) | n/a | n/a |
| DA-M3 | MAJOR | Missing control for per-layer widths | Partly (R1) | n/a | n/a |
| DA-M4 | MAJOR | Estimator validity | Yes (R1, R3) | n/a | n/a |
| DA-M5 | MAJOR | Collapse-rate statistics | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR | Uncited explanation; C3 narrowing | Yes (R1, R4) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No upheld DA-CRITICAL issue. The following are verified issues that undermine a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | "State of the art"/ImageNet claim unsupported; recent structured baselines and FLOPs missing | R1-W2, R2-W4, R4-W1, DA-M2 | Abstract; §5; Fig. 6 | Matched-FLOPs ResNet50/ImageNet comparison with TPP, CHIP/HRank and one recent method under one recipe; table with FLOPs and top-1; otherwise narrow the claim to small CNN classifiers | High; ≈ 300–600 GPU-h (partly via published checkpoints) | Partly (narrowing: yes; new runs: partly) |
| R2 | "MIPP implies re-trainability" not established | R1-ERR-1/2, R2-W3, DA-M1 | §1; §4.1; App. C | Restate as reconstructability, or prove a restricted-class result and test the link; fix proof notation | Medium; < 20 GPU-h for a test | Yes |
| R3 | No seeds, variance, tables, runs per bin | R1-W1, R4-W1, DA-M5 | Figs. 2, 3, 6 | Mean ± std over ≥ 3 seeds on CIFAR; exact-numbers table; runs per bin in Fig. 3 | Medium–High; ≈ 200–300 GPU-h | Partly |
| R4 | Causal attribution: per-layer widths vs MI | DA-M3, R1-W5 | §5; Figs. 3–4 | Transplant MIPP ratios to L1/ThiNet; add min-keep guard to baselines; random-node control at MIPP widths | Low–Medium; < 50 GPU-h | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Estimator sensitivity (MLP size, iterations, repeats, x% semantics) and scalar collapse of filters | R1-W3, R3-W2, DA-M4 | Ablations; agreement across repeats; synthetic validation | Low (< 20 GPU-h) | Yes |
| S2 | Cost of pruning and deployment metrics (wall-clock, latency) | R1-W4, R3-W1 | Report per-method pruning time, latency on a stated device | Low–Medium | Yes |
| S3 | Untrained-network claim and "re-initialized" baseline | R1-W5, DA-M6 | Define baseline; add train-from-scratch control; narrow C3 | Low | Yes |
| S4 | Novelty differentiation from ThiNet / Ding et al. | R2-W1, DA-M3 | Method-comparison table and ablation with ThiNet-style decoder | Low | Yes |
| S5 | Related work: Dai et al. 2018, DepGraph, LAMP, Frankle et al. 2021, Liu et al. 2019; Liebenwein description | R2-W2 | Add and differentiate; correct the description against that paper | Low | Yes |
| S6 | Define layer collapse; unify "sparsity" vs "neuron reduction"; move filter-collapse description into the main text; code for review | R4-W2, R1-W4 | Add definitions; anonymized code | Low | Yes |
| S7 | Protocol statements: data for MI estimation; data/split for Fig. 10 | R1-W4 | State them | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Uncited explanation about early-layer nodes (§5) | R4-W4, DA-M6 | Cite or phrase as hypothesis |
| N2 | App. D.1 formula units, "20 vs 21 values"; "Table 4" mis-reference; typos | R1-ERR-3/4, R4 | Fix |
| N3 | Bibliography entries (GraSP year/venue, Liebenwein venue, DCP authors) [verify] | R2-W5 | Check |
| N4 | Column-subset-selection baseline; per-class accuracy shifts; impact paragraph | R3-W3/W4 | Add if space |
| N5 | Extension to ViT/LLM pruning | R3, R4-W3 | Future work or a small experiment |
| N6 | "Rather than ranking" wording; "state-of-the art" on pixel selection (E.1) | DA-m1, DA-m4 | Reword |

## Estimated Revision Effort
- Priority 1: 4 items, about 3–5 weeks including ImageNet runs (≈ 500–1000 GPU-hours total).
- Priority 2: 7 items, about 1–2 weeks (mostly small ablations and writing).
- Priority 3: 6 items, a few days.
- **Total estimated revision time**: about 5–8 weeks; the claim-narrowing and writing items (R2, S3–S7) are rebuttal-feasible, the ImageNet comparison only partly.

*Not run: Gap Scout (post-review analysis, off by default and not requested).*
