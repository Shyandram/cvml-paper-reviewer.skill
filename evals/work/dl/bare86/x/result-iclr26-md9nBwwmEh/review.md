# Review: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads (Locate-Then-Correct, LTC)

I read the main text and the appendix up to B.3. I did not read the rest of the extracted file. Figures were not available, so figure-dependent claims (Figs. 2, 3, 4, 10–14) are judged from captions and text only.

## Summary
The paper proposes Locate-Then-Correct (LTC), a training-free method for reducing spurious correlations in CLIP ViTs.

1. **Decomposition.** The image representation is decomposed into per-head contributions (Gandelsman et al.). Each head's direct logit contribution is projected through the text side (logit lens).
2. **Locating heads.** For each sample, the head with the largest logit difference between the target class and the alternative is marked (a one-hot "argmax" vote), and the votes are averaged over a set. Contrasting this vote map between wrongly and correctly classified samples in the negatively-correlated group G_N isolates "spurious" heads, via σ(V_NW − V_NC). The reverse contrast isolates "target" heads.
3. **Correcting.** Spurious heads are mean-ablated. On target heads, an LLM-derived class-difference text direction is projected and added back ("knowledge injection", as in RoboShot).

Evaluation covers:
- Waterbirds and CounterAnimal (background bias).
- GenderBias-VL occupations (classification and retrieval) and FairFace (retrieval).
- Three OpenCLIP sizes, compared against TextSpan, Ortho-Cali and RoboShot.
- JTT-LTC, an extension on top of JTT.

LTC gives large worst-group gains on Waterbirds (for example, ViT-H WG 50.3→71.3) and large reductions in gender bias on GenderBias-VL. The paper also gives interpretations of the selected heads through SHAP over captions and pixel maps. It claims a "spurious-association" head (Z_SY) distinct from a pure spurious-attribute head.

## Strengths
- The idea is simple, cheap, and well motivated by the linear decomposition. Replacing TextSpan's manual head labeling with a contrastive, data-driven selection is a sensible and useful step.
- The ablations are informative:
  - Random heads (LTC (R)) are harmful, which supports the claim that localization matters (Tab. 6, 7).
  - KI at the head level beats RoboShot's KI at the whole-representation level with the same LLM concepts.
  - Selection reportedly needs few labels (Fig. 10).
- Results on three backbone sizes show a consistent trend for Waterbirds and GenderBias-VL, and the method doesn't depend on fine-tuning.
- The observation that the "spurious" heads found by the contrast encode the S–Y association rather than S alone (Sec. 6, Fig. 4) is interesting, if it holds up.
- The paper is honest about not tuning γ.

## Weaknesses
1. **The protocol is not really "zero-shot, no group labels."**
   - Locating Z_S and Z_Y requires G_NW and G_NC. These need ground-truth class labels, knowledge of which samples are in G_N (the spurious attribute s), and the model's correctness on them. The paper says "we only assume access to ground truth group labels for validation," but the non-tuning baselines are described as not assuming group labels.
   - Ortho-Cali and RoboShot also use the validation set, but TextSpan is run on ImageNet with no validation data. LTC therefore has the most supervision of all the training-free methods.
   - The LTC-Ŝ variant (zero-shot predicted group labels) is mixed. It is worse on ViT-B (61.8 vs 73.3) and is better or equal elsewhere. The paper should lead with the label-free variant and treat the labeled version as an oracle.
   - Comparisons against supervised-group-label methods (Cont Adapter, JTT) are hard to read. JTT's first stage is replaced by zero-shot group labels, and the hyperparameters (λ_up = 90/100) are tuned. Reporting results only at the best configuration is not a fair comparison.
2. **The gender evaluation is partly circular.**
   - The "worst group" G_N is the 10 occupations with the highest bias score under zero-shot inference, chosen separately for each model. Evaluation is on the 152 held-out occupations, but the 10 worst are again picked using zero-shot bias on the evaluation set.
   - The paper then reports "BT" on those worst occupations after the intervention. There is a selection effect (regression to the mean). Reported values (for example, 74.0→10.0 on ViT-B) are larger than the improvement in overall bias (16.3→9.4).
   - A fixed, a priori set of worst occupations, or bootstrap or confidence intervals, would be needed to make these numbers trustworthy.
   - Table 2 reports BT/BO/MT/MO, but there is no accuracy or utility metric, so a bias drop cannot be separated from a general performance loss (a classifier that is equally wrong for both genders has zero bias).
3. **Baseline results look anomalous and are insufficiently investigated.**
   - Ortho-Cali on ViT-H/14 Waterbirds has WG 18.1 and Avg 41.9, which is far below zero-shot and suggests a failed implementation or hyperparameter. The paper does not comment on it.
   - RoboShot's failure on gender is attributed to LLM safeguards, but this is a conjecture, not tested (for example, by supplying the spurious concept explicitly).
   - The Table 3 numbers for LTC (MA) equal TextSpan exactly on ViT-B (16.8) and ViT-L (26.2), which is suspicious and unexplained. It also means LTC is not better than TextSpan there, and the "automatic identification of the same heads" claim doesn't demonstrate a gain.
4. **Weak results on the multi-class benchmark.**
   - On CounterAnimal, the gains are 0.4–1.7 accuracy points over zero-shot. That is probably within noise, and no variance or significance is reported.
   - The method needs an ad hoc counterfactual class pairing ("most frequently misclassified class") derived from the easy split, and a pseudo-label retrieval hack (Sec. A.1). This is a substantial departure from the paper's general-purpose framing.
   - The evaluation covers only 45 of 1000 ImageNet classes. No accuracy is reported on the other classes or on standard ImageNet, so it is unknown whether the interventions damage general performance.
5. **The theoretical justification (Eqs. 8–10) is loose.**
   - V is first made one-hot per sample (Eq. 7), then averaged and normalized, and Eq. 8 treats it as a linear mixture V_Y + a_sy·V_S + ε. The mixture has no clear meaning for a one-hot vote or for a normalized distribution.
   - The claim that "Eq. 10 isolates positive V_S while filtering out negative V_Y" relies on normalizing both quantities to 1. This argument is heuristic. It is not shown that the mask σ(V_NW − V_NC) recovers spurious heads in any controlled setting (for example, a synthetic model or injected heads).
   - Only the top-1 head per sample enters the vote. Heads with a smaller but systematic direct effect, and indirect effects through later layers or MLPs, are ignored. MLPs are dropped entirely, and direct logit-lens effects are not causal effects. The reported success of ablation partially supports the direct-effect view, but no activation patching is performed.
   - The thresholded mask uses γ = 1/|P*_NW ∪ P*_NC|. This is a heuristic, and its sensitivity is only partly shown (Fig. 10, B.3). The Limitations section mentions "λ" but the text uses γ.
6. **Interpretation claims are stronger than the evidence.**
   - The statements that LTC "offers significantly greater interpretability" and that the interpretation "corroborates the contrastive mechanism" rest on a few visual examples (Waterbirds), SHAP on GPT-4o captions, and a single pair of heads (L10H10, L11H16).
   - There is no quantitative test, no human evaluation, and no check on other datasets. The paper itself says the S/SY separation does not occur for gender.
   - The explanation of that discrepancy ("background occupies a larger portion of the image") is speculative.
   - Mean ablation at the head level hides the finding that a head can be redundant or distributed. The paper does not test whether a few heads can contain all of a concept, and I could not verify it from the text.
7. **Narrow experimental scope.**
   - Only OpenCLIP ViTs are used. There is no CelebA (dropped with a short justification), no other spurious benchmarks (for example, MetaShift, CelebA hair/gender, Spawrious), and no other CLIP variants such as OpenAI or SigLIP.
   - Missing comparisons include more recent training-free or post-hoc methods (for example, FairerCLIP, SANER, and keyword/attribute-based methods such as Kim et al., which is cited but not compared), and simple ablation baselines such as a head-selection rule using gradients or activation patching.
   - There are no seeds or confidence intervals. Waterbirds G_N validation has only 240 samples, so the results are noisy. Waterbirds worst-group accuracy on the test set is known to be high-variance.
8. **The headline claim is mis-stated.** ">50% gain in worst-group accuracy compared to non-training post-hoc baselines" is vague. Relative to zero-shot, it appears to refer to ViT-H or ViT-B, but against the best baselines the gain is generally 0–10 points (for example, ViT-L: 75.5/74.6 vs Ortho-Cali's 73.3). Also, some numbers disagree (Table 1 gap for LTC ViT-L is 9.4 and Table 6 shows 9.6, while Avg − WG = 9.5), which is a minor inconsistency.
9. **Presentation.**
   - There are many typos and unclear notations (y with an overbar that is lost, "we hypothesis", the V_Y/V_S subscript overload, and inconsistent mentions of mean and zero ablation).
   - The experimental setup is defined late and in the appendix, and key details (what exactly "G_P" and "G_N" are for gender, what the validation set is for each dataset) are hard to follow.
   - Several claims are asserted without a table (for example, "no difference between mean and zero ablation").

## Questions
1. How is LTC affected when only zero-shot-predicted groups are available (the LTC-Ŝ regime), on all datasets and with the same hyperparameters? Please report this as the main result, with seeds or bootstrap intervals.
2. Why does Ortho-Cali fail so badly on ViT-H/14 Waterbirds (18.1 WG)? Why do LTC (MA) and TextSpan give the same numbers on two FairFace backbones? Were the TextSpan heads actually the same?
3. Can you show a controlled test (synthetic or injected spurious heads) where σ(V_NW − V_NC) recovers the ground-truth heads? Does the selection agree with activation patching, which would give causal rather than direct-effect evidence?
4. In the gender experiments, how do the results change when G_N is a fixed set of occupations that is independent of the model? Also, what is the accuracy on the occupation task before and after the intervention?
5. What is the effect of LTC on general zero-shot performance (ImageNet, the remaining 955 classes of CounterAnimal) and on the P-group (G_P) accuracy? Table 1 only shows average accuracy.
6. How sensitive is LTC to the choice of the LLM-derived class-difference text, to the choice of "other class" y-bar, and to γ (not just the fraction of labels)? How many heads are selected per dataset and model (K)?
7. How does the approach handle multiple, simultaneous spurious attributes, or an attribute that is not available in the validation data? Is the framework limited to binary S?

## Ratings
- **Soundness:** 2 (fair). The idea is plausible and the ablations are helpful, but the evaluation protocol has selection and label-leakage issues, the baselines have unexplained anomalies, no variance is reported, and the interpretability claims are not rigorously supported.
- **Presentation:** 2 (fair). The paper is readable at a high level, but the method derivation, notation and experimental definitions are loose, and there are many errors.
- **Contribution:** 2 (fair). Head-level localization for debiasing is a modest, incremental step over TextSpan and RoboShot. It is useful but narrow in scope.
- **Rating:** 4 (marginally below the acceptance threshold)
- **Confidence:** 4

This is a simple, practical idea with encouraging Waterbirds and gender-bias numbers. Before acceptance it needs a fairer, label-free-first evaluation, controlled validation of the head-selection procedure, variance estimates, and explanations for the baseline anomalies.
