# Academic Paper Review: "Semantic Energy: Detecting LLM Hallucination Beyond Entropy"

*Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Date: 2026-11-05. This is a simulation of how a careful panel would likely see this draft, not a prediction. The five reviewer passes were run one after another in a single model context (no subagents), so they share one context, and the reports were kept role-separated. Figures were not available (text only): Fig. 1, Fig. 2 and Fig. 3 were judged from captions, in-figure text and the text that cites them.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Semantic Energy: Detecting LLM Hallucination Beyond Entropy |
| Primary Discipline | ML → uncertainty quantification for LLMs (hallucination detection) |
| Secondary Discipline(s) | Statistical physics analogies (energy-based models), NLP (open-domain QA) |
| Paper Type | Empirical (new scoring method plus benchmark evaluation); composite weights: empirical |
| Core Technique(s) | Semantic entropy (sampling plus semantic clustering), raw-logit "energy" score, AUROC/AUPR/FPR95 against answer correctness |
| Target Venue | ICLR (stated by user); tier: top-tier ML conference; profile key `iclr` (2026 cycle, scale status *secondary*) |
| Venue-Specific Notes | none (no ECCV/ACM MM/TPAMI-specific rules). ICLR practice: public reviews, revised PDF allowed during discussion |
| Paper Maturity | Early draft / workshop-level submission: no appendix, no variance, one baseline, protocol largely unstated |
| Ethics-Relevant Content | none (public QA benchmarks, no human data) |

### Claimed Contributions (as stated by the authors, Sec. 1)
1. **C1:** "We expose the limitations of current uncertainty estimation methods based on probability and identify the failure cases in Semantic Entropy." (problem)
2. **C2:** "We introduce Semantic Energy, a novel framework to evaluate the uncertainty of LLM responses." (method; cluster-level energy from raw logits, Eq. 18–19)
3. **C3:** Boltzmann instantiation that "achieves an average performance improvement of more than 13% compared in terms of AUROC to Semantic Entropy in cases where the latter is confident." (result; Sec. 1, Sec. 4.3.1, Table 2)

### Paper memory (factual record shared with all reviewers)
- **Claims:** C1–C3 above. Abstract also claims: "Experiments across multiple benchmarks show Semantic Energy significantly improves hallucination detection"; Sec. 4.2 claims "robustness" and "better calibration".
- **Setup facts:** Models: Qwen3-8B and ERNIE-21B-A3B (MoE) (Sec. 4.1); Sec. 4.3.2 says "Qwen-8B". Datasets: "CSQA" (He et al., 2024, which is Chinese SimpleQA; Fig. 3 calls it "CSimpleQA") and TriviaQA (Sec. 4.1). Baseline: semantic entropy only (Sec. 4.1). Metrics: AUROC, AUPR, FPR95. Number of samples n, sampling temperature/top-p, clustering method, correctness judge, dataset sizes/subsets, prompts, seeds, compute, which response/cluster is scored: **not stated after search** (grep for split/select/tune/seed/temperature/judge/prompt/hyperparameter found nothing relevant; the only "5 responses" is the toy example in Sec. 3.1). Splits: no training involved; whole benchmarks presumably evaluated; no selection or tuning is described (k·τ = 1 "by default", Sec. 3.2.2).
- **Headline numbers:** Table 1 (AUROC 71.6→76.1, 69.6→74.8, 77.4→80.2, 75.1→81.0); Table 2 (SE exactly 50.0% AUROC, energy 66.7/62.1/58.9/65.8); ">13%" (Sec. 1, 4.3.1).
- **Appendix/supplement:** none. Code and intermediate data "available at [link removed]" (abstract).
- **Unverifiable:** Fig. 1 graphics, Fig. 2 (think mode, no numbers in text), Fig. 3 plots (only AUROC labels extracted: 69.1, 63.0, 74.8, 76.1). Some symbols (V vs. its barred version, Sec. 3.2.1; Eq. 14–16 sub-vocabulary notation) are garbled by extraction and are treated as unverifiable.

### Integrity signals
`scripts/integrity_scan.py` was run (with `--redact`): *No reviewer-directed text or hidden characters found.* No injected instructions were seen while reading either. Reviewers read the (unchanged) reviewer copy.

### Literature-check ledger (Phase 1.5; strict, cutoff 2025-09-24)
Fingerprint written (title, method names, distinctive phrases, cutoff). Queries: 4 claim (C1 ×1, C2 ×2, C3 ×1), 1 baseline (TriviaQA), 1 expansion that returned results, plus one further expansion query that kept nothing. `coverage` gap: "no prior work kept from 2021" (partly closed by `verify` of a 2020 sequence-uncertainty paper). 50 results kept, none dropped as the paper itself; `similarity`: no high conceptual overlap (cosine ≥ 0.30), no text overlap (0 shared 8-grams); closest prior: uncertainty-aware in-context learning (0.266), semantic entropy probes (0.202), VL-Uncertainty (0.199). `benchmarks` listed no external benchmark names; `scout` for TriviaQA found no abstract with comparable AUROC numbers. Claim-level novelty profile (`novelty`): C1 medium, C2 medium (both: closest prior LogTokU, level 3, cited by the paper), C3 high; paper novelty 0.72; attribution: *Estimating LLM Uncertainty with Evidence* (arXiv 2502.00290).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Halvard Osei-Lindqvist, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / uncertainty estimation, ML evaluation methodology, area-chair experience at ICLR/NeurIPS
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR actually accepts; counts evidence, not heads

### Reviewer 1 (Methodology): Dr. Kwabena Iversen-Mbeki, industrial research lab (North America)
- **Seniority / Expertise**: Mid-career industry scientist / LLM evaluation protocols, selective prediction, AUROC-based UQ benchmarks
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched normalisation and equal tuning across baselines; recomputes every table

### Reviewer 2 (Domain): Dr. Yuliana Torvaldsen-Park, NLP group, public research university (East Asia)
- **Seniority / Expertise**: Senior faculty / sampling-based and logit-based UQ for LLMs, factuality in QA
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work closely; wants the nearest prior method compared, not just cited

### Reviewer 3 (Perspective): Dr. Mateo Arkwright-Lindo, physics department, university (South America)
- **Seniority / Expertise**: Associate professor / statistical mechanics, energy-based models, evidential learning
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive and expansive; checks whether the physics borrowed is the physics used

### Reviewer 4 (Generalist): Dr. Ingrid Szabo-Nakamura, applied LLM group, industrial lab (Europe)
- **Seniority / Expertise**: Senior industry scientist / LLM applications, retrieval and generation
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; wants the paper readable and the claim matched to the evidence

### Devil's Advocate: Dr. Olamide Fairchild-Reyes, statistics department, university (Africa)
- **Seniority / Expertise**: Mid-career faculty / evaluation methodology, causal inference, ablation design
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and never hostile; asks what else could explain the result

*Personas are fictional. Proceeding with the stated assumptions (ICLR as stated; paper type Empirical).*

---

# Phase 1: Independent Reports

---

# Peer Review Report

## Paper: Semantic Energy: Detecting LLM Hallucination Beyond Entropy
## Reviewer: Dr. Kwabena Iversen-Mbeki, Reviewer 1 (Methodology) (industrial research lab, North America; fictional persona)
## Expertise: LLM evaluation protocols; selective prediction; AUROC-based UQ benchmarking
## Date: 2026-11-05

## Summary
The paper proposes Semantic Energy, a response-level uncertainty score for LLMs. Like semantic entropy, it samples several responses and clusters them by meaning. Instead of cluster probability mass it scores the cluster by the negated raw logits of the sampled tokens, averaged over tokens and members (Eq. 18–19). On Qwen3-8B and ERNIE-21B-A3B, with a Chinese and an English QA set, AUROC against answer correctness improves by 2.8–5.9 points over semantic entropy (Table 1). On questions where all samples fall into one cluster, where semantic entropy is constant, energy reaches 58.9–66.7 AUROC (Table 2).

## Strengths
### S1: A diagnostic that targets the right regime
Table 2 isolates the K=1 subset where semantic entropy is degenerate, and reports the same three metrics there. This is the right place to look and is a useful analysis of the baseline's failure mode (Sec. 4.3.1).
### S2: Consistent direction across the 12 reported comparisons
Energy beats semantic entropy on every model × dataset × metric cell in Table 1 and Table 2 (24 of 24). The arithmetic is correct: all 24 printed deltas recompute (e.g., 76.1 − 71.6 = 4.5; 81.0 − 75.1 = 5.9; 66.7 − 50.0 = 16.7).
### S3: Cheap and drop-in
Given logit access, the score adds no sampling cost over semantic entropy. Evaluating on two different model families and two languages is a sensible start (Sec. 4.1).
### S4: A semantic-aggregation ablation exists
Fig. 3 compares energy with and without clustering on two datasets, so the authors at least test one design choice (Sec. 4.3.3).

## Weaknesses
### W1: The claim "logits beat probabilities" is not isolated from two other differences (MAJOR)
(a) *Normalisation.* Semantic entropy as defined here uses the unnormalised sequence likelihood p(x|q) = ∏ p(x_t|·) (Eq. 6), while energy is length-averaged (Eq. 17, 19, "1/(nT_i)"). Whether the baseline was run with length-normalised probabilities is not stated, so the comparison may measure length normalisation, not logits. (b) *Cluster size.* In Eq. 18–19 the cluster energy is a sum over members divided by n, not by cluster size, so a cluster with more members has a larger total magnitude. Energy therefore partly re-encodes sample frequency, the information semantic entropy uses. (c) The authors' own Fig. 3 points this way. Single-response energy with no clustering reaches AUROC 69.1 (TriviaQA) and 63.0 (CSimpleQA). The matching semantic-entropy numbers in Table 1 (Qwen3-8B, identified by the identical 74.8/76.1 energy values) are 69.6 and 71.6. So raw-logit scoring alone is on par (−0.5) or clearly worse (−8.6) than semantic entropy; the gain appears only once logits are combined with cluster aggregation.
- **Suggested Fix:** A 2×2×2 grid on the existing samples: {prob, logit} × {length-normalised, not} × {cluster mass, cluster mean / discrete count}, plus discrete semantic entropy. Cost: re-scoring cached samples, under 1 GPU-hour if the intermediate data released with the paper include token logits.

### W2: One baseline, and the headline ">13%" is measured against a constant scorer (MAJOR)
The only comparator is semantic entropy (Sec. 4.1: "we use semantic entropy (Farquhar et al., 2024) as the baseline"). The paper defines token-level entropy (Eq. 2–4) but never evaluates it. In Table 2 semantic entropy is constant ("always zero", Sec. 4.3.1), giving exactly 50.0% AUROC and 95.0% FPR95, so ">13%" is the improvement of any non-constant score over chance. Sensible non-constant references on the same samples are missing: mean token log-probability of the answer, length-normalised predictive entropy, max logit, log-sum-exp of logits (the free-energy score from the OOD work the paper cites), and prior logit/evidence-based work (LogTokU, cited but not run).
- **Suggested Fix:** Add these scorers to Table 1 and, importantly, Table 2; report Table 2 against the best non-semantic scorer rather than against a constant. Cost: negligible if logits are cached.

### W3: The protocol is too under-specified to reproduce or interpret (MAJOR)
After a protocol sweep, none of the following is stated: number of samples n, sampling temperature/top-p, how responses are clustered (NLI model? LLM judge?), how answer correctness is decided (exact match? LLM judge?), which response or cluster the score and the correctness label refer to, dataset sizes/subsets, prompts, whether logits are raw or temperature-scaled, seeds, compute. The share of single-cluster questions is not given (Fig. 1 says only "This situation accounts for a large proportion"), so how much of Table 1's gain comes from the K=1 regime is unknown. There is no appendix. The abstract promises code and intermediate data; promised code gets capped Reproducibility credit.
- **Suggested Fix:** A protocol paragraph plus an appendix table with every item above, per-dataset K=1 share, and Table 1 split into K=1 / K>1 questions.

### W4: No uncertainty on the numbers; narrow scope behind broad wording (MAJOR)
Single runs with no CI or seeds. Gains of 2.8–5.9 AUROC on two benchmarks are probably real but unquantified. Evidence covers 2 models, 2 short-form QA sets and one think-mode figure (Fig. 2, numbers not given in the text), yet the text says "consistently outperform", "robustness" (Sec. 4.2) and the abstract says "Experiments across multiple benchmarks".
- **Suggested Fix:** Paired bootstrap CIs on AUROC differences over questions (minutes of compute); 3 resampling seeds for the n samples; one additional open-weight family and one long-form or reasoning-style set, or narrow the wording.

**Minor:** dataset naming (CSQA vs. CSimpleQA; "Qwen-8B" vs. Qwen3-8B); Eq. 19 binds x^(i) on the left and sums over x^(i) ∈ C_k on the right.

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | SE fails when samples agree but are wrong ("nearly half of the samples … are actually incorrect") | Sec. 3.1 | Table 2 AUPR 55.8/75.1/77.0/85.9 imply 44/25/23/14% incorrect | Partially (true for Qwen3-8B CSQA only, "some datasets" is defensible) |
| C2 | Logits capture inherent uncertainty lost by normalisation | Sec. 1, 3 | Table 1, Fig. 3 | Partially (not isolated, see W1) |
| C3 | ">13% AUROC where SE is confident" | Sec. 1, 4.3.1 | Table 2 (16.7, 12.1, 8.9, 15.8; mean 13.4) | Supported arithmetically; vs. a constant baseline |
| – | "better calibration" | Sec. 4.2 | none (no ECE/Brier) | Unsupported |

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E4 | Eq. 6 vs. Eq. 17/19, Sec. 4.1 | "we use semantic entropy (Farquhar et al., 2024) as the baseline" | Baseline defined with unnormalised sequence probability, energy length-averaged; implementation of the baseline not stated | Cross-referenced Eq. 6, Eq. 17, Eq. 19 | Medium | MAJOR | State and match normalisation (W1) |
| ERR-2 | E5 | Sec. 4.2 | "indicating better calibration and reduced false positive rates" | AUPR and FPR95 are ranking/threshold metrics, not calibration measures; no ECE/Brier reported | Checked metrics listed in Sec. 4.1 and Table 1 | High | MINOR | Reword or add ECE |
| ERR-3 | E2/E3 | Sec. 6 | "invariant to the scale of the logits" | Softmax and cross-entropy are invariant to an additive shift of all logits (softmax(z+c) = softmax(z)), not to scaling (softmax(2z) ≠ softmax(z)). The shift freedom is what makes absolute logit values unconstrained | Derived | High | MAJOR | Correct the statement; discuss shift invariance (see R3-W1) |
| ERR-4 | E6 | Sec. 4.1, 4.3.2, Fig. 3 | "experiments on Qwen-8B using the CSQA dataset" | Model named Qwen3-8B in Sec. 4.1; the dataset is "CSQA" in tables and "CSimpleQA" in Fig. 3 | Cross-referenced | High | MINOR | Harmonise names |
| ERR-5 | E1 | Tables 1–2 | all "⇑" deltas | Recomputed all 24 deltas, no mismatch | Recomputed | High | none | none |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Core claim not isolated; one baseline; protocol undefined |
| Clarity | 2 | Readable, but method details missing |
| Significance | 2 | Useful if it holds, but evidence narrow |
| Originality | 2 | Logit-based scoring plus SE clustering is a small step from prior logit/evidence work |

## Dimension Scores (0–100)
**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim is not separated from length normalisation and cluster frequency (W1), and the comparison set is a single baseline with the protocol unstated (W2–W3).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 44 | Developing | Confounded comparison; theory-to-score gap |
| Clarity & Presentation | 62 | Competent | Easy to follow at the idea level |
| Novelty & Originality | 48 | Developing | Incremental over cited LogTokU plus semantic entropy |
| Significance & Impact | 45 | Developing | Narrow evidence, no downstream demonstration |
| Experimental Validation | 38 | Developing | One baseline, no variance, two short-form sets |
| Reproducibility | 36 | Developing | Key setup absent; code only promised |
| Ethical Compliance | 65 | Competent | Nothing at stake; Sec. 6 states a real limitation |

## Questions for Authors
1. What are n, the sampling temperature, the clustering model and the correctness judge? Which response's correctness is the AUROC label? (Answers would let me judge Table 1; absence keeps Reproducibility low.)
2. Does the semantic-entropy baseline use length-normalised log-probabilities? If energy beats a length-normalised SE and discrete SE, W1 largely falls away.
3. What share of questions is K=1, and what are Table 1 AUROCs on K>1 only?
4. Is Fig. 3 on Qwen3-8B? (I inferred this from the matching 74.8/76.1.)

## Limitations Assessment
**Partially.** Sec. 6 honestly notes logits are "not strictly equivalent to energy". Missing: white-box requirement, sampling cost, scope (short-form QA, two models).

## Ethics Review Flag
**No.**

## Overall Score
**2: Reject.** The idea is reasonable and cheap, but the evidence neither isolates the claimed mechanism nor includes the baselines needed to interpret a few-point AUROC gain; the protocol cannot be reconstructed.

## Confidence
**4:** Checked all tables and equations; figures not visible; supplement absent (so not penalised as missing, only as unstated).

---

# Peer Review Report

## Paper: Semantic Energy: Detecting LLM Hallucination Beyond Entropy
## Reviewer: Dr. Yuliana Torvaldsen-Park, Reviewer 2 (Domain) (NLP group, public research university, East Asia; fictional persona)
## Expertise: sampling-based and logit-based UQ for LLMs; factuality in open-domain QA
## Date: 2026-11-05

## Summary
The work argues that semantic entropy, which uses normalised probabilities of semantic clusters, cannot flag confidently wrong answers where all samples agree. It replaces probability mass with a logit-based "energy" per cluster, motivated by a Boltzmann-distribution view and by prior energy-based OOD detection. Experiments on two models and two QA datasets show a few AUROC points of improvement and nontrivial AUROC where semantic entropy is constant.

## Strengths
### S1: A relevant, well-posed gap
Semantic entropy is the standard sampling-based detector, and its blindness to consistent errors (Fig. 1, Sec. 3.1) is a real limitation worth studying. The question is stated sharply with a concrete failure example.
### S2: Positioning against the closest recent work is at least gestured at
The paper names LogTokU (Ma et al., 2025) as the work that observed probabilities "lose the intensity information of logits" (Sec. 1) and builds the cluster-level aggregation on top (Sec. 4.3.3). The semantic-aggregation ablation is a sensible check of what is added.
### S3: Interesting cross-pollination
Importing the energy view from OOD detection (Liu et al., 2020) into sampling-based hallucination detection is a reasonable idea; the combination (logit intensity × semantic clustering) is not obviously done by the closest works I found (literature addendum below).
### S4: Honest closing caveat
Sec. 6 admits logits are only "energy-like".

## Weaknesses
### W1: Differentiation from LogTokU is thin and not empirical (MAJOR)
By the kept abstract of *Estimating LLM Uncertainty with Evidence* (arXiv 2502.00290; prior, arXiv-only, cited by the paper), that work already argues that probability-based methods perform poorly at token reliability, which is the paper's own motivation (Sec. 1). The paper cites it, so this is a differentiation issue, not a known-results issue. The claimed delta is the semantic clustering step (Sec. 4.3.3), yet LogTokU is never run; "w/o semantic" energy (Fig. 3a/b) is a proxy the authors built and describe as "such as in LogTokU". Novelty for C1 and C2 is therefore *medium* at best, and C1's framing ("we expose the limitations of probability-based methods") is shared with that work.
- **Suggested Fix:** Run LogTokU (or the closest faithful variant) as a baseline and add a delta paragraph (what is evidence-theoretic there vs. what is added here).

### W2: Related work and baseline set omit the standard sampling-based and internal-state comparators (MAJOR)
Related work (Sec. 5) lists method families but no comparison is made with any of them. Missing, with verified links in the addendum: kernel-based refinements of semantic entropy, cheap probe-based approximations of semantic entropy, internal-state methods, and standard UQ benchmarks that provide strong baselines and protocols. A paper positioned as "beyond entropy" needs at least the strongest entropy variants in Table 1.
- **Suggested Fix:** Add Kernel Language Entropy and a token-level length-normalised entropy baseline at minimum; adopt a published UQ benchmark protocol for comparability.

### W3: "Energy" is not the energy of the cited literature, and the theory is decorative (MAJOR)
The OOD work the paper builds on (Liu et al., 2020) uses a free-energy score that aggregates all logits of the output vocabulary through a log-sum-exp (as I recall it; authors please confirm). Here the energy is only the negative logit of the sampled token (Eq. 19), which resembles a max-logit-style score and discards the partition function the Boltzmann section introduces (Eq. 10–13). The assumption "we assume Zt is constant across t" (Sec. 3.2.1) removes exactly the quantity that defines an energy-based distribution. The Bayesian marginalisation (Eq. 14–16) does not enter the final score. The statement that semantic entropy "only reflects aleatoric uncertainty" while energy captures epistemic uncertainty (Sec. 3.1) is asserted, not tested.
- **Suggested Fix:** Evaluate the log-sum-exp free energy per token as a variant; shorten Sec. 3.2 to what is used, and either test the epistemic claim (e.g., on questions about entities of varying training frequency) or soften it.

### W4: Citation accuracy (MINOR→MAJOR if uncorrected; E7)
(i) The bibliography lists "Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation" as "Nature, 2024"; this paper has an arXiv v1 dated 2023-02-19 (verified by `verify`) and is not the Nature 2024 paper (Farquhar et al.). Sec. 2.1 attributes semantic entropy to Kuhn et al. 2024, Sec. 2.2/4.1 to Farquhar et al. 2024. (ii) Sec. 1 cites Fu et al. (2025) and Zhang et al. (2024) as showing logits "exhibit stronger inherent capabilities in characterizing uncertainty compared to probabilities"; the bibliography titles concern small-large model token routing and a decoding method, so I cannot tell what supports the sentence (a question, not an error).
- **Suggested Fix:** Fix the venue/year; replace or justify the logit-evidence citations.

### Novelty delta table (literature addendum)
| Claimed contribution | Closest prior work (link) | What it already does (from its abstract) | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 limits of probability-based UQ | Estimating LLM Uncertainty with Evidence (arxiv.org/abs/2502.00290) | Argues probability-based methods perform poorly at identifying token reliability | Failure case specific to semantic entropy (K=1 regime) | Cited; differentiated weakly |
| C2 energy-from-logits at cluster level | same | Logit-based evidence for token reliability | Aggregation over semantic clusters | Cited; no empirical comparison |
| C3 >13% AUROC in K=1 | none found (SEP arxiv.org/abs/2406.15927v1 targets cheap SE, not K=1) | – | Result against a constant baseline | n/a |

Per-claim verdicts (claim profile, `novelty`): C1 medium, C2 medium, C3 high (no close prior result found in 50 kept results; arXiv-only search, so at most medium by the skill's rule). One established-ish claim would be MAJOR at most; none reaches level 5. Attribution: the work closest to the paper as a whole is LogTokU.

### Baseline scout
| Benchmark / metric | Prior method (link, label) | Its reported number | Compared in the paper? | Paper's number | Note |
|---|---|---|---|---|---|
| TriviaQA / AUROC | Bias-Variance-Covariance Decomposition of Kernel Scores (arxiv.org/abs/2310.05833v2, prior peer-reviewed) | abstract: kernel entropy "more predictive … on CoQA and TriviaQA"; no number | No | – | Different settings; a pointer, not an under-report |
| TriviaQA | Semantic Reformulation Entropy (arxiv.org/abs/2509.17445v2) | none in abstract | No | – | concurrent: worth discussing only |
| TriviaQA | TECP (arxiv.org/abs/2509.00461v2) | none | No | – | concurrent: worth discussing only |

### Field snapshot (from kept results only)
Around 2020–22 the standard for sequence-level LLM/NLG uncertainty was token-likelihood and entropy scores (including sequence-level treatments such as Malinin and Gales) plus verbalised confidence ("Teaching models to express uncertainty in words"). From 2023–24 the field moved to sampling-based, meaning-aware scores (semantic entropy and variants), then to cheaper approximations (probes on hidden states, Bayesian budget-efficient estimates) and conformal/selective approaches. 2025 work adds logit- or evidence-based token reliability, internal dynamics analyses and reformulation-based variants. Current open problems named in kept abstracts: sampling cost, clustering instability, and reliability of single-answer confident errors. A few AUROC points over semantic entropy on short-form QA is incremental; a significant contribution now shows gains over the strongest entropy/kernel/probe baselines across several models and settings, or opens a new capability (long-form, reasoning, API-only). I used this to score Novelty and Significance in the 50s.

## Missing References
*Verified with `related_search.py verify` unless marked.*
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Nikitin et al., "Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities" (NeurIPS 2024; arxiv.org/abs/2405.20003v1, 2024-05-30) | Same problem (improving semantic entropy); must be discussed and ideally compared |
| Important | Kossen et al., "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs" (arXiv 2024; arxiv.org/abs/2406.15927v1) | Hidden-state approximation of semantic entropy; same detection task |
| Important | Vashurin et al., "Benchmarking Uncertainty Quantification Methods for Large Language Models with LM-Polygraph" (arxiv.org/abs/2406.15627v4, 2024-06-21) | Standard protocol and strong baselines (length-normalised and token-level scores) |
| Important | Chen et al., "INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection" (ICLR 2024; arxiv.org/abs/2402.03744v2) | Internal-state hallucination detection; relevant to the "inherent uncertainty" framing |
| Important | Malinin and Gales, "Uncertainty Estimation in Autoregressive Structured Prediction" (ICLR 2021; arxiv.org/abs/2002.07650v5) | Foundations of sequence-level uncertainty (length normalisation, token-level vs. sequence-level) |
| Helpful | Gruber and Buettner, "A Bias-Variance-Covariance Decomposition of Kernel Scores for Generative Models" (arxiv.org/abs/2310.05833v2) | Kernel entropy evaluated on TriviaQA |
| Helpful | Grathwohl et al., "Your Classifier is Secretly an Energy Based Model and You Should Treat it Like One" (ICLR 2020; arxiv.org/abs/1912.03263v3) | Logits-as-energy view with log-sum-exp |
| Helpful | Aichberger et al., "Semantically Diverse Language Generation for Uncertainty Estimation in Language Models" [verify] (not found on arXiv by title) | Improves sampling for semantic-entropy-style estimators |
| Discuss only | Semantic Reformulation Entropy (arxiv.org/abs/2509.17445v2, concurrent), TECP (arxiv.org/abs/2509.00461v2, concurrent) | Within 60 days of the cutoff: never a required comparison |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in baselines and theory-to-method link |
| Clarity | 2 | Fine at idea level; notation and citations slip |
| Significance | 2 | Plausibly useful, evidence narrow |
| Originality | 2 | Medium per claim profile |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a plausible idea in a crowded line (semantic-entropy improvements) with the nearest logit-based work not compared and the standard entropy/kernel baselines absent.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Derivation does not feed the score; "energy" differs from cited usage |
| Clarity & Presentation | 60 | Competent | Clear story, citation slips |
| Novelty & Originality | 50 | Developing | Medium on C1, C2; combination unchecked against LogTokU |
| Significance & Impact | 50 | Developing | Incremental in a crowded sub-field |
| Experimental Validation | 44 | Developing | One baseline |
| Reproducibility | 42 | Developing | Details absent |
| Ethical Compliance | 65 | Competent | Limitations honestly discussed in Sec. 6 |

## Questions for Authors
1. How does Semantic Energy compare empirically with LogTokU and with kernel language entropy on the same samples?
2. Do you intend the Liu et al. (2020) free-energy (log-sum-exp) score? If not, why is the sampled-token logit the right "energy"? (A log-sum-exp variant matching your results would strengthen the paper.)
3. What supports the sentence in Sec. 1 attributing "stronger inherent capabilities" of logits to Fu et al. (2025) and Zhang et al. (2024)?

## Limitations Assessment
**Partially.** Theory caveat given (Sec. 6); empirical scope limits and white-box requirement are not.

## Ethics Review Flag
**No.**

## Overall Score
**3: Borderline Reject.** A reasonable idea in a very active line whose closest prior work is cited but not compared, with a thin baseline set.

## Confidence
**4:** Literature check was arXiv-only; one point (Liu et al. score form) rests on my recollection.

---

# Peer Review Report

## Paper: Semantic Energy: Detecting LLM Hallucination Beyond Entropy
## Reviewer: Dr. Mateo Arkwright-Lindo, Reviewer 3 (Perspective) (physics department, university, South America; fictional persona)
## Expertise: statistical mechanics; energy-based models; evidential learning
## Date: 2026-11-05

## Summary
The authors borrow the vocabulary of thermodynamics to argue that raw logits carry "intensity" information that softmax normalisation discards, and use negative logits, averaged and aggregated over semantic clusters, as an uncertainty score. The empirical story is that this recovers signal in the cases where semantic entropy cannot discriminate (all samples semantically identical) and gives modest overall AUROC gains.

## Strengths
### S1: An appealing, practical observation
Normalisation indeed discards the common offset of the logits, and a score that looks at un-normalised magnitudes is a natural thing to try. It is nearly free at inference for open-weight models (Sec. 3.2.2, Eq. 19).
### S2: The degenerate-case analysis is a transferable idea
Looking at the subset where the incumbent score is constant (Table 2) is a clean way to find where a method adds information. Other UQ papers would benefit from the same breakdown.
### S3: Connection to a large literature on logits-as-energy
The link to energy-based OOD detection (Liu et al., 2020) opens a door to a body of results (free energy, partition-function arguments) the field can reuse.
### S4: Candour about the physics
Sec. 6 states that logits are "energy-like" only through implicit effects of initialisation and regularisation, which is the right caveat.

## Weaknesses
### W1: The central assumption is the one the physics warns against (MAJOR)
The framework sets E = −z and assumes the partition function is constant: "For simplicity, we assume Zt is constant across t." (Sec. 3.2.1). But softmax/cross-entropy fix logits only up to an additive per-context constant, so the training objective does not make the raw magnitude of a logit comparable across contexts (and the paper's Sec. 6 sentence on "scale" invariance is in fact about shift invariance; see R1 ERR-3). In physics terms, the paper compares energies from different systems with different, unknown reference levels. The empirical gains may still be real (the final-layer norm and unembedding scale make logits informative in practice), but the paper offers no analysis of why, and the explanation "probabilities lose intensity" is not a mechanism until the shift freedom is addressed.
- **Suggested Fix:** Add a diagnostic: correlate the sampled-token logit with the log-partition (log-sum-exp) and with the max logit across questions; show energy vs. free energy; discuss the shift freedom explicitly.

### W2: Deployment assumptions are not discussed (MAJOR for impact, fixable by text)
(i) White-box logit access: many deployed LLMs expose only top-k log-probabilities or none, so the method excludes API-only settings, where semantic entropy and its discrete variants still apply. (ii) Cost: n samples plus clustering remain, unreported. (iii) Thresholding: AUROC is shift-invariant but any deployed alarm needs a threshold, and logit scale differs across models, prompts and domains; no calibration or threshold-transfer analysis is given. (iv) Evidence is short-form QA with one-semantic-answer questions; long-form and reasoning outputs (where K=1 never happens exactly) are not addressed, although Sec. 4.3.2 touches think mode.
- **Suggested Fix:** Add a limitations paragraph and one threshold-transfer or selective-prediction curve (coverage vs. accuracy) across the two datasets.

### W3: "Downstream application" is not demonstrated (MINOR→MAJOR for impact)
The abstract says the method offers "more reliable signals for downstream applications such as hallucination detection". Hallucination detection is the evaluated task, not a downstream one; no selective answering, retrieval trigger or abstention experiment is shown (Sec. 5 lists such applications only as related work).
- **Suggested Fix:** One selective-prediction or RAG-trigger experiment, or reword.

### W4: Connections left unexplored (suggestion)
Evidential deep learning (Dirichlet evidence from logits) and conformal prediction are close relatives; entropy/frequency-regulation mechanisms in the final layers (a line of work on "confidence regulation neurons" appears in the literature check, link in addendum, title only read) bear directly on what logit magnitude reflects. Worth discussing for a mechanistic account.

## Missing References
*(optional for this role; I defer to Reviewer 2's verified list.)* Lines of work: evidential deep learning for classification uncertainty; free-energy scores for OOD; conformal prediction for generation; confidence-regulation/entropy neurons in LMs (arxiv.org/abs/2406.16254v2, title only).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Core assumption unaddressed |
| Clarity | 2 | Physics section does not match the score |
| Significance | 2 | Potentially useful, deployment unaddressed |
| Originality | 2 | Reasonable combination |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting, cheap idea with a visible regime-level win (Table 2), pulled back by the unsupported theory link and thin evidence.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Competent (low) | Empirics sound arithmetically; theory unsound as stated |
| Clarity & Presentation | 62 | Competent | Story easy to follow |
| Novelty & Originality | 54 | Competent (low) | Fresh angle on SE's blind spot |
| Significance & Impact | 56 | Competent (low) | Practical if it generalises |
| Experimental Validation | 48 | Developing | Narrow |
| Reproducibility | 45 | Developing | Details absent |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations stated |

## Questions for Authors
1. How do energy scores behave across prompts of different length or domain? Is the AUROC gain preserved when the logit offset is removed (e.g., subtracting the log-sum-exp)? A positive answer would raise my score; a negative one would change the paper's story.
2. Does the score survive API-style access (top-k logprobs only)?
3. Can you show one actual downstream use (selective answering)?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.** Nothing ethics-relevant (public QA benchmarks; no deployment claims). Minor: note over-reliance risk of a detection score used for safety decisions.

## Overall Score
**3: Borderline Reject.** I like the regime-level diagnostic and the cheapness, but the theory and scope need substantial work.

## Confidence
**3:** Outside my home field for the LLM-specific literature.

---

# Peer Review Report

## Paper: Semantic Energy: Detecting LLM Hallucination Beyond Entropy
## Reviewer: Dr. Ingrid Szabo-Nakamura, Reviewer 4 (Generalist) (applied LLM group, industrial lab, Europe; fictional persona)
## Expertise: LLM applications, retrieval and generation
## Date: 2026-11-05

## Summary
The paper identifies a failure of semantic entropy: when sampled responses all mean the same thing, entropy is zero even if the answer is wrong. It proposes to score semantic clusters by raw logits (an "energy") rather than normalised probabilities, and shows on two models and two QA datasets that this detects errors better than semantic entropy overall and especially where semantic entropy is constant.

## Strengths
### S1: A crisp problem and example
Fig. 1 with the "seconds in an hour" vs. "Huron Falls" contrast conveys the failure mode immediately; I could state the contribution after reading the introduction.
### S2: Simple method with tidy headline results
Table 1 and Table 2 report three metrics on four model/dataset pairs with all-positive deltas; the text states them accurately (I rechecked several).
### S3: Relevant to practitioners
Hallucination flagging is a pressing application need, and a score that costs nothing extra beyond semantic entropy is attractive (Sec. 3.2.2).
### S4: Honest discussion
Sec. 6 acknowledges limitations of the energy interpretation.

## Weaknesses
### W1: The method section is dominated by derivation that the score does not use; the score's actual definition is under-specified (MAJOR)
Sec. 3.2 spends two pages on Boltzmann distributions, a Bayesian marginalisation (Eq. 14–16), free-energy density and a sub-vocabulary conditional (Eq. 15), then collapses to "E = −z, kτ = 1" (Sec. 3.2.2, Eq. 19). A reader cannot tell which cluster's energy becomes the question-level score, how the cluster is chosen, or what n is; symbols are overloaded (T is temperature in Eq. 10's text and sequence length T_i; "partial function" appears where "partition function" is meant, Sec. 3.2.2). The experimental setup (Sec. 4.1) is two short paragraphs.
- **Suggested Fix:** Replace Sec. 3.2 with a half-page definition and a worked example (the 5-sample numbers in Fig. 1 with the actual formula), and move the physical motivation to a remark.

### W2: Wording is stronger than the evidence (MAJOR)
"Significantly improves" (abstract) with no test; "consistently outperform" and "robustness" (Sec. 4.2) from two models and two datasets; "indicating better calibration" (Sec. 4.2) with no calibration metric; "downstream applications such as hallucination detection" (abstract) when detection is the task; "average performance improvement of more than 13%" is in percentage points against a constant scorer.
- **Suggested Fix:** Narrow the wording to what Tables 1–2 show; report percentage points.

### W3: Evaluation scope is thin for ICLR (MAJOR)
One baseline, two models from one ecosystem, two QA sets of short answers, no variance, no ablation beyond Fig. 3. Accepted ICLR papers on LLM UQ typically show several model families and the strongest known baselines.
- **Suggested Fix:** Add a third model family, a stronger baseline set (see R2-W2) and CIs; or reposition as a focused diagnostic/workshop contribution.

**Minor:** "CSQA" vs. "CSimpleQA", "Qwen-8B" vs. "Qwen3-8B"; "In of physics" (Sec. 3.2); Fig. 2 caption gives no model or numbers in the text; Fig. 1 caption "clusters of activity".

### Venue criteria checklist (ICLR)
| Item | Grade | Location |
|------|-------|----------|
| Soundness (claims supported by evidence) | Partly | Tables 1–2 vs. W1 of R1 |
| Presentation | Partly | Sec. 3.2 vs. Sec. 4.1 |
| Contribution (significance for the community) | Partly | Sec. 1, Table 2 |
| Reproducibility (details/code) | Not met | Sec. 4.1; code only promised |
| Fit with ICLR topics | Met | representation of LLM uncertainty |
| Limitations stated | Partly | Sec. 6 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence partial |
| Clarity | 2 | Idea clear, method definition not |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Modest |

## Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a readable idea with consistent small gains, but one baseline, two datasets, no variance and an under-specified setup, which is the profile of a typical rejected submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | |
| Clarity & Presentation | 60 | Competent | Clear idea; method definition and notation weak |
| Novelty & Originality | 50 | Developing | |
| Significance & Impact | 52 | Developing | |
| Experimental Validation | 46 | Developing | |
| Reproducibility | 42 | Developing | |
| Ethical Compliance | 64 | Competent | |

## Questions for Authors
1. Which cluster supplies the question-level score (largest? that of the greedy answer?) and how is correctness assigned? (Needed to read Table 1 at all.)
2. Would the results survive a third model family? A "yes" with CIs would move me to borderline accept.
3. Are the numbers 35 and 25 in Fig. 1 cluster energies before or after the 1/n factor in Eq. 19?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3: Borderline Reject.** The community would lose little if this version were rejected and a more complete one resubmitted; the central idea is worth a fuller study.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Semantic Energy: Detecting LLM Hallucination Beyond Entropy
## Reviewer: Dr. Olamide Fairchild-Reyes (statistics department, university, Africa; fictional persona)

---

## Steelman
Semantic entropy gives zero uncertainty whenever all samples agree, yet agreeing samples are wrong a substantial fraction of the time. A logit-intensity score is not constrained to zero in that regime, and the authors show that it discriminates correct from incorrect single-cluster answers (AUROC 58.9–66.7) and improves overall AUROC by 2.8–5.9 points on two models and two datasets, at no extra sampling cost.

---

## Core Argument Chain
1. Semantic entropy depends on normalised probabilities, so it is blind to "inherent" (epistemic) uncertainty (Sec. 3.1).
2. Raw logits retain intensity information that normalisation discards (Sec. 1, 3.2).
3. A cluster-level energy built from raw logits therefore measures inherent uncertainty (Eq. 18–19).
4. Energy outperforms semantic entropy overall (Table 1) and where semantic entropy is constant (Table 2).
∴ Logit-based energy is a better hallucination detector because it captures uncertainty that probability-based entropy cannot.

---

## Strongest Counter-Argument
The evidence supports a much weaker conclusion than the thesis. The thesis is a *mechanism* claim, that logit intensity (versus normalised probability) carries the missing information. The experiments cannot isolate that mechanism for three reasons, all visible in the paper.

First, Table 2's headline compares energy with a constant. Semantic entropy is "always zero" in the K=1 regime, so its AUROC is exactly 50.0%; any non-constant per-response scalar (mean token log-probability, response length, max logit) would show a ">13%" gain. The comparison says nothing about logits versus probabilities.

Second, outside K=1 the authors' own ablation points against the mechanism. In Fig. 3, single-response energy without clustering reaches AUROC 69.1 and 63.0. The semantic-entropy numbers for the same Qwen3-8B datasets in Table 1 are 69.6 and 71.6. Logit scoring on its own is equal to or worse than the probability-based baseline; improvement arises only once logits are combined with cluster aggregation, and Eq. 18–19 aggregate by dividing a member sum by n (not by cluster size), which makes the cluster score partly a function of cluster frequency, the same information semantic entropy uses.

Third, the baseline in Eq. 6 is an unnormalised sequence probability, while energy is length-averaged (Eq. 19): a length-normalisation confound that the paper does not control.

A skeptical reader can therefore explain every reported gain as "length-normalised, frequency-aware cluster scoring", with nothing special about logits. If the authors compared a length-normalised log-probability version of the same cluster aggregation, the mechanism claim would stand or fall cleanly. Until then the title's "beyond entropy" and the claim to capture inherent uncertainty are not demonstrated. This is fixable by re-scoring cached samples, so the issue is MAJOR rather than CRITICAL: the evidence supports the weaker claim "a logit-based cluster score beats this semantic-entropy baseline on two QA sets".

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core empirical claim (energy outperforms the stated semantic-entropy baseline on the reported sets) survives; the issues below concern what it proves, and each is fixed by narrowing the claim or adding controls on existing samples. Protocol sweep: no statement of training, tuning or selection on a reported test set appears in the paper (nothing is trained; k·τ = 1 "by default"); criterion 3 is not triggered, and the missing selection protocol is a question, not a defect.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | Table 2; Fig. 3 vs. Table 1; Eq. 6 vs. Eq. 19; Eq. 18 | Mechanism not isolated: constant baseline in K=1; single-response energy 69.1 vs. SE 69.6 and 63.0 vs. 71.6; length-normalisation and cluster-frequency confounds. Evidence supports a weaker claim | Grid {prob, logit} × {length-normalised, not} × {mass, mean} plus non-semantic and discrete-SE baselines |
| DA-M2 | Scope / Overclaiming (E5) | Abstract; Sec. 4.2; Sec. 1 | "significantly improves" (no test); "consistently" / "robustness" (2 models, 2 datasets); "better calibration" (no calibration metric); "downstream applications such as hallucination detection" (detection is the task); "more than 13%" is points over chance | Narrow wording; add CIs and a calibration metric or drop the claim |
| DA-M3 | Logic | Sec. 3.2.1 ("assume Zt is constant"); Sec. 6 ("invariant to the scale of the logits"); Eq. 14–16; Liu et al. 2020 | Theory not connected to the score: Z_t assumed away; softmax is shift-invariant, not scale-invariant, so absolute logits are unconstrained; Bayesian derivation unused; "energy" is a sampled-token logit rather than the log-sum-exp free energy of the cited OOD work [verify] | Test the free-energy variant; correct Sec. 6; trim Sec. 3.2 |
| DA-M4 | Evidence / Reproducibility | Sec. 4.1; Table 1 | n, temperature, clustering model, correctness judge, scored cluster, K=1 share absent; Table 1 not decomposed by K; unknown how much of Table 1 is the K=1 effect | Full protocol; split Table 1 into K=1 and K>1 |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of naming | Sec. 4.1/4.3.2/Fig. 3 | CSQA vs. CSimpleQA; Qwen-8B vs. Qwen3-8B |
| DA-m2 | Citation | Bibliography (Kuhn et al.) | "Nature, 2024" for a paper with an arXiv v1 of 2023-02-19 |
| DA-m3 | Presentation | Eq. 19 | Left side U(x^(i)) with the sum over x^(i) in C_k |
| DA-m4 | Evidence | Fig. 2 | Think-mode result stated as "consistent with the observations in Table 1" without numbers (figure not visible to me; unverifiable) |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Average AUROC gain in K=1 (Sec. 1, 4.3.1) | "more than 13%" | (16.7 + 12.1 + 8.9 + 15.8)/4 = 13.375 | Yes (points, vs. 50.0 constant) |
| Table 1, Qwen3-8B CSQA AUROC | ⇑4.5% | 76.1 − 71.6 = 4.5 | Yes |
| Table 1, ERNIE TriviaQA AUROC | ⇑5.9% | 81.0 − 75.1 = 5.9 | Yes |
| Table 2, ERNIE CSQA AUROC | ⇑8.9% | 58.9 − 50.0 = 8.9 | Yes |
| Table 2, Qwen3-8B CSQA FPR95 | ⇑14.7% | 95.0 − 80.3 = 14.7 | Yes |
| "nearly half … incorrect" (Sec. 3.1) | nearly half | 100 − 55.8 = 44.2% (Qwen3-8B CSQA, if AUPR = share correct); 24.9, 23.0, 14.1% elsewhere | Partly (true for one cell; "some datasets") |
| Fig. 3(c),(d) vs. Table 1 energy (Qwen3-8B) | 74.8, 76.1 | 74.8, 76.1 | Yes (suggests Fig. 3 is Qwen3-8B) |
| Single-response energy vs. SE (Fig. 3a,b vs. Table 1) | n/a | 69.1 − 69.6 = −0.5; 63.0 − 71.6 = −8.6 | Energy w/o clusters ≤ SE |

## Ignored Alternative Explanations
- Length normalisation (baseline unnormalised, energy averaged) rather than logits.
- Cluster size/frequency encoded through the n-normalised cluster sum (Eq. 18–19).
- Template tokens: responses are full sentences (Fig. 1), so the token average is dominated by boilerplate tokens whose logits say little about the answer.
- Entity-popularity/token-frequency effects on logit magnitude (a larger logit for frequent tokens) rather than "epistemic" state.
- Clustering and correctness-labelling noise (unspecified), and the K=1 subset's different base rate (AUPR 55.8% vs. 53.6% overall).
- Selection effects of conditioning on K=1 (the subset depends on the sampler).

## Missing Stakeholder Perspectives
Practitioners using API-only models (no logits), users making safety-relevant decisions from a detection score without a calibrated threshold, and non-English/low-resource settings beyond a single Chinese QA set.

## Observations (Non-Defects)
- All 24 reported deltas recompute; the text quotes them accurately.
- Table 2 is an honest and useful diagnostic, and Sec. 6 openly says logits are not strictly energy.
- The literature check found no uncited prior work covering every central claim (claim profile: C1 medium, C2 medium, C3 high), so the novelty challenge is limited to differentiation from the cited LogTokU, not "known results".

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Mechanism confounded; theory not linked |
| Clarity & Presentation | 58 | Readable; definition gaps |
| Novelty & Originality | 46 | Medium per claim profile |
| Significance & Impact | 44 | Narrow |
| Experimental Validation | 36 | One baseline, no variance |
| Reproducibility | 38 | Protocol absent |
| Ethical Compliance | 62 | Nothing at stake |

**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison is against a constant, and the paper's own ablation undercuts the mechanism claim.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R4 | "No limitations discussion" (draft) | dropped | Sec. 6 discusses limitations; replaced by "partially" in Limitations Assessment |
| R2 | "Farquhar et al. already acknowledge consistent errors" (draft) | dropped | Could not be matched to a retrieved abstract; stating prior-work content from memory violates the novelty-statement rule |
| R3 | "No ethics/broader-impact statement" (draft) | moved to Minor | No ethics-relevant content; kept as a one-line remark |
| R4 | "Fig. 2 uninterpretable" (draft) | rewritten | Figure unavailable: recorded as unverifiable (DA-m4), not an author fault |
| R2-W4 | Citation point (ii) | rewritten as a question | Cannot show the cited works fail to support the sentence |
| R1-W3 | Protocol absent | kept | Verified by a text sweep; not answered in the paper |
| DA-M3 / R2-W3 | "Energy ≠ free energy of Liu et al." | kept, marked `[verify]` | Rests on the reviewers' recollection of Liu et al. 2020, not on a retrieved abstract |
Weaknesses were reordered by severity in all reports; scores unchanged.

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer Part A: merged issue list
| Issue | Source IDs | Class |
|-------|-----------|-------|
| I1. Mechanism not isolated (logits vs. length normalisation vs. frequency); constant baseline | R1-W1, R1-W2, R2-W2, R4-W3, DA-M1 | CONSENSUS-4 (hinge) |
| I2. Theory–score gap (Z constant, shift invariance, "energy" ≠ free energy) | R1-ERR-3, R2-W3, R3-W1, R4-W1, DA-M3 | CONSENSUS-4 |
| I3. Protocol under-specified, no variance | R1-W3, R1-W4, R4-W1, DA-M4 | CONSENSUS-3 (hinge) |
| I4. Narrow scope / one baseline | R1-W4, R3-W2, R4-W3, DA-M4 | CONSENSUS-4 |
| I5. Overclaiming wording | R1-ERR-2, R4-W2, DA-M2, R3-W3 | CONSENSUS-3 |
| I6. Thin differentiation from LogTokU | R2-W1 | SOLO |
| I7. Citation errors | R2-W4, DA-m2 | CONSENSUS-2 |
| I8. Significance of the K=1 diagnostic | R3-S2 positive vs. R1-W2/DA-M1 | SPLIT |
| DA-CRITICAL | none raised | – |

Official score (script `scores_before.json`, DA issues provisional; none raised): see Score Summary.

## EIC Meta-Review (Dr. Halvard Osei-Lindqvist)

### The Case For and Against
- **For acceptance:** A clean, cheap idea that targets a real, well-motivated blind spot of the standard sampling-based detector. Table 2 is a useful diagnostic, the gains are positive in every cell, the arithmetic is exact, and the authors are candid about the physics (Sec. 6).
- **Against acceptance:** The central mechanism claim is not isolated: the baseline is one unnormalised semantic-entropy variant, the K=1 headline compares with a constant, and the authors' own Fig. 3 shows non-semantic logit scoring on par with or worse than that baseline. The protocol (n, clustering, judging, scored cluster) is unstated, there is no variance, and the evidence is two short-form QA sets. The theory does not drive the score.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Single-response energy 69.1/63.0 vs. SE 69.6/71.6 | R1-W1, DA-M1 | Fig. 3a,b; Table 1 | Verified | Fig. 3 caption names no model; the identical 74.8/76.1 energy values tie it to Qwen3-8B (inference, plausible) |
| SE is constant in K=1; AUROC exactly 50.0 | R1-W2, DA-M1 | Sec. 4.3.1; Table 2 | Verified | "always zero" |
| Baseline unnormalised (Eq. 6) vs. energy length-averaged (Eq. 19) | R1-ERR-1, DA-M1 | Eq. 6, 17, 19 | Partly correct | Definitions differ as written; what was actually run for the baseline is not stated |
| Cluster sum divided by n encodes frequency | R1-W1, DA-M1 | Eq. 18–19 | Verified | |
| Protocol items absent (n, clustering, judge, scored cluster, seeds) | R1-W3, DA-M4, R4-W1 | Sec. 4.1 | Verified | text search; no appendix provided |
| "better calibration" unsupported | R1-ERR-2, DA-M2 | Sec. 4.2 | Verified | no calibration metric |
| "invariant to the scale of the logits" is shift-invariance | R1-ERR-3, R3-W1 | Sec. 6 | Verified | softmax(z+c) = softmax(z) |
| "energy" differs from the free energy of Liu et al. | R2-W3, DA-M3 | Eq. 19; Sec. 1 | Partly correct | Paper's own Eq. 19 is clearly a sampled-token logit; the comparison to Liu et al. rests on prior knowledge, kept `[verify]` |
| Weak differentiation from LogTokU; not run | R2-W1 | Sec. 1, 4.3.3 | Verified | LogTokU is cited and used only as an idea; not a baseline |
| Bibliography venue for Kuhn et al. | R2-W4, DA-m2 | References | Verified | "Nature, 2024"; arXiv v1 dated 2023-02-19 |
| No downstream application experiment | R3-W3, DA-M2 | Abstract; Sec. 5 | Verified | |
| All 24 table deltas recompute | R1, DA | Tables 1–2 | Verified | |
| Integrity: reviewer-directed text | scan | whole text | none found | no effect on any score |
Literature-ledger checks: the missing-comparison weaknesses rest on prior work (Kernel Language Entropy, probes, benchmarks), so they stand at MAJOR, not CRITICAL; concurrent preprints (SRE, TECP) are "discuss only" and play no role in the decision. No text overlap flag.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Every Error Log entry checks out at its location; the Fig. 3 cross-reference is the most decisive finding; one entry (baseline normalisation) is medium-confidence |
| R2 (Domain) | 3 | 4 | 1.0 | Sound and mostly verified; the free-energy point rests on recollection and is flagged |
| R3 (Perspective) | 3 | 3 | 1.0 | Fair, constructive; the shift-invariance point is verified; lower confidence outside home field |
| R4 (Generalist) | 3 | 4 | 1.0 | Typical, accurate review; well calibrated to ICLR |
| DA | 2 | 4 | 1.0 | Strongest counter-argument survived my check, but its Overall of 2 leans on points I rate MAJOR-fixable; no weight change |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |
(Ceiling: none. I checked the DA's MAJOR issues against the criteria: none shows evidence that contradicts the main claim, a test that cannot measure the claim, leakage, fabrication or an ethical issue; they support a narrower claim.)

### Final Decision and Justification
The reviewer ratings (2, 3, 3, 3, 2) give an official mean of 2.60 and an EIC-weighted starting point of 3 (rounded half up from about 2.56, which is near the 2.5 boundary; I keep 3 because the pool position evidence below puts the paper just under the borderline band, in the range of a typical rejected submission). The 0–100 cross-check (EIC composite 49.2, official 49.5) sits in the Reject band (35–49 by the decision mapping) while the rating points to 3; the script flags this one-step difference. It is within 1 point of the 50 band edge, the reviewers' low dimension scores are already reflected in their Overall ratings, and I cannot name a verified issue the ratings missed, so I treat it as a borderline signal and keep the starting point rather than depart. If the authors' controls (Priority 1) came back against the mechanism claim, the composite would be the better guide and the paper would be a 2. The decisive evidence is that the central mechanism claim is not separated from normalisation and cluster-frequency effects (Fig. 3 vs. Table 1; Eq. 6 vs. Eq. 19), the comparison set is a single baseline, and the protocol is unstated. These are fixable on cached samples, which keeps the paper from a Reject (2), and there is no upheld DA-CRITICAL ceiling. **My pool position: better than about 42% of ICLR submissions.** Deciding evidence: a reasonable and useful idea whose present evidence is below the bar of accepted ICLR papers (one baseline, two short-form sets, no variance, unstated protocol), but with a real, regime-specific signal (Table 2) that a revision could substantiate. **Final Overall: 3** (Borderline Reject; typical rejected submission, strong revision path).

---

## Editorial Decision

**Paper:** Semantic Energy: Detecting LLM Hallucination Beyond Entropy · **Date:** 2026-11-05 · **Target Venue:** ICLR | **Paper Type:** empirical

### Decision: Borderline Reject (3), how a careful panel would likely see this draft (simulation, not a prediction)

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60 · official composite 49.5
**EIC assessment** (internal): weighted rating 2.56 → starting point 3 · weighted composite 49.2 → band 2 (cross-check, ⚠ one step lower, within 1 point of the band edge) · **DA ceiling:** none · **Final (EIC):** 3
**ICLR rating (secondary scale status):** 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Soundness 2 / Presentation 2 / Contribution 2

### Score Summary
Script runs: `before.json` (official, no EIC weights, DA provisional; none raised) and `aggregate.json` (EIC weights R1 1.25, others 1.0; `--final 3 --venue iclr`).

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------|--------|
| Technical Rigor | 44 | 50 | 54 | 52 | 42 | 48.4 | 48.0 | 12 |
| Clarity & Presentation | 62 | 60 | 62 | 60 | 58 | 60.4 | 60.4 | 4 |
| Novelty & Originality | 48 | 50 | 54 | 50 | 46 | 49.6 | 49.4 | 8 |
| Significance & Impact | 45 | 50 | 56 | 52 | 44 | 49.4 | 49.0 | 12 |
| Experimental Validation | 38 | 44 | 48 | 46 | 36 | 42.4 | 42.0 | 12 |
| Reproducibility | 36 | 42 | 45 | 42 | 38 | 40.6 | 40.2 | 9 |
| Ethical Compliance | 65 | 65 | 66 | 64 | 62 | 64.4 | 64.4 | 4 |
| **Composite** | | | | | | **49.5 (before)** | **49.2 (after)** | no spread > 20 |

(EIC weighted values are from `aggregate.json`.) The script raised no consistency warnings.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Semantic Energy: Detecting LLM Hallucination Beyond Entropy" to ICLR. Estimating when LLMs hallucinate is an important problem, and the blind spot of semantic entropy that you target is real.

**Overall Assessment:** The panel found the idea simple, cheap and clearly motivated, with consistent gains in every reported cell. It was not convinced the current evidence supports the mechanism you claim, and it found the experimental protocol too thin to interpret or reproduce.

**Key Strengths Identified by Reviewers:**
1. A sharp, well-illustrated failure case of semantic entropy and a diagnostic on the exact regime where it fails (Table 2) (R1, R2, R3, R4).
2. A drop-in score at no extra sampling cost with consistent positive deltas (all 24 recompute) (R1, R4).
3. Candid discussion that logits are only "energy-like" (Sec. 6) (R2, R3, R4).

**Key Concerns Requiring Attention:**
1. The gain is not attributed to logits: single-response energy matches or trails semantic entropy in your Fig. 3; length normalisation and cluster frequency are uncontrolled; Table 2 compares against a constant (CONSENSUS-4).
2. One baseline and two short-form QA sets, no variance; stronger entropy/kernel/probe baselines and LogTokU are missing (CONSENSUS-4).
3. Missing protocol details (n, clustering, correctness judge, scored cluster) (CONSENSUS-3).
4. The Boltzmann derivation does not drive the score; the partition-function assumption and the "scale" statement need correction (CONSENSUS-4).

**Devil's Advocate:** No CRITICAL issue was raised. The DA's strongest objection (the mechanism is unproven and a weaker explanation fits the data) is addressed by the first Priority 1 item.

**Decision: Borderline Reject (3).** With the controls on existing samples, a fuller baseline set, a stated protocol with confidence intervals and corrected theory, the paper could become a solid contribution; in its present form the reasons to reject narrowly outweigh the reasons to accept.

Please refer to the Revision Roadmap below.

Sincerely,
Dr. Halvard Osei-Lindqvist
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Mechanism not isolated; baseline set thin | R1, R2, R4, DA | CONSENSUS-4 |
| Theory–score gap | R1, R2, R3, R4, DA | CONSENSUS-4 (+ R1's Error Log) |
| Narrow scope | R1, R3, R4, DA | CONSENSUS-4 |
| Protocol under-specified | R1, R4, DA | CONSENSUS-3 |
| Overclaiming wording | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Value of the K=1 diagnostic (Table 2) | R3 (transferable insight) | R1, DA (vs. a constant; uninformative about logits) | Both right: a good diagnostic, but its headline number is not evidence for the mechanism; ask for the best non-semantic scorer as the K=1 comparator |

### Score Spread Discussion
Spreads are listed in the script output (Score Summary appendix). Largest are Technical Rigor and Experimental Validation (R3 more lenient; R1/DA stricter). I adopt the stricter view on rigor because Fig. 3 vs. Table 1 is verified in the text, and the lenient view on Significance because a regime-specific signal exists.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Mechanism not isolated | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Overclaiming wording | Yes (R1, R4, R3) | n/a | n/a |
| DA-M3 | MAJOR | Theory not linked to score | Yes (R1, R2, R3, R4) | n/a | n/a |
| DA-M4 | MAJOR | Protocol/K-split absent | Yes (R1, R4) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Isolate logit vs. length-normalisation vs. cluster frequency | R1-W1, DA-M1 | Eq. 6/18/19; Fig. 3; Table 2 | Grid {prob, logit} × {length-normalised, not} × {mass, mean/discrete}; non-semantic scorers; K=1 comparator = best non-semantic score | Low–Med; < 5 GPU-h if samples cached | Yes |
| R2 | Stronger baselines (kernel language entropy, token-level length-normalised entropy, LogTokU, free-energy variant) | R1-W2, R2-W1, R2-W2 | Sec. 4.1; Table 1–2 | Add rows on the same samples; adopt a published UQ benchmark protocol | Med; ~20 GPU-h for baselines needing re-sampling | Partly |
| R3 | Full protocol + uncertainty | R1-W3, R1-W4, R4-W1, DA-M4 | Sec. 4.1 | State n, sampling settings, clustering, judge, scored cluster, K=1 share; Table 1 split by K; paired-bootstrap CIs; sampling seeds | Low–Med; ~10 GPU-h | Yes |
| R4 | Scope matched to claims | R1-W4, R3-W2, R4-W3 | Sec. 4; abstract | Add ≥ 1 further model family and one longer-form set, or narrow wording ("two models, two short-form QA sets") | Med–High; 30–60 GPU-h | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Theory–score gap: Z constant; shift-vs-scale; "energy" naming | R1-ERR-3, R2-W3, R3-W1, DA-M3 | Correct Sec. 6; test log-sum-exp variant; shorten Sec. 3.2 or justify | Low–Med | Yes |
| S2 | Differentiate from LogTokU | R2-W1 | Delta paragraph and empirical comparison | Low–Med | Yes |
| S3 | Overclaims: "significantly", "robustness", "calibration", "downstream" | R1-ERR-2, R4-W2, R3-W3, DA-M2 | Reword or add tests/ECE/selective-prediction experiment | Low | Yes |
| S4 | Missing references (Critical/Important lists of R2) | R2 | Cite and discuss | Low | Yes |
| S5 | Citation fixes (Kuhn et al. venue; Fu/Zhang support) | R2-W4, DA-m2 | Correct entries | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Deployment: white-box requirement, cost, threshold transfer | R3-W2 | Limitations paragraph; coverage–accuracy curve |
| N2 | Connections: evidential learning, conformal, confidence-regulation neurons | R3-W4 | Discuss |
| N3 | Naming/notation (CSQA vs. CSimpleQA, Qwen-8B, T overload, Eq. 19 binding, "partial function") | R1, R4, DA-m1/m3 | Harmonise |
| N4 | Fig. 1/Fig. 2 clarity; give the numbers for Fig. 2 | R4, DA-m4 | Table the think-mode result |

## Estimated Revision Effort
- Priority 1: 4 items, about 1–2 weeks (most on cached samples; scope item is the largest)
- Priority 2: 5 items, about 3–4 days
- Priority 3: 4 items, about 1 day
- **Total estimated revision time**: about 2–3 weeks

---

*A literature check was run (strict, cutoff 2025-09-24; 6 logged queries plus an empty expansion query; arXiv only; gap left open: nothing kept from 2021 beyond a verified pointer). Reviewer personas are fictional. This is a simulation of a careful panel's view of this draft, not a prediction.*

## Target-venue scores (ICLR; scale status: secondary: "Recent forms use…; verify against the current form")
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) for final Overall 3 |
| Official mean rating (raw) | 2.60 (internal 1–6 scale) |
| EIC-weighted rating | 2.56 (internal 1–6 scale) |
