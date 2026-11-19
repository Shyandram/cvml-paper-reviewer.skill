# Review: STAR-RAG — Temporal RAG via Graph Summarization (ICLR 2026 submission)

Note: figures are not available. Fig. 1–5 were judged from captions, the extracted text and the tables.

## Summary
The paper proposes STAR-RAG, a training-free retrieval pipeline for question answering over temporal knowledge graphs (TKGs).
1. Entities are labeled with "types" by running Apriori over the relation sets they participate in.
2. Events (s, r, o, t) are mapped to "rule nodes" ⟨c_s, r, c_o⟩.
3. Rule nodes are connected by edges between Hamming-distance-1 neighbours. Edges are selected greedily with an MDL criterion that combines a coverage term with an exponential model of the time gaps between events in the two rules.
4. At query time, the top-K1 events by NV-Embed cosine are mapped to rule nodes. A personalization vector is built from rule support and anchor rank. Personalized PageRank runs on the rule graph, the top-K2 rule nodes are taken, and their events are re-ranked by cosine. The top-10 events are passed to Llama-3.3-70B.

On CronQuestions, ForecastTKGQuestions and MultiTQ (1,000 sampled test questions each), the method beats five static GraphRAG baselines and two temporal-RAG baselines. It uses far fewer tokens than MedicalGraphRAG (97%). It reports a large gain on MultiTQ multi-event questions (44.4 vs 23.8 Hit@1).

## Strengths
- The problem is relevant: temporal constraints in graph-based RAG, with token efficiency treated as a first-class concern.
- The idea of summarizing events into a compact, type-level "rule graph" and propagating on it is simple. It needs no LLM fine-tuning, and the rule graph is built once offline.
- Evaluation covers three datasets with a reasonable set of baselines, a backbone swap (Llama-3-8B, GPT-4o-mini), ablations (no rule graph, uniform γ), a K1/K2 sensitivity study, and token/latency plots.
- The LLM-backbone ablation suggests the gain comes from retrieval rather than generation.
- The appendix gives details of the labeling algorithm, the MDL costs and γ, which helps reproducibility.

## Weaknesses
1. **The method does not actually enforce temporal constraints, contrary to the framing.**
   - The query is never parsed for temporal operators (before/after/first/last/in year X). Retrieval is cosine → rule-node PPR → cosine.
   - Time enters only through (a) the edge-selection MDL term over |t − t'| spans and (b) the LLM prompt.
   - Candidate edges (Eq. 2) are defined purely by Hamming distance over rule fields, with no temporal information.
   - Retrieved events are restricted neither to the query's time window nor to events that precede or follow the anchor.
   - The transition matrix Ã (edge weights) is never defined, so how "temporal proximity" affects propagation is unclear.
   - The statements "enforces temporal proximity during retrieval" and "time-consistent evidence" are therefore unsupported. No analysis shows that retrieved events are more time-consistent, for example the fraction of retrieved events inside the gold time window or in the correct order relative to the anchor.
   - It is also unclear why propagation over *type-level* rule nodes would favour the right time: rule nodes aggregate events across all time, so the final event set is "events sharing a category pattern with an anchor", re-ranked by semantics.

2. **The MDL formulation looks ill-posed or under-specified.**
   - Eq. 5 gives L_cov = Σ log(|supp(u)||supp(v)| / |T_uv|). This increases with support, yet the text says that "adding an edge that explains more connected events will bring fewer costs".
   - Eq. 7 accepts an edge if ΔL < 0. Every added edge adds a model cost, a coverage cost and a likelihood cost, and nothing defined in the paper reduces L(G | M) when an edge is added. There is no baseline description of events without the edge, so it is unclear when ΔL < 0 can occur at all.
   - The statement that the MDL "selects edges that best explain event trends" is not demonstrated. How many edges are kept, what the rule graph looks like in size and sparsity, and whether the MDL step matters relative to simply keeping all Hamming-1 edges are all left unreported.
   - The edge order is fixed and the algorithm is greedy, so the result depends on the order.
   - The ablations only test "no rule graph" and "uniform γ". There is no ablation of the MDL selection, the temporal term, the entity labeling, K_type or the Hamming threshold.

3. **The efficiency claim is largely an artifact of the comparison.**
   - STAR-RAG sends K1 = 10 events to the LLM. The "no-rule" ablation (cosine top-10) uses the same number of tokens, so the 97% token reduction (601 vs 20,453) comes from the baseline's retrieval size, not from the rule graph or PPR.
   - The headline comparison against MedicalGraphRAG, which does iterative context refinement, is an unfavorable choice. Baselines are not controlled for a matched token budget or matched top-k context.
   - Offline costs (Apriori labeling, candidate generation, greedy MDL on 460K events) are not reported. Retrieval latency is higher than static methods (e.g., 30 s per question on CronQuestion). Why PPR on a graph of rule nodes plus re-ranking of a possibly very large union of supports takes 10–20 s is not explained.
   - The claim of "significantly simplifying deployment" is not backed by cost numbers. There is also no discussion of updating the rule graph as the TKG grows, which is central for temporal data.

4. **Missing baselines and a weak experimental protocol.**
   - There is no simple temporal baseline, for example parsing the time expression and filtering events by timestamp or time window before dense retrieval, or a hybrid BM25/dense retrieval plus time-aware re-ranking. This is the obvious competitor for the claim of "time-aware retrieval".
   - There is no comparison to established TKGQA methods (e.g., TempoQR, CronKGQA, MultiQA, and LLM-based TKGQA such as GenTKGQA, which the paper cites but does not compare against) that report on the same benchmarks. Absolute numbers on these benchmarks are very low (MultiTQ single-event Hit@1 ≈ 26%, even though such questions are almost solvable by keyword/time filtering), which suggests that the evaluation setting, rather than the method, is the bottleneck.
   - Baselines were adapted from static/medical settings and "tuned to the best achievable". The tuning budgets, the context sizes each uses, and the way the LLM answer is turned into a Hit@k list are not described. The prompt asks for 10 ranked candidates, so Hit@k for k ≤ 10 depends on the LLM's output formatting.
   - Only 1,000 questions per dataset are sampled and "average over five runs" is reported, but there is no variance, confidence interval or significance test, and no explanation of what is random (the LLM decoding temperature, presumably). Several baseline gaps are small (e.g., Hit@10 on MultiTQ 47.7 vs 41.5).
   - K1, K2 and the other hyperparameters (θ, β, α, K_type, subset length 3) appear to be chosen on test-set sensitivity (Sec. 4.6, Fig. 5). No validation split is mentioned.

5. **Results are partly puzzling and not analysed.**
   - STAR-RAG leaves single-event accuracy unchanged (25.8 vs 26.8 for TS-Retriever) but nearly doubles multi-event accuracy (44.4 vs 23.8) with only 10 retrieved events. There is no breakdown by question type (before/after, first/last, equal) or by temporal operator, no failure analysis, and no check that the retrieved set contains the gold event. Retrieval recall or precision against gold evidence is never reported, although the paper is about retrieval; only end-to-end LLM accuracy is shown.
   - The ablation Hit@1 for the no-rule variant (CronQuestion 55.3) is below the best static baseline (TOG 69.5), which is not discussed.
   - Hit@k is reported with the LLM generating the candidates, so it is conflated with generation quality. The backbone-robustness claim ("max drop 4.4%") is made while the baselines' backbones are not varied.

6. **Limited novelty and scope.**
   - Each component (Apriori-based typing and MDL summarization from Zhang et al. 2024 / KGist, PPR from HippoRAG, and rule graphs with temporal proximity as in GenTKG) is borrowed. The novelty is combining them, which is not evidenced to be the source of the gains (see 2 and 4).
   - All datasets are template-generated questions over ICEWS or Wikidata with well-structured quadruples, where entity-type patterns are very regular. Generalization to textual corpora, free-form temporal questions, implicit time references or noisier KGs is not tested. The rule graph assumes recurring relation patterns.
   - The Forecast dataset involves forecasting future events, but the paper does not discuss whether the rule graph is built on the full event set or only on history (possible leakage of test-period events into the rule statistics).

7. **Presentation issues.**
   - The acronym STAR is never defined.
   - The related work conflates time-series forecasting (Yang et al. 2025) with TKG modelling.
   - Several key quantities are deferred to the appendix or missing (Ã, K_type, how events map to multiple rule nodes with multiple labels, and the "decay coefficient" vs "restart probability" wording for α).
   - Algorithm 1 mixes offline and online steps.
   - "Hit@k" is called "accuracy" in places.

## Questions for the authors
1. Where exactly does the query's temporal constraint enter retrieval? Please show how Ã is built from the T_uv statistics, and quantify time-consistency (e.g., the fraction of retrieved events within the gold window or on the correct side of the anchor).
2. Can you explain when ΔL < 0 occurs in Eq. 7, given the sign of the L_cov term and L(M)? How many nodes and edges survive, and what happens if all Hamming-1 edges are kept or if time is removed from the MDL?
3. Does the 97% token saving hold when all methods are limited to the same top-10 context? Please report token and latency numbers against the no-rule top-10 baseline, and the offline construction cost and update cost.
4. How does STAR-RAG compare with (a) a timestamp/time-window filter plus dense retrieval, and (b) published TKGQA systems on these benchmarks?
5. Please report retrieval-level metrics (gold-event recall@K), per-question-type results, and variance over the five runs with significance tests.
6. How were hyperparameters chosen and on which split? Were rule statistics built on future events for Forecast?
7. Why are single-event questions unimproved while multi-event questions double? Is there a mechanism (e.g., sequence neighbours) that explains this?

## Ratings
- Soundness: 2
- Presentation: 3
- Contribution: 2
- Rating: 4
- Confidence: 4

**Justification.** The topic is useful and the empirical gains over the selected baselines are large. However, the central claim that rule-graph propagation enforces temporal consistency is not supported by the method description or by diagnostic evidence. The MDL formulation is unclear, and the efficiency claims are confounded by retrieval size. Obvious temporal and TKGQA baselines are missing, and the experimental protocol lacks variance, retrieval metrics and clean hyperparameter selection. The paper would need to address these before acceptance.
