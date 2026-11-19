# Full Review: "Structured Attention Matters to Multimodal LLMs in Document Understanding"

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested)

*Simulation notice: this is how a careful panel would likely see this draft, not a prediction of any real outcome. The five reviewer passes were run sequentially in one shared model context (no subagents), so they are role-based perspectives, not independent agents. Figures were not available (text extraction only): claims that depend on Figures 3, 5 and 6 are judged from captions and surrounding text.*

---

# Phase 0: Paper Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Structured Attention Matters to Multimodal LLMs in Document Understanding |
| Primary Discipline | Multimodal LLMs → document question answering (DocQA) / long-document understanding |
| Secondary Discipline(s) | Retrieval-augmented generation; model interpretability (attention analysis); table/format serialization |
| Paper Type | Analysis/Insight with a lightweight prompting method (composite weights: analysis) |
| Core Technique(s) | Prompt an MLLM to rewrite OCR text + page image as LaTeX-structured text; feed image + structured text to a frozen MLLM; attention-map analysis |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (no ECCV/ACM MM/TPAMI-specific rules). ICLR form: Soundness/Presentation/Contribution 1–4, Rating, Confidence. Accepted share of submissions ≈ 27% |
| Paper Maturity | Early draft / workshop-level submission (short paper, 7B models, one-paragraph limitations) |
| Ethics-Relevant Content | none (public benchmarks, no human subjects) |
| Integrity signals | `integrity_scan.py` found no reviewer-directed text and no hidden characters; none seen while reading. The extracted text shows author names and affiliations (not anonymized); these were ignored. |

### Claimed Contributions (as stated by the authors)
1. **C1**: "unstructured OCR text often degrades rather than enhances MLLM performance compared to using images alone" (Abstract, §1, Observation 1 in §3.1, §4.2).
2. **C2**: A training-free "structure-preserving approach" that encodes OCR text with the LaTeX paradigm significantly improves MLLM document question answering without architectural changes or training (Abstract, §3.2, Observation 2, §4.3, Table 1).
3. **C3**: Attention analysis shows structured text induces "structured attention" on text and image tokens, which "is the key" to improvement (Abstract, §3.3, Observation 3, §4.4, Figures 3, 5, 6).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Models: Qwen2-VL-7B-Instruct, Qwen2.5-VL-7B-Instruct, LLaVA-v1.6-Mistral-7B, Phi-3.5-Vision-Instruct (§4.1). Benchmarks: MMLongBench, LongDocUrl, PaperTab, FetaTab (§4.1). Metric: binary correct/incorrect decision by LLaMA-3.1-8B-Instruct as judge, averaged (§4.1). Compute: 4 NVIDIA A100 GPUs (§4.1). Evidence pages: located, OCR'd, then converted by the method of §3.2 (§4.1); Table 1 caption says open-domain datasets use top-1 retrieval as in Han et al. (2025), closed-domain datasets use the dataset's evidence pages, but which dataset is which is **not stated**. Splits, sample counts per benchmark, seeds, number of runs, decoding parameters, prompts, the identity of the MLLM that writes the LaTeX, code/data release: **not stated after search**. Appendix/supplement: none present in the provided text.
- **Headline numbers.** "from 0.389 to 0.370" (§4.2; Table 1 prints 0.375 for that cell); "0.389 to 0.435", "10% performance improvement" (§4.3; Table 1 prints +11.8%); relative gains of +4.8% to +190.9% (Table 1), all relative to the image-only row.
- **Unverifiable parts.** Figures 3, 5, 6 (not available; Figure 6 axis labels are garbled in extraction); Figure 2 and 4 read from captions and extracted text.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Marguerite Okonkwo-Hale, large public research university (Europe)
- **Seniority / Expertise**: Senior faculty, repeated area chair / **Multimodal learning, document AI, evaluation practice**
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Counts what the evidence shows, not what the paper says it shows; wants one clean control before believing a mechanism.

### Reviewer 1 (Methodology): Dr. Anika Varga-Lindqvist, industrial research lab (Europe)
- **Seniority / Expertise**: Senior industry scientist / **MLLM evaluation protocols, LLM-as-judge validity, RAG ablations**
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table average; insists on matched controls and variance.

### Reviewer 2 (Domain): Prof. Ilesha Dombrowski, public research university (North America)
- **Seniority / Expertise**: Senior faculty / **Visually rich document understanding, table/structure serialization for LLMs**
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work first; asks what exactly is new relative to the closest two papers.

### Reviewer 3 (Perspective): Dr. Rafael Quispe-Ahn, applied research institute (South America)
- **Seniority / Expertise**: Mid-career / **Information design and accessibility (semantic markup), interpretability of transformers**
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive; "this could be stronger if…".

### Reviewer 4 (Generalist): Dr. Priya Nakamura-Obi, large public research university (East Asia)
- **Seniority / Expertise**: Mid-career / **Vision-language models (not document-specific)**
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee reader; weighs weaknesses against what ICLR usually accepts.

### Devil's Advocate: Dr. Lars Eklund-Mbeki, industrial research lab (Europe/Africa)
- **Seniority / Expertise**: Senior scientist / **Causal inference for ML evaluation, ablation design**
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

(Reviewers read the redacted reviewer copy and the paper memory. The integrity scan found nothing to redact.)

---

# Peer Review Report

## Paper: Structured Attention Matters to Multimodal LLMs in Document Understanding
## Reviewer: Dr. Anika Varga-Lindqvist, Reviewer 1 (Methodology) (industrial research lab, Europe; fictional persona)
## Expertise: MLLM evaluation protocols; LLM-as-judge validity; RAG ablations
## Date: 2026-11-10

---

## Summary
The paper studies how the *format* of text accompanying a page image affects 7B-scale MLLMs on document QA. It reports that adding raw OCR text to images often hurts (Observation 1), proposes to have an MLLM rewrite the OCR text plus image as LaTeX-structured text (§3.2, Figure 2), reports gains from image + structured text on four benchmarks (Table 1), and uses attention maps of one model to argue that "structured attention" is the mechanism (§3.3, §4.4).

## Protocol sweep (Step 0)
Searched the full text for split, validation, tuning, selection, seed, decoding and release statements. The paper states **no** split, tuning or selection protocol, no seeds or number of runs, no decoding settings, no prompts, and no code release. The only protocol sentences are in the Table 1 caption ("using the top-1 retrieval result as input") and §4.1 (LLaMA-3.1-8B-Instruct as judge producing "a binary decision (correct / incorrect)"). There is no statement of tuning on the reported data, so this is not an evaluation-leakage issue; it is an unstated-protocol issue (MAJOR question).

## Claim-to-Evidence Map

| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|-------------|----------|---------|
| C1 | OCR text "often degrades" performance | Abstract, §3.1 Obs. 1, §4.2 | Table 1: OCR lowers accuracy in 2 of 16 model×benchmark cells (MMLongBench for Qwen2-VL and Qwen2.5-VL); raises it in 14. Row averages rise for all four models | **Contradicted as worded**; supported for one benchmark |
| C2 | Structured text significantly enhances accuracy | Abstract, §4.3 | Beats image-only in 16/16 cells; vs. the matched image+OCR control it is higher in 10/16 cells and lower in 6 (recomputed) | Partially supported (vs image-only); **not supported** vs. the matched control |
| C3 | "structured attention is the key" | Obs. 3, §4.4, Fig. 3/5/6 | One model, one aggregate plot and one case; no OCR-text attention condition; no intervention | **Unsupported** (correlational at best) |

## Strengths

### S1: A simple, cheap intervention with a clear protocol idea
The method needs no training or architecture change (Figure 2 caption: "only requires API-level access with instruction-level control"), so it is easy to try and to compare against.

### S2: Several models and benchmarks, with an informative ablation
Four MLLMs from different families and four benchmarks are evaluated (§4.1, Table 1), and Table 2 honestly reports that structured text alone does not work ("Structured text is ineffective when not input alongside images"). That finding is useful, even though I read it differently from the authors (W2).

### S3: Gains over image-only are consistent in direction
Image + structured text beats image-only in all 16 cells of Table 1 (my count), and the relative gains in the Table 1 rows reproduce from the printed accuracies (e.g. 0.306/0.292 → +4.8%; 0.252/0.163 → +54.6%).

## Weaknesses

### W1: The headline gains are measured against the wrong control, and against the right control they largely vanish
All relative gains in Table 1 ("+4.8%" … "+190.9%") are over the image-only row (I reproduced them: 0.229/0.195 = +17.4%, 0.209/0.160 = +30.6%). But the claim of the paper is that *structure* matters, which requires comparing against image + unstructured OCR (the "Han et al., 2025" rows). Recomputed row averages: Qwen2-VL 0.313 vs 0.300 (+0.013); LLaVA 0.222 vs 0.219 (+0.003); Phi 0.287 vs 0.261 (+0.026); Qwen2.5-VL 0.371 vs 0.390 (−0.019; the printed 0.427 is wrong, see Error Log). In 6 of 16 cells the proposed input is lower than plain OCR text, most strikingly Qwen2.5-VL on LongDocUrl (0.221 vs 0.399), the strongest model on a benchmark where OCR helps most. §4.5 nevertheless says "We almost obtain the best results on almost every dataset and model"; the table gives 10 of 16.
- **Suggested Fix**: Report every table against image+OCR as the primary baseline; state gains in absolute points; add paired bootstrap CIs over questions. Cost: reanalysis only.

### W2: The structured text is not a format change; it is an extra MLLM pass, and no control separates the two
§3.2 says the MLLM receives the image and OCR text and produces the LaTeX ("We input the image and the corresponding OCR text into the MLLM to obtain the structured code"). That pass can correct OCR errors, transcribe chart values and drop clutter, none of which the OCR baseline gets. Gains are largest for the weakest image readers (LLaVA/Phi, +151.9%/+75.1% on FetaTab, Table 1) and smallest for the strongest (Qwen2.5-VL), which fits any extra, cleaner text helps a weak image reader. Table 2 points the same way: structured-only is *worse* than OCR-only for all four models (averages 0.188 vs 0.233, 0.211 vs 0.253, 0.199 vs 0.225, 0.206 vs 0.242), which is hard to reconcile with the idea that LaTeX structure makes text easier for the model to use. Which MLLM writes the LaTeX, its prompt, and the extra cost are not given.
- **Suggested Fix**: Add controls with the same generation pass: (a) MLLM-rewritten *plain* text, (b) Markdown/HTML/JSON structure, (c) a layout-aware OCR/parser output, (d) LaTeX with structure tokens shuffled or stripped. Report the generator model and tokens/latency. Cost: about 4 variants × 4 models × 4 benchmarks, roughly 100–200 A100-hours at 7B.

### W3: Evaluation is single-run, judge-scored, and under-specified
No seeds, runs, CIs or test sizes are given for any benchmark (MMLongBench, LongDocUrl, PaperTab, FetaTab; §4.1), and many differences are 0.002–0.02 (Table 1: LLaVA PaperTab 0.122 vs 0.127). Scoring uses LLaMA-3.1-8B-Instruct as a binary judge with no agreement check against the benchmarks' own metrics or human labels. Table 1 mixes "open-domain" (top-1 retrieval) and "closed-domain" (gold evidence pages) settings without saying which benchmark is which, and the baseline rows are attributed to "(Han et al., 2025)" without saying whether numbers were rerun or copied, or with what prompt.
- **Suggested Fix**: Report n per benchmark, decoding settings and prompts; validate the judge on a human-labeled subset (Cohen's κ); run 3 prompt/decoding seeds on the two smallest benchmarks. Cost: low to medium (~30 GPU-hours).

### W4: The attention analysis cannot carry "structured attention is the key"
Observation 3 and §4.4 rest on one aggregate distribution over "370 samples with the same number of image tokens" for one model (Qwen2.5-VL), whose selection criterion, layer, head aggregation and query position are not stated (Figure 3 caption: border attention scores "are lower in the presence of structured text"). The central hypothesis (§1, Abstract) is that *raw OCR* disperses attention, yet no OCR-text attention condition is shown in Figures 3, 5 or 6 (captions compare images alone vs. image + structured text only). Adding hundreds of text tokens changes softmax normalization by itself, and no intervention (attention steering, masking, or swapping attention patterns) tests causality.
- **Suggested Fix**: Add the image+OCR condition, report attention *mass* on evidence regions with region annotations, control for token count, and add one causal test. Cost: medium.

### W5: Table 3 contradicts or does not match Tables 1–2, and its element-type claim does not follow
For Qwen2.5-VL the Table 3 "w/ structured text" average is 0.363; Table 1 gives 0.435 for image + structured on MMLongBench and Table 2 gives 0.267 for structured-only, so Table 3 matches neither reading. If Table 3 is the image+structured configuration, it is *below* image-only (0.363 vs 0.395), reversing Table 1. The text says gains are "more pronounced" for charts or tables (§4.5), but in Table 3 pure-text questions gain as much or more (LLaVA: pure-text +0.089, chart +0.039, table +0.069; Phi: +0.130, +0.085, +0.116), and Qwen2.5-VL chart accuracy falls (0.364 vs 0.392).
- **Suggested Fix**: Define each Table 3 row, add the image+OCR and image+structured rows explicitly, and restate the element-type conclusion.

**Minor**: Table 2 caption says "different datasets" but shows two; "ans" typo in §4.5; Limitations (§6) lists open questions rather than limitations of the method (generator cost, error propagation, evidence-page oracle).

### Error Log

| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E1 | Table 1, Qwen2.5-VL w/ image+text, Avg | "0.375 0.399 0.229 0.557 0.427" (row) | Row mean is (0.375+0.399+0.229+0.557)/4 = 0.390, not 0.427; other 15 rows' averages reproduce | Recomputed | High | MAJOR | Correct the average; restate comparisons |
| ERR-2 | E1 | §4.2 vs Table 1 | "from 0.389 to 0.370" | Table 1 prints 0.375 for Qwen2.5-VL w/ image+text on MMLongBench | Cross-referenced | High | MINOR | Align text and table |
| ERR-3 | E1 | Table 3, Qwen2.5-VL w/ image+text, Avg | "0.375 0.367 0.374 0.420 0.388 0.285" (row) | Mean of the five columns is 0.385, not 0.285 | Recomputed | High | MINOR | Correct (likely typo) |
| ERR-4 | E5 | §4.5 vs Table 1 | "We almost obtain the best results on almost" | Ours is the best of the three configurations in 10 of 16 cells; lower than image+text in 6 | Recomputed from Table 1 | High | MAJOR | Reword to what the table shows |
| ERR-5 | E6 | Table 3 vs Tables 1–2 | "w/ structured text" rows | Qwen2.5-VL avg 0.363 matches neither Table 1 (0.435) nor Table 2 (0.267) under either configuration reading | Cross-referenced (config naming ambiguous) | Medium | MAJOR | Define rows; reconcile |
| ERR-6 | E5 | §4.3 | "This 10% performance improvement fully demonstrates the importance of structure" | 0.389→0.435 is +0.046 absolute, +11.8% relative (Table 1) | Recomputed | High | MINOR | State absolute and relative gain |

## Missing References
Not my role (see Reviewer 2).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Matched control not used for claims; internal numeric inconsistencies; no variance |
| Clarity | 2 | Readable, but claims outrun tables and key setup is missing |
| Significance | 2 | A prompt rewrite with small gains over the proper baseline on 7B models |
| Originality | 2 | Reformatting OCR as markup is a modest idea |

## Dimension Scores (0–100)

**Pool position:** better than about 18% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main comparison is not against the matched control and, against it, the method loses in 6/16 cells and on average for the strongest model; the mechanism claim is untested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | Wrong control for headline; mechanism confound; numeric inconsistencies (ERR-1, 3, 5) |
| Clarity & Presentation | 55 | Competent | Readable and organized; overstated language; setup missing |
| Novelty & Originality | 42 | Developing | Format conversion via prompting; little differentiation |
| Significance & Impact | 42 | Developing | Small, uncertain gains over text+image |
| Experimental Validation | 32 | Developing | Single run, judge unvalidated, no format controls, no variance |
| Reproducibility | 38 | Developing | No prompts, generator model, decoding, per-benchmark settings or code |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations section is thin |

## Questions for Authors
1. Which MLLM generates the LaTeX (§3.2), with what prompt, and what is the added token/latency cost per page? An answer showing the generator is the same 7B model and the gain survives a plain-text rewrite control would raise my score.
2. Is the "image+text" row in Table 1 your run or numbers from Han et al. (2025), and with which prompt? If copied, settings may differ (lowers my confidence in all comparisons).
3. Which benchmarks use gold evidence pages and which use top-1 retrieval?
4. What are Table 3's rows exactly (see ERR-5)?
5. Can you show attention for the image+OCR condition?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. §6 poses research questions but does not state the method's limits (extra pass, error propagation from OCR/LaTeX generation, oracle evidence pages, 7B models only).

## Ethics Review Flag
**No**

## Overall Score
**2 (Reject)**: The central claim that structure (not extra, cleaner text) helps is not isolated, and the matched comparison is mixed to negative; evaluation is single-run with unvalidated scoring and internal numeric errors.

## Confidence
**4**: Recomputed all averages; no appendix or code was available.

---

# Peer Review Report

## Paper: Structured Attention Matters to Multimodal LLMs in Document Understanding
## Reviewer: Prof. Ilesha Dombrowski, Reviewer 2 (Domain) (public research university, North America; fictional persona)
## Expertise: Visually rich document understanding; table/structure serialization for LLMs
## Date: 2026-11-10

---

## Summary
The submission argues that how OCR content is formatted matters for general MLLMs answering questions about long documents, offers a prompt-based LaTeX re-encoding of the page's OCR text, and supports it with accuracy tables on four benchmarks and attention visualizations. Its stated gap is that "a critical question remains unexplored" about how the format of input information influences document understanding (§1).

## Strengths

### S1: A well-chosen question
Whether text and image inputs help or interfere with each other in document QA matters to practitioners building RAG pipelines (§1, §2 last paragraph), and the paper is right that most work focuses on retrieval or context length.

### S2: A format that is plausible for the content
LaTeX `tabular`/`section` markup (Figure 2) is a natural, compact way to keep table cell relations in text, and §4.5/Table 3 at least attempt a per-element breakdown.

### S3: Use of recent open MLLMs and recent document benchmarks
The evaluation covers Qwen2-VL, Qwen2.5-VL, LLaVA-v1.6 and Phi-3.5-Vision on MMLongBench, LongDocUrl, PaperTab and FetaTab (§4.1), which are current, appropriate document benchmarks.

## Weaknesses

### W1: The "unexplored" framing overstates the gap, and related work does not cover input-format studies
Related Work (§2) has two paragraphs on DocQA models and RAG, with nothing on how serialization format affects LLM/MLLM understanding of structured content, a literature that exists for tables (format sensitivity benchmarks such as Sui et al.'s table-serialization study; Singha et al., 2023 on tabular representations and noise), for retrieved web content (HtmlRAG: keeping HTML structure beat plain text as RAG input), and for MLLMs reading tables as LaTeX, HTML or images (RealHiTBench, ACL 2025). The paper cites none and so neither differentiates itself nor inherits their controls (e.g., comparing several serializations).
- **Suggested Fix**: Add a related-work paragraph on input-format sensitivity and position the LaTeX choice against HTML/Markdown/JSON serializations.

### W2: Novelty is modest and no differentiation is shown against structure-aware parsers
The method is a prompt that asks an MLLM to emit LaTeX from image + OCR (§3.2). Document parsers that already output markup from page images (Nougat) and structure-aware document models (mPLUG-DocOwl 1.5, which the paper cites, and layout-aware LLMs such as LayoutLLM, Fujitake, LREC-COLING 2024) address the same need for structure. No parser-based or layout-aware baseline is compared, so it is unknown whether LaTeX via prompting is better than existing ways to keep structure.
- **Suggested Fix**: Compare with at least one off-the-shelf structure-preserving parser and one non-LaTeX serialization.

### W3: The premise (C1) is contradicted by the paper's own table and rests on citations that do not obviously support it
§1 cites four works for "unstructured OCR text often degrades rather than enhances MLLM performance" (Cho et al., 2024; Deng et al., 2024; Han et al., 2025; Zhang et al., 2024a). By the bibliography titles, Zhang et al. 2024a studies OCR errors in RAG, and Han et al. (2025) is a framework that combines text and image evidence; I could not verify from the paper that either reports degradation from adding OCR text [verify]. Table 1 shows OCR text helps in 14 of 16 cells and raises every row average (e.g., LLaVA 0.116→0.219). The domain claim "OCR hurts" therefore holds for one benchmark at most.
- **Suggested Fix**: Narrow Observation 1 to the setting where it holds (MMLongBench with Qwen models, differences of 0.005–0.014) or provide evidence on more settings.

### W4: Attention interpretation is not positioned against the interpretability literature
Lower "attention scores at the borders" (Figure 3 caption) resemble known artifact/sink tokens in ViTs and attention sinks in LLMs, and attention weights are known not to be faithful explanations by themselves. The paper treats attention concentration as a causal mechanism without discussing either.
- **Suggested Fix**: Discuss attention-sink/register-token findings and attention-faithfulness debates; add an intervention.

### Literature-check addendum (strict mode, cutoff 2025-09-24)
Mode: strict. arXiv API was reachable but slow; 7 queries completed (claim 5, baseline 1, expansion 1; budget 12), plus one early attempt that timed out. Gaps left open: no prior work kept from 2022; the benchmark scout found no kept paper reporting on MMLongBench/LongDocUrl/PaperTab/FetaTab, so no baseline-scout rows and no under-reported baselines could be checked (limit of arXiv-only search, not evidence of absence). Similarity: closest prior works (all cosine ≤ 0.23, **no text overlap**, no flag for high conceptual overlap): LayoutLLM (0.226), Aida et al., 2025 (0.196), TableVQA-Bench (0.186).

**Per-claim novelty (claim-level profile)**

| Claim | Dimension | Novelty | Top prior work (level, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------|-----------|
| C1: OCR text hurts MLLMs | result | medium (no close prior found among the kept results; search covers arXiv only) | Zhang et al. 2024a (cited, level 2); Lost in OCR Translation (recent preprint, discuss only) | Related findings concern OCR errors in retrieval; the specific claim that adding OCR to images hurts is not established, and the paper's own data weakly supports it |
| C2: LaTeX-structured OCR text helps | method | medium (level 3) | HtmlRAG, WWW 2025, https://arxiv.org/abs/2411.02959 (level 3, prior peer-reviewed, not cited); Table Meets LLM, WSDM 2024 (level 3, not cited) | Same idea (structure-preserving markup beats plain text as LLM input) in neighbouring modalities; not the same task or mechanism |
| C3: structured attention is the mechanism | method/result | medium (level 2) | Baek et al., EMNLP 2025, https://arxiv.org/abs/2505.15865 (level 2, prior peer-reviewed, not cited) | Head-level analysis of how LVLMs read text in images; different question |

Paper reading: no established ("known") claim; no criterion-7 candidate. Closest to the paper as a whole: LayoutLLM (by similarity) and HtmlRAG (by idea).

**Novelty delta table**

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|------------------------------|------------------|---------------------------|
| LaTeX-structured text for document QA | HtmlRAG (Tan et al., WWW 2025) | Shows HTML-preserving input beats plain text for RAG with LLMs | Applies LaTeX re-encoding, with images, for MLLM DocQA | No |
| Format matters for table content | Table Meets LLM (Sui et al., WSDM 2024); RealHiTBench (ACL 2025) | Compares table serializations (and LaTeX/HTML/PNG for MLLMs in RealHiTBench) | Long-document multi-element setting, generated via MLLM | No |
| Layout-aware document LLMs | LayoutLLM (Fujitake, LREC-COLING 2024) | Instruction-tunes an LLM with layout for document understanding | Training-free and prompt-only | No |

**Baseline scout.** Not available (no kept results reporting on the four benchmarks). No claim of a missing required baseline is made from the search.

**Field snapshot.** Before the cutoff, document QA moved from OCR+layout pipelines fine-tuned per task, through OCR-free models, to general-purpose MLLMs with strong built-in text reading plus retrieval over page images or OCR text (ColPali and M3DocRAG, both cited by the paper, represent that line). Current open problems named by recent work include multi-page evidence localization, long multi-element contexts, and when text input helps or interferes with images. Studies of input serialization for tables and web content (kept results above) show structure-preserving formats help in text-only LLMs. In this sub-field a contribution is significant when it shows a mechanism with clean controls, or a clear capability or efficiency gain over strong text+image baselines on multi-page benchmarks; a few points over an image-only baseline from a prompt rewrite on 7B models is incremental. I used this to score Significance and Novelty (not above the venue's accepted papers' bar).

**Error Log (Domain, E7)**

| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-D1 | E7 | §1, para. 2 | "Current approaches typically extract OCR text but discard critical structural information" (cites Khattab and Zaharia, 2020; Faysse et al., 2024) | ColBERT (bibliography: passage search via late interaction over BERT) is text retrieval and does not address OCR or structure loss | Compared claim to bibliography title | Medium | MINOR | Cite works that show OCR pipelines discarding layout |

## Missing References
*Verified with `related_search.py verify` where marked with a link; otherwise described or marked `[verify]` (arXiv-only search; venue details from my knowledge).*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | None required: no verified prior (peer-reviewed or 6+ month) work does the same task with the same mechanism | n/a |
| Important | Tan et al., "HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems", WWW 2025 (https://arxiv.org/abs/2411.02959) | Structure-preserving markup beats plain text as LLM input; direct analogy for C2 |
| Important | Sui et al., "Table Meets LLM: Can Large Language Models Understand Structured Table Data? A Benchmark and Empirical Study", WSDM 2024 (https://arxiv.org/abs/2305.13062) | Systematic study of table serialization formats; model for the missing format controls |
| Important | Wu et al., "RealHiTBench: A Comprehensive Realistic Hierarchical Table Benchmark for Evaluating LLM-Based Table Analysis", ACL 2025 (https://arxiv.org/abs/2506.13405) | Evaluates MLLMs/LLMs across LaTeX, HTML and PNG inputs for complex tables |
| Important | Blecher et al., "Nougat: Neural Optical Understanding for Academic Documents", 2023 (https://arxiv.org/abs/2308.13418; ICLR 2024 [verify]) | Page-image-to-markup parsing; natural structure-preserving baseline |
| Helpful | Baek et al., "How Do Large Vision-Language Models See Text in Image? Unveiling the Distinctive Role of OCR Heads", EMNLP 2025 (https://arxiv.org/abs/2505.15865) | Head-level analysis of how LVLMs use text in images; informs the attention study |
| Helpful | Singha et al., "Tabular Representation, Noisy Operators, and Impacts on Table Structure Understanding Tasks in LLMs", 2023 (https://arxiv.org/abs/2310.10358) | Format effects and noise robustness for tables |
| Helpful | Darcet et al., "Vision Transformers Need Registers", ICLR 2024; Xiao et al., "Efficient Streaming Language Models with Attention Sinks", ICLR 2024 | Explain high-attention artifact/sink tokens relevant to the border-token observation (Figure 3) |
| Helpful | Jain and Wallace, "Attention is not Explanation", NAACL 2019 | Caution on reading attention as mechanism |
| Helpful | Wang et al., "DocLLM: A layout-aware generative language model for multimodal document understanding", ACL 2024 [verify] | Layout-aware document LLM |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Experiments exist but do not isolate the claimed factor |
| Clarity | 2 | Clear idea; related work thin |
| Significance | 2 | Useful practitioner hint if validated |
| Originality | 1 | Prompt-based format conversion with no differentiation from structure-aware parsers/serializations |

## Dimension Scores (0–100)

**Pool position:** better than about 26% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is a prompt-level reformatting whose advantage over plain OCR text is small and mixed, positioned against almost no relevant prior work.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 45 | Developing | Reasonable setup, but claims exceed controls |
| Clarity & Presentation | 56 | Competent | Clear but repetitive "convincingly demonstrates" language |
| Novelty & Originality | 38 | Developing | Limited novelty; no parser/serialization baselines |
| Significance & Impact | 45 | Developing | Narrow, 7B-scale evidence |
| Experimental Validation | 40 | Developing | Four benchmarks, but no format controls or structure-aware baselines |
| Reproducibility | 45 | Developing | Benchmarks public; prompts/generator missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. How does LaTeX compare with Markdown/HTML for the same content? A clear LaTeX advantage would raise Novelty.
2. Do you cite and run any structure-preserving parser (e.g., Nougat-style)? Their absence lowers my score.
3. Which results in the four works cited for C1 report degradation from adding OCR text?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (§6 only asks questions).

## Ethics Review Flag
**No**

## Overall Score
**2 (Reject)**: Modest idea, thin positioning against input-format and structure-aware literature, and a premise the paper's own table largely contradicts.

## Confidence
**4**: Know the sub-area; the literature check was limited to arXiv search.

---

# Peer Review Report

## Paper: Structured Attention Matters to Multimodal LLMs in Document Understanding
## Reviewer: Dr. Rafael Quispe-Ahn, Reviewer 3 (Perspective) (applied research institute, South America; fictional persona)
## Expertise: Information design and semantic markup; transformer interpretability
## Date: 2026-11-10

---

## Summary
The paper proposes giving MLLMs a LaTeX-marked-up transcription of a document page alongside the page image, reports accuracy gains over image-only inputs on four benchmarks, and offers attention maps as evidence that the markup "structures" the model's attention. The practical message is that input formatting is a free lever for document assistants.

## Strengths

### S1: An accessible practical lever
Because the approach is training-free and API-level (Figure 2 caption), it speaks directly to practitioners who cannot fine-tune, and the observation that adding raw text may not simply help is a useful caution for RAG designers (§3.1).

### S2: The question connects to information design
Semantic markup that exposes hierarchy (sections, tables, captions) is exactly what accessibility and document-engineering communities rely on, so a bridge between those traditions and MLLM inputs is promising.

### S3: Honest negative ablation
Table 2 reports that structured text alone is worse than OCR text alone, which is a real and instructive result about complementarity between modalities (§4.5).

## Weaknesses (as opportunities)

### W1: Deployment realism: the method adds a generation pass, assumes known evidence pages, and is evaluated on 7B models
§4.1 says evidence pages are located before OCR and conversion, and Table 1's caption says closed-domain runs use gold evidence pages. Each page needs an extra MLLM generation (§3.2) whose cost, error rate and failure modes (hallucinated cells, wrong LaTeX) are not reported. A practitioner cannot tell whether a 2× cost is worth +0.003 to +0.026 average accuracy over plain OCR (Table 1).
- **Suggested Fix**: Report per-page latency/tokens, a rate of faithful vs. hallucinated transcriptions on a sample, and an end-to-end retrieval-then-structure run.

### W2: Unchallenged assumption that attention distribution *explains* behaviour
§3.3/§4.4 treat lower border-token attention and "focused" maps as the cause of better answers. Border-token attention in image encoders often reflects artifact tokens, and adding text changes how attention is normalized. Interpretability work distinguishes correlational attention from causal intervention (attention knockout, activation patching).
- **Suggested Fix**: Add one intervention (e.g., redirect or ablate attention to the predicted-evidence region) and test whether accuracy moves accordingly.

### W3: Other structure carriers and domains are untested
The paper tests LaTeX only. Accessibility trees and DOM-like markup for web agents, Markdown tables, or JSON schemas are natural alternatives; scanned, handwritten or non-English documents, where OCR is noisy, would stress the claim that OCR text can hurt.
- **Suggested Fix**: Add one alternative format and one noisy-OCR setting (e.g., degraded scans).

### W4: Limitations/broader impact are almost absent
§6 consists of open questions. Failure cases are not shown (Figure 4 shows one success), and no discussion covers over-reliance on generated transcriptions in finance/legal documents (Figure 4's example is a financial report).
- **Suggested Fix**: Add a failure-case analysis and a short risk note on silent transcription errors.

## Missing References
No additional entries beyond Reviewer 2's. Connections to follow: attention sinks and register tokens in ViTs/LLMs (named methods), attention-faithfulness debates, and accessibility-tree representations used for web agents.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Directionally sensible, not controlled |
| Clarity | 2 | Easy to follow |
| Significance | 2 | Practical hint, narrow evidence |
| Originality | 2 | Familiar idea in a new setting |

## Dimension Scores (0–100)

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting, cheap, practical observation and honest negative ablation, but weak evidence and no mechanism test keep it below the accept bar.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Controls missing; causal claim untested |
| Clarity & Presentation | 56 | Competent | Easy to read |
| Novelty & Originality | 48 | Developing | Plausible, familiar idea in a new setting |
| Significance & Impact | 52 | Developing | Real practitioner interest if it holds up |
| Experimental Validation | 42 | Developing | Several models, thin controls |
| Reproducibility | 48 | Developing | Public benchmarks, missing prompts |
| Ethical Compliance | 62 | Competent | Little at stake; limitations thin |

## Questions for Authors
1. What is the per-page cost and transcription error rate of the LaTeX generation, and does the gain hold when evidence pages are retrieved rather than given? A positive answer would raise Significance.
2. Does the effect persist on noisy scans or non-English documents?
3. Can you show a failure case where structured text misleads the model?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No (questions only).

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: A promising and practical idea with honest ablation, but the evidence is too thin and the mechanistic claim untested to clear ICLR.

## Confidence
**3**: Outside the document-AI core; judged mainly the assumptions and deployment angle.

---

# Peer Review Report

## Paper: Structured Attention Matters to Multimodal LLMs in Document Understanding
## Reviewer: Dr. Priya Nakamura-Obi, Reviewer 4 (Generalist) (public research university, East Asia; fictional persona)
## Expertise: Vision-language models (general)
## Date: 2026-11-10

---

## Summary
The paper claims that in document question answering, raw OCR text next to a page image can hurt multimodal LLMs, that converting the OCR text to LaTeX-structured text restores and exceeds image-only accuracy, and that this works by making attention "structured". Four open 7B MLLMs and four benchmarks are used. One paragraph: the contribution is an observation plus a prompt-level preprocessing step plus an attention visualization, aimed at practitioners using general-purpose MLLMs for documents.

## Venue-criteria checklist (ICLR)

| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Not met | Table 1 vs. C1/C2; Observation 3 |
| Contribution: clear and significant | Partly | §3.2; gains small vs. matched control |
| Presentation: clear to a non-specialist | Partly | §3, Figure 2; overstated language in §4 |
| Reproducibility | Not met | §4.1 (no prompts, generator, decoding, code) |
| Honest limitations | Partly | §6 (questions only) |

## Strengths

### S1: Clear motivation and an easy-to-state idea
The title question and Figure 1 (contrasting retrieval-centric work with an input-format study) make the contribution easy to grasp; a non-specialist can follow §3.1–3.2 in one reading.

### S2: Breadth of models and benchmarks for a short paper
Four model families and four benchmarks (Table 1) is more than many short submissions provide, and the direction of the gain vs. image-only is consistent.

### S3: Useful negative finding
Table 2's result that structured text alone is ineffective is a good, honest observation about modality complementarity.

## Weaknesses

### W1: Claims are stronger than the evidence, and the writing leans on assertion
Phrases such as "clearly and convincingly support observation 1" (§4.2), "fully demonstrates the importance of structure" (§4.3) and "convincingly demonstrates" (§4.5) sit beside tables where OCR hurts in 2 of 16 cells and the method loses to plain OCR in 6 of 16 (Table 1). Observations 1–3 are written as if proven. A reader leaves unsure what the paper actually established.
- **Suggested Fix**: Rewrite claims as "in our settings" findings with the actual deltas; report gains versus the OCR baseline first.

### W2: The central comparison is not the one the title promises
For the claim that structure matters, the relevant row pair is image+OCR vs. image+structured; it is mostly buried, and three of four models gain at most +0.026 on average (Table 1). The paper's headline relative gains (e.g., +190.9%) come from weak image-only baselines (0.077 → 0.224 on PaperTab for Phi-3.5).
- **Suggested Fix**: Put image+OCR in the abstract-level comparison and show absolute gains.

### W3: Setup and reproducibility are too thin for the venue
No prompts, generator, decoding or per-benchmark sample counts (§4.1), and the limitations section (§6) is questions rather than limitations. ICLR reviewers will ask for these.
- **Suggested Fix**: Add an appendix with prompts (Figure 2 pipeline), generator model, n per benchmark, and code.

**Minor**: Table 2 caption "different datasets"; "ans" typo (§4.5); "10%" vs +11.8%; extraction-only observation: Figure 6 axis labels unreadable here.

## Missing References
Defer to Reviewer 2.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence does not match claims |
| Clarity | 2 | Readable, overclaiming |
| Significance | 2 | Narrow |
| Originality | 2 | Modest |

## Dimension Scores (0–100)

**Pool position:** better than about 34% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting practical observation, but a typical rejected submission pattern: small gain over the matched baseline, one weak mechanism analysis, small models.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | Overstated vs. data |
| Clarity & Presentation | 55 | Competent | Understandable; repetitive claims |
| Novelty & Originality | 42 | Developing | Modest |
| Significance & Impact | 46 | Developing | Narrow |
| Experimental Validation | 42 | Developing | Breadth good, control poor |
| Reproducibility | 44 | Developing | Missing prompts/code |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. Can you restate Table 1 with image+OCR as the reference and absolute gains? Showing a consistent advantage there would move me to a 4.
2. What would the community lose if this were rejected? Please state what a practitioner should do differently after reading it.
3. Does the benefit hold for models over 7B or for GPT-class APIs?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: Clear, practical, and interesting, but the evidence does not support the stated claims and the matched comparison is weak.

## Confidence
**4**: Broad familiarity with VLMs; did not dig into every derivation.

---

# Devil's Advocate Report

## Paper: Structured Attention Matters to Multimodal LLMs in Document Understanding
## Reviewer: Dr. Lars Eklund-Mbeki (industrial research lab, Europe/Africa; fictional persona)

---

## Steelman
Frozen MLLMs read document images imperfectly, and a cheap, model-agnostic rewrite of the page's text into structured markup may help them, particularly weaker models; the authors show consistent gains over image-only inputs on four benchmarks and offer attention evidence consistent with their story. If the effect is real it is a free, practical improvement.

## Core Argument Chain
1. P1: Adding raw OCR text to page images often hurts MLLMs (Observation 1).
2. P2: Adding LaTeX-structured text instead improves accuracy (Observation 2, Table 1).
3. P3: With structured text, attention becomes more focused (Observation 3, Figures 3, 5, 6).
4. P4: Therefore *structure* is what helped, and "structured attention is the key to helping MLLMs answer DocQAs".
∴ Preserving input structure improves general MLLM document understanding.

## Strongest Counter-Argument
The step from P2 to P4 is not licensed. The structured text is not a re-formatting of the OCR text; it is the output of an MLLM that re-reads the image and the OCR (§3.2). Everything that pass adds (corrections, chart transcription, removal of OCR noise, an explicit text summary of the page) is confounded with "structure". The only like-for-like control the paper has, image+OCR versus image+structured, does not show the effect it needs: three models gain 0.003–0.026 in average accuracy and the strongest model loses (Qwen2.5-VL 0.371 vs 0.390 recomputed; 0.221 vs 0.399 on LongDocUrl), and the method is below plain OCR in 6 of 16 cells (Table 1). Table 2 adds that structured text alone is worse than OCR alone for all four models, which is the opposite of what one expects if LaTeX structure made text easier to use. The headline percentages are measured against image-only rows, and they are largest where the image-only model is weakest (LLaVA, Phi), which is what one expects if any additional clean text helps a model that reads images poorly. The premise that OCR text "often" hurts is likewise contradicted: it hurts in 2 of 16 cells by 0.005 and 0.014, and it raises every model's average. Finally, the attention evidence is a single-model, aggregate, correlational observation with no OCR-text condition, so "structured attention is the key" is asserted, not tested. The authors need a control that holds the extra MLLM pass fixed while varying only the structure (plain rewrite, Markdown/HTML, shuffled LaTeX), and an intervention on attention. Without them the title claim has no experimental support and the effect may be an artifact of an extra, stronger transcription step.

## Issue List

### CRITICAL Issues

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence / Logic | Table 1, Table 2, §3.2, §4.5 | The central thesis (structure of the text is what helps) is not tested by the paper's design and the paper's own like-for-like control contradicts it: ours < image+OCR in 6/16 cells and on average for Qwen2.5-VL (0.371 vs 0.390), +0.003 to +0.026 for the other three; structured-only < OCR-only for all 4 models (Table 2); the structured text is MLLM-generated from the image, confounding format with extra processing. Criteria 1/2 (evidence does not support, and the experiment cannot isolate, the main claim). The "weaker claim" that survives (beats image-only) is not the claim of the title | Add equal-pass controls (plain MLLM rewrite; Markdown/HTML; shuffled/stripped LaTeX; parser output); report vs. image+OCR with CIs; narrow the title and claims if the effect does not survive | **New data/experiments** |

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §3.1 Obs. 1, Abstract, Table 1 | "often degrades" holds in 2 of 16 cells; OCR improves all four row averages. Claim distortion (E5); fix is narrowing | Restate Observation 1 as benchmark-/model-specific |
| DA-M2 | Logic | Obs. 3, §3.3, §4.4, Fig. 3/5/6 | Causal reading of attention; single model; no OCR condition; token-count confound; "370 samples with the same number of image tokens" selection unexplained | Add OCR condition, token-matched control, one causal intervention |
| DA-M3 | Evidence | §4.5 | "We almost obtain the best results on almost" every cell: 10/16 | Reword; show the cells |
| DA-M4 | Evaluation | §4.1, Table 1 | Single run, LLaMA-3.1-8B binary judge unvalidated, differences of 0.002–0.02, unstated n and setting per benchmark, baseline provenance unstated | Validate judge, report n, CIs, provenance |
| DA-M5 | Evidence | Table 3, §4.5 | Table 3 does not reconcile with Tables 1–2; element-type claim not supported (pure-text gains ≥ chart/table gains for LLaVA/Phi) | Define rows; revise claim |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Numbers | Table 1 (Qwen2.5-VL image+text Avg), Table 3 (Avg 0.285), §4.2 (0.370) | Arithmetic/consistency slips (ERR-1–3) |
| DA-m2 | Wording | §4.3 | "10% performance improvement" for 0.389→0.435 |
| DA-m3 | Presentation | Table 2 caption | "different datasets" for two datasets |

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Qwen2.5-VL w/ image+text Avg (Table 1) | 0.427 | (0.375+0.399+0.229+0.557)/4 = 0.390 | **No** |
| Qwen2.5-VL w/ image+text Avg (Table 3) | 0.285 | (0.375+0.367+0.374+0.420+0.388)/5 = 0.385 | **No** |
| OCR degradation on MMLongBench, Qwen2.5-VL (§4.2) | 0.389 → 0.370 | Table 1: 0.389 → 0.375 | **No** |
| Gain on MMLongBench, Qwen2.5-VL (Table 1) | +11.8% | 0.435/0.389 − 1 = +11.8% | Yes (text says "10%") |
| Ours Avg, Qwen2.5-VL (Table 1) | 0.371 | (0.435+0.221+0.252+0.575)/4 = 0.371 | Yes |
| Cells where OCR text lowers accuracy vs. image-only | "often" | 2 of 16 | **Overstated** |
| Cells where ours ≥ both rows | "We almost obtain the best results on almost" every cell (§4.5) | 10 of 16 | **Overstated** |

## Ignored Alternative Explanations
- The MLLM pass that writes the LaTeX corrects OCR errors and transcribes charts: the gain is from better text, not structure.
- Weak image readers benefit from any additional clean text; gains are inversely ordered by image-only strength.
- Judge noise: a binary 8B judge with unstated n and no CI can produce ±0.01–0.02 differences.
- Lower border-token attention can follow from added text tokens (softmax normalization) or artifact tokens, not "focus".

## Missing Stakeholder Perspectives
Practitioners paying for an extra generation pass per page; users of financial or legal documents (Figure 4's example is a financial report) who would suffer from silently hallucinated cells in the generated markup.

## Observations (Non-Defects)
- Table 2's honest negative result and the choice to report four models and four benchmarks are good practice.
- Relative gains in Table 1 reproduce from the printed accuracies.
- The method is cheap and easy to test; the DA-C1 controls are cheap too.

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 36 | Confounded design, wrong headline control |
| Clarity & Presentation | 52 | Overclaimed, internally inconsistent numbers |
| Novelty & Originality | 40 | Modest |
| Significance & Impact | 42 | Small gains vs matched baseline |
| Experimental Validation | 32 | No controls for the claim; single run |
| Reproducibility | 40 | Prompts, generator, settings missing |
| Ethical Compliance | 60 | Little at stake |

## Overall: 2 | Confidence: 4
Pool position: better than about 18% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper's own matched control contradicts the thesis.

---

# Phase 1.6: Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | Draft W: "no comparison with MDocAgent" | rewritten | Paper's baseline rows are attributed to Han et al. (2025) (Table 1); reframed as a provenance question (R1-W3, Q2) |
| R2 | ColBERT citation (§1) | moved to Minor/Error Log (ERR-D1) | Medium confidence, low severity |
| R2 | "Han et al. and Zhang et al. do not support C1" | rewritten as a question marked `[verify]` | Cannot verify cited abstracts from the paper alone |
| R3 | Draft W: "no code released" | moved to R1-W3 | Belongs to methodology; avoided duplication |
| R4 | Draft W: "figures unclear" | dropped | Figures unavailable; cannot judge. Stated in notice |
| R1 | W5 (Table 3) | kept; ERR-5 marked Medium confidence | Ambiguity in row definition acknowledged |
| DA | DA-C1 | kept; checked against Table 1/2 numbers | Recomputed (see EIC verification) |
| All | Typos/captions | moved to one Minor line each | Cosmetic |

Scores unchanged by this step. Weaknesses were ordered by severity within each report.

---

# Phase 2: Editorial Decision

## Synthesizer Part A: Issue Map and Official Score

| Merged issue | Sources | Class |
|--------------|---------|-------|
| Wrong/matched control: gains vs. image-only; vs. image+OCR small/negative | R1-W1, R2-W3, R4-W2, DA-C1, DA-M3 | CONSENSUS-4 (and DA-CRITICAL) |
| Structure confounded with extra MLLM pass; no format controls | R1-W2, R2-W2, R3-W3, DA-C1 | CONSENSUS-4 |
| Attention evidence correlational/under-specified | R1-W4, R2-W4, R3-W2, DA-M2 | CONSENSUS-4 |
| Single run, judge unvalidated, setup/prompts missing | R1-W3, R4-W3, DA-M4 | CONSENSUS-3 |
| Overclaiming wording; Observation 1 contradicted | R1 (ERR-4), R2-W3, R4-W1, DA-M1, DA-M3 | CONSENSUS-4 |
| Table 3 inconsistencies / element-type claim | R1-W5, DA-M5 | CONSENSUS-2 |
| Limited related work on input formats; novelty modest | R2-W1/W2 | SOLO |
| Deployment cost / failure cases / limitations | R3-W1, R3-W4, R1 limitations | CONSENSUS-2 |

**Official score** (`aggregate_scores.py`, BEFORE, DA-C1 provisionally upheld): official composite 44.5, official rating 2.4 (plain mean of R1 2, R2 2, R3 3, R4 3, DA 2). No consistency warnings. Dimension spreads ≤ 12 (no ⚠).

## EIC Meta-Review (Dr. Marguerite Okonkwo-Hale)

### The Case For and Against
- **For acceptance:** A cheap, model-agnostic intervention that improves four 7B MLLMs over image-only inputs on four recent benchmarks, with an honest negative ablation (Table 2) and a thought-provoking question (do text and image inputs interfere?).
- **Against acceptance:** The paper's own matched control (image+OCR vs. image+structured) shows no consistent gain and a loss for the strongest model; the structured text comes from an extra MLLM pass that is never controlled; the premise "OCR hurts" holds in 2 of 16 cells; the mechanism claim is correlational; evaluation is single-run with an unvalidated judge; several table numbers are wrong or inconsistent.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Qwen2.5-VL image+text Avg printed 0.427 | R1 ERR-1, DA | Table 1 | **Verified** | (0.375+0.399+0.229+0.557)/4 = 0.390 |
| OCR lowers accuracy in only 2 of 16 cells | R1, R2, DA-M1 | Table 1, §4.2 | **Verified** | Qwen2-VL and Qwen2.5-VL on MMLongBench, −0.005 and −0.014 |
| Ours below image+OCR in 6 of 16 cells; Qwen2.5-VL LongDocUrl 0.221 vs 0.399 | R1-W1, DA-C1, DA-M3 | Table 1 | **Verified** | LLaVA ×3, Phi ×2, Qwen2.5-VL ×1 |
| Avg gain vs. image+OCR: +0.013, +0.003, +0.026, −0.019 | R1-W1, DA-C1 | Table 1 | **Verified** | Recomputed |
| Structured-only worse than OCR-only for all four models | R1-W2, DA-C1 | Table 2 | **Verified** | e.g. 0.211 vs 0.253 (Qwen2.5-VL) |
| Structured text is generated by an MLLM from image + OCR | R1-W2, DA | §3.2 | **Verified** | "We input the image and the corresponding OCR text into the MLLM to obtain the structured code" |
| Table 3 does not reconcile with Tables 1–2 | R1 ERR-5, DA-M5 | Table 3 | **Partly correct** | Numbers do not match either reading; row definition is ambiguous so intent cannot be ruled out |
| No OCR-condition attention shown | R1-W4, DA-M2 | Fig. 3, 5, 6 captions, §4.4 | **Verified (captions only)** | Figures unavailable; captions and text compare only image vs. image+structured |
| Attention rise is a mechanical effect of token count | DA, R3 | §4.4 | **Partly correct** | Plausible reasoning, not measured here |
| Han et al. / Zhang et al. do not support C1 | R2-W3 | §1 | **Not verifiable** | Cited abstracts not provided; treated as a question |
| ColBERT citation does not support OCR claim | R2 ERR-D1 | §1 | **Verified (minor)** | Title/venue in bibliography is text retrieval |
| Gains are largest for weakest image-only models | R1-W2, DA | Table 1 | **Verified** | LLaVA +151.9%, Phi +75.1% (FetaTab) vs Qwen2.5-VL +13.2% |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Every Error Log item checked held (ERR-1–4, 6 verified; ERR-5 partly); decisive for the outcome |
| R2 (Domain) | 2 | 4 | 1.0 | Literature points sound, but C1-citation point not verifiable; default |
| R3 (Perspective) | 3 | 3 | 1.0 | Constructive and consistent with the verified issues; default |
| R4 (Generalist) | 3 | 4 | 1.0 | Well-calibrated to venue; mostly restates others |
| DA | 2 | 4 | 1.25 | Core objection verified against Tables 1–2; some mechanism points only partly verified |


### DA-CRITICAL Rulings

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | **Yes.** Given a paper whose title and thesis are "structure matters", I would reject on this alone: the only like-for-like comparison does not show the effect (Table 1: lower than plain OCR in 6/16 cells and on average for Qwen2.5-VL), structured-only is worse than OCR-only for all four models (Table 2), and the structured text is an MLLM output (§3.2) with no equal-pass control. It meets criterion 1/2 (evidence does not support, and the design cannot isolate, the main claim). It is not on the "never critical" list: the method does *not* improve over the best matched baseline | **Upheld** | New data/experiments |

### Final Decision and Justification
The EIC-weighted rating (R1 1.25, DA 1.25, others 1.0, each times confidence weight) is 2.34, which rounds to the starting point **2**; the official plain mean is 2.4, and the 0–100 composite (EIC 44.0, official 44.5, band 2) agrees, so there is no cross-check disagreement. I keep the starting point. The two reviewers who rated 3 (R3, R4) credit the idea and its practicality, but their stated conditions for a higher score (a consistent advantage over image+OCR, a deployment-cost answer) are exactly what Table 1 and §3.2 fail to show. The upheld DA-CRITICAL issue caps the decision at 3 (Borderline Reject) because the fix needs new experiments; the final decision of 2 does not exceed that ceiling. **My pool position: better than about 22% of ICLR submissions** (accepted share ≈ 27%). Deciding evidence: the headline finding is not isolated, and the one proper control contradicts it, which is the pattern of a typical rejected submission rather than a borderline paper whose weaknesses are common among accepted ones.

**Final Overall: 2 (Reject).**

## Score Summary

### Official Scores and EIC Assessment (aggregate_scores.py, `--venue iclr --final 2`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 38 | 45 | 48 | 46 | 36 | 42.6 | 41.9 | 12 |
| Clarity & Presentation | 55 | 56 | 56 | 55 | 52 | 54.8 | 54.6 | 4 |
| Novelty & Originality | 42 | 38 | 48 | 42 | 40 | 42.0 | 41.7 | 10 |
| Significance & Impact | 42 | 45 | 52 | 46 | 42 | 45.4 | 44.9 | 10 |
| Experimental Validation | 32 | 40 | 42 | 42 | 32 | 37.6 | 36.9 | 10 |
| Reproducibility | 38 | 45 | 48 | 44 | 40 | 43.0 | 42.5 | 10 |
| Ethical Compliance | 62 | 62 | 62 | 60 | 60 | 61.2 | 61.2 | 2 |
| **Composite** | 41.6 | 44.8 | 49.4 | 46.1 | 40.4 | **44.5 (before)** | **44.0 (after)** | |

Official ratings: R1 2, R2 2, R3 3, R4 3, DA 2 → mean **2.40**. EIC-weighted rating **2.34**. DA ceiling: **3**. Final (EIC): **2**. No warnings, no ⚠ spreads.

### Target-Venue Scores (ICLR, scale status: secondary; present with "verify against the current form")

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 1 |
| Rating | **2 on {0,2,4,6,8,10}** (3 on the earlier {1,3,5,6,8,10} scale); venue composite 43.8 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Structured Attention Matters to Multimodal LLMs in Document Understanding" to ICLR. The question of how input format interacts with page images in MLLM document understanding is a useful one.

**Overall Assessment:** The panel found a simple, training-free idea and appreciated the honest ablation that structured text alone does not work (Table 2). However, the central claim that the *structure* of the text drives the gains is not isolated by the experiments, and the paper's own matched comparison does not support it.

**Key Strengths Identified by Reviewers:**
1. A cheap, API-level intervention evaluated on four MLLM families and four benchmarks (R1, R3, R4).
2. A clear, relevant question with a useful negative ablation in Table 2 (R2, R3, R4).
3. Consistent gains over image-only inputs, reproducible from the printed table (R1, R4).

**Key Concerns Requiring Attention:**
1. Headline gains are over image-only inputs; against image+unstructured OCR, gains are +0.003 to +0.026 for three models and negative for Qwen2.5-VL (Table 1), and the method is lower than OCR in 6 of 16 cells (CONSENSUS-4).
2. The structured text is generated by an MLLM from the image (§3.2), so format is confounded with an extra processing pass; no equal-pass or alternative-format controls (CONSENSUS-4).
3. The attention analysis is correlational, single-model and lacks the OCR condition (CONSENSUS-4).
4. Single-run evaluation with an unvalidated judge; missing prompts, generator, per-benchmark setup; numeric errors (Table 1 Avg, Table 3 Avg) (CONSENSUS-3).
5. The claim that OCR text often hurts is true in 2 of 16 cells (CONSENSUS-4).

**Critical Challenge (Devil's Advocate):** The step from image + structured text beating image-only to structure being the key is unsupported; the paper's own like-for-like control and Table 2 point the other way. This must be addressed with equal-pass controls and an attention intervention.

**Decision: Reject (2)** (ICLR rating 2 on {0,2,4,6,8,10}).

The upheld critical issue needs new experiments, which is beyond clarification. A resubmission that adds the controls in the Roadmap, reports gains against image+OCR with confidence intervals, validates the judge, and narrows the claims to what the data show would be a considerably stronger paper. Please refer to the Revision Roadmap.

Sincerely,
Dr. Marguerite Okonkwo-Hale
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)

| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Matched control missing / gains small vs. image+OCR | R1, R2, R4, DA | CONSENSUS-4 |
| Format confounded with extra MLLM pass; no format controls | R1, R2, R3, DA | CONSENSUS-4 |
| Attention evidence is correlational | R1, R2, R3, DA | CONSENSUS-4 |
| Overclaiming / Observation 1 not supported | R1, R2, R4, DA | CONSENSUS-4 |
| Single run, unvalidated judge, missing setup | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement

| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the idea/finding valuable enough to overcome weak evidence? | R3, R4 (Overall 3) | R1, R2, DA (Overall 2) | Both sides agree on the facts; the difference is how much potential counts. Evidence points to Reject because the decisive control is already in Table 1 and is negative/mixed |
| Table 3 as evidence of element-type effects | (authors, §4.5) | R1, DA | Table 3 does not reconcile with Tables 1–2; claim not relied upon |

### Score Spread Discussion
No dimension is flagged ⚠ (max spread 12, Technical Rigor). Clarity scores agree within 4 points.

### Devil's Advocate Highlights

| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Structure not isolated; matched control contradicts the thesis | Yes (R1-W1/W2, R2-W2, R4-W2) | **Upheld** | New data/experiments |
| DA-M1 | MAJOR | Observation 1 overstated (2/16 cells) | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Attention causal claim | Yes (R1, R2, R3) | n/a | n/a |
| DA-M3 | MAJOR | "best results on almost" every-cell claim (§4.5) | Yes (R1 ERR-4) | n/a | n/a |
| DA-M4 | MAJOR | Single run; judge unvalidated; unstated protocol | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Table 3 inconsistency | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Structure not isolated from the extra MLLM pass | DA-C1, R1-W2, R2-W2 | §3.2, Table 1, Table 2 | Equal-pass controls: MLLM plain-text rewrite; Markdown/HTML/JSON; shuffled or stripped LaTeX; one structure-preserving parser baseline. Same generator, report cost | High; ~100–200 A100-h | Partly (one model, one benchmark) |
| R2 | Headline comparison against wrong control; gains vs. image+OCR not significant/negative for Qwen2.5-VL | DA-C1, R1-W1, R4-W2, DA-M3 | Table 1, §4.3, §4.5 | Reframe all tables vs. image+OCR; paired bootstrap CIs; reword the best-results claim | Low | Yes |
| R3 | Correct numeric/consistency errors | R1 ERR-1–3, 5, 6 | Table 1 Avg, §4.2, Table 3, §4.3 | Fix averages, align text, define Table 3 rows, reconcile with Tables 1–2 | Low | Yes |
| R4 | C1 as stated is contradicted | DA-M1, R1, R2-W3 | Abstract, §3.1, §4.2 | Narrow to "in some settings"; document where OCR hurts (MMLongBench, Qwen) | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Attention analysis non-causal and under-specified | R1-W4, DA-M2, R3-W2 | Add OCR condition, token-matched control, region-level attention mass, one intervention | Medium; ~20–40 GPU-h | Partly |
| S2 | Single run; unvalidated judge; missing n, prompts, decoding, generator, provenance of baseline rows | R1-W3, R4-W3, DA-M4 | Report all; human-label subset for judge κ; ≥3 decoding/prompt seeds on two benchmarks; release prompts/code | Medium; ~30 GPU-h | Yes |
| S3 | Related work on input-format sensitivity and structure-aware parsers | R2-W1/W2 | Add and compare: HtmlRAG, Table Meets LLM, RealHiTBench, Nougat-style parser; fix ERR-D1 | Low–Medium | Yes (discussion) |
| S4 | Deployment cost and realism (extra pass, oracle evidence pages, 7B only) | R3-W1 | Report latency/tokens; run with retrieved pages; add a larger model | Medium | Partly |
| S5 | Element-type claim in §4.5 | R1-W5, DA-M5 | Restate using corrected Table 3 | Low | Yes |

### Priority 3 — Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Noisy-OCR/non-English settings; alternative structure carriers | R3-W3 | Add one degraded-scan setting |
| N2 | Failure cases and risk note on transcription errors | R3-W4 | Add examples and a short note |
| N3 | Attention-sink/register and attention-faithfulness references | R2-W4, R3 | Discuss Darcet et al.; Xiao et al.; Jain & Wallace |
| N4 | Caption/typo fixes (Table 2 caption, "ans") | R1, R4 | Fix |
| N5 | Replace limitations questions with limitations | R1, R3, R4 | Rewrite §6 |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 2–3 weeks (controls dominate; ~100–200 GPU-hours)
- Priority 2: 5 items, roughly 1–2 weeks
- Priority 3: 5 items, 2–3 days
- **Total estimated revision time**: about 4–5 weeks

*Journal mapping not applicable (conference target). Cross-venue outlook not requested. Gap Scout not requested.*
