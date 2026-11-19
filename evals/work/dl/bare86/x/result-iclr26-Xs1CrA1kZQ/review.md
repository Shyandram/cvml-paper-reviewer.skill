# Review: Goal-Guided Efficient Exploration via Large Language Model in RL (SGRL)

Note: figures were not available. Judgments about curves rest on captions and text only.

## Summary
The paper proposes SGRL, an LLM-enhanced RL method for Crafter and Craftax-Classic. It has two LLM-derived parts:
1. A **structured goal planner**. An LLM (DeepSeek-R1) writes a reusable Python function that maps the text observation to a set of candidate goals with normalized priority weights. The weights are adjusted by the LLM during training according to unlocked achievements.
2. A **goal-conditioned action pruner**. An LLM (DeepSeek-V3) lists the actions related to each goal, and these are cached in a goal-to-mask bank. Masks are OR-ed over the candidate goals and applied to the PPO logits. The mask is relaxed with a three-phase cosine-annealed Bernoulli schedule.

The PPO policy takes the state concatenated with a MiniLM embedding of the goal set. On Craftax-Classic at 5M steps, SGRL reaches a score of 33.8% against 28.5% for AdaRefiner, 28.4% for ELLM and 24.8% for PPO. It also reaches achievement depth 8 and a much higher SPS than ELLM and AdaRefiner. Ablations at 10M steps support the pruner and the priority weights.

## Strengths
- The idea of replacing per-step LLM queries with an LLM-authored, reusable goal-generating program plus a cached goal-to-mask bank is practical. It greatly reduces LLM cost: 18.5 vs 0.3–0.9 (×10²) SPS.
- The motivation is clear. A preliminary CodeGoal study identifies the weaknesses (slow deep achievements, late benefit) that the two components are meant to address.
- The ablation covers the pruner, the static vs annealed mask, and the priority weights. Five seeds are used. The goal-priority heatmap offers some interpretability.
- The soft/annealed masking is a reasonable way to tolerate LLM errors.
- Appendices give prompts and implementation details.

## Weaknesses
1. **Limited novelty relative to prior art.** LLM-generated code (Eureka-style) and LLM-based action masking or affordance pruning are both established. The goal function is effectively an LLM-written scripted curriculum or heuristic over Crafter's known tech tree. The contribution is mostly a combination of these.
2. **Heavy domain knowledge and possible leakage.** The goal function is generated from the task rules and code examples, then iteratively refined with feedback on unlocked achievements. The planner reads textual state (inventory, status) and uses knowledge of the Crafter achievement hierarchy. It is unclear how much human prompt engineering and iteration went into this, or how many LLM runs were discarded. There is no variance across LLM-generation runs. DeepSeek-R1 may also have memorized Crafter's tech tree. There is a large gap between this effectively hand-specified structure and the baselines, so "LLM prior knowledge" is not cleanly separated from "human-engineered curriculum".
3. **Weak and possibly unfairly constrained baselines.**
   - ELLM and AdaRefiner are queried only every 200 steps "under cost constraints", which handicaps them.
   - On Crafter, their numbers are copied from the original papers, which use different settings, so the Crafter comparison is not controlled.
   - The PPO baseline has no goal or text input and no action masking. There is no control that gives plain PPO or ELLM the same action-pruning mask, or a hand-written goal/mask heuristic. These would isolate the LLM's contribution.
   - There is no comparison with other Crafter or Craftax-Classic methods. These include stronger RL (DreamerV3, PPO-RNN, curiosity/ICM/RND, novelty-based), SPRING and other LLM-agent methods, and Craftax-Classic baselines.
4. **Modest gains and statistical support.**
   - On Craftax-Classic at 5M, SGRL's score is 33.8 ± 1.5 against 28.4–28.5 for the baselines, with a negligible reward difference (13.0 vs 12.2–12.3). The paper says reward shows no significant advantage and explains this away with a speculative argument that is not tested.
   - The ablation is run at 10M steps, but the baselines are reproduced only up to 5M. Longer-horizon PPO comparisons are missing, so the "faster Collect Diamond" claim is unsupported at equal budgets.
   - The reported "unlocks diamond after 3.7M steps" claim rests on the curves, which I could not inspect.
   - Differences in the ablation (e.g. 43.9 vs 40.0) are small relative to the standard deviations over five seeds. No significance tests are given.
5. **Inconsistent or unclear evaluation.** The text says Figure 5 shows results "on Crafter" but the caption and the table say Craftax-Classic. Compute differs between the Crafter (A100) and Craftax (4090) experiments. The "geometric mean score" formula in A.2 is nonstandard (the Crafter score uses log(1+ϱ) with ϱ in percent). Achievement depth is a coarse metric, and SGRL scoring depth 8 is a binary effect.
6. **Efficiency claims are overstated.** SGRL is 7× slower than PPO (18.5 vs 135.3). The cost of the code-generation and priority-update iterations, the number of LLM calls, and the token counts are never reported, despite "minimal LLM invocation" being a headline claim. Whether priority-weight updates need online LLM calls is unclear, and total cost vs ELLM is not quantified.
7. **Generality is not demonstrated.** Evaluation is on a single environment family (Crafter and its JAX port), with essentially one environment in two implementations. There are no other open-world or text-conditioned domains (e.g. Minecraft, MiniHack, NetHack, ALFWorld), and no study of the method's sensitivity to the LLM (R1/V3 only), prompts, or hyperparameters. Craftax-Classic is nearly saturated for some metrics in the literature. The claim of addressing "real-world open environments" is far from what is shown.
8. **Method specification and soundness issues.**
   - Eq. 5 multiplies logits by the mask and also subtracts C, which is odd. It is non-standard because zeroing logits is not masking, and it may produce distribution artifacts.
   - Annealing ξ from 1 → 0 → 1 means the mask is fully relaxed by 0.8T onward (Eq. 3–4), i.e. the final policy is unmasked at evaluation time, while the paper frames SGRL as constraining the agent. The ξ semantics in Eq. 4 (ξ=1 makes every masked action sampled with probability 1) conflict with the text ("small probability"). This is confusing.
   - The PPO ratio is computed under a stochastically relaxed mask, which changes the support between rollouts and updates.
   - The goal embedding uses a weighted set of goals, but how the weights are encoded is unspecified. Equal weighting vs weighting matters for the "w/o Priority" ablation, which is the key contribution.
   - The goal planner is given the agent's unlocked achievements, which is privileged feedback.
9. **Presentation.** Many claims are asserted from the curves ("demonstrates farsighted objectives"), such as the plateauing of Wake Up and Place Plant, with weak causal evidence. Related-work claims (e.g. that other methods are "of low practical utility") are sweeping. Main results are mostly in the appendix.

## Questions
1. How many iterations, LLM runs and human interventions were needed to produce the final goal function? How variable are results across independent LLM generations (seeds of code generation)?
2. What is the total LLM cost (calls, tokens, dollars) of SGRL vs ELLM and AdaRefiner? How are priorities updated, and how often?
3. What happens if PPO (or ELLM/AdaRefiner) is given the same pruning mask, or a hand-written goal list with the same priorities? How does the method perform with a weaker/open LLM or with prompts lacking the tech-tree description?
4. Why is the mask fully relaxed after 0.8T? Is evaluation done with the mask on or off? Do the ablation conclusions hold when ξ is varied?
5. Can you provide 10M-step (or 1B-step, which Craftax makes feasible) results for PPO and the other baselines, plus stronger non-LLM baselines (e.g. PPO-RNN, DreamerV3)?
6. Can you provide significance tests, and clarify the "Figure 5 on Crafter" inconsistency?
7. Does the approach transfer to a different environment, so that the claim is not specific to Crafter?

## Ratings
- **Soundness:** 2
- **Presentation:** 2
- **Contribution:** 2
- **Rating:** 4 (marginally below the acceptance threshold)
- **Confidence:** 4
