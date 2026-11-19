# Review: Prompt reinforcing for long-term planning of large language models (ICLR 2026)

Scope note: I read the main text (through the references). I did not read the appendix. Figures are not available, so I judged Figures 4–6 from their captions and the surrounding text.

## Summary
The paper proposes Reinforced Prompt Optimisation (RPO). It is a meta-prompting loop for improving the instruction prompt of an LLM agent in multi-turn tasks. The loop has three steps.
1. The agent interacts with simulated or real users.
2. An LLM "feedbacker" writes feedback on the trajectories. Two styles are compared. MC-style feedback is written once after the whole dialogue. TD-style feedback is written per turn. It predicts the user's next-turn emotion, forecasts dialogue success, and gives a suggestion. The per-turn pieces are then summarised.
3. An LLM "rewriter" produces a new prompt from the old prompt and the feedback. The "replay" variant also sees the earlier (prompt, feedback) pairs.

Each epoch generates 2 candidate prompts, and the one with the best validation score is kept.

Experiments cover three settings.
- **Text-to-SQL:** sharded multi-turn Spider from Laban et al. (2025), with 5 system LLMs.
- **MultiWOZ 2.1 with FnCTOD:** a simulated-user task-oriented dialogue setting, with 5 meta-prompting LLMs.
- **Medical QA:** general medicine and traditional Chinese medicine (TCM), judged by 3 human experts, with GPT-4o mini as the system.

RPO is compared with APO, GPO and a TextGrad-style MC feedbacker. The reported gains are an average of 0.477 against 0.333 on SQL for the sharded baseline, and 0.619 against 0.420 on MultiWOZ. The paper also reports that TD-style feedback is more stable early in training than MC-style feedback, and that the experience-replay rewriter helps.

## Strengths
- The problem is relevant. Prompt optimisation for multi-turn, interactive agents is less studied than the single-turn case, and the black-box, API-only setting is practical.
- The method is simple and task-agnostic. The feedbacker and rewriter prompts are fixed across tasks.
- The empirical scope is reasonable. There are three task types, a mix of open and closed models, and an objective metric plus a human-expert evaluation. The ablation on feedbacker inputs (user goal, API call) is informative.
- On the two tasks with automatic metrics, the full method beats the baselines in nearly every column (SQL and MultiWOZ).
- The paper is honest about limits. It reports a large remaining gap to the fully specified oracle. It also reports weaker results on TCM, where the base model's knowledge is thin.
- Training curves with 4 seeds and standard errors are shown for MultiWOZ.

## Weaknesses
1. **The RL framing is mostly metaphor, and the TD claim is unsupported.**
   - Eq. 3 defines δt = rt + γV(st+1) − V(st). Nothing in the method computes V, r or δ. "TD-style" is a prompt that asks an LLM to predict emotion and success at each turn and to give a suggestion.
   - The claims of "lower-variance" optimisation and "stability like traditional RL" rest on one set of curves, and the paper itself says final performance is comparable between MC and TD.
   - The TD-vs-MC comparison also confounds several differences. TD gets more tokens, per-turn context, and extra inputs such as the user goal and API calls. The ablation shows these inputs drive much of the gain. It is not clear whether the "temporal difference" structure matters or whether this is just richer, more granular feedback.
   - A needed control is MC-style feedback given the same user goal and API information. Also needed is per-turn feedback without the emotion and success forecasts.
   - The "long-term planning" claim is never tested directly. There are no analyses of planning-specific behaviour, such as early assumptions or clarification strategies.
2. **The baselines may not be a fair comparison.**
   - The feedbacker in RPO receives information that the baselines (APO and GPO) apparently do not. That information includes the user goal and the intermediate API calls, and for the medical task, expert feedback. Under the paper's own ablation ("basic" vs "full"), this information is what separates the methods.
   - "MC-style (TextGrad)" is a re-implementation of the paper's own MC feedbacker, not the actual TextGrad algorithm.
   - The binary-label APO adaptation and the GPO setup in the multi-turn setting are described only briefly.
   - Other closely related multi-turn or agent prompt optimisers are not compared. Examples are OPRO, Reflexion-style memory distilled into a prompt, ProTeGi/TextGrad proper, and Agent-Pro. A simple strong baseline is also missing: give the rewriter the full failure trajectories and the score history with no TD structure.
   - It is not stated how many candidates, epochs and LLM calls each baseline gets. Equal optimisation budget is essential here. RPO generates 2 candidates per epoch and picks by validation score. If baselines get a different budget or a different selection protocol, the comparison is not controlled.
   - The "+replay" variant is a separate, additional ingredient that gives most of the gain on Tables 1 and 2. For example, RPO-TD alone on SQL (0.408) is within about 0.02 of MC-style (0.388). The baselines are not given the same history access, which is unfair.
3. **Statistical rigour is limited.**
   - Tables 1 and 2 show single numbers without variances, seeds or confidence intervals. The Table 1 SQL results are on a sharded Spider subset whose size is not given in the main text. The SQL differences between methods are often a few points.
   - In Table 2, the gaps between APO, GPO, MC and RPO-TD are 0.01–0.02. That is likely within noise (Figure 4 uses 100 dialogues per evaluation).
   - Because the best of 2 candidates is selected on a validation score, selection bias and overfitting to the validation or evaluation split are possible. It is unclear whether the final test numbers use data separate from selection.
   - Table 1 has a few non-monotone entries, such as APO on GPT (0.374, below baseline). These suggest high variance and are not discussed.
4. **MultiWOZ results rely on a simulated user and a rule-based evaluator, and the evidence for generalisation is limited.**
   - The simulated user is an LLM. The same family of models may serve as feedbacker, user and system, so the optimised prompt may exploit simulator quirks. There is no human-user evaluation of the optimised dialogue systems, despite the stated aim of handling real users.
   - The optimised prompts are only evaluated in the same simulator and domain set used for optimisation.
   - There is no test of transfer across domains, of transfer to held-out user goals under a different simulator, or of whether a prompt optimised with one backbone transfers to another.
   - "Generalises across different LLM-based agents" is only partly shown. In Table 2, the system is always FnCTOD with GPT-4o mini, and only the meta-prompting LLM varies. The "agents" in the generalisation claim are the SQL system models.
   - In general, the claim of improvement "across LLMs" in Table 2 is about the optimiser's LLM and not about the agent. The text conflates these in places (Section 5.1, "System agents as different LLMs" vs "Prompt optimisation with different LLMs").
5. **Medical QA evaluation is weak.**
   - The evaluation is 90 pairs per domain from 3 experts, with a single combined preference of safety, professionalism and fluency. There is no inter-annotator agreement, no per-criterion breakdown, and no significance test.
   - The comparison to Huatuo-GPT-II mixes a prompt-engineered GPT-4o mini with a 7B model, so the win rate mainly reflects the stronger base model. It does not support the claim that prompt optimisation matches fine-tuning.
   - Optimisation uses an expert's feedback on 10 interactions per epoch. The evaluating experts may be the same people, or share the same preferences. This is not clarified.
   - In TCM the improvements over the plain GPT-4o mini system are modest. For example, 42.4% win against 30.3% tie and 27.3% loss, with ~33 pairs, is not significant. Safety is the key criterion in medical use, and optimised prompts may add confident medical advice. This is not examined.
   - The medical QA task is arguably not a "long-term planning" task, because single-turn and multi-turn settings are both used.
6. **The efficiency claim is not measured.** The paper argues that RPO lowers inference cost and latency relative to self-refine pipelines (Reflexion and similar). The paper reports no cost, token or latency numbers for optimisation or inference. The optimisation itself (feedbacker LLM per turn, 2 candidates, validation evaluations, replay with growing context) is expensive. There is also no empirical comparison to self-refine methods at inference time.
7. **Replay and context scaling.** The replay rewriter sees all previous prompt-feedback pairs. The context grows with epochs, and the paper does not discuss how this scales or whether older entries help. Number of epochs, prompt lengths, and the evolution of the optimised prompt (e.g. whether prompts grow long and overfit to task-specific rules) are not analysed. Only one example prompt (Figures 11–12) is shown. A qualitative analysis of what the optimiser learns would help show whether it finds general "planning" strategies or task-specific rules, such as API-argument formatting for FnCTOD.
8. **Presentation and claims.**
   - Several claims are stronger than the evidence: "robust", "stable, practical, efficient", "lower-variance", "warrants future research in RL-inspired parameter-free optimisation".
   - The Related Work argument from Petrov et al. (2024) is used post hoc to explain the TCM results. Other explanations are possible (e.g. data quality, language, evaluation noise).
   - The inline Mean ∆% in Table 1 includes OracleFull. The "+54.2%" figure averages relative gains over a low baseline. Models with low baselines (Llama-8B, Llama-4) dominate the relative numbers.
   - The code is not yet released.

## Questions
1. What are the exact optimisation budgets (epochs, candidates per epoch, LLM calls, tokens) for each method? Were baselines given the same budget and the same user-goal and API information as RPO's feedbacker?
2. Can you provide an MC-style feedbacker given the same inputs (user goal, API calls), and a replay-enabled version of APO, GPO and MC? This would isolate whether TD feedback itself matters.
3. What are the standard deviations or confidence intervals for Tables 1 and 2, across seeds? How large are the SQL train, validation and test splits? Is the test set disjoint from the data used to select candidates?
4. How do the optimised prompts transfer across models (optimise on GPT-4o mini, deploy on Llama), across simulators, and to real users?
5. Is there evidence that the optimised prompts improve long-term planning specifically (for example, fewer wrong early assumptions, or more clarifying questions in the SQL task), as opposed to patching recurring errors?
6. How do the costs of optimisation and of inference compare with Reflexion-style self-refine and with fine-tuning (LoRA, DPO) approaches that you state are impractical? Is there a head-to-head comparison?
7. For medical QA, what are the inter-annotator agreement, per-criterion results, and the overlap between feedback experts and evaluation experts? Were any safety regressions observed?

## Ratings
- **Soundness: 2** (the gains are plausible, but the baselines are not controlled, variance is not reported, and the TD claim is not isolated.)
- **Presentation: 3** (it is clearly written. The RL analogy is over-claimed, and the generalisation results are confusingly described.)
- **Contribution: 2** (it is an incremental combination of existing feedback-rewrite prompt optimisation with per-turn feedback and history, evaluated mostly in simulation.)

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

Justification: the problem is useful and the results are directionally positive. The conceptual novelty is modest, the RL/TD framing is not substantiated by the method or by a controlled comparison, and the baselines, statistics, and efficiency claims are not rigorous enough yet. Controlled baselines with equal information and budget, variance estimates, and a test with real users or a different simulator would move this toward acceptance.
