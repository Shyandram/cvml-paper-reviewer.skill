# Review: Mapping Post-Training Forgetting in Language Models at Scale (ICLR 2026)

*Based on the extracted text, main body only. Figures were not available, so claims that depend on them are judged from captions and prose. I did not read the appendix.*

## Summary
The paper proposes measuring forgetting in post-trained LMs per sample. Forgetting F is the fraction of items answered correctly before training and incorrectly after (1→0). Backward transfer BT is the fraction of 0→1 items. For multiple-choice benchmarks the authors subtract a chance baseline. The baseline comes from a response model in which the LM either "knows" or guesses uniformly, and pre/post guesses are independent. It is computed from marginal accuracies and k alone, which gives F_true, BT_true and "ceilings". They apply this to about 30 publicly released base→post-trained checkpoint pairs on 12 MCQ benchmarks, grouped into 9 categories. The training types are:
- domain-continual pretraining (Qwen-Coder/Math)
- instruction tuning
- reasoning SFT/RL from base models
- reasoning SFT/RL from instruct models, in low-data (s1, LIMO) and high-data (OpenThinker, OpenCodeReasoner, Intellect-2) regimes

They also test EMA/LERP/SLERP merging. The reported conclusions are:
- Forgetting is low to moderate, which contradicts the classical continual-learning narrative.
- Backward transfer is large for math and logic.
- Larger models forget less.
- Merging does not reliably help.
- The high-data regime has no clear pattern.

## Strengths
- The question is important and timely. Practitioners assume post-training does not erode pretrained knowledge, and there is little systematic evidence either way.
- Sample-wise 1→0 / 0→1 accounting is a sensible complement to aggregate accuracy. Aggregates can hide offsetting flips.
- The study is broad: many model families, sizes and post-training types, run in one evaluation harness (LightEval) with per-sample logs. The authors promise to release code and logs, which would be a useful resource.
- The authors are fairly candid about several limitations. They say backward transfer mostly reflects better elicitation, that F_true may reflect failed elicitation rather than erased knowledge, that the high-data results are "preliminary", and that merging results are limited.
- Several qualitative checks reveal real artefacts: answers embedded in code, answering with numbers instead of letters, and multilingual garbage from Qwen-Math-Instruct.

## Weaknesses
1. **The chance-correction rests on assumptions that are weak for CoT-generating LLMs and are not validated.**
   - The correction assumes the model either knows an item or guesses uniformly among k options, and that the pre- and post-training guess events are independent.
   - Real LM errors are structured. Distractor preference is not uniform, and "partial knowledge" is common (elimination of options).
   - Pre/post correctness is strongly correlated through shared weights and item difficulty. A "guess" is likely to persist as the same guess after small updates, so independence is likely violated.
   - The paper offers no empirical validation, for example against logit-based or multi-sample "knows" estimates, or a simulation or synthetic-noise test showing that F_true tracks injected true forgetting.
   - The correction is also dataset-level, using marginal accuracies. It therefore does not identify which individual items were really forgotten, which undermines the motivating "samples are not fungible" argument.
2. **Metric definition and worked example issues.**
   - F_true is a subtracted flip rate, not a rate conditional on items "genuinely known", which is what the introduction says it measures ("among items the model genuinely knew…, what fraction became wrong beyond chance?"). Normalisation by F_max is only mentioned as a ceiling.
   - The worked example does not match the formulas. With 80%→70% and k=4, F_chance = (0.2/3)(0.3) = 0.02, so the adjustment is about 2 points, not the "about 6%" stated. The example also treats a net accuracy drop as raw forgetting.
   - Clipping at zero introduces a bias. Noise in either direction is truncated at zero, so small-effect regimes are biased upward.
   - Many of the benchmarks may not be pure k-way MCQ with comparable guessing behaviour, and k varies. Applicability is not discussed.
3. **Measurement noise is ignored.**
   - Generation uses temperature 0.6 with what appears to be a single sample per item.
   - Stochastic decoding alone creates 1→0 and 0→1 flips even for an identical model. The chance correction does not address this. The key control is missing: a "forgetting" estimate between two independent runs of the same checkpoint, or between a model and itself under a different seed.
   - No confidence intervals, bootstrap or seed variance appear anywhere in the main text. The words "low", "moderate" and "high" are never defined by thresholds. Claims such as "marginally decreases with scale" cannot be assessed.
4. **Confounding by instruction-following and answer extraction, which the authors themselves show.**
   - Base models get few-shot formatting prompts and post-trained models get zero-shot chat templates. The comparison of "pre" and "post" is therefore also a comparison of prompting and format compliance.
   - Large "backward transfer" is attributed to elicitation, and large "forgetting" in several models to format failures (OpenCodeReasoner, Qwen-Math-Instruct, Nemotron). Such failures are extraction artefacts, not knowledge loss.
   - These artefacts change the paper's headline results by large amounts, yet no robust extraction was used, such as an LLM judge, log-likelihood scoring of options, or manual verification on a sample. The conclusion that the numbers "are highly dependent on the extraction method" undermines the quantitative maps.
   - The 32K / 4K length caps differ across models (Qwen-Math is limited to 4K) and may truncate long CoT.
5. **The experimental design cannot support the causal and scaling claims.**
   - The "~30 model–training pairs" are public checkpoints whose training data, recipes, hyper-parameters, teacher models and compute are uncontrolled and often unknown. A comparison across stages or sizes is confounded by data mix, number of steps, learning rate and base-model quality.
   - Claims such as "scaling model size reduces forgetting", "reasoning training yields larger backward transfer than instruction tuning", and "mixed domains improve both" are based on a handful of non-matched points, with no statistical analysis.
   - In the high-data regime the authors concede that "no single factor" explains the results, which is an inconclusive finding.
   - The title and abstract claim a "map at scale", but there is no controlled study that varies data scale, e.g. training the same base model on increasing amounts of data. "Data scale" is inferred from model families.
6. **Scope of "pretrained knowledge" is narrow and the headline conclusion is over-stated.**
   - Forgetting is measured only on short-answer MCQ benchmarks. Free-form generation, long-tail factual recall, calibration, multilinguality, safety and instruction-following are not covered.
   - MCQ recognition is a lenient probe of knowledge and is exactly where forgetting is easiest to hide. Concluding that "sequential training does not automatically erode pre-training knowledge" and that the continual-learning literature is mismatched is over-reaching, particularly as Table 1 compares to studies using different protocols.
   - Several "high-data" models are only 7B–32B, so the "at scale" framing is modest.
   - The Table 1 "Level" labels (Low/Med/High) are subjective. For example, a ~2% MMLU drop is labelled "Low" but is cited as evidence of forgetting.
7. **The merging section is thin.**
   - It covers three models and two-checkpoint interpolation, with no ablation over α in the main text. Interpolating a base with a heavily post-trained model is known to be non-benign for large weight drift.
   - The paper offers hypotheses that it does not test (weight drift, number of checkpoints). "Merging does not reliably mitigate forgetting" is too general a statement for this evidence. It also introduces a new topic that dilutes the contribution.
8. **Novelty of the metric is limited.** Per-sample flip analysis, "backward transfer" and "forgetting" as transitions, and chance correction (e.g. guessing correction in psychometrics) all exist. Contribution relative to these is not discussed. The paper presents the metric as a primary contribution but offers little validation.
9. **Presentation.**
   - Several claims in text and summary are inconsistent. The abstract says forgetting is "moderate" for CPT, while the key findings and Figure 3 caption say "low-to-moderate". Section 3.2 says scale "reduces forgetting and backward transfer" in the caption and "reduces forgetting and increases backward transfer" in the results paragraph.
   - There are typos, and the reference list has duplicate entries (Fernando et al., Li & Lee).
   - Most results sit in figures (heatmaps by category) whose numeric values are in the appendix. The 9-category clustering procedure is not described in the main text, so the grouping may be post-hoc.

## Questions
1. Can you validate the chance model? For example: compare F_true against forgetting measured with logit or multi-sample "knowledge" estimates, show the pre/post-guess independence assumption holds (or quantify the correlation), or run a synthetic experiment with injected forgetting.
2. What is the flip rate (F and BT, raw and adjusted) between two runs of the *same* checkpoint under different seeds and temperature 0.6? How do the reported effects compare to that noise floor? Please add confidence intervals.
3. How would the headline results change with an extraction-robust protocol, e.g. option log-likelihood scoring or an LLM-judge answer extractor, with the same prompt format for base and post-trained models? Which of the reported "forgetting" cells are format failures?
4. Can you run a controlled experiment (same base, same data mix, varying amount of data/steps and model size) to support the data-scale and model-scale claims?
5. How are the 9 categories and the low/moderate/high thresholds defined, and were they chosen before looking at the results?
6. Please reconcile the worked example (80%→70%, k=4 gives "about 6%") with the stated formulas.
7. How does the metric behave for non-MCQ and open-ended benchmarks, where chance correction is undefined?

## Ratings
- **Soundness:** 2. The chance model is unvalidated, there are no noise controls, and the measurement is confounded by prompting and extraction.
- **Presentation:** 2. The paper is readable, but there are internal inconsistencies, vague qualitative thresholds and a worked-example error.
- **Contribution:** 2. The question is relevant and the empirical resource may be useful, but the metric is a modest addition and the empirical conclusions are weakly supported.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

The topic is worthwhile and the breadth of evaluation is a plus. However, the conclusions depend on a metric whose assumptions are untested, on single-sample noisy evaluations without confidence intervals, and on uncontrolled public checkpoints whose "forgetting" is often shown to be an instruction-following or extraction artefact. I would raise the score for noise-floor controls, an extraction-robust re-evaluation, and at least one controlled scaling study.
