# Review: "Dataset Distillers Are Good Label Denoisers In the Wild"

## Summary

The paper proposes using dataset distillation as a way to learn from noisily labelled data. The argument is that conventional noisy-label learning (NLL) methods first estimate the noise and then discard, re-weight or re-label samples, and that this can fall into a "vicious cycle" when the first estimate is wrong. Distillation, the authors argue, condenses common patterns and so could filter label noise without that feedback loop. They benchmark three off-the-shelf distillation methods: DATM (trajectory matching, in a memory-efficient variant), DANCE (distribution matching) and RCIG (meta-learning). The settings are:
- CIFAR-10/100 and Tiny-ImageNet with symmetric noise;
- CIFAR-10/100 with asymmetric noise;
- CIFAR-10N/100N with human-annotation noise.

Each distilled set is compared to a ConvNet trained with plain cross-entropy on the full noisy dataset. The reported findings are:
- (I) under symmetric noise, distilled sets beat the full-noisy-data CE baseline, especially at high noise rates;
- (II) asymmetric, structured noise is absorbed into the distilled data, and distillation then underperforms the baseline;
- (III) on CIFAR-N, distillation helps for high noise (Worst) but not for low noise (Aggre).

Two "corollaries" relate IPC to the noise rate: an IPC upper bound, and a probabilistic lower bound on τ. The paper also claims benefits for efficiency and privacy.

All quantitative results are in figures (Figs. 2, 4, 5). I only had the extracted text and captions, so my reading of the results relies on the authors' descriptions in the text.

## Strengths

1. The question of how dataset distillation behaves on noisy labels is reasonable and of some practical interest, because most distillation work assumes clean labels.
2. The study covers three methodologically distinct families (trajectory, distribution and meta-learning matching), several datasets, and three noise types, including real human noise (CIFAR-N).
3. The paper reports negative findings honestly. Structured asymmetric noise is carried into the synthetic data, and distillation hurts at low noise rates. This is a useful caution for anyone tempted to treat distillation as a universal denoiser.
4. The paper is easy to follow at a high level, and the qualitative visualisation (Fig. 3) gives intuition about what DATM keeps under increasing noise.

## Weaknesses

1. **The baseline is too weak, so the main claim is not supported.** The only comparison is standard cross-entropy training on the full noisy dataset. It is well known that CE without early stopping memorises noisy labels and collapses at 60–80% symmetric noise. Beating it with a handful of synthetic images is therefore expected and says little about "denoising". The paper reviews many NLL methods (Co-teaching, DivideMix, DISC, GCE, loss correction, etc.) but compares against none of them. Simple and strong baselines are also missing:
   - CE with early stopping;
   - GCE/SCE;
   - small-loss selection followed by training;
   - coreset or random subset selection at the same IPC from the noisy data.

   Without these, the paper cannot claim that distillation is a "good label denoiser", or that it improves on the "vicious-cycle" methods it criticises.
2. **No new method.** The contribution is an empirical benchmark of existing distillers with default settings. Nothing is proposed to address the failure modes the paper identifies: asymmetric noise, choosing the IPC, and tail classes. The abstract and conclusion describe "a novel approach", which overstates what is delivered.
3. **The "vicious cycle" argument is not tested and partly misplaced.** DATM's expert trajectories and DANCE's expert encoders are trained on the noisy data, so the noise also enters the distillation objective through those experts. The paper does not analyse this. It also gives no empirical evidence that the claimed vicious cycle actually limits existing NLL methods.
4. **The corollaries are unproven and appear ill-posed.**
   - Corollary I (IPC ≤ |S̃|(1−τ)/C) is just a count of the clean samples per class. It is not derived from any property of distillation, and "perfectly preserve the sample information" is never defined.
   - Corollary II claims a high-probability bound P(τ ≥ 1 − C·IPC/|S̃|) ≥ 1 − δ conditional on "validation accuracy matching the original dataset". But δ, the probability space and the assumptions are never specified, and no proof is given.

   These statements read as heuristics dressed as results, and they are not validated empirically. For example, the paper never checks whether the IPC at which accuracy matches the baseline actually predicts τ on CIFAR-N.
5. **Evaluation protocol concerns.** The text says "Final test accuracies are reported throughout the distillation process", and the baselines are "training on the full dataset at the current noise rate". It is unclear:
   - whether any checkpoint, IPC or hyperparameter selection used the clean test set;
   - whether the baseline uses the same ConvNet, augmentation (RCIG uses augmentation) and training budget;
   - how many seeds were run.

   No numbers, variances or tables are reported. The results exist only as curves, so they are hard to verify or compare.
6. **Claims beyond the evidence.**
   - Privacy: the paper asserts "strong privacy protection" without any privacy analysis, attack or formal guarantee. Distilled data is known to leak information about the training data.
   - Efficiency: no distillation cost is reported. Trajectory matching requires training many expert models on the full data, which likely costs more than a single robust training run.
   - "In the wild" and imbalance: Clothing1M and WebVision are mentioned but not evaluated, and the tail-class / imbalanced-data claim is only a hypothesis, with no experiment behind it.
7. **Limited scale and architectures.** Only small ConvNets are used, at low resolution. There are no larger backbones and no cross-architecture evaluation, even though cross-architecture evaluation is a standard check in distillation papers.
8. **Presentation.** There are many typos ("Realted Works", "bellow", "Both of which" for three noise types). The background section is long and simply restates the DATM, DANCE and RCIG objectives. Insights are phrased as "warrants deeper exploration" rather than being investigated. The submission appears to use a non-ICLR template.

## Questions

1. How does distillation compare with standard NLL methods at matched compute? Candidates are DivideMix, Co-teaching, GCE, and CE with early stopping on a clean validation split. How does it compare with selecting IPC real samples by small-loss or random selection?
2. Were the expert trajectories (DATM) and expert encoders (DANCE) trained on noisy labels? If so, how sensitive are the results to early-stopping the experts? Is part of the gain simply implicit early stopping?
3. How were the IPC, the distillation iteration and the reported checkpoint chosen? Was the test set used for any of these choices?
4. Can you provide a proof, or at least precise assumptions, for Corollary II, including what δ is? Can you test empirically whether it predicts τ on CIFAR-N?
5. What is the total wall-clock and GPU cost of distillation plus evaluation, compared with robust training on the full data?
6. What privacy guarantee, if any, do you claim? Have you evaluated membership inference on the distilled sets?
7. Can you include Clothing1M or WebVision, and an imbalanced noisy benchmark, to support the "in the wild" and tail-class claims?

## Ratings

- **Soundness:** 1
- **Presentation:** 2
- **Contribution:** 1
- **Rating:** 2 (reject)
- **Confidence:** 4
