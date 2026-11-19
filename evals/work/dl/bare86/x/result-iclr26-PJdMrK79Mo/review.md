# Review: Sample-efficient and Scalable Exploration in Continuous-Time RL (COMBRL)

*Figures were not available. Figure-based claims are judged from captions and surrounding text only.*

## Summary
The paper proposes COMBRL, a continuous-time model-based RL algorithm. It plans in a learned probabilistic ODE model (GP, or ensemble/BNN) and maximizes (r + λ_n‖σ_{n-1}‖)/(1+λ_n). The model is the posterior mean (or a Lipschitz surrogate for GPs), not an optimistic model chosen from the confidence set. This replaces the intractable joint optimization over policy and dynamics in OCORL (Treven et al., 2023). The objective is the continuous-time analogue of SOMBRL (Sukhija et al., 2025b) and MaxInfoRL. The paper claims two theoretical results:
- Theorem 1: a regret bound O(√(I_N³ N)) in the reward-driven case.
- Theorem 2: a sample-complexity bound O(√(I_N³/N)) for the unsupervised case (λ→∞).

Experiments include:
- GP-based Pendulum and MountainCar, compared with OCORL, PETS and mean planning.
- Gym/DMC tasks with probabilistic ensembles and SAC, using auto-tuned λ.
- Zero-shot downstream-task evaluation, comparing balanced and unsupervised variants.
- A λ ablation.
- A time-adaptive (TaCoS) setting.

## Strengths
- The question is well motivated: tractable optimism for continuous-time MBRL, with a single knob interpolating between exploitation, balanced exploration and pure exploration.
- The method is simple, model-agnostic and easy to implement. It removes the (d_x + d_u)-dimensional reparametrization used by OCORL.
- Code is released. The appendix gives hyperparameters and GP experiment details.
- The unsupervised variant shows better downstream generalization on the 7 reported domains, and the λ ablation (Fig. 4) gives an interpretable trade-off.
- It covers several settings: GP, ensembles, and the TaCoS adaptive-sampling setting.

## Weaknesses
1. **Limited novelty.** The core objective (reward + λ·epistemic uncertainty, normalized by 1+λ) is essentially SOMBRL (Sukhija et al., 2025b) and MaxInfoRL, moved to continuous time. The theory reuses Treven et al. (2023) components: Lemma 4 on trajectory deviation, Proposition 1 on model complexity, and the MSS machinery. The paper says continuous time "requires different theoretical analysis" but does not identify what is new beyond citing OCORL lemmas.
2. **The theory does not match the algorithm that is run.**
   - The regret bound needs λ_n = 2β_n L_r(1+L_π)e^{L*(1+L_π)T}. This is large and exponential in the horizon. In the experiments λ is hand-tuned (1.0, 10⁶) or auto-tuned, and never set by the theorem.
   - The proof gives a bound with a factor (λ_N² + 2λ_N), which contains β_N and e^{LT}. The main-text Theorem 1 hides this factor. Its constants need discussion.
   - The main text states I_N^{3/2}√N, while the appendix proof ends at √(N I_N) times the λ factor. The discrepancy should be explained.
   - The main text says Theorem 1 holds under Assumptions 1–3. The proofs use Assumption 4 (RKHS), the GP-specific Lipschitz surrogate f_n, and monotone variance. The bound is a GP result. For BNN/ensemble models (used in all deep experiments) Assumption 3 is asserted via "re-calibration", with no verification.
   - In practice µ_n is used, which "might not lie in M_{n-1} ∩ F" (footnote 2). The theory is therefore not about the evaluated algorithm.
3. **Theorem 2 and its proof look unsound or at least unclear.**
   - The theorem is stated for λ_n → ∞, yet the proof carries a factor (1+λ_N)², so the bound diverges. With the (1+λ) normalization and r = 0 the objective is λ-independent, so the bound should not depend on λ. The statement is inconsistent with the proof.
   - The proof chain has a missing 1/N in one step and a Cauchy–Schwarz step that is not explained.
   - The first inequality relies on monotonicity of σ, which is assumed outright for general models.
   - The result bounds the maximal uncertainty integral along a trajectory. It does not translate into error on the dynamics or into a downstream-task guarantee, which is what the experiments claim.
   - The main-text Theorem 2 has I_N³/N under the root, the appendix I_N³ under N. These need reconciling.
   - Lemma 4 uses L_f in one inequality and L_B in the other. The index (σ_{n-1} vs σ_n) is inconsistent between Eq. (3), Eq. (7) and the lemmas.
4. **The scalability claim is weakly supported.** The only head-to-head comparison with OCORL is on Pendulum and MountainCar with GPs, 5 seeds, and a single "≈3× compute" figure. No comparison with any optimistic-dynamics method is given on the higher-dimensional Gym/DMC tasks, where scalability is claimed. On those tasks OCORL is intractable, so "scales better than prior methods" rests on a non-comparison. On the GP tasks the return advantage over OCORL is "matching or exceeding", not clearly better.
5. **Missing baselines for the deep RL claims.** Baselines are only mean planning (≈ Yildiz et al.) and PETS. The paper omits:
   - SOMBRL / MaxInfoRL, the closest discrete-time versions. These are needed to show that continuous time matters.
   - Modern MBRL (MBPO, TD-MPC2, DreamerV3).
   - Intrinsic-motivation methods (disagreement/Plan2Explore, OPAX) for the unsupervised claim.
   - A discrete-time COMBRL with the same ensemble.
   The headline "outperforms baselines across several deep RL tasks" is therefore weakly supported.
6. **The experiments hardly exercise continuous time.** The deep RL experiments use fixed-rate control and equidistant sampling on ordinary Gym/DMC simulators, with a fine discretization. In substance this is discrete-time MBRL with an ODE-parametrized model. The theory requires |S_n| growing with n, but experiments use a fixed rate (ν = 20 or 1). The only adaptive-sampling experiment is TaCoS (Fig. 5), on two tasks. Fig. 5 reports only final returns, so the claim of "fewer interactions" and sample efficiency cannot be read from it.
7. **Statistical rigor and fairness.**
   - Seeds are 5 (GP) or 10, with standard-error bands only and no significance analysis. "Higher asymptotic returns" is claimed for curves that may overlap within error.
   - λ is hand-tuned per environment (static case) or auto-tuned using a method from prior work. The tuning budget for COMBRL and for the baselines is not described. The OCORL baseline gets β fixed, and λ = 10⁶ for MountainCar suggests heavy tuning.
   - Model quality (for example, held-out dynamics error) is never measured directly in the unsupervised downstream study (Fig. 3), so the claim of a "globally accurate model" is untested.
   - Some claims are inflated, such as "state of the art" or "largest gains in sparse tasks", with no analysis of why.
8. **Assumptions are strong and under-discussed.** The GP experiments assume noise-free access to state derivatives. The system is deterministic, with known simulators and Lipschitz policies. The paper's real-world continuous-time motivation is not tested: there is no experiment with noisy derivatives or hardware.

## Questions
1. Can the authors give the exact statement of Theorem 1 including the dependence on λ_N, β_N and e^{LT}, and reconcile I_N^{3/2} vs I_N between the main text and appendix? What does the bound become with λ_n as chosen in experiments?
2. For Theorem 2, why does the bound depend on λ when λ→∞? Can the proof be fixed so this factor disappears? Does the result imply anything about the global model error ‖f* − µ_N‖ or downstream regret?
3. What is the justification for the guarantees when the planner uses µ_n rather than a member of M_{n-1} ∩ F, and with ensembles whose calibration is not verified?
4. How does COMBRL compare with SOMBRL/MaxInfoRL, and with a discrete-time COMBRL with the same ensemble and planner? Which gains are specific to the continuous-time formulation?
5. Can you show OCORL (or an approximation) on a higher-dimensional task to substantiate scalability? Does the 3× compute gap grow with dimension?
6. How were λ, β and baseline hyperparameters tuned? What happens with a single λ across all environments?
7. For Fig. 5, can you report return vs. number of interactions, not just final returns?

## Scores
- **Soundness:** 2. The theory has gaps and inconsistencies and does not cover the implemented algorithm. The empirical claims are partly supported.
- **Presentation:** 3. The paper is clearly organized, but theorem statements are inconsistent and some claims are overstated.
- **Contribution:** 2. Incremental relative to SOMBRL and OCORL, with limited evidence that continuous time matters in the evaluated setups.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 3**
