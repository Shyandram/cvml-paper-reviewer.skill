# Review: BrowseComp-ZH: Benchmarking Web Browsing Ability of LLMs in Chinese

(Text-only review. Figures were not available, so I judged them from captions and text.)

## Summary
The paper presents BrowseComp-ZH, a Chinese counterpart of BrowseComp. It has 289 reverse-designed, multi-constraint questions with short verifiable answers across 11 topics. The questions were written by 10 annotators with master's or PhD degrees. Construction runs in three steps:
1. Annotators check that the answer is not on the first page of Baidu, Bing or Google, and that GPT-4o and DeepSeek with search do not trivially solve the question.
2. A difficulty filter: other annotators, using search engines only, get 10 minutes per question. This removes 76 of 480.
3. An uniqueness filter: top AI agents answer the questions and annotators check whether their answers are valid alternatives. This removes 115, leaving 289.

The paper evaluates 22 configurations: open and closed LLMs without browsing, and commercial AI search products. Accuracy is graded by GPT-4o for LLMs and by humans for products. Calibration error is also reported. OpenAI DeepResearch scores best at 42.9%. Most others score below 20%, and many below 10%. The paper reports four findings:
- Reasoning models beat non-reasoning ones.
- Multi-round retrieval beats single-round retrieval.
- Enabling search for DeepSeek-R1 lowers accuracy from 23.2% to 7.6%.
- Search increases calibration error.

## Strengths
- It fills a real gap. A hard, natively Chinese browsing benchmark is useful, and the Chinese web differs structurally from the English one (Baidu Baike, Zhihu and other platforms, naming variation).
- The construction protocol is reasonably principled. It combines multi-engine retrievability checks, cross-annotator human solving under a time limit, and an AI-assisted answer-uniqueness check. The numbers of items removed at each stage (480 → 404 → 289) are reported.
- The evaluation covers many systems, including Chinese commercial products such as Doubao, Kimi, Yuanbao and DeepSeek. This makes it a useful snapshot of the field.
- The headline difficulty result is credible. The best system gets 42.9% and many get below 10%, so the benchmark has headroom. Prompts and grading templates are given in the appendix, and the paper states the dataset is released.

## Weaknesses
1. **Selection bias from adversarial filtering.**
   - Questions were revised or dropped based on GPT-4o and DeepSeek with search. The answer-uniqueness filter used OpenAI DeepSearch, Perplexity, Doubao, o1 and Gemini-2.5-Pro, and the paper says they were chosen as the best performers on the 404 candidates.
   - The same systems are then ranked on the final set. Items where these agents found a valid alternative answer were removed. Items where they simply failed were kept. This can change rankings in ways the paper does not quantify, and it can systematically disadvantage the filtering models.
   - The paper should compare filtering-model and non-filtering-model performance, or use held-out models for the filter. Choosing the filter agents by their performance on the same candidate set is also circular.
2. **Answer correctness and uniqueness are not validated beyond the agents' own failures.**
   - Uniqueness is checked only against the alternatives that five AI systems happened to produce. Weak or failing agents will not surface valid alternative answers, so ambiguity probably remains.
   - There is no independent human audit of the ground truth, no inter-annotator agreement, and no estimate of the label-noise rate. When the top accuracy is 20–40%, a 5–10% label error rate matters.
   - The authors concede that uniqueness "cannot be fully guaranteed" and that answers may change over time. No temporal stability check is done.
3. **The difficulty definition is operationally weak.**
   - "Difficult" means not answered in 10 minutes by a human using search engines, or not on the first page for three keyword combinations. This conflates question obscurity with browsing and reasoning skill.
   - There is no human baseline or human solve rate with unlimited time. Evidence URLs are required, but there is no check that questions are solvable by browsing.
   - Several questions (see Fig. 1) look like obscure knowledge recall, such as TV cast trivia. Whether the benchmark measures browsing or long-tail parametric knowledge is unclear. The paper's own results show no-browse reasoning models (o1 29.1%, R1 23.2%, Gemini-2.5-Pro 27.3%) matching or beating most search products. This suggests parametric knowledge contributes substantially, and the paper does not analyse it. A browse vs no-browse comparison for the same underlying model is the cleaner test.
4. **Confounded and non-reproducible comparisons.**
   - AI search products were queried manually through GUIs by human annotators, who also extracted the answers and judged correctness. No dates, versions or number of runs are given. Products change over time and cannot be rerun.
   - The central "search hurts R1" finding (23.2% → 7.6%) compares the API model with no search against the DeepSeek consumer product with search. This is a different system (different prompting, retrieval pipeline and answer-format handling), not a controlled ablation of search on the same model. The explanation that retrieved content overrides more accurate internal knowledge is a hypothesis with no supporting evidence, such as traces or error categorisation.
   - Product accuracy may also be depressed by instruction non-compliance and a different answer protocol. LLMs are graded by GPT-4o and products by humans, so the two groups are scored differently.
   - The categories ("open-source", "closed-source", "search products") mix model strength, search quality and deployment. The claim that multi-round retrieval gives significantly higher accuracy rests on 6 products whose underlying models, search engines and budgets all differ. No statistical test is shown despite the phrase "Statistical analysis shows".
5. **No uncertainty estimates or multiple runs.**
   - With N=289, the 95% CI on a 20% accuracy is about ±4.6 points. Several gaps (e.g., Perplexity 22.6 vs R1 23.2, Yuanbao 12.2 vs Grok 12.9) are within noise, and Doubao Standard vs Deep Search (7.3 points) is marginal.
   - Sampling at T=0.6 means run-to-run variance exists, yet one run is reported. Rankings are presented without CIs or seeds.
6. **Internal inconsistencies and shallow analysis.**
   - Sec. 4.7 says calibration error for DeepSeek-R1 "increases from 59% to 65% when search is enabled". The 65% is the DeepSeek (Deep Think) product, again a different system. The claim that search increases calibration error is not consistent across Table 1: DeepResearch has 9, Grok 39 and Doubao Standard 37, all with search and all lower than most no-search LLMs.
   - The calibration metric uses 5 bins on verbalised confidence, with little discussion. Calibration errors of 70%+ for non-search LLMs are expected from overconfidence on a hard set, but the finding is not analysed.
   - The "reasoning helps" analysis rests on three pairs, and each pair differs in more than reasoning (model generation, training data). "Consistently demonstrate" overstates it.
   - There is no failure analysis, no per-topic breakdown of accuracy (despite 11 topics and Fig. 2), and no analysis of the number of search steps, tool use or cost. The Future Work section acknowledges that failure cases and reasoning/search-strategy analysis have not been done. For an ICLR submission, the insight beyond the dataset is thin.
7. **Claims about Chinese-specific challenges are asserted, not demonstrated.**
   - The introduction claims translation of English benchmarks "does not yield a meaningful evaluation" and that Chinese-specific properties (ellipsis, idioms, inconsistent naming, search-engine indexing) drive difficulty. There is no supporting experiment, such as a comparison with translated BrowseComp, English vs Chinese queries over the same entities, or an error taxonomy tying failures to Chinese-specific properties.
   - The abstract mentions "censorship-related complexities" but the benchmark and analysis never address them.
   - Questions were validated with Google and Bing, which behave differently in mainland China. The effect on difficulty is unclear.
8. **Scale, coverage and annotator effects.**
   - 289 questions from 10 annotators across 11 topics is small, and some topics have only 7–10 items (Academic Papers, Policy & Law). Topic coverage reflects annotator interests, which the paper admits. Per-topic claims would be unreliable.
   - The paper does not discuss contamination risk once the dataset is public, and offers no held-out split or answer protection (BrowseComp-style canary strings, encrypted answers).
   - The models are dated for this submission period (Claude-3.7, Llama 4, GPT-4o, o1). Open browsing-agent systems are not tested.
9. **Related work and positioning.** The comparison with other Chinese search benchmarks (LevelNavi, DynamicQA, CRUD-RAG) is qualitative only. Claims like "lacks rigorous control over task difficulty" are not backed by measurement. The "first benchmark" claim should be scoped carefully.

## Questions
1. How were the five uniqueness-filter agents selected as top performers on the candidate set, and how do their scores on the final 289 compare to models not used in filtering? Can you provide results on a set filtered without them?
2. What is the estimated label-noise rate? Please provide an independent audit of a random sample (including inter-annotator agreement) and a human solve rate with unlimited time and the evidence URLs.
3. For the R1 search/no-search claim, can you run the same model in the same harness with and without a search tool, and provide trace-level evidence for the "retrieval overrides internal knowledge" hypothesis?
4. What is the accuracy of each system with confidence intervals over multiple runs? When were the products queried, and how many annotators were involved?
5. How much of the accuracy comes from parametric knowledge? For example, how do no-browse models perform per topic, and how many questions are solved with no search?
6. Is there any evidence (e.g., a translated-BrowseComp or English-parallel comparison) that Chinese-specific properties cause the difficulty?
7. Why were products evaluated through human GUI interaction rather than APIs or open agent frameworks, which would allow reproducibility? How do you plan to keep answers stable over time?
8. Is GPT-4o grading validated against human judgements on this benchmark (agreement rate)?

## Ratings
- Soundness: 2 / 4
- Presentation: 3 / 4
- Contribution: 2 / 4

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

Rationale: The dataset fills a real need and the construction pipeline is reasonable, so it could be a useful community resource. As a research contribution at ICLR, though, the empirical analysis is shallow. The key conclusions come from confounded comparisons (API vs product, human vs LLM grading, single runs, no CIs). Label quality is not independently validated. The agent-based filtering introduces potential bias against the filtering models. The Chinese-specific motivation is not tested. Stronger validation, controlled ablations and error analysis would move this toward acceptance.
