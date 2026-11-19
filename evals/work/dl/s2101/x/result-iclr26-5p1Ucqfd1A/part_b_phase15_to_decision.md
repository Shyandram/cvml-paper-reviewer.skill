
---

## Phase 1.5: Literature Check (Domain Reviewer addendum)

**Run:** `literature check: strict` (everything after 2025-09-24 dropped); arXiv API via `scripts/related_search.py`; 9 of 12 queries (claim queries: C1 ×2, C2 ×3, C3 ×1, C4 ×1; expansion ×2); 96 kept candidates after self-exclusion filtering; 6 titles checked with `verify` (5 found, Ego4D not found by title). Paper's own benchmark gives `benchmarks` = none, so no baseline scout table applies (the paper reports on its own benchmark only). **Gaps left open:** search is arXiv-only and abstract-level; Dyn-VQA, Encyclopedic-VQA and MRAG-Bench were confirmed by title lookup but did not surface in claim queries, so they are not in the claim-level profile and the verdicts below may understate coverage. `similarity`: closest prior works have cosine ≤ 0.155, no high conceptual overlap (threshold 0.30), no text overlap (0 shared 8-grams): no integrity flag.

### Per-claim novelty (claim-level profile; levels are my ratings from abstracts, `novelty` script output)

| Claim | Dimension | Novelty (script) | Top prior work (level, verified link, label, cited?) | Reasoning |
|-------|-----------|------------------|------------------------------------------------------|-----------|
| C1 first wearable MM-RAG benchmark | problem | medium (coverage 0.39) | MMSearch (3) https://arxiv.org/abs/2409.12959v2, prior (arXiv-only), not cited | Multimodal search benchmarks exist; the egocentric / wearable framing with image-KG + web APIs is the new part |
| C2 dataset (6.2K egocentric images, 13 domains, slices) | resource | medium (0.39) | InfoSeek (3) https://arxiv.org/abs/2302.11713v5, prior (peer-reviewed, EMNLP 2023), not cited | Entity-centric info-seeking VQA exists; egocentric capture, popularity buckets and multi-turn are new |
| C3 mock image-KG / web APIs | resource | medium (0.42) | MMSearch (3), not cited | MMSearch provides a multimodal search pipeline for LMMs; fixed corpora with hard negatives differ |
| C4 results (≈ 32% / 43–45%) | result | high (0.25) | EgoBlind (2) https://arxiv.org/abs/2503.08221v4, prior (peer-reviewed), not cited | No prior work reports these quantities; EgoBlind shares only "models struggle" |

Script paper reading: no established claim; "no close prior work found" is not claimed anywhere (search is arXiv-only), so no verdict is above *medium* for C1–C3. No candidate for DA criterion 7.

### Novelty delta table (closest prior works)

| Claimed contribution | Closest prior work (link) | What that work already does | What is new here | Cited and differentiated? |
|----------------------|---------------------------|-----------------------------|------------------|---------------------------|
| C1 wearable MM-RAG benchmark | MMSearch (arXiv 2409.12959) | Benchmarks LMMs as multimodal search engines over web pages | Egocentric smart-glasses images, image-KG API, truthfulness metric, multi-turn | No |
| C2 entity-centric dataset | InfoSeek (arXiv 2302.11713) | Info-seeking VQA needing entity knowledge | Egocentric capture, six question types, popularity, conversations | No |
| C2/C3 visual-knowledge retrieval | Visual-RAG (arXiv 2502.16636) | Text-to-image retrieval QA, isolates retrieved-image use | Image-to-KG retrieval, web retrieval, wearable domain | No |
| C1 egocentric assistance | EgoBlind (arXiv 2503.08221) | Egocentric video QA collected from blind users, 16 MLLMs evaluated | Still images with retrieval, factual (not situational) questions | No |
| Closest by text similarity | RAG-Check (arXiv 2501.03995), cos 0.155 | Reliability measures for multimodal RAG | Different problem (benchmark, not metric) | No |

### Field snapshot (as of the cutoff)
Knowledge-based VQA began with OK-VQA (2019) and A-OKVQA (2022), where outside knowledge was commonsense or from a fixed source; InfoSeek (2023) moved to entity-level, retrieval-needing questions. In 2024–2025 the focus shifted to LMMs as multimodal search engines (MMSearch; Vision Search Assistant), multimodal-RAG benchmarks (Visual-RAG, MRAMG-Bench) and surveys of multimodal RAG, while egocentric assistants (EgoBlind, EgoLife) show interest in wearable settings, mostly with video and without retrieval. Open problems stated by recent work: reliable retrieval across modalities, hallucination under noisy retrieval, and evaluation that isolates what retrieval contributes. A significant benchmark contribution now is a new capability setting with trustworthy labels, a metric that separates abstention from error, and analysis that shows what drives difficulty; yet another VQA set with similar accuracy is incremental. I used this to score Significance 68 and Novelty 60: the setting is new, the analysis of *why* it is hard is thin.

### Verified missing references (citation-integrity rule; links from `verify`)

| Priority | Reference | Verification | Why it matters |
|----------|-----------|--------------|----------------|
| Critical | Chen et al., "Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?", EMNLP 2023 | Found: https://arxiv.org/abs/2302.11713v5 (prior, peer-reviewed) | Entity-centric knowledge VQA; supports/qualifies C1–C2 |
| Critical | Mensink et al., "Encyclopedic VQA: Visual questions about detailed properties of fine-grained categories", ICCV 2023 | Found: https://arxiv.org/abs/2306.09224v2 | Fine-grained entity VQA with a retrievable knowledge base |
| Important | Li et al., "Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent", 2024 | Found: https://arxiv.org/abs/2411.02937v5 (prior, arXiv-only at cutoff) | Multimodal-RAG benchmark with changing knowledge; bears on "dynamism" and "first" |
| Important | Hu et al., "MRAG-Bench: Vision-Centric Evaluation for Retrieval-Augmented Multimodal Models", 2024 | Found: https://arxiv.org/abs/2410.08182v2 | Multimodal-RAG benchmark predating CRAG-MM |
| Important | Jiang et al., "MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines", 2024 | Found: https://arxiv.org/abs/2409.12959v2 | Closest search-pipeline benchmark (above) |
| Helpful | "EgoBlind: Towards Egocentric Visual Assistance for the Blind", NeurIPS 2025 Datasets & Benchmarks track (per arXiv comment) | Found: https://arxiv.org/abs/2503.08221v4 | Egocentric assistive QA collected from real users |
| Helpful | Grauman et al., "Ego4D: Around the World in 3,000 Hours of Egocentric Video", CVPR 2022 `[verify]` | Not found by title on arXiv; keep `[verify]` | Egocentric data practice, de-identification |

Only the two *prior* labels can be required comparisons; all rows above are prior. None is a "missing baseline" (CRAG-MM reports on its own data). Missing related work is a MAJOR-at-most positioning issue.

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2-W1 | "WebQA ... image and web search" | rewritten | Consistency: Table 1 footnotes (a, b) say retrieval is prefetched; wording now includes it |
| DA-M3 | "WebQA row ... multimodal" | rewritten | Same footnote correction |
| R4-W2 | "industry SOTA ... not products" | rewritten | §5.2 already says "built upon MM-LLMs and search engines"; the point is abstract clarity only |
| R3-W3 | "many entities are US-centric" | rewritten | Only the shown examples (Fig. 1) support it |
| R4-W3 | "figure-dependent claims hard to check" | rewritten as a clarity question | Extraction artifact: figures unreadable; now asks only for the reference base of "dropped by up to X%" |
| R1-W7 | threshold / prompt choices unspecified | moved to Minor | Unlikely to change conclusions |
| R3-W4 | cross-field links | kept, ordered last | Expansion suggestion, Priority 3 |
| R1-W1…W6, R2-W2…W4, R3-W1…W3, R4-W1, DA-M1, M2, M4–M7 | — | kept | Specific, not answered in the paper (searches: annotator agreement, privacy/consent/licence, dynamism, egocentric QA comparison, limitations: none found), consistent with the paper, actionable |

Scores were not changed. Checked "not already answered": no appendix section reports annotator agreement, privacy, limitations, an egocentric-vs-public QA result, or a dynamism analysis.

---

## Phase 2: EIC Meta-Review and Decision

### Synthesizer package (Part A)

**Integrity signals:** none (scan clean). **Literature check:** strict, no text-overlap flag, no criterion-7 candidate.

**Issue list and consensus classes**

| Issue | Sources | Class | Hinges? |
|-------|---------|-------|---------|
| No limitations, ethics or privacy statement | R1-lim, R2-lim, R3-W1, R4-lim, DA-M7 | CONSENSUS-5 (privacy specifically: CONSENSUS-2, R3-W1, DA-M7) | Ethics flag |
| Abstract/intro claims drift from evidence ("dynamism", "first", "+28%", counts) | R1-ERR-1/W3, R2-W1, R4-W2, DA-M2/M3 | CONSENSUS-4 | Yes |
| Headline comparisons mix split / retrieval / model; gain is abstention | R1-W3, R4-W2, DA-M2 | CONSENSUS-3 | Yes |
| Egocentric differentiator not tested on QA results | R1-W6, R2-W4, DA-M5 | CONSENSUS-3 | Yes |
| Related work / Table 1 selective; missing prior benchmarks | R2-W1, DA-M3, R4-W1 | CONSENSUS-3 | Yes |
| Label (annotation) quality unvalidated | R1-W1, DA-M6 | CONSENSUS-2 | Yes |
| Judge validation weak ("Incorrect" precision 68.1) | R1-W2, DA-M4 | CONSENSUS-2 | Yes |
| No variance; slice sizes vs public-test size | R1-W4, R4-W3 | CONSENSUS-2 | |
| Retrieval world built around questions; realism unvalidated | R1-W5, R3-W3 | CONSENSUS-2 | |
| Frozen ground truth vs live web (staleness) | DA-M1 | SOLO | Yes |
| Template-generated questions contradict critique of prior work | R2-W2 | SOLO | |
| No latency / cost reporting | R3-W2 | SOLO | |
| Multi-turn data generated by an evaluated model | DA-M6 | SOLO | |

**SPLIT issues:** none. **DA-CRITICAL:** none raised. **Score spreads:** all ≤ 12 points (no ⚠). Pool positions range 52–72 (spread 20, below the 30-point trigger).

**Official output (before EIC weights)** (`before.json`): official mean rating 3.60; official composite 60.1; ratings R1 3, R2 4, R3 4, R4 4, DA 3.

### EIC Meta-Review (Dr. Ingrid Solheim)

**The case for acceptance.** A new, usable resource: 6.2K smart-glasses images, mock image-KG and web APIs with hard negatives, six question types and multi-turn conversations, with transparent prompts, versions and dates, nine baseline MM-LLMs and a public competition. The numbers I could recompute (Tables 2–5) are consistent, and the authors flag the non-comparable rows. It fills a niche that existing knowledge-VQA sets do not cover.

**The case against acceptance.** The headline "challenging" reading rests on labels with no reported quality check, a judge whose "Incorrect" class has precision 68.1, single runs, and non-comparable headline rows (+28 points across splits, mainly abstention). The differentiating property (egocentric) is never shown to drive difficulty, the abstract promises a "dynamism" dimension that does not exist in the paper, and there is no privacy, consent, licence or limitations statement for daily-life captures.

**Verification of decisive points (EIC read of the paper)**

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "Dynamism" never analysed | R1-ERR-1, R4-W2 | Abstract; text search | Verified | One hit only, in the abstract |
| +28% is 28.3 points across splits, driven by abstention | R1-W3, DA-M2 | Table 5, §5.2 | Verified | 19.7 − (−8.6); accuracy 35.3 → 29.3; hallucination 43.9 → 9.6; §5.2 admits non-comparability |
| Egocentric vs normal never compared on QA | R1-W6, DA-M5, R2-W4 | Fig. 4 panel titles, Fig. 6 / App. A.5.2 | Verified | Retrieval recall only; Fig. 4 slices are image quality, OCR, popularity, type, context, turns |
| Judge "99.1%" hides weak Incorrect class | R1-W2, DA-M4 | Table 7, §4 | Verified | Precision 68.1, F1 78.2; n and systems unstated |
| R1's "≈ 11-point truthfulness swing" from judge error | R1-W2 | Table 7 | Overstated | Needs an extreme error flow; my estimate under a plausible flow is ≈ 6 points downward, still comparable to between-system gaps |
| No annotation-quality evidence | R1-W1 | §3.2, App. A.3–A.4 | Verified | No annotator count, agreement, removal rate (search) |
| Slice margin-of-error claim | R1-ERR-2 | §3.2, Table 3, §3.4 | Partly correct | Holds at full-set size for most question-type slices; fails at public-test size; split sizes not stated |
| Frozen ground truth vs live-web industry runs | DA-M1 | Fig. 1, Fig. 2, App. D | Partly correct | Dates and volatile answers verified; that scoring was actually biased is not demonstrated |
| "First MM-RAG benchmark" and selective Table 1 | R2-W1, DA-M3 | §1, Table 1 | Partly correct | Prior multimodal-RAG benchmarks exist (verified, lit. check); WebQA is footnoted as prefetched, so a narrowed "first" is defensible |
| Template critique inconsistent | R2-W2 | §1, §3.2, App. A.3 | Verified | |
| No privacy / consent / licence statement | R3-W1 | §3.1, §3.4 | Verified | Text search: none |
| Multi-turn truthfulness ≠ Acc − Hallu | R1-ERR-3 | Tables 4, 5 | Verified | 42.2 − 32.8 = 9.4 vs 12.7; macro-averaging (§4) likely explains it |
| Single-turn table arithmetic consistent | R1-S2, DA | Tables 4, 5 | Verified | Acc + Miss + Hallu ≈ 100; Truth = Acc − Hallu |
| Popularity: balanced buckets vs "21% torso-to-tail" | R1-ERR-4 | §3.1 vs §1 | Partly correct | Possibly balanced only on the KG-based subset |
| 15% low-quality egocentric | R1-ERR-5 | §1, Table 2 | Verified (minor) | 13.9% egocentric; 15.2% overall |

**Reviewer weights**

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points verified (no dynamism, no label QA, cross-split +28, weak judge class); one estimate overstated; calibration slightly harsh |
| R2 (Domain) | 4 | 4 | 1.0 | Positioning points verified by the literature check; one wording corrected in report check |
| R3 (Perspective) | 4 | 3 | 1.0 | Privacy gap verified; remaining points reasonable but generic |
| R4 (Generalist) | 4 | 4 | 1.0 | RQ1 and wording-drift points verified; calibrated to the venue |
| DA | 3 | 4 | 1.0 | Most issues survive (M1 partly, M3 partly); no CRITICAL inflation |

**DA-CRITICAL rulings:** none raised ("No CRITICAL issues found"). I agree: no verified leakage, no contradiction of the main claim, and no fabricated or inconsistent headline number. DA ceiling: none.

**Scores.** Official ratings R1 3, R2 4, R3 4, R4 4, DA 3 → official mean **3.60**, official composite **60.1**. EIC-weighted rating **3.56** → starting point **4**. EIC-weighted composite **59.8** → band 3; cross-check flagged ⚠.

**Final decision.** I keep the starting point: **Final Overall 4 (Borderline Accept)**, ICLR label "6 on {0,2,4,6,8,10}" with Soundness 2 / Presentation 3 / Contribution 3 (scale status: secondary). The composite sits 0.2 below the band edge (60) and is pulled down mainly by Ethical Compliance (5% weight, mean 45) and Experimental Validation (55); this is a boundary swap, not a verified issue the ratings missed, and every issue behind the low dimension scores appears in the reviewers' own Overall ratings. I could name no verified issue that the ratings did not already account for, so I do not depart. My pool position is **65**: better than about 65% of ICLR submissions. Deciding evidence: a genuinely useful resource with real egocentric data, runnable retrieval APIs and transparent baselines, adopted in a public challenge (the paper's claim; not independently checked), against fixable evidence gaps (labels, judge, variance, egocentric analysis, privacy) that are typical of resource papers at this venue. If the claims in the abstract are not narrowed and the label and judge audits are not added, I would move this to Borderline Reject. The decision does not exceed any DA ceiling (none applies). It is a simulation of how a careful panel would likely see this draft, not a prediction.

---

## Editorial Decision

**Paper:** CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark · **Date:** 2026-11-10 · **Target Venue:** ICLR · **Paper Type:** benchmark
**Review Team (fictional personas):** EIC Dr. Ingrid Solheim; R1 Dr. Tomasz Wieczorek (Methodology); R2 Prof. Amara Okonkwo-Reyes (Domain); R3 Dr. Kenji Hayashida (Perspective); R4 Dr. Priya Raghunathan (Generalist); DA Prof. Daniel Mbeki-Larsen

### Decision: Borderline Accept (4) · ICLR label: 6 on {0,2,4,6,8,10} (6 on {1,3,5,6,8,10}); Soundness 2, Presentation 3, Contribution 3 (scale status: secondary)

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60 · official composite 60.1
**EIC assessment** (internal): weighted rating 3.56 → starting point 4 · weighted composite 59.8 → band 3 (cross-check ⚠, boundary) · **DA ceiling**: none · **Final (EIC)**: 4 · EIC pool position 65

### Score Summary (from `aggregate.json`, `--final 4`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 55 | 62 | 64 | 62 | 52 | 59.0 | 58.6 | 12 |
| Clarity & Presentation | 62 | 64 | 66 | 64 | 62 | 63.6 | 63.4 | 4 |
| Novelty & Originality | 58 | 60 | 62 | 60 | 52 | 58.4 | 58.3 | 10 |
| Significance & Impact | 66 | 68 | 74 | 68 | 62 | 67.6 | 67.3 | 12 |
| Experimental Validation | 50 | 58 | 60 | 60 | 48 | 55.2 | 54.8 | 12 |
| Reproducibility | 56 | 62 | 64 | 62 | 56 | 60.0 | 59.7 | 8 |
| Ethical Compliance | 45 | 50 | 42 | 48 | 42 | 45.4 | 45.5 | 8 |
| **Composite** | 57.2 | 61.9 | 64.2 | 62.2 | 54.8 | **60.1 (before)** | **59.8 (after)** | |

Target-venue scores (ICLR 2026, scale status: secondary; wording not official): Soundness 2, Presentation 3, Contribution 3; rating label "6 on {0,2,4,6,8,10}". Earlier-cycle scale {1,3,5,6,8,10} also gives 6. Only the ICLR venue was requested; no cross-venue comparison was made.

### Editorial Decision Letter

Dear Authors,

Thank you for submitting "CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark" to ICLR. A benchmark for factual, image-grounded assistance on wearable devices addresses a timely and practically important setting.

**Overall Assessment:** The panel saw a useful and carefully assembled resource whose headline conclusions are not yet backed by enough validation. Reviewers agreed on the value of the egocentric data, retrieval APIs and transparent reporting, and on a shared set of gaps in label, judge and statistical validation and in the framing of the claims.

**Key Strengths Identified by Reviewers:**
1. A new combination: egocentric smart-glasses images with image-KG and web retrieval APIs, six question types and multi-turn conversations (R2, R3, R4).
2. Transparent, auditable evaluation: prompts, model versions, call dates, separate accuracy/missing/hallucination reporting; internally consistent tables (R1, R4, DA).
3. Broad baselines, practical grounding and demonstrated community use (R1, R3, R4).

**Key Concerns Requiring Attention:**
1. Claims drift from evidence: "dynamism" (CONSENSUS-4); "+28%" is 28.3 points across splits and mostly abstention (CONSENSUS-3); "first" claims and a selective Table 1 (CONSENSUS-3).
2. The egocentric property is not tested on QA results (CONSENSUS-3).
3. Label and judge validity are unreported (annotation agreement; "Incorrect" precision 68.1) (CONSENSUS-2 each), with no confidence intervals.
4. No privacy, consent, licence or limitations statement for daily-life captures (CONSENSUS-5 on limitations; ethics flag raised by R3).

**Decision: Borderline Accept (4).** The contribution outweighs the weaknesses, which are fixable with existing data and modest annotation effort, but the abstract and headline comparisons need to be brought in line with the evidence, and the privacy statement is required. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Ingrid Solheim, Editor-in-Chief (meta-reviewer; fictional persona)

### Consensus and Disagreement Map

**Points of consensus (3+ reviewers):** see the issue list above (limitations CONSENSUS-5; claim drift CONSENSUS-4; headline comparisons, egocentric, related work CONSENSUS-3).

| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the weakness set fatal or typical? | R1, DA (Overall 3) | R2, R3, R4 (Overall 4) | Typical of resource papers and fixable; no fatal flaw verified (EIC) |
| "First" claim | R2, DA | Table 1 footnotes (prefetched retrieval) | Narrow the claim to the supported combination |

**Score spread discussion:** no dimension exceeds the 20-point spread flag; the largest spreads (12) are Technical Rigor, Significance and Experimental Validation, from R1/DA (stricter) vs R3 (more positive); the editor adopts the middle, weighting R1 slightly higher.

### Devil's Advocate Highlights

| Issue ID | Severity | Issue | Raised by others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| (none) | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Frozen ground truth vs live-web systems | Partly (R1-ERR-1) | Partly correct | Existing data + re-verification of time-sensitive items |
| DA-M2 | MAJOR | +28 points across splits, abstention | Yes (R1-W3, R4-W2) | Verified | Clarification / same-split rerun |
| DA-M3 | MAJOR | "First", "comprehensive" overclaim | Yes (R2-W1) | Partly correct | Rewording, Table 1 |
| DA-M4 | MAJOR | Judge validation | Yes (R1-W2) | Verified | Small new validation sample |
| DA-M5 | MAJOR | Egocentric untested | Yes (R1-W6, R2-W4) | Verified | Existing results, re-sliced |
| DA-M6 | MAJOR | Generator bias in multi-turn | No | Partly correct | Removal stats, small analysis |
| DA-M7 | MAJOR | No limitations / ethics | Yes (R3-W1) | Verified | Writing |

---

## Revision Roadmap

### Priority 1: Required (must fix)

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Abstract / intro claims drift: "dynamism", "+28%" (points, cross-split, abstention), "first", "industry solutions", counts (8K, 21%, 15%) | R1-ERR-1/5, R2-W1, R4-W2, DA-M2/M3 | Abstract, §1, §5.2, Table 5 | Remove or define "dynamism"; say "+28 points (private vs public)"; narrow "first"; define industry systems as tool-enabled APIs; reconcile counts | Low | Yes |
| R2 | Same-split, same-corpus comparison and an always-abstain (0) / risk–coverage reference | R1-W3, DA-M2, R3-W3 | Tables 4–5, §5.2 | Re-run one baseline and one winner on one split; add a truthfulness-0 reference and a risk–coverage plot | Medium (≈ 20–40 GPU-h or API cost) | Partly |
| R3 | Egocentric property never tested on QA | R1-W6, DA-M5, R2-W4 | Table 2, Fig. 4, App. A.5.2 | Report Tables 4–5 for egocentric vs public images matched on domain / type | Low (existing outputs) | Yes |
| R4 | Label and judge validity | R1-W1, R1-W2, DA-M4, DA-M6 | §3.2, §4, Table 7, App. A.3–A.4, B.1 | Double-annotate 300–500 items (agreement, error rate); per-system human-vs-judge truthfulness difference with n; report removal rates of generated turns | Medium (≈ 2–3 annotator-days) | Partly |
| R5 | Privacy, consent, licence and limitations statement | R3-W1, DA-M7, all limitations | §3.1, §3.4, §6 | Datasheet-style statement: consent, de-identification, per-source licence, takedown, limitations (English, still images, mock corpora, judge profile) | Low | Yes |

### Priority 2: Strongly suggested (should fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Intervals and split sizes; slice-size claim | R1-W4, R1-ERR-2, R4-W3 | State split sizes and the two held-out domains; bootstrap 95% intervals; flag n < 100 | Low | Yes |
| S2 | Stale ground truth vs live-web systems | DA-M1 | Tag time-sensitive questions; re-verify on the evaluation date; report with and without | Medium | Partly |
| S3 | Related work and Table 1 | R2-W1, R4-W1 | Add related-work section; extend Table 1 with InfoSeek, Encyclopedic-VQA, Dyn-VQA, MRAG-Bench, MMSearch (links above); show the same models on one existing benchmark (RQ1) | Medium | Partly |
| S4 | Retrieval-world realism; recall estimation | R1-W5, R3-W3 | Describe how 89% recall was estimated; add a 10× distractor run | Medium | Partly |
| S5 | Template critique inconsistency; question provenance shares | R2-W2 | Report share of template / annotator / LLM questions; drop "uncommon in real life" without evidence | Low | Yes |
| S6 | Latency / tokens / cost | R3-W2 | Add per-question latency and tokens for Tables 4–5 | Low–Medium | Yes |

### Priority 3: Nice to fix (optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Multi-turn Truth ≠ Acc − Hallu; averaging unstated | R1-ERR-3, DA-m2 | State macro/micro averaging |
| N2 | Popularity distribution vs balanced buckets | R1-ERR-4 | Report distribution |
| N3 | Baseline thresholds / token budgets | R1 Minor | State selection split |
| N4 | "Task 1 marginal improvement" generalizes the best case | DA-m3 | Qualify (Table 8: Claude 3.7 Sonnet −9.3 → −29.5) |
| N5 | Cross-field suggestions (pooled relevance judgments, selective prediction, de-identification practice, Ego4D `[verify]`) | R3-W4 | Consider |
| N6 | Missing venues in references; model versions in Table 5 | R2 Minor, R4 Minor | Fix |

## Estimated Revision Effort
- Priority 1: 5 items, ≈ 1–2 weeks (annotation audit and rerun dominate; wording and privacy statement are hours)
- Priority 2: 6 items, ≈ 1 week
- Priority 3: 6 items, ≈ 1 day
- **Total estimated revision time**: ≈ 2–3 weeks; items R1, R3, R5, S1, S5 are feasible within a typical one-week ICLR discussion window with a revised PDF.

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
