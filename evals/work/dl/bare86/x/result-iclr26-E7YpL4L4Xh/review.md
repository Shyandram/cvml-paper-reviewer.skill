# Review: EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling

*Based on text only. Figures were not available, so claims about Figs. 2 and 3 are judged from captions and prose.*

## Summary
The paper proposes a three-part pipeline for RL in instruction-guided image editing.
1. **EditReward-Bench.** A human-annotated benchmark with 3,072 pairwise preferences, built from 13 editing subtasks and 11 editing models. Two experts must fully agree on a tiered ranking of 5 outputs, along three axes: prompt following, consistency and overall quality.
2. **EditScore.** Qwen2.5-VL (7B/32B/72B) models, LoRA-finetuned as generative reward models. They output reasoning followed by a score in the VIEScore style (semantic consistency and perceptual quality, combined as a geometric mean). The training labels are distilled from GPT-4.1 on 70k synthetic samples and filtered by group-wise max score and std. At inference, K stochastic passes are averaged ("self-ensemble").
3. **Downstream use.** EditScore is used for best-of-N selection and for Flow-GRPO fine-tuning of OmniGen2. The authors report that off-the-shelf Qwen2.5-VL (7B–72B) rewards fail to converge, while EditScore gives stable gains: GEdit-Bench overall 6.28→6.68 and ImgEdit 3.40→3.63.

## Strengths
- The problem is timely. Reward models for editing are scarce, and the open release of a benchmark and models should be useful to the community.
- The benchmark protocol is careful. It uses tiered rankings with ties and requires full inter-annotator agreement. Its candidate pool includes strong proprietary editors, and it has three evaluation axes. It covers more subtasks than ImagenHub or GenAI-Bench.
- Evaluation is end-to-end: reward-model accuracy, then best-of-N, then RL.
- The cost analysis (Fig. 2) suggests that test-time self-ensembling is more FLOP-efficient than scaling parameters. This is a useful practical observation, though I could only read it from the caption and text.
- The ablations on score range and reasoning-first output (Table 3) are informative.
- The variance-vs-accuracy observation (Table 4) is interesting and consistent with the optimization view of reward models in Razin et al.

## Weaknesses
1. **Claims of beating or matching proprietary VLMs are overstated and not statistically supported.**
   - EditScore-72B Avg@4 reaches 0.763 on overall quality, against 0.755 for GPT-5. The abstract says the model "surpasses GPT-5", and the introduction says it surpasses "leading proprietary VLMs".
   - The gap is small and no confidence intervals or significance tests are given. Pairs from the same prompt are not independent, so a bootstrap over prompts is needed.
   - The comparison is asymmetric. EditScore gets K=4 samples, while GPT-4.1, GPT-5 and Gemini appear to be evaluated single-pass. Table 3 shows GPT-5 at 0.755 with no ensembling. The proprietary models were not given the same inference-time ensembling.
   - EditScore is distilled from GPT-4.1 labels, and its single-pass accuracy (0.703 for the 72B) only matches its teacher (0.705).
2. **Circular evaluation of the downstream gains.**
   - The reward model is trained on GPT-4.1 VIEScore-style labels. The RL policy is then evaluated on GEdit-Bench and ImgEdit-Bench, using GPT-4.1-based VIEScore as the metric (Tables 4 and 5, Fig. 3). The metric and the reward share a rubric and a teacher, so reward hacking against that shared bias is not excluded.
   - The GPT-5 cross-check in Table 4 is only a partial remedy, and its differences are tiny (5.834 vs 5.768).
   - There is no human evaluation or user study of the RL policy, and no check for reward hacking such as degraded consistency or artifacts.
   - The judge used for ImgEdit-Bench should be stated.
3. **The central causal claim, that a high-fidelity reward model is the key to unlocking RL, is under-supported.**
   - The only evidence is that Qwen2.5-VL 7B/32B/72B used directly as rewards give unstable training (Fig. 3b, a single curve per model). That failure may come from prompt or score-range mismatch, miscalibration or low reward variance. It need not reflect "accuracy".
   - A direct baseline is missing: RL with the teacher (GPT-4.1 or GPT-5) as reward on the same OmniGen2 setup and budget. It would show how much RL improvement is lost relative to the teacher.
   - Table 5 compares with UniPic2 "RL w/ GPT-4.1", but that is a different base model and recipe, so it is not a controlled comparison.
   - Table 4 shows that RM accuracy is essentially identical (0.637 vs 0.638) while RL outcomes differ. This partly contradicts the headline narrative that fidelity is the key. The conclusion that GPT-4.1 labels are "better for RL" rests on a GEdit difference of 0.083 from what appears to be a single run.
   - There are no seeds, error bars or run-to-run variance for any RL result. Gains of this size are within plausible RL noise.
4. **The accuracy metric is under-specified.**
   - The base Qwen2.5-VL-7B scores 0.325 on consistency, well *below* chance. This suggests an issue in how pairwise accuracy is defined.
   - The paper does not say how ties in predicted scores are counted, how human-tied pairs are treated, or what the chance level is.
   - The 3,072 pairs come from tiered rankings of 5 outputs, so pairs share prompts and images. The effective sample size is far smaller than 3,072.
   - Per-category numbers (Table 2) are noisy and are used without any intervals.
5. **Possible data overlap and leakage.**
   - The benchmark's tasks are "curated from" GEdit-Bench-EN and ImgEdit-Bench, and the same benchmarks are used to evaluate the RL policy.
   - Training instructions are generated by Qwen2.5-VL-72B from reference instructions. The paper does not say whether these references or the input images overlap with the GEdit/ImgEdit/EditReward-Bench prompts. A decontamination statement is needed.
   - The benchmark's candidate pool includes OmniGen2 outputs, and OmniGen2 is the RL base model.
6. **Novelty is modest, and the comparison to related work is thin.**
   - The recipe is assembled from existing components: a VIEScore rubric, GPT distillation, a generative reward model with CoT, test-time score averaging as in DeepSeek-GRM, and Flow-GRPO.
   - Related editing reward models and benchmarks are dismissed as outdated or not open-source. No other editing reward model (e.g. ADIEE or concurrent work) is evaluated on the new benchmark.
   - There is no comparison to a pairwise or Bradley-Terry reward model. The data filtering is described in two sentences with no ablation, although "meticulous curation" is claimed as a key factor.
7. **Training details are insufficient.**
   - It is unclear how the 70k labelled samples are used (a single GPT-4.1 score per output, or pairwise?), what the filtering thresholds and LoRA settings are, and what temperature is used for the K passes.
   - The RL section lists few hyperparameters. The reward normalization, the training compute, and the fact that Avg@4 multiplies reward cost by 4 are not discussed.
   - Only the 7B model is used for RL. No analysis relates RL outcome to RM accuracy across the 7B/32B/72B EditScore models. "Accuracy translates to RL" is shown only for Avg@1 vs Avg@4 (Fig. 3c), where the y-axis spans just 6.30–6.70.
8. **Scope of the RL evidence.** Only one base model (OmniGen2) and one RL algorithm (Flow-GRPO) are tested. Other editors are covered only by best-of-N, and Qwen-Image-Edit shows minimal gains.
9. **Presentation.**
   - There are inconsistencies. Figure 2 is described as a "gray dashed line" in the caption but "gray dotted lines" in the text. "EditReward" and "EditScore" are used interchangeably in Fig. 3 and the Table 5 discussion. The text refers to "Appendix 5". The abstract says "learning proprietary VLMs". The Table 5 text says "Semantic Control" for Semantic Consistency.
   - "Efficient" is claimed but never measured as latency or throughput per reward call, and K=4 ensembling multiplies the cost.

## Questions
1. How is pairwise accuracy computed with tied predictions and tied human labels? Why is the 7B Qwen at 0.325 on consistency? What is the chance level?
2. Can you give prompt-level bootstrap confidence intervals for Table 2? Is EditScore-72B Avg@4 > GPT-5 significant? What do GPT-5 and GPT-4.1 achieve with the same Avg@4 ensembling?
3. What happens in the RL setup if GPT-4.1 or GPT-5 is the reward, even for a short run? What happens with base Qwen2.5-VL prompted with the same [0,25] reasoning format? Is the failure caused by low reward variance or calibration?
4. How many seeds underlie Tables 4 and 5? Please give variance.
5. Do any prompts, images or reference instructions overlap among the RM training set, EditReward-Bench, GEdit-Bench, ImgEdit-Bench and the RL prompts?
6. Is there human evaluation of the RL policy, or an evaluation with a judge unrelated to the training labels? Is there evidence that consistency and image quality did not degrade?
7. What do ablations of the two filtering steps and of CoT in training show? How does EditScore compare with a Bradley-Terry reward model on the same data, and with other editing reward models on EditReward-Bench?
8. Is the "reward std" in Table 4 global or within-group? Within-group std would matter through GRPO advantage normalization.

## Ratings
- **Soundness:** 2 (fair). The benchmark construction is reasonable, but the claims about beating GPT-5 and about being the "key" to RL lack controls, uncertainty estimates and independent evaluation.
- **Presentation:** 3 (good). The structure is clear, but there are typos, inconsistent naming and missing details.
- **Contribution:** 3 (good). The released benchmark and models are useful, but the technical novelty is incremental.

**Rating: 6** (marginally above the acceptance threshold). An annotated benchmark and open reward models with a working RL demonstration are valuable. I would raise the score if the RL results had a teacher-reward baseline, seeds, and human or independent judging.

**Confidence: 4**
