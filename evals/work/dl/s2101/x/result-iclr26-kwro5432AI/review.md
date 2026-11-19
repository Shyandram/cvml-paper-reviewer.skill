# Simulated Review: "Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization" (STAR-RAG)

*Date: 2026-11-05. Request: full review, target venue ICLR, skip confirmation, literature check strict, cutoff 2025-09-24. This is a simulation of how a careful panel would likely see this draft, not a prediction. All five reviewers were run as separate role-based passes in one model context (no subagents), so they share one context; independence is by instruction only. Figures were not available: Figures 1–3, 5–7 are judged from captions, extracted text and the numeric grid of Figure 5 only.*

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## Paper Analysis

| Item | Finding |
|------|---------|
| Title | Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization |
| Primary Discipline | ML / NLP → retrieval-augmented generation over (temporal) knowledge graphs |
| Secondary Discipline(s) | Data mining (graph summarization, MDL), temporal knowledge graph QA |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Apriori-mined entity labels → rule-node graph; MDL edge selection; seeded personalized PageRank (PPR); frozen LLM (Llama-3.3-70B AWQ) |
| Target Venue | ICLR (top-tier ML conference; stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | None. Pool base rate ≈ 27% accepted (venue_profiles.md) |
| Paper Maturity | Submission-ready draft (no limitations section, no code statement) |
| Ethics-Relevant Content | None (public event/Wikidata KGs, no human subjects) |

### Claimed Contributions (as stated by the authors; ledger IDs used throughout)
1. **C1.** A temporal GraphRAG framework, STAR-RAG, for accurate and token-efficient temporal QA, training-free (Abstract; §1 bullets 1 and 3).
2. **C2.** A time-aligned *rule graph*: entity labels from Apriori, rule nodes ⟨c_s, r, c_o⟩, edges selected by an MDL criterion with a temporal-span term (§1 bullet 2(i); §3.2; Eqs. 1–7; Appendices A–B).
3. **C3.** Seeded personalized PageRank over the rule graph to focus retrieval on a "time-aligned subgraph" (§1 bullet 2(ii); §3.3; Eq. 8; Appendix C).
4. **C4 (result).** "improves answer accuracy by 9.1% while reducing token usage by 97.0%" vs. MedicalGraphRAG (§1, last paragraph).

## Paper memory (shared factual record)

- **Setup:** Datasets CronQuestion, Forecast, MultiTQ (Table 1, §4.1). Test protocol: "we randomly sample 1,000 questions from the test set of each dataset and report the average performance over five runs" (§4.1). What varies across the five runs is not stated; no variance reported. Splits for tuning: **not stated after protocol sweep** (the only selection sentence is §4.4: "we tune the hyperparameters of each baseline and report their best achievable performance"; split unspecified). Embeddings NV-Embed for "all methods" (§4.3). LLM Llama-3.3-70b-instruct-awq by default (§4.3); K1=10, K2=20, ε=1e-5, α=0.2 (§4.3, §3.3); θ=0.6, β=0.7, τ=1/|U_seed| (Appendix C). Hardware: Xeon Silver 4314, 500 GB RAM, 4×RTX A30 (§4.3). Seeds, K_type, Apriori support threshold, edge weights of Ã, code/data availability: **not stated after search**.
- **Headline numbers:** Table 2 (Hit@1/5/10 on three datasets); Table 3 (MultiTQ Hit@1 single vs. multiple events, STAR-RAG 25.8 / 44.4); Figure 3 (tokens 20,453 for MedicalGraphRAG vs. 601 for STAR-RAG, MultiTQ; §4.4); Table 4 (ablations and backbone swap); Figure 5 (K1×K2 grid, MultiTQ Hit@1).
- **Appendix adds:** Algorithm 2 (entity labeling), MDL model cost L(M) (Appendix B), personalization vector (Appendix C), token/time plots for the other two datasets (Figures 6–7, not readable), prompt and a worked retrieval example (Appendix E).
- **Unverifiable:** all figures (Figures 1–3, 6–7 content), Figure 5 only via its extracted numbers, equations partly garbled by extraction (Eqs. 5–6 rebuilt by hand).

## Integrity scan (`integrity_scan.py`, Phase 0)

No reviewer-directed text or hidden characters found. Reviewers read the (unchanged) redacted copy. No integrity signals reported to the EIC.

## Literature check (Phase 1.5): strict, cutoff 2025-09-24

Fingerprint written (title, STAR-RAG variants, three distinctive phrases). 8 counted queries of 12 (6 claim: "temporal GraphRAG", "temporal rule retrieval LLM", "personalized PageRank GraphRAG", "knowledge graph summarization MDL" [0 results], "training-free temporal RAG", plus expansion "graph summarization description length"; 1 benchmark: "temporal knowledge graph QA"; one expansion query was refused for >4 words). Also `scout` (CronQuestions/Hits@1), `coverage`, `similarity`, `novelty`, and 2 `verify` calls. `benchmarks` detected none (the three datasets are the paper's external benchmarks; scouted by hand). Gaps left open: no relevant arXiv-only prior found for C3 (PPR-based retrieval): the arXiv search misses HippoRAG, which the paper itself cites and uses as a baseline, so this is a limit of the search. Similarity: highest cosine 0.168 (TempoQR), no text overlap, no "high conceptual overlap" flag. Closest prior works (similarity): TempoQR, KG-IRAG, GenTKG.

**Claim-level novelty profile (`related_search.py novelty`):** C1 medium (top prior: KG-IRAG, level 3, uncited), C2 high by the script (top prior GenTKG level 2) but the Domain Reviewer raises it to "medium: MDL rule summarization of KGs is established (KGist, ANOT, both cited)", C3 "no close prior work found (at most medium)", HippoRAG (cited, PPR for RAG) is the known precedent, C4 n/a. Paper reading: no central claim fully covered by prior work.

## Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ramón Iturbe, large public research university (Southern Europe)
- **Seniority / Expertise**: Senior faculty, area chair at ML venues / knowledge-graph reasoning, retrieval-augmented LLMs
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Decides on whether the central claim is measured; tolerant of ordinary weaknesses, intolerant of untested mechanisms

### Reviewer 1 (Methodology): Dr. Kavya Menon, industrial research lab (South Asia)
- **Seniority / Expertise**: Senior industry scientist / RAG evaluation, KG-based QA protocols
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched retrieval budgets and on ablations that isolate each claimed component

### Reviewer 2 (Domain): Prof. Femi Adeyemi, research university (West Africa)
- **Seniority / Expertise**: Mid-career faculty / temporal KG QA and reasoning, KG summarization
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks that every description of prior work matches the cited paper

### Reviewer 3 (Perspective): Dr. Sofia Lindqvist, database and data-management group, public university (Northern Europe)
- **Seniority / Expertise**: Mid-career / graph compression, MDL, index structures, data-management deployment
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; reads methods as systems, asks about update cost and scale

### Reviewer 4 (Generalist): Dr. Hyun-woo Baek, ML/NLP lab, university (East Asia)
- **Seniority / Expertise**: Postdoc-to-assistant-professor / LLM applications, QA
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee reader; weighs weaknesses against what accepted ICLR papers share

### Devil's Advocate: Dr. Marisol Quispe, evaluation-methodology institute (South America)
- **Seniority / Expertise**: Senior researcher / evaluation design, causal attribution of gains
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; asks whether the proposed mechanism is what produces the gain

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Reviewer: Dr. Kavya Menon, Methodology (industrial research lab, South Asia; fictional persona)
## Expertise: RAG evaluation; KG-based question answering protocols; retrieval-budget matching
## Date: 2026-11-05

## Summary
STAR-RAG retrieves events for temporal KG question answering without training. It labels entities by frequent relation sets, maps events to rule nodes, links rule nodes by Hamming-1 neighbourhood with an MDL criterion that includes an exponential model of time spans, and at query time runs seeded personalized PageRank from the top-K1 cosine-similar events. Events in the top-K2 rule nodes are re-ranked by cosine and passed to a frozen Llama-3.3-70B. It reports higher Hit@1/5/10 than seven GraphRAG baselines on three template-generated temporal KGQA datasets and a large token reduction.

## Strengths
### S1: Consistent gains over the listed baselines on three datasets
Table 2 shows STAR-RAG best in all nine cells; on Hit@1 the margin over the best baseline is 7.4 (CronQuestion vs. TOG), 7.7 (Forecast vs. TS-Retriever) and 5.0 (MultiTQ vs. TS-Retriever) points (derived from Table 2). Margins of this size are unlikely to be sampling noise on 1,000 questions.

### S2: Ablations isolate two components and a sensitivity grid is given
Table 4 removes the rule graph (STAR-RAG-no-rule) and replaces the personalization vector with a uniform one; the deltas quoted in §4.5 (21.6, 10.0, 12.2 and up to 8.7 points) match Table 4. Figure 5 reports a full K1×K2 grid on MultiTQ.

### S3: Efficiency is reported, not just accuracy
Tokens and latency are reported per method (Figure 3, §4.4) and the paper is candid that STAR-RAG roughly doubles latency relative to semantic search (§4.5: no-rule "roughly halves the inference time").

### S4: Appendix gives the model cost and personalization formulas
Appendices B–C give L(M), γ and its constants (θ=0.6, β=0.7), which is more than many RAG papers provide. I verified that Eq. 6 follows from an exponential MLE: −Σ log(λe^{−λd}) = |T| + |T| log(Σd/|T|).

## Weaknesses
### W1: The temporal mechanism is never tested, and Algorithm 1 never uses timestamps at retrieval time
The claim is that STAR-RAG "enforces temporal proximity during retrieval" (Abstract) and restricts retrieval to "time-aligned" evidence (§1, §3.3). In Algorithm 1 the query's temporal constraint is never parsed. The anchors are chosen by cosine similarity (line 8), PPR runs over the rule graph (lines 9–13), all events in the top-K2 rule nodes are collected (line 15) and the output is the top-K1 by cosine (line 16). Timestamps enter only offline, through the span set T_uv in Eqs. 5–6, which decides which rule-node edges survive. A rule node's support contains events from every date. The ablations (Table 4) remove the whole rule graph or the personalization vector; none removes the temporal term L_time, none replaces the Hamming-1 candidate edges, and none compares to a non-temporal category filter (relation/type match). The gain (+12 to +22 Hit@1 over STAR-RAG-no-rule) is therefore attributable to "restricting the candidate pool by event category", not demonstrably to time alignment. Because line 16 re-ranks a subset of F by the same cosine used in line 8, the final set can differ from plain top-K1 only by *dropping* top-cosine anchors whose rule nodes fall outside the top-K2; Figure 5 (K2=5: 26.3–28.3) versus no-rule 18.3 shows this dropping helps, but the paper never says why.
- **Suggested Fix:** add (a) rule graph with L_time removed and (b) a type-only/relation-only filter at equal K, (c) a timestamp-aware filter (e.g. restrict to events after/before the parsed anchor date), and report Hit@1 on the "before/after/first/last" question types (Table 3 categories). Cost: ≈ 3 variants × 3 datasets × 1,000 questions, ≈ 30 GPU-hours with the paper's setup.

### W2: Token-efficiency claim is confounded by the retrieval budget
The headline "reducing token usage by 97.0%" (§1; §4.4: "(20453-601)/20453") compares with MedicalGraphRAG, the baseline with the largest context on MultiTQ. STAR-RAG passes only K1=10 events (≈600 tokens), and the no-rule variant with K1=10 would pass the same ≈600 tokens (token counts for no-rule are not reported in Table 4). The reduction is therefore a property of the K1 cap, not of the rule graph or PPR. The statement "lowers token consumption without sacrificing accuracy" (Abstract) needs an accuracy-vs-tokens comparison at matched context length (e.g. each baseline truncated to 10 events or ≈600 tokens). Also, (20453−601)/20453 = 97.06% rounds to 97.1%, not 97.0% (derived; trivial).
- **Suggested Fix:** report tokens and Hit@1 for every baseline and for no-rule at K1∈{5,10,20,40}, and plot Hit@1 against tokens. Cost: ≈ 8 methods × 4 K1 values × 1 dataset, ≈ 20 GPU-hours.

### W3: Baseline selection and tuning protocol favour STAR-RAG's story and are under-specified
(i) The accuracy headline is against MedicalGraphRAG, described as "state-of-the-art" (§1), a medical-domain method that is far from the strongest baseline in Table 2 (CronQuestion Hit@1 50.4 vs. TOG 69.5). (ii) §4.4 says baselines were tuned "and report their best achievable performance", but no split is named; §4.1 samples from the test set and no validation split is mentioned anywhere (protocol sweep). If tuning was on the same 1,000 questions, baseline numbers are selected on test data (a question, not an accusation). (iii) §4.3 states NV-Embed is used "across all methods", yet §1 describes TS-Retriever as "training a shared encoder"; it is unclear whether TS-Retriever, the strongest temporal baseline, runs with its trained encoder. (iv) Microsoft GraphRAG and LightRAG are cited in §1 ("Edge et al., 2024", "Guo et al., 2024") but not compared, although the abstract claims gains over "strong GraphRAG baselines". (v) No supervised temporal-KGQA model is given as a reference, so the cost of "no training" in accuracy is unquantified.
- **Suggested Fix:** state the tuning split, tune on a held-out validation sample of questions and report the untouched test sample; state how each baseline was run (official code, retriever, prompt); add GraphRAG/LightRAG or explain the omission; include one trained TKGQA reference per dataset marked as an upper reference. Cost: mostly rerun, ≈ 40 GPU-hours.

### W4: No variance, and "five runs" is undefined
§4.1 says results are "the average performance over five runs" but Tables 2–4 and Figure 5 have no standard deviations, and it is not stated whether the runs resample questions, the LLM decoding seed or both. The margins in Table 2 are large, so this matters mostly for Table 4 and Figure 5, where differences of 0.1–1.0 are interpreted ("clear gain" 28.5→30.5; "marginal" 30.5→30.9).
- **Suggested Fix:** report mean ± std (state what varies) and a paired bootstrap CI for STAR-RAG vs. the best baseline.

### W5: Reproducibility gaps in the method specification
Edge weights of Ã are never defined ("formed by building edges and normalizing edge weights", §3.3). K_type (Algorithm 2 line 9), the Apriori support threshold, the edge insertion order for the greedy MDL ("fixed order", §3.2), the answer-matching rule for Hit@k, and offline cost (rule-graph build time, number of rule nodes/edges) are not stated. §3.1 claims "a much sparser rule graph" without any node/edge counts. No code link or release statement.
- **Suggested Fix:** add a table of rule-graph statistics (nodes, edges, build time, memory) per dataset and the missing hyperparameters; release code.

**Minor:** Table 4 is captioned "Figure 4" in the extracted text; "average accuracy" in that caption is Hit@1 (values equal Table 2); Llama-3.3 and NV-Embed references lack accessed dates/years ("Accessed: YYYY-MM-DD").

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1/E5 | §4.4 vs. Table 2 | "Static-graph approaches such as TOG and DALK perform notably worse than temporal methods" | CronQuestion: TOG Hit@1 69.5 > TS-Retriever 68.5 > T-GRAG 67.3; Hit@5 76.4 > 74.1, 72.9 | Cross-referenced Table 2 rows | High | MAJOR (wording; main result intact) | Qualify to Forecast/MultiTQ or drop |
| ERR-2 | E1 | §1 vs. Table 2 | "our method improves answer accuracy by 9.1%" | No Table 2 comparison with MedicalGraphRAG gives 9.1: Hit@1 diffs 26.5/9.4/9.4; nine-cell mean 57.3 vs. 44.3 (13.0). Closest: Forecast Hit@1–10 mean 49.0 vs. 39.8 (9.2) | Recomputed | Medium (dataset/metric unstated) | MAJOR | State dataset, metric, absolute vs. relative |
| ERR-3 | E1/E5 | §4.4 vs. Table 2 | "strongest baseline TS-Retriever" | On CronQuestion Hit@1 and Hit@5 the strongest baseline is TOG (69.5, 76.4), not TS-Retriever (68.5, 74.1) | Cross-referenced Table 2 | High | MINOR | Name the strongest per dataset |
| ERR-4 | E6 | §4.1 vs. Table 1 / Figure 2 | "derive temporal events from the ICEWS21 and ICEWS14 data streams" | MultiTQ has |T|=4,017 timestamps (Table 1) and Figure 2 shows events dated 2005–2011; a single-year stream cannot produce this | Cross-referenced two locations | Medium | MINOR | Name the actual ICEWS snapshot |
| ERR-5 | E6 | Appendix E | "Yemane Gebremeskel on 2005-11-24" | The "Thoughts" cite events (also "Foreign Affairs (Syria) on 2005-10-31") that are not among the 10 listed retrieval results | Cross-referenced the list | Medium | MINOR | Align the example |
| ERR-6 | E6 | §3.2 vs. Appendix B | "directed chain edges" | §3.2 defines undirected pairs {u,v} with absolute spans |t′−t|, yet §1 and Appendix B describe directed "what-follows-what" edges | Cross-referenced | High | MAJOR (it removes the before/after signal the paper motivates) | Define direction or drop the claim |

## Missing References
*(Domain Reviewer's job; see R2.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Large consistent gains, but mechanism and token claims are untested (W1, W2) |
| Clarity | 2 | Clear storyline; method has undefined pieces and inconsistent definitions (W5, ERR-6) |
| Significance | 2 | Useful training-free recipe for template-style temporal KGQA; scope narrow |
| Originality | 2 | Known pieces (MDL summarization, PPR) combined; temporal contribution not isolated |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central "time-aligned" mechanism is not isolated by any ablation (Algorithm 1, Table 4) and the efficiency headline is set by the K1 cap against a weak comparator; typical rejected submissions share a contested attribution of gains.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Method plausible, but timestamps unused at retrieval; undirected vs. directed inconsistency |
| Clarity & Presentation | 56 | Competent | Readable; undefined Ã weights, K_type, Apriori support |
| Novelty & Originality | 48 | Developing | MDL machinery borrowed (Appendix B follows Zhang et al., 2024); PPR from HippoRAG-style retrieval |
| Significance & Impact | 50 | Developing | Real efficiency interest, but evidence limited to three template datasets |
| Experimental Validation | 45 | Developing | Large gains but no variance, tuning split unstated, matched-budget comparison missing |
| Reproducibility | 42 | Developing | No code, missing hyperparameters, no offline costs |
| Ethical Compliance | 58 | Competent | Nothing at stake; but no limitations section |

## Questions for Authors
1. On which split were baseline hyperparameters and STAR-RAG's θ, β, α, K_type chosen? A validation sample would raise my score; tuning on the reported 1,000 questions would lower it.
2. What do Hit@1 and tokens look like for STAR-RAG-no-rule and for each baseline at K1=10?
3. Does any retrieval step use event timestamps or the question's anchor date? If not, how is "time-consistent" supported beyond the LLM's own reasoning?
4. How many rule nodes and edges result for each dataset, and how long does construction take?
5. What varies across the "five runs"?

## Limitations Assessment
**Partially / No.** There is no limitations section; the paper does not discuss template-generated questions, structured-KG-only scope, offline construction cost or update cost.

## Ethics Review Flag
**No**

## Overall Score
**3**: Strong empirical gains, but the paper does not show that the proposed temporal mechanism, rather than a candidate-pool cap and category filtering, produces them; fixable with ablations and matched-budget baselines.

## Confidence
**4**: Checked tables, algorithm and appendix directly; figures unavailable.

---

# Peer Review Report

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Reviewer: Prof. Femi Adeyemi, Domain (research university, West Africa; fictional persona)
## Expertise: Temporal KG QA; KG summarization; graph-based RAG
## Date: 2026-11-05

## Summary
The paper builds an MDL-selected graph over event categories and uses seeded PPR to expand from semantically retrieved events before re-ranking, positioning the result as a training-free, temporal GraphRAG. It compares with static GraphRAG methods and two temporal RAG methods on CronQuestions, ForecastTKGQuestions and MultiTQ.

## Strengths
### S1: Well-motivated gap and sensible scope of related-work axes
§1 and §2 separate static GraphRAG, MDL graph summarization and temporal KG reasoning, and identify KGist and ANOT as the closest summarization works (§2). The motivation that semantic similarity ignores temporal constraints is credible.

### S2: Includes a very recent temporal GraphRAG baseline
T-GRAG (Li et al., 2025; arXiv 2508.01680, dated 2025-08-03, i.e. concurrent with respect to the cutoff) is both cited and compared (Table 2), which is more than ECCV-style rules would require.

### S3: Uses the three standard temporal KGQA benchmarks
CronQuestions, ForecastTKGQuestions and MultiTQ are the established benchmarks (Table 1; cited as Saxena et al., 2021; Ding et al., 2023; Chen et al., 2023). Each is large (>300K events).

### S4: The rule-node abstraction is a reasonable way to transfer an MDL summarization idea to retrieval
Entity labels from relation sets (§3.2; Zhang et al., 2024) is a coherent adaptation of KGist/ANOT-style inductive rules to an indexing problem.

## Weaknesses
### W1: Novelty is largely application of existing MDL KG summarization and PPR retrieval; the genuinely new part is not isolated
Literature check (strict): KGist (Belth et al., 2020; found on arXiv, "unsupervised KG summarization with a set of inductive, soft rules") and ANOT are cited, and Appendix B states "we follow the standard formulation utilized in Zhang et al. (2024) to calculate L(M)". PPR over a KG for RAG is the core of HippoRAG (cited, a baseline). The delta is (a) a temporal-span term L_time (Eq. 6) and (b) the pairing of both for event retrieval. Since no ablation removes L_time (Table 4), the claim-level novelty of C2 reduces to "known MDL summarization applied to retrieval". Claim verdicts: C1 medium (KG-IRAG, level 3, uncited), C2 medium, C3 medium (HippoRAG precedent, cited but the contrast with it is not discussed in §2).
- **Suggested Fix:** add a delta table against KGist/ANOT and HippoRAG, and show that L_time changes the retrieved set or accuracy.

### W2: Positioning omits the temporal-KGQA line and two closest retrieval-style works
Uncited prior work on the same task: TempoQR, TwiRGCN, EXAQT (compact question-relevant subgraph retrieval, then ranking, for complex temporal questions) and KG-IRAG (GraphRAG for temporally dependent queries). None needs to be beaten (they are trained or LLM-agentic), but §2 says temporal KG methods are all "model-centric" and "depend on pairwise similarity over the full event set"; EXAQT's first stage computes a compact subgraph, which contradicts that characterization for at least one prior method [verify against the full paper; based on its abstract]. A supervised reference per dataset would also show what "no training" costs.
- **Suggested Fix:** cite and differentiate these; add one trained reference row.

### W3: Descriptions of baselines are inconsistent with the paper's own text and bibliography
DALK is "a dual-level adaptive knowledge graph to balance semantic and structural reasoning" in §4.2 but "constructs two domain-specific knowledge graphs from scientific corpora" in §2, and its bibliography title is about Alzheimer's disease QA. TOG is described as organizing "knowledge into topic-oriented subgraphs for efficient traversal" (§4.2) while its entry is "Think-on-graph: Deep and responsible reasoning of LLM on knowledge graph" [verify against the original abstract]. In §1, "Yang et al. (2025)" is offered as a model of temporal structure of *knowledge graphs* but is a time-series forecasting method (ICASSP; bibliography title "Timerag: Boosting LLM time series forecasting").
- **Suggested Fix:** correct descriptions after rereading each cited abstract; replace the time-series example.

### W4: "State-of-the-art MedicalGraphRAG" and "strong GraphRAG baselines" are not warranted
Three of the five static baselines are domain-specific (MedicalGraphRAG, DALK) or agentic (TOG) systems rather than the standard GraphRAG/LightRAG family, the latter two being cited in §1 but absent from Table 2.
- **Suggested Fix:** add or justify the omission of standard GraphRAG baselines; reword "state-of-the-art".

### Baseline scout (CronQuestions / Hits@1; abstract numbers are pointers only)
| Benchmark / metric | Prior method (link, label) | Its reported number | Compared in the paper? | Paper's number | Note |
|---|---|---|---|---|---|
| CronQuestions Hits@1 | TMA fusion network, https://arxiv.org/abs/2302.12529v2 (prior, peer-reviewed) | abstract: +24% Hits@1 over best baseline on complex questions (no absolute) | No | n/a | trained model; different setting: not a missing required baseline |
| CronQuestions | CronKGQA, https://arxiv.org/abs/2106.01515v1 (prior, ACL 2021; dataset paper) | no number in abstract | No (dataset cited) | n/a | trained |
| Forecast | ForecastTKGQuestions, https://arxiv.org/abs/2208.06501v2 (prior, ISWC 2023) | no number in abstract | No (dataset cited) | n/a | |

No under-reported baseline can be identified; settings differ (supervised Hits@k vs. LLM-generated candidate lists).

### Field snapshot (from kept results, before the cutoff)
Five years ago temporal KGQA was dominated by trained embedding or GNN models (CronKGQA, TempoQR, TwiRGCN) with Hits@k evaluation on template questions. From 2023 the field moved to LLM-based pipelines (GenTKG for forecasting; GraphRAG variants with temporal conflict handling such as T-GRAG, 2025) and to benchmarks for temporal RAG on text (concurrent: ChronoQA, 2025). Open problems stated by recent work: temporal ambiguity, time-insensitive retrieval and redundancy (T-GRAG), multi-step temporal reasoning (KG-IRAG). A significant contribution now is a method that handles relative temporal operators ("after", "first") on realistic, non-template questions with measurable cost gains. The paper's setting (template questions over fully structured events) is the earlier regime, which tempers significance.

## Missing References
*(Literature check strict, cutoff 2025-09-24; only items labelled prior can be required.)*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Ruiyi Yang, Hao Xue, Imran Razzak, Hakim Hacid, Flora D. Salim. "Beyond Single Pass, Looping Through Time: KG-IRAG with Iterative Knowledge Retrieval." arXiv 2025 (arXiv:2503.14234; found, prior arXiv-only) | Closest prior GraphRAG work on temporally dependent queries (similarity top-2); must be differentiated |
| Important | Zhen Jia, Soumajit Pramanik, Rishiraj Saha Roy, Gerhard Weikum. "Complex Temporal Question Answering on Knowledge Graphs." CIKM 2021 (found) | Temporal KGQA with question-relevant compact-subgraph retrieval; contradicts the §2 "model-centric / full event set" characterization |
| Important | Costas Mavromatis et al. "TempoQR: Temporal Question Reasoning over Knowledge Graphs." AAAI 2022 (found) | Closest by similarity score (0.168); standard TKGQA reference point |
| Important | Aditya Sharma et al. "TwiRGCN: Temporally Weighted Graph Convolution for Question Answering over Temporal Knowledge Graphs." EACL 2023 (found) | Temporal edge weighting by question time relevance: directly relevant to the undefined edge weights of Ã |
| Important | Yushan Liu et al. "TLogic: Temporal Logical Rules for Explainable Link Forecasting on Temporal Knowledge Graphs." AAAI 2022 (found on arXiv; venue from memory [verify]) | Temporal rule mining on TKGs, the line GenTKG builds on; positions the rule-graph idea |
| Helpful | Bernal Jiménez Gutiérrez et al. "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models." arXiv 2025 (arXiv:2502.14802; found) | HippoRAG successor using PPR retrieval; relevant to C3 positioning |
| Helpful (worth discussing, concurrent/recent preprints; not required) | Ziyang Chen et al., "A Question Answering Dataset for Temporal-Sensitive Retrieval-Augmented Generation" (arXiv:2508.12282, concurrent); Ze Yu Zhang et al., "Respecting Temporal-Causal Consistency: Entity-Event Knowledge Graphs for Retrieval-Augmented Generation" (arXiv:2506.05939, recent preprint); Junhong Lin et al., "Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs" (arXiv:2509.15464, concurrent) | Natural-question temporal RAG evaluations; never a required comparison |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains real; attribution to the temporal design unproven |
| Clarity | 2 | Inconsistent baseline descriptions |
| Significance | 2 | Narrow, template-based setting |
| Originality | 2 | Combination of established parts |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central pieces (MDL summarization, PPR retrieval) are inherited from cited work and the new temporal term is not shown to matter; gains over the best baseline are real but baselines are a narrow set.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Competent | Derivations (Eq. 6) correct; undefined weights; undirected vs. directed |
| Clarity & Presentation | 58 | Competent | Clear organization, inconsistent prior-work descriptions |
| Novelty & Originality | 56 | Competent | New combination for retrieval; claim-level novelty medium |
| Significance & Impact | 52 | Competent | Template benchmarks; practical angle |
| Experimental Validation | 50 | Developing | Three datasets and ablations; thin baselines |
| Reproducibility | 45 | Developing | Hyperparameters partly given; no code |
| Ethical Compliance | 58 | Competent | Nothing at stake; limitations absent |

## Questions for Authors
1. How does the retrieval step differ from HippoRAG's PPR beyond the graph on which PPR runs? A direct comparison of PPR on a plain entity graph vs. on the rule graph would raise my novelty score.
2. Is L_time (Eq. 6) responsible for any accuracy gain? A no-L_time ablation would resolve this.
3. How does the method compare, even as an upper reference, with a trained TKGQA model such as TempoQR on CronQuestions?

## Limitations Assessment
**No.** No limitations section.

## Ethics Review Flag
**No**

## Overall Score
**3**: A reasonable combination of known components with demonstrated gains, but novelty rests on an unisolated temporal term and the positioning against temporal KGQA and the closest retrieval works is incomplete.

## Confidence
**4**: Literature check supported claims against abstracts; I did not read the cited papers in full.

---

# Peer Review Report

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Reviewer: Dr. Sofia Lindqvist, Perspective (database and data-management group, Northern Europe; fictional persona)
## Expertise: Graph compression and MDL; index maintenance; data-management deployment
## Date: 2026-11-05

## Summary
This paper proposes a precomputed event-category graph plus a query-time PageRank diffusion as a lightweight index for temporal retrieval before an LLM. The pitch is that no model training is needed, the LLM context stays short, and accuracy improves on temporal QA benchmarks.

## Strengths
### S1: A data-management-flavoured, training-free alternative is appealing
Building a summarization index offline and doing a cheap diffusion at query time (§3.3) is a familiar and deployable pattern; avoiding encoder training or LLM fine-tuning (Abstract, §1) lowers the operational barrier, which matters in domains with changing data.

### S2: Context length is small
With K1=10 events and ≈600 tokens per query (§4.4), serving cost with a 70B model is small compared with baselines using ≈20K tokens (Figure 3, as quoted in §4.4). I note that part of this is a property of the K1 setting.

### S3: Robustness check across generators
Table 4 shows only a 3.5–4.4-point Hit@1 drop with Llama-3-8B-Instruct and a similar value with GPT-4o-mini, which suggests a deployable cheaper-generator path.

### S4: The summarization idea transfers cleanly from the data-mining literature
The use of MDL to decide which links in an event-category graph are worth keeping (Eq. 3, Eq. 7) is a principled alternative to hand-tuned thresholds.

## Weaknesses
### W1: Update and scale behaviour of the rule graph is not discussed
Temporal KGs grow continuously; the rule graph requires Apriori mining over entity relation-sets (Appendix A, Algorithm 2) and a greedy MDL pass over a candidate set that includes all Hamming-1 pairs (Algorithm 1, line 3) which can be quadratic in rule nodes. The paper reports query-time latency (Figure 3, Table 4: 20.6–30.4 s per query) but not build time, memory, number of rule nodes, or how to update the graph when new events arrive.
- **Suggested Fix:** report build time and graph size per dataset, and a short incremental-update discussion (e.g., re-run only for new time windows).

### W2: The setting is highly structured and template-generated; the "temporal RAG" in the title promises more
All three datasets are KG event triples with template-generated questions (§4.1: "questions are generated by filling templates with entity aliases"). The method needs typed relations to derive entity labels; free-text temporal RAG (news, documents) is out of scope but not acknowledged. Claims about "real-world knowledge" (§1) are supported only by two ICEWS-derived and one Wikidata-derived benchmark.
- **Suggested Fix:** add a limitations paragraph and, if possible, one natural-question benchmark or a small LLM-paraphrased question set.

### W3: Time alignment is a statistical property of event categories, not a per-query constraint
In deployment, users ask "before X" or "in 2011". Eq. 6 models the average gap between categories; the question's own time constraint is left to the LLM (Appendix E prompt: "Apply temporal operator precisely"). A simple, standard data-management solution (a timestamp range filter or sorted index around the anchor date) is not compared and may be cheaper and more exact.
- **Suggested Fix:** add a timestamp-range-filter baseline on questions with explicit dates.

### W4: Robustness and error analysis are missing
No failure cases or per-relation breakdown; Table 3 splits by single/multiple events only. A rule graph built from frequent relation sets will under-represent rare relation types, which are likely to matter for the long tail (§3.3 acknowledges "rare, low-support rules" as unreliable).
- **Suggested Fix:** report accuracy by relation frequency decile and show failure examples.

## Missing References
*(none beyond R2's list; I suggest the authors consult the database literature on temporal indexing and on incremental graph summarization, described only by line of work.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound pipeline, consistent gains |
| Clarity | 3 | Understandable, some inconsistencies |
| Significance | 3 | Practical interest for lightweight temporal retrieval |
| Originality | 3 | New application of familiar summarization ideas |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically relevant training-free recipe with large reported gains over several baselines; held back by narrow template-based evaluation and missing system-cost reporting.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Principled MDL selection; scale not analysed |
| Clarity & Presentation | 62 | Competent | Generally clear |
| Novelty & Originality | 62 | Competent | Useful cross-field transfer |
| Significance & Impact | 68 | Competent | Training-free and short-context are deployment-relevant |
| Experimental Validation | 58 | Competent | Three datasets, ablations, no variance |
| Reproducibility | 50 | Developing | No code; missing hyperparameters |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. What are the rule-graph build time and size on CronQuestion (125K entities)? A modest build cost would raise my score.
2. How would you update the graph for a new month of events?
3. Would a simple date-range filter around the anchor event match STAR-RAG on date-explicit questions?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No**

## Overall Score
**4**: A practical, training-free, short-context retrieval recipe with strong reported gains; its weaknesses (narrow benchmarks, unreported system costs) are common among accepted papers, though the temporal mechanism needs better support.

## Confidence
**3**: Fairly confident; I read the method as a systems person and did not audit baselines.

---

# Peer Review Report

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Reviewer: Dr. Hyun-woo Baek, Generalist (ML/NLP lab, university, East Asia; fictional persona)
## Expertise: LLM applications; retrieval and QA
## Date: 2026-11-05

## Summary
The paper presents STAR-RAG, a retrieval front-end for temporal knowledge-graph QA that groups events into category-level rule nodes, selects links with an MDL criterion, and uses personalized PageRank from semantic anchors to pick evidence for a frozen LLM. Experiments on three datasets show higher Hit@k than seven baselines and far fewer prompt tokens than the baseline with the longest context.

## Strengths
### S1: Clear problem and storyline
The introduction states a concrete failure mode (semantic retrieval ignores temporal constraints, §1) and gives a worked example (Figure 1 caption; the example question about Oman and Qatar).

### S2: Strong headline table
Table 2 shows the best result on every metric in three datasets; Table 3 shows the largest gain on multiple-event questions (44.4 vs. 23.8 for T-GRAG, ×1.87 derived), where temporal reasoning is expected to matter.

### S3: Useful ablation and sensitivity analyses
Table 4 and Figure 5 respond to the obvious questions (is the rule graph needed, does γ matter, how sensitive are K1 and K2). The default setting is not the best-scoring cell (31.2 at K1=40, K2=40 vs. 30.5 default), which indicates it was chosen for cost, not to maximise the number.

### S4: Appendix example and prompt aid understanding
Appendix E shows the prompt, a one-shot demonstration and a retrieval result for a "last before" question.

## Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | Gains supported (Table 2); mechanism claims not isolated (Table 4) |
| Contribution: significant for the ICLR audience | Partly | Practical retrieval recipe; limited to template KGQA |
| Presentation: clear to a non-specialist | Mostly | §3.2 mixes notation; Algorithm 1 is helpful |
| Reproducibility: details and code | Not met | No code statement; missing hyperparameters |
| Honest limitations | Not met | No limitations discussion |

## Weaknesses
### W1: The paper's central claim ("time-aligned retrieval") is stronger than what the experiments show
Table 4 shows the rule graph helps, but not that its *temporal* part helps; the method never compares against a non-temporal rule graph (§3.2, Eq. 6). I expect other reviewers to say this; as a generalist reader, I also found that Algorithm 1 never touches timestamps at query time.
- **Suggested Fix:** a no-L_time ablation and a plain timestamp-filter baseline.

### W2: Fairness of the comparison is unclear to a non-specialist
It is not clear how baselines were run, with which prompts and context lengths, and tuned on which questions (§4.4). The headline compares with MedicalGraphRAG (§1), a baseline not obviously relevant to temporal ICEWS or Wikidata events, instead of the best baseline per dataset.
- **Suggested Fix:** put the best-baseline comparison in the abstract and add an "how baselines were run" paragraph with prompts and K.

### W3: Writing and consistency issues that obscure method details
§3.2 uses Hamming distance with three fields (Eq. 2) while footnote 3 relaxes to "dH ≤ 2 as timestamps are always different", which implies four fields for events. Edge weights of Ã are undefined. The α parameter is a "decay coefficient" in §3.3 and a "restart probability" in Appendix C and Algorithm 1.
- **Suggested Fix:** unify definitions and add a notation table.

### W4: No limitations section
The paper does not discuss scope (structured TKGs, template questions), offline cost, or failure modes.
- **Suggested Fix:** add a Limitations paragraph.

**Minor:** the "Accessed: YYYY-MM-DD" placeholder in the Llama reference; NV-Embed has no year; "Retrival results" typo in Appendix E; Table 4 caption labelled Figure 4.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains solid, attribution not demonstrated |
| Clarity | 3 | Readable with definitional gaps |
| Significance | 2 | Narrow template setting |
| Originality | 2 | Known parts combined |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: large margins on three datasets are a plus, but the central mechanism claim, baseline fairness and missing limitations/code place it in the typical-rejected band rather than the accepted one.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Reasonable design, untested mechanism |
| Clarity & Presentation | 60 | Competent | Clear story, definitional inconsistencies |
| Novelty & Originality | 52 | Competent | Incremental combination |
| Significance & Impact | 54 | Competent | Useful but narrow |
| Experimental Validation | 52 | Competent | Three datasets, ablations; no variance |
| Reproducibility | 45 | Developing | No code, missing details |
| Ethical Compliance | 58 | Competent | Nothing at stake |

## Questions for Authors
1. Can you give the best-baseline comparison (not MedicalGraphRAG) for tokens and accuracy in the abstract? A matched-budget table would raise my score.
2. Why is TOG's CronQuestion Hit@1 (69.5) above both temporal baselines, given the text says static methods "perform notably worse"?
3. Is the code going to be released?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No**

## Overall Score
**3**: The idea is sensible and the numbers are strong, but ICLR's bar needs the central temporal claim demonstrated and the comparison made fair and reproducible; these are fixable but substantial.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Reviewer: Dr. Marisol Quispe, evaluation-methodology institute, South America (fictional persona)

## Steelman
A frozen-LLM temporal RAG pipeline that needs no training and gets about 5–26 more Hit@1 points than seven baselines on three benchmarks, with a 10-event context, is a practically valuable result. The rule graph gives a principled, data-driven way to propagate from semantically retrieved anchors to related event categories, and the ablations show that removing it costs 10–22 points.

## Core Argument Chain
1. P1: Semantic retrieval ignores temporal constraints and wastes tokens (§1).
2. P2: A rule graph with temporally-informed MDL edges encodes "what follows what" (§3.2).
3. P3: Seeded PPR on that graph retrieves time-consistent evidence (§3.3).
4. P4: STAR-RAG beats strong GraphRAG baselines on accuracy with 97% fewer tokens (Table 2, Figure 3).
5. P5: Removing the rule graph loses accuracy (Table 4).
∴ Time-aligned propagation over the rule graph is what yields better accuracy and efficiency (§4.4–4.5).

## Strongest Counter-Argument
The argument slides from P5 to the conclusion without the intermediate steps. P5 shows that *something in the rule graph pipeline* helps; it does not show the helpful thing is temporal. Algorithm 1 never conditions on any timestamp: anchors come from cosine similarity, rule nodes are ranked by PPR, all events in the top-K2 rule nodes are pooled, and the final step re-ranks them by the same cosine similarity. Time enters only offline, through spans |t′−t| (absolute values, so direction is lost, and Appendix B's "directed chain edges" contradict the undirected {u,v} of Eq. 2). A rule node is a category of events (⟨country-type, relation, country-type⟩) whose support spans the whole timeline. So the likeliest mechanism of the gain is category filtering: restrict the candidate pool to event types similar to the anchors, which removes semantically similar but wrong-relation distractors. That would help on template questions (where the relation is named in the question) regardless of time, and would explain why the single-event gain is zero (Table 3: 25.8 vs. 26.8 for TS-Retriever) whereas multi-event questions, which include a named relation, gain heavily. Also, since the final output is a top-K1 re-ranking of a subset of F, increasing K2 should converge to the "no-rule" 18.3 (Table 4), yet Figure 5 increases with K2 up to 40; the paper does not explain which events are dropped. Meanwhile the 97% token figure is determined by K1=10 and a comparator chosen for having the largest context. Until a no-L_time ablation, a non-temporal category-filter control and a matched-context baseline exist, the paper's conclusion is "a candidate-pool restriction improves LLM QA on three template datasets", which is a weaker claim.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The improvements over baselines in Table 2 are large, the headline numbers are not shown to be test-selected (the selection sentence in §4.4 names no split: protocol-sweep row "not stated" → MAJOR), and the weaker claim survives.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | Algorithm 1 lines 8–16; Eqs. 5–6; Table 4 | Timestamps unused at retrieval; no ablation of L_time or non-temporal category filter; mechanism claim ("enforces temporal proximity during retrieval") unsupported: evidence supports a weaker claim | No-L_time, type-filter and date-filter controls; reword the claim |
| DA-M2 | Evidence | §1, §4.4, Figure 3, Table 4 | 97.0% token reduction vs. the largest-context baseline; set by K1=10; no matched-budget comparison | Matched-K1 / accuracy-vs-tokens plot |
| DA-M3 | Protocol | §4.4 ("we tune the hyperparameters of each baseline and report their best achievable performance"); §4.1 | Tuning split unstated; no validation split exists in the protocol; baselines tuned and then reported on the test sample (protocol sweep: only these two selection statements) | State the split; tune on held-out questions |
| DA-M4 | Scope / E5 | §4.4, Table 2 vs. text | "Static-graph approaches ... perform notably worse than temporal methods" contradicted on CronQuestion by TOG; headline comparator MedicalGraphRAG is not the strongest baseline | Correct wording, report best-baseline deltas |
| DA-M5 | Logic | §3.2 vs. Appendix B | Directedness ("what-follows-what") claimed but edges are undirected and spans absolute; before/after not encoded | Define direction or drop the claim |
| DA-M6 | Validity | §4.1, Table 1 | Forecast benchmark is built so that the TKG available for inference should contain only the past; the paper uses the whole event set F (335,303 events) with no statement that retrieval is restricted to events before the question time | State and enforce the temporal cut-off, or explain |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of examples | Appendix E | LLM "Thoughts" cite events absent from the 10 retrieved results |
| DA-m2 | Consistency | §4.1 vs. Table 1/Figure 2 | "ICEWS14" cannot yield 4,017 timestamps and 2005–2011 events |
| DA-m3 | Citation | §1 | TimeRAG (time series) offered as KG temporal modelling |
| DA-m4 | Wording | Table 4 caption | "average accuracy" actually Hit@1; Table 4 labelled Figure 4 |
| DA-m5 | Statistics | §4.1 | "five runs" unspecified; no variance |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Accuracy gain over MedicalGraphRAG | "9.1%" (§1) | Hit@1: 26.5 / 9.4 / 9.4 points; relative on MultiTQ 44.5%; nine-cell mean 57.3 − 44.3 = 13.0; Forecast mean 49.0 − 39.8 = 9.2 | No exact match; unstated basis |
| Token reduction | "(20453-601)/20453 = 97.0%" | 97.06% → 97.1% | Rounds differently (trivial) |
| Gain over strongest baseline | "at least a 5%" Hit@1 (§4.4) | 5.0 / 7.7 / 8.4 vs. TS-Retriever; vs. strongest per dataset 5.0 / 7.7 / 7.4 | Yes (absolute points); "TS-Retriever strongest" false on CronQuestion |
| Rule graph ablation | 21.6 / 10.0 / 12.2 (§4.5) | 76.9−55.3, 39.8−29.8, 30.5−18.3 | Yes |
| Uniform-γ drop | "up to an 8.7% drop" on Forecast | 39.8−31.1 | Yes |
| Backbone drop | "maximum drop of 4.4%" | 3.5 / 4.4 / 4.0 (Llama-3-8B) | Yes |
| Multi-event vs. best baseline | "nearly doubling ... 23.8%" | 44.4 / 23.8 = 1.87 | Yes |
| Default K1/K2 | 30.5 | Figure 5 grid K1=10, K2=20 = 30.50 = Table 2 MultiTQ Hit@1 | Yes |

## Ignored Alternative Explanations
1. Category filtering (relation/type match) rather than time alignment explains the gain.
2. Baselines run with larger contexts or unmatched prompts, so the accuracy gap partly reflects context noise and prompt differences (the same 10-event setting for baselines is never tried).
3. LLM pretraining exposure to Wikidata/ICEWS events (Llama-3.3-70B) with no contamination check.
4. Hyperparameter tuning of baselines and STAR-RAG's θ, β, α on the same sampled questions.
5. Template-question regularities (relation named in the question) make type filtering unusually effective.

## Missing Stakeholder Perspectives
Practitioners with evolving KGs (update cost) and users asking natural-language, non-template temporal questions.

## Observations (Non-Defects)
The ablation arithmetic in §4.5 is accurate; the default K1/K2 is not the best-scoring cell, so the sensitivity sweep does not show test-selection of the headline (DA decision table row 1); the authors honestly report the 2× latency over semantic search; the Eq. 6 derivation is correct.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Mechanism claim unsupported by the algorithm |
| Clarity & Presentation | 55 | Inconsistent definitions |
| Novelty & Originality | 45 | Known parts; temporal delta not isolated |
| Significance & Impact | 45 | Narrow template evaluation |
| Experimental Validation | 40 | Missing controls, variance, matched budgets |
| Reproducibility | 40 | No code; missing hyperparameters |
| Ethical Compliance | 55 | Nothing at stake; no limitations |

**Pool position:** better than about 33% of submissions to ICLR. Deciding evidence: the central claim's mechanism is untested and partly contradicted by the algorithm itself.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Editorial Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 mechanism untested | kept | Specific; algorithm lines quoted; verified in the paper |
| R1 | W2 token confound | kept (rewritten: "no-rule token count not reported" stated as a gap) | Fig. 3 unavailable; the K1 cap argument rests on §4.3 and §4.4 |
| R1 | W3 baseline protocol | kept | Quotes located (§4.4, §4.3) |
| R1 | W5 reproducibility | kept; K_type etc. confirmed absent after search | Appendix checked |
| R1 | Minor line | moved to Minor | Cosmetic |
| R2 | W2 "contradicts §2 characterization" for EXAQT | rewritten | Based on abstract only; marked [verify] |
| R2 | W3 TOG description | rewritten as question [verify] | Not checked against the original abstract |
| R3 | W3 date-range filter baseline | kept | Actionable |
| R3 | S2 "context length is small" praised without the K1 caveat | kept with caveat | The caveat is in S2 text |
| R4 | W1 | kept | Duplicate of R1-W1 (merged in Phase 2) |
| DA | Strongest counter-argument "dropping anchors ... converge to no-rule" | kept | Derived from Algorithm 1 lines 8, 15, 16; stated as derivation, not as observed |
| DA | DA-M6 Forecast temporal cut-off | rewritten as a question | Cannot be verified from the text; asks for a statement |

No score changed.

## Synthesizer package: issue classes (Phase 2, Part A)

| Issue | Sources | Class | Hinge? |
|-------|---------|-------|--------|
| Temporal mechanism not isolated / timestamps unused at retrieval | R1-W1, R2-W1, R4-W1, DA-M1, R3-W3 | CONSENSUS-4/5 | **Yes** |
| Baseline fairness, tuning split, best-baseline comparator | R1-W3, R2-W4, R4-W2, DA-M3, DA-M4 | CONSENSUS-4/5 | **Yes** |
| Token claim set by K1 / unmatched budgets | R1-W2, DA-M2, R4-W2 | CONSENSUS-3 | Yes |
| No variance, "five runs" undefined | R1-W4, DA-m5 | CONSENSUS-2 | No |
| Reproducibility / undefined components, no code | R1-W5, R4-W3, R3-W1, R4 | CONSENSUS-3 | No |
| Directed vs. undirected edges | R1 Error Log ERR-6, DA-M5 | CONSENSUS-2 | No |
| Missing temporal-KGQA / closest prior work | R2-W2 | SOLO | No |
| Inconsistent baseline/prior-work descriptions | R2-W3 | SOLO | No |
| Rule-graph build/update cost not reported | R3-W1, R1-W5 | CONSENSUS-2 | No |
| Template-only scope, no limitations | R3-W2, R4-W4 | CONSENSUS-2 | No |
| Forecast temporal cut-off | DA-M6 | SOLO | No |
| SPLIT | none (R3 rates significance higher but raises the same issues) | | |
| DA-CRITICAL | none | | |

Official output (BEFORE, no EIC weights, DA-CRITICAL list empty): ratings R1 3, R2 3, R3 4, R4 3, DA 2, mean 3.00; composite 52.1; weighted rating 2.96; spread flag: Significance & Impact 23 (R3 68 vs. DA 45). No consistency warnings.

---

# Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization
## Date: 2026-11-05
## Target Venue: ICLR (2026 cycle, scale status: secondary) | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Ramón Iturbe; R1 Methodology Dr. Kavya Menon, R2 Domain Prof. Femi Adeyemi, R3 Perspective Dr. Sofia Lindqvist, R4 Generalist Dr. Hyun-woo Baek, DA Dr. Marisol Quispe

---

## Decision: Borderline Reject (3). ICLR label: rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 52.1
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 51.3 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 42% of ICLR submissions.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A training-free temporal retrieval front-end that gains 5–26 Hit@1 points over seven baselines on three standard datasets, with ablations that support the value of the rule-graph stage, a short context and robustness to the generator (Tables 2–4). A practical result that ICLR audiences working on RAG would read.
- **Against acceptance:** The paper's stated mechanism, time-aligned retrieval, does not appear in the retrieval algorithm and is not isolated by any ablation; the efficiency headline is set by a context cap against a weak comparator; baseline tuning is unspecified; there are no variances, no code and no limitations section. The evidence supports a weaker claim than the one made.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Algorithm 1 never uses timestamps at retrieval; time enters only offline through T_uv | R1-W1, DA-M1, R4-W1, R3-W3 | Algorithm 1 lines 8–16; Eqs. 5–6 | **Verified** | Lines 8, 15, 16 use cosine and rule-node support only; §3.3 does not describe a date filter |
| No ablation of L_time, Hamming candidates or a non-temporal filter | R1-W1, R2-W1, DA | Table 4, §4.5 | **Verified** | Only no-rule and uniform-γ variants exist |
| Final top-K1 is a cosine re-ranking of a subset of F, so it can only drop anchors | R1-W1, DA counter-argument | Algorithm 1 lines 8, 15, 16 | **Verified (derivation)** | Whether it explains Figure 5 is untested; stated as a question |
| Token claim set by K1=10 | R1-W2, DA-M2 | §4.3, §4.4, Figure 3 | **Partly correct** | K1=10 is stated in §4.3; Figure 3 and no-rule token counts not visible, so the equal-token claim for no-rule is inferred |
| "Static ... notably worse than temporal methods" contradicted | R1 ERR-1, R4-Q2, DA-M4 | §4.4, Table 2 CronQuestion | **Verified** | TOG 69.5 > 68.5, 67.3 on Hit@1 |
| "9.1%" not reproducible | R1 ERR-2, DA | §1, Table 2 | **Partly correct** | No cell gives 9.1; dataset/metric of the claim is unstated, so "unstated basis" is the right wording |
| Baseline tuning split unstated; no validation split | R1-W3, DA-M3 | §4.1, §4.4 | **Verified** | Only two selection sentences; text search found no validation/held-out sentence |
| Directed vs. undirected edges | R1 ERR-6, DA-M5 | §3.2, Appendix B | **Verified** | |
| TS-Retriever run with its trained encoder or NV-Embed | R1-W3 | §1, §4.3 | **Partly correct** | Both sentences exist; whether they conflict depends on what "all methods" means, so it remains a question |
| Appendix E "Thoughts" cite events not in the list | R1 ERR-5, DA-m1 | Appendix E | **Verified** | Minor |
| ICEWS14 inconsistent with Table 1 / Figure 2 | R1 ERR-4, DA-m2 | §4.1 | **Partly correct** | Internal evidence (|T|=4,017; dates from 2005) supports it; the exact snapshot is not stated |
| EXAQT contradicts §2's characterization of temporal methods | R2-W2 | §2 | **Overstated** | Based on an abstract only and marked [verify]; kept as Important reference, not as an error |
| R3: "97% fewer tokens" as a strength of the method | R3-S2 | §4.4 | **Overstated** | Reviewer adds a caveat, but scores Significance 68 partly on it |
| Forecast cut-off (whole F used) | DA-M6 | §4.1, Table 1 | **Not verifiable** | Treated as a question |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points verified (W1, W3, ERR-1/6); well calibrated; one wrong-basis claim (ERR-2) was flagged as unstated basis |
| R2 (Domain) | 3 | 4 | 1.0 | Literature check sound; EXAQT and TOG descriptions overstated but marked [verify] |
| R3 (Perspective) | 4 | 3 | 0.75 | Rating partly rests on the token-efficiency strength (confounded by K1) and a "principled MDL" reading that did not check whether time enters retrieval |
| R4 (Generalist) | 3 | 4 | 1.0 | Typical, calibrated, verified |
| DA | 2 | 4 | 1.0 | Counter-argument verified for the algorithm; its causal explanation (category filtering) is a hypothesis, but it was stated as such; Overall 2 is a little harsh, but weight equals the typical |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
The starting point is the EIC-weighted rating 2.92 → 3 (official mean 3.00). The weighted composite of 51.3 falls in band 3 as well, so the two signals agree and there is no cross-check disagreement. There is no upheld DA-CRITICAL issue, so there is no ceiling. I do not depart from the starting point. The deciding evidence is the verified gap between the claim and the algorithm: the abstract and §3.3 sell time-consistent retrieval, but Algorithm 1 uses timestamps only offline and the ablations never isolate the temporal term. Combined with a headline comparator that is not the strongest baseline, a token claim set by the context cap, and no variance, tuning split, code or limitations, this sits in the typical-rejected band for ICLR (pool position ≈ 42), although the large and consistent gains on three datasets and the practical, training-free angle keep it close to the borderline. Most weaknesses (variance, code, wording, baseline fairness) are common among accepted papers, but the combination with an unsupported central mechanism claim is not. The issues are fixable within a revision cycle, mainly with ablations and matched-budget baselines, which is why this is 3 and not 2. The decision of 3 does not exceed any ceiling.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 48 | 52 | 60 | 55 | 42 | 51.4 | 50.5 | 18 |
| Clarity & Presentation | 56 | 58 | 62 | 60 | 55 | 58.2 | 57.8 | 7 |
| Novelty & Originality | 48 | 56 | 62 | 52 | 45 | 52.6 | 51.6 | 17 |
| Significance & Impact | 50 | 52 | 68 | 54 | 45 | 53.8 | 52.5 ⚠ | 23 |
| Experimental Validation | 45 | 50 | 58 | 52 | 40 | 49.0 | 48.1 | 18 |
| Reproducibility | 42 | 45 | 50 | 45 | 40 | 44.4 | 43.8 | 10 |
| Ethical Compliance | 58 | 58 | 60 | 58 | 55 | 57.8 | 57.6 | 5 |
| **Composite** | 48.9 | 52.7 | 60.3 | 53.6 | 44.9 | **52.1 (before)** | **51.3 (after)** | |

Spread discussion (Significance, 23 points): R3 (68) values the training-free/short-context deployment angle; the DA (45) notes the template-only evaluation. I adopt the middle: the practical angle is real but unproven beyond template KGQA.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}), corresponding to the internal Overall 3 (Borderline Reject). Labels are "as reported on recent analyses; verify against the current form". |
| Official rating (mean of reviewers' Overall) / EIC-weighted | 3.00 / 2.92 |

### Cross-Venue Outlook
Not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Right Answer at the Right Time — Temporal Retrieval-Augmented Generation via Graph Summarization" to ICLR. The question of making retrieval-augmented generation respect time, without training, is worth studying.

**Overall Assessment:** The panel found a practical, training-free pipeline with large and consistent gains over the compared GraphRAG baselines on three temporal KGQA benchmarks, and a short LLM context. The panel's main reservation is that the paper's central explanation (time-aligned retrieval) is not demonstrated by its experiments or its algorithm, and several comparison details limit how far the headline numbers can be trusted.

**Key Strengths Identified by Reviewers:**
1. Consistent gains in all nine Hit@k cells of Table 2 (R1, R4, R3).
2. A training-free design with short context, with ablations and a sensitivity grid (R3, R4, R1).
3. Inclusion of a very recent temporal GraphRAG baseline and standard benchmarks (R2).

**Key Concerns Requiring Attention:**
1. Timestamps are not used at retrieval time in Algorithm 1, and no ablation isolates the temporal term (R1, R2, R4, DA, R3: CONSENSUS-5).
2. Baseline protocol: unspecified tuning split, headline comparator not the strongest baseline, some unsupported wording, GraphRAG/LightRAG not compared (R1, R2, R4, DA: CONSENSUS-4).
3. The token-reduction claim is set by the retrieval cap and not matched across methods (R1, DA, R4: CONSENSUS-3).

No CRITICAL issue was raised by the Devil's Advocate.

**Decision: Borderline Reject (3).** The panel sees real promise, and the weaknesses can be fixed with additional ablations and matched-budget comparisons, a variance report and a tidier method specification. A revision that shows what the temporal component contributes (no-L_time, a non-temporal category filter, a date filter) and compares at matched context length would change our view.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ramón Iturbe
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Temporal mechanism not isolated / timestamps unused at retrieval | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Baseline fairness, tuning split, comparator | R1, R2, R4, DA | CONSENSUS-4 |
| Token claim confounded by K1 / matched budget | R1, R4, DA | CONSENSUS-3 |
| Reproducibility gaps, no code | R1, R3, R4 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Practical significance of training-free, short-context retrieval | R3 (68) | DA (45), R1 (50) | Real but conditional on matched-budget evidence and non-template scope |

### Score Spread Discussion
Significance & Impact (spread 23): see above.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Temporal mechanism untested | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Token claim | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | Tuning split unstated | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Text–table contradiction, comparator | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Directed vs. undirected | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR (question) | Forecast cut-off | No | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*The EIC verified these as undermining a main claim; they are not DA-CRITICAL.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Temporal mechanism not isolated; timestamps unused at retrieval | R1-W1, R2-W1, R4-W1, DA-M1, R3-W3 | Algorithm 1; Eqs. 5–6; Table 4 | Add no-L_time, non-temporal type filter, date-range filter; report per question type; reword "enforces temporal proximity" if unsupported | Med; ≈ 30 GPU-h | Partly (one dataset) |
| R2 | Baseline protocol and comparator | R1-W3, R2-W4, R4-W2, DA-M3, DA-M4 | §1, §4.2, §4.4, Table 2 | State tuning split, tune on held-out questions, report best-baseline deltas, add GraphRAG/LightRAG or justify, fix "TOG and DALK" sentence | Med; ≈ 40 GPU-h | Partly |
| R3 | Token-efficiency claim at matched budget | R1-W2, DA-M2 | §4.4, Figure 3, Table 4 | Hit@1 vs. tokens at K1∈{5,10,20,40} for all methods incl. no-rule | Med; ≈ 20 GPU-h | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No variance; "five runs" undefined | R1-W4, DA-m5 | mean ± std, paired bootstrap | Low | Yes |
| S2 | Undefined components; no code; offline cost | R1-W5, R3-W1, R4-W3 | Define Ã weights, K_type, support threshold, edge order; rule-graph stats and build time; release code | Low–Med | Yes |
| S3 | Directed vs. undirected edges | R1 ERR-6, DA-M5 | Define direction or drop the claim | Low | Yes |
| S4 | Missing positioning: KG-IRAG, EXAQT, TempoQR, TwiRGCN, TLogic; KGist/HippoRAG delta | R2-W1, R2-W2 | Cite and differentiate; add one trained TKGQA reference row | Low–Med | Yes |
| S5 | Inconsistent descriptions of DALK, TOG, TimeRAG | R2-W3 | Re-read abstracts and correct | Low | Yes |
| S6 | Forecast temporal cut-off; dataset snapshot (ICEWS14 vs. 2005–2015) | DA-M6, R1 ERR-4 | State and enforce | Low | Yes |
| S7 | Limitations section; template-only scope | R3-W2, R4-W4 | Add a limitations paragraph; add a natural-question evaluation if possible | Low–Med | Partly |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Appendix E example inconsistent | R1 ERR-5 | Align events with the retrieved list |
| N2 | Error-analysis by relation frequency | R3-W4 | Add per-relation breakdown and failures |
| N3 | Typos, placeholders, caption labels | R1, R4 | Fix |
| N4 | Concurrent/recent work worth discussing (ChronoQA benchmarks, entity-event KG RAG, EvoReasoner) | R2 | Discuss; not required |
| N5 | Incremental-update discussion | R3-W1 | Short paragraph |

## Estimated Revision Effort
- Priority 1: 3 items, about 90 GPU-hours and 1–2 weeks (a subset is rebuttal-feasible).
- Priority 2: 7 items, about 3–5 days.
- Priority 3: 5 items, about 1 day.
- **Total estimated revision time**: about 2–3 weeks.
