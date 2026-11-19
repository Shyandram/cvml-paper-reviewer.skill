# Review: "Structured RAG for Answering Aggregative Questions" (S-RAG)

*Simulated panel review (full mode), target venue ICLR, literature check: strict, cutoff 2025-09-24. Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction. The five reviewers were run as five sequential role-based passes in one shared model context (not independent agents). Figures were not available (text extraction only): Figures 1–3 are judged from captions and text.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Structured RAG for Answering Aggregative Questions |
| Primary Discipline | NLP / information retrieval → retrieval-augmented generation, question answering over document corpora |
| Secondary Discipline(s) | Databases (text-to-SQL, information extraction / schema induction), LLM evaluation |
| Paper Type | Empirical (method + two new small datasets + evaluation); composite weights: empirical |
| Core Technique(s) | LLM schema induction, per-document LLM record extraction into an SQL table, LLM text-to-SQL, LLM-as-judge evaluation |
| Target Venue | ICLR (stated); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (ICLR: Soundness / Presentation / Contribution, Rating, Confidence; accepted share ≈ 27% of submissions) |
| Paper Maturity | Submission-ready preprint (formatted "Preprint"; core results only, short appendix) |
| Ethics-Relevant Content | none of substance: synthetic documents (HOTELS), Wikipedia (WORLD CUP), public financial filings (FinanceBench); LLM use disclosed (Appendix F) |

### Claimed Contributions (as stated by the authors, §1)
1. **C1 (problem):** "We highlight the importance of aggregative queries over a private corpus" and demonstrate the limitations of existing benchmarks and methods (§1, contribution 1).
2. **C2 (resource):** "We introduce two new datasets", HOTELS and WORLD CUP (§1, contribution 2).
3. **C3 (method):** a novel approach, S-RAG, and "show that it significantly outperforms existing methods" (§1, contribution 3).

### Paper memory (factual record, shared by all reviewers)

- **Setup facts.** Corpus D of n documents, one shared schema S (Eq. 1, §3.1). Schema prediction: iterative GPT-4o, 4 iterations, 12 documents + 10 questions, zero-shot (§3.2.1, App. B). Record prediction: LLM per document, type validation by post-processing code (§3.2.2); record/text-to-SQL model not named. Inference: question + schema + column statistics → SQL → result stringified → LLM answer (§3.3). Answer generator GPT-4o for S-RAG, GPT-o3 for VectorRAG and FullCorpus (§5.3). Judge GPT-4o for both metrics (App. E). VectorRAG: 500-token chunks, Qwen2-7B-instruct embedder, top-40, no BM25/rerank (App. A). FullCorpus: each document truncated to 20,000 tokens, concatenated until the context window is full (§5.1). OpenAI-Responses: closed agentic system with FileSearch (§5.1).
- **Splits / selection.** No train/validation/test split is described for the new datasets; the 12 documents and 10 questions for schema prediction are "later discarded from the dataset" (§5.2 (ii)). Gold schema "contains all the relevant attributes to answer all of the queries in all aggregative benchmarks" (§5.2 (i)). Seeds, number of runs, decoding temperature, variance: not stated after search. Code: not mentioned; datasets public (footnote 2, link removed).
- **Datasets (Table 1).** Hotels 350 docs / 596 tokens per doc / 193 queries; WorldCup 22 / 18,881 / 88 queries (text §4.2 says 83); FinanceBench 360 / 109,592 / 150 queries (50 aggregative, "FB-Agg", §5.4).
- **Headline numbers.** Table 3 (Answer Recall / Answer Comparison): Hotels S-RAG Gold 0.845 / 0.899, Inferred 0.500 / 0.518, VectorRAG 0.352 / 0.331, FullCorpus 0.478 / 0.473, OAI 0.253 / 0.184; WorldCup Gold 0.909 / 0.856, Inferred 0.766 / 0.769, VectorRAG 0.735 / 0.676, FullCorpus 0.516 / 0.441, OAI 0.715 / 0.566; FB-Agg Gold 0.750 / 0.725, Inferred 0.230 / 0.234, VectorRAG 0.650 / 0.598, FullCorpus 0.100 / 0.040, OAI 0.670 / 0.593. Table 4 (full FinanceBench): VectorRAG 0.598 / 0.677, OAI 0.529 / 0.553, Hybrid-S-RAG 0.667 / 0.702. Table 2 (o3 without context): FinanceBench 0.443 / 0.505, Hotels 0.047 / 0.049, WorldCup 0.798 / 0.712.
- **Appendix adds.** A: VectorRAG details. B: schema prompts. C: one example Hotels document (Figure 3, image not available). D: attribute statistics. E: Answer Comparison judge prompt only (the Answer Recall prompt is not shown). F: LLM-use statement.
- **Unverifiable.** Figures 1–3 (images); Eq. 1 is readable.

### Integrity signals
Manual scan (the integrity script was outside this run's allowed tools; I read the whole text and searched it for reviewer-directed phrases such as "ignore", "give a positive", "rate this"): **no text addressed to reviewers or AI systems was found.** The reviewers read the unmodified text.

### Literature check status
Mode **strict** (cutoff 2025-09-24). The fingerprint was written, but `scripts/related_search.py search` failed twice with "arXiv API unreachable (HTTP Error 429)", so **no kept results exist** (2 queries issued, purpose: claim C1 and C3; 0 benchmark queries; no `similarity`, `novelty`, `scout` or `verify` runs). Per the skill, the phase falls back to `literature check: off`: missing references come from knowledge and are all marked `[verify]`; no per-claim novelty profile was computed and no claim is declared "known". Gaps open: all claims, FinanceBench baseline scout.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Helena Marwick-Doyle, senior faculty at a large public research university (North America)
- **Seniority / Expertise**: senior faculty / information retrieval, retrieval-augmented generation, QA evaluation; ICLR-style area chair
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: judges against what the venue accepts; wary of oracle components in headline numbers

### Reviewer 1 (Methodology): Kofi Adjei-Mensah, industrial research lab (Western Europe)
- **Seniority / Expertise**: senior industry scientist / LLM-as-judge validity, benchmark contamination, RAG evaluation protocols
- **Focus**: design, statistics, fairness of comparison, reproducibility
- **Style**: insists on matched components and recomputes every delta

### Reviewer 2 (Domain): Lucía Ferrante-Oyelaran, NLP and IR group, public university (Southern Europe)
- **Seniority / Expertise**: mid-career faculty / multi-document QA datasets, structured extraction, text-to-SQL
- **Focus**: literature, theory, domain contribution
- **Style**: asks "what exactly is new relative to the closest prior system"

### Reviewer 3 (Perspective): Sung-min Ahlgren, data-management group, public university (East Asia)
- **Seniority / Expertise**: mid-career faculty / declarative analytics over unstructured data, enterprise data pipelines
- **Focus**: cross-disciplinary links (databases), deployment, assumptions, broader impact
- **Style**: constructive, expansive, positive but not uncritical

### Reviewer 4 (Generalist): Priyanka Tolliver, industrial ML lab (North America)
- **Seniority / Expertise**: mid-career industry researcher / representation learning and LLM applications, not RAG specifically
- **Focus**: contribution clarity, venue fit, presentation
- **Style**: typical program-committee member; weighs weaknesses against what accepted papers have

### Devil's Advocate: Mateus Brandl-Okafor, evaluation-methodology group (South America / Europe)
- **Seniority / Expertise**: postdoc / causal evaluation design, oracle-vs-deployable comparisons, claim auditing
- **Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous, never hostile

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Structured RAG for Answering Aggregative Questions
## Reviewer: Kofi Adjei-Mensah, Reviewer 1 (Methodology) (industrial research lab, Western Europe; fictional persona)
## Expertise: LLM-as-judge validity; benchmark contamination; RAG evaluation protocols
## Date: 2026-11-10

## Summary
The paper proposes S-RAG, which converts a corpus of same-type documents into an SQL table at ingestion time (LLM-induced schema, LLM-extracted records) and answers a question by translating it into SQL and giving the result to an LLM (§3). It introduces two datasets, HOTELS (synthetic pages) and WORLD CUP (Wikipedia, synthetic questions), and evaluates on them and on FinanceBench against VectorRAG, a truncated full-corpus baseline and OpenAI's file-search agent (§5–6). With an oracle ("gold") schema S-RAG wins by large margins; with a schema predicted from 12 documents and 10 questions the picture is mixed (Table 3).

## Strengths
### S1: The task is well chosen and the failure mode of top-K retrieval is real
§2 lists four concrete reasons chunk retrieval cannot answer aggregation questions (completeness, bounded context, long-range context, embedder limits). Table 5 shows this concretely: VectorRAG sees 13 of 22 tournaments and FullCorpus 8, so both aggregate incomplete evidence.
### S2: The gold-vs-inferred ablation is reported honestly
Table 3 reports both S-RAG-GoldSchema and S-RAG-InferredSchema, and §6 explains the gap by missing attributes and under-specified descriptions (the CapitalExpenditure "1" vs "1M" vs "1B" example). The schema-prediction inputs (12 docs, 10 questions) are said to be removed from the evaluation set (§5.2 (ii)).
### S3: Contamination is measured, not ignored
Table 2 runs o3 without context. It shows HOTELS is unseen (0.047 / 0.049) and WORLD CUP is largely known (0.798 / 0.712), which lets readers discount WORLD CUP.
### S4: Baseline details are partly given
App. A gives chunk size, embedder, top-K and the absence of BM25/rerank; App. B gives the schema prompts; App. E gives the judge prompt for Answer Comparison.

## Weaknesses
### W1: The headline gains come from an oracle schema built with knowledge of the test questions; the deployable variant does not consistently win
§5.2 (i) defines GoldSchema as containing "all the relevant attributes to answer all of the queries in all aggregative benchmarks", and §6 says it was built manually "via prompting" in "a few hours". The abstract and §6 ("Across all datasets, S-RAG consistently outperforms the baselines") rest on this variant. The only variant that uses no knowledge of the evaluation questions, InferredSchema, scores 0.234 Answer Comparison on FB-Agg against 0.598 (VectorRAG) and 0.593 (OAI-Responses): a gap of −0.364 and −0.359 (derived). On HOTELS its margin over the best baseline (FullCorpus) is +0.045 comparison / +0.022 recall (derived: 0.518−0.473, 0.500−0.478), on 193 questions.
- **Suggested Fix:** Report InferredSchema as the main S-RAG result everywhere, with GoldSchema labeled "oracle upper bound"; add a "schema from a different/held-out question set" variant and a human-written schema built without seeing evaluation questions. Narrow the abstract and §6 wording. Cost: ≈ 1 day of re-prompting plus no new corpus-level runs for Table 3 rows already present.

### W2: The new datasets are generated from the same schema-and-record representation that S-RAG inverts (design circularity)
§4.1 builds each dataset by first fixing a schema S, sampling records, verbalizing each record into a document, and generating questions "given a random subset of records". Every Hotels answer is therefore a function of schema attributes by construction, and the documents state the attributes explicitly (§4.2). The paper does not say whether the Hotels gold schema equals the generating schema S; if it does, Hotels Gold (0.899) mostly measures how well an LLM inverts a verbalization template. WorldCup gold answers come from 22 manually curated records (§4.2) with unreported curation or validation.
- **Suggested Fix:** State the relationship between gold and generating schemas; add a question-type breakdown (aggregate operator, number of documents involved, filter complexity); validate a sample of questions and gold answers with humans; and report one dataset where the question set was written independently of the schema (e.g., human-written). Effort: Medium.

### W3: The baselines are weak or narrowly configured for the claim "outperforms common RAG systems and long-context LLMs"
(a) FullCorpus truncates every document to 20,000 tokens and fills o3's context (§5.1). HOTELS totals ≈ 208.6k tokens (350 × 596, derived), barely over a 200k window, so a longer-context model would see the whole corpus; the paper's own explanation of FullCorpus's HOTELS score ("relatively smaller", §6) points to this. (b) VectorRAG fixes K = 40 chunks of 500 tokens (≈ 20k tokens, App. A) with no K sweep, although §2 identifies K as the problem; "preliminary experiments showed" BM25 and re-ranking "did not yield performance improvements", with no numbers. (c) No agentic baseline with code execution over retrieved documents, no GraphRAG-style baseline (cited, §7.1), and no extract-then-query baseline such as Arora et al. (2023) (cited, §7.1, but not run). (d) The statement that VectorRAG "is on-par with the best performing method reported by Wang et al. (2025)" (§5.1) gives no number or setting.
- **Suggested Fix:** Add a K sweep (K ∈ {40, 100, 200}) and a long-context (≥ 1M tokens) run on HOTELS; add an Evaporate-style or text-to-SQL-over-extracted-table baseline that shares S-RAG's extraction but not its schema induction; give the Wang et al. comparison numbers. Cost: roughly 3 × 350-document passes plus API spend on the order of tens of dollars.

### W4: Generator and judge asymmetry, and no judge validation
S-RAG answers with GPT-4o while baselines use o3 (§5.3), and the same GPT-4o family judges all outputs (App. E). The paper argues this favors the baselines, but it also means the judge is the S-RAG generator's model family, S-RAG outputs are short ("Average = 123.64", Table 5) and baseline outputs are long reasoning chains. No human agreement, no judge-bias check, and the Answer Recall prompt is not given (App. E shows only Answer Comparison).
- **Suggested Fix:** Human-check ≈ 100 judged answers per dataset; cross-judge with a different model family; run S-RAG with o3 as generator as well.

### W5: No variance; small evaluation sets; claimed gains on FinanceBench are within noise
Everything is a single run of stochastic LLM pipelines; decoding settings and seeds are not stated (searched). Binomial standard errors at p ≈ 0.5 are ≈ 0.036 (n = 193), 0.053 (n = 88), 0.071 (n = 50) (derived), so 95% intervals are ≈ ±0.07, ±0.10, ±0.14. Table 4 reports Hybrid-S-RAG over VectorRAG at 0.702 vs 0.677 comparison (+0.025, about 4 of 150 questions, derived) and Table 4 uses the gold schema built with knowledge of the benchmark's queries, yet §6 concludes it "demonstrate[s] that S-RAG can perform well also on general purpose datasets".
- **Suggested Fix:** Repeat each pipeline ≥ 3 times; report bootstrap CIs and paired tests; soften the §6 sentence. Cost: ≈ 3× current API spend.

### W6: Missing implementation, cost and failure analysis
The record-prediction model and the text-to-SQL model are not named (searched: GPT-4o appears only for schema prediction, answer generation and judging); the record-prediction and text-to-SQL prompts are not given; SQL failures, invalid values and documents longer than the context (FinanceBench averages 109,592 tokens, Table 1) are not discussed; ingestion cost is absent (360 × 109,592 ≈ 39.5M input tokens per pass, derived) against a chunk-and-embed baseline; no error breakdown (extraction vs text-to-SQL vs standardization) even though §6 attributes S-RAG's remaining errors to these.
- **Suggested Fix:** Release prompts and code, add an error taxonomy over the Gold-schema failures, and a cost/latency table.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | Table 1 vs §4.2 | "generate 83 aggregative questions" (§4.2); Table 1 lists 88 queries for World Cup | Same quantity differs between text and table | Cross-referenced two locations | High | MINOR | Reconcile (88 vs 83) |
| ERR-2 | E5 | §6, first paragraph | "Across all datasets, S-RAG consistently outperforms the baselines" | Table 3: InferredSchema on FB-Agg 0.234 vs 0.598 / 0.593 | Recomputed from Table 3 | High | MAJOR | Restrict claim to GoldSchema or reword |
| ERR-3 | E1 | §6, VectorRAG & OAI paragraph | "∼10-20% behind S-RAG-GoldSchema" / "∼50-60% behind" | Absolute differences vs OAI: WorldCup comparison 0.856−0.566 = 0.290; Hotels 0.899−0.184 = 0.715; "%" used for absolute points | Recomputed from Table 3 | High | MINOR | State absolute points and the ranges actually observed |
| ERR-4 | E8 | §3.3, §5.2 | "an LLM is instructed to translate it into a formal language query" | Model for text-to-SQL and record prediction not named | Full-text search for model names | High | MAJOR | Name models, versions, prompts, decoding settings |

Claim-to-evidence map (key claims): C1 "limitations of existing benchmarks and methods" (§1, Table 1) — Partially supported: the "Aggregative: High/Low" column of Table 1 is undefined and not measured. C2 datasets — Partially: released but unvalidated and schema-generated (W2). C3 "substantially outperforms both common RAG systems and long-context LLMs" (abstract) — Supported only for the oracle schema; Partially/Contradicted for the inferred schema on FB-Agg (W1).

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline numbers use an oracle schema over self-generated datasets, and the deployable variant loses on the one external benchmark.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Oracle component in headline; baseline and judge asymmetries; claim wording exceeds Table 3 |
| Clarity & Presentation | 66 | Competent | Short and readable; undefined Table 1 column, FB-Agg undefined in text, 88 vs 83 |
| Novelty & Originality | 52 | Developing | Pipeline of known pieces (schema induction + extraction + text-to-SQL); see R2 |
| Significance & Impact | 58 | Competent | Real problem; evidence of practical benefit rests on oracle and small sets |
| Experimental Validation | 44 | Developing | Small n, single runs, no CI, limited baselines, no failure analysis |
| Reproducibility | 50 | Developing | Schema prompts and VectorRAG details given; record/SQL prompts, models, code missing |
| Ethical Compliance | 66 | Competent | Synthetic/public data; limitations paragraph present but no deployment-risk discussion |

NeurIPS-style: Quality 2 (Technical Rigor and Experimental Validation average 47); Clarity 3; Significance 2; Originality 2.

## Questions for Authors
1. Is the HOTELS and WORLD CUP gold schema identical to the schema S that generated the records (§4.1)? If yes, how should Table 3 Gold rows be read? (Raises my score if the gold schema was written independently of the generator.)
2. What do Table 3 results look like with S-RAG using o3 as answer generator, and with a judge from a different model family?
3. What model and prompts do record prediction and text-to-SQL use, and what is the SQL-failure rate?
4. For the FinanceBench gold schema, which questions informed its attributes, and are any of those among the 150/50 evaluated?

## Limitations Assessment
**Partially.** §8 names the single-schema assumption and simple attributes; it does not discuss reliance on an oracle for the best numbers, extraction errors silently corrupting aggregates, or ingestion cost.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: Useful task and honest gold/inferred split, but the abstract-level claim rests on an oracle schema over author-generated data, with a single run and no validation of judge or questions.

## Confidence
**4**: Careful read of a short paper; did not run code; figures unavailable.

---

# Peer Review Report

## Paper: Structured RAG for Answering Aggregative Questions
## Reviewer: Lucía Ferrante-Oyelaran, Reviewer 2 (Domain) (NLP and IR group, public university, Southern Europe; fictional persona)
## Expertise: multi-document QA datasets; structured extraction; text-to-SQL
## Date: 2026-11-10

## Summary
S-RAG turns "aggregative" questions (those needing evidence from many documents) into database queries by first inducing a schema and extracting one record per document with an LLM. The paper contributes this pipeline, two small datasets, and experiments showing that, given a well-specified schema, SQL over the extracted table answers such questions far better than top-K chunk retrieval or a truncated long-context prompt.

## Strengths
### S1: A clear, practically motivated gap
§1–§2 frame analyst-style questions ("average ARR for South American companies...") and show why top-K retrieval, a fixed K and embedder limits (Weller et al., 2025) break them. The problem statement is crisp and a good fit for ICLR's applied-LLM audience.
### S2: Appropriate decomposition into schema, record and query stages
Eq. 1 and §3.2–3.3 give a simple, auditable intermediate representation; the type validation and attribute statistics (§3.2.2, App. D) are sensible engineering that lets the query LLM map phrases to lexical values.
### S3: Datasets targeting unseen content
HOTELS is fully synthetic so that parametric knowledge cannot help (Table 2: 0.047 / 0.049), which is a thoughtful design relative to Wikipedia-based multi-answer sets (§7.2).
### S4: Related-work paragraph engages two near neighbors
§7.1 cites GraphRAG (Edge et al., 2024) and Arora et al. (2023) and explains the difference from each in one sentence.

## Weaknesses
### W1: Novelty of the method is incremental against extract-then-query systems, and the closest one is not evaluated
Schema induction + per-document LLM extraction into a table + query is the core of Arora et al. (2023) ("generating structured views of heterogeneous data lakes"), which the paper cites but dismisses because it "was not evaluated in the context of RAG performance" (§7.1). That is a reason to run it as a baseline, not to skip it. The additions here (question-conditioned schema refinement, column statistics for text-to-SQL, a hybrid fallback) are reasonable but small, and the paper does not isolate them with ablations (e.g., schema refinement iterations, statistics on/off). Relevant adjacent work on LLM-powered analytics over unstructured text (table-augmented generation, semantic operators, declarative document-processing pipelines) is not discussed at all. Novelty: MAJOR at most, since the difference is cited and argued, if briefly.
- **Suggested Fix:** Add a novelty-delta table against the closest systems; run an Evaporate-style baseline; ablate statistics and iterations.

### W2: Positioning of the datasets against existing multi-document benchmarks is thin
§7.2 argues existing sets "do not focus on large-scale retrieval, and are based on Wikipedia", and Table 1 labels FinanceBench "Aggregative: Low" and the new sets "High" without defining or measuring the property. Wolfson et al. (2025, MoNaCo) and Amouyal et al. (2023, QAMPARI) are cited, but S-RAG is not run on them and no statistic (documents per question, aggregate operator mix) shows the new sets are harder in the relevant sense. WORLD CUP is also Wikipedia (the very property criticized) and is flagged "LLM leak ✓" (Table 1).
- **Suggested Fix:** Define "aggregative" (e.g., minimum number of evidence documents plus an aggregate operator), report it per dataset, and either run on a subset of MoNaCo-like questions or explain why S-RAG cannot.

### W3: Domain-specific evaluation practice for extraction-based pipelines is missing
For an extraction pipeline the natural diagnostics are per-attribute extraction accuracy against gold records and SQL execution accuracy; the paper has gold records for HOTELS and WORLD CUP (§4.1–4.2) but reports only end-to-end judged answers. Without them, §6's statement that the remaining errors come from "imperfect text-to-sql conversion, standardization issues in the ingestion phase, and wrong records prediction" is unquantified.
- **Suggested Fix:** Report record-level precision/recall per attribute and execution accuracy of generated SQL.

### W4: The "FinanceBench is public and aggregative" claim needs care
Only 50 of 150 FinanceBench questions are tagged aggregative ("metrics-generated queries", footnote 4); such questions typically need a few values from one filing, which Table 1 itself describes as "up to a single document" (§4.2). So FB-Agg is a weak test of cross-document aggregation, and the S-RAG result there (Gold 0.725, Inferred 0.234) says more about schema coverage of financial statements than about corpus-level aggregation.
- **Suggested Fix:** Say so in §5.4 and add an aggregative financial setting that really spans filings (e.g., cross-company questions).

### Minor
"Antropic" (§2, references); "JLM PROMPT" heading (App. E); FB-Agg and "OAI-Responses" used in Table 3 but named differently in text (§5.1 "OPENAI-RESPONSES").

## Missing References
*Literature check unavailable (arXiv API HTTP 429); all entries marked [verify] and described as lines of work. None can be a "required comparison" under the strict-mode rule since they were not verified; they are context for Related Work.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Arora et al., *Language models enable simple systems for generating structured views of heterogeneous data lakes* (arXiv 2023) — already cited | Closest extract-then-query system; run it (or an equivalent) as a baseline |
| Important | Biswal et al., "Text2SQL is Not Enough: Unifying AI and Databases with TAG", arXiv 2024 [verify] | Table-augmented generation: LLM queries combining SQL and LM reasoning; same task family |
| Important | Patel et al., "Semantic Operators: A Declarative Model for Rich, AI-based Analytics Over Text Data" (LOTUS), arXiv 2024 [verify] | Declarative LLM operators for aggregation/filtering over text corpora |
| Important | Li et al., "StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization", ICLR 2025 [verify] | Structuring retrieved information at inference time for reasoning-heavy queries |
| Helpful | Shankar et al., "DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing", arXiv 2024 [verify]; Lin et al., "Towards Accurate and Efficient Document Analytics with Large Language Models" (ZenDB), arXiv 2024 [verify]; Liu et al., "Palimpzest" (CIDR 2025) [verify] | Document-analytics systems with schema/extraction/optimization |
| Helpful | Line of work: LLM-based text-to-SQL and table QA (2023–2025) | Informs how the SQL-generation stage should be evaluated |

**Citation check (E7).** Arora et al. (2023) is described in §7.1 as building "structured representation of an unstructured corpus" and "not evaluated in the context of RAG performance"; this matches the title in the reference list ("generating structured views of heterogeneous data lakes"). Edge et al. (2024) is described as "primarily designed for global sense-making questions"; the reference title ("From local to global ... query-focused summarization") is consistent. Wang et al. (2025) is cited as "corpus-specific training" (§7.1) and as the best FinanceBench system (§5.1); the reference is FinSage, a multi-aspect RAG system, which does not obviously match "corpus-specific training" — I could not verify this from the text alone (question, not an error).

**Per-claim novelty (no literature check; from the paper's related work and knowledge, [verify]).** C1 problem: medium (aggregation over many documents is discussed by QAMPARI/MoNaCo, cited). C2 resource: medium (small synthetic sets; document-type novelty of HOTELS). C3 method: incremental (extract-then-query is established; refinements are modest).

**Field snapshot (from knowledge, not search results).** Around 2020–22 RAG meant dense top-K chunk retrieval for single- and multi-hop QA. By 2024–25 attention shifted to long-context models, graph/structured indexing, agentic multi-step retrieval and LLM-driven analytics over documents; benchmarks like MoNaCo and QAMPARI test multi-document aggregation, and FinanceBench is a standard stress test. Open problems: reliable extraction at scale, schema discovery, evaluation of aggregation. A significant contribution now shows a deployable (non-oracle) pipeline that beats strong agentic and long-context baselines on independently written questions; a +10-point gain with an oracle schema on self-generated data is suggestive, not yet significant.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in baselines and diagnostics |
| Clarity | 3 | Clear, short |
| Significance | 2 | Real problem, evidence limited |
| Originality | 2 | Combination of known pieces |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental method relative to a cited, un-run neighbor; datasets small and generated from the method's own representation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound pipeline; stages not individually evaluated |
| Clarity & Presentation | 68 | Competent | Understandable; undefined "aggregative" measure |
| Novelty & Originality | 50 | Developing | Incremental over extract-then-query systems |
| Significance & Impact | 58 | Competent | Useful niche; limited evidence |
| Experimental Validation | 48 | Developing | See R1; no per-stage diagnostics |
| Reproducibility | 54 | Competent | Prompts partly shown, models/code missing |
| Ethical Compliance | 66 | Competent | Little at stake; limitations paragraph present |

## Questions for Authors
1. What exactly does S-RAG add over an Evaporate-style pipeline plus text-to-SQL? An ablation answering this would raise my Novelty score.
2. Can you give record-level extraction accuracy against the gold records for HOTELS and WORLD CUP?
3. How would S-RAG behave on MoNaCo- or QAMPARI-style questions where the answer set is entity lists?

## Limitations Assessment
**Partially.** Single-schema and simple-attribute limits are stated (§8); missing: dependence on extraction quality, schema drift, and comparison scope.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: Reasonable idea and useful problem framing, but novelty is incremental against a cited system that is not tested, and the evaluation does not isolate what S-RAG adds.

## Confidence
**4**: Know the QA and extraction literature; reference claims not checked online.

---

# Peer Review Report

## Paper: Structured RAG for Answering Aggregative Questions
## Reviewer: Sung-min Ahlgren, Reviewer 3 (Perspective) (data-management group, public university, East Asia; fictional persona)
## Expertise: declarative analytics over unstructured data; enterprise pipelines
## Date: 2026-11-10

## Summary
The paper revives a classical idea from data management: if a corpus's documents are instances of one entity, extract them into a relational table and let a query engine do the aggregation, using LLMs both to build the table and to write the query. It shows large gains over chunk-based RAG when the schema is right, and degradation when the schema is predicted automatically.

## Strengths
### S1: Right abstraction for a recurring enterprise need
Aggregations, filters and extremes ("highest number of reviews", §1) are what relational engines do exactly; delegating them to SQL removes the completeness and arithmetic failure modes shown in Table 5 (VectorRAG's 13 of 22 tournaments).
### S2: Schema/record separation gives inspectable, auditable state
The intermediate table (§3.2, App. D statistics) can be examined, corrected and reused across queries, unlike an LLM reading a long context each time.
### S3: Hybrid mode is a pragmatic bridge
§3.3 uses SQL to narrow the corpus when the schema lacks an attribute, then classical RAG; Table 4 suggests the approach is not confined to aggregation questions, though the gain is small (0.702 vs 0.677 comparison) and the schema is the gold one.
### S4: Honest scoping
§8 states the single-schema restriction and the absence of list/nested attributes (footnote 3).

## Weaknesses
### W1: The practical value hinges on schema creation, which the paper treats as an afterthought
The best results need a gold schema that, per §6, "required only a few hours" to build manually via prompting, by someone who knows the queries. In practice enterprise users do not know future questions; schema drift, new attributes and rare attributes (§3.3) are the main failure sources and the paper's fallback is the hybrid mode, evaluated once (Table 4). This is an opportunity: databases have decades of work on schema matching, incremental view maintenance and attribute discovery that could be used here.
- **Suggested Fix:** Evaluate schema coverage (what share of questions are answerable from the induced schema) and show how performance degrades as questions go outside the schema; discuss incremental schema extension.

### W2: Deployment assumptions are unexamined: privacy, cost, silent errors
The motivation is a "private corpus" (§1), yet the pipeline sends every document to a hosted LLM (GPT-4o, App. B) at ingestion. Per-document LLM calls scale linearly with corpus size and with every schema change (FinanceBench ≈ 39.5M input tokens per pass, derived from Table 1), but no cost or latency figures are given. An extraction error becomes a silently wrong aggregate with no provenance back to the source span.
- **Suggested Fix:** Report ingestion cost/latency, add provenance (source span per value) and an uncertainty or validation mechanism; discuss on-prem models.

### W3: Assumptions about the data and the questions
(i) Each document is one entity with recurring attributes (§1, §3.1), which fits hotel pages and 10-K filings but not mixed corpora (acknowledged, §8). (ii) Questions are answerable by one SQL query over one table; joins, nested attributes and temporal reasoning are excluded (footnote 3). (iii) Benchmarks built from the schema (§4.1) favor this assumption by construction. Real analyst questions often mix attribute-answerable and free-text parts.
- **Suggested Fix:** Report what fraction of FinanceBench questions fail the single-table assumption; add a small multi-entity corpus case.

### Broader impact
No ethics concern beyond the usual: aggregate statistics from LLM-extracted records could mislead financial or HR decisions (the paper's own examples); a sentence on validation before use is warranted.

### Minor
Table 1's "LLM leak?" column uses ✓/× without definition.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound design; evaluation limited |
| Clarity | 3 | Clear |
| Significance | 3 | Fits a real need |
| Originality | 2 | Combination of known techniques |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear and practically relevant idea with large effect where it applies; weaknesses (oracle schema, small sets) are common among accepted application papers, though here they touch the main claim.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound approach, caveats on evaluation |
| Clarity & Presentation | 72 | Competent | Readable |
| Novelty & Originality | 60 | Competent | Well-motivated combination |
| Significance & Impact | 70 | Competent | Strong practical relevance |
| Experimental Validation | 56 | Competent | Adequate to show the effect, not the margin |
| Reproducibility | 58 | Competent | Partial prompts, no code mentioned |
| Ethical Compliance | 64 | Competent | Little at stake; deployment risks undiscussed |

## Questions for Authors
1. What share of FinanceBench and HOTELS questions are answerable from the inferred schema (coverage)? A high coverage with an extraction-failure explanation would raise my Significance score.
2. Can values carry source spans so that users can audit an aggregate?
3. How does cost scale with corpus size relative to VectorRAG?

## Limitations Assessment
**Partially.** Scope limits stated; deployment limits (privacy, cost, provenance) are not.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: A relevant, intuitive system with large effects when the schema is right; I lean to accept because the weaknesses are fixable and typical of applied papers, but I hold this with modest confidence.

## Confidence
**3**: Strong on the database side, less on current RAG baselines.

---

# Peer Review Report

## Paper: Structured RAG for Answering Aggregative Questions
## Reviewer: Priyanka Tolliver, Reviewer 4 (Generalist) (industrial ML lab, North America; fictional persona)
## Expertise: LLM applications; representation learning (non-specialist in RAG)
## Date: 2026-11-10

## Summary
The paper argues that RAG systems are built for questions answerable from a few passages, and proposes S-RAG for questions that aggregate over many documents: build a table from the corpus with an LLM, translate the question to SQL, answer from the result. It adds two small datasets and shows large gains with an oracle schema, mixed gains with an automatically induced schema.

## Strengths
### S1: Easy to understand and well motivated
§1–§2 explain the problem with concrete examples; Figure 1 (caption) and Table 5 make the pipeline and the failure of baselines tangible. A non-specialist gets the point in one read.
### S2: Interesting and honest results structure
Reporting Gold vs Inferred schema (Table 3) and measuring parametric knowledge (Table 2) are habits I would like to see more often.
### S3: Datasets are released and match the problem
Footnote 2 states public availability of HOTELS and WORLD CUP; a benchmark for this question type is useful to the community even if small.
### S4: Good fit to ICLR's applied-LLM audience
A system paper with a new task framing and datasets is in scope; the idea is simple and could be adopted.

## Weaknesses
### W1: Evidence is thinner than the abstract suggests
The abstract says S-RAG "substantially outperforms both common RAG systems and long-context LLMs", but the large wins use the gold schema (Table 3), the full-FinanceBench gain is 0.025 (Table 4), and the long-context baseline is a truncated o3 prompt (§5.1). I read the claim as true for Gold on HOTELS and WORLD CUP, and as unproven for the deployable version.
- **Suggested Fix:** Rewrite the abstract and §6 around InferredSchema, with Gold as an upper bound; show confidence intervals.

### W2: The datasets are small and described only at a high level
HOTELS has 193 questions, WORLD CUP 88 (Table 1; §4.2 says 83), and the paper gives no question-type statistics, no examples beyond one HOTELS question (§1) and one WORLD CUP question (Table 5), no validation of gold answers, no license/datasheet information (not stated after search).
- **Suggested Fix:** Add a dataset section with question taxonomy, statistics and validation; add a datasheet in the appendix.

### W3: Presentation of the experiments leaves the reader to reconstruct the protocol
Which model does record prediction and SQL generation (not stated), what is FB-Agg (used in Table 3 but only described in §5.4), what are Hybrid-S-RAG's generator and retriever (§5.2 (iii) says VectorRAG over the sub-corpus), and what Answer Recall's decomposition prompt is (not in App. E).
- **Suggested Fix:** Add a protocol table listing the model, prompt and decoding settings for each component and baseline.

### Venue-criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | abstract vs Table 3 |
| Contribution: new insight or capability | Partly | §3, Table 3 Gold rows |
| Presentation: readable, complete protocol | Partly | §5, App. A–E |
| Reproducibility: artifacts, details | Partly | footnote 2, App. A–B |
| Honest limitations | Partly | §8 |

### Minor
Typos ("Antropic", "JLM PROMPT"); inconsistent system names (OAI-Responses / OPENAI-RESPONSES).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound design; evidence partly oracle |
| Clarity | 3 | Clear and short |
| Significance | 3 | Useful direction |
| Originality | 2 | Assembly of known techniques |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear problem, readable paper, real effect when the schema is good; weaknesses typical of accepted applied papers but sit close to the main claim.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound idea, uneven evaluation |
| Clarity & Presentation | 72 | Competent | Easy to follow; protocol gaps |
| Novelty & Originality | 58 | Competent | Useful combination |
| Significance & Impact | 66 | Competent | Relevant to industry and research |
| Experimental Validation | 56 | Competent | Three datasets, but small and oracle-based |
| Reproducibility | 56 | Competent | Partial |
| Ethical Compliance | 64 | Competent | Little at stake |

## Questions for Authors
1. Can you give InferredSchema numbers with confidence intervals and a second inferred-schema seed? A stable gap on HOTELS and WORLD CUP would raise my score.
2. Which numbers in the abstract refer to Gold and which to Inferred?
3. Is code released?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: Clear paper on a useful problem with a plausible approach; I would accept if the claims were narrowed to what the inferred schema shows, but the current evidence is not far above a typical borderline submission.

## Confidence
**4**: Fully read; less familiar with RAG-specific baselines.

---

# Devil's Advocate Report

## Paper: Structured RAG for Answering Aggregative Questions
## Reviewer: Mateus Brandl-Okafor, evaluation-methodology group (fictional persona)

---

## Steelman
Top-K retrieval cannot in principle answer questions that need all instances of an entity; materializing a table and delegating aggregation to SQL is the natural fix, and on three datasets with a good schema it beats the best baseline by about 13–43 points of Answer Comparison (derived from Table 3: FB-Agg 0.725−0.598, WorldCup 0.856−0.676, Hotels 0.899−0.473). Schema quality is the identified bottleneck, and the authors say so.

---

## Core Argument Chain
1. Aggregative queries need many documents and arithmetic; top-K RAG and truncated long context fail (§2, Table 5).
2. A structured table plus SQL handles completeness and aggregation (§3).
3. On HOTELS, WORLD CUP and FB-Agg, S-RAG (gold schema) beats VectorRAG, FullCorpus and OAI-Responses (Table 3).
4. Schema induction from 12 docs and 10 questions makes this practical (§3.2.1, §6).
5. Hybrid-S-RAG extends the benefit to general QA (Table 4).
∴ S-RAG "substantially outperforms both common RAG systems and long-context LLMs" (abstract).

---

## Strongest Counter-Argument
Premise 3 is true only for an oracle, and premise 4 is untested where it matters. The claim "S-RAG outperforms RAG" is a claim about a system a user could deploy, i.e., InferredSchema. That variant beats the best baseline on HOTELS by +0.045 comparison / +0.022 recall (0.518 vs 0.473; 0.500 vs 0.478), on WORLD CUP by +0.093 comparison over VectorRAG (0.769 vs 0.676) while the context-free o3 already gets 0.712 (Table 2), and it loses by −0.364 / −0.359 on FB-Agg (0.234 vs 0.598 / 0.593) — the one dataset not written by the authors. The paper's response is that the gold schema takes "a few hours" (§6), but a gold schema "contains all the relevant attributes to answer all of the queries" (§5.2 (i)): it is a schema written by a person who has read the evaluation questions, i.e., it injects the answer's structure. On the two author-built datasets the questions are generated from schema records (§4.1), so every answer is a function of schema attributes by design, and nothing in the paper tells the reader whether the gold schema is the generating schema. So Gold rows measure (extraction fidelity of an LLM given the exact answer-relevant attributes) rather than (the ability to cope with aggregative questions). In short: the baselines are asked to discover which of dozens of documents matter; S-RAG-Gold is told. A fair oracle comparison would give baselines the same help (e.g., the list of relevant documents or the gold records), and a fair deployable comparison would use the inferred schema and show it wins. The paper currently has only one of these, and it does not win on the external benchmark.

---

## Issue List

### CRITICAL Issues
**No CRITICAL issues found.** The evidence supports a weaker claim (oracle schema wins; inferred schema is mixed) and the fix is to narrow the claim and add controls, so none of the strict criteria is met (the oracle is disclosed, labeled as such in §5.2, and the Inferred rows are reported; there is no test-set selection of a reported configuration, no fabrication, no unreadable method).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / Scope | Abstract, §6, Table 3 | Headline "substantially outperforms" and "consistently outperforms the baselines" rest on GoldSchema; InferredSchema loses on FB-Agg (0.234 vs 0.598/0.593) and is within ~0.05 of the best baseline on HOTELS (evidence supports a weaker claim, not a contradicted one) | Lead with Inferred, label Gold as oracle, narrow wording |
| DA-M2 | Logic / Evaluation design | §4.1, §5.2 (i), Table 3 | Questions are generated from schema records, and the gold schema covers the attributes needed by all evaluation queries; whether Gold = generating schema is unstated (question) | State the relation; add a baseline given equivalent oracle help; add independently written questions |
| DA-M3 | Alternative explanation | §5.3, Table 2 vs 3 | WORLD CUP: every baseline except S-RAG scores below the context-free o3 (comparison 0.676, 0.441, 0.566 vs 0.712), so the dataset does not test retrieval and the instruction to ignore knowledge (§5.3) is not verified | Run with entity names masked or a post-cutoff event; report context-free results alongside |
| DA-M4 | Evidence | Table 4, §6 | "demonstrate that S-RAG can perform well also on general purpose datasets": +0.025 comparison (≈ 4 questions of 150, derived), gold schema built from the benchmark's queries, no CI | Soften; run CIs; use inferred schema |
| DA-M5 | Fair comparison | §5.1, §5.3, App. E | Different generators (GPT-4o vs o3), same GPT-4o judge family, no human validation; FullCorpus is a truncated o3 prompt, not a long-context system (Hotels corpus ≈ 208.6k tokens, derived) | Cross-judge, human check, ≥ 1M-token context baseline |
| DA-M6 | Novelty / Overclaiming | §1 C1, Table 1, §7.1 | C1 "demonstrate the limitations of existing benchmarks and methods" and Table 1's "Aggregative: High/Low" lack a definition or measurement; the closest extract-then-query system (Arora et al., 2023) is cited and not run | Define and measure; add the baseline |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 1 vs §4.2 | 88 vs 83 WORLD CUP queries |
| DA-m2 | Consistency | §6 | "∼10-20%" / "∼50-60%" understate gaps to OAI-Responses (0.290 and 0.715 absolute on comparison, derived) and mix absolute points with "%" |
| DA-m3 | Reproducibility | §3.3, App. E | Record/SQL models, Answer Recall prompt, decoding, seeds not stated |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| §6 VectorRAG/OAI "∼10-20% behind" Gold (WorldCup, FB) | ∼10–20% | WorldCup comparison: 0.856−0.676 = 0.180, vs OAI 0.290; FB-Agg: 0.725−0.598 = 0.127, vs OAI 0.132; recall: 0.174/0.194 (WC), 0.100/0.080 (FB) | Mostly; OAI on WorldCup comparison is 0.29 |
| §6 Hotels "∼50-60% behind" Gold | ∼50–60% | 0.899−0.331 = 0.568; 0.899−0.184 = 0.715; recall 0.845−0.352 = 0.493, 0.845−0.253 = 0.592 | Partly (OAI comparison 0.715) |
| Table 1 vs §4.2 WORLD CUP queries | 88 vs 83 | n/a | No |
| Table 4 Hybrid vs VectorRAG | 0.702 vs 0.677 | +0.025 (≈ 4 of 150 questions) | Yes (arithmetic), gain small |
| Hotels corpus vs o3 context (§6 "All datasets exceed GPT-o3's context window") | 350 docs × 596 tokens | ≈ 208,600 tokens | Barely exceeds a 200k window |

## Ignored Alternative Explanations
- Gold-schema wins reflect leakage of question structure into the schema rather than better aggregation handling.
- WORLD CUP results partly reflect parametric knowledge (Table 2) and the model-family difference (GPT-4o vs o3).
- A text-to-SQL or code-interpreter pipeline over any extraction (not S-RAG's schema induction) could achieve the same Gold-row numbers.
- A GPT-4o judge may favor short, GPT-4o-style answers.

## Missing Stakeholder Perspectives
Practitioners who must audit an aggregate (no provenance), organizations whose corpora cannot leave their premises (hosted-LLM ingestion), and the annotators/curators of the WORLD CUP records (curation process unreported).

## Observations (Non-Defects)
Reporting both Gold and Inferred rows, measuring context-free performance (Table 2), removing the schema-prediction documents from the evaluation set (§5.2 (ii)) and disclosing the limitation to single-schema corpora (§8) all make the paper easy to audit and are the reason no issue here is CRITICAL.

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Oracle and generation circularity; asymmetric components |
| Clarity & Presentation | 68 | Clear; minor inconsistencies |
| Novelty & Originality | 48 | Assembly of established components; closest system not tested |
| Significance & Impact | 56 | Real problem; evidence not yet decisive |
| Experimental Validation | 40 | Small n, single run, weak/narrow baselines, no failure analysis |
| Reproducibility | 50 | Key models and prompts missing |
| Ethical Compliance | 62 | Little at stake |

## Overall: 3 | Confidence: 4

---

# Phase 1.5 / 1.6

**Literature check:** not run to completion (arXiv API HTTP 429 twice). See Phase 0 status; every recommended reference above is marked `[verify]`, none was required.

**Report check (Phase 1.6).** Each weakness in the five reports was tested for specificity, whether the paper already answers it (full-text search, appendix included), consistency with the paper, and actionability. Scores unchanged.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1-W2 / DA-M2 | "gold schema equals generating schema" | rewritten as a question | The paper does not state this (searched §4.1, §5.2, App. B–C); kept as an open question and a design-circularity concern |
| R2-W4 | FinanceBench "single-document" aggregative queries | rewritten | §4.2 says questions "typically require up to a single document"; wording aligned to that quote |
| R3-W3 (iii) | benchmarks favor single-schema assumption | kept | consistent with §4.1 |
| R4 / R2 minor | "Antropic", "JLM PROMPT", naming of OAI-Responses | moved to Minor | cosmetic |
| R1-W6 | missing cost analysis | kept | no cost figure found after search |
| All | — | none dropped | none was answered by the appendix; none contradicted by the paper |

---

# Phase 2: Synthesizer Package, EIC Meta-Review and Decision

## Synthesizer, part A: issue map

| Merged issue | Source IDs | Class |
|---|---|---|
| Headline claims rest on oracle gold schema; Inferred loses on FB-Agg / marginal on HOTELS | R1-W1, R4-W1, R3-W1, DA-M1, (R2-W4) | CONSENSUS-4 (outcome may hinge) |
| Datasets generated from the schema representation, small, unvalidated, no question taxonomy | R1-W2, R2-W2, R4-W2, DA-M2, R3-W3(iii) | CONSENSUS-4 |
| Baselines/judge/generator asymmetry, truncated "long context" | R1-W3, R1-W4, DA-M5 | CONSENSUS-2 |
| No variance / tiny gain in Table 4 | R1-W5, DA-M4, R4 Q1 | CONSENSUS-3 |
| Novelty vs extract-then-query systems (Arora et al.); no ablation of additions | R2-W1, DA-M6 | CONSENSUS-2 |
| Missing implementation/prompts/cost | R1-W6, R4-W3, R3-W2, DA-m3 | CONSENSUS-3 |
| WORLD CUP contaminated (baselines below context-free o3) | DA-M3, R1-S3 (partially) | SOLO |
| Deployment: privacy, provenance | R3-W2 | SOLO |
| 88 vs 83 | R1 ERR-1, DA-m1, R4-W2 | CONSENSUS-3 (minor) |
| Splits: R3 (Overall 4) and R4 (Overall 4) vs R1, R2, DA (Overall 3) | — | SPLIT (Overall) |

DA-CRITICAL issues: none. Official output (before EIC weights; `before.json`): official mean rating 3.40, composite 56.9, band 3, no warnings; pool positions 45 / 48 / 66 / 66 / 42 (spread 24, below the 30-point rule).

## EIC Meta-Review (Helena Marwick-Doyle)

### The Case For and Against
- **For acceptance:** A timely, easily understood problem (aggregation over many documents) with a pipeline that fixes real failure modes of top-K retrieval (Table 5). With a well-specified schema the gains are very large (HOTELS 0.899 vs 0.331 comparison; WORLD CUP 0.856 vs 0.676), results are reported honestly with and without an oracle, two datasets are released, and the weaknesses (single runs, narrow baselines) are the kind many accepted applied papers share.
- **Against acceptance:** The abstract-level claim is carried by an oracle schema built with knowledge of the evaluation questions, on datasets generated from the same schema-and-record representation; the deployable InferredSchema variant loses badly on the only external aggregative subset (0.234 vs 0.598/0.593) and is marginal on HOTELS. Method novelty is incremental against Arora et al. (2023), which is not run; evaluation has no variance, small n, and unvalidated judge/gold answers.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Gold schema contains attributes for all queries (oracle) | R1-W1, DA-M1, R4-W1 | §5.2 (i) | **Verified** | "contains all the relevant attributes to answer all of the queries in all aggregative benchmarks" |
| InferredSchema loses on FB-Agg | R1-W1, DA | Table 3 | **Verified** | 0.234 vs 0.598 and 0.593; recall 0.230 vs 0.650 / 0.670 |
| "Across all datasets, S-RAG consistently outperforms the baselines" | R1 ERR-2, DA-M1 | §6 first paragraph | **Verified** as an overstatement (true for Gold only) | |
| Gold schema = generating schema on Hotels / WorldCup | R1 Q1, DA-M2 | §4.1, §5.2 | **Partly correct** | §4.1 describes schema-first generation; the paper does not state the relation. Treated as an open question, not as an error |
| FullCorpus is a truncated o3 prompt; Hotels ≈ 208.6k tokens | R1-W3, DA-M5 | §5.1, §6, Table 1 | **Verified** (arithmetic derived) | The 200k window is o3's as stated by the paper; I did not check it |
| WORLD CUP baselines below context-free o3 | DA-M3 | Tables 2, 3 | **Verified** | 0.676 / 0.441 / 0.566 vs 0.712 |
| 88 vs 83 WORLD CUP queries | R1 ERR-1 | Table 1, §4.2 | **Verified** | minor |
| Table 4 gain small; gold schema used | R1-W5, R3-S3, DA-M4 | Table 4, §5.2 | **Verified** | R3 cites it with the right hedge |
| Record/text-to-SQL models not named | R1 ERR-4 | §3.2.2, §3.3 | **Verified** | search for model names finds only schema, answer and judge uses |
| Novelty gap vs Arora et al. | R2-W1, DA-M6 | §7.1 | **Partly correct** | The paper cites it and differentiates it in a sentence (not evaluated for RAG); that is weak differentiation, MAJOR at most, not "known" |
| Wang et al. described as "corpus-specific training" | R2 | §7.1 vs references | **Unverified** (no literature check) | kept as a question |
| Privacy of private-corpus motivation with hosted LLM | R3-W2 | §1, App. B | **Verified** | no discussion in the paper |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log entry re-checked and holds; the decisive oracle-vs-inferred point is verified and well calibrated |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; novelty point verified but partly hedged; citation point unverifiable offline |
| R3 (Perspective) | 4 | 3 | 1.0 | Verified deployment points; rating a little generous given its own W1, but hedged |
| R4 (Generalist) | 4 | 4 | 1.0 | Correctly reads the abstract claim as Gold-only; rating a bit lenient relative to its own W1 |
| DA | 3 | 4 | 1.0 | Strongest objection verified in substance; the generating-schema premise is only a question; calibration to "no CRITICAL" is right |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so there is nothing to uphold or downgrade (`da_critical` is empty in both runs). I independently considered whether the oracle schema meets criterion 1 or 2: the evidence contradicts only the *wording* of the main claim (§6 "consistently"), not the claim that S-RAG with a given schema beats the baselines, and the experiment does test that; so the issue is MAJOR (narrow the claim), not fatal. The oracle is also not a "test-set selection" case under criterion 3: no configuration was chosen by its score on the reported set.

### Final Decision and Justification
Starting point: the EIC-weighted rating is 3.36 (official mean 3.40), which rounds to **3**; the composite cross-check (official 56.9, EIC-weighted 56.5) is also in band 3, so the two signals agree and no departure is warranted. My own pool position is **about 52%**: better than about half the ICLR submissions, in the "typical rejected" band (42–54) but near its upper edge. The deciding evidence: (i) the deployable variant does not clearly beat baselines on the one external aggregative subset, so the abstract's main claim is not supported as worded; (ii) the new datasets cannot arbitrate because their questions are produced from the same records that define the gold schema (the relation is unstated, so I treat this as a question); (iii) the method is an assembly of established parts whose contribution over Arora et al. (2023) is not isolated. The reviewers' pool positions (42–66, spread 24) are within the 30-point range, so I weighed the shared evidence rather than the disagreement. Mitigating factors that keep this from a 2: the problem is real, the experiments are honest about Gold vs Inferred, and the issues (claim narrowing, K sweep, a long-context baseline, extraction diagnostics, variance) look fixable with modest compute; this is why the decision is 3 and not lower. No DA ceiling applies; the decision of 3 is below any ceiling. This is a simulation of how a careful panel would likely see this draft, not a prediction of the venue's decision.

---

## Editorial Decision

## Paper: Structured RAG for Answering Aggregative Questions
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Helena Marwick-Doyle; R1 Kofi Adjei-Mensah (Methodology); R2 Lucía Ferrante-Oyelaran (Domain); R3 Sung-min Ahlgren (Perspective); R4 Priyanka Tolliver (Generalist); DA Mateus Brandl-Okafor

## Decision: Borderline Reject (3)
**ICLR labels** (scale status: secondary; as labeled by the script): 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Soundness 2, Presentation 3, Contribution 2.

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40** · official composite **56.9**
**EIC assessment** (internal): weighted rating **3.36** → starting point **3** · weighted composite **56.5** → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: **3**

## Score Summary

#### Reviewer weights (EIC, internal)
| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Methodology) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Perspective) | 3 | 0.70 | 1.00 | 16% |
| R4 (Generalist) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

#### Official scores and EIC assessment
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 56 | 62 | 62 | 48 | 55.6 | 55.1 | 14 |
| Clarity & Presentation | 66 | 68 | 72 | 72 | 68 | 69.2 | 68.9 | 6 |
| Novelty & Originality | 52 | 50 | 60 | 58 | 48 | 53.6 | 53.3 | 12 |
| Significance & Impact | 58 | 58 | 70 | 66 | 56 | 61.6 | 61.1 | 14 |
| Experimental Validation | 44 | 48 | 56 | 56 | 40 | 48.8 | 48.3 | 16 |
| Reproducibility | 50 | 54 | 58 | 56 | 50 | 53.6 | 53.3 | 8 |
| Ethical Compliance | 66 | 66 | 64 | 64 | 62 | 64.4 | 64.5 | 4 |
| **Composite** | 53.5 | 55.8 | 62.5 | 61.4 | 51.2 | **56.9 (before)** | **56.5 (after)** | |
| Pool position (P%) | 45 | 48 | 66 | 66 | 42 | | EIC: 52 | |

No dimension is flagged (all spreads ≤ 20). Script warnings: none.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) — secondary, not official wording |
| Venue-weighted composite | 56.4 (band 3, no shift) |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Structured RAG for Answering Aggregative Questions" to ICLR. Answering questions that aggregate evidence over many documents is a timely problem, and the idea of materializing a table and delegating aggregation to SQL is intuitive and well explained.

**Overall Assessment:** The panel found a clear, readable paper with a real effect when the schema is well specified, but the evidence supports a narrower claim than the abstract makes. The panel leaned toward rejection in its current form, with two reviewers leaning toward acceptance.

**Key Strengths Identified by Reviewers:**
1. A well-motivated problem and an inspectable pipeline; Table 5 shows concretely why top-K retrieval and truncated long-context prompts aggregate incomplete evidence (R1, R3, R4).
2. Honest reporting of Gold and Inferred schemas and a context-free contamination check (Table 2) (R1, R4, DA).
3. Released datasets aimed at an under-served question type (R2, R4).

**Key Concerns Requiring Attention:**
1. The headline numbers use an oracle schema that covers the attributes needed by every evaluation question; the deployable InferredSchema loses on FB-Agg (0.234 vs 0.598/0.593) and is marginal on HOTELS (CONSENSUS-4).
2. The datasets are small and generated from the same schema-and-record representation S-RAG inverts, with no question taxonomy or validation; WORLD CUP is largely known to LLMs (Table 2) (CONSENSUS-4).
3. Baselines and judge: truncated "long-context" baseline, fixed K = 40, no extract-then-query baseline (Arora et al., 2023), GPT-4o judge without human validation, no variance (CONSENSUS-2/3).
4. Method novelty relative to extract-then-query systems is not isolated by ablation; implementation details (record and SQL models, prompts) are missing (CONSENSUS-2/3).

**Decision: Borderline Reject (3).** The reasons to reject (claim carried by an oracle on self-generated data; no clear win for the deployable variant on the external benchmark) outweigh the reasons to accept. What would change the decision: a main-results table built on InferredSchema (or an independently written schema) with confidence intervals, a baseline given equivalent help or an Evaporate-style baseline, a K sweep and a ≥ 1M-token long-context run, validated datasets with a question taxonomy, and a claim set narrowed to what these show. The issues look addressable with modest compute.

Sincerely,
Helena Marwick-Doyle
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Oracle gold schema carries the headline; Inferred does not consistently win | R1, R3, R4, DA (R2 partly) | CONSENSUS-4 |
| Datasets small, schema-generated, unvalidated | R1, R2, R3, R4, DA | CONSENSUS-4/5 |
| No variance, small n | R1, R4, DA | CONSENSUS-3 |
| Missing implementation details, prompts, cost | R1, R3, R4, DA | CONSENSUS-3 |
| 88 vs 83 queries | R1, R4, DA | CONSENSUS-3 (minor) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall recommendation | R3, R4 (4) | R1, R2, DA (3) | Both sides agree on the facts (oracle, small sets). The disagreement is how heavily the oracle weighs; I side with 3 because the weight lands on the abstract's main claim and the one external benchmark, per verified Table 3 |

### Score Spread Discussion
No dimension exceeds the 20-point spread; the largest is Experimental Validation (16: R3/R4 56 vs DA 40), driven by how much weight the generous reviewers give to "adequate to show the effect" versus the small-n/oracle problems. I adopt the lower end for validation (EIC assessment 48.3) because the oracle and n limits are verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Headline rests on Gold; Inferred mixed | Yes (R1-W1, R4-W1, R3-W1) | n/a | Narrow claims, re-run main table |
| DA-M2 | MAJOR | Questions generated from schema records; Gold = generating schema? | Partly (R1-W2) | n/a (question) | Clarification plus independent questions |
| DA-M3 | MAJOR | WORLD CUP baselines below context-free o3 | No | n/a | Masked entities or post-cutoff event |
| DA-M4 | MAJOR | Table 4 generality claim | Yes (R1-W5) | n/a | Soften; CIs |
| DA-M5 | MAJOR | Generator/judge asymmetry, truncated "long context" | Yes (R1-W3/W4) | n/a | Cross-judge, long-context run |
| DA-M6 | MAJOR | C1 unmeasured; Arora et al. not run | Yes (R2-W1) | n/a | Define, measure, add baseline |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld. These are the issues the EIC verified as undermining the main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline claims rest on an oracle schema; Inferred loses on FB-Agg, marginal on HOTELS | R1-W1, R4-W1, R3-W1, DA-M1 | Abstract, §5.2 (i), §6, Table 3 | Make InferredSchema the main result; label Gold as oracle; add a held-out-question or independently written schema; narrow abstract and §6 wording | Low–Medium (rewrite + small re-runs; ≈ 10–30 GPU-free API hours) | Yes |
| R2 | Datasets generated from the schema representation; relation of gold to generating schema unstated; no taxonomy or validation | R1-W2, R2-W2, R4-W2, DA-M2 | §4.1–4.2, Table 1 | State the relation; add question-type statistics; human-validate a sample; add independently written questions | Medium | Partly (statement and statistics yes; new questions need time) |
| R3 | Baselines and protocol: add extract-then-query (Evaporate-style) baseline, K sweep, ≥ 1M-token long-context run, o3-as-S-RAG-generator, cross-family judge with human check | R1-W3/W4, R2-W1, DA-M5/M6 | §5.1, §5.3, App. A, App. E | Run the added baselines on HOTELS (and WORLD CUP) | Medium–High (several × 350-document passes; API spend tens to hundreds of dollars) | Partly |
| R4 | Variance and significance | R1-W5, DA-M4 | Tables 3–4 | ≥ 3 runs; bootstrap CIs; paired tests; soften §6 sentence on general datasets | Medium (≈ 3× current API spend) | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Missing implementation: record and text-to-SQL models, prompts, decoding, SQL-failure handling, long documents, code | R1-W6, R4-W3, DA-m3 | Protocol table; release prompts and code | Low | Yes |
| S2 | Per-stage diagnostics and error taxonomy (extraction accuracy vs gold records, SQL execution accuracy) | R1-W6, R2-W3 | Report on HOTELS and WORLD CUP | Low–Medium | Yes |
| S3 | WORLD CUP contamination (baselines below context-free o3) | DA-M3 | Entity masking or post-cutoff data; report Table 2 beside Table 3 | Medium | Partly |
| S4 | Novelty positioning and ablation of additions (statistics, refinement iterations, hybrid) | R2-W1, DA-M6 | Novelty-delta table; ablations | Low–Medium | Yes |
| S5 | Related work: adjacent LLM-analytics and structured-RAG lines (all `[verify]`): TAG (Biswal et al. 2024), LOTUS (Patel et al. 2024), StructRAG (Li et al., ICLR 2025), DocETL, ZenDB, Palimpzest | R2 | Add and discuss | Low | Yes |
| S6 | Define "aggregative" and measure it per dataset; clarify FB-Agg is mostly single-filing | R2-W2/W4, DA-M6 | Definition and statistics | Low | Yes |
| S7 | Deployment: privacy of hosted-LLM ingestion, ingestion cost, provenance of extracted values | R3-W2 | Cost/latency table; provenance spans; discussion | Low–Medium | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Schema coverage analysis and incremental schema extension | R3-W1 | Report share of questions answerable from the inferred schema |
| N2 | Multi-entity corpora and joins | R3-W3 | Small multi-schema case |
| N3 | Minor: 88 vs 83, "Antropic", "JLM PROMPT", "OAI-Responses" naming, "%" vs absolute points, Table 1 "LLM leak?" definition, FB-Agg definition in text, ∼10-20% wording | R1, R2, R4, DA | Copy-edit |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 2–3 weeks (mostly new runs, API spend only; no model training).
- Priority 2: 7 items, ≈ 1 week.
- Priority 3: 3 items, ≈ 1–2 days.
- **Total estimated revision time**: ≈ 3–4 weeks.

---
*Notes on process: five role passes shared one model context and are not independent agents; the literature check could not run (arXiv HTTP 429), so no claim-level novelty profile or baseline scout exists and all references are `[verify]`; figures were not available.*
