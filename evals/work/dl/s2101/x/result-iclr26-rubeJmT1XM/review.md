# Simulated Review: "Splat Regression Models" (ICLR, full mode)

*Simulation of how a careful panel would likely see this draft. It is not a prediction of the real decision. Date: 2026-11-05. The five reviewers were run as sequential role passes sharing one model context (no subagents); independence was kept by not letting any pass read another pass's report. Figures were not available, so figure-dependent statements rely on captions and extracted text only.*

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Splat Regression Models |
| Primary Discipline | ML → function approximation / scientific ML (physics-informed learning) |
| Secondary Discipline(s) | Optimal transport and gradient flows on measure spaces; computer graphics (3D Gaussian Splatting) |
| Paper Type | Theoretical (composite weights: theoretical). Hybrid: three of the four stated contributions are formal or conceptual; experiments are small (d ≤ 2). |
| Core Technique(s) | Mixtures of anisotropic Gaussian-like bumps with vector weights; Wasserstein-Fisher-Rao (WFR) gradient flows; Bures-Wasserstein geometry |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | Public reviews, revised PDFs allowed during discussion; pool base rate ≈ 27% accepted |
| Paper Maturity | Early draft / workshop-level experiments with a developed formal framework |
| Ethics-Relevant Content | None (no human data, no deployment risk) |
| Integrity scan | `integrity_scan.py`: no reviewer-directed text or hidden characters found. The five reviewers read the redacted copy (identical to the original). |
| Literature check | Mode `strict`, cutoff 2025-09-24. 7 queries (claim 5, baseline 1, expansion 1), 67 unique kept results, no coverage gaps flagged. `benchmarks` found no external benchmark names (the experiments use self-generated functions), so `scout` was not run. |

### Claimed Contributions (as stated by the authors, Section 1)
1. **C1** Splat Regression Model; "some preliminary structural theorems" and universal approximation (Prop. 2, Prop. 3, Thm. 3).
2. **C2** "Principled optimization algorithms" via WFR gradient flows over a "distribution over distributions" (Thm. 1).
3. **C3** "We recover 3D Gaussian Splatting as an instance of splat regression modeling" (Example 2).
4. **C4** Empirical performance on low-dimensional regression and physics-informed fitting (Section 4), "often vastly outperforming" KAN and MLP.

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** §4.1/Fig. 1: f*(x)=sin(20πx(2−x)), d=p=1, k=30 splats, n=200 noiseless uniform samples, init v_i=0, b_i=(i−1)/k, A_i=1/2k, Wasserstein gradient descent, lr 10^-4, no momentum; baselines Chebyshev interpolation (m=30, 45) and Haar wavelets (up to m=255). §4.2/Fig. 2: f(x,y)=sin(3π√x)cos(3πy), n=1000, noise N(0,0.01), 10^4 Adam steps, lr 10^-4, β=(0.9, 0.99), MLP (2–3 layer ReLU), KAN (10th-order splines, 5 grid intervals, jaxKAN), splat ρ=N(0,I). §4.3/Fig. 3: Allen–Cahn ε=0.1 on [0,1]², 10^5 interior and 5·10^4 boundary samples, MLP widths [20]–[100], [20,20], KAN [20]–[100], splat k up to 400. Seeds, hyperparameter selection, validation-set size, hardware, wall-clock time and code availability: **not stated after search** (grep for seed/tuned/hyperparam/held-out/GPU/code/time).
- **Headline numbers.** Abstract/§1 give no numbers. §1: "vastly outperforming" KAN/MLP "in architecture size, generalization error, and convergence speed". Fig. 2 caption: "order of magnitude lower fitting error". Fig. 3 caption: k=50 splat "outperforms all KAN and MLP architectures by an order of magnitude". All are figure-only (not tabulated).
- **Appendix.** A: proofs of Prop. 2, Cor. 1 (=Prop. 3), Thm. 3. B: WFR background, proofs of Prop. 1 and Thm. 1 ("at a formal level"). C.1: sawtooth target and Chebyshev-initialisation runs (Figs. 4–5). C.2: heterogeneous mixtures on P(R^p×R^d), Theorem 9, a heuristic discretisation sketch for Fisher–Rao dynamics.
- **Unverifiable.** All figure contents; several garbled equations in extraction (Prop. 2 statement, parts of eq. (1), Thm. 3 constants).

### Review Team (fictional personas)

**EIC (meta-reviewer): Dr. Helena Marquardt-Okoye**, applied-mathematics and ML department, large public research university (Western Europe). Senior faculty; mean-field theory of neural networks, scientific ML. *Style:* weighs verified technical errors against contribution; knows ICLR accepts theory-flavoured papers with thin experiments only when the formal content is sound and new.

**Reviewer 1 (Methodology): Dr. Tomasz Adeyinka-Reyes**, industrial research lab (Europe). Mid-career; PINN benchmarking, proof checking for optimisation theory. *Style:* reads proofs line by line, insists on tuned and matched baselines.

**Reviewer 2 (Domain): Prof. Anselm Rautavaara-Lindgren**, mathematics department, public university (Northern Europe). Senior faculty; optimal transport, Wasserstein–Fisher-Rao flows, RBF approximation theory. *Style:* checks novelty against the abstracts of prior work.

**Reviewer 3 (Perspective): Dr. Mei-Ling Tzeng-Abara**, computer graphics group, research university (East Asia). Mid-career; neural rendering, volumetric rendering, Gaussian splatting systems. *Style:* constructive, looks for cross-field reinventions and deployment realities.

**Reviewer 4 (Generalist): Dr. Rafael Quintero-Dahl**, ML group, private research university (North America). Postdoc-to-assistant-professor level; representation learning. *Style:* typical PC member; judges clarity and venue fit.

**Devil's Advocate: Dr. Ayesha Karimi-Lindqvist**, statistics and evaluation-methodology group, European research institute. Senior researcher; evaluation design, causal inference. *Style:* rigorous, never hostile; steelmans first.

*Personas are fictional. Assumptions: venue ICLR (stated); paper type theoretical (hybrid, see card).*

---

## Phase 1: Independent Reviews

# Peer Review Report (Reviewer 1: Methodology)

## Paper: Splat Regression Models
## Reviewer: Dr. Tomasz Adeyinka-Reyes, Methodology (industrial research lab, Europe; fictional persona)
## Expertise: PINN benchmarking; proof checking in optimisation theory; evaluation protocols for function approximators
## Date: 2026-11-05

### Summary
The paper proposes a function class f_µ(x)=E[vρ_{A,b}(x)], a finite mixture of affinely transformed bump functions with vector weights, and studies it as a two-layer network with a localised activation. It states universal-approximation results (Prop. 3, Thm. 3), derives gradient formulas for µ↦F(f_µ) under Wasserstein and Fisher–Rao geometry (Thm. 1), and describes 3D Gaussian Splatting as a special case (Example 2). Experiments on a 1D multiscale fit, a 2D noisy regression and a 2D Allen–Cahn solve compare against Chebyshev, Haar, MLP and KAN baselines (§4, Figs. 1–3).

### Protocol sweep and claim-to-evidence map
Sweep (`seed`, `tuned`, `hyperparameter`, `held-out`, `validation`, `test set`): no statement on seeds, number of runs, hyperparameter selection for any model, validation-set size, or which split is reported; Fig. 3 uses both "Validation error" (middle panel) and "Final Test Error" (right panel axis title) without defining either. No statement that tuning used a held-out test set (so no leakage finding).

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | universal approximator, structural theorems | §3.1, App. A | Prop. 3 proof, Thm. 3 proof | Partially: result is plausible, proofs have gaps (ERR-2, 3, 4) |
| C2 | "principled optimization algorithms … crucial to our empirical success" | §1, Thm. 1, App. B.2 | Thm. 1 derivation; experiments use plain GD/Adam | Partially: gradients equal backprop gradients; FR part unused; sign inconsistency (ERR-1) |
| C3 | "we recover the heuristic methods used to optimize Gaussian Splat models" | §3.2, Example 2 | none (formulation only) | Unsupported as worded; §3 end says "pave the way to interpret" |
| C4 | "often vastly outperforming" KAN/MLP in size, error, speed | §1, §4.2, §4.3 | Figs. 2–3 (single runs, figure-only) | Partially: supported only against weak/untuned baselines, one target function, d ≤ 2 |

### Strengths
**S1: Clean, compact model with a transparent gradient calculus.** The class in eq. (1) is simple, differentiable to any order given a smooth ρ (Prop. 2), and Thm. 1 / Example 1 give explicit per-splat gradients in terms of the first variation. Example 1 correctly observes that the v-gradient is "precisely the error signal vector that is propagated to model parameters through backpropagation", which makes the machinery easy to check.

**S2: The 1D study (§4.1, Figs. 1, 4, 5) is honest about a negative.** The authors state that with a 90-parameter budget "the splat model achieves slightly worse approximation error" than Chebyshev interpolation, and they show a sawtooth and an alternative initialisation in App. C.1.

**S3: Experiments cover three regimes** (1D multiscale, 2D noisy regression, 2D PDE) with accuracy-versus-parameters curves (Figs. 2–3) rather than a single operating point. This is a sensible way to present size/accuracy trade-offs.

### Weaknesses (by severity)

**W1: Baselines in §4.2–4.3 are untuned and unusually configured, so the headline claim is not established.** Section 4.2 trains all models with the same lr 10^-4 for 10^4 Adam steps; no tuning for MLP or KAN is stated (sweep: not stated). KAN uses "10-th order spline functions" with 5 grid intervals, far from the usual low-order setting; MLPs are plain ReLU networks of width ≤ 1000 and depth 2–3 even though the paper's own thesis is that "smart positional encoding is all you need" (§2) and cites Fourier-feature and RBF encodings [TSM+20, ZBG24]. In §4.3 the PINN baselines are tiny ([20]–[100], [20,20]) and trained for ~5000 steps with Adam only. The statement "outperforms all KAN and MLP architectures by an order of magnitude" (Fig. 3 caption) is therefore a statement about these configurations. *Fix:* add (i) an RBF network with learned centres and widths (isotropic splats) and PIRBN-style baseline, (ii) a Fourier-feature MLP and SIREN, (iii) per-model learning-rate/width tuning on a validation split with equal budget, (iv) L-BFGS or longer schedules for the PINN. Cost: ≈ 10–20 GPU-hours.

**W2: The 1D comparison with Chebyshev/Haar is not like-for-like.** The splat model is fit by least squares to n=200 random samples (§4.1) after ≥10^4 iterations, whereas Chebyshev interpolation needs function values at designed nodes and is closed-form; how the Chebyshev and Haar models use the 200 samples is not stated. The parameter budget counts Chebyshev as "2×m=90" by "counting the Chebyshev node locations as parameters", although the nodes are fixed analytically; a matched budget would be m=90 coefficients, which would favour Chebyshev further. Fig. 1's caption nevertheless says the splat "competes with the gold-standard Chebyshev polynomial interpolation". Training cost (iterations, wall-clock) is not compared, and only one target function is used in the main text; "robust to different initializations and functions" is introduced with "Anecdotally, the exponentially fast convergence". *Fix:* state data access for each method, add Chebyshev at 90 coefficients, report time-to-error, and add 5–10 target functions (smooth, oscillatory, discontinuous) with 5 seeds. Cost: < 2 GPU-hours.

**W3: No variance or repeat runs anywhere.** Figs. 1–3 are single runs per configuration (seeds not stated). Splat training from random b_i∼U (§4.2) and the order-of-magnitude claims depend on initialisation. Experiments are small enough that 5 seeds are cheap. *Fix:* report mean±std over ≥5 seeds for Figs. 2–3 and a table of final errors with the metric defined (relative L2?), including the noise floor (see Q1).

**W4: Theory–experiment disconnect.** Thm. 1's Fisher–Rao component (weights/teleportation) is never used: §4.1 trains by "Wasserstein gradient descent", §4.2 by Adam, and parameter counts are 3×k (§4.1), i.e., µ-masses are not learned. §4.3's Allen–Cahn loss is not covered by the Poisson formulas of Example 2, and the NVS case (Example 2.2) is explicitly deferred to autodifferentiation ("gradient formulas depend on the specific approximations used in practice and can be computed using autodifferentiation"). The abstract's "can be implemented using Wasserstein-Fisher-Rao gradient flows" is therefore untested for the F-R part. *Fix:* include an experiment that learns masses/reaction (birth–death, pruning criterion) and ablates it; or state that the experiments use parameter-space gradient descent.

**W5: Proof gaps (see Error Log).** Prop. 3's proof realises a splat with a rank-one A (outside the model class) and uses a non-negative measure to prove "discriminatory"; Thm. 3's probabilistic step applies Chebyshev's inequality to a non-centred quantity; Thm. 1's A-gradient sign differs between statement and derivation. These are repairable, but a paper whose first contribution is theorems needs them correct. *Fix:* see log.

**W6: Reproducibility.** No code or anonymous link, no hardware, no wall-clock, and the Allen–Cahn ground truth ("True solution under this parameter regime", Fig. 3) is not specified (equation, boundary data u*, solver). Several quantities are undefined in §4.3 (D, f, the error norm). *Fix:* add an implementation appendix and code.

**Minor:** text says snapshots are "arranged from right to left" (§4.1; presumably left to right); Fig. 4 caption "in the setting of 1" refers to Fig. 1; Fig. 3 axis says "Final Test Error" while text and caption say validation; duplicated bibliography entries ([KKLD23a/b], [MST+21a/b], [MMM19a/b], [ZPBG02a/b]); [Li24] is cited for KAN in §4.2 where [LWV+25] is meant.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E2 | Thm. 1 (§3.2) and its restatement in App. B.2 vs. derivation at end of App. B.2 | "= − ⟨δF[fµ ](x), v⟩(I + ∇x log ρA,b (x)(x − b)T )A−T" | The derivation yields −ρ_{A,b}(I+∇log ρ (x−b)^T)A^{-T} (matches the auxiliary computation just above), but the stated ∇A formula (and Example 1's ∇A) has no minus sign | Differentiated ρ(A^{-1}(x−b))\|det A\|^{-1} by hand; cross-referenced statement vs. derivation. Extraction could drop a glyph, so check the PDF | Medium | MAJOR (statement of main theorem) | Fix sign in Thm. 1, Example 1 |
| ERR-2 | E2/E3 | App. A, proof of Cor. 1 (= Prop. 3) | "to realize G(x) as a splat, take" (A = e1 y^T, b = e1 θ) | A has rank one, so ρ_{A,b} is not a density and A^{-1}, \|det A^{-1}\| in eq. (1) do not exist; a ridge function is not integrable on R^d. The construction is outside Definition 1 | Checked against Def. 1 / eq. (1) | High | MAJOR | Use a limiting argument with elongated invertible A and rescaled v on compact Ω, or cite RBF-network universality |
| ERR-3 | E2 | App. A, proof of Cor. 1 | "Let µ be a nonzero measure on [0, 1]d and let s ∈ supp(µ)." | Discriminatory (Thm. 2) quantifies over signed measures; the argument "0 = ∫ρ1 ≥ t P(ρ1>t)" treats µ as non-negative, so it does not show ρ1 is discriminatory | Read proof against the definition in Thm. 2 | High | MAJOR | Cite Hornik/Leshno-type results (non-polynomial σ) or give a signed-measure argument |
| ERR-4 | E2 | App. A, proof of Thm. 3 | (no clean quote: the probability display after "Take random x1 . . . xk" is garbled in extraction; it reads P(sup∥fµ−f^ε∥ > ε) ≤ Var(·)/ε²) | Chebyshev bounds \|Z−EZ\|, not Z; E[Z] of the sup-deviation is never bounded, so the probability-½ conclusion for k=2C_Ω ε^{-2(d+2)}(…)² does not follow. Also f^ε is the mollification of f over R^d while E[f(x_i)ε^{-d}ρ((x−x_i)/ε)] carries a 1/\|Ω\| factor and boundary leakage | Re-derived the step; checked normalisation | High (Chebyshev); Medium (normalisation) | MAJOR | Bound E[Z] (symmetrisation/covering) and include the \|Ω\| factor |
| ERR-5 | E1/E2 | Example 1 | "and so δF[f ](xi ) = n2" (extracted) | The displayed first variation already equals (1/n)Σ⟨ξ,∇L⟩ = ∫⟨ξ,∇L⟩dπ, so δF=∇ŷL; the extra 2/n double-counts 1/n (and ∇L for squared loss already contains the 2) | Recomputed from the displayed first variation | Medium | MINOR | Fix constants |
| ERR-6 | E6 | Eq. (1) lines 1–2 vs. Def. 1 | (first line of eq. (1); extracted text is garbled, so no clean quote) | Line 1 multiplies ρ_{A,b}(x) (already including \|det A\|^{-1}) by \|det A^{-1}\| again; line 2 writes ρ(A^{-1}(x−b))\|det A^{-1}\| once | Cross-referenced the two lines; garbled extraction possible | Medium | MINOR | Remove the duplicate factor |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Proof gaps and untuned baselines (W1, W5) |
| Clarity | 2 | Dense formal presentation, undefined quantities in §4.3 |
| Significance | 2 | Potential, but evidence is d ≤ 2 |
| Originality | 2 | Medium novelty, see R2 |

### Dimension Scores (0–100)
**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline empirical claim rests on untuned baselines at d ≤ 2, and the first-listed contribution (theorems) has three located proof gaps.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 44 | Developing | ERR-1…4; "formal level" derivations |
| Clarity & Presentation | 54 | Developing/Competent | Readable narrative; notation and §4.3 definitions incomplete |
| Novelty & Originality | 52 | Competent | Reformulation of RBF/mean-field ideas, see R2 |
| Significance & Impact | 48 | Developing | Low-dimensional only |
| Experimental Validation | 36 | Developing | W1–W3 |
| Reproducibility | 38 | Developing | No code, seeds, ground truth for PDE |
| Ethical Compliance | 64 | Competent | Nothing at stake; limitations partly discussed (§4.2, §5) |

### Questions for Authors
1. Is ε_i∼N(0, 0.01) in §4.2 a variance or a standard deviation, and is the validation MSE in Fig. 2 computed against clean f or noisy y? If noisy with variance 0.01, an MSE near 10^-3 (as the extracted axis ticks suggest; figures unavailable) would lie below the noise floor. A clean-target metric would raise my Experimental Validation score; an undetected floor violation would lower it.
2. How were the Chebyshev and Haar models given the n=200 samples (Fig. 1), and what is the wall-clock for each? Equal-cost results would change my view of the "competes with" claim.
3. Do any experiments update masses (Fisher–Rao part)? If not, what in Section 4 depends on Thm. 1 beyond ordinary backpropagation?
4. How is the Allen–Cahn "true solution" (Fig. 3, left) obtained, and with what boundary data u*?

### Limitations Assessment
**Partially.** §4.2 and §5 mention overfitting and the need for regularisation, but the low-dimensionality, single-run, and baseline-tuning limitations are not discussed.

### Ethics Review Flag
**No.**

### Overall Score
**3** (Borderline Reject): an interesting formulation with a plausible core, but the empirical claim is not established and the theorems need repair. **Confidence 4** (read all proofs, but figures unavailable).

---

# Peer Review Report (Reviewer 2: Domain)

## Paper: Splat Regression Models
## Reviewer: Prof. Anselm Rautavaara-Lindgren, Domain (mathematics department, public university, Northern Europe; fictional persona)
## Expertise: optimal transport and WFR flows; RBF approximation theory; mean-field neural networks
## Date: 2026-11-05

### Summary
The paper presents a model class built from anisotropic bumps, studies its geometry via Bures–Wasserstein structure (Prop. 1), proves universal approximation (Prop. 3, Thm. 3), gives WFR gradients (Thm. 1), and positions 3DGS as an instance. In my reading, with learned centres, widths (A_i) and weights, the model is a two-layer network with a localised activation, i.e., an adaptive radial basis function network with anisotropic Gaussian units; the contribution is the measure-space viewpoint and the link to splatting.

### Strengths
**S1: A useful unifying viewpoint.** Writing the model as µ on R^p×BW_ρ(R^d) (Def. 1) and placing it next to mean-field theory of two-layer networks (§2, [CB18, MMM19]) is clean, and the observation that the first layer lives on a Bures–Wasserstein manifold (Prop. 1) is a reasonable differentiator from ReLU mean-field analyses.

**S2: Correct and precise connection to Chizat–Bach-style calculus.** The chain-rule presentation in App. B.2 (differentials d^W f_µ, d^{FR} f_µ) is a good teaching device and the Fisher–Rao gradient formula in Thm. 1 is the expected one.

**S3: Honest statement that the 3DGS heuristics are a direction for future work** at the end of §3 ("our results pave the way to interpret these heuristics"), even though §3.2 words it more strongly.

### Weaknesses

**W1: Novelty of C1 is medium and not differentiated from RBF networks.** Gaussian radial basis networks with trainable centres/widths and their universality are classical, and the paper's own reference [Li24] shows KANs are RBF networks. Section 2 never cites or compares with RBF-network or PIRBN-type work. The literature check (below) found physics-informed radial basis networks [PIRBN, arXiv 2304.06234] that already use a one-hidden-layer local RBF network for PDEs and report advantages over PINNs. *Fix:* add an RBF/anisotropic-RBF related-work paragraph and an isotropic-splat (RBF) ablation to isolate what heterogeneity buys.

**W2: Novelty of C2 is medium: WFR descent on mixture weights and locations exists.** Yan–Wang–Rigollet (arXiv 2301.01766) run WFR gradient descent over mixtures of Gaussians (weights and locations, particle system) with convergence guarantees; Wang–Chizat and Domingo-Enrich et al. do the same for particles in games. The paper cites none of these, and does not explain what Thm. 1 adds beyond treating each particle's scale matrix A as a coordinate. Moreover, for a finite k-splat measure the "Wasserstein gradient" in coordinates is the ordinary parameter gradient (the paper itself says so in Example 1), so C2 is largely a reinterpretation. *Fix:* cite and position against this line; state precisely what is new (e.g., the BW-geometry structure and Fisher–Rao reaction for kernel-valued particles) and give a guarantee or experiment where it matters.

**W3: C3 ("recover 3DGS") is a formulation, not a derivation.** Example 2 writes NVS as an inverse problem with RTE forward operator, eq. (3), parametrises σ and s with splat models, and then states the gradients "depend on the specific approximations used in practice". The real 3DGS pipeline (per-Gaussian opacity, front-to-back α-compositing after EWA projection, tile rasterisation, densification/pruning) is not shown to be an instance, and α-blending of per-Gaussian opacities is not the same discretisation as volume rendering with σ=Σ Gaussians. The abstract's "providing a unified theoretical framework for this state-of-the-art technique" and §3.2's "we recover the heuristic methods used to optimize Gaussian Splat models" are not matched by a theorem or an experiment, and later text only "anticipates" the interpretation of selective noising and states that Thm. 1 "prescribes a pruning criterion that is guaranteed (in the continuous-time limit) to decrease the loss". *Fix:* either give the exact correspondence (what is σ, α_i, ordering, projection) or narrow the claim to "a continuous-time formalism in which 3DGS-like models can be posed".

**W4: Related work is thin on neural fields and Gaussian primitives for fields.** No mention of Gaussian-primitive field representations beyond NVS (e.g., Gaussian Fluids, arXiv 2405.18133, which models a PDE solution as a weighted sum of Gaussians inspired by 3DGS and solves it by first-order optimisation), nor of classical adaptive/free-knot approximation. Reference [CRY25] is described as "a modified ReLU network architecture whose neurons can be ‘superpositions’ of ReLU functions", yet its title is "Gaussian mixture layers for neural networks"; if the work trains Gaussian-mixture neurons with WFR flows it is a very close relative and the differentiation by BW-geometry would need more than one sentence. [verify: I could not check that abstract].

**W5: Theory adds little to expressivity.** Prop. 3 follows from classical RBF/Cybenko results, and Thm. 3 uses fixed-scale isotropic bumps (kernel ε^{-d}ρ(x/ε)) with k ≲ ε^{-2(d+2)} (§3.1), which is worse than the ε^{-d} of a uniform grid for Lipschitz functions; it does not exhibit any benefit of learned anisotropy, the paper's central selling point ("locally adjust the scale and direction", Abstract). *Fix:* prove an approximation-rate statement where adaptivity helps (e.g., functions with localised sharp features), or de-emphasise.

**Minor:** Prop. 1 assumes a "centered isotropic mother splat" but Def. 1 requires only "zero mean and identity covariance"; the W2=BW identification needs spherical symmetry of ρ. Duplicate bibliography entries.

### Literature-check addendum (strict, cutoff 2025-09-24; 7 queries: claims 5, baseline 1, expansion 1; 67 kept results)
**Per-claim novelty (claim-level profile, `related_search.py novelty`):**

| Claim | Dim. | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|------|---------|----------------------------------------------|-----------|
| C1 model + universality | method | medium | PIRBN (level 3) https://arxiv.org/abs/2304.06234v2, prior (arXiv-only, 6+ months), not cited | local one-hidden-layer RBF network for PDEs; no BW/measure view or heterogeneous vector weights |
| C2 WFR training | method | medium | Learning Gaussian Mixtures Using the WFR Gradient Flow (level 3) https://arxiv.org/abs/2301.01766v1, prior (arXiv-only), not cited | WFR flow on mixture weights and locations; no per-particle scale matrix, no regression functional |
| C3 recovers 3DGS | result | no close prior work found in 67 results (arXiv only; at most medium) | none | nothing found; absence of a prior does not validate the claim (see W3) |
| C4 outperforms KAN/MLP | result | medium | PIRBN (level 3), not cited | prior RBF-vs-PINN comparisons |

Paper reading: no established claim at level ≥ 4; no candidate for "known results presented as new". Closest prior work overall: PIRBN (script attribution). `similarity` flagged no high conceptual overlap (top cosine 0.121, "Gradient Flows for Sampling: Mean-Field Models, Gaussian Approximations and Affine Invariance") and no text overlap.

**Novelty delta table**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C1 | PIRBN (2304.06234) | Local radial-basis network for PDEs, NTK analysis | Anisotropic learned A, vector weights, measure-space formulation | No |
| C2 | Yan–Wang–Rigollet (2301.01766) | WFR descent on Gaussian-mixture weights/locations | Scale matrices as BW coordinates, regression/PINN functionals | No |
| C3 | Gaussian Fluids (2405.18133) | Gaussian-sum representation of a PDE solution inspired by 3DGS | WFR interpretation, Example 2 | No |

**Baseline scout.** No external benchmark was identified by `benchmarks` (experiments use synthetic targets), so no scout table. Relevant baselines for the setting that the paper omits: RBF networks / PIRBN, Fourier-feature MLP, SIREN, spectral-mixture GP solvers (ICLR 2024 "Solving High Frequency and Multi-Scale PDEs with Gaussian Processes", https://arxiv.org/abs/2311.04465v2, prior peer-reviewed).

**Field snapshot.** Three to five years ago, low-dimensional fitting and PINNs relied on MLPs, with Fourier features and RBF encodings as fixes for spectral bias. Since 3DGS (2023), Gaussian primitives have become a standard explicit representation in graphics, with 2024–2025 work transferring them to fluids, images and signed distance fields; at the same time KAN variants and RBF/KAN equivalences have been studied for PDE fitting. For this sub-field, a significant contribution would show a clear accuracy or cost advantage over properly tuned MLP/Fourier/RBF/KAN baselines on standard PDE benchmarks (not a single Allen–Cahn instance), or a theorem that explains when learned anisotropic primitives help. Such results are not present here, so I score Significance and Novelty at the medium level.

### Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | J. Bai, G.-R. Liu, A. Gupta, L. Alzubaidi, X.-Q. Feng, Y. Gu. Physics-informed radial basis network (PIRBN): A local approximating neural network for solving nonlinear PDEs. arXiv 2304.06234, 2023. https://arxiv.org/abs/2304.06234v2 (verified via `verify`) | Closest model-level prior: one-hidden-layer local RBF network vs. PINN on PDEs |
| Critical | Y. Yan, K. Wang, P. Rigollet. Learning Gaussian Mixtures Using the Wasserstein-Fisher-Rao Gradient Flow. arXiv 2301.01766, 2023. https://arxiv.org/abs/2301.01766v1 (found by search) | WFR gradient descent over mixture weights and locations |
| Important | J. Xing, B. Wang, M. Chu, B. Chen. Gaussian Fluids: A Grid-Free Fluid Solver based on Gaussian Spatial Representation. arXiv 2405.18133, 2024. https://arxiv.org/abs/2405.18133v2 (verified) | 3DGS-inspired Gaussian-sum PDE solver |
| Important | J. Park, I. W. Sandberg. Universal approximation using radial-basis-function networks. Neural Computation, 1991. [verify] | Universality for RBF networks makes Prop. 3 classical |
| Important | G. M. Rotskoff, E. Vanden-Eijnden. Trainability and accuracy of neural networks: an interacting particle system approach. arXiv 1805.00915 (verified), published later in CPAM | Particle/mean-field training of two-layer networks |
| Helpful | S. Wang, Y. Teng, P. Perdikaris. Understanding and mitigating gradient pathologies in physics-informed neural networks. arXiv 2001.04536 (verified) | Standard PINN baseline tuning (loss weighting) |
| Helpful | Approximating signed distance fields with sparse ellipsoidal RBF networks (arXiv 2505.02350, May 2025, recent preprint: "worth discussing", not required) | Anisotropic RBF fitting in 3D |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory repairable but flawed; weak empirical control |
| Clarity | 2 | Clear idea, heavy notation |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Medium (above) |

### Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: both central methodological claims have verified uncited near-neighbours (RBF networks; WFR for Gaussian mixtures), and the 3DGS claim is not derived.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing/Competent | Formal derivations; Prop. 3/Thm. 3 weak |
| Clarity & Presentation | 56 | Competent | Good intuition, dense notation |
| Novelty & Originality | 50 | Developing/Competent | Medium on C1, C2; unverified C3 |
| Significance & Impact | 52 | Developing/Competent | Potential bridge, limited evidence |
| Experimental Validation | 42 | Developing | Missing RBF/Fourier baselines |
| Reproducibility | 45 | Developing | No code |
| Ethical Compliance | 66 | Competent | Limitations partly discussed |

### Questions for Authors
1. What exactly separates Thm. 1 from running parameter-space gradient descent on the splat parameters, and which result in the paper would fail for an RBF network with trainable centres and widths? A concrete answer could raise Novelty.
2. Is [CRY25] a Gaussian-mixture-neuron model trained by WFR flows? If so, how does the present model differ?
3. Can you state the precise correspondence to the published 3DGS rasteriser (opacity, α-compositing, projection)? A theorem would raise Significance; "formulation only" would lower the 3DGS-related claims.

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**3**: a coherent framework whose individual ingredients are close to classical RBF networks and to existing WFR-for-mixtures work, with limited evidence. **Confidence 4.**

---

# Peer Review Report (Reviewer 3: Perspective)

## Paper: Splat Regression Models
## Reviewer: Dr. Mei-Ling Tzeng-Abara, Perspective (computer graphics group, research university, East Asia; fictional persona)
## Expertise: neural and volumetric rendering; Gaussian splatting systems; physically based simulation
## Date: 2026-11-05

### Summary
The paper brings the Gaussian-splat representation from rendering into regression and PDE fitting, arguing that spatially localised, anisotropic primitives act as an adaptive positional encoding for low-dimensional signals. It supplies a measure-theoretic description and gradient formulas, and shows small experiments where splat models fit a multiscale 1D function, a 2D noisy function and a 2D Allen–Cahn solution with few parameters.

### Strengths
**S1: A genuinely interesting cross-field idea.** Moving from "renderer" to "general low-dimensional function class" is natural to someone from graphics: the same primitives power real-time rendering, and the authors correctly note both NVS and physics-informed learning pay for pointwise MLP evaluation (§1). Fitting 2D PDE solutions with 50 splats (Fig. 3 caption) would be attractive if it generalised.

**S2: Honest framing of heuristics as future work.** §3 and §5 list pruning, selective noising and compositions ("deep splat networks") as directions, which is exactly where the graphics literature has accumulated engineering knowledge.

**S3: Compactness argument is relevant to deployment.** A few hundred parameters versus 10^4–10^5 for MLP/KAN (Figs. 2–3) matters for scientific-computing kernels where evaluation cost dominates.

### Weaknesses

**W1: The paper under-uses the graphics side that motivates it.** The NVS case (Example 2.2) is formulated but never run, even on a small synthetic scene; the key deployment knowledge of 3DGS (view-sorted α-compositing, EWA projection, tile-based rasterisation, densification) is absent, so "replicate the successes of 3D Gaussian Splatting across a wide variety of physical modeling and inverse problems" (§1) remains aspirational. *Fix:* run a minimal differentiable 2D splat renderer (image fitting) with the same optimiser and report PSNR/time against a standard 2D Gaussian-splatting implementation. Cost: a few GPU-hours.

**W2: Assumption audit: low dimension and smooth/low-frequency structure.** The method relies on k scaling with the number of features; the paper's own Thm. 3 gives k ≲ ε^{-2(d+2)} and all experiments have d ≤ 2. How the approach behaves for d=3–5 (PDEs in 3D, spatio-temporal problems) or with sharp, thin features (the Allen-Cahn interfaces as ε→0 are mentioned in §4.3 but only ε=0.1 is tested) is unknown. *Fix:* add a 3D Poisson or Allen–Cahn run and an ε sweep.

**W3: Reinvention risk in other fields.** Adaptive RBF/free-knot methods in numerical analysis and meshless collocation methods (RBF collocation), and the PIRBN literature in scientific ML, address the same "adaptive grid" idea; the paper cites none of these (§2 mentions only RBF-versus-KAN in [Li24]). Fourier-feature and hash-grid encodings used in graphics (and SIREN) would be natural baselines for the "smart positional encoding" thesis. *Fix:* add them as baselines and discuss.

**W4: Deployment considerations.** Evaluation cost per query point, gradient cost for PDE residual terms (Laplacians of splats), and conditioning of the gradient flow when A_i become ill-conditioned are not discussed; training time is not reported. *Fix:* report time per step, memory, and conditioning behaviour.

**Minor:** nothing to flag for ethics or societal impact; a one-line statement would suffice.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Experiments narrow |
| Clarity | 3 | Motivation is easy to follow |
| Significance | 3 | Promising bridge between rendering and PDE fitting |
| Originality | 3 | Fresh transfer of an idea across fields |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a fresh cross-field transfer with a plausible benefit, but evidence is preliminary.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Calculus is sound in outline |
| Clarity & Presentation | 68 | Competent | Motivation clear |
| Novelty & Originality | 64 | Competent | Transfer from graphics is non-obvious |
| Significance & Impact | 66 | Competent | Possible benefit for scientific computing |
| Experimental Validation | 52 | Developing/Competent | Small d, few cases |
| Reproducibility | 50 | Developing | No code/ground truth |
| Ethical Compliance | 70 | Competent | Nothing at stake |

### Questions for Authors
1. Does the approach keep its advantage at d=3 and with sharp interfaces (ε=0.02)? A positive answer would raise Significance by a band.
2. What is wall-clock time per training step relative to MLP/KAN at equal accuracy?
3. Can you show one image-fitting experiment so that readers from graphics can calibrate against GaussianImage-style methods?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**4** (Borderline Accept): an attractive idea whose promise is visible even if the evidence is early. **Confidence 3** (outside my core area for the optimal-transport proofs).

---

# Peer Review Report (Reviewer 4: Generalist)

## Paper: Splat Regression Models
## Reviewer: Dr. Rafael Quintero-Dahl, Generalist (ML group, private research university, North America; fictional persona)
## Expertise: representation learning, architectures
## Date: 2026-11-05

### Summary (the contribution in one paragraph)
The authors propose a regression architecture in which outputs are sums of weighted anisotropic bumps, argue that it is a universal approximator with a measure-valued parameter geometry, derive gradients using Wasserstein–Fisher-Rao calculus, and present small experiments where it beats MLP and KAN baselines on low-dimensional fitting. They also claim it unifies 3D Gaussian Splatting.

### Venue Criteria Checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported by theory/evidence | Partly | Thm. 1/3 proofs formal; §4 single runs |
| Contribution: new and significant for ICLR audience | Partly | §1 list vs. §2 positioning |
| Presentation: clear to a general ICLR reader | Partly | §3 abstract-first; §4 sparse details |
| Reproducibility: details and code | Not met | §4 (no seeds, tuning, code) |
| Limitations stated | Partly | §4.2, §5 (overfitting only) |

### Strengths
**S1: Clear one-line model.** The displayed formula in the Introduction (sum of v_i N(x; b_i, A_iA_i^T)) and the remark that the model is "a two-layer neural network with an atypical activation function" make the idea instantly graspable.

**S2: Honest scope statements.** §5 says a "larger scale computational study" is beyond scope and §4.2 flags overfitting risk, which helps readers calibrate.

**S3: Broad, interesting audience.** The paper speaks to ICLR readers in scientific ML, mean-field theory and neural fields, and the connection to 3DGS is memorable.

### Weaknesses
**W1: The contribution list is wider than the evidence.** Of four contributions, only C4 is tested, with three small experiments in d ≤ 2 (Figs. 1–3). The abstract's "diverse approximation, estimation, and inverse problems" has no estimation or inverse-problem experiment (the Allen–Cahn run is a forward solve). "High interpretability" (Abstract) is not evaluated anywhere in the text. *Fix:* narrow the abstract, or add an inverse problem (e.g., 2D Poisson source identification) and an interpretability illustration.

**W2: Experimental details are insufficient for a general reader.** §4.2 does not define the validation set or whether noise 0.01 is a variance; §4.3 leaves the ground truth, the operator D and the metric undefined; Fig. 3 uses "validation" and "test" interchangeably. There are no numbers in a table, so "order of magnitude" cannot be read off precisely. *Fix:* add a table with mean±std over seeds, define metrics, and release code.

**W3: Presentation order.** Readers are told they may "skip to (1)" but the proofs of the main results are in appendices with notation (e.g., first variation, BW coordinates) introduced late; §3 mixes definitions, theorems and examples without an overview figure of how µ, f_µ and the coordinates relate. *Fix:* add a schematic and a short "what to take away" paragraph per theorem.

**Minor:** typos ("continuosly", "my minimizing"), duplicated references, the "right to left" remark in §4.1.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See W1–W2 |
| Clarity | 3 | Idea is clear; details are missing |
| Significance | 2 | Narrow evidence |
| Originality | 3 | New packaging, plausible novelty |

### Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an intriguing idea but claims outrun small, loosely documented experiments, which is typical of rejected submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing/Competent | Reasonable outline, other reviewers found proof gaps |
| Clarity & Presentation | 58 | Competent | Clear core idea, missing details |
| Novelty & Originality | 55 | Competent | Fresh combination |
| Significance & Impact | 52 | Developing/Competent | Unproven beyond d=2 |
| Experimental Validation | 44 | Developing | Narrow and thinly documented |
| Reproducibility | 46 | Developing | No code or seeds |
| Ethical Compliance | 66 | Competent | Nothing at stake |

### Questions for Authors
1. Which of the abstract's claims (estimation, inverse problems, interpretability) are supported by experiments, and where? Clear pointers would raise my Clarity and Significance scores.
2. Can you provide a table of final errors with std over seeds for Figs. 2–3?
3. What would you drop from the contribution list if page limits forced it?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**3**: a promising idea, but at ICLR the claims should match the evidence. **Confidence 3.**

---

# Devil's Advocate Report

## Paper: Splat Regression Models
## Reviewer: Dr. Ayesha Karimi-Lindqvist, Devil's Advocate (statistics and evaluation-methodology group, European research institute; fictional persona)

## Steelman
The paper offers a compact, differentiable, localised function class with a clean measure-space description, and shows on three small problems that with few parameters it can fit multiscale targets and a PDE solution better than default MLP and KAN settings. If the geometry and universality results are right, the model is a natural bridge between splatting and scientific ML.

## Core Argument Chain
1. P1: Splat models f_µ are a universal approximator (Prop. 3, Thm. 3).
2. P2: Training them is principled via WFR gradient flows (Thm. 1), which "recovers" 3DGS optimisation heuristics (§3.2, Example 2).
3. P3: Splat models outperform KAN/MLP on low-dimensional regression and PDE fitting in size, error and speed (Figs. 2–3).
4. P4: This performance comes from spatial localisation, i.e., "smart positional encoding" (§2, §4.2).
∴ Splat regression is a promising unifying framework for low-dimensional modelling and inverse problems (Abstract).

## Strongest Counter-Argument
Even if every experiment is correct, the evidence does not show that anything specific to splat models, as opposed to "any localised radial basis expansion with trainable centres and widths", produces the gains, and the theory does not distinguish the two. The paper itself explains the gains by locality ("spatially localized nature, which can be viewed as a learned positional encoding", §4.2) and cites that KANs are RBF networks [Li24], but it never runs an RBF network, an isotropic-splat ablation, a Fourier-feature MLP or a tuned PINN. The baselines are default-configured and given the same lr 10^-4 for 10^4 steps; the KAN has 10th-order splines; the PDE baselines are width ≤ 100 for ~5000 Adam steps. So the "order of magnitude" in Fig. 3 is compatible with "default MLPs/KANs are poorly suited to a low-frequency 2D target at lr 10^-4". Meanwhile the formal part adds little in the direction of the claim: Thm. 1's Wasserstein gradient equals backpropagation for a finite sum (Example 1: "precisely the error signal vector that is propagated to model parameters through backpropagation"), the Fisher–Rao half is never exercised, universality follows from classical RBF results (and its proof as written uses rank-one A outside the class), and the only quantitative rate (Thm. 3, k ≲ ε^{-2(d+2)}) uses fixed-scale isotropic bumps and is worse than a grid, so it cannot explain the claimed efficiency. The 3DGS "recovery" is a restatement of the rendering equation with splat-parametrised fields and an appeal to autodifferentiation. What remains, as a supported claim, is that a trained adaptive RBF-type model fits three small problems well. That is a narrower paper than the abstract describes. The authors should address this in a rebuttal by adding the controls above, or by narrowing the claims.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The strongest objections (untuned baselines, claim-versus-evidence gap, proof gaps) all support a weaker version of the claims or concern repairable derivations, and the paper reports no test-set selection, so the core contribution survives in narrowed form.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §4.2, §4.3, Figs. 2–3 | Baselines untuned/unusual (same lr for all, 10th-order KAN splines, tiny PINNs, no Fourier/RBF/SIREN); single runs; "order of magnitude" is figure-only | Tuned equal-budget baselines incl. RBF network and Fourier-feature MLP; 5 seeds; table |
| DA-M2 | Logic | §4.2 / Abstract | Attribution to "anisotropic, heterogeneous splats" is untested: no isotropic-splat or fixed-width ablation; "high interpretability" never evaluated | Add ablations (isotropic A, shared A, no v-vectors) and an interpretability study or drop the word |
| DA-M3 | Scope/E5 | Abstract; §3.2; Example 2; §3 end | "unified theoretical framework", "we recover the heuristic methods used to optimize Gaussian Splat models", "inverse problems": contradicted by the paper's own softer statements ("pave the way", "We anticipate", gradients via autodifferentiation); no NVS or inverse experiment | Narrow wording or add a concrete derivation/experiment |
| DA-M4 | Evidence (theory) | App. A, Prop. 3 and Thm. 3 proofs | Rank-one A used to realise a splat (outside Def. 1); discriminatory argument assumes µ ≥ 0; Chebyshev applied to a non-centred sup-deviation; main text Thm. 3 drops the (1+L_f M_ρ) factor and "Lipschitz" vs. C^1 | Repair or cite classical RBF results; align statements |
| DA-M5 | Theory | Thm. 3 (§3.1) | k ≲ ε^{-2(d+2)} with fixed isotropic bumps is worse than a uniform grid and says nothing about learned anisotropy | State as a baseline guarantee only; add adaptive-rate result or remove emphasis |
| DA-M6 | Fairness | §4.1, Fig. 1 | Parameter accounting "counting the Chebyshev node locations as parameters" inflates Chebyshev's budget; Chebyshev uses designed nodes while the splat uses 200 random samples and ≥10^4 iterations; "competes with the gold-standard" | Equal-budget (m=90 coefficients) and equal-data/cost comparison |
| DA-M7 | Theory–practice | Thm. 1, §4 | Fisher–Rao component unused; Thm. 1 A-gradient sign inconsistent between statement and derivation | Use/ablate FR reaction; fix sign |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | Fig. 4 caption | "which can exactly fit vertical discontinuities": the sawtooth 2(6x mod 1)−1 has jumps at multiples of 1/6, which are not dyadic, so Haar cannot fit them exactly at finite scale |
| DA-m2 | Integrity of notation | Eq. (1); Example 1; Prop. 1 vs. Def. 1 | Duplicate \|det A^{-1}\| factor; 2/n constant; "isotropic" vs. "identity covariance" |
| DA-m3 | Presentation | §4.1, Figs. 1, 4 | Left panels run to 180000 (Fig. 1) / 90000 (Fig. 4) steps while right-hand iteration axes end at 20000 / 10000: clarify the unit (question, figures unavailable) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Splat parameter count (§4.1) | "3 × k = 90" with k=30 | 3·30 = 90 | Yes |
| Chebyshev parameter count (§4.1) | "2 × m = 90" with m=45 | 2·45 = 90; matched budget with coefficients only would be m=90 | Yes (but accounting favours splats) |
| Splat params per unit in Fig. 2 (2D) | not stated | v(1)+A(2×2=4)+b(2)=7; k=400 ⇒ 2800 vs. n=1000 samples | Derived (overparameterised) |
| Wavelet "m=255" at l=8 (§4.1) | m=255 | 2^8−1 = 255 | Yes |
| Thm. 3 exponent | ε^{-2(d+2)} | proof gives ε^{-2(d+2)}(…)² and error (1+L_f M_ρ)ε | Main-text statement drops factors |

## Ignored Alternative Explanations
- Default-configured MLP/KAN at lr 10^-4, 10^4 steps are under-trained for smooth targets; splats initialised with Ai=0.1 I and bi uniform in the unit square are well matched to a target supported in [0,1]².
- Any localised RBF expansion would show similar gains; isotropic vs. anisotropic is untested.
- Allen–Cahn at ε=0.1 is a mild instance (interfaces are not sharp); gains may vanish at smaller ε.
- Noise floor and clean-vs-noisy validation target (§4.2) may change the reading of Fig. 2.

## Missing Stakeholder Perspectives
Practitioners in scientific computing who need accuracy at equal wall-clock and robust gradient conditioning; graphics practitioners who need the actual rasterisation pipeline. No negative societal impact is expected.

## Observations (Non-Defects)
- The paper clearly acknowledges overfitting risk and the need for regularisation (§4.2, §5).
- The 1D example honestly reports that Chebyshev is slightly better at matched parameters (§4.1).
- The measure-space notation is consistent across the main text and appendix, and the chain-rule derivation of Thm. 1 is easy to audit.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Multiple proof gaps (DA-M4, DA-M5, DA-M7) |
| Clarity & Presentation | 58 | Clear idea; undefined §4.3 quantities |
| Novelty & Originality | 46 | Close to RBF networks and WFR for mixtures |
| Significance & Impact | 44 | Not shown beyond d=2 |
| Experimental Validation | 34 | Untuned baselines, no ablation, single runs |
| Reproducibility | 38 | No code, seeds, PDE ground truth |
| Ethical Compliance | 62 | Nothing at stake |

## Overall: 2 | Confidence: 4
Pool position: better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central empirical comparison does not isolate the claimed mechanism and the theory does not support it.

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R4 | (draft) "no discussion of limitations" | dropped → partly folded into the Limitations line | §4.2 and §5 discuss overfitting and future work |
| R2 | (draft) "[CRY25] is mischaracterised" | rewritten as W4 clause + Question with `[verify]` | Cannot confirm from the cited title alone; suspicion, not an error (Hard Rule 10) |
| R3 | (draft) "no societal impact statement" | moved to Minor | Nothing at stake for this work |
| R1 | (draft) "no data splits" | rewritten as W3/W6 with the protocol-sweep result | Not stated after search; no leakage claimed |
| DA | (draft) "Haar cannot fit sawtooth" | rewritten as DA-m1 with the dyadic argument and location | Precise location and reason required |
| R1 | Question on Fig. 2 noise floor | kept under Questions | Depends on figure ticks (not verifiable here) |

Scores unchanged.

---

## Phase 2: EIC Meta-Review and Decision

### Synthesizer, Part A: package for the EIC

**Merged issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Baselines untuned / missing RBF, Fourier-feature, SIREN, PIRBN; single runs | R1-W1, R1-W3, R3-W3, R2-W1, DA-M1, R4-W2 | CONSENSUS-5 (hinges) |
| Claims outrun evidence (3DGS "unified/recover", inverse problems, interpretability) | R2-W3, R4-W1, DA-M3, R1 (C3 verdict) | CONSENSUS-4 (hinges) |
| Novelty of C1/C2 vs. RBF networks / WFR for mixtures; missing related work | R2-W1, R2-W2, R2-W4, R3-W3, DA strongest counter-argument | CONSENSUS-3 |
| Proof gaps (Prop. 3, Thm. 3) and Thm. 1 sign | R1-W5/ERR-1…4, DA-M4, DA-M7, R2-W5 (Thm. 3 weak) | CONSENSUS-3 (hinges) |
| 1D comparison not like-for-like | R1-W2, DA-M6 | CONSENSUS-2 |
| Theory–experiment disconnect (FR unused) | R1-W4, DA-M7 | CONSENSUS-2 |
| Experimental details/reproducibility missing | R1-W6, R4-W2, R3-W4 | CONSENSUS-3 |
| Low dimensionality only (d ≤ 2) | R3-W2, R4-W1, DA | CONSENSUS-3 |
| Value of cross-field idea | R3-S1 vs. R2-W2 / DA counter-argument | SPLIT |
| DA-CRITICAL | none raised | n/a |

**Official output** (script, before EIC weights): official mean Overall 3.00, composite 52.2; spread > 20 flagged only for Significance (22). Integrity scan: no findings. Literature check: no established claim, no text overlap; recommended references limited to verified items or marked `[verify]`.

### EIC Meta-Review (Dr. Helena Marquardt-Okoye)

#### The Case For and Against
- **For acceptance:** A compact, differentiable and interpretable-looking function class with a tidy measure-space description, a plausible bridge between splatting and scientific ML, and a first set of results (Figs. 2–3) where few-parameter splat models fit well. ICLR does accept conceptual framework papers with early experiments.
- **Against acceptance:** The empirical headline rests on untuned and unusually configured baselines at d ≤ 2 with no repeats and no isolating ablation; the first-listed theory contribution has verified proof gaps and is largely classical (RBF universality, parameter-space gradients); the 3DGS "recovery" is a formulation not a derivation; and the two methodological ingredients have uncited close neighbours.

#### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Baselines same lr 10^-4 / 10^4 steps, no tuning statement; KAN 10th-order splines; no RBF/Fourier/SIREN | R1-W1, DA-M1 | §4.2 text; §4.3 | Verified | grep: no tuning/seed statement; "10-th order spline functions"; baselines listed in Figs. 2–3 legends |
| Parameter accounting favours splat vs. Chebyshev; "competes with gold-standard" | R1-W2, DA-M6 | §4.1, Fig. 1 caption | Verified | Paper itself admits splat is "slightly worse" at m=45; with m=90 coefficients Chebyshev would be stronger (derived) |
| Prop. 3 proof uses rank-one A and non-negative µ | R1 ERR-2/3, DA-M4 | App. A | Verified | Read the proof; both steps as stated |
| Thm. 3 Chebyshev step on non-centred quantity | R1 ERR-4, DA-M4 | App. A | Verified | Chebyshev applied to Z, not Z−EZ |
| Thm. 3 rate worse than grid and independent of anisotropy | R2-W5, DA-M5 | §3.1, App. A | Verified | Kernel ε^{-d}ρ(x/ε), fixed scale |
| Thm. 1 A-gradient sign | R1 ERR-1, DA-M7 | §3.2, App. B.2 | Partly correct | Statement and derivation differ in sign; no experiment depends on it (autodiff); possible extraction artifact |
| FR component unused | R1-W4, DA-M7 | §4.1–4.3 | Verified | §4.1 "Wasserstein gradient descent"; §4.2 Adam; params 3×k |
| "Recover 3DGS" overclaimed | R2-W3, R4-W1, DA-M3 | Abstract; §3.2; end of §3 | Verified | §3 end: "pave the way", "We anticipate"; Example 2: autodiff |
| R3's reading that the paper replicates 3DGS successes | R3-S1/W1 | §1 | Overstated | R3 accepts the aspiration; no NVS result exists |
| Novelty vs. WFR-for-mixtures and PIRBN | R2-W1/W2 | §2 | Verified | Not cited in §2/reference list; abstracts read in kept results (levels 3, medium) |
| "[CRY25] described inconsistently with its title" | R2-W4 | §2 | Partly correct | The description and title differ; relation cannot be checked without the abstract (`[verify]`) |
| Fig. 4 caption: Haar "can exactly fit" the sawtooth | DA-m1 | App. C.1 | Verified (minor) | Jumps at multiples of 1/6, non-dyadic |
| ε variance/noise floor question | R1-Q1 | §4.2, Fig. 2 | Unverifiable | Needs figure |

#### Reviewer Weights
| Reviewer | Overall | Confidence | EIC weight | Reason |
|----------|---------|------------|------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error Log items verified at their locations; calibrated; Q on noise floor legitimately left as a question |
| R2 (Domain) | 3 | 4 | 1.0 | Novelty statements match abstracts; one entry ([CRY25]) only partly checkable |
| R3 (Perspective) | 4 | 3 | 0.75 | Rating leans on potential and accepts the 3DGS aspiration; did not note that Example 2 defers to autodiff or that no baseline controls exist |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound, typical review; claim-versus-evidence point verified |
| DA | 2 | 4 | 1.25 | Counter-argument and proof checks verified; no inflated CRITICAL |

#### DA-CRITICAL Rulings
No DA-CRITICAL issues were raised, so none to rule on. EIC cross-check: the DA's most severe items (DA-M1, DA-M4) fail the strict criteria (they concern a missing control and repairable proofs, supporting a weaker claim), so MAJOR is the right level; no test-set selection was stated (grep), so criterion 3 does not apply. **DA ceiling: none.**

#### Final Decision and Justification
The official mean is 3.00; the EIC-weighted rating is 2.87, giving a starting point of **3 (Borderline Reject)**; the composite cross-check (official 52.2, EIC-weighted 50.9) is also in band 3, so the signals agree. I keep the starting point. The decisive verified issues are: (i) the headline comparison (DA-M1, R1-W1) uses untuned baselines and omits the RBF/Fourier controls that the paper's own explanation (locality) calls for, and does not isolate anisotropy; (ii) the first contribution's proofs have three located gaps (ERR-2, 3, 4) in material that is largely classical; (iii) C3 and the abstract's "inverse problems" and "interpretability" wording are not backed by any experiment or derivation. These are fixable and the weaknesses of the type found in accepted papers (single runs, narrow benchmarks) alone would not sink it; what moves it to the reject side is that the main claim is not tested against the explanation the authors themselves give. My pool position: better than about 40% of ICLR submissions. The decision does not exceed the (non-existent) ceiling.

**Final Overall: 3** (ICLR label: "4 on {0,2,4,6,8,10}").

---

## Editorial Decision

# Editorial Decision

## Paper: Splat Regression Models
## Submission ID: iclr26-rubeJmT1XM (evaluation id)
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: theoretical (hybrid)
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Helena Marquardt-Okoye; R1 Methodology Dr. Tomasz Adeyinka-Reyes, R2 Domain Prof. Anselm Rautavaara-Lindgren, R3 Perspective Dr. Mei-Ling Tzeng-Abara, R4 Generalist Dr. Rafael Quintero-Dahl, DA Dr. Ayesha Karimi-Lindqvist

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 52.2
**EIC assessment** (internal): weighted rating 2.87 → starting point 3 · weighted composite 50.9 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**Journal recommendation:** n/a (conference target).

*How a careful panel would likely see this draft; a simulation, not a prediction.*

### Score Summary (script output, with EIC weights; `--venue iclr --final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 44 | 50 | 60 | 50 | 44 | 49.6 | 48.2 | 16 |
| Clarity & Presentation | 54 | 56 | 68 | 58 | 58 | 58.8 | 57.8 | 14 |
| Novelty & Originality | 52 | 50 | 64 | 55 | 46 | 53.4 | 52.1 | 18 |
| Significance & Impact | 48 | 52 | 66 | 52 | 44 | 52.4 | 50.7 | 22 ⚠ |
| Experimental Validation | 36 | 42 | 52 | 44 | 34 | 41.6 | 40.0 | 18 |
| Reproducibility | 38 | 45 | 50 | 46 | 38 | 43.4 | 42.2 | 12 |
| Ethical Compliance | 64 | 66 | 70 | 66 | 62 | 65.6 | 65.0 | 8 |
| **Composite** | 48.1 | 51.5 | 62.2 | 52.9 | 46.3 | **52.2** (before) | **50.9** (after) | |
| Pool position (P%) | 36 | 42 | 66 | 46 | 33 | | | |

Reviewer weights (script): R1 25%, R2 20%, R3 12%, R4 17%, DA 25% of the EIC assessment.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); the label follows the EIC's final Overall 3 |

Spread discussion (Significance ⚠, 22): R3 (66) sees cross-field potential, the others (44–52) see limited evidence. The EIC adopts the lower view because no experiment reaches beyond d=2 and no inverse problem was run.

### Editorial Decision Letter

Dear Authors,

Thank you for submitting "Splat Regression Models" to ICLR. The paper takes an attractive step: it moves the splat representation from rendering into general low-dimensional regression and PDE fitting and describes it with a measure-space formalism.

**Overall Assessment:** The panel found the core idea clear, the formalism tidy and the cross-field link interesting (R3, R4, R2). The reviewers were not convinced that the evidence supports the headline claims, and several derivations need repair.

**Key Strengths Identified by Reviewers:**
1. A compact, differentiable model with explicit gradient formulas and a clean measure-space viewpoint (R1-S1, R2-S1).
2. A cross-field transfer from graphics to scientific ML with a plausible efficiency benefit (R3-S1, R4-S3).
3. Honest reporting of a negative 1D comparison and acknowledged overfitting risk (R1-S2, R4-S2).

**Key Concerns Requiring Attention:**
1. Baselines and controls (CONSENSUS-5): untuned or unusually configured MLP/KAN/PINN baselines, no RBF/Fourier-feature/SIREN/PIRBN comparison, no ablation of anisotropy, single runs (R1-W1, R1-W3, R2-W1, R3-W3, R4-W2, DA-M1, DA-M2).
2. Claims outrun evidence (CONSENSUS-4): "unified framework", "recover the heuristic methods", inverse problems and interpretability have no matching derivation or experiment (R2-W3, R4-W1, DA-M3).
3. Proof gaps and novelty (CONSENSUS-3): Prop. 3 (rank-one A, signed measures), Thm. 3 (Chebyshev step, rate worse than a grid), a sign inconsistency in Thm. 1, and uncited close prior work on RBF networks and on WFR flows for Gaussian mixtures (R1-W5, R2-W1/W2, DA-M4/M5).

No Devil's Advocate CRITICAL issue was raised; the DA's strongest challenge is that the evidence does not isolate splat-specific properties from generic localised RBF expansions.

**Decision: Borderline Reject (3)**

The idea is worth developing, and the weaknesses are fixable. The decision turns on the main empirical claim not being tested against the explanation the paper itself offers (locality), plus proof gaps in the first contribution. A revised version with tuned baselines, an isotropic/RBF ablation, repaired proofs, narrowed claims and at least one experiment that exercises the NVS or an inverse-problem claim would likely be seen differently. Please refer to the Revision Roadmap.

Sincerely,
Dr. Helena Marquardt-Okoye
Editor-in-Chief (meta-reviewer; fictional persona)

### Consensus and Disagreement Map

**Points of consensus (3+ reviewers)**
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Untuned/missing baselines, single runs | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Claims outrun evidence (3DGS, inverse problems, interpretability) | R1, R2, R4, DA | CONSENSUS-4 |
| Novelty vs. RBF networks / WFR for mixtures, missing related work | R2, R3, DA | CONSENSUS-3 |
| Proof gaps and theory not supporting efficiency | R1, R2, DA | CONSENSUS-3 |
| Reproducibility details missing | R1, R3, R4 | CONSENSUS-3 |
| d ≤ 2 only | R3, R4, DA | CONSENSUS-3 |

**Points of disagreement**
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Value/promise of the cross-field transfer | R3 (Overall 4) | R2, DA | The EIC credits the idea but weights evidence: the 3DGS side is untested (Verified), R3 weight 0.75 |
| Severity of novelty gap | R2 (medium) | R3, R4 (fresh combination) | Verified abstracts put C1/C2 at level 3: medium, not "known" |

**Devil's Advocate Highlights**
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Untuned baselines, single runs | Yes: R1, R2, R3, R4 | n/a | n/a |
| DA-M3 | MAJOR | Claim distortion (3DGS, inverse problems, interpretability) | Yes: R2, R4 | n/a | n/a |
| DA-M4 | MAJOR | Proof gaps | Yes: R1 | n/a | n/a |
| (CRITICAL) | none raised | | | | |

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline comparison lacks matched, tuned baselines and controls; attribution to anisotropy untested | R1-W1, R1-W3, R2-W1, R3-W3, DA-M1, DA-M2 | §4.2, §4.3, Figs. 2–3 | Add RBF network (isotropic splats), PIRBN-style, Fourier-feature MLP, SIREN; per-model tuning on a validation split with equal budget; ≥5 seeds; table with mean±std; define metrics and noise floor | Medium; ≈ 10–20 GPU-h | Partly (time-limited) |
| R2 | Claims not matched by evidence (3DGS "unified/recover", inverse problems, interpretability) | R2-W3, R4-W1, DA-M3 | Abstract, §3.2, Example 2, end of §3 | Narrow wording, or provide the exact 3DGS correspondence and one NVS/2D image-fitting or inverse-problem experiment | Low (wording) to High (experiment) | Yes (wording); Partly (experiment) |
| R3 | Proofs: Prop. 3 (rank-one A, signed measures), Thm. 3 (Chebyshev step, normalisation, rate), Thm. 1 sign; main-text/appendix statement mismatch | R1 ERR-1…4, DA-M4, DA-M5, DA-M7 | §3.1, §3.2, App. A, App. B.2 | Repair with a limiting argument or cite classical RBF universality; bound E[Z]; fix sign; align statements | Medium | Yes |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | 1D comparison not like-for-like; parameter accounting | R1-W2, DA-M6 | m=90 Chebyshev, equal data/cost, time-to-error, more targets | Low; < 2 GPU-h | Yes |
| S2 | Fisher–Rao component unused; theory–experiment gap | R1-W4, DA-M7 | Learn masses/birth-death pruning and ablate, or state that parameter-space descent is used | Medium | Partly |
| S3 | Related work: RBF/PIRBN, WFR for Gaussian mixtures, Gaussian Fluids, Park–Sandberg [verify], Rotskoff–Vanden-Eijnden; [CRY25] relation | R2-W1, R2-W2, R2-W4 | Add paragraph and differentiate | Low | Yes |
| S4 | Reproducibility and definitions in §4.3 (ground truth, D, f, norm), code, hardware, wall-clock | R1-W6, R4-W2, R3-W4 | Implementation appendix and code | Low | Yes |
| S5 | Beyond d=2 and sharp interfaces | R3-W2 | 3D problem, ε sweep | Medium | Partly |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Notation: eq. (1) duplicate factor, Example 1 constants, "isotropic" vs. identity covariance | R1 ERR-5/6, R2 Minor | Fix and state spherical symmetry assumption |
| N2 | Fig. 4 caption on Haar and discontinuities; "right to left" remark; Fig. 3 "test" vs. "validation" | DA-m1, R1 Minor | Correct |
| N3 | Duplicate references; [Li24] vs. [LWV+25] | R1 Minor | Clean bibliography |
| N4 | Deep splat networks, compositions, pruning heuristics | R3 | Future work |

### Estimated Revision Effort
- Priority 1: 3 items, ≈ 2–3 weeks (experiments ≈ 10–20 GPU-hours; proofs ≈ 3–5 days).
- Priority 2: 5 items, ≈ 1 week.
- Priority 3: 4 items, ≈ 1 day.
- **Total estimated revision time**: ≈ 3–4 weeks.

---
*Literature-check note: strict mode, cutoff 2025-09-24; 7 queries (claim 5, baseline 1, expansion 1), 67 unique kept results; no gaps flagged; `benchmarks` returned none (synthetic targets) so no baseline scout; search ledger and kept results are in the results directory. Recommended references were verified with `verify` where marked, otherwise marked `[verify]`.*
