# Simulated Panel Review: "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG"

*Simulation of how a careful panel would likely see this draft; not a prediction of any real decision. Date: 2026-11-10. Request: target venue ICLR, full review, confirmation skipped, literature check strict (cutoff 2025-09-24). Figures were not available (text extraction only): figure-dependent claims are judged from captions and surrounding text. The five reviewers are five role-based passes sharing one model context; they are not independent agents. Supplement: none referred to; the appendix (Tables 3–9, Figures 4–5) is in the file.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG |
| Primary Discipline | Machine learning → mechanistic interpretability → circuit discovery in language models |
| Secondary Discipline(s) | Statistics (resampling, estimator stability); causal mediation analysis |
| Paper Type | Analysis/Insight (composite weights: analysis) |
| Core Technique(s) | Edge attribution patching (EAP, EAP-IG inputs/activations, clean-corrupted), bootstrap resampling, Jaccard index of edge sets, noise injection |
| Target Venue | ICLR (stated); profile key `iclr`, 2026 cycle, scale status secondary |
| Venue-Specific Notes | None (no declared contribution type). ICLR submissions are public and revisions can be uploaded during discussion |
| Paper Maturity | Submission-ready in form, early in substance (formatted as a preprint; no limitations section) |
| Ethics-Relevant Content | None (no human data, no deployment risk) |

### Claimed Contributions (as stated by the authors; ids used by the literature check)
1. **C1** (problem/framing): circuit discovery "should be viewed as statistical estimators, subject to questions of variance and robustness" (Abstract; §1; §3).
2. **C2** (result): EAP-IG circuits "exhibit high variance under data resampling" and are "sensitive to hyperparameter choices" (§1; §5.1; §5.2; Table 1; Tables 3–9).
3. **C3** (method): injecting noise into the causal analysis is a useful stability stress test; "A noise level of 0.2 seems to be a good starting point for gpt2-small" (§5.3; §6).
4. **C4** (recommendation): report bootstrap stability metrics routinely, justify hyperparameters, use noise checks (§6).

### Paper memory (factual record shared with all reviewers)
- **Setup:** tasks IOI, Subject-Verb Agreement (SVA, own grammar-based generator), Greater-Than (§4). Models gpt2-small, Llama-3.2-1B, Llama-3.2-1B-Instruct (§4). Circuit stopping rule: start with n = 30 edges by absolute score, grow to 2000 "until a path from input to output is found"; otherwise "no faithful circuit is found" (§3.1). D_eval = D, i.e. circuit metrics are computed on the discovery data (§3.2). Metrics: circuit error (prediction mismatch with full model), KL, pairwise Jaccard of edge sets, reported as µ, σ², CV (§3.2).
- **Not stated after text search (no supplement is referenced):** number of examples per dataset, number of bootstrap replicates or runs, seeds, IG steps m, the default EAP variant and hyperparameters used for the bootstrap/meta-dataset/paraphrase experiments, how non-circuit edges are treated when evaluating M_C, noise direction and which inputs receive noise, compute, a limitations section, a code link (the text says "Our publicly available codebase", §6).
- **Headline numbers:** Table 1 averages (bootstrap Jaccard 0.561, CV 0.335, CErr 0.440; meta-dataset Jaccard 0.790; paraphrase Jaccard 0.799); Table 2 Jaccard-to-median ranges (Greater-Than 0.086–1; IOI 0.071–1).
- **Appendix:** Tables 3–5 per-model aggregates; Tables 6–8 hyperparameter tables for Llama-3.2-1B and gpt2-small and KL for Table 2; Figure 4 heatmap; Figure 5 CV vs noise; Table 9 noise plots.
- **Unverifiable:** all figures (Figures 1–5) as images; the "median circuit" construction rule (not defined in text).
- **Integrity scan** (`integrity_scan.py`): no reviewer-directed text or hidden characters found; reviewers read the redacted copy (identical to the original).

## Literature check (Phase 1.5, mode: strict, cutoff 2025-09-24)
Run through `related_search.py`: 6 search queries (5 claim-driven for C1–C3, 1 expansion), 62 kept results, `similarity`, `novelty`, `coverage` and 3 `verify` calls. No baseline-purpose query was run because the benchmarks (IOI, SVA, Greater-Than) are task datasets from earlier circuit papers, not leaderboards. Open gap: no query for "stability selection / feature-selection stability" (arXiv hits for statistical queries were dominated by physics papers). The search covers arXiv only; "no close prior work found" is a limit of the search, not evidence of novelty. Closest prior works by similarity (all prior): *Have Faith in Faithfulness* (cosine 0.348; already cited by the paper as the EAP-IG source), *EAP-GP* (0.345; a new attribution method, not a stability study), *Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability* (0.198). No text overlap (0 shared 8-grams).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valdemar, senior faculty, public research university (Northern Europe)
- **Seniority / Expertise**: Senior / statistical learning, interpretability evaluation, area chairing at ML conferences
- **Role**: Reads all five reviews, checks decisive points, weights reviewers, decides
- **Style**: Rewards honest, well-scoped empirical findings; unmoved by framing language the experiments don't carry

### Reviewer 1 (Methodology): Dr. Tomasz Veldkamp, industrial research lab (Europe)
- **Seniority / Expertise**: Mid-career industry scientist / activation patching and circuit evaluation protocols; resampling statistics
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; asks what the reference scale of each metric is

### Reviewer 2 (Domain): Prof. Aiyana Whitcombe, interpretability group, large public university (North America)
- **Seniority / Expertise**: Senior faculty / transformer circuits, causal mediation, circuit-discovery benchmarks
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks that prior work is described as its abstract describes it

### Reviewer 3 (Perspective): Dr. Lucía Ferraro-Okonkwo, statistics and causal-inference department, university (South America)
- **Seniority / Expertise**: Mid-career / uncertainty quantification, stability selection, reproducibility of scientific findings
- **Review Focus**: Cross-disciplinary connections, deployment of findings, assumptions, broader impact
- **Style**: Constructive; reads weaknesses as opportunities

### Reviewer 4 (Generalist): Dr. Mei-Ling Dornbusch, ML lab, research university (East Asia)
- **Seniority / Expertise**: Postdoc-to-assistant professor / language-model analysis, not circuit methods specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: The typical program-committee member; asks "what do I learn that I can use?"

### Devil's Advocate: Prof. Samir Haldorsen, department of statistics, university (Europe)
- **Seniority / Expertise**: Senior / estimator theory, identifiability, evaluation methodology
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, fair; frames objections as questions

*Personas are fictional. Assumptions stated: venue ICLR (given), paper type analysis (the paper also argues a position, but its evidence is an empirical case study).*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Reviewer: Dr. Tomasz Veldkamp, Reviewer 1 (Methodology) (industrial research lab, Europe; fictional persona)
## Expertise: activation patching and circuit evaluation; resampling statistics; faithfulness metrics
## Date: 2026-11-10

---

## Summary
The paper treats a circuit-discovery pipeline as an estimator and measures how much its output changes when the discovery data are bootstrapped, redrawn from the same generator, paraphrased, or when pipeline choices and embedding noise are altered. Using EAP and three EAP-IG-style scorers on IOI, Subject-Verb Agreement and Greater-Than, with GPT-2 small and Llama-3.2-1B (base and Instruct), it reports pairwise edge-set Jaccard between circuits and a "circuit error" against the full model. It concludes that bootstrap resampling gives low Jaccard (0.561 averaged), that configurations disagree widely (Table 2), and that moderate noise (0.2) exposes instability, and it recommends routine stability reporting.

## Strengths

### S1: A real and under-measured question, asked with a simple, usable protocol
Bootstrapping the discovery set and reporting the mean pairwise Jaccard of edge sets (§3.2–3.3) is cheap and transferable. Circuits are usually reported as single point estimates; showing that the output moves is a useful reminder (§1, §6).

### S2: Several kinds of perturbation are separated
Sampling variance (bootstrap, meta-dataset), prompt form (paraphrase), pipeline choices (Table 2, Tables 6–8) and intervention noise (§5.3) are distinguished in §3.3, which is a sensible decomposition even if the conditions are not matched (see W2).

### S3: Reported aggregates are arithmetically consistent
I recomputed the Table 1 means from Tables 3–5: bootstrap circuit error 0.439 (reported 0.440), bootstrap Jaccard 0.5625 (0.561), meta-dataset 0.299 and 0.790, paraphrase 0.148 and 0.800. The reported CV values also agree with σ²/µ in the appendix (e.g. Table 3, Llama-3.2-1B Greater-Than: σ = 0.0216, CV = 0.10).

### S4: Honest disclosure of D_eval = D and of cases where no circuit was found
§3.2 states that circuit metrics are evaluated on the discovery data, and Figure 2 marks that no faithful circuits were found for Greater-Than on gpt2-small. Both are things authors often omit.

## Weaknesses

### W1: Jaccard on variable-size circuits mostly measures size mismatch, so "variance" is not isolated (§3.1, §3.2, Tables 2, 6, 8)
The stopping rule grows n from 30 up to 2000 edges "until a path from input to output is found" (§3.1), so every circuit has whatever size that rule yields. Circuit sizes in Table 2 range from 3 to 33 edges and in Table 6 from 5 to 448. In Table 6 (IOI) the clean-corrupted circuit has 448 edges and Jaccard 0.016 to the median; with a 7-edge median this equals 7/448 = 0.0156, i.e. exactly the bound for a circuit that contains the median. The EAP-IG-activations circuit (117 edges) gets 0.042 = 5/119. Low Jaccard here reflects size, not disagreement on which edges matter. The same applies to Table 2 IOI, where sizes of 3–12 edges against a median of 6 edges (inferred from Jaccard 1.000 rows of size 6) give values as low as 0.071. Table 1 averages pairwise Jaccard across circuits whose size is never reported for bootstrap runs.
- **Suggested Fix:** Report circuit size distributions per condition; recompute stability at a fixed edge budget k (top-k for several k) and with a size-insensitive statistic (overlap coefficient |A∩B|/min(|A|,|B|), per-edge inclusion frequency). Cost: no new model runs beyond the existing scores if edge scores were saved; otherwise about one GPU-day for 100 bootstrap replicates × 3 tasks × 3 models.

### W2: The perturbation conditions are not like-for-like, and Table 1 mixes different cells (§5.1, Table 1, Tables 3–5)
Paraphrasing is not run for SVA (§4), so Table 1's paraphrase row averages 5 cells while bootstrap and meta-dataset average 8; the omitted SVA cells include Llama circuit error of 0.75–0.80 and a degenerate GPT-2 Jaccard of 1.00. The circuit-error gap (0.440 vs 0.150) is therefore partly composition. On the five shared cells (Greater-Than ×2 Llama, IOI ×3) I get bootstrap circuit error 0.376 and Jaccard 0.43, meta-dataset 0.164 and 0.75, paraphrase 0.148 and 0.80, so the ordering survives, but the printed numbers are not comparable. More basically, a bootstrap of the original dataset and a fresh draw from the generator should show similar sampling variance if the original data are i.i.d. from that generator. The large gap (Jaccard 0.56 vs 0.79) points to a small original dataset, duplicated examples in resamples (about 63% unique), or a generator mismatch, none of which can be examined because the dataset size and replicate count are not stated.
- **Suggested Fix:** Average only over common cells (or report per cell); state N and the number of replicates; add a stability-versus-N curve (e.g. N ∈ {50, 100, 200, 400}) and a subsample-without-replacement control.

### W3: The operating point is non-standard and mostly non-functional, which limits what "EAP-IG is unstable" means (§3.1, §5, Tables 2, 3, 7)
By the authors' definition a "faithful circuit" is one in which a path exists; yet Llama circuits for IOI have circuit error 0.66–0.69 and for SVA 0.75–0.80 (Table 3; Table 2), meaning they disagree with the full model on most inputs. Variance of a minimal connected path through a noisy edge ranking is expected to be large; it says little about EAP-IG used at a faithfulness threshold. I could not confirm that this stop rule matches standard EAP-IG practice, and I read the original practice as reporting a sweep over the number of edges with a faithfulness target. The authors say they follow the original procedure (§3.1) but give no reference to where the path rule appears.
- **Suggested Fix:** Repeat the key experiment with n chosen to reach a fixed faithfulness (for instance 85% of the full-model logit difference) and at several fixed n; report whether Jaccard stability changes.

### W4: The circuit-performance metric looks insensitive to the circuit, and it is undefined how M_C is evaluated (§3.2, Tables 2, 7, 8)
In Table 7, Greater-Than circuits of 23, 17, 10, 16 and 16 edges all report circuit error 0.20 and KL 6.4·10⁻⁷; IOI circuits of 3, 12, 6, 7 and 9 edges all report 0.69 and 9.1·10⁻⁶. In Table 8 (gpt2-small SVA) a 1-edge and a 21-edge circuit both have KL = 0. A KL of order 10⁻⁷–10⁻⁵ next to circuit error 0.20–0.69 is also hard to reconcile. §3.2 never says what non-circuit edges are replaced with when M_C is run (zero, mean, corrupted input) and, from Table 2, circuit error also seems to depend on the intervention type. Until this is clarified I cannot tell whether circuit error measures anything about the circuit.
- **Suggested Fix:** Define M_C precisely (ablation applied to excluded edges); show faithfulness-versus-size curves for each condition; add random same-size circuits as a floor and the full model as a ceiling.

### W5: No reference scale or null for "high" variance (§5.1, §6, Fig. 1)
A Jaccard of 0.56 cannot be called high without a baseline: random circuits of equal size, a different method (ACDC, edge pruning, top-k EAP at the same k), or a second independent estimate of the same quantity. The abstract's "high structural variance" and §5.1's "critical vulnerability of the method" are stated without any comparison. Fig. 1's claim that "none of the tested EAP methods consistently yields circuits with lower variance" compares only within the EAP family.
- **Suggested Fix:** Add random-circuit and at least one non-EAP baseline; report bootstrap confidence intervals of the mean Jaccard, not only pairwise variances.

### W6: Pairwise statistics and the CV are not appropriate variance estimates (§3.2, Tables 1, 3–5)
With N circuits there are N(N−1)/2 pairs that share circuits, so the pooled pairwise Jaccard distribution is not an i.i.d. sample; σ² and CV across pairs describe the spread of pairwise similarity, not the sampling variance of the circuit. The CV of a [0,1]-bounded similarity blows up when the mean is small and is not comparable between cells (Llama IOI bootstrap: CV 0.85 and 0.76 drive Table 1's 0.335, while the other six cells lie between 0.00 and 0.36). The multimodality claim for GPT-2 (§5.1) rests on a visual impression of Figure 2 without a test.
- **Suggested Fix:** Use per-edge inclusion probability (stability selection style) and bootstrap CIs of mean pairwise Jaccard with replicate-level resampling; drop CV or report it with the mean.

### W7: Noise experiment is thin, and the recommendation outruns it (§5.3, §6, Figures 3 and 5)
Only gpt2-small and two tasks are used. The Figure 3 IOI circuit-error axis spans about 0.100–0.1125, so the effect of noise on error is about one percentage point; the claim that the averaged CVs peak at a noise amplitude of around 0.2 comes from a plot whose CV axis ends at 0.2 and is averaged over two tasks. "Noise of a controlled amplitude and fixed direction" (§3.3) is a deterministic shift, not noise, and the amplitude has no scale relative to embedding norm, so "0.2" cannot transfer to other models (§6, item 3). §5.3 also refers to "Table 3" for the noise results, but Table 3 is the bootstrap aggregate (E6).
- **Suggested Fix:** Express amplitude relative to embedding norm; use random directions with several draws; add Llama models and SVA; or reduce §6 item 3 to a hypothesis.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | Figure 4 caption vs §5.2 | "circuits found in gpt2-small on the Greater-Than task" | §5.2 says Figure 1 shows "gpt2-small for the IOI task", and Figure 2 says no Greater-Than circuit was found for gpt2-small | Cross-referenced (Fig. 4 caption, §5.2, Fig. 2 annotation) | High | MINOR | State the task of Figure 1 and fix the caption |
| ERR-2 | E6 | §5.3 vs Table 3 caption | "Table 3 shows the effect of increasing noise amplitude" | Table 3 caption: "Aggregated results from Figure 2 for bootstrap resampling" | Cross-referenced | High | MINOR | Refer to Figure 3 / Table 9 |
| ERR-3 | E1 | §5.1 vs Table 1 | "more stable circuits, with higher Jaccard indices (resp. 0.790 and 0.799) and lower CVs" | Circuit-error CV for paraphrasing is 0.134, above bootstrap's 0.123 | Read from Table 1 | High | MINOR | Say "lower CV of the Jaccard index" |
| ERR-4 | E5 | §1 vs §4 | "three tasks and three model architectures" | §4 lists gpt2-small, Llama-3.2-1B and its Instruct variant: two architectures, three models | Cross-referenced | High | MINOR | Say "three models" |
| ERR-5 | E4/E1 | Table 1 | "averaged over tasks and models" | Paraphrase row omits SVA cells; recomputed common-cell means differ (see W2) | Recomputed from Tables 3–5 | High | MAJOR | Report common cells |

**Minor:** the Table 1 paragraph is duplicated almost verbatim in §5.1 (two paragraphs report the same Table 1 numbers, one containing the typo "tields"); Table 2's caption says the median circuit is bold but the median construction is not defined; "EAP-IP" appears in §4 for EAP-IG.

## Missing References
See the Domain review; none added here.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Size-confounded metric, non-standard operating point, undefined M_C (W1, W3, W4) |
| Clarity | 2 | Key protocol items missing (N, replicates, default config) |
| Significance | 2 | Topic matters; evidence for the strong claim is thin |
| Originality | 2 | Bootstrap analysis of one method; statistical framing is not formalised |

## Dimension Scores (0–100)

**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline quantity (Jaccard) is confounded by circuit size and the operating point is non-functional for most Llama cells; the study covers one method on three small tasks.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Size confound (W1), undefined M_C (W4), non-independent pairwise statistics (W6) |
| Clarity & Presentation | 55 | Competent | Readable, but N, replicates and default configuration missing; duplicated paragraph |
| Novelty & Originality | 50 | Developing | Simple bootstrap application; no new estimator or test |
| Significance & Impact | 58 | Competent | Reporting circuit stability is useful if the measurements are sound |
| Experimental Validation | 44 | Developing | No null or baseline, three tasks, one method, noise study on one model |
| Reproducibility | 45 | Developing | Dataset size, replicate counts, seeds, defaults not stated; no code link in the text |
| Ethical Compliance | 62 | Competent | Nothing at stake; no limitations section |

## Questions for Authors
1. What are N, the number of bootstrap replicates and the IG steps m? If N is small (e.g. below 100), my reading of the bootstrap/meta-dataset gap (W2) changes; a stability-versus-N curve would raise my score.
2. How is M_C evaluated, and why do circuits of 10–23 edges have identical circuit error and KL in Table 7? A clear answer showing that the metric responds to circuit content would remove my main doubt (W4).
3. If circuits are re-selected at a fixed faithfulness (or fixed k), does the Jaccard gap between bootstrap and meta-dataset persist? If it vanishes, the headline finding is largely a stop-rule artifact.
4. Which EAP variant and hyperparameters produce Tables 1, 3–5?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. There is no limitations section; D_eval = D is disclosed (§3.2), but the small model scale, single method, three tasks and the non-standard stopping rule are not discussed.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A worthwhile protocol, but the central statistic is confounded by circuit size and the operating point is non-functional for much of the data, so "high variance" is not yet established.

## Confidence
**4**: I recomputed the tables and read the whole text, but could not see the figures.

---

# Peer Review Report

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Reviewer: Prof. Aiyana Whitcombe, Reviewer 2 (Domain) (interpretability group, large public university, North America; fictional persona)
## Expertise: transformer circuits; causal mediation; circuit-discovery evaluation
## Date: 2026-11-10

---

## Summary
The paper argues that circuit discovery is an estimator and demonstrates, for EAP-style edge attribution, that the circuits move under data resampling, configuration changes and injected noise. Its contribution is an empirical case study plus recommendations, positioned as filling a gap where "dedicated studies analyzing the stability of circuit discovery outputs to variations in input data, experimental conditions, or method hyperparameters are scarce" (§2.3).

## Strengths

### S1: Right problem at the right time
The non-identifiability literature (Méloux et al., cited) and metric-robustness work (Miller et al., cited) leave an open question about the sampling behaviour of practical discovery pipelines. A direct measurement on the widely used EAP-IG fits that gap (§1, §2.3).

### S2: Uses the community's standard testbeds
IOI, Greater-Than and SVA with GPT-2 small are the usual circuit tasks (§4), so results are comparable with earlier circuit papers and the data generators are reused (§4).

### S3: The meta-dataset and paraphrase conditions go beyond plain bootstrap
Separating sampling variance from distribution shift (§3.3) is a useful conceptual distinction and echoes the generalisation questions asked of the IOI circuit in earlier work (Wang et al., 2023, cited).

### S4: Related work is mostly accurate and correctly attributes EAP/EAP-IG (§2.1)
The EAP family and its evaluation criteria are described fairly; faithfulness, sufficiency and sparsity are laid out cleanly (§2.2).

## Weaknesses

### W1: The novelty claim that dedicated stability studies are scarce is under-argued, and the closest statistical work is cited only in passing (§2.3)
Shi et al. (2024), cited in §2.2 only for faithfulness, is titled as a hypothesis-testing treatment of circuits, which is the closest existing statistical framing; Méloux et al. (2025) already frame multiple incompatible circuits as non-identifiability; Miller et al. (2024) study robustness of circuit metrics; and an arXiv search (strict, before the cutoff) surfaces *Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability* (Nainani et al., 2024), which tests how the IOI circuit changes across prompt variants, close to the paraphrase condition here. None is differentiated from the present work beyond one sentence. Per-claim novelty from the literature profile: C1 (framing) high by the script but I judge **medium**, since §3.1 adds notation, not an estimand or method; C2 (EAP-IG bootstrap instability) medium (no close prior found in arXiv results; the search is arXiv-only); C3 (noise probe) no close prior found, at most medium.
- **Suggested Fix:** Add a short table distinguishing this work from Shi et al., Méloux et al., Miller et al. and the prompt-variant circuit study on what is varied and what is measured.

### W2: The "statistical estimation" framing is not carried through (Title; §3.1; §6)
An estimator needs an estimand. §3.1 defines C = F_CD(M, D, Λ) but never defines the population-level circuit or the loss for which the estimator's bias or variance is measured, never relates bootstrap variance to the sampling variance of an i.i.d. draw, and gives no uncertainty interval or test. The title and abstract promise a statistical treatment; what is delivered is a descriptive study of Jaccard indices. The established analogue, feature-selection stability (stability selection; stability indices for feature selection), is not mentioned, and neither is the explanation-robustness literature for attributions, which the paper cites only for Adebayo et al. (2018).
- **Suggested Fix:** Either define the estimand and report intervals (per-edge inclusion probabilities with bootstrap CIs), or retitle around "stability analysis" and cut the estimation language.

### W3: Variance is conflated with non-identifiability and redundancy (§5.1, §6)
Different edge sets can implement the same behaviour (backup components are known in IOI; the paper itself notes multimodal Jaccard "echoing the concept of non-identifiability"). Low Jaccard therefore does not show that "a circuit identified from a single dataset may not be representative of the underlying mechanism" (§6). The test that separates the two is functional: do circuits from different bootstrap draws recover the behaviour on each other's data, and does their union or consensus do better? §3.2 explicitly evaluates on D only (D_eval = D).
- **Suggested Fix:** Cross-evaluate each bootstrap circuit on held-out and other-resample data; report faithfulness of the consensus/median circuit.

### W4: Citation characterisations that do not match the cited work (§2.1, §2.3)
§2.1 describes AlphaEdit (Fang et al., 2025) as a variant of causal tracing: the paper's own bibliography lists it as "Null-space constrained model editing for language models", an editing method. §2.1 also lists Sundararajan et al. (2017, integrated gradients) among "feature visualization" origins of circuit discovery, whereas it is an attribution method that the paper itself uses in EAP-IG. In §2.3 the claim that Hoelscher-Obermaier et al. (2023) show that edits "can fail to extend to novel contexts" stretches a paper whose bibliography title concerns edit specificity; I am not certain and put this in Questions.
- **Suggested Fix:** Correct the descriptions or cite works that support the stated claim.

### Missing References
*Verified through `related_search.py verify` where a link is given; otherwise marked [verify].*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Meinshausen & Bühlmann, "Stability selection", J. R. Stat. Soc. B, 2010 [verify details] | The standard resampling-based stability framework for selected sets; directly gives per-edge inclusion probabilities |
| Important | Nogueira, Sechidis & Brown, "On the stability of feature selection algorithms", JMLR, 2017/2018 [verify year] | Stability measures for selected subsets that handle varying subset sizes, relevant to the Jaccard-size problem |
| Important | Haklay, Orgad, Bau, Mueller & Belinkov, "Position-aware Automatic Circuit Discovery", arXiv 2025 (https://arxiv.org/abs/2502.04577v1, verified) | Prior (arXiv-only) work extending edge attribution patching and trading circuit size against faithfulness: a size-aware comparison point |
| Important | Nainani, Vaidyanathan, Yeung, Gupta & Jensen, "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability", arXiv 2024 (https://arxiv.org/abs/2411.16105v2, verified) | Closest prior work on how an IOI circuit behaves across prompt variants; relates to the paraphrase condition |
| Helpful | Mueller et al., "MIB: A Mechanistic Interpretability Benchmark", arXiv 2025 (https://arxiv.org/abs/2504.13151v2, verified) | Standard comparison of circuit-localisation methods that could supply a reference scale |
| Helpful | Ghorbani, Abid & Zou, "Interpretation of neural networks is fragile", AAAI 2019 [verify] | Analogous robustness analysis for attribution methods |
| Helpful | Zhang et al., "EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification", arXiv 2025 (https://arxiv.org/abs/2502.06852v1, verified) | An EAP-IG variant whose circuits could be included in the stability comparison |

All items are prior to the cutoff and none rests on a recent preprint or concurrent work.

### Baseline scout
No external leaderboard applies (tasks are circuit testbeds with no published numbers to compare), so no under-reported baseline can be checked; the table is not applicable.

### Field snapshot (as of the cutoff)
Five years ago circuits were hand-traced in small models; ACDC (2023) automated discovery and attribution patching (EAP, 2023) made edge-level discovery cheap, with EAP-IG improving faithfulness. The current focus is on whether discovered circuits are faithful, minimal and identifiable (non-identifiability analysis, metric robustness, hypothesis-testing views), and on benchmarks for localisation methods. Open problems are evaluation without ground truth and generalisation across inputs and models. A significant contribution now is one that either supplies a principled stability or uncertainty tool that changes how circuits are reported, or shows that a widely trusted method is unreliable across several methods and models. A single-method, small-model descriptive result is incremental unless it carries a clear reference scale and a fix. This snapshot is built from the kept results and calibrates Significance and Novelty.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Framing outruns the analysis (W2, W3) |
| Clarity | 3 | Well organised (apart from missing setup facts) |
| Significance | 2 | Useful topic, limited scope |
| Originality | 2 | Case study without new estimator; prior circuit-robustness work only lightly differentiated |

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a topical question with a plausible finding, but the contribution is a descriptive study of one method that stops short of the statistical content its title promises.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing/Competent | Framing not formalised; variance vs identifiability conflated |
| Clarity & Presentation | 58 | Competent | Clear exposition; mis-described citations |
| Novelty & Originality | 48 | Developing | Incremental over circuit-robustness literature |
| Significance & Impact | 58 | Competent | Relevant to MI practice |
| Experimental Validation | 48 | Developing | One method, no null |
| Reproducibility | 50 | Developing | Setup details missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. What is the estimand in §3.1, and how would you report an uncertainty interval for "the circuit"? A concrete definition would raise my Technical Rigor score.
2. Do circuits from different bootstrap draws recover the behaviour on each other's data? If yes, instability would be about redundancy, not unreliability.
3. How does Table 1's variance compare with that of ACDC or edge pruning on the same tasks?
4. Do you intend the Hoelscher-Obermaier et al. citation (§2.3) to support robustness of circuits? If so, on what basis?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No (no limitations section; scope claims in §6, "broadly applicable to other circuit discovery methods", are untested).

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. Valuable direction, but a thin statistical framing and one method on small models; prior circuit-robustness work is not properly differentiated.

## Confidence
**4**

---

# Peer Review Report

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Reviewer: Dr. Lucía Ferraro-Okonkwo, Reviewer 3 (Perspective) (statistics and causal-inference department, university, South America; fictional persona)
## Expertise: uncertainty quantification; stability selection; reproducibility of scientific findings
## Date: 2026-11-10

---

## Summary
The paper brings a reproducibility mindset from empirical science to circuit discovery: if the same method on resampled data yields different circuits, single circuits should not be read as findings. The authors show this for EAP-IG across three tasks and three models and recommend reporting bootstrap stability, justifying hyperparameters and stress-testing with noise.

## Strengths

### S1: Imports a good scientific norm
Reporting variability alongside a discovered object is standard in statistics and in replication research (the paper cites Breznau et al., 2022 and Ioannidis, 2005). The call in §6 (item 1) to report mean pairwise Jaccard and CV of circuit error under bootstrap is concrete and cheap.

### S2: Connects to non-identifiability and gives it an empirical face
The observation that GPT-2 Jaccard looks multimodal (§5.1) and the divergent circuits in Fig. 1/Fig. 4 give a tangible picture of what the identifiability argument (Méloux et al.) means in practice.

### S3: Practical, actionable recommendations
The three recommendations (§6) are things a practitioner can adopt in an afternoon, and the direction of characterising a distribution over possible circuits (§6, Future Directions) is a promising reframing.

### S4: Stability metrics beyond structure
Reporting circuit error and KL next to Jaccard (§3.2) links structural instability to functional quality.

## Weaknesses

### W1: Stability selection and feature-selection stability offer ready tools (§3.2, §6)
Selecting a subset of edges from noisy scores under resampling is the setting of stability selection and of feature-selection stability indices; both handle varying subset sizes and give per-element selection probabilities with theory behind them. Adopting them would turn the descriptive Jaccard table into per-edge inclusion frequencies, a "core" circuit (edges selected in ≥ 90% of resamples), and interpretable uncertainty. Opportunity: this would also answer why Jaccard is so low in Table 6 (size mismatch).
- **Suggested Fix:** Report per-edge inclusion probabilities across bootstrap replicates, plot their distribution, and define a consensus circuit with a threshold.

### W2: The notion of a "true" circuit is left open, which limits how the recommendations can be used (§6, Future Directions)
If circuits are non-identifiable, then variance in structure is partly irreducible and a stability report must state what it is stable *with respect to*. The recommendation to "report the variance of circuit structure" would be stronger with guidance on how to act on it (for instance, only interpret edges selected in a stated fraction of resamples).
- **Suggested Fix:** Add a worked example: apply the proposed report to a published circuit and show which components survive.

### W3: Scale and setting assumptions (§4, §6)
All experiments use ≤ 1.2B-parameter models, short templated prompts and a single method. The extrapolation to "larger, more capable models that are of ultimate interest" (§5.1) rests on a comparison of gpt2-small and Llama-3.2-1B, which differ in family, tokenizer and training data as well as size. Real deployments of circuit analysis (safety, auditing) would involve larger models and naturalistic prompts. The paper's introduction invokes regulatory explainability (§1) but never connects stability to that use.
- **Suggested Fix:** State the scope explicitly; if possible add one mid-size model or one naturalistic task; otherwise phrase the scaling statement as a hypothesis.

### W4: The noise recommendation is not portable (§5.3, §6)
Embedding noise amplitude depends on each model's embedding scale; "0.2" is tied to gpt2-small. I would present the noise check as a method (amplitude relative to the embedding norm) rather than a constant.
- **Suggested Fix:** Normalise amplitudes by embedding norm and test on at least one Llama model.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound idea, evidence moderately thin |
| Clarity | 3 | Easy to follow |
| Significance | 3 | A norm worth adopting |
| Originality | 2 | Familiar statistical practice applied to MI |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a timely, communicable message with a cheap protocol that practitioners could adopt; weaknesses (limited scale, one method) are typical of workshop-to-main-track analysis papers and fixable.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasonable protocol, some confounds |
| Clarity & Presentation | 64 | Competent | Clear narrative |
| Novelty & Originality | 60 | Competent | Application of known statistics to a new object |
| Significance & Impact | 72 | Competent (upper) | The reporting norm could change practice |
| Experimental Validation | 54 | Developing/Competent | Small scale, three tasks |
| Reproducibility | 60 | Competent | Code said to be public; setup details missing |
| Ethical Compliance | 68 | Competent | No ethical issues; limitations not discussed |

## Questions for Authors
1. Can you show the per-edge inclusion frequencies for the canonical IOI circuit under bootstrap? A stable core would raise my score; a flat distribution would sharpen the paper's message.
2. What would you recommend an author do when the stability report is poor?
3. Does stability track faithfulness, i.e. are higher-error circuits less stable?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (they disclose D_eval = D in §3.2 but have no limitations section). A short section on scale, single method and the irreducible part of variance would help.

## Ethics Review Flag
**No**

## Overall Score
**4**: Borderline Accept. A useful message with a cheap protocol on a real problem; the weaknesses are fixable and typical of analysis papers that are accepted.

## Confidence
**3**: Statistical framing is my strength; I did not independently re-derive the circuit-specific tables.

---

# Peer Review Report

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Reviewer: Dr. Mei-Ling Dornbusch, Reviewer 4 (Generalist) (ML lab, research university, East Asia; fictional persona)
## Expertise: language-model analysis; evaluation of explanation methods (not circuit methods specifically)
## Date: 2026-11-10

---

## Summary
The paper asks whether the circuits found by EAP-IG are stable. It resamples the discovery data, changes pipeline settings and adds noise, and measures how much the discovered edge sets and their fidelity to the full model change. It finds that bootstrap resampling gives clearly different circuits (mean pairwise Jaccard 0.56), settings change circuits substantially, and recommends reporting stability. It is a short paper with a clear message.

## Strengths

### S1: The contribution is easy to state and relevant to the venue
One paragraph says it: circuit discovery outputs vary, so report their variability. ICLR has a strong interpretability audience and the question of reliability is current (§1).

### S2: Clean experimental narrative
Section 5 maps one-to-one to the stability dimensions of §3.3 (resampling, hyperparameters, noise), and Table 1 and Table 2 summarise the key results compactly.

### S3: Candid on one important design choice
§3.2 states D_eval = D openly, and the appendix gives KL next to circuit error (Tables 7–9).

### S4: Sensible, concrete recommendations
§6 states three recommendations with a named metric for each.

## Weaknesses

### W1: The main claim is stronger than the evidence a non-specialist can verify (Abstract; §5.1; §6)
"A critical vulnerability of the method" (§5.1) and "questioning the stability of its findings" (Abstract) rest on one metric (Jaccard) with no yardstick. As a reader outside the sub-field I cannot tell if 0.56 is "high": there is no comparison to another method, to random circuits or to the variation among circuit papers' own reruns. The paper also never states the dataset size or the number of resamples, so I cannot judge the reliability of the estimates.
- **Suggested Fix:** Add a reference scale (random circuits of equal size, and one other discovery method) and report N and replicates.

### W2: Venue criteria checklist shows presentation and soundness gaps (see checklist below)
Missing setup facts (N, replicates, default configuration), a duplicated results paragraph in §5.1, a cross-reference to the wrong table in §5.3 (Table 3 for noise), and a caption (Figure 4) that contradicts the text about which task Figure 1 shows reduce confidence in the analysis. None is fatal, but together they look unpolished for a paper whose subject is rigor.
- **Suggested Fix:** Add a "setup" table (dataset sizes, replicates, seeds, defaults); remove the repeated paragraph; fix cross-references.

### W3: Scope of the conclusions (§4, §5.1, §6)
Three small tasks, GPT-2 small and one 1B family, and one method family. The statements about larger models and about instruction tuning ("may not fundamentally alter the stability", §5.1) come from two Llama points and no statistical comparison, and the recommendation text, "the statistical framework we have proposed is broadly applicable to other circuit discovery methods" (§6), is untested.
- **Suggested Fix:** Soften those statements to hypotheses, or add one more method (e.g. ACDC or edge pruning) and one larger model.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location / note |
|-----------|--------|-----------------|
| Soundness: claims supported | Partly | Jaccard confounded by size; no reference scale (§3.2, Table 6) |
| Contribution: significance to the community | Partly met | Practical norm, narrow evidence (§6) |
| Presentation: clear and self-contained | Partly | Missing setup facts; duplicated paragraph (§5.1) |
| Related work positioned | Partly | Statistical stability literature not covered (§2.3) |
| Reproducibility: details and code | Partly | "Our publicly available codebase" but no link in the text (§6); N not stated |
| Limitations stated | Not met | No limitations section |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence does not yet carry the claims |
| Clarity | 3 | Mostly clear; some inconsistencies |
| Significance | 3 | Relevant to MI practice |
| Originality | 2 | Modest |

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, relevant message, but the main claim is not calibrated against any reference, and the analysis covers a narrow slice.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing/Competent | No reference scale; missing details |
| Clarity & Presentation | 56 | Competent | Clear structure; duplicated text; wrong cross-references |
| Novelty & Originality | 52 | Developing/Competent | Modest |
| Significance & Impact | 62 | Competent | Reporting norm useful |
| Experimental Validation | 48 | Developing | Narrow |
| Reproducibility | 48 | Developing | Setup details missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. What is the dataset size and number of resamples? A small N would explain the bootstrap-versus-meta-dataset gap and change how I read §5.1.
2. How does the Jaccard between two *independent* meta-dataset draws compare with the bootstrap values? That is the cleanest yardstick available from your own data.
3. If a practitioner follows your three recommendations, what should they conclude when Jaccard is 0.6?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No; add a limitations section covering scale, method coverage and the non-standard stopping rule.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. The idea is relevant and the message is clear, but the central claim lacks a reference scale and the experiments are narrow and under-documented.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Reviewer: Prof. Samir Haldorsen, Devil's Advocate (department of statistics, university, Europe; fictional persona)

---

## Steelman
Circuit discovery pipelines are routinely used to make claims about "the" mechanism, yet they are rarely reported with any measure of variability. By bootstrapping the discovery data and perturbing the pipeline on standard tasks, the authors show that the edges selected by a state-of-the-art method differ substantially between resamples. Even if the exact numbers depend on details, the existence of non-trivial instability justifies a reporting norm.

## Core Argument Chain
1. Circuit discovery is an estimator whose output should be stable under resampling and reasonable pipeline changes.
2. Under bootstrap resampling of D, EAP-IG circuits have low mean pairwise Jaccard (0.561) and non-trivial circuit-error variance (Table 1).
3. Pipeline choices (variant, aggregation, intervention) change circuits widely (Table 2).
4. Noise injection raises instability at moderate amplitude (§5.3).
5. Therefore EAP-IG findings are not stable, single circuits may be artifacts of the sample, and stability reporting should be routine.

## Strongest Counter-Argument
Premise 1 is not justified by the paper, and premise 2 does not measure it. An estimator's instability is only meaningful relative to a target and to a reference level of variation. The paper has neither: it defines no estimand (§3.1) and gives no reference scale for Jaccard, so "0.56" cannot be read as high or low. Worse, the Jaccard index between sets of unequal and tiny size is dominated by size: Table 6 gives a 448-edge circuit with Jaccard 0.016 to a 7-edge median (exactly 7/448), and Table 2's IOI circuits have 3–12 edges. The stopping rule (grow n until any input-to-output path exists, §3.1) yields minimal connected paths whose identity depends on near-ties in the edge ranking; and the same circuits mostly fail functionally (circuit error 0.66–0.80 for Llama on IOI and SVA, Table 3). A minimal path through a noisy ranking will differ across resamples whatever the method; that tells us about the stopping rule and about redundancy in the model (many equivalent paths), not about whether EAP-IG "findings" are unreliable. The authors' own multimodality remark (§5.1: "distinct, yet stable circuit solutions") is the signature of non-identifiability, not estimator variance, and they never test the decisive question: whether circuits from one resample reproduce the behaviour on another. Because evaluation is in-sample (D_eval = D, §3.2), the paper cannot distinguish "different but equally good circuits" from "unreliable circuits". The conclusion that circuits "may be an artifact of the sample" (§6) therefore does not follow. If the authors fix size, cross-evaluate and add a reference scale, the result may well survive; as written, the headline is an artifact-prone description of one pipeline setting.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim that circuits vary under resampling is supported by the paper's own tables (e.g. Table 3 Jaccard means 0.33–0.69 for most cells) in a weaker form than worded, so the fix is narrowing and controls, not a redesign of the whole study.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §3.2; Table 6; Table 2 | Jaccard is confounded by circuit size (448 vs 7 edges: 0.016 = 7/448) and no size-controlled comparison is given | Fixed-k and overlap-coefficient analyses |
| DA-M2 | Logic | §5.1, §6 | Variance is conflated with non-identifiability/redundancy; no cross-evaluation of resampled circuits | Evaluate circuits on other resamples and held-out data |
| DA-M3 | Evidence | §3.1; Table 3 | "Faithful circuit" is defined by path existence; Llama circuits have 0.66–0.80 error | Re-run at fixed faithfulness thresholds |
| DA-M4 | Scope | Abstract; §5.1; §6 | Claims about "the method", larger models, instruction tuning and "broadly applicable" framework rest on one method family, two architectures and no tests | Narrow wording or add methods/models |
| DA-M5 | Integrity of measurement | Table 7; Table 8 | Identical circuit error/KL across circuits of very different sizes (e.g. 0.20 and 6.4·10⁻⁷ at 10–23 edges) suggests the metric is insensitive to circuit content or M_C is undefined | Define M_C; add random-circuit floor |
| DA-M6 | Evidence | Table 1 | Cross-strategy averages cover different cells (paraphrase excludes SVA) | Use common cells (ordering holds: bootstrap Jaccard 0.43 vs 0.75 vs 0.80) |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | §5.1 | Table 1 paragraph repeated; typo "tields" |
| DA-m2 | Consistency | Figure 4 caption vs §5.2 and Fig. 2 | Figure 1 attributed to IOI in §5.2 and to Greater-Than (gpt2-small) in the Figure 4 caption; Fig. 2 reports no Greater-Than circuit for gpt2-small |
| DA-m3 | Consistency | §5.3 | Refers to "Table 3" for noise results |
| DA-m4 | Wording | §1 | "three model architectures": two architectures, three models |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Bootstrap mean circuit error (Table 1) | 0.440 | mean of Table 3 µ (8 cells) = 0.439 | Yes |
| Bootstrap mean Jaccard (Table 1) | 0.561 | mean of Table 3 µ = 0.5625 | Yes |
| Paraphrase mean Jaccard (Table 1) | 0.799 | mean of Table 5 µ (5 cells) = 0.800 | Yes |
| Table 6 IOI 448-edge circuit Jaccard to median | 0.016 | 7/448 = 0.0156 (if the 7-edge median is contained) | Yes (consistent with size artifact) |
| Bootstrap vs paraphrase circuit error, same cells (GT ×2, IOI ×3) | 0.440 vs 0.150 (Table 1, different cells) | 0.376 vs 0.148 | Ordering holds, magnitude differs |
| Paraphrase CV of circuit error vs bootstrap | "lower CVs" (§5.1) | 0.134 vs 0.123 | No (Jaccard CV is lower, circuit-error CV is higher) |

## Ignored Alternative Explanations
- Stopping-rule artifacts: minimal connected paths from near-tied rankings differ by chance.
- Redundant or backup components give many equivalent circuits (functional equivalence, not instability).
- Small or low-diversity discovery sets; duplicates in bootstrap samples (about 63% unique) reduce effective sample size.
- Size mismatch drives Jaccard (Tables 2, 6).
- Evaluation on discovery data may mask functional differences or exaggerate them (D_eval = D).
- Model family and tokenizer differences, not scale, explaining GPT-2 versus Llama differences.

## Missing Stakeholder Perspectives
Practitioners who use circuits for safety or auditing decisions would need to know what to do with a low-stability report; users of published circuits (e.g. IOI) are not told whether their circuits survive the proposed checks.

## Observations (Non-Defects)
The reported aggregates are arithmetically consistent across Tables 1 and 3–5. The paper discloses that circuits are evaluated on the discovery data and marks cases where no circuit was found. Even the weaker claim (circuits are not invariant to the sample) is valuable and cheaply checked. The ordering bootstrap < meta-dataset ≈ paraphrase survives the common-cell recomputation.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Size confound, in-sample evaluation, no estimand |
| Clarity & Presentation | 54 | Readable; inconsistencies |
| Novelty & Originality | 44 | Bootstrap of one method; framing not formal |
| Significance & Impact | 54 | Useful if sound |
| Experimental Validation | 38 | No null, one method, narrow |
| Reproducibility | 44 | Core settings missing |
| Ethical Compliance | 60 | Nothing at stake; no limitations |

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central statistic is size-confounded and unreferenced, and the experiments cannot separate estimator variance from redundancy.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Each weakness was checked for specificity, whether the paper (appendix included) already answers it, consistency with the paper, and actionability. Scores unchanged.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 Size-confounded Jaccard | kept | Quotes sizes and values from Tables 2, 6; arithmetic checked |
| R1 | W2 Non-like-for-like conditions | kept | Cell composition confirmed in Tables 3–5 and §4 |
| R1 | W3 Non-standard operating point | rewritten | Statement about "original practice" softened to a question, since the original procedure is not in the paper |
| R1 | W4 Insensitive metric / undefined M_C | kept | Table 7 and 8 values verified; flagged as an observation plus question |
| R1 | W5 No reference scale | kept | Paper contains no comparison (searched "random", "baseline") |
| R1 | W6 Pairwise statistics | kept | Section 3.2 definitions |
| R1 | W7 Noise experiment | kept | Fig. 3 axis read from caption/extraction; flagged as figure-dependent |
| R1 | Minor items | moved to Minor | Cosmetic |
| R2 | W1 Novelty claim under-argued | rewritten | Novelty statements about Shi et al. and Hoelscher-Obermaier tempered to what the bibliography titles support; Nainani et al. abstract read from kept results |
| R2 | W2 Framing not carried through | kept | §3.1 contains no estimand |
| R2 | W3 Variance vs non-identifiability | kept | §3.2 D_eval = D and §5.1 multimodality |
| R2 | W4 Citation characterisations | rewritten | AlphaEdit claim supported by the paper's own bibliography title; Hoelscher-Obermaier item moved to Questions (low confidence) |
| R3 | W1 Stability selection | kept | Constructive suggestion |
| R3 | W2 "True" circuit undefined | kept | |
| R3 | W3 Scale assumptions | kept | |
| R3 | W4 Noise portability | kept (duplicate of R1-W7) | Merged in Phase 2 |
| R4 | W1 Claim stronger than evidence | kept | |
| R4 | W2 Presentation gaps | rewritten | Narrowed to issues that reduce trust (missing setup, wrong cross-references); cosmetic issues to Minor |
| R4 | W3 Scope | kept | |
| DA | M1–M6, m1–m4 | kept | Each has a location and fix; DA-M5 phrased as an observation about identical values |

No weakness was dropped as already answered by the appendix: the appendix (Tables 3–9) does not state dataset size, replicates or M_C.

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer package (Part A)

**Official score (BEFORE, no EIC weights, DA provisional):** ratings R1 3, R2 3, R3 4, R4 3, DA 2 → official rating 3.00; official composite 53.7 (band 3); no warnings. DA raised no CRITICAL issue, so `da_critical` is empty and the ceiling is none.

**Issue list and consensus:**

| Merged issue | Sources | Class |
|--------------|---------|-------|
| Jaccard confounded by circuit size / no size control | R1-W1, DA-M1, R3-W1 (via stability-selection fix), R4-W1 (no yardstick, partial) | CONSENSUS-3 (hinges) |
| No reference scale / null for "high variance" | R1-W5, R4-W1, DA (counter-argument), R2-W2 | CONSENSUS-4 (hinges) |
| Variance conflated with non-identifiability; no cross-evaluation | R2-W3, DA-M2, R3-W2 | CONSENSUS-3 (hinges) |
| Operating point non-functional / path-based "faithful" | R1-W3, DA-M3 | CONSENSUS-2 |
| Cross-condition averages not like-for-like | R1-W2, DA-M6 | CONSENSUS-2 |
| Missing setup facts (N, replicates, defaults, M_C) and no limitations | R1-W4, R1 Q1, R4-W2, R4 Q1 | CONSENSUS-2 |
| Scope overreach (larger models, instruction tuning, "broadly applicable") | R3-W3, R4-W3, DA-M4 | CONSENSUS-3 |
| Noise recommendation (0.2) not portable; thin experiment | R1-W7, R3-W4 | CONSENSUS-2 |
| Statistical framing not formalised; stability-selection literature missing | R2-W2, R3-W1 | CONSENSUS-2 |
| Novelty vs prior circuit-robustness work under-differentiated | R2-W1 | SOLO |
| Metric insensitive to circuit content (Tables 7, 8) | R1-W4, DA-M5 | CONSENSUS-2 |
| Citation characterisations (AlphaEdit, integrated gradients) | R2-W4 | SOLO |
| Pairwise statistics / CV not valid variance estimates | R1-W6 | SOLO |
| Disagreement: significance and acceptability | R3 (4, pool 66) vs DA (2, pool 38) | SPLIT (pool positions differ by 28) |

## EIC Meta-Review

*(signed: Prof. Ingrid Valdemar, Editor-in-Chief / meta-reviewer)*

### The Case For and Against
- **For acceptance:** The paper asks a question the interpretability community should ask, uses a cheap, transferable protocol, and its qualitative message (circuits are not invariant to the discovery sample or to pipeline choices) is plausible and supported by consistent tables. It is a short, readable analysis paper whose recommendation to report stability is easy to adopt.
- **Against acceptance:** The key statistic (pairwise Jaccard) is confounded by circuit size and unreferenced, the operating point (path-existence stopping) yields largely non-functional Llama circuits, the setup is under-documented (N, replicates, M_C), and the study covers one method family on three small tasks. The title's statistical framing is not carried through, and conclusions about "the method", scale and instruction tuning outrun the evidence.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Jaccard is dominated by size: 448-edge circuit with Jaccard 0.016 to a 7-edge median | R1-W1, DA-M1 | Table 6 (IOI) | Verified | 7/448 = 0.0156; sizes 3–33 in Table 2 also confirmed. That the median circuit has 7 edges is inferred from the 1.000 row, hence "partly inferred" |
| Table 1 rows are averaged over different cells | R1-W2, DA-M6 | §4, Tables 3–5 | Verified | Paraphrase excludes SVA (§4 states it); common-cell recompute keeps the ordering, so the conclusion survives |
| Llama circuits are largely non-functional (error 0.66–0.80) while called "faithful" | R1-W3, DA-M3 | §3.1, Tables 2, 3 | Verified | Definition of "faithful" is path existence in §3.1 |
| Circuits of different size share identical circuit error and KL | R1-W4, DA-M5 | Tables 7, 8 | Verified (observation); interpretation open | Values printed identical; I cannot tell metric bug from saturation; not treated as an error |
| "Standard EAP-IG practice differs from the stop rule" | R1-W3 | §3.1 | Partly correct / unverifiable | The original procedure is not in the paper; reviewer phrased it as a question, which is fair |
| Setup facts absent (N, replicates, seeds, defaults, M_C, compute, limitations, code link) | R1-W4, R4-W2 | whole text | Verified | Text search on terms for size, seeds, replicates, limitation, compute found nothing; no supplement is referenced |
| "three model architectures" vs three models | R1 ERR-4, DA-m4 | §1 vs §4 | Verified | Two architectures; R3 repeated the authors' framing in its summary |
| Figure 4 caption contradicts §5.2/Fig. 2 | R1 ERR-1, DA-m2 | Fig. 4 caption, §5.2 | Verified | Cosmetic |
| §5.3 cites Table 3 for noise results | R1 ERR-2 | §5.3 | Verified | Cosmetic |
| Paraphrase has lower "CVs" than bootstrap | R1 ERR-3, DA numerical check | §5.1, Table 1 | Verified | Jaccard CV lower; circuit-error CV higher (0.134 vs 0.123) |
| AlphaEdit and integrated gradients mis-described | R2-W4 | §2.1 | Partly correct | AlphaEdit's bibliography title says editing; "variant of causal tracing" is loose, not wrong in kind; the integrated-gradients label is a minor mis-description |
| Prior circuit-robustness work under-differentiated | R2-W1 | §2.2, §2.3 | Partly correct | Shi et al. and Méloux et al. are cited but not differentiated; Nainani et al. is uncited (prior, arXiv) so at most a MAJOR-level request to cite, not a required comparison |
| Pairwise Jaccard pairs not independent; CV ill-suited | R1-W6 | §3.2 | Verified (reasoning) | Methodological point, not an error in the numbers |
| Noise experiment effect is small and constants not portable | R1-W7, R3-W4 | §5.3, Figs. 3, 5 | Partly correct | Axis scale read from figure text; figures not viewed as images |
| "Variance vs non-identifiability" alternative explanation | R2-W3, DA | §5.1 | Verified (as an untested alternative) | The paper itself invokes non-identifiability for the multimodality |
| Table 1 and Table 3–5 arithmetic | R1-S3, DA | Tables 1, 3–5 | Verified | Means and CVs recompute |

Literature labels: every reference recommended by R2 is prior (before the cutoff); none is a recent preprint, concurrent or newer work. No missing-comparison weakness rests on such work; the Nainani et al. request is "cite and differentiate", not a required comparison. No claim is judged "known": the script's paper reading is "no central claim fully covered by prior work", and I agree. No text-overlap flag. No integrity signal.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points (size artifact, cell composition, non-functional circuits, missing setup) verified at their locations; one softened question about original EAP-IG practice |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly sound; the Hoelscher-Obermaier worry unverified (placed under Questions) and the first-pass novelty statement partly tempered; typical review |
| R3 (Perspective) | 4 | 3 | 0.75 | Accepts the authors' "three models/three architectures" framing and states the scale-up story without noting the confounds; Overall 4 sits above what the verified issues support, though it correctly flags fixability |
| R4 (Generalist) | 3 | 4 | 1.0 | Balanced and calibrated, cites the right gaps, no overstated points |
| DA | 2 | 4 | 1.0 | Strong counter-argument survived my check (size artifact, in-sample evaluation, variance vs redundancy); Overall 2 is slightly harsh because the qualitative finding survives, so full weight only on the arguments that held |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | n/a (no CRITICAL issue was raised; the strongest counter-argument is MAJOR: DA-M1/M2/M3) | n/a |

Ceiling: none. Total DA-CRITICAL raised 0, upheld 0.

### Final Decision and Justification
**Official ratings** are R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00, official composite 53.7. With my weights (R1 1.25, R3 0.75, others 1.0, each times the confidence weight) the **EIC-weighted rating is 2.92**, which rounds to **3**, and the weighted composite is 52.9 (band 3), so the composite cross-check agrees with the rating and there is no flag. I keep the starting point. My own pool position: **better than about 47% of ICLR submissions**. The decisive evidence is the unreferenced, size-confounded Jaccard on stopping-rule circuits that are non-functional in the Llama cells (verified in Tables 2, 3, 6), together with the narrow single-method scope; against this, the qualitative finding is plausible, survives the common-cell recomputation, and the topic is relevant. The weaknesses are largely fixable by controls the authors can run quickly (fixed-k and overlap analyses, cross-evaluation, a reference scale, a stability-versus-N curve), but that is new analysis and not a clarification, and a typical ICLR submission of this kind would not be accepted in the current form. The decision does not exceed the DA ceiling (none). The official ratings remain as written; the EIC assessment is internal.

**Final Overall: 3 (Borderline Reject).** ICLR label from the aggregation script: "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})", scale status secondary. ICLR sub-scores from the script: Soundness 2, Presentation 2, Contribution 2.

---

## Editorial Decision

## Paper: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG
## Submission ID: iclr26-YD1P4DVtdk
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: analysis
## Review Team (fictional personas): EIC Prof. Ingrid Valdemar; R1 Methodology Dr. Tomasz Veldkamp, R2 Domain Prof. Aiyana Whitcombe, R3 Perspective Dr. Lucía Ferraro-Okonkwo, R4 Generalist Dr. Mei-Ling Dornbusch, DA Prof. Samir Haldorsen

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 53.7
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 52.9 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR rating (script, scale secondary):** 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Soundness 2 / Presentation 2 / Contribution 2

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 54 | 60 | 54 | 44 | 52.4 | 51.7 | 16 |
| Clarity & Presentation | 55 | 58 | 64 | 56 | 54 | 57.4 | 56.8 | 10 |
| Novelty & Originality | 50 | 48 | 60 | 52 | 44 | 50.8 | 50.0 | 16 |
| Significance & Impact | 58 | 58 | 72 | 62 | 54 | 60.8 | 59.8 | 18 |
| Experimental Validation | 44 | 48 | 54 | 48 | 38 | 46.4 | 45.7 | 16 |
| Reproducibility | 45 | 50 | 60 | 48 | 44 | 49.4 | 48.3 | 16 |
| Ethical Compliance | 62 | 62 | 68 | 62 | 60 | 62.8 | 62.4 | 8 |
| **Composite** | 51.6 | 53.3 | 62.3 | 54.6 | 46.9 | **53.7 (before)** | **52.9 (after)** | |

No dimension spread exceeds 20; no consistency warnings. Pool positions: R1 45, R2 48, R3 66, R4 52, DA 38, EIC 47 (R3 and DA differ by 28, below the 30-point trigger).

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG" to ICLR. You address a question that the mechanistic interpretability community needs to take seriously: whether circuits reported from a single dataset and a single pipeline setting are reliable.

**Overall Assessment:** The panel found the question important and the protocol simple and transferable. The qualitative message that discovered circuits are not invariant to resampling or pipeline choices is plausible and consistent with your tables. The panel was not convinced that the evidence supports the strength of the claims, mainly because the headline statistic is confounded by circuit size and has no reference scale, and because the setup is under-documented.

**Key Strengths Identified by Reviewers:**
1. A relevant, under-measured question with a cheap, reusable bootstrap protocol (R1, R3, R4).
2. Several perturbation types separated and reported together; honest disclosure of D_eval = D and of cases with no circuit (R1, R4).
3. Concrete, adoptable recommendations and arithmetic that checks out across Tables 1 and 3–5 (R1, R3, DA).

**Key Concerns Requiring Attention:**
1. Jaccard on circuits of very different size mostly reflects size (448 vs 7 edges gives 0.016 = 7/448 in Table 6) and has no reference scale; "high variance" is not established (R1, R4, DA; CONSENSUS-4 to 3).
2. Variance is conflated with non-identifiability/redundancy; circuits are never cross-evaluated on other resamples, and the path-existence stopping rule yields circuits that disagree with the full model on most Llama inputs (R2, R3, DA, R1).
3. Missing setup (dataset size, replicates, M_C, defaults), cross-strategy averages over different cells, no limitations section, and claims about "the method", scale and instruction tuning that outrun a one-method, three-small-task study (R1, R3, R4, DA).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The strongest challenge (MAJOR) is that the results cannot separate estimator variance from redundant, equally good circuits, because no circuit is evaluated outside its own discovery data. This must be addressed in any revision.

**Decision: Borderline Reject (3).** The topic and approach have merit, but the confounds above need new analysis (fixed-size comparisons, cross-evaluation, a reference scale, a stability-versus-sample-size curve) rather than clarification alone. If those controls show that instability persists once size and functional equivalence are accounted for, and the narrowed claims are matched to the evidence, the paper would be a competitive submission. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Valdemar
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No reference scale / null for "high" variance | R1, R2, R4, DA | CONSENSUS-4 |
| Jaccard confounded by circuit size / no size-controlled analysis | R1, DA, R3 (via stability selection), R4 (partial) | CONSENSUS-3 |
| Variance conflated with non-identifiability; no cross-evaluation | R2, R3, DA | CONSENSUS-3 |
| Scope overreach (larger models, instruction tuning, broad applicability) | R3, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the paper's contribution significant enough for ICLR as is? | R3 (Overall 4, pool 66) | DA (Overall 2, pool 38), R1, R2, R4 (3) | Both are partly right: the question is significant, but I weight the verified confounds (size, in-sample evaluation, no scale) more than the potential, as the skill's standard is the paper's evidence at the venue |

### Score Spread Discussion
No dimension exceeded the 20-point flag. Significance has the widest spread (18, R3 72 versus DA 54); I adopt a value near the panel's mean (59.8 weighted) because the relevance is clear but the evidence is limited.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| (none) | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Jaccard confounded by circuit size | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Variance vs non-identifiability, no cross-evaluation | Yes (R2-W3) | n/a | n/a |
| DA-M3 | MAJOR | Non-functional circuits under path-based "faithful" | Yes (R1-W3) | n/a | n/a |
| DA-M4 | MAJOR | Scope overreach | Yes (R3-W3, R4-W3) | n/a | n/a |
| DA-M5 | MAJOR | Identical metric values across circuit sizes | Yes (R1-W4) | n/a | n/a |
| DA-M6 | MAJOR | Table 1 averages over different cells | Yes (R1-W2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Issues the EIC verified as undermining the main claim ("high structural variance of EAP-IG").*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Jaccard confounded by circuit size; no size-controlled stability | R1-W1, DA-M1, R3-W1 | §3.2, Tables 1, 2, 6 | Report size distributions; recompute at fixed k and with overlap coefficient / per-edge inclusion frequencies | Medium; about 1 GPU-day if edge scores are not stored | Yes |
| R2 | No reference scale for "high" variance | R1-W5, R4-W1, R2-W2, DA | §5.1, §6, Fig. 1 | Add random-size-matched circuits, two independent meta-dataset draws as yardstick, and one non-EAP method; bootstrap CIs for the mean Jaccard | Medium; 1–2 GPU-days | Partly |
| R3 | Variance not separated from redundancy/non-identifiability | R2-W3, DA-M2, R3-W2 | §3.2, §5.1, §6 | Cross-evaluate each circuit on other resamples and held-out data; report consensus/median circuit faithfulness | Medium; under 1 GPU-day | Yes |
| R4 | Non-standard, non-functional operating point | R1-W3, DA-M3 | §3.1, Tables 2, 3 | Re-run key experiments with n chosen at a fixed faithfulness target and at fixed n; confirm stop rule against original practice | Medium–High; 1–3 GPU-days | Partly |
| R5 | Missing setup facts and an undefined M_C | R1-W4, R4-W2, DA-M5 | §3.2, §4, Tables 7, 8 | State N, replicates, seeds, IG steps, default variant, M_C ablation; explain identical metric values across sizes; add limitations section; give an anonymised code link | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Table 1 averages over different cells; bootstrap versus meta-dataset gap unexplained | R1-W2, DA-M6 | Common cells; stability-versus-N curve; subsample-without-replacement control | Medium | Yes |
| S2 | Scope overreach (larger models, instruction tuning, "broadly applicable", "critical vulnerability") | R3-W3, R4-W3, DA-M4 | Soften wording or add a method (ACDC or edge pruning) and a larger model | Low (wording) / High (experiments) | Yes (wording) |
| S3 | Noise recommendation (0.2) not portable and effect small | R1-W7, R3-W4 | Normalise amplitude by embedding norm; random directions; Llama models | Medium | Partly |
| S4 | Pairwise Jaccard variance and CV not valid variance estimates | R1-W6 | Replicate-level resampling; drop CV or give with mean | Low | Yes |
| S5 | Statistical framing not formalised; stability-selection literature missing | R2-W2, R3-W1, R2 references | Define estimand and intervals or retitle; cite stability selection (Meinshausen & Bühlmann, 2010 [verify]) and feature-selection stability (Nogueira et al., JMLR [verify year]) | Low–Medium | Yes |
| S6 | Differentiate from prior circuit-robustness work | R2-W1 | Short comparison table: Shi et al. 2024, Méloux et al. 2025, Miller et al. 2024, Nainani et al. 2024 (https://arxiv.org/abs/2411.16105v2), Haklay et al. 2025 (https://arxiv.org/abs/2502.04577v1) | Low | Yes |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Citation descriptions (AlphaEdit, integrated gradients, Hoelscher-Obermaier) | R2-W4 | Correct or support them |
| N2 | Cosmetic and consistency errors: duplicated Table 1 paragraph, "tields", Figure 4 caption versus §5.2, Table 3 cited for noise, "three model architectures", "EAP-IP" | R1, DA | Fix text and captions |
| N3 | Worked example on a published circuit; guidance on acting on a poor stability report | R3 | Add to §6 |
| N4 | Helpful references: MIB benchmark (https://arxiv.org/abs/2504.13151v2), EAP-GP (https://arxiv.org/abs/2502.06852v1), Ghorbani et al. 2019 [verify] | R2 | Cite where relevant |

---

## Estimated Revision Effort
- Priority 1: 5 items, roughly 1–2 weeks (3–6 GPU-days plus writing).
- Priority 2: 6 items, roughly 1 week.
- Priority 3: 4 items, 1–2 days.
- **Total estimated revision time**: about 3 weeks; a subset (R1, R3, R5, S1, S2, N2) is feasible within a one-week discussion period.
