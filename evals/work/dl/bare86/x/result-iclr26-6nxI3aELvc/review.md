# Review: Mutual Information Preserving Neural Network Pruning (MIPP)

## Summary
The paper proposes MIPP, a structured pruning method that works backwards from the output layer. For each adjacent layer pair it applies the transfer-entropy redundancy criterion (TERC) with MI ordering. A node is pruned if removing it leaves the estimated MI between the layer and the next layer unchanged. MI is estimated with a Covert et al. (2020)-style loss-difference estimator: a small MLP reconstructs the downstream activations, and the loss is compared with and without each node. Each comparison is run five times, and a confidence level x% sets the sparsity. The authors claim three things:
- Perfect MI preservation is equivalent to the existence of a reconstruction function, and so implies re-trainability (Theorem 1).
- The method avoids layer collapse and yields per-layer pruning ratios automatically.
- It prunes trained and untrained networks competitively with GraSP, SynFlow, ThiNet and SOSP-H.

Experiments cover LeNet5/MNIST, VGG11/ResNet18/ResNet34 on CIFAR10, VGG19/ResNet50 on CIFAR100, and ResNet50 on ImageNet (ThiNet only as baseline).

Note: figures were not available, so I judged the plots from captions, axis text and the surrounding prose.

## Strengths
- The idea is clean. It uses an information-theoretic, adjacent-layer, dynamically updated criterion in place of static top-k ranking, which is a sensible attempt to address interaction effects and layer collapse.
- Per-layer pruning ratios emerge without a global ranking. Fig. 4 shows interpretable block-periodic structure for ResNets.
- The layer-collapse diagnostic (Fig. 3) is useful. So is the observation that pruning untrained networks becomes harder when the input carries task-irrelevant information (deformed MNIST).
- Many architectures are covered, and both trained and untrained settings are considered.

## Weaknesses
1. **The theory is weak and partly incorrect.**
   - Theorem 1 states "X_L = sup_g g(X'_{L-1}) iff I(X'_{L-1};X_L) = I(X_{L-1};X_L)". This is ill-formed: a supremum of functions is equated with a random variable, and the function class F is undefined.
   - The appendix proof is a sketch. It plugs g(X_{L-1}) = X_L into the Donsker–Varadhan bound and asserts that equality "only holds if f(X'_{L-1}) = X_L" with no argument. Nothing shows the function is learnable or "discoverable by gradient descent".
   - Existence of a reconstruction function does not imply that the pruned network can be re-trained to the original accuracy. The claim that MIPP "implies re-trainability" is untested: there is no re-training experiment.
   - Layers are deterministic functions of their inputs, so for continuous activations I(X_l;X_{l+1}) = H(X_{l+1}) is degenerate. The paper notes this itself in Sec. 4.4. The exact MI equality the method targets is therefore not well defined, and the finite estimates cannot test it.
2. **The MI estimator and pruning criterion are heuristic and noisy.**
   - MI is replaced by a difference in MLP losses (2×256 hidden units, 20 or 150 re-training iterations after masking each node). The estimator is exact only for discrete variables with cross-entropy. Here activations are continuous and the loss is MSE, so no guarantee follows.
   - Each decision depends on an under-trained MLP, with only 5 repeats used for "confidence intervals". The decision to keep a node is plausibly dominated by optimisation noise. The repeats are not independent samples of a well-defined estimand, so it is unclear what "x% sure" means statistically.
   - The test "loss drops back below the original" conflates the estimator's variance with the effect of the node.
3. **Computational cost is not reported, and is likely very high.**
   - MIPP trains an MLP and then re-trains it once per node, sequentially, for every layer. For ResNet50 or VGG this is thousands of sequential MLP fits.
   - The paper dismisses iterative-retraining methods as impractical, yet there is no wall-clock or FLOP comparison with any baseline.
   - The sparsity hyperparameter x% is swept over 20 values, so each plotted point needs a full pruning run.
4. **The baselines are unfair or incomplete.**
   - GraSP and SynFlow are unstructured methods. They are made structured by an ad hoc L1 aggregation of weight scores, which they were not designed for.
   - Modern structured-pruning baselines are missing: HRank, CHIP, FPGM, DepGraph, Group-Fisher, and the cited TPP and Liebenwein et al. Only ThiNet (2017) and SOSP-H are structured baselines, and ThiNet is the only baseline on ImageNet.
   - ThiNet is given a uniform pruning ratio, while MIPP gets learned layer-wise ratios. This conflates layer-wise allocation with the MI criterion. A baseline that uses MIPP's per-layer ratios with magnitude or ThiNet scoring is needed.
   - The ImageNet result reports only "average neuron reduction" (71.1%). FLOPs, parameter counts, and comparison to published ImageNet numbers are absent. Neuron reduction is not a proxy for compute savings, so the practical benefit cannot be judged.
5. **The experimental evidence is weak and the SOTA claims are overstated.**
   - Results are accuracy-vs-neuron-reduction plots with very different y-axis ranges per panel. There are no tables, no seeds, and no confidence intervals. The paper itself concedes "noisy results" on ResNet50/CIFAR100.
   - The text acknowledges MIPP being outperformed on untrained VGG11, on VGG19/CIFAR100 at high sparsity, and by SOSP-H on ResNet34 at 80–90%. This supports "competitive" rather than "outperforms state of the art".
   - Baseline pruning ratios are copied from MIPP's per-run average neuron reduction. Costs per neuron differ across layers, so methods are not matched in FLOPs or parameters.
   - The method is acknowledged to be "inapplicable" when inputs carry task-irrelevant information, and it already degrades on CIFAR100 untrained. This limits the "prune at initialization" claim.
6. **Layer-collapse claims are not well measured.**
   - Collapse is shown as a percentage of runs per 5% sparsity bin, with only ~20 sparsity levels per experiment, so each bin holds very few runs and the percentages are coarse.
   - How collapse is detected (a whole layer pruned, or chance-level accuracy) is not specified.
   - There is no guarantee against collapse. The argument that remaining nodes "become increasingly vital" is informal.
7. **Key design choices are not ablated, and CNN handling undermines the MI claim.**
   - The output-to-input order is argued with loose information-bottleneck reasoning and is not ablated against forward pruning. MI ordering is not ablated against random order.
   - Each conv filter is collapsed to a single scalar (L1 norm of the feature map). This discards spatial information, so "preserving MI" is essentially void for the CNNs that make up the whole experimental setting. Fig. 10 compares collapse functions only through accuracy and layer-collapse, not MI.
   - Skip connections stay unpruned and batch-norm handling is ad hoc, so residual-stream channels in ResNets are not pruned.
8. **Presentation and novelty.**
   - The method largely combines TERC (from an RL state-variable selection paper) with the Covert et al. estimator. The new methodology is thin.
   - There are notation slips (e.g. "gradient ascent" in one place and "descent" in another, a stray "textupfL−1"), and the references contain errors ("CCVPR").
   - Several explanatory claims are asserted without evidence (e.g. "CNNs generalize better when remaining nodes are concentrated in the early layers").
   - The feature-selection experiment (App. E.1) is described by the authors as non-intuitive and has no feature-selection baselines.
   - Code is not available.

## Questions
1. What is the wall-clock cost of MIPP compared with ThiNet, SOSP and GraSP on ResNet50/ImageNet, and how many MLP fits are needed in total?
2. Can you provide a re-trainability experiment, such as loss curves after pruning for MIPP versus magnitude pruning at equal per-layer ratios?
3. Please give a precise statement of Theorem 1 (function class, almost-sure sense, deterministic layers where MI is infinite) with a complete proof. How does it apply to your estimator, which is not the MI?
4. What are the FLOPs and parameter counts at each reported sparsity? What is ImageNet top-1 at matched FLOPs against published results (e.g. TPP, CHIP, DepGraph, HRank)?
5. How much of the gain over ThiNet comes from layer-wise allocation alone? Please run ThiNet and magnitude pruning with MIPP's per-layer ratios.
6. How stable are the masks across seeds, MLP sizes and iteration counts?
7. How exactly is layer collapse operationalised?
8. How are ResNet skip-connection channels treated?

## Scores
- Soundness: 2
- Presentation: 2
- Contribution: 2
- **Rating: 4** (marginally below the acceptance threshold)
- **Confidence: 4**

The idea of dynamic, adjacent-layer, information-based node selection is reasonable and the emergent layer-wise allocation is interesting. However, the theory is underspecified, the estimator is a noisy proxy, and the cost is unreported. The baselines are dated or unfairly adapted, and the evidence for superiority over the state of the art, especially on ImageNet, is thin. The ablations needed to attribute gains to the MI criterion are missing.
