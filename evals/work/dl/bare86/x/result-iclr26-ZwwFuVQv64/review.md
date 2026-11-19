# Review: Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus

## Summary
The paper studies quantum federated learning (QFL) where clients can run parametrized quantum circuits (PQCs) of different depths because their hardware noise differs. It ports DepthFL to this setting. Each client trains a depth-d_k PQC with a layerwise loss. The loss is the sum of per-layer BCE terms plus pairwise KL "mutual distillation" between per-layer classifiers. The server aggregates each parameter over the clients that hold it, using circular (atan2) averaging of rotation angles.

The main technical issue is that measuring a qubit after each layer to read a per-layer classifier collapses the state. The paper offers four circuit designs:
- **Layerwise:** re-run the circuit once per depth, so the shot cost is linear in depth.
- **Ancilla:** entangle the first qubit with a fresh ancilla after each layer, then measure the ancillas at the end.
- **Blocking:** a mid-circuit measurement, claimed to be logically equivalent to Ancilla.
- **Funnel:** drop one qubit after each layer so all measurements can be made at the end.

Evaluation is in noiseless simulation on six binary MNIST and Fashion-MNIST tasks, using PCA to 10 features and angle encoding. There are 5 clients with depths 2–6, 128 samples per client, and five data splits. The baselines are Q-HeteroFL (the authors' own adaptation), Vanilla QFL at the shallowest depth, and Standalone training. The paper reports up to 12.4% average gain over Q-HeteroFL and larger gradient norms for early layers. Trained Funnel models are then evaluated on six IBM QPUs on 100 test points of one task (Pullover/Coat).

## Strengths
- The problem is well motivated: depth heterogeneity across NISQ devices is realistic, and the FL-style parameter-sharing view of it is sensible.
- The measurement-collapse obstacle to per-layer classifiers is real and is identified clearly. The four designs map to distinct resource trade-offs (shots, qubits, mid-circuit measurement, Hilbert-space size), and Table 1 makes the trade-offs explicit.
- The Funnel design, which yields several classifiers from a single circuit execution with only terminal measurements, is an interesting and practical idea.
- Some real-hardware evaluation is included on six IBM devices, which is uncommon in QFL papers. Code is promised.
- The experiments report variance over five splits. The appendix includes ablations on ansatz and layer count.

## Weaknesses
1. **Limited novelty at the method level.** The loss, aggregation scheme and reverse-distillation idea come from DepthFL, and the paper states that it does not re-justify them for the quantum case. Angle averaging is a small adaptation. The contribution is therefore the circuit designs for extracting intermediate outputs. Those are reasonable but modest, and they are motivated by hardware arguments rather than learning-theoretic ones. The "first QFL framework with layerwise losses" claim is not accompanied by an experimental comparison to eSQFL (Yun et al.).

2. **Weak and possibly unfair baselines.**
   - Q-HeteroFL is constructed by the authors. Its loss sits only on the deepest classifier, and it shows very large variance and surprising collapse (for example 58.8% on MNIST 3/4 at 2L and 62.4 ± 33.5 on Trouser/Boot). That suggests the baseline is under-tuned or ill-conditioned, for example from averaging parameters trained against different objectives, rather than a strong state of the art.
   - The headline "12.4% over the state-of-the-art" is relative to this self-built baseline only.
   - No stronger or more natural baselines are used: FedAvg on the shallowest shared sub-circuit with local fine-tuning of the deeper layers, per-depth FL groups, layerwise loss without KD, or a HeteroFL variant with auxiliary heads.
   - The comparison is also not apples-to-apples. Quorus-Layerwise is evaluated as an *ensemble* of L−1 per-layer classifiers (Appendix D.1). The baselines use a single output. Part of the gain may come from ensembling rather than from the federated or layerwise-loss mechanism. Baselines with equivalent ensembling (or a Quorus variant using only the final classifier) are missing.

3. **The gain over simple baselines is small and often not significant.** Against Standalone and Vanilla QFL (2L), Quorus-Layerwise's mean improvement is typically 0–2 points. This is within one standard deviation on most tasks (for example 98.5 ± 0.8 vs 98.3 ± 1.0 on MNIST 0/1, depth 5 vs 4L Standalone; 78.7 ± 1.0 vs 77.1 ± 1.0 on Pullover/Coat). On Bag/Sandal, Quorus is *worse* than Standalone at every depth ≥ 4. At the smallest capacity, Quorus loses to Standalone and Vanilla QFL on several tasks. With five splits, the bold "best" markings are not backed by any statistical testing. The data are also very small (128 samples per client, 5 clients), which makes federation benefits hard to measure.

4. **The scope of the evaluation is narrow.**
   - Only binary tasks, with PCA to 10 features and angle encoding, are used. This is far from settings where depth heterogeneity and barren plateaus matter, and where federation would add something beyond a small centralized model.
   - Accuracy is already ~98% on several tasks regardless of method. Clients appear to be random IID samples. Non-IID data, the core difficulty in FL, is not studied, and neither are client drop-out or the number of clients.
   - Federated PCA is emulated centrally. Privacy, the stated motivation for FL, is not examined.
   - Depth saturation (Table 7) shows only marginal gains beyond 5–6 layers, which undercuts the premise that enabling deeper circuits is valuable here.

5. **Noise-awareness is not evaluated in training.** The abstract and intro frame Quorus as "error-aware". All training is in noiseless simulation, and hardware is used only for *inference* of Funnel models on a single task with 100 test points. With n = 100, the standard error is about ±4–5 points, so the 3% gap to ideal simulation and the differences between devices are weakly supported. There are no repeated runs or confidence intervals. The setup also never tests the central claim that clients with noisy devices train a *shallower* model and still contribute usefully to FL. The hardware results in fact show accuracy dropping from ~76% to ~58% as depth goes 2→5 on Kingston (Fig. 8b, judged from the caption and text). Deeper clients are therefore the *harmful* ones on noisy devices, which is in tension with the premise that Quorus lets clients exploit more layers. No noisy-simulation or noise-in-the-loop federated training is performed. Hardware numbers are for Funnel only, while the main results table uses Layerwise; Ancilla/Blocking is never run on hardware.

6. **The barren-plateau / gradient-norm claim is weakly supported.** Per-layer losses defined directly after early layers trivially give early parameters larger gradients, since they are closer to the measurement. This is a property of cost-function locality (Cerezo et al.), not evidence that deep circuits become trainable. The paper itself admits later-layer gradients stay small. Fig. 7 compares only to Q-HeteroFL, with one task and depth, smoothed curves, and no variance across seeds. Higher gradient norm is also not shown to relate to better optima. Statements such as "reducing barren plateau effect" and "scalable trainability for deep quantum circuits" are overclaims, particularly at depths ≤ 6 on 5–10 qubits, where barren plateaus are not an issue.

7. **The Ancilla/Blocking design is not equivalent to Layerwise, and shot efficiency is untested.** The text acknowledges that for layers ≥ 2 the statistics differ because the first qubit is dephased. The "hypothesis" that training still works rests only on the simulated accuracies in Table 3, which are all very close to each other. The shot-efficiency claims are never quantified: the paper reports no shot counts and no shots-versus-accuracy curves. Training appears to use exact simulation, so finite-shot gradient estimation is not tested. The Blocking design is discussed only in theory, and the Funnel design restricts the Hilbert space without that cost being measured against the shot savings.

8. **Presentation and consistency issues.**
   - The "Capacity" framing is confusing. Table 2 reports, for each capacity, what the client attains, but the Quorus numbers for different capacities appear to be sub-ensembles of one model.
   - Table 7's capacity column and layer counts are hard to follow; the capacity-1 rows include a "2L" entry.
   - The count of classifiers (L−1 for L layers) is inconsistent with the "layer count" used elsewhere.
   - The 12.4% average is not reproducible from the tables (the averaging rule is not given), and "up to 12.4%" versus "on average 12.4%" is used interchangeably between abstract and contributions.
   - There is no theoretical analysis of convergence or aggregation. Circular averaging of angles is not justified (for example wrap-around bias, or a near-zero resultant).
   - Related work says classical model-heterogeneous FL methods "cannot be directly applied" without trying adapted versions. ReeFL/ScaleFL-style early exits are dismissed rather than evaluated.
   - Figures are not available in the text extraction, so I judged Figs. 7–8 from captions and text only.

## Questions
1. How is the "12.4%" computed (over which tasks, depths, and clients)? How does Quorus compare to a tuned Q-HeteroFL (learning rate, initialization, and so on), and why is the Q-HeteroFL variance so high?
2. Please add a baseline that ensembles per-layer classifiers without the layerwise/KD loss, and an ablation of the KL term versus BCE-only per-layer losses, to isolate the contribution of the federated layerwise loss.
3. Can you report results under non-IID client splits, more clients, and larger feature dimension or multiclass tasks?
4. Can you train with a noise model (or on hardware) at client-specific noise levels and show that low-fidelity clients help the global model? Currently no experiment has noisy clients participating in training.
5. Can you provide significance tests, and hardware results with larger test sets and repeated runs? Can Layerwise or Ancilla be run on hardware on at least a couple of devices?
6. What are the actual shot counts per training step for each design, and does accuracy hold under finite-shot gradient estimates?
7. Does the gradient-norm advantage persist across seeds, tasks, and larger qubit counts (where barren plateaus actually arise)? Is it correlated with accuracy?

## Ratings
- **Soundness:** 2 (fair). Reasonable construction, but baselines are self-built, noise-awareness is not tested in training, and the gradient and shot-efficiency claims are untested.
- **Presentation:** 3 (good). Readable and well organised, with some inconsistent labelling and overclaims.
- **Contribution:** 2 (fair). A sensible adaptation of DepthFL with practical circuit designs, but small-scale, with modest gains over simple baselines.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 3**
