# Review of "Heat Kernel Goes Topological" (simulated ICLR panel, skill v2.10.1)

*Simulation of how a careful panel would likely see this draft; not a prediction of the venue outcome. Run date 2026-11-10. User request: full review, skip confirmation, literature check strict, cutoff 2025-09-24. The five reviewer passes were run one after another in one shared model context (no subagents); independence is by role and instruction only. The manuscript text is extracted from the PDF; **figures are not available**, so figure-dependent claims (Fig. 1–7) are judged from captions and text only.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Heat Kernel Goes Topological |
| Primary Discipline | ML → topological deep learning / expressivity of graph and higher-order networks |
| Secondary Discipline(s) | Spectral graph theory; discrete geometry (heat kernel signatures from shape analysis); molecular property prediction |
| Paper Type | Empirical (method paper with a theoretical expressivity claim; composite weights: empirical). A theoretical weighting was considered and rejected because the headline evidence is experimental. |
| Core Technique(s) | A rank-weighted Laplacian on rank-0 cells of a combinatorial complex (CC); per-node heat kernel signature (HKS) at d=10 times; transformer / MLP-Mixer backbone |
| Target Venue | ICLR (stated by user), profile key `iclr` |
| Venue-Specific Notes | Public OpenReview discussion; ICLR 2025 already published the closest expressivity paper (SMCN, ref. [6]) |
| Paper Maturity | Submission-ready in form; theory and protocol sections read as an early draft (sketch proofs, broken cross-references) |
| Ethics-Relevant Content | None beyond a boilerplate positive-impact statement (Conclusion, "Social Impact") |

### Claimed Contributions (as stated by the authors, Section 1)
1. **C1** Topological embeddings for transformers: a CC embedding that is "permutation-invariant and computationally efficient" (Section 1, item 1; Sections 3.1–3.3).
2. **C2** Theoretical expressiveness: distinguishes non-isomorphic CCs and outperforms WL-based methods; "maximally expressive" (Abstract; Section 1, item 2; Theorem 4.3, Corollary 4.3).
3. **C3** Empirical performance: "state-of-the-art results" on MolHIV, PROTEIN and topological structure datasets (Section 1, item 3; Tables 2–3). The Abstract says only "competitive performance".
4. **C4** Scalability and efficiency: "scales efficiently to large combinatorial complexes" (Section 1, item 4; Figure 6; Table 3).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** d = 10 times, equally spaced in [0, 3] (Section 5, intro). Hardware: single V100 32 GB; "1 to 5 hours" per training; "6,000 GPU hours" total (Section 5). Splits: "equivalent to [5]" for MolHIV and PROTEIN (Section 5.3); the split of [18] for Gifflar (Section 5.4). Seeds / number of runs: not stated for Tables 2–3 (only Figure 6 says "Mean over five runs"). Hyperparameters of the network (depth, width, learning rate, epochs, selection criterion): not stated after search. Baseline provenance (copied or re-run): not stated. Code: "after acceptance" (Section 1).
- **Headline numbers.** Table 3: MolHIV 83.1 ± 1.3 (SMCN 81.16 ± 0.90; CIN 80.94 ± 0.57); PROTEIN 79.2 ± 1.0 (CIN 77 ± 4.2); Glycose MCC 0.90 ± 0.03 (SMCN 0.90 ± 0.07); Immunogenicity MCC 0.84 ± 0.01 (SMCN 0.85 ± 0.01). Table 2 / Fig. 5a: 223 distinguished pairs, 100% accuracy, 95–100 it/s vs SMCN 7–10 it/s. Section 5.2: "approximately 12 times faster than SMCN".
- **Appendix** (Section 8) contains full proofs of Cor. 8.1, Thm 8.1–8.3, Lemma 8.1, Cor. 8.2–8.3. No additional experiments, no hyperparameter table, no supplement.
- **Unverifiable.** All figures (1–7) are not available; Fig. 4 / Fig. 7 (the Hodge vs CC Laplacian counterexample) and Fig. 5b–c cannot be inspected. Table 1 was read from extracted text (cell alignment medium confidence).
- **Integrity scan** (`integrity_scan.py`): no reviewer-directed text or hidden characters found; the reviewers read an identical redacted copy. No out-of-place instructions were seen while reading.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ilse Brandvold, senior area chair (large public research university, Northern Europe)
- **Seniority / Expertise**: Senior faculty / geometric deep learning, graph expressivity, spectral methods
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Checks every theorem statement against its proof before trusting a ratings summary

### Reviewer 1 (Methodology): Dr. Kwabena Osei-Lindqvist, mid-career (industrial research lab, West Africa / Europe)
- **Seniority / Expertise**: Mid-career / evaluation of graph learning benchmarks (OGB protocols); proofs of expressivity results
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every headline delta; insists on matched backbones and stated seeds

### Reviewer 2 (Domain): Prof. Anaïs Ravelo-Tan, senior faculty (research university, Southeast Asia)
- **Seniority / Expertise**: Senior faculty / hypergraph and simplicial Laplacians; topological deep learning
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads definitions line by line and tests them on small examples

### Reviewer 3 (Perspective): Dr. Priyanka Delacroix-Nair, mid-career (computational geometry group, Western Europe)
- **Seniority / Expertise**: Mid-career / spectral shape analysis, signal processing on graphs
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for what the idea could become

### Reviewer 4 (Generalist): Dr. Mateo Sorensen-Ikeda, postdoc-to-faculty transition (university, East Asia / Americas)
- **Seniority / Expertise**: Early-career faculty / representation learning for structured data
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; reads the whole paper, does not rederive every proof

### Devil's Advocate: Prof. Yusra Haldane-Okafor, senior faculty (statistics department, Middle East / Europe)
- **Seniority / Expertise**: Senior / algebraic graph theory, evaluation methodology
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: States the strongest version of the claim, then tests it against a counterexample

---
*Personas are fictional. Venue was stated by the user, so no inference was needed.*

---

# Phase 1: Independent Reviews

# Peer Review Report

## Paper: Heat Kernel Goes Topological
## Reviewer: Dr. Kwabena Osei-Lindqvist, Reviewer 1 (Methodology) (industrial research lab; fictional persona)
## Expertise: graph-learning evaluation protocols; expressivity proofs
## Date: 2026-11-10

## Summary
The paper defines a Laplacian on the rank-0 cells of a combinatorial complex as a rank-weighted sum of incidence outer products (Eq. 2), takes per-node heat kernel diagonals at ten diffusion times as node descriptors (Eq. 5), and feeds them with the node features to a transformer or MLP-Mixer. It claims the descriptors separate any non-isomorphic CCs (Theorem 4.3), reports perfect separation on a self-built torus pair set (Fig. 5a, Table 2), and reports competitive or better scores and much lower time than higher-order message-passing baselines (Table 3, Fig. 6).

**Protocol sweep (full text, no supplement).** Quotes on splits and selection: "The train/val/test setup is equivalent to [5]." (Section 5.3); "We train all models using the train/val/test split from [18]" (Section 5.4). Which split was used for tuning, early stopping or checkpoint choice, and which split is reported: **not stated after search**. Seeds/number of runs for Tables 2–3: not stated after search. Hyperparameters beyond d = 10 and the time grid: not stated. Compute: stated (V100, 1–5 h, 6,000 GPU hours, Section 5). Code: promised "after acceptance". No statement of selecting on the test set exists, so no leakage claim is made.

## Strengths
### S1: A clear, cheap pipeline
Eq. 2–5 plus Section 3.3 define a pipeline that is simple to state: one dense eigendecomposition per complex, then a standard sequence model. It is a practical alternative to higher-order message passing if the descriptors carry the stated information.

### S2: Honest limitations paragraph
The Limitations paragraph (Section 7) states that a "full eigendecomposition" preprocessing step is expensive and that diffusion times and network sizes must be chosen. This is more candid than the efficiency claims in Sections 1 and 5.2, and is useful to readers.

### S3: Evaluation spans three data regimes
The paper reports a controlled expressivity test (Table 2), a scalability test (Fig. 6) and four real tasks (Table 3: MolHIV, PROTEIN, Glycose, Immunogenicity). Reporting mean ± std in Table 3 is better than many method papers.

## Weaknesses
### W1: The expressivity theorem (C2) is not proved by the given argument
Theorem 4.1 equates "there exists an invertible orthogonal matrix Π with L′ = ΠLΠ^T" with isomorphism. Orthogonal similarity of symmetric matrices only means equal spectrum (cospectrality); isomorphism needs a *permutation* matrix. Non-isomorphic cospectral graphs, which are rank-1 CCs by Corollary 4.1, are orthogonally similar yet non-isomorphic, so the statement is false as written. Step 1 of the Theorem 4.3 proof sketch ("non-isomorphic … then their Laplacians L and L′ are not similar") has the same flaw. The appendix proof of Theorem 8.3 only shows that K_t is determined by L (the wrong direction) and never shows that different Laplacians give different descriptors. Corollary 4.3 then applies universal approximation to descriptors that are ten scalars per node at fixed times, without addressing permutation invariance over the node set.
- **Suggested Fix**: Restrict C2 to what is proved (e.g., separation of specific CC families with a rigorous proof), or add the missing assumptions; cite known limits of spectral invariants. Cost: theory work, no GPU.

### W2: The real-data experiments do not test the topological claims, and key controls are missing
By Corollary 4.1, MolHIV and PROTEIN (graphs) and the simplicial Gifflar sets reduce to a rescaled graph Laplacian plus, for Gifflar, small cells. The Table 3 results therefore mostly measure "HKS features + transformer" versus message passing. No row isolates the descriptor: transformer without HKS, transformer with Laplacian-eigenvector or random-walk encodings, or HKS from the Hodge Laplacian. Section 5.1 states "An important note is that this only works with the CC Laplacian and not with the Hodge Laplacian" but reports no number. The MLP-Mixer claim ("comparable or superior performance", Section 3.3) has no numbers, and Section 5.4 is titled "GIFFLAR with MLP Mixer" without saying which backbone produced which cell of Table 3.
- **Suggested Fix**: Add an ablation table (no HKS / Laplacian-eigenvector PE / Hodge-HKS / CC-HKS; Transformer vs Mixer; d and time grid), 5 seeds each. Roughly 4 settings × 4 datasets × 5 seeds × ~3 h ≈ 240 GPU-hours at the stated run lengths.

### W3: The expressivity benchmark is self-built, ambiguous and circular
Section 5.1: "We created a new dataset to prove that we also outperform SMCN in terms of expressivity." The pairs differ by one rank-4 cell, which Section 6 says SMCN cannot see ("SMCN can only distinguish CC up to rank 3"), so the failure of SMCN is by construction. A trivial baseline (counting, per node, the incident cells of each rank) would also separate them. The metric is undefined: Fig. 5a/Table 2 give "Distinguished Pairs 223" and "Accuracy 0%" for SMCN and CIN, but chance for a two-class pair task would be 50%, not 0%. Dataset size, split, what is trained and tested, and the model's feature set are not given.
- **Suggested Fix**: Define the task and metric; add a degree-by-rank counting baseline and a rank-labelled hypergraph baseline; report on more than one construction.

### W4: Gains are small relative to the noise shown, and the SOTA wording is not supported
Table 3: MolHIV 83.1 ± 1.3 vs 81.16 ± 0.90 (SMCN), +1.94 (derived), about 1.5 TopoHKS std; PROTEIN 79.2 ± 1.0 vs CIN 77 ± 4.2, +2.2 (derived), inside CIN's std; Glycose 0.90 vs 0.90 (tie); Immunogenicity 0.84 vs SMCN 0.85 (lower). Yet Section 1 says "state-of-the-art results" and Section 5.3 says the method "outperforms the state-of-the-art topological methods and graph neural networks" while the Abstract says "competitive". The number of runs is not stated. The MolHIV column is labelled "ACC" although the metric usually reported on this dataset is ROC-AUC (accuracy is uninformative at ~3% positives); the label should be checked. Stronger MolHIV baselines (graph transformers with spectral encodings) are absent. CIN "failed to learn" on two datasets (Table 3 caption), which suggests the baseline was not tuned.
- **Suggested Fix**: State runs and metric; add paired tests or at least 10 seeds; add graph-transformer baselines; align wording with the evidence.

### W5: Efficiency claims (C4) are not measured in a comparable way
Table 3 mixes seconds and iterations per second in one "speed" column; it is not stated whether the eigendecomposition is included, nor whether training or inference is timed (Fig. 6 says "Inference timing", the axis says "Iterations per Second"). Section 5.2: "our method maintains a constant computational footprint regardless of complex size", measured only for 4 to 100 cells, contradicts the Limitations paragraph (expensive full eigendecomposition). "On average, it is approximately 12 times faster than SMCN" cannot be reproduced from Table 3: ratios are 3.1/0.65 = 4.8 (MolHIV), 2.8/0.3 = 9.3 (PROTEIN), 4.1/3.2 = 1.28 (Glycose), 4.0/3.3 = 1.21 (Immunogenicity), mean 4.15 (all derived); Table 2 gives 95/7 = 13.6 and Fig. 5a 100/10 = 10. Table 1 also marks SMCN scalable (SC ✓) whereas Section 5.2 says it "fails to scale beyond 50 cells".
- **Suggested Fix**: Report preprocessing + forward time separately, in one unit, on graphs of 10²–10⁵ nodes; fix the Table 1 row and the "12 times" sentence.

### W6: Reproducibility gaps
No network sizes, optimiser, learning rate, epochs, selection rule, or baseline provenance (copied from [5], [6], [18] or re-run). "Training took approximately 1 to 5 hours" yet "6,000 GPU hours" were consumed, i.e. on the order of thousands of runs, which is unexplained and raises the question of how much search went into the reported configuration. Code only "after acceptance".
- **Suggested Fix**: Add a hyperparameter table and search protocol (on validation only), and an anonymised code link.

**Minor**: equation and figure references do not match (Section 4.1 cites "Eq. (10)" and "Eq. (11)" for Eq. 7–8; Lemma 4.1 cites "Fig. 7" for Fig. 4; Section 3 points to "Section 4.2" for computational benefits, but 4.2 only treats expressiveness); typos in Table 3 caption ("Immuginicity", "Immogenicity").

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | Theorem 4.1 (Eq. 6); Section 4.2 step 1; Theorem 8.3 proof | "there exists an invertible orthogonal matrix" | Orthogonal similarity ≠ isomorphism (needs a permutation); cospectral non-isomorphic graphs are counterexamples; Thm 8.3 proves only that L determines K_t | Cross-referenced Eq. 6, Step 1 of Thm 4.3, Thm 8.3 | High | MAJOR | Correct statement and proof |
| ERR-2 | E1 | Section 5.2 vs Table 3 | "approximately 12 times faster than SMCN" | Table 3 ratios average 4.15 | Recomputed from Table 3 | High | MAJOR | State which measurements give 12× |
| ERR-3 | E6 | Table 1 vs Section 5.2 | "SMCN fails to scale beyond 50 cells" | Table 1 marks SMCN as scalable | Cross-referenced | Medium (Table 1 read from extracted text) | MINOR | Fix Table 1 |
| ERR-4 | E1 | Section 1 item 3 / Section 5.3 vs Abstract / Table 3 | "achieves state-of-the-art results on molecular prediction benchmarks" | Abstract says "competitive"; Table 3 shows a tie and a loss on the Gifflar sets | Cross-referenced, Table 3 | High | MAJOR | Align claims |

### Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Permutation-invariant, efficient CC embedding | §1, §3 | Eq. 2–5 (invariance not shown; Def. 2.3 sign convention ambiguous; see R2-W1) | Partially |
| C2 | Maximally expressive, distinguishes arbitrary non-isomorphic CCs | Abstract, §4.2 | Thm 4.3, Cor 4.3, Table 2 | Unsupported (proof flawed) |
| C3 | State of the art on MolHIV, PROTEIN, topological sets | §1, §5 | Tables 2–3 | Partially (competitive, within noise) |
| C4 | Scales efficiently to large CCs | §1, §5.2 | Fig. 6 (≤100 cells), Table 3 timing | Partially / unsupported for "large" |

## Missing References
Not my focus (see Reviewer 2).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Flawed proof of the main theorem; no ablation isolating the descriptor |
| Clarity | 2 | Inconsistent references and units; several definitions ambiguous |
| Significance | 1 | If the claims held, relevant; currently unsupported |
| Originality | 2 | Heat kernel signature on a rank-weighted Laplacian is a modest variation |

## Dimension Scores (0–100)
**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline theorem is not proved as stated, and the only support for the topological claim is a self-built dataset that the baseline cannot see by design.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 32 | Developing | ERR-1; no isomorphism argument that survives cospectral graphs |
| Clarity & Presentation | 45 | Developing | Broken cross-references, mixed units |
| Novelty & Originality | 48 | Developing | HKS on a hypergraph-like operator |
| Significance & Impact | 42 | Developing | Unproven expressivity; benchmark gains within noise |
| Experimental Validation | 36 | Developing | No ablation, tiny scalability range, undefined torus metric |
| Reproducibility | 38 | Developing | No hyperparameters, code deferred, baseline provenance unstated |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations paragraph present |

## Questions for Authors
1. Do Tables 2–3 use the same transformer for all rows of TopoHKS? Which backbone gives each Table 3 cell? A table with and without HKS would raise my score.
2. What exactly is "accuracy" in Fig. 5a/Table 2, and why is 0% (below chance) reported for SMCN and CIN?
3. Is the eigendecomposition included in the timings of Table 3 and Fig. 6? A "no" would lower my view of C4.
4. How many runs underlie Table 3, and was the configuration chosen on the validation split?
5. Are the MolHIV numbers ROC-AUC, as is usual for this dataset?

## Limitations Assessment
**Partially.** The Limitations paragraph (Section 7) is honest about preprocessing cost; it does not mention the expressivity limits of spectral descriptors or the ambiguity in Definition 2.3.

## Ethics Review Flag
**No**: no human data or deployment risk.

## Overall Score
**2**: Reject. The main theoretical claim is not proved, and the empirical evidence neither isolates the descriptor nor clears the noise on most benchmarks.

## Confidence
**4**: I checked the proofs and recomputed the tables; Fig. 4–7 were not visible.

---

# Peer Review Report

## Paper: Heat Kernel Goes Topological
## Reviewer: Prof. Anaïs Ravelo-Tan, Reviewer 2 (Domain) (research university, Southeast Asia; fictional persona)
## Expertise: hypergraph and simplicial Laplacians; topological deep learning
## Date: 2026-11-10

## Summary
The paper proposes a single operator on rank-0 cells of a combinatorial complex, built from incidence matrices from rank 0 to every rank i, weighted by constants with distinct subset sums (Definition 3.1, Eq. 2). It argues this is more informative than the Hodge Laplacian on CCs (Lemma 4.1, Corollary 4.2), and uses the heat kernel diagonal as a node descriptor. The positioning is against higher-order message-passing networks (CIN, SMCN, TopNetX).

## Strengths
### S1: A sensible question
Asking whether pre-computed diffusion descriptors can replace costly higher-order message passing (Section 1) is timely given the scalability problems of SMCN [6] noted in Section 5.2.
### S2: Heat kernel signatures are a well-motivated descriptor family
HKS [10] is multi-scale and isometry-invariant in the manifold setting, and the paper links small t to local and large t to global structure (Section 3.2, Fig. 1 caption).
### S3: The Hodge-blind-spot observation is real
Lemma 4.1's point that a Hodge Laplacian built from consecutive-rank boundaries does not see a cell with no neighbouring ranks is correct in the setting the paper defines.

## Weaknesses
### W1: Definition 2.3 / Eq. 2 do not define a canonical operator
Definition 2.3 sets δ_k(x, y) = ±1 and says that for each cell y "there exists exactly one" x_i with +1 and all other incident rank-0 cells −1. Which node gets +1 is not specified. This matters: take rank-0 cells 1–4 with two rank-2 cells y1 = {1,2,3}, y2 = {2,3,4} and unit weight. Columns v1 = (1, −1, −1, 0). Choosing the +1 at node 2 for y2 gives v2 = (0, 1, −1, −1), v1·v2 = 0, and ‖L‖_F² = 9 + 9 + 2·0 = 18. Choosing it at node 4 gives v2′ = (0, −1, −1, 1), v1·v2′ = 2, and ‖L‖_F² = 9 + 9 + 2·4 = 26. Different spectra, hence different heat kernels, for the *same* complex (all derived by hand). So L, the HKS and the "uniqueness" of Theorem 4.1 depend on an arbitrary convention, and the claimed permutation invariance (C1) is not established.
- **Suggested Fix**: Specify a canonical symmetric construction (for example a hypergraph-style clique or star expansion that is invariant by definition) and re-prove the properties for it.

### W2: Theorem 4.2 (smoothness) is false for cells with three or more nodes
Section 4.1 says f^T L f "expresses the smoothness" and equals B·Σ w_ij (f_i − f_j)² (Eq. 7–8). With the columns of Definition 2.3, f^T L f = Σ_y b_{rk(y)} (f_a − Σ_{j≠a} f_j)². For the constant function f ≡ 1 and a cell of size m this gives (2 − m)², which is nonzero for m ≥ 3, whereas a Dirichlet energy must vanish on constants. The appendix proof (Theorem 8.2) starts from "L_ij = −w_ij … L_ii = Σ_k w_ik", i.e. it assumes L is a weighted graph Laplacian, which is not derived from Definition 3.1. The positive-definiteness desideratum stated in Section 3.1 ("symmetric and positive definite") also conflicts with the requirement that L extend the graph Laplacian, which is singular.
- **Suggested Fix**: Derive the quadratic form from Definition 3.1, or change the definition so that constants lie in the kernel.

### W3: The comparison with the Hodge Laplacian is a straw man
Lemma 4.1 / Corollary 4.2 compare a Hodge Laplacian Δ_k acting on k-cochains with an operator on rank-0 cells that is allowed to use incidences from rank 0 to *any* rank. Operators built from incidences between non-consecutive ranks (rank-to-rank neighbourhood or up/down Laplacian matrices, which I believe the CC literature of [4] allows [verify]) would plausibly also see the rank-4 cell; the paper does not compare with them. The counterexample's cell structure (which rank-0 cells the rank-4 cell contains) is not stated in the text (Fig. 4 not visible). Corollary 4.2's second half, equal expressiveness on simplicial complexes, is asserted ("the Hodge Laplacian captures all valid interactions") without argument; Δ_0 of a simplicial complex ignores 2-simplices, whereas L includes δ_2.
- **Suggested Fix**: Compare against rank-to-rank up/down Laplacians of [4] and against hypergraph Laplacians, with a stated membership of the rank-4 cell.

### W4: Related work omits the closest operator-level and encoding-level literature
Definition 3.1 is a rank-weighted sum of node-membership outer products, i.e. an operator on a hypergraph with rank-dependent weights. Hypergraph Laplacians and hypergraph neural networks are not discussed. Spectral and diffusion-based positional or structural encodings for graph transformers, the natural baselines for "HKS + transformer", are absent (Section 6 covers only spectral embeddings and message passing). The sentence "its potential for improving GNN expressivity remains unexplored" (Section 6) is therefore doubtful.
- **Suggested Fix**: Add and differentiate these lines of work and compare empirically (see addendum below for verified entries).

### W5: Contribution is narrower than claimed
After W1–W2, what remains is a heat kernel diagonal of a (rank-weighted, hyperedge-expanded) Laplacian on rank-0 cells plus a standard backbone. The use of higher-rank cells enters only through which nodes they contain and a rank weight; Section 4.1's own "Observation" says "L does not change much for higher rank, as their individual contributing weights become smaller", which undercuts the motivation of capturing high-rank cells.
- **Suggested Fix**: State precisely what information about cell-cell structure L can and cannot see.

**Minor**: "Corollary 8.2" is cited in Section 2 before it is defined; Eq. 3 uses Φ^T diag Φ while Theorem 8.3 uses Φ diag Φ^T.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | Definition 2.3 / Eq. 2 | "there exists exactly one" | +1 position unspecified; two choices on one CC give ‖L‖_F² = 18 vs 26 | Derived by hand on a 4-node, 2-cell example | High on arithmetic; Medium on reading of the definition | MAJOR | Canonical convention |
| ERR-2 | E2 | Theorem 4.2 / Eq. 7–8 | "expresses the smoothness of a function" | f ≡ 1 gives (2 − m)² ≠ 0 for cells of size m ≥ 3 | Derived from Def. 2.3 and Eq. 2 | High | MAJOR | Re-derive or change Definition 3.1 |
| ERR-3 | E6 | Section 3.2 vs Definition 3.2 | "Further, we only consider the kernel for cells of rank 1." | Descriptor is defined on rank-0 cells | Cross-referenced | High | MINOR | Fix wording |

## Missing References
*Literature-check addendum below lists verified entries; the pointers here are by line of work.*
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Hypergraph Laplacians and hypergraph neural networks (see addendum) | The operator in Eq. 2 is a hypergraph-type Laplacian |
| Important | Spectral / diffusion positional and structural encodings for graph transformers (see addendum) | Natural controls for "HKS + transformer" |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Definition ambiguous; smoothness theorem false |
| Clarity | 2 | Definitions admit multiple readings |
| Significance | 1 | Depends on unproven claims |
| Originality | 2 | Modest relative to hypergraph Laplacians and spectral encodings |

## Dimension Scores (0–100)
**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the core operator is ill-defined as written and its stated smoothness property fails on a one-line check.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 35 | Developing | ERR-1, ERR-2 |
| Clarity & Presentation | 50 | Developing | Definitions ambiguous but organisation is readable |
| Novelty & Originality | 45 | Developing | Close to hypergraph Laplacian + known HKS |
| Significance & Impact | 42 | Developing | Narrow if claims shrink |
| Experimental Validation | 40 | Developing | Not my focus; no ablation of the operator |
| Reproducibility | 45 | Developing | Definition not canonical |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. Which cell receives +1 in Definition 2.3, and is the descriptor invariant to that choice? A proof would raise my score.
2. Does the rank-4 cell in Fig. 4 contain only cell 3, or other rank-0 cells too?
3. How does L differ from a rank-weighted hypergraph Laplacian on the rank-0 cells?
4. Is positive definiteness (Section 3.1) claimed, given that graphs give a singular L?

## Limitations Assessment
**Partially.** No discussion of what the Laplacian cannot see.

## Ethics Review Flag
**No**.

## Overall Score
**2**: Reject. The central operator is not canonical and a stated property is false; the novelty over hypergraph Laplacians is not argued.

## Confidence
**4**: I tested the definitions by hand; Figures 4/7 were not visible.

---

# Peer Review Report

## Paper: Heat Kernel Goes Topological
## Reviewer: Dr. Priyanka Delacroix-Nair, Reviewer 3 (Perspective) (computational geometry group; fictional persona)
## Expertise: spectral shape analysis; signal processing on graphs
## Date: 2026-11-10

## Summary
The paper brings the heat kernel signature, a workhorse of non-rigid shape matching, to combinatorial complexes, and feeds it to sequence models as a pre-computed structural descriptor, aiming to avoid higher-order message passing. It claims full expressivity, strong scalability and competitive molecular results. I read it as an attempt to transfer a mature spectral idea into topological deep learning, which I find attractive.

## Strengths
### S1: A good transfer of an established idea
HKS has a long record of use as a compact multi-scale local descriptor (Section 3.2 cites [10], [59]–[63]). Moving it to cells of a CC, and keeping the heavy computation in a one-off preprocessing step, is a sensible engineering split.
### S2: Multi-scale design with a small number of times
The descriptor uses d = 10 times between 0 and 3 (Section 5). This gives a compact, fixed-length vector that pairs naturally with transformers or MLP-Mixers and avoids sign ambiguity of eigenvectors, because the diagonal of exp(−tL) is basis-independent.
### S3: A natural bridge for other domains
Glycan data (Section 5.4) is a good example of naturally higher-order structure; the idea could extend to meshes, molecules and brain-network data named in the Social Impact paragraph.

## Weaknesses
### W1: In shape analysis, HKS is known to be informative only up to its limits, and the paper does not discuss them
The descriptor is the diagonal of the heat kernel, the return probability at a node. In shape analysis the community moved to scale-invariant, wave-kernel and pair-wise variants because the diagonal alone loses information; for graphs, highly symmetric (walk-regular) graphs give the same diagonal at every node, and cospectral graphs share the heat trace. The claim "maximally expressive" (Abstract; Corollary 4.3) cannot be reconciled with this experience, and the paper does not discuss spectral limits at all.
- **Suggested Fix**: Discuss the limits; consider off-diagonal kernel entries K_t(c, c′), wave-kernel signatures (cited as [63]) or learnable times (named in Future Work).

### W2: The claimed sensitivity to high-rank cells conflicts with the weight choice
Section 3.1 uses weights with distinct subset sums such as {2⁻¹, …, 2⁻ⁿ}, and Section 4.1 notes that L "does not change much for higher rank". With the example weights, a rank-4 cell then carries 2⁻⁴ = 1/16 against 1/2 for rank 1, i.e. one eighth of the weight of a rank-1 cell. With ten diffusion times and finite precision, small rank-4 effects may be numerically weak, and the exact-distinctness argument (distinct subset sums) is about exact arithmetic, not about a trained network reading ten floats.
- **Suggested Fix**: Report the actual gap in HKS values for the Table 2 pairs, and test the sensitivity to the weight sequence and noise.

### W3: Scalability and deployment are asserted rather than analysed
Section 7 admits a "full eigendecomposition" per complex, which is cubic in the number of rank-0 cells, while Section 5.2 claims a "constant computational footprint". Practical alternatives (partial spectra, Chebyshev or Krylov approximations of exp(−tL), stochastic estimation of the diagonal) are not discussed. Data of the size where higher-order models struggle (Fig. 6 stops at 100 cells) is not tested.
- **Suggested Fix**: Add a complexity statement and a timing study on 10³–10⁵ nodes with an approximate heat-kernel diagonal.

### W4: Assumption that rank labels are meaningful and given
The method assumes each cell has a trustworthy rank and that the user supplies the CC; on molecular graphs no higher-rank cell is used (MolHIV and PROTEIN are graphs), so the experiments say little about how the rank labelling would be chosen in practice. The broader-impact paragraph (Conclusion) names drug design, brain modelling and quantum systems without any evidence.
- **Suggested Fix**: Add a case where rank structure comes from domain knowledge (e.g. rings in molecules, glycan motifs) and measure whether it helps.

**Minor**: Future-work items (learned times, dynamic complexes, self-supervision) would be strengthened by a first small experiment.

### Error Log
No concrete errors beyond those found by Reviewers 1 and 2.

## Missing References
Not my focus; see Reviewer 2. A cross-disciplinary pointer: approximations of the heat kernel by polynomial or Krylov methods in graph signal processing.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good intuition; the expressivity claim and scalability study are weak |
| Clarity | 2 | Readable idea, many loose ends |
| Significance | 2 | Could matter for cheap higher-order features |
| Originality | 2 | Transfer of known idea; partly new operator |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a promising and cheap idea with a clear story, but the evidence for the main claims is thin and below what accepted papers on this topic offer.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 45 | Developing | I did not check every proof; the expressivity claim is at odds with spectral experience |
| Clarity & Presentation | 52 | Competent | Story is clear |
| Novelty & Originality | 52 | Competent | Transfer plus a new operator |
| Significance & Impact | 50 | Developing | Real potential, not shown |
| Experimental Validation | 45 | Developing | Few settings, no ablation |
| Reproducibility | 48 | Developing | Code after acceptance |
| Ethical Compliance | 62 | Competent | Boilerplate impact statement; nothing at stake |

## Questions for Authors
1. What happens to the HKS gap between the Table 2 pairs as t varies? A plot would raise my score.
2. Can the diagonal be approximated without a full eigendecomposition, and what accuracy is lost?
3. Which real data would really benefit from rank ≥ 3 cells?

## Limitations Assessment
**Partially.** Preprocessing cost is acknowledged; spectral limits are not.

## Ethics Review Flag
**No**.

## Overall Score
**3**: Borderline Reject. An appealing transfer of a classical descriptor whose theory and evidence are not yet at the bar.

## Confidence
**3**: I am a spectral-geometry reviewer, not a topological deep learning specialist; I did not check every proof.

---

# Peer Review Report

## Paper: Heat Kernel Goes Topological
## Reviewer: Dr. Mateo Sorensen-Ikeda, Reviewer 4 (Generalist) (university; fictional persona)
## Expertise: representation learning for structured data
## Date: 2026-11-10

## Summary
The paper proposes to replace higher-order message passing on combinatorial complexes by (i) a new Laplacian on rank-0 cells, (ii) heat kernel signatures at ten times as node descriptors, and (iii) a transformer or MLP-Mixer. In one paragraph: a pre-computed spectral descriptor makes topological learning cheaper, is claimed to be maximally expressive, and gives competitive molecular and glycan results at much lower cost.

## Strengths
### S1: The topic fits ICLR
Topological deep learning and expressivity have appeared at ICLR recently (the closest work, [6], is an ICLR 2025 paper), so the audience exists.
### S2: Accessible high-level story
Fig. 1–3 captions and Section 3 give a story a non-specialist can follow: local structure at small t, global at large t, then a standard sequence model.
### S3: Candid limitations and compute statement
Section 7 and Section 5 give hardware and the preprocessing limitation.

## Weaknesses
### W1: Claims are inconsistent across the paper
The Abstract says "competitive performance with the state-of-the-art descriptors", Section 1 says "state-of-the-art results", Section 5.3 says the method "outperforms the state-of-the-art topological methods and graph neural networks", but Table 3 shows a tie on Glycose and a lower score on Immunogenicity (0.84 vs 0.85). The Abstract says the representations are "permutation-equivariant", Section 1 item 1 says "permutation-invariant". Table 1 gives TopoHKS a check on every property including "Isomorphism", while the evidence for that is Theorem 4.3, whose proof is only a sketch.
- **Suggested Fix**: One consistent, evidence-matched statement of each claim.

### W2: The theory is presented as sketches and may not hold
Section 4.1 introduces Theorem 4.1 with "The proof closely follows the following line of thought" and the full proofs in the appendix are largely verbal. Theorem 4.1 mentions an "invertible orthogonal matrix" where a permutation would be expected; Corollary 4.3 argues from universal approximation in two sentences. As a non-specialist I cannot confirm these, and the other reviewers' checks matter here; I am not able to vouch that "maximally expressive" is justified.
- **Suggested Fix**: Move the key proof steps into the main text with their assumptions, or weaken the claim.

### W3: The evidence for the main message is narrow
The expressivity evidence is one author-built torus dataset; the real-data tables show moderate gains without ablation (Table 3). I would want to see what the HKS adds over a transformer alone and over standard positional encodings. Section 3.3's MLP-Mixer discussion has no numbers.
- **Suggested Fix**: Ablation table and a second expressivity dataset from an external source.

### W4: Presentation and cross-referencing
Equations and figures are cited with the wrong numbers (Section 4.1 uses "Eq. (10)" and "Eq. (11)" for Eq. 7–8; Lemma 4.1 refers to "Fig. 7"; Section 3 refers to Section 4.2 for "computational benefits", which Section 4.2 does not treat). Table 3 mixes seconds and iterations per second. "Corollary 8.2" appears in Section 2 before it exists. The paper does not read as a finished submission.
- **Suggested Fix**: Proofread and unify numbering and units.

**Minor**: typos "Immuginicity" and "Immogenicity" (Table 3 caption); "MolHIV" metric labelled ACC.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Not met | §4.2, Table 2 |
| Soundness: experiments isolate the contribution | Not met | Table 3, no ablation |
| Presentation: clear and consistent | Partly | cross-reference and unit issues |
| Contribution: a new, useful idea for the ICLR audience | Partly | cheap spectral descriptor; narrow |
| Honest limitations | Partly | §7 |

### Error Log
Concrete errors are reported under W1 and W4 with locations; no independent audit was run.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory not convincing; experiments thin |
| Clarity | 2 | Inconsistent claims and references |
| Significance | 2 | Narrow, potentially useful |
| Originality | 2 | Moderate |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting direction at the right venue, but inconsistent claims and an unfinished-looking theory section.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Cannot confirm proofs; red flags |
| Clarity & Presentation | 45 | Developing | Inconsistent claims, numbering, units |
| Novelty & Originality | 52 | Competent | New operator and combination |
| Significance & Impact | 50 | Developing | Potentially useful |
| Experimental Validation | 46 | Developing | No ablation |
| Reproducibility | 45 | Developing | Details missing |
| Ethical Compliance | 58 | Competent | Boilerplate |

## Questions for Authors
1. Which of "competitive" and "state-of-the-art" do you stand behind, and on what rows of Table 3?
2. Is the representation permutation-invariant or equivariant, and where is it shown?
3. What does HKS add over the plain transformer?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**.

## Overall Score
**3**: Borderline Reject. A relevant idea; as submitted, the claims run ahead of the evidence and the exposition needs substantial work.

## Confidence
**3**: Generalist read; I did not rederive the proofs.

---

# Devil's Advocate Report

## Paper: Heat Kernel Goes Topological
## Reviewer: Prof. Yusra Haldane-Okafor, Devil's Advocate (statistics department; fictional persona)

---

## Steelman
A cheap spectral descriptor computed once per complex can replace expensive higher-order message passing. Because the Laplacian aggregates incidences of every rank into one operator, its heat kernel sees structure that Hodge-based and rank-limited methods miss, which is shown on a hand-built torus pair set and not contradicted by the molecular results.

---

## Core Argument Chain
1. A rank-weighted Laplacian L on rank-0 cells is canonical and uniquely determined by the CC (Def. 3.1, Thm 4.1).
2. Non-isomorphic CCs have non-orthogonally-similar Laplacians (Thm 4.1, step 1 of Thm 4.3).
3. Non-similar Laplacians give different HKS descriptors (Thm 4.3 / 8.3).
4. A universal approximator can separate distinct descriptors (Cor. 4.3).
5. SMCN/CIN fail on a rank-4 torus set while TopoHKS separates it (Table 2, Fig. 5a); TopoHKS is faster and competitive on real data (Fig. 6, Table 3).
∴ TopoHKS is "maximally expressive", efficient and state of the art for topological learning.

---

## Strongest Counter-Argument
Premise 2 is false, and it is false inside the paper's own scope. By Corollary 4.1, graphs are rank-1 CCs and L is a rescaled graph Laplacian. There are non-isomorphic graphs that are cospectral, and orthogonal similarity of two symmetric matrices only means they share a spectrum, not that a permutation relates them (Theorem 4.1, Eq. 6). Worse for the claim, there are non-isomorphic graphs with *identical heat kernel diagonals at every node and every time*: two strongly regular graphs with the same parameters, for instance the 4×4 rook's graph and the Shrikhande graph (both srg(16,6,2,2)). In a strongly regular graph all powers of A lie in span{I, A, J}, so every closed-walk count at every node depends only on the parameters, and K_t(c) is the same for all c, for all t, in both graphs. TopoHKS descriptors are then identical, and the downstream function approximator cannot separate them, whatever its capacity. So Theorem 4.3, Corollary 4.3 and the abstract's "maximally expressive … distinguish arbitrary non-isomorphic CCs" are contradicted by a rank-1 example, and "we can determine any WL classes by theoretical design" (Cor. 4.3) is not meaningful as stated. A second gap: the corollary needs infinitely many times to recover a spectrum, yet d = 10 is used.

The remaining empirical story cannot rescue the claim. The torus test (Section 5.1) is a dataset the authors built so that the pairs differ in a rank-4 cell, which the baseline SMCN is described as unable to see; any feature that counts incident cells by rank would separate it. Real-data tables use graphs where, by Corollary 4.1, no higher-order information exists, and no ablation isolates HKS from the transformer.

---

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Logic / Evidence | Abstract; Section 1 item 2; Theorem 4.1, Theorem 4.3 (8.3), Corollary 4.3 | The headline expressivity claim ("maximally expressive", "distinguish arbitrary non-isomorphic CCs") is contradicted by rank-1 counterexamples (cospectral graphs; srg(16,6,2,2) pairs have identical per-node heat kernel diagonals). The proofs conflate orthogonal similarity with isomorphism and prove only that L determines K_t. Evidence contradicts the claim (criterion 1), not merely a narrower reading: a proved-false theorem is the paper's main theoretical contribution. | Withdraw the claim; replace with a correct, restricted statement and proof (e.g., separation of defined CC families); redo Table 1's "Isomorphism" column | New theory / redesign of the claim and Laplacian (not clarification only) |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic | Definition 2.3, Eq. 2, Theorem 4.2 | The Laplacian depends on an unspecified +1 position (two valid choices on the same CC give different ‖L‖_F², 18 vs 26, derived for cells {1,2,3}, {2,3,4}); f ≡ 1 has nonzero "Dirichlet energy" for cells of size ≥ 3, contradicting Theorem 4.2. | Specify a canonical operator, re-prove its properties |
| DA-M2 | Evidence | Section 5.1, Table 2, Fig. 5a | Circular expressivity test: pairs built to differ in a rank-4 cell, SMCN limited to rank 3 by the authors' own account; metric "accuracy 0%" undefined (below chance); no trivial baseline. | Define metric; add rank-count baseline; external datasets |
| DA-M3 | Claim distortion (E5) | Abstract, §1 item 3 and 4, §5.2, §5.3 | "state-of-the-art", "scales efficiently", "constant computational footprint", "12 times faster" are not supported as worded (tie/loss on Gifflar; ≤100 cells; average 4.15× from Table 3). | Align wording with evidence |
| DA-M4 | Alternative explanation | Table 3, Section 3.3 | No control separates HKS from the transformer/MLP-Mixer, the sin/cos feature map O = sin(XG) cos(XG) (G unspecified), or hyperparameter search ("6,000 GPU hours"). At small t, K_t(c) ≈ 1 − t·L_cc is essentially a weighted-degree feature. | Ablations with 5+ seeds |
| DA-M5 | Straw man | Lemma 4.1, Corollary 4.2 | The Hodge Laplacian is defined with consecutive-rank boundaries only; rank-to-rank CC Laplacians in [4] would see the rank-4 cell. | Compare with rank-to-rank and hypergraph Laplacians |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 1 vs Section 5.2 | SMCN marked scalable (SC ✓) yet "fails to scale beyond 50 cells" |
| DA-m2 | Consistency | Abstract vs Section 1 | "permutation-equivariant" vs "permutation-invariant" |
| DA-m3 | Presentation | Sections 3, 4.1, 4.1 refs | Wrong equation / figure / section cross-references |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Average speed-up over SMCN | "approximately 12 times" (Section 5.2) | Table 3: 4.8, 9.3, 1.28, 1.21 → mean 4.15; Table 2: 95/7 = 13.6; Fig. 5a: 100/10 = 10 | No for Table 3 |
| MolHIV gain over SMCN | 83.1 vs 81.16 | +1.94 (≈ 1.5 × TopoHKS std 1.3) | Gain smaller than noise-scale |
| PROTEIN gain over CIN | 79.2 vs 77 | +2.2 (CIN std 4.2) | Within CIN's std |
| Glycose | 0.90 ± 0.03 vs SMCN 0.90 ± 0.07 | 0.00 | Tie, not "outperform" |

## Ignored Alternative Explanations
Benefit from the transformer backbone or the sin/cos feature map rather than HKS; degree-like information at small t; a larger or more heavily searched configuration (6,000 GPU hours) than baselines; baselines copied from other papers under different splits; for Table 2, trivially separable pairs.

## Missing Stakeholder Perspectives
Practitioners with large complexes (the paper's own limitation excludes 10⁶ cells); drug-design users, since the broader-impact paragraph names applications that are not evaluated.

## Observations (Non-Defects)
The Limitations paragraph is candid. Mean ± std is reported in Table 3. The Hodge-blindness observation of Lemma 4.1 is correct in the restricted setting. The choice of a basis-free diagonal avoids eigenvector sign ambiguity.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 30 | Main theorem false; operator ambiguous |
| Clarity & Presentation | 45 | Inconsistent claims, references |
| Novelty & Originality | 45 | Operator differs only by rank weights from hypergraph-type Laplacians |
| Significance & Impact | 40 | Depends on claims that fail |
| Experimental Validation | 35 | Circular expressivity test, no ablation |
| Reproducibility | 40 | No hyperparameters, code after acceptance |
| Ethical Compliance | 60 | Nothing at stake |

**Pool position:** better than about 25% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper's headline theorem is disproved by a rank-1 example and the empirical support does not isolate the method.

## Overall: 2 | Confidence: 4


---

# Phase 1.5: Literature Check (strict, cutoff 2025-09-24)

*Mode `strict`; arXiv API through `scripts/related_search.py`; 11 of 12 queries used (9 claim: C1 ×3, C2 ×4, C3 ×1, C4 ×1; 1 baseline; 1 expansion). Two over-long queries were refused and not counted. Everything after the cutoff is dropped. 51 unique results kept; none was the reviewed paper (fingerprint: title and method name only; no authors visible). The search covers arXiv abstracts only. Gaps left open: C4 returned only off-topic results ("no close prior work found in this search (arXiv only)", at most medium); `benchmarks` found no external benchmark names in the text, and the MolHIV baseline query kept one irrelevant result, so no baseline scout table can be built from this search.*

## Reviewer 2 literature-check addendum

### Per-claim novelty (from `related_search.py novelty`; verdicts describe what this arXiv search found, not the paper's merit)
| Claim | Dimension | Novelty verdict | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|-----------------|---------------------------------------------|-----------|
| C1 Laplacian on CC rank-0 cells + HKS embeddings | method | medium | NetLSD (level 3; https://arxiv.org/abs/1805.10712v2; prior, arXiv-only 6+ months; **not cited**). Cell Complex Neural Networks (level 2; https://arxiv.org/abs/2010.00743v4; cited as [7]) | NetLSD is a permutation-invariant, scale-adaptive heat-kernel spectral descriptor for graphs; the paper's graph case (Cor. 4.1) overlaps it. The CC-specific part (rank-weighted incidence Laplacian) is new in form but close to hypergraph-type Laplacians (Submodular hypergraphs, level 2, https://arxiv.org/abs/1803.03833v4, peer-reviewed, not cited). |
| C2 maximal expressivity | result | high (search artifact: no prior paper makes this exact claim; the claim is contradicted in review, see DA-C1) | Comparing Graph Transformers via Positional Encodings (level 2; https://arxiv.org/abs/2402.14202v4; peer-reviewed; not cited) | Shared topic: expressivity of positional encodings for transformers. |
| C3 SOTA on MolHIV / PROTEIN / Gifflar | result | high (no matching prior result found) | Molecular topological deep learning for polymer property prediction (level 1; https://arxiv.org/abs/2410.04765v1) | Not a novelty issue; an evidence issue (see R1-W4). |
| C4 scalable | result | no close prior work found (arXiv only; at most medium) | none | Search limit, not evidence of novelty. |

**Paper reading (script):** no central claim fully covered by prior work. **Attribution:** closest to the paper as a whole is NetLSD (script), then Cell Complex Neural Networks (similarity cosine 0.282; below the 0.30 high-overlap threshold). **Text overlap:** none (0 shared 8-grams for every kept result). No DA criterion-7 candidate.

### Novelty delta table
| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| Heat-kernel node descriptors as permutation-invariant embeddings (C1) | NetLSD (https://arxiv.org/abs/1805.10712v2) | Heat-kernel-trace graph descriptor, permutation-invariant, scale-adaptive (abstract) | Per-node diagonal at 10 times, on a CC operator, fed to a transformer | No (Section 6 cites only [64] and says HKS "potential for improving GNN expressivity remains unexplored") |
| CC Laplacian (C1) | Hypergraph Laplacian literature (e.g. https://arxiv.org/abs/1803.03833v4) | Laplacians on hyperedge structures with spectral analysis | Rank-dependent weights b_i; rank-0 restriction | No |
| Expressivity via descriptors + UFA (C2) | https://arxiv.org/abs/2402.14202v4 | Relates positional-encoding choice to transformer distinguishing power | Claim of full distinguishing power (not supported) | No |

### Baseline scout
No usable rows (see note above). Only prior (peer-reviewed or 6+ month arXiv) work can be a missing required baseline: the graph-transformer baselines in the next list satisfy this.

### Field snapshot (kept results only)
Topological deep learning began with message passing on simplicial and cell complexes and the combinatorial-complex formalism (2020–2022), then moved to unification frameworks and benchmarks (e.g. a framework for generalized CC networks, 2024) and to expressivity analyses. In parallel, graph transformers with positional and structural encodings (spectral attention, learnable structural/positional representations, a "recipe" for scalable graph transformers, and 2024 comparison and benchmarking studies of encodings) became the standard cheap way to inject structure. Open problems stated in the kept abstracts: standardised evaluation, expressivity versus scalability, and which encodings add power. For a paper offering pre-computed spectral features as a substitute for higher-order message passing, a significant contribution would show a correct separation result *and* gains over strong encoding-equipped transformers at equal or lower cost; a rank-4 toy set and +1 to +2 points on MolHIV are incremental by that standard.

### Missing references (each checked with `related_search.py verify`)
| Priority | Reference | Link / status | Why it matters |
|----------|-----------|---------------|----------------|
| Important | Tsitsulin, Mottin, Karras, Bronstein, Müller. NetLSD: Hearing the Shape of a Graph. KDD 2018 | https://arxiv.org/abs/1805.10712v2 (found) | Heat-kernel spectral descriptor for graphs; relevant to Section 6's claim |
| Important | Kreuzer, Beaini, Hamilton, Létourneau, Tossou. Rethinking Graph Transformers with Spectral Attention. NeurIPS 2021 | https://arxiv.org/abs/2106.03893v3 (found) | Spectral encodings for transformers: control for "HKS + transformer" |
| Important | Rampášek, Galkin, Dwivedi, Luu, Wolf, Beaini. Recipe for a General, Powerful, Scalable Graph Transformer. NeurIPS 2022 | https://arxiv.org/abs/2205.12454v4 (found) | Standard strong MolHIV-style baseline family |
| Important | Dwivedi, Luu, Laurent, Bengio, Bresson. Graph Neural Networks with Learnable Structural and Positional Representations. ICLR 2022 | https://arxiv.org/abs/2110.07875v2 (found) | Learnable structural/positional encodings; also bears on the "learned times" future work |
| Important | Black et al. Comparing Graph Transformers via Positional Encodings. ICML 2024 | https://arxiv.org/abs/2402.14202v4 (found) | Expressivity of encodings for transformers |
| Important | Feng, You, Zhang, Ji, Gao. Hypergraph Neural Networks. AAAI 2019 | https://arxiv.org/abs/1809.09401v3 (found) | Hypergraph operators; closest relative of Eq. 2 |
| Important | Zhou, Huang, Schölkopf. Learning with Hypergraphs: Clustering, Classification, and Embedding. NeurIPS 2006 | **[verify]** not found on arXiv by title; I am confident it exists | Classical hypergraph Laplacian |
| Helpful | Lim, Robinson, Zhao, Smidt, Sra, Maron, Jegelka. Sign and Basis Invariant Networks for Spectral Graph Representation Learning. ICLR 2023 | https://arxiv.org/abs/2202.13013v4 (found) | Eigenvector ambiguity vs the paper's diagonal-only choice |

No result labelled recent, concurrent or newer is used as a weakness; two concurrent results (a TDL-in-molecular-sciences review, 2025-09-21, and one hypergraph network, 2025-08-16) are "worth discussing" only.

---

# Phase 1.6: Report Check (Editorial Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | W3 (Hodge straw man): claim that [4], [36], [43] define rank-to-rank Laplacians | **Rewritten** | The kept abstracts of [7] and TopoTune do not state this; hedged and marked `[verify]` in the report; the weakness stays as "no comparison with rank-to-rank / hypergraph operators" |
| R3 | W1: "cospectral … graphs give identical diagonals" | **Rewritten** | Test 3 (consistent): cospectral graphs share the heat trace, not necessarily per-node diagonals; narrowed to walk-regular graphs |
| R1 | W4: MolHIV "ACC" label | Kept (as a request to check, and moved into Questions 5) | Not a verified error; the metric of OGB MolHIV is commonly ROC-AUC, so it stays a question |
| R4 | W1: Table 1 "Isomorphism" check | Kept | Table 1 read from extracted text; consistent with line "TopoHKS (ours) ✓ ✓ ✓ ✓" |
| R1, R2, R3, R4, DA | Typos, cross-reference numbering | Moved to one Minor line each | Cosmetic |
| R1, R2, DA | All other weaknesses | Kept | Specific, located, not answered in the paper (full-text search; no supplement exists), consistent, actionable |

Scores were not changed. Hard Rule 9: integrity scan clean.

# Phase 2: Synthesizer Part A (package for the EIC)

**Master issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Expressivity theorem not proved / false (Thm 4.1, 4.3, Cor 4.3; Abstract) | R1-W1, R3-W1, R4-W2, DA-C1 | **DA-CRITICAL**; also CONSENSUS-4 |
| Operator not canonical (Def. 2.3) and smoothness theorem false (Thm 4.2) | R2-W1, R2-W2, DA-M1 | CONSENSUS-2 |
| Torus experiment circular, metric undefined | R1-W3, DA-M2 | CONSENSUS-2 |
| No ablation isolating HKS; missing graph-transformer baselines; gains within noise | R1-W2, R1-W4, R4-W3, DA-M4, R2-W4 | CONSENSUS-4 |
| Claim inconsistency / overclaim (SOTA, scalable, 12×) | R1-W4, R1-W5, R4-W1, DA-M3 | CONSENSUS-3 |
| Efficiency measured inconsistently; ≤100 cells; eigendecomposition | R1-W5, R3-W3 | CONSENSUS-2 |
| Hodge comparison a straw man; hypergraph / PE literature omitted | R2-W3, R2-W4, DA-M5 | CONSENSUS-2 |
| Reproducibility gaps | R1-W6 | SOLO |
| High-rank cells weakly weighted (weights 2⁻ⁱ) | R3-W2, R2-W5 | CONSENSUS-2 |
| Presentation, cross-references | R1, R2, R4-W4, DA-m3 | CONSENSUS-3 (Minor) |

**Hinge issues for the EIC:** DA-C1; operator well-definedness (R2-W1/W2); whether the empirical results isolate the descriptor.

**Official output (run BEFORE EIC weights, DA-C1 provisionally upheld):** official ratings 2, 2, 3, 3, 2 → mean 2.40; official composite 44.8; confidence-only assessment 2.35 → 2 (Reject); composite band 2; DA ceiling 3. No consistency warnings.

---

# Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: Heat Kernel Goes Topological
## Date: 2026-11-10
## Target Venue: ICLR (profile `iclr`) | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Ilse Brandvold; R1 Methodology Dr. Kwabena Osei-Lindqvist, R2 Domain Prof. Anaïs Ravelo-Tan, R3 Perspective Dr. Priyanka Delacroix-Nair, R4 Generalist Dr. Mateo Sorensen-Ikeda, DA Prof. Yusra Haldane-Okafor

---

## Decision: Reject (2). ICLR rating **2** on {0,2,4,6,8,10} (3 on the legacy {1,3,5,6,8,10} scale); scale status `secondary`.

**Official ratings** (shown to authors): R1 2, R2 2, R3 3, R4 3, DA 2 → mean 2.40 · official composite 44.8
**EIC assessment** (internal): weighted rating 2.31 → starting point 2 · weighted composite 44.1 → band 2 (cross-check agrees) · **DA ceiling**: 3 · **Final (EIC)**: 2
**ICLR sub-scores (script):** Soundness 1, Presentation 2, Contribution 2.
**EIC pool position:** better than about 28% of ICLR submissions.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The idea of a pre-computed, basis-independent spectral descriptor in place of higher-order message passing is attractive and cheap, it is at home at ICLR, and the Limitations paragraph is candid. The torus pair set (Table 2) and the timing comparisons (Fig. 5a, Fig. 6, Table 3) are suggestive that rank ≥ 3 information can be injected cheaply.
- **Against acceptance:** The headline theorem (maximal expressivity) is false as stated and its proof conflates orthogonal similarity with isomorphism. The core operator is not canonical as defined (Definition 2.3), and its stated smoothness property fails on the constant function. The empirical evidence does not isolate the descriptor (no ablation, no strong graph-transformer baselines), the expressivity test is built to favour the method, and gains on real data are within the noise shown.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Thm 4.1 equates orthogonal similarity with isomorphism | R1-W1/ERR-1, DA-C1 | Theorem 4.1, Eq. 6; Section 4.2 step 1 | Verified | Statement says "invertible orthogonal matrix"; no permutation constraint. |
| Thm 8.3 proves only that L determines K_t | R1-W1, DA-C1 | Theorem 8.3 proof | Verified | Proof ends "the diffusion pattern is uniquely determined", the forward direction only. |
| Maximal expressivity contradicted by rank-1 examples (srg(16,6,2,2)) | DA-C1 | Abstract; Cor. 4.1; Thm 4.3 | Verified | Rederived: in a strongly regular graph K_t lies in span{I, A, J}, so the diagonal is constant and fixed by the parameters; graphs are CCs per Section 2; L = b₁·L_G by Cor. 4.1. Feature-free descriptors coincide. |
| Def. 2.3 leaves the +1 position unspecified; two choices change ‖L‖_F² (18 vs 26) | R2-W1/ERR-1, DA-M1 | Definition 2.3; Eq. 2; Thm 8.1 proof ("ambiguity … affects all terms consistently") | Verified | Arithmetic reproduced; Thm 8.1's invariance remark is asserted, not shown. |
| f ≡ 1 gives nonzero energy for cells of size ≥ 3 | R2-W2/ERR-2, DA-M1 | Theorem 4.2; Thm 8.2 proof | Verified | The proof assumes L_ij = −w_ij, L_ii = Σ w_ik, not derived from Def. 3.1. |
| "approximately 12 times faster" not reproducible from Table 3 | R1-W5/ERR-2, DA numerical check | Section 5.2; Table 3 | Verified | Mean ratio 4.15 (derived); Table 2 gives 13.6. |
| SOTA wording vs ties/losses | R1-W4/ERR-4, R4-W1, DA-M3 | Abstract; Section 1; Section 5.3; Table 3 | Verified | Glycose tie, Immunogenicity 0.84 < 0.85. |
| Torus metric "accuracy 0%" undefined | R1-W3, DA-M2 | Fig. 5a; Table 2 | Verified (as an omission) | No definition of the task; figures not inspected. |
| Hodge Laplacian is a straw man; [4] defines rank-to-rank Laplacians | R2-W3 | Lemma 4.1; Cor. 4.2 | Partly correct | The comparison is restricted to a single Hodge Δ_k; the claim about [4] is unverified and stays `[verify]`. |
| Rank-4 cell carries 1/8 the weight of rank 1 | R3-W2 | Definition 3.1; Section 4.1 "Observation" | Partly correct | Observation quote verified; the 2⁻ⁱ assignment is only the paper's example. |
| Table 1 marks SMCN scalable vs Section 5.2 | R1 ERR-3, DA-m1 | Table 1; Section 5.2 | Partly correct | Table 1 read from extracted text; cell alignment not guaranteed. |
| Efficiency "constant footprint" vs full eigendecomposition | R1-W5, R3-W3 | Section 5.2; Section 7 | Verified | Both statements are in the paper; Fig. 6 stops at 100 cells (figure not inspected, text says 4 to 100). |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | ERR-1, ERR-2, ERR-4 all verified; recomputations correct; decisive on proof and efficiency claims |
| R2 (Domain) | 2 | 4 | 1.25 | Definition and smoothness errors verified by hand; one prior-work statement had to be hedged (R2-W3) |
| R3 (Perspective) | 3 | 3 | 1.0 | Mostly sound; one statement was narrowed (cospectral clause), 1/8 weight point rests on the paper's example; I did not move the weight |
| R4 (Generalist) | 3 | 3 | 1.0 | Inconsistencies verified; hedged on theory, no errors; default weight |
| DA | 2 | 4 | 1.25 | Counterexample rederived; numerical check correct; DA-C1 survives the AC check |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes. The abstract's "maximally expressive … arbitrary non-isomorphic CCs" and contribution 2 are the paper's headline theory; the theorem is false by a rank-1 counterexample inside the paper's own scope (Cor. 4.1), and the supporting proofs are invalid (criterion 1: evidence contradicts the main claim). A narrower true statement is possible, but it is a different theorem needing a new proof. | **Upheld** | New theory / redesign of the claim and of the operator definition (not clarification alone) |

### Final Decision and Justification
The EIC-weighted rating is 2.31, so the starting point is 2 (Reject), and the composite cross-check (44.1, band 2) agrees; I keep the starting point. The DA ceiling is 3 and does not bind. The two accept-leaning reviews (R3, R4, both 3) rest on the appeal of the idea and on theory they said they could not fully verify; I verified the decisive points and the counterexample holds, so those ratings do not change the outcome. Pool position: about 28%. Deciding evidence: the main theorem is false and its proof invalid, the operator definition is ambiguous, and the experiments neither isolate the descriptor nor clear the noise on most tasks, which is what typical rejected submissions share. What accepted papers on this topic add (a correct separation result, ablations against strong encoding-equipped transformers, scalable timing on large complexes) is missing. The decision does not exceed the DA ceiling and is below the 4 the weaknesses typical of accepted papers would allow. Nothing in the integrity scan affected the decision.

---

## Score Summary

### Official Scores and EIC Assessment (script output, with EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 32 | 35 | 45 | 48 | 30 | 38.0 | 36.7 | 18 |
| Clarity & Presentation | 45 | 50 | 52 | 45 | 45 | 47.4 | 47.2 | 7 |
| Novelty & Originality | 48 | 45 | 52 | 52 | 45 | 48.4 | 47.8 | 7 |
| Significance & Impact | 42 | 42 | 50 | 50 | 40 | 44.8 | 44.0 | 10 |
| Experimental Validation | 36 | 40 | 45 | 46 | 35 | 40.4 | 39.6 | 11 |
| Reproducibility | 38 | 45 | 48 | 45 | 40 | 43.2 | 42.7 | 10 |
| Ethical Compliance | 62 | 60 | 62 | 58 | 60 | 60.4 | 60.5 | 4 |
| **Composite** | 41.6 | 43.5 | 49.5 | 48.9 | 40.2 | **44.8 (before)** | **44.1 (after)** | |

No spread exceeds 20 points; pool positions 30, 33, 48, 44, 25 (EIC: 28) all lie on the reject side.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 1 / 2 / 2 (of 4) |
| Rating | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Heat Kernel Goes Topological" to ICLR. Bringing heat kernel signatures to topological deep learning, and avoiding higher-order message passing with a pre-computed descriptor, is a worthwhile aim.

**Overall Assessment:** The panel found the idea appealing and the pipeline simple, but considered that the theory does not support the central claim and the experiments do not yet show where the gains come from. This is how a careful panel would likely see this draft, not a prediction.

**Key Strengths Identified by Reviewers:**
1. A cheap, basis-independent spectral descriptor with a clear multi-scale story (R1, R3, R4).
2. Candid limitations and compute disclosure (R1, R4).
3. Relevant to an active ICLR topic and a useful transfer from shape analysis (R3, R4).

**Key Concerns Requiring Attention:**
1. The expressivity theorem is not correct as stated (CONSENSUS-4; DA-C1 upheld).
2. The Laplacian of Definition 2.3 / Eq. 2 is not canonical and its smoothness property fails (R2, DA).
3. No ablation separates HKS from the transformer; the torus test is self-built and its metric undefined; gains are within noise (R1, R4, DA).
4. Efficiency and SOTA wording exceed the evidence ("12×", "constant footprint", "state-of-the-art") (R1, R4, DA).

**Critical Challenge (Devil's Advocate):** Strongly regular graphs with equal parameters (for example the 4×4 rook's graph and the Shrikhande graph) are rank-1 CCs with identical heat kernel diagonals at every node and time, so no network on these descriptors can separate them. This contradicts Theorem 4.3 and Corollary 4.3 and must be addressed.

**Decision: Reject (2).** A revised version would need a correct, restricted expressivity result, a canonical and proved Laplacian, an ablation against strong positional-encoding transformers, and a cleaner efficiency study.

Sincerely,
Dr. Ilse Brandvold, Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Expressivity theorem unsupported | R1, R3, R4, DA | CONSENSUS-4 |
| No ablation / strong baselines; gains within noise | R1, R2, R4, DA | CONSENSUS-4 |
| Claims exceed evidence (SOTA, scalable, 12×) | R1, R4, DA | CONSENSUS-3 |
| Cross-reference and presentation problems | R1, R2, R4, DA | CONSENSUS-3 (Minor) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall rating (2 vs 3) | R3, R4 (3: promising idea) | R1, R2, DA (2) | R3/R4 said they could not verify the proofs; the verified errors favour 2. |

### Score Spread Discussion
No dimension exceeded 20 points (Technical Rigor 18 is the widest: R4 48 vs DA 30); the gap is due to R4 not rederiving proofs, and the EIC adopts the lower view after verification.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Maximal expressivity false (rank-1 counterexamples, invalid proofs) | Yes: R1-W1, R3-W1 (partly), R4-W2 | Upheld | New theory / redesign |
| DA-M1 | MAJOR | Operator not canonical; smoothness false | Yes: R2-W1, R2-W2 | n/a | n/a |
| DA-M2 | MAJOR | Circular torus test, undefined metric | Yes: R1-W3 | n/a | n/a |
| DA-M3 | MAJOR | Claim distortion | Yes: R1, R4 | n/a | n/a |
| DA-M4 | MAJOR | No control for backbone / features / search | Yes: R1-W2, R4-W3 | n/a | n/a |
| DA-M5 | MAJOR | Hodge straw man | Yes: R2-W3 | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Expressivity claim false / invalid proof | DA-C1, R1-W1, R4-W2 | Abstract; Thm 4.1, 4.3, Cor 4.3; Thm 8.3 | Withdraw "maximally expressive"; prove a restricted separation result (permutation-based, not orthogonal); discuss strongly regular / cospectral limits; fix Table 1 "Isomorphism" | High (theory; no GPU) | No |
| R2 | Operator not canonical; smoothness property false | R2-W1, R2-W2, DA-M1 | Def. 2.3; Eq. 2; Thm 4.2, 8.2 | Fix a symmetric, ordering-independent construction; re-prove invariance, kernel on constants, PSD claims | High | No |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No ablation isolating HKS; missing graph-transformer baselines | R1-W2, R4-W3, DA-M4, R2-W4 | HKS vs none vs LapPE/RWSE vs Hodge-HKS; Transformer vs Mixer; d and time grid; GPS / SAN-type baselines; 5+ seeds (~240 GPU-h) | Medium–High | Partly |
| S2 | Torus experiment circular, metric undefined | R1-W3, DA-M2 | Define the task; add rank-count and hypergraph baselines; external CC datasets | Medium | Yes |
| S3 | Claims exceed evidence (SOTA, scalable, 12×) | R1-W4, R1-W5, R4-W1, DA-M3 | Align wording; report runs and paired tests; fix the 12× sentence | Low | Yes |
| S4 | Efficiency study | R1-W5, R3-W3 | Preprocessing and forward time in one unit on 10²–10⁵ nodes; approximate heat-kernel diagonal | Medium (~50 GPU-h) | Partly |
| S5 | Hodge comparison; hypergraph / PE related work | R2-W3, R2-W4, DA-M5 | Compare with rank-to-rank and hypergraph Laplacians; add the verified references | Medium | Yes |
| S6 | Reproducibility | R1-W6 | Hyperparameter table, search protocol on validation, baseline provenance, anonymised code | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | High-rank weights 2⁻ⁱ weaken high-rank signal | R3-W2 | Report HKS gap for the Table 2 pairs; test weight sequences |
| N2 | Rank labels in practice; broader-impact claims | R3-W4 | Add a domain-motivated rank structure (rings, glycan motifs) |
| N3 | Cross-references, units, typos | R1, R2, R4 | Fix Eq./Fig./Section pointers, use one speed unit |

---

## Estimated Revision Effort
- Priority 1: 2 items, weeks of theory work (no GPU).
- Priority 2: 6 items, ~2 weeks; ~290 GPU-hours.
- Priority 3: 3 items, days.
- **Total estimated revision time**: roughly 4–6 weeks; not feasible inside a one-week rebuttal.
