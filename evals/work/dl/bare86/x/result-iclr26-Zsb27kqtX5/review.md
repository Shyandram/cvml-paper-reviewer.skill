# Review: On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering (ICLR 2026)

Reviewed from the extracted text only. Figures were not available, so I judged figure-dependent claims from captions and text. I read the main paper and the limitations section closely. I did not read the appendix proofs (A, B) or the COCO-MIG appendix in detail.

## Summary
The paper studies ratio/product-of-densities steering, p* ∝ ∏ q^(i)_t^{γ_i}, where the experts are pretrained diffusion or flow models with different noise schedules and dimensionalities. It identifies "Marginal Path Collapse": the unnormalised product h_t can be non-integrable at intermediate t even though h_0 and h_1 are integrable.

Contributions:
1. **Criterion.** For experts whose data distribution has compact support, h_t is integrable for all t if C_k(t) = Σ_{i∋k} γ_i(t)/(α_t^{(i)})² > 0 for every coordinate k. It is non-integrable if some C_k < 0 (Thm 2.1).
2. **Correction (ACE).** Add a bump B·t(1−t) to one exponent so that C_k > 0 throughout (Thm 2.2). Simulate the resulting path with a Feynman–Kac-corrector (FKC) style weighted SDE with time-varying exponents plus resampling (Thm 2.3).
3. **Experiments.**
   - A 2D checkerboard toy problem.
   - Flexible-pose scaffold decoration by composing EDM, GeoDiff and DiffSBDD (Eq. 9–10), evaluated on CrossDock subsets, with gains over NR/FKC and over task-specific models.
   - A COCO-MIG result in the appendix.

## Strengths
- **A real, clearly stated failure mode.** The Gaussian example (Eq. 3) shows concretely that valid endpoints do not imply valid intermediate densities. Practitioners who compose experts with different schedules, or use large CFG-style exponents, should know about this.
- **A cheap diagnostic.** For compactly supported data the test depends only on the schedules and exponents, so it can be checked on the sampler grid before any model is evaluated. The tail-dominance argument behind Eq. 4 is plausible and elegant.
- **A minimal fix.** The correction leaves the endpoint exponents unchanged, so the target p*_1 is preserved. The extension of FKC to time-dependent γ_i(t) (Thm 2.3) is a reasonable technical contribution.
- **Prevalence study.** The sweep over 125 schedule triples and several guidance scales (41–80% collapse among heterogeneous ones) supports the claim that this is not an artefact of one contrived choice. This is reported in the main text, but I did not verify it in the appendix.
- **Strong headline numbers** on CrossDock, with the ablation over B showing the expected threshold behaviour (B=10 invalid and bad, B≥20 valid).

## Weaknesses
1. **The theory applies to idealised paths, not to the trained networks actually used.**
   - Thm 2.1 treats q_t^{(i)} as the exact marginal of the interpolant with a compactly supported q_1. The sampler uses learned scores and velocity fields. The EDM, GeoDiff and DiffSBDD checkpoints are not guaranteed to be consistent with the "α_t" used in C_k.
   - The product of learned scores need not correspond to any density, and the paper does not show that the learned fields exhibit non-integrability at the predicted times.
   - The molecular data are mixed continuous/categorical, and the paper admits (Limitations) that categorical variables are outside the theory. So the guarantee does not cover the molecule experiment as run.
   - Sampler discretisation and the ESS/resampling behaviour are also outside the guarantee.
   - "Provably guarantees"/"complete solution" in the abstract and conclusion is therefore overstated.
2. **The criterion is exact only in a narrow setting.**
   - The converse in Thm 2.1 gives non-integrability only for strictly negative C_k. Boundary cases (C_k = 0, where sub-leading terms decide) are not addressed, and C_k as t→1 is a sum of diverging terms.
   - The paper claims the criterion "predicts exactly when collapse occurs", but this holds only for compact-support experts with exact Gaussian smoothing. The Gaussian-mixture case is deferred to the appendix, and the unbounded-support case is not covered.
   - A positive C_k does not imply the density is well conditioned. Near-zero C_k gives huge variance and high weight variance, which is the regime in which the experiments show degradation for large B.
3. **ACE modifies the target path, and the practical consequences are under-analysed.**
   - Moving the exponents in the interior changes the intermediate marginals, so the FK weights (Eq. 8) acquire a γ̇_i log q̃ term proportional to B. Large B means large weight variance and SMC degeneracy; the paper itself notes errors being "linearly amplified" by B.
   - There is no ESS trace, no resampling-count statistics, no particle-count study, and no runtime or NFE comparison against NR/FKC.
   - B is chosen post hoc by performance. The claim that "B=30 works across all schedule combinations" rests on the synthetic study only.
   - Which expert j receives the bump is a free choice, and no ablation over j or over alternative bump shapes is given.
4. **The experimental evidence is small and statistically thin.**
   - The OSR values in Tables 3 and 4 (62.2, 44.4, 33.3, 28.9, 73.3, …) suggest a handful of pockets and a few dozen molecules. The number of pockets, samples per pocket and how the subsets were chosen are not in the main text.
   - There are no confidence intervals or seeds for the molecular tables, although the toy table has 5 seeds.
   - Some numbers are inconsistent. FKC at w=1.4 on CrossDock-SBDD has a better mean than at w=1.2 and 1.3 (−4.16 vs −3.04, −2.39). NR and FKC at w=1.0 should coincide, yet the CrossDock-SBDD Vina mean differs (−3.61 vs −2.28) while the other columns are identical. ACE (w=1.0) equals FKC (w=1.0).
   - The criterion predicts collapse for w>1.1, yet NR/FKC at w=1.1 look fine or even better than at w=1.0 in places. The "catastrophic collapse" narrative therefore rests on noisy numbers.
5. **The "outperforms task-specific models" claim is not a fair comparison.**
   - ACE is reported at the best w (1.2 or 1.3), apparently selected on the evaluation benchmark, while the baselines are fixed.
   - The setups differ: the specialised models are conditioned on a reference scaffold pose and ACE is not, and the training data differ. Vina score is also a weak proxy that improves with stronger pocket guidance, so the comparison mostly shows that stronger guidance lowers docking energy.
   - Diversity, novelty, scaffold preservation, strain energy, PoseBusters-type validity and SA/QED are absent from the main text, so it is not possible to tell whether guidance collapses diversity.
6. **Baselines are limited.**
   - NR and FKC are the only steering baselines. There is no comparison with aligning the schedules of the experts (e.g. re-parameterising one model's time so the α_t match, which is a standard equivalence between VP/VE/linear schedules), with clipping or annealing the guidance scale, or with guidance restricted so that C>0 holds.
   - If schedule reparameterisation removes the heterogeneity, the practical need for ACE would be much weaker. This should be discussed and tested, since the experts are standard Gaussian diffusions.
   - The toy problem is built to mirror the failure, so the gain there (W1 0.28 vs 0.78 for NR) is expected.
7. **Overclaiming and framing.**
   - "Complete solution", "fundamental failure mode", "unstable heuristic → reliable tool", and "+9.57%p on COCO-MIG" as evidence of a "general steering paradigm" are not supported. The COCO-MIG case has no collapse, so a different mechanism (sharper intermediate distributions) is at work, and it sits in the appendix.
   - The novelty of the correction over existing time-varying guidance schedules (e.g., CFG schedulers) deserves more discussion. The novelty is mainly the criterion and the FK derivation.
8. **Presentation.**
   - Essential material (proofs, setup, metrics, hyper-parameters, sample counts) is deferred to a 60+ page appendix.
   - Table 2 has odd entries (e.g. B=30 W2 mean 0.40 with std 0.51 but a tight W1; B=20 marked valid despite very high variance), and there are typos ("cooridnate").
   - Figures 1–4 are central to the story but qualitative.

## Questions
1. Do the learned EDM/GeoDiff/DiffSBDD fields behave like the idealised paths? Can you verify the predicted collapse directly, e.g. via the tail behaviour of the learned log h_t, or an ESS trace, at times where C<0 versus C>0?
2. What happens if each expert's time is re-parameterised to a common schedule so that α_t^{(i)} coincide? Does collapse vanish, and if so what does ACE add in the molecular setting?
3. How many pockets, molecules per pocket and seeds underlie Tables 3–4? Can you provide confidence intervals and diversity, novelty, scaffold-RMSD and PoseBusters-style metrics?
4. Why do NR and FKC differ at w=1.0 on CrossDock-SBDD? How was w selected for ACE, and was that done on the evaluation set?
5. How do ESS, resampling frequency and weight variance scale with B? Would a schedule that keeps C(t) just above 0 do better than a large bump?
6. How is the theory applied to the discrete atom and bond types? What exactly was steered for those variables?
7. Does the criterion extend to non-compactly supported data (e.g. images)? The Gaussian-mixture treatment in B.4 should be summarised in the main text.

## Scores
- **Soundness:** 2 (the idealised theory is plausible but the guarantee is overstated relative to what the experiments implement; the empirical evidence is thin).
- **Presentation:** 2
- **Contribution:** 3 (a useful and under-discussed failure mode with a simple diagnostic).

**Rating: 4** (borderline reject). The core observation and criterion are interesting and potentially valuable, but the claims outrun the evidence. The guarantee does not cover the learned, mixed-type models that were evaluated. The schedule-alignment baseline is missing, and the molecular results are small, lack uncertainty and diversity metrics, and contain internal inconsistencies. I would raise my score if the authors validated the criterion on the actual networks, added the schedule-alignment baseline, and provided larger, statistically sound molecular evaluations.

**Confidence: 3**
