# Review: Transformers self-organize like newborn visual systems when trained in prenatal worlds (ICLR 2026)

Figures were not available. Figure-based claims are judged from captions and text only.

## Summary
The paper trains small ViTs (4/5/6 layers and heads, 64×64 input, 8×8 patches) with a contrastive-learning-through-time objective (ViT-CoT). The training data is 160k frames from the Godfrey & Swindale retinal wave simulator (chick preset). The authors then probe three "signatures of newborn visual systems":
1. Edge sensitivity in early layers, measured as correlation between layer RDMs on rotated-bar stimuli and a hand-built orientation-tuned RDM.
2. Shape over colour grouping in later layers, measured by RDMs on 4 shapes × 4 colours.
3. Growing receptive-field size across layers, measured by the spatial variance of an input-gradient map.

Untrained models lack these properties and trained models show them. Models trained on temporally scrambled frames do not. The authors conclude that transformers "learn like brains", that the structure of newborn visual systems is explained by generic space-time fitting, and that "it is unnecessary to postulate a central role for genes".

## Strengths
- The question is interesting: what can generic learners extract from prenatal-like spontaneous activity? Using a biologically motivated simulator for training data is a sensible choice.
- The temporal-scrambling control is a useful ablation. It suggests the effect depends on temporal contiguity under this objective.
- Three architecture sizes, three seeds and a data-quantity sweep (10k–160k) are reported.
- The paper is short and clearly written.
- The authors argue that ViTs, unlike CNNs, do not hard-code locality, which makes them a more suitable testbed than prior retinal-wave CNN work.

## Weaknesses
1. **The central claims go far beyond the evidence.**
   - The conclusions are "transformers learn like brains" and "unnecessary to postulate a central role for genes". These are not supported by three coarse probes on a small model.
   - Matching a qualitative property (edge-like selectivity, larger RFs deeper in the network) does not show the same mechanism, or the same structure at the level of neural data.
   - No comparison is made to any newborn neural or behavioural data. "Newborn visual system" is operationalised by cartoon criteria.
   - Sufficiency in a model does not rule out a genetic contribution in animals. The inference is a logical overreach.
   - Almost any hierarchical learner given smooth, local input would likely show these properties, so the result does not discriminate among hypotheses.

2. **Missing baselines and controls.** There is no comparison to:
   - CNNs trained on the same data, or other architectures.
   - Other objectives (SimCLR-style augmentation, masked autoencoding, next-frame prediction), or other generic learners (ICA/sparse coding, which Albert et al. 2008 already showed gives oriented filters on retinal waves).
   - Training on natural videos, noise or static images. Without these, it is impossible to say what is specific to retinal waves versus any temporally smooth, spatially local input.
   - The paper itself concedes that the objective ablation is future work.
   - The scrambled control changes the temporal structure but also the contrastive positives and the batch statistics. It does not isolate "retinal waves" from "smooth motion".
   - A control with smooth non-wave motion, or with wave frames whose spatial structure is destroyed but whose temporal order is kept, is absent.

3. **The "untrained" baseline is weak and the metrics are partly circular.**
   - An untrained ViT is a poor reference for "no structure". The claim that untrained transformers lack these properties depends on the specific probe.
   - The edge metric correlates RDMs with a hand-chosen geometric RDM (decay 0.5). This is arbitrary, with no sensitivity analysis and no statistical test.
   - The edge stimuli are periodic random-binary bar gratings rotated 0–90° in 10° steps. A 0–90° range with no wraparound makes the RDM design ambiguous. Interpolation artefacts from rotating random bars can also drive similarity.
   - Orientation sensitivity at the representation level is not tuning, and nothing shows that individual units are edge detectors. No filters or Gabor fits are shown, and no comparison to V1 data is made.

4. **The shape-sensitivity test is weak.**
   - The shape-vs-colour grouping is measured on 16 synthetic objects, with RDMs from mean-pooled patch tokens.
   - If the training frames are greyscale-like wave images, the model may simply be insensitive to colour. This would produce "shape bias" without any shape representation.
   - "Untrained models are colour-based" is a statement about random projections of pixel statistics.
   - Shape bias is not shape selectivity as in IT, where it means tuning to contour fragments. No generalisation tests (silhouettes, texture-vs-shape conflict) are performed.
   - It is unclear how colour is handled at input.

5. **The receptive-field analysis is problematic.**
   - It backpropagates the mean activation of a central 3×3 or 4×4 token patch, averaged over all channels, to the input. The spatial variance of the normalised gradient map is then reported as "RF size".
   - Every transformer layer has a global receptive field by construction. Gradient spread through attention is not a receptive field in the CNN or retinotopic sense.
   - Min-max normalisation followed by sum normalisation of signed gradients is questionable, because the gradients are signed and there is no abs or squaring.
   - The variance depends on the object and position (29 frames of one rotating shape on white). A single stimulus is used.
   - Retinotopy is not tested at all (no position-sensitivity or topographic map analysis), yet the paper claims "hierarchical & retinotopic architectures".
   - The measure is not validated on a CNN with known RFs. There are no error bars or tests, and the units and scale are unclear.

6. **Statistical rigour is lacking.** Three seeds are mentioned, but the text gives no variability, confidence intervals or tests. Claims such as "robust" and "spontaneously" rest on curves in figures, with no quantitative summary in the text or in tables. Which layers count as "early" or "later" is never pinned down.

7. **Questionable experimental design and framing.**
   - Training uses an unshuffled stream, a constant LR and 100 epochs over the same ordered 160k frames. Ordered, non-i.i.d. batches may matter, and no ablation on this is given.
   - The simulator is run at a single (chick) preset. Wave statistics are not varied. The 3-frame, 300 ms window is asserted without justification. How wave frames are rasterised into 64×64 images is not described.
   - Framing this as a test of "selectional vs instructional theories" is a false dichotomy. The architecture, patching and contrastive objective are themselves strong inductive biases chosen by the experimenter, and are arguably analogues of genetic instruction.
   - The claim that transformers have "no hardcoded priors" overlooks patch tokenisation (which embeds locality), position embeddings and the architecture.

8. **Novelty and related work.**
   - Retinal-wave training of ANNs (Albert 2008, Cappell 2024, Ligeralde 2024) and emergent locality in non-convolutional networks (Ingrosso & Goldt) already exist. The delta is ViT + CoT objective + three probes.
   - Prior CNN/ICA studies are dismissed because CNNs are "hardcoded", but no empirical comparison is made.
   - The paper is heavily self-citing and builds on the same group's ViT-CoT work. Related work on emergent locality in ViTs and developmental SSL is thin.

9. **Presentation.** The bulk of the paper is framing and discussion. Methods are underspecified (the contrastive loss form, negatives, image channels, how the wave is rendered, the layer definition used for RDMs, and the t-SNE settings are not described). The broader-impact claim that a "prenatal phase" makes models more brain-like is speculative and untested, since there is no downstream or transfer experiment.

## Questions
1. What happens with CNNs, other objectives (SimCLR/MAE/predictive) and non-retinal-wave temporally smooth inputs (natural video, moving noise)? Is anything specific to retinal waves?
2. Could you add a control with smooth non-wave motion, and one that preserves temporal order but removes spatial contiguity?
3. How sensitive are the edge scores to the decay factor of the hand-built RDM, to the 0–90° range, and to the stimulus type? Can you show unit-level tuning curves and filters?
4. Are the training images colour or greyscale? If greyscale, is the "shape bias" simply insensitivity to colour?
5. Can you validate the RF measure on a CNN with known RFs? Can you use several stimuli, and a retinotopy measure (sensitivity as a function of probed position)?
6. How are "early" and "later" layers defined? Please provide per-layer numbers with seed variance and statistical tests.
7. Does the ordered-batch regime matter? Do shuffled batches with temporal-window positives give the same structure?
8. How do you reconcile "no genes" with the experimenter-specified architecture, patching, loss and temporal window?

## Ratings
- **Soundness: 2**. The measurements are weak or non-validated, controls are missing, and the headline inference does not follow from the evidence.
- **Presentation: 2**. It is clear at a high level, but the methods are underspecified and the framing is overstated.
- **Contribution: 2**. The question is interesting, but the result is incremental over prior retinal-wave work and does not discriminate among hypotheses.

**Rating: 4** (marginally below the acceptance threshold). The scrambling control and the premise are of interest, but the overclaiming, absent baselines and weak probes keep it below acceptance.

**Confidence: 4**
