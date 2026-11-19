# Simulated Review: "Mirror Mean-Field Langevin Dynamics" (ICLR, full mode)

*Date: 2026-11-05. Simulation of how a careful panel would likely see this draft; not a prediction of any real decision. The five reviewer passes were run one after another in a single shared model context (no independent agents), each from its own role file. Figures were not available (text extraction only), so Figure 1 is judged from its caption and the text of Section 5.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Mirror Mean-Field Langevin Dynamics |
| Primary Discipline | Machine-learning theory → optimization over probability measures (mean-field Langevin dynamics, mirror Langevin sampling) |
| Secondary Discipline(s) | Stochastic analysis / functional inequalities (log-Sobolev), convex optimization (mirror descent, self-concordance), mean-field neural networks |
| Paper Type | Theoretical (composite weights: theoretical) |
| Core Technique(s) | Mirror Langevin dynamics (Hessian-metric diffusion), mean-field Langevin dynamics (McKean–Vlasov), uniform log-Sobolev inequality, entropy sandwich, one-step interpolation, uniform-in-N propagation of chaos |
| Target Venue | ICLR (stated by the user); profile key `iclr`, scale status secondary |
| Venue-Specific Notes | None. ICLR reviews are public and authors may upload a revision during discussion, so fixable and fundamental issues are separated. Base rate ≈ 27% accepted. |
| Paper Maturity | Submission-ready draft: 10 pages of main text plus an appendix of related work and proofs; one small experiment |
| Ethics-Relevant Content | None (no human data, no deployment risk). There is no limitations section. |

### Claimed Contributions (as stated by the authors; Section 1.1 and abstract)
1. **C1.** The mirror mean-field Langevin dynamics (MMFLD), "the first algorithm minimizing (1) with global convergence guarantees" for general convex X ⊆ R^d.
2. **C2.** Linear convergence of the continuous-time MMFLD via a uniform (mirror) log-Sobolev inequality (Theorem 3.2).
3. **C3.** Uniform-in-time propagation of chaos for the time- and particle-discretized algorithm (Theorems 4.1 and 4.3).
4. **C4.** Numerical evidence that MMFLD avoids the boundary mass accumulation of projected MFLD (Section 5, Figure 1).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** No datasets or splits (theory paper). The only experiment is on the unit simplex with d = 3, entropy mirror map, F as a mean-matching term plus a log-barrier with β ∈ {0, 10⁻⁴}, 50K particles, η = 3×10⁻³, λ = 0.1. Not stated after search: target q, initial law µ₀, number of iterations T, definition and estimator of the plotted "loss", seeds or repeats, hardware, code availability.
- **Headline results.** Theorem 3.2 rate e^{−2C_LSI λ t}; Theorem 4.3 rate exp(−C_LSI λ η k) plus LR²/(2N) plus δ_η/(2C_LSI λ). No empirical numbers are quoted in the text.
- **Appendix.** A: related work. B.1–B.4: proofs of Theorems 2.2, 3.1, 3.2 and the entropy sandwich (Lemma B.1). B.5: proof of Theorem 4.3. B.6: Lemma B.2 (Hessian-stability bound used in B.5). Theorem 4.1 is proved in one sentence by reference to Nitanda (2024).
- **Unverifiable.** Figure 1 (images unavailable). Several displayed formulas (M, ξ_t in Theorem 4.3 and Lemma B.2; the Grönwall display after (21); equation (18)) are partly garbled in the extraction, so the exact constants are treated as unverified where noted.

### Integrity scan
`integrity_scan.py` found no reviewer-directed text or hidden characters. The reviewers read the redacted copy, which equals the original. No injection found.

### Literature check
Mode **strict**, cutoff **2025-09-24**, arXiv only. 7 queries (6 claim, 1 expansion; 0 benchmark queries because the paper reports on no external benchmark). Gaps left open: no baseline/benchmark scout (none applicable); no prior work found for the experiment claim C4 in this search. Run after the reports were drafted; results enter only the Domain Reviewer's addendum (Phase 1.5).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Halvard Teixeira, research university (Western Europe)
- **Seniority / Expertise**: senior faculty / applied probability, optimization theory, learning theory
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Rederives the decisive inequality before trusting a rating; knows that accepted theory papers often assume strong conditions but expect at least one verified instance.

### Reviewer 1 (Methodology): Dr. Mei-Ling Castellanos, public university (East Asia)
- **Seniority / Expertise**: mid-career / functional inequalities, McKean–Vlasov processes, proof verification
- **Review Focus**: Proof correctness, assumptions, statement-versus-proof consistency, experimental validity
- **Style**: Reads proofs line by line and recomputes constants.

### Reviewer 2 (Domain): Prof. Tobias Nwankwo, public research institute (Europe)
- **Seniority / Expertise**: senior / Langevin sampling, optimal transport, mean-field neural networks
- **Review Focus**: Literature positioning, novelty against the closest prior work
- **Style**: Compares every theorem with its closest antecedent.

### Reviewer 3 (Perspective): Dr. Priya Valdivieso, industrial research lab (North America)
- **Seniority / Expertise**: mid-career / convex optimization, interior-point and mirror-descent methods, constrained Bayesian inference
- **Review Focus**: Connections to optimization and OR, practicality, assumption audit
- **Style**: Constructive; asks where the method would actually be used.

### Reviewer 4 (Generalist): Dr. Anand Mbeki-Larsen, private university (South Asia)
- **Seniority / Expertise**: postdoc-to-assistant-professor / learning theory broadly
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; does not rederive proofs.

### Devil's Advocate: Prof. Lucía Okonkwo-Brandt, university (Oceania)
- **Seniority / Expertise**: senior / evaluation of theoretical claims, applied mathematics
- **Review Focus**: Core-argument challenges, vacuity, overclaiming
- **Style**: Fair but exacting; checks whether a theorem says anything non-trivial.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Mirror Mean-Field Langevin Dynamics
## Reviewer: Dr. Mei-Ling Castellanos, Methodology Reviewer (public university, East Asia; fictional persona)
## Expertise: functional inequalities; McKean–Vlasov processes; proof verification
## Date: 2026-11-05

## Summary
The paper extends mean-field Langevin dynamics to measures supported on a convex set X by replacing the Euclidean diffusion with the mirror-Langevin diffusion of a Legendre-type barrier ϕ. Under a uniform mirror log-Sobolev inequality for the proximal Gibbs measures, the continuous flow converges linearly in the free energy (Theorem 3.2). For an N-particle, time-discretized version (Algorithm 1) the paper states a uniform-in-time propagation-of-chaos bound (Theorem 4.3) by combining the one-step interpolation of Jiang (2021) with the LSI-constant-free particle bound of Nitanda (2024). A single simplex experiment compares MMFLD with projected MFLD (Section 5).

**Protocol sweep.** Searched the full text, appendix included, for: test set, test split, validation, held-out, selected, tuned, hyperparameter, early stopping, best, per task. Nothing relevant: there is no data split, tuning or selection in this theory paper. The experiment in Section 5 fixes η, λ, N, β without any stated selection. Nothing to report on leakage.

## Strengths
### S1: A clean, well-posed question with a natural construction
The mirror-geometry Fokker–Planck equation (13) has the same stationary law µ* ∝ exp(−λ⁻¹ δF/δµ) as the unconstrained flow (Theorem 3.1), and the paper's reduction of the problem to a Hessian-metric flow is sound in outline (Section 3).

### S2: Theorems 2.2 and 3.2 check out given their hypotheses
I re-derived the Appendix B.1 and B.4 computations (d/dt KL = −λFI; d/dt(L − L*) = −λ²FI(µt‖µ̂t) ≤ −2λ²C·KL(µt‖µ̂t) ≤ −2λC(L − L*)). The rate 2C_LSI λ is correct for the mirror Fisher information, provided boundary terms in the integrations by parts vanish.

### S3: Honest bookkeeping of what is imported
The paper says that its proof "mirrors that of ordinary MFLD" (Section 3) and that Theorem 4.1 follows from Nitanda (2024) (Section 4.2), so the reader can see which parts are new.

## Weaknesses

### W1: The bound in Theorem 4.3 is infinite for every mirror map the paper admits
Theorem 4.3 contains M = exp(2c₁D/√c₂) with D := max over u, v of ‖∇ϕ(u) − ∇ϕ(v)‖², and δ_η is proportional to M. But Lemma 2.1(i) states ∇ϕ(X) = R^d, and Section 2.1 requires ‖∇ϕ(x)‖ → ∞ at ∂X, so the maximum is +∞ and so are M and δ_η. Lemma B.2 even states "when c1 = 0 and D = ∞" as a convention for M = 1, and c₁ = 0 means ∇²ϕ* has constant Hessian, i.e., no constraint. For every genuinely constrained example the final bound is vacuous. The same D enters the deterministic bound used for the rare event in ξ_t (proof of Lemma B.2). The exact form of M and ξ_t is partly garbled in the extraction, but the definition of D and Lemma 2.1(i) are unambiguous.
- **Suggested Fix**: Either supply an argument that avoids the sup over the whole dual space (e.g., a moment bound on the dual displacement ‖Y_t − Y_0‖ using the noise covariance ∇²ϕ(X₀), or a modified self-concordance as in Li–Tao–Vempala–Wibisono 2022), or restrict the theorem to a class where D < ∞ and exhibit one concrete (X, ϕ, F) with all constants finite. Estimated cost: new proof, weeks of work; not rebuttal-feasible.

### W2: The uniform LSI assumptions are never checked for any instance, and Assumption 4 is stated with the wrong Fisher information
Assumption 4 (Section 2.2) is stated on R^d with "the relative Fisher information … as in (6), except without the modifier ∇²(ϕ)⁻¹", yet the proof of Theorem 3.2 (B.4) uses the mirror Fisher information FI(µt‖µ̂t) of (6). As printed, the hypothesis of Theorem 3.2 does not give the step "FI ≤ … KL" used in B.4; what is needed is a uniform mirror LSI for the proximal Gibbs measures. Assumption 8 (uniform-in-N mirror LSI) is the hard step in the unconstrained theory (it needs the machinery of Chewi–Nitanda–Zhang and Wang, both cited), but here it is assumed. No sufficient condition and no example is given for Assumptions 4, 5, 7 or 8 jointly, and the discussion after Assumption 4 cites Bakry–Émery, Holley–Stroock and Aida–Shigekawa, which are Euclidean statements.
- **Suggested Fix**: State Assumption 4 for the mirror Fisher information; give a sufficient condition in Hessian geometry (relative strong convexity plus a perturbation argument) and verify all hypotheses for at least one worked class, e.g., a two-layer network with parameters in a ball and the barrier ϕ(x) = −log(1 − ‖x‖²). Cost: moderate to high.

### W3: The experiment does not test the theory and is under-specified
(a) With the entropy map ϕ(x) = Σ x_i log x_i, ∇²ϕ = diag(1/x_i), so [∇²ϕ]⁻¹ = diag(x_i). The barrier term β Σ log(1/x_i) used in Figure 1(d–f) has dual-norm² gradient β² Σ 1/x_i, which is unbounded as x_i → 0 (my computation), violating Assumption 5(i). The β = 0 run is the only one inside the stated framework. (b) "Loss curves" are shown, but how L = F + λEnt is estimated for 50K particles (the entropy needs a density estimate) is not stated, nor the target q, µ₀, T, or any repeat. (c) The claim "MMFLD is able to achieve significantly smaller loss" has no numbers or variability. (d) Nothing tests the exponential rate of Theorem 3.2 or the 1/N behaviour of Theorem 4.3. (e) The only baseline is naive projection, which the paper itself calls a "trivial failure case" at β = 0.
- **Suggested Fix**: Report mean ± std over ≥5 seeds, define the plotted quantity, add a log-linear plot of L − L* against t, a sweep over N, and one stronger baseline (e.g., MFLD run on a softmax/logit reparametrization). Cost: well under 10 GPU-hours; rebuttal-feasible.

### W4: Theory analyses exact simulation of the diffusion step; the experiment uses one Euler step
Section 4.1 says the analysis follows [AC21, Jia21] in simulating the SDE in line 5 of Algorithm 1 exactly "for simplicity of exposition", then that "our experiments indicate that the trivial one-step discretization generally suffices". That statement rests on one three-dimensional example.
- **Suggested Fix**: State this as a limitation and, ideally, quantify the one-step bias in the experiment (vary the number of sub-steps).

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E3/E6 | Section 2.2 after Assumption 4 vs. Appendix B.4 | "except without the modifier" | Assumption 4 uses the Euclidean Fisher information; B.4 needs the mirror one | Cross-referenced (two locations) | High | MAJOR | State a mirror LSI for µ̂ |
| ERR-2 | E2/E3 | Theorem 4.3 (definition of D), Lemma 2.1(i), Lemma B.2 | "when c1 = 0 and D = ∞" | D = max‖∇ϕ(u) − ∇ϕ(v)‖² is infinite since ∇ϕ(X) = R^d; M and δ_η are infinite | Derived from the paper's own definitions | High for D = ∞; the exact form of M is partly garbled | MAJOR | See W1 |
| ERR-3 | E6 | Theorem 4.3 vs. proof B.5; Theorem 4.1; Assumption 3 | "Suppose Assumptions 2, 6-8 hold" | The proof says "Now using Assumptions 5, 7, and (16)"; Assumption 2 is the Euclidean condition; Assumption 3 assumes a minimizer of (7) rather than (11) | Cross-referenced | High | MINOR | Correct the hypothesis lists |
| ERR-4 | E3 | Section 5 | "barrier preventing collapse towards the boundary" | The barrier violates Assumption 5(i) for the entropy map: ‖∇ δF/δµ‖²_{[∇²ϕ]⁻¹} = β²Σ1/x_i | Computed by hand from the definitions | High | MAJOR for the claim that Section 5 illustrates the theory; no effect on correctness of Theorems | Say so, or pick a barrier satisfying 5(i) |

**Minor.** Intro: "convex F : P2 (X ) → Rd" should be R. Section 3: "that (13) corresponds to the following Fokker-Planck PDE" should refer to (12). Duplicate bibliography entries for the same Li–Zha–Tao paper (LZT21a/LZT21b). Appendix B.4 writes L(µ) where L(µ*) is meant.

## Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | "first algorithm … with global convergence guarantees" | §1.1 | Theorems 3.2, 4.3 | Partially: Theorem 3.2 is conditional on an unverified mirror LSI; Theorem 4.3 is vacuous as stated (W1) |
| C2 | Linear convergence of continuous MMFLD | Abstract, Thm 3.2 | B.4 | Supported given Assumptions 4 (corrected) and 5 |
| C3 | Uniform-in-time propagation of chaos | Abstract, Thm 4.3 | B.5, B.6 | Unsupported as stated (D = ∞); also conditional on Assumption 8 |
| C4 | MMFLD more stable and optimal than projected MFLD | §5 | Figure 1 (not visible) | Partially: single toy run, no numbers |

## Missing References
Not my focus (see Reviewer 2).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Core flow theorem fine; discretization theorem vacuous as stated; experiment weak |
| Clarity | 3 | Readable, but hypotheses and notation inconsistent |
| Significance | 2 | Conditional guarantees in a niche setting |
| Originality | 2 | Adapts three known arguments |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline discretization bound is infinite under the paper's own definitions (ERR-2), and no instance satisfies the assumptions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Theorem 3.2 correct; Theorem 4.3 vacuous; Assumption 4 misstated |
| Clarity & Presentation | 62 | Competent | Clear exposition; inconsistent hypotheses and symbols |
| Novelty & Originality | 52 | Developing | Imported techniques; first constrained MFLD claim is real but narrow |
| Significance & Impact | 55 | Competent (low) | Useful gap-closing if assumptions can be met |
| Experimental Validation | 38 | Developing | One 3-d toy run, no variability, off-assumption |
| Reproducibility | 50 | Developing | Experimental details missing; proofs reproducible except constants |
| Ethical Compliance | 60 | Competent | Nothing at stake; no limitations section |

## Questions for Authors
1. Is D in Theorem 4.3 finite for any ϕ satisfying Lemma 2.1(i)? If so, for which, and what is M for the entropy map on the simplex? A finite example would raise my score by one step.
2. Which Fisher information does Assumption 4 refer to? Can you verify Assumptions 4, 5, 7, 8 for the Section 5 problem at β = 0?
3. In the Grönwall step after (21), the combined inequality reads d/dt u ≤ −C_LSI λ u + Nδ_η (from (20) and ½E‖π‖² ≤ Nδ_η), whose fixed point is Nδ_η/(C_LSI λ), whereas the paper uses Nδ_η/(2C_LSI λ). Is a factor of 2 missing? (Low-to-medium confidence: the display is partly garbled.)
4. In (18), the drift ∇·G_t appears without a factor λ, while (13) and (19) carry λ. Is this a typo? (Same caveat.)
5. How is Ent(µ) estimated for the loss curves, and are results repeated over seeds?

## Limitations Assessment
**Partially.** Future work (mirror Poincaré) is mentioned in Section 6, but the exact-diffusion assumption, the unverified LSI assumptions and the toy experiment are not discussed as limitations.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A correct but routine continuous-time result, and a discretization theorem that is vacuous as stated, with unverified assumptions and a weak experiment.

## Confidence
**4**: Re-derived B.1, B.4 and the structure of B.5; the constants of Lemma B.2 were only partly readable.

---

# Peer Review Report

## Paper: Mirror Mean-Field Langevin Dynamics
## Reviewer: Prof. Tobias Nwankwo, Domain Reviewer (public research institute, Europe; fictional persona)
## Expertise: Langevin sampling; optimal transport; mean-field neural networks
## Date: 2026-11-05

## Summary
The paper combines two established lines: mirror Langevin dynamics for constrained sampling (Hsieh et al. 2018, Zhang et al. 2020, Jiang 2021, Ahn–Chewi 2021) and mean-field Langevin dynamics for entropy-regularized convex functionals over measures (Nitanda–Wu–Suzuki 2022, Chizat 2022). The resulting flow MMFLD is shown to converge linearly under a mirror LSI, and a discretized particle version is analysed using the one-step interpolation argument and the improved particle approximation of Nitanda (2024).

## Strengths
### S1: Closes an explicitly open gap
The introduction states "the problem for general X has remained open" (Section 1), and the many applications listed (trajectory inference, barycenters, constrained neural networks) are credible motivation. No work found in my search treats this exact object.

### S2: Careful, honest relation to the mirror-Langevin literature
Appendix A accurately traces the bias and discretization story of mirror Langevin ([ZPFP20], [AC21], [LTVW22], [GV22], Metropolis-adjusted variants), and Theorem 2.2 is correctly attributed to [Jia21].

### S3: The continuous-time proof is correct
Theorem 3.2 follows the Nitanda et al. argument with the Euclidean Fisher information replaced by the mirror one; I checked B.4 and found no gap given the stated assumptions.

## Weaknesses

### W1: Technical novelty is modest and the headline wording overstates it
Theorem 3.2 repeats the argument of [NWS22] with a metric; the entropy sandwich is verified in one sentence ("It is straightforward to see that the proof of"); Theorem 4.1 is proved by "The arguments of [Nit24, Appendix A] directly hold over". The only genuinely new analysis is Theorem 4.3 (combining [Jia21] and [Nit24]). Yet the abstract and Section 1.1 present "the first algorithm … with global convergence guarantees", and Section 4.3 says the result "extends … the sharpest known bounds". Convergence rests on a mirror LSI (Assumptions 4 and 8) that is assumed, not established, for any non-trivial class (see Reviewer 1).
- **Suggested Fix**: Add a short "what is new" paragraph per theorem and qualify the first/sharpest wording.

### W2: Positioning against projected/reflected Langevin and mirror descent in measure space is missing
The experiment's only baseline is projected MFLD, but the projected Langevin literature (Bubeck–Eldan–Lehec) and mirror-descent-in-measure-space work (Aubin-Frankowski–Korba–Léger) are not cited (see Missing References).
- **Suggested Fix**: Cite and contrast; explain what the Hessian-metric Wasserstein flow gives over mirror descent in measure space.

### W3: Some citations do not support the sentence attached to them
Section 2.1: "It is also mentioned the stronger mirror LSI may not hold in general [OV00]". The bibliography entry for [OV00] (Otto–Villani, "Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality") does not, by its title, concern mirror LSI; please cite where it is mentioned. Section 1 also asserts the analyses "may be applied if X is a complete Riemannian manifold without boundary" without a citation. The bibliography lists the same Li–Zha–Tao paper twice (LZT21a, LZT21b).
- **Suggested Fix**: Correct or add citations; deduplicate.

### Literature-check addendum (Phase 1.5; strict, cutoff 2025-09-24, arXiv only, 7 queries)

**Per-claim novelty (claim-level profile; `related_search.py novelty`).**
| Claim | Dim. | Novelty | Top prior work (level; label; cited?) | Reasoning |
|-------|------|---------|---------------------------------------|-----------|
| C1 constrained MMFLD with guarantees | method | medium | Efficient constrained sampling via the mirror-Langevin algorithm, arXiv 2010.16212 (3; arXiv-only prior; cited) | Mirror Langevin handles linear F only; mean-field coupling is new. No prior constrained MFLD with guarantees found in this arXiv-only search. |
| C2 linear convergence, continuous | result | medium | Convergence of mean-field Langevin dynamics: Time and space discretization, stochastic gradient, and variance reduction, arXiv 2306.07221 (3; cited) | Same entropy-sandwich structure; mirror metric is the change. |
| C3 propagation of chaos | result | medium | Improved Particle Approximation Error for Mean Field Neural Networks, arXiv 2405.15767 (3; cited) | Particle bound inherited; discretization argument inherited from mirror Langevin. |

Paper reading from the script: "no central claim fully covered by prior work". Attribution (closest prior work as a whole): Nitanda (2024), cited. One established claim is not found; no MAJOR novelty finding.

**Novelty delta table.**
| Claimed contribution | Closest prior work | What it already does | What is new | Cited and differentiated? |
|----------------------|--------------------|----------------------|-------------|---------------------------|
| MMFLD | Mirror Langevin (arXiv 2010.16212; Jiang 2021) | Mirror diffusion for linear potentials on convex X | Mean-field (McKean–Vlasov) drift | Yes |
| Rate for MMFLD | Mean-field Langevin discretization (arXiv 2306.07221; NWS22) | Linear rate for unconstrained MFLD under uniform LSI | Mirror metric and relative smoothness conditions | Yes |
| Propagation of chaos | Nitanda 2024 (arXiv 2405.15767) | LSI-constant-free particle error, unconstrained | Constrained version via [Jia21] interpolation | Yes |

**Text-overlap flag (factual, for the editor).** `similarity` reports 8 shared verbatim 8-word sequences with Nitanda (2024) (e.g., "dynamics mfld minimizes an entropy regularized nonlinear convex"). These are the standard opening sentence of the MFLD literature and a phrase near Theorem 4.1; the work is cited throughout. This is noted only as a flag for the editor and is not an accusation; only abstracts were compared.

**Baseline scout.** Not applicable: the paper reports on no external benchmark (`benchmarks` lists none).

**Field snapshot.** Roughly 2018–2020, mean-field analyses of two-layer networks gave qualitative convergence (Mei–Montanari–Nguyen, Chizat–Bach). The 2022 analyses of Nitanda–Wu–Suzuki and Chizat gave linear rates under a uniform LSI of the proximal Gibbs law. 2023–2025 work removed the LSI-constant dependence and obtained uniform-in-time propagation of chaos via uniform-in-N LSI (Chen–Ren–Wang, Suzuki–Wu–Nitanda, Chewi–Nitanda–Zhang, Nitanda 2024, Nitanda et al. 2025). On the sampling side, mirror/Hessian-metric Langevin gained vanishing-bias discretizations (Ahn–Chewi, Li et al., Gatmiry–Vempala) and Metropolis-adjusted variants. Open problems named by the literature include Poincaré-type conditions for MFLD, constrained domains, and verifiable conditions for the uniform-in-N LSI. What counts as significant now: a result that removes an assumption or handles a new domain with checkable conditions, rather than another transfer of known arguments to a modified metric. This snapshot is built from kept results only.

**Verified missing references** (checked with `related_search.py verify`; links from arXiv):
- Important: Aubin-Frankowski, Korba, Léger, "Mirror Descent with Relative Smoothness in Measure Spaces, with application to Sinkhorn and EM", NeurIPS 2022 (arXiv 2206.08873). Relative smoothness in measure space is close in spirit to Assumption 5.
- Important: Bubeck, Eldan, Lehec, "Sampling from a log-concave distribution with Projected Langevin Monte Carlo", Discrete & Computational Geometry 2018 (arXiv 1507.02564). The natural reference for the projected baseline.
- Helpful: Deb, Kim, Pal, Schiebinger, "Wasserstein mirror gradient flow as the limit of the Sinkhorn algorithm", 2023 (arXiv 2307.16421).
- Worth discussing only (concurrent, within 60 days of the cutoff; not required, no effect on scores): Songbo Wang, "Large-scale concentration and relaxation for mean-field Langevin particle systems" (arXiv 2508.16428); Mohamed Alfaki Aboubacrine Assadek, "Exponential ergodicity of mean-field Langevin dynamics by synchronous coupling" (arXiv 2509.03124).

### Error Log
No new concrete errors beyond the citation points in W3 (E7). Confidence for the [OV00] point is Medium (based on the bibliography title only), so it is raised as a request rather than as an error.

## Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | none found (the closest prior works are all cited) | |
| Important | Aubin-Frankowski, Korba, Léger. Mirror Descent with Relative Smoothness in Measure Spaces, with application to Sinkhorn and EM. NeurIPS 2022 | Mirror geometry on measures with relative smoothness |
| Important | Bubeck, Eldan, Lehec. Sampling from a log-concave distribution with Projected Langevin Monte Carlo. DCG 2018 | Projected Langevin baseline context |
| Helpful | Deb, Kim, Pal, Schiebinger. Wasserstein mirror gradient flow as the limit of the Sinkhorn algorithm. arXiv 2023 | Another mirror-in-Wasserstein-space construction |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Continuous-time part sound; discretization constants not verified by me |
| Clarity | 3 | Well organized |
| Significance | 3 | Fills a stated gap in the MFLD literature |
| Originality | 2 | Natural combination of known tools |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean, expected result that closes a named open gap and is correctly positioned; held back by its dependence on assumed LSIs and a modest experiment.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Theorems 2.2 and 3.2 correct; Theorem 4.3 constants not rechecked |
| Clarity & Presentation | 64 | Competent | Good related-work appendix; some citation slips |
| Novelty & Originality | 60 | Competent | Medium novelty on all three central claims |
| Significance & Impact | 62 | Competent | Useful to the mean-field community |
| Experimental Validation | 45 | Developing | Toy example only; acceptable for a theory paper but thin |
| Reproducibility | 55 | Competent (low) | Proofs given; experiment details missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Which of the three central contributions is technically new beyond [Jia21] and [Nit24]? A crisp statement would move my Originality score up.
2. Can you cite where "the stronger mirror LSI may not hold in general" is shown?
3. How does MMFLD compare with mirror descent in measure space (Aubin-Frankowski et al.) in the regime λ → 0?

## Limitations Assessment
**Partially.** Open directions are stated; assumption strength is not.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: A correct, clearly positioned extension that closes a stated open gap, with the usual caveats about conditional guarantees and a thin experiment.

## Confidence
**4**: Know the MFLD and mirror-Langevin literature; did not recompute the constants of Lemma B.2.

---

# Peer Review Report

## Paper: Mirror Mean-Field Langevin Dynamics
## Reviewer: Dr. Priya Valdivieso, Perspective Reviewer (industrial research lab, North America; fictional persona)
## Expertise: convex optimization; interior-point and mirror-descent methods; constrained Bayesian inference
## Date: 2026-11-05

## Summary
MMFLD runs a particle system whose diffusion is shaped by the Hessian of a barrier function so that particles never leave a convex domain, while their interaction is the first variation of a convex functional. The authors prove linear convergence of the idealized flow and a uniform-in-time particle bound for a discretized scheme, and illustrate on a 3-component simplex.

## Strengths
### S1: A bridge between two communities
The paper links interior-point geometry (Legendre barriers, self-concordance via [NN94]) with distributional optimization for neural networks. This is a useful translation: it shows that barrier-induced Hessian metrics make Langevin diffusion respect constraints with no projection (Section 2.1).

### S2: Natural applications are named
Section 1 lists support-constrained barycenters, trajectory inference and bounded-support deconvolution, all of which genuinely need boundary-aware particle methods, and Section 5 uses the simplex, which also models mixture-weight posteriors.

### S3: The experiment makes the right qualitative point
The comparison in Section 5 isolates the boundary behaviour (mass piling up on ∂Δ₃ under projection, from the text of Section 5). Even a toy illustration clarifies why projection is a poor default.

## Weaknesses

### W1: Practical regimes are not addressed (dimension, boundary conditioning, cost)
The constants δ_η and M involve d and the geometry of ϕ (Theorem 4.3), and near the boundary the dual noise covariance ∇²ϕ(X) blows up, so the dual-space step becomes badly scaled. Algorithm 1 requires an inner SDE solve with state-dependent covariance, and the interaction term costs O(N²) per step for general F. None of this is discussed; the experiment is d = 3.
- **Suggested Fix**: Add a short practical-considerations paragraph and one higher-dimensional run (e.g., a 10–50-component simplex) with wall-clock comparison.

### W2: The motivating application (constrained neural networks) is never instantiated
Section 4.2 develops the theory for mean-field two-layer networks, but gives no neuron class h(x, ·) with constrained weights and a mirror map for which Assumptions 5–8 can be checked. A reader cannot tell if the theorem applies to any network of interest.
- **Suggested Fix**: Work one example (weights in a Euclidean ball with ϕ(x) = −log(1 − ‖x‖²), a bounded activation) and verify the assumptions, or state clearly that none is known.

### W3: Simpler alternatives are not discussed
MMFLD in the dual variable is an MFLD with a state-dependent diffusion. Why is this better than running Euclidean MFLD on an unconstrained reparametrization (softmax/logit for the simplex), or a penalty/barrier in the potential? The paper adds a log-barrier only in the experiment, and then to the baseline's disadvantage.
- **Suggested Fix**: Add a reparametrization baseline and a short discussion of when changing geometry beats changing coordinates.

### Fundamental assumptions audited
(1) A uniform mirror LSI for all proximal Gibbs laws, which is not examined; (2) a relative gradient bound (5(i)) that the paper's own barrier violates (computation: gradient norm² = β²Σ1/x_i near the boundary); (3) exact diffusion simulation, whereas the code uses one step.

**Minor.** No limitations or broader-impact paragraph; for a theory paper a single sentence suffices.

## Missing References
Method pointers only (no specific papers named): the Dikin walk and Hessian-metric samplers for polytopes; interior-point-based sampling; Fisher–Rao and Hellinger-type flows as alternative geometries for constrained measures.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound core, assumptions heavy |
| Clarity | 3 | Clear flow of ideas |
| Significance | 3 | Opens a direction |
| Originality | 3 | New combination, non-trivial bridge |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a coherent bridge between interior-point geometry and mean-field optimization, with correct continuous-time theory.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Core flow analysis fine; assumptions strong |
| Clarity & Presentation | 66 | Competent | Clear narrative |
| Novelty & Originality | 62 | Competent | Useful transfer across fields |
| Significance & Impact | 64 | Competent | Potential for constrained mean-field methods |
| Experimental Validation | 48 | Developing | Toy |
| Reproducibility | 58 | Competent (low) | Details missing |
| Ethical Compliance | 70 | Competent | Nothing at stake; no limitations paragraph |

## Questions for Authors
1. What does MMFLD buy over MFLD on a softmax-reparametrized simplex?
2. Is there any example neuron class where all assumptions can be verified?
3. How does the iteration cost scale with d and N, and is the boundary-conditioning problem observed at d ≥ 10?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: An interesting bridge with correct core theory; the work would be considerably stronger with one verified instance and a practical comparison.

## Confidence
**3**: Strong on the optimization side, less on the functional-inequality details.

---

# Peer Review Report

## Paper: Mirror Mean-Field Langevin Dynamics
## Reviewer: Dr. Anand Mbeki-Larsen, Generalist Reviewer (private university, South Asia; fictional persona)
## Expertise: learning theory (broad)
## Date: 2026-11-05

## Summary
The paper asks how to optimize an entropy-regularized functional over probability measures supported on a convex set, which standard mean-field Langevin dynamics cannot do because the noise leaves the domain. It proposes running the mean-field dynamics in the geometry induced by a barrier function (mirror Langevin), proves linear convergence in continuous time and a uniform-in-time particle bound for a discrete scheme, and shows a small simplex experiment.

## Strengths
### S1: A clear and well-motivated problem statement
Section 1 explains why constraints matter (applications to neural networks, barycenters, trajectory inference) and why projection is unsatisfactory (mass on the boundary; Section 2.1 and Section 5).

### S2: Well-organized exposition for a theory paper
The preliminaries on mirror Langevin (Section 2.1) and mean-field Langevin (Section 2.2) make the paper accessible to readers who know only one of the two; the structure Section 3 (continuous), Section 4 (discrete) mirrors the contribution list.

### S3: Proofs are included and the dependence on prior work is explicit
Appendix B gives the proofs; Theorem 2.2 and the entropy sandwich are marked as recovered from the literature.

## Weaknesses

### W1: Headline wording is stronger than the conditions allow
The abstract and Section 1.1 present "global convergence guarantees" for "the first algorithm" of its kind, but Theorem 3.2 requires a uniform LSI of every proximal Gibbs measure (Assumption 4) and Theorem 4.3 additionally a uniform-in-N LSI (Assumption 8), neither verified for any example. A reader skimming the abstract will not learn this.
- **Suggested Fix**: State the LSI conditions in the abstract or Section 1.1 and give at least one setting where they hold.

### W2: Presentation inconsistencies that obstruct checking
Theorem 4.3 is stated with "Suppose Assumptions 2, 6-8 hold" while its proof uses Assumption 5; the constants c, c₁, c₂, M and D are defined only in Assumption 7, Theorem 4.3 and Lemma B.2, with c₁ and c₂ not introduced before use; Assumption 7 mixes ϕ* and ϕ; the numbered equation referenced in Section 3 is off by one ((13) for (12)). The paper abuses the same symbol C_LSI for different LSI constants (Section 1.2), which makes Theorems 3.2 and 4.3 hard to compare.
- **Suggested Fix**: Give a notation table; index the LSI constants; fix the assumption lists.

### W3: Experimental section is too small to support the "optimality" language
One three-dimensional problem, one baseline, no repeats, no numbers, and the claim "demonstrating higher stability and optimality for constrained optimization" in Section 5 is not supported by a quantitative comparison. The authors themselves describe the β = 0 case as a "trivial failure case" for projection.
- **Suggested Fix**: Soften the language or add a quantitative, repeated comparison and one more problem.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims follow from the arguments | Partly | Theorem 3.2 fine; Theorem 4.3 questionable (see R1) |
| Presentation | Partly | Notation and hypothesis lists inconsistent (W2) |
| Contribution matters to ICLR audience | Partly | Learning-theory audience yes; wider ICLR audience limited |
| Claims match evidence | Partly | W1, W3 |
| Reproducibility of the experiment | Not met | Section 5 lacks target, T, µ₀, seeds, loss definition |
| Limitations stated | Not met | No limitations paragraph; only future work in Section 6 |

**Minor.** Typos: "dyamics", "Riemmanian", "whave"; "R^d" for "R" in the introduction.

## Missing References
Not my focus.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Assumptions unverified; experiment thin |
| Clarity | 2 | Readable but inconsistent |
| Significance | 2 | Narrow audience |
| Originality | 2 | Combination of known tools |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a competent but incremental, assumption-heavy theory paper with a thin empirical section, i.e., the median submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound outline; unverified assumptions |
| Clarity & Presentation | 60 | Competent | Structure good; notation inconsistent |
| Novelty & Originality | 56 | Competent | Natural extension |
| Significance & Impact | 55 | Competent (low) | Niche |
| Experimental Validation | 40 | Developing | Toy |
| Reproducibility | 52 | Developing | Experimental details missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Where do Assumptions 4 and 8 hold? A concrete instance would raise my rating.
2. Can the abstract state the conditions under which the guarantees hold?
3. Can you add a quantitative, repeated experiment?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A reasonable contribution for a specialist audience, but the guarantees are conditional on unverified assumptions and the empirical support is thin; this is the median submission.

## Confidence
**3**: Did not rederive the proofs.

---

# Devil's Advocate Report

## Paper: Mirror Mean-Field Langevin Dynamics
## Reviewer: Prof. Lucía Okonkwo-Brandt (university, Oceania; fictional persona)

---

## Steelman
The authors identify a real gap: mean-field Langevin analyses cannot handle bounded domains because the noise exits them. By running the dynamics in a Hessian geometry that makes the boundary unreachable, the stationary law is unchanged, the continuous flow keeps the linear rate, and, in principle, the NeurIPS-era machinery for discretization and particle approximation transfers.

---

## Core Argument Chain
1. Mean-field Langevin dynamics cannot solve problem (1) on a constrained convex X (Section 1).
2. Mirror Langevin preserves constraints for linear F, so running it with the mean-field drift gives MMFLD (12).
3. Under a uniform mirror LSI and relative smoothness (Assumptions 4, 5), MMFLD converges linearly in continuous time (Theorem 3.2).
4. Under Assumptions 2, 6–8 the discretized N-particle algorithm satisfies a uniform-in-time propagation-of-chaos bound (Theorem 4.3).
5. Experiments show MMFLD avoids boundary accumulation and achieves smaller loss than projected MFLD (Section 5).
∴ MMFLD is "the first algorithm minimizing (1) with global convergence guarantees" (Section 1.1).

---

## Strongest Counter-Argument
Even granting the steelman, the argument's weakest link is premise 4, and through it the conclusion. The only part of the paper that goes beyond re-reading [NWS22] with a metric is Theorem 4.3. Its discretization error δ_η scales with M = exp(2c₁D/√c₂), where D is defined in the theorem as max‖∇ϕ(u) − ∇ϕ(v)‖² over the domain. But Lemma 2.1(i) says ∇ϕ(X) = R^d and Section 2.1 requires ‖∇ϕ(x)‖ → ∞ at ∂X; so D = ∞ for every admissible mirror map, hence M = δ_η = ∞ and the bound says nothing. Lemma B.2 records the convention "M = 1 when c1 = 0 and D = ∞", i.e., finiteness is obtained only when the self-concordance constant is zero, which is the unconstrained, flat-metric case. Combined with the fact that (a) Assumptions 4 and 8 are not verified for any instance (and Assumption 4 is stated with the Euclidean rather than the mirror Fisher information), and (b) the experiment's barrier violates Assumption 5(i) and uses a different time-stepping than the analysis (one Euler step instead of exact simulation), the paper does not, as written, exhibit a single implementable constrained MMFLD for which a non-vacuous guarantee is proved. What remains is a routine continuous-time rate, conditional on an unverified inequality. "First algorithm with global convergence guarantees" is then a claim about a theorem whose bound is infinite. The authors can answer this only by new analysis (avoiding the sup over the dual space) or by identifying a class with finite D.

---

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence / Logic (criterion 1: the result as stated does not deliver the claimed guarantee) | Theorem 4.3; Lemma 2.1(i); Section 2.1; Lemma B.2 ("when c1 = 0 and D = ∞") | D := max‖∇ϕ(u) − ∇ϕ(v)‖² is infinite for any ϕ with ∇ϕ(X) = R^d, so M and δ_η are infinite and the uniform-in-time bound is vacuous for every constrained example. The abstract advertises this as one of two headline results. The exact formulas for M and ξ_t are partly garbled in the extraction; the definition of D and Lemma 2.1(i) are legible. | Replace the sup by a probabilistic bound on the dual displacement, or restrict the claim to a class with D < ∞ and give one explicit example with all constants finite; otherwise remove "uniform-in-time propagation of chaos" from the abstract | New data/experiments/redesign (new analysis) |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic | Assumptions 4 and 8; Section 2.2; Appendix B.4 | Assumption 4 is stated with the Euclidean Fisher information; B.4 needs a mirror LSI. Neither Assumption 4 nor 8 is verified for any example; "first algorithm with global guarantees" is conditional on them. | State the right inequality, give sufficient conditions and one verified instance |
| DA-M2 | Scope | Abstract, Section 1.1, Section 4.3 | Wording ("first … global convergence guarantees", "sharpest known bounds") exceeds what is proved (claim distortion, E5). The evidence supports a weaker claim, so the fix is narrowing. | Qualify the wording; list assumptions in the abstract |
| DA-M3 | Evidence | Section 5; Figure 1 caption | The barrier at β = 10⁻⁴ violates Assumption 5(i) (gradient norm² = β²Σ1/x_i); no numbers, repeats, or definition of the plotted loss; "higher stability and optimality" unsupported; the β = 0 case is called by the authors a "trivial failure case". | Quantify, repeat, add reparametrization baseline, choose a barrier compatible with Assumption 5 |
| DA-M4 | Logic | Section 4.1; Algorithm 1 line 5 | Analysis assumes exact simulation of the dual diffusion; experiments use one Euler step; "our experiments indicate" it suffices rests on one example. | State as limitation or analyse the one-step scheme |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | Theorem 4.3 vs. B.5; Theorem 4.1; Assumption 3 | Hypothesis lists reference Assumption 2 (Euclidean) where Assumption 5 is used; Assumption 3 refers to (7) instead of (11). |
| DA-m2 | Citations | Section 2.1; bibliography | [OV00] cited for "stronger mirror LSI may not hold"; LZT21a/LZT21b duplicate. |
| DA-m3 | Typos | Section 1.1, Section 3 | "convex F : P2 (X ) → Rd"; "(13) corresponds" should be (12). |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Continuous rate (Thm 3.2) | e^{−2C_LSI λ t} | −λ²FI ≤ −2λ²C·KL ≤ −2λC(L − L*) gives 2Cλ | Yes |
| Discrete rate (Thm 4.3) | exp(−C_LSI λ η k) | Young's inequality halves the Fisher term: −(λ²/2)FI ≤ −λ²C·KL = −λC(L − L*) | Yes |
| δ_η from (21) | δ_η = 2ηM₂⁴M(ηM₁² + 2λd) | ½E‖π‖² ≤ 2NM₂⁴ηM(ηM₁² + 2λd) = Nδ_η | Yes |
| Fixed point of the Grönwall step | Nδ_η/(2C_LSI λ) | u′ ≤ −C_LSI λ u + Nδ_η gives Nδ_η/(C_LSI λ) | **No** (factor 2; medium confidence, display partly garbled) |
| D in Theorem 4.3 | finite (used in M) | max over ∇ϕ(X) = R^d is +∞ | **No** |
| Assumption 5(i) for the Section 5 barrier | bounded by M₁ | ‖∇ δF/δµ‖²_{[∇²ϕ]⁻¹} = β²Σ1/x_i, unbounded as x_i → 0 | **No** |

## Ignored Alternative Explanations
- The better loss of MMFLD in Section 5 could come from comparing different objectives: projected MFLD places mass on ∂Δ₃ where the entropy term is undefined, so the plotted "loss" may not be the same functional for the two methods.
- A softmax/logit reparametrization with Euclidean MFLD might give the same behaviour without the Hessian geometry.
- Slower early convergence of MMFLD may reflect the dual-space step size rather than the geometry.

## Missing Stakeholder Perspectives
Practitioners of constrained neural-network training: no network class is shown to satisfy the assumptions.

## Observations (Non-Defects)
Theorem 3.2's proof is clean. The paper is candid about reusing [NWS22], [Jia21] and [Nit24]. Appendix A is accurate and useful. The definition of the algorithm is precise, and the dual-space formulation (16) is a nice way to present it.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 40 | Headline discretization bound vacuous; assumption misstatement |
| Clarity & Presentation | 60 | Readable; inconsistent hypotheses |
| Novelty & Originality | 52 | Only Theorem 4.3 is new analysis |
| Significance & Impact | 50 | Conditional, no verified instance |
| Experimental Validation | 32 | Off-assumption toy run |
| Reproducibility | 48 | Experiment under-specified |
| Ethical Compliance | 60 | Nothing at stake |

**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper's discretization theorem is vacuous under its own definitions and no instance satisfies the assumptions.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (D = ∞) | kept | Specific, locations given; not answered in the paper (the "D = ∞" convention is restricted to c₁ = 0) |
| R1 | W2 (assumptions) | kept | Specific; the discussion after Assumption 4 is Euclidean only |
| R1 | W3 (experiment) | kept; barrier claim marked "derived" | Computation shown; consistent with the text of Section 5 |
| R1 | W4 (exact simulation) | kept | The paper states the exact-simulation convention itself, so this is framed as a limitation request |
| R1 | Questions 3 and 4 (factor 2; λ in (18)) | kept as Questions, not errors | Displays partly garbled in the extraction; unverifiable-grade |
| R2 | W1 (novelty modest) | rewritten | Novelty statement made to match the abstracts of [Jia21]/[Nit24] titles; no claim that any prior work already proves the result |
| R2 | W2 (missing refs) | kept; references verified | Links from `verify` |
| R2 | W3 ([OV00]) | rewritten as request | Based only on the bibliography title; Medium confidence |
| R3 | W1 (practical regimes) | kept | Specific to Algorithm 1 and Theorem 4.3 |
| R3 | W2 (no NN instance) | kept | Section 4.2 gives no instance |
| R3 | W3 (alternatives) | kept | Actionable |
| R3 | "No limitations paragraph" | moved to Minor | Cosmetic for a theory paper |
| R4 | W1 (wording) | kept | Section 1.1 wording quoted |
| R4 | W2 (presentation) | kept; typos moved to Minor | Affects checkability, not only style |
| R4 | W3 (experiment too small) | kept | Merged with R1-W3 in Phase 2 |
| DA | DA-C1 | kept as CRITICAL for the EIC to rule on | Quote and location legible; exact M formula partly garbled |
| DA | DA-M1–M4 | kept | Specific |

Scores unchanged.

---

# Phase 2: Synthesizer Part A: Package for the EIC

### Master issue list
| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Theorem 4.3 bound infinite (D = ∞) | R1-W1, DA-C1 | **DA-CRITICAL** (also CONSENSUS-2); outcome may hinge |
| I2 | Uniform LSI assumptions (4, 8) unverified; Assumption 4 misstated; no instance | R1-W2, R3-W2, R4-W1, DA-M1 | CONSENSUS-4 |
| I3 | Experiment thin and outside Assumption 5(i); no numbers or repeats | R1-W3, R3-W1/W3, R4-W3, DA-M3 | CONSENSUS-4 |
| I4 | Wording "first / global guarantees / sharpest" overstated | R2-W1, R4-W1, DA-M2 | CONSENSUS-3 |
| I5 | Analysis assumes exact diffusion simulation vs. one-step experiment | R1-W4, DA-M4 | CONSENSUS-2 |
| I6 | Hypothesis lists and notation inconsistent | R1-ERR-3, R4-W2, DA-m1 | CONSENSUS-3 |
| I7 | Modest technical novelty | R2-W1 vs. R3-S1/R2-S1 | SPLIT |
| I8 | Missing references (projected Langevin, mirror descent in measure space) | R2-W2 | SOLO |
| I9 | No comparison with reparametrization alternatives | R3-W3 | SOLO |
| I10 | Citation slips ([OV00], duplicate entry) | R2-W3, DA-m2 | CONSENSUS-2 |

Outcome may hinge on: I1, I2. Integrity signals: none (injection scan clean); a text-overlap flag with Nitanda (2024) is noted as standard shared phrasing with a cited source.

### Official score (before EIC weights; DA-C1 provisionally upheld)
Official ratings R1 3, R2 4, R3 4, R4 3, DA 2 → mean 3.20; official composite 55.5. Dimension spread flagged ⚠ for Technical Rigor (24: R1/DA low versus R2/R3 high). Output saved in `before.json`.

---

# Editorial Decision

## Paper: Mirror Mean-Field Langevin Dynamics
## Submission ID: iclr26-Lvkbe0CgmZ
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: theoretical
## Review Team (fictional personas): EIC Prof. Halvard Teixeira; R1 Methodology Dr. Mei-Ling Castellanos, R2 Domain Prof. Tobias Nwankwo, R3 Perspective Dr. Priya Valdivieso, R4 Generalist Dr. Anand Mbeki-Larsen, DA Prof. Lucía Okonkwo-Brandt

---

## Decision: Borderline Reject (3). ICLR rating: 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}); ICLR sub-scores Soundness 2, Presentation 3, Contribution 2 (scale status: secondary)

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 3, DA 2 → mean 3.20 · official composite 55.5
**EIC assessment** (internal): weighted rating 3.02 → starting point 3 · weighted composite 54.0 → band 3 (cross-check agrees) · **DA ceiling**: 3 · **Final (EIC)**: 3
**Journal recommendation**: not applicable (conference target).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The paper closes an explicitly stated gap (constrained mean-field Langevin), the construction is natural, the continuous-time theorem is correct, the exposition is clear and honest about what is imported, and the related-work appendix is accurate. Theory papers of this kind are routinely accepted at ICLR with strong assumptions.
- **Against acceptance:** The one piece of new analysis, Theorem 4.3, has an infinite constant under the paper's own definitions, so the advertised uniform-in-time propagation of chaos is vacuous for every genuinely constrained case. The remaining result is a routine adaptation conditional on a uniform mirror LSI that is misstated (Assumption 4) and verified for no instance, and the single experiment falls outside the assumptions and is not quantified.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| D = max‖∇ϕ(u) − ∇ϕ(v)‖² is infinite, so M and δ_η are infinite | R1-W1, DA-C1 | Theorem 4.3; Lemma 2.1(i); Section 2.1; Lemma B.2 | **Verified** | The definition and Lemma 2.1(i) are legible; the exact formula of M is partly garbled, so I rely on the definition of D and on the "c1 = 0 and D = ∞" convention |
| Assumption 4 uses the Euclidean Fisher information while B.4 uses the mirror one | R1-ERR-1, DA-M1 | Section 2.2; Appendix B.4 | **Verified** | A one-line fix, but it shows the assumption was not examined for any instance |
| The barrier in Section 5 violates Assumption 5(i) | R1-ERR-4, R3, DA-M3 | Section 5; Assumption 5 | **Verified** (derived) | With ∇²ϕ = diag(1/x_i), the dual-norm² of the barrier gradient is β²Σ1/x_i |
| Theorem 3.2's proof is correct | R1-S2, R2-S3 | Appendix B.4 | **Verified** | Steps re-derived given the assumptions |
| "First algorithm … global convergence guarantees" overstated | R2-W1, R4-W1, DA-M2 | Section 1.1 | **Partly correct** | The sentence is hedged by "to the best of our knowledge" and the literature check found no contrary prior work (arXiv only); the overstatement is that the guarantee is conditional on unverified LSI assumptions |
| Grönwall fixed point off by a factor 2 | R1-Q3, DA numerical check | Thm 4.3; proof after (21) | **Partly correct** | My derivation agrees (Nδ_η/(C_LSI λ)), but the display is partly garbled; a constant, not qualitative |
| [OV00] does not support the sentence | R2-W3, DA-m2 | Section 2.1 | **Partly correct** | Only the bibliography title was available; a request for clarification, not an error |
| Text overlap with Nitanda (2024) | similarity scan | Section 1, Section 4.2 | **Verified (shared standard phrasing)** | Source cited throughout; for the editor's information only, no effect on scores |
| Aubin-Frankowski et al. and Bubeck et al. missing | R2-W2 | Section 5, Appendix A | **Verified** | Not found in the paper's bibliography; links verified |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.5 | Every MAJOR error-log entry verified at its location (D = ∞, Assumption 4, barrier violating 5(i)); decisive and well calibrated |
| R2 (Domain) | 4 | 4 | 0.75 | Positioning and references verified, but the rating rests on "technically sound" for Section 4 whose headline bound is infinite; [OV00] point rests on the title only |
| R3 (Perspective) | 4 | 3 | 0.75 | Useful practical points, but the assumption audit overlooks that the paper's own barrier violates Assumption 5(i), and the rating rests on the assumptions being benign |
| R4 (Generalist) | 3 | 3 | 1.0 | Well calibrated for a median submission; did not rederive proofs but nothing overstated |
| DA | 2 | 4 | 1.25 | DA-C1 verified; DA-M1 to M4 verified; rating of 2 is slightly harsher than the ruling below supports |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes. Section 4 is half the paper and the abstract names the propagation-of-chaos result as one of two headline results. Without it the paper contains a routine adaptation of [NWS22] under an unverified inequality. Criterion 1: the stated result, under the paper's own definitions, does not deliver the claimed guarantee (the bound is infinite). This is not a missing baseline, a single run or an overclaim that survives in weaker form: no non-trivial weaker version is stated. | **Upheld** | New data/experiments/redesign (new analysis or a class with D < ∞ and a worked example) |

### Final Decision and Justification
The EIC-weighted rating is 3.02, so the starting point is 3 (Borderline Reject); the weighted composite (54.0, band 3) agrees, and I do not depart from the starting point. The upheld DA-CRITICAL issue caps the decision at 3, since fixing it needs new analysis; the final decision is 3, which does not exceed the ceiling. The two accept-leaning ratings (R2, R3) are down-weighted for a specific, verified reason: both rest on the assumptions and constants being sound, and Step 2 showed that the headline constant is infinite and that the paper's own experiment leaves the assumptions. My pool position is **45** (better than about 45% of ICLR submissions): the work is clean, correct in continuous time and clearly positioned, which keeps it above the weakest submissions, but its new analysis is vacuous as stated, no instance satisfies its assumptions and its experiment is thin, which is typical of a rejected submission. The weaknesses are not of the kind accepted theory papers usually carry (a missing baseline or a strong-but-standard assumption backed by one verified example): here the central quantitative claim does not hold as written. A revision that fixes Theorem 4.3 (or restates it for a class with finite D, with one verified example) and corrects Assumption 4 would plausibly move this to Borderline Accept.

---

## Score Summary

### Official Scores and EIC Assessment

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.50 | 30% |
| R2 (Domain) | 4 | 0.85 | 0.75 | 15% |
| R3 (Persp.) | 3 | 0.70 | 0.75 | 12% |
| R4 (Gen.) | 3 | 0.70 | 1.00 | 17% |
| DA | 4 | 0.85 | 1.25 | 25% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 62 | 64 | 58 | 40 | 54.8 | 52.4 | 24 ⚠ |
| Clarity & Presentation | 62 | 64 | 66 | 60 | 60 | 62.4 | 62.0 | 6 |
| Novelty & Originality | 52 | 60 | 62 | 56 | 52 | 56.4 | 55.1 | 10 |
| Significance & Impact | 55 | 62 | 64 | 55 | 50 | 57.2 | 55.9 | 14 |
| Experimental Validation | 38 | 45 | 48 | 40 | 32 | 40.6 | 39.1 | 16 |
| Reproducibility | 50 | 55 | 58 | 52 | 48 | 52.6 | 51.6 | 10 |
| Ethical Compliance | 60 | 62 | 70 | 62 | 60 | 62.8 | 61.9 | 10 |
| **Composite** | 52.1 | 59.8 | 62.5 | 55.6 | 47.5 | **55.5 (before)** | **54.0 (after)** | |
| Pool position (P%) | 45 | 65 | 66 | 50 | 35 | | | |

The Technical Rigor spread (24) comes from R1 and the DA (50, 40), who checked Section 4's constants, versus R2 and R3 (62, 64), who did not; the editor adopts the first view because it was verified.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}); skill-internal Overall 3 = Borderline Reject |

Upheld DA-CRITICAL cap applies to every venue. Cross-venue comparison was not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Mirror Mean-Field Langevin Dynamics" to ICLR. You address a gap that the mean-field Langevin literature has left open, optimization over measures on constrained convex domains, with a natural geometric construction.

**Overall Assessment:**
The panel appreciated the clear motivation, the correct continuous-time convergence theorem and the honest account of what is imported from earlier work. The panel was divided on significance, and concerns about the discretization theorem, the verification of the assumptions and the experiment weighed most.

**Key Strengths Identified by Reviewers:**
1. A well-motivated, previously open problem with a natural solution (R2, R3, R4).
2. Theorems 2.2 and 3.2 are correct given their hypotheses (R1, R2).
3. Clear exposition and accurate related-work appendix (R2, R4).

**Key Concerns Requiring Attention:**
1. Theorem 4.3: the constant D is infinite under the paper's own conditions, so the uniform-in-time propagation-of-chaos bound is vacuous for constrained domains (R1, DA; CRITICAL).
2. Assumptions 4 and 8 are not verified for any example, and Assumption 4 is stated with the wrong Fisher information (CONSENSUS-4).
3. The experiment is a single 3-dimensional run without numbers or repeats, and its barrier violates Assumption 5(i) (CONSENSUS-4).

**Critical Challenge (Devil's Advocate):**
The only analysis that goes beyond transferring [NWS22] to a metric is Theorem 4.3, and its error term is infinite for any mirror map satisfying Lemma 2.1(i). Authors need either a new argument for the dual-space displacement or a class with finite D and a worked example.

**Decision: Borderline Reject (3)**

The ceiling set by the upheld critical issue and the weighted ratings both point to 3. A revision with a non-vacuous discretization theorem (or a restated theorem for a class with finite D), a corrected mirror LSI assumption with at least one verified instance, and a quantified experiment would materially change the assessment. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Halvard Teixeira
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Assumptions 4 and 8 unverified; Assumption 4 misstated | R1, R3, R4, DA | CONSENSUS-4 |
| Experiment thin, off-assumption | R1, R3, R4, DA | CONSENSUS-4 |
| Overstated headline wording | R2, R4, DA | CONSENSUS-3 |
| Hypothesis lists and notation inconsistent | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Technical novelty | R3, R2 (positive on the construction) | R2 (modest), R1, DA | Modest: Theorem 3.2 and Theorem 4.1 are adaptations; only Theorem 4.3 is new analysis, and it is vacuous as stated |
| Soundness of Section 4 | R2, R3 (no objection) | R1, DA (D = ∞) | Verified against the paper: R1 and DA are right |

### Score Spread Discussion
Technical Rigor (24): R1 50 and DA 40 versus R2 62, R3 64, R4 58. The editor adopts the lower view because the infinite constant was verified at its location.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Theorem 4.3 bound infinite (D = ∞) | Yes (R1-W1) | Upheld | New analysis / class with D < ∞ |
| DA-M1 | MAJOR | Assumptions 4, 8 unverified; Assumption 4 misstated | Yes (R1, R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | Wording exceeds results | Yes (R2, R4) | n/a | n/a |
| DA-M3 | MAJOR | Experiment off-assumption, unquantified | Yes (R1, R3, R4) | n/a | n/a |
| DA-M4 | MAJOR | Exact simulation versus one Euler step | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Theorem 4.3 bound infinite (D = ∞) | DA-C1, R1-W1, R1-ERR-2 | Theorem 4.3; Lemma 2.1(i); Lemma B.2 | Bound the dual displacement probabilistically (using the noise covariance ∇²ϕ(X₀)) or restate for a class with D < ∞ with one explicit example with all constants finite; update abstract | High (new proof, weeks; no GPU) | No |
| R2 | Assumptions 4 and 8 misstated or unverified, no instance | R1-W2, R1-ERR-1, R3-W2, R4-W1, DA-M1 | Section 2.2; Assumptions 4, 5, 7, 8; B.4 | State Assumption 4 with the mirror Fisher information; give sufficient conditions in Hessian geometry; verify all assumptions for one worked class (e.g., ball-constrained two-layer network with ϕ(x) = −log(1 − ‖x‖²)) | Medium to high | Partly (the restatement yes, the worked example probably not) |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Experiment thin and off-assumption | R1-W3, R1-ERR-4, R3-W1/W3, R4-W3, DA-M3 | Define the plotted loss; ≥5 seeds with mean ± std; rate plot (log(L − L*) versus t) and an N sweep; a barrier compatible with 5(i); reparametrization baseline; one higher-dimensional run | Low to medium; < 10 GPU-hours | Yes |
| S2 | Overstated wording | R2-W1, R4-W1, DA-M2 | Qualify "first/global/sharpest"; list assumptions in the abstract; "what is new" paragraph per theorem | Low | Yes |
| S3 | Exact diffusion simulation versus one Euler step | R1-W4, DA-M4 | State as a limitation; vary sub-steps in the experiment | Low to medium | Yes |
| S4 | Hypothesis lists and notation | R1-ERR-3, R4-W2, DA-m1 | Fix assumption lists (2 → 5 in Theorem 4.3, Theorem 4.1, Assumption 3); notation table; index LSI constants | Low | Yes |
| S5 | Missing references | R2-W2 | Add and discuss: Aubin-Frankowski–Korba–Léger (NeurIPS 2022); Bubeck–Eldan–Lehec (DCG 2018) | Low | Yes |
| S6 | Constants in the Grönwall step and in (18) | R1-Q3/Q4, DA | Recheck the factor 2 and the placement of λ, update Theorem 4.3 | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Comparison with reparametrization/penalty alternatives | R3-W3 | Short discussion of when changing geometry beats changing coordinates |
| N2 | Practical regimes (dimension, boundary conditioning, cost) | R3-W1 | Practical-considerations paragraph |
| N3 | Citation slips ([OV00], duplicate LZT21), Deb et al. 2023 | R2-W3, DA-m2 | Correct or add; mention concurrent work (arXiv 2508.16428, 2509.03124) if desired |
| N4 | Typos; limitations paragraph | R1, R4 | "dyamics", "Riemmanian", "whave"; F : P2(X) → R; (12)/(13); one-paragraph limitations |

## Estimated Revision Effort
- Priority 1: 2 items, estimated 3–6 weeks (a new proof argument plus a worked example)
- Priority 2: 6 items, estimated 1–2 weeks including < 10 GPU-hours
- Priority 3: 4 items, 1–2 days
- **Total estimated revision time**: about 1–2 months, dominated by Theorem 4.3

*Simulation notice: this outcome is how a careful panel would likely see this draft; it is not a prediction of any real decision.*
