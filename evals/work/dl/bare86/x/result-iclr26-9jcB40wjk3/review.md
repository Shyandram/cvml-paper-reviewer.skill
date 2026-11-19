# Review: SAFA-SNN — Sparsity-Aware On-Device FSCIL with Fast-Adaptive SNN

Note: this review is based on text extracted from the PDF. Figures are not available, so I judged them from captions and text. The appendix is not in the extracted text and I did not read it.

## Summary
The paper proposes SAFA-SNN for few-shot class-incremental learning (FSCIL) with spiking neural networks. It has three parts:
1. **Sparsity-aware dynamic thresholds.** A channel-wise mask splits neurons into "stable" and "active" groups. The threshold update (Eq. 6–7) pushes firing rates in incremental sessions toward base-session firing rates.
2. **Zeroth-order gradient estimation.** A multi-sample finite-difference estimate replaces the surrogate gradient for the spike function. It is used only in base-session training.
3. **Prototype subspace projection.** Novel-class prototypes are mixed with their projection onto the span of the base-class prototypes (Eq. 14–15).

The paper evaluates on CIFAR100, MiniImageNet, CIFAR-10-DVS, DVS128-Gesture and N-Caltech101. Baselines are SNN versions of existing FSCIL methods. It also reports energy and training time measured on a Jetson Orin AGX. It claims +4.01% last-session accuracy over the best baseline (CLOSER) on MiniImageNet and "20% lower energy".

## Strengths
- The topic is relevant. SNN-based FSCIL is under-explored, and the paper covers both static and event-based datasets.
- The components are simple and cheap. The incremental stage uses only prototype computation with a frozen backbone.
- The experiments are broad. They cover several backbones (Spiking VGG, ResNet, Spikingformer), three seeds with standard deviations, and an ablation.
- Training energy and runtime are measured on a real edge device, which is more concrete than theoretical SOP counts.
- The limitations section is honest about deep networks and fixed N-way K-shot sessions.

## Weaknesses
1. **The SNN-specific parts are not shown to matter for FSCIL, and the "on-device" claim is loosely supported.**
   - The backbone is frozen in incremental sessions. The only incremental-session operations are prototype averaging and projection, which are generic and could be applied to an ANN.
   - Zeroth-order optimization is used only in base training.
   - The paper never shows how the threshold update (Eq. 7) behaves, what it does to the features, or why it limits forgetting. The ablation cannot show this.
   - There is no ANN baseline with a matched backbone and budget (for example ResNet-18 or VGG with CEC, FACT or TEEN). So there is no evidence that the SNN gives an advantage in accuracy or energy for this problem. The only non-SNN baseline is ALADE, a class-incremental method and not an FSCIL method.
   - Only the base session is trained on-device, for 300 epochs. The paper does not say whether that cost counts as "on-device".
2. **The baseline comparison looks uneven and possibly unfair.**
   - In Table 1, SAFA-SNN's base-session accuracy is 74.66%, against 54–66% for the SNN baselines. Much of the last-session gain comes from the stronger base session. The drop over sessions is about 26 points for SAFA-SNN and about 21 for CLOSER. The paper does not say whether baselines use the same backbone, epochs, time steps and tuning.
   - Several baselines look implausibly weak. S3C oscillates between 15% and 31%, and WARP has standard deviations around ±4.
   - The "+4.01%" headline is a gain over a single baseline (CLOSER).
   - The ablation (Fig. 6) treats "SA only" as the baseline. There is no "plain SNN + prototypes" baseline, and no CLOSER-style training on the same backbone.
   - Table 2 compares only WARP and TEEN on the neuromorphic datasets.
   - Table 3 parameter sizes are inconsistent. Spiking VGG5 is 221M for Early Bird against 32.85M for SAFA-SNN with the same backbone. SAFA-SNN's VGG9 has 22.63M parameters on MiniImageNet and 262.6M on CIFAR-10-DVS, with no explanation.
3. **The energy claim is weakly supported.**
   - The abstract says "20% lower energy". Fig. 4, read from the extracted values, shows differences of roughly 10% (about 12.6k J against 13.9–15.8k J) between methods with different training protocols.
   - Energy is power × time on a GPU device, so it mostly reflects wall-clock time and not any event-driven benefit of spikes. The Jetson runs SNNs as dense tensors.
   - The paper does not say which baseline the 20% is measured against.
   - It attributes the speed-up to "not modifying synaptic weights", which suggests the savings come from the protocol and not from the model.
   - Inference energy is theoretical (appendix). There are no on-device memory or latency figures despite the memory-constrained motivation.
4. **Technical and mathematical issues.**
   - Eq. 14: B̃ ∈ R^{B×D}, so B̃ᵀB̃ is D×D with rank at most B. It is singular whenever B < D, which is the usual case. The dimensions of G and of P̃_proj = C̃G also do not work out consistently. The projector should use prototypes as columns and a pseudo-inverse.
   - The text calls G a "generalized inverse" and says it builds "|C_B| distinct orthogonal subspaces", but it is a single projector onto one subspace.
   - Eq. 11–12 are presented as a convergence result for a non-differentiable function with a δ-biased gradient estimate. The claim E[g(u_T) − g(u*)] ≤ O(1/√T) is a convex-style rate that does not follow from a non-convex stationarity result. The theory is inherited from prior zeroth-order SNN work (Mukhoty et al., 2023) and adds little here.
   - The estimator in Eq. 9–10 is itself a smoothed surrogate. The paper does not compare gradient quality, or accuracy, against standard surrogate-gradient training. The "ZOO" ablation does not isolate this.
   - Notation and algorithm are inconsistent. Algorithm 1 uses τ, Eq. 1 uses γ, and Eq. 6 reuses γ as a hyper-parameter. Algorithm 1 chooses the mask randomly, while Sec. 5.3 uses the first ⌊ηC⌋ channels. Eq. 13 mixes CE and MSE terms and describes λ as the weight of a "temporal prediction error term".
   - Eq. 7 needs the base-task firing rate r̄_b in incremental sessions. Base data is unavailable then, so it must be stored, and the overhead is not discussed. It is also unclear what data drives the threshold updates, and whether test data is used (which would be test-time adaptation).
5. **Evaluation protocol and reporting.**
   - CIFAR-10-DVS and DVS128-Gesture use "1-way 1-shot" sessions, with only four or five sessions and very few classes. This setting is very small.
   - Table 2 reports only Avg and Last, with no comparison to CLOSER or FACT.
   - Novel-class and harmonic accuracy are mostly absent from the main tables. Table 3 reports HAcc of about 25%, which suggests novel-class accuracy is poor. That is the quantity FSCIL should be judged on.
   - Some baseline standard deviations are very small (CLOSER ±0.09). This suggests the seeds may only change the session sampling and not the training.
   - Deep backbones such as Spiking ResNet-34 degrade, which limits scalability.
6. **Presentation.**
   - The text is repetitive and has grammar and word-choice problems. The motivation overstates some points (for example, "most existing neuromorphic systems are still trained offline", "PEFT … ineffective for on-device").
   - Figure 1 claims SNNs reduce on-device memory, but no memory is measured.
   - Several claims (80% sparsity, hyper-parameter and shot studies) are only in the appendix.

## Questions
1. Do all baselines use the same backbone, time steps, epochs and training tricks (TET loss, etc.)? Why is SAFA-SNN's base accuracy 10–20 points above the strongest baseline? What happens if CLOSER or TEEN is trained with your base recipe?
2. Can you add a matched-backbone ANN comparison (accuracy, memory, latency, energy)?
3. Please clarify Eq. 14–15: the dimensions of G, whether B̃ᵀB̃ is invertible, and whether a pseudo-inverse is used. Please give the effect of α and an ablation of SP alone against plain prototypes and against TEEN's or CLOSER's calibration.
4. How exactly are thresholds updated in incremental sessions, and with what data? Does this use test data? What is stored from the base session?
5. Please add a ZOO against surrogate-gradient ablation (accuracy, gradient error, time and memory).
6. Which baseline gives the "20% lower energy", and what are the exact numbers? What are the measured on-device memory and latency?
7. Why do the parameter counts in Table 3 differ so much between methods using the same backbone?
8. Can you report novel-class accuracy and harmonic accuracy in the main benchmark tables?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- **Rating: 4** (marginally below the acceptance threshold)
- **Confidence: 3**

SNN-based FSCIL is a reasonable idea and the headline results look strong. But the contributions combine existing pieces (zeroth-order SNN training, prototype calibration, dynamic thresholds). The comparison fairness, the missing ANN comparison, the weak energy evidence, and the errors in the method's equations leave the central claims insufficiently supported.
