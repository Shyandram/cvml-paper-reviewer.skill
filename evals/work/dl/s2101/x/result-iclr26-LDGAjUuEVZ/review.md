# Simulated Peer Review: BrowseComp-ZH (target venue: ICLR, full mode)

*Simulation of how a careful panel would likely see this draft; not a prediction of any outcome. Date: 2026-11-10. Figures were not available (text extraction only): Figures 1–3 were judged from captions and surrounding text. Reviewer personas are fictional; the five reviewers were run as separate role-based passes sharing one model context (no independent agents). The paper recognized from prior knowledge as a known public benchmark; it was reviewed on its merits only.*

## 📋 Phase 0: Paper Analysis

| Item | Finding |
|------|---------|
| Title | BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese |
| Primary Discipline | NLP / ML → evaluation of LLM agents, web search and information retrieval |
| Secondary Discipline(s) | Information retrieval, Chinese-language NLP, evaluation methodology |
| Paper Type | Benchmark (dataset + model evaluation); composite weights: benchmark |
| Core Technique(s) | Reverse-designed multi-constraint questions; two-stage QC (human search check, AI-agent uniqueness check); LLM-as-grader (GPT-4o); verbalized-confidence calibration error |
| Target Venue | ICLR 2026 (stated); profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution, Rating, Confidence; scale status secondary) |
| Paper Maturity | Submission-ready, short (9 pages main text, analysis section thin) |
| Ethics-Relevant Content | Web-sourced factual questions about named public figures (Fig. 1 film example); annotator labour; no licence, consent or compensation statement |

### Claimed Contributions (as stated by the authors)
1. **C1** First benchmark for web browsing in the Chinese information environment, natively constructed (Abstract, §1, §2, §5).
2. **C2** 289 multi-hop questions, 11 domains, with a two-stage quality-control protocol that ensures difficulty and answer uniqueness (§3.1–3.3).
3. **C3** Evaluation of over 20 models and AI-search products; most are below 10%, best (OpenAI DeepResearch) 42.9% (Table 1, §4.4).
4. **C4** Findings: reasoning helps (§4.5), multi-round retrieval helps (§4.6), retrieval can hurt (DeepSeek-R1, §4.6), search raises calibration error (§4.7).

### Paper memory (factual record, shared with all reviewers)
- **Construction:** 10 annotators (Master's/PhD) pick ≥5 topics each by "personal interests" (§3.1); questions tested on Baidu/Bing/Google with 3 keyword combinations per engine; also tested with GPT-4o and DeepSeek in web mode, revised if both "consistently retrieve the correct answer" (§3.1). 480 preliminary → Stage 1 cross-check (peers, search engines only, 10-minute limit) removes 76 → 404 → Stage 2 AI-agent uniqueness check removes 115 → 289 (§3.2). Arithmetic: 480−76=404, 404−115=289 (consistent).
- **Statistics:** Fig. 2 topic counts sum to 289 (18+22+10+23+7+26+45+29+40+32+37) and the percentages match; Fig. 3 questions mostly 60–90 characters, answers mostly 5–10 characters (from the text; plot unavailable).
- **Evaluation setup:** temperature 0.6 / top-p 0.95 for models with configurable decoding; O1 and Claude-3.7 fixed (§4.2). Answers extracted by regex and graded by GPT-4o with the BrowseComp grading prompt (§4.2, Fig. 5). AI search products run by human annotators through GUIs, answers extracted manually (§4.2). Metrics: accuracy and ECE with 5 bins over verbalized confidence (§4.3). 22 rows in Table 1.
- **Not stated after search:** seeds/number of runs/variance; human performance or solvability audit; inter-annotator agreement; contamination analysis; dates and versions of products and of the grader; licence/consent/compensation; per-topic or per-difficulty results; error analysis. No train/dev/test split exists (all 289 items are the test set; no tuning is done on it by the paper).
- **Appendix adds:** the exact model and grading prompts (A.1, A.2/Fig. 4–5). Nothing else.
- **Unverifiable here:** Figures 1–3 (only captions and text read).

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. No redaction was needed; reviewers read the original text.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ingrid Solheim, senior area chair, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / evaluation of LLM agents, benchmark design, retrieval
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Asks whether the central claim is actually measured; tolerant of small benchmarks if construction is honest

### Reviewer 1 (Methodology): Prof. Rahul Venkataraman, large public research university (South Asia)
- **Seniority / Expertise**: Senior faculty / LLM evaluation protocols, LLM-as-judge validity, benchmark contamination
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every headline number; insists on confidence intervals and matched comparisons

### Reviewer 2 (Domain): Dr. Mei-Ling Zhou, industrial research lab (East Asia)
- **Seniority / Expertise**: Senior industry scientist / Chinese QA and retrieval benchmarks, search agents
- **Review Focus**: Literature, positioning, domain contribution
- **Style**: Compares against the closest prior benchmark, sceptical of "first" claims

### Reviewer 3 (Perspective): Dr. Tomás Aguirre, information-science department, university (South America)
- **Seniority / Expertise**: Mid-career / information-seeking behaviour, web search practice, search-engine bias and platform ecosystems
- **Review Focus**: Cross-disciplinary connections, deployment realism, broader impact
- **Style**: Constructive; asks how the benchmark relates to what people and products really do

### Reviewer 4 (Generalist): Dr. Amara Okafor, university AI group (West Africa)
- **Seniority / Expertise**: Mid-career / NLP and question answering, not search agents specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted benchmark papers look like

### Devil's Advocate: Prof. Lukas Brandt, university statistics and ML group (Central Europe)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, causal inference, measurement validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks "does this number measure what the title says?"

*Personas are fictional. Proceeding with stated assumptions (venue stated by user; paper type Benchmark).*

---

# Phase 1: Independent Reports

# Peer Review Report

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Reviewer: Prof. Rahul Venkataraman, Methodology Reviewer (large public research university, South Asia; fictional persona)
## Expertise: LLM evaluation protocols; LLM-as-judge validity; benchmark contamination
## Date: 2026-11-10

---

## Summary
The paper builds a 289-question benchmark of multi-constraint, short-answer questions about the Chinese web, following the reverse-design idea of an English predecessor. Ten annotators write questions, which pass a human search-engine check and an AI-agent check for alternative answers. 22 models and commercial search products are then evaluated, with OpenAI DeepResearch best at 42.9%. The authors draw four conclusions about reasoning, multi-round retrieval, retrieval harming DeepSeek-R1, and calibration.

---

## Strengths

### S1: Clear, replicable construction recipe with stated counts
§3.1–3.2 give the funnel 480 → 404 → 289 with reasons for each drop; I checked 480−76=404 and 404−115=289 and the topic counts in Figure 2 (sum 289, percentages match). The three-engine, three-keyword-set check and the "unseen on first page" rule are concrete and testable.

### S2: Difficulty is real and discriminative at the top
Accuracies span 4.8% to 42.9% (Table 1), so the set is far from saturated, and the question format (short exact answers) keeps grading simple. Honest limitations paragraph (§5) concedes size and uniqueness.

### S3: Prompts and grading prompt are in the appendix
Fig. 4–5 (A.1, A.2) give the instruction and grader prompts in Chinese and English, which many benchmark papers omit.

---

## Weaknesses

### W1: Validity of the ground truth and of "difficulty" is not measured (E4/E8)
Answer uniqueness (§3.2 Stage 2) is checked only by reading the outputs of five AI agents that mostly fail (top accuracy 42.9%); alternatives are therefore found only when an agent happens to produce one, so recall of ambiguity is low by construction. 115 of 404 candidates (28%) were rejected for ambiguity, which suggests the base rate of non-unique questions is high and the residual rate among the 289 is unknown. No independent human solver, no re-audit of a random sample, no inter-annotator agreement and no human performance number is given, so we cannot tell whether 42.9% means "hard" or "partly ill-posed". Difficulty (§3.2 Stage 1) is defined as "not found in 10 minutes by a peer using search engines", which says little about solvability.
- **Suggested Fix**: Have two independent annotators (not the author) solve a random 60–100 questions with unlimited time, report agreement with the gold answers, human accuracy and time; report the error rate of the gold answers. ≈ 30–40 annotator-hours.

### W2: The headline comparisons are confounded and some conclusions are not supported by Table 1 (E5/E1)
(a) §4.5 and §1 finding 2 attribute gains to "reasoning" by comparing different model generations (Claude-3.5 vs 3.7, Gemini-2.0-Flash vs 2.5-Pro); whether extended thinking was on is not stated. O4-mini, a reasoning model, scores 15.2%, below O1 (29.1%), which points to knowledge capacity, not reasoning. (b) §4.6 compares DeepSeek-R1 (23.2%, API, no search) with the DeepSeek chat product (7.6%) and calls the difference "enabling web search"; these are different systems with different prompts, answer extraction (human vs regex+GPT-4o) and retrieval stacks. (c) §4.7 says "integrating search functionality results in increased calibration errors", but Table 1 shows the nine search products have a mean calibration error of 49.3% (444/9, derived) against 65.7% (854/13, derived) for the 13 non-browsing models, with DeepResearch at 9%. Only the R1/DeepSeek pair supports the sentence. (d) The Conclusion says multi-turn products "outperform purely parametric models", yet Doubao (Deep Search) 26.0% and Perplexity 22.6% are below O1 (29.1%) and Gemini-2.5-Pro (27.3%) in Table 1.
- **Suggested Fix**: Narrow the claims to what the pairs show; add matched comparisons (same open model with and without a fixed search tool, e.g., a ReAct-style loop over one search API); state extended-thinking settings. Compute: ≈ 3 open models × 289 questions × 2 conditions, a few GPU-days.

### W3: No variance or uncertainty; many conclusions are within noise
Single run per system at temperature 0.6 (§4.2), no repeated sampling, no bootstrap CI. With n = 289 the 95% interval for 42.9% is about ±5.7 points (derived), and for 8.0% vs 7.6% (Kimi vs DeepSeek) the gap is one question (23 vs 22 of 289, derived). O1 (29.1%) vs Gemini-2.5-Pro (27.3%) is about five questions. §4.6 states "Statistical analysis shows that systems employing multi-round retrieval achieve significantly higher accuracy", but no test appears anywhere, and the groups are three products each, with the multi/single-round labels of closed products asserted without evidence.
- **Suggested Fix**: Report bootstrap CIs over questions and 3 samples per non-product model (≈ 3× current API cost); remove "significantly" unless a test is given.

### W4: Evaluation of products is not reproducible and mixes manual and automatic scoring
§4.2: product outputs come from human annotators using GUIs, answers extracted manually. Number of annotators, access dates, product versions, modes, region/IP, and agreement are not stated; Table 1 model strings are incomplete ("Claude-3.5-Sonnet()", "Gemini-2.0-Flash()", §4.1). Products change weekly, so Table 1 cannot be re-run. The grader (GPT-4o) is not validated against human judgments, and the grader prompt instructs "Put 100 if there is no confidence score available" (Fig. 5), which would inflate calibration error for models that omit confidence; the paper does not say how often this happened.
- **Suggested Fix**: Report dates/versions, a human audit of ≥100 graded outputs for grader error, and the fraction of missing confidences (and ECE excluding them).

### W5: Possible circularity between benchmark filtering and evaluated systems
Questions were revised until GPT-4o and DeepSeek in search mode did not "consistently retrieve the correct answer" (§3.1) and rejected when five agents (OpenAI DeepSearch, Perplexity, Doubao, O1, Gemini-2.5-Pro) gave defensible alternatives (§3.2); the same systems are then top-ranked in Table 1. Low GPT-4o accuracy (6.2%) is partly by construction. No contamination analysis; the dataset is released openly with no canary or encryption, so future training-data leakage is likely.
- **Suggested Fix**: Report scores on the items never revised against GPT-4o/DeepSeek, discuss filtering bias, and add a canary string or encrypted release.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5/E1 | §4.7 vs Table 1 | "integrating search functionality results in increased calibration errors" | Mean calibration error of 9 browsing products 49.3% vs 65.7% for 13 non-browsing models; DeepResearch 9% | Recomputed from Table 1 | High | MAJOR | Restrict claim to R1 vs DeepSeek and discuss counter-evidence |
| ERR-2 | E5 | §5 vs Table 1 | "further outperform purely parametric models" | Doubao 26.0% and Perplexity 22.6% < O1 29.1%, Gemini-2.5-Pro 27.3% | Cross-referenced | High | MAJOR | Say "only DeepResearch outperforms" |
| ERR-3 | E5 | §4.6 | "Statistical analysis shows that systems employing multi-round retrieval achieve significantly higher accuracy" | No test or CI reported anywhere | Protocol sweep (no test found) | High | MAJOR | Add test or delete "significantly" |
| ERR-4 | E1 (minor) | §4.5 | "nearly 8% absolute improvement" | 26.0 − 18.7 = 7.3 points | Recomputed | High | MINOR | Write 7.3 |

**Minor:** "Fig. 4" and "Fig. 5" prompts are cited as "Appendix 4/5" in §4.2 though they are A.1/A.2; the §1 finding 4 in the Introduction duplicates §4.6.

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | First native Chinese browsing benchmark | Abstract, §5 | None needed beyond related work | Plausible; see R2 |
| C2 | Difficulty and uniqueness ensured | Abstract, §3.2 | Funnel counts only | Partially supported |
| C3 | Most models <10%, handful >20% | Table 1 | 10 of 22 below 10%, 6 above 20% (counted) | Supported |
| C4 | Reasoning / multi-round / search-hurts / calibration | §4.5–4.7 | Confounded pairs | Partially; calibration claim contradicted |

---

## Missing References
Not my role; see Reviewer 2.

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Construction is sensible but validity of gold answers and key comparisons are untested |
| Clarity | 3 | Clear funnel and prompts |
| Significance | 3 | A useful resource if gold answers are reliable |
| Originality | 2 | Adaptation of an existing recipe to Chinese |

---

## Dimension Scores (0–100)

**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful resource, but ground-truth validity is unmeasured, key comparisons are confounded and one analysis claim contradicts Table 1; typical accepted benchmark papers audit their gold labels.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Unvalidated uniqueness, confounded pairs, claim vs table mismatches |
| Clarity & Presentation | 70 | Competent | Easy to follow; analysis thin |
| Novelty & Originality | 55 | Competent | Adaptation of reverse design; useful new setting |
| Significance & Impact | 62 | Competent | Chinese agents benchmark is of real use |
| Experimental Validation | 48 | Developing | Single runs, no CIs, no human baseline, no matched search/no-search comparison |
| Reproducibility | 50 | Developing | Data released but products not re-runnable; versions missing |
| Ethical Compliance | 58 | Competent | Limitations stated; no licence/annotator statement |

---

## Questions for Authors
1. What is the accuracy and agreement of independent humans on a random sample, and how many gold answers were found wrong? (A low error rate would raise my Experimental Validation score; a high one lowers it.)
2. How much of the 23–29% accuracy of non-browsing models (R1, O1, Gemini-2.5-Pro) is memorization of pages in pretraining data?
3. Was extended thinking enabled for Claude-3.7-Sonnet, and which reasoning effort for O1/O4-mini?
4. How many product outputs lacked a confidence and were scored with 100?

---

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. §5 admits size and non-guaranteed uniqueness, but does not discuss filtering against evaluated systems, grader error, snapshot nature of product results or contamination.

## Ethics Review Flag
**No**: minor privacy/licence statement missing, not an ethics-review matter.

## Overall Score
**3**: Borderline Reject. A sensible, useful dataset whose central measurements (validity of gold answers, matched comparisons, uncertainty) are missing, with several analysis claims not supported by Table 1; fixable but needs new human annotation.

## Confidence
**4**: Confident; I recomputed Table 1 quantities, but did not see the figures or data.

---

# Peer Review Report

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Reviewer: Dr. Mei-Ling Zhou, Domain Reviewer (industrial research lab, East Asia; fictional persona)
## Expertise: Chinese QA and retrieval benchmarks; search agents
## Date: 2026-11-10

---

## Summary
The paper adapts the English BrowseComp recipe (answer-first, multi-constraint, hard to search) to the Chinese web and releases 289 questions across 11 topics. It evaluates a mixed bag of LLMs and commercial AI-search products and reports that most score under 10%, with DeepResearch best at 42.9%. It adds short analyses on reasoning, retrieval depth, a DeepSeek-R1 search regression and calibration.

---

## Strengths

### S1: Fills a real gap
Existing Chinese retrieval sets listed in §2 (Level-Navi, a dynamic QA set, CRUD-RAG, medical QA) are either easy, time-sensitive, RAG-generation focused or domain specific; a hard, short-answer, multi-constraint set natively in Chinese is a legitimate, community-useful addition (§1, §2).

### S2: Sensible design adaptations
Checking against Baidu, Bing and Google (§3.1) and Chinese-specific examples (Figure 1 caption: the heritage-art and TV-drama questions) show that translation would not preserve the questions, which is the right instinct for a Chinese benchmark.

### S3: Broad system coverage with Chinese products
Including Doubao, Kimi, Yuanbao and DeepSeek apps alongside Western products (§4.1) gives data that Western benchmark papers cannot offer.

---

## Weaknesses

### W1: Novelty is an adaptation, and the Chinese-specific difficulty is asserted, not shown
The construction recipe, answer format, grader prompt and calibration metric are taken from the English benchmark (§3.1 "Inspired by", §4.2, §4.7 "Following the methodology adopted in BrowseComp"). The new element, Chinese-web specificity, is argued in §1 ("directly translating English browsing benchmarks into Chinese does not yield a meaningful evaluation framework") with no experiment: no translated-English control, no per-question analysis of Baidu Baike/Zhihu/government-portal dependence, no comparison of difficulty drivers. The abstract also promises "censorship-related complexities", but no section examines censorship.
- **Suggested Fix**: Translate a sample of the English questions (or use machine translation) and report model accuracy; tag each question with the source platform types and report accuracy by tag; or delete the censorship phrase.

### W2: Positioning against closest prior benchmarks is thin
§2 dismisses Hu et al. (2024) as lacking "rigorous control over task difficulty" with no evidence, and does not discuss Chinese factuality sets or general web-traversal benchmarks (see Missing References and the literature-check addendum). There is no table comparing size, answer type, languages and construction control across benchmarks. "First benchmark" (Abstract, §5) is plausible for Chinese short-answer browsing but is stated without a feature comparison.
- **Suggested Fix**: Add a comparison table (size, language, multi-hop, answer verifiability, construction, difficulty control) and rephrase "first" to the precise intersection.

### W3: Domain-level coverage and interpretation of the results
Topic coverage is driven by annotator "personal interests" (§3.1, §3.3), giving 15.6% Film & TV but 2.4% Academic Papers and 3.5% Policy & Law, which are exactly the regions of the Chinese web where government portals and CNKI-type sources matter; Table 1 is never broken down by topic. §4.4's "demonstrating the strength of high-capacity language models" misreads the fact that DeepSeek-R1, O1 and Gemini-2.5-Pro exceed 20% with no browsing: it indicates that a large fraction of the questions is answerable from parametric memory, weakening the claim that the benchmark isolates browsing.
- **Suggested Fix**: Report per-topic accuracy, and the accuracy on the subset where no-browsing models fail, as the "pure browsing" subset.

### W4: Product-level evaluation measures systems, not LLM browsing
The title and abstract frame the benchmark as measuring "web browsing ability of LLMs", yet four of the seven highest-scoring rows (DeepResearch, Doubao ×2, Perplexity) are closed commercial products with unknown retrieval stacks and engines (Table 1). Without a fixed search tool and open backbones, domain readers learn which products are better in spring 2025, not why.
- **Suggested Fix**: Add a controlled agent baseline (one open reasoning model and one open non-reasoning model with the same search API and tool loop).

### Missing References
*Literature check ran in strict mode; see the addendum below. Recommendations are given with the citation-integrity rule.*

(see "Literature-check addendum", Phase 1.5)

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gold-answer validity not shown, analyses thin |
| Clarity | 3 | Clear |
| Significance | 3 | Fills a language gap |
| Originality | 2 | Adaptation of BrowseComp; novelty is the language and data |

---

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: addresses an actual gap with a hard, usable test set that matches what accepted benchmark papers offer in kind, but is an adaptation with a thin analysis; this puts it at the upper edge of borderline.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Reasonable recipe, validity unmeasured |
| Clarity & Presentation | 72 | Competent | Clear |
| Novelty & Originality | 58 | Competent | Language adaptation of a known recipe, no new method |
| Significance & Impact | 66 | Competent | Useful for Chinese agents |
| Experimental Validation | 58 | Competent | Broad coverage, shallow analysis |
| Reproducibility | 60 | Competent | Data and prompts released, products unreproducible |
| Ethical Compliance | 62 | Competent | Limitations stated |

---

## Questions for Authors
1. How does model accuracy change on a machine-translated English BrowseComp sample, and on the Chinese originals? (If Chinese-specific difficulty is shown this raises Novelty.)
2. Which question types or platforms drive failures of DeepResearch?
3. How does the benchmark compare in size and design with other Chinese factuality sets?

---

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (size and uniqueness only).

## Ethics Review Flag
**No**.

## Overall Score
**4**: Borderline Accept. Fills a real language gap with a hard test set; novelty is modest and the evidence for "Chinese-specific" difficulty is missing, but the resource is useful and the weaknesses are fixable with existing data and modest additions.

## Confidence
**4**: Know the Chinese benchmark landscape well; did not see the dataset.

---

# Peer Review Report

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Reviewer: Dr. Tomás Aguirre, Perspective Reviewer (information-science department, South America; fictional persona)
## Expertise: information-seeking behaviour; web search practice; platform ecosystems
## Date: 2026-11-10

---

## Summary
The authors build a hard Chinese browsing benchmark and show that even strong commercial search agents solve fewer than half of its questions. They interpret model differences in terms of reasoning, iterative retrieval and the difficulty of reconciling retrieved evidence with internal knowledge.

---

## Strengths

### S1: Matches how information-seeking research thinks about "known-item, hard-to-find" tasks
Reverse-designed items with a single verifiable answer (§1, §3.1) resemble the "known-item" and "exploratory lookup" tasks of information-seeking research and give a clean automatic grader, which is a practical advantage for agent evaluation.

### S2: An interesting, actionable observation about retrieval hurting a strong model
§4.6 reports DeepSeek-R1 drops from 23.2% to 7.6% when search is enabled and offers the hypothesis that retrieved content overrides better internal knowledge; this knowledge-conflict phenomenon is of broad interest for deployment of search-augmented assistants.

### S3: Candid limitations and public release
§5 concedes size and that web answers drift over time; releasing the data and guidelines enables community use.

---

## Weaknesses

### W1: Ecological validity: questions are adversarially filtered, not drawn from real information needs
Questions were written by ten annotators, selected to defeat first-page search and then to defeat GPT-4o and DeepSeek (§3.1). They do not represent real Chinese information needs (Figure 1 shows trivia such as an actress's husband's hometown and a heritage art form). High scores would not translate to usefulness for users and low scores do not show the deployment gap the Introduction motivates ("real-world reasoning and information-seeking capabilities", §1).
- **Suggested Fix**: State the intended construct (hard deep-lookup), add a small set of naturally occurring queries from search logs or forums (with consent) and report the correlation of system rankings.

### W2: Web-environment assumptions are unexamined (platform, region, time, language)
Chinese-web difficulty is attributed to platform fragmentation and censorship-related complexities (Abstract, §1), but neither the search backend (Baidu vs Bing vs Google, region, login state) nor the temporal snapshot is controlled. Products differ in which engines and indexes they can reach (Table 1), and §5 notes answers may change. Results therefore mix retrieval-access differences with model ability.
- **Suggested Fix**: Record engine, region and date for each run; provide a frozen snapshot of the evidence pages (URLs are already collected, §3.1 "Evidence traceability") so retrieval can be evaluated offline.

### W3: Opportunity: process-level and cost analyses are missing
The study reports only final accuracy and calibration. Information-retrieval evaluation normally looks at the search trajectory (number of queries, sources visited, time or cost). §4.6 asserts DeepSeek products "perform only a single round of retrieval" without logs. Cost/latency matter for deployment of products such as DeepResearch.
- **Suggested Fix**: Log number of search calls and time per question for a subset and relate it to accuracy; link to HCI/IR literature on search effort.

### W4: Societal and privacy considerations are absent
Questions use real, named public figures' private-life details (Figure 1 film example); sources are scraped web content of varied licence status; annotator working conditions and pay are unspecified; and the public release will let future models memorize answers. No ethics or data statement is given.
- **Suggested Fix**: Add a datasheet: licence of source pages, handling of personal data, annotator compensation, and a contamination statement (canary string).

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound recipe, thin validation |
| Clarity | 3 | Easy to follow |
| Significance | 3 | A needed Chinese benchmark |
| Originality | 2 | Adaptation, new language and data |

---

## Dimension Scores (0–100)

**Pool position:** better than about 68% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful resource in a hot area with an interesting side-finding, though modest in insight and with no ecological or process analysis.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sensible but unvalidated |
| Clarity & Presentation | 74 | Competent | Clear |
| Novelty & Originality | 60 | Competent | New language and data, same recipe |
| Significance & Impact | 70 | Competent | Likely to be used for Chinese agent evaluation |
| Experimental Validation | 58 | Competent | Wide model list, shallow analysis |
| Reproducibility | 60 | Competent | Data and prompts released; products unreproducible |
| Ethical Compliance | 55 | Competent | No data/privacy/annotator statement |

---

## Questions for Authors
1. Do system rankings on this benchmark correlate with rankings on naturally occurring Chinese queries? (A positive answer would raise Significance.)
2. What search backends and regions did each product use, and on what dates?
3. Can you release a frozen evidence snapshot to separate retrieval from reasoning?

---

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**: privacy/licence details are missing but nothing here needs ethics review.

## Overall Score
**4**: Borderline Accept. A needed resource with an interesting knowledge-conflict observation; the suggestions above would turn a leaderboard into a study of search behaviour.

## Confidence
**3**: Fairly confident; outside the LLM-agent evaluation core.

---

# Peer Review Report

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Reviewer: Dr. Amara Okafor, Generalist Reviewer (university AI group, West Africa; fictional persona)
## Expertise: NLP, question answering
## Date: 2026-11-10

---

## Summary
The paper presents BrowseComp-ZH, 289 hard, short-answer, multi-constraint questions for Chinese web browsing agents, built answer-first with two quality-control stages. A table evaluates 22 LLMs and search products; the best reaches 42.9%. Four takeaways are offered on reasoning, retrieval depth, retrieval hurting some models and calibration.

---

## Strengths

### S1: Clear contribution and writing
The contribution (a Chinese BrowseComp) is stated in the first page and the paper is easy to read; Figure 1 with bilingual examples (Introduction) gives a non-Chinese reader a good sense of the questions.

### S2: Fit with the ICLR audience as a benchmark paper
ICLR has a dataset/benchmark audience; agent evaluation and search are hot topics, and the paper's difficulty level means it will remain informative for some time.

### S3: Transparent data pipeline and summary statistics
§3.2 gives the funnel and §3.3 gives topic and length distributions; Table 1 reports every number in one place, and the prompts are in the appendix.

---

## Weaknesses

### W1: The analysis section is thin for a venue like ICLR
§4.4–4.7 amount to roughly two pages: no per-topic breakdown (despite Figure 2), no analysis by question length or number of constraints (despite Figure 3), no failure-case study (deferred to "Future Work", §5), and no human reference. A reader learns a leaderboard plus four loosely supported statements. Typical accepted benchmark papers include an error taxonomy and some insight into why models fail.
- **Suggested Fix**: Add accuracy by topic and by constraint count; a manual error taxonomy for 50 failures of the top systems; a human accuracy reference.

### W2: Several statements in the text are stronger than Table 1 supports
The Conclusion says multi-turn products "further outperform purely parametric models", but Table 1 gives O1 29.1% and Gemini-2.5-Pro 27.3% above Doubao (Deep Search) 26.0% and Perplexity 22.6%. §4.7 says search "results in increased calibration errors", yet DeepResearch has 9% error against 52–78% for several non-browsing models. §4.6 says "significantly higher accuracy" with no test. Abstract mentions "censorship-related complexities" never examined.
- **Suggested Fix**: Align wording with the table or add the analysis; delete the censorship phrase.

### W3: Scale and robustness of the benchmark
289 questions with 10 authors and a single run per system limit statistical resolution (≈ ±5.7 points at 42.9%, derived), and the authors themselves list size as a limitation (§5). The ranking among the many systems in the 5–30% range is not reliable. No confidence intervals.
- **Suggested Fix**: Bootstrap CIs, mark statistically indistinguishable groups, and consider growing the set or adding a held-out private split.

### W4: Related work and presentation details
§2 is mostly a list; the positioning paragraph's claim that previous Chinese sets "lack rigorous control" is not demonstrated. Model names in §4.1 have empty parentheses, and appendix references are mislabeled (§4.2 "Appendix 4/5" vs A.1/A.2).
- **Suggested Fix**: Add a comparison table; complete model versions.

**Minor:** "representative example" → "examples" (§1); the same four findings appear in §1 and again in §4.5–4.7.

### Venue-criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | §4.6–4.7 vs Table 1 |
| Soundness: dataset quality documented | Partly | §3.2 funnel yes; no audit, no agreement |
| Presentation: clear | Met | whole paper |
| Contribution: new resource with community use | Met | §3, Table 1 |
| Reproducibility: data and prompts | Partly | A.1, A.2; products not re-runnable |

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good recipe, overclaimed analysis |
| Clarity | 3 | Clear writing |
| Significance | 3 | Useful resource |
| Originality | 2 | Adaptation |

---

## Dimension Scores (0–100)

**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a well-written resource with a clear gap that the venue's benchmark audience will use; accepted benchmark papers usually add more analysis than this, so I put it at the borderline-accept edge, not above.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasonable design, overclaimed analysis |
| Clarity & Presentation | 74 | Competent | Clear writing, minor labeling slips |
| Novelty & Originality | 58 | Competent | Adaptation |
| Significance & Impact | 64 | Competent | Useful benchmark |
| Experimental Validation | 58 | Competent | Many systems, little analysis |
| Reproducibility | 60 | Competent | Prompts present, products unreproducible |
| Ethical Compliance | 62 | Competent | Limitations present |

---

## Questions for Authors
1. Can you add topic- and constraint-level breakdowns and a failure taxonomy? (Doing so would move me toward Accept.)
2. Which of the stated analysis claims would you keep after adding CIs?
3. Will a private or periodically refreshed split be maintained against contamination?

---

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**.

## Overall Score
**4**: Borderline Accept. Clear, useful resource for the ICLR benchmark audience; I lean to accept because the weaknesses (thin analysis, overclaimed sentences) are fixable by rewording and by analyses on existing results.

## Confidence
**4**: Confident about venue norms; less so about search-agent specifics.

---

# Devil's Advocate Report

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Reviewer: Prof. Lukas Brandt, Devil's Advocate (university statistics and ML group, Central Europe; fictional persona)

---

## Steelman
A hard, short-answer Chinese browsing set is scarce; the questions were produced answer-first, checked against three engines, human peers and strong agents, and the best product reaches only 42.9%, showing room for progress. The data and prompts are public and the format makes grading cheap, so the community can adopt it immediately.

---

## Core Argument Chain
1. Existing English browsing benchmarks do not transfer to the Chinese web (§1).
2. A native Chinese reverse-designed set with two-stage QC yields hard questions with unique answers (§3.1–3.2).
3. Low accuracy of 22 systems on it shows that models lack browsing/reasoning ability for the Chinese web (Table 1, §4.4).
4. Reasoning, multi-round retrieval and retrieval/internal-knowledge reconciliation explain differences (§4.5–4.7).
∴ BrowseComp-ZH validly measures web-browsing ability of LLMs in Chinese and exposes specific limitations.

---

## Strongest Counter-Argument
Low scores do not show that the benchmark measures browsing. Three observations from the paper itself weaken step 3. First, three non-browsing models exceed 20% (R1 23.2%, O1 29.1%, Gemini-2.5-Pro 27.3%, Table 1), and O1 beats every browsing product except DeepResearch. A large fraction of items is therefore answerable from parametric memory, so the score mixes memorized knowledge, reasoning and browsing in unknown proportions; the paper's own reading (§4.4) is "the strength of high-capacity language models". Second, the items were selected adversarially against GPT-4o and DeepSeek (§3.1) and for non-ambiguity against the five strongest agents (§3.2), then the same agents are ranked on them. Low scores for GPT-4o-class models are partly by construction, and the agent-based uniqueness filter can only remove ambiguity the agents themselves produced. Third, "ground truth" has no independent check: no human solver, no sample audit, no agreement. 115 of 404 candidates (28%) were non-unique, so the rate of residual non-unique or wrong items among the 289 is plausibly not small, and every system's accuracy is capped by it. In such a case, 42.9% could be close to the achievable ceiling for ill-posed items, and "even the best system reaches just 42.9%" (Abstract) would not demonstrate a capability gap. The explanatory step 4 then rests on confounded comparisons: model generations rather than a reasoning switch, an API model versus a consumer app for "enabling search", and three-versus-three product groups with no test. Together these mean the paper establishes that the set is hard for current systems, but not what it is hard for.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main claim in its narrow form (a hard Chinese set on which current systems score low) is consistent with Table 1; the problems narrow what the benchmark can be said to measure and are fixable by additional audits and rewording, so none meets the strict criteria.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (E8/E4) | §3.2 Stage 1–2; Limitations §5 | Gold-answer validity and uniqueness unmeasured: uniqueness checked only with agents that fail most items; difficulty = unsolved by a peer in 10 minutes; no human solvability or error rate. Evidence supports only "hard", not "valid". | Independent human audit of a random sample; report gold error rate and human accuracy |
| DA-M2 | Scope/Logic | §4.4 ("exceeding 20%"), Table 1 | 23–29% accuracy without browsing shows parametric answerability; benchmark does not isolate browsing as the title and abstract state. Evidence supports a weaker claim (hard knowledge+reasoning set). | Report the "needs-browsing" subset (items that non-browsing models fail) and narrow the title/abstract claim |
| DA-M3 | Overclaiming (E5) | §4.7 vs Table 1; §5; §4.6 | Three analysis claims not supported or contradicted by Table 1: calibration rises with search (browsing mean 49.3% vs non-browsing 65.7%, derived), multi-turn products outperform parametric models (only DeepResearch does), "statistical analysis" with no test. Weaker versions hold. | Reword or add tests and matched comparisons |
| DA-M4 | Confound | §4.5–4.6 | "Reasoning" and "search" effects come from comparing different models or product vs API (R1 23.2% vs DeepSeek Deep Think 7.6%); human extraction vs regex+GPT-4o grading differ across the pair. | Controlled with/without search and with/without thinking comparisons on the same backbone |
| DA-M5 | Circularity | §3.1, §3.2 | Filtering used GPT-4o, DeepSeek, and five agents that are later ranked; no analysis of the induced bias; no contamination control; open release without canary. | Report results on unrevised items; add canary/encryption |
| DA-M6 | Overclaiming (E5) | Abstract; §1 | "censorship-related complexities" and "Crucially, directly translating English browsing benchmarks into Chinese does not yield a meaningful evaluation framework" are never tested. | Add translation control or remove |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Statistics | Table 1 | No CIs; differences of 1–5 questions (e.g., 8.0% vs 7.6%) are read as ranks. |
| DA-m2 | Reporting | Fig. 5 | "Put 100 if there is no confidence score available" may inflate calibration error. |
| DA-m3 | Reporting | §4.1 | Empty parentheses for model versions; no product dates. |
| DA-m4 | Presentation | §4.5 | "nearly 8%" for 7.3 points. |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| R1 vs V3 gain (§1) | 14.5% | 23.2 − 8.7 = 14.5 points | Yes |
| Claude-3.7 vs 3.5 (§1) | 12.2% | 17.7 − 5.5 = 12.2 points | Yes |
| Doubao Deep vs Standard (§4.5) | "nearly 8%" | 26.0 − 18.7 = 7.3 points | Loosely |
| Funnel 480 → 404 → 289 (§3.2) | 76 and 115 removed | 480−76=404; 404−115=289 | Yes |
| Topic counts (Fig. 2) | sum 289 | 18+22+10+23+7+26+45+29+40+32+37 = 289 | Yes |
| "below 10%" count (Abstract) | "a large number" | 10 of 22 rows (derived) | Yes |
| ">20%" count (Abstract) | "only a handful" | 6 of 22 rows (derived) | Yes |
| Search raises calibration error (§4.7) | increase | browsing mean 49.3% vs non-browsing 65.7% | **No** (except R1 pair: 59 → 65) |
| Multi-turn products beat parametric (§5) | outperform | Doubao 26.0 and Perplexity 22.6 < O1 29.1, Gemini 27.3 | **No** (partly) |

## Ignored Alternative Explanations
- Low scores partly reflect ill-posed or mislabeled items (no gold-error audit).
- Differences between products reflect search backend and index access (region, Baidu access) rather than agent quality.
- R1's drop with search may be due to the consumer app's system prompt, truncation or single-round retrieval rather than a "reconciliation" failure; no logs (§4.6).
- DeepResearch's lead may reflect longer compute budgets per question, not better "browsing".
- Accuracy of knowledge-heavy models tracks parameter count (O4-mini 15.2% vs O1 29.1%), not reasoning.

## Missing Stakeholder Perspectives
Chinese users and web publishers (consent and licence for scraped pages), annotators (pay and conditions), and practitioners who need process metrics (cost, latency) rather than final accuracy.

## Observations (Non-Defects)
The construction funnel arithmetic is consistent; the topic table adds up; the authors openly state that uniqueness cannot be fully guaranteed (§5); the answer format keeps grading robust to formatting; and publishing the prompt text is good practice.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Unvalidated gold labels; confounded explanatory claims |
| Clarity & Presentation | 68 | Clear but misaligned text/table claims |
| Novelty & Originality | 52 | Adaptation of BrowseComp |
| Significance & Impact | 58 | Useful if validity is shown |
| Experimental Validation | 44 | Single runs, no CI, no human reference, no matched controls |
| Reproducibility | 50 | Products not re-runnable; versions missing |
| Ethical Compliance | 55 | Limitations stated; no data statement |

**Pool position:** better than about 50% of submissions to ICLR. Deciding evidence: the evidence supports "hard set", not "measures browsing", and a typical rejected submission shares exactly this gap between claim and measurement; polish does not offset it.

## Overall: 3 | Confidence: 4

---

# Phase 1.5: Literature Check (Domain Reviewer addendum)

**Run details.** `literature check: strict`, cutoff 2025-09-24 (everything after dropped). arXiv API, 6 queries of the 12 allowed: claim queries C1 ×2, C2 ×2, C4 ×1, baseline ×1. The `coverage` gaps left open: no kept prior work from 2021; no query for C3 (the paper's own measured result, nothing external to search) and, after refusal of 5-word queries, a narrower C4 query only. The paper reports results only on its own benchmark, so there was no external benchmark to `scout`; the one baseline-purpose query (multi-hop QA) returned only methods papers from the HotpotQA era and nothing that bears on this paper. Search covers arXiv only. `similarity` flagged no text overlap (0 shared 8-grams with every candidate) and no high conceptual overlap (highest cosine 0.22 vs threshold 0.30).

**Per-claim novelty (claim-level profile, `related_search.py novelty`).**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 first native Chinese browsing benchmark | resource (central) | medium | Level-Navi Agent: A Framework and benchmark for Chinese Web Search Agents (level 3; https://arxiv.org/abs/2502.15690v1; prior arXiv-only; **cited**) | A Chinese web-search-agent benchmark already exists; what differs is difficulty control and the reverse-designed short-answer format. Chinese SimpleQA (level 2; https://arxiv.org/abs/2411.07140v2; prior; not cited) is closed-book short-answer Chinese factuality, and WebWalker (level 2; https://arxiv.org/abs/2501.07572v3; prior; not cited) is website-traversal QA; neither is a browsing benchmark of this kind |
| C2 two-stage QC for difficulty and uniqueness | method (central) | high | Chinese SimpleQA (level 2; same link; not cited) | Shares the idea of a multi-step QC for a short-answer Chinese set; the human+agent uniqueness procedure is specific to this paper |
| C4 retrieval can degrade a strong model | result (non-central) | medium | Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation (level 3; https://arxiv.org/abs/2307.11019v3; prior arXiv-only; not cited) | Retrieval changing or hurting correct parametric answers is a known phenomenon; the paper presents it as a counter-intuitive finding from one product comparison |

Script reading: "no central claim fully covered by prior work". Attribution: Level-Navi Agent (closest prior work, cited). No claim is "known"; the "first" wording in C1 should be narrowed to the precise intersection (hard, reverse-designed, short-answer, Chinese web browsing).

**Novelty delta table (closest prior works).**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| Chinese web-browsing benchmark | Level-Navi Agent (arXiv 2502.15690) | Chinese web-search-agent framework and benchmark | Harder, reverse-designed, verifiable short answers, broader model/product coverage | Cited; dismissed in §2 as lacking "rigorous control over task difficulty and answer accessibility" with no evidence |
| Short-answer Chinese factual evaluation with QC | Chinese SimpleQA (arXiv 2411.07140) | Chinese closed-book short-form factuality with QC | Browsing-needed, multi-constraint, hard-to-search items | Not cited |
| Browsing difficulty via entangled constraints | BrowseComp (arXiv 2504.12516; cited by the paper; labelled **recent preprint** under the strict 6-month rule, so discussion only) | English version of the same recipe | Chinese construction | Cited and acknowledged as inspiration |

**Baseline scout.** Not applicable (no external benchmark). Worth discussing, never required: ManuSearch (open multi-agent deep-search framework, 2025-05, recent preprint) and DeepDive (deep search agents with multi-turn RL, 2025-09-12, concurrent) would give open, controllable agents for the matched search/no-search comparison asked for in R1-W2.

**Field snapshot (as of the cutoff).** Three to five years ago, search-related LLM evaluation relied on Wikipedia-based multi-hop QA (HotpotQA-style sets) and RAG benchmarks, where many answers could be found with one keyword search. Over 2024–2025 the focus moved to agentic search: web-traversal sets (WebWalker), Chinese-language search-agent and factuality benchmarks (Level-Navi, Chinese SimpleQA) and, from April 2025, hard, entangled-constraint browsing sets with short verifiable answers (BrowseComp). Commercial deep-research products are the strongest systems, and open-source agents still lag. Open problems named in this literature are controlled comparisons of open agents with a fixed search tool, knowledge conflicts between retrieved and parametric information, and contamination of public web benchmarks. What counts as significant now for a new benchmark: demonstrated validity of gold answers (human audit, agreement), separation of browsing from parametric knowledge, controlled agent baselines and some diagnostic insight; a new language or domain version of an existing recipe is welcome but sits at the incremental-to-medium end. This calibrates Novelty at 55–60 and Significance in the mid-60s.

**Missing references (citation-integrity rule; each checked with `related_search.py verify`).**
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Yancheng He et al., "Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models", arXiv 2024 (https://arxiv.org/abs/2411.07140; verified) | Closest Chinese short-answer factuality benchmark with a stated QC process; needed to position the new set and its quality control |
| Important | Jialong Wu et al., "WebWalker: Benchmarking LLMs in Web Traversal", arXiv 2025 (https://arxiv.org/abs/2501.07572; verified) | Prior web-agent benchmark that the related work does not mention |
| Helpful | Ruiyang Ren et al., "Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation", arXiv 2023 (https://arxiv.org/abs/2307.11019; verified in search results) | Prior analysis of how retrieval affects answers a model already knows; relevant to the R1 search-hurts finding |
| Helpful | Zhuoran Jin et al., "Tug-of-War Between Knowledge: Exploring and Resolving Knowledge Conflicts in Retrieval-Augmented Language Models", LREC-COLING 2024 (https://arxiv.org/abs/2402.14409; verified in search results) | Knowledge-conflict framing for the §4.6 hypothesis |
No prior work qualifies as Critical. The DA raised no criterion-7 issue.

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 "Low GPT-4o accuracy (6.2%) is partly by construction" | Rewritten (kept) | §3.1 filtering ran GPT-4o in web-search mode while Table 1 evaluates it without browsing; direction plausible, magnitude unknown. Treated as a question about bias |
| R1 | ERR-4 ("nearly 8%" for 7.3 points) | Moved to Minor | Cosmetic |
| R1 | §4.2 "Appendix 4/5" labels | Moved to Minor | Cosmetic |
| R2 | W3 speculation about government/CNKI-type sources | Rewritten | Unsupported by the paper; kept only as the request for per-topic results |
| R3 | S2 (R1-vs-DeepSeek as "interesting observation") | Flagged for EIC | Comparison is API model vs consumer product (Table 1); bears on R3's weight |
| R3 | W3 "§4.6 asserts DeepSeek products single round" | Rewritten | The statement is at §4.5 (and §4.6 relies on it); location corrected |
| R3 | W4 privacy/licence | Kept | Paper has no data or ethics statement after search |
| R4 | W4 model-name and appendix-label slips | Moved to Minor | Cosmetic |
| DA | DA-M2 "benchmark does not isolate browsing" | Rewritten | Numbers verified; the memorization inference is plausible but not demonstrated, so it is a MAJOR concern about the construct, not a finding |
| All others | — | Kept | Specific, located, not answered by the paper, actionable |

Scores unchanged.

# Phase 2: Synthesizer Package, EIC Meta-Review and Decision

## Synthesizer Part A: package for the EIC

**Official score run (before EIC weights; no DA-CRITICAL issue raised, `da_critical: []`):** ratings R1 3, R2 4, R3 4, R4 4, DA 3 → plain mean **3.6**; official composite **59.7**; per-reviewer composites R1 56.2, R2 62.8, R3 63.8, R4 62.4, DA 53.2; no consistency warnings, no dimension spread above 20 (largest 14: Technical Rigor and Experimental Validation).

**Merged issue list.**
| ID | Issue | Sources | Class | Hinge? |
|----|-------|---------|-------|--------|
| I1 | Gold-answer validity, uniqueness and difficulty not independently audited; no human baseline or agreement | R1-W1, DA-M1, R4-W1 | CONSENSUS-3 | **Yes** |
| I2 | Statements contradicted or unsupported by Table 1 (search ⇒ higher calibration error; multi-turn products outperform parametric models; "significantly" without a test) | R1-W2/ERR-1..3, R4-W2, DA-M3 | CONSENSUS-3 | **Yes** |
| I3 | Reasoning and search effects estimated from confounded pairs (generations, API vs consumer product) | R1-W2, DA-M4, R2-W4 | CONSENSUS-3 | Yes |
| I3b | R3 praises the R1/DeepSeek search drop as an interesting finding; R1 and DA show the comparison is confounded | R3-S2 vs R1-W2, DA-M4 | SPLIT | n/a |
| I4 | Single run; no CIs; ranks differ by 1–5 questions | R1-W3, R4-W3, DA-m1 | CONSENSUS-3 | No |
| I5 | Browsing not isolated from parametric knowledge (>20% without browsing) | DA-M2, R2-W3 (R1-Q2) | CONSENSUS-2 | **Yes** |
| I6 | Product evaluation not reproducible (no dates/versions, human extraction, grader unvalidated, default-100 confidence) | R1-W4, R3-W2, R4-W4, DA-m2/m3 | CONSENSUS-4 | No |
| I7 | Thin analysis (no per-topic, constraint or failure analysis; no process metrics) | R4-W1, R2-W3, R3-W3 | CONSENSUS-3 | No |
| I8 | Chinese-specific difficulty and "censorship" asserted, not tested; positioning thin | R2-W1/W2, DA-M6 | CONSENSUS-2 | No |
| I9 | Filtering against evaluated systems; contamination; open release without canary | R1-W5, DA-M5, R3-W4 | CONSENSUS-3 | No |
| I10 | Ecological validity; ethics/data statement | R3-W1, R3-W4 | SOLO | No |

**DA-CRITICAL issues:** none raised ("No CRITICAL issues found"). **Integrity signals:** none; no text overlap.

## EIC Meta-Review (Dr. Ingrid Solheim; step 1: read all five reports and the package first)

### The Case For and Against
- **For acceptance:** A hard, short-answer, verifiable benchmark for the Chinese web fills a real gap that the ICLR benchmark audience will use; construction counts are consistent (480 → 404 → 289; Figure 2 counts sum to 289); Table 1 spans 22 systems with real headroom (best 42.9%); prompts and the grader prompt are in the appendix; limitations about size and uniqueness are admitted (§5). For a first paper on this setting, the task is clearly valuable.
- **Against acceptance:** What the benchmark measures is not validated: gold answers and uniqueness rest on an agent-based check with no human audit or agreement, three non-browsing models score above 20%, and the filtering involved the very systems that are ranked. The analysis (§4.4–4.7) is thin and three of its statements are unsupported or contradicted by Table 1, with confounded comparisons and no uncertainty estimates. The novelty over BrowseComp is the language and data only.

### Verification of Decisive Points (step 2: EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Search products have lower, not higher, calibration error: browsing mean 49.3% (9 rows) vs non-browsing 65.7% (13 rows), DeepResearch 9% | R1 ERR-1, R4-W2, DA-M3 | §4.7 vs Table 1 | Verified | Recomputed by me. The R1 59 → DeepSeek 65 pair supports the sentence; the table as a whole does not |
| Multi-turn products "outperform purely parametric models" | R1 ERR-2, DA-M3 | §5 vs Table 1 | Verified | Doubao Deep 26.0 and Perplexity 22.6 are below O1 29.1 and Gemini-2.5-Pro 27.3; only DeepResearch is above all |
| "Statistical analysis shows … significantly higher accuracy" with no test | R1 ERR-3, DA-M3 | §4.6 | Verified | Text search finds no test, CI or p-value anywhere in the paper |
| No independent audit of gold answers or uniqueness; difficulty = unsolved in 10 minutes | R1-W1, DA-M1 | §3.2 Stage 1–2, §5 | Verified | Uniqueness check used five AI agents; 115 of 404 (28%) rejected; no agreement or human accuracy reported |
| Non-browsing models above 20% show parametric answerability | DA-M2, R2-W3 | §4.4, Table 1 (23.2, 29.1, 27.3) | Partly correct | Numbers verified; that these items are memorized (rather than solved by reasoning over remembered facts) is an inference. The consequence stands: the set does not isolate browsing |
| GPT-4o's 6.2% is "partly by construction" | R1-W5, DA | §3.1 vs Table 1 | Overstated | §3.1 filtered with GPT-4o in web-search mode; Table 1 runs it without browsing. Bias direction plausible, size unknown |
| R1 23.2% (API) vs DeepSeek (Deep Think) 7.6% is "enabling web search" | R3-S2 (accepts), R1-W2, DA-M4 (reject) | §4.6, Table 1 | Verified as confounded | Different systems, prompts and answer extraction (human vs regex+GPT-4o). R3's strength is overstated |
| "Censorship-related complexities" never examined | R2-W1, DA-M6 | Abstract; text search | Verified | The word appears only in the abstract |
| Model strings "Claude-3.5-Sonnet()", "Gemini-2.0-Flash()"; no product dates | R1-W4, DA-m3 | §4.1 | Verified | |
| Grader default confidence of 100 | R1-W4, DA-m2 | Fig. 5 | Verified (quote) / effect unknown | Frequency of missing confidences not reported |
| "§4.6 asserts DeepSeek single round" | R3-W3 | §4.5 | Partly correct | Statement is in §4.5 ("perform only a single round of retrieval"); location corrected |

Error-log entries ERR-1, -2, -3 hold at their locations; ERR-4 is cosmetic.

### Reviewer Weights (step 3; every reviewer started at 1.0)
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Error-log entries and recomputed claims verified; one overstatement (GPT-4o "by construction") |
| R2 (Domain) | 4 | 4 | 1.0 | Sound positioning points, all located; no decisive check moved the weight (the CNKI-type speculation was marginal) |
| R3 (Perspective) | 4 | 3 | **0.75** | Accepted the confounded R1-vs-DeepSeek comparison as a strength (R3-S2), mislocated one statement, and most points are generic; the rating does not account for the table contradictions |
| R4 (Generalist) | 4 | 4 | 1.0 | Caught the Table 1 contradictions and thin analysis; balanced |
| DA | 3 | 4 | **1.25** | Counter-argument and numbers verified against Table 1; correctly withheld CRITICAL; one inference (memorization) flagged as plausible only |

### DA-CRITICAL Rulings (step 4)
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a. I also checked the DA's candidates against the strict criteria: the evidence supports a weaker claim ("hard set"), it does not contradict the main claim; the adversarial filtering is not criterion-3 leakage (no method is tuned on a test set); no fabrication signal | No ceiling | n/a |

### Final Decision and Justification (steps 5–6)
**Scores.** Official ratings R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60; official composite 59.7. With my weights (confidence × quality weight: R1 1.06, R2 0.85, R3 0.53, R4 0.85, DA 1.06) the **EIC-weighted rating is 3.51 → starting point 4** (rounded half up) and the EIC weighted composite is 58.9, band 3 (Borderline Reject). The two signals sit on either side of a boundary (the rating is 0.01 above 3.5; the composite is 1.1 below 60), so by the skill's own rule neither disagreement by itself justifies a departure. DA ceiling: none.

**Decision: Borderline Reject (3), one step below the starting point.** I depart for named, verified issues that the accept-leaning ratings did not account for: (i) the three Table-1 contradictions (I2, verified above) appear in no R2 or R3 report and are why R3's weight is reduced; and (ii) the gold-answer validity gap (I1) and the unisolated browsing construct (I5) mean the paper's central claim, that the set measures LLM browsing ability, is not tested, which is one of the rubric's signals of a typical rejected submission. My pool position is **58**: better than about 58% of ICLR submissions, in the borderline range (55–69). The deciding evidence points to the lower side: a first, useful benchmark for a new setting deserves credit and is why I am not at 2, but accepted benchmark papers at this venue usually validate their labels and add some diagnostic insight, and here the validation is missing and the diagnostic claims partly contradict the paper's own table. None of the issues is fatal: nearly all can be fixed with a human audit (≈30–40 annotator-hours), bootstrap CIs, subset analyses on existing outputs, rewording, and one matched search/no-search experiment. I would expect a revision with these to move the paper to Borderline Accept or Accept. There is no DA ceiling. Simulation only: this describes how a careful panel would likely see this draft.

**Venue translation (ICLR, scale status secondary; label from `aggregate_scores.py --final 3`).** Soundness 2, Presentation 3, Contribution 2; rating **4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})**, i.e., just below the acceptance line on either scale. The script's ICLR-weighted composite is 59.7 (official) / 58.9 (EIC).

---

# Editorial Decision

## Paper: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese
## Submission ID: iclr26-LDGAjUuEVZ (blinded)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: benchmark
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Ingrid Solheim; R1 Methodology Prof. Rahul Venkataraman, R2 Domain Dr. Mei-Ling Zhou, R3 Perspective Dr. Tomás Aguirre, R4 Generalist Dr. Amara Okafor, DA Prof. Lukas Brandt

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60 · official composite 59.7
**EIC assessment** (internal): weighted rating 3.51 → starting point 4 · weighted composite 58.9 → band 3 (cross-check) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR rating label:** 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Soundness 2, Presentation 3, Contribution 2.

## Score Summary

### Official Scores and EIC Assessment (from `aggregate_scores.py`, with EIC weights)
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 62 | 62 | 60 | 48 | 56.8 | 55.7 | 14 |
| Clarity & Presentation | 70 | 72 | 74 | 74 | 68 | 71.6 | 71.2 | 6 |
| Novelty & Originality | 55 | 58 | 60 | 58 | 52 | 56.6 | 56.0 | 8 |
| Significance & Impact | 62 | 66 | 70 | 64 | 58 | 64.0 | 63.2 | 12 |
| Experimental Validation | 48 | 58 | 58 | 58 | 44 | 53.2 | 52.1 | 14 |
| Reproducibility | 50 | 60 | 60 | 60 | 50 | 56.0 | 55.1 | 10 |
| Ethical Compliance | 58 | 62 | 55 | 62 | 55 | 58.4 | 58.5 | 7 |
| **Composite** | 56.2 | 62.8 | 63.8 | 62.4 | 53.2 | **59.7 (before)** | **58.9 (after)** | |

Reviewer pool positions: R1 55, R2 66, R3 68, R4 65, DA 50; EIC 58.

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese" to ICLR. A hard, verifiable benchmark for browsing agents in Chinese is a worthwhile and timely goal.

**Overall Assessment:** The panel agrees that the resource is useful, clearly presented and genuinely difficult for current systems. It was not persuaded that the paper yet shows what the benchmark measures, and several analytic statements go beyond Table 1.

**Key Strengths Identified by Reviewers:**
1. A clear funnel with stated counts and consistent arithmetic (R1, R4), and prompts in the appendix (R1, R4).
2. Fills a real language gap with native Chinese construction and broad coverage including Chinese products (R2, R3, R4).
3. Real headroom: 4.8% to 42.9% across 22 systems (R1, R4).

**Key Concerns Requiring Attention:**
1. Gold-answer validity and uniqueness are checked only by AI agents; no human audit, agreement or human baseline (R1, DA, R4; CONSENSUS-3).
2. Claims contradicted or unsupported by Table 1: search raising calibration error, multi-turn products outperforming parametric models, "statistical analysis … significantly" without a test (R1, R4, DA; CONSENSUS-3).
3. Reasoning and search effects come from confounded comparisons; one reviewer found the DeepSeek-R1 observation interesting while two showed it compares an API model with a consumer product (SPLIT).
4. Three non-browsing models exceed 20%, so browsing is not isolated; no variance estimates; thin analysis (DA, R2, R4).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection is that low scores show the set is hard but not what it is hard for: parametric knowledge, filtering against the evaluated systems and possibly ill-posed items all contribute, and the explanatory step of the paper rests on confounded pairs. The authors need to address it with the audit and controls below.

**Decision: Borderline Reject (3).** The contribution is useful and the problems are fixable, but the paper's central measurement claim is not yet tested and parts of its analysis do not follow from its own table. A revision that adds a human audit of the gold answers, a browsing-needed subset, bootstrap CIs, one controlled search/no-search comparison and corrected claims would likely change this assessment. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Ingrid Solheim
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Product evaluation not reproducible (dates, versions, human extraction) | R1, R3, R4, DA | CONSENSUS-4 |
| Gold-answer validity / human audit missing | R1, R4, DA | CONSENSUS-3 |
| Claims unsupported or contradicted by Table 1 | R1, R4, DA | CONSENSUS-3 |
| Confounded reasoning/search comparisons | R1, R2, DA | CONSENSUS-3 |
| No variance / CIs | R1, R4, DA | CONSENSUS-3 |
| Thin analysis | R2, R3, R4 | CONSENSUS-3 |
| Filtering against evaluated systems; contamination | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| R1-vs-DeepSeek search drop is an "interesting, actionable observation" | R3 | R1, DA | Against: Table 1 compares an API model with a consumer product; the observation is a hypothesis, not a finding |
| Accept-leaning (4) vs reject-leaning (3) overall | R2, R3, R4 | R1, DA | Weighted mean 3.51; I depart one step down on verified issues missing from the accept-leaning reports (see Final Decision) |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. The widest (14 points: Technical Rigor, Experimental Validation) separates R1/DA (44–52) from R2–R4 (58–62); I side with the lower values on Experimental Validation because the absence of a human audit, CIs and matched controls is verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | None raised | n/a | n/a | n/a |
| DA-M1 | MAJOR | Gold validity and uniqueness unmeasured | Yes (R1, R4) | n/a | New annotation (small) |
| DA-M2 | MAJOR | Browsing not isolated from parametric knowledge | Partly (R2) | n/a | Analysis of existing outputs |
| DA-M3 | MAJOR | Claims contradicted or unsupported by Table 1 | Yes (R1, R4) | n/a | Rewording / tests |
| DA-M4 | MAJOR | Confounded reasoning/search pairs | Yes (R1, R2) | n/a | New controlled runs |
| DA-M5 | MAJOR | Circular filtering, contamination | Yes (R1, R3) | n/a | Analysis + canary |
| DA-M6 | MAJOR | "Censorship" and translation claims untested | Yes (R2) | n/a | Rewording or small experiment |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Verified issues that undermine a main claim (no upheld DA-CRITICAL issue exists, so no ceiling applies).*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Gold answers and uniqueness not independently validated; no human baseline | R1-W1, DA-M1, R4-W1 | §3.2, §5 | Two independent annotators solve a random 60–100 items; report gold error rate, agreement, human accuracy and time | Medium; ≈ 30–40 annotator-hours | Yes |
| P1-2 | Statements not supported by Table 1 | R1 ERR-1..3, R4-W2, DA-M3 | §4.6, §4.7, §5 | Reword to what the table shows (only DeepResearch beats the best parametric models; calibration claim limited to R1/DeepSeek, discuss DeepResearch 9%); remove "significantly" or add a test | Low | Yes |
| P1-3 | Browsing not isolated from parametric knowledge | DA-M2, R2-W3 | §4.4, Table 1 | Report accuracy on the subset that non-browsing models fail; temper title/abstract claims accordingly | Low (existing outputs) | Yes |
| P1-4 | No uncertainty; ranks within noise | R1-W3, R4-W3, DA-m1 | Table 1, §4.4 | Bootstrap 95% CIs over questions; 3 samples per API model; mark indistinguishable groups | Low–Medium; ≈ 3× current API cost | Yes (CIs); partly (repeats) |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Confounded reasoning/search comparisons | R1-W2, DA-M4, R2-W4, I3b | Matched with/without-search runs on one or two open models with a fixed search API; state thinking settings | Medium; a few GPU-days | Partly |
| S2 | Product evaluation not reproducible | R1-W4, R3-W2, R4-W4, DA-m2/m3 | Dates, versions, regions, annotator counts; audit of ≥100 grader outputs; fraction of missing confidences | Low–Medium | Yes |
| S3 | Filtering against evaluated systems; contamination | R1-W5, DA-M5, R3-W4 | Report results on items not revised against GPT-4o/DeepSeek; add canary or encrypted release | Low | Yes |
| S4 | Chinese-specific difficulty and "censorship" untested | R2-W1, DA-M6 | Translation control on a sample or delete the claims; per-platform tags | Low–Medium | Partly |
| S5 | Thin analysis | R4-W1, R2-W3, R3-W3 | Per-topic and constraint-count breakdowns; failure taxonomy over 50 failures; search-call counts for a subset | Medium | Partly |
| S6 | Positioning and missing references | R2-W2, Phase 1.5 | Comparison table of Chinese and web-agent benchmarks; cite Chinese SimpleQA and WebWalker; narrow "first" | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Ecological validity | R3-W1 | Small natural-query set; correlate rankings |
| N2 | Data statement (licences, personal data, annotator pay) | R3-W4 | Add a datasheet |
| N3 | Knowledge-conflict references | Phase 1.5 | Cite prior retrieval-vs-parametric analyses when discussing §4.6 |
| N4 | Minor slips | R1, R4, DA-m4 | "7.3 points", "Appendix 4/5" → A.1/A.2, complete model strings |

## Estimated Revision Effort
- Priority 1: 4 items, about 3–5 days (annotation is the long pole)
- Priority 2: 6 items, about 1–2 weeks including controlled runs
- Priority 3: 4 items, 1–2 days
- **Total estimated revision time**: about 2–3 weeks

*Simulation note: this is how a careful panel would likely see this draft, not a prediction of any real outcome. Figures were not available and were judged from captions and text only.*
