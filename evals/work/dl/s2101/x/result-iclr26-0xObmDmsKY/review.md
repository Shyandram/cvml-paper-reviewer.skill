# Simulated Review: "ViscoReg: Neural Signed Distance Functions via Viscosity Solutions"

*Simulation of how a careful panel would likely see this draft; not a prediction of any real outcome. Date: 2026-11-05. Mode: full. Target venue: ICLR (profile `iclr`, 2026 cycle, scale status: secondary). Literature check: strict, cutoff 2025-09-24. Figures were not available (text extracted from the PDF); figure-dependent claims are judged from captions and text only. All five reviewer passes share one model context (no subagents were run); each pass was written from its own role file.*

---

## Phase 0 — Field Analysis and Reviewer Configuration

### 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | ViscoReg: Neural Signed Distance Functions via Viscosity Solutions |
| Primary Discipline | Computer vision / geometry processing → neural implicit surface reconstruction from unoriented point clouds |
| Secondary Discipline(s) | PDE theory (viscosity solutions, Hamilton–Jacobi / Eikonal), physics-informed learning, numerical analysis |
| Paper Type | Empirical (method + benchmark evaluation, with a theory component) (composite weights: empirical) |
| Core Technique(s) | SIREN sine networks, Eikonal loss, vanishing-viscosity (Laplacian) regularization with decaying ε, MFGI initialization, gradient-flow linearization |
| Target Venue | ICLR (top-tier ML) (stated by user); profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution, Rating, Confidence) |
| Paper Maturity | Submission-ready (full paper, supplement included in the text file; figures missing) |
| Ethics-Relevant Content | none (no human data, no deployment-risk content) |

**Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters found. Reviewers read the copy and the paper memory below.

### Claimed Contributions (as stated by the authors, §1)
- **C1** Generalization-error bound for neural SDFs in terms of training error, via viscosity-solution theory (Theorem 2, Eq. 12; "Generalization error bounds are presented…").
- **C2** A novel regularizer: Eikonal loss with a dynamically scaled (decaying) viscosity term, ViscoReg (Eq. 23–24).
- **C3** Justification via gradient flow: stabilizes early training for high-frequency components (§3.3–3.4, Eq. 25–31).
- **C4** Empirical comparison against DiGS and StEik on several datasets showing improvement, "without adding significant computational cost" (abstract, §4).

### Paper memory (shared factual record)
- **Setup facts.** *SRB* (§4.2, §6.2.1): 5 noisy shapes, normals not used; 5 hidden layers × 128; 10,000 iterations, lr 1e-4; 15,000 surface + 15,000 uniform points per iteration; weights [αm, αnm, αe] = [3000, 100, 50]; ε piecewise-linear 1 → 0.8/0.08/0.01/0 at 20/40/60/80% of iterations; shape *lordquas* uses 0.5/0.2/0.05/0; "quad" variant uses StEik architecture with decay at 40%/60% to 0.01/0.0 except *anchor* and *gargoyle* (60%/80% to 0.03/0.0). *Scene* (§4.3, §6.2.2): 8×512, 100k iterations, lr 8e-6, ε 0.5 → 0.01 at 50% → 0 at 60%. *ShapeNet* (§4.4, §6.2.3): 4×256, first 20 test shapes of each of 13 classes (protocol of Williams et al.), 10,000 iterations, lr 5e-5, ε from 1.0 decreasing at 10/20/30/40% to 0, except rifle, lamp, table which start at ε = 10.0. Single RTX A6000. Which p (1 or 2) is used in Eq. 24 for the experiments: **not stated** after search. Seeds / repeated runs / variance: **not stated**. Validation split or protocol for choosing ε schedules: **not stated** (see "benefited", "coarse grid search"). Runtime / memory comparison: **not stated**. Code release: **not stated**.
- **Headline numbers.** Table 1 (SRB): Ours (lin) dC 0.18 / dH 2.96; Ours (quad) 0.18 / 2.73; DiGS 0.19 / 3.52; StEik (lin) 0.20 / 4.56; StEik (quad) 0.18 / 2.80. Table 3 (ShapeNet): ViscoReg (quad) mean squared Chamfer 3.98e-5, IoU mean 0.959; StEik (quad) 6.86e-5 / 0.967. Table 2 (ε-decay ablation, one SRB shape).
- **Supplement adds.** Lemma 1–2 proofs, L2 variant of Theorem 2 (§6.1.3), per-shape SRB numbers (Table 4), per-shape hyperparameters (§6.2), ShapeNet per-class results (Fig. 5), Eikonal-deviation curve (Fig. 6).
- **Unverifiable.** Figures 1–6 (images not available); Fig. 4 appears to repeat Fig. 2 with a longer caption, which cannot be checked from text.

### 👥 Review Team (fictional personas)

**EIC (meta-reviewer): Dr. Anneliese Okonkwo-Reyes**, large public research university (Europe). Senior faculty / geometry processing and learning-based reconstruction; long experience as area chair at ML and vision venues. *Style:* weighs the contribution against what the venue actually accepts; checks every decisive claim in the text herself.

**Reviewer 1 (Methodology): Dr. Priyanka Menezes-Lund**, applied-math and geometry-processing lab, public university (South Asia). Mid-career / PINN-style training, Eikonal solvers, reconstruction evaluation protocols. *Style:* reads proofs line by line and recomputes tables.

**Reviewer 2 (Domain): Prof. Dae-ho Whitlock**, graphics and geometry group, research university (East Asia). Senior faculty / neural implicit surfaces, unoriented point-cloud reconstruction. *Style:* insists on closest-prior-work differentiation.

**Reviewer 3 (Perspective): Dr. Lucía Ferraro-Obuya**, numerical analysis and scientific computing department, university (Latin America). Mid-career / Hamilton–Jacobi numerics, level sets, heat-based distance computation. *Style:* constructive, connects to classical numerics.

**Reviewer 4 (Generalist): Dr. Samuel Achterberg**, industrial research lab (North America). Senior industry scientist / 3D vision generalist. *Style:* typical program-committee member; reads for contribution clarity and venue fit.

**Devil's Advocate: Dr. Noor Haddad-Lindqvist**, independent evaluation-methodology institute (Middle East). Mid-career / evaluation methodology, hyperparameter-selection protocols. *Style:* rigorous, never hostile.

*Personas are fictional.*

---

## Phase 1 — Independent Reports

### Peer Review Report — Reviewer 1 (Methodology)

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Reviewer: Dr. Priyanka Menezes-Lund, Methodology (applied-math and geometry-processing lab; fictional persona)
## Expertise: PINN-style training and Eikonal solvers; reconstruction evaluation protocols; proof checking
## Date: 2026-11-05

**Protocol sweep** (searched the whole text, appendix included): split / tuning statements found: §4.2.1 "a schedule surpassing SoTA may be obtained via coarse grid search"; §6.2.1 "The shape lordquas benefited from a different linear decay setting"; §6.2.1 quad variant: decay differs "for all but anchor and gargoyle"; §6.2.3 "For these shapes, we start the decay at ε = 10.0." (rifle, lamp, table). No validation split or independent selection protocol is stated anywhere. SRB and ShapeNet are evaluated against ground truth; each shape is optimized separately, so these shapes are the test shapes. Shared with the DA.

### Summary
The paper trains neural SDFs from unoriented points by replacing the Eikonal residual with a "viscous" residual ‖∇u‖−1−εΔu, with ε annealed to zero, and motivates this with the vanishing-viscosity theory of Hamilton–Jacobi equations. It adds a Gagliardo–Nirenberg-based L∞ error bound for a trained SIREN in terms of the manifold and Eikonal losses, and a linearized gradient-flow analysis. Experiments compare against DiGS and StEik on the Surface Reconstruction Benchmark, a scene reconstruction task and 13 ShapeNet classes, with small improvements, mostly in Hausdorff distance and mean squared Chamfer.

### Strengths
**S1: Principled motivation that connects to classical numerics.** Casting the ε annealing as vanishing viscosity (Eq. 2, Eq. 24) is a clean idea, and the paper makes the connection to Fast Marching (§1) explicit. The method adds only a Laplacian term to an existing pipeline (§3.4).

**S2: Fair-comparison effort on the StEik axis.** §4.1 separates StEik's regularizer from its quadratic-layer architecture and reports both settings (Table 1, Table 3: "lin" and "quad" rows). This isolates the regularizer, which many papers do not do.

**S3: Useful ablation of the schedule, and an honest limitation.** Table 2 reports the sensitivity to the ε schedule (e.g., "Fast decay (0 @ 20%)" dH 2.34 versus baseline 1.44), and the conclusion states that tuning ε "is" a limitation. The ε = 0 row (SIREN: 0.34 / 6.27) shows the viscous term matters on that shape.

**S4: Broad task coverage.** Three settings (SRB, a room-scale scene, 260 ShapeNet shapes) with both Chamfer-type and IoU metrics (Table 3).

### Weaknesses

**W1: Hyperparameters are chosen per shape and per class on the evaluated shapes, while baselines are reported once.** Quote: "The shape lordquas benefited from a different linear decay setting" (§6.2.1); "For these shapes, we start the decay at ε = 10.0." (§6.2.3, rifle, lamp, table); anchor and gargoyle also get a different quad schedule (§6.2.1); and §4.2.1 says "a schedule surpassing SoTA may be obtained via coarse grid search". No validation shapes or selection rule are given. Table 2 shows how much the schedule matters on the one shape it covers (dC 0.15–0.17, dH 1.34–2.34 against DiGS 0.15 / 1.70). The headline margins are small: Table 1 quad versus StEik quad is dC 0.18 vs 0.18 and dH 2.73 vs 2.80 (2.5% lower, derived). Margins of that size are comparable to what per-shape tuning can buy.
- **Suggested Fix:** report all SRB / ShapeNet results with one fixed schedule (the §4.2 baseline), or select the schedule on held-out shapes or via leave-one-shape-out; report seeds. Cost: SRB is 5 shapes × 10k iterations, a few GPU-hours; ShapeNet 260 shapes ≈ 1 GPU-day.

**W2: The error bound (C1) rests on an assumption that excludes the regime it describes, and on constants that are never controlled.** Assumption 1 requires ‖∇u_θ*‖ ≥ 1/Cθ* > 0 everywhere on Ω, with the domain taken to be "the volume enclosed by the surface" (§3.2). A smooth network that is near zero on ∂Ω and approximates an SDF inside has an interior extremum, hence a point with ∇u = 0. In general, if no critical point exists, every interior point must lie within about 2‖g_θ*‖∞·Cθ* of the boundary along a gradient line, so Cθ* must scale like (inradius)/‖g_θ*‖∞, which is huge when the boundary loss is small. In addition, Theorem 2 depends on M_θ*, a W^{6,1} norm of ‖∇u_θ*‖ and u_θ*|∂Ω for a sine network, which grows with the frequency content needed for fine detail. The bound is never evaluated numerically, and it holds for the plain Eikonal loss, not for ViscoReg (Eq. 24).
- **Suggested Fix:** state Theorem 2 as a conditional statement, quantify (or estimate empirically) M_θ* and Cθ* on the trained SRB networks, and either prove a bound for L_veik or remove the implication that C1 supports C2. Low–medium effort; rebuttal-feasible.

**W3: Lemma 2's dependence on Cf is inverted, and Lemma 2 is applied outside its hypotheses.** See ERR-1 and ERR-2. As printed, Eq. (8) and Eq. (16) say a larger Cθ* tightens the bound, which is the opposite of what the proof's own inequalities give.
- **Suggested Fix:** redo the constants (the correct factor is of order Cf², derived below) and re-derive Lemma 2 for nonzero boundary data.

**W4: The "stability" claim (C3) is a heuristic whose algebra is wrong and whose key sign is assumed.** See ERR-3, ERR-4. The conclusion "stable for high frequencies" requires κe > 0, where κe = sign(1+εΔu−‖∇u‖) changes sign with the pointwise residual; the paper treats it as positive. The same linearization applied to the plain Eikonal flow (ε = 0) also gives non-growing modes (û′ = −ω₁²û for p = 2), so Eq. 26–31 do not by themselves show the instability that ViscoReg is meant to remove.
- **Suggested Fix:** present Eq. 26–31 as an illustration, correct the Fourier signs, state the κe > 0 condition explicitly, and add an empirical stability measurement (training-loss curves over seeds for SIREN, DiGS, StEik, ViscoReg).

**W5: Claims are stated more strongly than Tables 1–3 support (E5).** "Our method is top 2 in every metric compared to SoTA" (Table 3 caption): the IoU mean of ViscoReg (quad) is 0.959, behind StEik (quad) 0.967 and StEik (lin) 0.963, and the median squared Chamfer of ViscoReg (quad) is 2.19e-5 against StEik (quad) 6.33e-6 (3.5× worse, derived). The mean Chamfer gain comes from a smaller tail (std 7.38e-5 vs 3.34e-4). §4.2: "Our method improves upon all other methods in this task." Table 4 shows ViscoReg worse than DiGS and PHASE+FF on lordquas (dH 1.09 vs 0.91 and 0.71).
- **Suggested Fix:** word the claims as "better mean Chamfer, comparable IoU, mixed on SRB", add per-class medians and a paired bootstrap over shapes.

**W6: No evidence for "without adding significant computational cost"** (abstract). No time per iteration, memory or total training time is reported. The Laplacian Δu requires second-order autodiff through a sine MLP, and the baseline SIREN needs only first-order gradients for the Eikonal term. The only cost number is "approximately 25% fewer parameters than DiGs or SIREN" (§4.2), without the baseline's parameter count.
- **Suggested Fix:** a table of seconds per 1k iterations and peak memory for SIREN, DiGS, StEik, ViscoReg on SRB and ShapeNet. About 2 GPU-hours.

**Minor.** Table 1 IGR wo n dH is 16.30 but Table 4 gives 16.33; the ∆dC/∆dH columns are not defined well enough to recompute (e.g., DiGS ∆dC 0.0 with dC 0.19 and best 0.18); Table 4's "StEik" rows equal the quad numbers (per-shape dH mean 2.80) but are compared with the lin ViscoReg row; which p is used is never stated; the Table 2 caption "dc" is ambiguous (the numbers match the DC shape in Table 4).

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | Eq. (8); proof of Lemma 2, Eq. (35)–(37) (§6.1.2) | "∥u1 − u2 ∥∞ ≤ CΩ Cf−2 ∥f1 − f2 ∥∞" | With 1/Cf ≤ f1, one has λ−1 ≤ max(f2−f1)/f1 ≤ Cf‖f1−f2‖∞ (not 1/Cf), and ‖u1‖∞ ≤ diam·sup f1 ≤ C Cf (not Cf⁻¹). The factor should be ≈ Cf², not Cf⁻². | Derived from the paper's own definitions (slowness f, arrival time u) | High | MAJOR | Recompute constants; restate Theorem 2's Cθ* dependence |
| ERR-2 | E3 | Assumption 1 and §3.2 | "it is natural that Assumption 1 holds" | Smooth u_θ* near 0 on ∂Ω and SDF-like inside has an interior critical point, contradicting ‖∇u_θ*‖ ≥ 1/Cθ* > 0 on Ω; otherwise Cθ* ≳ inradius/‖g_θ*‖∞. The justification "the ground truth SDF satisfies ‖∇u‖ = 1" ignores the kink at the medial axis. | Derived (extremum argument; gradient-line length bound) | High | MAJOR | Weaken or replace the assumption; quantify Cθ* |
| ERR-3 | E2 | Eq. (26)–(28), §3.4 | "Taking the Fourier transform of the above PDE gives" | Fourier transform of ∂²_{x₁}u is −ω₁²û, not +ω₁²û; Eq. (27) has the wrong sign. With the correct sign the exponent is −κe(ω₁² + ε²|ω|⁴) and stability requires κe > 0 at all frequencies, not only large ones. Also the linearization of ∇·(∇u/‖∇u‖) about a·x is the transverse Laplacian ∂₂₂+∂₃₃, not ∂²_{x₁}, for the p = 1 flow. | Recomputed | High (sign); Medium (p = 1 operator) | MAJOR | Redo Eq. 26–28 |
| ERR-4 | E2 | Eq. (30) | "Taking the Fourier transform of this fourth order PDE" | The PDE term ε∂ₓ₁(Δu) transforms to −iεω₁|ω|²û; Eq. (30) prints iω₁³û (no ε, wrong power). κe is also used for p = 2 although it is defined only for p = 1 (E6). The real part used for the conclusion is unaffected. | Recomputed | High | MINOR | Correct Eq. (30)–(31) |
| ERR-5 | E5 | Table 3 caption vs. Table 3 | "Our method is top 2 in every metric compared to SoTA" | IoU mean: StEik (quad) 0.967, StEik (lin) 0.963, ViscoReg (quad) 0.959; median Chamfer: StEik (quad) 6.33e-6 vs ViscoReg (quad) 2.19e-5 | Compared rows of Table 3 | High | MAJOR | Reword the claim |
| ERR-6 | E4 | §6.2.1, §6.2.3 | "The shape lordquas benefited from a different linear decay setting" | Hyperparameters chosen by evaluated shapes; baselines not given the same freedom | Cross-referenced §4.2.1, §6.2.1, §6.2.3, Table 2 vs. Table 4 | Medium (selection by score is inferred from "benefited") | MAJOR | Fixed schedule or held-out selection |
| ERR-7 | E1 | Table 1 vs Table 4 | 16.30 vs 16.33 (IGR wo n, dH) | Same quantity, two values | Cross-referenced | High | MINOR | Fix one |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Per-shape tuning on evaluated shapes, theory with errors and an inconsistent assumption |
| Clarity | 2 | Readable, but p, ∆ columns and table labels are underspecified |
| Significance | 2 | Small margins on a mature benchmark; theory not usable |
| Originality | 2 | Annealed viscous residual is a modest variant of annealed Laplacian regularization |

### Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the margins over StEik/DiGS are small and obtained with per-shape schedules; the theory contains verified errors and an assumption that fails in the regime it addresses.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | ERR-1–4; bound not connected to ViscoReg |
| Clarity & Presentation | 58 | Competent | Understandable; undefined ∆ columns, p unstated |
| Novelty & Originality | 50 | Developing | Modest variant; see R2 |
| Significance & Impact | 50 | Developing | Niche, small gains |
| Experimental Validation | 44 | Developing | Single runs, per-shape tuning, ablation on one shape |
| Reproducibility | 56 | Competent | Per-shape settings listed in supplement; p, seeds, code not stated |
| Ethical Compliance | 60 | Competent | Nothing at stake; one limitation stated |

### Questions for Authors
1. Which p (1 or 2) produced Tables 1–3? If p = 2, is the ε²(Δu)² term in the expansion of Eq. 24 not exactly a DiGS-style Laplacian penalty with weight ε²? (A convincing answer that separates ViscoReg from DiGS would raise my novelty and rigor scores.)
2. How were the per-shape and per-class schedules chosen (§6.2.1, §6.2.3)? What are SRB and ShapeNet results with the single baseline schedule? (Single-schedule results that keep the margins would raise Experimental Validation by ~10 points; a loss of the margins would lower it.)
3. What are the seed-to-seed standard deviations for dC/dH on SRB?
4. What are Mθ* and Cθ* for your trained networks, and how large is the bound of Eq. 12 numerically?
5. How were the StEik (lin) numbers in Table 1 and DiGS/StEik numbers in Table 3 obtained (copied or re-run, same tuning effort)?

### Limitations Assessment
**Partially.** The paper names ε tuning as a limitation, but not per-shape tuning, missing variance, cost, or the gap between the bound and the method.

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject):** An interesting, cheap idea with some support, but the per-shape tuning, the small margins, and the flawed theory leave the central "outperforms StEik/DiGS and is theoretically justified" claim unsupported as written.

### Confidence
**4:** Checked the proofs and the tables line by line; figures unavailable.

---

### Peer Review Report — Reviewer 2 (Domain)

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Reviewer: Prof. Dae-ho Whitlock, Domain (graphics and geometry group; fictional persona)
## Expertise: neural implicit surfaces; unoriented point-cloud reconstruction; Eikonal-based regularization
## Date: 2026-11-05

### Summary
The paper proposes a loss for learning SDFs from raw points that adds a decaying viscosity term εΔu inside the Eikonal residual, and derives an L∞ bound for SIREN-based neural SDFs. It claims improved stability and reconstruction relative to DiGS and StEik. Related work is organized into classical reconstruction, INRs and neural PDE solvers (§2).

### Strengths
**S1: Well-chosen, well-explained theoretical lens.** Linking the Eikonal ill-posedness to viscosity solutions (§1, §3.2) is a natural and pedagogically useful framing that the neural-SDF community has used little; the 1-D zig-zag example (§3.2) is clear.

**S2: Appropriate benchmarks and the right strong baselines.** DiGS and StEik are the right comparisons, and PHASE, SAL, IGR and VisCo Grids are included in Table 1; Table 3 follows the Neural Splines protocol with 13 classes.

**S3: Honest positioning against StEik and DiGS in text.** §2.2 states criticisms of each (Laplacian minimization smooths fine detail; directional divergence may be redundant when the Eikonal is satisfied), which makes the intended contrast clear.

### Weaknesses

**W1: The distinction from DiGS is overstated, and the closest-prior-work delta is thin.** §3.4 says ViscoReg "is different from the DiGS loss because we do not want to minimize the divergence". For p = 2, expanding Eq. 24 gives (‖∇u‖−1)² − 2ε(‖∇u‖−1)Δu + ε²(Δu)², i.e., a squared Laplacian penalty with weight ε² plus a cross term; Eq. 29 itself contains −ε²Δ(Δu). With ε annealed to zero on a piecewise schedule that is described as "a similar annealing strategy" to DiGS (§4.2), the practical difference is the cross term and the schedule. Table 2 is the only ablation, and it has no row isolating DiGS-style Laplacian annealing with the same schedule. VisCo Grids [43], which already applies viscosity to the Eikonal problem, is described as "non-neural … with a fixed non-decaying viscosity coefficient" (§2.1), so the delta over it is also the decay and the network.
- **Suggested Fix:** add an ablation: ViscoReg versus Eikonal + annealed Laplacian (DiGS) with the identical schedule and MFGI initialization, on all five SRB shapes; state p.

**W2: Contribution C1 is a loose extension of existing PINN theory, and "first such estimate" is not established.** The proof follows Mishra and Molinaro [37] with the Eikonal comparison principle and Gagliardo–Nirenberg interpolation; the novel pieces are Lemma 1–2 (classical comparison and stability) and a quadrature assumption. The statement "To the best of our knowledge, this is the first such estimate" is made without discussing HotSpot, which (per its abstract in the literature check) designs a screened-Poisson-based loss that is an "asymptotically sufficient condition" for convergence to a true distance function and analyzes Eikonal stability. Also, the bound is for the plain Eikonal loss; the viscous loss that is the paper's method has no analogue (§3.2 vs §3.4).
- **Suggested Fix:** cite and differentiate HotSpot and the other work below; restrict the "first" claim; either prove a bound for L_veik or say it is not covered.

**W3: Unsupported or inconsistent attributions (E7).** "introduced by Karniadakis et al. [24]" (§2.3): reference [24] is a review, *Physics-informed machine learning* (Nature Reviews Physics), not the PINN paper. The scene benchmark is attributed to "Sitzmann et al. [48]" in §4.1 but "[47]" in §4.3 and Fig. 2, and Table 2 labels ε = 0 as "SIREN [47]" while §2.2 cites SIREN as [48] ([47] is Scene Representation Networks). These do not change results but weaken scholarship.
- **Suggested Fix:** cite Raissi et al. for PINNs and correct [47]/[48].

**W4: Missing comparison with other unoriented-point-cloud neural methods.** Neural-Singular-Hessian (arXiv 2309.01793, found by the literature check; prior, arXiv-only) targets the same task with a Hessian-based regularizer and is not cited or compared; the paper's related work covers only the gradient-Hessian alignment of [50]. This is a MAJOR-at-most omission (ledger label: prior, arXiv-only 6+ months before the cutoff).
- **Suggested Fix:** cite and discuss; compare on SRB if the authors' numbers are available (copying published numbers is acceptable with settings stated).

**W5: Significance of the result.** Gains over the state of the art on SRB are 0.01 in dC and 0.07 in dH for the quad variants (Table 1; 2.5% in dH, derived). The ShapeNet table shows better mean squared Chamfer but lower IoU than StEik in both settings (Table 3). For the field's current bar (see snapshot below), these are incremental results.
- **Suggested Fix:** broaden the claim to what is shown, and add a setting where a stability gain is the point (e.g., high-frequency or thin structures with quantitative metrics, not only Fig. 1–2 captions).

**Minor.** Notation: Eq. 2 and Eq. 24 sign conventions for u (positive inside vs. negative inside) are not stated, although the SDF is signed and the viscosity solution of |∇u| = 1 on the enclosed volume is the positive distance; Table 2 caption "dc"; "VisCo Grids" vs "ViscoGrids".

### Literature-check addendum
*Strict mode, cutoff 2025-09-24, 5 search queries run (3 claim queries C1–C3, 1 baseline query, 1 additional claim query); 22 candidate results; similarity run. Gaps left open: the C2 query ("viscosity", Eikonal, neural) kept nothing, no expansion queries, `scout` not run (only the paper's SRB/ShapeNet benchmarks, whose abstracts report no comparable numbers). arXiv-only coverage; results are pointers, not verdicts.*

**Per-claim novelty (claim-level profile, entailment levels estimated by hand from abstracts and the paper's own text)**

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------------|-----------|
| C1 error bound | result | medium | Mishra & Molinaro, PINN generalization estimates (level 3, https://arxiv.org/abs/2006.16144, prior, cited [37]); HotSpot (level 3, https://arxiv.org/abs/2411.14628, prior arXiv-only, not cited) | Method of proof reused; Eikonal viscosity application new; HotSpot gives a different sufficiency guarantee |
| C2 decaying viscous Eikonal residual | method | incremental | VisCo Grids [43] (level 4, cited, differentiated by non-neural/fixed ε); DiGS [5] (level 3, annealed Laplacian, cited) | Core mechanism (viscosity inside the Eikonal loss, annealed) is covered by two cited works; difference is the neural setting and decay |
| C3 gradient-flow stability | result | medium | StEik [52] (level 3–4, https://arxiv.org/abs/2305.18414, prior, cited) | StEik already analyzes the gradient flow of the Eikonal loss; the linearization here differs in the regularizer |
| C4 empirical gains | result | high (no close prior found in this search) | — | Numbers are new; margins small |

**Novelty delta table**

| Claimed contribution | Closest prior work (link) | What that work already does | What is new here | Cited and differentiated? |
|----------------------|---------------------------|-----------------------------|------------------|---------------------------|
| Decaying viscosity in Eikonal loss | StEik (https://arxiv.org/abs/2305.18414) | Gradient-flow analysis, stabilization for neural SDFs from points | Viscous residual with annealed ε | Yes |
| Distance-function guarantee | HotSpot (https://arxiv.org/abs/2411.14628) | Loss from screened-Poisson solution that is an asymptotically sufficient condition for a true distance function, stable optimization | Viscosity-solution error bound for plain Eikonal loss | No (not cited) |
| Unoriented point-cloud regularizers | Neural-Singular-Hessian (https://arxiv.org/abs/2309.01793) | Hessian-singularity regularization for unoriented points | — | No |

Text overlap flags: none (shared 8-grams = 0 for all three closest prior works; cosine 0.22 / 0.22 / 0.22 against StEik, HYVE, HotSpot, below the 0.30 threshold). Closest prior work as a whole: StEik, then HotSpot.

**Baseline scout.** Not run: ShapeNet (Chamfer, IoU) is the only external benchmark detected, and the kept abstracts report no comparable numbers. Under-reported baselines: none verifiable.

**Field snapshot.** Five years ago, SIREN-based neural SDFs trained with the Eikonal loss and normals (IGR, SAL/SALD) dominated; unoriented-point training then became the open problem, addressed by DiGS (Laplacian), StEik (divergence/stability, quadratic layers), Hessian-based and gradient-alignment methods, and, more recently, heat- and Poisson-based losses (HotSpot, 2024; a 2025 variational heat-distance preprint, a recent preprint, discussed only). The current accepted bar on SRB is dH around 2.7–3.5 with dC ≈ 0.18; improvements of ~0.01 dC are within the spread of baselines. What counts as significant now is a change that gives stable training without per-shape tuning, a guarantee that bears on the actual loss, or a clear gain on thin or high-frequency structure under a quantitative metric. I use this to put Novelty and Significance at "incremental to modest" (50–52).

### Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Wang et al. [authors verify], *HotSpot: Signed Distance Function Optimization with an Asymptotically Sufficient Condition*, arXiv 2411.14628 (2024; venue [verify]) | Same goal (guarantee + stability for neural SDFs from the Eikonal's weaknesses); must be positioned against the "first" claim |
| Important | Wang et al. [authors, venue verify], *Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian*, arXiv 2309.01793 (2023) | Same task, competing regularizer |
| Important | Raissi, Perdikaris, Karniadakis, *Physics-informed neural networks…*, J. Comput. Phys., 2019 | The actual PINN source; [24] is a review |
| Helpful (worth discussing, recent preprint; not required) | *SDFs from Unoriented Point Clouds using Neural Variational Heat Distances*, arXiv 2504.11212 (2025) | Recent preprint replacing the Eikonal equation with the heat method |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory loosely tied to the method; margins small |
| Clarity | 2 | Positioning clear, citations inconsistent |
| Significance | 2 | Incremental in a mature sub-area |
| Originality | 2 | Variant of annealed Laplacian / VisCo-Grids idea |

### Dimension Scores (0–100)
**Pool position:** better than about 47% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the core mechanism is covered by two cited works, and the result margins are small.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Competent | Framework sound in outline; bound loosely tied to the method |
| Clarity & Presentation | 60 | Competent | Well organized; citation slips |
| Novelty & Originality | 50 | Developing | See delta table |
| Significance & Impact | 52 | Developing | Small gains |
| Experimental Validation | 52 | Developing | Right baselines, thin ablation |
| Reproducibility | 58 | Competent | Settings listed |
| Ethical Compliance | 60 | Competent | Nothing at stake |

### Questions for Authors
1. Is ViscoReg (p = 2) distinguishable in practice from DiGS with the same annealing schedule? An ablation showing a consistent gap would raise my Novelty score.
2. How does Theorem 2 relate to a model trained with L_veik?
3. How does the method differ from HotSpot in the guarantee it provides?

### Limitations Assessment
**Partially.** ε tuning is mentioned; the gap between theory and the proposed loss is not.

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject):** A tidy idea with partial novelty over DiGS/VisCo Grids, a bound that does not cover the method, and small, partly tuned gains.

### Confidence
**4**

---

### Peer Review Report — Reviewer 3 (Perspective)

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Reviewer: Dr. Lucía Ferraro-Obuya, Perspective (numerical analysis and scientific computing department; fictional persona)
## Expertise: Hamilton–Jacobi numerics; level sets and distance computation; stability of regularized flows
## Date: 2026-11-05

### Summary
The authors bring vanishing-viscosity ideas from Hamilton–Jacobi numerics to the training of neural SDFs: the Eikonal residual is augmented with εΔu and ε is decreased during training, much as a numerical solver reduces artificial viscosity. A linearized gradient-flow analysis and an L∞ bound for the trained network accompany the loss. Experiments show reconstruction gains on SRB, a room-scale scene and ShapeNet.

### Strengths
**S1: Right instinct from numerical PDE practice.** In classical solvers, adding viscosity and then letting it vanish (or using an upwind scheme that does so implicitly) is how one selects the physical solution among many Lipschitz solutions; transferring that to neural training (§1, §3.4) is a sensible bridge between communities.

**S2: A continuation / annealing mechanism that is cheap and general.** The decaying ε is, from an optimization view, a continuation method (smooth problem first, sharp problem last), and the paper's Mandelbrot example (Fig. 1, from caption: DiGS and StEik fail to keep the boundary connected) is a good stress test of fine structure.

**S3: Identification of a real issue.** The forward–backward diffusion structure of the Eikonal gradient flow (§3.3, resemblance to Perona–Malik) is a good diagnostic and links the instability to a well-studied class of equations.

**S4: Modest cost of adoption.** The method is a drop-in loss change on top of SIREN, with a single new scalar schedule (§4.2).

### Weaknesses

**W1: The analysis is local and one-sided.** The stability argument linearizes around u₀ = a·x with a fixed direction (§3.4) and takes κe > 0. Numerical analysts would also want the nonlinear regime near the medial axis, where the SDF has kinks and viscosity does its real work (the sign of Δu there is what the viscosity solution picks). The paper never states the sign convention of its SDF, though the viscosity solution of |∇u| = 1 on the enclosed volume is the positive distance, while neural SDFs are usually negative inside.
- **Suggested Fix:** state conventions; add a 1-D or 2-D experiment where the neural solution is compared with the exact viscosity solution as ε decays (the 1-D zig-zag example of §3.2 is ideal).

**W2: Natural connections to other fields are missing.** Heat-based distance computation (Crane et al.), level-set methods (Osher–Sethian), and PINN failure-mode studies with curriculum-style regularization (Krishnapriyan et al.) address the same ill-posedness and would sharpen both the motivation and the comparisons.
- **Suggested Fix:** a short discussion paragraph and, ideally, a heat-method-style baseline.

**W3: Practical hyperparameter burden is understated.** The annealing schedule needs breakpoints, values and, per Table 2, shows noticeable sensitivity; the paper says ε-tuning is a limitation but frames the decay as adding no hyperparameters (§4.2). For deployment on new scenes (mapping, robotics) a rule is needed.
- **Suggested Fix:** a recommended default and a sensitivity plot across all SRB shapes; the adaptive-ε idea in the conclusion is the natural next step.

**W4: Assumptions on the data.** Assumption 2 ("Ignoring measurement errors, we consider the sampling process to be deterministic") conflicts with SRB, which is noisy by design (§4.2), and with the fresh random samples drawn at each iteration (§6.2.1).
- **Suggested Fix:** discuss noise robustness and, if possible, add a noise-level sweep.

**Minor.** No broader-impact discussion; acceptable for this topic (no human data).

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Local analysis and unreported variance |
| Clarity | 3 | Motivation clear |
| Significance | 3 | Bridge with numerical PDE practice is valuable |
| Originality | 3 | New for neural SDFs |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a sensible, cheap idea with a sound conceptual bridge, and results that go in the right direction on all three tasks.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound framing, local analysis |
| Clarity & Presentation | 64 | Competent | Clear narrative |
| Novelty & Originality | 64 | Competent | New for neural SDFs |
| Significance & Impact | 64 | Competent | Useful bridge |
| Experimental Validation | 58 | Competent | Broad but thin on variance |
| Reproducibility | 60 | Competent | Settings listed |
| Ethical Compliance | 64 | Competent | Nothing at stake |

### Questions for Authors
1. Does the learned solution match the exact viscosity solution in 1-D as ε decays (a result that would raise my significance score)?
2. What is the sign convention of u, and does it matter for Eq. 2?
3. How robust is the method to ε-schedule choice on new data?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**4 (Borderline Accept):** A conceptually well-motivated, cheap method whose theory is imperfect but whose idea is worth the community seeing.

### Confidence
**3:** Did not recompute tables in detail.

### Missing References (optional)
Crane, Weischedel, Wardetzky, *Geodesics in Heat*, ACM TOG 2013; Osher and Sethian, *Fronts propagating with curvature-dependent speed*, J. Comput. Phys. 1988; Krishnapriyan et al., *Characterizing possible failure modes in physics-informed neural networks*, NeurIPS 2021.

---

### Peer Review Report — Reviewer 4 (Generalist)

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Reviewer: Dr. Samuel Achterberg, Generalist (industrial research lab; fictional persona)
## Expertise: 3D vision (general)
## Date: 2026-11-05

### Summary
The paper adds a decaying viscosity term to the Eikonal loss for learning SDFs from point clouds, provides a generalization-style bound and a gradient-flow analysis, and reports improvements over DiGS and StEik on SRB, a scene reconstruction task and ShapeNet.

### Strengths
**S1: Clear problem and a simple core idea.** The introduction states the Eikonal ill-posedness and the viscosity remedy in a way a non-specialist can follow (§1, Eq. 2).

**S2: Reasonable evaluation breadth.** SRB, a scene, and 13 ShapeNet classes with both Chamfer and IoU (§4.2–4.4).

**S3: Transparent about some settings.** Per-dataset hyperparameters and ε schedules are listed in the supplement (§6.2), and the conclusion acknowledges the ε-tuning limitation.

### Weaknesses

**W1: The paper tells two stories that are not connected.** The theory (Theorem 2) is about the plain Eikonal loss and a trained SIREN; the method (Eq. 24) is a different loss. The intro frames the theory as "validating" the method, but no result in §3.2 applies to ViscoReg, and the bound is never evaluated (§3.2, Conclusion: "difficulty in practical validation").
- **Suggested Fix:** present the theory as a separate, clearly labeled result or extend it to L_veik.

**W2: Table 3's caption and the surrounding text overstate the result.** "Our method is top 2 in every metric compared to SoTA" is not what the table shows for the mean IoU (ViscoReg (quad) 0.959; StEik 0.963 and 0.967), and the text says the table shows "quantitative and qualitative improvements with respect to the state of the art". A reader sees a mixed result: better mean Chamfer, lower IoU than StEik.
- **Suggested Fix:** reword; report medians and per-class results in the main paper.

**W3: Presentation of the tables and the supplement.** Table 1's ∆dC and ∆dH columns are not defined; "wo n" is not explained; Table 4 labels the StEik rows without lin/quad while the main table has both; the SRB ablation (Table 2) is on a single shape without saying so in the caption; and the qualitative claims (Fig. 1, 2) are central but come with only captions, so a reader must trust the text.
- **Suggested Fix:** define the columns, label the shape in Table 2, show a random (not curated) subset of ShapeNet reconstructions.

**W4: No cost or variance information.** The abstract's "without adding significant computational cost" has no timing, and no table has error bars.
- **Suggested Fix:** add a runtime table and 3–5 seeds on SRB.

**Minor.** Typos / citation slips ([47] vs [48]; "VisCo Grids"/"ViscoGrids"); "dc" in the Table 2 caption.

### Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly | Tables 1–3; claims exceed evidence |
| Soundness: theory correct | Partly | §3.2, §3.4 |
| Presentation | Partly | tables, caption issues |
| Contribution: significance | Partly | small margins |
| Experiments reproducible | Partly | §6.2, p and code not stated |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mixed evidence |
| Clarity | 2 | Table labels, caption claims |
| Significance | 2 | Small gains |
| Originality | 2 | Modest variant |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, simple idea, but gains small and the claims stated more strongly than the tables support.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Theory/method disconnected |
| Clarity & Presentation | 56 | Competent | Table definitions missing |
| Novelty & Originality | 52 | Developing | Modest |
| Significance & Impact | 54 | Developing | Small gains |
| Experimental Validation | 50 | Developing | Single runs, one-shape ablation |
| Reproducibility | 58 | Competent | Settings listed |
| Ethical Compliance | 60 | Competent | Nothing at stake |

### Questions for Authors
1. Which p do the experiments use?
2. Can you provide a runtime and memory comparison?
3. Why does ViscoReg have a lower IoU than StEik in both settings (Table 3)?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject):** A clear idea, but the evidence is thinner than the claims, and I would want the theory-method link and the tuning protocol fixed.

### Confidence
**3**

---

### Devil's Advocate Report

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Reviewer: Dr. Noor Haddad-Lindqvist, Devil's Advocate (independent evaluation-methodology institute; fictional persona)

### Steelman
Neural SDF training from unoriented points is unstable because the Eikonal equation has many solutions; borrowing the vanishing-viscosity device from classical solvers gives a principled, cheap regularizer, and across three benchmarks it matches or beats the best published methods with fewer parameters.

### Core Argument Chain
1. The Eikonal equation is ill-posed; the SDF is its unique viscosity solution (§1, §3.2).
2. Therefore minimizing the Eikonal residual at finitely many points need not give the SDF, and the gradient flow is forward–backward and unstable (§3.3).
3. Adding a decaying viscosity term selects the viscosity solution and stabilizes high frequencies (§3.4).
4. Theory bounds the error of a trained network by its training loss (Theorem 2).
5. Experiments show improvements over DiGS and StEik at no significant cost (§4).

∴ ViscoReg is a theoretically justified improvement over the state of the art.

### Strongest Counter-Argument
The improvement in step 5 is not separated from tuning, and the theory in steps 3–4 does not touch the method. The only place that varies the key ingredient, Table 2, covers one SRB shape, and on that shape most alternative schedules are *worse than DiGS* in dC (0.16–0.17 vs 0.15) and several are worse in dH (Piecewise Const. 1.82, Quintic 2.11, Fast decay 2.34, against DiGS 1.70), while the authors write "a schedule surpassing SoTA may be obtained via coarse grid search". The supplement then shows per-shape and per-class departures from the default schedule (lordquas, anchor, gargoyle; rifle, lamp and table with ε starting at 10.0), described as the shape having "benefited". SRB and ShapeNet have no validation shapes: each shape is optimized separately and scored against its own ground truth, so the shapes used to pick ε are the shapes reported. DiGS and StEik are reported with their published settings. Under these conditions, margins of 0.01 dC and 0.07 dH (quad vs StEik) cannot be attributed to the regularizer. Meanwhile, Theorem 2 speaks about the plain Eikonal loss; its Assumption 1 cannot hold for a smooth SDF-like network on the enclosed volume, and its constants (a W^{6,1} norm of a sine network) are uncontrolled. The training-stability claim relies on a linearization with a sign error and a sign assumption (κe > 0). So neither the "theoretically justified" nor the "outperforms" half of the title claim stands on its own, and the paper's own ablation hints that the gain depends on tuning that the baselines did not receive.

### Issue List

#### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence (criterion 3: selection on the reported shapes) | §4.2.1, Table 2 vs Table 4; §6.2.1; §6.2.3; Tables 1 and 3 | Selection quotes: "a schedule surpassing SoTA may be obtained via coarse grid search" (§4.2.1); "The shape lordquas benefited from a different linear decay setting" (§6.2.1); "For these shapes, we start the decay at ε = 10.0." (§6.2.3). SRB has no validation split (ground truth meshes are the evaluation), and ShapeNet shapes are optimized one by one and scored against their own ground truth, so these are held-out test sets under the DA criteria. The selected schedules produce the headline values (Table 2's BL row = Table 4 DC row 0.15 / 1.44; Table 1 "Overall" averages the per-shape rows). On the one shape with a sweep, the comparison with DiGS does not hold at the other swept values (dC 0.16–0.17 vs 0.15; dH 1.82, 2.11, 2.34 vs 1.70). Baselines are not tuned per shape. | Re-run SRB and ShapeNet with one fixed schedule (or select on held-out shapes), and re-report with seeds; show StEik and DiGS with equal tuning freedom | New experiments (≈ 1–2 GPU-days) |

*Note on strength: the paper does not say "we selected by the test score" in so many words; "benefited" and "coarse grid search" imply it. On lordquas the tuned ViscoReg still loses to DiGS (dH 1.09 vs 0.91), so not every special setting visibly helps. The issue is raised as CRITICAL because disclosure does not make test-selected numbers valid and the main comparison does not survive the sweep in Table 2.*

#### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic | §3.2, Thm 2, Eq. 12 vs §3.4, Eq. 24 | The theorem covers the plain Eikonal loss; the method has no bound; the bound is never evaluated; Assumption 1 is incompatible with a small-boundary-loss SDF-like network (extremum argument) | Prove for L_veik or decouple the claims; drop or weaken Assumption 1 |
| DA-M2 | Evidence (claim distortion, E5) | Table 3 caption, §4.2, §4.4, abstract | "Our method is top 2 in every metric compared to SoTA"; IoU mean ranks 3rd (0.959 vs StEik 0.967/0.963); median Chamfer (quad) 2.19e-5 vs StEik 6.33e-6; "Our method improves upon all other methods in this task." Abstract says "outperforms … StEik" while quad ties on dC | Narrow the claims |
| DA-M3 | Novelty | §3.4, Eq. 24, 29 | "we do not want to minimize the divergence with this formulation" vs. ε²(Δu)² in the expansion for p = 2; the delta against DiGS is the cross term and schedule | Ablation vs annealed-Laplacian with same schedule |
| DA-M4 | Evidence | Abstract; §4 | "without adding significant computational cost" has no measurement | Runtime/memory table |
| DA-M5 | Rigor | §3.4, Eq. 26–31 | Fourier sign error, the ∂²ₓ₁ operator for p = 1, κe > 0 assumed; the linearization of the unregularized flow is already non-growing | Correct and reframe as illustration |
| DA-M6 | Rigor | Tables 1–3 | Single runs, no variance; gains 0.01–0.07 | 3–5 seeds, paired bootstrap |

#### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 1 vs Table 4 | IGR wo n dH 16.30 vs 16.33; Table 4 "StEik" rows equal the quad numbers while compared with lin ViscoReg |
| DA-m2 | Citation | §2.3, Table 2, §4.1/§4.3 | [24] is a review; [47] vs [48] |
| DA-m3 | Clarity | Table 1 | ∆ columns undefined; p unstated |

### Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| ViscoReg (lin) overall dH (Table 4 rows 5.36, 2.94, 1.44, 3.96, 1.09) | 2.96 | 2.96 | Yes |
| DiGS overall dH (7.19, 3.72, 1.70, 4.10, 0.91) | 3.52 | 3.52 | Yes |
| StEik overall dH (4.26, 1.72, 1.73, 4.49, 1.81) | 2.80 | 2.80 | Yes |
| ViscoReg (quad) overall dH (4.18, 1.98, 1.35, 4.50, 1.69) | 2.73 | 2.74 | Rounding-level difference |
| Table 3: mean squared Chamfer, quad ViscoReg vs StEik | 3.98e-5 vs 6.86e-5 | 42% lower | Yes (derived) |
| Table 3: median squared Chamfer, quad | 2.19e-5 vs 6.33e-6 | 3.5× higher for ViscoReg | Contradicts "top 2 in every metric" framing |
| Table 2 vs Table 4: BL, DiGS, SIREN rows for DC | 0.15/1.44; 0.15/1.70; 0.34/6.27 | Equal to Table 4 DC rows | Yes: Table 2 is one shape |

### Ignored Alternative Explanations
- Gains come from the schedule or the extra tuned hyperparameters rather than from the viscosity argument (annealed Laplacian + cross term would behave the same).
- The initialization (MFGI from DiGS) and the weights [3000, 100, 50] may matter more than the regularizer; no controlled study.
- Reduced model size (5×128) could explain part of the effect by acting as capacity regularization.
- Mean Chamfer gains in Table 3 are driven by fewer catastrophic failures (std 7.38e-5 vs 3.34e-4), which a few seeds or a failure analysis would reveal.

### Missing Stakeholder Perspectives
Practitioners who need a default schedule for new scenes; users who care about runtime (autodiff of Δu).

### Observations (Non-Defects)
The ε = 0 row of Table 2 isolates a large effect of the viscous term relative to SIREN; the supplement lists the per-shape settings openly, which is what makes the selection issue visible; the stability intuition about forward–backward diffusion is a valuable diagnostic.

### Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Verified errors; theory detached |
| Clarity & Presentation | 58 | Readable |
| Novelty & Originality | 46 | Delta vs DiGS/VisCo Grids thin |
| Significance & Impact | 46 | Small gains |
| Experimental Validation | 38 | Per-shape tuning on test shapes, single runs |
| Reproducibility | 52 | Settings listed; p, seeds, code missing |
| Ethical Compliance | 58 | Nothing at stake |

**Pool position:** better than about 36% of submissions to ICLR.

## Overall: 2 | Confidence: 4

---

## Phase 1.5 — Literature check summary
Mode strict, cutoff 2025-09-24, 5 queries (4 claim-tagged, 1 baseline), no expansion queries; 1 claim query returned nothing usable; `similarity`: no high-overlap or text-overlap flag. Ledger: `search_ledger.jsonl`, `kept_results.jsonl` in this directory. Recent preprint listed as "worth discussing" only: arXiv 2504.11212. No weakness in the reports rests on recent, concurrent or newer work.

## Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | W4 missing Neural-Singular-Hessian | rewritten | Verified in ledger as prior, arXiv-only; kept as MAJOR-at-most, not a required baseline |
| R2 | W2 "first such estimate" | rewritten | Tied to HotSpot abstract from the literature check, not to memory |
| R3 | no broader-impact discussion | moved to Minor | Nothing at stake; not substantive |
| R4 | Fig. 4 vs Fig. 2 look duplicated | dropped | Cannot be checked from text (E9 requires page images) |
| R1 | p-value of the "∆" columns not recomputable | moved to Minor/Questions | Definition unclear; extraction cannot settle it |
| R3 | W1 sign convention | kept, phrased as a question-level concern | The paper does not state it; no verified error |
| DA | DA-M5 linearization operator for p = 1 | kept, confidence Medium | Derived; sign error (ERR-3) is the high-confidence part |
| All | Weaknesses ordered by severity | moved cosmetic items into one Minor line | Per skill |

Scores unchanged.

## Synthesizer package (Part A)

**Consensus map.** CONSENSUS-4: claims overstated vs tables and tuned/limited evidence (R1-W5, R2-W5, R4-W2, DA-M2) ; CONSENSUS-4: theory not connected to the method (R1-W2, R2-W2, R4-W1, DA-M1); CONSENSUS-3: no variance or cost evidence (R1-W6, R4-W4, DA-M4/M6); CONSENSUS-2: novelty vs DiGS thin (R2-W1, DA-M3); CONSENSUS-2: per-shape tuning (R1-W1, DA-C1); SOLO: Lemma 2 constant inversion (R1-W3), Fourier algebra (R1-W4/DA-M5), citation slips (R2-W3). SPLIT: overall value of the idea (R3 positive vs R1/R4/DA). DA-CRITICAL: DA-C1. Issues the outcome may hinge on: DA-C1, the theory defects, Table 3 claim wording.

**Official aggregate (before EIC)** `before.json`: official mean Overall 3.00; composite 53.5 → 3; DA cap provisionally 3; ICLR (secondary scale) rating 4 on {0,2,4,6,8,10}.

---

# Editorial Decision

## Paper: ViscoReg: Neural Signed Distance Functions via Viscosity Solutions
## Submission ID: iclr26-0xObmDmsKY
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Anneliese Okonkwo-Reyes; R1 Methodology, R2 Domain, R3 Perspective, R4 Generalist, DA as above

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 53.5
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite per `aggregate.json` → band 3 (cross-check agrees) · **DA ceiling**: 3 · **Final (EIC)**: 3 · ICLR rating label from `aggregate.json`

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A cheap, intuitive regularizer motivated by classical vanishing viscosity; results go in the right direction on three tasks and on mean Chamfer / Hausdorff against DiGS; theory is an honest attempt to connect neural SDFs to PDE analysis; the supplement lists settings openly.
- **Against acceptance:** The improvement over the closest baseline (StEik, quad) is tiny, partly with schedules chosen per shape/class on the evaluated shapes and with no variance; the theorem concerns a different loss, rests on an assumption that cannot hold in the regime it describes and has an inverted constant; the stability analysis has a sign error and an assumed sign; the abstract's "outperforms" and "no significant computational cost" claims are not supported as worded.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Per-shape/class schedules chosen without a validation protocol | DA-C1, R1-W1 | §4.2.1, §6.2.1, §6.2.3 | Verified | All three quotes are in the text; no validation split is stated anywhere (searched for "validation", "selected", "tuned", "grid search"). "Chosen by score" is inferred from "benefited"; not stated outright. |
| Headline numbers equal the tuned/default-schedule rows; the sweep does not preserve the comparison | DA-C1 | Table 2 vs Table 4 DC row; Table 1 | Verified | BL row (0.15/1.44) equals Table 4 DC ViscoReg; alternative schedules in Table 2 give dC 0.16–0.17 vs DiGS 0.15, dH 1.82/2.11/2.34 vs 1.70. Sweep covers one shape only. |
| Table 3 "top 2 in every metric" | R1-W5, R4-W2, DA-M2 | Table 3 | Verified | IoU mean ViscoReg (quad) 0.959 < StEik 0.967/0.963; median Chamfer 2.19e-5 vs 6.33e-6 |
| "Our method improves upon all other methods" on SRB | R1-W5, DA-M2 | §4.2, Table 4 | Partly correct | True for overall dH; dC ties (0.18) with StEik (quad); lordquas dH 1.09 vs 0.91 (DiGS) |
| Assumption 1 incompatible with SDF-like smooth network | R1-W2, DA-M1 | §3.2 | Verified | Extremum argument holds under the paper's setup (Ω = enclosed volume, Assumption 1 on Ω) |
| Lemma 2 constant dependence inverted | R1-W3 | Eq. 8, §6.1.2 | Verified | Rederived: factors Cf, not 1/Cf |
| Fourier sign error in Eq. 27 | R1-W4, DA-M5 | §3.4 | Verified (sign); Partly correct (p = 1 operator, which depends on the sign convention of the flow) | Conclusion on stability depends on κe > 0 |
| ε² (Δu)² term makes ViscoReg (p = 2) contain a DiGS-style penalty | R2-W1, DA-M3 | Eq. 24, Eq. 29, §3.4 | Verified (algebra); Partly correct as a novelty verdict (cross term and schedule differ; p not stated) | |
| "without adding significant computational cost" | R1-W6, R4-W4, DA-M4 | Abstract, §4 | Verified | No timing anywhere |
| [24] is a review, not the PINN source | R2-W3 | §2.3, ref [24] | Verified | |
| HotSpot, NSH not cited | R2-W2/W4 | §2, ledger | Verified | prior, arXiv-only; MAJOR at most; no weakness rests on the recent preprint |
| R3: "conceptual bridge is valuable; results go in the right direction" | R3 | §1, §4 | Partly correct | The direction holds for dH against DiGS; not for IoU against StEik |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Most points verified (ERR-1, 2, 3, 5); selection point correct though "by score" is inferred |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; the novelty delta is a fair reading; citation points verified |
| R3 (Perspective) | 4 | 3 | 0.75 | Positive overall rests partly on results "in the right direction" that Table 3 does not support against StEik; did not check the theory; calibration lenient (pool 66 vs the evidence) |
| R4 (Generalist) | 3 | 3 | 1.0 | Typical, correct on Table 3 and the disconnected theory |
| DA | 2 | 4 | 1.0 | Main objections verified; some strength in DA-C1 was inferred; Overall 2 slightly harsh relative to MAJOR-level residue, offset by sound issues |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Applying criterion 3: the benchmark has no validation split, the paper states per-shape departures from the default schedule ("benefited", "coarse grid search") on the evaluated shapes, these feed the headline averages, and the only sweep (Table 2, one shape) shows the comparison with DiGS does not hold at other values. Disclosure does not make it valid; the "chosen by score" step is inferred, and the visible effect on lordquas is nil, which keeps this from being a fabrication-level concern, but the ruling follows the decision table rather than the size of the effect. | **Upheld** | New data/experiments (fixed-schedule or held-out selection re-runs) |

### Final Decision and Justification
The EIC-weighted rating is 2.92, so the starting point is 3, and the composite cross-check (about 53, band 3) agrees. The decision is **Borderline Reject (3)**, equal to the starting point and equal to the DA ceiling (upheld DA-C1 needs new experiments, cap 3). I do not depart upward: even without the upheld issue, the verified problems (a bound for a different loss with an inconsistent assumption and an inverted constant; a stability analysis with a sign error; claims in Table 3 and the abstract that the tables do not support; margins of a few percent with no variance) keep this paper on the typical-rejected side. I do not depart downward either: the idea is cheap, plausible, and moves results in the right direction against DiGS, and every issue is fixable by the authors (a fixed-schedule rerun, narrowed claims, corrected constants). EIC pool position: better than about 45% of ICLR submissions; deciding evidence: the headline gain over StEik is 2.5% in dH (derived) and obtained with schedules chosen per shape, and the theory does not cover the method. Confirmed not above the DA ceiling.

---

## Score Summary

### Official Scores and EIC Assessment
See `aggregate.json` for the full script output after the EIC weights. Reviewer dimension scores:

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | Spread |
|-----------|----|----|----|----|----|---------------------|--------|
| Technical Rigor | 46 | 54 | 62 | 54 | 42 | 51.6 | 20 |
| Clarity & Presentation | 58 | 60 | 64 | 56 | 58 | 59.2 | 8 |
| Novelty & Originality | 50 | 50 | 64 | 52 | 46 | 52.4 | 18 |
| Significance & Impact | 50 | 52 | 64 | 54 | 46 | 53.2 | 18 |
| Experimental Validation | 44 | 52 | 58 | 50 | 38 | 48.4 | 20 |
| Reproducibility | 56 | 58 | 60 | 58 | 52 | 56.8 | 8 |
| Ethical Compliance | 60 | 60 | 64 | 60 | 58 | 60.4 | 6 |
| **Composite** | 50.4 | 54.3 | 62.0 | 54.1 | 46.6 | **53.5 (before)** | |

### Target-Venue Scores (ICLR, scale status: secondary)
Soundness / Presentation / Contribution and the rating are given in `aggregate.json` (ICLR 2026 scale {0,2,4,6,8,10}; earlier cycles {1,3,5,6,8,10}). These are produced by the script from the internal scores, not scored separately, and the label wording is not official.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "ViscoReg: Neural Signed Distance Functions via Viscosity Solutions" to ICLR. The topic, stabilizing neural SDF training from unoriented points through classical vanishing-viscosity ideas, is timely, and the idea of a decaying viscous term is attractive for its simplicity.

**Overall Assessment:** The reviewers appreciated the principled motivation and the cheap, drop-in nature of the loss, and they found the direction of the results encouraging against DiGS. They were concerned that the gains over StEik are small, that the schedules were set per shape and class without a stated validation protocol, and that the theory does not cover the proposed loss and contains errors.

**Key Strengths Identified by Reviewers:**
1. A clear bridge from vanishing-viscosity theory to neural SDF training, with a useful diagnostic of the forward–backward Eikonal flow (R1, R2, R3, R4).
2. Fair separation of StEik's regularizer and architecture, and breadth of tasks (R1, R4).
3. An honest ablation of the ε schedule and open listing of per-shape settings (R1, R4, DA).

**Key Concerns Requiring Attention:**
1. Per-shape and per-class ε schedules chosen on the evaluated shapes, one-shape ablation, no variance (CONSENSUS-2, R1, DA).
2. Theory disconnected from the method; an assumption that cannot hold; an inverted constant; a Fourier-sign error in the stability argument (CONSENSUS-4, R1, R2, R4, DA).
3. Claims stronger than the tables: Table 3 "top 2 in every metric", "outperforms … StEik", "no significant computational cost" (CONSENSUS-4).

**Critical Challenge (Devil's Advocate):** The reported margins cannot be separated from schedule tuning on the evaluated shapes; the sweep in Table 2 shows that the comparison with DiGS does not hold at most other schedules. This must be addressed with a fixed-schedule or held-out-selection evaluation.

**Decision: Borderline Reject (3).** The work could become a solid paper if the evaluation is redone under a fixed schedule or with held-out selection, the claims are narrowed to what the tables show, and the theory is either corrected and connected to the loss or presented separately. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Anneliese Okonkwo-Reyes
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Claims exceed tables (Table 3, "outperforms", "all other methods") | R1, R2, R4, DA | CONSENSUS-4 |
| Theory not connected to the method / bound not informative | R1, R2, R4, DA | CONSENSUS-4 |
| No variance, no cost evidence | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the idea worth publishing despite the weaknesses | R3 | R1, R4, DA (R2 neutral-negative) | The EIC weights R3 down because its positive view rests on a result direction that Table 3 contradicts against StEik |

### Score Spread Discussion
Technical Rigor (spread 20) and Experimental Validation (spread 20) are at the edge of the flag: R3 scores the theory and experiments higher because it read the framing as sound without recomputing; R1 and the DA recomputed. The EIC adopts the lower view, as it was verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Per-shape schedule selection on evaluated shapes | Yes (R1-W1) | Upheld | New experiments |
| DA-M1 | MAJOR | Theory/method gap, Assumption 1 | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Claim distortion in Table 3 and abstract | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Delta vs DiGS | Yes (R2) | n/a | n/a |
| DA-M4 | MAJOR | Cost claim unmeasured | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Stability analysis algebra | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR | Single runs | Yes (R1, R4) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Per-shape / per-class ε schedules chosen on the evaluated shapes; one-shape ablation | DA-C1, R1-W1 | §4.2.1, §6.2.1, §6.2.3, Table 2, Tables 1/3 | Re-run SRB and ShapeNet with the single baseline schedule (and, if desired, report a held-out-selected schedule); give StEik/DiGS equal tuning freedom or fixed published settings; extend Table 2 to all five SRB shapes | High; ≈ 24–48 GPU-hours | Partly (SRB yes; full ShapeNet maybe) |
| R2 | Claims exceed the evidence (Table 3 caption, §4.2 "all other methods", abstract "outperforms … StEik") | R1-W5, R4-W2, DA-M2 | Table 3, §4.2, §4.4, abstract | Narrow wording; add medians, IoU comparison, per-class table to the main paper | Low | Yes |
| R3 | Theorem 2: Assumption 1 inconsistent; inverted Cf constant; no bound for ViscoReg; "first" claim | R1-W2/W3, DA-M1, R2-W2 | §3.2, Eq. 8, 12, 16, §6.1.2 | Correct constants, weaken or replace Assumption 1, quantify Mθ*, Cθ*, or present the theorem as separate; restrict "first" | Medium | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Stability analysis algebra and κe > 0 | R1-W4, DA-M5 | Correct Eq. 26–31; state the condition; add empirical stability curves | Low–Medium | Yes |
| S2 | Delta over DiGS / VisCo Grids; state p | R2-W1, DA-M3 | Ablation: annealed Laplacian vs viscous residual, same schedule, MFGI | Medium; ≈ 6 GPU-hours | Yes |
| S3 | Cost claim | R1-W6, R4-W4, DA-M4 | Runtime/memory table | Low; ≈ 2 GPU-hours | Yes |
| S4 | Variance | R1, DA-M6 | 3–5 seeds on SRB, paired bootstrap on ShapeNet | Medium | Partly |
| S5 | Missing related work: HotSpot, Neural-Singular-Hessian (ledger: prior, arXiv-only); PINN source; [47]/[48] | R2-W2/W3/W4 | Cite and discuss; compare if numbers are available | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Cross-field links (heat method, level sets, PINN failure modes) | R3 | Short discussion |
| N2 | 1-D comparison with exact viscosity solution | R3 | Use the §3.2 zig-zag example |
| N3 | Table definitions (∆ columns, "wo n", Table 2 caption) | R1, R4 | Define and relabel |
| N4 | Noise-robustness study, adaptive ε | R3 | Follow-up |
| N5 | Table 1/4 minor inconsistencies (16.30 vs 16.33; StEik lin/quad labels) | R1 | Fix |

---

## Estimated Revision Effort
- Priority 1: 3 items, roughly 2–4 weeks including re-runs and a rewritten theory section.
- Priority 2: 5 items, roughly 1–2 weeks.
- Priority 3: 5 items.
- **Total estimated revision time**: 3–5 weeks.
