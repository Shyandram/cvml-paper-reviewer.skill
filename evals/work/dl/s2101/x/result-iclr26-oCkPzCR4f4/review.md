# Academic Paper Review: "From Charts to Code: A Hierarchical Benchmark for Multimodal Models" (Chart2Code)

*Mode: full · Target venue: ICLR · Literature check: strict, cutoff 2025-09-24 · Date: 2026-11-10 · Submission ID: iclr26-oCkPzCR4f4*
*The five reviewer passes were performed one after another in a single shared model context (not independent agents). Figures were not available: figure-dependent claims are judged from captions and text only. This is a simulation of how a careful panel would likely see this draft, not a prediction.*

---

## 📋 Paper Analysis (Phase 0)

| Item | Finding |
|------|---------|
| Title | From Charts to Code: A Hierarchical Benchmark for Multimodal Models |
| Primary Discipline | Machine learning → multimodal LLM evaluation → chart-to-code generation |
| Secondary Discipline(s) | Data visualization, code generation, LLM-as-judge evaluation |
| Paper Type | Benchmark (composite weights: benchmark) |
| Core Technique(s) | Benchmark construction (human-AI annotation), matplotlib `Figure`-object parsing metric, GPT-5-mini as code-level and image-level judge |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (accepted share ≈ 27%) |
| Paper Maturity | Submission-ready draft with unresolved table/text inconsistencies |
| Ethics-Relevant Content | Charts scraped from arXiv papers and Kaggle/annual-report data (redistribution licensing), crowd/student annotators (compensation not stated); no human subjects |

### Claimed Contributions (as stated by the authors, §1, Abstract)
1. **C1**: "the first hierarchical benchmark targeting chart2code generation with progressively more challenging tasks" (Chart reproduction, editing, long-table→chart; 2,023 tasks, 22 chart types).
2. **C2**: "multi-level evaluation protocols that jointly assess code executability and visual fidelity" (execution rate, matplotlib-object "base evaluation", GPT-5-mini LLM-score and LMM-score).
3. **C3**: "an extensive empirical study across 25 mainstream LMMs" yielding "new insights".
4. **C4** (framing claim): the benchmark is "explicitly designed from a user-driven perspective" and "reflects real-world usage".

### Paper memory (factual record shared with all reviewers)
- **Data:** L1 = 863 tasks (719 unique charts; DR 719 + CRD 36 + CFD 108, §3.2.3, Table 2), L2 = 1,010 edits reusing L1 charts (§3.3), L3 = 150 instructions on 85 charts from 39 Excel files (§3.3). Chart sources: ≈5,000 arXiv charts (Jan 2024–Jul 2025), 1,000 library-tutorial charts, 300 from ChartMimic (§3.2.1). Filtering: 10 undergraduates → 5 experts, 1–5 scores on 3 dimensions, "inter-rater agreement (> 0.8)" (App. C.1).
- **Annotation:** GT code written "with the assistance of the LMM" (L1); L2 edits via "prompt engineering and Python code injection", 4,700+ scripts filtered to 1,010 (§3.2.3).
- **Metrics:** execution rate (Eq. 1); eight-dimension matplotlib `Figure`-object similarity ("base evaluation", App. E.2, Eq. 2–45); LLM-Score = GPT-5-mini static analysis of code "without execution" (App. E.3, K.2); LMM-Score = GPT-5-mini image comparison, "assume a perfect score of 100, and then to deduct points" (App. E.4).
- **Setup:** 25 table rows (22 distinct checkpoints + 3 thinking-mode rows) in Table 3; temperature "fixed at 0.1 across all models" (§4.1) vs Table 9 (Temp. column shows 0 for proprietary models); max output 8,192 (L1/2) and 32,768 (L3) tokens; single run, no seeds or variance stated; V100 GPUs.
- **Headline numbers:** GPT-5 "0.57 ... code-based" and "0.22 ... chart-quality" on editing (Abstract; Table 4 gives 0.5663 and 0.2506); L3 ER 29–40% and LMM ≤ 0.07 (Table 5).
- **Appendix:** extra tables 6–8 (L1 detail), human-vs-model figures 7–11 (figures not visible), metric derivations (E.2), run configs (Table 9), licences (Table 11), prompts (K).
- **Unreadable / unavailable:** all figures (Fig. 1–11), garbled Fig. 2 text, code/data link ("[Our code and data are available on Chart2Code]" gives no URL in the blinded text), long appendix code listings skimmed for protocol statements only.

### Integrity scan (Hard Rule 9)
`integrity_scan.py` was not run (this run was restricted to file reads and the aggregation script). Instead the full text was searched for reviewer-directed phrases (e.g., "ignore previous", "give a positive review", "LLM reviewers", "strong accept"). **No reviewer-directed or hidden instruction text was found**; all hits for "LLM" are ordinary content. The reviewers read the same text.

### Literature check (Phase 1.5): strict mode, cutoff 2025-09-24
7 counted queries (5 claim, 1 baseline, 1 expansion), 1 refused (5 concept words, not counted); 50 unique kept results; `similarity`: no high-overlap (max cosine 0.224 with ChartEdit) and no text overlap flags. Closest prior works: ChartEdit, ChartMimic, ChartReformer. Open gaps: no prior work kept from 2021; claim C3 (empirical study) got no query (a benchmark-results claim, not a novelty claim). arXiv-only search, so "no prior work found" is a limit of the search, not evidence of novelty.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Solheim-Okafor, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / multimodal foundation-model evaluation, benchmark design
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Calibrated to what ICLR actually accepts; wants benchmark validity shown, not asserted

### Reviewer 1 (Methodology): Dr. Mateus Okonkwo-Hartmann, industrial research lab (Western Europe)
- **Seniority / Expertise**: Senior industry scientist / evaluation protocols for code-generating LMMs, LLM-as-judge validity
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table and cross-checks the appendix against the main text

### Reviewer 2 (Domain): Dr. Léa Marchetti-Nwosu, vision-language group, mid-sized public university (Southern Europe)
- **Seniority / Expertise**: Mid-career / chart understanding and chart-to-code benchmarks, document intelligence
- **Review Focus**: Literature, positioning, domain contribution
- **Style**: Insists on a delta table against the nearest benchmarks

### Reviewer 3 (Perspective): Dr. Priyanka Delacroix-Ibarra, data-visualization and HCI lab, public research university (North America)
- **Seniority / Expertise**: Associate professor / visualization authoring tools, end-user programming
- **Review Focus**: Cross-disciplinary links, real-user relevance, deployment, broader impact
- **Style**: Constructive; asks who the actual user is

### Reviewer 4 (Generalist): Dr. Haruto Vanterpool, vision lab, large public research university (East Asia)
- **Seniority / Expertise**: Mid-career / multimodal learning (not chart-specific)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Selin Arvidsson-Park, research institute (Nordic region)
- **Seniority / Expertise**: Senior researcher / measurement validity, causal evaluation of ML systems
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks "does the metric measure what is claimed?"

*Personas are fictional. Assumptions: target venue ICLR as stated; paper type benchmark.*

---

# Phase 1: Independent Reviews

# Peer Review Report

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Reviewer: Dr. Mateus Okonkwo-Hartmann, Methodology (industrial research lab, Western Europe; fictional persona)
## Expertise: evaluation protocols for code-generating LMMs; LLM-as-judge validity; benchmark statistics
## Date: 2026-11-10

### Protocol sweep (Step 0)
Searched for split/selection/tuning statements. A benchmark paper does not train or tune on its own test set; the relevant "selection" statements are the **task filtering** ones: "we reduce the data to 3,000 charts" (§3.2.2), "4,700 edited and modified scripts, which were further filtered through the data selection process, ultimately yielding 1,010 high-quality Level 2 data entries" (§3.2.3), "Our code and data are available on Chart2Code" (Abstract). The L2 filtering criterion is **not stated** after search, nor is whether filtering used model outputs. No model tuning on the benchmark is reported. Prompts are fixed in App. K.1; decoding is "temperature ... fixed at 0.1" (§4.1). Seeds, repeated runs and variance: **not stated after search**. Dataset licence/redistribution terms: **not stated after search** (Table 11 gives model licences only).

## Summary
Chart2Code is a benchmark of 2,023 matplotlib-code generation tasks in three levels: reproducing a chart from an image (optionally with data supplied as text or as a figure), editing a chart by instruction, and building a chart from long tables. Models are scored with an execution rate, a rule-based comparison of matplotlib `Figure` objects, a GPT-5-mini "LLM-Score" on the code and a GPT-5-mini "LMM-Score" on rendered images. The paper evaluates 25 model rows and concludes that models execute code but fall far short of visual fidelity, especially on Level 3.

## Strengths
### S1: Useful, well-motivated task structure
Level 1 settings with supplied data (CRD/CFD, §3.1) and Level 3 long-table inputs (Table 2: up to 10,960 lines per file) test data handling, not only visual copying, which earlier chart-to-code benchmarks in Table 1 do not.
### S2: Breadth of evaluated models and reporting of component scores
Tables 3–5 report execution rate and per-dimension code-level scores for proprietary and open-weight models, plus thinking variants for three models, so readers can separate executability from fidelity.
### S3: Transparent limitations on the judge and appendix material
§5 admits that LLM judges "may introduce inaccuracies or biases", and App. F/H/K disclose configs, licences and prompts, which is good practice for reproducibility.
### S4: Honest flagging of anomalies
§4.2.2 "Metric Sensitivity" itself recognises that some scores look inconsistent and calls for audits.

## Weaknesses
### W1: The numbers in the paper cannot be trusted as printed: the main text, main tables and appendix tables disagree (E1/E6)
The text analyses of Level 2 quote values absent from Table 4 (e.g., Gemini ER "90.49" vs 90.30; InternVL-3-38B ER "61.51" vs 67.43; LMM-Score for Gemini/Claude/GPT-5 "0.2134/0.1844/0.2201" vs 0.2459/0.2147/0.2506; the "unusually high figure-level 0.4713" for MiMo-VL-7B-RL vs 0.1573 in Table 4). Table 3 contradicts Tables 6–8: InternVL-3-8B in Table 3 repeats the InternVL-3.5-8B row exactly (66.34 / 0.4371 / 0.1389) whereas Table 6 gives 21.97 / 0.3802 / 0.0949; InternVL-2.5-38B has "0" ER on CRD and CFD in Table 3 but 88.89 and 43.52 in Tables 7–8; Seed-1.6-VL's DM LMM-Score is 0.8117 in Table 3 and 0.23 in Table 6; Table 5 gives Claude-Sonnet-4 and GPT-5 identical code-level values in every column. The "outlier" analysed in §4.2.1/4.2.2 therefore appears to be a typo. Because model rankings and the abstract's headline are drawn from these tables, a reader cannot tell which numbers are right.
- **Suggested Fix**: Regenerate every table from a single results file by script; add a consistency check; state which version of the numbers the prose describes. Cost: low (< 1 day), no new inference needed.

### W2: The evaluation metrics are not validated, and the key claim "superior evaluation performance" is asserted, not shown (C2)
§3.4 claims the base evaluation has "superior evaluation performance (see Appendix E.2)", but App. E.2 lists qualitative advantages ("More Efficient/General/Versatile/Precise") with no experiment against ChartMimic's metrics or human judgments. LMM-Score is "most aligned with human intuition" (§3.4) yet no agreement statistic (Pearson/Spearman/κ, number of items, rater protocol) is given in text; App. D.1 mentions Figs. 7–11 comparing "human scores versus model scores", which I cannot see. The judge GPT-5-mini is also used for subjects (GPT-5 family), with no check for self-preference. The absolute scale is arbitrary ("Start at 100, deduct points", App. K.2; App. E.4): without a human or ground-truth-code ceiling, "0.22" cannot be read as "low".
- **Suggested Fix**: Report judge–human correlation on a stratified sample (e.g., 300 items × 3 raters ≈ 2 annotator-days), a second judge from another family, and a ceiling (GT code re-rendered; a human re-implementation).

### W3: The denominator of the scores is not stated, and the table pattern suggests conditional averaging
Molmo-7B-D has CRD ER 4.55% yet the highest CRD LMM-Score of any model (0.4600 vs ≤0.27 for proprietary models, Table 3); in Table 4 models with ER 0.99–2.57% have Grid/Layout 0.56–0.82. If code-level and image-level scores are averaged only over executed outputs, models are compared on different, self-selected subsets. §3.4 does not say whether failures count as zero.
- **Suggested Fix**: Report both "all tasks (failures = 0)" and "executed only", plus the paired-subset score on tasks every model executed.

### W4: Level 3 conclusions are confounded by context/token limits and cover only 5 models
§4.2.1 attributes the <50% ER "primarily" to "long-context inputs exceeding the maximum input limits" and says "only a couple of open-source models could even complete inference", yet Table 5 lists only five proprietary models. LMM-Scores of 0.007–0.061 are at floor and cannot rank models; Seed rows have LLM-Score = 0.0000 with non-zero code-level sub-scores (Table 5), which the paper itself calls possible "edge-case artifacts". The conclusion that fidelity is "the main bottleneck" is therefore not separated from input truncation.
- **Suggested Fix**: Report input-token length vs. success, evaluate with chunked/retrieval-style table access, and drop or flag floor-level ranks.

### W5: Single run, tiny sub-settings, no uncertainty
CRD has 36 tasks (ER values are multiples of 1/36, e.g., 97.2 = 35/36) and CFD has 108 (87.04 = 94/108); the difficulty analysis uses 30 samples per bucket (§4.3). One gap of 2.8 points on CRD is one task. Decoding is sampled (Table 9 "Do Sample: True") at T = 0.1 with a single run; no bootstrap CIs.
- **Suggested Fix**: Paired bootstrap CIs over tasks; 3 sampling seeds for the top-10 models (≈ 30–60 GPU/API-hours).

### W6: Overstated analytic claims (E5)
(a) "Thinking Helps Procedural Compliance" (§4.2.2) is drawn from Level 2 for MiMo only; in Table 3, thinking *lowers* Qwen3-VL-30B ER (DR 64.67→45.06, CFD 70.37→39.81, a −30.6-point drop, derived). (b) "reproducing existing charts (CFD) is the hardest subtask in Level1" holds for ER, but by LMM-Score GPT-5's CFD (0.2382) is above its CRD (0.2238), and Claude's CFD/CRD differ by under 0.01 (0.2273 vs 0.2360), on CRD n = 36. (c) "clear correlation with manually annotated difficulty levels across all benchmark stages" (§4.3): in the Fig. 3 text extraction, two Level-1 rows read 0.383/0.407/0.318 and 0.221/0.287/0.206 (Easy/Medium/Hard), i.e., Medium ≥ Easy, and all Level-3 values are ≈0 (figure itself not visible).
- **Suggested Fix**: Narrow the wording or add the missing conditions/figures.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 2 | "Total instructions" = 2,509 | Rows give 899 + 1,010 + 150 = 2,059 | Recomputed | High | MAJOR | Correct total |
| ERR-2 | E1/E6 | Table 2 | "Average data entries" 810,329.3 vs "Maximum data entries" 51,391 | Average exceeds maximum | Cross-referenced (same table) | High | MINOR | Fix units |
| ERR-3 | E1 | §4.2.2 vs Table 4 | "unusually high figure-level 0.4713" | Table 4 gives 0.1573 for MiMo-VL-7B-RL; text-vs-table mismatch for ≥ 9 values | Cross-referenced | High | MAJOR | Regenerate text |
| ERR-4 | E6 | Table 3 vs Table 6 | "shows an unusually high DM LMM-Score" | Table 6 gives 0.23 for Seed-1.6-VL (Table 3: 0.8117) | Cross-referenced | High | MAJOR | Fix value; drop "outlier" discussion |
| ERR-5 | E6 | Table 3 vs Tables 6–8 | InternVL-3-8B row 66.34 / 0.4371 / 0.1389 | Identical to InternVL-3.5-8B; Table 6 gives 21.97 / 0.3802 / 0.0949; InternVL-2.5-38B CRD/CFD "0" vs 88.89/43.52 | Cross-referenced | High | MAJOR | Regenerate |
| ERR-6 | E1 | Table 5 | Claude-Sonnet-4 and GPT-5 rows | Identical ER 38.00 and nine identical sub-scores, different LMM-Score | Cross-referenced (rows) | Medium | MAJOR | Verify against raw outputs |
| ERR-7 | E6 | §4.1 | "we selected 12 representative vision-language models" | Lists ≈ 18 models, "25" total; Table 3 has 22 distinct checkpoints + 3 thinking rows | Counted | High | MINOR | State the count |
| ERR-8 | E5 | §4.2.2 | "Thinking Helps Procedural Compliance" | Contradicted by Qwen3-VL-30B in Table 3 | Recomputed | High | MAJOR | Narrow claim |

## Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | first hierarchical chart2code benchmark | Abstract, §1 | Table 1, §3 | Partially (hierarchy is defined by task type, not shown to be a difficulty ordering, §4.3) |
| C2 | multi-level protocols, "superior evaluation performance" | §3.4, App. E | none beyond assertion | Unsupported |
| C3 | extensive study of 25 LMMs | §4 | Tables 3–5 | Partially (22 distinct; L3 only 5; numbers inconsistent) |
| C4 | "user-driven", "reflects real-world usage" | Abstract, §1 | App. B examples only | Unsupported |
| C5 | GPT-5 0.57 code / 0.22 chart on editing | Abstract | Table 4 | Partially (0.5663 ✓; LMM 0.2506 ✗ vs 0.22) |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Printed tables conflict; metric unvalidated (Technical Rigor 40, Exp. Validation 38 → mean 39) |
| Clarity | 2 | Text analyses describe numbers not in the tables |
| Significance | 2 | Useful task, but conclusions depend on an unvalidated judge |
| Originality | 2 | Level 3 and CRD/CFD settings are new in form; L1/L2 close to prior work |

## Dimension Scores (0–100)
**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: printed results are mutually inconsistent in several places, and the evaluation metric is unvalidated while it carries every conclusion; typical accepted benchmarks validate the metric against humans.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | Unvalidated judge, unstated denominator, table conflicts |
| Clarity & Presentation | 45 | Developing | Text and tables describe different numbers; typos |
| Novelty & Originality | 45 | Developing | Incremental over ChartMimic/ChartEdit apart from L3 |
| Significance & Impact | 55 | Competent | Practical task; limited by metric trust |
| Experimental Validation | 38 | Developing | Single run, floor effects at L3, 5-model L3 |
| Reproducibility | 48 | Developing | Prompts/configs given, but no code link visible, L2 filter unstated |
| Ethical Compliance | 55 | Competent | Limitations honest; data licensing/annotator pay absent |

## Questions for Authors
1. Are LLM-Score/LMM-Score averaged over all tasks (failures = 0) or only executed outputs? A "all tasks" re-table would raise my score if rankings hold.
2. What is the judge–human agreement (n, raters, statistic) behind Figs. 7–11, and what is the score of the GT code itself under the LMM-Score?
3. Which numbers are correct where text, Tables 3–5 and Tables 6–8 disagree?
4. What criterion filtered 4,700 → 1,010 L2 scripts, and was any model output used?
5. How was T = 0.1 set for GPT-5 and other reasoning APIs (Table 9 shows 0 for proprietary models)?

## Limitations Assessment
**Partially.** The judge limitation is acknowledged (§5); missing: data licences, contamination, single-run variance, truncation effects at L3.

## Ethics Review Flag
**No**: licensing of scraped arXiv figures and Kaggle data should be stated, but this is a documentation gap.

## Overall Score
**2**: A useful benchmark idea whose headline evidence is currently unreliable (conflicting tables) and whose metric is unvalidated; fixable but needs new validation experiments.
## Confidence
**4**: Tables recomputed and cross-checked; figures not visible.

---

# Peer Review Report

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Reviewer: Dr. Léa Marchetti-Nwosu, Domain (vision-language group, public university, Southern Europe; fictional persona)
## Expertise: chart understanding and chart-to-code benchmarks; document intelligence
## Date: 2026-11-10

## Summary
The paper proposes a three-level chart-to-code benchmark and compares it with ChartMimic, ChartEdit, Plot2Code and a related chart paper (Table 1). Its positioning is that existing benchmarks "suggest that the problem is close to being solved", while realistic tasks (edit a chart, plot from long raw tables) remain hard. It evaluates 25 model rows and reports low image-level fidelity.

## Strengths
### S1: Level 3 targets a real gap
Turning long, unprocessed tables (up to 10,960 lines, Table 2) into a chart that follows a reference style is not covered by the benchmarks in Table 1.
### S2: Reasonable scale and diversity
2,023 tasks over 22/19/12 chart families (§3.3), chart sources spanning arXiv 2024–2025, library tutorials and ChartMimic (§3.2.1).
### S3: Data-in-the-loop Level 1 settings
CRD/CFD (§3.1) require extracting or using data, closer to authoring than pure reproduction.
### S4: Related work correctly describes ChartEdit and ChartMimic at the level of their abstracts
§2 matches the kept abstracts (code-based chart editing; chart-to-code from images with instructions).

## Weaknesses
### W1: The "first hierarchical" claim and Table 1 omit closely related benchmarks and tasks (literature-check addendum)
Strict-mode search (cutoff 2025-09-24) found, with abstracts read: **ChartEdit** (ACL 2025 Findings; 1,405 edit instructions on 233 real charts, code- and chart-level evaluation) is the nearest prior work for Level 2 and is cited, but Chart2Code does not discuss how its 1,010 edits differ in kind. **Text2Chart31** (EMNLP 2024; 11.1K description–code–data-table–plot tuples, a "hierarchical pipeline" for chart generation) and **Doc2Chart** (EMNLP 2025 Main; chart generation from long documents given a user intent, evaluated with a data-accuracy metric) are prior, peer-reviewed and uncited; Doc2Chart overlaps with the "long, information-dense input → faithful chart" idea of Level 3, though it takes documents with an intent rather than tables plus a style reference. One claim (L3) is thus partly covered, not "known". Worth discussing only (recent or concurrent, never grounds for a weakness): ChartM³ (multi-level chart editing with multimodal instructions, 1,000 samples, four editing levels; recent preprint), ChartMaster and ChartGen (chart-to-code with real charts / synthetic generation; concurrent / recent preprints). The word "first" should be qualified to "first with this combination of reproduction, editing and long-table tasks".
- **Suggested Fix**: Add Doc2Chart/Text2Chart31 to Table 1 and related work; state exactly what is new in L3 versus them.

### W2: Level 1 "Customized Data" is said to be "not included in previous studies" without a delta
§3.1 says the second L1 setting is "closely aligned with real-world chart creation needs and not included in previous studies (Yang et al., 2025a; Wu et al., 2025; Zhang et al., 2024)". The kept ChartMimic abstract (4,800 triplets with instructions) does not settle this; from my knowledge ChartMimic has a customized-data task [verify]. If so, the novelty is only the CFD/figure-data variant (108 tasks).
- **Suggested Fix**: Add a task-by-task delta table against ChartMimic (inputs, outputs, counts).

### W3: "Existing benchmarks are nearly solved" compares unlike metrics
§2 cites GPT-4o "83.2" on ChartMimic and "93.6" on ChartEdit to motivate difficulty, but Chart2Code uses a different, harsher deduction-based GPT-5-mini score (App. E.4) and does not run GPT-4o. Lower numbers may reflect the metric rather than harder tasks. 
- **Suggested Fix**: Run 3–4 shared models on ChartMimic/ChartEdit subsets with the Chart2Code metric (≈ 1 day API cost).

### W4: The base-evaluation novelty (parsing `Figure` objects) is presented against ChartMimic without citing or comparing to its metrics empirically
App. E.2 argues efficiency, generality, versatility and precision by assertion ("up to twelve executions" per sample for ChartMimic). No timing or agreement experiment is given. 
- **Suggested Fix**: Report runtime and correlation with ChartMimic's metrics on the 300 reused ChartMimic charts.

### W5: Citation hygiene (E7)
§2 names "ChartXiv (Wang et al., 2024b)" whereas the bibliography entry is CharXiv; Table 1 lists CharXiv, a QA benchmark (its own Output column says "NL"), among "chart-to-code benchmarks"; "AcademiaChart" in Table 1 is not the title of the cited Zhang et al. (2024) paper ("Is GPT-4V(ision) all you need for automating academic data visualization?").
- **Suggested Fix**: Correct names; separate QA from code benchmarks in Table 1.

## Novelty assessment (claim-level, from abstracts)
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 first hierarchical benchmark | problem/resource | medium | ChartEdit (3; https://arxiv.org/abs/2505.11935v2; prior peer-reviewed; cited), ChartMimic (3; https://arxiv.org/abs/2406.09961v2; prior peer-reviewed; cited), Doc2Chart (2–3; https://arxiv.org/abs/2507.14819v2; prior peer-reviewed; **uncited**) | Each level partly exists; the bundle plus L3 is new |
| C2 multi-level evaluation | method | incremental | ChartMimic (4; multi-level code and chart metrics) , Plot2Code (3; GPT judge over images) | Same two-level code/chart design; new element is `Figure`-object matching |
| C3 empirical study of 25 LMMs | result | not a novelty claim | n/a | judged under Experimental Validation |

## Novelty delta against closest prior works
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| Level 2 editing | ChartEdit (Zhao et al., 2025) | Chart editing via code, 1,405 instructions, 233 charts, code- and chart-level evaluation | 1,010 edits on 719 charts, types incl. multi-subplot | Cited, weakly differentiated |
| Level 1 reproduction | ChartMimic (Yang et al., 2025) / Plot2Code (Wu et al., 2025) | Chart-to-code from image + instruction; GPT image judge | CFD variant, harder subset | Cited |
| Level 3 | Doc2Chart (Jain et al., 2025), Text2Chart31 (Zadeh et al., 2024) | Chart code from long documents / tables | Long Excel tables with style reference | **Not cited** |

**Baseline scout.** The kept abstracts of ChartMimic and ChartEdit give no numbers on a setting comparable to this paper's, so no under-reported-baseline check was possible. The paper's cited GPT-4o numbers (83.2, 93.6) are not verifiable from abstracts.

**Field snapshot.** Three years ago chart work was mainly chart QA and captioning (ChartQA-style); in 2024 chart-to-code emerged (Plot2Code, ChartMimic), and by mid-2025 editing (ChartEdit and a multimodal-editing benchmark), synthetic-data training (ChartGen) and RL for chart-to-code (ChartMaster, others) were all active. Frontier models already reach high execution rates on reproduction; the open problems stated by recent work are visual consistency, data fidelity and robust editing. A significant benchmark contribution at this point is one that (i) opens a capability not covered (long-table, intent-driven charting), and (ii) comes with a validated automatic metric and a clear headroom; a few more chart types or tasks with an unvalidated judge is incremental. This calibrates my Novelty and Significance scores below.

## Missing References
*Literature-check results (strict mode, arXiv only).*
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | none (no prior work found with the same task and mechanism) | n/a |
| Important | Jain, Ramu, Garimella, Saxena, et al. "Doc2Chart: Intent-Driven Zero-Shot Chart Generation from Documents", EMNLP 2025 Main, https://arxiv.org/abs/2507.14819v2 | Prior work on chart generation from long inputs; relates to Level 3 |
| Important | Pesaran Zadeh, Kim, Kim, Kim. "Text2Chart31: Instruction Tuning for Chart Generation with Automatic Feedback", EMNLP 2024, https://arxiv.org/abs/2410.04064 | Data table + instruction → chart code with a hierarchical pipeline |
| Important | Zheng, Chiang, Sheng, et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks, https://arxiv.org/abs/2306.05685 | Position/self-preference biases of LLM judges; the paper's metrics depend on one |
| Helpful | Yan, Bhosale, Lal, Adhikari, Doermann. "ChartReformer: Natural Language-Driven Chart Image Editing", ICDAR 2024, https://arxiv.org/abs/2403.00209 | Earlier chart-editing line for Level 2 |
| Worth discussing (recent / concurrent, not required) | Yang, Zhang, Yue, Chen, et al. "ChartM³: Benchmarking Chart Editing with Multimodal Instructions" (arXiv 2507.21167); Tan, Cao, Xue, Zhan, et al. "ChartMaster" (arXiv 2508.17608); Kondic, Li, Joshi, et al. "ChartGen" (arXiv 2507.19492) | Multi-level chart editing and chart-to-code with real/synthetic charts; discuss, do not require |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Metric unvalidated; positioning incomplete |
| Clarity | 2 | Related-work naming slips, table/text mismatches |
| Significance | 2 | Useful, but headroom claim depends on judge |
| Originality | 2 | Bundle new, parts incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: moderate novelty (L3 and CFD are new, L1/L2 sit next to ChartMimic/ChartEdit) with positioning gaps and no validated metric; typical accepted benchmarks add a validated evaluation or a clearly new capability.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Metric design plausible but unvalidated |
| Clarity & Presentation | 55 | Competent | Understandable; naming slips |
| Novelty & Originality | 52 | Developing | Medium at claim level (C1), incremental (C2) |
| Significance & Impact | 58 | Competent | Practical task; moderate |
| Experimental Validation | 48 | Developing | Broad model coverage, weak controls |
| Reproducibility | 55 | Competent | Prompts, configs, licences listed |
| Ethical Compliance | 55 | Competent | Basic |

## Questions for Authors
1. What exactly does L3 add over data-table-to-chart work such as Text2Chart31 and Doc2Chart? A clear delta would raise my Originality score.
2. Is the CRD setting really absent from ChartMimic? [verify]
3. How do models rank under your metric on ChartMimic/ChartEdit subsets?

## Limitations Assessment
**Partially.** Language and judge limits are noted; novelty boundaries and contamination are not.
## Ethics Review Flag
**No**
## Overall Score
**3**: A reasonable benchmark with a new long-table level, but positioning is incomplete and the evidence that it measures chart faithfulness is thin.
## Confidence
**4**: Closest-work abstracts read; ChartMimic details not fully verifiable from its abstract.

---

# Peer Review Report

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Reviewer: Dr. Priyanka Delacroix-Ibarra, Perspective (data-visualization/HCI lab, public university, North America; fictional persona)
## Expertise: visualization authoring tools, end-user programming, human evaluation of visual similarity
## Date: 2026-11-10

## Summary
The paper builds a benchmark intended to mirror how people actually create and revise charts with code assistants, and shows that frontier and open models rarely produce faithful charts when asked to edit or to start from long tables. I read it as a contribution to data-visualization authoring evaluation as much as to LMM benchmarking.

## Strengths
### S1: Right instinct about authoring workflows
Editing existing charts and plotting from messy spreadsheets (Level 2/3; §3.1) mirror real analyst practice better than copy-the-picture tasks.
### S2: Appendix B shows concrete failure cases
The user-centric case studies (App. B) give readers qualitative examples of failure.
### S3: Mixed code- and image-level evaluation is the right idea
Separating "does it run", "is the code structurally right" and "does the picture match" (§3.4) maps to what visualization practitioners care about.

## Weaknesses
### W1: "User-driven" and "real-world usage" are claims without user evidence
The abstract says the benchmark is "explicitly designed from a user-driven perspective", but instructions are written by annotators and LLM-assisted pipelines (§3.2.3; "prompt engineering and Python code injection"), and edit operations were chosen when annotators "first categorize and summarize chart editing operations" themselves. No user survey, query log or practitioner study supports task frequencies. 
- **Suggested Fix**: Ground the operation taxonomy in a small practitioner survey or public usage logs, or soften the framing to "inspired by".

### W2: Pixel-fidelity as the target ignores what users need
Users usually judge charts by the correctness of data encoding and legibility, not exact style match. LMM-Score deducts for every visual difference (App. E.4), so style differences with a correct data mapping are punished as much as wrong data. §4.2.2 interprets low LMM-Scores as "pixel-level" failure without this distinction, and notes (a) a "style carry-over" weakness for CFD with no experiment. 
- **Suggested Fix**: Report a data-fidelity-only score (extract plotted values from the rendered figure) next to style fidelity; report weights.

### W3: Domain-shift and contamination are not discussed
Charts come from public arXiv papers (Jan 2024–Jul 2025), public library tutorials and ChartMimic (§3.2.1): all likely in training corpora of recent models, and the tutorial "golden standard" examples are widely reproduced. No analysis of memorisation (e.g., performance vs publication date, Fig. 5) is given.
- **Suggested Fix**: Report results by chart-source and by date split; note which models' cutoffs precede the charts.

### W4: Licensing, consent and annotator conditions
Charts scraped from papers and Kaggle/annual-report data are redistributed, yet only model licences are given (Table 11); dataset licence/terms and annotator compensation (10 undergraduates, 5 experts) are not stated. 
- **Suggested Fix**: Add a datasheet: licence per source, redistribution basis, annotator compensation.

### W5: Cross-disciplinary assumption: executable matplotlib code is the unit of "chart2code"
Practitioners also use Plotly/Vega/Excel; §3.2.1 lists Plotly and Matlab examples as chart sources while the base evaluation only handles matplotlib `Figure` objects (App. E.2). It is unclear how those references were converted. 
- **Suggested Fix**: State the conversion; discuss Vega-Lite/Plotly generalisation.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Judge unvalidated, single run |
| Clarity | 2 | Understandable, with inconsistencies |
| Significance | 3 | Realistic use case, practical |
| Originality | 2 | Task variants more than new problem |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically relevant task and a useful Level 3, offset by unsupported "user-driven" framing and the absence of a validated metric.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Reasonable design, unvalidated |
| Clarity & Presentation | 56 | Competent | Readable |
| Novelty & Originality | 55 | Competent | New workflow framing |
| Significance & Impact | 62 | Competent | Useful for tool builders |
| Experimental Validation | 50 | Developing | Broad but uncontrolled |
| Reproducibility | 58 | Competent | Configs, prompts |
| Ethical Compliance | 52 | Developing | Data licensing and annotator conditions missing |

## Questions for Authors
1. What evidence supports the frequency of edit types in Level 2?
2. Can you provide a data-only fidelity score?
3. Do results change on charts published after each model's training cutoff?

## Limitations Assessment
**Partially.** English-only and LLM-judge limits stated; contamination, licensing and matplotlib-only scope are not.
## Ethics Review Flag
**No**: documentation gap on data licensing, not a harm concern.
## Overall Score
**3**: A relevant and practical benchmark whose claims of realism and its fidelity metric need support before it can serve as a reliable yardstick.
## Confidence
**3**: Outside my core area on LMM evaluation statistics; figures not visible.

---

# Peer Review Report

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Reviewer: Dr. Haruto Vanterpool, Generalist (vision lab, public university, East Asia; fictional persona)
## Expertise: multimodal learning, vision-language models
## Date: 2026-11-10

### Contribution in one paragraph
Chart2Code is a three-level benchmark (reproduce, edit, long-table-to-chart) with 2,023 tasks and a multi-part evaluation, used to show that 25 model rows execute code more often than they match target charts, with Level 3 near floor. It matters if people want a harder chart-to-code yardstick after ChartMimic-style benchmarks saturate.

## Summary
The paper introduces a hierarchical chart-to-code benchmark and evaluates a broad set of proprietary and open LMMs. It reports a consistent gap between executability and visual fidelity and a sharp drop at Level 3.

## Strengths
### S1: Clear structure and message
The three-level organisation (Fig. 1, §3.1) is easy to follow, and the executability vs fidelity message is stated crisply.
### S2: Broad, current model coverage
Table 3–5 include GPT-5, Gemini-2.5-Pro, Claude-Sonnet-4 and many open models, including thinking variants.
### S3: Good appendix transparency
Prompts (App. K), run configurations (Table 9), model versions and dates (Table 12) are given.
### S4: Human-labelled difficulty buckets
§4.3 and Fig. 3 attempt to validate that levels are harder with human easy/medium/hard labels, a nice idea.

## Venue criteria checklist (ICLR)
| Item | Status | Location |
|------|--------|----------|
| Soundness: claims supported by evidence | Partly | §4.2; text/table conflicts (Tables 3–6) |
| Contribution: significant for the community | Partly | Level 3, Table 1 |
| Presentation: clear writing and figures | Partly | Text analyses quote numbers absent from the tables |
| Reproducibility: details, code, data | Partly | App. F, K; no link visible |
| Related work positioned | Partly | §2, Table 1 |
| Ethics/limitations | Partly | §5, App. A |

## Weaknesses
### W1: Result text and tables do not agree, which hides the contribution
Section 4.2.1/4.2.2 quote values that differ from Table 4 (e.g., InternVL-3-38B ER "61.51" vs 67.43; Qwen2.5-VL-72B figure-level "0.1437" vs 0.1684), the abstract's "0.22" differs from Table 4's 0.2506 for GPT-5, and Table 2 sums to 2,059 instructions, not the printed 2,509. A reader cannot tell which version the conclusions rest on. 
- **Suggested Fix**: One script generates all tables and in-text numbers.

### W2: The evaluation is mostly by one LLM judge with no reported validation
The final score is GPT-5-mini ("most aligned with human intuition", §3.4), the metric benefits from a rubric that deducts from 100, and the judge is from the same family as an evaluated model. Appendix Figs. 7–11 compare human and model scores but the text gives no numbers. 
- **Suggested Fix**: Report human agreement with CIs; add a second judge.

### W3: Analysis is largely a restatement of table cells
§4.2.2 repeats numbers for each level with limited diagnosis: no error taxonomy (syntax vs data vs style), no breakdown by chart type, no examples tied to failures (App. B is generic). The third contribution, "new insights", is thus thin. 
- **Suggested Fix**: Add an error taxonomy over ER failures and a chart-type breakdown (Fig. 2 already has the types).

### W4: Level definitions are not shown to be an ordering of difficulty
Level 2 reuses Level 1 charts (§3.3) and Level 3 changes the input modality and length; the metrics and ER ceilings differ. In Fig. 3 (as extracted, model attribution of rows garbled) two Level-1 rows have Medium ≥ Easy. 
- **Suggested Fix**: Report per-level human difficulty or solve rates for controlled variants.

**Minor**: "Projecet lead", "Deatiled data statistic", "origianl" (Table 10), "ChartXiv", duplicate "Setting 2" label in Fig. 1, "DM"/"DR" naming, abstract's code/data link without URL (blinded).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See W1–W2 |
| Clarity | 2 | Text/table conflicts |
| Significance | 3 | Likely used if validated |
| Originality | 2 | Incremental plus L3 |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a decent, useful benchmark but with unvalidated metrics and visible internal inconsistencies, typical of borderline-to-rejected benchmark submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Judge-based, partly unvalidated |
| Clarity & Presentation | 50 | Developing | Text vs table conflicts |
| Novelty & Originality | 55 | Competent | New level, moderate |
| Significance & Impact | 60 | Competent | Useful task |
| Experimental Validation | 50 | Developing | Broad but shallow analysis |
| Reproducibility | 55 | Competent | Prompts and configs |
| Ethical Compliance | 58 | Competent | Limitations discussed |

## Questions for Authors
1. Which values are correct in the Level 2 text vs Table 4? A corrected, consistent set would raise my Clarity score.
2. What is the judge–human agreement?
3. What are the dominant failure types behind ER < 40% at Level 3?

## Limitations Assessment
**Partially.**
## Ethics Review Flag
**No**
## Overall Score
**3**: A reasonable benchmark with an interesting Level 3, but evaluation validity and internal consistency need to be fixed before the results can be relied on.
## Confidence
**4**

---

# Devil's Advocate Report

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Reviewer: Dr. Selin Arvidsson-Park, research institute, Nordic region (fictional persona)

## Steelman
Chart-to-code is a practical capability, frontier models look strong on older benchmarks, and Chart2Code adds harder, more realistic tasks (editing, long-table plotting) with per-dimension scoring, showing that executing code is not the same as producing a faithful chart.

## Core Argument Chain
1. Existing benchmarks give high scores (GPT-4o 83.2 on ChartMimic, 93.6 on ChartEdit; §2), "suggesting that the problem is close to being solved".
2. Chart2Code tasks are more realistic ("user-driven") and harder (three levels).
3. Models score low on Chart2Code (GPT-5 0.57 code / 0.22 chart on editing; Level 3 LMM ≤ 0.07).
4. The scores are valid measures of chart fidelity (GPT-5-mini judge, `Figure`-object matching).
∴ Current LMMs are far from solving realistic chart2code, and Chart2Code measures this reliably.

## Strongest Counter-Argument
The inference from premises 1–3 to the conclusion silently depends on premise 4, which is never tested. "Low scores" are interpreted as "hard task", but the LMM-Score is a GPT-5-mini deduction rubric that starts at 100 and subtracts for every visual difference (App. E.4); its scale is arbitrary and its calibration is unknown. The paper never reports the score of the ground-truth code against itself, a human re-implementation, or the correlation of the judge with humans (the text gives no statistic), and it uses a different, harsher scoring than the 83.2/93.6 it contrasts with, on a different model set (GPT-4o is not evaluated). So the "gap between old benchmarks and Chart2Code" may come from metric change, not task difficulty. Second, the headline Level 3 result (LMM ≈ 0.04) is at floor and described by the authors themselves as likely affected by input-length limits ("long-context inputs exceeding the maximum input limits") and "edge-case artifacts" (LLM-Score = 0 with non-zero sub-scores); a floor effect cannot show that "fidelity is the main bottleneck". Third, the supporting tables are internally inconsistent: Table 3 contradicts Tables 6–8, the text of §4.2 quotes values not in Table 4, and two of the three "metric anomalies" the paper analyses (Seed-1.6-VL 0.8117; MiMo-VL-7B-RL 0.4713) are not reproducible from the other tables (Table 6: 0.23; Table 4: 0.1573). The authors must show (i) judge validity and a ceiling, (ii) a shared-metric comparison with ChartMimic/ChartEdit, and (iii) one consistent set of results. Without these, the benchmark's central claim, that it reveals a real capability gap and reliably ranks models, is untested rather than refuted.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The evidence supports a weaker claim ("these models fall short on these tasks under this judge"), which authors can narrow or validate; nothing contradicts the main claim, no test-set selection is reported, and the metric is imperfect but not one that cannot measure fidelity at all.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §3.4, App. E.2–E.4 | Metrics not validated; "superior evaluation performance" asserted; one judge family; no ceiling; absolute scores uninterpretable | Human agreement with CIs, second judge, GT-code ceiling |
| DA-M2 | Evidence/Integrity of reporting | Tables 2–6, §4.2.2, Abstract | Text–table–appendix conflicts; "0.22" vs 0.2506; two analysed anomalies are not reproducible | Regenerate all numbers from one file |
| DA-M3 | Logic | §2, §1 | "Close to being solved" contrasts non-comparable metrics and models | Shared-metric run on ChartMimic/ChartEdit |
| DA-M4 | Scope/Confound | §4.2.1, Table 5, Fig. 3 | Level 3 floor and truncation confound; only five models; difficulty ordering not shown | Length-vs-success analysis; chunked inputs; flag floor ranks |
| DA-M5 | Evidence | §3.2.3 | Annotation loop uses "the LMM" and LLM-written edits; filtering 4,700 → 1,010 unspecified; possible bias toward the annotating model family or adversarial filtering | Name the models; state filter criteria; report per-annotating-model effects |
| DA-M6 | Scope | Abstract, §1 | "User-driven"/"real-world" claim lacks user evidence; contamination not analysed | Survey/logs; date-split results |
| DA-M7 | Claim distortion (E5) | §4.2.2 | "Thinking Helps Procedural Compliance" contradicted by Qwen3-VL-30B in Table 3 | Narrow claim |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Reporting | Table 2 | Total instructions 2,509 vs 899+1,010+150 = 2,059; average > maximum data entries |
| DA-m2 | Reporting | §3.2.2 vs App. C.2 | "80 raw data figures" vs "80 structured data files (such as CSVs)" |
| DA-m3 | Reporting | §4.1, Table 9 | "12 representative" vs ≈ 18 listed; "temperature ... 0.1 across all models" vs Table 9 shows 0 for proprietary models; `deepseek-vl-7b-base` and `glm-4-9b` checkpoints listed |
| DA-m4 | Presentation | §2, Table 1 | "ChartXiv"; QA benchmark listed as chart-to-code; "AcademiaChart" label |
| DA-m5 | Reproducibility | Abstract | "Our code and data are available on Chart2Code" has no resolvable link in the blinded text (unverified, not an error) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Total instructions (Table 2) | 2,509 | 899 + 1,010 + 150 = 2,059 | ✗ |
| Total charts (Table 2) | 2,023 | 863 + 1,010 + 150 = 2,023 | ✓ |
| Unique instructions (Table 2) | 1,305 | 145 + 1,010 + 150 = 1,305 | ✓ |
| GPT-5 editing LLM-Score (Abstract "0.57") | 0.57 | Table 4: 0.5663 | ✓ |
| GPT-5 editing chart score (Abstract "0.22") | 0.22 | Table 4: 0.2506 (text §4.2.2: 0.2201) | ✗ |
| Seed-1.6-VL DM LMM-Score | 0.8117 (Table 3) | 0.23 (Table 6) | ✗ |
| Level 3 ER, Gemini | 29.33 | 44/150 = 29.33 | ✓ |
| CFD sample size | 87.04% ER | 94/108 = 87.04% | ✓ (n = 108) |
| Qwen3-VL-30B CFD ER, thinking vs non-thinking | 70.37 → 39.81 | −30.56 points | contradicts "thinking helps" |

## Ignored Alternative Explanations
- Low LMM-Score reflects the judge's deduction rubric and style sensitivity, not necessarily task difficulty.
- Conditional averaging (executed outputs only) can inflate weak models (Molmo-7B-D: ER 4.55%, CRD LMM 0.46).
- L3 failures may come from token/context limits, not chart ability.
- Contamination of public arXiv/tutorial/ChartMimic charts may inflate L1/L2 for some models.
- Judge self-preference (GPT-5-mini judging GPT-5 outputs).

## Missing Stakeholder Perspectives
Practitioners (analysts, scientists) who write charts; the annotators and original chart authors whose figures are redistributed.

## Observations (Non-Defects)
The authors flag judge limits (§5), disclose configurations and licences, and notice several of their own metric anomalies (§4.2.2); the L3 task design is genuinely harder than prior suites, and the code-vs-image separation is a sound idea.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Unvalidated metric; conflicting tables |
| Clarity & Presentation | 48 | Text and tables describe different numbers |
| Novelty & Originality | 48 | Incremental apart from L3 |
| Significance & Impact | 52 | Limited by trust in the scores |
| Experimental Validation | 40 | Floor effects, single run, small subsets |
| Reproducibility | 50 | Prompts yes; filters, link, conditional averaging unclear |
| Ethical Compliance | 55 | Basic |

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: metric validity untested and headline tables internally inconsistent.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 table conflicts | kept | All quoted values re-found in the text (Table 4 vs §4.2; Table 3 vs 6–8) |
| R1 | W2 judge unvalidated | rewritten | Added that Figs. 7–11 (human vs model) exist but are not visible; no statistic in text |
| R1 | W3 denominator | kept | Phrased as question-plus-evidence; Molmo row verified in Table 3 |
| R1 | W6(c) Fig. 3 monotonicity | rewritten | Marked as based on garbled figure text; moved to hedged wording |
| R2 | W2 ChartMimic customized task | rewritten | Cannot be verified from the kept abstract; marked [verify] and turned into a question |
| R2 | W5 citation hygiene | moved to Minor | Cosmetic naming issues |
| R3 | W5 matplotlib-only scope | kept (Minor-leaning) | Reasonable but low severity |
| R4 | W4 level ordering | rewritten | Hedged on Fig. 3 extraction |
| R4 | typos | moved to Minor | One line |
| DA | DA-m5 code link | kept as unverified | Blinded text, not an error |
Scores were not changed.

# Synthesizer package (Part A)

**Master issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Text/table/appendix numerical conflicts | R1-W1, R4-W1, DA-M2, DA-m1 | CONSENSUS-3 (hinge) |
| Metric/judge unvalidated; no ceiling; self-preference | R1-W2, R4-W2, DA-M1, R2-W3/W4 (partly), R3-W2 (partly) | CONSENSUS-4 (hinge) |
| Denominator / conditional averaging | R1-W3, DA (alt. explanations) | CONSENSUS-2 |
| Level 3 floor/truncation, 5 models | R1-W4, DA-M4 | CONSENSUS-2 |
| Single run, small sub-settings | R1-W5 | SOLO |
| Overstated analysis ("thinking helps", difficulty ordering, "hardest") | R1-W6, R4-W4, DA-M7 | CONSENSUS-3 |
| Positioning: Doc2Chart/Text2Chart31 uncited; "first" claim | R2-W1, R2-W2 | SOLO |
| "User-driven" unsupported; contamination | R3-W1, R3-W3, DA-M6 | CONSENSUS-2 |
| Licensing/annotator conditions | R3-W4, R1 (Repro.) | CONSENSUS-2 |
| Annotation by "the LMM"; filter unspecified | DA-M5, R1 (protocol sweep) | CONSENSUS-2 |
| Shallow analysis, no error taxonomy | R4-W3 | SOLO |
**DA-CRITICAL:** none. **SPLIT:** none (reviewers differ only by 1 Overall point). Outcome may hinge on: numerical conflicts and judge validation.
Official output (BEFORE run, no EIC weights): see below.

---

# Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: From Charts to Code: A Hierarchical Benchmark for Multimodal Models
## Submission ID: iclr26-oCkPzCR4f4
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: benchmark
## Review Team (fictional personas): EIC Prof. Ingrid Solheim-Okafor; R1 Methodology Dr. Mateus Okonkwo-Hartmann, R2 Domain Dr. Léa Marchetti-Nwosu, R3 Perspective Dr. Priyanka Delacroix-Ibarra, R4 Generalist Dr. Haruto Vanterpool, DA Dr. Selin Arvidsson-Park

---

## Decision: Borderline Reject (3), ICLR rating label from the script below

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60 · official composite 51.0
**EIC assessment** (internal): weighted rating 2.52 → starting point 3 · weighted composite 50.3 → band 3 (cross-check agrees, but sits only 0.3 above the 3/2 edge at 50) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR label** (script, `--final 3`): 4 on {0,2,4,6,8,10} (5 on the earlier {1,3,5,6,8,10} scale); Soundness 2, Presentation 2, Contribution 2.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely benchmark with a genuinely harder Level 3 (long Excel tables → chart with style reference), a CRD/CFD data-in setting, broad coverage of current proprietary and open models, and disclosed prompts/configs. Chart-to-code benchmarks have been well received and the reported gap between executability and fidelity is plausible and useful.
- **Against acceptance:** Every conclusion is read through an unvalidated GPT-5-mini rubric; the main text, Table 3–5 and the appendix tables contradict each other in at least a dozen cells, two of three analysed "anomalies" are artefacts of those inconsistencies, the Level 3 result sits at floor on only five models, and novelty is moderate (L1/L2 are close to ChartMimic/ChartEdit; related chart-generation work is uncited).

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Text values for Level 2 differ from Table 4 (ER 90.49/90.92/71.89/61.51 vs 90.30/91.19/71.49/67.43; LMM 0.2134/0.1844/0.2201 vs 0.2459/0.2147/0.2506) | R1-W1, R4-W1, DA-M2 | §4.2.1–4.2.2, Table 4 | Verified | Re-read both locations |
| "unusually high figure-level 0.4713" for MiMo-VL-7B-RL (non-thinking) | R1 ERR-3, DA-M2 | §4.2.2 vs Table 4 | Verified | Table 4 gives 0.1573; text also says thinking row "lacks figure-level" but Table 4 has 0.1737 |
| Seed-1.6-VL DM LMM-Score 0.8117 is an error | R1 ERR-4, DA | Table 3 vs Table 6 | Verified | Table 6: 0.23; Table 3 CRD Seed values swapped vs Table 7 as well |
| Table 3 InternVL-3-8B duplicates 3.5-8B; InternVL-2.5-38B "0" | R1 ERR-5 | Tables 3, 6, 7, 8 | Verified | Table 6/7/8 give distinct rows |
| Table 5 Claude/GPT-5 identical sub-scores | R1 ERR-6 | Table 5 | Verified | Identical nine values; possible copy error (Medium confidence kept) |
| Table 2 total instructions 2,509 | R1 ERR-1, DA | Table 2 | Verified | 2,059 by the table's own rows; unique total 1,305 sums correctly |
| Abstract "0.22" chart-quality | DA | Abstract vs Table 4 | Verified | 0.2506 in Table 4 (0.2201 only in text) |
| No judge–human statistic in the text | R1-W2, R4-W2, DA-M1 | §3.4, App. D.1/E | Partly correct | Figs. 7–11 "human vs model" exist but figures/numbers are unavailable; Appendix C.1 agreement (> 0.8) concerns chart selection, not the judge. Treated as unverified, not absent |
| "superior evaluation performance" unsupported | R1-W2, R2-W4, DA | §3.4, App. E.2 | Verified | E.2 argues qualitatively only |
| Denominator unstated; Molmo CRD LMM 0.46 at ER 4.55% | R1-W3 | §3.4, Table 3 | Verified (inference Medium) | Consistent with conditional averaging; not proven |
| "Thinking Helps Procedural Compliance" overstated | R1-W6, DA-M7 | §4.2.2, Table 3 | Verified | Qwen3-VL-30B CFD ER 70.37→39.81; DR 64.67→45.06 |
| Difficulty "clear correlation" (§4.3) | R1-W6(c), R4-W4, DA | §4.3, Fig. 3 | Partly correct | Garbled extraction shows Medium ≥ Easy in two Level-1 rows; figure not visible, treated as a question |
| Doc2Chart / Text2Chart31 uncited and relevant | R2-W1 | §2, Table 1 | Verified (abstracts) | Prior, peer-reviewed; overlap with L3 is partial, not "known" |
| ChartMimic "Customized" task already exists | R2-W2 | §3.1 | Unverifiable from the kept abstract | Kept as [verify]; no effect on weights or decision |
| "User-driven" claim lacks user evidence | R3-W1, DA-M6 | Abstract, §3.2.3 | Verified | No survey/log/practitioner evidence found by search |
| Dataset licence not stated | R3-W4, R1 | Table 11 only for models | Verified | Text search found no dataset licence statement |
| Judge self-preference risk | R1-W2, DA | §3.4, App. E.3–E.4 | Verified (as a risk) | GPT-5 is evaluated; GPT-5-mini family judges; no control |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error log verified item by item; central points hold; calibration at the harsh end but justified |
| R2 (Domain) | 3 | 4 | 1.0 | Literature points verified from abstracts; one point unverifiable and correctly hedged |
| R3 (Perspective) | 3 | 3 | 1.0 | Realism/licensing/contamination points verified; some generic |
| R4 (Generalist) | 3 | 4 | 0.9 | Core points sound, but credits the Fig. 3 difficulty validation as a strength, which the extracted figure text only weakly supports |
| DA | 2 | 4 | 1.25 | Counter-argument survives my check (premise 4 untested, non-comparable metrics, table conflicts); no overstatement found |

### DA-CRITICAL Rulings
None raised ("No CRITICAL issues found"). I agree: no leakage or test-set selection, nothing contradicts the main claim, and the metric, while unvalidated, is not one that cannot measure fidelity. The DA's MAJOR issues stand (DA-M1…M7). The DA ceiling is therefore none.

### Final Decision and Justification
The EIC-weighted rating is 2.52 and the plain mean is 2.60, so the starting point is 3 (Borderline Reject). The rating sits within 0.1 of the 2.5 boundary and the composite cross-check (50.3) agrees with band 3 but only 0.3 above the edge to band 2, so both signals say "weak reject-side borderline", and I cannot name a verified issue the ratings missed that would justify moving either way. The decision is 3: the benchmark idea is worthwhile and Level 3 is a real addition, but the verified evidence problems are not cosmetic: results the paper itself analyses (the 0.812 and 0.4713 "anomalies") do not exist in its other tables, and no quantified judge validation or ceiling supports reading 0.22 as "low". All of this is fixable, mostly without new training but with new judge-validation and a shared-metric comparison, which is why I stay at 3 and do not go to 2. My pool position for this draft: better than about 40% of ICLR submissions (accepted share ≈ 27%). Deciding evidence: unvalidated sole metric and internal numerical conflicts versus a useful new level; typical accepted benchmarks validate their metric. The decision does not exceed any DA ceiling (none).

---

## Score Summary

### Official Scores and EIC Assessment
*(Final script run with EIC weights R1 1.25, R2 1.0, R3 1.0, R4 0.9, DA 1.25; the full table is in `aggregate.json`.)*

| Dimension | R1 | R2 | R3 | R4 | DA |
|-----------|----|----|----|----|----|
| Technical Rigor | 40 | 50 | 52 | 50 | 42 |
| Clarity & Presentation | 45 | 55 | 56 | 50 | 48 |
| Novelty & Originality | 45 | 52 | 55 | 55 | 48 |
| Significance & Impact | 55 | 58 | 62 | 60 | 52 |
| Experimental Validation | 38 | 48 | 50 | 50 | 40 |
| Reproducibility | 48 | 55 | 58 | 55 | 50 |
| Ethical Compliance | 55 | 55 | 52 | 58 | 55 |
| **Composite (own)** | 45.8 | 53.2 | 55.4 | 53.6 | 47.0 |

BEFORE (no EIC weights): official composite 51.0, confidence-weighted 50.8; ratings mean 2.60, weighted 2.59 → 3.
AFTER (EIC weights): official composite 51.0 (unchanged), EIC-weighted composite 50.3; EIC-weighted rating 2.52 → 3.

| Dimension | Official (raw mean) | EIC assessment (weighted) |
|---|---|---|
| Technical Rigor | 46.8 | 46.0 |
| Clarity & Presentation | 50.8 | 50.2 |
| Novelty & Originality | 51.0 | 50.4 |
| Significance & Impact | 57.4 | 56.8 |
| Experimental Validation | 45.2 | 44.4 |
| Reproducibility | 53.2 | 52.6 |
| Ethical Compliance | 55.0 | 55.0 |
| **Composite** | **51.0** | **50.3** |

### Target-Venue Scores (ICLR, scale status: secondary)
Soundness 2, Presentation 2, Contribution 2; ICLR rating (script, `--final 3`): 4 on {0,2,4,6,8,10} (5 on the earlier {1,3,5,6,8,10} scale), to be quoted "as labeled on recent forms; verify against the current form".

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "From Charts to Code: A Hierarchical Benchmark for Multimodal Models" to ICLR. Chart-to-code generation is a timely topic and the attempt to move beyond image reproduction to editing and long-table plotting is welcome.

**Overall Assessment:** The panel found the task design, in particular Level 3 and the data-in Level 1 settings, a useful addition, and appreciated the breadth of models and the disclosed prompts. The panel also found that the evidence does not yet support the central conclusions: the numbers in the text, the main tables and the appendix disagree, and the evaluation metric is not validated.

**Key Strengths Identified by Reviewers:**
1. A realistic, harder Level 3 (long tables to chart) and data-in settings absent from the compared benchmarks (R1, R2, R3).
2. Broad coverage of proprietary and open-weight models, with component scores that separate executability from fidelity (R1, R4).
3. Open disclosure of prompts, configs and limitations (R1, R4, DA).

**Key Concerns Requiring Attention:**
1. The headline tables and text contradict each other (CONSENSUS-3; verified by the EIC).
2. The GPT-5-mini-based scores are unvalidated, have no ceiling and no second judge (CONSENSUS-4).
3. Level 3 conclusions are confounded by input limits and floor effects, with only five models (CONSENSUS-2).
4. Positioning: uncited chart-generation work, an unqualified "first", and an unsupported "user-driven" framing.

**Critical Challenge (Devil's Advocate):** none rated CRITICAL; the strongest objection is that "low scores" are interpreted as "hard task" although the metric's calibration is unknown and the cited prior-benchmark scores come from a different metric and model set.

**Decision: Borderline Reject (3)**

The idea merits publication once the evidence is repaired. A revision that regenerates all numbers from one source, validates the judge against humans (with a ceiling and a second judge), compares on shared metrics with ChartMimic/ChartEdit and reports denominators and uncertainty would make this a competitive submission. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Solheim-Okafor
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Text/table/appendix numerical conflicts | R1, R4, DA | CONSENSUS-3 |
| Metric/judge unvalidated | R1, R2, R3, R4, DA | CONSENSUS-4 (+) |
| Overstated analytic claims | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the difficulty hierarchy is validated (§4.3, Fig. 3) | R4 (strength) | R1, DA | EIC: partly correct; the extracted figure text weakly supports monotonicity; figure not visible; weight R4 at 0.9 |
| Severity of the overall paper | R2, R3, R4 give 3 | R1, DA give 2 | EIC: 3, because defects are fixable without redesign |

### Score Spread Discussion
No dimension exceeds the 20-point spread; the largest spread is 12 points (Technical Rigor, Experimental Validation).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Metrics unvalidated | Yes (R1, R4) | n/a | n/a |
| DA-M2 | MAJOR | Text–table conflicts | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Non-comparable "nearly solved" contrast | Partly (R2) | n/a | n/a |
| DA-M4 | MAJOR | L3 floor/truncation | Yes (R1) | n/a | n/a |
| DA-M5–M7 | MAJOR | Annotation loop, user-driven claim, thinking claim | Partly | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Numerical conflicts across text, Tables 2–8 and abstract (e.g., 0.8117 vs 0.23; 0.4713 vs 0.1573; 2,509 vs 2,059; duplicated rows in Tables 3 and 5) | R1-W1, R4-W1, DA-M2 | Abstract, Tables 2–8, §4.2 | Regenerate all tables and in-text numbers from one results file; re-verify Table 5 Claude/GPT-5 rows against raw outputs; delete the "outlier" analyses that were artefacts | Low–Med; ≈ 0 GPU-h, 1–2 days | Yes |
| R2 | Metric validity: judge–human agreement, ceiling (GT code), second judge, self-preference check | R1-W2, R4-W2, DA-M1, R3-W2 | §3.4, App. D–E | Stratified human study (≈ 300 items × 3 raters), second judge from a different family, GT-code ceiling | Med; ≈ 2–4 annotator-days + API cost | Partly |
| R3 | Score denominators and conditional averaging | R1-W3 | §3.4, Tables 3–5 | Report "all tasks" and "executed only" and a paired common-subset score | Low | Yes |
| R4 | Shared-metric comparison to back "nearly solved" and the "gap" claim | DA-M3, R2-W3 | §1–2 | Run 3–4 models on ChartMimic/ChartEdit subsets with the Chart2Code metric | Low–Med; ≈ 1 day | Yes |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Level 3 confounds (token limits, floor, 5 models) | R1-W4, DA-M4 | Length-vs-success analysis; chunked table access; flag floor ranks | Med | Partly |
| S2 | Uncertainty: single run, n = 36/108/30 | R1-W5 | Paired bootstrap CIs; 3 seeds for top models | Med; 30–60 GPU/API-h | Partly |
| S3 | Overstated claims (thinking, hardest subtask, difficulty ordering, "first") | R1-W6, R4-W4, DA-M7, R2-W1 | Narrow wording or add evidence | Low | Yes |
| S4 | Positioning and Table 1: Doc2Chart, Text2Chart31, ChartReformer; delta table vs ChartMimic/ChartEdit; fix names | R2-W1, W2, W5 | Add references and a task-delta table | Low | Yes |
| S5 | Annotation loop and filtering (which LMM, criteria 4,700 → 1,010) and contamination by source/date | DA-M5, R3-W3 | Document; date-split results | Low–Med | Yes |
| S6 | "User-driven" evidence; data-fidelity metric | R3-W1, W2 | Practitioner survey or soften; data-only score | Med | Partly |
| S7 | Dataset licences, annotator pay | R3-W4 | Datasheet | Low | Yes |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Error taxonomy and chart-type breakdown | R4-W3 | Add analysis from Fig. 2 types |
| N2 | Matplotlib-only scope; Plotly/Matlab reference conversion | R3-W5 | State conversion; discuss Vega-Lite |
| N3 | Typos and naming (Projecet, Deatiled, origianl, ChartXiv, DM/DR, duplicate "Setting 2") | R4, R2 | Copy-edit |
| N4 | Table 9 vs §4.1 temperature; checkpoints (`deepseek-vl-7b-base`, `glm-4-9b`) | DA-m3 | Clarify |
| N5 | Worth discussing: ChartM³, ChartMaster, ChartGen | R2 | Discuss, not required |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 1–2 weeks (dominated by the human validation study)
- Priority 2: 7 items, ≈ 1–2 weeks
- Priority 3: 5 items, 1–2 days
- **Total estimated revision time**: ≈ 3–4 weeks
