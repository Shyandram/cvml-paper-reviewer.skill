# Academic Paper Review — full mode (simulation)

**Paper:** Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
**Date:** 2026-11-10 · **Request:** target venue ICLR, full review, skip confirmation, literature check strict (cutoff 2025-09-24)
**Execution note:** the five reviewer passes and the EIC pass were run one after another in a single model context (no subagents). They share one context and are not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only and are marked as such.

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking |
| Primary Discipline | ML → LLM text watermarking and provenance (statistical detection) |
| Secondary Discipline(s) | Statistical hypothesis testing / scan statistics; coding theory (pattern codes); security (spoofing) |
| Paper Type | Empirical (method + light theory + simulated evaluation); composite weights: empirical |
| Core Technique(s) | Logit-bias (green-list-style) watermarking with a fixed vocabulary partition and a deterministic cyclic tag pattern; sliding-window pattern-match statistics; Janson-inequality false-alarm bound |
| Target Venue | ICLR 2026 (stated); profile key `iclr` |
| Venue-Specific Notes | none; ICLR rating scale is `secondary` status (script prints {0,2,4,6,8,10} and the older scale) |
| Paper Maturity | Submission-ready draft, short evaluation |
| Ethics-Relevant Content | none (no human data). Dual-use is mild: the paper's own motivation is spoofing/misattribution; an LLM (Gemini-2.5-Flash) is prompted to write misinformation in Appendix B.2 |

### Claimed Contributions (as stated by the authors)
1. **C1:** A new task, "detecting post-generation edits locally made to watermarked LLM outputs", with two metrics (detection accuracy, Type-I/false-alarm rate) (Abstract; §1; Definitions 1–2).
2. **C2:** A general combinatorial pattern-based watermark: disjoint vocabulary subsets, a deterministic cyclic tag pattern (Examples 3.1 and 3.2) (§3.1).
3. **C3:** A global detection statistic and lightweight local edit statistics, with a false-alarm bound (Theorem 3.1) (§3.2–3.3, Appendix A).
4. **C4:** Empirical evidence of edit localization on simulated edits, and that the watermark "remains reliably detectable, comparable to state-of-the-art schemes" (§1, §4).

### Paper memory (factual record, shared with all reviewers)
- **Setup facts:** models LLaMA-2-7B and OPT-1.3b (Fig. 1 table; §4); prompts from WikiText (§4); "deterministic decoding with 4-beam search" (§4); 64-token texts, 2000 texts total (Fig. 1), "1,000 samples of 64 tokens" (§4.1); random edits of type replace/insert/delete, span 1–6 tokens (§4, Fig. 1); threshold calibrated to Type-I = 0.1 (§4); tolerance L = 3 (§4.1); δ = 5.8 (Fig. 4, Fig. 5); window w = 8 for the 8-tag-slot pattern, w = 2 elsewhere "including the baselines" (§4). Baselines: KGW [27], Unigram [41] "treating them as having a degenerate pattern" AA… (§4.1). Hardware RTX 6000Ada (§4). Not stated after search: green-list fraction γ for baselines and sizes of the vocabulary subsets; which texts the thresholds are calibrated on; seeds, repeats, intervals; code or data release; ethics/broader-impact statement; perplexity oracle model.
- **Headline numbers:** Type-I = 0.1 (§4); L = 3 (§4.1); δ = 5.8 (Fig. 5); Table 1 (Appendix B.2): 81.4% (59 texts), 90.9% (44), 91.7% (36) for AB at δ = 4.5 on OPT-2.7b, 139 texts, 100 tokens; human check: 90% of 50 sampled edits contained clear misinformation.
- **Appendix adds:** proofs and a miss-probability bound (A); worked pattern examples and design insights, other δ, multinomial sampling (temperature 1.0, top_p 0.8, 200 samples × 100 tokens, Fig. 7), score drop under edits (Fig. 8), a misinformation experiment (Table 1), a worst-case degradation bound (Eq. 6), complexity (C).
- **Unverifiable:** all figures (4–8) — only captions and surrounding text were read; Fig. 5 values and whether Fig. 6 contains baseline curves could not be checked.

### Integrity signals
`scripts/integrity_scan.py` found no text addressed to reviewers or AI systems and no hidden characters. No redaction was needed. (`injection_found`: none.)

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Marguerite Solvang-Adeyemi, statistics and learning-theory group, large public university (Northern Europe)
- **Seniority / Expertise**: senior faculty / statistical testing, privacy and security of ML systems
- **Role**: reads all five reviews, checks decisive points against the paper, weights reviewers, decides
- **Style**: wants the central claim measured by the experiment, tolerant of simple ideas

### Reviewer 1 (Methodology): Tomasz Weerasinghe, applied-statistics team, industrial research lab (North America)
- **Seniority / Expertise**: mid-career industry scientist / evaluation of LLM watermarks, false-alarm calibration, scan statistics
- **Review Focus**: design, statistics, comparison fairness, reproducibility
- **Style**: recomputes numbers, insists on matched operating points

### Reviewer 2 (Domain): Amara Veltman, security and NLP lab, public research university (South Asia)
- **Seniority / Expertise**: senior faculty / LLM watermarking, spoofing and stealing attacks, mixed-authorship detection
- **Review Focus**: literature, theoretical framework, domain contribution
- **Style**: checks every novelty sentence against the cited abstract

### Reviewer 3 (Perspective): Lucía Okonkwo-Brandt, information-theory and coding group, engineering school (Latin America)
- **Seniority / Expertise**: associate professor / synchronization and error-correcting codes, tamper-evident media
- **Review Focus**: cross-disciplinary connections, deployment, assumptions
- **Style**: constructive, looks for what the idea could become

### Reviewer 4 (Generalist): Kenji Almeida-Roth, NLP group, mid-size research university (East Asia)
- **Seniority / Expertise**: mid-career faculty / language generation and evaluation (not watermarking specifically)
- **Review Focus**: contribution clarity, venue fit, presentation
- **Style**: typical program-committee reader; weighs weaknesses against ICLR norms

### Devil's Advocate: Sana Petrovic-Hale, evaluation-methodology group, industrial lab (Western Europe)
- **Seniority / Expertise**: senior industry scientist / causal evaluation, adversarial robustness of detectors
- **Review Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous, asks "what would an adaptive adversary do?"

*Personas are fictional. Proceeding with stated assumptions.*

---

# Phase 1: Independent Reviews

(All reviewers read the reviewer copy, which here is identical to the manuscript text, and the paper memory above.)

---

# Peer Review Report

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Reviewer: Tomasz Weerasinghe, Reviewer 1 — Methodology (applied-statistics team, industrial lab; fictional persona)
## Expertise: LLM watermark evaluation; false-alarm calibration; scan statistics
## Date: 2026-11-10

## Summary
The paper proposes to watermark LLM output by forcing the token sequence to follow a fixed cyclic pattern of vocabulary subsets (e.g., alternating A/B halves). A sliding-window indicator counts pattern-consistent windows; the mean over all windows gives a global detector (Eq. 4) and the mean over the w windows covering a token gives a local edit score (Eq. 5). Positions with a low local score are flagged as edits. A Janson-inequality bound on the per-token false-alarm probability is given (Theorem 3.1). Experiments on simulated random edits (LLaMA-2-7B, OPT-1.3b) compare against KGW and Unigram.

## Strengths
### S1: The task is cleanly formalized and the metrics are explicit
Definitions 1 and 2 (§2.2) fix a tolerance L and define detection accuracy and a position-level Type-I rate. This makes results comparable in principle and the metric choice is honest about tolerance.
### S2: Simple, cheap statistic with an interpretable failure mode
The local score (Eq. 5) is O(Tw) with rolling hashes (Appendix C), and the authors state exactly which edits are invisible to the AB pattern (even-length aligned deletions, §4.1).
### S3: Limitations are partly disclosed
The conclusion admits weak performance on one- and two-token edits and a narrow pattern space (§5). The Appendix B.3 bound is honest that degradation grows with w.

## Weaknesses

### W1: The operating point makes the headline accuracy hard to interpret (E4/E5)
Thresholds are "calibrated to control the Type-I error rate (i.e., false alarm rate) at 0.1 across all experiments" (§4), and Definition 2 is a per-position rate. On a 64-token text that is on the order of six flagged positions per unedited text (0.1 × 64, derived; independence not assumed to be exact). Detection accuracy is reported only at this single point, with no ROC/precision–recall curve, no text-level false-alarm rate and no precision. Algorithm 3's decision ("Edit detected") uses a minimum over positions, so the text-level false-alarm rate is not controlled at 0.1. The paper does not state which texts the thresholds were calibrated on (not stated after search).
- **Suggested Fix:** report ROC or precision/recall over thresholds, a text-level false-alarm rate on unedited watermarked and on human-written text, and calibrate on a split disjoint from the evaluation texts. Cost: reruns of existing outputs, under 1 GPU-hour.

### W2: Baselines are ad-hoc adaptations, and compared settings are not matched (E4)
KGW and Unigram are "treated as having a degenerate pattern" AA… and use w = 2, as the paper does for its own AB pattern (§4: "w = 2 for all other cases including the baselines"). The green-list fraction γ, the number of window sizes tried for the baselines, and the subset sizes of the proposed partition are not stated after search. All methods are run at one δ = 5.8 (Fig. 5), yet §4.2 says the best edit-detecting pattern has "the weakest trade-off between detectability and text quality". Matching δ is therefore not matching quality: the comparison should be at matched perplexity or matched watermark Type-II error. No method designed for edit/segment localization is compared (e.g., the segmentation method in the literature addendum, HC [25], PALD [30], Tr-GoF [32]).
- **Suggested Fix:** report γ and subset sizes; sweep w for every method; compare at matched PPL (curves over δ); add at least one localization-capable baseline. Cost: ~10–20 GPU-hours on the existing models.

### W3: Evaluation covers only random token-level edits on short texts, one or two small models (E5)
Edits are "randomly selected contiguous spans" (§4) of at most six tokens, independent of text content, applied to 64-token continuations of WikiText prompts with 4-beam search. Real edits are semantic and often longer; edited strings must be re-tokenized, which §2.2 does not discuss. The only non-random experiment (Table 1, Appendix B.2) is 139 texts, one pattern (AB), one δ = 4.5, OPT-2.7b, with no baseline, no stated L, threshold or false-alarm rate. The abstract's "strong empirical performance" and §4.1's "Combinatorial patterns significantly outperform baseline KGW and Unigram" are supported only for the synthetic setting. Fig. 5 values could not be read; the wording "significantly" has no interval or test.
- **Suggested Fix:** add human-edited and LLM-paraphrased edits, longer texts (≥ 200 tokens), an instruction-tuned model, multinomial sampling in the main figure, and bootstrap intervals; narrow the wording if not done.

### W4: Theorem 3.1 does not cover the algorithm's decision, and its conditions are unchecked (E2/E3)
Theorem 3.1 bounds Pr[|s|E(t) < τe | no edit] "at token t". Algorithm 3 returns "Edit detected" if min over t of |s|E(t) < τe, which needs a bound over all T positions (a union bound or scan-statistic argument is absent). The proof applies Janson's inequality to the window indicators, which are functions of an LLM's dependent token draws; the appendix itself says the dependency structure is "intricate and difficult to characterize". It also assumes an identical alignment probability for every window (μ1^(w)). The bound is vacuous in the regime used (hard case μ1 = 1 gives zero by assumption; soft case depends on an intractable Δ(w)). The authors acknowledge that the miss-probability bound "may not be very informative" and "we rely primarily on the empirical results in Section 4".
- **Suggested Fix:** state Theorem 3.1 as a per-position heuristic or add the union bound; verify Janson's conditions or replace with an empirical calibration plus a test of the independence assumption.

### W5: Reproducibility is thin (E8)
No code/data release statement, seeds, repeats, intervals, or perplexity oracle model were found after search. The baseline settings (γ, key handling, hash context) are not given. Fig. 7 uses 200 samples per cell, Fig. 5 uses 1,000 samples shared over 18 edit conditions (about 56 per cell on average, derived from Fig. 1's uniform design; ambiguous), i.e., a binomial 95% interval of about ±13 points at 50% accuracy (derived).
- **Suggested Fix:** release code and generated texts, state all parameters, report cell counts and Wilson/bootstrap intervals.

**Minor:** Algorithm 3 line 2 index range ("t−w+1" presumably T−w+1); Appendix A.1 bound on Δ(T,w) counts neighbours on one side only (see Error Log); Fig. 7 axes appear to stop at edit length 5 while §4 states 1–6 (may be an extraction artifact).

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2/E5 | Thm 3.1 vs Algorithm 3 | "Type-I error rate at token t under a clean (unedited) watermark is bounded by" | Bound is per token; Algorithm 3 decides on a minimum over t, so no guarantee for the text-level decision | Cross-referenced Theorem 3.1 statement with Algorithm 3 line 2 | High | MAJOR | Add union bound or restate |
| ERR-2 | E5 | §1 vs §4.2 | "remains reliably detectable, comparable to state-of-the-art schemes" | §4.2 reports no baseline curve in text and states the long pattern "exhibits the weakest trade-off between detectability and text quality"; baselines are only KGW and Unigram | Cross-referenced §1 and §4.2 text; Fig. 6 not readable | Medium | MAJOR | Add baseline curves at matched PPL; narrow wording |
| ERR-3 | E2 | Appendix A, proof of Thm A.1 | "(T−w+1)µ1 + (T−w+1)(w−1)µ1" | If Δ is a sum over ordered pairs as in Theorem 3.1 (factor 2 on cross terms), the count of neighbours should be 2(w−1), not (w−1); constant off by up to ~2 | Recomputed pair count; depends on the convention of Δ | Medium | MINOR | Fix constant |

### Claim-to-Evidence Map (key claims)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | New task | Abstract, §1 | §2.2 definitions; literature check shows a close prior (segmentation of watermarked text) | Partially (task is new in form, not in kind) |
| C2 | Pattern watermark enables localization | §3.1, §4.1 | Fig. 5 (unreadable), Fig. 4 examples | Partially: synthetic random edits only |
| C3 | Type-I guarantee | §3.3, Thm 3.1 | Appendix A | Partially: per-token, assumptions unchecked |
| C4a | Edit localization strong, beats KGW/Unigram | Abstract, §4.1 | Fig. 5, baselines adapted | Partially |
| C4b | Detectability comparable to SOTA | §1 | Fig. 6 (no baselines in text), Fig. 8 | Unsupported as worded |

## Missing References
(Domain Reviewer's responsibility; none added here.)

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation does not test the claim beyond random edits; bound does not cover the decision |
| Clarity | 3 | Clear, short, a few notation slips |
| Significance | 2 | Useful problem, but impact depends on unshown real-edit performance |
| Originality | 2 | New framing; method is a fixed-partition green-list variant |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: single synthetic evaluation with ad-hoc baselines at an unmatched operating point; central comparison cannot be interpreted.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Theorem not matched to the algorithm; assumptions unchecked |
| Clarity & Presentation | 66 | Competent | Easy to follow |
| Novelty & Originality | 52 | Developing | Fixed-partition pattern watermark; new framing |
| Significance & Impact | 48 | Developing | Only synthetic edits |
| Experimental Validation | 38 | Developing | One regime, weak baselines, no intervals |
| Reproducibility | 46 | Developing | No code/params/seeds |
| Ethical Compliance | 62 | Competent | Limitations partly discussed |

## Questions for Authors
1. On which texts are thresholds calibrated, and what are the text-level false-alarm rate and precision at the reported operating point? (Would raise my score if low.)
2. What are γ and the vocabulary subset sizes, and how do results change when all methods are compared at equal perplexity?
3. How does accuracy change with human-written or paraphrase edits and with 200+ tokens?

## Limitations Assessment
**Partially.** Narrow edit model, adaptive attackers and re-tokenization are not covered.

## Ethics Review Flag
**No.**

## Overall Score
**2 (Reject)**: the paper's central claim is not measured at an interpretable operating point, and the theory does not cover the algorithm; the idea is worth a stronger evaluation.

## Confidence
**4**: confident; figures unreadable.

---

# Peer Review Report

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Reviewer: Amara Veltman, Reviewer 2 — Domain (security and NLP lab, public university; fictional persona)
## Expertise: LLM watermarking; spoofing/stealing; mixed-authorship detection
## Date: 2026-11-10

## Summary
The paper recasts "was this watermarked text edited, and where" as a task and answers with a watermark whose token class sequence is a fixed cycle. Pattern violations in a sliding window mark edits. It positions itself against KGW/Unigram-style schemes, an order-agnostic pattern watermark [9], and watermark-agnostic or segment-based detectors [25, 30].

## Strengths
### S1: A well-motivated gap
The intro ties watermark spoofing to the lack of local visibility into edits (§1, citing [35]); localization is a sensible complement to global detection.
### S2: The relationship to [9] is described accurately
§1.1 says the AB pattern is a special case of the Markov-chain pattern mark of [9] and differs by deterministic transitions and repeated tags. This matches the abstract of [9] (a Markov-chain-based, pattern-based watermark for order-agnostic LMs).
### S3: Simple methods are easy to build on
The window indicator formalism (Eq. 3–5) and the design insight about even/odd alternation (Appendix B.1) are reusable.

## Weaknesses

### W1: The novelty statement "no existing method" is overstated (E5/E7, MAJOR)
§1.1 states: "no existing method addresses the challenge of determining whether a watermarked LLM output has been post-edited" and where. The literature check found *Segmenting Watermarked Texts From Language Models* (NeurIPS 2024; arXiv 2410.20670, verified). Its abstract says the user "can modify the generated text by substitutions, insertions, or deletions", and the method segments "the published text into watermarked and non-watermarked sub-strings" with Type I/II error control via change-point detection. It is not identical (it targets longer non-watermarked substrings, uses ordinary watermark scores, and does not design the watermark for localization), but it is the same task family and is uncited. Claim C1 gets a novelty verdict of *incremental* (level 4 against that work). The paper cites [30] (PALD) and [25] (HC) but dismisses [25] as having power that "may converge slowly in practice" without evidence.
- **Suggested Fix:** cite and differentiate; compare empirically against a change-point or segmentation baseline; soften "no existing method".

### W2: A cited work is mischaracterized, and it is the closest baseline for edited watermarked text (E7, MAJOR)
Reference [32] (Li et al.) is placed in "Most existing detectors are calibrated to flag long content, such as AI-generated content detection [5, 7, 16, 32, 34, 37]". The kept abstract for [32] describes a truncated goodness-of-fit test for "detecting watermarked text under human edits", a watermark-based detector, not a zero-shot AIGC detector. It is never compared. Relatedly, reference [19] is listed as "Sam Hopkins and Ankur Moitra, Edit-distance robust watermarks for language models, ICML 2024"; the arXiv work I can verify with the closest title ("Edit Distance Robust Watermarks via Indexing Pseudorandom Codes") is by Golowich and Moitra, NeurIPS 2024. I cannot tell whether these are the same work, so I raise it as a question.
- **Suggested Fix:** move [32] to the watermark-under-edits group, discuss it, and check the [19] entry.

### W3: The pattern idea overlaps with [9]; the claimed generality is not explored (Novelty, MINOR–MAJOR)
Per the claim-level profile, C2 is *medium* (top prior [9], level 3, cited). The "general framework" is demonstrated with two patterns (and a third in Appendix B.2), with ≤ 4 tags (§5). The fixed, context-independent partition (Algorithm 1 takes the partition as input) is the Unigram-style design [41]; its known vulnerability to learning-based stealing is not discussed, although the intro motivates the work by spoofing.
- **Suggested Fix:** discuss stealing attacks that learn green lists, and evaluate an informed adversary who preserves the pattern.

### W4: Baselines omit the closest watermark designs for edited text (Experiments in domain terms)
Only KGW and Unigram are compared. Edit-robust designs such as indexing pseudorandom codes (verified title, below) address insertions/deletions directly; they are not localization methods, but they define what "robust to edits" means for the field.
- **Suggested Fix:** position against them in related work; run at least one localization-capable comparator.

## Missing References
*Follow the citation-integrity rule. "verify" = checked with `related_search.py verify` under strict mode.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Xingchi Li, Guanxun Li, Xianyang Zhang. *Segmenting Watermarked Texts From Language Models.* NeurIPS 2024 (arXiv 2410.20670, 2024-10-28; verified, prior peer-reviewed) | Same family of task: segment watermarked vs. non-watermarked parts of edited text with error control; closest prior to C1 |
| Important | Noah Golowich, Ankur Moitra. *Edit Distance Robust Watermarks via Indexing Pseudorandom Codes.* NeurIPS 2024 (arXiv 2406.02633, 2024-06-04; verified, prior peer-reviewed) | Provable robustness to insertions/deletions; may be the work behind [19] |
| Important | Line of work: watermark stealing attacks that learn green-list statistics from API outputs, e.g. *Large Language Model Watermark Stealing With Mixed Integer Programming* (arXiv 2405.19677, 2024-05-30; title verified, authors not recalled [verify]) | A fixed partition is the easiest to steal; relevant to the spoofing motivation |
| Helpful | Xuanyu Zhang et al. *EditGuard: Versatile Image Watermarking for Tamper Localization and Copyright Protection* (arXiv 2312.08883, 2023-12-12; verified) | Same idea in images: watermark designed for tamper localization |

### Literature-check addendum
*Mode: strict, cutoff 2025-09-24. 8 queries (claim 7, baseline 1), all concept-only; coverage gap "no baseline query" closed (the paper reports on no external benchmark: edits are simulated, WikiText only supplies prompts). `similarity`: no high conceptual overlap (max cosine 0.21) and no text overlap (0 shared 8-grams). Closest prior works: Robust Detection of Watermarks for LLMs Under Human Edits (cited as [32]); Large Language Model Watermark Stealing With Mixed Integer Programming; Duwak (dual watermarks). Search covers arXiv only.*

**Per-claim novelty (claim profile, `related_search.py novelty`):**
| Claim | Dimension | Novelty | Top prior (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|-----------------------------------------|-----------|
| C1 new task | problem | incremental | Segmenting Watermarked Texts From Language Models (4, arxiv.org/abs/2410.20670, prior peer-reviewed, not cited) | Detects and segments edited text under substitutions/insertions/deletions with error control |
| C2 pattern watermark | method | medium | A Watermark for Order-Agnostic Language Models (3, arxiv.org/abs/2410.13805, prior arXiv-only, cited as [9]) | Pattern-mark is Markov-chain based for order-agnostic LMs; deterministic cyclic pattern for left-to-right LMs is the delta |
| C3 statistics + bound | method | medium | Segmenting Watermarked Texts (3, same link, not cited) | Different statistic family (change point) |

Paper-level novelty 0.44; attribution: Segmenting Watermarked Texts From Language Models. One established-level claim at most (C1 level 4, not 5): a claim-level finding, MAJOR at most. No criterion-7 candidate (not every central claim is covered by the same uncited work).

**Novelty delta table:**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited/differentiated? |
|---|---|---|---|---|
| Local edit detection in watermarked text | Segmenting Watermarked Texts | Segments edited text into watermarked/non-watermarked parts, error control | Watermark designed for localization at token level, short edits | No |
| Pattern-based watermark | Pattern-mark [9] | Markov-chain pattern watermark for order-agnostic LMs | Deterministic cyclic pattern, left-to-right LMs, localization statistic | Yes ([9], differentiated) |
| Watermark under edits | Tr-GoF [32] | Robust watermark detection under human edits | Localization, not only global detection | Cited but mischaracterized |

**Baseline scout:** no external benchmark; the table is empty. Baselines present: KGW [27], Unigram [41]. Prior localization-capable methods not compared: segmentation method above (prior, peer-reviewed), [25], [30], [32].

**Field snapshot.** Three to four years ago LLM watermarking meant green-list logit bias (KGW) with a z-test over long text; since then the field split into distortion-free sampling schemes, undetectable and edit-robust constructions (with provable guarantees for insertions/deletions), and attack papers on spoofing, stealing and paraphrase removal. Current work targets robustness under human edits and mixed-authorship texts, and attribution of text parts. Open problems stated by recent work: detection under heavy edits on short text, security against learned attacks, and quality-preserving watermarks at low entropy. A significant contribution now is a method that localizes edits or mixed authorship on realistic edits with calibrated error, or one with provable guarantees on a realistic edit model; a gain on random token edits at δ ≈ 5 against adapted baselines would be incremental. This snapshot was used to score Significance and Novelty.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Experiments narrower than the claims; theory loose |
| Clarity | 3 | Clear and short |
| Significance | 2 | Depends on real edits |
| Originality | 2 | New framing, partly covered by unreferenced prior work |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a reasonable idea and a real gap, but novelty positioning misses a directly relevant NeurIPS 2024 paper and the empirical case is thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound construction; theory loose |
| Clarity & Presentation | 68 | Competent | Well organized |
| Novelty & Originality | 54 | Developing | Incremental per claim profile |
| Significance & Impact | 54 | Developing | Real problem; evidence narrow |
| Experimental Validation | 44 | Developing | Weak, adapted baselines |
| Reproducibility | 52 | Developing | Parameters missing |
| Ethical Compliance | 62 | Competent | Little at stake; limitations stated |

## Questions for Authors
1. How does the method differ in practice from segmentation by change-point detection on KGW/Unigram scores? A head-to-head result would raise my score.
2. Is [19] the Golowich–Moitra paper, and why is [32] listed among AIGC detectors?
3. What happens if an attacker who has learned the A/B partition edits in a pattern-preserving way?

## Limitations Assessment
**Partially.** No discussion of stealing/learned-partition attacks.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a sensible, simple idea whose novelty claim and comparisons do not account for close prior work.

## Confidence
**4**

---

# Peer Review Report

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Reviewer: Lucía Okonkwo-Brandt, Reviewer 3 — Perspective (information theory and coding group; fictional persona)
## Expertise: synchronization and error-correcting codes; tamper-evident media
## Date: 2026-11-10

## Summary
The paper embeds a periodic structure in token classes so that any local break of the structure is evidence of editing. In my terms it is a fixed, tiny "pattern code" with a sliding-window syndrome check: an interesting and pragmatic use of redundancy for tamper localization rather than for message transmission.

## Strengths
### S1: A useful lens: from detection to forensics
Moving from "is this machine text" to "which part was changed" matches needs in academic writing, journalism and logging (§1). The Figure 2 illustration communicates the idea in one glance (caption read; figure not visible).
### S2: Natural connection to coding theory
The design insight in Appendix B.1 (even/odd alternation lets a w = 2 test work) is a parity-style check. A deterministic cyclic pattern is a repetition code whose "syndrome" is the window score, and deletions that are multiples of the period are exactly the undetectable errors of such codes, as §4.1 observes for AB.
### S3: The trade-off is shown, not hidden
§4.2 and Appendix B.3 show that more tags lower quality and that longer windows lose more watermark signal under edits.

## Weaknesses

### W1: Aligned edits are structurally invisible, which an adversary can exploit
For AB, "removals of length two, four, and six" are hard to detect (§4.1); for the 8-slot pattern, deletions of multiples of the period are equally invisible by construction. A malicious editor who infers the partition can use pattern-preserving edits. Since the motivation is spoofing and misinformation (§1), the main threat model is exactly where a deterministic fixed pattern is weakest, and the paper does not test it.
- **Suggested Fix:** add a randomized or key-dependent phase/pattern (a keyed pseudo-random sequence of tags) so period-aligned edits are not systematically invisible, and evaluate an informed attacker.

### W2: Detection-quality-robustness triangle is only partly explored
Appendix B.3 shows that the worst-case loss in detection score grows with w, and Fig. 8 text says "larger decreases observed for longer edit lengths and more complex patterns". The pattern that localizes best is thus the least robust for global detection of edited text, and costs the most quality (§4.2). A coding-theory view suggests synchronization markers or interleaved check symbols with a tunable rate.
- **Suggested Fix:** present the three-way trade-off explicitly (curves of localization accuracy vs. PPL vs. post-edit detection), and discuss rate-distortion style limits.

### W3: Deployment assumptions
The method needs the identical tokenization between generation and detection; user edits arrive as strings that are re-tokenized, a point absent from §2.2. It also assumes the generator controls decoding (a provider-side watermark) and that texts are ≥ 64 tokens. Behaviour on low-entropy spans (names, numbers, code) where the LLM cannot follow the pattern would produce false flags that cluster rather than spread uniformly; Type-I is calibrated as an average (§4).
- **Suggested Fix:** report false flags by token entropy; test re-tokenized human edits.

### W4: Safety of the misinformation experiment
Appendix B.2 prompts Gemini-2.5-Flash to produce clear misinformation (human check: "90%"). The content is benign in scale (short edits), but a statement on handling of the generated text would be appropriate.

## Missing References
(Optional; see Domain Reviewer.) Connections to name rather than cite: insertion/deletion-channel codes and synchronization codes; fragile and semi-fragile watermarking for tamper localization in images/audio (one verified example in the Domain report); scan statistics and CUSUM change-point tests for the sliding-window decision.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound construction; evaluation limited |
| Clarity | 3 | Clear |
| Significance | 3 | Forensics direction is valuable |
| Originality | 3 | Fresh application of an old idea |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean, new-problem paper with a plausible path to impact; held back by a synthetic evaluation (this is a first paper on a new task, so baseline coverage is judged leniently).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Sound; bound loose |
| Clarity & Presentation | 72 | Competent | Concise |
| Novelty & Originality | 68 | Competent | New framing and use of structure |
| Significance & Impact | 70 | Competent | Integrity and forensic uses |
| Experimental Validation | 54 | Developing | Synthetic only |
| Reproducibility | 60 | Competent | Algorithms given; parameters partly missing |
| Ethical Compliance | 68 | Competent | Limitations honest; no impact statement |

## Questions for Authors
1. Would a keyed pseudo-random tag sequence keep the localization benefit while removing period-aligned blind spots?
2. How does accuracy depend on token entropy and on re-tokenization after human editing?
3. Can you estimate an operational false-flag count per page at the reported thresholds?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: a promising framing and a clean mechanism for a new task; evidence is preliminary but the direction is worth publishing if the evaluation is strengthened.

## Confidence
**3**

---

# Peer Review Report

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Reviewer: Kenji Almeida-Roth, Reviewer 4 — Generalist (NLP group, mid-size university; fictional persona)
## Expertise: language generation and evaluation
## Date: 2026-11-10

## Summary
The contribution in my words: a text watermark that makes token classes follow a repeating pattern, so that a simple window test can say both "this text is watermarked" and "these spots were changed afterwards". It is evaluated on simulated edits to texts from two open LLMs, against two common watermarks.

## Strengths
### S1: Clear one-paragraph contribution and a readable paper
The intro, Figure 2 (caption) and Examples 3.1–3.2 make the idea understandable to a non-specialist in about two pages.
### S2: Fits ICLR's interest in LLM safety and provenance
A new task and a method, with some theory and an appendix with additional settings.
### S3: Honest limitation paragraph
§5 admits weak performance for one- and two-token edits, a narrow pattern space and a "lightweight" detector.

## Weaknesses

### W1: The evidence is thin for a conference paper's main claim
Main results are two figures (Fig. 5 and Fig. 6) plus the appendix; the paper itself says the theory is "not very informative" and relies on experiments (Appendix A). The statement "Combinatorial patterns significantly outperform baseline KGW and Unigram" (§4.1) comes without intervals, with baselines adapted by the authors, and with the best pattern having "the weakest trade-off" in quality (§4.2). Typical accepted ICLR papers on a new task show a realistic dataset or a human-edit study; Table 1 is a start but is placed in the appendix and has no comparison.
- **Suggested Fix:** move a realistic-edit experiment with baselines into the main text.

### W2: Venue criteria (Soundness / Presentation / Contribution)
| Criterion | Status | Location |
|---|---|---|
| Claims supported by evidence | partly | §4.1 supports synthetic edits only |
| Soundness of theory | partly | Thm 3.1 per-token; Appendix A caveats |
| Presentation | met | §§1–3 |
| Contribution is significant for ICLR audience | partly | new task; narrow evidence |
| Reproducibility statement | not met | none found after search |

### W3: Related work is brief and positioning is by exclusion
"To the best of our knowledge, no existing method addresses" (§1.1) is a strong sentence for a one-page related-work section; the domain reviewer's findings apply. I note it because a generalist reader would take the sentence at face value.
- **Suggested Fix:** a short table of closest methods and what each can and cannot do.

**Minor:** typos in Algorithm 3 range; several figures present examples whose selection is not described (Fig. 4: "Four examples").

## Missing References
(See Domain Reviewer.)

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation narrow |
| Clarity | 3 | Clear |
| Significance | 2 | Plausible but unproven impact |
| Originality | 3 | New task framing |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea on a new task, but the empirical support is lighter than for typical accepted papers; I put it on the rejected side and say why: the main comparison cannot be trusted as stated.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound but limited |
| Clarity & Presentation | 66 | Competent | Clear |
| Novelty & Originality | 58 | Competent | Incremental but new framing |
| Significance & Impact | 58 | Competent | Moderate |
| Experimental Validation | 46 | Developing | Limited |
| Reproducibility | 54 | Developing | Missing parameters |
| Ethical Compliance | 64 | Competent | Adequate |

## Questions for Authors
1. Can the realistic-edit experiment (Table 1) be repeated with KGW/Unigram and a segmentation baseline?
2. What do the failure cases look like (false flags on unedited text)?
3. Will code and generated data be released?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: clear, new-task paper; the empirical case does not yet match the claims.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Reviewer: Sana Petrovic-Hale (evaluation-methodology group, industrial lab; fictional persona)

## Steelman
For a provider who watermarks its own output, structure in the watermark is free redundancy: a periodic pattern costs nothing at generation, gives a global detector and a local scan, and exposes localized tampering at a controlled false-alarm rate. A first paper that defines the task, supplies a simple solution and shows high accuracy for ≥ 3-token edits has value.

## Core Argument Chain
1. A deterministic cyclic tag pattern makes edits show up as pattern violations (§3.1, Fig. 2).
2. A sliding-window average localizes violations (Eq. 5, Alg. 3).
3. At fixed Type-I = 0.1 the method detects random edits more accurately than KGW/Unigram (§4.1, Fig. 5).
4. The watermark stays detectable "comparable to state-of-the-art schemes" (§1, §4.2).
∴ The scheme is a practical way to detect and localize post-generation edits.

## Strongest Counter-Argument
The evaluation measures something different from the claim. "Post-generation edits" in the motivation are human revisions and spoofing attacks (§1), where an adversary chooses edits to change meaning while preserving the watermark. The experiments instead inject edits of ≤ 6 tokens chosen at random "in randomly selected contiguous spans" (§4), independent of content and of the watermark partition. Under such edits, a replacement token breaks an AB pattern with probability about one half by chance, and a region of random tokens is easy to flag; the more the edit looks like fluent, meaning-changing text written without knowledge of the partition, the more it behaves like those random tokens, but nothing tests an informed adversary. A fixed, context-independent partition (Algorithm 1) is also the design most easily learned from a few hundred samples, after which a pattern-preserving edit (or any edit whose length is a multiple of the period) is invisible by construction (§4.1 concedes this for AB).

The comparison itself is stacked in a second way. The baselines, KGW and Unigram, were not designed for localization; they are re-purposed as "AA…" patterns with a two-token window, at δ = 5.8 for everyone (Fig. 5), which is a strong watermark whose perplexity cost the paper shows only for its own patterns (Fig. 6; baseline curves could not be checked) and which it says is worst for the best-localizing pattern (§4.2). Per-position false-alarm 0.1 on 64-token texts implies several false flags per clean text, so the 80–90% accuracies in Table 1 are not interpretable without precision. Finally, the one realistic experiment (Table 1) has no baseline, no stated threshold or L, and 139 texts. The data support a weaker claim: "on random short edits at high watermark strength, the AB/ACADBCBD pattern localizes better than adapted KGW/Unigram at a per-token false-alarm rate of 0.1." The paper's title and abstract claim much more.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The evidence supports a narrower claim (random edits, strong watermark, adapted baselines) rather than contradicting the main claim; no test-set selection, fabrication or ethics violation was found, and the experiment can test the narrowed claim.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Scope/Evidence | §4, Fig. 5, Table 1 | Random-edit simulation and no informed-adversary test, while motivation is spoofing and human revision | Add adversarial and human edits; evaluate pattern-preserving edits |
| DA-M2 | Evidence | §4.1, Fig. 5 | Adapted baselines, same δ, w = 2 for baselines; no matched-PPL comparison; no localization baseline | Matched-quality comparison and one segmentation baseline |
| DA-M3 | Logic | §4, Def. 2, Alg. 3 | Per-position FPR 0.1 and single operating point; no precision/ROC; text-level FP unspecified | ROC/PR and text-level false-alarm rate |
| DA-M4 | Overclaiming (E5) | §1 "comparable to state-of-the-art schemes"; §4.2 | Detectability claim not backed by baseline curves in the text; own text reports the longest pattern as weakest trade-off | Narrow or add evidence |
| DA-M5 | Novelty/E5 | §1.1 "no existing method addresses…" | Uncited peer-reviewed segmentation work with the same task family (addendum) | Cite, differentiate, compare |
| DA-M6 | Theory (E2/E5) | Thm 3.1 vs Alg. 3 | Per-token bound presented as the Type-I guarantee of a min-over-positions decision | Union bound or restate |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Reporting | Fig. 5 | Cell sizes about 56 on average (derived); no intervals for "significantly" |
| DA-m2 | Reporting | Table 1 | Decoding, L, threshold not stated for this experiment |
| DA-m3 | Reporting | Fig. 4 | Selection of four examples not described |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Table 1 counts sum to the number of generated texts | 59 + 44 + 36 vs "139 texts" (Appendix B.2) | 139 | Yes |
| Table 1 percentages are integer fractions | 81.4%, 90.9%, 91.7% | 48/59 = 81.36%, 40/44 = 90.91%, 33/36 = 91.67% | Yes |
| Texts per Fig. 5 cell | 2000 texts (Fig. 1), 18 conditions (3 types × 6 lengths) | ≈ 111 per condition over both models, ≈ 56 per model (derived; design ambiguity) | Interval about ±13 points |
| Expected false flags per clean 64-token text at 0.1 | Type-I 0.1 (§4) | ≈ 6 | Derived, see W1 of R1 |
| Worst-case guarantee of Eq. 6 for w = 8, six edited tokens | N = T − w + 1 = 57 (T = 64) | w·S = 48 of 57 windows may be lost | Bound vacuous at w = 8 |

## Ignored Alternative Explanations
- Better accuracy of the pattern watermark may come from per-token adherence (partition and δ), not from the pattern: baselines with a matched effective adherence and a tuned w might close the gap.
- The Table 1 accuracy for 1-token edits (81.4%) is far above the authors' own admission of weakness for 1-token edits (§5): the edit distribution (LLM-written, often changing neighbouring tokens after re-tokenization) may differ from the random simulation.

## Missing Stakeholder Perspectives
Providers who need low false flags on human-written or heavily legitimate edited text (e.g., students using grammar tools), and users whose legitimately edited text would be flagged at a 10% per-token rate.

## Observations (Non-Defects)
The paper states which edit types its own pattern cannot see (§4.1), openly lists limitations (§5), and reports a quality trade-off for its own patterns rather than hiding it (§4.2). Table 1 arithmetic is consistent.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Theorem does not cover decision; operating point unclear |
| Clarity & Presentation | 64 | Readable; several reporting gaps |
| Novelty & Originality | 48 | Incremental claims; close uncited prior |
| Significance & Impact | 48 | Depends on an unshown regime |
| Experimental Validation | 36 | Adapted baselines, synthetic edits, no intervals |
| Reproducibility | 48 | Parameters absent |
| Ethical Compliance | 60 | Little at stake |

**Pool position:** better than about 40% of submissions to ICLR. **Overall: 2 | Confidence: 4**

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (operating point) | kept | Specific; paper does not answer it (searched "calibrat", "validation") |
| R1 | W2 (baselines) | kept | γ and subset sizes not stated after search |
| R1 | W3 (random edits, small scale) | kept | Table 1 exists but lacks baselines; wording notes that |
| R1 | W4 (theorem) | kept | Matches Alg. 3 and Thm 3.1 text |
| R1 | W5 (reproducibility) | rewritten | Cell-size inference marked as derived and ambiguous |
| R1 | "Appendix A.1 constant" | moved to Minor/Error Log (Medium confidence) | Convention-dependent |
| R2 | W1 (novelty "no existing method") | kept | Matches the kept abstract; wording "same task family", not "known" |
| R2 | W2 ([32], [19]) | rewritten | [19] turned into a question; [32] kept (verified against abstract) |
| R2 | W3 | kept (Minor–Major) | Claim profile medium |
| R2 | W4 | moved to Minor | Overlaps R1-W2 |
| R3 | W1–W4 | kept; W4 moved to Minor | Concern is mild |
| R4 | W1–W3 | kept | W2 is a criteria table, W3 overlaps R2-W1 |
| DA | DA-M1…M6, DA-m1…m3 | kept | All have locations and fixes; DA-M2 and DA-M3 duplicate R1-W1/W2 (merged in Phase 2) |

No scores were changed. No weakness was found already answered in the paper.

# Phase 2, Part A: Synthesizer Package

**Issue list (merged) and classes**
| # | Issue | Sources | Class | May decide outcome? |
|---|-------|---------|-------|---------------------|
| I1 | Evaluation limited to random short edits; no informed adversary or realistic edits (only Table 1) | R1-W3, R4-W1, R3-W1, DA-M1 | CONSENSUS-4 | Yes |
| I2 | Baselines adapted, unmatched δ/quality, no localization baseline | R1-W2, R2-W4, DA-M2, R4-W1 | CONSENSUS-4 | Yes |
| I3 | Single operating point; per-position FPR 0.1; no ROC/precision | R1-W1, DA-M3, R3-W3 (entropy clustering) | CONSENSUS-3 | Yes |
| I4 | Novelty: "no existing method" vs uncited segmentation work; [32] mischaracterized | R2-W1, R2-W2, R4-W3, DA-M5 | CONSENSUS-3 | Yes |
| I5 | Detectability "comparable to state-of-the-art" unsupported; trade-off | R1-ERR-2, DA-M4, R3-W2 | CONSENSUS-3 | Medium |
| I6 | Theorem per-token vs min-decision; assumptions | R1-W4, DA-M6 | CONSENSUS-2 | Medium |
| I7 | Reproducibility/code/parameters | R1-W5, R4 criteria table | CONSENSUS-2 | No |
| I8 | Pattern invisible edits, fixed partition vs stealing | R3-W1, R2-W3, DA-M1 | CONSENSUS-3 | Medium |
| I9 | [19] reference entry mismatch (question) | R2-W2 | SOLO | No |

**SPLIT:** significance and overall: R3 (4) vs R1/DA (2). **DA-CRITICAL:** none.

**Official score (before EIC weights):** run with `scores_before.json`: ratings R1 2, R2 3, R3 4, R4 3, DA 2 → mean 2.80; official composite 54.6; before-composite 54.6; band 3; no warnings; spread flag on Significance (22).

---

# Phase 2, Part B: EIC Meta-Review

# Editorial Decision

## Paper: Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking
## Date: 2026-11-10
## Target Venue: ICLR 2026 | Paper Type: empirical
## Review Team (fictional personas): EIC Marguerite Solvang-Adeyemi; R1 Tomasz Weerasinghe (Methodology), R2 Amara Veltman (Domain), R3 Lucía Okonkwo-Brandt (Perspective), R4 Kenji Almeida-Roth (Generalist), DA Sana Petrovic-Hale

## Decision: Borderline Reject (3) — ICLR rating "4 on {0,2,4,6,8,10}" (venue's own label; scale status secondary; older scale "5 on {1,3,5,6,8,10}")

**Official ratings** (shown to authors): R1 2, R2 3, R3 4, R4 3, DA 2 → mean 2.80 · official composite 54.6
**EIC assessment** (internal): weighted rating 2.73 → starting point 3 · weighted composite 54.0 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
*This is a simulation of how a careful panel would likely see this draft, not a prediction.*

### The Case For and Against
- **For acceptance:** a new, well-motivated task with a simple, nearly free mechanism, clear writing, a Type-I bound (even if loose), honest limitations, and evidence that localization works for ≥ 3-token random edits; a first paper on a new task is judged with some leniency on baseline coverage.
- **Against acceptance:** the evidence measures random token edits at strong watermark strength against adapted baselines at a single per-token operating point; the novelty statement misses directly relevant peer-reviewed work; the detectability claim is not supported as worded; the threat model (spoofing) is not tested.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Random, content-independent edits; "Random edits are injected in randomly selected contiguous spans" | R1-W3, DA-M1 | §4 | Verified | Table 1 is the only non-random test |
| Baselines adapted as degenerate AA pattern, w = 2 "including the baselines"; γ not stated | R1-W2, DA-M2 | §4, §4.1 | Verified | Text search for γ/gamma found nothing |
| Thresholds calibrated at Type-I 0.1, per-position (Def. 2); no calibration split stated | R1-W1, DA-M3 | §4, Def. 2 | Verified | "≈ 6 flagged positions per clean 64-token text" is a derived estimate that assumes the stated per-position meaning |
| Theorem 3.1 is per token; Alg. 3 uses a minimum over t | R1-W4/ERR-1, DA-M6 | Thm 3.1, Alg. 3 | Verified | Appendix concedes the bound is loose |
| "no existing method addresses…" contradicted by segmentation work | R2-W1, DA-M5 | §1.1 | Partly correct | Same task family; the prior work targets longer non-watermarked segments, so "known" is too strong; Overstated claim in the paper, MAJOR |
| [32] mischaracterized as an AIGC detector | R2-W2 | §1.1 | Verified (against kept abstract) | |
| [19] authors/venue mismatch | R2-W2 | References | Not verifiable | Treated as a question |
| "comparable to state-of-the-art schemes" unsupported | R1-ERR-2, DA-M4 | §1, §4.2 | Partly correct | §4.2 text lacks baselines; Fig. 6 and Fig. 8 unreadable; Fig. 8 (appendix) does compare score drops with KGW/Unigram. Claim concerns detectability vs quality, which Fig. 8 does not address |
| Table 1 arithmetic | DA | App. B.2 | Verified | 59+44+36 = 139; percentages equal fractions |
| Appendix A.1 pair-count constant (ERR-3) | R1 | App. A | Partly correct | Convention-dependent; minor |
| Per-cell sample size ≈ 56 | R1-W5, DA-m1 | Fig. 1, §4.1 | Partly correct | Design ambiguous: may be per condition |
| R3: "Detection–quality–robustness triangle", pattern-aligned deletions invisible | R3-W1/W2 | §4.1, §4.2, App. B.3 | Verified | |
| R4 criteria table | R4 | various | Verified | |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Operating-point, baseline and theorem points all verified; ERR-3 medium-confidence minor; slightly harsh on Overall 2 given composite 50 |
| R2 (Domain) | 3 | 4 | 1.25 | Central novelty point verified against the abstract and stated at the right strength (same family, not "known"); [19] raised as a question rather than an accusation |
| R3 (Persp.) | 4 | 3 | 1.0 | Sound points, constructive; accepts the detectability claim largely at face value; default weight |
| R4 (Gen.) | 3 | 4 | 1.0 | Typical, calibrated review; no verification problems |
| DA | 2 | 4 | 1.0 | Counter-argument verified; no CRITICAL raised (correctly); several items duplicate R1; its "informed adversary" point is an extrapolation not tested by the paper, so the weight stays at the default |

### DA-CRITICAL Rulings
No CRITICAL issue was raised ("No CRITICAL issues found."). I checked the candidates: evaluation leakage (criterion 3): thresholds are calibrated on false-alarm rate, not selected for accuracy on edited test text, and no selection statement was found; known results (criterion 7): not every central claim is covered by the same uncited work (C2 is medium); claim contradicted (criterion 1): the evidence supports a narrower claim. The ceiling is none.

### Final Decision and Justification
Starting point: EIC-weighted rating 2.73 → 3. Composite cross-check 54.0 → band 3, consistent. I keep 3 and do not depart. **Pool position (EIC): better than about 46% of ICLR submissions.** Deciding evidence: this is a neat idea for a new problem, but the main comparison cannot be interpreted (a single per-position operating point, adapted baselines at matched δ rather than matched quality, random edits), and the novelty positioning misses a closely related NeurIPS 2024 paper. Single-regime evaluations and adapted baselines are common among accepted papers when the main claim still survives them; here they sit directly on the main claim (localization accuracy against baselines), so they weigh more. The reviewers' pool positions spread by 28 points (38–66), below the 30-point trigger; the disagreement is about how much a first paper on a new task should be credited, and I side with the lower group because the deciding evidence (operating point and baselines) is verified. The decision does not exceed the (absent) DA ceiling. The issues are fixable with existing models and modest compute, which matters for the rebuttal and revision (ICLR allows a revised PDF).

---

## Score Summary

### Official Scores and EIC Assessment
(Output of `aggregate_scores.py scores.json --venue iclr --final 3`.)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.25 | 24% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 19% |
| DA | 4 | 0.85 | 1.00 | 19% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 56 | 64 | 56 | 46 | 54.4 | 54.0 | 18 |
| Clarity & Presentation | 66 | 68 | 72 | 66 | 64 | 67.2 | 67.0 | 8 |
| Novelty & Originality | 52 | 54 | 68 | 58 | 48 | 56.0 | 55.3 | 20 |
| Significance & Impact | 48 | 54 | 70 | 58 | 48 | 55.6 | 54.7 | 22 ⚠ |
| Experimental Validation | 38 | 44 | 54 | 46 | 36 | 43.6 | 43.0 | 18 |
| Reproducibility | 46 | 52 | 60 | 54 | 48 | 52.0 | 51.5 | 14 |
| Ethical Compliance | 62 | 62 | 68 | 64 | 60 | 63.2 | 62.9 | 8 |
| **Composite** | 50.0 | 54.4 | 64.3 | 56.2 | 48.0 | **54.6 (before)** | **54.0 (after)** | |
| Pool position | 38 | 50 | 66 | 52 | 40 | | | |

Official rating mean 2.80; EIC-weighted rating 2.73 → starting point 3. Composite bands: official 3, EIC 3; no consistency warnings.

**Spread discussion (Significance, 22 ⚠):** R3 (70) credits the forensic direction; R1/DA (48) point out that impact depends on edits not tested. The editor adopts the middle-low view (about 55) since significance of a method for real edits is not shown.

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); the label equals the EIC decision 3. Presented as the skill's translation, not official wording |

Cross-venue outlook was not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Detecting Post-generation Edits to Watermarked LLM Outputs via Combinatorial Watermarking" to ICLR.

The paper tackles a timely question: not only whether text is LLM-generated, but whether and where it was changed afterwards. The idea of putting a deterministic pattern in the watermark itself is simple and appealing.

**Overall Assessment:** the panel valued the new framing and the clear exposition, but concluded that the experiments do not yet establish the central claim. The comparison is performed on random token edits, at a single per-position false-alarm rate, against baselines that were adapted rather than designed for localization.

**Key Strengths Identified by Reviewers:**
1. A new, well-motivated task with explicit metrics (R1, R2, R3, R4).
2. A cheap, interpretable mechanism with honest discussion of edits it cannot see (R1, R3).
3. Clear writing and candid limitations (R1, R3, R4).

**Key Concerns Requiring Attention:**
1. The evaluation is limited to random short edits; no informed-adversary or human-edit comparison with baselines (CONSENSUS-4).
2. Baseline treatment and the choice to match δ rather than quality or detectability (CONSENSUS-4).
3. The operating point (per-position false alarm 0.1) and absent ROC/precision (CONSENSUS-3).
4. Novelty statement and related work, including an uncited NeurIPS 2024 segmentation method and a mischaracterized reference (CONSENSUS-3).

No Devil's Advocate CRITICAL issue was raised; its strongest objection (the evaluation measures random edits, not the stated threat) is recorded as MAJOR.

**Decision: Borderline Reject (3).** The panel sees a promising direction whose evidence does not yet match its claims. A revision that matches operating points, adds realistic edits, and positions the work against segmentation/edit-robust methods would change this assessment.

Please refer to the Revision Roadmap below.

Sincerely,
Marguerite Solvang-Adeyemi
Editor-in-Chief (meta-reviewer, fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Random/synthetic edits only, no adversary | R1, R3, R4, DA | CONSENSUS-4 |
| Baselines adapted, unmatched quality | R1, R2, R4, DA | CONSENSUS-4 |
| Operating point / FPR / no ROC | R1, R3, DA | CONSENSUS-3 |
| Novelty positioning and citations | R2, R4, DA | CONSENSUS-3 |
| Detectability vs quality/robustness trade-off | R1, R3, DA | CONSENSUS-3 |
| Fixed pattern, aligned edits, stealing | R2, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall rating of a first paper on a new task | R3 (4) | R1, DA (2) | Credit for a new task is real, but the main comparison is not interpretable; EIC keeps 3 |
| Whether the method's detectability is "comparable" | Paper, R3 (Fig. 8 text) | R1, DA | Fig. 8 compares score drops under edits, not detectability against quality; Overstated as worded |

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Random edits vs stated threat | Yes (R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | Adapted baselines, unmatched quality | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | Single operating point | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Detectability claim | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Uncited close prior work | Yes (R2) | n/a | n/a |
| DA-M6 | MAJOR | Theorem vs algorithm | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are issues the EIC verified as undermining the main claim, ordered by impact on the decision.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Main comparison at a single per-position operating point; no ROC, precision or text-level false-alarm rate; calibration split not stated | R1-W1, DA-M3 | §4, Def. 2, Fig. 5 | Report ROC/PR curves, text-level false alarms on clean watermarked and human text; calibrate on disjoint texts | Low; < 1 GPU-h on existing outputs | Yes |
| P1-2 | Baselines adapted ad hoc, matched δ not matched quality; γ and subset sizes unstated; no localization baseline | R1-W2, DA-M2, R2-W4 | §4, §4.1, Fig. 5, Fig. 6 | State γ and sizes; sweep w for all methods; compare at matched PPL; add segmentation/change-point baseline and [25]/[32] where applicable | Medium; ~10–20 GPU-h | Yes (partly) |
| P1-3 | Evaluation is random short edits only; threat model untested | R1-W3, R4-W1, R3-W1, DA-M1 | §4, Table 1 | Add human and LLM-paraphrase edits, ≥ 200 tokens, instruction-tuned model, multinomial sampling in main text, pattern-preserving attacker; add baselines to Table 1; or narrow title/abstract | High; ~30–60 GPU-h plus annotation | Partly |
| P1-4 | Novelty statement and related work: uncited segmentation work, [32] mischaracterized | R2-W1, R2-W2, DA-M5 | §1.1 | Cite and differentiate Segmenting Watermarked Texts (NeurIPS 2024); correct [32] description; replace "no existing method" | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Detectability "comparable to state-of-the-art" not supported | R1-ERR-2, DA-M4 | Add baseline curves in §4.2; narrow wording | Low–Med | Yes |
| S2 | Theorem 3.1 per-token vs min-decision; assumptions of Janson's inequality | R1-W4, DA-M6 | Union bound or restate as heuristic; check conditions | Low | Yes |
| S3 | Fixed partition: stealing and period-aligned blind spots | R2-W3, R3-W1 | Discuss stealing attacks; try keyed pseudo-random phase | Medium | Partly |
| S4 | Reproducibility: code, seeds, intervals, PPL oracle | R1-W5 | Release code and texts; report intervals and cell counts | Low | Yes |
| S5 | Missing references: Golowich–Moitra; stealing line of work | R2 | Cite and discuss; check entry [19] | Low | Yes |
| S6 | Detection–quality–robustness triangle | R3-W2 | Plot the three-way trade-off | Medium | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Appendix A.1 pair-count constant | R1 ERR-3 | Check convention (EIC: Partly correct) |
| N2 | Algorithm 3 index range; Fig. 4 example selection | R1, DA-m3 | State selection rule |
| N3 | Table 1 settings (decoding, L, threshold) | DA-m2 | State them |
| N4 | Re-tokenization and token-entropy analysis | R3-W3 | Add short analysis |
| N5 | Cross-field links (codes, fragile watermarking, change-point tests) | R3 | Short related-work paragraph |
| N6 | Statement on handling of generated misinformation | R3-W4 | One sentence |

## Estimated Revision Effort
- Priority 1: 4 items, about 1–2 weeks (P1-1 and P1-4 within a rebuttal window; P1-3 is the long pole).
- Priority 2: 6 items, about 3–5 days.
- Priority 3: 6 items, about 1 day.
- **Total estimated revision time:** about 2–3 weeks including new experiments.

---

## Notes on the run
- A literature check ran in strict mode (cutoff 2025-09-24): 8 queries (7 claim, 1 baseline); no external benchmark exists in the paper; all kept results used are prior (peer-reviewed or arXiv-only 6+ months). No recent or concurrent preprint is used as a weakness.
- The reports were produced sequentially from one context, not by independent agents.
- Figures were unavailable; E9 (figure integrity) was not checked.
