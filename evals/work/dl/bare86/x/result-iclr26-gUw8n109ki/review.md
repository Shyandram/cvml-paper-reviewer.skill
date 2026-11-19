# Review: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs

(Text-only review. Figures were not available, so I judge them from captions and text.)

## Summary
The paper studies image-based "OOD" jailbreaks of VLMs: SI-Attack (shuffling), CS-DJ (distraction sub-images) and JOOD (mixup).

1. **"Weak-OOD" phenomenon.** Attack success rate (ASR) and toxicity peak at a moderate perturbation strength and drop at stronger ones (Fig. 1; GPT-4o, GPT-4.1, Doubao-1.6).
2. **Explanation.** The authors attribute it to a trade-off between "input intent perception" and "model refusal triggering". Intent perception is robust to mild shifts, and refusal triggering is brittle.
   - Evidence is a PCA of Qwen2.5-VL-7B activations on SI-Attack shuffles (Fig. 2).
   - Evidence also includes two layer-averaged cosine-similarity metrics (Figs. 3–4) and a GPT-4o-mini study (Table 2).
3. **Pre-training/alignment gap.** The authors argue the trade-off follows from a gap between pre-training and alignment. This is stated as constraints and "properties" (Eq. 7, §4.1).
4. **JOCR.** The paper proposes a typographic attack in the style of FigStep. It randomly perturbs font size, character and word spacing, colour and layout. It reports higher ASR than baselines on RedTeam-2K and HarmBench across 6 VLMs (Table 4).

## Strengths
- The weak-OOD observation is simple and consistent across three attack families and three target models. It is a useful empirical note for red-teaming practitioners.
- The question is worthwhile. Explaining why attacks work, rather than only proposing new ones, is better for the community.
- The authors try to connect the analysis to a method (JOCR). The ablation of JOCR vs. FigStep vs. shuffle variants (Table 5) is a reasonable sanity check.
- JOCR is cheap and black-box, and Table 4 shows large gains over FigStep and several other baselines on several models.
- The authors release code, which helps reproducibility.

## Weaknesses

1. **The central explanation is weakly supported, and the metrics do not measure what they claim.**
   - The "intent perception" score (Eq. 3) is the cosine similarity of the hidden state at the *instruction token* between x and A(x). That measures representation stability, not recognition of harmful intent. It is averaged over all layers, including early layers where similarity is trivially near 1.
   - Section 3.1 itself says (following Zhao et al. 2025a) that harmfulness is encoded at t_post-inst and refusal at t_inst. The metrics in §3.2 use the opposite assignment: t_inst for intent, t_post-inst for refusal. This looks inconsistent.
   - The "refusal" score (Eq. 5) projects intermediate hidden states through the output head (a logit-lens-like step). It takes the cosine similarity with token *embeddings* of 50 refusal words. These vectors live in R^V, and the output head and the embeddings do not share a space. With the head applied to arbitrary middle layers, the quantity is poorly defined. Its values, 0.00–0.02, are close to zero.
   - Fig. 4 compares changes of two quantities with different units and axes (0.92–1.0 vs. 0.006–0.012). Calling one drop "sharp" and the other "gradual" is a visual impression and not a statistical statement. No normalisation, no error bars and no tests are given.
2. **The pre-training vs. alignment attribution is not tested.** The "theoretical argument for inevitability" consists of assumed constraints (Eq. 7) and asserted "properties" (text-variation robustness, intent preservation, small-sample weak generalisation). There is no theorem, proof or bound in the main text. Nothing measures dist(x, D_pre) or dist(x, D_align). Nothing intervenes on the alignment stage, for example by comparing base and aligned checkpoints, or by fine-tuning on shuffled refusals. The claim that the gap is the cause is a hypothesis presented as a finding. "Inevitability" is not justified.
3. **Table 2 is weak evidence and partly contradicts the narrative.**
   - The GPT-4o-mini "harm accuracy" is only 34–39% even for the unshuffled baseline. That means the model labels most of the known-harmful items as "Harmless". This is not a meaningful measure of intent perception.
   - Key-phrase similarity differs by ~0.01 (0.2425 vs 0.2433), with no variance reported.
   - Harm accuracy declines monotonically with shuffle (38.8→34.0), and the refusal rate also falls monotonically (84→63) without any rise at larger shuffle. So Table 2 shows no "peak" at mild shuffling and does not reproduce the trade-off. The non-monotonic ASR in Fig. 1 is not explained by these data.
   - Different models are used in each part: Qwen2.5-VL-7B for the PCA and metrics, GPT-4o-mini for Table 2, and GPT-4o/4.1/Doubao for the ASR curves. The explanation is never tested on the models where the phenomenon was observed.
4. **The PCA argument (§2.3) is over-read.**
   - It is a 2-D PCA of final-token activations at three layers, for samples that were initially refused. "Distance from the refusal region" is read from a plot, with no quantitative measure, and no probe or refusal direction is used.
   - Shuffle-4 being farthest and Shuffle-9 nearest does not exclude feature destruction. It might reflect other effects such as OCR/readability or prompt-length changes.
   - Layers 17/19/21 are chosen by citation to prior work, not by validation on this model.
5. **The weak-OOD phenomenon is based on a small, noisy set of experiments.**
   - The sample sizes are 200/200/150. No confidence intervals or repeated runs are reported, even though the effects shown (e.g., ASR 0.40 to 0.45) are modest and the judge is an LLM.
   - GPT-4o is both a target model and the judge. SI-Attack itself uses a toxicity judge for selection.
   - The perturbation axes (patch count, number of sub-images, mixup alpha) are not comparable, and the number of grid points is small (4–5).
   - Some of the plotted ranges (CS-DJ 3–15) are hard to read from the extracted text.
   - The claim that the trend is "universal" is thus stronger than the evidence.
6. **JOCR evaluation has several problems.**
   - JOCR is largely FigStep plus random typographic perturbation. The novelty over FigStep, over typographic and OCR-based attacks, and over perturbation-based variants is limited, and Table 5 shows most of the gain comes from perturbation alone (FigStep 19→JOCR 50 on GPT-4o).
   - The claim "JOCR achieves over 10% ASR higher than baselines" (Table 4 caption) is not true everywhere. On RedTeam-2K, GPT-4o has JOCR 31.65 vs CS-DJ 37.50, and Gemini 43.25 vs 42.40 (a tie). On HarmBench GPT-4o it is 50.0 vs 47.5. The gain over the strongest baseline CS-DJ is often only a few points.
   - There is no variance across random perturbation seeds, and no number of attempts per query is given (best-of-N vs. single sample would change the comparison materially).
   - Baselines are probably not tuned with the same query budget. Other relevant baselines are missing, including SI-Attack and JOOD themselves (the very methods analysed), HADES, and recent typographic/OCR attacks.
   - The evaluation uses an LLM judge only, with no human validation or judge-sensitivity analysis. Defences such as input-filtering or safety fine-tuned VLMs are not tested.
7. **The JOCR ablation does not validate the theory.**
   - In Table 6, fixing font size drops GPT-4o ASR from 50 to 23.5, but the other perturbations barely matter. This suggests the effect comes from one or two simple visual factors, which is more consistent with a generic robustness/typography-OOD effect than with the proposed pre-training story.
   - Table 5 shows JOCR-shuffle < JOCR but FigStep-shuffle > FigStep. This is explained post hoc ("VLMs are not enhanced for OCR of shuffled text"). That explanation would fit nearly any outcome.
   - The claim that JOCR "indirectly validates our findings" is circular. A better attack does not show that the explanation of why weak-OOD helps is correct.
   - The analysis is performed on SI-Attack, while the method is built from FigStep-style typography. The weak-OOD analysis is never applied to JOCR, for example by testing whether intent perception stays high and refusal falls along the perturbation-strength axis.
8. **Presentation and consistency issues.**
   - JOOD and CS-DJ are cited with the same reference (Jeong et al. 2025a/b are identical entries), so CS-DJ is given the wrong citation.
   - Eq. 8–9 are referenced but the constraints are numbered Eq. 1–2.
   - "GPT-4.1 (Achiam et al., 2023)" cites the GPT-4 report.
   - The ethics statement says the purpose is "web-based agent systems", which is unrelated to the paper. It also does not address dual-use risk or responsible disclosure, even though the paper presents a stronger jailbreak.
   - Claims of being "first to investigate from a feature perspective" are not carefully positioned against earlier mechanistic jailbreak/refusal work (e.g., HiddenDetect, which is cited).
   - The paper offers no defence or alignment recommendation beyond "informing VLM safety alignment", even though that is claimed as a goal.

## Questions
1. Why does Sec. 3.1 assign harmfulness to t_post-inst and refusal to t_inst while the metrics in 3.2 use the opposite? Can you replicate the analysis using a learned harmfulness direction and refusal direction (as in Arditi et al. / Zhao et al.), measuring projections on each as the perturbation grows?
2. Do the metrics in Eqs. 3–6 show a non-monotonic change that matches the ASR peak? Could you show them for every perturbation level together with ASR on the same model (e.g., Qwen2.5-VL, or an open model where ASR is also measured)?
3. Can you provide confidence intervals or seeds for Fig. 1, Table 4, 5 and 6, plus the number of attempts per query? How do results change with a different judge or human labels?
4. What evidence supports the pre-training/alignment gap as cause, e.g., a base vs. instruction-tuned comparison, or fine-tuning with refusals on perturbed images, which should remove weak-OOD if your explanation holds?
5. Can you apply the weak-OOD sweep to JOCR (perturbation magnitude) and show the same inverted-U pattern, and how does JOCR compare with SI-Attack and JOOD in the same setting?
6. What are the OCR-robustness checks, e.g., do the JOCR images remain readable (OCR accuracy vs. perturbation level)? Does the attack succeed because of OCR robustness or because the text is no longer matched by safety training on typographic prompts?
7. What are the defences or alignment changes that your analysis suggests, and have they been tried?

## Ratings
- **Soundness: 2** — The empirical phenomenon looks real, but the mechanism metrics are ill-defined, the theory is assumption-only, and the explanatory experiments do not reproduce the key non-monotonicity.
- **Presentation: 2** — The core idea is readable, but there are notation and citation errors, mismatched equations, inconsistent token assignments, and overclaiming in the captions.
- **Contribution: 2** — The weak-OOD observation is mildly useful and JOCR is a simple, effective attack. The headline "understanding" and "theory" contributions are not established, and the method is an incremental extension of FigStep.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**
