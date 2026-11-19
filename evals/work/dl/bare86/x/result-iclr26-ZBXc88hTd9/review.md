# Review: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation (CSFNet)

Note: figures were not available. Figs 4–5 are judged from captions and text only. The appendices (A–F) are not in the extracted text, so I could not check them.

## Summary
The paper proposes CSFNet, a two-stage audio-visual speech separation (AVSS) system.
- **Stage 1:** a TF-GridNet-style separator takes the mixture and lip features from a pretrained Auto-AVSR video encoder. It produces coarse waveforms.
- **Stage 2:** the coarse waveforms and the lip video go back into the Auto-AVSR (its ASR branch plus an MLP) to get audio-visual "enhanced semantics". The same separator is fine-tuned with these features to give the refined output.

Two further components are added:
- A "speaker-wise perceptual" (SP) fusion block: an MLP and conv fusion of the mixture feature with each speaker's upsampled lip feature.
- A "multi-range spectro-temporal" (MST) backbone: TF-GridNet with parallel unfold ranges and a smaller BLSTM.

The paper reports SOTA SI-SDRi on LRS2, LRS3 and VoxCeleb2 (16.8 / 19.4 / 14.8 dB; 17.5 / 20.1 / 15.4 dB with dynamic mixing). It also reports large gains over the first stage on 3- and 4-speaker mixtures, lower WER, and strong results on NTCD-TIMIT and LRS3+WHAM!.

## Strengths
- The idea is simple and practical. Visual-only semantic features are ambiguous, and re-encoding a first-pass estimate with an AVSR model that also sees audio is intuitive. It is a form of iterative refinement that fits the AVSS setting.
- Results are strong on standard benchmarks. The gain from stage 1 to stage 2 is consistent across datasets, and Table 4 shows a large gain at 4 speakers (10.5 to 14.3 dB).
- The evaluation is broader than usual. It covers 2–4 (and 5) speakers, noisy data, WER, a visual-occlusion study, and a computational cost table.
- Table 5 tests several AVSR front-ends and shows the refinement helps with each, which suggests the idea is not tied to one model.
- The compute is reported openly. MACs are about 3.5x IIANet's, and the paper does not claim to be efficient in absolute terms.

## Weaknesses
1. **The central claim is not isolated from confounds.** The stage-2 gain is attributed to "recursive semantic enhancement", but other explanations are not ruled out.
   - Stage 2 is a second model pass with extra training: it fine-tunes from stage 1 at a different learning rate and batch size, for up to 200 more epochs. The full model therefore gets roughly twice the training and twice the inference of single-pass baselines.
   - The needed controls are missing:
     - (a) Fine-tune stage 1 for the same extra epochs with the original visual features.
     - (b) Feed the coarse audio to a second cascaded separator or refinement network with no AVSR semantics. This would show whether the gain comes from the AVSR features or from iterative refinement/cascading, which is well established in speech enhancement and separation.
     - (c) Use a parameter-matched deeper single-stage model.
   - Without these, the claim that the fine stage "enhances semantic information" is not supported. Table 5's WER evidence is indirect, because lower WER of the output audio is expected from any better separation.
2. **Second-stage training and supervision details are not discussed.** Stage 2 is trained on stage-1 outputs, but the paper does not say whether these come from training data the stage-1 model has already fit. Stage-1 outputs on training data are better than on test data, which creates an exposure-bias mismatch. It also does not state whether the AVSR is frozen, whether gradients flow back to stage 1, or how coarse outputs are matched to lip streams in 3–4 speaker mixtures. These details matter for reproducibility.
3. **Comparisons with prior work are not fully like-for-like.**
   - The TF-GridNet and Crossnet audio-only baselines are "reproduced by our implementation", while the AV-CrossNet row is taken from its paper. CSFNet also uses a much heavier pipeline: Auto-AVSR with an ASR branch, trained on large external audio-visual data.
   - There is a possible leakage question. Auto-AVSR is pretrained on LRS2/LRS3, and in stage 2 its audio branch sees near-clean speech of test-set speakers. The paper does not discuss overlap between Auto-AVSR's training data and the test sets.
   - The "Pretrain Model: Yes/No" column in Table 2 mixes pretrained models of very different sizes, and the GPU time and memory numbers are not clearly comparable. It is unclear whether CSFNet's 42.5 MB memory and 117 ms include the AVSR model and both passes. 117 ms looks low for two full passes plus Auto-AVSR (VSR and ASR). The accounting needs clarification.
   - Sec. 4.4.1 says "MAVINet still delivers gains", a stray name, which suggests text was carried over from another paper and lowers confidence in the writing.
4. **Gains on noisy datasets look implausibly large.** Table 3 shows CSFNet at PESQ 2.72 and eSTOI 0.91 on LRS3+WHAM!, against 1.52 and 0.68 for the best baseline. SI-SDRi on NTCD-TIMIT rises from 11.0 to 15.67 dB. Baseline numbers are copied from another paper (AVLiT), with possibly different mixture protocols, training sets and test conditions. The dataset construction is only in an appendix. The audio-only CSFNet already shows a big PESQ jump on NTCD-TIMIT (1.78 vs 1.35), which hints at a protocol or capacity difference rather than a method effect. Table 3 also does not show the coarse vs fine split, so the noisy-condition story cannot be tied to the stage-2 mechanism.
5. **The architectural contributions (SP fusion, MST) are incremental and lightly evaluated.**
   - MST is TF-GridNet with a few extra unfolded branches. SP fusion is an MLP/concat on interpolated lip features.
   - The only SP ablation (Fig. 5, SP vs concatenation) uses a different setup from the main tables and is available only as a figure. There is no MST vs vanilla TF-GridNet ablation in the main text, so the claims of better multi-scale modelling and efficiency are unverified. The paper's own audio-only variant (10.7M parameters) beats TF-GridNet by only 0.4 dB on LRS2.
   - The claims of "speaker-aware" fusion and "encoding identity" have no analysis showing that identity is encoded.
6. **The robustness claim for missing visual input is partly contradicted by the paper's own caption.** Fig. 5's caption says that when a larger portion of visual input is absent, "the advantage of any fusion strategy diminishes, rendering them less meaningful". That undermines the "most graceful decline" claim. The occlusion experiment (Fig. 4) also does not say whether models were trained with visual dropout, or whether baselines such as IIANet were evaluated under the same occlusion.
7. **Statistical rigor is absent.** There are no seeds, no variance and no confidence intervals. The coarse-stage margin over the best baseline is about 0.2 dB, which the paper itself calls marginal. Table 5 evaluates 2 s segments, which differs from the usual full-utterance protocol.
8. **Novelty and fit to ICLR.** Feeding a first-pass estimate back for refinement is an application of a known cascade/iterative pattern. Representation-learning insight is limited: there is no analysis of what changes in the semantic features (e.g. phoneme discriminability, speaker-confusion rates), no failure analysis and no listening test. The framing "recursive" is also misleading: it is exactly two passes, with no experiments on whether a third pass helps.
9. **Presentation.** Terminology is inconsistent: "Speaker-aware perceptual fusion" vs "Speaker-wise perceptual"; SI-SNRi vs SI-SDRi. The Fig. 5 axis says "Mixture number 2–5" while the text describes 2–4 mixtures elsewhere. Several key details (data generation, losses, architectural ablations) are relegated to the appendix.

## Questions
1. How does the coarse-stage model, fine-tuned for the same extra budget without the AVSR feedback, compare with the fine stage? How does a second cascaded separator without AVSR compare?
2. Are stage-2 training inputs the stage-1 outputs on training data? How do you handle the train/test mismatch? Is Auto-AVSR frozen, and is any gradient passed back to stage 1?
3. How are coarse outputs matched to lip streams in the fine stage with 3–4 speakers? Does the large gain at 4 speakers come from better speaker-lip association?
4. Does Auto-AVSR's pretraining data overlap with the test speakers or videos (LRS2/LRS3 test)? Could this partly explain the WER decline?
5. What exactly is measured in Table 2 (one or two passes; with or without Auto-AVSR)? How can a two-pass system with Auto-AVSR run in 117 ms?
6. For Table 3, did you retrain the baselines on the same mixtures, or copy numbers? What are the coarse and fine numbers? Why is the PESQ/eSTOI gain so large?
7. Do more than two iterations help? Is there a saturation point?
8. Please provide MST vs TF-GridNet ablations and report variance across seeds.

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- Rating: 4 (marginally below the acceptance threshold)
- Confidence: 4

The idea is reasonable and the benchmark numbers are strong. However, the missing controls for the main claim, the unexplained protocol and compute accounting, the unverifiable large noisy-condition gains, and the incremental architecture and limited representation-learning insight keep this below the bar for ICLR in its present form.
