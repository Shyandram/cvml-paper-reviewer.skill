# Simulated Peer Review: "Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus"

*Simulation of how a careful ICLR panel would likely see this draft. It is not a prediction of the real outcome. Date: 2026-11-10. Mode: full. Literature check: strict, cutoff 2025-09-24. Figures were not available, so figure-dependent statements rest on captions and on numbers printed in the extracted text. The five reviewer passes were run one after another in a single model context (not independent agents), as the skill allows. The Gap Scout was not requested and was not run.*

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus |
| Primary Discipline | Quantum machine learning → quantum federated learning (variational circuits) |
| Secondary Discipline(s) | Federated learning with heterogeneous models; NISQ hardware and circuit design |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Parameterized quantum circuits with data re-uploading; layerwise cross-entropy plus KL "reverse distillation" loss (from DepthFL); circular-mean parameter aggregation; ancilla / mid-circuit / funnel designs for intermediate readout |
| Target Venue | ICLR (stated by the user; 2026 cycle; accepted share ≈ 27%); profile key `iclr` |
| Venue-Specific Notes | none; ICLR form: Soundness / Presentation / Contribution (1–4), Rating, Confidence. Scale status: secondary |
| Paper Maturity | Submission-ready (full paper with appendix; no limitations section) |
| Ethics-Relevant Content | none (public image benchmarks, no human data). No limitations discussion found |

### Claimed Contributions (as stated by the authors)
1. **C1** (§1, bullet 1; Abstract): "The first structured quantum federated learning framework (Quorus) that utilizes layerwise losses and reverse distillation."
2. **C2** (§1, bullet 2; §4.3; Table 1): quantum model designs (Layerwise, Ancilla/Blocking, Funnel) giving an ensemble of classifiers "from a single shot of a quantum circuit".
3. **C3** (Abstract; §1, bullet 3; §5; Table 2): testing accuracy gain of 12.4% over Q-HeteroFL, "while being shot-efficient".
4. **C4** (§1, bullet 4; §6; Figures 7–8): higher gradient norms ("reducing barren plateau effect") and accuracy "within 3% of ideal simulation" on IBM QPUs.
5. Code and dataset open-sourced (link removed in the blinded copy; not checkable).

### Paper memory (shared factual record, built before Phase 1)
- **Setup (location):** K = 5 clients, one per depth 2L–6L (Table 4); 128 datapoints per client (§5, Table 4); IID (Table 4); test set "3000; 100 for hardware runs only" (Table 4); 10 qubits, 30 parameters per layer, angle embedding of 10 PCA features (Table 4, App. C); T = 1000, E = 1, batch 32, Adam lr 0.001, init N(0,1) (Table 4); training "For training, none (analytic)", hardware 1000 shots (Table 4). Five runs = five data allocations, with the same test data and initial parameters across runs (App. C). Seeds: not stated after search. **No validation split is stated after search** (terms `validation`, `val set`, `held-out`, `tuned`, `checkpoint`, `we select` returned nothing). Ansatz, design and layer count were chosen on testing accuracy (§4.2 "performs the best"; Table 3 caption; App. D.1; App. D.2).
- **Headline numbers:** 12.4% (Abstract, §1, §5, §7; source Table 2); "within 3%" (§1; source Fig. 8(a): 76% vs ideal 79%); 48% on IBM Brisbane (Fig. 8(a)).
- **Appendix adds:** Prop. 1 equivalence proof Ancilla ≡ Blocking (App. B); hyperparameters (Table 4); federated PCA emulated centrally (App. C); Q-HeteroFL definition (Alg. 2, App. C.1); QPU error table (Table 5); ansatz sweep (Table 6); layer-count ablation (Table 7); hardware ensemble note (Fig. 10, App. D.3).
- **Unverifiable:** all figures as images (Figs. 1–10); Algorithm 1 and 2 typesetting and Table 7 row layout are partly garbled in extraction.

### Integrity scan
`scripts/integrity_scan.py` found no reviewer-directed text and no hidden characters. Nothing was reported to the EIC and nothing was redacted. No text addressed to reviewers or AI systems was seen while reading. Author identity was not visible (blinded copy).

### Literature check status
Mode strict, cutoff 2025-09-24. The arXiv API was intermittently rate-limited (HTTP 429 / 503). Four claim queries succeeded (C1 ×2, C2, C4), covering 29 kept results. C3 got no query. `benchmarks` recognised no external benchmark, so no baseline scout was run. `coverage` reports gaps: no 2025 prior work, no C3 query, no baseline query. `similarity` flagged no text overlap (0 shared 8-grams for all candidates). Its top "closest prior work" entries were a software framework paper (cosine 0.315, not the same task) and *Layerwise learning for quantum neural networks* (0.277).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Marisol Quenneville, ML area-chair profile, large public research university (North America)
- **Seniority / Expertise**: Senior faculty / optimization, federated learning, learning theory
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Calibrates against what the venue actually accepts; weights verified claims over harsh or generous tone.

### Reviewer 1 (Methodology): Lucia Ferreyra-Okafor, quantum ML systems lab, public research university (South America)
- **Seniority / Expertise**: Mid-career / variational-circuit training, NISQ evaluation protocols, federated optimization
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; insists on matched inference protocols and held-out selection.

### Reviewer 2 (Domain): Henrik Daalmans, quantum information group, European technical university
- **Seniority / Expertise**: Senior faculty / quantum federated learning, barren plateaus, ansatz design
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks each novelty claim against the cited abstracts.

### Reviewer 3 (Perspective): Priya Subramaniam-Lund, edge and distributed systems, industrial research lab (South Asia)
- **Seniority / Expertise**: Senior industry scientist / resource-aware federated systems, cloud scheduling, cost models
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; reads the paper as a systems practitioner and looks for what it could become.

### Reviewer 4 (Generalist): Tomasz Weiland-Abara, machine learning group, mid-sized university (Central Europe)
- **Seniority / Expertise**: Mid-career / representation learning and deep learning (not quantum)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical programme-committee member; asks whether a non-specialist can follow and whether the claim matches the evidence.

### Devil's Advocate: Samira Oduya-Lindqvist, evaluation methodology and causal inference, independent research institute (Europe)
- **Seniority / Expertise**: Senior researcher / experimental design, ablation logic, evaluation validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; states the strongest version first, then attacks it.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

*Reviewers read the redacted reviewer copy (identical to the paper, since the scan was clean) and the paper memory. No reviewer saw another report.*

---

# Peer Review Report

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Reviewer: Lucia Ferreyra-Okafor, Methodology Reviewer (quantum ML systems lab, public research university; fictional persona)
## Expertise: variational-circuit training; NISQ evaluation protocols; federated optimization
## Date: 2026-11-10

---

## Summary
The paper studies federated training of parameterized quantum circuits when clients can only run circuits of different depths (2 to 6 layers, one client per depth). Quorus applies a DepthFL-style layerwise loss (cross-entropy per layer plus pairwise KL terms) with circular-mean aggregation of shared rotation angles. It proposes three circuit designs (Layerwise, Ancilla/Blocking, Funnel) for reading out a classifier after every layer. On six binary MNIST / Fashion-MNIST tasks, simulated with analytic gradients, it reports an average gain of 12.4 points over a quantum adaptation of HeteroFL, higher early-layer gradient norms, and a single-model hardware test on six IBM QPUs.

---

## Strengths

### S1: Clear, well-posed problem and transparent setup
Depth-heterogeneous clients are a coherent formulation (§1, Fig. 1). Table 4 lists hyperparameters, client count, data per client, optimizer and rounds. App. C also states how the baselines are made deliberately favourable to Standalone (persistent Adam state, federated PCA for all).

### S2: Five data allocations with mean ± std everywhere
All of Tables 2, 3, 6 and 7 report mean ± std over five runs. This is above the minimum expected for small-scale experiments. The std of several cells (e.g. 33.5 for Q-HeteroFL at 2L, Trouser/Boot, Table 2) is informative.

### S3: Useful internal ablations
Table 6 (ansatz), Table 7 (layer count) and Table 3 (design variants) give the reader some view of sensitivity. The Ancilla ≡ Blocking proof (App. B, Prop. 1) is correct as written for one layer.

### S4: Honest reporting of a negative cell
§5 acknowledges "Notably, for clients of the smallest capacity" Quorus is not best.

---

## Weaknesses

### W1: The comparison that carries the headline is against a baseline built by the authors, and the strongest comparisons show no gain
Q-HeteroFL is "our quantum version of a classical technique called HeteroFL" with "The loss function is defined solely on" the deepest classifier (App. C.1). It is not state of the art (Abstract). It is the weakest design among the plausible baselines, and its 2L-client accuracy collapses (58.8 ± 12.6 on MNIST 3/4; 62.4 ± 33.5 on Trouser/Boot). Recomputing Table 2 over all 30 cells (5 capacities × 6 tasks): mean Quorus − Q-HeteroFL = +12.37 points (the paper's 12.4), but mean Quorus − Standalone = **+0.24** and mean Quorus − Vanilla QFL = **+0.43** points, with per-cell stds of 0.2–8.1. Standalone beats Quorus on Bag/Sandal at every capacity (e.g. 95.3 vs 92.7 at 6L). The table caption's "consistently outperforms the baselines across client capacities" is therefore not supported.
- **Suggested Fix:** Narrow the claim to "improves over a HeteroFL-style quantum baseline". Add stronger baselines: a per-client layerwise-loss model without aggregation (isolates what federation adds), and a heterogeneous-depth FedAvg with per-depth heads. Cost: ≈ 2 baselines × 6 tasks × 5 runs × 5 clients on a 10-qubit statevector simulator, roughly under 50 CPU-hours.

### W2: Three factors are confounded in the Quorus rows: loss, KL term and test-time ensembling
App. D.1 says "That is what is shown in Table 6 and is how Quorus is evaluated" and that a client "can ensemble the outputs of" its intermediate classifiers. Whether Q-HeteroFL, Vanilla QFL and Standalone are scored with a single final classifier is not stated. Eq. 1 is "the same loss function as in DepthFL", yet there is no ablation of the CE-only layerwise loss versus the KL "reverse distillation" term. Fig. 10 / App. D.3 suggests ensembling alone raises accuracy. The attribution of the gain to the layerwise loss (C1) is therefore untested.
- **Suggested Fix:** Report Quorus-Layerwise with (a) last-classifier-only readout, (b) CE-only layerwise loss, (c) CE+KL, and give baselines the same ensemble where defined. Cost: ≈ 3 variants × 6 tasks × 5 runs.

### W3: Model selection was done on the test accuracy; no validation split exists
The V-shape ansatz is chosen because it has the highest testing accuracy most often (App. D.1: "accuracy the most times, so we use it for all of our experiments"; Table 6). Layerwise and Funnel are chosen because they "have the highest testing accuracy (we use them for subsequent experiments)" (Table 3 caption). Layer count is justified on test accuracy (App. D.2, Table 7). Table 4 lists a 3000-point "Testing set" and no validation set. The V-shape rows of Table 6 are identical to the Quorus rows of Table 2 (e.g. 97.0 ± 1.4, 78.2 ± 0.6 at 2L). The baselines use the same V-shape ansatz, and their learning rate and rounds are fixed without tuning. The 12.4-point comparison with Q-HeteroFL survives the alternative ansatzes (Staircase beats Q-HeteroFL in 30/30 cells and Alternating in 29/30, Table 6 vs Table 2), so I treat this as MAJOR, not fatal.
- **Suggested Fix:** Carve a validation split from the 128 points per client, or from a held-out pool, make all selections on it, and report the untouched test set once.

### W4: Efficiency, hardware and gradient claims go beyond the evidence
(i) "Shot-efficient" (Abstract, §1, §5 "the Quorus-Funnel model is also shot-efficient") is not measured: training is "For training, none (analytic)" (Table 4) and Table 1 is a qualitative check-mark table. (ii) "within 3% of ideal simulation on IBM superconducting QPUs" (§1) is true for one of six devices: Torino 76% vs ideal 79%, while Brisbane gets 48% (§6). It is a single Funnel model, evaluated only on "100 datapoints" (§6A), where the binomial standard error at 76% is about 4.3 points, so 3 points is within noise. No baseline is run on hardware, so nothing shows Quorus helps there. (iii) §4.3 says "we hypothesize, and confirm on IBM hardware (Sec. 5)" that the Ancilla design trains effectively; §6 uses only Funnel for hardware, and nothing is trained on hardware. (iv) Higher early-layer gradient norms (Fig. 7) follow by construction from adding losses attached to shallow prefixes. They are not evidence of "improved and scalable trainability for deep quantum circuits" (§6), when accuracy saturates by 6 layers (Table 7) and the loss scale is not normalized.
- **Suggested Fix:** Either measure (finite-shot training with shots-to-accuracy curves; noise-model simulation using the calibration data of Table 5; hardware evaluation of baselines on ≥ 1000 test points with several models), or drop the corresponding claims.

### W5: Statistical protocol understates variance and leaves provenance unclear
The five runs share "the same training data split between clients" and, per App. C, the same testing data and initial parameters, so std reflects data allocation only, not initialization or optimizer noise. Seeds are not stated. No paired test or CI is given for margins smaller than the std (most Quorus-vs-Standalone cells). Table 4 gives a test size of 3000, which is larger than the 2,000–2,100 images that the official test splits hold for these binary class pairs (my recollection of MNIST/Fashion-MNIST class counts; please confirm), so the origin of the test points is unclear.
- **Suggested Fix:** Vary initialization seeds, report paired-bootstrap CIs for Quorus − each baseline, and state the source of the test set and its disjointness from the 640 training points.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5 | Table 2 caption | "Quorus-Layerwise consistently outperforms the baselines across client capacities" | Standalone/Vanilla beat Quorus on Bag/Sandal at all 5 capacities and on 5 of 6 tasks at 2L; mean margin vs Standalone is +0.24 | Recomputed from Table 2 (30 cells) | High | MAJOR | Narrow the claim |
| ERR-2 | E1/E5 | §1 bullet 3 vs Abstract, §5 | "improves testing accuracy by up to 12.4% over Q-HeteroFL" | 12.4 is the mean difference (371.1/30 = 12.37); the maximum is 36.4 (2L Trouser/Boot, 98.8 vs 62.4) | Recomputed | High | MINOR | Say "on average" |
| ERR-3 | E4 | App. D.1, Table 3 caption, App. D.2 | "accuracy the most times, so we use it for all of our experiments" | Design, ansatz and depth chosen on test accuracy; no validation split stated | Protocol sweep (no `validation`/`val set`); Table 6 V-shape rows = Table 2 rows | High | MAJOR | Held-out selection |
| ERR-4 | E5/E6 | §4.3 vs §6 | "we hypothesize, and confirm on" | Only Funnel is run on hardware (§6 "we perform our hardware analysis using the Quorus-Funnel design"); "Sec. 5" has no hardware run | Cross-referenced | High | MAJOR | Remove the claim or run Ancilla on hardware |
| ERR-5 | E5 | §1 bullet 4 | "within 3% of ideal simulation on IBM superconducting QPUs" | 1 of 6 devices (Torino 76% vs 79%); others 48–74% (Fig. 8(a), per extracted labels); n = 100 | Cross-referenced §6, Fig. 8(a) | High | MAJOR | Report all devices and CIs |
| ERR-6 | E5 | §5, Table 1 | "the Quorus-Funnel model is also shot-efficient" | No shot-count or finite-shot experiment; training is analytic | Table 4 "For training, none (analytic)" | High | MAJOR | Measure or drop |
| ERR-7 | E6 | App. D.1 vs Eq. 1, Table 7 | "L − 1 different classifiers (one classifier per layer" | Eq. 1 sums over d_k classifiers; Table 7 reports a 1L model, which would have 0 classifiers under L − 1 | Cross-referenced | Medium | MINOR | Define classifier count and "layer" precisely |

---

## Claim-to-Evidence Map (key claims)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | First layerwise-loss + reverse-distillation QFL framework | §1, Eq. 1, Alg. 1 | Loss is DepthFL's ("We use the same loss function as"); no ablation | Partially (the transfer works; attribution untested) |
| C2 | Single-shot ensemble from one circuit | §4.3, Tables 1, 3 | Table 3 shows accuracy parity across designs; no shot accounting | Partially |
| C3 | +12.4% over state of the art | Abstract, Table 2 | +12.37 vs self-built Q-HeteroFL; +0.24 vs Standalone | Partially (narrower claim supported) |
| C4 | Reduced barren plateau; within 3% on QPUs | §6, Figs. 7–8 | Gradient norms by construction; one of six QPUs, 100 points | Partially / Unsupported as worded |

## Fairness-of-comparison and reproducibility notes
- Federated PCA is emulated centrally ("we emulate Federated PCA"), and the Standalone baseline gets the pooled PCA (App. C): this favours Standalone, so Quorus's margin there is conservative.
- Baseline hyperparameters (lr 0.001, 1000 rounds) are shared without tuning; no tuning effort is reported for any method.
- Reproducibility is good for simulation (Table 4 complete; code promised/open-sourced, unverifiable here). Missing: seeds, transpilation settings and QPU calibration dates for hardware runs, simulation compute.

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound circuits, but the headline rests on a weak baseline, a test-selected configuration and confounded inference |
| Clarity | 3 | Readable; Eq. 1 / classifier-count ambiguity |
| Significance | 2 | Toy scale; no federation gain over Standalone |
| Originality | 2 | Loss is borrowed; circuit designs are the new part |

## Dimension Scores (0–100)

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline gain is against an author-built baseline, and the federated method is indistinguishable from Standalone (+0.24 points) in the same table, which is a typical-rejected-submission signature.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Sound circuits and proof, but test-set selection and confounded loss/ensemble |
| Clarity & Presentation | 62 | Competent | Understandable; headline wording inconsistent |
| Novelty & Originality | 50 | Developing | Loss and algorithm come from DepthFL; designs are the new part |
| Significance & Impact | 46 | Developing | Benefit of the method over trivial alternatives is not shown |
| Experimental Validation | 40 | Developing | Weak baseline, no ablation of its components, 100-point hardware test |
| Reproducibility | 62 | Competent | Full hyperparameters and code; seeds and hardware details missing |
| Ethical Compliance | 56 | Competent | Nothing at stake, but no limitations discussion found |

---

## Questions for Authors
1. Do Q-HeteroFL, Vanilla QFL and Standalone use a single final classifier at test time while Quorus ensembles L − 1 classifiers? Raising or lowering my score depends on a Quorus-without-ensemble row.
2. What does CE-only layerwise training (no KL term) give in Table 2? If it matches Quorus, C1's "reverse distillation" is not the cause.
3. Where do the 3000 test points come from, and how are they kept disjoint from the PCA fit and the training points?
4. In Fig. 8, Kingston at depth 5 reads about 68% in panel (a) but about 58% in panel (b) (read from extracted figure labels; low confidence, figure not available). Are these different runs or calibrations?
5. How many initialization seeds underlie each cell? A paired CI of Quorus − Standalone would settle whether federation helps.

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. No limitations discussion was found (IID data, 5 clients, 10 PCA features, binary tasks, analytic training, one hardware model). Adding one would be rewarded.

## Ethics Review Flag
**No**: public benchmark data; no human subjects.

## Overall Score
**3**: Borderline Reject. A coherent idea with careful hyperparameter reporting, but the main empirical claim is relative to a weak self-built baseline, test-selected configurations, and untested efficiency/hardware claims.

## Confidence
**4**: Recomputed Table 2 in full; hardware figures were read from captions and extracted labels only.

---

# Peer Review Report

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Reviewer: Henrik Daalmans, Domain Reviewer (quantum information group, European technical university; fictional persona)
## Expertise: quantum federated learning; barren plateaus; ansatz design
## Date: 2026-11-10

---

## Summary
The paper argues that existing QFL ignores device heterogeneity and introduces Quorus for clients whose circuits have different depths. It transplants the DepthFL layerwise objective to PQCs and contributes quantum-specific ways to read out intermediate classifiers (copying the state, ancilla/mid-circuit measurement, or a funnel that drops qubits). It reports gains over a quantum HeteroFL baseline, larger early-layer gradient norms and an IBM hardware study.

---

## Strengths

### S1: A real gap at the intersection of two literatures
Depth-limited clients are a natural consequence of heterogeneous NISQ devices (§1). The paper correctly sees that classical depth-wise FL (§3: DepthFL, ScaleFL, FEDepth) presupposes cheap intermediate classifiers, which quantum measurement collapse breaks (§4.3, Fig. 3).

### S2: The quantum-specific contribution is the circuit-design part
The Layerwise / Ancilla / Blocking / Funnel family (§4.3, Figs. 4–6, Table 1) with the Ancilla ≡ Blocking proof (App. B) is where the paper adds something a classical DepthFL port would not provide.

### S3: Fair description of why eSQFL does not transfer
The paper explains that eSQFL's layerwise inner products need "computing inner products requires long-distance connectivity" (§3), and positions its designs against hardware connectivity (§4.2).

---

## Weaknesses

### W1: Contribution C1 is largely DepthFL transplanted; "first-of-its-kind" is overstated
The loss in Eq. 1 is taken whole: "We use the same loss function as" DepthFL, and "so we do not repeat the discussion for the quantum case" (§4.1). Alg. 1 also cites Kim et al. (2023). With the analytic simulator used for all training, Quorus-Layerwise is DepthFL with a PQC classifier. The paper itself calls DepthFL "most closely related to Quorus" (§3). What is new is how to read out intermediate classifiers (C2), and that part is not compared to prior ensemble/early-readout ideas for noisy quantum classifiers (see Missing References). "Quorus is the first-of-its-kind work" (§1) should be reduced to "first quantum adaptation of DepthFL-style training, plus new readout circuits".
- **Suggested Fix:** State precisely what is taken from DepthFL and what is new; reorder the contributions to lead with the circuit designs.

### W2: The related-work framing contradicts the paper's own citations
§1 says "existing QFL techniques do not consider the heterogeneity of quantum devices". Yet the paper cites SpoQFL (Rahman et al., 2025) and NAC-QFL (Sahu & Gupta, 2024) for noise-affected QFL, and SpoQFL's abstract states that devices "experience heterogeneous noise levels due to variances in hardware quality" and proposes a QFL framework against it. The accurate claim is that depth heterogeneity is not addressed; noise heterogeneity is. These works are not compared empirically, and §3 spends two sentences on all QFL (Chen & Yoo 2021; eSQFL). Non-IID and heterogeneous-client QFL literature is not discussed.
- **Suggested Fix:** Rewrite §1/§3 around "depth heterogeneity", and compare with at least one noise-aware QFL method (SpoQFL is a recent preprint, so a discussion rather than a required comparison under the venue's concurrent-work norm).

### W3: The gradient-norm result is an instance of a known effect that the paper cites but does not use
Cerezo et al. (2021), cited in §1, shows that cost functions defined on shallow prefixes avoid barren plateaus while global ones do not. Attaching losses to early layers (Eq. 1) therefore raises their gradient norms by design (Fig. 7 caption: "our modified loss function has larger gradient norms throughout"). Layerwise learning for QNNs (Skolik et al., 2021) also targets this. The paper acknowledges that later-layer gradients "remain small" (§6). The sentence "improved and scalable trainability for deep quantum circuits" (§6) needs depth beyond 6 layers where plateaus appear, plus normalized comparisons.
- **Suggested Fix:** Frame the effect as an application of local-cost results, cite layerwise learning, and test at depths where barren plateaus matter (Table 7 shows saturation by 6–10 layers, so the current regime does not).

### W4: Baseline and "state-of-the-art" language
Q-HeteroFL is the authors' own construction ("our quantum version of", §5), so "over the state-of-the-art" (Abstract) refers to a method that did not exist before this paper. The paper says HeteroFL "has not yet been proposed in QFL" (App. C.1), which is a reason to call it a baseline, not the state of the art.
- **Suggested Fix:** Replace "state-of-the-art" with "a HeteroFL-style quantum baseline" throughout.

### Citation check (E7)
- DepthFL, HeteroFL and ScaleFL are described consistently with their roles in the text; I cannot check abstracts beyond what the paper states (Hard Rule 2).
- The claim that inner-product layerwise losses are "not applicable to run on real hardware" cites Sá et al. (2023), whose title concerns a BCS-Hamiltonian gap calculation. Whether it supports the statement is unclear (question, low confidence).
- "FEDepth … Zhang et al., 2025" corresponds to an arXiv entry first posted in 2023 (kept literature result); the year is a minor citation slip. FedAvg is cited as "McMahan et al., 2023" (arXiv revision year).
- §3 first sentence ("The problem of depth-heterogeneous quantum federated learning, where clients have classical models") conflates classical and quantum settings; presumably "classical federated learning" was meant.

### Literature-check addendum (strict mode, cutoff 2025-09-24)
Four successful claim queries (C1 ×2, C2, C4); 29 kept results; C3 not queried; no baseline scout (MNIST / Fashion-MNIST not external benchmarks per `benchmarks`); coverage gaps open: no 2025 prior work found, no C3 query. API rate limits (429/503) restricted the search.

**Per-claim novelty (claim profile, `related_search.py novelty`):**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|-----------------------------------------------|-----------|
| C1 | method | medium | Memory-adaptive Depth-wise Heterogeneous FL (3; https://arxiv.org/abs/2303.04887v3; prior, peer-reviewed; cited) | Loss/algorithm from the classical, cited DepthFL; the quantum transfer is non-trivial but the objective is not new |
| C2 | method | medium | QUILT (3; https://arxiv.org/abs/2309.15056v1; prior, peer-reviewed; not cited); ensemble error mitigation for shallow-circuit classifiers (3; https://arxiv.org/abs/2301.12707v2; arXiv-only prior; not cited) | Ensembles of quantum classifiers for noisy hardware exist; the single-circuit readout from intermediate layers is the new part |
| C3 | result | no close prior work found (at most medium) | none | Result against the authors' own baseline |
| C4 | result | medium | Layerwise learning for QNNs (3; https://arxiv.org/abs/2006.14904v1; prior, peer-reviewed; not cited) | Layerwise/local-cost trainability is known |

Script reading: "no central claim fully covered by prior work". One claim-level finding (C1) is MAJOR at most, and the closest whole-paper attribution is the depth-wise FL paper above.

**Novelty delta (closest prior works):**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|--------------------------|
| C1 | DepthFL (classical, cited); FeDepth (cited) | Layerwise CE + KL for depth-heterogeneous clients | PQC classifiers, circular aggregation | Yes, differentiated by the measurement-collapse argument |
| C2 | QUILT; Li et al. ensemble error mitigation | Ensembles of diverse quantum classifiers to reduce hardware error | Obtaining all layer classifiers from one circuit run | No |
| C4 | Skolik et al. | Layerwise training to ease quantum training landscapes | Layerwise losses inside FL | No |

**Field snapshot.** Before the cutoff, QFL is dominated by FedAvg-style training of identical small PQCs (Chen & Yoo 2021). 2022–2025 work adds non-IID handling (e.g. one-shot-communication QFL), noise heterogeneity (SpoQFL, NAC-QFL), communication efficiency and adversarial robustness (RobQFL, concurrent). Evaluations are almost always small simulations on MNIST/Fashion-MNIST/Iris with few qubits and few clients, and real-hardware validation is rare. A small accuracy gain over a plain QFL baseline is the norm and counts as incremental. A significant contribution would show benefit under non-IID data and realistic noise, with quantified shot or communication cost, ideally including training on hardware. This snapshot calibrated my Significance score (50) and Novelty score (52).

## Missing References
*Verified with `related_search.py verify` where marked; no `Critical` entries, since in strict mode only peer-reviewed or old arXiv work can be required and none is a direct competitor on depth-heterogeneous QFL.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | A. Skolik, J. R. McClean, M. Mohseni, P. van der Smagt, M. Leib. "Layerwise learning for quantum neural networks." Quantum Machine Intelligence 3(5), 2021. https://arxiv.org/abs/2006.14904v1 (verified) | Closest prior work on layerwise training of PQCs for trainability; frames C4 |
| Important | D. Silver, T. Patel, D. Tiwari. "QUILT: Effective Multi-Class Classification on Quantum Computers Using an Ensemble of Diverse Quantum Classifiers." AAAI 2022. https://arxiv.org/abs/2309.15056v1 (verified) | Ensemble of quantum classifiers on noisy hardware; positions C2 |
| Important | Q. Li, Y. Huang, X. Hou, Y. Li, X. Wang, A. Bayat. "Ensemble-learning error mitigation for variational quantum shallow-circuit classifiers." arXiv 2023. https://arxiv.org/abs/2301.12707v2 (verified, arXiv-only) | Ensembles as hardware-error mitigation |
| Helpful | H. Zhao. "Non-IID quantum federated learning with one-shot communication complexity." Quantum Machine Intelligence, 2023. https://arxiv.org/abs/2209.00768v2 (verified) | Heterogeneity in QFL beyond noise; for related work |
| Helpful | J. R. McClean, S. Boixo, V. N. Smelyanskiy, R. Babbush, H. Neven. "Barren plateaus in quantum neural network training landscapes." Nature Communications, 2018. https://arxiv.org/abs/1803.11173v1 (verified) | The original barren-plateau reference; the paper cites only later work |
| Helpful | M. Chehimi, W. Saad. "Quantum Federated Learning with Decentralized Data." ICASSP 2022. [verify] (not found on arXiv by title) | Early QFL on decentralized data |

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation does not isolate what is new |
| Clarity | 3 | Clear problem framing |
| Significance | 2 | Narrow and small-scale |
| Originality | 2 | Loss borrowed; readout circuits new |

## Dimension Scores (0–100)

**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a genuine new question and non-trivial circuit designs, but the main objective is borrowed and the evidence that the whole is better than simple alternatives is thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Circuit reasoning and proof are sound; evaluation confounds |
| Clarity & Presentation | 62 | Competent | Clear problem, imprecise related-work framing |
| Novelty & Originality | 52 | Developing | Medium for C1/C2/C4 per claim profile |
| Significance & Impact | 50 | Developing | Small-scale; incremental by the field snapshot |
| Experimental Validation | 48 | Developing | Weak baseline, small tasks |
| Reproducibility | 62 | Competent | Code and Table 4; hardware details missing |
| Ethical Compliance | 58 | Competent | No limitations section found |

## Questions for Authors
1. Besides the loss, what in Quorus is not available in DepthFL when the simulator is analytic? A sentence in §4.1 would change my Novelty score.
2. Why is SpoQFL/NAC-QFL not an empirical baseline, given that §1 motivates the work by device heterogeneity?
3. How do QUILT-style ensembles compare with the single-circuit readout on hardware?
4. Does Sá et al. (2023) support the connectivity statement on inner-product losses?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No (none discussed).

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A real gap and non-trivial circuit designs, but the contribution is narrower than claimed and the literature framing needs correction.

## Confidence
**3**: Familiar with the QFL and barren-plateau literature. The search was limited by API rate limits.

---

# Peer Review Report

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Reviewer: Priya Subramaniam-Lund, Perspective Reviewer (edge and distributed systems, industrial research lab; fictional persona)
## Expertise: resource-aware federated systems; cloud scheduling and cost models
## Date: 2026-11-10

---

## Summary
Quorus lets clients with quantum processors of different quality participate in one federated model by assigning each a circuit depth it can execute accurately, and by supervising every layer so shallow prefixes remain useful classifiers. The paper is a systems-flavoured contribution: it counts shots, qubits and mid-circuit measurements for each design (Table 1) and checks the idea on six IBM QPUs.

---

## Strengths

### S1: A timely systems problem
Quantum cloud access is expensive ("$96" per minute, §4.3) and devices differ sharply (Table 5 two-qubit errors from 3.57E-3 to 1.74E-2). Treating that as a federation problem is a sensible and useful framing.

### S2: Explicit resource accounting
Table 1 states which resource each design spends (shots, qubits, mid-circuit measurement, Hilbert space). The Funnel design is a clever way to trade width for readout without mid-circuit measurement.

### S3: Real-hardware contact
Six real QPUs (Table 5, Fig. 8) show device variability (48% to 76% on one model) and the depth-versus-accuracy trade-off on one device (Fig. 8(b)). Few QFL papers go this far.

---

## Weaknesses (framed as opportunities)

### W1: The deployment story is not closed: depth assignment and training happen outside the noise
Clients get a depth by fiat (Table 4, "1 Client per Depth level"), and training uses ideal, shot-free simulation. The device error table (Table 5) does not predict the measured accuracies in Fig. 8(a): Kingston has the lowest layered two-qubit error (3.57E-3) but about 68% accuracy, while Torino has 7.50E-3 and 76% (labels as extracted). A practical rule for choosing a depth per device is needed, and the learned models should be trained or tested under the devices' noise models.
- **Suggested Fix:** Use backend noise models built from Table 5 calibration data for training and evaluation, and propose and test a depth-selection rule.

### W2: Cost accounting is qualitative
Training on hardware with parameter-shift gradients needs on the order of two circuit evaluations per parameter per step (my estimate; 30 parameters per layer, Table 4), multiplied by shots and data points. The paper claims shot efficiency but gives no shots-to-accuracy figures. A deployment reader needs total shots, wall-clock and dollars per design.
- **Suggested Fix:** Add a table of total shots and estimated cost per round for each design and depth, and an accuracy-versus-shots curve.

### W3: Benchmarks versus real-world utility, and the classical reference
All tasks are binary, with 10 PCA features and 128 samples per client, IID. A classical model on the same features would give the reader the reference point for what the federated PQC adds. Standalone already matches Quorus on average (Table 2), so the incentive to federate is not demonstrated. Non-IID clients and fewer samples are where federation matters.
- **Suggested Fix:** Add label-skew non-IID partitions and a smaller-data regime, plus a classical small-model reference.

### W4: Connections from other fields
Multi-exit ("early-exit") networks and anytime-prediction architectures, and deeply supervised networks in classical deep learning, use the same intermediate-classifier idea, and resource-aware FL work on such networks is a natural bridge (§3 already points to ReeFL). Quantum error-mitigation methods (readout-error mitigation, zero-noise extrapolation) are complementary to depth limiting, and combining them could extend usable depth per client. Privacy is claimed as motivation (§1) but no privacy analysis of the shared parameters is given.

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Careful setup; limited breadth |
| Clarity | 3 | Readable |
| Significance | 3 | Useful framing for quantum cloud use |
| Originality | 3 | New readout circuits in a new setting |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: timely problem with a hardware demonstration, unusual in this sub-field; I discount for the small evaluation scale but weight the systems framing.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound circuit design and proof |
| Clarity & Presentation | 68 | Competent | Clear framing and cost table |
| Novelty & Originality | 62 | Competent | New setting, new readout designs |
| Significance & Impact | 66 | Competent | Useful for quantum cloud users |
| Experimental Validation | 56 | Competent | Small scale; hardware part thin |
| Reproducibility | 66 | Competent | Table 4, code released |
| Ethical Compliance | 64 | Competent | Nothing at stake; limitations not discussed |

## Questions for Authors
1. How would a client pick its depth in practice, given that Table 5 error rates do not rank the Fig. 8(a) accuracies?
2. What is the total shot cost to train a depth-5 Funnel model on hardware to the reported accuracy?
3. Would the layerwise advantage persist under label-skew non-IID data?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. Hardware cost is mentioned, but scale, IID data and training outside noise are not.

## Ethics Review Flag
**No**

## Overall Score
**4**: Borderline Accept. A timely, practical framing with creative circuit designs and a real-hardware step, whose evidence base is small but typical of early work in this area.

## Confidence
**3**: Systems perspective; less able to judge quantum-specific details.

---

# Peer Review Report

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Reviewer: Tomasz Weiland-Abara, Generalist Reviewer (machine learning group, mid-sized university; fictional persona)
## Expertise: representation learning and deep learning (not quantum)
## Date: 2026-11-10

---

## Summary
The paper proposes Quorus, a federated training scheme for quantum clients whose circuits have different depths. Each client optimizes a loss that sums per-layer classification losses and a symmetric-like KL consistency term, so shallow clients and deep clients share parameters that all produce useful outputs. Three circuit designs trade shots, qubits and mid-circuit measurement for readout of intermediate layers. Experiments on six binary image tasks and a six-device IBM hardware test aim to show accuracy gains and practicality.

---

## Strengths

### S1: The contribution is easy to state
Depth-heterogeneous quantum clients, a layerwise objective and three readout circuits are identifiable in §1 and Fig. 1. A non-specialist can follow the motivation (§1) and the measurement-collapse obstacle (Fig. 3).

### S2: Modular design with explicit trade-offs
Table 1 maps each variant to one cost. That helps a reader decide which variant fits which client.

### S3: Detailed experimental table and appendices
Table 4 and Appendices B–D answer most reproducibility questions, and the proof of Ancilla ≡ Blocking is short and clear.

### S4: Hardware experiment included
Evaluating on six QPUs (Table 5, Fig. 8) adds credibility that the circuits run, which many QML papers omit.

---

## Weaknesses

### W1: The headline sentence and the evidence do not line up
The abstract claims "improves testing accuracy by 12.4% on average over the state-of-the-art", §1 says "by up to 12.4%", and the Table 2 caption says "consistently outperforms the baselines". Reading Table 2, the gain is large only against Q-HeteroFL (a baseline the authors built) and is about zero against Standalone and Vanilla QFL, which are the baselines a practitioner would try first. Readers outside QML will see this as a framing problem before they see anything else.
- **Suggested Fix:** Make one consistent claim (average gain over a HeteroFL-style baseline, parity with Standalone in this IID regime) and show it in a compact summary figure.

### W2: Scope and limitations are not stated, and the results are small-scale for ICLR
Tasks are binary, 10 PCA features, 128 samples per client, five clients, IID (Table 4), with no classical reference and no limitations section found. ICLR audiences will ask why federation is needed when each client can already reach about the same accuracy alone, and how the method behaves beyond 10 qubits. The fit to ICLR is plausible (learning on a new compute substrate), but the contribution to the representation-learning audience is currently narrow.
- **Suggested Fix:** Add a limitations paragraph and one regime where federation clearly helps (non-IID or very small data).

### W3: Presentation of the main results and terminology
Table 2 packs 6 tasks × 5 capacities × 4 methods with delta annotations, and the key takeaway is hard to extract. "Layer", "depth", "capacity" and "L" are used interchangeably, and App. D.1 says an L-layer client has "L − 1" classifiers while Eq. 1 sums over d_k classifiers; Table 7 lists a 1-layer model. §3's first sentence mixes classical and quantum settings.
- **Suggested Fix:** Define "capacity" once, state the classifier count, and add a summary plot (gain versus capacity for each baseline).

**Minor:** Eq. 1 refers to "logits" while single-qubit outputs are probabilities; "McMahan et al., 2023" for FedAvg; Sec. 6 refers to "Sec. 5" for hardware results.

### Venue criteria checklist (ICLR)
| Item | Grade | Location |
|------|-------|----------|
| Soundness: claims backed by experiments | Partly | Table 2 vs Standalone; §6 hardware |
| Contribution: significant to the ICLR audience | Partly | Narrow scale; new substrate |
| Presentation: clear to non-specialists | Mostly met | §1–§4; Table 2 dense |
| Reproducibility / code | Met (unverified link) | Table 4, §1 bullet 5 |
| Honest limitations | Not met | no section found |

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claim and evidence mismatch |
| Clarity | 3 | Good flow, dense results |
| Significance | 2 | Narrow evidence of benefit |
| Originality | 2 | New setting, borrowed loss |

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, reasonably written paper whose main empirical claim is narrower than its wording.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Sound pieces, evaluation not isolating them |
| Clarity & Presentation | 64 | Competent | Readable; headline inconsistent |
| Novelty & Originality | 54 | Developing | New setting; known loss |
| Significance & Impact | 52 | Developing | Niche, small scale |
| Experimental Validation | 48 | Developing | Weak baseline, narrow tasks |
| Reproducibility | 64 | Competent | Table 4 and code |
| Ethical Compliance | 58 | Competent | Nothing at stake, limitations missing |

## Questions for Authors
1. In what regime does a client gain from federation compared with Standalone? A plot would raise my score.
2. Which classifier outputs are used at test time for each method?
3. How does the approach scale beyond 10 qubits in simulation?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A tidy, understandable paper whose evidence supports a narrower claim than the one made.

## Confidence
**3**: Not a quantum specialist; the comparison logic is checkable from the tables.

---

# Devil's Advocate Report

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Reviewer: Samira Oduya-Lindqvist (evaluation methodology and causal inference, independent research institute; fictional persona)

---

## Steelman
Depth-limited quantum clients are a real consequence of heterogeneous NISQ devices, and classical depth-wise FL cannot be ported directly because measurement collapses the state. Quorus shows that three readout circuits make a DepthFL-style objective usable, that this beats a HeteroFL-style quantum baseline by a large average margin, and that the circuits run on real IBM devices.

---

## Core Argument Chain
1. Quantum devices differ in error, so clients can only run circuits of different depths (§1, Table 5, Fig. 8(a)).
2. Training only the deepest output causes parameter mismatch across depths (Q-HeteroFL, §5).
3. A layerwise loss with reverse distillation aligns objectives across depths (Eq. 1, borrowed from DepthFL).
4. Intermediate classifiers need new readout circuits; three designs give them (§4.3).
5. Quorus beats Q-HeteroFL by 12.4 points on average and raises gradient norms (Table 2, Fig. 7).
6. Quorus-Funnel runs on IBM QPUs within 3% of ideal (Fig. 8).
∴ Quorus is an effective, practical QFL framework for heterogeneous quantum clients that improves on the state of the art.

---

## Strongest Counter-Argument
Premise 5 does not support the conclusion. The only baseline Quorus clearly beats is one the authors built for this paper, with a loss that is known to leave shallow sub-models poorly trained, and with the weakest possible readout (deepest output only). Against the two baselines any practitioner would try first, Standalone training and Vanilla QFL (everyone uses the shallowest depth), Table 2 shows nothing: recomputed over 30 cells, mean Quorus − Standalone is +0.24 points and Quorus − Vanilla is +0.43 points, with per-cell stds of 0.2–8.1, and Standalone wins on Bag/Sandal at every capacity. So the experiment cannot show that the layerwise loss, rather than the quantity of quantum depth or the test-time ensemble, helps federated training. The Quorus rows are also evaluated as ensembles of L − 1 classifiers (App. D.1), and the ablations that would separate CE-only layers from KL distillation from ensembling are absent. The claim "over the state-of-the-art" thus compares a full pipeline (loss + KL + ensemble + selected ansatz) with a deliberately minimal pipeline, in an IID setting with 128 points per client where federation itself adds nothing measurable. Premise 1's motivation, noise heterogeneity, plays no role in training: depth is assigned by fiat and training is analytic and shot-free (Table 4), so the paper never shows that depth-heterogeneous FL beats the alternatives under the noise that motivates it. The hardware result evaluates one model on 100 points on six devices and reports the best one ("within 3%") in the contribution list; nothing on hardware compares Quorus with any baseline. Finally the gradient-norm claim follows from attaching losses to early layers (by construction, as Cerezo et al. show for local costs) and says nothing about trainability at depths where plateaus bite (accuracy already saturates by 6 layers, Table 7). The authors must answer: what does federation add over Standalone, what does the layerwise loss add over ensembling, and what is the benefit under noise?

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in a narrower form (Quorus improves over a HeteroFL-style quantum baseline on these IID toy tasks): the comparison with Q-HeteroFL holds under every alternative ansatz in Table 6 (Staircase 30/30 cells, Alternating 29/30; the exception is 2L MNIST 0/1: 88.2 vs 90.3), so even the test-set selection cannot change that conclusion.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (selection) | App. D.1 / Table 6; Table 3 caption; App. D.2 | Ansatz, designs and layer count selected by testing accuracy: "accuracy the most times, so we use it for all of our experiments". Table 6 V-shape rows equal the Table 2 Quorus rows. No validation split (protocol sweep found none). Decision-table row: best-scoring option, chosen by score, but the main comparison with Q-HeteroFL holds at every other swept value (one cell excepted) → MAJOR, not CRITICAL. | Select on a validation split, report the untouched test set |
| DA-M2 | Logic / Scope | Table 2, caption | "consistently outperforms the baselines" is contradicted; federation adds +0.24 points over Standalone (derived), +0.43 over Vanilla QFL. Evidence supports a weaker claim (fixable by narrowing). | Narrow the claim; add regimes where federation matters (non-IID, fewer samples) |
| DA-M3 | Evidence | §5, App. C.1 | "State-of-the-art" baseline is the authors' own Q-HeteroFL, with loss only at the deepest classifier; no tuning reported for any method. | Add stronger baselines; rename |
| DA-M4 | Confounds | App. D.1, Fig. 10 / App. D.3 | Quorus rows use an L − 1-classifier ensemble; baseline readout unstated; no CE-only / KL / ensemble ablation. | Ablate; give baselines matching readout |
| DA-M5 | Scope / Overclaim | §1 bullet 4, §6, Fig. 8, App. D.3 | "within 3%" holds for 1 of 6 QPUs, one model, 100 points (SE ≈ 4 points); no baseline on hardware; Ancilla design claimed "confirmed on IBM hardware" but never run. | Report all devices with CIs and a hardware baseline; restate |
| DA-M6 | Overclaim | §1 bullet 4, §6 | Gradient-norm increase is by construction; later layers stay small; no depth where barren plateaus bite. "scalable trainability for deep quantum circuits" unsupported. | Normalize loss scale, test deeper circuits, or tone down |
| DA-M7 | Overclaim | Abstract, §5, Table 1, Table 4 | "Shot-efficient" is never measured; training is analytic. The paper's motivating noise is absent from training. | Finite-shot / noise-model experiments |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §1 bullet 3 vs Abstract | "up to 12.4%" vs "on average"; the maximum cell gap is 36.4 points |
| DA-m2 | Consistency (question) | Fig. 8(a) vs Fig. 8(b) | Kingston depth 5 reads about 68% vs about 58% in the extracted labels; figure unavailable, so unverified |
| DA-m3 | Clarity | §3 first sentence | Classical and quantum FL conflated |
| DA-m4 | Provenance | Table 4 | Test size 3000 vs binary class-pair test splits of roughly 2,000 images (from my recollection of the datasets) |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Average gain over Q-HeteroFL | 12.4 | Sum of 30 cell differences 371.1 → 12.37 | Yes (as a mean absolute-point gain) |
| "up to 12.4%" | 12.4 | Maximum cell difference 36.4 | No |
| Gain over Standalone | not reported | mean +0.24 (2L −0.97, 3L +0.20, 4L +0.15, 5L +0.78, 6L +1.03) | n/a (derived) |
| Gain over Vanilla QFL (2L) | not reported | mean +0.43 | n/a (derived) |
| "within 3%" | 3 | 79 − 76 = 3 for Torino only | Partly |
| "nearly 40% worse" (3/4) | ≈ 40 | 95.0 − 58.8 = 36.2 | Approximately |
| 1-layer "40% lower" | ≈ 40 | 98.8 − 58.6 = 40.2 (Table 7) | Yes |
| Funnel "always within 1%" of best Quorus | ≤ 1 | all Table 3 deltas for Funnel ≤ 0.7 | Yes |

## Ignored Alternative Explanations
- Test-time ensembling and the number of trainable layers explain the accuracy rise with capacity, not federation.
- Q-HeteroFL fails because its shallow sub-models never get a direct loss, which would be fixed by any per-depth head; this is not specific to the layerwise-KL design.
- PCA features and IID data make the task easy enough that Standalone matches the federated model.
- Hardware accuracy differences across QPUs may reflect transpilation and finite-sample noise as much as device error (Table 5 error rates do not rank Fig. 8(a) results).
- Funnel (smaller Hilbert space later) beats Layerwise on the hardest tasks (Table 3, e.g. 85.2 vs 83.1 at 6L, MNIST 4/9), which sits oddly with the expressivity explanation given in App. D.1.

## Missing Stakeholder Perspectives
Quantum-cloud users who must pay per shot are the target, but no cost per design is quantified. Clients with low-quality QPUs would be assigned shallow depth and may contribute little (§6 says so), so who benefits from federation is not examined. Privacy of shared parameters is not analysed.

## Observations (Non-Defects)
- The Ancilla ≡ Blocking proof (App. B, Prop. 1) is correct as stated for one layer.
- The authors make Standalone deliberately strong (persistent Adam state, federated PCA) and report the unfavourable smallest-capacity cells honestly.
- Hyperparameters are fully reported (Table 4) and five data allocations with std are shown.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Test-selected configuration and confounded readout |
| Clarity & Presentation | 62 | Readable; claim wording inconsistent |
| Novelty & Originality | 46 | Loss borrowed; readout designs partly new |
| Significance & Impact | 44 | Benefit over simple alternatives not shown |
| Experimental Validation | 38 | Weak baseline, no ablations, thin hardware test |
| Reproducibility | 58 | Table 4 complete; seeds and hardware settings missing |
| Ethical Compliance | 54 | No limitations section found |

**Pool position:** better than about 34% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline margin exists only against an author-built baseline, and the federated method is indistinguishable from Standalone in the same table.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

The five reports were checked against the four tests (specific, not already answered, consistent with the paper, actionable). Scores were not changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "No seeds stated" (draft) | rewritten (merged into W5 with the shared-initialization point) | Seeds are indeed not stated, but App. C says five data allocations are used; specific location added |
| R1 | Test size origin (3000) | moved from weakness to a question inside W5 | Depends on my recollection of dataset sizes, not on a statement in the paper |
| R2 | Missing empirical comparison with SpoQFL | rewritten as "discuss", not "require" | SpoQFL is a recent preprint (July 2025) and is cited by the paper |
| R2 | Sá et al. (2023) does not support the claim | moved to a question | Cannot be verified from the abstract; low confidence |
| R3 | "No classical baseline" (draft) | rewritten as a reference-point suggestion inside W3 | The paper does not claim quantum advantage |
| R4 | Typos and "logits" wording | moved to Minor line | Cosmetic |
| DA | Fig. 8(a) vs 8(b) inconsistency | kept as MINOR question | Read from extracted figure labels; figures unavailable |
| DA | Test-set selection | kept as MAJOR | Selection quotes found at App. D.1, Table 3 caption, App. D.2; decision-table row 2 applies |
| All | Hardware overclaim (R1-W4, R3, DA-M5) | kept; merged in Phase 2 | Verified against §6 and Fig. 8 |

---

# Phase 2: Synthesizer Package, EIC Meta-Review and Decision

## Synthesizer, part A: merged issue list and consensus map

| Merged issue | Sources | Class | Hinges on outcome? |
|--------------|---------|-------|--------------------|
| Headline gain is against an author-built baseline; ≈ 0 against Standalone/Vanilla | R1-W1, R4-W1, R3-W3, DA-M2, DA-M3, R2-W4 | CONSENSUS-5 | Yes |
| Confounded loss / KL / ensemble readout; no ablation | R1-W2, DA-M4 | CONSENSUS-2 | Yes |
| Selection on test accuracy, no validation split | R1-W3, DA-M1 | CONSENSUS-2 | Checked |
| Hardware claims overstated (1 of 6 QPUs, 100 points, no baseline; Ancilla not run) | R1-W4, R3-W1 (partly), DA-M5 | CONSENSUS-3 | Yes |
| Shot-efficiency and noise motivation not tested | R1-W4, R3-W2, DA-M7 | CONSENSUS-3 | Yes |
| Gradient-norm / barren-plateau claim by construction | R1-W4, R2-W3, DA-M6 | CONSENSUS-3 | Minor |
| C1 loss borrowed from DepthFL; novelty overstated | R2-W1 | SOLO | Partly |
| Related-work framing contradicts cited SpoQFL / NAC-QFL | R2-W2 | SOLO | No |
| No limitations section; scale small | R4-W2, R3-W3 | CONSENSUS-2 | No |
| SPLIT: hardware as strength (R3-S3, R4-S4) vs overclaim (R1, DA) | R3, R4 vs R1, DA | SPLIT | Yes |
| DA-CRITICAL | none raised | n/a | n/a |

**Official output (before EIC weights; DA list empty), from `aggregate_scores.py --venue iclr`:** official ratings R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00; official composite 54.0; no consistency warnings; ⚠ spread only on Significance & Impact (22).

---

## EIC Meta-Review (Marisol Quenneville)

### The Case For and Against
- **For acceptance:** A new, well-defined problem (depth-heterogeneous quantum clients) with a non-trivial quantum-specific obstacle (measurement collapse) and three concrete circuit designs, a correct equivalence proof, full hyperparameters and an actual six-device hardware step that is rare in QFL papers. Weaknesses such as small scale and IID data are typical of early papers in this area.
- **Against acceptance:** The main empirical claim is relative to a baseline the authors built, while the federated method is statistically indistinguishable from Standalone and Vanilla QFL in the same table. The gain cannot be attributed to the layerwise loss because the ensemble readout and the KL term are not ablated, configurations were chosen on test accuracy, and the efficiency, hardware and barren-plateau claims go beyond what was measured.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Mean Quorus − Standalone ≈ +0.24, − Vanilla ≈ +0.43 points | R1-W1, DA-M2 | Table 2 | Verified | I recomputed all 30 cells: 7.2/30 and 12.8/30 |
| 12.4 is a mean absolute gain; "up to" wording wrong | R1 ERR-2, DA-m1 | Abstract, §1 bullet 3, Table 2 | Verified | 371.1/30 = 12.37; max 36.4 |
| Gain over Q-HeteroFL shrinks with depth (22.4 points at 2L, 6.8 at 6L) | (EIC) | Table 2 | Verified | Most of the 12.4 comes from the 2L–3L cells where Q-HeteroFL collapses |
| Quorus rows are evaluated as ensembles; baseline readout not stated | R1-W2, DA-M4 | App. D.1 | Partly correct | Ensembling for Quorus verified; whether baselines ensemble is unstated, so the confound is possible, not shown |
| Selection on test accuracy; V-shape rows equal Table 2 rows | R1-W3, DA-M1 | App. D.1, Table 3 caption, App. D.2, Table 6 | Verified | Quotes found by text search; no validation split anywhere |
| Q-HeteroFL comparison survives other ansatzes | DA (critical-issue check), R1-W3 | Table 6 vs Table 2 | Verified | Staircase 30/30, Alternating 29/30 |
| "within 3%" is 1 of 6 QPUs; n = 100; single Funnel model | R1-W4, DA-M5 | §6A, Fig. 8(a) | Verified | Torino 76% vs 79%; Brisbane 48% |
| R3 treats hardware as validation of robustness | R3-S3 | §6, App. D.3 | Overstated | Same single-model, 100-point evidence; no baseline on hardware |
| Ancilla "confirmed on IBM hardware" | R1 ERR-4 | §4.3 vs §6 | Verified | Hardware uses Funnel only |
| Intro claim contradicts cited SpoQFL / NAC-QFL | R2-W2 | §1, §3, SpoQFL abstract | Verified | Depth heterogeneity is the accurate scope; noise heterogeneity is addressed |
| Gradient norms higher by construction; later layers stay small | R2-W3, DA-M6 | §6, Fig. 7 caption | Partly correct | The paper itself says later layers stay small; "by construction" is an inference, consistent with the cited local-cost result |
| Fig. 8(a) vs 8(b) Kingston discrepancy | DA-m2, R1 Q4 | Fig. 8 | Partly correct | Read from extracted labels only; cannot be confirmed without the figure |
| "L − 1 classifiers" vs Eq. 1 / Table 7 | R1 ERR-7, R4-W3 | App. D.1, Eq. 1, Table 7 | Verified | A clarity issue, not a result error |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log entry I checked holds (ERR-1 to ERR-6); recomputation matches; the one Medium-confidence entry is correctly labelled MINOR |
| R2 (Domain) | 3 | 3 | 1.0 | Citation framing point verified; the literature check was limited by the API; no overstatement found |
| R3 (Perspective) | 4 | 3 | 0.75 | Treats single-model, 100-point hardware evidence as validation of robustness (Overstated); calibration is generous relative to the verified evidence |
| R4 (Generalist) | 3 | 3 | 1.0 | Claims verified; sound, typical review |
| DA | 2 | 4 | 1.0 | Counter-argument verified; test-selection rightly rated MAJOR, not CRITICAL; the Overall of 2 sits at the harsh end for a paper whose narrower claim is supported |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | No DA-CRITICAL issue was raised, so no ceiling applies. I also checked the test-selection issue against the criterion-3 table (best-scoring ansatz, chosen by its score, producing the headline rows): the comparison with Q-HeteroFL holds at every other swept value except one cell, so row 2 applies and MAJOR is correct | n/a |

### Final Decision and Justification
The reviewers' recommendations are 3, 3, 4, 3, 2 (official mean 3.00, official composite 54.0). With my weights (R1 1.25, R3 0.75, others 1.0) the EIC-weighted rating is 2.92, which rounds to the starting point **3**; the weighted composite is 53.0, in band 3, so the composite cross-check agrees and I do not depart. No DA ceiling applies. My own pool position is **42**: the paper is on the rejected side of the ICLR bar (accepted share ≈ 27%) because its main claim rests on an author-built baseline, the federated method is indistinguishable from Standalone in the same table, and test-selected design choices and an unablated ensemble readout leave the source of the gain unknown. It is not lower, because the problem is new, the circuit designs and the equivalence proof are real contributions, the reporting of setup is unusually complete, and most issues are fixable by narrowing claims and adding ablations on a small simulator. R3's 4 depends on hardware evidence I verified to be a single model on 100 points, so I do not follow it; DA's 2 weights the same weaknesses a step more harshly than the narrower, still supported, claim warrants. The final Overall is **3 (Borderline Reject)**, equal to the starting point, and within the ceiling (none).

---

## Editorial Decision

## Paper: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus
## Date: 2026-11-10
## Target Venue: ICLR (2026 cycle) | Paper Type: empirical
## Review Team (fictional personas): EIC Marisol Quenneville; R1 Lucia Ferreyra-Okafor (Methodology), R2 Henrik Daalmans (Domain), R3 Priya Subramaniam-Lund (Perspective), R4 Tomasz Weiland-Abara (Generalist), DA Samira Oduya-Lindqvist

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 54.0
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 53.0 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR translation** (scale status: secondary; present as "recent forms use…; verify against the current form"): Soundness 2, Presentation 3, Contribution 2; Rating **4 on {0, 2, 4, 6, 8, 10}** (5 on {1, 3, 5, 6, 8, 10}); Confidence per reviewer above.
**Pool positions:** R1 38, R2 46, R3 66, R4 48, DA 34; EIC 42.

---

## Score Summary

### Official Scores and EIC Assessment
| Reviewer | Overall | Confidence | Pool pos. | Own composite | EIC weight | Weight share |
|----------|---------|------------|-----------|---------------|------------|--------------|
| R1 | 3 | 4 | 38 | 50.4 | 1.25 | 0.277 |
| R2 | 3 | 3 | 46 | 54.3 | 1.0 | 0.182 |
| R3 | 4 | 3 | 66 | 62.6 | 0.75 | 0.137 |
| R4 | 3 | 3 | 48 | 54.9 | 1.0 | 0.182 |
| DA | 2 | 4 | 34 | 47.7 | 1.0 | 0.221 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 56 | 62 | 54 | 46 | 53.6 | 52.6 | 16 |
| Clarity & Presentation | 62 | 62 | 68 | 64 | 62 | 63.6 | 63.2 | 6 |
| Novelty & Originality | 50 | 52 | 62 | 54 | 46 | 52.8 | 51.9 | 16 |
| Significance & Impact | 46 | 50 | 66 | 52 | 44 | 51.6 | 50.1 | 22 ⚠ |
| Experimental Validation | 40 | 48 | 56 | 48 | 38 | 46.0 | 44.7 | 18 |
| Reproducibility | 62 | 62 | 66 | 64 | 58 | 62.4 | 62.0 | 8 |
| Ethical Compliance | 56 | 58 | 64 | 58 | 54 | 58.0 | 57.4 | 10 |
| **Composite** | | | | | | **54.0 (before)** | **53.0 (after)** | |

⚠ Significance spread: R3 (66) values the systems framing and the hardware step; R1 and DA (46, 44) see no demonstrated benefit over Standalone. I adopt the lower view, since the benefit over simple alternatives was verified to be near zero in Table 2.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus" to ICLR. The question of how quantum clients with devices of different quality can train together is timely, and the paper takes the unusual step of running on six IBM processors.

**Overall Assessment:** The panel found a clearly posed problem, creative readout circuits and a complete hyperparameter table. It also found that the main empirical claim is narrower than its wording: the large gain is against a baseline built for this paper, and Table 2 shows the federated method is on average indistinguishable from standalone training and from vanilla QFL in the studied IID regime.

**Key Strengths Identified by Reviewers:**
1. A well-motivated problem and a quantum-specific obstacle (measurement collapse), with three concrete circuit designs and a correct equivalence proof (R2, R3, R4).
2. Transparent setup: full hyperparameters, five data allocations with mean ± std, ansatz and layer-count sweeps (R1, R4).
3. A real-hardware evaluation across six QPUs, rare in this literature (R3, R4).

**Key Concerns Requiring Attention:**
1. The headline gain is measured against Q-HeteroFL, constructed by the authors, labelled "state-of-the-art", while Quorus ≈ Standalone (+0.24 points) and ≈ Vanilla QFL (+0.43 points) in Table 2 (CONSENSUS-5).
2. The layerwise loss, KL term and ensemble readout are not separated by ablation, and the loss is taken from DepthFL (CONSENSUS-2, SOLO R2).
3. Ansatz, design and depth were selected on test accuracy with no validation split (CONSENSUS-2, MAJOR).
4. Efficiency, hardware ("within 3%" holds for 1 of 6 QPUs, one model, 100 points) and barren-plateau claims go beyond what was measured; the Ancilla design is described as confirmed on hardware but was not run there (CONSENSUS-3; SPLIT on the value of the hardware step).

**Decision: Borderline Reject (3).** The panel sees reasons to reject slightly outweighing reasons to accept for this draft. A revision that narrows the claims, adds the ablations and stronger baselines below, uses a validation split, and quantifies shot cost or noise would put the paper in a much stronger position. This is a simulation of how a careful panel would likely see the draft, not a prediction of any real outcome. Please refer to the Revision Roadmap below.

Sincerely,
Marisol Quenneville
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Headline gain vs author-built baseline; parity with Standalone / Vanilla | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Hardware claims overstated (1 of 6 QPUs, 100 points, no baseline) | R1, R3 (qualified), DA | CONSENSUS-3 |
| Shot-efficiency / noise motivation untested | R1, R3, DA | CONSENSUS-3 |
| Gradient-norm claim by construction | R1, R2, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Hardware evaluation as validation | R3, R4 (strength) | R1, DA (overclaim) | Overstated: single Funnel model, 100 points, no baseline on hardware; useful as a feasibility demonstration only |
| Overall recommendation | R3 (4) | DA (2) | Weighted to 3; R3's rating rests on the overstated hardware point, DA's is a step harsh |

### Score Spread Discussion
Significance & Impact (spread 22 ⚠): R3 66 vs R1 46 and DA 44, as explained above; the lower view is adopted. Technical Rigor (16), Novelty (16) and Experimental Validation (18) are below the 20-point flag.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Selection on test accuracy | Yes (R1-W3) | n/a (checked: MAJOR is right) | Clarification plus a rerun of selection on a validation split |
| DA-M2 | MAJOR | Federation adds ≈ 0 over Standalone | Yes (R1, R4, R3) | n/a | Claim narrowing plus new regimes |
| DA-M3 | MAJOR | Author-built baseline called state of the art | Yes (R1, R2) | n/a | Renaming plus stronger baselines |
| DA-M4 | MAJOR | Loss / KL / ensemble confound | Yes (R1-W2) | n/a | Ablation on existing code |
| DA-M5 | MAJOR | Hardware overclaim | Yes (R1, R3) | n/a | Rewording plus more hardware points |
| DA-M6 | MAJOR | Gradient norm by construction | Yes (R2, R1) | n/a | Rewording / deeper circuits |
| DA-M7 | MAJOR | Shot-efficiency untested | Yes (R1, R3) | n/a | Finite-shot / noise-model runs |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No DA-CRITICAL issue was upheld. These items are issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline gain relies on an author-built baseline; ≈ 0 over Standalone / Vanilla; "state-of-the-art", "consistently" and "up to" wording | R1-W1, R4-W1, DA-M2, DA-M3, R2-W4, ERR-1, ERR-2 | Abstract, §1, Table 2 caption, §5 | Narrow the claim to a HeteroFL-style baseline; add per-client layerwise-loss (no aggregation) and per-depth-head FedAvg baselines; add a regime where federation matters (non-IID or fewer samples) | Medium; < 50 CPU-h | Partly (wording yes; new regimes need more time) |
| R2 | Source of the gain unknown: loss vs KL vs ensemble readout | R1-W2, DA-M4 | Eq. 1, App. D.1, Fig. 10 | Ablate CE-only, CE+KL, last-classifier-only; state baseline readout | Low–Medium; ≈ 90 runs on the simulator | Yes |
| R3 | Selection on test accuracy; no validation split | R1-W3, DA-M1, ERR-3 | App. D.1, D.2, Tables 3, 6, 7 | Select on a validation split; report test once; fix seeds and initialisation variation | Medium | Partly |
| R4 | Hardware and efficiency claims unsupported as worded | R1-W4, R3-W2, DA-M5, DA-M7, ERR-4, ERR-5, ERR-6 | §1 bullet 4, §4.3, §5, §6, Fig. 8 | Report all six QPUs with CIs on ≥ 1000 points, add a baseline on hardware, drop "confirmed" for Ancilla, and either measure shot cost (finite-shot or noise-model training) or remove "shot-efficient" | Medium–High; hardware queue plus 50–100 CPU-h | Partly |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Gradient-norm / barren-plateau claim by construction | R2-W3, DA-M6, R1-W4 | Frame as application of local-cost results; normalize loss scale; test deeper circuits | Medium | Partly |
| S2 | C1 loss borrowed from DepthFL; "first-of-its-kind" | R2-W1 | State the delta precisely; lead with the circuit designs | Low | Yes |
| S3 | Related-work framing vs cited QFL work | R2-W2 | Reframe around depth heterogeneity; discuss SpoQFL / NAC-QFL; compare with one noise-aware baseline | Low–Medium | Partly |
| S4 | Missing Important references: Skolik et al. (2021), QUILT (AAAI 2022), Li et al. (2023) ensemble error mitigation | R2 | Cite and differentiate | Low | Yes |
| S5 | Variance protocol and test-set provenance | R1-W5, DA-m4 | Vary initialisation seeds; paired CIs; state test-set source and disjointness | Low | Yes |
| S6 | Add a limitations section; Table 2 readability; "L − 1 classifiers" definition | R4-W2, R4-W3, ERR-7 | Limitations paragraph; summary plot; define capacity and classifier count | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Depth-selection rule per device; noise-model-based training | R3 | Propose and test a rule; use Table 5 calibration data |
| N2 | Connections to multi-exit networks, deep supervision, error mitigation, privacy analysis | R3 | Discuss as related lines of work |
| N3 | Fig. 8(a) vs 8(b) Kingston values; Sá et al. support; citation years | DA-m2, R2 | Clarify or correct |
| N4 | Helpful references (Zhao 2023; McClean et al. 2018; Chehimi & Saad 2022 [verify]) | R2 | Add to related work |
| N5 | Classical reference model; scaling beyond 10 qubits | R3, R4 | Optional reference points |

---

## Estimated Revision Effort
- Priority 1: 4 items, roughly 2–4 weeks (simulator runs under ~150 CPU-hours in total, plus hardware queue time).
- Priority 2: 6 items, roughly 1–2 weeks (mostly writing, plus a few simulator runs).
- Priority 3: 5 items, optional.
- **Total estimated revision time**: about 4–6 weeks, of which only the Priority 1 wording, ablations and reference additions fit a one-week rebuttal window.
