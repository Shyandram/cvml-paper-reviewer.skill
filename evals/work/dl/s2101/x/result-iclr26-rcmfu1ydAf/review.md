# Simulated Review: "HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks"

*Date: 2026-11-10 · Mode: full · Target venue: ICLR (2026 cycle profile) · Literature check: strict, cutoff 2025-09-24 · Submission ID: iclr26-rcmfu1ydAf*
*This is a simulation of how a careful panel would likely see this draft, not a prediction. Five role-based passes were run one after another in one shared model context (no subagents), so the reviewers are separate perspectives, not independent agents. Figures were not available (text extraction only): figure-dependent claims are judged from captions and text, and bold/underline marks in Table 2 could not be checked.*

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks |
| Primary Discipline | NLP → text embeddings, evaluation methodology / benchmark analysis |
| Secondary Discipline(s) | Information retrieval (relevance judgments), human annotation and inter-rater reliability, multilingual NLP |
| Paper Type | Benchmark / evaluation study (composite weights: benchmark) |
| Core Technique(s) | Human annotation (Argilla) of 16 downsampled MTEB datasets in 4 task categories; comparison with 13 embedding models; inter-annotator agreement (Fleiss κ, ARI, Spearman, Kendall τ) |
| Target Venue | ICLR (stated by user); profile key `iclr` |
| Venue-Specific Notes | None. ICLR form: Soundness / Presentation / Contribution (1–4), Rating, Confidence. Accepted share ≈ 27% of submissions |
| Paper Maturity | Submission-ready (full paper with appendix; the code/data link is removed in the blinded copy) |
| Ethics-Relevant Content | Human annotators (3 persons, all male, 20–35; compensation, consent and exposure to toxic text not stated); social-media and Reddit text; toxic-content dataset; released annotations |

### Claimed Contributions (as stated by the authors, §1)
1. **C1:** "a generalizable framework for human evaluation of embedding tasks" (resource/method).
2. **C2:** "empirical evidence of how humans perform across diverse datasets and task types" (result): human average 77.6 vs 80.1 for the best of 13 models (Abstract, Table 2, Fig. 1).
3. **C3:** "comparative analysis of models and humans that highlights strengths, weaknesses, and ambiguities in both benchmarks and models" (result): apparent model "superhuman" performance coincides with low human agreement; some MTEB datasets are unreliable; humans beat models in non-English sentiment and Arabic STS (§4.3, §5).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** 16 MTEB datasets, 26 task-language pairs (Table 2 header "(26)"); languages eng, ara, rus, dan, nob (§3.2, footnote 1). Samples: reranking 20–49 queries, classification 40–48 examples, clustering 30 items, STS 30–50 pairs (§3.3). Annotation in Argilla; binary relevance for reranking, categorical labels for classification, free cluster IDs for clustering, 0–5 scores for STS (§3.3). English tasks: 2 annotators; multilingual tasks: 1 annotator (§3.3). Annotators: male, 20–35, "experienced NLP practitioners" (§3.3); §5.3 says "three annotators participated overall". Models: 13, 22M–7B parameters (§3.4, Table 7). Metrics: MAP / accuracy / V-measure / Spearman as primary (§3.4). **Not stated:** how items were sampled, how multiple annotators' labels are turned into one "human performance" number, MTEB-side protocol details (classifier training set, number of clusters, instruction prompts for instruction-tuned models), annotator pay or consent, annotation guidelines text, uncertainty estimates, seeds.
- **Headline numbers.** Human 77.6 overall, rank 4 of 14 (Abstract, Fig. 1, §4, Table 2); best model 80.1 (jasper_en_vision_language_v1, Table 2); humans best on 4 of 26 pairs (Fig. 13, §4.1) but Table 2 caption says "5 of 14"; humans above median model on 61.5% of pairs (§4.1); Emotion κ = 0.39, ArXiv ARI = −0.001, Toxicity κ = 0.55 (§4.3).
- **Appendix.** A: full per-dataset tables (Tables 3–6). B: annotation-interface screenshots with agreement and performance in captions (Figs. 4–12). C: dataset-quality narratives (STS22-Russian, Russian sentiment, Emotion, ArXiv). D: agreement numbers by task. E: gap plots (Figs. 13–16). F: model list (Table 7). G: LLM-usage statement.
- **Unverifiable.** All figures (read from captions only); bold/underline in Table 2; the released code, data and leaderboard (link removed); annotation guidelines.
- **Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters found. The reviewers read the redacted copy (identical to the paper text here).

### Literature check (Phase 1.5; mode strict, cutoff 2025-09-24)
Five queries run (claim: 4, baseline: 1; expansion: 0; budget 12). Kept 62 results, all prior (2 recent preprints). The script's `benchmarks` listing found no external benchmark to scout, so there is no baseline-scout table beyond the models the paper itself lists. Closest prior works by similarity (all "pointers", cosine ≤ 0.25, no text overlap): MMTEB (cited by the paper), jina-embeddings-v3, LUSIFER. No prior work found on human baselines for MTEB-style embedding tasks (arXiv only; a limit of the search, not proof of novelty). Gap left open: none beyond that.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Teodora Valcheva, large public research university (Southeast Europe)
- **Seniority / Expertise**: Senior faculty / retrieval evaluation, test-collection methodology, multilingual NLP benchmarks
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Has chaired benchmark and datasets tracks; wants claims that the data can carry.

### Reviewer 1 (Methodology): Dr. Kwabena Asante-Rowe, industrial research lab (North America)
- **Seniority / Expertise**: Senior industry scientist / annotation protocols and inter-annotator statistics; evaluation of embedding models
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; insists on uncertainty estimates and matched protocols.

### Reviewer 2 (Domain): Dr. Mireille Duquesnoy, public research institute (Western Europe)
- **Seniority / Expertise**: Mid-career / text embedding models, MTEB-style benchmarks, relevance assessment
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work line by line; checks what each cited paper really claims.

### Reviewer 3 (Perspective): Dr. Selim Barakzai, psychology and measurement department, university (Middle East)
- **Seniority / Expertise**: Mid-career / psychometrics, inter-rater reliability, crowdsourcing ethics
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive, asks what the measurement means.

### Reviewer 4 (Generalist): Dr. Priya Raghunathan-Beck, industrial research lab (South Asia)
- **Seniority / Expertise**: Mid-career / representation learning, general ML (not evaluation methodology)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers look like.

### Devil's Advocate: Prof. Joaquín Medrano-Lindqvist, university statistics and ML group (Latin America)
- **Seniority / Expertise**: Senior faculty / causal inference, evaluation validity, measurement error
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks "does this prove what they claim?"

*Personas are fictional. Venue and paper type were stated or chosen as above; they drive calibration.*

---

# Phase 1: Independent Reviews

# Peer Review Report

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Reviewer: Dr. Kwabena Asante-Rowe, Reviewer 1 (Methodology) (industrial research lab, North America; fictional persona)
## Expertise: annotation protocols and inter-annotator statistics; evaluation of embedding models
## Date: 2026-11-10

---

## Summary
The paper collects human annotations on small, downsampled subsets (20–50 items) of 16 MTEB datasets in four task types and five languages, and scores the annotators with the same metrics as 13 embedding models. Humans average 77.6 and rank fourth, behind three models (§4, Table 2). The authors then relate human agreement to model–human gaps, argue that "superhuman" model scores concentrate on low-agreement tasks, recommend replacing several datasets, and say humans beat models on non-English sentiment and Arabic STS (§4.2–§5). The study is useful in intent and the raw per-dataset tables (Tables 3–6) are a real resource. The conclusions go well beyond what the sample can carry.

---

## Strengths

### S1: A new, useful measurement
Table 2 and Tables 3–6 give per-dataset human scores next to 13 models on identical instances, which MTEB lacks. Even with large error bars, the per-task numbers are a starting point for the community.

### S2: Agreement is reported per task with task-appropriate statistics
Appendix D reports κ, ARI, ρ and Kendall τ, with item counts and raw percentage agreement (e.g., Emotion: 2 annotators, 48 items, 52.1%). This transparency is what makes several inconsistencies below checkable.

### S3: Honest limitations and a usable resource
§5.3 states the small sample, the two-annotator limit and annotator background, and says the downsampled subsets are in the MTEB package (§3.3). That supports reuse and re-analysis.

---

## Weaknesses

### W1: The human and model protocols are not matched, but the paper says they are
§3.4 states that models are evaluated "using identical metrics, protocols, and computational settings". The task definitions differ for the two sides. Humans labelled "without access to ground truth or model predictions" (§3.3) and used "free assignment of cluster IDs" for clustering and "binary relevance judgments" for reranking. The paper does not say how the model side was run: the size of the training set for the classifier in classification, how many clusters were fixed for the clustering metric, how ties from a binary or 0–5 human scale enter MAP and Spearman, and what instruction prompts the instruction-tuned models received. Each of these can move the human–model gap by more than the 2.5-point headline gap (80.1 vs 77.6). In particular, an annotator who sees no labelled examples is compared with a model whose classifier may be fit on labelled examples.
- **Suggested Fix**: Describe the model-side MTEB protocol per task type in a table; add matched controls (humans given the same number of labelled examples or the true cluster count; models evaluated zero-shot or with the same budget). About 1–2 days of re-running models, plus a small extra annotation round.

### W2: No uncertainty anywhere, on very small samples with 1–2 annotators
Samples are 20–50 items per dataset (§3.3), one annotator for all multilingual tasks and two for English. No confidence interval, bootstrap or significance test appears (the paper contains no such terms). A single accuracy on 40 items has a standard error of about 6–8 points near 50–75%. Yet the paper ranks humans "4th place" (Fig. 1) against models that differ by 0.1–2.5 points (Table 2: 80.1, 78.3, 78.2 vs 77.6, 77.5), reports win rates (Fig. 3), and contrasts κ = 0.39 (Emotion) with κ = 0.55 (Toxicity) from 48 and 45 items. By the usual large-sample approximation (derived, assuming chance agreement near 0.2) a κ of 0.39 on 48 items has a 95% interval of roughly ±0.18, so "fair" and "moderate" are not separable.
- **Suggested Fix**: Paired bootstrap over items (and annotators where available) for every human-vs-model gap and every κ/ARI/ρ; drop rank-based claims that do not survive. Negligible compute.

### W3: "Human performance" is not defined; one annotator carries ten of 26 pairs
The paper never says how two annotators' labels become one human score (mean of individual scores, consensus, or one annotator). The numbers are consistent with micro-averaging (Emotion 45.8% = 44/96 over 96 annotations), but see ERR-4 below for a case that does not fit. All non-English results, including the headline "humans beat models" in Arabic and Russian, come from one annotator on 30–40 items (App. D.1: "Single annotator (no agreement metrics)"). §3.3 says annotators had native or near-native proficiency in the evaluated languages while §5.3 says three annotators participated overall for five languages. Annotator idiosyncrasy and "cultural knowledge" (§4.2) cannot be separated.
- **Suggested Fix**: Define the aggregation; report per-annotator scores; add a second annotator for at least Arabic STS22 and the three sentiment subsets (about 4 tasks × 40 items).

### W4: One pooled number mixes metrics and is mostly English; section averages are English-only
The overall 77.6 averages accuracy, MAP, V-measure and Spearman×100 over 26 pairs, 16 of them English. These metrics have different chance levels. The per-category averages in §4.1 ("Human performance averages 70.3 across classification tasks") equal the English-only means (recomputed: (45.8+77.5+84.4+73.3)/4 = 70.25; over all seven classification pairs the mean is 79.1; clustering 67.4 English vs 68.0 all; STS 83.2 English vs 76.5 all). The text presents them as category averages.
- **Suggested Fix**: Report chance-corrected or normalized scores, macro-average by language group, and label every average with the pairs it covers.

### W5: The central interpretive claim ("models exploit patterns where humans disagree") is never tested
§5.1 itself says "the mechanisms behind this inverse relationship remain unclear", while the Conclusion says the pattern suggests "models exploit patterns rather than achieving true semantic understanding". No correlation between agreement and gap is computed. The agreement statistics (κ, ARI, ρ) are on different scales and for most tasks cover English subsets only. The data also include counter-cases: reranking has the highest agreement (ρ 0.64–0.85) and still shows a 9-point model advantage (87.2 vs 96.4), and STS12 (ρ = 0.77) shows none.
- **Suggested Fix**: Compute a rank correlation (with bootstrap interval) between a common-scale agreement measure and the gap; test an alternative (in-domain training exposure of the models); soften the conclusion to "consistent with".

### W6: Several numbers in the paper contradict each other (Error Log below)
The Emotion example in §4.3 uses a best-model score (87.1) that is not the best model on Emotion in Table 4 (75.4), and five agreement values in the appendix figures differ from Appendix D. Because agreement values are the independent variable of the central thesis, these need to be fixed and re-checked.
- **Suggested Fix**: Single source of truth for all statistics, generated from the evaluation script.

### W7: Reproducibility gaps on the human side
The text of the annotation guidelines is not given (only screenshots, App. B), nor is the item-sampling procedure ("principled dataset sampling", §3.1) or the amount of time and pay per annotator. The subsets are said to ship in the MTEB package (§3.3) and a code/data link is mentioned (Abstract; link removed, so unverified), which partly offsets this.
- **Suggested Fix**: Add guidelines, sampling seed and procedure, annotator time per task, and the MTEB version and commit.

**Minor:** Table 2 caption says humans are top in "5 of 14" pairs; the table shows 4 (Arabic, Norwegian and Russian sentiment, Arabic STS), matching Fig. 13 ("only 4 tasks"). STS22-Russian human score is 58.7 in Table 2 and §4 but 58.5 in App. C.1.1 and Fig. 15. Fig. 2's caption says "16 tasks" for 26 rows.

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Generalizable framework for human evaluation | §1, §3.1 | Interfaces (App. B), metrics (§3.2), four task types | Partially: described, but protocols not matched to MTEB and not tested beyond four task types |
| C2 | Humans 77.6 vs 80.1, rank 4 | Abstract, Table 2, Fig. 1 | Table 2, Tables 3–6 | Partially: values reproduce from the tables (recomputed 77.64), but n is tiny and no uncertainty |
| C3a | Models look superhuman where agreement is low | §4.3, §5.1, §6 | Appendix D, Table 4 | Unsupported as a mechanism; the correlation is not quantified |
| C3b | Humans beat models in non-English sentiment and Arabic STS | §4.2, §5.1 | Table 2 | Supported as a descriptive result (4 pairs, one annotator each); the cultural-knowledge explanation is untested |
| C3c | Specific MTEB datasets should be replaced | §5.2 | App. C | Partially: Emotion and ArXiv by argument; STS22-Russian rests on a single annotator (ERR-7) |

### Protocol sweep (Step 0)
Searched the full text for split, selection and tuning statements. There is no model training, tuning or checkpoint selection in the paper. Statements found: "All models are evaluated on the downsampled instances annotated by humans" (§3.4) and "The downsampled task subsets used for comparisons are included in the MTEB package" (§3.3). Which MTEB split the items were drawn from (train or test) is **not stated after search**. No selection on a reported held-out set is described.

### Omission sweep
| Item | Status |
|------|--------|
| Splits / tuning split | Source split of the subsets not stated after search; no tuning described |
| Seeds, runs, variance | Not stated after search (no CI, bootstrap, or standard error) |
| Baseline (model) settings | Not stated after search: instruction prompts, classifier training data, k for clustering |
| Hyperparameters | N/A for humans; model-side not stated |
| Compute | Not stated (not central) |
| Licence, consent, personal data | Not stated after search for annotator consent/pay; dataset licences not stated |
| Failure cases / limitations | Present (§5.3) |
| Code / data availability | Claimed (Abstract), link removed; subsets said to be in the MTEB package (§3.3) |

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | §4.3 vs Table 4 vs Fig. 13 | "(87.1% vs. 45.8% human)" | Table 4 gives the best Emotion model as 75.4 (jasper); Fig. 13 gap is −29.6 = 45.8 − 75.4. 87.1 is the best English classification *average* (§4.1, Table 2). The same 87.1 appears in Fig. 4 and App. D.1.1 | Cross-referenced Table 4, Fig. 13, §4.1; recomputed | High | MAJOR | Use 75.4; re-check all "best model" values in App. B/D |
| ERR-7 | E3 / E6 | App. C.1.1, §5.2 vs App. D.1.4 | "may help explain the comparatively low human agreement we observed" | App. D.1.4 says STS22 Arabic and Russian have a "Single annotator (no agreement metrics)"; no agreement was observed for Russian, yet STS22-Russian is recommended for replacement (§5.2) | Cross-referenced two locations | High | MAJOR | Remove the agreement claim for Russian or add a second annotator |
| ERR-8 | E6 | §4.3, §5.1 vs App. D.2 | "Tasks with high human agreement (κ > 0.6 or ρ > 0.7)" | Toxicity (κ = 0.55) is presented as a high-agreement "reliable benchmark" (§4.3, §5.1), below this threshold; STSBenchmark (ρ = 0.58, "moderate" in D.1.4) is listed as high-agreement in D.2.1 and would be low under D.2.2's "ρ < 0.6" | Recomputed against the paper's own thresholds | High | MAJOR | Apply one rule to all tasks and re-derive the "reliable" and "problematic" lists |
| ERR-3 | E6 | App. B captions vs App. D.1 | "This task achieved fair agreement (ARI = 0.34)" | Reddit ARI is 0.42 in D.1.2; Tweet κ 0.48 (Fig. 5) vs 0.41 (D.1.1); SICK-R ρ 0.68 (Fig. 12) vs 0.63 (D.1.4); SIB200 ARI 0.42 (Fig. 8) vs English 0.15 (D.1.2); Robust04 ρ 0.72 (Fig. 9) vs 0.75 (D.1.3) | Cross-referenced | High | MAJOR (central variable) | Regenerate captions from one table |
| ERR-4 | E1 / E8 | App. D.1.1 vs Table 4 | "Mean percentage agreement: 62.2%" | For Tweet Sentiment, two annotators with mean accuracy 84.4% vs gold must agree on at least 2×0.844 − 1 = 68.8% of items. Reported agreement 62.2% (28/45) is below that bound, so the human score is not the mean of the two annotators' accuracies, or the figures come from different item sets | Derived; assumes both annotators labelled the same 45 items | Medium | MAJOR | State how the human score is formed; recompute |
| ERR-5 | E6 / E5 | §4.1 | "Human performance averages 70.3 across classification tasks" | Equals the English-only mean; all seven classification pairs give 79.1 | Recomputed from Table 2 / Fig. 15 | High | MINOR | Label averages by coverage |
| ERR-2 | E1 | Table 2 caption | "Humans achieve top performance in 5 of 14 aggregated task-language pairs" | Table 2 shows human above all models in 4 pairs; Fig. 13 says 4 tasks | Counted column by column | High | MINOR | Correct to 4 |

---

## Missing References
*(Domain Reviewer's job; none added here.)*

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Derived value is 1 (avg of rigor and validation = 42); raised one step because the per-task human data are real and usable |
| Clarity | 3 | Clear prose; inconsistent counts and captions |
| Significance | 2 | Useful if made reliable; current conclusions not supported |
| Originality | 2 | New measurement, no new method |

---

## Dimension Scores (0–100)

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison rests on unmatched protocols and 20–50 items with no uncertainty (W1, W2), and the main interpretive claim is untested (W5).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 44 | Developing | Unmatched protocols, undefined human score, internal numeric contradictions |
| Clarity & Presentation | 62 | Competent | Readable; counts and captions conflict |
| Novelty & Originality | 52 | Developing | Measurement novelty only |
| Significance & Impact | 55 | Competent | Community interest is real; reliability limits impact |
| Experimental Validation | 40 | Developing | No uncertainty, 1 annotator for non-English, small n |
| Reproducibility | 55 | Competent | Subsets released; guidelines, sampling, model-side protocol missing |
| Ethical Compliance | 50 | Developing | No statement on annotator pay or consent; limitations discussed |

---

## Questions for Authors
1. How is each task's "human performance" computed from two annotators, and how does Tweet Sentiment give 84.4% accuracy with 62.2% pairwise agreement? A consistent definition would remove ERR-4 and raise my confidence in the tables.
2. For classification and clustering, what did the MTEB-side protocol use (training examples, number of clusters, prompts)? If humans and models were matched, I would raise Technical Rigor by about 10 points.
3. What are the bootstrap intervals for the overall 77.6, the rank, and the main gaps? If the rank claims do not survive, I would expect the text to say so.
4. Which split of each dataset were the items drawn from, and how (random seed, stratification)?
5. Can a second annotator be added for Arabic STS22 and the three sentiment subsets? That is the cheapest way to support the headline human advantage.

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially.

§5.3 acknowledges sample size and annotator pool. It does not discuss the unmatched protocols, the single-annotator non-English results, or the lack of uncertainty, and it still states that "decisions on evaluation datasets can be made from even a few samples".

---

## Ethics Review Flag

**No**: no serious concern, but a statement on annotator compensation, consent, and exposure to toxic text (Toxicity dataset) is missing.

---

## Overall Score

**2**: Reject. The data are worth releasing, but the comparison is not protocol-matched, has no uncertainty on 20–50 items, and the paper's main conclusions (mechanism, dataset replacement, cultural advantage) are stronger than its evidence.

## Confidence

**4**: Confident. I recomputed the tables; I could not see the figures or the code.

---
---

# Peer Review Report

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Reviewer: Dr. Mireille Duquesnoy, Reviewer 2 (Domain) (public research institute, Western Europe; fictional persona)
## Expertise: text embedding models; MTEB-style benchmarks; relevance assessment
## Date: 2026-11-10

---

## Summary
HUME measures how well annotators do on downsampled MTEB tasks and sets this against 13 embedding models. The authors report that humans sit in the middle of the model range, that models are strongest where humans disagree, and that some datasets (Emotion, ArXiv clustering, STS22-Russian) should be replaced. The question is a good one for the embedding community, which has relied on leaderboards with no human reference. My concerns are with how the work is positioned against prior literature on human baselines and label noise, with the support for the dataset-quality claims, and with model coverage.

---

## Strengths

### S1: A real gap in the MTEB ecosystem
MTEB and MMTEB (§2.1) provide no human reference, as the paper says. Putting humans and 13 models on identical instances (§3.4, Table 2) answers a question practitioners ask ("is 0.85 MAP good?", §1).

### S2: Sensible choice of task categories and languages
Sixteen datasets across reranking, classification, clustering and STS, with high- and low-resource languages (§3.2), gives breadth that a single-task study would lack.

### S3: Dataset diagnostics are a useful use of human baselines
Using a human pass to flag problematic gold labels (e.g., the Emotion examples in §4.3 and App. C.1.3) is a practical idea that benchmark maintainers can adopt, even if the specific recommendations need more evidence.

---

## Weaknesses

### W1: Related work does not engage with the literature on human baselines, "superhuman" claims and label noise
§2.2 treats TREC as "gold standards rather than benchmarks of human performance". The IR evaluation literature has studied assessor disagreement and its effect on system rankings directly (e.g., Voorhees, 2000 [verify]). Critiques of human-vs-model comparisons and of "superhuman" claims on NLU benchmarks exist (Tedeschi et al., ACL 2023, a position paper that takes a critical look at claims of superhuman performance on benchmarks such as SuperGLUE and SQuAD), as do studies of label errors in widely used test sets (Northcutt et al., NeurIPS 2021 Datasets & Benchmarks, which estimates at least 3.3% label errors on average across 10 common datasets). The paper cites Plank (2022) on label variation but not the learning-from-disagreement literature. Without these, the paper's central argument (low agreement ⇒ dataset problem; high model score ⇒ pattern matching) is presented as new where it is a known line of discussion.
- **Suggested Fix**: Add a related-work paragraph on assessor agreement in IR, superhuman-performance critiques, and label-noise audits, and state what is new relative to them (the MTEB-specific multilingual human scores).

### W2: The dataset-quality conclusions go beyond the evidence and are partly inconsistent
(a) STS22-Russian is recommended for replacement (§5.2) on the basis of "systematic parsing artifacts", but no agreement was measured for Russian (single annotator, App. D.1.4) and the "context expansion" example in App. C.1.1 is a generic pattern ("Company reports earnings" vs …), not an item from the data. (b) The Russian sentiment dataset is described as containing neutral press releases that are "difficult to categorize" (App. C.1.2), yet the human score on it is 92.5, the second highest in Table 2, and §5.1 uses the same pair as evidence of "genuine model limitations in cross-cultural understanding". Both cannot hold without an explanation. (c) For ArXiv clustering the gold label is the paper's arXiv category chosen by its submitters; disagreement among two readers of 30 titles shows the categories are fuzzy at the boundary, but a model that predicts submitters' conventions is solving the task as defined. "Models reproduce label patterns" is not by itself a flaw.
- **Suggested Fix**: Report item-level evidence (a table of disagreeing items with gold and annotator labels) for each dataset flagged; restrict "replace" to cases with measured low agreement on at least two annotators; reconcile the Russian sentiment narrative.

### W3: Model coverage is narrow for "best model" and rank claims
Thirteen models (Table 7) include older English-only encoders (all-MiniLM-L6-v2, all-mpnet-base-v2) and the best overall model is an English vision-language variant (jasper_en_vision_language_v1). Strong multilingual systems available before the cutoff are absent: for example, larger Qwen3-Embedding variants from the same report the paper cites (Zhang et al., 2025b; only the 0.6B model is used), Gemini Embedding (Lee et al., 2025), and M3-Embedding (Chen et al., 2024). The statements "humans rank 4th" and "80.1 for the best embedding model" (Abstract) therefore depend on the model sample, and Fig. 3's "100% against the mean" for non-English languages is driven by English-only models in the pool.
- **Suggested Fix**: Add two or three of the strongest multilingual models, report win rates against the multilingual-capable subset only, and word the abstract as "among the 13 evaluated models".

### W4: The "cultural knowledge" explanation is asserted
§4.2 attributes the Arabic and Russian advantage to "cultural and contextual knowledge that models fail to capture". This is a plausible hypothesis, but the study has no test of it (no item-level analysis, no non-native annotator control, one native annotator per language). Alternatives include annotation-protocol artifacts (humans labelling binary sentiment with no training set vs. models with a classifier on top), dataset provenance (news vs tweets), and the weakness of the English-only models in the pool.
- **Suggested Fix**: Treat as a hypothesis; add an item-level error analysis for Arabic STS22 and the sentiment subsets.

### W5: Domain framing of the contribution: "framework" is thin
C1 is a "generalizable framework" (§1, §3.1), but what is described is a set of annotation interfaces, a sampling choice and a metric list. No procedure is given for adding a new task type or for guideline design, and no new task is demonstrated.
- **Suggested Fix**: Present the paper as a measurement study with a released resource, or add a procedure and demonstrate it on a task outside the four categories (e.g., retrieval with graded relevance or pair classification).

**Minor:** Related work lists MTEB variants (§2.1) without saying which already include some human validation; the Emotion label provenance is not described in the paper (as I recall, labels derive from hashtags: a question for the authors, [verify]).

### Novelty delta table (literature check)
| Claimed contribution | Closest prior work | What that work already does | What is actually new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|---------------------------|---------------------------|
| C1 framework | MMTEB (arXiv 2502.13595, v4; peer-reviewed label) | Broad multilingual embedding benchmark, no human baselines | Human annotation interfaces and aligned scoring on a subset | Cited (§2.1); differentiated by the missing human baseline |
| C2 human scores | none found in 5 queries (arXiv only) | n/a | First reported human scores on MTEB-style tasks, as far as I can tell | n/a |
| C3 superhuman / label quality | Tedeschi et al. 2023 (arXiv 2305.08414, ACL 2023); Northcutt et al. 2021 (arXiv 2103.14749, NeurIPS D&B 2021) | Critiques of human-vs-model comparisons; audits of label errors in test sets | MTEB-specific human agreement and the proposal of an agreement-weighted reading | Not cited |

### Per-claim novelty (claim-level profile; `related_search.py novelty`)
| Claim | Dimension | Novelty | Top prior work | Reasoning |
|-------|-----------|---------|----------------|-----------|
| C1 | resource | high (script) | MMTEB, level 2 | Related benchmark, no human protocol; the framework itself is thin (W5) |
| C2 | result | no close prior work found in 5 results sets (at most medium) | none | Search covers arXiv only; the human score table is new to me |
| C3 | result | medium | Tedeschi et al., level 3 | The argument that "superhuman" claims need scrutiny exists; the MTEB-specific evidence is new |

No claim is established by an uncited prior work at level 5, so this is not a "known results" case. Closest prior work as a whole (script attribution): Tedeschi et al. 2023, for the framing; MMTEB for the setting.

### Field snapshot
Around 2020–2022 the standard embedding evaluations were STS and BEIR/MTEB-style task suites. Since 2023, LLM-based embedders (7B-scale decoders) topped MTEB, and MMTEB (2025) extended it to 250+ languages. Open problems stated by recent work include benchmark saturation, label noise and contamination, and fair comparison across instruction-tuned and non-instruction models. In this sub-field, a significant evaluation contribution now needs (i) a measurement that changes how scores are read, with uncertainty, and (ii) a method others can apply. A new leaderboard-style number alone is incremental. I use this to place Significance in the 55–60 range: the question is important, the evidence is preliminary.

## Missing References

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Simone Tedeschi, Johan Bos, Thierry Declerck, Jan Hajic, Daniel Hershcovich, Eduard Hovy et al. "What's the Meaning of Superhuman Performance in Today's NLU?" ACL 2023 (arXiv 2305.08414, verified) | Critical look at claims of superhuman performance; directly relevant to §4.3–§5 |
| Important | Curtis G. Northcutt, Anish Athalye, Jonas Mueller. "Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks." NeurIPS 2021 Datasets & Benchmarks (arXiv 2103.14749, verified) | Prior audit of label errors and their effect on benchmark rankings; relevant to the dataset-quality claims |
| Important | Ellen M. Voorhees. "Variations in relevance judgments and the measurement of retrieval effectiveness." Information Processing & Management, 2000 [verify] | Measured assessor disagreement and its effect on system rankings in IR evaluation |
| Important | Alexandra Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, Massimo Poesio. "Learning from Disagreement: A Survey." JAIR, 2021 [verify] | Frames annotator disagreement as signal, relevant to treating low agreement as "bad task" |
| Helpful | Jinhyuk Lee et al. "Gemini Embedding: Generalizable Embeddings from Gemini." arXiv 2025 (arXiv 2503.07891, verified; arXiv-only, prior) | Strong multilingual embedder before the cutoff; model coverage |
| Helpful | Jianlv Chen et al. "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation." Findings of ACL 2024 (arXiv 2402.03216, verified) | Strong multilingual embedder; model coverage |

*Literature check was run (strict, cutoff 2025-09-24, 5 queries). Only prior works are listed; none is a required comparison, none is a recent preprint.*

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea; evidence too thin for the conclusions |
| Clarity | 3 | Clear writing |
| Significance | 2 | Interesting but conclusions overreach |
| Originality | 2 | New measurement; framing known in other literatures |

---

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful and apparently first measurement (pushes up) with thin evidence for dataset-quality and cultural-advantage claims and weak positioning against prior critiques (pushes down).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Dataset-quality inferences inconsistent (W2) |
| Clarity & Presentation | 64 | Competent | Clear, well organised |
| Novelty & Originality | 55 | Competent | First measurement of its kind as far as found; no method novelty |
| Significance & Impact | 58 | Competent | Relevant to the MTEB community |
| Experimental Validation | 48 | Developing | Narrow model set, tiny samples |
| Reproducibility | 58 | Competent | Subsets released; protocols partly missing |
| Ethical Compliance | 52 | Developing | No annotator-welfare statement |

---

## Questions for Authors
1. How do you reconcile the description of the Russian sentiment dataset as ambiguous (App. C.1.2) with a human score of 92.5 and its use as evidence of model limitations (§5.1)? An explanation would raise my Technical Rigor score.
2. Do the dataset-quality recommendations (§5.2) hold if only tasks with two annotators are considered? If Emotion and ArXiv still stand, I would be more convinced.
3. Which of the 13 models were trained on in-domain training splits of the MTEB tasks used here (the MTEB leaderboard tracks a zero-shot share)? This is an alternative to "pattern matching" that should be discussed.
4. What would the ranking look like with the strongest multilingual models added?

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially. The sample-size and annotator-pool limits are acknowledged (§5.3); model coverage, unmatched protocols and untested explanations are not.

---

## Ethics Review Flag

**No**: no flag; see Reviewer 3 for annotator-welfare points.

---

## Overall Score

**3**: Borderline Reject. A relevant first measurement, but the dataset-quality and cultural claims outrun the evidence and the related work misses directly relevant critiques.

## Confidence

**4**: Confident on the embedding side; the IR and label-noise references are from memory where marked [verify].

---
---

# Peer Review Report

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Reviewer: Dr. Selim Barakzai, Reviewer 3 (Perspective) (psychology and measurement department, university, Middle East; fictional persona)
## Expertise: psychometrics; inter-rater reliability; crowdsourcing ethics
## Date: 2026-11-10

---

## Summary
The paper asks how well humans do on the tasks that embedding benchmarks use to score models, and uses the answer to read model scores and to question some datasets. From a measurement perspective this is the right instinct: a score without a reference population is hard to interpret. The execution is a pilot, with a few annotators and a few dozen items per task. The paper's most valuable output is the pairing of human performance with human agreement per task, which could change how benchmark scores are reported.

---

## Strengths

### S1: Reframes benchmark scores relative to human reference points
§1 and §5.2 argue that a score such as 0.85 means different things at different agreement levels ("Consider Agreement-Weighted Evaluation"). This is how reliability enters psychometrics, and it is a constructive proposal for ML benchmarks.

### S2: Agreement statistics and chance correction for classification
Fleiss' κ (§3.3) and the κ bands in App. D give readers a chance-corrected view for classification, which is better than raw accuracy alone.

### S3: Practical diagnostic for benchmark maintainers
Task-level lists of low-agreement datasets (Emotion, ArXiv) give maintainers something to inspect, as a screening step rather than a verdict.

### S4: Transparent about annotator demographics
§3.3 reports that all annotators were male, aged 20–35 and experienced in NLP. Reporting this allows readers to judge representativeness.

---

## Weaknesses

### W1: The notion of "human performance" needs a definition and a reference population
Human scores here come from three NLP-experienced young men (§3.3, §5.3) with a different mix of tasks each, scored against gold labels that may themselves be one rater's judgment. In measurement terms, the paper reports accuracy of individuals against a criterion without reporting between-annotator variance, or an estimate of the ceiling that annotator-to-annotator agreement implies (the "noise ceiling" idea used in neuroscience and psychometrics). Without it, "humans rank 4th" has no stable meaning.
- **Suggested Fix**: Report the inter-annotator ceiling (e.g., one annotator against the other) next to the human-vs-gold score, with bootstrap intervals; use Krippendorff's α or a common scale so agreement can be compared across task types.

### W2: Agreement values from different statistics are compared as if they were one scale
κ, ARI, Spearman ρ and Kendall τ are used to sort tasks into "high" and "low" agreement (App. D.2, thresholds κ > 0.6 or ρ > 0.7), but these are not commensurable (ARI depends on the number of clusters annotators choose; ρ on ties in a 0–5 scale). With 30–50 items the intervals are wide.
- **Suggested Fix**: Use a single reliability coefficient family (e.g., Krippendorff's α with the appropriate distance for each level of measurement), and report intervals.

### W3: Low agreement is treated as a defect of the task; it may be valid subjectivity
§4.3 and §5.2 read low agreement as "ambiguous annotation guidelines or inherently subjective judgments" and then as a reason to replace the dataset. Emotion and topic labels are inherently multi-label for some items; treating disagreement as signal (perspectivist approaches in annotation research) is an alternative that supports reporting, not removal. A recommendation to drop datasets should come with a test that a better-specified version of the task yields higher agreement.
- **Suggested Fix**: Pilot revised guidelines (e.g., multi-label or "primary category" instructions) on 30 ArXiv items and report whether agreement moves.

### W4: Annotator welfare, consent and compensation are not described
The study has human participants and one dataset with toxic content (Toxicity; Table 1), plus social-media and Reddit text. The paper does not say whether the annotators were authors, paid, informed of the use of their labels, or protected from distressing material, and it has no ethics statement. The all-male, 20–35 panel is acknowledged (§3.3) but not discussed as a limitation of the "human" in "human performance", especially for claims about cultural knowledge and sentiment.
- **Suggested Fix**: Add a short statement: who annotated, compensation, consent for publishing labels, content warnings, and a limitation on panel diversity.

### W5: Practical interpretation for model builders is premature
§5.2 advises developers under the heading "Prioritize High-Agreement Tasks for Development" and calls for "architectural innovations" for cultural gaps. These recommendations rest on 4 non-English pairs with one annotator each. For deployment, the more immediate use is to treat the human numbers as a rough sanity range per task, not as design guidance.
- **Suggested Fix**: Soften §5.2 to hypotheses; add the measurement caveats from W1–W2.

### Cross-disciplinary connections
- **Psychometrics / item response theory:** fit an IRT model across items to separate item difficulty from annotator and model ability; this would make the "model superhuman where humans disagree" claim directly testable on the existing data.
- **IR evaluation:** assessor-agreement studies and pooled judgments can calibrate the reranking results.
- **Annotation research (perspectivism):** treat disagreement as information.
- **Crowdsourcing ethics (HCI):** pay, consent and wellbeing protocols for text-labelling work.

### Fundamental assumption audit
1. *A human score is a capability ceiling or reference*: the paper itself notes "humans neither represent a performance ceiling nor a lower bound" (§4); the assumption then needs care when used for model comparison.
2. *Gold labels define correct semantic understanding*: the paper uses disagreement with gold as evidence of label flaws on some datasets and as evidence of cultural advantage on others, which are different readings of the same signal.
3. *30–50 items represent a dataset*: the paper says "decisions on evaluation datasets can be made from even a few samples" (§5.3); with this n, dataset-level conclusions are provisional.

### Future directions
Add graded-relevance retrieval and pair classification; recruit non-expert and expert pools to measure the effect of expertise; release item-level annotations; run IRT.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Pilot-scale evidence; measurement concepts underspecified |
| Clarity | 3 | Clear |
| Significance | 3 | Potentially useful reframing of benchmark scores |
| Originality | 3 | New use of human reference in embedding evaluation |

---

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting, useful question with a concrete deliverable (agreement-aware reporting) puts it above the median; pilot-scale evidence keeps it below a solid accepted paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Measurement concepts underspecified, no intervals |
| Clarity & Presentation | 70 | Competent | Readable |
| Novelty & Originality | 62 | Competent | New angle for the embedding community |
| Significance & Impact | 68 | Competent | Reframes how scores are interpreted |
| Experimental Validation | 55 | Competent | Small samples but a broad task set |
| Reproducibility | 62 | Competent | Subsets released |
| Ethical Compliance | 55 | Competent | Demographics disclosed; welfare, pay, consent missing |

---

## Questions for Authors
1. Were the annotators authors, and were they compensated? Clarity here would settle my ethics concern.
2. What is the inter-annotator ceiling per task, expressed in the same metric as the model scores? If it is reported with intervals, I would raise my Technical Rigor score.
3. Would revised guidelines raise agreement on ArXiv or Emotion? A positive answer would support the "task design" reading over the "valid subjectivity" reading.

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially. Sample size and panel are acknowledged; ethics and measurement limits are not.

---

## Ethics Review Flag

**No**: the study uses text from public datasets and its own annotators. The missing items (compensation, consent, content warning) should be added but do not by themselves call for ethics review.

---

## Overall Score

**4**: Borderline Accept. An interesting question and a constructive proposal for agreement-aware reporting; the pilot-scale evidence is the main gap, and I would want it labelled as a pilot.

## Confidence

**3**: Fairly confident; outside my core area of embedding models.

---
---

# Peer Review Report

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Reviewer: Dr. Priya Raghunathan-Beck, Reviewer 4 (Generalist) (industrial research lab, South Asia; fictional persona)
## Expertise: representation learning; general ML
## Date: 2026-11-10

---

## Summary
The paper builds a human annotation setup on 16 MTEB datasets, measures human performance on small subsets, and compares it with 13 embedding models. Humans average 77.6 versus 80.1 for the best model; humans do better than models on Arabic semantic similarity and on non-English sentiment; models do best where humans agree least; and several datasets are argued to be unreliable. The authors release code, data and a leaderboard (link removed). The paper wants to change how embedding benchmark scores are interpreted.

**Contribution in one paragraph (my words).** A first human reference for a popular embedding benchmark, plus an argument that benchmark scores should be read with task reliability in mind. The reference exists; the argument is plausible but not established by the evidence given.

---

## Strengths

### S1: A question the community cares about
MTEB is the default embedding benchmark (§2.1). A human reference answers "is this score good?" (§1) and could be used by many groups.

### S2: Clearly written and well organized
The main text is short and readable; Table 2 gives a one-glance comparison of humans and all models, and the appendix carries per-dataset tables (Tables 3–6) and agreement values (App. D).

### S3: Concrete, shareable resource
The downsampled subsets are said to be in the MTEB package (§3.3) and code, data and leaderboard are announced. Resources like this get reused.

### S4: Limitations section is candid
§5.3 acknowledges the small sample, the limited annotator pool and the lack of specialized annotators.

---

## Weaknesses

### W1: Conclusions are stated more strongly than the evidence allows
Examples: "Our analysis reveals systematic quality issues in several MTEB datasets" that the paper says fundamentally compromise their reliability as benchmarks (§4.3); datasets "should be replaced in future MTEB iterations" (§5.2); "decisions on evaluation datasets can be made from even a few samples" (§5.3); the conclusion says models "exploit patterns rather than achieving true semantic understanding". These rest on 30–48 items per dataset and 1–2 annotators. §5.1 itself admits the mechanisms are unclear. At ICLR a benchmark/analysis paper is expected to have conclusions that follow from the numbers.
- **Suggested Fix**: Frame the work as a pilot study; replace "should be replaced" with "warrant re-examination"; remove the causal wording unless tested.

### W2: Counts and labels are inconsistent, which makes the headline harder to follow
The paper says 16 datasets, 26 task-language pairs (Table 2), 14 aggregated columns ("5 of 14", Table 2 caption), "16 tasks" for a figure with 26 rows (Fig. 2 caption), and "13 state-of-the-art" models including 2021-era encoders. The Table 2 caption says humans are top in 5 pairs; the table shows 4, as does Fig. 13. A reader trying to verify the headline has to re-derive which average covers what (§4.1 category averages are English-only).
- **Suggested Fix**: One counting convention; state in each caption which pairs are averaged.

### W3: Headline presentation hides the uncertainty and mixes metrics
The abstract's "77.6% compared to 80.1%" averages different metrics, with no intervals, from small samples. The "4th place" framing in Fig. 1 suggests a precision the data do not have.
- **Suggested Fix**: Show intervals in Fig. 1 and Table 2 and put a one-sentence caveat in the abstract.

### W4: Scope of the "framework" claim
"A generalizable framework" (C1) is asserted; §3.2 says the "systematic selection ensures our findings generalize across the diverse landscape of embedding applications". With four task types, five languages and no new task demonstrated, this wording is not supported.
- **Suggested Fix**: Say "a protocol and resource for four task types".

**Minor:** The appendix is long relative to the body and carries several statistics that differ from the main text (see Reviewer 1's log). Some captions use "%" for Spearman correlations.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly: descriptive results ok; interpretive claims not | §4.3, §5 |
| Soundness: fair, reproducible protocol | Partly: subsets released; model-side protocol missing | §3.3–§3.4 |
| Presentation: clear and consistent | Partly: clear prose; counts and statistics inconsistent | Table 2, Fig. 2, App. B vs D |
| Contribution: new insight for the community | Met in part: first human reference; mechanism untested | §4, §5 |
| Limitations honestly stated | Partly met | §5.3 |

### Balanced judgment
- *What would the community lose if rejected?* The human numbers and the idea of agreement-aware reporting; both can reappear after a stronger study.
- *Are these weaknesses typical of accepted ICLR papers?* Small samples and overclaiming are common in accepted papers, but here the sample is the entire evidence for the paper's main claims, and the paper has no variance estimate at all; that is more than the usual single-seed caveat.
- *Three changes that would help most:* uncertainty estimates; a matched-protocol check; toning down the dataset-replacement claims.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea, thin evidence |
| Clarity | 3 | Clear, with inconsistent counts |
| Significance | 3 | Useful reference if made reliable |
| Originality | 2 | New measurement, no new method |

---

## Dimension Scores (0–100)

**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear question and a usable resource, held back by tiny samples and conclusions beyond the data; this looks like a typical rejected submission with a solid core.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | No uncertainty; interpretive leaps |
| Clarity & Presentation | 66 | Competent | Clear prose, inconsistent counts |
| Novelty & Originality | 56 | Competent | New measurement |
| Significance & Impact | 60 | Competent | Relevant to the embedding community |
| Experimental Validation | 50 | Developing | Small subsets; narrow annotator pool |
| Reproducibility | 58 | Competent | Subsets released |
| Ethical Compliance | 52 | Developing | No ethics statement |

---

## Questions for Authors
1. Can you add intervals to Table 2 and Fig. 1? If the 4th place claim becomes "within the top group", I would be comfortable.
2. Are you willing to reword §5.2 as recommendations to re-examine rather than replace? That would address my main concern.
3. What would convince you that "pattern matching" is wrong for ArXiv clustering (e.g., a model that predicts submitters' categories legitimately)?

---

## Limitations Assessment

**Have the authors adequately addressed limitations?** Partially (§5.3 is candid about sample size but contradicts itself with "decisions ... can be made from even a few samples").

---

## Ethics Review Flag

**No**: no concern that needs ethics review; an ethics/annotator statement would be good practice.

---

## Overall Score

**3**: Borderline Reject. Good question and a useful resource, but the evidence does not support the conclusions as worded; a restructured pilot-study framing with uncertainty could be accepted.

## Confidence

**3**: Fairly confident; I did not recompute every table.

---
---

# Devil's Advocate Report

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Reviewer: Prof. Joaquín Medrano-Lindqvist, Devil's Advocate (university statistics and ML group, Latin America; fictional persona)

---

## Steelman
No one had measured how humans do on MTEB-style tasks. The authors do so on identical instances across four task types and five languages, find humans competitive with but not above the best models, and observe that the largest model advantages occur on datasets whose labels are contested. That observation is a legitimate prompt for benchmark maintainers to look again at those datasets.

---

## Core Argument Chain
1. Human annotators on 20–50 items per dataset score on average 77.6; the best of 13 models scores 80.1 (Table 2).
2. Both are measured under "identical metrics, protocols, and computational settings" (§3.4).
3. Models' advantage is largest where human agreement is lowest (§4.3, §5.1).
4. Therefore models achieve "superhuman" performance by reproducing label patterns, not by understanding (§4.3, §6).
5. Therefore low-agreement datasets (Emotion, ArXiv, STS22-Russian) are unreliable and should be replaced (§5.2).
6. Humans' advantage in Arabic and Russian reflects cultural knowledge models lack (§4.2, §5.1).
∴ Embedding benchmark scores must be interpreted in light of human agreement, and MTEB needs human-validated task design.

---

## Strongest Counter-Argument
The comparison that drives every conclusion, human vs model, is not a comparison of like with like, and the samples are too small to let the gap say anything about mechanism. On the human side, annotators see no labelled data ("without access to ground truth", §3.3), choose their own clusters ("free assignment of cluster IDs"), and make binary relevance calls. On the model side, MTEB tasks are run with whatever the benchmark's default protocol is, which for classification includes a classifier fitted on labelled training examples, for clustering fixes the number of clusters, and for instruction-tuned models may include task instructions. The paper does not describe any of this, so the 2.5-point gap (and each per-task gap) mixes "understanding" with "got to see the labelled examples and the answer-format". On the largest gaps (Emotion, Reddit, ArXiv, all classification and clustering) this is exactly the asymmetry that favours the model.

The interpretation then adds a second step the data cannot support. "Models are strongest where humans agree least" is read as "models exploit annotation artifacts". But a model that sees thousands of labelled examples of a contested labelling scheme, possibly including the dataset's own training split, will naturally predict the scheme's conventions better than a person who sees none. That is not evidence of a flawed dataset; it is what a supervised measurement does, and it applies equally to a well-specified dataset. In ArXiv clustering the gold label is the submitters' own category; predicting it is the task, and two readers disagreeing on 30 titles is a statement about reader knowledge. The paper never quantifies the relation (no correlation, no interval), it uses κ, ARI and ρ interchangeably, it contains counter-cases (reranking has high agreement and a 9-point model lead), and §5.1 concedes that "the mechanisms behind this inverse relationship remain unclear" before §5.2 and the Conclusion proceed to recommend replacing datasets. The cultural-knowledge story has the same shape: single annotators, 30–40 items, English-only models in the pool, and a Russian sentiment dataset that Appendix C.1.2 calls ambiguous but on which humans score 92.5.

A fair reading is a descriptive pilot with a promising idea. The paper claims a diagnosis.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The human scores are measured and reproduce from the tables, so the main descriptive claim stands, and the interpretive claims are not contradicted by the data; they are unsupported as worded. The fix is narrowing the claims and adding controls, which makes these MAJOR.

*Applied the criteria: not 1 (evidence does not contradict the headline); not 2 (the human and model scores are measured; the causal reading is a secondary interpretation the authors partly hedge in §5.1, and a missing control is MAJOR); not 3 (no tuning or selection on a reported held-out set is described; protocol sweep found none); not 4–7.*

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | §3.3–§3.4, §4 | Human and model protocols are not matched (no labelled examples for humans; free clusters; binary relevance) and the model-side protocol is undocumented, yet §3.4 asserts "identical" protocols. "Evidence supports a weaker claim" (humans and models differ under their respective protocols) rather than contradiction. | Document MTEB-side protocol; add matched controls; reword the headline gap |
| DA-M2 | Logic | §4.3, §5.1, §6, App. C.2 | Causal claim that models "exploit patterns" is not tested; alternative explanations ignored (in-domain supervised training, label provenance, humans as zero-shot). Low human score is read as bad labels and high model score as artifacts, whatever the dataset. "Evidence supports a weaker claim". | Compute and report the agreement–gap relation with intervals; test zero-shot vs in-domain-trained models; reword |
| DA-M3 | Evidence | §3.3, §4.3, App. D | Low agreement on n = 30–48 items (κ = 0.39 ± ~0.18 by the usual approximation) is used to condemn datasets; ARI on free-cluster annotations is sensitive to the number of clusters chosen; thresholds are applied inconsistently (Toxicity κ = 0.55 "reliable"; STSBenchmark ρ = 0.58 "high"). | One reliability measure, intervals, consistent thresholds; second annotator for flagged datasets |
| DA-M4 | Scope / Evidence | §4.2, §5.1, Table 2, App. C.1.2 | Cultural-knowledge explanation rests on one annotator per language, English-only models in the comparison pool, and a Russian sentiment dataset the authors themselves describe as ambiguous. "Evidence supports a weaker claim". | Second annotator; compare against multilingual models only; item-level analysis |
| DA-M5 | Evidence | Abstract, Table 2, Fig. 1 | The headline 77.6 vs 80.1 pools four metrics, is 62% English, has no interval, and ranks humans 4th among models separated by 0.1–2.5 points. | Normalized, macro-averaged scores with bootstrap intervals; drop rank claims |
| DA-M6 | Overclaiming (E5) | §3.2, §4.3, §5.2, §5.3, §6 | Wording exceeds evidence: "ensures our findings generalize across the diverse landscape of embedding applications"; dataset issues said to compromise reliability "fundamentally" (§4.3); "should be replaced"; "decisions on evaluation datasets can be made from even a few samples"; "state-of-the-art" for 13 models including 2021-era encoders. Survives in weaker form. | Narrow each claim to what the data show |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 2 caption, Fig. 13 | "5 of 14" vs 4 pairs where humans are top |
| DA-m2 | Consistency | §4.3 vs Table 4 | Emotion best-model 87.1 vs 75.4 (Table 4, Fig. 13) |
| DA-m3 | Consistency | App. B vs App. D | Agreement values differ (Reddit, Tweet, SICK-R, SIB200, Robust04) |
| DA-m4 | Evidence | App. C.1.1 | The STS22-Russian "context expansion" pattern is illustrated by a generic example, not by items shown from the dataset; unverifiable |
| DA-m5 | Presentation | §4.1 | Category averages are English-only without saying so |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Overall human mean over 26 pairs | 77.6 | (553.5 + 476.3 + 530.0 + 458.8)/26 = 77.64, from Table 2 and Fig. 15 values | Yes |
| Human rank | 4th | Table 2: 80.1, 78.3, 78.2, then human 77.6 | Yes |
| Gap to the best model | 80.1 − 77.6 | 2.5 | Yes |
| Humans top in "5 of 14" pairs | 5 | 4 (ara/nob/rus sentiment, ara STS) | **No** (Fig. 13 says 4) |
| Classification human mean | "averages 70.3 across classification tasks" | English only 70.25; all seven 79.1 | Only English |
| Clustering human mean | 67.4 | English 67.4; all seven 68.0 | English only |
| STS human mean | 83.2 | English 83.15; all six 76.5 | English only |
| Emotion: best model | 87.1 (§4.3, Fig. 4, App. D) | 75.4 (Table 4, jasper), consistent with Fig. 13 gap −29.6 | **No** |
| Humans above the median model | 61.5% | 16 of 26 positive bars in Fig. 14 listing = 61.5% | Yes |
| Model/human ratio example | 85/45.8 = "185%" | 185.6% | Yes |

## Ignored Alternative Explanations
- Models trained or fine-tuned on in-domain training splits of MTEB tasks (zero-shot share varies by model) vs humans who see none.
- Humans zero-shot with no labelled examples vs a classifier fit on training data (classification); free cluster count vs fixed (clustering); binary judgments vs graded ranking (reranking).
- Gold-label provenance (e.g., distant supervision, submitter-chosen categories) as the source of both low agreement and learnable model "patterns".
- Annotator expertise and fatigue on 30–50 items; one annotator per language.
- Non-multilingual models in the pool lowering the "mean" and "median" model comparisons for non-English languages.
- Sampling noise: with n = 20–50 per dataset, most gaps below about 10 points are within one standard error.

## Missing Stakeholder Perspectives
- Annotators: pay, consent, exposure to toxic content, and a three-person, all-male panel.
- Speakers of Norwegian, Danish, Arabic and Russian, whose datasets are judged by one annotator.
- Benchmark maintainers, who may act on the replace recommendations.
- Dataset creators whose labelling schemes are called flawed on small evidence.

## Observations (Non-Defects)
- The paper reports the agreement statistics in the appendix, so readers can check the claims; this transparency is what made the inconsistencies detectable.
- The overall 77.64 recomputes from the paper's own tables.
- The Limitations section is candid about sample size.
- The authors state that humans are neither a ceiling nor a floor, which is the right framing if carried through.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Unmatched protocols, untested mechanism, inconsistent thresholds |
| Clarity & Presentation | 60 | Readable; counts and statistics conflict |
| Novelty & Originality | 50 | Measurement is new; framing known |
| Significance & Impact | 52 | Relevant but weakly supported |
| Experimental Validation | 38 | Tiny n, no uncertainty, one annotator for non-English |
| Reproducibility | 50 | Subsets released; protocols and guidelines missing |
| Ethical Compliance | 50 | No annotator-welfare statement |

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central comparison is unmatched and unquantified, so the paper's main takeaways are not established.

## Overall: 2 | Confidence: 4

---
---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Each weakness was tested for specificity, whether the paper already answers it, consistency with the paper, and actionability. I searched the paper (appendix included) for each point. Scores were not changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (unmatched protocols) | kept, rewritten | The MTEB-side details are not in the paper; reworded as "not stated" (a question about protocol) rather than as a fact about what MTEB does |
| R1 | W3 (human score undefined) | kept | §3.3 and §3.4 do not define it (searched) |
| R1 | W7 (code/data gaps) | rewritten | The paper says code, dataset and leaderboard are public and that subsets are in the MTEB package (§3.3); the claim now reads "guidelines, sampling and annotator time not given", not "no code" |
| R1 | Error Log ERR-2, ERR-5 (and Minor items) | moved to Minor | Cosmetic or labelling slips; the conclusions do not change |
| R1 | ERR-4 | kept, Medium confidence | Depends on how the human score is formed, which is unstated |
| R2 | W1 (related work) | kept | The prior works are verified by the literature check (Tedeschi, Northcutt) or marked [verify] (Voorhees, Uma) |
| R2 | W2(b) Russian sentiment | kept | Verified in App. C.1.2 against Table 2 (92.5) |
| R2 | Minor note on Emotion label provenance | rewritten | Stated from memory, so framed as a question with [verify] |
| R3 | W1–W5 | kept | W4 checked against the paper: demographics are given (§3.3), compensation and consent are not (searched) |
| R3 | W5 | kept, softened | Reworded to avoid criticizing the authors' intent |
| R4 | W2 (counts) | kept | Table 2 caption, Fig. 2 caption and §3.2/§4 verified |
| R4 | Minor (appendix length) | moved to Minor | Cosmetic |
| DA | DA-M1–M6 | kept | Each has a location and a fix; M1/M2 depend partly on MTEB internals not stated in the paper, so the EIC treats them as questions to the authors |
| DA | DA-m4 | kept | Checked against App. C.1.1 |

No weakness was dropped as already answered. Reports were not changed otherwise.

---

# Phase 2: Synthesizer Part A and EIC Meta-Review

## Issue list and consensus map (Synthesizer, Step 1)

| Issue | Sources | Class |
|-------|---------|-------|
| Human and model protocols not matched / undocumented | R1-W1, DA-M1, R2-W4 (alt. explanations) | CONSENSUS-3 |
| No uncertainty on small n; rank and gap claims | R1-W2, R4-W3, DA-M3, DA-M5, R3-W1 | CONSENSUS-4 |
| "Models exploit patterns" untested; overclaimed | R1-W5, R3-W3, R4-W1, DA-M2, DA-M6, R2-W2(c) | CONSENSUS-4/5 |
| Dataset-replacement claims rest on thin or inconsistent evidence | R2-W2, R1 (ERR-7, ERR-8), R4-W1, DA-M3 | CONSENSUS-4 |
| Single-annotator non-English results / cultural explanation untested | R1-W3, R2-W4, DA-M4, R3-W1 | CONSENSUS-4 |
| Internal numeric inconsistencies (87.1 vs 75.4; agreement values; "5 of 14") | R1 Error Log, R4-W2, DA-m1–m3 | CONSENSUS-3 |
| Pooled metric / English-only averages | R1-W4, DA-M5, R4-W2 | CONSENSUS-3 |
| Related-work gaps (human baselines, superhuman critiques, label noise) | R2-W1 | SOLO |
| Model coverage narrow | R2-W3 | SOLO (DA-M4 touches it) |
| Annotator welfare / consent / compensation | R3-W4 | SOLO |
| "Framework" thinly defined | R2-W5, R4-W4 | CONSENSUS-2 |
| Agreement statistics not commensurable | R3-W2, DA-M3, R1 (ERR-8) | CONSENSUS-3 |
| SPLIT: value of the contribution (R3 Overall 4 vs R1/DA Overall 2) | R3 vs R1, DA | SPLIT |
| DA-CRITICAL | none raised | none |

Issues the outcome may hinge on: protocol matching, the untested mechanism, and the internal inconsistencies (the EIC checks each against the text below).

**Official score (before EIC weights, provisional):** ratings R1 2, R2 3, R3 4, R4 3, DA 2 → mean **2.80**; official composite **54.7** (`before.json`). No consistency warnings from the script.

---

# Editorial Decision

## Paper: HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks
## Submission ID: iclr26-rcmfu1ydAf
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: benchmark
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Teodora Valcheva; R1 Methodology Dr. Kwabena Asante-Rowe, R2 Domain Dr. Mireille Duquesnoy, R3 Perspective Dr. Selim Barakzai, R4 Generalist Dr. Priya Raghunathan-Beck, DA Prof. Joaquín Medrano-Lindqvist

---

## Decision: Borderline Reject (3) · ICLR rating 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}); scale status: secondary

**Official ratings** (shown to authors): R1 2, R2 3, R3 4, R4 3, DA 2 → mean 2.80 · official composite 54.7
**EIC assessment** (internal): weighted rating 2.65 → starting point 3 · weighted composite 53.8 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 45% of ICLR submissions (accepted share ≈ 27%).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The question is useful and, as far as the literature check found, this is the first human reference on MTEB-style tasks across languages. The per-dataset tables (Tables 3–6) are a resource, the headline mean (77.64) recomputes from the paper's own tables, the agreement statistics are disclosed so the work can be checked, and the idea of reading scores alongside task reliability is constructive. Such papers are sometimes accepted at ICLR's datasets-and-benchmarks end.
- **Against acceptance:** The evidence is a pilot: 20–50 items per task, one annotator for all non-English pairs, no uncertainty estimate anywhere. The human–model comparison is not shown to be protocol-matched, and the interpretive claims that carry the paper (mechanism of "superhuman" scores, replace three datasets, cultural advantage) go beyond the data, with several internal numeric contradictions. Related work misses directly relevant critiques.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Emotion best-model 87.1 vs 75.4 | R1 ERR-1, DA-m2 | §4.3; Table 4; Fig. 13; App. D.1.1 | Verified | Table 4 lists jasper 75.4 as best on Emotion; Fig. 13 gap −29.6 = 45.8 − 75.4; 87.1 is the English-classification average in §4.1 |
| "5 of 14" top pairs vs 4 | R1 ERR-2, R4-W2, DA-m1 | Table 2 caption; Fig. 13 | Verified (minor) | I counted 4 columns where human exceeds every model |
| Agreement values differ between appendix B and D | R1 ERR-3, DA-m3 | Figs. 5, 7, 8, 9, 12 vs App. D.1 | Verified | Five mismatches; the independent variable of the thesis |
| STS22-Russian "low agreement" with a single annotator | R1 ERR-7, R2-W2(a) | App. C.1.1 vs D.1.4; §5.2 | Verified | Russian: "Single annotator (no agreement metrics)" |
| Inconsistent high/low agreement thresholds | R1 ERR-8, R3-W2, DA-M3 | §4.3, §5.1, App. D.2 | Verified | Toxicity κ = 0.55 "reliable"; STSBenchmark ρ = 0.58 listed as high |
| Tweet agreement 62.2% vs human 84.4% | R1 ERR-4 | App. D.1.1; Table 4 | Partly correct | The bound holds if the human score is the mean of two annotators; the paper does not define it, so this is a question |
| Unmatched protocols | R1-W1, DA-M1 | §3.3–§3.4 | Partly correct | The human side is as described (no ground truth, free clusters, binary relevance); the MTEB-side details are not in the paper, so the asymmetry is unverified rather than proven |
| Category averages are English-only | R1 ERR-5, DA-m5 | §4.1; Table 2 | Verified | Recomputed (70.25; 79.1 for all seven pairs) |
| Mechanism "models exploit patterns" never tested | R1-W5, DA-M2, R4-W1 | §5.1 vs §6 | Verified | §5.1: "mechanisms ... remain unclear"; Conclusion asserts it |
| Russian sentiment: ambiguous dataset, yet humans 92.5 | R2-W2(b) | App. C.1.2; Table 2; §5.1 | Verified | Both statements are in the paper |
| R3: findings "reveal genuine" cross-cultural gaps; recommendations for developers | R3 (S/W5), paper §5.1–5.2 | §4.2, §5.2 | Overstated | One annotator per language, 30–40 items; R3 already softens in W5 |
| DA: "humans 4th" is within noise | DA-M5, R1-W2 | Table 2 | Partly correct | Top four models differ by 0.1–2.5 points; no interval in the paper; the noise size is my estimate, not shown by the paper |
| Missing related work (Tedeschi, Northcutt) | R2-W1 | §2.2 | Verified | Literature check: both are prior, peer-reviewed, uncited; not required comparisons, but the positioning gap is real |
| No ethics / compensation statement | R3-W4 | whole paper | Verified | Searched; absent (only the LLM statement, App. G) |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error Log entries ERR-1, 2, 3, 5, 7, 8 verified at their locations; ERR-4 is hedged correctly. Slightly harsh on the Overall for a resource paper, hence not 1.5 |
| R2 (Domain) | 3 | 4 | 1.0 | Citations verified; W2(b) verified; model-coverage point is reasonable; sound and typical |
| R3 (Perspective) | 4 | 3 | 0.75 | Measurement points are good, but the rating leans on benefits (cross-cultural insight, practical guidance) that the evidence does not yet support; the paper's own §5.1 hedges the mechanism |
| R4 (Generalist) | 3 | 3 | 1.0 | Calibrated to ICLR and consistent with its text; counts issue verified |
| DA | 2 | 4 | 1.0 | Most arguments verified; M1 and M2 rely on MTEB internals the paper doesn't state, so their weight is limited to what the text shows; no CRITICAL inflation |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

The DA's strongest objection (DA-M1/M2: unmatched protocols and an untested mechanism) was checked against the paper. It does not contradict the main claim, and the experiment does measure what the headline numbers say (human and model scores under their own protocols), so it is a MAJOR weakness, not a cap.

### Final Decision and Justification
The EIC-weighted rating is 2.65, which rounds to a starting point of 3 (Borderline Reject); the composite cross-check (53.8, band 3) agrees, so I do not depart from the starting point, and no DA ceiling applies. The deciding evidence: (i) the central human-vs-model comparison is not shown to be protocol-matched (§3.3–§3.4) and has no uncertainty on 20–50 items per task; (ii) the claims the paper emphasizes (mechanism, dataset replacement, cultural advantage) are unsupported as worded and partly internally inconsistent (§4.3 vs Table 4; App. C.1.1 vs D.1.4; App. D.2 thresholds); (iii) the positives (a first measurement, a usable resource, an interesting framing) are real but do not outweigh the weaknesses for a typical ICLR submission. I place the paper at about the 45th percentile of submissions, in the typical-rejected band, not borderline: the problems are fixable but need new annotation and analysis (not a rebuttal-length fix). Reframed as a pilot with uncertainty and narrower conclusions, a revised version could well succeed at a datasets-and-benchmarks venue. Final: **3**, which does not exceed any ceiling.

---

## Score Summary

### Official Scores and EIC Assessment (output of `aggregate_scores.py`, with EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 44 | 52 | 58 | 54 | 42 | 50.0 | 48.9 | 16 |
| Clarity & Presentation | 62 | 64 | 70 | 66 | 60 | 64.4 | 63.8 | 10 |
| Novelty & Originality | 52 | 55 | 62 | 56 | 50 | 55.0 | 54.2 | 12 |
| Significance & Impact | 55 | 58 | 68 | 60 | 52 | 58.6 | 57.6 | 16 |
| Experimental Validation | 40 | 48 | 55 | 50 | 38 | 46.2 | 45.0 | 17 |
| Reproducibility | 55 | 58 | 62 | 58 | 50 | 56.6 | 56.0 | 12 |
| Ethical Compliance | 50 | 52 | 55 | 52 | 50 | 51.8 | 51.4 | 5 |
| **Composite** | 50.9 | 55.4 | 62.0 | 56.9 | 48.3 | **54.7 (before)** | **53.8 (after)** | |
| Pool position (P%) | 38 | 48 | 66 | 50 | 38 | | | |

No spread above 20; no consistency warnings. Weighted reviewer shares: R1 27%, R2 21%, R3 13%, R4 18%, DA 21%.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}); internal Overall 3 (Borderline Reject) |
| Confidence | 3.6 (mean of reviewer confidences: 4, 4, 3, 3, 4) |

*ICLR labels are secondary-status: "Recent analyses report {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}; verify against the current form." The ICLR venue composite is 53.9.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks" to ICLR. Giving embedding benchmarks a human reference is an ambitious and useful goal, and the question is well chosen.

**Overall Assessment:**
The panel found the question valuable and the per-dataset human scores a resource that the community can use. The evidence is at pilot scale, though, and the conclusions the paper emphasizes go beyond what the data can carry. This is how a careful panel would likely see this draft, not a prediction of any real outcome.

**Key Strengths Identified by Reviewers:**
1. A first human reference on MTEB-style tasks across four task types and five languages, with per-dataset tables (R1, R2, R4).
2. A constructive idea: read model scores together with task agreement, reported with task-appropriate statistics (R1, R3).
3. A transparent appendix and a candid limitations section that make the work checkable (R1, R4, DA).

**Key Concerns Requiring Attention:**
1. Human and model scores are not shown to come from matched protocols, and no uncertainty is reported on 20–50 items per task and 1–2 annotators (CONSENSUS-4: R1, R4, DA, R3).
2. The mechanism claim ("models exploit annotation patterns where humans disagree") and the recommendation to replace Emotion, ArXiv clustering and STS22-Russian are not tested, and partly rest on inconsistent or missing agreement data (CONSENSUS-4: R1, R2, R3, R4, DA).
3. Internal numeric inconsistencies, e.g., Emotion best-model 87.1 in §4.3 against 75.4 in Table 4, five agreement values that differ between Appendix B and D, and the Table 2 caption (CONSENSUS-3).
4. All non-English results come from one annotator; the cultural-knowledge explanation is untested (CONSENSUS-4).
5. Related work does not engage with the literature on human baselines, "superhuman" claims and label noise (R2, SOLO), and there is no statement about annotator compensation, consent and welfare (R3, SOLO).

**Critical Challenge (Devil's Advocate):** none rated CRITICAL. The DA's strongest objection is that the 2.5-point gap mixes understanding with protocol differences (humans see no labelled examples; the model-side protocol is undocumented) and that "models are strongest where humans disagree" does not show that datasets are flawed. The EIC checked it and treats it as a MAJOR weakness that the authors can address by documenting the protocol, matching it, and narrowing the claims.

**Decision: Borderline Reject (3).**
The deciding factor is that the paper's central comparison and its main interpretive claims are not yet supported at the level ICLR expects, and the fix needs new annotation and analysis rather than rewording. To change this assessment, the authors would need uncertainty estimates, a matched-protocol check, a second annotator for the non-English headline results, and conclusions narrowed to what the data show.

Please refer to the Revision Roadmap below for prioritized guidance.

Sincerely,
Prof. Teodora Valcheva
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No uncertainty on small n; rank and gap claims | R1, R3, R4, DA | CONSENSUS-4 |
| Mechanism claim untested; overclaimed wording | R1, R2, R3, R4, DA | CONSENSUS-4/5 |
| Dataset-replacement claims on thin or inconsistent evidence | R1, R2, R4, DA | CONSENSUS-4 |
| One annotator for non-English; cultural explanation untested | R1, R2, R3, DA | CONSENSUS-4 |
| Unmatched / undocumented protocols | R1, R2, DA | CONSENSUS-3 |
| Numeric inconsistencies | R1, R4, DA | CONSENSUS-3 |
| Pooled metrics / English-only averages | R1, R4, DA | CONSENSUS-3 |
| Agreement statistics not on one scale | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the paper worth accepting in current form? | R3 (4) | R1, DA (2); R2, R4 (3) | R3's rating relies on benefits the evidence does not yet support (weight 0.75); the specific inconsistencies R1 found verified |
| Is low agreement a sign of a bad dataset? | Authors; partly R2 (Emotion) | R3 (valid subjectivity), DA (artifact of supervised measurement) | The paper's own §5.1 says the mechanism is unclear; treat as hypothesis |
| Is the human advantage in Arabic/Russian "genuine"? | Authors | R1, R2, DA | One annotator per language; explanation untested |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag (largest: Experimental Validation, 17; Technical Rigor and Significance, 16). R3 is highest on every dimension (consistent with its role and its pool position of 66); the EIC weights it at 0.75 for the reason above. Overall ratings range from 2 to 4; the weighted rating 2.65 sits between R1/DA and R2/R4.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Unmatched protocols | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Untested mechanism | Yes (R1-W5, R4-W1) | n/a | n/a |
| DA-M3 | MAJOR | Agreement thresholds and sample size | Yes (R1, R3) | n/a | n/a |
| DA-M4 | MAJOR | Cultural-knowledge explanation | Yes (R2-W4) | n/a | n/a |
| DA-M5 | MAJOR | Pooled headline number and rank | Yes (R1-W4, R4-W3) | n/a | n/a |
| DA-M6 | MAJOR | Overclaiming wording | Yes (R4-W1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Items that undermine the main interpretive claims, ordered by impact on the decision. No DA-CRITICAL issue was upheld, so these come from verified issues on main claims.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Human and model protocols unmatched / undocumented | R1-W1, DA-M1 | §3.3–§3.4; Table 2 | Document MTEB-side protocol per task type; add matched controls (human with labelled examples or true cluster count; models zero-shot/same budget); remove "identical protocols" unless shown | High (new small annotation round plus model re-runs; < 20 GPU-h) | Partly (documentation yes; new controls need a week or more) |
| R2 | No uncertainty; rank and gap claims | R1-W2, R4-W3, DA-M3, DA-M5 | Table 2, Fig. 1, Fig. 3, App. D | Paired bootstrap over items (and annotators) for every gap, κ/ARI/ρ; report normalized, macro-averaged scores; drop claims that do not survive | Low (hours; no GPU) | Yes |
| R3 | Mechanism claim untested; dataset-replacement and cultural claims | R1-W5, DA-M2, DA-M4, R2-W2, R4-W1, DA-M6 | §4.2–§4.3, §5.1–§5.2, §6 | Quantify agreement–gap relation with intervals on a common reliability scale; test in-domain-trained vs other models; second annotator for flagged datasets and the non-English headline pairs; reword to "warrant re-examination" | High (≈ 4–6 tasks × 40 items extra annotation) | Partly (rewording yes; new annotation no) |
| R4 | Numeric inconsistencies in the evidence base | R1 Error Log ERR-1, 3, 7, 8, DA-m1–m3 | §4.3, App. B vs D, App. D.2, Table 2 caption | Regenerate every statistic from a single script; fix 87.1→75.4; apply one agreement threshold; correct "5 of 14" | Low | Yes |
| R5 | Human score undefined; one annotator for non-English | R1-W3, ERR-4 | §3.3, App. D.1 | Define the aggregation; report per-annotator scores and the inter-annotator ceiling | Low–Medium | Yes (definition), No (second annotator) |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Related work lacks human-baseline, superhuman and label-noise literature | R2-W1 | Add and position against Tedeschi et al. (ACL 2023), Northcutt et al. (NeurIPS 2021 D&B), IR assessor-agreement work (Voorhees 2000 [verify]), learning-from-disagreement survey (Uma et al. 2021 [verify]) | Low | Yes |
| S2 | Model coverage narrow for "best model" and rank claims | R2-W3 | Add strongest multilingual models (e.g., larger Qwen3-Embedding variants, Gemini Embedding, M3-Embedding); report the non-English comparison only against multilingual models | Medium (≈ 10–30 GPU-h) | Partly |
| S3 | Ethics: annotator pay, consent, welfare, panel diversity | R3-W4 | Add an annotator statement and a limitation | Low | Yes |
| S4 | Pooled metrics, English-only averages | R1-W4, R4-W2 | Label averages by coverage; normalized scores | Low | Yes |
| S5 | Agreement statistics on different scales | R3-W2 | Use Krippendorff's α (appropriate distance per measurement level) with intervals | Low | Yes |
| S6 | Reproducibility on the human side | R1-W7 | Add guidelines, sampling procedure and seed, annotator time, MTEB version | Low | Yes |
| S7 | "Framework" claim | R2-W5, R4-W4 | Narrow the wording, or add a procedure and one new-task demonstration | Low (wording) / High (demo) | Wording only |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Low agreement as valid subjectivity | R3-W3 | Pilot revised guidelines on 30 ArXiv items; report agreement change |
| N2 | IRT analysis across items, annotators, models | R3 | Fit an item-response model on existing data |
| N3 | Appendix length and caption style | R4 Minor | Move per-dataset text into tables; unify captions |
| N4 | Minor slips: STS22-Russian 58.7 vs 58.5; Fig. 2 "16 tasks"; "%" for Spearman | R1 Minor | Correct |
| N5 | Perspectivist reporting of disagreement; release item-level annotations | R3 | Future work |

---

## Estimated Revision Effort
- Priority 1: 5 items, roughly 2–3 weeks (documentation and statistics: 2–3 days; matched-control annotation and extra annotators: 1–2 weeks; model re-runs: < 1 day of GPU).
- Priority 2: 7 items, roughly 1 week (writing and a few additional models).
- Priority 3: 5 items, optional.
- **Total estimated revision time**: about 3–4 weeks, mostly annotation logistics.
