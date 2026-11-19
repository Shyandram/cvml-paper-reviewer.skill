# Review: Mirror Mean-Field Langevin Dynamics (ICLR 2026 submission)

*Note: figures were not available. My comments on Figure 1 rest on the caption and text only.*

## Summary

The paper studies entropy-regularized distributional optimization, min_µ F(µ) + λEnt(µ), over probability measures supported on a convex set X ⊂ R^d. It combines mirror Langevin dynamics (MLD) with mean-field Langevin dynamics (MFLD) into the "mirror mean-field Langevin dynamics" (MMFLD). Particles evolve through a Hessian-metric diffusion in the dual space, with the drift given by the first variation of F.

The paper gives three kinds of results.

1. **Continuous time.** Under a mirror LSI assumption on the proximal Gibbs measure, the objective gap L(µ_t) − L(µ*) decays at rate e^{−2C_LSI λ t} (Thm 3.2). The proof is the NWS22 argument with the Fisher information replaced by a mirror Fisher information.
2. **Particle approximation.** The static particle-approximation bound of Nitanda (2024) is extended to convex X (Thm 4.1).
3. **Discretized algorithm.** For the time- and particle-discretized algorithm, the paper gives a uniform-in-time bound on the per-particle objective gap (Thm 4.3). It combines Jiang (2021) with Nitanda (2024), using a "forward" discretization from Ahn & Chewi (2021) and an assumed uniform-in-N mirror LSI.

A single toy experiment (3-simplex, entropic mirror map) compares MMFLD against projected MFLD.

## Strengths

- The problem is well motivated. Constrained domains do arise in MFLD applications (barycenters, trajectory inference, bounded parameters), and the global-noise issue is real.
- The mirror approach is a natural idea. The continuous-time analysis is clean, and the proof structure in B.1/B.4 is easy to follow. The observation that the entropy sandwich survives on convex X, and that µ* ∝ exp(−δF/λ) is preserved in primal coordinates, is a useful sanity check.
- The paper is honest that the proofs largely follow NWS22, Jia21 and Nit24. Related work is covered well.
- The toy experiment shows the qualitative boundary-accumulation artifact of projection, which motivates the method.

## Weaknesses

1. **The central discrete-time bound appears vacuous for the mirror maps the method needs.**
   - Thm 4.3 has M = exp(2c₁D/√c₂) with D = max_{u,v}‖∇φ(u) − ∇φ(v)‖². The paper requires ‖∇φ(x)‖ → ∞ at ∂X (Sec. 2.1) and the dual space is all of R^d, so D = ∞ and M = ∞. This holds for the entropic map used in Sec. 5, where ∇φ = log x + 1.
   - The only finite case is the stated convention "M = 1 when c₁ = 0 and D = ∞", which is the Euclidean, unconstrained case.
   - Hence δ_η is infinite and the discretization error term is vacuous for any genuinely constraining barrier. The paper does not acknowledge this, and the abstract and contributions describe the result as holding for "general convex X".
   - The "in expectation" refinement of M in Lemma B.2 gives a finite value, but the proof falls back on the deterministic bound on the exceptional event, which again needs D < ∞.
   - If I have misread this, the authors should give a concrete (X, φ) with finite D and c₁ > 0 that satisfies all assumptions. Otherwise the theorem is essentially empty.

2. **The key functional-inequality assumptions are assumed, not established, and mismatched with their use.**
   - Assumption 4 (uniform LSI) is written with the *Euclidean* Fisher information ("except without the modifier ∇²φ⁻¹"), but the proof of Thm 3.2 uses the *mirror* Fisher information. A Euclidean LSI does not imply the mirror one in general. The notation (abusing C_LSI for all variants) hides this.
   - The paper itself notes (Sec. 2.1) that a mirror LSI may not hold in general. It gives no example of (X, φ, F) where a uniform mirror LSI for all proximal Gibbs measures µ̂ is verified. It offers no mirror analogue of Bakry–Émery / Holley–Stroock / Aida–Shigekawa. Without this, the setting in which Thm 3.2 is non-vacuous is unclear.
   - Assumption 8 (uniform-in-N mirror LSI for µ*^(N)) is the hardest ingredient of uniform-in-time propagation of chaos. In the Euclidean case it required dedicated work (Chen–Ren–Wang, Chewi–Nitanda–Zhang, Wang). Here it is simply assumed. The headline claim of "uniform-in-time propagation of chaos" therefore rests on an unverified assumption that carries most of the difficulty.

3. **Inconsistencies and gaps in the proofs.**
   - Thm 4.3 lists Assumptions 2, 6–8, but the proof uses Assumption 5 (relative Lipschitz). Assumption 2 is the Euclidean version and is not compatible with the stated setting.
   - Thm 3.2 cites Assumptions 4 and 5 but not 3.
   - In (20), the diffusion matrix G₀ (the Hessian inverse at the initial point of the step) appears in the dissipation term and is compared with [∇²φ(x_t)]⁻¹. Lemma B.2 gives this comparison only up to the factor M. Yet the rate e^{−C_LSI λ η k} appears with no M-dependence and without loss of constants. It is unclear how this is justified.
   - Lemma B.2 contains several errors:
     - λ is dropped from the √(2λtd) term in places.
     - The inequality 1 − e^{−d} ≥ 1 − e^{−d/(16c₁²)} needs c₁ ≥ 1/4.
     - The same symbol M is used for a deterministic bound and an "in expectation" bound.
     - Assumption 7 is stated for ∇³φ* but bounded by ⟨u, ∇²φ(x)u⟩ with x in the primal and u in the dual, which is dimensionally confusing.
   - The formula for δ_η has M₂⁴ and M inconsistently placed between (21) and Thm 4.3.
   - Assumption 5(ii) uses W_{2,φ}, which is asymmetric (the weight depends on x′ only). It is not a metric, and the Lipschitz condition in terms of ‖∇φ(x) − ∇φ(x′)‖ is never checked for any example, including the mean-field network (17).
   - Typos suggest the draft is not carefully checked: "F: P₂(X) → R^d" in the contributions, and (13) is referred to for the SDE (12).

4. **The analysis does not cover the algorithm that is run.**
   - Alg. 1 simulates the diffusion exactly (an unrealistic oracle for nonlinear φ*). The experiments use a one-step discretization with no analysis.
   - The mean-field propagation-of-chaos theorem is specialized to the supervised risk F in (17), with Assumption 6(ii) bounding E_{µ*}|h|². The paper does not verify this on constrained domains or show an instance with a mirror LSI.
   - Thm 4.1 is a verbatim reuse of Nit24 (a static bound), so it is not mirror-specific.

5. **Weak and potentially unfair empirical evidence.**
   - Only one d = 3 synthetic problem is run, with no seeds or error bars and no neural-network or realistic application.
   - The baseline is projected MFLD only. Reflected MFLD, other mirror-type or barrier-based approaches, and MLD-with-interaction particle systems are not compared.
   - With β > 0 and the log(1/x) barrier, projected particles that land on ∂Δ get infinite F, so it is unsurprising that projection fails. The claim that MMFLD "achieves significantly smaller loss" is thus partially a property of the objective. In the β = 0 case it is unclear whether lower loss reflects better optimization rather than the different (Lebesgue vs. Hessian) entropy accounting.
   - There is no study of the discretization-error, N, or step-size dependence predicted by Thm 4.3, so the theory is not tested.

6. **Overstated novelty.**
   - "First algorithm minimizing (1) with global convergence guarantees" is too strong. Mean-field Langevin on compact manifolds and with reflection or barrier terms has been analyzed, and Wasserstein-barycenter work (Chizat; Vaskevicius–Chizat) already handles constrained supports.
   - The technical content is largely a direct substitution of the mirror metric into existing proofs (NWS22, Jia21, Nit24). The one genuinely new element, handling the interaction of the mirror geometry with the mean-field nonlinearity (e.g. G₀ vs G_t, the distance W_{2,φ}), is handled in the least careful part of the paper.

7. **Presentation.** The paper is short and reads like a workshop version.
   - The preliminaries recap occupy several pages.
   - The algorithmic discussion of how to compute ∇φ*, Hessians, and the exact diffusion for general X is missing.
   - There is no discussion of computational cost versus projection.
   - Limitations (e.g. the strength of the mirror LSI, the infinite D) are not discussed.

## Questions to the authors

1. For which (X, φ) is D finite while satisfying ‖∇φ‖ → ∞ at the boundary? If none, what does Thm 4.3 imply for the simplex example in Sec. 5?
2. Can you give a concrete F and domain (e.g. a mean-field two-layer network on a box or simplex) for which the uniform mirror LSI for µ̂ (Assumption 4, mirror version) and the uniform-in-N mirror LSI (Assumption 8) are verified? Do the Euclidean tools (Bakry–Émery, Holley–Stroock) extend to the Hessian metric, given that the Ricci curvature of a Hessian manifold can be unfavorable?
3. How is the factor M from Lemma B.2 absorbed in (20), given that G₀ ≠ G_t? Why does the rate not degrade?
4. Why is Assumption 2 listed for Thm 4.1/4.3 and not Assumption 5? Please reconcile the assumption lists, and check Assumption 5 for (17).
5. Does the one-step diffusion used in experiments retain the guarantees, and what is its bias empirically? Could the Euler–Maruyama analysis of LTVW22 be used?
6. Please add experiments with realistic mean-field networks on constrained parameters, comparisons against reflected MFLD or barrier-penalized MFLD, multiple seeds, and an ablation over N and η.

## Ratings

- **Soundness:** 2. The continuous-time theorem is fine conditional on a (never verified) mirror LSI. The discrete-time theorem is vacuous or inconsistent as stated and has errors in its supporting lemma.
- **Presentation:** 2
- **Contribution:** 2. Natural idea, but the theory is a thin adaptation and the experiments are minimal.
- **Rating:** 4 (marginally below the acceptance threshold)
- **Confidence:** 3
