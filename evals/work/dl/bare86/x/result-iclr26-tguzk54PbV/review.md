# Review: Adversarial Reinforcement Learning for LLM Agent Safety (ARLAS)

Note: figures are not available. I judged the heatmaps from the numbers in the extracted text and from the captions.

## Summary
The paper proposes ARLAS, which co-trains an attacker LLM and a web agent LLM as a two-player zero-sum game. The attacker writes indirect prompt injections that are appended to a random line of the observation. The agent is rewarded for finishing the task without leaking synthetic private user data. The pipeline is SFT warm-up on filtered teacher episodes, then multi-turn GRPO for both players. The agent trains against a uniformly sampled population of all earlier attacker checkpoints, to avoid cyclic dynamics. Experiments use Gemma3-12B and Qwen3-14B on BrowserGym, with transfer tested on AgentDojo. Baselines are SPAG, a frozen-attacker automated red-teaming method (ART), ARLAS without population-based learning (PBL), and ARLAS without adversarial learning. On BrowserGym, the ARLAS agent has the lowest average ASR against the pool of attackers, and ARLAS also has the strongest attacker. On AgentDojo the gains are small. An embedding-based analysis shows increasing diversity of attacks.

## Strengths
- The topic matters. Learned, co-evolving attackers are better motivated than hand-written templates or fixed red-team sets.
- The recipe is clean: SFT warm-up, GRPO for both players, and a population of past attackers for the agent. The reason for PBL is explained clearly.
- The cross-play evaluation in Fig. 3 and Fig. 4 is more informative than evaluating against one fixed attacker. It also shows the attacker and agent improving over training.
- The ablations (w/o PBL, w/o AL) isolate the contributions, and there are three seeds with standard errors. A second base model is included.
- Transfer to AgentDojo is an out-of-distribution check, and the paper reports honestly that the gain is small.

## Weaknesses
1. **The threat model and the evaluation are narrow and mostly in-distribution.**
   - The only harm is string-matching leakage of synthetic user data into tool parameters ("any subset" of the private information).
   - The attacker, the training attacks and the main evaluation attacks all come from the same generator family, with the same objective, insertion mechanism and prompts.
   - The headline Fig. 4 numbers are agents against attackers trained in this same framework. The ARLAS attacker is by construction the one best matched to the ARLAS agent.
   - The "average over attackers" row is dominated by the ARLAS attacker. The attackers of SPAG, ART and the other baselines are weak: ASR is 6–13% for every agent against them.
   - There is no evaluation against independent attacks, such as static injection suites, AgentDojo's own named attacks, adaptive human red-teaming, or GCG-style optimization.
   - There is no comparison with other defenses, such as instruction hierarchy, StruQ/SecAlign, spotlighting, or prompt-based or detector-based defenses.
   - The 3-seed standard errors are computed on a fixed attacker and a fixed eval set. They do not obviously capture variance from training.
2. **The AgentDojo evidence is weak.**
   - Gemma3-12B ASR goes from 6.3 to 5.4 and TSR from 24.4 to 25.8. For Qwen3-14B, ASR goes from 1.6 to 1.4 and TSR from 30.2 to 31.2.
   - These differences are about one point and probably not meaningful. SPAG, which has no population, matches ARLAS exactly (5.4 ASR, 26.2 TSR).
   - The base ASR is already very low, so there is little headroom. The claim of "effective generalization to the unseen AgentDojo environment" is therefore an overstatement.
   - The base-model rows have no variance, while the other rows have tiny errors (±0.0, ±0.1). It is unclear whether seeds vary the training or only the evaluation sampling.
   - The paper does not say which AgentDojo attack was used, whether the attack goal matches the training objective, or how ASR is defined.
   - A base ASR of about 6% is much lower than typical AgentDojo numbers under standard attacks. This suggests a weak attack configuration.
3. **The task success rate trade-off is not as favorable as claimed.**
   - In Fig. 4 (right), ARLAS TSR against the ARLAS attacker is 35%, compared with 48–52% for the non-adversarial variants. Part of this is unavoidable, because the attacker can sabotage the task, but it weakens "maintaining high task completion".
   - The no-attack gain (base 38 to ARLAS 56) comes mostly from SFT/RL on BrowserGym task data (ARLAS w/o AL gets 59). It should not be read as a benefit of the safety method.
   - Absolute ASR under the ARLAS attacker remains high (34–41% for the final agent).
4. **Attack diversity is weakly supported.**
   - Diversity is measured as mean pairwise cosine distance in Qwen3-embedding space, on a cumulative set, with a y-axis that spans only about 0.85 to 1.0.
   - The cumulative set mechanically grows in coverage because it unions earlier checkpoints. An increase of APD is therefore not clear evidence that the attacker becomes more diverse, rather than just different.
   - Single-checkpoint diversity is not reported.
   - Diversity is not compared with the baselines (ART, SPAG, hand-crafted templates), although the central claim is that ARLAS improves over them.
   - There is no semantic or strategy-level analysis, such as clustering by attack type. Embedding distance can reflect length or phrasing, not different exploits.
   - The attacker is rewarded only for success and has no diversity term. It could collapse to a few effective attacks with varied surface form, and the metric cannot tell the difference.
   - The qualitative UMAP views are shown for only one or two tasks.
5. **Over-refusal and generality are untested.**
   - The agent may learn simply to avoid putting user-info strings into tool calls. That would also hurt tasks that legitimately need the private data, and the paper does not test such tasks.
   - There is no evidence that robustness extends to other harms, such as unauthorized tool calls, even though the paper says the method "can be easily extended".
6. **The baselines are weak or insufficiently specified.**
   - SPAG was adapted (offline RL objective, iterative learning), and ART uses a frozen attacker and critic with unspecified budgets. The tuning effort each baseline received relative to ARLAS is unclear.
   - The ART and w/o PBL attackers are very weak (ASR 6–13%). Yet in Fig. 3 the ARLAS RL iter 5 and iter 10 attackers, which are the same kind of iterative attackers, already reach 30–45% ASR on the same agents. This may point to an implementation or hyperparameter issue in the baselines, so the PBL benefit may be overstated.
   - The cleanest result is ARLAS vs. w/o PBL, at 12 vs. 15 average ASR in Fig. 4. That is a modest effect, on one base model.
   - There is no sensitivity analysis on population size or sampling scheme, and the extra compute from training against all checkpoints is not discussed.
   - The paper gives no direct measurement of cycling in the iterative baseline, so the motivation for PBL is not tested.
7. **Method novelty is limited.** The ingredients are known: LLM self-play (SPAG), population-based/fictitious play, GRPO, and learned attacker LLMs for prompt injection. The contribution is mainly the application and the combination. There is no theoretical argument for why uniform past-checkpoint sampling avoids cycling.
8. **Reward and setup details.**
   - The attacker gets -1 on both task success and task failure, so it has no incentive to disrupt the task rather than cause a leak. The agent gets -1 for both a leak and a task failure, so safe-but-incomplete behavior is penalized like a leak.
   - Task failure gives -1 to both players, so the game is not strictly zero-sum as claimed.
   - The imitation data comes from larger models of the same family, so the student may inherit teacher attack patterns.
   - Training uses LoRA, short horizons (L=5), 128 tasks per iteration and 15 iterations. These are small.
9. **Reproducibility.** The paper does not mention a code release. It gives no number of RL steps per iteration, no evaluation set sizes, and no count of BrowserGym test tasks. Only 12–14B models are used, so the claim of generality to "agents" is limited (acknowledged by the authors).
10. **Presentation.** There are typos ("focuese", "seciton"). The agent's developer prompt in the appendix is mislabeled "for the attacker". Eq. 2 has a stray minus sign on the clip term and inconsistent index notation. Main results are shown only as dense numeric heatmaps.

## Questions
1. How does the ARLAS agent do against independent, non-ARLAS attacks, such as the AgentDojo built-in attacks (state the exact one), static injection corpora, or adaptive attacks computed against the final agent?
2. What is the diversity of ART, SPAG and ARLAS attackers on the same metric, and what is the within-checkpoint (non-cumulative) APD? Can you show clustering by attack strategy?
3. Is there evidence of cycling for the iterative baseline, such as an agent's ASR against old attackers over training? What is the effect of population size and sampling strategy, and what is the extra compute?
4. Does the defended agent over-refuse on tasks that legitimately need the private data? What is the TSR on such tasks?
5. How were the baselines tuned, and why are the ART and w/o PBL attackers so weak when intermediate ARLAS attackers are much stronger?
6. What do the seeds vary on AgentDojo? Given the sub-1-point gains, are the ARLAS vs. base differences statistically significant?
7. Does the method help on other harms (e.g., unauthorized tool use), and on larger models or a stronger agent setting?

## Scores
- Soundness: 2
- Presentation: 3
- Contribution: 2
- Rating: 4
- Confidence: 4

Overall: a reasonable and timely idea with a sensible training recipe. The evidence is dominated by in-framework cross-play and a narrow leakage-only threat model. The one external benchmark shows gains of about one point that SPAG matches, and the diversity claim is not tested against baselines. I lean toward rejecting at this stage. Independent attacks, stronger baselines, comparisons with other defenses and a proper diversity analysis would make it a much stronger paper.
