# Review: "From Charts to Code: A Hierarchical Benchmark for Multimodal Models" (Chart2Code)

Note: figures were not available. Figure-dependent claims (Figs. 2–4, 7–11) are judged from captions and text only.

## Summary
The paper introduces Chart2Code, a chart-to-code benchmark with 2,023 tasks in three levels:
- **L1, chart reproduction.** 863 tasks: direct reproduction, plus reproduction with user-supplied text or figure-format table data.
- **L2, chart editing.** 1,010 tasks.
- **L3, long-table-to-chart generation.** 150 tasks over 39 Excel files.

Reference charts come from arXiv papers, matplotlib and other gallery examples, and ChartMimic. They were filtered by annotators and 5 experts down to 719 L1 references, and ground-truth code was written with LLM assistance.

Evaluation uses four signals:
- execution rate;
- a rule-based "base" comparison of matplotlib Figure objects across eight dimensions;
- an LLM score from GPT-5-mini reading the code;
- an LMM score from GPT-5-mini comparing the rendered chart to the reference.

The paper evaluates about 25 LMMs. Its conclusions are:
- Executability is high for proprietary models on L1 and L2 but drops sharply on L3.
- Rendered-chart fidelity is low everywhere (LMM-score about 0.2–0.4 on L1, about 0.2 on L2, about 0.04 on L3).
- Open-source models lag far behind.

## Strengths
- The task is practically motivated. Editing a chart, and building one from raw tables under a style reference, are realistic scenarios that ChartMimic and Plot2Code only partly cover. The L1 "customized data" settings, L2 editing with 1,010 distinct instructions and L3 long tables add some real coverage.
- The model list is broad: 5 proprietary models, many open-source models, and thinking vs. non-thinking variants.
- The benchmark is hard. Frontier models score low on L2/L3, so there is headroom. The execution-rate cliff on L3, which the paper partly attributes to context limits, is an informative finding.
- Reporting both code-level and image-level scores is a sensible design. The observation that high layout and type scores coexist with low rendered fidelity is interesting, if the metric supports it.
- The data statistics in Table 2 and the annotation and filtering description in the appendix are reasonably detailed.

## Weaknesses

**1. Metric validity is not established, and the headline metric is poorly motivated.**
- The primary "final" metric is the LMM-score, a GPT-5-mini judgment of rendered chart vs. reference. The main text provides no human-agreement study, no judge-robustness check and no alternative judge. The paper points to human-vs-model figures (Figs. 7–11) in the appendix, but these appear to compare scores across models, not judge-vs-human agreement.
- The claim that the base evaluation has "superior evaluation performance" is deferred to the appendix, and the main text does not quantify it.
- Using a small model (GPT-5-mini) as judge, with GPT-5 among the evaluated models, raises self-preference and calibration concerns. The authors admit this only in one limitations sentence and in the "Metric Sensitivity" paragraph, where they list anomalies and then do not resolve them.
- The scale of the LMM-score is not interpretable. An LMM-score of 0.22 does not tell us whether outputs are visually near-identical with small errors or broken. Statements such as "pixel-level fidelity" and "pixel-accurate" are unsupported, because the metric is not pixel-based.
- The central conclusion, that "code-level compliance is high but visual fidelity is the bottleneck", compares two incommensurable scores. Layout and Type scores near 0.95 to 1.0 are likely saturated, trivially satisfiable features. L3 Layout = 1.0 for every model, which suggests the metric is uninformative there. The gap may reflect metric design rather than model behavior.

**2. Level 3 results are computed on a biased subset, and the conclusions are overstated.**
- L3 execution rates are 18–40%, so code-level and figure-level scores are presumably averaged only over executable outputs. This is not stated. If failures count as zero for the LMM-score, then the "collapse" mostly reflects execution failure. If they are excluded, the models are compared on different subsets.
- Open-source models could not process L3 at all, which gives a very limited model comparison (5 proprietary models only).
- The paper says failures stem "primarily from long-context inputs exceeding the maximum input limits". That makes L3 partly a context-window test rather than a chart-generation test. The L3 average data entries (810,329.3) and max (51,391) in Table 2 are internally inconsistent.
- L3 has only 85 unique charts and 150 instructions, so its statistical power is low. With near-zero scores, the differences between models (0.007 vs 0.036 vs 0.061) are meaningless without confidence intervals.

**3. Pervasive numerical inconsistencies between tables, text, appendix and figures, which undermine trust in the results.**
- Table 5 gives identical rows for Claude-Sonnet-4 and GPT-5 on every code-level metric and the LLM-score (0.5676, 0.7963, ..., 0.5125), while the LMM-score differs (0.007 vs 0.0362). This is almost certainly a copy-paste error.
- Table 3 gives identical numbers for InternVL-3-8B and InternVL-3.5-8B on all nine columns.
- Text and tables disagree. For L2, the text cites Gemini ER 90.49, Claude 90.92, Qwen2.5-VL-72B 71.89%, and "MiMo-VL-7B-RL ER 16.54→28.32", while Table 4 gives 90.30, 91.19, 71.49 and 20.59→27.62. The text cites LMM-score values such as Gemini 0.2134 and GPT-5 0.2201 against 0.2459 and 0.2506 in the table. It also cites a "0.4713 figure-level for MiMo-VL-7B-RL (non-thinking)", which does not appear in Table 4 (0.1573).
- Seed-1.6-VL DR LMM-score is 0.8117 in Table 3 but 0.23 in the appendix Table 6, so one is a typo. The text then builds a "metric sensitivity / evaluator calibration" discussion on the main-table number, which is probably just an error.
- Several table entries look anomalous. Molmo-7B-D has an LMM-score of 0.46 on CRD at 4.55% ER. Qwen3-VL-30B's LLM-score on CRD (0.25) is much lower than other models' while its ER is 77.8%. LLM-score is 0.0000 for the Seed models on L3 despite non-zero executability and LMM-score. Level 3 and Level 2 numbers for the same model show unexplained non-monotonic behavior. The text also mentions "InternVL-3.5-38B" and "InternVL-3-38B" being evaluated, but only some of these appear in the tables, and L1 reports no InternVL-3-38B rows although the text discusses "InternVL-3-8B/38B".
- Inconsistent naming ("Direct Mimic" vs "Direct Reproduction"; "Setting 2" used twice in Fig. 1). The "25 models" count does not obviously match the tables (about 22 rows, some duplicated model names with thinking variants).
- The paper reports ER, LLM-score and LMM-score without any variance, seeds or confidence intervals, yet draws fine-grained conclusions from differences in the second decimal place.

**4. Evaluation confounds.**
- ER varies enormously across models (0% to 100%). It is unclear how the code-level, LLM- and LMM-scores treat non-executable code. Models with low ER (e.g., MiMo-VL at 20%) have higher visual and code-level scores than models with higher ER, which suggests scores are averaged over successes only. This makes cross-model comparison invalid.
- It is unclear how much low ER among open-source models reflects capability versus the evaluation setup. Examples: V100 GPUs; a max output of 8,192 tokens (the paper itself notes truncation for InternVL-3.5-38B); temperature 0.1 for thinking models; and 7B models whose context could not fit the inputs. The V100 setting also limits which model sizes and precisions could be run.
- "Thinking helps procedural compliance" rests on two 7B model pairs (MiMo-VL) and one Qwen3-VL pair, with differences of 1–7 points and no variance. This is too thin to support the claim.
- Models are not run in the L1/L2 settings under a common prompt. Prompt sensitivity, dependency versions (matplotlib and others) and sandbox failures are not analyzed. A failure taxonomy (syntax error, missing library, data mismatch, etc.) is not provided, so the benchmark gives little diagnostic insight into *why* models fail.

**5. Novelty and construction concerns.**
- The benchmark combines ChartMimic-style reproduction with ChartEdit-style editing and a long-table setting. The novelty claim "first hierarchical benchmark" mainly rests on bundling these. The "hierarchy" is not validated: is L2 harder than L1 by construction or by metric? The L1 LMM-scores (about 0.2–0.4) and L2 (about 0.2) are close, and different input conditions (reference image and instruction vs data) make the levels not directly comparable. The manual easy/medium/hard analysis uses only 30 samples per subset.
- L2 reuses L1 charts. Of the 1,010 edits, 0 are on unique charts, so L2's diversity is bounded by the 719 L1 charts. The L2 instructions are generated with LLM help and "prompt engineering and Python code injection", then filtered to 1,010 out of 4,700. How the filtering was done and whether edit instructions are ambiguous or underspecified is unclear. Ground-truth code is also LLM-assisted, so GT correctness and bias toward the annotation LLM are unquantified.
- Possible data contamination. Charts are from arXiv, public matplotlib galleries and ChartMimic, whose code is widely available. The paper offers no contamination analysis. 300 charts come directly from ChartMimic, which the intro says models nearly saturate; "difficult" selection is not defined.
- The L1 "figure data" and "raw data" settings are only 108 and 36 items respectively, which is tiny. The paper claims 863 L1 tasks and 2,023 total, and states 899 L1 instructions elsewhere in Table 2. The unit of counting is unclear (charts vs instructions) and the stats are internally confusing (e.g., 863+1,010+150 = 2,023, but instructions are 2,509).
- The inter-rater agreement ">0.8" is reported without the statistic used.
- The L3 requirement of "pixel-accurate" generation from tables with 1,000–10,000+ rows puts most of the burden on data aggregation and long-context handling. It is unclear whether failures come from visualization skill or from table processing, and no ablation separates them (e.g., providing pre-extracted data).

**6. Presentation.** The paper's writing is uneven. Typos ("Projecet lead", "Deatiled", "ChartXiv"), contradictory text ("Chart2Code ... first... "), a text sentence that is cut off ("the unusually high 0.4713 ... merits."), and an abstract that reports "0.57 on code-based evaluation and 0.22 on chart quality for GPT-5 on editing" that does not clearly match the table (the nearest table value is the 0.2506 LMM-score; the 0.57 is the LLM-score 0.5663, which is not "code-based" in the rule-based sense). The Related Work claims GPT-4o scores 83.2 and 93.6 on ChartMimic/ChartEdit, but GPT-4o is not evaluated here, which makes the "benchmarks are saturated" motivation not directly comparable. The first sentence of the Level 3 results ("only a couple of open-source models could even complete inference") is not reflected in the table, which lists no open-source models. There is no model-level qualitative analysis in the main text, and the paper provides few insights beyond "models are far from perfect".

## Questions for the authors
1. What is the agreement (e.g., Spearman/Kendall, pairwise accuracy) between the LMM-score and human judgments on a sample of rendered charts, per level? How does it vary across judges (GPT-5-mini vs GPT-5, Claude, Gemini, open-source)? Is there self-preference bias when GPT-5 is the evaluated model?
2. How are non-executable outputs treated in the LLM-score, LMM-score and code-level metrics? Please report scores on the common subset of executable outputs and with failures counted as zero.
3. Please reconcile Table 3, Table 4, Table 5, the text and Appendix Table 6, including the identical Claude/GPT-5 rows in Table 5, the identical InternVL-3-8B/3.5-8B rows, the Seed-1.6-VL 0.8117 vs 0.23, and the text values (e.g., 71.89, 0.4713) that do not appear in the tables. Which numbers are authoritative?
4. For L3, how many of the failures are caused by input-length overflow vs runtime errors vs wrong data? What would results look like if the long table were pre-processed or retrieval-augmented?
5. What fraction of L2 instructions are unambiguous? Was there a human check that the GT code truly implements the instruction, and that the instruction is feasible?
6. Is there overlap or contamination between the benchmark charts and the training data of the evaluated models (e.g., arXiv, ChartMimic)?
7. What is the variance across runs (sampling with temperature 0.1) and the confidence intervals for scores, particularly on the 150-task L3 and the 30-sample difficulty subsets?
8. How do GPT-4o, o3, Gemini-2.5-Flash and Claude-Opus-4 compare, and does a render-and-fix agentic loop improve things (the paper itself suggests this but does not test it)?
9. How is the 0/1 "Layout" feature of 1.0 on L3 computed, and why is it identical across models?

## Scores
- **Soundness: 2.** Metric validity is not established, scores are likely averaged over different subsets, and there are many numerical inconsistencies.
- **Presentation: 2.** The paper is readable at a high level, but the tables, text and appendix contradict each other, and there are several typos and unresolved notes.
- **Contribution: 3.** The benchmark is useful and challenging and covers realistic editing and table-to-chart settings. The novelty is incremental, and the evaluation reliability limits its value.

## Rating: 4 (marginally below the acceptance threshold)
The benchmark addresses a real gap and the dataset could be useful for the community. But the evaluation, which is the core of a benchmark paper, is not shown to be valid: there is no human validation of the judge, the treatment of failures is unclear, and the reported numbers are riddled with inconsistencies (duplicated rows, text/table mismatches, and an outlier that the authors interpret as a "calibration effect" although it is likely a typo). The L3 conclusions also rest on small and heavily filtered data. I would raise my score if the authors fix and audit the numbers, validate the metrics against human ratings, and analyze the failures.

## Confidence: 4
