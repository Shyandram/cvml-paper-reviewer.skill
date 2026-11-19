# Review: "Dataset Distillers Are Good Label Denoisers In the Wild"

## Summary

The paper asks whether dataset distillation can serve as a label-noise remedy: distill a small synthetic set from a noisy-labeled training set, then train on that set. The authors argue this avoids the "vicious cycle" of estimate-noise-then-filter/reweight/relabel methods, and they also claim gains in efficiency and privacy. Three off-the-shelf distillers are benchmarked: DATM (trajectory matching, in its memory-efficient variant), DANCE (distribution matching) and RCIG (meta-learning). The settings are CIFAR-10/100 and Tiny-ImageNet with symmetric noise (τ = 0.2 to 0.8), CIFAR-10/100 with asymmetric (class-pair flip) noise, and CIFAR-10N/100N. Small ConvNets are used throughout, and accuracy is plotted against images per class (IPC). The only reference is cross-entropy training on the full noisy set. The paper reports three findings:
- (I) under symmetric noise, distilled sets beat the full-noisy-data baseline once noise is high enough;
- (II) under asymmetric noise, distillation absorbs the structured flips and generally does worse than the baseline;
- (III) on CIFAR-N, distillation helps mainly in the high-noise "Worst" and CIFAR-100N settings, and struggles in low-noise ones such as "Aggre".

Two "corollaries" give an IPC upper bound (Eq. 10) and a probabilistic noise-rate bound (Eq. 11). Neither comes with a proof. No new method is proposed.

All quantitative results are in Figures 2, 4 and 5, which I could not see. My assessment of the results relies on the captions and the text's description of them.

## Strengths

1. The question is reasonable and somewhat interesting. Distillation methods match aggregate statistics (gradients, trajectories, feature means), and these could plausibly average out symmetric label noise. Running three families of distillers under several noise types is a sensible first probe.
2. The negative finding on asymmetric noise (II) is honest and useful. Structured label flips are "common patterns" too, so they get distilled. This caveat matters to anyone who would use the idea in practice.
3. The paper is easy to follow, and the experimental setup follows the standard noisy-label benchmarks (CIFAR-N, standard asymmetric flip maps).

## Weaknesses

1. **No noisy-label baselines.** The paper is pitched as a new approach to learning with noisy labels, yet the only comparison is plain CE on the full noisy set. That is the weakest possible reference: at τ = 0.6 or 0.8 symmetric noise, almost any procedure that reduces the effective noise or regularizes heavily beats it. Several standard comparators are missing:
   - established noisy-label methods that the paper itself cites (Co-teaching, DivideMix, GCE, DISC, ELR);
   - a random clean-ish coreset of the same IPC;
   - early-stopped CE;
   - a small-loss selected subset of the same size.

   Without them, "distillers are good label denoisers" cannot be judged against the state of the art it claims to replace. From the text, the distilled sets do worse than full-data CE in low-noise regimes (e.g., CIFAR-N Aggre). Even an untuned modern noisy-label method would beat full-data CE by a large margin there.
2. **The mechanism is assumed, not measured.** The central claim is that distillation "captures common patterns while ignoring outliers such as noise." The paper never tests this directly. It does not measure how much the noisy samples influence the synthetic set, for example through gradient or trajectory contributions, or by distilling from the clean subset versus the noisy subset. The only support is downstream accuracy and a qualitative image grid (Fig. 3). The expert trajectories (DATM), the trained encoder (DANCE) and the kernel targets (RCIG) are all fit to the noisy labels, so the reason denoising should happen is not obvious. The paper never discusses this.
3. **The "corollaries" are not results.** Eq. 10 says the IPC needed to "perfectly preserve" information is at most the number of clean samples per class. This is close to a tautology, and it is stated without a definition of "perfectly preserve" or a proof. Eq. 11 states a high-probability noise-rate bound from "validation accuracy matches the original dataset," with no derivation, no assumptions, no definition of δ, and no empirical check. Calling these corollaries overstates them.
4. **Possible test-set selection.** The protocol says "final test accuracies are reported throughout the distillation process." If the reported number is the best test accuracy over distillation iterations or hyperparameters, that is selection on the test set. This matters especially when comparing against a single CE baseline. Nothing in the text mentions a validation split, seeds, variance, or error bars.
5. **Claims beyond the evidence.**
   - *Privacy.* "Strong privacy protection" is asserted but never evaluated, with no membership-inference test and no DP analysis. Distilled images are known to leak training data.
   - *Efficiency.* No compute numbers are given, and distillation itself (especially trajectory matching with expert training) is expensive.
   - *Tail classes.* The claim that tail classes are "lossy compressed" in imbalanced data is only a hypothesis; no imbalanced experiment is run.
   - *"In the wild."* Clothing1M and WebVision are introduced but never used, so the real-world evidence is CIFAR-N with 3–4-layer ConvNets at 32×32 resolution.
6. **Thin novelty and analysis depth.** Applying existing distillers to noisy data, with no modification, is a benchmark observation. The findings ("helps for symmetric noise at high rates, hurts for structured noise, hurts at low noise") are largely what one would predict from the averaging intuition. The open questions the paper itself raises are left open: how to choose IPC given the noise rate, and how to handle structured noise. The paper also does not engage with prior work on dataset distillation and coreset selection under label noise.
7. **Presentation.** All results are in plots with no tables of numbers. There are typos ("Realted Works", "bellow", "Both of which" for three types), and Section 3.2 spends more space restating the three distillers' objectives than analysing them. The formatting appears to come from a different venue template, and there is no appendix with hyperparameters.

## Questions

1. How do the distilled sets compare at matched compute with DivideMix, Co-teaching, ELR/GCE, early-stopped CE, and a random or small-loss-selected subset of the same IPC?
2. How is the reported accuracy selected? Is it the last iterate, or the best over distillation iterations? Is the selection done on test data or on a held-out validation set? How many seeds were run?
3. Can you test the mechanism directly? For example, distil from the clean-only subset and from the noisy-only subset and compare, or measure what fraction of the distillation signal comes from mislabeled samples.
4. Please give proofs and precise assumptions for Eqs. 10 and 11, and an empirical check that Eq. 11 actually estimates τ on CIFAR-N.
5. What evidence supports the privacy and efficiency claims?
6. Do the conclusions hold for ResNet-scale models, higher resolution, or Clothing1M/WebVision?

## Bracket against calibration anchors

- **Anchor just below: none clearly; the paper sits at about the level of A.** Like A, the contribution is an observation about existing tools that the field largely expects: averaging-style distillation suppresses random noise and absorbs structured noise. There is no method and no principled explanation (W2, W6). The input variables are also poorly controlled. There are no proper baselines (W1), selection on the test set is possible (W4), and there is no variance. This is the same failure as A's poorly controlled inputs and shallow analysis. It is not better than A in scope either: A had four benchmarks and four models, while this paper has small ConvNets on CIFAR/Tiny-ImageNet only.
- **Anchor just above: B.** B had a clean formalism whose link to its phenomenon was loose. Here the formal content (the two corollaries) is unproven and close to tautological (W3), and several headline claims are not tested at all: privacy, efficiency, tail classes, "in the wild" (W5). So the paper falls short of B's level of soundness.
- **Placement:** pool position about 10–15, near A. Rating 2.

## Scores

- **Soundness:** 1. There are no meaningful baselines, the selection protocol is unclear, the corollaries are unproven, and the central claims are untested.
- **Presentation:** 2
- **Contribution:** 1

## Rating

**2 (reject)**

## Confidence

4. I know the noisy-label and dataset-distillation literature well. My confidence is reduced slightly because the result figures were not available to me.
