# Review: "LLM-based Automated Theorem Proving Hinges on Scalable Synthetic Data Generation" (ICLR 2026 submission)

Figures were not available. I judged them from captions and text only. This matters most for the search-depth and beam-decay dynamics (Fig. 3/5).

## Summary
The paper targets stepwise (tree-search) LLM theorem proving in Lean 4. It makes two proposals.

1. **Proof-state exploration for data synthesis.**
   - Starting from STP seed problems, an existing policy (BFS-Prover) explores the proof-state space with a large beam (B=32).
   - Tactic operators are chosen by constrained decoding over a curated set of 60 common tactics. This set comes from nucleus filtering (p=0.999) of tactic frequencies in STP. The policy then completes the premises.
   - Exploration is pruned heuristically: keep αB branches, of which β are top-probability and the rest random. The budget shrinks by γ=0.9 when a distinct proof is found.
   - The result is about 20M proof transitions (synthetic plus Mathlib). Qwen2.5-Math-7B is fine-tuned on them for one epoch, with no expert iteration.
2. **Adaptive beam size.** The beam decays linearly with the expansion index, from Bmax to Bmin, with a decay-rate hyperparameter λ.

At Pass@1 with K=1 and E=600, the model reaches 60.74% on MiniF2F-test and 21.18% on ProofNet-test. These compare with BFS-Prover at 55.5–56.6% and 12–13% on the same benchmarks, and InternLM2.5-StepProver at 47.3% and 19.9%. The authors also release DoBeVi, a Lean interaction and visualization tool.

## Strengths
- The problem is well motivated: data scarcity in Lean, and the cost of expert iteration combined with tree search. A one-pass synthesis procedure without EI is practically appealing for low-resource groups.
- The idea of forcing tactic-level diversity across intermediate states, by decoupling tactic choice from premise completion, is simple and reasonable. Training on intermediate states of a search distribution rather than only on successful proofs is a sensible way to reduce train/test distribution mismatch.
- The empirical numbers are competitive for a 7B stepwise prover at small budget. Fixed-beam results are reported with ± across runs. Several beam sizes are shown for the proposed model.
- The observation that the optimal fixed beam size differs by benchmark (8 on MiniF2F, 32 on ProofNet) is interesting, and the cheap beam-decay schedule gets some of the benefit of tuning without a grid.
- Code and checkpoint are said to be released. The tool contribution (DoBeVi) and the honest "unsuccessful attempts" and limitations sections are welcome.

## Weaknesses
1. **The central claim is not isolated by any ablation.**
   - The title and abstract attribute the gains to scalable synthetic data. There is no ablation of the data pipeline.
   - Missing controls include: (a) the same base model fine-tuned on STP/BFS-Prover-style data or Mathlib only, with the same transition count; (b) exploration without the 60-tactic constrained decoding (plain beam); (c) without pruning (α, β, γ); (d) varying tactic-set size; (e) varying data size.
   - There is no data-scaling curve, so "scalable" and "hinges on" are unsupported. The results show only that the final system beats two baselines, not why.
2. **Confounded comparison with baselines.**
   - The policy used to generate the data is BFS-Prover itself, and the seeds are STP data. The final model is therefore a distillation or extension of a baseline plus additional data and a different search implementation.
   - BFS-Prover at B=2 is compared with its published setup. Its stronger published results (with a much larger budget and EI) are not shown, and the budget definitions differ. For the proposed model, the best fixed beam gets 8–32 samples per expansion, versus 2 for BFS-Prover. The "same budget" claim (K×B×E) therefore hides a roughly 4–16x difference in tactic samples per step.
   - Several baselines (the asterisked ProofNet numbers) were re-run with the authors' own search implementation and extra search tricks (early termination, timeout/restart handling). Their implementation quality and tuning are uncertain.
   - Compute spent on synthesis (a 32-wide exploration over the full seed set) is never reported or compared. The claim of lower cost than EI is asserted, not measured.
3. **Adaptive beam hyperparameters appear tuned on the test sets.**
   - Bmax, Bmin and λ are set separately per benchmark (16/4/15 for MiniF2F; 48/24/2 for ProofNet). No validation split is described.
   - The gain of adaptive over the best fixed beam is small: 60.74±0.88 vs 59.51±0.79 on MiniF2F, and 21.18±0.55 vs 20.75±0.94 on ProofNet. These are within roughly one to two standard deviations.
   - The claim of improving "without searching for the best beam size" is contradicted by the per-benchmark tuning. There is no sensitivity analysis for λ, Bmin or Bmax, and no comparison with simple alternatives such as a fixed, tuned beam of 12.
   - The "exploration vs. exploitation" framing is not tested. The top-p dynamic beam variant tried in A.5 is dismissed without numbers.
4. **Statistical rigor and gap size.**
   - The ProofNet improvement over InternLM2.5-StepProver (19.89 vs 20.75–21.18) is within noise.
   - Seed counts are not stated, and the ± is not defined.
   - MiniF2F-test has only 244 problems, so 1 problem is about 0.4%.
   - The "SOTA among tree search methods" claim omits recent stepwise provers and value-guided or MCTS methods. The comparison set is two models.
   - Whole-proof provers are far stronger (DeepSeek-Prover-V2, Kimina, Goedel). The paper dismisses them with no comparable-budget results, so the practical significance of the 60% number is limited.
5. **Contamination and leakage concerns.**
   - Decontamination uses BLEU overlap only. Lean statements are easily paraphrased, and the seeds come from Lean Workbook/STP, which are known to overlap MiniF2F/ProofNet-style problems. Mathlib also contains related material (ProofNet is derived from undergraduate texts).
   - There is no threshold, no counts removed, and no semantic or goal-level check.
   - The explanation that the optimal beam differs "primarily due to training distribution" is speculative and untested.
6. **Method design is heuristic, and some claims are unsupported.**
   - The nucleus filter over 173 tactics to get 60 is a frequency filter, and it removes rare tactics. This arguably contradicts the stated goal of exploring tactics the model rarely uses.
   - The "novel" label overstates the contribution. The algorithm is beam-search exploration with random pruning, and the "diversity" is never measured (no tactic or state diversity statistics, no comparison with data from standard search).
   - The pruning keeps random branches, which can produce valid but useless states. There is no analysis of data quality, such as the proportion of states that lie on a proof path.
   - Algorithm 1 adds all valid next states to the queue, and the transition is also stored for invalid ones, until post-hoc filtering. The inconsistency between the algorithm and the text, and the unspecified `budget`, make reproduction hard.
   - Mixing synthetic data with Mathlib data changes the claim: it is not fully "synthetic".
7. **Weak analysis and presentation.**
   - Section 4.3 is largely narrative. There are claims like "beam size is sometimes as important as the policy model" with no controlled experiment. The scoring-function discussion ("significant issues") is supported by "nearly indistinguishable" results with no numbers.
   - The Related Work and introduction are loosely written, with imprecise terms ("proof states aka proof terms"). The RL framing in Section 2 is hand-wavy.
   - The limitations section admits that the method cannot produce problems harder than the seeds. This undercuts the title's scaling claim.

## Questions
1. What happens if you train the same base model on (i) plain tree-search data from the same BFS-Prover policy, with matched transition count, and (ii) STP data only? How much of the improvement comes from the data and how much from the beam choice and search tricks?
2. How many GPU-hours does the synthesis step take, compared to one EI iteration on the same seed set? What was the total evaluation compute per theorem, including timeouts and restarts?
3. How were Bmax, Bmin and λ chosen? Was a held-out validation set used? Please show a sensitivity grid. What is the result of adaptive beam transferred across benchmarks (MiniF2F parameters on ProofNet and vice versa)?
4. How many random seeds were used for the ± values? Are the improvements significant under a paired test?
5. Could you report diversity metrics, such as unique (state, tactic) pairs and tactic entropy, for the synthesized data versus standard search data? Please also report a scaling curve (e.g., 2M/5M/10M/20M transitions).
6. What is the effect of the 60-tactic restriction on tactics such as `aesop` or `nlinarith`, which may be needed for ProofNet?
7. How does BLEU decontamination compare with a goal-level exact or normalized match? How many examples were removed?
8. How does the model compare to BFS-Prover at its own published budget and beam, and to other recent tree-search provers, under a matched total compute budget?

## Ratings
- **Soundness:** 2/4. The headline results may be real, but attribution is unsupported, the hyperparameters were likely tuned on the test set, and the differences are small.
- **Presentation:** 2/4. The paper is readable, but the algorithm is under-specified and the discussion is narrative.
- **Contribution:** 2/4. The ideas are incremental (a heuristic data pipeline plus a linear beam schedule), and there is a tool release.

**Rating: 4 (marginally below the acceptance threshold).**

**Confidence: 4.** I know this area. I could not inspect the figures.
