# Review: "Heat Kernel Goes Topological" (TopoHKS)

Scope note: I read the extracted text only. Figures were not available, so I judged figure-dependent claims (Figs. 1–7) from captions and surrounding text.

## Summary
The paper defines a Laplacian on combinatorial complexes (CCs) as a weighted sum of rank-0-to-rank-i incidence products, L = Σ_i b_i δ_i δ_iᵀ. The weights b_i are chosen so that all subset sums are distinct (e.g. 2^-i). It computes the diagonal of the heat kernel exp(−tL) at d=10 times in [0,3] as a node descriptor (HKS). It concatenates this descriptor with node features and feeds the result to a transformer or MLP-Mixer.

The paper claims four things:
- The Laplacian reduces to the graph Laplacian and is "unique".
- The descriptor distinguishes all non-isomorphic CCs, so the method is "maximally expressive".
- It beats SMCN and CIN on a modified torus blind-spot dataset, with 10x or more speedup.
- It is competitive on MolHIV, PROTEIN, and two GIFFLAR glycan tasks.

## Strengths
- The motivation is clear. Higher-order message passing is costly, and a cheap spectral preprocessing step that injects higher-rank information into a standard backbone is attractive.
- The construction is simple and easy to implement. Combining it with a transformer or MLP-Mixer is sensible.
- The empirical speed gains over SMCN, CIN and TopNetX are large and plausible. The torus blind-spot pairs are separated, including a new pair differing in a rank-4 cell.
- The paper is upfront that eigendecomposition preprocessing limits scaling.

## Weaknesses

1. **The central expressivity claim ("maximally expressive", distinguishes arbitrary non-isomorphic CCs) is wrong, and the proofs do not support it.**
   - L is an n×n matrix on rank-0 cells. HKS(c) = (exp(−tL))_cc is built only from the spectrum and the eigenvector diagonal of a single symmetric matrix.
   - Complete isomorphism testing by such spectral descriptors would solve graph isomorphism. Even for ordinary graphs (the rank ≤ 1 case, where the paper itself shows L equals the graph Laplacian), cospectral non-isomorphic graphs exist. Their rank-0 HKS multisets coincide. Strongly regular graphs are a standard counterexample: they are 1-WL-equivalent and cospectral, and the diagonal heat kernel is constant on them.
   - Theorem 4.1/8.1 asserts that "if L' = ΠLΠᵀ with an orthogonal Π then C' is isomorphic to C". Orthogonal similarity is just cospectrality (same eigenvalues). It is not permutation equivalence, and the cospectral counterexamples above violate the theorem. The proof is a hand-wave about "factorizations unique up to orthogonal transformation" and never shows that an orthogonal Π must be a permutation.
   - Theorem 4.3 does not establish what it claims. "L' ≠ ΠLΠᵀ for every orthogonal Π ⇒ different HKS" confuses the heat kernel matrix with its diagonal, a node-wise signature. Its proof argues that exp is injective on eigenvalues, which says nothing about whether the diagonal descriptors separate the complexes. The proof also treats the eigenvectors as "unique up to orthogonal transformations", which is wrong for repeated eigenvalues.
   - Corollary 4.3 invokes universal approximation on a set of per-node features. The approximator would need to be permutation-invariant, and the set-level HKS multiset is much weaker than the full matrix. The step "descriptors are distinct ⇒ a network can separate them" is also only an existence statement. It says nothing about learnability or about the model class actually used, a transformer with sin/cos features and no stated width or depth.
   - The paper never positions its power against WL or k-WL hierarchies. Its closest relatives are spectral positional encodings (Laplacian-PE, RWPE, heat-kernel PE, SPE), which are known to be incomplete. Statements such as "we can determine any WL classes by theoretical design" are unsupported.

2. **L loses most of the CC structure, so the expressivity gap to SMCN is likely not what is claimed.**
   - δ_i encodes only node-to-rank-i-cell membership. Everything is collapsed to a weighted hypergraph/clique-expansion-like operator on nodes. Containment relations among higher-rank cells that do not change node-set membership are invisible.
   - Distinct CCs can have identical node-membership structure. Rank assignments of cells enter only through the weight b_i, so a rank shift can be hidden by a coincidence of subset sums.
   - Such cases need to be examined. The torus examples are a handful of hand-built pairs, and each is separated by an operator on node membership.

3. **Definition 3.1 and the incidence matrix are ill-specified or inconsistent.**
   - Def. 2.3 gives δ_k ∈ R^{|X_0|×|X_k|} with exactly one +1 and the rest −1 per cell. For a rank-i cell with m>2 nodes, δδᵀ then yields off-diagonal entries that depend on an arbitrary choice of the "+1 node". L is then not permutation-equivariant. It is also not a Dirichlet form of the claimed type Σ w_ij(f_i − f_j)², and Thm 4.2 does not follow.
   - The claim in Thm 4.2 that f⊤Lf = B Σ w_ij(f_i−f_j)² with w_ij = 0 iff no connecting cell is only true under a specific symmetric choice that the paper never makes. The Appendix proof assumes the standard Laplacian form L_ij = −w_ij and L_ii = Σ w_ik. It never derives this from Def. 3.1.
   - The indices are inconsistent. Eq. (2) sums to R but the text says |B| = R. The observation uses L(r) = Σ_{i=0}^r. B = Σ_{i=0}^R β_i uses β where b was defined. Equation references are broken (Eq. (10)/(11)/(8)).
   - The statement in Sec. 3.2 ("we only consider the kernel for cells of rank 1") contradicts the rank-0 descriptors elsewhere.
   - Weights 2^{-i} make the contribution of higher ranks exponentially small. The paper itself notes that L barely changes. With float arithmetic, the high-rank signal can fall below numerical resolution of the heat kernel at small t. No analysis or ablation of the choice of B is given. A 1/i weighting or learned weights would be natural alternatives.
   - Heat kernels are claimed to be "permutation-equivariant/invariant". That would need an explicit statement for the chosen incidence signs, and none is given.

4. **The experiments do not support SOTA or "superior" claims.**
   - The baseline set is weak. Missing are strong graph baselines on MolHIV (GIN/GCN with virtual node, GraphGPS, GraphTransformer with LapPE/RWPE, Graphormer, and other PE-augmented models). TopoHKS is a transformer, so the right control is the same transformer with standard Laplacian/heat-kernel/RWPE positional encodings on the graph. Without that, a gain cannot be attributed to the CC Laplacian rather than to the transformer plus any spectral PE.
   - MolHIV is reported as "ACC" 83.1. The standard metric is ROC-AUC, and the numbers are unlabelled and not comparable to the literature. For PROTEIN the std of TopoHKS (±1.0) is close to the gap with CIN (77 ± 4.2), and the difference is small. On the glycan tasks TopoHKS only ties SMCN (0.90 vs 0.90, 0.84 vs 0.85), so the abstract's claim of outperforming existing topological methods and "state of the art" is not supported there. Several entries are "NaN" because CIN is said to fail to learn, with no investigation of whether baselines were tuned.
   - The data splits come from [5] and [18]. It is unclear whether hyper-parameters (d, time grid, depth, MLP-Mixer vs transformer) were tuned per dataset on validation data, and whether baselines received comparable tuning.
   - There is no ablation: no comparison against the Hodge Laplacian on the real data, none on number of times d, time range, weight sets B, descriptor choice (HKS vs WKS vs full kernel), or Mixer vs Transformer. The claim that the CC Laplacian differs from the Hodge Laplacian is shown on one toy pair.
   - The expressivity benchmark is narrow. The "223 distinguished pairs, 100% accuracy" row for the original blind-spot torus set merely ties SMCN. The new rank-4 pair dataset is built by the authors, small, and designed so that SMCN is known to fail. SMCN is by design limited here, and that is a limitation of that model rather than evidence of general expressivity. Standard expressivity tests (EXP, CSL, BREC, strongly regular graphs) are missing, and these would test the central claim directly.
   - CIN scoring 0 pairs and 0% is expected from earlier work and does not inform the comparison.

5. **The efficiency claims are overstated.**
   - Speed numbers (it/s, seconds) come from different units, different hardware settings, and unclear batch sizes, and some baselines are reimplemented. The full cost of dense eigendecomposition (O(n³) per complex) appears to be excluded from "iterations per second". The Limitations paragraph concedes this. The abstract and Sec. 5.2 ("constant computational footprint regardless of complex size", "scales efficiently") are therefore misleading. Preprocessing time must be reported, and Fig. 6 only goes to 100 cells.
   - The scalability claim also needs comparison against cheaper baselines (e.g. graph transformer with LapPE, other GNNs). Table 3 shows TopoHKS is 10–100x slower than GCN/GIN on MolHIV/PROTEIN, so scalability is relative only to higher-order message passing.
   - A 6,000 GPU-hour budget is stated for a project whose runs take 1–5 hours each. This sits oddly with the "efficient" narrative and with the small number of experiments.

6. **Novelty and related work.**
   - Weighted clique/star expansions of hypergraphs and their Laplacians are classical (Zhou et al. hypergraph Laplacian, and others). The paper does not cite or compare against them or against spectral hypergraph methods. Heat-kernel and spectral features for graph transformers (e.g. Laplacian PE, SPE, heat-kernel PE, Graphormer/GPS PEs) are not discussed.
   - The "Laplacian for CCs" is essentially a weighted hypergraph Laplacian on nodes. Calling it a new topological Laplacian that "extends the Hodge Laplacian" is not justified. It does not act on cochains of rank k, loses the rank-k structure, and is not a topological operator (no chain-complex property).
   - Lemma 4.1 (the Hodge Laplacian cannot see a rank-4 cell with no incident rank-3/5 cells) shows a limitation of Hodge Laplacians on general CCs, but this is largely a consequence of the definition of boundary operators rather than a deep result.

7. **Presentation.**
   - Many proofs are sketches, with informal language such as "we can argue".
   - Table 1's check marks (SC, R2, IS, EQ) are asserted without definitions, and "IS" (isomorphism) is not true as discussed.
   - Typos and inconsistent names appear throughout (Immuginicity/Immogenicity/Immunogenicity; "than B' = B''"; Cor. 8.2 cited for the Hodge limitation, which is in Sec. 4).
   - The MLP-Mixer paragraph (Sec. 3.3) claims comparable or superior performance with fewer resources, but no results are shown. Code is not released.
   - Fig. 5a and Table 2 repeat the same numbers with slightly different speeds (10/9/100 vs 7/10/95 it/s) and no explanation.
   - Deep-learning details are missing: layers, width, optimizer, number of seeds, and how the sizes of different complexes are batched.

## Questions
1. Do you have a counterexample check, or a proof, that TopoHKS separates cospectral non-isomorphic graphs (e.g. strongly regular graphs of the same parameters)? If not, how can the claim "distinguishes arbitrary non-isomorphic CCs" stand, given that L reduces to the graph Laplacian when rank ≤ 1 (your Corollary 4.1)?
2. How is the "+1 node" chosen in δ_i for cells with more than two nodes? Is L invariant under that choice and under node permutations? Please give the explicit weights w_ij for a rank-3 cell with three nodes and show L_ij = −w_ij.
3. Can you report results for the same transformer with standard Laplacian-PE/RWPE/heat-kernel PE on the graph (rank ≤ 1) for MolHIV and PROTEIN? What is the metric on MolHIV (ROC-AUC)? How many seeds, and how were d and the time grid chosen?
4. Can you report end-to-end timings including eigendecomposition, for complexes up to thousands of cells? Is it fair to compare it with SMCN at constant footprint?
5. What happens numerically with b_i = 2^{-i} at larger R? Does the rank-R signal vanish at floating point for t ≤ 3? Have you ablated alternative weight sets?
6. Can you add tests on BREC/EXP/CSL, on additional CCs with the same node-membership but different rank structure, and on random hypergraph pairs with identical clique expansions?

## Ratings
- **Soundness: 1** (the headline theory is incorrect or unproven, and the Laplacian definition is inconsistent)
- **Presentation: 2**
- **Contribution: 2**
- **Rating: 2** (reject)
- **Confidence: 4**

The idea of cheap spectral descriptors for topological models is reasonable. But the central theoretical claim fails against known cospectral counterexamples, the experiments lack the right controls, and the efficiency claims omit the dominant preprocessing cost.
