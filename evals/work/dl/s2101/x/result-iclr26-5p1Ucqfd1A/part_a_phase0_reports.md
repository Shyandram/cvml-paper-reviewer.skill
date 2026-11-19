# Academic Paper Review: CRAG-MM (ICLR, full mode)

*Date: 2026-11-10 · Simulation of how a careful panel would likely see this draft; not a prediction of any outcome. Reviewer personas are fictional. The five reviewers are five sequential role passes sharing one model context (no subagents ran); independence was kept by writing each report before reading the next and by giving the Phase 1.5 literature check only to the Domain Reviewer's addendum. Figures were not available: figure-dependent claims are judged from captions and text only.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark |
| Primary Discipline | ML / multimodal LLMs → retrieval-augmented generation and visual question answering benchmarks |
| Secondary Discipline(s) | Information retrieval; wearable / egocentric computing; evaluation methodology (LLM-as-judge) |
| Paper Type | Benchmark (with a new dataset); composite weights: benchmark |
| Core Technique(s) | Mock image-KG search (CLIP ViT-L/14@336px + ChromaDB), mock web search (BGE chunk embeddings), MM-LLM baselines, LLM-as-judge (GPT-4o), truthfulness metric (accurate = +1, missing = 0, incorrect = −1) |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status: secondary). Literature check: strict, cutoff 2025-09-24 |
| Venue-Specific Notes | Public reviews; revised PDF can be uploaded during discussion; rating on {0,2,4,6,8,10}; Soundness / Presentation / Contribution on 1–4 |
| Paper Maturity | Submission-ready (full paper with 10 main pages plus appendix A–D) |
| Ethics-Relevant Content | Images captured by vendors with smart glasses "in their daily lives" (§3.1); web-scraped pages (App. A.5.3); images from public sources. No consent, privacy, bystander or licence statement found after search |

### Claimed Contributions (as stated by the authors)
1. **C1 (problem/resource):** "the first comprehensive benchmark that focuses on wearable AI use cases" and "the first publicly released benchmark capable of effectively evaluating multi-modal RAG" (§1; Abstract; §6).
2. **C2 (resource):** 6.5K single-turn (image, question, answer) triplets and 2K multi-turn conversations over 13 domains, 6.2K egocentric images, with five image-quality issues, six question types, entity popularity, "information dynamism" and turn count (Abstract; §3; Tables 2–3).
3. **C3 (resource):** Three tasks (single-source, multi-source, multi-turn), each with a mock image-KG API (68K entries) and a web-search API (800K pages) for fair comparison (§2.2, §3.3, App. A.5).
4. **C4 (result):** Straightforward RAG reaches 32% / 43% truthfulness (single / multi-turn); industry solutions 32% / 45%, "underscoring ample room for improvement" (Abstract; Tables 4–5; §5).
5. **C5 (impact):** KDD Cup 2025 hosting, "nearly 1K participants and 5K submissions", winners improve over baseline by 28% (Abstract; §1; §5.2).

## Paper memory (factual record, shared with all reviewers)

- **Setup facts.** Splits: 30% validation / 30% public test / 40% private test, after holding out "two domains for private test only" (§3.4); which two domains and the split sizes are **not stated** (searched). Validation and public test released on HuggingFace (§3.4; link removed). Backbones: Llama-3.2-90B/11B-Vision, Gemini-2.5-Flash, GPT-5-mini (+ five more in Tables 8–9). Retrieval baseline: top-30 images, similarity threshold 0.75, 2K-token image context, 8K-token web context (§5.1, App. C.1). Judge: GPT-4o, answers truncated to 75 tokens, ~20 in-context examples (App. B.1). Industry runs: GPT-5-2025-08-07, Gemini-2.5-Pro, Claude-Sonnet-4-20250514 via API with search tools, 2025-09-01 to 2025-09-10 (App. D). Seeds / temperature / decoding / number of runs: **not stated** (searched). Compute: not stated. Hyperparameter-selection split for the baseline settings: **not stated** (searched "select/tun/threshold").
- **Headline numbers and sources.** 32%/43% ← Table 4 (31.5 Task 2 GPT-5 Mini; 42.5 Task 3 GPT-5 Mini). 32%/45% ← Table 5 (GPT-5 32.2 / 45.0). "+28%" ← Table 5 (winning team 19.7 vs Llama 3.2 11B RAG −8.6) and §5.2 ("+28% for single-turn and +18% for multi-turn"). 37% / 50% / 63% accuracy ← Tables 4–5. 99.1% judge accuracy ← Table 7. 79% egocentric ← Table 2 (6248 / 7943). 52% KG recall (51.9) and 89% web recall (88.6) ← Fig. 3.
- **Appendix additions.** A: image-quality definitions (Table 6), KG- and web-based QA construction, mock-API construction, recall by image type (Fig. 6), API code. B: judge prompt and Table 7. C: baseline implementation, prompts, nine-model Tables 8–9, slice results (Fig. 7). D: industry-system versions, tool settings, prompts.
- **Unverifiable parts.** Figures 1–7 not seen (extracted text of Figs. 3, 4, 6, 7 is garbled); benchmark and HuggingFace links removed; the KDD Cup leaderboard is external. No supplementary file is referenced.

**Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters found; reviewers read the redacted copy (identical to the paper text). `injection_found`: none.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ingrid Solheim, senior area chair profile (Europe)
- **Seniority / Expertise**: Senior faculty / multimodal LLM evaluation, benchmark design, dataset papers
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Calibrates to what the venue actually accepts; weights verified evidence over tone

### Reviewer 1 (Methodology): Dr. Tomasz Wieczorek, mid-career, ML evaluation group, large public research university (Central Europe)
- **Seniority / Expertise**: Mid-career / benchmark construction and annotation quality; LLM-as-judge validity; retrieval evaluation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes tables, insists on confidence intervals and validated judges

### Reviewer 2 (Domain): Prof. Amara Okonkwo-Reyes, senior faculty, language and vision group (West Africa / Latin America research collaboration)
- **Seniority / Expertise**: Senior faculty / knowledge-based VQA, multimodal RAG, entity-centric QA
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work closely; checks that "first" claims survive a literature scan

### Reviewer 3 (Perspective): Dr. Kenji Hayashida, industry human-computer interaction lab (East Asia)
- **Seniority / Expertise**: Senior industry scientist / wearable and always-on devices, privacy, voice interfaces
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks how the benchmark maps to what a user of smart glasses actually experiences

### Reviewer 4 (Generalist): Dr. Priya Raghunathan, postdoc, vision-and-language lab, public research university (South Asia)
- **Seniority / Expertise**: Postdoc / vision-language models, VQA, general ML
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads like a typical program-committee member; weighs weaknesses against the contribution

### Devil's Advocate: Prof. Daniel Mbeki-Larsen, senior faculty, evaluation methodology and causal inference (Southern Africa / Northern Europe)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, measurement validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks "does the measurement show what the headline says?"

*Personas are fictional. Assumptions: venue ICLR stated by the user; paper type benchmark.*

---

## Phase 1: Independent Reviews

# Peer Review Report

## Paper: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
## Reviewer: Dr. Tomasz Wieczorek, Reviewer 1 / Methodology (ML evaluation group, large public university, Central Europe; fictional persona)
## Expertise: benchmark construction and annotation quality; LLM-as-judge validity; retrieval evaluation
## Date: 2026-11-10

---

## Summary
The paper builds a benchmark for question answering about images taken with smart glasses, where answers need outside facts. It supplies 6.5K single-turn questions and 2K multi-turn conversations, mock image-KG and web-search APIs, a truthfulness metric (correct +1, missing 0, wrong −1) scored by a GPT-4o judge, and baseline results for nine multimodal LLMs, three industry systems and KDD Cup winners. The headline finding is that both simple RAG pipelines and industry systems reach only about 32% truthfulness in the single-turn setting.

---

## Protocol sweep (Step 0)
Searched the full text (terms: select, tuned, hyperparameter, checkpoint, threshold, validation, test set). Statements found: "We released the validation and public test sets on HuggingFace" (§3.4); "performance of visual QA systems on the CRAG-MM public test set" (§5); "results from winning teams were reported on the private test set, while the other solutions used the public test set" (§5.2). **No statement** about how the baseline settings (threshold 0.75, top-30, 2K/8K token budgets; §5.1, App. C.1) or prompts were chosen, or on which split. No training or selection on the reported split is *stated*; the selection protocol is *not stated after search*.

## Claim-to-evidence map (compressed)

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | first comprehensive wearable / first MM-RAG benchmark | §1, Abstract, §6 | Table 1 (columns chosen where only CRAG-MM has all ✓) | Partially: wearable framing supported by 6.2K egocentric images; "first ... multi-modal RAG" is weakened by Table 1's own WebQA row (footnoted as prefetched retrieval) |
| C2 | diversity along image quality, question type, popularity, **dynamism**, turns | Abstract; Tables 2–3 | Tables 2–3, Fig. 4 | Partially: no dynamism dimension is defined or analysed anywhere |
| C3 | fair, realistic retrieval environment (1:20 and 1:2 relevant:irrelevant) | §1, §3.3, App. A.5 | Fig. 3; App. A.5.1, A.5.3 | Partially: coverage and ratios are by construction; "mimic real-world" not validated |
| C4 | 32%/43% vs 32%/45%, "ample room" | Abstract, Tables 4–5 | Tables 4–5 | Numbers verified; interpretation confounded (different models, split, retrieval) |
| C5 | winners improve baseline by 28% | Abstract, §5.2 | Table 5 | Verified as 28.3 points, but across different splits and driven by abstention |

---

## Strengths

### S1: Transparent and reproducible evaluation environment
The judge prompt (App. B.1), all baseline prompts (App. C.2), the retrieval settings (App. C.1) and exact industry model versions, tool configs and call dates (App. D) are given. This is above the norm for benchmark papers and makes the numbers in Tables 4–5 auditable.

### S2: Reporting accuracy, missing and hallucination separately
Tables 4, 5, 8, 9 give Acc./Miss./Hallu./Truth. instead of a single score, so abstention behaviour is visible. I checked the single-turn rows: Acc + Miss + Hallu ≈ 100 and Truth = Acc − Hallu hold in every row of Tables 4, 5 and 8.

### S3: Broad baseline coverage
Nine MM-LLMs with and without retrieval (Tables 8–9), plus industry APIs and KDD Cup winners, give a useful reference spectrum. The authors also state that the Table 5 comparison is "not fully comparable" (§5.2).

### S4: Table 2 and Table 3 are internally consistent
I recomputed every row and column total of Table 2 (e.g. 5143+267+191+370+116+161 = 6248; grand total 7943) and Table 3 (e.g. column total 462+2614+928+977+772+709 = 6462; multi-turn 1956). All match the text ("6.5K", "2K", "79% egocentric": 6248/7943 = 78.7%).

---

## Weaknesses

### W1: No evidence that the labels are correct
Ground truth for web-based questions is written by annotators who also write the search query (§3.2, App. A.4); multi-turn conversations are generated by Llama-3.2-90B-Vision-Instruct and then "reviewed" (§3.2); KG-based answers are "the associated attribute values" (App. A.3). The paper gives no number of annotators, training, agreement, share of items removed or revised, or an audit of the final answers. The KG attribute values are raw wikitext in the API example (`'roof': '{{convert|870|ft|m|0|abbr|=|on}}'`, App. A.5.4), so answer fields may be noisy. For a benchmark whose headline is "models fail", unverified labels are the first alternative explanation.
- **Suggested Fix**: Report annotator counts and instructions, double-annotate a random 300–500 items and give agreement and error rate, and report the share of LLM-generated turns removed. Cost: roughly 2–3 annotator-days.

### W2: The judge is validated with a headline that hides its weak class
§4 and Table 7 report "99.1%" accuracy, but that is the mean of three one-vs-rest accuracies, one of which ("Missing", 100%) is trivial. The class that drives hallucination counts is weak: "Incorrect" precision is 68.1 (F1 78.2) and "Accurate" recall is 90.8. The size and source of the validation set, which systems' answers it contains, and whether a GPT-4o judge was validated on GPT-5 / GPT-5-mini answers (systems the judge may favour) are not stated. Because an incorrect label costs −1 and a correct label +1, a judge that under-credits 9% of correct answers moves truthfulness by about twice that share of the questions: for a system with 62.7% accuracy (Table 5, GPT-5), if the missed 9.2% were labelled Incorrect, accuracy would drop by about 5.8 points and hallucination rise by about 5.8, i.e. an ≈ 11-point truthfulness swing (derived, illustrative; true error flow is not reported). This is the same size as the gaps the paper draws conclusions from (e.g. 32.2 vs 31.5).
- **Suggested Fix**: Report judge validation per system family with n, a confusion matrix, human-vs-judge truthfulness difference per system, and a second judge from a different vendor on a sample.

### W3: Headline comparisons mix splits, retrieval worlds and models
Table 5 compares the winning team (private test) with other rows (public test) (§5.2: "results from winning teams were reported on the private test set"); the private set also contains two domains absent from public data (§3.4). The abstract nonetheless reports that winners improved "baseline performance by 28%", which Table 5 shows as 19.7 − (−8.6) = 28.3 absolute points, not a relative gain. Accuracy actually fell (35.3 → 29.3) while hallucination fell 43.9 → 9.6, so the gain is almost entirely abstention. Likewise "industry solutions have similar quality (32%/45%)" compares GPT-5 with its own live web search to GPT-5-mini with the authors' curated corpora; reasoning effort and decoding settings are not stated (App. D).
- **Suggested Fix**: Re-run the straightforward baseline and one winner on the same split; state "+28 points"; report the always-abstain reference (truthfulness 0) in Tables 4–5; give reasoning-effort/decoding settings.

### W4: No variance, and the slice-size statement does not hold at the evaluated sizes
All results are single runs without intervals. §3.2 states "The size of each slice allows us to get metrics with <5% margin-of-error (with 95% confidence level) for most of the slices". A ±5% margin on a proportion near 0.5 needs about 385 items (derived). Results are reported on the public test split (30%, §3.4), so a 385-item slice needs ≥ 1,283 questions in the full set; no slice in Table 3 other than the total reaches this. Truthfulness ranges over [−1, 1] and has larger variance than a proportion. The image-quality slices in Fig. 4a rest on 124–401 images in total (Table 2), of which about 30% are in the public test; the "dropped by up to 46%" (§5.3) is therefore unlikely to be separated from noise for the smaller categories.
- **Suggested Fix**: State split sizes; add bootstrap 95% intervals to Tables 4–5 and Fig. 4/7; merge or flag slices with n < 100.

### W5: The retrieval world is built around the questions
The mock image KG is seeded with the images that generated the questions plus up to 30 hard negatives each (App. A.5.1), and the web corpus is the top-50 results of the annotators' queries per question (App. A.5.3: 50 × ≈16K turns ≈ 800K pages, derived). So "93% entity coverage" (§3.3) and the 1:20 / 1:2 ratios (§1) are properties of the construction, not evidence that the corpus "mimics real-world conditions". The web "estimated recall of 89%" (§3.3, Fig. 3 caption) has no described estimation method.
- **Suggested Fix**: Describe the recall estimation; add a run with a distractor-only expansion (e.g. 10× more entities) to show how much the numbers depend on corpus size; soften "mimic real-world".

### W6: The central differentiator (egocentric) is not shown to matter
No QA result compares egocentric with normal images. Fig. 6 / App. A.5.2 compares only *retrieval recall* by image type. In Table 2 almost all quality defects are egocentric (e.g. Rotated: 161 vs 6) and "Normal" quality is mostly egocentric (5143 vs 1593), so the Fig. 4a defect-vs-normal contrast cannot separate "egocentric" from "defective".
- **Suggested Fix**: Report Tables 4–5 for egocentric vs public images (matched on domain and question type).

**Minor:** The 0.75 similarity threshold, top-30 retrieval and 2K/8K token budgets (§5.1; App. C.1) have no stated selection split (state that they were fixed a priori or tuned on validation only); multi-turn Truth ≠ Acc − Hallu (Tables 4, 5, 9; averaging unstated, see log); "8K conversations" (§1) vs Table 3 total 8,418 mixing single and multi-turn; "68K entries" (§1) vs "68K images and 26K entities" (§3.4); App. A numbering skips A.2 content.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5 | Abstract vs full text | "differing information dynamism" | No dynamism slice, definition, table or analysis exists (search "dynamis*": one hit, the abstract) | Text search | High | MAJOR | Define and report it, or remove from abstract |
| ERR-2 | E1 | §3.2 vs Table 3, §3.4 | "<5% margin-of-error (with 95% confidence level) for most of the slices" | At the 30% public-test size, ±5% needs ≥1,283 full-set items per slice; none (except total) in Table 3 qualifies; truthfulness variance is larger than a proportion's | Derived: n = 1.96²·0.25/0.05² ≈ 385; 385/0.3 ≈ 1,283 | Medium (public-test size not stated) | MAJOR | State split sizes and CIs |
| ERR-3 | E6 | Tables 4, 5, 9 vs §4 | Table 5 Gemini multi-turn: Acc 66.2, Hallu 30.3, Truth 30.1 | Acc − Hallu = 35.9; likewise Table 4 Llama 3.2 90B multi-turn 42.2 − 32.8 = 9.4 vs 12.7. Probably macro vs micro averaging (§4), but Acc/Miss/Hallu averaging is not stated | Recomputed | Medium | MINOR | State the averaging |
| ERR-4 | E6 | §3.1 vs §1 | "created equal number of questions for each bucket" | Head/torso/tail balanced would give ~67% torso-to-tail, but §1 says "21% questions involve torso-to-tail entities"; reconcilable only if balancing applies to a subset | Cross-referenced | Medium | MINOR | Report the popularity distribution |
| ERR-5 | E1 | §1 vs Table 2 | "15% of images are low-quality egocentric images" | Low-quality egocentric = 267+191+370+116+161 = 1,105 = 13.9% of 7,943 (17.7% of egocentric); 15.2% only if public low-quality images are included | Recomputed | Medium | MINOR | Fix wording |

## Missing References
Not my responsibility; see Reviewer 2.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Unvalidated labels, partly validated judge, no intervals (W1, W2, W4) |
| Clarity | 3 | Understandable; key construction details sit in the appendix |
| Significance | 3 | Real gap for wearable MM-RAG; adoption by a challenge |
| Originality | 2 | Resource and setting are new; design and metric inherited from CRAG (§1, §4) |

## Dimension Scores (0–100)

**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the benchmark is a real, usable resource, but nothing shows the labels or the judge are reliable, and the main differentiator (egocentric) is not tested; benchmark papers with unvalidated labels are typically on the rejected side.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Metric and tables consistent; label quality, judge bias and corpus construction unvalidated |
| Clarity & Presentation | 62 | Competent | Readable; construction deferred to appendix |
| Novelty & Originality | 58 | Competent | New setting, inherited design |
| Significance & Impact | 66 | Competent | Useful niche; adopted by a challenge |
| Experimental Validation | 50 | Developing | Single runs, no CIs, non-comparable headline rows, no egocentric analysis |
| Reproducibility | 56 | Competent | Prompts and versions given; links removed, seeds/decoding missing |
| Ethical Compliance | 45 | Developing | No privacy/consent/licence statement for daily-life smart-glasses images (R3 scores this in depth) |

---

## Questions for Authors
1. What are the human-vs-judge truthfulness differences per system on a sample of ≥ 300 answers? (A difference above 3 points would lower my score further; a small, system-independent bias would raise it.)
2. How many annotators produced answers, and what was inter-annotator agreement on a double-annotated sample?
3. How large are the validation, public-test and private-test sets, and which two domains were held out (§3.4)?
4. Do truthfulness and accuracy differ between egocentric and public images on the same domains and question types?
5. How was the 89% web recall (Fig. 3) estimated, and how was the judge prompt's "WRONG for refusal" rule (App. B.1, rule 1) reconciled with "missing" scoring 0 (§4)? (Suspicion only; no error claimed.)

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. There is no limitations section; the conclusion has two sentences (§6). Please add English-only data, single still images, mock corpora, the judge's error profile and data-collection privacy.

## Ethics Review Flag
**No** (flagged by R3 for the editor's attention instead).

## Overall Score
**3 (Borderline Reject)**: A useful resource whose headline difficulty claims rest on unvalidated labels, a partly validated judge, single runs and non-comparable rows; most gaps are fixable with annotation audits and intervals.

## Confidence
**4**: I recomputed the tables and searched the full text; figures were not available.

---

# Peer Review Report

## Paper: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
## Reviewer: Prof. Amara Okonkwo-Reyes, Reviewer 2 / Domain (senior faculty, language and vision group; fictional persona)
## Expertise: knowledge-based VQA; multimodal retrieval-augmented generation; entity-centric QA
## Date: 2026-11-10

---

## Summary
The paper proposes a benchmark of image-grounded factual questions with a wearable-device angle: egocentric photos from smart glasses, entity-popularity buckets, six question types and multi-turn conversations, with mock retrieval APIs. It positions itself against general VQA, knowledge-based VQA and text RAG benchmarks (Table 1) and argues that no existing resource covers wearable use. Experiments show low truthfulness for simple RAG pipelines and commercial systems.

---

## Strengths

### S1: A real gap in the combination of properties
Table 1 shows no listed benchmark combines egocentric capture, image search, web search, multi-turn and torso/tail facts. The union is new even if each ingredient exists (§1, "Differences from CRAG and other existing benchmarks").

### S2: Controlled design axes
Entity popularity (head / torso / tail, following Sun et al. 2023, §3.1), six question types (§2.1) and five image-quality defects (Table 6) give analysis dimensions that earlier knowledge-VQA sets lack.

### S3: Inherits a validated metric philosophy
Scoring accurate / missing / incorrect as +1 / 0 / −1 (§4) follows CRAG (Yang et al., 2024) and makes abstention a first-class behaviour, which suits the factuality setting.

### S4: A mock API that others can run
Releasing image-KG and web-search APIs with fixed corpora (§3.3, App. A.5.4) lets different groups compare retrieval-plus-generation pipelines, as the KDD Cup showed (§5.2).

---

## Weaknesses

### W1: "First" claims and the comparison table are selective
§1 states that CRAG-MM is "the first publicly released benchmark capable of effectively evaluating multi-modal RAG". Table 1 itself lists WebQA as multimodal with image and web search ✓ (footnoted "Prefetched images" / "Prefetched snippets from wikipedia", so the distinction is that CRAG-MM exposes search APIs), and SnapNTell, MultiModalQA, MM-Vet. The table's columns (Egocentric, Torso & tail facts, Multi-turn) are those on which CRAG-MM is unique, and it lists no recent multimodal knowledge-seeking or multimodal-RAG benchmark. I recall several (entity-centric knowledge VQA sets such as InfoSeek and Encyclopedic-VQA; dynamic-knowledge and multimodal-RAG benchmarks such as Dyn-VQA, MRAG-Bench and MMSearch; marked `[verify]` below and checked in the literature addendum). There is no Related Work section; positioning is four paragraphs in §1.
- **Suggested Fix**: Add a related-work section and extend Table 1 with size, image source, retrieval type and answer type; narrow "first" to the supported combination (egocentric + mock image-KG + web + multi-turn).

### W2: Inconsistent critique of prior benchmarks
§1 faults prior benchmarks for being "created by templates (Talmor et al., 2021)", yet the KG-based questions here are generated from templates (§3.2: "create meaningful QA templates"; App. A.3 steps 1–3, multi-hop template "what is the latest book of this book's author?"). The multi-turn data are LLM-generated (§3.2). The characterization of WebQA/MultiModalQA as having "questions uncommon in real life" has no supporting evidence. 
- **Suggested Fix**: Report the share of template-, annotator- and LLM-written questions, and compare question naturalness with real user queries or drop the claim.

### W3: Novelty is mostly in setting, not design
Principles, the metric and the scoring follow CRAG (§1 "follows the key features outlined in Yang et al. (2024)"; §4 "We adopt the metrics and evaluation in Yang et al. (2024)"). The multi-turn protocol is "adapt[ed]" from Bai et al. (2024) (§4), but the adaptation (early stop after two consecutive failures) is not contrasted with the source. The genuine contributions are the egocentric data, the multimodal corpora and the multi-turn extension.
- **Suggested Fix**: State plainly what is new relative to CRAG and to MT-Bench-101-style multi-turn scoring.

### W4: Domain accuracy of claims about the data
(i) Egocentric images are the main differentiator, but there is no result showing egocentric images are harder for MM-RAG (only retrieval recall, App. A.5.2). (ii) The "information dynamism" dimension appears only in the abstract. (iii) Questions are single still images, whereas wearable products use continuous capture and speech; scope should be stated.
- **Suggested Fix**: Add the egocentric-vs-public comparison; remove or define dynamism; add scope limits.

**Minor:** Missing venue for Talmor & Berant (2018) and Vu et al. (2023) in the reference list; Table 5 rows "Claude Sonnet / Gemini / GPT-5" should carry model versions in the table.

## Missing References *(pending literature-check addendum below; entries are `[verify]` until checked)*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | InfoSeek: Chen et al., "Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?" (EMNLP 2023) `[verify]` | Entity-centric knowledge-seeking VQA, directly relevant to C1/C2 |
| Critical | Encyclopedic-VQA: Mensink et al. (ICCV 2023) `[verify]` | Fine-grained entity VQA with retrieval over a knowledge base |
| Important | Dyn-VQA: Li et al., "Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent" (2024) `[verify]` | Multimodal RAG benchmark with changing answers; bears on the dynamism claim |
| Important | MRAG-Bench: Hu et al. (2024) `[verify]` | Vision-centric multimodal RAG benchmark |
| Important | MMSearch: Jiang et al. (2024) `[verify]` | Benchmark for multimodal search-engine pipelines |
| Helpful | Ego4D: Grauman et al. (CVPR 2022) `[verify]` | Egocentric data collection, privacy practice and benchmark design |

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound construction overall; not all claims validated |
| Clarity | 3 | Clear positioning in §1 but no related-work section |
| Significance | 3 | Useful niche resource |
| Originality | 2 | New combination; design inherited from CRAG |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a real, non-trivial resource (egocentric data, mock APIs, multi-turn) in an area of current interest, with positioning gaps that are fixable by rewriting; this puts it just on the accept side of the bar, not above it.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Standard construction; known gaps in validation |
| Clarity & Presentation | 64 | Competent | Positioning compressed into §1 |
| Novelty & Originality | 60 | Competent | New combination of properties; inherited design |
| Significance & Impact | 68 | Competent | Wearable QA is timely; adopted in a public challenge |
| Experimental Validation | 58 | Competent | Broad baselines; weak statistical support |
| Reproducibility | 62 | Competent | Prompts and versions given; data links not available to me |
| Ethical Compliance | 50 | Developing | No privacy/licensing statement |

---

## Questions for Authors
1. Which existing multimodal-RAG and knowledge-seeking VQA benchmarks did you consider, and why are they absent from Table 1? (A convincing delta would raise my score; a missing close benchmark would lower it.)
2. What proportion of questions are template-generated vs annotator-written vs LLM-generated?
3. How does the early-stop multi-turn scoring differ from the cited MT-Bench-101 protocol?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. No limitations section; add scope (English, single images, mock corpora).

## Ethics Review Flag
**No** (see R3).

## Overall Score
**4 (Borderline Accept)**: A genuinely new combination of properties that fills a practical niche; positioning claims need narrowing, but the resource is useful.

## Confidence
**4**: I know this literature but verified little beyond the paper in this pass (the literature check follows).

---

# Peer Review Report

## Paper: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
## Reviewer: Dr. Kenji Hayashida, Reviewer 3 / Perspective (industry human-computer interaction lab; fictional persona)
## Expertise: wearable and always-on devices; privacy; voice-first interfaces
## Date: 2026-11-10

---

## Summary
CRAG-MM packages realistic smart-glasses questions with a fixed retrieval environment so that researchers can study visual question answering with outside knowledge. It reports that today's models answer fewer than one third of questions net of errors and shows breakdowns by image quality, entity recognition, popularity and question type. The work targets a real product category and an open research need.

---

## Strengths

### S1: Grounded in an actual product category
Images are captured with smart glasses by vendors in "pre-defined" and "free-form" modes (§3.1), including defects such as truncation and low light (Table 2, Table 6) that appear in wearable capture. Few benchmarks have this property.

### S2: The metric reflects user cost of wrong answers
Penalizing wrong answers (−1) and allowing abstention (§4) matches the product setting, where a confident wrong answer about a medication, price or flight rule is worse than "I don't know" (Fig. 1 examples such as the carry-on rule).

### S3: Multi-turn with topic drift
Conversations of 2–6 turns that cover one to three domains (§3.2) and the early-stop rule (§4) approximate a user giving up after repeated failures, a useful behavioural proxy.

### S4: Actionable analysis axes
§5.3 and Fig. 4 link failures to image quality, OCR vs non-OCR entities and popularity, which suggests concrete engineering directions (cropping, OCR, retrieval for tail entities).

---

## Weaknesses

### W1: Privacy and consent are not addressed for data captured in daily life
Vendors wore glasses and "interact[ed] in their daily lives" for free-form collection (§3.1), and the dataset is released (§3.4). Images from people's surroundings can contain bystanders' faces, licence plates, addresses and screens. A search of the full paper finds no mention of consent, face/plate blurring, PII review, licence of the released images, or of the public images "found online" (§3.1) and redistributed. This is the only ethical issue of substance in the paper but it is unaddressed.
- **Suggested Fix**: Add a datasheet-style statement: collector consent and compensation, de-identification applied, licence per image source, takedown process.

### W2: The deployment view is missing latency, cost and modality
Wearable assistants are voice-first and latency-bound; Tables 4–5 compare models with different reasoning effort, tool use and context budgets (8K tokens, App. C.1; "thinking_budget=-1" for Gemini, App. D) but report no latency, token cost or answer length. A system that wins by long deliberation would not be deployable on glasses. The data are single still images, whereas devices continuously capture video and audio (§1 examples describe the user "holding" an item).
- **Suggested Fix**: Report latency/tokens per question for Tables 4–5 and state clearly that continuous capture, speech input and non-English use are out of scope.

### W3: Assumptions about realism are untested
Questions are written by annotators or generated from templates/LLMs (§3.2), not collected from real wearable users, and several of the examples shown are US-centric (Walmart/Target price comparison, the carry-on liquids rule, Fig. 1). No user study or comparison with real query logs supports "reflect real-world scenarios" (§1). Abstention-aware metrics from selective prediction (risk–coverage analysis) would show whether the winners' lower hallucination is a better trade-off or just abstention.
- **Suggested Fix**: Compare a sample of questions with real assistant queries or ask users to rate plausibility; add risk–coverage curves to §5.2.

### W4: Cross-field links that would strengthen the evaluation
Pooling-based relevance judgments from information retrieval (to estimate recall of the corpus rather than "estimated recall of 89%", Fig. 3), calibration and selective-prediction metrics (for the abstain/answer trade-off), and de-identification practice from large egocentric datasets (e.g. Ego4D `[verify]`) would improve the benchmark's measurement and release.
- **Suggested Fix**: Adopt pooled relevance judgments for a sample, report risk–coverage, and follow an egocentric de-identification protocol.

**Minor:** Names such as "Rabbit R1" and "Humane AI Pin" (§1) are product examples; no evidence is given that the benchmark questions reflect them.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid construction, limited validation |
| Clarity | 3 | Clear task design (Fig. 2) |
| Significance | 3 | Practical, timely |
| Originality | 3 | Novel combination of data and setting |

## Dimension Scores (0–100)

**Pool position:** better than about 72% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the benchmark addresses a concrete, current product setting with data few groups can collect, and its weaknesses (privacy statement, latency, realism evidence) are the kind that accepted resource papers routinely carry.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Sound but under-validated |
| Clarity & Presentation | 66 | Competent | Clear tasks; details deferred |
| Novelty & Originality | 62 | Competent | New setting |
| Significance & Impact | 74 | Strong | Real product relevance; adopted by a challenge |
| Experimental Validation | 60 | Competent | Broad but not deep |
| Reproducibility | 64 | Competent | Prompts, versions and APIs |
| Ethical Compliance | 42 | Developing | Daily-life captures with no privacy or licence statement |

---

## Questions for Authors
1. What de-identification (faces, plates, text) was applied to the egocentric images before release, and what consent did collectors give? (A clear protocol would raise the Ethical score; "none" would lower it and strengthen the ethics flag.)
2. What are the per-question latency and token costs of the Table 4–5 systems?
3. Is there any evidence the questions match real wearable-user queries?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. No limitation or broader-impact section exists.

## Ethics Review Flag
**Yes**: Smart-glasses images captured in daily life (§3.1) and released (§3.4) without any stated consent, de-identification or licensing; a data-ethics check is warranted. This is a missing-disclosure concern for the editor, not an accusation of wrongdoing.

## Overall Score
**4 (Borderline Accept)**: A timely, practically grounded benchmark; missing privacy, latency and realism evidence are fixable and typical for resource papers, but the privacy statement should be added.

## Confidence
**3**: Fairly confident; I could not see figures or the released data.

---

# Peer Review Report

## Paper: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
## Reviewer: Dr. Priya Raghunathan, Reviewer 4 / Generalist (vision-and-language lab, public research university, South Asia; fictional persona)
## Expertise: vision-language models; VQA; general ML
## Date: 2026-11-10

---

## Summary
The paper introduces CRAG-MM, a visual question answering benchmark in which questions about everyday objects, landmarks and products (mostly photographed with smart glasses) require retrieval from an image knowledge graph and web pages. It adds multi-turn conversations, three tasks of increasing retrieval access, a truthfulness metric and baseline results. The authors conclude that existing models and systems leave "ample room for improvement", and note that the benchmark ran as a public competition.

**The contribution in one paragraph (own words).** A new test bed for "what is this and tell me something about it" assistants on wearables, with fixed retrieval backends so that results are comparable, plus evidence that current systems are far from reliable.

---

## Venue Criteria Checklist (ICLR 2026: Soundness, Presentation, Contribution)

| Criterion | Grade | Location |
|-----------|-------|----------|
| Contribution is a resource the community can use | Met | §2.2, §3.3, §3.4 (public validation/test released) |
| Claims supported by evidence | Partly | Abstract "dynamism" and "first" claims; Tables 4–5 numbers verified |
| Soundness of data and evaluation | Partly | No annotation-quality evidence; judge validated (Table 7) but "Incorrect" F1 78.2 |
| Presentation (self-contained main text) | Partly | Construction in App. A; §6 has two sentences |
| Limitations / ethics | Not met | None in paper |
| Reproducibility | Partly | Prompts, versions, dates given; links removed |

---

## Strengths

### S1: Clear task design
Fig. 2 and §2.2 explain Task 1 (image-KG only), Task 2 (plus web), Task 3 (multi-turn) so that each added source's effect can be read from Table 4.

### S2: Honest reporting of abstention and non-comparability
Tables 4–5 show missing and hallucination rates, and §5.2 warns that the winners (private test) are "not fully comparable". This is the right instinct for a benchmark paper.

### S3: Useful set of questions and taxonomy
The six question types (§2.1) and 13 domains (Table 3) make failure analysis interpretable; example questions in Fig. 1 are concrete and varied.

### S4: Substantial effort and adoption
Collecting 6.2K egocentric images with a vendor team, building two retrieval corpora and running a public challenge (KDD Cup, §1) is a nontrivial community service.

---

## Weaknesses

### W1: The main text does not stand alone, and the analysis is thin relative to the effort
Annotation procedures (App. A.3–A.4), retrieval construction (App. A.5), judge validation (App. B.1) and nine-model results (Tables 8–9) are in the appendix, while §5.3 enumerates findings (image quality, OCR, popularity, question type, context dependence) with figures I could not read and little explanation beyond "showing the need for more robustness". RQ1 asks whether CRAG-MM "reveal[s] new challenges beyond straightforward solutions", but it is answered only with low absolute numbers; the same systems are never evaluated on another benchmark, so "new" is not shown. The conclusion (§6) is two sentences and there is no limitations section.
- **Suggested Fix**: Move the annotation and judge summaries into §3–4; run two or three models on an existing multimodal-QA or MM-RAG benchmark to show the difficulty contrast; add limitations.

### W2: Headline and abstract wording drifts from the evidence
Abstract: "differing information dynamism" is never analysed. §1: "8K conversations" vs 6.5K + 2K elsewhere; "21% questions involve torso-to-tail entities" vs balanced buckets (§3.1); "winning solutions improving baseline performance by 28%" is 28.3 absolute points computed across splits (Table 5); "state-of-the-art industry solutions" are, per §5.2 ("built upon MM-LLMs and search engines") and App. D, three LLM APIs with a search tool enabled, which the abstract wording does not make clear. "Multi-turn conversations contain simpler questions" (§1) is asserted without evidence.
- **Suggested Fix**: Align the abstract with measured quantities; say "points", define "industry solutions" as tool-enabled APIs.

### W3: The reference for "dropped by up to X%" is not stated
The text (§5.3) reports "dropped by up to 46%" / "37%" / "22%" for Fig. 4a/4b/4e without saying whether these are absolute truthfulness points or relative changes, relative to which baseline category, or with what intervals. I could not read the figures from the extracted text, so I treat the values as unverified rather than wrong.
- **Suggested Fix**: Put key numbers in a table with n and 95% intervals.

**Minor:** Typos ("winnings' solutions" in Table 5 caption, "Comp." vs "Comparison"); Table 5 rows should name model versions.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid construction, thin validation |
| Clarity | 3 | Readable; main text defers a lot |
| Significance | 3 | Useful resource, practical angle |
| Originality | 3 | New setting, derived design |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, usable resource with an active community, and presentation/overclaim issues that most accepted resource papers also have; no sign of a fatal flaw.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Standard, mostly consistent |
| Clarity & Presentation | 64 | Competent | Readable; thin conclusion; appendix-heavy |
| Novelty & Originality | 60 | Competent | New combination |
| Significance & Impact | 68 | Competent | Timely for wearables |
| Experimental Validation | 60 | Competent | Many baselines; no variance |
| Reproducibility | 62 | Competent | Prompts and versions given |
| Ethical Compliance | 48 | Developing | No limitations/ethics statement |

---

## Questions for Authors
1. Can you show the same models on an existing multimodal-QA or MM-RAG benchmark so that "new challenges" (RQ1) is evidenced?
2. In §5.3, are "dropped by up to X%" values absolute points or relative, and what are the intervals?
3. What is meant by "information dynamism" in the abstract?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No** (see R3).

## Overall Score
**4 (Borderline Accept)**: A clear and useful benchmark whose presentation and claims need tightening; the weaknesses are typical of accepted resource papers.

## Confidence
**4**: Confident on venue fit and clarity; less on figure content.

---

# Devil's Advocate Report

## Paper: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
## Reviewer: Prof. Daniel Mbeki-Larsen, Devil's Advocate (evaluation methodology; fictional persona)

---

## Steelman
CRAG-MM is a carefully scoped, large benchmark with egocentric data, fixed retrieval APIs, a penalty-for-hallucination metric and a validated automatic judge. Even strong commercial systems net only about a third of the maximum truthfulness, so the benchmark exposes a real reliability gap and a public competition confirms it is usable and discriminative.

---

## Core Argument Chain
1. Existing VQA/QA benchmarks lack wearable (egocentric), multi-source and multi-turn factual questions (§1, Table 1).
2. CRAG-MM supplies such data and fixed retrieval resources with realistic noise (§3, App. A).
3. The judge is accurate (99.1%, Table 7) and truthfulness measures reliable answering (§4).
4. Under this measurement, simple RAG and industry systems reach ≈ 32% / 43–45% (Tables 4–5).
5. Winning competition solutions improve the baseline by 28% (Table 5).
∴ CRAG-MM is a challenging, useful benchmark that reveals "ample room for improvement", and the field should adopt it.

---

## Strongest Counter-Argument
The paper's conclusion is that the *benchmark is hard because wearable MM-RAG is hard*. The evidence cannot separate that from four measurement artifacts, each visible in the paper itself. (1) **Time.** Ground truth was fixed at collection time, yet many answers are volatile (prices in Fig. 1, "sells at $599" in Fig. 2), and industry systems were queried against the live web on 1–10 Sept 2025 (App. D). Correct, current answers to such questions can be scored as "incorrect", biasing exactly the industry rows that anchor the "ample room" story, and the abstract's "information dynamism" is never analysed. (2) **Metric.** Truthfulness equals accuracy minus wrong-rate; Table 5 shows the "winning team" has *lower accuracy* than the baseline (29.3 vs 35.3) and wins by abstaining (missing 61.2%). The "+28%" is therefore a statement about abstention, computed across different splits (private vs public), and "similar quality" between GPT-5-with-live-search and GPT-5-mini-with-curated-corpora compares different things. (3) **Judge.** The "99.1%" accuracy hides Incorrect precision 68.1; with a −1 penalty, a modest bias moves truthfulness as much as the gaps discussed. (4) **Attribution.** The benchmark's identity is "egocentric", but no QA result shows egocentric images are harder than public ones; the defect slices in Fig. 4a are almost all egocentric by construction (Table 2). Without these controls, "challenging" could equally mean "noisy ground truth, stale answers and a harsh judge". The authors can answer by freezing live-web answers, reporting a same-split comparison, intervals and an egocentric-vs-public contrast, but as submitted the headline reading is not established.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in a narrower form: the benchmark is a useful resource and the reported numbers are internally consistent; what is not established is the interpretation of difficulty. No evidence of tuning or selection on a reported test split was found (protocol sweep: not stated), and the main findings do not depend on a single contested number.

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Fig. 1, Fig. 2, App. D | Frozen ground truth vs live-web industry systems; volatile answers (prices) can be penalized | Tag time-sensitive questions, re-verify answers on the evaluation date, report results with and without them |
| DA-M2 | Evidence / Scope | Abstract, §5.2, Table 5 | "+28%" is absolute points across private vs public test, driven by abstention (Acc 35.3 → 29.3, Hallu 43.9 → 9.6); "industry solutions" are tool-enabled APIs | Same-split rerun; say "points"; add always-abstain (0) and risk–coverage reference |
| DA-M3 | Logic / Overclaim | §1, Table 1, Abstract | "first ... capable of effectively evaluating multi-modal RAG" while Table 1's WebQA row is multimodal with image and web search (footnoted as prefetched) and several multimodal knowledge-seeking benchmarks are absent; "comprehensive" with English-only, single images, 13 domains | Narrow wording; extend Table 1 |
| DA-M4 | Evidence | Table 7, §4, App. B.1 | Judge headline hides "Incorrect" precision 68.1; validation n and systems unstated; GPT-4o judges GPT-5 family | Per-system validation, second judge, confusion matrix |
| DA-M5 | Attribution | Table 2, Fig. 4a, App. A.5.2 | Egocentric property never tested on QA performance; defects almost all egocentric | Egocentric-vs-public comparison matched on domain/type |
| DA-M6 | Alternative explanation | §3.2 | Multi-turn conversations generated by Llama-3.2-90B-Vision, which is also evaluated (Table 4); no rate of removed or revised turns | Report removal rates; evaluate generator-vs-other bias |
| DA-M7 | Ethics / Scope | §3.1, §6 | No limitations, privacy, consent or licence statement | Add them (see R3-W1) |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | §1 | "Multi-turn conversations contain simpler questions" asserted without data |
| DA-m2 | Clarity | Tables 4, 5, 9 | Truth ≠ Acc − Hallu in multi-turn rows (averaging unstated) |
| DA-m3 | Logic | §5.1 | "Task 1 ... marginal improvement (+4%)" is the best case; Table 8 shows Task 1 lowers Claude 3.7 Sonnet truthfulness (−9.3 → −29.5) |
| DA-m4 | Clarity | §1 vs §3.4 | "68K entries" vs "68K images and 26K entities"; 30/30/40 split vs two held-out domains |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Single-turn straightforward truthfulness | 32% (Abstract) | Table 4 Task 2 GPT-5 Mini 31.5 | Yes (rounded) |
| Multi-turn straightforward truthfulness | 43% | Table 4 Task 3 GPT-5 Mini 42.5 | Yes (rounded) |
| Industry single / multi | 32% / 45% | Table 5 GPT-5 32.2 / 45.0 | Yes |
| Winner gain single | +28% | 19.7 − (−8.6) = 28.3 points | Yes, as absolute points across splits |
| Winner gain multi | +18% | 26.6 − 8.8 = 17.8 points | Yes, as absolute points |
| Egocentric share | 79% | 6248 / 7943 = 78.7% | Yes |
| Low-quality egocentric share | 15% | 1105 / 7943 = 13.9% (15.2% incl. public) | Partly |
| Table 5 Gemini multi-turn Truth | 30.1 | 66.2 − 30.3 = 35.9 | No (averaging unstated) |
| Table 4 Llama 3.2 90B multi-turn MM-LLM Truth | 12.7 | 42.2 − 32.8 = 9.4 | No (averaging unstated) |
| Slice margin of error | <5% for most slices | ±5% needs ≈ 385; ≈ 1,283 at 30% split | Not supported at evaluated size (split size unstated) |

## Ignored Alternative Explanations
Stale or noisy ground truth; judge bias against correct answers (and toward the GPT family); abstention, not capability, explaining the winners' gain; corpus-construction artifacts (documents retrieved per question) making retrieval easier than the real web; Llama-generated multi-turn data favouring Llama-style models; prompt sensitivity (a single prompt per setting, App. C.2) driving the "I don't know" rates.

## Missing Stakeholder Perspectives
Bystanders captured by always-on glasses (no consent or de-identification described); users outside the US/English context; accessibility users who rely on such devices.

## Observations (Non-Defects)
The authors disclose non-comparability in §5.2; they report Miss/Hallu separately; all single-turn table rows are arithmetically consistent; Table 2 and Table 3 totals reconcile; model versions and dates are listed (App. D).

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 52 | Judge, labels and corpus construction unvalidated; averaging and split details unstated |
| Clarity & Presentation | 62 | Clear tasks; abstract drifts from content |
| Novelty & Originality | 52 | New setting but inherited design and overclaimed "first" |
| Significance & Impact | 62 | Useful niche resource |
| Experimental Validation | 48 | Single runs, non-comparable headline rows, no egocentric test |
| Reproducibility | 56 | Prompts/versions present; links removed, decoding unstated |
| Ethical Compliance | 42 | No privacy/consent/licence/limitations statement |

## Pool position
Better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline difficulty claim is confounded by metric, time and corpus construction, and the key differentiator is untested; these are signals of a typical rejected submission, offset only partly by the resource's usefulness.

## Overall: 3 | Confidence: 4
