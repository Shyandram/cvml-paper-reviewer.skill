# Review: Structured RAG for Answering Aggregative Questions (ICLR 2026)

*Figures were not available. I judged Figures 1 and 2 from their captions and the text.*

## Summary
The paper studies "aggregative" questions over a corpus: averages, counts and extrema that need evidence from many documents. The authors propose S-RAG.

- **Ingestion.** An LLM induces a flat schema from 12 documents and 10 questions. It then fills one record per document into an SQL table.
- **Inference.** An LLM translates the question into SQL, using the schema and per-column statistics. The SQL result is passed to an answer LLM.
- **Hybrid variant.** SQL selects documents, and ordinary vector RAG runs on them.

The paper also introduces two datasets. HOTELS is fully synthetic, with 350 documents and 193 questions. WORLD CUP uses 22 Wikipedia pages and 83 or 88 generated questions. S-RAG is compared with VectorRAG, FullCorpus (a truncated concatenation) and OpenAI Responses. The comparison covers these two datasets and the 50 aggregative questions of FinanceBench.

With a gold schema, S-RAG is far ahead on HOTELS (0.90 vs 0.33 for VectorRAG). With an inferred schema it is much weaker. On FB-Agg it reaches only 0.23, against 0.60 for VectorRAG and 0.59 for OAI.

## Strengths
- The problem is well motivated. Aggregation over many documents is a real weakness of top-k RAG, and the completeness and bounded-context arguments in §2 are sound.
- Table 5 is a clear qualitative example. The baselines miss tournaments, so their averages are wrong.
- The paper reports a negative result openly. Inferred-schema performance collapses on FinanceBench, and the paper explains why with a concrete failure (unit ambiguity for CapitalExpenditure).
- The datasets are released. HOTELS is built to avoid parametric-knowledge leakage, and Table 2 checks this: o3 with no context scores about 0.05.
- The paper is short and readable. The limitations section is honest about the single-schema assumption.

## Weaknesses
1. **Limited novelty.** The core idea is to turn documents into a table with an LLM and query it with text-to-SQL. This is close to Evaporate (Arora et al., 2023) and to the text-to-table and schema-induction literature.
   - Related work dismisses Arora et al. in one sentence ("not evaluated in the context of RAG performance"), and there is no comparison with Evaporate or similar systems.
   - There are no comparisons with agentic, code-based or map-reduce aggregation, such as an LLM iterating over documents or a tool-using agent.
   - The only strong baselines are top-40 chunk RAG and a truncated full context.
2. **The headline results depend on an oracle schema.**
   - The numbers in the abstract and conclusions (0.90, 0.86, 0.73) use a hand-built "gold" schema that "contains all the relevant attributes to answer all of the queries" in the evaluation set. The schema is therefore designed with the test questions in view.
   - The realistic variant, InferredSchema, scores 0.52 on HOTELS and 0.23 on FB-Agg. On FB-Agg it is below VectorRAG and OAI, and on Answer Recall it is even below the truncated FullCorpus.
   - "Strong results … even compared to top-performing RAG methods" overstates this.
   - The "few hours" of manual schema construction is not measured, and it is not shown that it scales to a user's real query distribution.
3. **The benchmarks favour the method.**
   - HOTELS documents are verbalizations of structured records, and its questions are generated from the same records. Extracting a flat table from such documents is close to inverting the generation process.
   - WORLD CUP has 22 documents of a single entity type, with manually curated gold records, and it is heavily leaked into LLM pretraining (o3 gets 0.71 without context).
   - Both datasets fit the method's assumptions: one schema, simple attributes, no nested or list attributes.
   - FinanceBench is the only independent, realistic benchmark. On it the realistic variant fails, and the gold variant needs a manually built schema. The claim to handle real unstructured corpora is therefore untested.
   - There are only 50 FB-Agg queries, and no confidence intervals, seeds or significance tests are reported anywhere.
4. **The baseline comparison is confounded and the baselines are weak.**
   - S-RAG answers with GPT-4o, while the baselines use o3. The paper presents this as fairness, but it confounds the comparison. A same-generator comparison is needed.
   - VectorRAG is a single configuration: 500-token chunks, top-40, a Qwen2-7B embedder, no BM25 or reranker, and "preliminary experiments" that are not shown. Any fixed K fails by design, as §2 argues, so this baseline is weak against the problem.
   - Baselines that fit the problem are missing: iterative retrieve-and-aggregate agents, a per-document LLM map step followed by a reduce step, and long-context models (HOTELS is about 210k tokens, which fits in 1M-token models).
   - FullCorpus truncates each document and cannot hold the corpora, as the paper admits. It does not support the abstract's claim of outperforming "long-context LLMs".
   - OAI-Responses is a black box, with no stated model, tool configuration or number of retrieval calls.
5. **The evaluation relies on unvalidated LLM judges.**
   - Both metrics use GPT-4o as judge. There is no human agreement study, and the judge prompt has no numeric tolerance (123.64 vs 123.6).
   - Answer Recall is not described in detail.
   - S-RAG outputs a bare number, while baselines output long reasoning chains, so judge behaviour may differ between the two.
   - The WORLD CUP question count is inconsistent: 83 in §4.2, 88 in Tables 1 and 2.
6. **There is no error analysis or ablation.**
   - Failures are attributed to "imperfect text-to-SQL, standardization issues, wrong records" with no quantification, although gold records exist for HOTELS and WORLD CUP.
   - Record extraction accuracy and SQL execution accuracy are not reported, and neither are results by question type (count, average, argmax, filter).
   - There are no ablations on the number of documents and questions used for schema induction (12 and 10), the number of iterations (4), the column statistics given to the SQL generator, or the hybrid mode.
   - Ingestion cost (one LLM call per document) is not discussed or compared with VectorRAG, which matters for the large-corpus motivation.
7. **The hybrid result is weak.** Hybrid-S-RAG scores 0.702 against 0.677 for VectorRAG on 150 questions (Table 4). This 2.5-point gap is within noise, and it uses the gold schema. It does not support "S-RAG can perform well also on general purpose datasets".
8. **The scope is narrow and the dataset construction is thin.**
   - The method needs one schema per corpus and excludes list and nested attributes. There are no joins and no multi-entity corpora. The title suggests broader scope than this.
   - Hybrid mode is described only briefly: how documents are selected, and what happens when SQL returns nothing.
   - The question-generation procedure is under-specified: how question types are chosen, how gold answers are validated, and whether any human check was done.
   - Because questions are generated from the records, many are likely answerable by a single SQL query by construction, and this is not analysed.
9. **Related work is incomplete.** Missing are the table-augmented generation and LLM-over-database-style systems for semantic queries over text (for example LOTUS, Palimpzest, ZenDB). The paper cites MoNaCo, QAMPARI and QUEST but does not evaluate on them, though they would give an independent test of aggregative retrieval.

## Questions
1. How do the InferredSchema results change with more or different documents and questions? Please report variance across seeds and across the samples used for schema induction.
2. How does an agentic or map-reduce baseline perform when given a comparable per-document LLM budget? How does Evaporate perform when substituted for the S-RAG ingestion?
3. What are the record-level extraction accuracy and the text-to-SQL execution accuracy on HOTELS and WORLD CUP, where gold records exist?
4. Did the authors who wrote the gold schemas see the test questions? How long did each schema take, and how were they constructed?
5. What are the results when the same answer generator is used for all systems?
6. What are the ingestion cost and latency compared with VectorRAG? How is a corpus update handled?
7. What is the agreement between the LLM judge and human annotation, especially for numeric answers?
8. How many HOTELS and WORLD CUP questions are answerable by a single SQL query with no further reasoning? How are the 83 and 88 question counts reconciled?

## Ratings
- **Soundness: 2.** The pipeline is sensible, and the qualitative claims about the failure modes of top-k RAG are plausible. The headline numbers use an oracle schema, the evaluation sets are small, there is no variance reporting, the baselines are weak and confounded, and the judge is not validated.
- **Presentation: 3.** The paper is clear and concise. There are some inconsistencies (question counts), and key details (hybrid mode, answer recall, dataset construction) are thin.
- **Contribution: 2.** The problem is relevant, but the method combines known pieces (LLM schema induction plus text-to-SQL). The datasets are small, synthetic and fit the method.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

The paper identifies a real problem and offers a clean, easy-to-adopt solution, with honest reporting of its limits. Its main empirical claims are not yet backed by independent, realistic benchmarks or strong baselines. The oracle-schema gap and the FinanceBench failure of the realistic variant undercut the headline claim. I would raise my score for three things:

- a comparison against Evaporate and agentic baselines under a matched generator;
- ablations and error analysis of schema induction;
- results with an inferred schema on an external aggregative benchmark.
