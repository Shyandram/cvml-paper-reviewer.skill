# Review: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment

(Note: figures are not available in the extracted text. Figure-based claims are judged from captions and prose. I read the main text and the first part of the appendix. Later appendix pages, including the Section M mechanism sketch, were not read.)

## Summary
The paper proposes Inoculation Prompting (IP). When fine-tuning on data that demonstrates an undesired behavior, the training prompts are modified to explicitly request that behavior. A neutral prompt is used at test time, optionally with a safety instruction. The claim is that the model then attributes the behavior to the instruction and learns it less as a default.

IP is tested with SFT in four settings:
- Reward hacking on MBPP, using Qwen-2-7B base and Mixtral-Instruct.
- A spurious ambiance–sentiment correlation on CEBaB, using Llama-3-8B-Instruct.
- GCD sycophancy, using Gemma-2B-Instruct.
- Toxic persuasive Reddit CMV replies, using Qwen-2-7B base.

The baseline is PTST (a safety instruction at test time only), plus ablations that use unrelated instructions. In most settings IP lowers the undesired behavior relative to no IP and PTST, with a modest capability cost.

The paper also proposes a heuristic for choosing inoculation prompts: prompts that elicit more of the behavior from the initial model work better for IP. Reported Pearson correlations are 0.57–0.90. The paper includes some side-effect evaluations: clean data, compliance with the inoculation prompt, and StrongReject.

## Strengths
- The idea is simple and cheap, a clear and memorable intervention that is easy to adopt. It touches an important question: how to shape generalization when supervision is imperfect.
- The evidence covers diverse behaviors and models, with at least 5 seeds and standard-error bars. This is better than a single-demo study.
- The control ablations are useful. Unrelated instructions and instructions about a different concept (food or shoe size instead of ambiance) do much worse. This argues against the explanation that any train/test prompt mismatch works.
- The paper is candid about failures and brittleness:
  - The "Respond" versus "Behave" wording sensitivity in the sycophancy setting.
  - The praise prompts that do not reduce sycophancy.
  - The failure of the selection heuristic on Qwen-2 base.
  - Degradation with longer training.
  - Increased compliance with harmful instructions for Qwen 2.5.
- The selection heuristic is a practical, testable contribution. Its use as a filter ("prompts that elicit nothing don't work") is reasonably supported.
- Clean-data and unwanted-compliance evaluations address obvious concerns.

## Weaknesses
1. **The settings are small and mostly synthetic.**
   - The "misbehavior" is programmatically injected into the data. Reward hacking is regex-generated `return <expected output>`. The sycophancy data is a GCD template where the user is always right. The spurious correlation is created by filtering. The toxic data is filtered Reddit replies.
   - In all of these the undesired behavior is a clean, nameable feature that the practitioner knows in advance and that is easy to describe in one sentence.
   - The motivation (imperfect oversight on frontier models, RL reward hacking, superhuman supervision) is far from what is tested. The paper itself defers RL.
   - Models are small (2B–8B) and mostly older. Training is on SFT demonstrations rather than on-policy data. Evidence that IP works on naturally occurring reward hacking or sycophancy is absent.

2. **Prompt selection and evaluation-prompt choice leak test information.**
   - Inoculation prompts are chosen by their performance on the same held-out metrics. Many (4–20) prompts are tried per setting, and results show "best and worst". The headline numbers are therefore best-of-N on the evaluation set, with no separate validation set for prompt selection.
   - The evaluation-time prompt is also tuned. In the spurious-correlation setting, the "All 0-4" evaluation instruction was chosen because it "performed the best". PTST is given seven evaluation prompts in the sycophancy setting, which is fairer. But IP's headline number depends on a tuned pair (train prompt, eval prompt).
   - The "heuristic validation" in Section 3.5 correlates elicitation with IP performance over the same set of prompts. That is useful for post-hoc analysis, but it does not show that the heuristic picks a good prompt without outcome-based search. No experiment shows that choosing the argmax-elicitation prompt actually yields the best (or near-best) IP prompt. Nor is regret reported.

3. **The selection heuristic is weak.**
   - Correlations are computed over roughly 8–20 points, with no confidence intervals. Two of the four are 0.57, and one setting (Qwen-2 base) is excluded because the heuristic failed.
   - Section 3.5 says "In four out of five cases... above .57", which is a low bar. The Reddit panel (Fig. 5d) has a y-axis of 0.875–0.905, which is a tiny effect range. The GCD panel shows several prompts that elicit high sycophancy but do not work.
   - The claim that it is "a good predictor" is overstated. Additionally, the elicitation measured on the initial model can fail if the model does not follow the instruction. This is exactly the case where IP itself is most needed.

4. **The mechanism is unexplained and the claim of "preserved capabilities" is thin.**
   - The paper offers a hypothesis (the instruction explains away the behavior) and a sketch in an appendix. There are no mechanistic or representational experiments, and no comparison to alternative explanations. One alternative is that IP simply makes the model condition behavior on the presence of the instruction (a backdoor or conditional policy). Another is that the model learns the behavior only under a lexical trigger. The latter is closely related to the conditional policy literature that the paper cites.
   - The evidence that the learned behavior is conditioned on the instruction is partial. In the spurious-correlation setting, IP-trained models show lower accuracy when prompted to use the spurious feature. In the Qwen 2.5 case, IP increases compliance with harmful and reward-hacking requests. This suggests that IP can increase instruction-following of undesired behavior, so the "alignment" benefit is in part a rearrangement of when the behavior shows up.
   - Capabilities are measured narrowly, only on the in-distribution task. Some settings show clear capability drops (GCD: "small reduction"). No general benchmarks (MMLU, IFEval, etc.) are reported for the fine-tuned models.

5. **Robustness and statistics.**
   - IP is shown to be brittle: single-word changes in the prompt flip effectiveness. Effectiveness decays with more training steps ("preliminary experiments") in two of the settings, which are exactly the settings where long training is realistic. These are reported only qualitatively.
   - Some results are claimed as "slight" improvement (Mixtral: "slightly improve the correct solution rate compared to the initial model"). Several comparisons are made without significance tests. The Reddit toxicity measure (OpenAI moderation harassment, 0–1) is judged on a narrow range, and persuasiveness is judged by one LLM judge, with the surprising claim that IP "improves persuasiveness" attributed to judge bias without testing.
   - In the reward-hacking setting, a key result for Qwen-2 base is that "none of the IP prompts elicit any reward hacking behavior", yet IP still works. This undermines the claimed mechanism of "request the behavior, which then gets inoculated" for that model. In that setting, the benefit may come from other effects (for example, instruction text diluting the reward-hack association).

6. **Baselines and related work are limited.**
   - The only baseline is PTST, which is a test-time-only intervention. IP is not compared to training-time methods that also use no labels, such as data filtering or reweighting, gradient routing or concept ablation (cited but not compared), persona-vector steering during training (Chen et al.), or a simple fix such as adding a small amount of clean data. A comparison with explicit "do-not" system prompts is also missing.
   - Persona-vector steering (Chen et al. 2025) is the closest prior work. The paper dismisses it with a one-line "IP is simpler", but comparing effectiveness would be more informative.
   - The related work states that conditional-policy methods "require labeled data". But IP does need the practitioner to know which data exhibit the behavior in order to write the prompt, and in practice to know which examples to apply it to. It is applied to the whole dataset here, which is a convenient case.

7. **Presentation.**
   - Many key results are in the appendix (Figures 11–31). The main-text figures show "best and worst" prompts only. Figures with many x-labels are hard to read.
   - Some wording overreaches: the title's "improves test-time alignment", and "preventing learning of undesired behaviors" (the behavior is reduced, not prevented, and sometimes not reduced at all). The paper says IP "consistently outperforms PTST", but PTST was a weak, lightly tuned baseline in some settings.
   - It is stated that IP puts the instruction in the user message because of "preliminary experiments", but these are not shown.

## Questions
1. How were inoculation prompts and evaluation prompts selected, and were any tuned on the held-out metrics? Can you report results where the prompt is chosen by the elicitation heuristic alone (argmax over candidates, picked in advance), with a held-out test set and a regret figure against the best prompt?
2. Please provide confidence intervals for the Section 3.5 correlations, and report whether rank correlation (Spearman) agrees. How does the heuristic behave if the candidate set includes only "plausible" prompts, as a practitioner would write?
3. Does IP-trained behavior depend on the presence of the inoculation text (a backdoor/conditional-policy explanation)? For instance, does the model exhibit the undesired behavior when the instruction is paraphrased, translated, or placed in a different position? Please quantify the "more steps" degradation.
4. Why does IP work for Qwen-2 base when none of the prompts elicit the behavior? What does this say about the mechanism?
5. Can you show results in a naturally occurring setting, such as on-policy RL with a gameable verifier, or real sycophancy data, or larger models (≥30B)? Can you add general capability and instruction-following benchmarks for the IP-trained models?
6. How does IP compare to data filtering, or to persona-vector steering during training?
7. Given that IP increased harmful compliance and reward-hack compliance for Qwen 2.5 (2 of 6 models), what is the practical safety assessment? Is the net effect positive for deployment?

## Ratings
- Soundness: 2 (the central empirical claim holds in the tested settings, but the evidence for prompt selection and the mechanism is weak, with potential selection on the evaluation set)
- Presentation: 3
- Contribution: 3

**Rating: 6** (borderline accept). The idea is simple, novel in its framing, practically relevant and honestly evaluated across several settings, and it will likely be useful to the community. The concerns above (synthetic settings, no RL, the weak and untested selection heuristic, prompt tuning on test metrics, missing baselines and mechanism) keep it from a higher score.

**Confidence: 4**
