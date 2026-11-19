# Review: Principled Out-of-Distribution Generalization via Simplicity (ICLR 2026)

Note: I read the main text through the references. The appendix proofs were not read in detail. Figures are unavailable, so Figures 1 and 2 are judged from captions and text only.

## Summary
The paper argues that OOD generalization, in particular compositional generalization in diffusion models, can be explained by a simplicity principle. Among all parameters that minimize the source-domain loss, the generalizing one (β*) is assumed to be the one with the smallest value of a complexity measure R.

The motivation is empirical. A diffusion model on 28×28 circle images with 3 binary attributes generalizes to 4 held-out attribute combinations. A 2-layer MLP learns the identity map on R³ from 4 source clusters. Models forced to deviate from the identity on the target clusters (uniform, permutation and flipped/interpolated maps) have larger summed squared weight norms than the identity-generalizing model.

The theory studies the regularized MLE β̂λ = argmin ℓn(β) + λR(β) under covariate shift, in a well-specified parametric model. It gives two results:
- Theorem 4.1 (constant gap): with a simplicity gap ∆ > 0 and strong convexity, the target excess risk is Õ(Tr(I_T I_S⁻¹)/n + (term)/(∆² n)).
- Theorem 4.2 (vanishing gap): under a Hölder-type condition ‖β0−β*‖ ≤ (R(β0)−R(β*))^τ with τ ≥ 9 and a manifold of source minimizers, the rate is Õ(n^{-1+2/(3τ)}).

The paper calls these "the first sharp sample complexity guarantees" for learning the true simple model.

## Strengths
- The question is important and timely: formalizing implicit simplicity bias as a mechanism for extrapolation outside the training support.
- The controlled synthetic setting, with multiple source-perfect solutions of differing norms, cleanly illustrates non-identifiability.
- The theorems are non-asymptotic. They recover Ge et al. (2023) when BS is a singleton, and the dependence on Tr(I_T I_S†) has a sensible interpretation.
- The vanishing-gap regime with a manifold of source minimizers, handled via a pseudoinverse, is a nontrivial extension of the unique-minimizer setting.
- The writing is clear, and the paper is candid about the equivalence-class limitation.

## Weaknesses
1. **The central hypothesis is assumed, not derived, and the theory is close to circular.**
   - The key assumption is β* = argmin_{β∈BS} R(β). Given this, the result that a regularized estimator with R recovers β* is largely a consequence of the definition.
   - The theory does not explain why simplicity under a given R governs generalization in diffusion or foundation models. It does not say which R is right, why SGD or the architecture would implement it, or when the hypothesis fails.
   - The title and abstract ("principled OOD generalization", explaining foundation models) overreach. What is proved is a statistical analysis of regularized MLE when the right regularizer is known and λ is tuned using ∆.

2. **The empirical evidence for the "simplicity" claim is weak and confounded.**
   - The diffusion experiment shows only that generalization happens. No complexity measure is computed for the diffusion model, and no non-generalizing diffusion solutions are compared.
   - In the MLP experiment, the non-generalizable models are trained on 800 samples that include deliberately contradictory target mappings (e.g. outputs shifted into [0,2]³). They need larger weights simply because they fit a more complicated function. This does not show that simplicity selects the generalizing solution.
   - The experiment does not test the actual claim: that source-only training (SGD, with or without weight decay) finds the min-norm source-perfect solution, or that norm predicts failure among source-only trained networks.
   - The identity task is privileged (near-linear), so it is unclear that the generalizable model is generically norm-minimal.
   - Only "a well-initialized and optimized MLP" is reported, with no seed statistics. I could not view Fig. 2.

3. **The assumptions do not fit the motivating neural-network or diffusion setting.**
   - A.1 requires uniform concentration of ℓn over all β with a constant B0 (effectively bounded loss). A.2 requires a bounded third derivative for all β, x, y. Neither holds for log-likelihoods of neural networks or diffusion models.
   - A.3 assumes a gap between the global minimum and all other local minima. This is effectively an assumption that the non-convex problem is benign.
   - The estimator is the global minimizer of ℓn+λR, so optimization is ignored, even though the paper's motivation is overparameterized networks.
   - The regime is underparameterized with fixed d and n→∞, the opposite of foundation models. The link between theory and the motivating examples is tenuous.
   - A.4 requires R to be convex and L-smooth, which fits ‖β‖² but is unrelated to "structural complexity" in a network.

4. **The constant-gap and vanishing-gap conditions are restrictive.**
   - B.1 and B.2 imply that BS consists of isolated strongly convex minima with a minimum simplicity gap. Compositional generalization typically involves a continuum of spurious solutions, as in the paper's own uniform-map example.
   - C.3 requires τ ≥ 9. No example, including the MLP, is given in which C.1–C.3 or τ are verified.
   - No lower bound shows that the exponent −1+2/(3τ) is sharp in the vanishing-gap case.
   - The paper itself notes that symmetries (β vs −β) violate C.3. This is a serious limitation, since symmetric parameterizations are ubiquitous in neural networks. The proposed quotient-space fix is only conjectured.

5. **"Sharp" and "first" claims are overstated.**
   - Minimax optimality is inherited from Ge et al. (2023) for the unique-minimizer case only. There is no lower bound for the ∆-dependence or for the regularization term in the new regimes.
   - The sample-size thresholds N* and N′ are polynomial in many constants (∆⁻¹, G⁻¹, ...), so the results may hold only for very large n.
   - λ depends on the unknown ∆ (or ∆max) and B0, and adaptivity is not discussed.
   - The introduction states the rate as n^{1−3τ}, which is inconsistent with the theorem (n^{-1+2/(3τ)}).
   - Related work on implicit regularization, minimum-norm interpolation under covariate shift, and simplicity/Occam-type generalization (MDL, implicit bias of gradient descent) is thin. The idea that simplicity drives generalization is not new.

6. **Presentation and completeness.**
   - The experiments are small and lack quantitative detail (number of seeds, how target error is measured).
   - The reference list contains duplicates (Dhariwal & Nichol 2021a/b, Ho et al. 2020a/b).

## Questions
1. Can you show that source-only trained networks land on the min-norm source-perfect solution, and that norm among source-perfect networks predicts target failure?
2. For the diffusion model, what is a meaningful R, and can it be computed for generalizing versus non-generalizing checkpoints?
3. Is there any model class (e.g. linear or two-layer networks) in which Assumptions A–C, including τ, can be verified?
4. Is the rate n^{-1+2/(3τ)} tight? Is τ ≥ 9 only technical?
5. What happens if R is mis-specified, i.e. the R-simplest source-compatible solution is not β*? Is there a robustness statement?
6. How should λ be chosen without knowing ∆?
7. How do the results differ from standard analyses of ridge or min-norm regression under covariate shift with a degenerate source covariance?

## Ratings
- **Soundness:** 2. The theorems appear plausible and technically careful given their assumptions, but the assumptions are strong and the link to NN or diffusion models is not established.
- **Presentation:** 3
- **Contribution:** 2

**Rating:** 4 (marginally below the acceptance threshold)

**Confidence:** 3
