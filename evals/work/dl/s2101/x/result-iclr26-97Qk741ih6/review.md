# Academic Paper Review: CLAUSE (full mode, target venue ICLR)

*Simulation of how a careful panel would likely see this draft; not a prediction of any real outcome. Date: 2026-11-10. Request: full review, skip confirmation, literature check strict, cutoff 2025-09-24. Figures were not available (text extraction only): figure-dependent claims are judged from captions, axis text and prose, and marked as such. The five reviewer passes were performed one after another in a single model context, not by independent agents; each pass was written from its role file without reading the later reports.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering |
| Primary Discipline | ML → reinforcement learning for knowledge-graph question answering / retrieval-augmented generation |
| Secondary Discipline(s) | NLP (multi-hop QA), multi-agent RL, constrained optimization, efficient LLM inference |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Three cooperating policy agents (edit / traverse / curate) on a KG; CTDE PPO with Lagrangian multipliers (LC-MAPPO); frozen reader LLM (Qwen3-32B for baselines) |
| Target Venue | ICLR (stated by user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none (ICLR: soundness, presentation, contribution; ≈27% acceptance in the 2026 cycle) |
| Paper Maturity | Submission-ready in form, but the appendix is referenced as "Appendix ??" (§4.1, §4.4) and is not part of the text |
| Ethics-Relevant Content | none (public QA datasets; no human data) |

**Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters. The reviewers' copy is identical to the paper text.

### Claimed Contributions (as stated by the authors; claim IDs used below)
- **C1** Problem framing: KGQA as requirements-conditioned context assembly with per-query budgets/prices (§1 Contributions (1); §3, Eq. 1).
- **C2** Framework: CLAUSE, three agents (Subgraph Architect, Path Navigator, Context Curator) that jointly build compact subgraphs, explore paths and curate minimal auditable context with a learned STOP (§1 Contributions (2)–(5); §4.3).
- **C3** Training: LC-MAPPO, constrained CTDE PPO with separate cost heads and dual variables for edges/steps/tokens, with a shadow-price property and convergence (§1 Contribution (6); §4.4; convergence "stated in Appendix ??").
- **C4** Deployment control: one checkpoint adapts per query to caps or prices without retraining; "Requirement sweeps reveal clear accuracy–latency–cost Pareto frontiers" (Abstract; §1 p. 2; §4.5).
- **C5** Results: higher EM@1 with lower subgraph growth and latency at equal or lower token budgets on HotpotQA, MetaQA, FactKG; on MetaQA-2-hop vs. GraphRAG "+39.3 EM@1 with 18.6% lower latency, and 40.9% lower edge growth" (Abstract; §5.1).

### Paper memory (factual record shared with all reviewers)
- **Datasets/splits:** MetaQA (1/2/3-hop), HotpotQA (distractor), FactKG (§5 "Dataset"). Train/validation/test splits, training-set size, and how a KG is built for HotpotQA: not stated after search (grep for *split, validation, test set, tuned*: no hits).
- **Models:** reader/shared retriever for RAG and agent baselines is Qwen3-32B (§5 Baselines). CLAUSE's reader: "Reader LLM" in Fig. 1, model not named. Neural scorer architecture, weights w1–w4, horizon H, η, PID settings, reward Racc definition: not stated.
- **Compute, seeds, variance, code:** not stated after search (grep: *seed, variance, std, GPU, hardware, code*: no relevant hits).
- **Headline numbers and sources:** 71.7 / 84.2 / 91.0 / 87.3 / 85.5 EM@1 (Table 1); latency 1.48 / 1.36 / 0.98 / 1.14 / 1.27 (Table 2); edge budget 0.78 / 0.74 / 0.77 / 0.78 / 0.90 (Table 3); +39.3, 18.6%, 40.9% (Abstract, from Tables 1–3); feasibility 0.340 vs. 0.117, violations 0.577 vs. 0.880, latency cost 0.738 vs. 0.838, duals 0.004 vs. 0.001 (§5.1, Fig. 3); ablations Table 4.
- **Appendix/supplement:** none provided; algorithms, shadow-price proof and convergence are deferred to "Appendix ??". Details said to be there are treated as unverified, not missing.
- **Unverifiable:** Figures 1–4 as images (read from extracted text only); Fig. 2 has no numbers (family averages, "mean ± SD" label).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Marisol Thackeray-Yilmaz, research university (Western Europe)
- **Seniority / Expertise**: Senior faculty / reinforcement learning, retrieval-augmented LLMs, area-chair experience at ICLR-level venues
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Counts evidence, not heads; asks whether the central claim is measured.

### Reviewer 1 (Methodology): Dr. Lenka Varga-Ito, industrial research lab (Central Europe)
- **Seniority / Expertise**: Senior industry scientist / multi-agent and constrained RL evaluation; RAG benchmarking and latency measurement
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched budgets, variance over seeds, and measured wall-clock cost.

### Reviewer 2 (Domain): Prof. Abiodun Casterman, public research university (West Africa)
- **Seniority / Expertise**: Senior faculty / knowledge-graph QA and neuro-symbolic reasoning; LLM+KG retrieval
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks every citation against the claim it supports.

### Reviewer 3 (Perspective): Dr. Soraya Beltrami-Nakamura, database-systems group, public research university (East Asia)
- **Seniority / Expertise**: Mid-career / learned query optimization, cost-based planning, human-centered auditability
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive, asks how an operator would actually use the knobs.

### Reviewer 4 (Generalist): Dr. Hyun-woo Pellegrin, ML group, private research university (North America)
- **Seniority / Expertise**: Mid-career / deep learning for NLP broadly; typical ICLR program-committee member
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads for the one-paragraph contribution and whether the evidence is easy to find.

### Devil's Advocate: Prof. Dariusz Ellingsworth-Rao, statistics and evaluation-methodology group (South Asia / UK)
- **Seniority / Expertise**: Senior faculty / causal inference for ML evaluation, confound analysis
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, fair, steelmans before attacking.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering
## Reviewer: Dr. Lenka Varga-Ito, Methodology Reviewer (industrial research lab, Central Europe; fictional persona)
## Expertise: multi-agent and constrained RL evaluation; RAG benchmarking; latency measurement
## Date: 2026-11-10

## Summary
The paper trains three small policies (graph editing, path traversal, evidence selection) jointly with a Lagrangian-constrained multi-agent PPO so that edge edits, interaction steps and selected tokens are priced or capped. A frozen LLM reads the curated context. On MetaQA, HotpotQA (distractor) and FactKG it reports higher EM@1 than RAG and LLM-agent baselines with lower normalized latency and edge counts than most of them, plus an ablation (Table 4) and a constraint-satisfaction comparison against MAPPO, fixed-penalty PPO and RCPO (Fig. 3).

## Strengths
### S1: Clear, deployment-relevant problem statement
Treating steps, edges and tokens as explicit costs (§3, Eq. 1) is a sensible framing, and attributing each cost to its source action (§4.3 "cost attribution") makes the per-head design easy to follow.

### S2: Consistent accuracy gains across three datasets and hop counts
Table 1 shows CLAUSE best in every column; the gain over the strongest baseline (KG-Agent) is large at MetaQA 2/3-hop (87.3 vs. 78.0; 85.5 vs. 75.4) and modest elsewhere (71.7 vs. 68.7 HotpotQA; 84.2 vs. 82.1 FactKG).

### S3: Efficiency is reported next to accuracy, and headline arithmetic is correct
I recomputed the abstract's numbers: 87.3 − 48.0 = 39.3 (Table 1); (1.40 − 1.14)/1.40 = 18.6% (Table 2); 1 − 0.78/1.32 = 40.9% (Table 3). Also 191% = (0.340 − 0.117)/0.117 and 34% = (0.880 − 0.577)/0.880 (§5.1) check out.

### S4: Component ablations and a constraint-learning comparison are included
Table 4 removes each agent and the dual updates, and Fig. 3 compares four constrained-optimization variants, which is more than many system papers offer.

## Weaknesses

### W1: The headline comparison does not control for training, budgets or tuning (Table 1–3, §5)
CLAUSE is trained with RL on (presumably) each dataset's training queries; the LLM baselines are described only as "under a shared retriever/reader and decoding" (§5 Baselines). The paper does not say whether baselines were tuned, whether they ran with CLAUSE's step/token budgets, or whether KG-Agent (a trained method) was retrained or run from released weights. Token consumption, which the abstract treats as a matched quantity ("at equal or lower token budgets"), appears only as family averages in Fig. 2, not per method. HotpotQA is a text benchmark; how its KG is constructed is not stated.
- **Suggested Fix**: Report per-method tokens, steps and wall-clock latency; run the best baselines under matched token/step caps; state split sizes, baseline settings and tuning protocol, and add a trained non-agentic baseline (e.g., a learned reranker with the same reader). Cost: a few GPU-days of inference.

### W2: The central deployment claim (budget/price control without retraining) is not tested (Abstract; §1 p. 2; §4.5; Fig. 3)
The introduction states "Requirement sweeps reveal clear accuracy–latency–cost Pareto frontiers", but no table or figure in the paper varies βedge, βlat, βtok or λ and reports EM. The only constraint experiment (Fig. 3, caption and §5.1) uses one setting (edge budget 0.5, latency budget 0.7, normalized to an unstated reference), reports feasibility 0.340 for LC-MAPPO (i.e., about two thirds of episodes infeasible on the paper's own metric), and reports no EM. Tables 1–3 show CLAUSE latency 0.98–1.48×, above the 0.7 budget used in Fig. 3, so the headline results are not from the constrained regime. §4.5 nevertheless promises "hard guarantees" in cap mode. How the policy is trained to respond to arbitrary test-time λ or β (budgets are in the state bt, but the duals converge to fixed values) is not described.
- **Suggested Fix**: Show EM vs. cost curves for several caps and prices from one checkpoint, with violation rates and EM under the same constraints for all four trainers; define "feasibility rate"; describe the budget/price sampling during training.

### W3: Text claims about efficiency disagree with Tables 2–3 (§5.1)
See Error Log ERR-1, ERR-2. In particular "CLAUSE achieves the smallest edge budgets across all settings" is contradicted by LightRAG in two columns, and CLAUSE's latency is above Vanilla RAG in four of five columns and above Hybrid RAG on HotpotQA and FactKG.
- **Suggested Fix**: Restate as "lower than all agent baselines and GraphRAG" and add the accuracy/cost trade-off against LightRAG.

### W4: Ablations are confounded and partly inconsistent with Table 1 (Table 4, §5.2)
The "w/o Subgraph Architect" variant is labelled "StaticRAG; no-KG" and scores 74.8 EM, while Vanilla/Hybrid RAG score 37.6/41.5 on MetaQA-2-hop in Table 1; a "no-KG" variant also has an edge budget (1.44×), which is undefined without a graph. The ablated variants replace learned agents by heuristics, so they do not test whether three jointly trained agents are needed versus one policy with three action heads. Table 4 does not state which MetaQA hop is used (87.3 equals the 2-hop number in Table 1; the 3-hop average would be 87.9). The "Greedy-Hop" variant (82.1) already exceeds KG-Agent (78.0), suggesting much of the gain does not come from the learned navigator.
- **Suggested Fix**: State the hop setting; define each variant precisely; add a single-agent LC-PPO variant, an RCPO variant with EM, and all hops.

### W5: No variance, seeds or learning curves for an RL method (all tables; Fig. 3)
Tables 1–4 and Fig. 3 give single numbers. RL with dual ascent is notoriously seed-sensitive; the 191% feasibility gain rests on 0.340 vs. 0.117 with no spread. The Fig. 2 label "mean ± SD" is unexplained.
- **Suggested Fix**: 5 seeds for CLAUSE and the three trainers (≈ 5× training cost); report mean ± SD and training curves of EM and dual variables.

### W6: Reproducibility details are missing (§4, §5)
Reward definition, scorer architectures, w1–w4, H, η, PID settings, reader model for CLAUSE, hardware, how latency is measured (§3 calls steps a "latency proxy", Table 2 reports "average latency"), and code are not given; algorithms and proofs sit in "Appendix ??".
- **Suggested Fix**: Provide the appendix, a hyperparameter table, the latency protocol (hardware, batch size) and anonymized code.

**Minor:** Fig. 3 panel (d) uses the dual value (0.004 vs. 0.001) as "constraint learning" strength; "Appendix ??" appears three times; Table 4 title says "Core ablations on MetaQA" without hop.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | §5.1 "Average Edge Budget" vs. Table 3 | "CLAUSE achieves the smallest edge budgets across all settings (0.74–0.90)" | Table 3: LightRAG 0.75 < CLAUSE 0.77 (MetaQA 1-hop); 0.82 < 0.90 (3-hop); ties at 0.78 (HotpotQA, 2-hop) | Cross-referenced two locations | High | MAJOR | Correct the text; discuss LightRAG trade-off |
| ERR-2 | E1 | §5.1 "Latency" vs. Table 2 | "its latency is close to or below Hybrid/GraphRAG" | HotpotQA 1.48 vs. Hybrid 1.18 (+25%); FactKG 1.36 vs. 1.15 (+18%) | Recomputed from Table 2 | High | MINOR | Qualify the sentence |
| ERR-3 | E6 | Table 4 vs. Table 1 | "w/o Subgraph Architect (StaticRAG; no-KG)" | 74.8 EM vs. Vanilla RAG 37.6 / Hybrid RAG 41.5 (MetaQA-2-hop); "no-KG" variant has edge budget 1.44× | Cross-referenced | Medium (depends on the unstated hop setting and variant definition) | MAJOR | Define variant and hop; reconcile |
| ERR-4 | E6 | Eq. 1 vs. §4.5 and Abstract | "for hard guarantees" | Eq. 1 constrains expectations E[C] ≤ β, not per-query cost; feasibility is 0.340 (§5.1) | Cross-referenced | High | MAJOR | State expectation vs. per-episode semantics; soften "guarantees" |

## Missing References
*(Domain Reviewer's task; none added here.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Accuracy gains are real in-paper, but deployment claims and baselines are under-controlled (W1, W2, W4) |
| Clarity | 2 | Method is understandable, but essential details sit in a missing appendix |
| Significance | 2 | Useful if the control claim were demonstrated; currently shown on one templated KGQA benchmark family |
| Originality | 2 | Known RL components combined for a new control target (see R2) |

## Dimension Scores (0–100)
**Pool position:** better than about 32% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper's main selling point (budget-controllable, predictable behavior) is not measured, baselines are not budget-matched, and no variance is reported for an RL method.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Eq. 1 vs. per-query claims; unspecified training of price-conditioned policy; unverified convergence |
| Clarity & Presentation | 50 | Developing | Dense, "Appendix ??" ×3, undefined metrics |
| Novelty & Originality | 48 | Developing | Composition of known CTDE/Lagrangian ingredients |
| Significance & Impact | 46 | Developing | Controllable cost would matter; evidence is narrow |
| Experimental Validation | 42 | Developing | Single runs, unmatched budgets, one-setting constraint test |
| Reproducibility | 32 | Developing | No code, hyperparameters, compute, splits |
| Ethical Compliance | 55 | Competent | Low-risk data; no limitations section |

## Questions for Authors
1. Were CLAUSE and all baselines evaluated on the same test queries, and was CLAUSE trained on the datasets' own training sets while baselines were zero-shot? A matched trained baseline would raise my Experimental Validation score; a "yes, zero-shot only" would lower it.
2. Provide EM at three or more caps/prices from one checkpoint (the promised Pareto frontier). This is the single result that would most change my assessment.
3. Which MetaQA hop does Table 4 use, and what exactly is "StaticRAG; no-KG"?
4. Published results for KG-Agent and trained KGQA systems on MetaQA are, to my recollection, substantially higher than the numbers in Table 1 [verify]; were baselines re-run under a different protocol (EM@1 vs. Hits@1, different reader)?
5. Does the appendix report seeds and variance?

## Limitations Assessment
**Partially.** There is no limitations section; the paper does not discuss single-benchmark-family evaluation, training cost, or the 0.340 feasibility rate as a limitation.

## Ethics Review Flag
**No**: public QA benchmarks; no human data.

## Overall Score
**2**: Gains are plausible, but the evaluation does not test the paper's main claim (controllable budgets) and the baseline comparison is under-specified.

## Confidence
**4**: I checked the tables and arithmetic directly; I could not see the appendix or figures.

---

# Peer Review Report

## Paper: CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering
## Reviewer: Prof. Abiodun Casterman, Domain Reviewer (public research university, West Africa; fictional persona)
## Expertise: knowledge-graph QA; neuro-symbolic reasoning; LLM+KG retrieval
## Date: 2026-11-10

## Summary
CLAUSE proposes to learn how a KG-based context is assembled for a reader LLM: which edges to add or remove, how far to walk, and which snippets to keep, with explicit penalties on edges, steps and tokens. The authors position it between fixed k-hop retrieval, LLM agent loops (ReAct, AutoGen, KG-Agent) and RL path-walkers (MINERVA), and contribute a multi-head Lagrangian MAPPO variant to train it.

## Strengths
### S1: A reasonable gap in related work
Related Work (§2.2) makes a fair case that most KG-RAG pipelines fix hop limits and top-k, and few optimize construction, traversal and selection jointly under explicit costs.

### S2: Sensible choice of baseline families
Table 1 includes zero-retrieval LLMs, RAG variants (including GraphRAG, LightRAG), LLM agents and a KG-specific agent (KG-Agent), and the constrained-RL comparison includes RCPO and MAPPO (§5, Fig. 3).

### S3: Positioning of the RL side is explicit
§2.2 ("MARL and constrained optimization") states precisely what LC-MAPPO is meant to fix in COMA, QMIX, MAPPO and RCPO, which makes the intended novelty checkable.

## Weaknesses

### W1: The algorithmic novelty of LC-MAPPO is incremental and under-differentiated (§4.4, §2.2)
The ingredients are all cited: MAPPO, COMA-style counterfactual advantages, a QMIX monotonic mixer, per-cost heads, projected dual ascent and PID Lagrangian control (Achiam et al.; Stooke et al.). Multiple Lagrange multipliers for multiple constraints are standard in constrained RL, so "separate cost heads and duals" (Contribution (6)) is a configuration choice rather than a new method. The related work criticizes QMIX because it "can misattribute credit when joint action values are non-monotonic", yet §4.4 uses a monotonic mixer for every head; the text does not say why that is acceptable here. The related work does not discuss existing Lagrangian or constrained variants of MAPPO from the safe multi-agent RL literature (see Missing References), which are the natural prior art for a "Lagrangian-constrained MAPPO".
- **Suggested Fix**: Add a delta table against safe/constrained MARL methods, and justify or ablate the mixer and counterfactual advantage choices.

### W2: Positioning against KG-LLM reasoning and RL-trained retrieval agents is incomplete (§2.2, Table 1)
Table 1's strongest trained KGQA competitor is KG-Agent; widely used LLM-KG pipelines that retrieve subgraphs or paths for a reader (Think-on-Graph, Reasoning-on-Graphs, GNN-RAG, SubgraphRAG) and trained KGQA systems on MetaQA (e.g., NSM, GraftNet) are not compared, and evaluation avoids WebQSP/CWQ, the standard KGQA benchmarks for these. §2.2 also lumps GRPO/DPO together as learning "from static pairwise/group preferences over complete responses in bandit-like, text-only settings", which does not describe GRPO as used in DeepSeekMath (the cited source: online sampled groups with relative advantages); RL-trained search/retrieval agents are not discussed.
- **Suggested Fix**: Compare to at least two of these on a standard benchmark, or explain why they are out of scope; revise the GRPO characterization.

### W3: Several citations do not support the claims attached to them (§1, §2.2, §5, References)
(a) MetaQA is attributed to "Puerto et al., 2023", whose bibliography title is "MetaQA: Combining expert agents for multi-skill question answering", a different work from the 1/2/3-hop movie KGQA benchmark generally called MetaQA (that benchmark is, to my knowledge, from a 2018 variational-reasoning KGQA paper [verify]). (b) The claim that "Fixed k-hop expansions serialize many triples, inflating token mass and latency" is supported only by two LLM-efficiency surveys (Zhou et al., 2024; Wan et al.), which do not address KG expansion. (c) The Press et al. entry carries a stray note ("Introduces Self-Ask with tool calls") and a garbled author list, and several references lack years (Wan, Wu, Ma, Shen, Liu). 
- **Suggested Fix**: Cite the original dataset paper; support the k-hop claim with KG-specific evidence (ideally the authors' own measurement); clean the bibliography.

### W4: "Neuro-symbolic" and "auditable/provenance-preserving" are asserted, not evaluated (§2.1, Abstract)
§2.1 relaxes neuro-symbolic to "differentiable logic is unnecessary", so the label applies to any scorer over graph actions. The abstract's "provenance-preserving" contexts are never measured (no faithfulness, path-validity or human-audit evaluation); the single case study (§5.3, Fig. 4) is one co-star question.
- **Suggested Fix**: Add a provenance metric (e.g., fraction of answers whose cited path is gold-supporting) or drop the claim from the abstract.

**Minor:** the novelty of "context engineering" as a term is overstated for what is learned retrieval selection; "Appendix ??".

### Literature-check addendum (strict, cutoff 2025-09-24)
- **Status:** the literature check was attempted through `scripts/related_search.py` (fingerprint written; paper excluded by title, method names and phrases). Queries reached the arXiv API but it returned **HTTP 429 (rate limiting)** on every attempt, including a retry, so **no results were kept** (1 claim query logged, 0 kept, 0 expansion queries, no similarity run). Per the skill, I fell back to knowledge: no novelty verdicts, delta table or baseline scout table can be given from retrieved abstracts, and all recommended references are marked `[verify]`. The ledger is `search_ledger.jsonl`.
- **Per-claim novelty from knowledge (not search-backed, `[verify]`):** C1 problem framing: medium (budget-aware retrieval has precedents in adaptive retrieval, cited as Jeong et al.; Zhang et al.); C2 three-agent KG controller: medium; C3 LC-MAPPO: incremental; C4 and C5 are results claims, not novelty claims.
- **Closest prior work (from the paper's own related work and my knowledge):** MINERVA (Das et al., 2018, cited) for RL path-walking on KGs; KG-Agent (cited); MAPPO with Lagrangian constraints from safe MARL (uncited).
- **Field snapshot (from knowledge, 150 words):** Three to five years ago KGQA meant embedding or GNN-reader systems with subgraph retrieval; since 2023 the dominant recipe is LLM reasoning over retrieved subgraphs or paths (Think-on-Graph, Reasoning-on-Graphs, GNN-RAG, SubgraphRAG), evaluated mainly on WebQSP and CWQ. In 2025 attention moved to RL-trained search and retrieval agents with outcome rewards and to agentic GraphRAG variants. Open problems named by this work include cost-aware retrieval, stopping, and provenance. A significant contribution now is a controllable accuracy/cost trade-off shown across several operating points on standard benchmarks against strong trained baselines, or a clear capability gain; a gain over zero-shot RAG on a templated benchmark is expected, not significant. This was used to score Significance and Novelty.

## Missing References
*Citation-integrity rule applied: all entries are from my knowledge and marked `[verify]`; none could be checked with the search tool (HTTP 429).*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Gu et al., "Multi-Agent Constrained Policy Optimisation" (safe MARL, with a MAPPO-Lagrangian baseline), arXiv 2021 / journal version later `[verify]` | Closest prior art for a Lagrangian-constrained MAPPO; the novelty delta must be argued against it |
| Critical | Sun et al., "Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph", ICLR 2024 `[verify]` | LLM-driven KG exploration for multi-hop QA; same task family as the agent baselines |
| Important | Luo et al., "Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning", ICLR 2024 `[verify]` | Path-based, provenance-oriented KGQA with LLMs; relevant to the provenance claim |
| Important | Mavromatis and Karypis, "GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning", 2024 `[verify]` | Learned subgraph retrieval for a reader LLM |
| Important | Li et al., "Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation" (SubgraphRAG), ICLR 2025 `[verify]` | Trained subgraph retriever with budget-sized context; direct competitor to the Curator |
| Important | Zhang et al., "Variational Reasoning for Question Answering with Knowledge Graph", AAAI 2018 `[verify]` | Source of the 1/2/3-hop MetaQA benchmark |
| Helpful | He et al., "Improving Multi-hop Knowledge Base Question Answering by Learning Intermediate Supervision Signals" (NSM), WSDM 2021 `[verify]` | Trained MetaQA baselines are much stronger than those in Table 1 (to my recollection) |
| Helpful | Recent RL-trained search/retrieval-agent preprints (2025), e.g., Search-R1-style outcome-reward training `[verify]` | Worth discussing only (recent preprints); not a required comparison |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in baselines and citations |
| Clarity | 2 | Related work reads well; some mis-citations |
| Significance | 2 | Narrow benchmark family |
| Originality | 2 | Novel composition; algorithm incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a reasonable idea in a crowded area, with the closest prior art (constrained MARL, LLM-KG retrievers) uncited and no comparison to modern trained KG-RAG systems.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | QMIX mixer vs. its own critique of monotonicity; convergence deferred |
| Clarity & Presentation | 55 | Competent | Related work is clear; citation slips |
| Novelty & Originality | 50 | Developing | Composition of cited components; incremental algorithm |
| Significance & Impact | 52 | Developing | Relevant problem, narrow evidence |
| Experimental Validation | 48 | Developing | Baseline set omits the modern LLM-KG pipelines |
| Reproducibility | 40 | Developing | Missing appendix and details |
| Ethical Compliance | 58 | Competent | No limitations discussion |

## Questions for Authors
1. What is the precise difference between LC-MAPPO and a MAPPO with several Lagrange multipliers from the safe-MARL literature? A clear technical delta, supported by an ablation, would raise Novelty.
2. Why use a monotonic mixer when §2.2 criticizes monotonic mixing?
3. How does CLAUSE compare with SubgraphRAG- or GNN-RAG-style retrievers under the same reader and token cap?
4. Which source defines the MetaQA benchmark used (hop-wise movie KG)?

## Limitations Assessment
**Partially.** No discussion of when learned control fails or of domain transfer.

## Ethics Review Flag
**No**.

## Overall Score
**3**: A reasonable, practically motivated idea whose algorithmic contribution is incremental and whose positioning omits the closest prior art.

## Confidence
**4**: Strong on KGQA; the literature check could not retrieve results, so some positioning points rest on memory (marked `[verify]`).

---

# Peer Review Report

## Paper: CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering
## Reviewer: Dr. Soraya Beltrami-Nakamura, Perspective Reviewer (database-systems group, public research university, East Asia; fictional persona)
## Expertise: learned query optimization; cost-based planning; auditability
## Date: 2026-11-10

## Summary
The paper turns "how much of the graph to read, how far to walk, and how much text to hand the LLM" into a learned, priced decision. From a systems perspective this is a learned query planner with a cost model whose prices the operator can set. The authors show better accuracy and cost than several RAG and agent baselines on three QA datasets.

## Strengths
### S1: Cost as a first-class objective
Exposing per-query caps or prices (§3, §4.5) resembles cost-based optimization in databases and is what practitioners need; most KG-RAG papers report cost only afterward.

### S2: Discrete, inspectable actions
Edits, traversal and curation are discrete symbolic actions with a step-level trace (§4.5, §5.3), which is a good basis for debugging and audit compared to free-form agent loops.

### S3: Cost attribution at the source
"Costs are attributed at source" (§4.3) decomposes credit assignment sensibly and is transferable to other pipelines (e.g., SQL-plus-LLM planners).

### S4: Honest separation of three resources
Edges, steps and tokens are different bottlenecks (graph store, orchestration, reader); modeling them separately is more realistic than a single "cost".

## Weaknesses

### W1: "Latency" is a proxy, not a measurement, for deployment (§3, Table 2, §5.3)
Section 3 calls interaction steps a "latency proxy"; Table 2 reports normalized "average latency" without hardware, batch size, graph store, or whether reader-LLM time (usually dominant) is included. The only absolute number is 238.6 ms in the case study (§5.3). An operator cannot map these ratios to service-level targets.
- **Suggested Fix**: Report wall-clock latency with hardware and batch size, split into graph operations, scorers and reader; report p50/p95, since the paper stresses "predictable" runtime.

### W2: How would an operator choose prices λ or caps β? (§4.5)
The paper offers two knobs but gives no calibration procedure, no sensitivity analysis and no guidance for per-query variation. Query difficulty differs; a fixed cap may starve hard queries. Compare with anytime or adaptive-computation methods and learned query optimizers with cardinality feedback.
- **Suggested Fix**: Add a sensitivity study and a recipe (e.g., fit λ from a target latency percentile); discuss adaptive-computation baselines.

### W3: Scale and shift assumptions are untested (§5, Table 1)
MetaQA is a templated movie KG with a handful of relation types; CLAUSE learns edge scoring on it. Whether the policies transfer to a large, heterogeneous KG (Wikidata-scale degree distributions), a changed KG (new facts), or unseen question types is not examined, and the HotpotQA KG construction is not described. Training cost is not reported, which matters for deployment per KG.
- **Suggested Fix**: Add a cross-dataset transfer test (train on one, test on another), a scale test on a larger KG, and report training cost.

### W4: The "auditable" benefit is asserted, not shown (Abstract, §4.2, Fig. 4)
Traces exist, but no one checks them. In the case study the token mass (≈ 36) is far below βtok = 512, so the budget never binds, and no failure trace is shown.
- **Suggested Fix**: Add trace-validity statistics and a failure-case analysis, ideally with a small human audit.

**Minor:** no limitations or broader-impact paragraph; Fig. 2 gives family averages only.

## Missing References
Only lines of work (no specific papers): learned query optimization with cost models; adaptive computation / learning to stop (anytime inference); budgeted and knapsack-constrained bandits; cost-aware retrieval and ranking cascades. `[verify]` any specific paper before citing.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Deployment claims lack measurements |
| Clarity | 2 | Clear design, thin evaluation description |
| Significance | 2 | Relevant to practice if demonstrated |
| Originality | 2 | Fresh framing, familiar parts |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically meaningful framing with partial evidence; deployment claims are not yet backed by measured latency or operating curves.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Sound structure, unverified guarantees |
| Clarity & Presentation | 56 | Competent | Concept clear |
| Novelty & Originality | 55 | Competent | New framing of cost-aware context assembly |
| Significance & Impact | 58 | Competent | Practical relevance |
| Experimental Validation | 50 | Developing | Measurements not at deployment level |
| Reproducibility | 42 | Developing | No code or details |
| Ethical Compliance | 62 | Competent | Low risk, no limitations statement |

## Questions for Authors
1. Is reader-LLM time included in Table 2? If not, what is the end-to-end share of CLAUSE's controllable portion?
2. How should an operator pick λ? A sensitivity plot would raise Significance.
3. Does a policy trained on one KG work on a differently distributed KG?

## Limitations Assessment
**Partially.** No limitations section; transfer and scale are not discussed.

## Ethics Review Flag
**No**.

## Overall Score
**3**: A promising, practical framing whose deployment claims are not yet evidenced.

## Confidence
**3**: Strong on systems aspects, less sure about KGQA benchmark conventions.

---

# Peer Review Report

## Paper: CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering
## Reviewer: Dr. Hyun-woo Pellegrin, Generalist Reviewer (ML group, private research university, North America; fictional persona)
## Expertise: deep learning for NLP; typical ICLR program-committee member
## Date: 2026-11-10

## Summary
The paper contributes CLAUSE, a learned controller that decides what KG context to build for an LLM reader and when to stop, under user-specified edge, step and token budgets, trained by a constrained multi-agent PPO. It reports higher exact match and lower normalized cost than RAG and agent baselines on HotpotQA, MetaQA and FactKG, and argues the result yields predictable, auditable behavior.

## Strengths
### S1: A problem ICLR readers care about
Cost-aware retrieval for LLM reasoning is timely, and a learned stop/continue decision with explicit prices is an appealing idea (§1, §3).

### S2: Consistent empirical picture
CLAUSE leads every column of Table 1 and is cheaper than agent baselines in Tables 2–3, and the abstract's numbers are arithmetically consistent with the tables.

### S3: Readable high-level structure
The three-agent decomposition and the per-source cost attribution (§4.3) are easy to remember; Fig. 1 summarizes the pipeline compactly.

### S4: Ablations and a constrained-RL comparison are present
Table 4 and Fig. 3 show the authors tried to isolate components.

## Weaknesses

### W1: The paper's evidence for its main selling point is thin, and the contribution as claimed is broader than what is shown (§1 Contributions, §5)
The seven-item contribution list (§1) restates one method in several ways (items 2–5) and counts "Results" as a contribution. The abstract promises "predictable performance under deployment constraints", yet the evaluation consists of three table rows per dataset and one single-setting constraint plot; no budget sweep is shown (§1 p. 2 mentions sweeps, but no figure or table appears).
- **Suggested Fix**: Condense the contributions to three (problem, method, evidence) and add the sweep figure the introduction promises.

### W2: Essential content is missing from the submitted paper (§4.1, §4.4)
"Appendix ??" is cited for the algorithms (§4.1), the shadow-price proof (§4.4) and convergence (§4.4). Without these, the central training procedure (reward, scorer inputs, how budgets are sampled in training) cannot be understood from the main text, and §4.4 mixes QMIX-style mixing, COMA-style advantages, PPO and dual ascent in a few sentences.
- **Suggested Fix**: Include the appendix; give an algorithm box in the main text with the update order and a table of hyperparameters.

### W3: Key evaluation terms are undefined and figures are hard to interpret (§5.1, Fig. 2–3)
"Feasibility rate", "violation rate", "normalized cost", "constraint learning" (Fig. 3) are not defined; Fig. 3(d) treats a larger dual value as better. Fig. 2 shows token usage only as family averages with an unexplained "mean ± SD". The reader cannot tell which budget a number refers to (Fig. 3 uses edge budget = 0.5, latency budget = 0.7 against an unstated unit).
- **Suggested Fix**: Define each metric in §5; give per-method tokens in a table.

### W4: Claims and tables disagree in places (§5.1)
Examples: "smallest edge budgets across all settings" (LightRAG is lower in two Table 3 columns); the headline "+39.3 EM@1" compares against GraphRAG, while against the strongest baseline in that cell (KG-Agent 78.0) the gap is 87.3 − 78.0 = 9.3. The abstract's qualifier "strongest RAG baseline" is literal but easy to misread.
- **Suggested Fix**: Report the gain against the best baseline overall in the abstract.

**Minor:** inconsistent ">" symbols and typesetting in the case study quotes; missing years in several references; "neuro-symbolic" is used loosely (§2.1).

### ICLR criteria checklist
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly: accuracy/efficiency vs. baselines supported; budget control not | §5, Fig. 3 |
| Soundness: method specified well enough to check | Not met in main text | §4.4, "Appendix ??" |
| Presentation: terms and figures clear | Partly | Fig. 2–3 |
| Contribution: significant and well positioned | Partly | §2.2 |
| Reproducibility: details/code | Not met | §5 |
| Limitations discussed | Not met | none |

## Missing References
*(None added by this reviewer; see Reviewer 2.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thin for stated claims |
| Clarity | 2 | Missing appendix, undefined metrics |
| Significance | 2 | Timely problem, narrow evidence |
| Originality | 2 | Familiar parts, new target |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper reads as a promising but incomplete system paper; a typical accepted ICLR paper would show the claimed trade-off curves and complete method details.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Unchecked guarantees, deferred proofs |
| Clarity & Presentation | 50 | Developing | Missing appendix, undefined metrics, padded contribution list |
| Novelty & Originality | 52 | Developing | New combination for a timely target |
| Significance & Impact | 54 | Developing | Relevant but narrowly shown |
| Experimental Validation | 48 | Developing | Single runs, one constraint setting |
| Reproducibility | 40 | Developing | No code or hyperparameters |
| Ethical Compliance | 55 | Competent | No limitations section |

## Questions for Authors
1. Can you add the budget sweep promised in §1 p. 2? Its presence would move me toward borderline accept.
2. What does "feasibility rate" measure, and why is 0.340 considered strong?
3. Can the main text include the algorithm and the reward definition?

## Limitations Assessment
**No.** There is no limitations section.

## Ethics Review Flag
**No**.

## Overall Score
**3**: An interesting direction with an incomplete evidence and presentation package for an ICLR submission.

## Confidence
**4**: Familiar with the area; did not check proofs (not provided).

---

# Devil's Advocate Report

## Paper: CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering
## Reviewer: Prof. Dariusz Ellingsworth-Rao (statistics and evaluation-methodology group; fictional persona)

## Steelman
A learned controller that prices edges, steps and tokens could plausibly beat heuristic k-hop retrieval and LLM agent loops on both accuracy and cost, and the paper's tables show exactly that on three datasets, with ablations showing every component matters and a constrained-RL comparison favoring the proposed trainer.

## Core Argument Chain
1. Fixed k-hop expansion and long reasoning inflate context and latency without control (§1, citing efficiency surveys).
2. A jointly trained three-agent controller with learned STOP and Lagrangian prices avoids this (§4).
3. CLAUSE has higher EM@1 and lower latency/edges than RAG and agent baselines (Tables 1–3).
4. Removing components or duals hurts (Table 4); LC-MAPPO satisfies constraints better than alternatives (Fig. 3).
5. One checkpoint adapts to any budget or price without retraining (§4.5; §1 p. 2).
∴ budget-aware multi-agent control is what produces accurate, compact, predictable contexts.

## Strongest Counter-Argument
The paper's causal story (learned *budget-aware multi-agent control* explains the gains) is not isolated from a simpler explanation: CLAUSE is trained with an answer reward on in-distribution questions, whereas the LLM baselines are evaluated "under a shared retriever/reader" with no stated training or tuning. MetaQA questions are templated, so a policy trained on them can learn the templates; Table 4 is consistent with this reading, since the "Greedy-Hop" variant (82.1 EM, no learned traversal) already beats the strongest baseline KG-Agent (78.0 at 2-hop, Table 1) and "MAPPO (no duals)" (85.0) is within 2.3 points of the full model (87.3). The constraint machinery, the paper's most distinctive contribution, therefore accounts for at most a couple of EM points on this evidence, and the matching efficiency claim cannot be attributed to budget awareness because no baseline is run with the same step/token caps and no operating curve is shown. The deployment claim, "deliver predictable performance under deployment constraints", is contradicted in spirit by the paper's own constraint test: LC-MAPPO is feasible in 34.0% of episodes (0.340), i.e., it violates the constraints most of the time. An opponent would conclude that the paper shows a trained KGQA system beating untrained pipelines on an easy benchmark, with budget control claimed but unmeasured. A skeptic would want: (i) a trained non-agentic baseline with the same reward and reader; (ii) baselines under matched caps; (iii) EM at several budgets from one checkpoint; (iv) results on a benchmark where templates cannot be memorized.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The tables support a weaker claim (CLAUSE outperforms the listed baselines at modest cost), so the problems below are fixable by narrowing claims or adding controls; none shows leakage, fabrication or a contradiction of the main accuracy claim.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Table 1, §5 Baselines | Trained-vs-untrained confound; baselines not budget-matched; training data and baseline settings unstated (evidence supports a weaker claim) | Add trained baseline with same reward/reader; match caps; state protocols |
| DA-M2 | Scope | §4.5, §1 p. 2, Fig. 3 | "Without retraining" and "predictable" claims untested: no sweep; feasibility 0.340; Eq. 1 constrains expectations while text says per-query "hard guarantees" | Sweep β/λ; EM and violations at each; reword guarantees |
| DA-M3 | Logic (E5) | Abstract; §5.1 | Claim distortion: +39.3 is against GraphRAG (against KG-Agent in the same cell: 87.3 − 78.0 = 9.3); "smallest edge budgets across all settings" false in two columns; latency "reducing" holds only vs. agents/GraphRAG | Report vs. best baseline; correct wording |
| DA-M4 | Evidence | Table 4 vs. Table 1 | "StaticRAG; no-KG" 74.8 EM vs. RAG baselines 37.6/41.5 and a "no-KG" variant with an edge budget; hop unstated | Define variants; state hop; reconcile |
| DA-M5 | Scope | Abstract, §5.3 | "Provenance-preserving/auditable" not evaluated; one case study where βtok = 512 is far from binding (≈ 36 tokens) | Add path-validity metric and failures |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of presentation | Fig. 2 | Only family averages with unexplained "mean ± SD" |
| DA-m2 | Citation | References | Stray annotation "Introduces Self-Ask with tool calls"; missing years; k-hop claim supported by LLM-efficiency surveys |
| DA-m3 | Evidence | Fig. 3(d) | Larger dual value presented as "strongest constraint learning" |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| EM gain vs. GraphRAG, MetaQA-2-hop | +39.3 | 87.3 − 48.0 = 39.3 | Yes |
| Latency reduction vs. GraphRAG, MetaQA-2-hop | 18.6% | (1.40 − 1.14)/1.40 = 18.57% | Yes |
| Edge reduction vs. GraphRAG | 40.9% | 1 − 0.78/1.32 = 40.91% | Yes |
| Feasibility improvement | 191% | (0.340 − 0.117)/0.117 = 190.6% | Yes |
| Violation reduction | 34% | (0.880 − 0.577)/0.880 = 34.4% | Yes |
| Latency-cost reduction | 12% | (0.838 − 0.738)/0.838 = 11.9% | Yes |
| Gain vs. strongest baseline (KG-Agent), MetaQA-2-hop | not reported | 87.3 − 78.0 = 9.3 | n/a (derived) |
| "Smallest edge budgets across all settings" | 0.74–0.90 | LightRAG lower at 1-hop and 3-hop | **No** |
| Table 4 full model vs. Table 1 | 87.3 | equals 2-hop; 3-hop mean = 87.93 | Hop not stated |

## Ignored Alternative Explanations
- Training on templated in-distribution questions vs. zero-shot baselines (Table 1, Table 4 Greedy-Hop 82.1).
- Reader-side effects: shorter contexts help the reader independently of the controller; no baseline uses the same learned reranker.
- Normalization effects: all costs are ratios to Vanilla RAG (itself weak at 3-hop: 33.0 vs. 39.0 without retrieval, Table 1), which can flatter or distort cost comparisons.
- Baseline reimplementation quality: published numbers for trained KGQA systems on MetaQA are, to my recollection, higher than those in Table 1 `[verify]`.

## Missing Stakeholder Perspectives
Operators who must set β and λ per workload; users who rely on "auditable" traces; practitioners with large or changing KGs.

## Observations (Non-Defects)
The abstract's arithmetic is correct; the problem framing is clean; the paper reports costs next to accuracy; the ablation table is a good practice; Eq. 1 and the dual update are standard and written clearly.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Expectation vs. per-query mismatch; deferred proof; confounds |
| Clarity & Presentation | 52 | Understandable but undefined terms |
| Novelty & Originality | 46 | Known components |
| Significance & Impact | 45 | Unclear transfer beyond templated KGQA |
| Experimental Validation | 36 | Untested central claim; unmatched baselines |
| Reproducibility | 34 | Details absent |
| Ethical Compliance | 55 | Nothing at stake; no limitations |

## Overall: 2 | Confidence: 4

*Pool position (DA): better than about 30% of submissions to ICLR.*

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept (W6 shortened) | All specific, located; W6 partly overlaps R4-W2 |
| R1 | Question 4 (published baseline numbers) | kept as Question | Cannot be verified from the paper; recall-based, marked `[verify]`, not a Weakness |
| R2 | W3(a) MetaQA citation | kept | Bibliography entry title shows a different work; original benchmark source marked `[verify]` |
| R2 | W2 (GRPO characterization) | rewritten | Kept as a claim about §2.2 wording only; no statement about a paper's content beyond what the cited bibliography entry shows |
| R2 | "context engineering" novelty remark | moved to Minor | Terminology, not substance |
| R3 | W1–W4 | kept | W4 overlaps DA-M5 and R2-W4 |
| R3 | Missing references | kept as lines of work | No specific papers named |
| R4 | W1 | rewritten | "Padded contribution list" moved to Minor-level; main point is missing sweep |
| R4 | W4 | kept | Duplicate of R1-W3, DA-M3 |
| DA | Strongest counter-argument sentence "violates the constraints most of the time" | rewritten | Feasibility rate is undefined in the paper; phrase as "feasible in 34.0% of episodes on the paper's own metric" |
| DA | DA-M1..M5 | kept | Located, actionable |
| All | Appendix claims | none dropped | Appendix not provided; details said to be there are questions, not errors |

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer Part A: Package for the EIC

**Merged issue list and consensus classes**
| Issue | Sources | Class |
|-------|---------|-------|
| Central deployment claim (budget control without retraining, Pareto frontiers) not measured; feasibility 0.340; Eq. 1 expectation vs. "hard guarantees" | R1-W2, R4-W1, R4-W3, R3-W2, DA-M2 | CONSENSUS-4 (hinges) |
| Baseline comparison not controlled (training, budgets, tokens per method, baseline settings) | R1-W1, DA-M1 | CONSENSUS-2 (hinges) |
| Missing appendix, hyperparameters, compute, code | R1-W6, R4-W2, R3-W3 | CONSENSUS-3 |
| Text–table inconsistencies / claim distortion | R1-W3, R4-W4, DA-M3 | CONSENSUS-3 |
| Ablation confounds and Table 4 vs. Table 1 mismatch | R1-W4, DA-M4 | CONSENSUS-2 (hinges) |
| No variance, seeds, learning curves | R1-W5 | SOLO |
| Algorithmic novelty incremental; closest prior art (constrained MAPPO, LLM-KG retrievers) missing | R2-W1, R2-W2 | SOLO (R2) |
| Citation errors (MetaQA source; k-hop claim support) | R2-W3, DA-m2 | CONSENSUS-2 |
| Provenance/audit/"neuro-symbolic" claims not evaluated | R2-W4, R3-W4, DA-M5 | CONSENSUS-3 |
| Latency not measured as wall-clock | R3-W1, R1-W6 | CONSENSUS-2 |
| DA-CRITICAL | none raised | n/a |

**Integrity-scan findings:** none. **Literature check:** attempted, HTTP 429 from the arXiv API, no results kept (see R2 addendum).

**Official score computation (BEFORE, no EIC weights, no DA-CRITICAL):** see `before.json` and the score summary below.

## EIC Meta-Review (Prof. Marisol Thackeray-Yilmaz)

### The Case For and Against
- **For acceptance:** A timely idea (explicit priced budgets for KG context construction) with a clean formulation, a coherent method, consistent gains on three datasets, ablations and a constrained-RL comparison. Abstract arithmetic is correct.
- **Against acceptance:** The paper's most distinctive claim, controllable and predictable behavior from a single checkpoint, is not measured (no sweep, feasibility 0.340, expectation-only constraints). The baseline comparison is not controlled for training or budgets, Table 4 is internally inconsistent with Table 1, key sections are in a missing appendix, and the closest prior art is uncited.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "Smallest edge budgets across all settings" is false | R1 ERR-1, DA-M3, R4-W4 | §5.1 vs. Table 3 | **Verified** | LightRAG 0.75 < 0.77 and 0.82 < 0.90; ties at 0.78 twice; only FactKG is strictly smallest |
| Latency "close to or below Hybrid/GraphRAG" | R1 ERR-2 | §5.1 vs. Table 2 | **Verified** | HotpotQA 1.48 vs. Hybrid 1.18; FactKG 1.36 vs. 1.15; small point |
| No budget/price sweep despite "Requirement sweeps reveal…" | R1-W2, R4-W1, DA-M2 | §1 p. 2; whole paper | **Verified** (as to the provided text) | Searched all tables/figures; none varies β/λ. Appendix not provided, so unverified whether it holds a sweep |
| Feasibility 0.340 vs. "hard guarantees"; Eq. 1 is expectation-based | R1 ERR-4, DA-M2 | Eq. 1, §4.5, §5.1 | **Verified** | Feasibility undefined, so "violated most of the time" is Partly correct; the 0.340 value is the paper's own |
| Headline +39.3 is against GraphRAG; against KG-Agent 9.3 | DA-M3, R4-W4 | Abstract, Table 1 | **Partly correct** | Arithmetic correct; the qualifier "strongest RAG baseline" is literal (GraphRAG 48.0 > Hybrid 41.5 at 2-hop); selection of comparator is a framing concern, not an error |
| Table 4 "no-KG" 74.8 vs. Table 1 RAG 37.6/41.5; no-KG with edges | R1 ERR-3, DA-M4 | Table 4, Table 1 | **Verified** (discrepancy); cause unknown | Hop and variant definitions unstated |
| Greedy-Hop 82.1 > KG-Agent 78.0 so gains not from navigator alone | DA counter-argument | Table 4 vs. Table 1 | **Partly correct** | True only if Table 4 is 2-hop; the hop is unstated |
| MAPPO (no duals) within 2.3 EM of full | DA | Table 4 | **Verified** | 87.3 − 85.0 = 2.3; but edges 1.28× vs. 1.00× is also a real cost gap |
| MetaQA cited as Puerto et al. 2023 | R2-W3 | References | **Verified** (bibliography title); source of hop benchmark `[verify]` | |
| k-hop claim supported only by LLM-efficiency surveys | R2-W3 | §1, §2.2, References | **Verified** | Titles are "Efficient large language models: A survey" and "A survey on efficient inference for large language models" |
| GRPO/DPO characterized as static preference learning | R2-W2 | §2.2 | **Partly correct** | Plausible concern about GRPO; cannot be checked against a fetched source; weight accordingly |
| Case study budget never binds (≈ 36 tokens vs. 512) | R3-W4, DA-M5 | §5.3 | **Verified** | |
| R1 Q4: published baseline numbers are higher | R1, DA | Table 1 | **Unverifiable** | Recollection only, marked `[verify]`; not used in the decision |
| Single run / no variance | R1-W5 | Tables 1–4 | **Verified** (absence after search) | |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error-log entries ERR-1, ERR-2, ERR-4 verified; ERR-3 verified as a discrepancy; arithmetic all correct; well calibrated |
| R2 (Domain) | 3 | 4 | 1.0 | Citation points verified; several positioning points rest on memory (`[verify]`) and the lit-check failed |
| R3 (Perspective) | 3 | 3 | 1.0 | Points verified (case-study budget, latency definition); somewhat generic otherwise |
| R4 (Generalist) | 3 | 4 | 1.0 | Points verified; overlaps R1 |
| DA | 2 | 4 | 1.0 | Counter-argument largely survives (M1–M4 verified), but "Greedy-Hop beats KG-Agent" depends on an unstated hop, and "violates constraints most of the time" over-reads an undefined metric |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a (no DA-CRITICAL; no ceiling) | n/a |

### Official ratings → EIC assessment
Official ratings: R1 2, R2 3, R3 3, R4 3, DA 2 → plain mean **2.60**. EIC-weighted (confidence × quality weight) rating: ≈ **2.56**, rounded half up → starting point **3**. The weighted composite (≈ 48, Reject band) is a cross-check one step below the rating; because the weighted rating sits within 0.1 of x.5 and the composite is within 2 points of a band edge, I treat the disagreement as a borderline signal and not as grounds to depart.

### Final Decision and Justification
The reviewers' recommendations (2/3/3/3/2) and my own reading agree that this is a below-the-bar submission with a real idea. I keep the starting point **3 (Borderline Reject)**, not 2: the in-paper results are internally consistent in arithmetic, the formulation is clear, nothing indicates leakage or fabrication, and the verified weaknesses (an untested central claim, uncontrolled baselines, an inconsistent ablation, a missing appendix) are fixable with experiments the authors can plausibly run; none contradicts the main accuracy result. I do not go to 2 because no verified issue shows the evidence contradicts the central accuracy claim, and the three most serious defects are already reflected in the reviewers' ratings. I do not go higher because the claim that distinguishes this paper from a trained KGQA pipeline (controllable cost without retraining) is exactly the one not measured. No DA-CRITICAL issue was raised, so there is no ceiling; the decision is 3. **My pool position: better than about 35% of ICLR submissions.** Deciding evidence: the headline selling point is unmeasured, and baselines are not matched on training or budgets; a typical accepted paper shows the operating curves.

### Editorial Decision Letter
Dear Authors,

Thank you for submitting "CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering" to ICLR.

Learning how a knowledge-graph context is assembled, with explicit prices on edges, steps and tokens, is a timely and well-motivated direction.

**Overall Assessment:** The panel found a clearly stated problem, a coherent three-agent design, consistent accuracy gains on three datasets and correct headline arithmetic. It also found that the paper's distinctive claim, adaptation to per-query budgets from one checkpoint with predictable behavior, is not demonstrated in the submitted text, and that the comparison and ablations leave several confounds open.

**Key Strengths Identified by Reviewers:**
1. A clean, deployment-relevant formulation with per-resource costs (R1, R3, R4).
2. Best EM@1 in every column of Table 1 with lower edge and latency cost than agent baselines (R1, R4).
3. Ablations and a constrained-RL comparison are included (R1, R4).

**Key Concerns Requiring Attention:**
1. No budget or price sweep supports the "without retraining / predictable" claim; feasibility is 0.340 and Eq. 1 is expectation-based (CONSENSUS-4).
2. Baselines are not controlled for training, caps or per-method tokens; Table 4 conflicts with Table 1 (R1, DA).
3. The appendix is missing from the text ("Appendix ??"); hyperparameters, compute, seeds and code are absent (CONSENSUS-3).
4. Text claims exceed the tables (smallest edge budget, headline comparator) (CONSENSUS-3).
5. Closest prior art for constrained MAPPO and modern LLM-KG retrievers is not discussed (R2); `[verify]` the references listed.

**Decision: Borderline Reject (3)** (ICLR rating label from the script below). A revision would be reconsidered positively if it shows EM against several budgets/prices from one checkpoint, matched-budget and trained baselines, variance over seeds, a consistent Table 4, and the missing appendix.

Sincerely,
Prof. Marisol Thackeray-Yilmaz, Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Central deployment claim unmeasured | R1, R3, R4, DA (+R2 indirectly) | CONSENSUS-4 |
| Missing appendix / reproducibility details | R1, R3, R4 | CONSENSUS-3 |
| Text–table inconsistency / claim distortion | R1, R4, DA | CONSENSUS-3 |
| Provenance / audit / neuro-symbolic claims unevaluated | R2, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Strength of the accuracy gains | R4 S2, R1 S2 (consistent, large at 2/3-hop) | DA (confounded by training vs. zero-shot) | EIC: gains are real in the paper's own protocol; attribution to budget awareness is unestablished |
| Novelty | R3 (fresh framing) | R2 (incremental algorithm) | EIC: framing is moderately novel, algorithm incremental; consistent with a rejected-band submission |

### Score Spread Discussion
See the aggregation tables below; no dimension has a spread above the 20-point warning threshold except as flagged by the script.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Trained-vs-untrained confound, unmatched caps | Partly (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Budget control untested | Yes (R1, R3, R4) | n/a | n/a |
| DA-M3 | MAJOR | Claim distortion | Yes (R1, R4) | n/a | n/a |
| DA-M4 | MAJOR | Table 4 vs. Table 1 | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Provenance unevaluated | Yes (R2, R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Show the claimed budget/price control | R1-W2, R4-W1, R3-W2, DA-M2 | §1 p. 2, §4.5, Fig. 3 | EM, latency and violation rate at ≥ 4 caps and prices from one checkpoint; define "feasibility"; reword "hard guarantees"; explain training under varied β/λ | High; ~20–40 GPU-h | Partly |
| R2 | Control the baseline comparison | R1-W1, DA-M1 | Tables 1–3, §5 | Per-method tokens/steps/latency; baselines under matched caps; trained non-agentic baseline with same reward and reader; state splits, tuning, baseline settings | High; ~30 GPU-h | Partly |
| R3 | Repair the ablation | R1-W4, DA-M4 | Table 4 | State hop; define variants; reconcile 74.8 vs. 37.6/41.5; add single-agent LC-PPO and RCPO with EM; all hops | Medium; ~15 GPU-h | Yes |
| R4 | Provide the missing appendix and details | R1-W6, R4-W2 | §4.1, §4.4, §5 | Algorithms, proofs/convergence assumptions, reward, hyperparameters, compute, latency protocol, code | Medium | Yes |
| R5 | Correct claims that exceed the tables | R1 ERR-1/2, R4-W4, DA-M3 | Abstract, §5.1 | Fix "smallest edge budgets"; report gain vs. best baseline | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No variance/seeds/curves | R1-W5 | 5 seeds; mean ± SD; training curves | Medium; ~5× training | Partly |
| S2 | Incremental algorithm vs. constrained MAPPO; modern LLM-KG retrievers | R2-W1, R2-W2 | Delta table; compare ≥ 2 retrievers on a standard KGQA benchmark | Medium | Partly |
| S3 | Citation fixes | R2-W3, DA-m2 | Original MetaQA source; KG-specific evidence for k-hop claim; clean bibliography | Low | Yes |
| S4 | Provenance/audit unevaluated | R2-W4, R3-W4, DA-M5 | Path-validity metric; failure cases | Medium | Partly |
| S5 | Latency measurement | R3-W1 | Wall-clock with hardware, split by component, p50/p95 | Low–Medium | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Operator guidance for choosing λ, β | R3-W2 | Sensitivity analysis and recipe |
| N2 | Transfer and scale | R3-W3 | Cross-dataset and larger-KG tests |
| N3 | Contribution list and terminology | R4-W1, R2 | Condense; define "neuro-symbolic" use |
| N4 | Fig. 2/3 presentation | R4-W3, DA-m1/m3 | Per-method token table; define metrics |

## Estimated Revision Effort
- Priority 1: 5 items, roughly 1–2 weeks including ~70–100 GPU-hours.
- Priority 2: 5 items, about 1 week.
- Priority 3: 4 items.
- **Total estimated revision time**: 2–3 weeks.

---

## Score Summary

*Produced by `scripts/aggregate_scores.py --venue iclr` from `scores_before.json` (BEFORE: no EIC weights, no DA-CRITICAL) and `scores.json` with `--final 3` (AFTER). Outputs: `before.json`, `aggregate.json`.*

### Official Scores and EIC Assessment

| Reviewer | Overall | Confidence | EIC weight | Own composite | Pool position |
|----------|---------|------------|------------|---------------|---------------|
| R1 (Methodology) | 2 | 4 | 1.25 | 45.8 | 32 |
| R2 (Domain) | 3 | 4 | 1.0 | 50.6 | 40 |
| R3 (Perspective) | 3 | 3 | 1.0 | 53.8 | 45 |
| R4 (Generalist) | 3 | 4 | 1.0 | 50.0 | 38 |
| DA | 2 | 4 | 1.0 | 43.4 | 30 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 48 | 52 | 54 | 50 | 42 | 49.2 | 49.0 | 12 |
| Clarity & Presentation | 50 | 55 | 56 | 50 | 52 | 52.6 | 52.4 | 6 |
| Novelty & Originality | 48 | 50 | 55 | 52 | 46 | 50.2 | 49.9 | 9 |
| Significance & Impact | 46 | 52 | 58 | 54 | 45 | 51.0 | 50.5 | 13 |
| Experimental Validation | 42 | 48 | 50 | 48 | 36 | 44.8 | 44.5 | 14 |
| Reproducibility | 32 | 40 | 42 | 40 | 34 | 37.6 | 37.2 | 10 |
| Ethical Compliance | 55 | 58 | 62 | 55 | 55 | 57.0 | 56.7 | 7 |
| **Composite** | | | | | | **48.7 (before)** | **48.4 (after)** | |

- Official rating (plain mean of Overall): **2.60**. EIC-weighted rating: **2.56**, starting point **3**. Composite band: 2 (Reject): the cross-check flag is the one discussed in the meta-review (weighted rating within 0.1 of x.5; composite 1.6 points below the band edge at 50), treated as a borderline signal, not as a reason to depart. DA ceiling: none. No consistency warnings were raised. **Final (EIC): 3.**
- No dimension exceeds the 20-point spread threshold.

### Target-Venue Scores (ICLR, scale status: secondary; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating label for final Overall 3 | **4 on {0,2,4,6,8,10}** (5 on the earlier {1,3,5,6,8,10} scale) |
| ICLR-weighted composite | 48.3 |

**Venue recommendation:** ICLR rating 4 on {0,2,4,6,8,10}, "marginally below the bar". Heuristic simulation, not a prediction.

### Notes on the process
- Literature check: strict mode, cutoff 2025-09-24; one claim query reached the arXiv API, which returned HTTP 429 on every attempt (three tries over two invocations); no results were kept, so the Domain Reviewer's recommended references are all marked `[verify]` and no novelty verdicts, similarity or baseline scout could be run from retrieved abstracts.
- The five reviewer passes shared one model context; independence is by role instruction only.
