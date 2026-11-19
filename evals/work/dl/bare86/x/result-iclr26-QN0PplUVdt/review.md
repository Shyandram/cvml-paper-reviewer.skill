# Review: LOOP: A Plug-and-Play Neuro-Symbolic Framework for Enhancing Planning in Autonomous Systems

## Summary
The paper proposes LOOP, a "neuro-symbolic" planning framework with 13 components in four modules. The components are a GAT-based GNN over task embeddings, confidence-based strategy selection, hierarchical decomposition, LLM-driven PDDL generation and refinement, a 12-agent LLM validator ensemble, a causal memory built from state-transition traces, and cross-domain pattern transfer. GPT-4 produces PDDL, and Fast Downward solves it. On six IPC domains the paper reports 85.8% success, against 55.0% for LLM+P, 19.2% for LLM-as-Planner and 3.3% for Tree-of-Thoughts. An ablation (Table 2) and Wilcoxon tests (Table 3) are provided. No figures were available; I judge Fig. 1 and 2 from captions and text only.

## Strengths
- The problem is relevant: LLM-generated PDDL with iterative symbolic feedback is a sensible direction, and keeping a classical planner in the loop preserves plan validity.
- Ablations at the level of component groups are attempted, and failure modes of one-shot translation (missing preconditions, malformed PDDL) are described.
- Sub-optimal-but-valid plans are reported in parentheses, and the compute cost (4.8x) is acknowledged as a limitation.

## Weaknesses
1. **The experimental protocol is under-specified, so the results are not interpretable.** The paper does not state the number of problem instances per domain, how instances were generated or selected, how the natural-language descriptions were obtained, or the seeds and number of runs. Success rates are all multiples of 5, which suggests about 20 instances per domain; at that size the confidence intervals are very wide. "Training examples" for the GNN and causal memory are mentioned, but the training data, the train/test split, and whether memory carries over between test problems are never described. If memory persists across test problems, ordering and leakage matter.
2. **Internal numerical inconsistencies.**
   - The full system is 85.8% in Table 1 but 82.1% in Table 2 ("averaged across domains").
   - The Discussion says Storage reaches 67%, whereas Table 1 gives 80%.
   - The plan-quality (optimality ratio) values are not defined per domain.
   - Table 2 lists the full system at 13 features, but the neural core (6) plus symbolic core (3) is 9, and the remaining features are unaccounted for.
   - The "No GNN Components" row (10 features) drops 3 features and "No Causal Components" (9 features) drops 4, with no mapping given.
3. **The statistical claims are incorrect.** Wilcoxon signed-rank on 6 paired domain scores has a minimum exact two-sided p of 0.031, so the reported p=0.016 implies a one-sided test that is not stated. "Confidence = 1 − p" (98.4%) is not a valid interpretation. The comparison against the strongest baseline, LOOP vs LLM+P, has p=0.078, which is not significant, yet the abstract and text describe significant outperformance of "the best baseline". Using domains as the units, with no per-instance tests, does not support the claim.
4. **Baseline fairness and strength.** All baselines were "recreated" by the authors, with no released prompts and no tuning details. LLM+P originally reported 90%+ on Blocksworld-like domains, yet here it gets 0% on Floortile and 10% on Rovers. It is unclear whether these failures reflect the method or a weak reimplementation. Missing baselines include LLM+P with VAL-driven or planner-error self-repair, LLM-Modulo, plain "GPT-4 writes PDDL, retry on planner error" (which is the core of the claimed contribution), and current reasoning models. Tree-of-Thoughts is not a planning-specific baseline, so 3.3% is uninformative. The "classical baseline" in Table 2 is not defined (what input does it get?). If it is given PDDL, Fast Downward solves these IPC problems almost always; if it is given NL, it is not a classical planner.
5. **The contribution of the neural components is not demonstrated.** Nothing shows that the GNN, causal memory or confidence score does anything beyond what an LLM-with-planner-feedback loop does. The pivotal ablation, "LLM + PDDL refinement loop only", is missing. The ablation removes groups of components, with no per-feature results despite the "13 features" framing. The GNN only embeds sentence-transformer vectors of task text; there is no explanation of what it is trained on, with what loss, or how its output influences PDDL generation. The text itself speaks of "single-pass inference for state representation and action guidance", but no mechanism for guidance is specified. The "causal learning" is essentially counting add/delete effects of actions from traces, which is effect extraction and does not involve causal inference. The claims of "learning in real time" and "bidirectional learning" are not tested (no learning curves, no comparison with and without memory over time).
6. **Claims of "guaranteed optimality" and "logical guarantees" are unsupported.** The LLM writes the PDDL, so correctness against the true domain is not guaranteed. A multi-agent LLM validator with a 0.7 consensus threshold gives no formal guarantee. Fast Downward's optimality is with respect to the generated model, not the intended task. How "success" is verified against the ground-truth domain (e.g. with VAL) is not stated.
7. **The worked example is invalid.** The Fig. 2 example is a plan the paper calls "optimal" for a 6-block task. Step 2, unstack(D,B), is applied while the hand still holds A (from step 1), and put-down(D) comes last even though C must be stacked on D at step 10. The plan is not executable. This is a serious red flag for the validity claims, since the example is the only qualitative evidence.
8. **Cost accounting and generalization.** The claim of "significantly lower overhead than ToT" is not supported by reported LLM calls or tokens. LOOP's 215s average against a 300s timeout suggests many runs near the limit, and 12 validator LLM agents per step seem expensive. The "cross-domain transfer" and "new domains" claims (Rovers/Satellite) have no experiment isolating transfer. IPC domains are small and well known, and LLMs likely have seen them; no held-out or obfuscated domain is used (cf. Mystery Blocksworld in PlanBench).
9. **Presentation and scholarship.** The paper uses the AAAI 2026 template and copyright notice. Citations are garbled (e.g. "Lexing 2018", "Sylvie 2020", "Peter 2023", "Michael 2024", "Paolo 2004" are author-name artifacts). Some are misattributed (LLMs cited to Vaswani et al.), and some statements are inaccurate (e.g. "74% on Game of 24" attributed to LLM+P). The related work is a list of one-line summaries. The tone is promotional ("finally be trusted with critical real-world applications", "million-dollar losses"), and the code is only claimed to exist. The equations are incomplete (the GAT equation, the Delta+ definition without Delta-).
10. **Novelty.** Iterative LLM-PDDL generation with planner/validator feedback and memory has been explored (LLM+P variants, LLM-Modulo, AdaPlanner, Plan-SOFAI, PDDL-refinement papers). The novelty is mostly in bundling many components, and the paper does not show which ones matter. The "plug-and-play" claim is not evaluated.

## Questions
- How many instances per domain, from which IPC tracks, and how were NL descriptions generated? Were the same instances used for GNN/memory training?
- What does the ablation "GPT-4 + PDDL generation + planner-error feedback loop" alone achieve, with and without validator agents?
- Reconcile 85.8 vs 82.1, and 80 vs 67 for Storage. Which numbers are correct?
- What is the Table 2 "Classical Baseline" and what is its input?
- How is success verified (VAL against the ground-truth domain)? How often is the LLM-generated domain semantically wrong yet solved?
- What exactly does the GNN output, and how does it condition PDDL generation? What are its training data and loss?
- Please provide LLM call counts and token costs per method. Is the Fig. 2 plan really what the system outputs?
- Why does LLM+P get 0% on Floortile and 10% on Rovers? Please provide the failure analysis and the prompts.

## Ratings
- Soundness: 1
- Presentation: 2
- Contribution: 2
- Rating: 2
- Confidence: 4

The venue fit is also poor (a planning-systems paper, mostly engineering), but the main grounds are the unreliable evaluation and unsupported claims.
