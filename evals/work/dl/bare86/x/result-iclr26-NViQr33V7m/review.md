# Review: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation (ICLR 2026)

*Figures were not available. Figure-dependent claims (Fig. 1 continual learning, Fig. 2 hypergradient norm and sharpness) are judged from captions and text only.*

## Summary
The paper applies sharpness-aware minimization (SAM) to the outer loop of trajectory-matching dataset condensation (MTT-style). The outer variable is the synthetic dataset φ. The perturbation ε is computed in φ-space from the hypergradient of the trajectory-matching loss. The update uses the hypergradient at φ+ε.

SAM would roughly double the cost, so the authors add three things:
- **Truncated unrolling hypergradient (TUH):** backpropagate only through the last inner steps.
- **Trajectory reusing (TR):** start the perturbed inner trajectory from the midpoint τ of the unperturbed one.
- **Closed-form learning-rate update:** a first-order rule for learning the inner learning rate.

They also add Gaussian noise proportional to ||φ_j|| to "smooth" the landscape. Theory consists of a truncation-error bound (Prop. 4.1) and a trajectory-divergence bound (Thm. 4.2).

Experiments cover CIFAR-10/100 and Tiny-ImageNet, ImageNet subsets, ImageNet-1K versus TESLA, cross-architecture transfer, continual learning, and a combination with DATM. Reported gains over FTD/TESLA/MDC are small on standard benchmarks and larger in some cross-architecture cases.

## Strengths
- The problem is reasonable: trajectory-matching outer loops are noisy and generalise poorly across architectures. Bringing flatness ideas to this setting is a sensible and relatively unexplored direction.
- The method is simple and plugs into existing MTT code. The memory and runtime analysis (Tables 1 and 6) is useful, since naive SAM would double the cost. TUH+TR keeps runtime near MTT's and below TESLA's.
- Evaluation breadth is decent: several datasets, ImageNet subsets, cross-architecture transfer, continual learning, and a combination with DATM.
- The cross-architecture results (Table 5, CIFAR-10 IPC 50: AlexNet 56.9 vs 53.8 for FTD, VGG11 63.5 vs 58.4) are the most convincing evidence that the method helps beyond the training architecture.
- Hypergradient-norm and sharpness-dynamics plots (Fig. 2) are a reasonable attempt to connect the mechanism to observed behaviour.

## Weaknesses
1. **In-domain gains are marginal and often within noise.**
   - Table 2 deltas versus FTD are 0.1–0.5 pts on CIFAR-10 (73.9±0.2 vs 73.8±0.3; 67.1±0.3 vs 66.6±0.3), comparable to the reported standard deviations.
   - On CIFAR-100 IPC 10, SATM (43.1) is below FTD (43.4).
   - Table 3 gains over FTD are 0.3–2 pts with overlapping standard deviations.
   - No significance testing is given, and the number of seeds is not clear from the main text. "Noticeable improvement margins" is overstated.

2. **No ablation isolates the role of sharpness minimisation.** This is the central weakness.
   - There is no ablation separating (a) the SAM perturbation, (b) the Gaussian input noise, (c) TUH, (d) TR, and (e) the learning-rate rule.
   - Truncated backpropagation alone is known to help and regularise trajectory matching (TESLA and related work), and the noise perturbation resembles randomised smoothing or data augmentation.
   - Without "MTT + TUH", "MTT + noise" and "MTT + SAM without TR", the gains cannot be attributed to flatness.
   - There is no sensitivity analysis for ρ, γ, τ or ι, although Table 8 shows very high sensitivity to the truncation fraction (see 5).

3. **The link between "flatness" and generalisation of the synthetic set is asserted rather than demonstrated.**
   - Sharpness is defined in φ-space (pixels) of the outer objective. SAM's generalisation argument concerns parameter-space flatness of a model on the data distribution. Why flatness with respect to synthetic pixels should improve transfer to new architectures or tasks is not argued.
   - Fig. 2 (judged from the caption and text) shows a lower hypergradient norm, a smaller variance, and a decreasing L(φ+ε)−L(φ). A lower gradient norm does not equal a flatter minimum, and it is also expected from truncation or from the smoothing noise.
   - There is no comparison of sharpness at convergence between MTT and SATM using a common metric. A decreasing trend during training does not show that the final solution is flatter than MTT's.
   - No Hessian or loss-surface analysis is given.

4. **The theory is weak and partly mismatched with the practical setting.**
   - Prop. 4.1 assumes the inner loop has converged to a locally strongly convex region with α ≤ 1/K. In dataset condensation the inner loop is a short, non-converged trajectory from an expert checkpoint in a non-convex network, so the assumptions do not hold and the exponential decay in N−ι+1 is not informative.
   - The notation is confusing: ι is described as "the number of truncated steps" but the sum runs from ι to N. The bound has a factor 2ι and a max over i∈{0..ι}, which looks inconsistent.
   - Thm. 4.2 gives ||Δθ_τ|| ≤ ατ(2σ+βρ). This grows linearly in τ and is loose. It is stated for an unspecified "carefully chosen learning rate", and no numerical check is given that the bound is small for the τ used.
   - The assumptions "σ-smooth" and "β-continuous" second derivatives are imprecise.
   - "Rigorous theoretical support" and "mathematically well-supported" in the abstract are overstated.
   - The learning-rate update (Eq. 10) is only described qualitatively in the main text, and the comparison with the second-order version is deferred to the appendix.

5. **Table 8 reveals fragility and is inconsistent with the narrative.**
   - For CIFAR-100 IPC 50, accuracy swings from 23.4 (1/6 of the steps retained) to 50.9 (1/3). That is a 27-point change across a knob the paper presents as an efficiency setting.
   - The text says "performance improves as the number of truncated iterations decreases", which is confusing. The table's columns are the retained fraction, and accuracy rises as more steps are retained.
   - Table 2 CIFAR-100 IPC 50 reports 50.9, which matches the best setting. This suggests per-dataset tuning of this knob, and it is unclear whether baselines received comparable tuning.

6. **The efficiency claims are somewhat overstated.**
   - Table 6 shows SATM using 5.7 GB versus TESLA's 3.6 GB on CIFAR-100. This is not "constant memory" and is worse than TESLA's.
   - CIFAR-100 runtime is 12.0 s versus MTT's 12.1 s and TESLA's 15.3 s, a negligible difference from MTT.
   - ImageNet-1K memory is identical (26.6 GB) for all three methods, which is suspicious or uninformative. The text also says MTT needed two GPUs on ImageNet-1K, which does not match the table.
   - Table 1 gives SATM a cost of O(cN+cτ) versus O(cN) for MTT, yet the text claims SATM is faster than MTT. This should be explained.
   - ImageNet-1K runtimes (45.4 vs 46.8 vs 47.4 in Table 6, 44.7 vs 46.8 in Table 4) differ by about 4%, which is not a meaningful advantage.

7. **The ImageNet-1K and large-scale claims are thin.**
   - The paper claims "noticeable improvement margins on ImageNet-1K where most existing methods fail to condense", but the only comparison is to TESLA at IPC 1/10/50 (+1.2–1.4 pts, with ±1 std).
   - There is no comparison with modern ImageNet-scale methods (SRe²L, RDED, etc.). RDED is mentioned only in passing.
   - The text says SATM beats TESLA "even without relying on soft-label fitting tricks". It is not stated whether the TESLA numbers use soft labels, which would make the comparison unequal.
   - ImageNet subsets (Table 3) compare only to MTT and FTD, not TESLA or DATM.

8. **Baseline coverage and reporting issues.**
   - Recent trajectory-matching methods are absent from the main tables. DATM appears only in the add-on experiment.
   - The SATM-DA experiment (Table 7) shows mixed results: lower at Tiny-ImageNet IPC 1 (16.4 vs 17.1), and ≤1.1 pts elsewhere with overlapping standard deviations.
   - MTT is reported as 65.4 on CIFAR-10 IPC 10 in Table 2 but 64.3 in Table 5. The settings are not reconciled.
   - Continual learning (Fig. 1) compares only DM, MTT and FTD. Only curves are shown, with no numbers or variance, so "consistently outperforms" cannot be checked from the text.
   - There are several typos ("syntactic dataset", "ImageWoor", "ImageNeow", "MMT", "THU" vs "TUH", "Vasson").

9. **Novelty and the soundness of the perturbation design.**
   - Applying SAM-style perturbation to the data variable is a fairly direct transplant. The engineering contributions (truncated backprop, reuse of the first unroll) are incremental. Similar ideas exist in Sharp-MAML (cited) and in truncated backpropagation used elsewhere.
   - The noise γ proportional to ||φ_j||₂ is motivated by citations to randomised smoothing without analysis.
   - Trajectory reusing starts the perturbed run from θ_τ(φ) rather than from a trajectory trained on φ+ε. The second hypergradient therefore does not correspond to the gradient at φ+ε, and the optimised objective is not exactly Eq. 5. The "sharpness-aware" label is questionable, and the effect may be closer to a perturbed late-stage hypergradient.

## Questions
1. Can you provide a full ablation (MTT; +TUH; +noise; +SAM perturbation without TR; full SATM) on CIFAR-10/100 and cross-architecture, with ≥5 seeds, to show the sharpness term contributes?
2. How were ρ, γ, τ=ι and the learning rates chosen, per dataset or globally? Did MTT, FTD and TESLA get a similar tuning budget?
3. Can you measure final sharpness (e.g., top Hessian eigenvalue of the outer loss, or loss increase under random and adversarial perturbations) for MTT, FTD and SATM at convergence, and in weight space for models trained on the condensed data?
4. Given the Table 8 sensitivity, how robust is the method to the truncation fraction on other datasets and IPCs? Why does CIFAR-100 drop to 23.4 at 1/6?
5. Do the assumptions of Prop. 4.1 hold in practice? Can you compare truncated and full hypergradients empirically (cosine similarity, norm ratio) and check Thm. 4.2 against measured ||θ_τ(φ+ε) − θ_τ(φ)||?
6. Why is ImageNet-1K memory identical across methods in Table 6? How does SATM's memory (5.7 GB) compare with TESLA's (3.6 GB), and does "constant memory" hold?
7. How does SATM compare with SRe²L / RDED on ImageNet-1K, and do the TESLA numbers use soft labels?
8. How many seeds were used for Tables 2–5, and can you report significance tests or paired comparisons?

## Ratings
- **Soundness:** 2/4. The theory does not match the practical regime. The approximation changes the objective, and the evidence that flatness is the cause is indirect.
- **Presentation:** 2/4. The notation in Sec. 4.2 is confusing, there are many typos, and key derivations are in the appendix.
- **Contribution:** 2/4. The idea is natural and potentially useful, but the improvements are modest and the novelty is mostly in combining existing components.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

The paper is a sensible, simple and reasonably evaluated idea. I would want ablations that isolate the sharpness term, direct evidence for the "flatness" explanation, and larger or more consistent gains before recommending acceptance.
