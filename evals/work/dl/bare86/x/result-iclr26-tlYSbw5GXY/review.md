# Review: Closing the Safety Gap: Surgical Concept Erasure in Visual Autoregressive Models (ICLR 2026)

Figures are not available to me. Figure-dependent claims are judged from captions and text only.

## Summary
The paper studies concept erasure in next-scale visual autoregressive (VAR) text-to-image models, using Infinity-2B. It has two parts.

1. **VARE** is a training framework. Per-scale alignment is computed with teacher-forced "auxiliary" tokens r^ori, produced by the original model from the neutral prompt c. The goal is to avoid error accumulation across scales when diffusion-style losses are applied naively.
2. **S-VARE** is the method built on it. A filtered bitwise cross-entropy erasure loss (L_FCE) masks tokens whose bits are mostly already "correct". A KL preservation loss (L_Pre) distills the original model's behavior under the neutral prompt.

It is evaluated on nudity, object (Imagenette, mainly "church") and style (Van Gogh) erasure. Baselines are ESD, AC, FMN and UCE, all re-implemented inside VARE. Robustness is tested on I2P, MMA and Ring-A-Bell. The paper reports strong erasure (nudity Sen. 158→5) with small FID/CLIP changes.

## Strengths
- The problem is timely. Safety of VAR and bitwise AR text-to-image models is under-explored, and a working adaptation to Infinity is useful.
- The design is motivated by model specifics: BSQ bitwise prediction, self-correction training, next-scale dependence. The α ablation (Table 5) shows a clear erasure/quality trade-off, so the filter does something.
- Coverage is reasonable: three erasure types, ten Imagenette classes, multi-concept erasure (Table 7), module ablations, and three adversarial prompt sets. Training is cheap (50 prompt pairs, 500 iterations, one A6000), with the same hyperparameters across tasks.
- Preservation metrics (ACC_i, FID, CLIP) are better than the adapted baselines, and the two-loss ablation (Table 4) is consistent.

## Weaknesses
1. **Train/inference mismatch in VARE is not addressed.** Training feeds teacher-forced tokens r^ori from the original model (Eq. 7, Sec. 4.1). At inference the erased model must condition on its own tokens. The paper never says whether auxiliary tokens are used at inference, or how the model behaves on its own contexts, so exposure bias is a real risk. The claim that VARE "stabilizes" training rests on one qualitative figure (Fig. 2). There is no quantitative measure of cross-scale error accumulation, no per-scale analysis, and no teacher-forced vs. free-running comparison.
2. **Baselines are weak and partly strawmanned.** All are self-ported, with diffusion losses turned into MSE on token probabilities. The appendix itself says several collapse by construction (AC-N, ESD "subtracting visual tokens"). UCE's failure is attributed to T5 robustness without any test. No per-baseline tuning is reported. The closest prior work, EAR (Fan et al., 2025, erasure for unified AR models), is cited and its data pipeline is used, but it is not compared. "First effective method" is therefore unsupported. There is no simple strong baseline either, such as ESD/AC with bitwise CE but without the filter. Table 4's ablation baseline equals AC-N (9.8/68.9/35.3/30.6), so the comparison is essentially AC-N versus AC-N plus the two new losses.
3. **Narrow lexical form undermines "robust".** The appendix says training prompts use only the word "naked", not "nude" and similar words, and test prompts explicitly contain the target concept. The headline numbers (Sen. 5, ACC_e 4.4) are therefore near the training distribution. Specific problems:
   - There is no quantitative synonym or paraphrase evaluation, only a few qualitative figures.
   - Style erasure leaves residual detection (8.2%).
   - The adversarial sets were built for diffusion models and are not adaptive attacks on this model. No white-box or prompt-optimization attack is tried.
   - Ring-A-Bell is largely token-level perturbation, so a text-side change can look like robustness without removing the capability.
4. **"Surgical" is not demonstrated for nudity.** Common-content count (Com.) falls from 112 to 57 in Table 1, and in Table 3 from 419→146, 477→184 and 105→52. That is a 50–70% loss of non-sexual body-part content. The text hedges ("performs only below UCE"). There is no evaluation on clothed people, anatomy, or art/medical contexts. COCO CLIP/FID is a weak proxy for damage to adjacent concepts. Object erasure tests only other Imagenette classes, with no closest-concept test (other buildings or places of worship). Style erasure does not report effects on other artists, the standard test.
5. **Thin evaluation protocol.**
   - There are no seeds, confidence intervals or variance. Differences such as 4.4 vs 3.8/4.2 are within plausible noise, and the test-set size is not stated.
   - NudeNet is a single detector, and counts can fall because of image degradation.
   - "Church" is the only concept in the main comparison and the loss ablation. Style is Van Gogh only. The Imagenette table has no baselines.
   - For some classes ACC_e of the original is only 16–20% (English Springer, French Horn), so erasure there is not meaningfully measurable.
   - There is no human evaluation.
6. **The method description is imprecise.**
   - Eq. 7 applies L2 to "p_θ(r_i|·)" without saying what object this is (probabilities, logits, bits). Sec. 4.2 then argues MSE is inapplicable and replaces it. The contributions list is internally inconsistent (S-VARE vs VARE).
   - Eq. 8–10 are confused. L_CE is defined as log p (no minus sign). ratio(L_CE ≥ γ) is described as the percentage of correct bits, and γ = −log(1/2) is called "accuracy". The text says a token with fewer than α incorrect bits is excluded, but Eq. 9 as written selects tokens whose correct ratio exceeds α, so the mask direction is ambiguous. Eq. 10 has no target.
   - The CE target is the original model's quantized (hard) output under c, not a soft distribution. Why is that preferable to distilling soft targets? The explanation for why swapping CE and KL collapses (App. C.3) is speculation with no analysis.
   - KL(p_θ || p_θ*) in Eq. 11 is in the reverse of the usual distillation direction, with no justification.
   - Fig. 3 (loss heatmaps for one prompt) is used to justify the filter, with no quantitative support.
7. **Scope.** Only Infinity-2B is used, so claims about "VAR models" are tested on a single bitwise model with a T5 encoder. Weight-level recovery (relearning by light fine-tuning) is not tested. The "closing the safety gap" framing is too strong for the evidence.
8. **Minor.**
   - The abstract's "97% erasure, <2% CLIP degradation" is not stated explicitly in the results.
   - Typos and labeling errors: "CA-N" vs "AC-N", Eq. 15 labeled L_AC−M, "β0/β1".
   - A learning rate of 2×10⁻³ with AdamW is unusually high and unjustified.

## Questions
1. At inference, does the erased model use its own generated tokens? How does it behave away from teacher-forced contexts? Please compare teacher-forced and free-running training quantitatively (per-scale error, FID).
2. Why is EAR not compared? Can you add an ESD/AC variant with the same bitwise-CE loss, to separate the gain of your filter and preservation loss from the choice of loss type?
3. Please report results with synonyms and paraphrases ("nude", "topless", "unclothed"), prompts outside the training lexical form, and at least one adaptive attack.
4. What explains the roughly 50% loss in Com.? Please evaluate related-but-not-erased concepts (clothed people, anatomy, other artists, other buildings) and run a human study.
5. Please fix Eq. 8–10 and the mask direction, and show how many tokens are masked per scale and epoch. Are α and γ selected on the same Ring-A-Bell data used for reporting? How sensitive are they across concepts?
6. How many seeds and images underlie each number, and what is the variance?
7. Does the erasure survive light fine-tuning attacks?

## Scores
- Soundness: 2
- Presentation: 2
- Contribution: 2

## Rating: 4 (marginally below the acceptance threshold)

## Confidence: 4

The problem is relevant and the pipeline is practical, with consistently better numbers than the ported baselines. However, the key mechanism is under-justified (inference-time mismatch), the closest prior work is not compared, the "surgical" and "robust" claims are not supported (halved common content, a single lexical form, no adaptive attacks), the evaluation lacks variance and breadth, and the method equations contain errors.
