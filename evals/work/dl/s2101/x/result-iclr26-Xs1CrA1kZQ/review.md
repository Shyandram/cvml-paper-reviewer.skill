# Full Review: "Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning" (SGRL)

*Simulated panel review, target venue ICLR, mode `full`, literature check `strict` (cutoff 2025-09-24), confirmation skipped. Date: 2026-11-10. The decision is a simulation of how a careful panel might see this draft, not a prediction. The five reviewer passes were run one after another in a single shared model context, not by independent agents. Figures were not available (text extraction only), so figure-dependent claims are judged from captions and surrounding text, and Tables 4 and 5 were partly garbled by extraction.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning |
| Primary Discipline | Machine learning → reinforcement learning (exploration, goal-conditioned RL) |
| Secondary Discipline(s) | LLM agents and program synthesis; open-world game environments |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | PPO with LLM-written goal-generation code, LLM-derived goal-to-action masks, annealed stochastic mask relaxation |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle; scale status secondary; accepted share about 27% of submissions) |
| Venue-Specific Notes | none (ICLR: Soundness / Presentation / Contribution 1–4 plus a rating on {0,2,4,6,8,10}) |
| Paper Maturity | Submission-ready draft; some text/figure inconsistencies remain |
| Ethics-Relevant Content | None (game environments, no human data). No limitations or impact statement was found in the text. |

### Claimed Contributions (as stated by the authors; Sec. 1, last bullet list)
1. **C1**: SGRL, an LLM-enhanced RL method with a structured goal-generation function whose goal priority weights and goal-conditioned action constraints are adjusted dynamically, improving exploration "while maintaining low LLM invocation frequency and minimal input token consumption per call".
2. **C2**: A structured goal planner (LLM-written reusable goal function with priorities) plus a goal-conditioned action pruner (mask bank).
3. **C3**: Results on Crafter and Craftax-Classic claimed to "consistently outperform or match" LLM-enhanced RL baselines on success rate, score, reward and achievement depth.

### Paper memory (factual record shared with all reviewers)
- **Setup.** Benchmarks: Crafter (Sec. 5.1.1) and Craftax-Classic, a JAX re-implementation of the same game (App. A.1). The two are one game in two implementations. Compute: A100 for Crafter, RTX 4090 for Craftax-Classic (Sec. 5.1.2). Five seeds ("averaged over five random seeds", Sec. 5.1.2); the meaning of "±" is not stated. PPO hyperparameters follow SB3/Craftax defaults (Table 3, App. B.4). Crafter: 1 env, steps {1M, 5M}; Craftax-Classic: 256 envs, steps {5M, 10M}.
- **LLMs.** DeepSeek-R1 writes the goal code; DeepSeek-V3 selects goal-relevant actions (App. B.1). Decoding: temperature 0.5, top-p 1.0, max 100 tokens. Goal priorities are rewritten by the LLM every 2M steps (App. B.3.1). Text embedding: paraphrase-MiniLM-L6-v2 (App. B.2).
- **Baselines.** ELLM, AdaRefiner (DeepSeek-V3, "queried every 200 steps under training time and cost constraints", footnotes 1–2) and PPO. On Craftax-Classic they are reproduced only to 5M steps (App. D). On Crafter the ELLM/AdaRefiner numbers are copied from their papers (App. D). A human reference is included.
- **Headline numbers (Table 1, Craftax-Classic, 5M steps).** Score: SGRL 33.8 ± 1.5, AdaRefiner 28.5 ± 2.3, ELLM 28.4 ± 2.5, PPO 24.8 ± 5.7, Human 50.5 ± 6.8. Reward: 13.0 ± 0.3 / 12.3 ± 0.9 / 12.2 ± 1.0 / 11.9 ± 1.1 / 14.3 ± 2.3. Depth: 8 / 7 / 6 / 6 / 8. SPS (×10²): 18.5 / 0.3 / 0.9 / 135.3. Ablations (Table 2, 10M steps): SGRL 43.9 ± 2.6; w/ Static-Prun 38.5 ± 1.9; w/o Prun 40.0 ± 2.1; w/o Priority 35.3 ± 1.6.
- **Appendix adds.** Full prompts (App. B.3), PPO hyperparameters (Table 3), Crafter results (Table 4, Figs. 11–17), ablation table/figures (Table 5, Figs. 18–21), annealing-schedule comparison (App. F, Figs. 22–24).
- **Unverifiable.** All figures; Table 4 per-method assignment (extraction garbled); Table 5 row-to-variant assignment; the generated goal code itself (not shown).

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. The five reviewers read the redacted copy (identical to the original).

### Literature check (Phase 1.5; run after the reports were drafted)
Mode `strict`, cutoff 2025-09-24, search restricted to arXiv. 5 counted queries (3 claim: C1, C2, C3; 2 baseline), 2 refused for length (not counted), `scout` for Crafter, `coverage`, `similarity`, `novelty`, and 2 `verify` calls. Gaps left open: no prior work kept from 2021–2022; the first C1 query ("LLM generated goal code") returned software-engineering papers and was discarded as off-topic; nothing was run for LLM-generated reward code (Eureka, Text2Reward are already cited by the paper). Similarity: no text-overlap flag, no high-conceptual-overlap flag (top cosine 0.156). Claim-level profile: C1 medium, C2 medium, C3 high; "no central claim fully covered by prior work".

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Mirela Castellanos-Odum, senior researcher at an industrial research lab (Europe)
- **Seniority / Expertise**: senior area chair / RL exploration, LLM agents
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: starts from the reviewers' ratings, departs only for a verified, located issue

### Reviewer 1 (Methodology): Hyun-woo Pellegrini, mid-career faculty, vision/RL group at a large public research university (East Asia)
- **Expertise**: PPO-based exploration; evaluation protocols on Crafter/Craftax
- **Review Focus**: design, statistics, comparison fairness, reproducibility
- **Style**: insists on matched budgets and recomputes every delta

### Reviewer 2 (Domain): Okonkwo Brandvold, senior faculty, language-agent lab at a research university (Northern Europe)
- **Expertise**: LLM-guided RL, open-ended learning, Minecraft/Crafter agents
- **Review Focus**: literature, positioning, domain contribution
- **Style**: checks every novelty sentence against the cited abstract

### Reviewer 3 (Perspective): Salma Ivarsson-Tran, associate professor, cognitive/curriculum-learning and education-technology group (North America)
- **Expertise**: curriculum design, hierarchical task structure, human skill acquisition
- **Review Focus**: cross-disciplinary links, deployment, assumptions, impact
- **Style**: constructive and expansive; looks for what the idea could become

### Reviewer 4 (Generalist): Dmitri Haldane-Park, senior scientist, industrial ML lab (South Asia)
- **Expertise**: broad deep learning; typical program-committee member for ICLR
- **Review Focus**: contribution clarity, venue fit, presentation
- **Style**: reads once end to end and asks whether the community should see it

### Devil's Advocate: Noor Eichholtz, postdoctoral researcher in evaluation methodology, public research institute (Central Europe)
- **Expertise**: causal evaluation of agents, benchmark validity
- **Review Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous skeptic, never hostile

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reports

# Peer Review Report (Reviewer 1)

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Reviewer: Hyun-woo Pellegrini, Methodology Reviewer (vision/RL group, large public research university, East Asia; fictional persona)
## Expertise: PPO-based exploration; Crafter/Craftax evaluation; comparison fairness
## Date: 2026-11-10

### Summary
SGRL has an LLM write a Python goal-generating function for Crafter that returns a few prioritised goals from a text observation; the LLM later rewrites the priority numbers (every 2M steps), and a second LLM call maps each goal to a set of relevant actions, cached in a mask bank. The mask is relaxed stochastically by an annealed coefficient, goal embeddings are concatenated to the PPO state, and training runs on Crafter and Craftax-Classic. On Craftax-Classic at 5M steps the method scores 33.8 against 28.4–28.5 for ELLM/AdaRefiner and 24.8 for PPO (Table 1), with ablations at 10M steps (Table 2).

### Protocol sweep (grep over the full text, appendix included)
- Train/test split: not applicable in the usual sense; Crafter and Craftax-Classic are procedurally generated and agents are trained and evaluated in the same generator. No separate tuning split is stated.
- Selection: "SGRL w/ 3-Stage Cos" is highlighted as the best of four annealing schedules by Craftax-Classic performance (App. F.2: the three-stage cosine strategy "achieves the most effective balance"). Prompt iteration count and code selection are described only as "in just a few iterations and optimizations" (Sec. 3.1). Whether LLM-generated code was chosen using training returns is not stated after search.
- Seeds: five (Sec. 5.1.2). Seeds for the LLM-generated code (does each seed reuse one program?): not stated.

### Strengths
**S1: Simple, well-motivated interface.** Using LLM-written code as a reusable goal generator (Sec. 3.1, Fig. 2a) removes per-step LLM calls, which is a sensible answer to the cost problem of ELLM-style methods (Sec. 1). The preliminary CodeGoal study (Fig. 1) motivates the two additions.
**S2: Ablations isolate the two components.** Table 2 and Fig. 5–6 remove the pruner, the priorities, or the annealing, and App. F compares four annealing schedules. Priority removal shows the largest drop (43.9 to 35.3).
**S3: Better-than-usual disclosure.** Full prompts (App. B.3.1–B.3.2), PPO hyperparameters (Table 3), LLM versions and decoding parameters (App. B.1), five seeds with ± values, and hardware (Sec. 5.1.2) are given. The baselines' reduced query frequency is disclosed in footnotes 1–2.

### Weaknesses
**W1: Comparison is not matched in information, LLM or query budget (E4).** SGRL's prompt contains the full environment specification: items, collectable resources, craftable tools "with required materials, nearby crafting stations", the achievement list, a request for "a crafting dependency tree", and 17-action semantics (App. B.3.1–B.3.2). It is not stated that ELLM/AdaRefiner receive the same information. SGRL uses DeepSeek-R1 for planning; baselines use DeepSeek-V3 (App. B.1). The baselines are queried "every 200 steps" (footnotes 1–2), a reduced setting whose sensitivity is not shown, and are run only to 5M steps (App. D). The main result (Table 1) therefore cannot separate "structured code interface" from "more domain knowledge and a stronger LLM".
- *Fix:* give ELLM and AdaRefiner the same rule sheet; run SGRL with DeepSeek-V3 for planning; add a scripted-goal oracle (hand-written tech-tree curriculum + same masks) and an "unstructured LLM text goals + same mask" row. About 5 seeds × 3 new rows × 5M steps on Craftax-Classic (JAX, roughly 20–40 GPU-hours).
**W2: The baseline set is too small for the "state-of-the-art" wording (E4/E8).** Table 1 has two LLM methods and PPO. Achievement Distillation (Moon et al., 2023) is cited in the reference list and addressed to Crafter but not compared; no intrinsic-motivation or model-based baseline appears, and CodeGoal (Fig. 1) is absent from Table 1. Abstract: "compared to existing state-of-the-art methods".
- *Fix:* add at least one strong non-LLM Crafter method and CodeGoal to Table 1, or narrow the wording to "LLM-enhanced PPO baselines".
**W3: The efficiency claim is not measured (E8).** The contribution list says "while maintaining low LLM invocation frequency and minimal input token consumption per call", yet no LLM-call count, token count or dollar cost is given for SGRL or the baselines; Table 1 reports only SPS. SGRL's SPS is 18.5×10² against PPO's 135.3×10², i.e. 7.3× slower (derived), and the SPS comparison with ELLM/AdaRefiner mixes API latency with implementation.
- *Fix:* report calls, input/output tokens and cost per 1M steps for each method.
**W4: Crafter results are not comparable and the text says otherwise (E4/E6).** Sec. 5.1.2: "are based on the same configurations". App. D: "we report the original results of ELLM and AdaRefiner from their papers" for Crafter (Table 4).
- *Fix:* state the settings of the copied numbers or rerun them; remove the "same configurations" sentence for Crafter.
**W5: Statistical support is thin for the ablation claims (E5).** "±" is undefined (std or s.e.m.); no tests. Table 1 reward gains (13.0 vs 12.3, derived +0.7) lie inside the baselines' spread. Table 2: SGRL vs w/o Prun is 43.9 ± 2.6 vs 40.0 ± 2.1 (derived +3.9; reward 14.9 vs 14.7), yet Sec. 5.3.2 says SGRL "significantly outperforms all variants on most of the deeper achievements".
- *Fix:* define ±, add paired bootstrap or Welch tests over seeds, soften "significantly".
**W6: Core mechanism under-specified (E6/E8).** Number of candidate goals k, how weights enter the goal encoder (Sec. 3.3), number of LLM iterations, and whether the final program is shared by all seeds are not stated. The generated program is not shown, which is the main artifact of the method.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6/E4 | Sec. 5.1.2 vs App. D, Table 4 | "are based on the same configurations" vs "we report the original results of ELLM and AdaRefiner from their papers" | Crafter baseline numbers come from other papers, not the same configuration | Cross-referenced (two locations) | High | MAJOR | Correct text; give or rerun settings |
| ERR-2 | E6 | Sec. 5.3.2 vs Sec. 5.3.1, Fig. 5 caption | "for all 22 achievements on Crafter" | Fig. 5 and Table 2 are on Craftax-Classic | Cross-referenced | High | MINOR | Replace "Crafter" with "Craftax-Classic" |
| ERR-3 | E2/E6 | Eq. (3)–(4); App. F.1, Eq. (7) | "allows masked-out actions to be sampled with a small probability" (Eq. (4) uses Bernoulli(ξ(1 − M_j)) with ξ(0) = ½(1+cos 0) = 1) | By Eq. (4), ξ = 1 turns every masked action back on, so Eq. (3) starts with no masking, reaches full masking at 0.4T and none again at 0.8T. This conflicts with the description of ξ as gradually relaxing the pruner (App. F.1) | Evaluated Eq. (3) at t = 0, 0.4T, 0.8T | Medium (intent unclear) | MAJOR for reproducibility | State the intended direction and what is evaluated at test time |
| ERR-4 | E5 | Sec. 5.3.2 | "SGRL significantly outperforms all variants on most of the deeper achievements" | No test; Table 2 w/o Prun gap is +3.9 with std 2.1–2.6, reward +0.2 | Recomputed from Table 2 | High | MINOR | Test or soften |
| ERR-5 | E8 | Sec. 1 contributions; Sec. 3.1 | "low LLM invocation frequency and minimal input token consumption per call" | No call or token counts anywhere (searched) | Full-text search | High | MAJOR | Report counts and cost |

### Questions for Authors
1. Do ELLM/AdaRefiner receive the same environment description and crafting rules as SGRL's planner? A "yes, with the same LLM" answer would remove my main fairness concern; a "no" keeps it.
2. Table 5 (5M steps) lists a score of 34.2 ± 1.7 next to SGRL's 33.8 ± 1.5, but extraction does not let me assign it to a variant. If a pruner or priority ablation matches full SGRL at 5M, the Table 1 comparison does not show the components are needed at that budget (unverifiable here).
3. Is the pruner (mask) active at evaluation, and is the final policy trained with ξ = 1 for the last 20% of steps (Eq. 3)?
4. How many generated programs were tried, and were they selected by training return? How do results vary across independently generated programs?
5. What do the baselines score at 10M steps, matching Table 2?

### Missing References
(Domain Reviewer's job; none added here.)

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gain is real in direction but unmatched baselines and thin statistics |
| Clarity | 2 | Eq. (3)/(4) and several text/figure inconsistencies |
| Significance | 2 | One game, small budgets, gap to humans remains |
| Originality | 2 | Sensible but incremental combination |

### Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: baselines are weak and unmatched (W1, W2), and a single game is the whole evidence base.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Mask schedule unclear; priority/pruner effects partly within noise |
| Clarity & Presentation | 60 | Competent | Readable; several inconsistencies |
| Novelty & Originality | 52 | Developing/Competent | Known pieces recombined for a known game |
| Significance & Impact | 48 | Developing | Narrow benchmark, 5M-step regime |
| Experimental Validation | 42 | Developing | 2 LLM baselines + PPO; unmatched LLM/prompt/budget; copied Crafter numbers |
| Reproducibility | 50 | Developing | Prompts and PPO settings given; code, generated program and call counts missing |
| Ethical Compliance | 60 | Competent | Low stakes; no limitations section |

### Limitations Assessment
**Partially.** No limitations section; Sec. 1 only lists limitations of the preliminary CodeGoal.

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject)**: a plausible idea with a favorable but unmatched comparison on one game.

### Confidence
**4**: read in full including prompts; figures not viewable.

---

# Peer Review Report (Reviewer 2)

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Reviewer: Okonkwo Brandvold, Domain Reviewer (language-agent lab, research university, Northern Europe; fictional persona)
## Expertise: LLM-guided RL; open-ended learning; Crafter/Minecraft agents
## Date: 2026-11-10

### Summary
The paper positions itself between LLM-as-decision-maker methods and LLM goal generators such as ELLM and AdaRefiner, arguing the latter need frequent, costly LLM calls. SGRL replaces per-step LLM goal generation with an LLM-authored program that emits prioritised goals, adds an LLM-derived goal-to-action mask, and trains PPO on Crafter and Craftax-Classic. The related work (Sec. 4) is short and grouped into hierarchical RL, model-based RL and LLM-enhanced RL.

### Strengths
**S1: Clear niche.** The "code as goal generator, LLM off the critical path" framing (Sec. 1, Sec. 3.1) is a clear and practical angle on ELLM-style cost.
**S2: The CodeGoal experiment is an honest motivation.** Fig. 1 and the two stated limitations (Sec. 1) show what the first version could not do, and the paper then addresses them.
**S3: Appropriate benchmark choice for the claim.** Crafter/Craftax-Classic has a hierarchical achievement structure and a depth metric (App. A.1–A.2), which suits long-horizon exploration claims.

### Weaknesses
**W1: Related work omits LLM-guided Crafter agents and non-LLM Crafter methods (literature check).** Missing and relevant: DLLM, "World Models with Hints of Large Language Models for Goal Achieving" (Liu et al., 2024, arXiv 2406.07381), whose abstract reports results on HomeGrid, Crafter and Minecraft; SPRING (Wu et al., 2023, arXiv 2305.15486), an LLM-only Crafter agent; DECKARD (Nottingham et al., ICML 2023), LLM-guided subgoal graphs for crafting. None is cited. Achievement Distillation (Moon et al., NeurIPS 2023) is cited in passing but not compared.
- *Fix:* discuss these in Sec. 4 and add at least one of them as a baseline or explain why not (settings differ).
**W2: Novelty is stated more broadly than the evidence allows (Sec. 1, Sec. 4.2).** Related work says goal-generator methods "suffer from low practical utility and poor computational efficiency" because of "frequent and intensive LLM invocations", applied to ELLM, AdaRefiner, LLMV-AgE and Ruiz-Gonzalez et al. For Ruiz-Gonzalez et al. this is not supported by the abstract I could check (Words as Beacons describes a teacher-student scheme with LLM-provided subgoals; no call frequency is stated); LLMV-AgE was not found in the search and is left unchecked. The claimed gap, "semantic mismatch" (abstract), is never defined or measured.
- *Fix:* qualify the sentence per method; define "semantic mismatch" or drop it.
**W3: Domain knowledge is supplied rather than discovered.** The planner prompt lists items, tools, recipes and all 22 achievements and asks for "a crafting dependency tree" (App. B.3.1). Crafter's tech tree is public and widely discussed, so the LLM may largely transcribe it. The paper does not compare with a hand-written curriculum, so what the LLM adds beyond transcription is unknown. This matters for the open-world framing (Sec. 1) because novel environments will not have a rule sheet.
- *Fix:* add a hand-written goal-program baseline; test on a variant with perturbed recipes or an environment less covered by pretraining data.
**W4: Component novelty is moderate.** Per the claim-level profile (literature check): C1 (LLM-authored goal program with LLM-tuned priorities) medium, nearest prior ELLM (partial coverage); C2 (goal-conditioned LLM action mask) medium, nearest "Knowing What Not to Do" (Liu et al., 2024, arXiv 2405.16854), which uses LLMs for action-space pruning in multi-agent RL and is uncited; C3 (result) high. No established claim; this is a MAJOR-at-most positioning gap, not a known-result issue.

### Novelty delta table (closest prior works; links from the literature check)
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited/differentiated? |
|----------------------|--------------------|----------------------|------------------|-----------------------|
| C1 goal program with priorities | ELLM (Du et al., ICML 2023; arXiv 2302.06692) | LLM proposes goals for exploration, rewards agent for achieving them | Goals come from a reusable LLM-written program, priorities re-tuned offline | Cited; differentiated by cost |
| C1 | Words as Beacons (arXiv 2410.08632) | LLM teacher decomposes task into subgoals for RL | Code-based reuse and priorities | Cited, not differentiated |
| C1 | DLLM (arXiv 2406.07381) | LLM subgoal hints inside model rollouts, Crafter included | Model-free PPO with mask | **Not cited** |
| C2 goal-conditioned action mask | Knowing What Not to Do (arXiv 2405.16854) | LLM prunes action space (MARL) | Goal-conditioned, cached, annealed | **Not cited** |

### Baseline scout (Crafter)
| Benchmark | Prior method (link, label) | Reported number in its abstract | Compared? | Note |
|-----------|----------------------------|--------------------------------|-----------|------|
| Crafter | DLLM (arXiv 2406.07381; prior, arXiv-only) | "27.7%, 21.1%, and 9.9%" gains over recent methods on HomeGrid, Crafter, Minecraft | No | Different setting; a pointer only |
| Crafter | SPRING (arXiv 2305.15486; prior, arXiv-only) | none in abstract | No | LLM-only agent |
| Crafter | "From Laws to Motivation" (arXiv 2411.15891; prior, arXiv-only) | none | No | LLM+RL exploration on Crafter |
| Crafter | ELLM (ICML 2023) | none | Yes | Copied on Crafter (App. D) |
No under-reported baseline can be established: the paper's Crafter settings for copied numbers are not stated.

### Field snapshot (as of the cutoff)
Around 2021–2022 Crafter was addressed by PPO variants and model-based agents, and by exploration bonuses. From 2023, LLM-based approaches appeared in two families: LLM-as-agent (SPRING) and LLM-as-goal/reward proposer for an RL learner (ELLM and successors). The Craftax re-implementation moved evaluation to larger step budgets. Open problems named by recent work: reducing LLM calls, verifying LLM plans, and generalising beyond games with public documentation. Currently, a contribution counts as significant here when it shows a clear gain over strong non-LLM and LLM baselines at matched budgets, or demonstrates the idea on an environment the LLM cannot simply recall. A +5 score gain over PPO at 5M steps is a modest result by that standard.

### Missing References (all searched in strict mode; only the first group could be required comparisons)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | none | — |
| Important | Zeyuan Liu, Ziyu Huan, Xiyao Wang, Jiafei Lyu, Jian Tao, Xiu Li. "World Models with Hints of Large Language Models for Goal Achieving", arXiv 2406.07381, 2024 (found by `verify`/search) | LLM subgoals for long-horizon sparse-goal RL, evaluated on Crafter |
| Important | Yue Wu et al. "SPRING: Studying the Paper and Reasoning to Play Games", arXiv 2305.15486, 2023 (found; venue [verify]) | LLM-only Crafter agent; shows how much rule text alone gives |
| Important | Kolby Nottingham et al. "Do Embodied Agents Dream of Pixelated Sheep: Embodied Decision Making using Language Guided World Modelling", ICML 2023 (found) | LLM-hypothesised subgoal graph for crafting |
| Important | Zhihao Liu et al. "Knowing What Not to Do: Leverage Language Model Insights for Action Space Pruning in Multi-agent Reinforcement Learning", arXiv 2405.16854, 2024 (found) | LLM action-space pruning |
| Important | Danijar Hafner et al. "Mastering Diverse Domains through World Models" (DreamerV3), arXiv 2301.04104, 2023 (found) | Standard strong non-LLM Crafter baseline |
| Helpful | Jenny Zhang et al. "OMNI: Open-endedness via Models of human Notions of Interestingness", arXiv 2306.01711, 2023 (found; ICLR 2024 venue [verify]) | LLM-judged interestingness for open-ended exploration |
| Helpful | Shenao Zhang et al. "How Can LLM Guide RL? A Value-Based Approach", arXiv 2402.16181, 2024 (found) | Another LLM-guidance formulation |
| Worth discussing (concurrent, not required) | Carta et al. "HERAKLES: Hierarchical Skill Compilation for Open-ended LLM Agents", arXiv 2508.14751, 2025 (found) | Concurrent work on hierarchical goals in open-ended settings |

### Questions for Authors
1. Can you state, per cited method, the measured LLM call frequency behind "frequent and intensive LLM invocations" (Sec. 4.2)? A measured table would support the framing.
2. How does SGRL compare with SPRING-style rule-reading or DLLM on Crafter? A "not comparable" answer should explain the settings gap.
3. Does SGRL work if the recipe list in the prompt is removed or perturbed?

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See R1 on matching |
| Clarity | 3 | Clear overall prose |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Medium claim-level novelty |

### Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is a sensible but incremental recombination, and the positioning ignores directly relevant Crafter work.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing/Competent | Sound overall design, unclear schedule |
| Clarity & Presentation | 62 | Competent | Readable |
| Novelty & Originality | 50 | Developing | Medium on both central claims |
| Significance & Impact | 50 | Developing | Crafter-only |
| Experimental Validation | 46 | Developing | Missing the closest and strongest baselines |
| Reproducibility | 56 | Competent | Prompts released in appendix |
| Ethical Compliance | 62 | Competent | Low stakes |

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject)**: an incremental, sensibly engineered method whose literature positioning and baseline set do not match the claims.

### Confidence
**4**

---

# Peer Review Report (Reviewer 3)

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Reviewer: Salma Ivarsson-Tran, Perspective Reviewer (cognitive/curriculum-learning group, North America; fictional persona)
## Expertise: curriculum design; hierarchical task structure; human skill acquisition
## Date: 2026-11-10

### Summary
The paper turns LLM knowledge into a small program that tells a PPO agent what to work on next, ranked by priority, and into a mask that removes irrelevant actions. Seen from curriculum learning, SGRL is an automatically authored curriculum over a known achievement hierarchy, with the action mask acting as a soft scaffold that is withdrawn over training.

### Strengths
**S1: A practical pattern.** One-off program synthesis plus occasional re-weighting (every 2M steps, App. B.3.1) is closer to how a practitioner would deploy an LLM than step-wise querying. Compute per training run is likely small compared with ELLM-style querying (footnotes 1–2), although it is not measured.
**S2: The scaffold-then-withdraw idea is reasonable.** The annealing study (App. F.2) suggests that sustained guidance during skill acquisition and later autonomy helps; this mirrors scaffolding in learning science.
**S3: Priority weights are inspectable.** Fig. 7 and Fig. 21 (heatmaps of goal weights) give an interpretable record of the curriculum the LLM chose, which many methods lack.

### Weaknesses (opportunities)
**W1: The key assumption is a known, enumerable goal hierarchy.** The planner receives the full item/recipe/achievement list (App. B.3.1). In the open-world settings motivating the paper (Sec. 1) goals are not enumerated. The paper should state this assumption and test a setting with partial or noisy rules.
- *Fix:* add a rule-perturbation or partial-rule experiment, or discuss explicitly as a limitation.
**W2: Cost and deployment claims are asserted, not shown.** "Low LLM invocation frequency and minimal input token consumption" (Sec. 1) has no numbers; SGRL is 7.3× slower than PPO by SPS (Table 1, derived), which is expected for LLM-in-the-loop but should be broken down (LLM wall-clock vs environment).
- *Fix:* table of calls/tokens/dollars and wall-clock split.
**W3: No discussion of failure modes of LLM-written code.** A mis-specified priority could starve an achievement; the paper shows only a successful program. Safety of executing LLM code is not discussed.
- *Fix:* report failed or degenerate programs and how often; sandbox note.
**W4: Evidence of generality is thin.** Crafter and Craftax-Classic are the same game (App. A.1), so the paper has one environment. Other hierarchical-task domains (e.g., Minecraft-style tasks or text-based worlds) would show whether the pattern transfers.
- **Minor:** no limitations section; "farsighted" is used loosely (Sec. 5.2).

### Cross-disciplinary connections
Automatic curriculum learning (prerequisite-graph curricula, learning-progress-based goal selection) and classical hierarchical task networks both offer non-LLM ways to produce the same prioritised goal lists; a comparison with a prerequisite-graph curriculum would show the LLM's marginal value. Education research on scaffolding suggests withdrawing support based on competence rather than a fixed step schedule; ξ could be driven by the agent's success rates instead of time.

### Fundamental assumption audit
(1) Goal hierarchy known and static; (2) the text observation is a faithful, privileged description of the local map (Sec. 3.1, App. B.3.1 rendering function), which pixel-only baselines do not have; (3) five seeds of one generator are representative.

### Questions for Authors
1. Could ξ be adapted from per-achievement success instead of the step count (Eq. 3)? Results would show whether the schedule is a tuned constant.
2. What happens when the LLM-written program contains a wrong recipe?
3. Do you see the pattern working where the LLM cannot recall the rules?

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence partly matched |
| Clarity | 3 | Easy to follow |
| Significance | 3 | Useful deployment pattern |
| Originality | 3 | Fresh combination |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practical, low-cost pattern with clear ablations, tempered by one-game evidence.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound approach |
| Clarity & Presentation | 66 | Competent | Clear |
| Novelty & Originality | 62 | Competent | Good combination |
| Significance & Impact | 64 | Competent | Useful pattern |
| Experimental Validation | 56 | Competent | Adequate for claims, limited |
| Reproducibility | 60 | Competent | Prompts released |
| Ethical Compliance | 60 | Competent | Low stakes, no limitation section |

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**4 (Borderline Accept)**: a promising practical pattern; the evidence is narrow but supports the main direction.

### Confidence
**3**

---

# Peer Review Report (Reviewer 4)

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Reviewer: Dmitri Haldane-Park, Generalist Reviewer (industrial ML lab, South Asia; fictional persona)
## Expertise: broad deep learning; ICLR program-committee generalist
## Date: 2026-11-10

### Summary
The paper proposes SGRL, which uses LLMs offline-ish (code generation, periodic priority updates, mask construction) to give a PPO agent prioritised goals and action masks in Crafter-family environments. It reports higher score and depth than ELLM, AdaRefiner and PPO on Craftax-Classic at 5M steps, and ablations at 10M.

### Contribution in one paragraph
A cheaper way to use an LLM for goal-guided exploration: write goal logic once as code, re-weight it occasionally, and prune actions per goal. It matters if LLM-guided exploration is to be affordable; it is less convincing as a general method because it is shown on one game.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Claims supported by evidence | Partly | Table 1; efficiency not measured (Sec. 1) |
| Sound methodology (Soundness) | Partly | Unmatched baselines; Eq. (3)–(4) |
| Clear presentation | Mostly | Several inconsistencies (Sec. 5.3.2 "Crafter") |
| Significance/contribution | Partly | One game, modest gains over PPO |
| Reproducibility | Partly | Prompts yes; code and generated program not found |

### Strengths
**S1: Clear writing and structure.** Motivation → preliminary CodeGoal → method → results is easy to follow (Sec. 1–5).
**S2: Cheap by design.** Mask bank (Sec. 3.2) and periodic re-weighting avoid per-step calls; the SPS gap to ELLM/AdaRefiner (Table 1) supports this direction, even if cost is not itemised.
**S3: Informative ablations.** Table 2 and App. F show which components matter; the Static-Prun result (Sec. 5.3.2) is a useful nuance about over-reliance on the LLM.
**S4: Disclosure of the prompts** (App. B.3).

### Weaknesses
**W1: The evaluation is narrow for the framing.** The paper motivates "open and complex environments" (abstract, Sec. 1) but tests on one game in two implementations (App. A.1). A reader cannot tell whether the method generalises or is a tuned Crafter solution.
- *Fix:* add a second, structurally different environment or narrow the framing to Crafter.
**W2: Baselines are few and the comparison is not clean.** Two LLM baselines at reduced query frequency and a different LLM (footnotes 1–2, App. B.1), PPO only; Crafter numbers copied (App. D); strongest non-LLM Crafter methods absent.
- *Fix:* see R1-W1/W2.
**W3: Core mechanism is hard to follow in places.** Eq. (3) as written produces a schedule that starts with no masking, peaks at 0.4T and then relaxes; the text calls it gradual relaxation. The number of candidate goals k and the way weights enter the encoder (Sec. 3.3) are not given.
- *Fix:* add a one-line pseudo-algorithm and a plot of ξ(t).
**W4: Claims are worded more strongly than results.** "compared to existing state-of-the-art methods" (abstract); "This phenomenon demonstrates that our goal-generation method produces farsighted objectives" (Sec. 5.2), based on plateau shapes in Fig. 3 (c), (h); reward gain in Table 1 is inside noise (13.0 ± 0.3 vs 12.3 ± 0.9).
- *Fix:* soften and support with a direct measurement (e.g., time to each achievement).
**Minor:** Sec. 5.3.2 says "Crafter" where Craftax-Classic is meant; "Methd" in Table 2 header; the human reference in Table 1 (50.5 ± 6.8) is the same number as in the Crafter Table 4 though the environments differ.

### Questions for Authors
1. Which result would you highlight if reviewers asked for one experiment: a second environment, or matched baselines?
2. Is code release planned, including the final goal program?
3. How sensitive is the method to the LLM (DeepSeek-V3 vs a small open model)?

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See above |
| Clarity | 3 | Mostly clear |
| Significance | 2 | One game |
| Originality | 2 | Incremental |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: readable and cost-aware but narrow; a typical submission at this level is rejected.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound but under-specified |
| Clarity & Presentation | 62 | Competent | Good flow, some inconsistencies |
| Novelty & Originality | 50 | Developing | Incremental |
| Significance & Impact | 52 | Developing | Narrow |
| Experimental Validation | 48 | Developing | Few baselines |
| Reproducibility | 56 | Competent | Prompts and hyperparameters, no code |
| Ethical Compliance | 60 | Competent | Low stakes |

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No.**

### Overall Score
**3 (Borderline Reject)**: a readable, practical idea with narrow and not fully matched evidence.

### Confidence
**3**

---

# Devil's Advocate Report

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Reviewer: Noor Eichholtz, evaluation-methodology postdoc, public research institute, Central Europe (fictional persona)

## Steelman
LLMs hold useful priors about open-world games. If an LLM writes the goal logic once and is consulted rarely, an RL agent can benefit from those priors at a small fraction of the cost of step-wise LLM guidance, and the ablations (Table 2) show that both the priority mechanism and the mask contribute.

## Core Argument Chain
1. P1: Per-step LLM goal generation is costly and semantically mismatched with the agent (abstract, Sec. 1).
2. P2: A structured LLM-written goal function with LLM-tuned priorities supplies better, cheaper guidance (Sec. 3.1).
3. P3: A goal-conditioned action mask makes the policy goal-consistent (Sec. 3.2).
4. P4: SGRL beats ELLM, AdaRefiner and PPO on Craftax-Classic and matches or beats them on Crafter (Table 1, App. D).
∴ Structured goal guidance is the better way to use LLMs for exploration in open-world RL.

## Strongest Counter-Argument
Table 1 shows that a particular system, SGRL with a reasoning model and a full rule sheet, beats two older systems run with a weaker model and reduced query rate. It does not show that *structure* is what helps. SGRL's prompt contains the entire Crafter tech tree and asks for "a crafting dependency tree" (App. B.3.1); Crafter's rules are public and heavily represented in pretraining data. The most economical explanation of the gain is therefore that the LLM transcribes a known curriculum into code and the mask, and that any method given a comparable curriculum (including a hand-written one) would score similarly. Nothing in the paper rules this out: there is no hand-written-curriculum oracle, no baseline given the same rule sheet and LLM, no environment where the rules are unknown, and no strong non-LLM Crafter baseline. The claimed efficiency advantage compounds the problem, since call counts and tokens are never reported, and the only cost figure, SPS, shows SGRL 7.3× slower than PPO (derived from 18.5 vs 135.3 ×10²). The conclusion "structured goal guidance is better than existing LLM-enhanced RL" is not supported; the weaker conclusion "LLM-written curriculum code can help PPO on Crafter at 5M steps" is. The authors can answer this with matched controls, so I rate it MAJOR, not CRITICAL.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in weaker form: gains over PPO (+9.0 score, Table 1) and over ELLM/AdaRefiner (+5.3/+5.4) exist on the paper's own protocol, no test-set selection is stated (Crafter has no hidden test split), and the confounds are partly controlled and fixable by matched experiments.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Alternative explanation | App. B.3.1–B.3.2; Table 1 | Rule/tech-tree knowledge supplied to SGRL's planner and masker; not shown for baselines. LLM differs (R1 vs V3). Evidence supports a weaker claim | Matched-information baselines; scripted oracle; weaker LLM |
| DA-M2 | Evidence | Sec. 5.1.2 vs App. D; Table 4 | "same configurations" while Crafter baselines are copied from original papers | Rerun or restate |
| DA-M3 | Scope | Abstract, Sec. 1, App. A.1 | "Open and complex environments" evidenced by one game in two implementations | Second environment or narrow framing |
| DA-M4 | Overclaim (E5) | Abstract; Sec. 5.2 | "compared to existing state-of-the-art methods"; "demonstrates that our goal-generation method produces farsighted objectives" from plateau shapes | Narrow wording; measure time-to-achievement |
| DA-M5 | Evidence | Sec. 1 contribution 1; Table 1 | Efficiency not measured; SPS slower than PPO | Calls/tokens/cost table |
| DA-M6 | Selection | App. F.2 | Best of four schedules chosen by performance on the reported environment, with no tuning budget stated for baselines | State protocol; give baselines equal tuning |
| DA-M7 | Mechanism | Eq. (3)–(4), App. F.1 | Schedule direction at start (ξ = 1 = no masking) conflicts with the text | Clarify |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Sec. 5.3.2 | "on Crafter" for a Craftax-Classic figure |
| DA-m2 | Metric | App. A.2 | Achievement Depth ("furthest achievement it unlocks") is a max over episodes/seeds and is sensitive to a single lucky run; define the aggregation |
| DA-m3 | Reference | Table 1 | Human reference numbers identical to the Crafter table though the environment differs |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| SGRL vs AdaRefiner score gain (Table 1) | 33.8 vs 28.5 | +5.3 | Consistent |
| SGRL vs ELLM score gain | 33.8 vs 28.4 | +5.4 | Consistent |
| SGRL vs PPO score gain | 33.8 vs 24.8 | +9.0 (+36% relative) | Consistent |
| SGRL reward gain over best baseline | 13.0 vs 12.3 | +0.7 (std of AdaRefiner 0.9) | Within noise; paper says "does not exhibit a significant advantage" |
| SGRL vs w/o Prun (Table 2) | 43.9 vs 40.0 | +3.9 (std 2.6/2.1) | Weaker than "significantly" |
| SPS ratio SGRL vs PPO | 18.5 vs 135.3 (×10²) | PPO 7.3× faster | SGRL is slower than PPO |
| SPS ratio SGRL vs ELLM / AdaRefiner | 18.5 vs 0.9 / 0.3 | 20.6× / 61.7× faster | Consistent with "faster training speed" |
| SGRL 5M score Table 1 vs Table 5 | 33.8 ± 1.5 both | — | Match |

## Ignored Alternative Explanations
- Transcription of public Crafter rules by the LLM (DA-M1); a scripted curriculum may match.
- The stronger planning LLM (R1 vs V3) rather than the structure.
- Privileged text observations for the goal planner (rendered from env state, App. B.3.1) versus pixel-only baselines in the PPO policy input, unless baselines share the same input (not stated).
- Differences in training schedule and annealed masking explaining early-vs-late curves (Sec. 5.3.2, "Static-Prun") rather than "over-reliance on the LLM".
- Pretraining contamination: DeepSeek models may know Crafter.

## Missing Stakeholder Perspectives
Practitioners who need the method where rules are unknown or noisy; reproducers who need the generated program and call counts; compute-constrained groups for whom the R1 planning step may itself be costly.

## Observations (Non-Defects)
Five seeds with spread values; reported negative nuance about Static-Prun; honest statement that reward gains are not significant (Sec. 5.2); appendix prompts released; the Craftax-Classic baselines were actually reproduced rather than only copied.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Alternative explanation untested; schedule unclear |
| Clarity & Presentation | 58 | Inconsistencies |
| Novelty & Originality | 46 | Medium novelty |
| Significance & Impact | 44 | One game |
| Experimental Validation | 38 | Unmatched, few baselines |
| Reproducibility | 48 | No code/program, no call counts |
| Ethical Compliance | 58 | Low stakes, no limitations |

**Pool position:** better than about 38% of submissions to ICLR. Deciding evidence: the main claim is confounded and the evidence base is one environment.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "Hyperparameters and prompts are missing" (draft) | Dropped | Answered by Table 3 and App. B.3; replaced by W6 on k, iteration count, shared program |
| R1 | "Single seed" (draft) | Dropped | Five seeds in Sec. 5.1.2; kept only the undefined "±" and no tests (W5) |
| R2 | "No annealing-schedule ablation" (draft) | Dropped | App. F.1–F.2 contain it |
| R2 | W2 novelty sentence about ELLM/AdaRefiner | Rewritten | Limited to claims not supported by cited abstracts (Ruiz-Gonzalez et al., Chi et al.) as a question about measured call frequency |
| R3 | "Method may be unethical" (draft) | Dropped | No human data; ethics flag No |
| R4 | W4 reward-gain wording | Rewritten | Added the paper's own admission (Sec. 5.2) to keep it consistent |
| DA | DA-M6 selection of annealing schedule | Kept, rated MAJOR | Not a held-out-split issue: Crafter has no hidden test split; no CRITICAL |
| R1/R4/DA | Typos and minor naming | Moved to Minor | Cosmetic |
Scores were not changed.

---

# Phase 2: Synthesizer Part A and EIC Meta-Review

## Issue list and consensus map (Synthesizer)
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| Evidence is narrow (one game in two implementations) | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Baselines few/unmatched; missing strong or closest methods | R1, R2, R4, DA | CONSENSUS-4 |
| Efficiency claim not measured | R1, R3, R4, DA | CONSENSUS-4 |
| Domain knowledge supplied to planner/masker; confound with structure | R1, R2, R3, DA | CONSENSUS-4 (hinge) |
| Overclaim wording (SOTA, "farsighted", "significantly") | R1, R4, DA | CONSENSUS-3 |
| Mask-schedule specification (Eq. 3–4) | R1, R4, DA | CONSENSUS-3 |
| Crafter baselines copied vs "same configurations" | R1, DA | CONSENSUS-2 (hinge) |
| Uncited closely related work (DLLM, SPRING, DECKARD, LLM action pruning) | R2 | SOLO |
| Failure modes of LLM-written code; no limitations | R3 | SOLO |
| DA-CRITICAL | none raised | — |
Hinge points: domain-knowledge confound; baseline matching; efficiency claim.

Official output (from `aggregate_scores.py`, before weights): ratings 3, 3, 4, 3, 2, mean 3.00, composite 52.9, no warnings.

# Editorial Decision

## Paper: Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning
## Submission ID: iclr26-Xs1CrA1kZQ
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Mirela Castellanos-Odum; R1 Methodology Hyun-woo Pellegrini, R2 Domain Okonkwo Brandvold, R3 Perspective Salma Ivarsson-Tran, R4 Generalist Dmitri Haldane-Park, DA Noor Eichholtz

---

## Decision: Borderline Reject (3), ICLR rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); scale status secondary

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 52.9
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 52.0 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 47% of ICLR submissions (accepted share ≈ 27%). Deciding evidence: a sensible and cheap idea with a favorable result, but the comparison is not matched, the baseline set is small, and one game carries all the evidence; typical accepted ICLR papers in this area show stronger controls or a second domain.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** SGRL is a clear, practical way to take an LLM off the critical path of exploration; the gain over PPO and the two LLM baselines is large relative to seed spread (+5.3 to +9.0 score, Table 1), the ablations isolate the components (Table 2), and prompts and hyperparameters are disclosed.
- **Against acceptance:** the comparison gives SGRL more domain knowledge and a stronger LLM than the baselines, and the paper contains no control that separates the claimed "structure" from that knowledge. The headline efficiency claim is unmeasured, Crafter baseline numbers are copied from other papers while the text says "same configurations", the closest Crafter prior work and strong non-LLM baselines are missing, and all evidence comes from one game.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Crafter baselines copied but text says same configurations | R1-ERR-1, DA-M2 | Sec. 5.1.2; App. D | **Verified** | Both sentences present verbatim |
| SGRL prompt includes the full rule/tech-tree and achievement list | R1-W1, R2-W3, DA-M1 | App. B.3.1–B.3.2 | **Verified** | Prompt content verified; that baselines lack it is unstated, not shown |
| Baselines use a different LLM and reduced query rate | R1-W1, DA-M1 | App. B.1; footnotes 1–2 | **Verified** | R1 vs V3; "queried every 200 steps" |
| Efficiency claim has no call/token counts | R1-ERR-5, R3-W2, R4, DA-M5 | Sec. 1; Table 1 | **Verified** | Only SPS reported; SGRL 18.5 vs PPO 135.3 (×10²) |
| Eq. (3)–(4): ξ starts at 1 = no masking | R1-ERR-3, R4-W3, DA-M7 | Eq. (3), (4); App. F.1 | **Partly correct** | Arithmetic holds; the authors' intent is unclear; a clarity and reproducibility issue |
| "Significantly outperforms all variants" without tests | R1-ERR-4 | Sec. 5.3.2; Table 2 | **Verified** (as MINOR) | +3.9 with std 2.1–2.6 |
| DLLM/SPRING/DECKARD/LLM action pruning uncited | R2-W1, W4 | Sec. 4; reference list | **Verified** | Reference list read in full; titles and abstracts from the strict-mode search |
| Achievement Distillation cited but not compared | R1-W2, R2-W1 | Intro; reference list; Table 1 | **Verified** | |
| Table 5 shows a variant with score ≥ SGRL at 5M | R1-Q2 | Table 5 | **Unverifiable** | Extraction does not assign rows; kept as a question |
| SGRL "cheap" and deployable | R3-S1 | Sec. 1, 3.1 | **Overstated** | Plausible but unmeasured |
| One-game evidence | all | App. A.1 | **Verified** | Craftax-Classic re-implements Crafter |
| No limitations section | R1, R3 | whole paper | **Verified** | No such heading or discussion found |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error Log items verified at their locations (same-configuration, Sec. 5.3.2 mismatch, no call counts); calibrated for ICLR |
| R2 (Domain) | 3 | 4 | 1.0 | Missing-work claims verified against the ledger and reference list; no points moved |
| R3 (Perspective) | 4 | 3 | 0.75 | Efficiency strength rests on an unmeasured claim; rating of 4 sits above the evidence in her own weaknesses |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound, typical review |
| DA | 2 | 4 | 1.0 | Main counter-argument verified in part (prompt content) but untested causally; no CRITICAL raised; rating of 2 slightly harsher than the verified issues |

### DA-CRITICAL Rulings
None raised. DA-M1 (matched-information confound) was considered under the AC test: it is partly controlled (the pruner and priority ablations exist), is resolvable with matched experiments, and the evidence supports a weaker claim, so it is MAJOR, not fatal. DA-M6 (annealing schedule chosen on the reporting environment) is not a held-out-split issue in Crafter, where there is no hidden test split; MAJOR.

### Final Decision and Justification
The EIC-weighted rating is 2.92, which gives a starting point of 3, and the composite (52.0) agrees. I keep 3. The accept-leaning review (R3, rating 4) rests on cost and deployment benefits that the paper does not measure (verified in Sec. 1 and Table 1). The three verified, located issues that move this below the accept line are: (1) Table 1 compares SGRL against baselines without matched rule knowledge, LLM or query budget (App. B.1, B.3; footnotes 1–2); (2) Crafter baseline numbers are copied while Sec. 5.1.2 claims the same configurations (App. D); (3) the efficiency claim in the contribution list is unmeasured. These are fixable with matched experiments and a cost table, and the underlying idea is sensible, so I would not call the paper a clear reject (2). No DA ceiling applies. Pool position about 47, inside the "typical rejected submission" band but near its top.

---

## Score Summary

### Official Scores and EIC Assessment (from `aggregate_scores.py --venue iclr --final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 48 | 54 | 62 | 56 | 44 | 52.8 | 51.7 | 18 |
| Clarity & Presentation | 60 | 62 | 66 | 62 | 58 | 61.6 | 61.1 | 8 |
| Novelty & Originality | 52 | 50 | 62 | 50 | 46 | 52.0 | 51.3 | 16 |
| Significance & Impact | 48 | 50 | 64 | 52 | 44 | 51.6 | 50.4 | 20 |
| Experimental Validation | 42 | 46 | 56 | 48 | 38 | 46.0 | 44.9 | 18 |
| Reproducibility | 50 | 56 | 60 | 56 | 48 | 54.0 | 53.2 | 12 |
| Ethical Compliance | 60 | 62 | 60 | 60 | 58 | 60.0 | 60.0 | 4 |
| **Composite** | 50.0 | 53.0 | 61.1 | 53.9 | 46.3 | **52.9 (before)** | **52.0 (after)** | |
| Pool position (P%) | 42 | 46 | 66 | 50 | 38 | | | |

Reviewer weight shares of the EIC assessment: R1 27%, R2 21%, R3 13%, R4 18%, DA 21%. No ⚠ spread warnings (largest spread 20, Significance).

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning" to ICLR. The paper addresses a real problem: using LLM knowledge to guide RL exploration without per-step LLM calls.

**Overall Assessment:** The reviewers found the idea practical and clearly presented, with useful ablations and released prompts. They were less convinced that the evidence separates the proposed structure from the domain knowledge and LLM supplied to it, and they noted that the evaluation rests on a single game.

**Key Strengths Identified by Reviewers:**
1. A cost-aware design (code-as-goal-generator, mask bank, periodic re-weighting) (R1, R3, R4).
2. Ablations isolating priorities, the pruner and the schedule (R1, R4, R2).
3. Disclosure of prompts, LLM versions, hyperparameters and five seeds (R1, R4).

**Key Concerns Requiring Attention:**
1. Baselines are not matched in rule knowledge, LLM and query budget, and the baseline set is small (CONSENSUS-4).
2. The efficiency claim is not quantified; SGRL is slower than PPO by SPS (CONSENSUS-4).
3. Evidence from one game in two implementations; Crafter baseline numbers are copied from other papers while the text says "same configurations" (CONSENSUS-5 / CONSENSUS-2).

No CRITICAL challenge was raised by the Devil's Advocate; the strongest objection (gains may reflect transcribed public rules) was ruled MAJOR.

**Decision: Borderline Reject (3).** The method is sensible and the result is favorable on its own protocol, but the controls needed to support the central claim are missing. A revision that adds matched baselines, a scripted-curriculum oracle, measured LLM cost and a second environment would put the paper in the accept range.

Please refer to the Revision Roadmap below.

Sincerely,
Mirela Castellanos-Odum
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| One-game evidence | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Few or unmatched baselines | R1, R2, R4, DA | CONSENSUS-4 |
| Efficiency not measured | R1, R3, R4, DA | CONSENSUS-4 |
| Supplied domain knowledge confound | R1, R2, R3, DA | CONSENSUS-4 |
| Overclaiming wording | R1, R4, DA | CONSENSUS-3 |
| Eq. (3)–(4) clarity | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the approach "cheap and deployable"? | R3, R4 | R1, DA | Not measured; treated as unsupported until call/token/cost numbers appear |
| Overall level | R3 (4) | DA (2), R1/R2/R4 (3) | Rating of 4 rests on the unmeasured efficiency; 3 retained |

### Score Spread Discussion
No dimension exceeds the 20-point flag (Significance spread is exactly 20: R3 at 64 vs DA at 44; R3 credits deployment value, DA the single-game scope; the EIC adopts the lower-middle view).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Knowledge/LLM confound | Yes (R1, R2, R3) | n/a | New experiments |
| DA-M2 | MAJOR | Copied Crafter numbers vs "same configurations" | Yes (R1) | n/a | Clarification or rerun |
| DA-M3 | MAJOR | One-game scope | Yes (all) | n/a | New environment or narrowed claim |
| DA-M5 | MAJOR | Efficiency unmeasured | Yes (R1, R3, R4) | n/a | Logging existing runs |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Matched-information, matched-LLM comparison; scripted-curriculum oracle; unstructured-text-goals + same mask | R1-W1, DA-M1, R2-W3 | Table 1; App. B.1, B.3 | Give ELLM/AdaRefiner the same rule sheet; run SGRL with DeepSeek-V3; add oracle and ablation rows; 5 seeds, 5M steps | High; ~30–60 GPU-h plus API cost | Partly (a subset of rows) |
| P1-2 | Quantify the efficiency claim | R1-ERR-5, R3-W2, DA-M5 | Sec. 1, Table 1 | Table of LLM calls, tokens, dollars and wall-clock split for every method, per 1M steps | Low (logs) | Yes |
| P1-3 | Crafter baseline provenance | R1-ERR-1, DA-M2 | Sec. 5.1.2; App. D; Table 4 | State settings of copied numbers or rerun; fix "same configurations" | Low–High | Yes (text) / No (rerun) |
| P1-4 | Add strong comparison methods and narrow SOTA wording | R1-W2, R2-W1 | Table 1; abstract | Add a strong non-LLM Crafter baseline (e.g., Achievement Distillation) and one LLM-guided Crafter method, or limit wording to "LLM-enhanced PPO baselines" | Medium–High | Partly |

### Priority 2: Strongly Suggested
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Second environment or rule-perturbation test | R3-W1, R4-W1, DA-M3 | Add a structurally different environment, or perturb recipes | High | Partly |
| S2 | Clarify Eq. (3)–(4) and the test-time use of the mask; plot ξ(t); give k, encoder details | R1-ERR-3, R4-W3, DA-M7 | Pseudo-algorithm and figure | Low | Yes |
| S3 | Release the generated program; variance across LLM-generated programs; selection protocol | R1-W6, R4-Q2 | Report programs per seed and how chosen | Medium | Partly |
| S4 | Statistics: define ±, paired tests, soften "significantly" | R1-W5, ERR-4 | Welch/bootstrap over seeds | Low | Yes |
| S5 | Related work: DLLM, SPRING, DECKARD, LLM action pruning, DreamerV3; per-method qualification of "frequent LLM invocations" | R2-W1, W2, W4 | Rewrite Sec. 4 | Low | Yes |
| S6 | Selection of annealing schedule and equal tuning for baselines | DA-M6 | State protocol | Low–Medium | Partly |
| S7 | Baselines at 10M steps to match Table 2 | R1-Q5 | Extend runs | Medium | Partly |

### Priority 3: Nice to Fix
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Limitations section, failure modes of LLM code, code-execution safety | R3, R1 | Add |
| N2 | "Crafter" vs "Craftax-Classic" in Sec. 5.3.2; "Methd" in Table 2 | R1, R4 | Fix |
| N3 | Define Achievement Depth aggregation; human reference provenance in Table 1 | DA-m2, DA-m3 | Clarify |
| N4 | Adaptive ξ driven by success rate | R3 | Optional experiment |
| N5 | Concurrent work (HERAKLES) | R2 | Discuss |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–4 weeks including compute and API cost (rebuttal covers P1-2, P1-3 text, part of P1-1)
- Priority 2: 7 items, about 2–3 weeks
- Priority 3: 5 items, a few days
- **Total estimated revision time**: roughly 4–7 weeks.

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
