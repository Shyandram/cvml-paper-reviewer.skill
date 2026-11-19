# Academic Paper Review: "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders"

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested)

*Execution note: the five reviewer reports and the EIC were produced as sequential role-based passes sharing one model context, not as independent agents. The paper was read as extracted text; **figures were not available**, so figure-dependent claims (Figures 1–10) are judged from captions and surrounding text only. The paper has no supplement beyond its appendix (A.1–A.7). The integrity scan found no reviewer-directed text. The reviewers read the redacted copy (identical to the original).*

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders |
| Primary Discipline | Machine learning → mechanistic interpretability → sparse autoencoders (SAEs) for LLM activations |
| Secondary Discipline(s) | Sparse coding / dictionary learning; superposition theory |
| Paper Type | Analysis/Insight (composite weights: analysis), with a small methodological component (the Nth decoder projection score) |
| Core Technique(s) | BatchTopK SAEs, synthetic ground-truth toy model with correlated features, decoder-projection statistic, k-sparse probing |
| Target Venue | ICLR, top-tier conference (stated); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | None (ICLR 2026 form: Soundness / Presentation / Contribution, Rating, Confidence) |
| Paper Maturity | Submission-ready in form, but short (about 4 pages of main text, then appendix); marked "Preprint. Under review." |
| Ethics-Relevant Content | None (no human data, no deployment risk, no direct misuse potential) |

### Claimed Contributions (as stated by the authors)
1. **C1.** L0 is not a free hyperparameter: if it is not set "precisely", BatchTopK SAEs mix correlated features (too low) or find degenerate mixtures (too high) (Abstract; §3, Figure 1).
2. **C2.** Under too-low L0, MSE loss incentivizes incorrect latents, so the sparsity–reconstruction tradeoff is a misleading criterion (§3.1; Appendix A.2, Figures 6–7).
3. **C3.** A method, the Nth decoder projection score s_dec_n, determines the correct L0 on a given training distribution: it finds the true L0 in toy models and "coincides with peak sparse probing performance in LLMs" (§3.2, §4; Figures 2–4).
4. **C4.** "Most commonly used SAEs have an L0 that is too low" (Abstract; §6; Appendix A.5, Figure 9).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Toy model: 50 mutually orthogonal true features in R^100, P(f0)=0.345 decreasing linearly to P49=0.05, random correlation matrix, magnitudes ~N(1.0, 0.15), true L0 = 11, 15M synthetic samples, SAELens, BatchTopK (§3). Toy SAE width, batch size, learning rate and steps for the main runs: not stated after search (A.3 gives 25k+5k steps for the transition experiment only). LLM: Gemma-2-2b layer 12, 32k width (stated only in Figure 3/10 captions), 500M Pile tokens, lr 3e-4, decoder normalized, one SAE per L0 in 10, 20, …, 250, then wider spacing up to 2500 (§4). Hook point, batch size, seeds, compute: not stated. Code: "[link removed]".
- **Splits and selection.** No train/validation/test split is described for s_dec_n (which inputs it is computed on is not stated beyond "training inputs"/"training activations", §3.2). Sparse probing uses the Kantamneni et al. benchmark with k=1 and k=16 ("over 100 sparse probing tasks", §4). No statement of tuning or selecting on a reported test set was found by the protocol sweep.
- **Headline numbers.** Toy MSE 2.73 (learned, L0=5) vs 4.88 (ground-truth SAE at L0=5) (§3.1). "Outperform the ground-truth SAE on variance explained by over 2x" at L0=1,2 (A.2). Correct L0 for Gemma-2-2b layer 12 "around 200-250" (Figs 3–4, A.5). Neuronpedia gemma-2-2b: 40 SAEs, mean L0 93.0, median 40.5 (Figure 9).
- **Appendix adds:** toy-model details (A.1), the reconstruction cheating experiment (A.2), L0-transition experiment (A.3), an unvalidated-in-LLM procedure for tuning L0 during training (A.4), the Neuronpedia histogram (A.5), limitations (A.6), extended s_dec_n plots (A.7).
- **Unverifiable:** all figures (images unavailable); Eq. 3 transpose notation and the A.4 gradient-bias formula (extraction may have dropped symbols).

### Review Team (fictional personas)

**EIC (meta-reviewer): Prof. Ingrid Valdemar-Osei**, large public research university (Northern Europe). Senior faculty; representation learning, evaluation methodology for interpretability. Role: reads all five reviews, checks decisive points, weights reviewers, decides. Style: calibrates to what ICLR actually accepts; asks whether the headline claim is measured.

**Reviewer 1 (Methodology): Dr. Anselm Okafor-Lindqvist**, industrial ML research lab (Europe). Mid-career; SAE training and evaluation, sparse probing protocols. Focus: design, statistics, comparison fairness, reproducibility. Style: wants variance, matched budgets and every hyperparameter written down.

**Reviewer 2 (Domain): Prof. Leilani Varga-Mendes**, interpretability group, public research university (North America). Senior faculty; dictionary learning, superposition, SAE literature. Focus: literature, theory, domain contribution. Style: checks every novelty statement against the cited abstract.

**Reviewer 3 (Perspective): Dr. Ravindra Chaudhary-Holt**, signal-processing and computational-neuroscience department, university (South Asia). Mid-career; compressed sensing, sparse coding in neural populations. Focus: cross-field links, practical use, assumptions. Style: constructive, sees potential.

**Reviewer 4 (Generalist): Dr. Mei-Lin Abernathy-Zhou**, ML group, mid-sized research university (East Asia). Mid-career; representation learning, not an SAE specialist. Focus: contribution clarity, venue fit, presentation. Style: typical program-committee member; weighs contribution against ordinary weaknesses.

**Devil's Advocate: Dr. Oluwaseun Brandt-Ferreira**, evaluation-methodology and causal-inference group, university (South America). Senior postdoc; Focus: core argument, overclaiming. Style: rigorous, never hostile.

*Personas are fictional. Assumptions: venue ICLR (stated), paper type Analysis.*

### Literature check record (Phase 1.5; run after the reports were drafted, mode `strict`)
Fingerprint written (title, method names, distinctive phrases, cutoff 2025-09-24). 7 of 12 queries used (5 claim, 1 baseline, 1 expansion); 52 unique kept results (18 prior peer-reviewed, 20 prior arXiv-only, 7 recent preprints, 7 concurrent); coverage gaps: none by count. The query on L0 selection for SAEs kept nothing: "no close prior work found in this search (arXiv only)", which is a limit of the search, not evidence of novelty. Similarity run: closest prior works are Leask et al. (canonical units, cosine 0.249), Paulo & Belrose (0.219), Ensembling SAEs (0.183); all below the 0.30 overlap flag, no text overlap (0 shared 8-grams). Novelty profile (`related_search.py novelty`): C1 high, C2 high, C3 high by the script, with Feature Hedging listed as "worth discussing" because it is a *recent preprint* (2025-05-16, under 6 months before the cutoff). The Domain Reviewer's own reading is more careful than the script (see R2). Benchmark scout: the only external benchmark is the Kantamneni et al. sparse-probing suite, which reports no numbers the paper compares against, so there is no baseline-number table.

---

# Phase 1: Independent Reviews

## Reviewer 1 (Methodology): Peer Review Report

**Paper:** Sparse but Wrong · **Reviewer:** Dr. Anselm Okafor-Lindqvist, Methodology (industrial ML lab, Europe; fictional persona) · **Expertise:** SAE training, sparse-probing protocols · **Date:** 2026-11-10

### Summary
The paper studies BatchTopK SAEs and argues that the average number of active latents (L0) must match the true number of active features. In a synthetic model with correlated features, SAEs at L0 5, 11 and 18 recover the true features only at the true L0 (Figure 1). It shows that at low L0 a ground-truth dictionary has worse MSE than a corrupted learned one (§3.1, Appendix A.2). It proposes a statistic of decoder-to-input projections whose minimum is said to mark the correct L0, reports a minimum around L0 200–250 for a Gemma-2-2b layer-12 SAE family, and notes that sparse-probing F1 peaks in the same region (Figures 3–4). It concludes that most public SAEs have too low an L0.

### Strengths
**S1: A clean, falsifiable toy demonstration of reconstruction "cheating".** §3.1 and Appendix A.2 (Figure 6) compare the learned SAE with a hand-built ground-truth SAE at the same L0: "achieves a MSE of 2.73, while the SAE with ground-truth correct latents achieves a much worse MSE of 4.88." This directly tests the claim that lower MSE does not imply correct features, and it is the best-controlled result in the paper.
**S2: A label-free statistic that is cheap to compute and shows a clear dependence on L0 in both settings.** §3.2 defines s_dec_n in two equations (Eq. 3–4), and Figures 2–3 report a minimum in the toy model and in Gemma-2-2b.
**S3: Useful side experiments and honest limits.** Appendix A.3 (transition experiment, Figure 8) shows asymmetry: starting too high recovers, starting too low does not. Appendix A.4 openly states that the tuning procedure "works very well in toy models" but needs heavy tuning in LLMs, and A.6 states the single-layer limit.

### Weaknesses

**W1: The LLM evidence for C3/C4 is one layer, one width, one seed per L0, one proxy.** §4 and A.6 ("We limit our investigated to Gemma-2-2b layer 12") cover a single model, layer and 32k width (Figure 3 caption), trained on 500M tokens, with no repeated seeds and no uncertainty on any curve in §4. In an LLM there is no ground truth, so "correct L0" is defined only by where s_dec_n is minimal and where F1 peaks. Both are read off a grid with 10-step spacing to L0=250 and much wider spacing after, so "200-250" is a handful of points. High-L0 SAEs may also be under-trained at 500M tokens.
- **Suggested fix:** replicate across ≥3 layers, ≥2 widths (for example 16k and 65k) and one more model family, with 3 seeds on a coarser L0 grid; report the L0 minimizing each metric with bootstrap intervals. Rough cost (my estimate): 100–150 SAE runs, order of 100–300 GPU-hours.

**W2: The toy model does not exercise the regime the claims are about, and its setup is under-specified.** §3 uses "50 mutually orthogonal true features" in R^100, so there is no superposition and no overcompleteness, the central difficulty in LLMs. One random correlation matrix, one run, and only three L0 values appear in Figure 1; Figure 2 gives the sweep for the metric but there is no quantitative feature-recovery curve over L0 (for example mean best-match cosine). SAE width, batch size, learning rate and steps for the main toy runs are not stated after search. Width matters: the hedging mechanism the paper invokes depends on width relative to the number of true features.
- **Suggested fix:** add a recovery-vs-L0 curve over ≥5 seeds and ≥3 random correlation matrices; vary the number of features relative to the dimension and the correlation strength; state SAE width and training hyperparameters. Cost: small (CPU/single-GPU hours).

**W3: s_dec_n is an ungrounded heuristic whose minimum is not well defined.** §3.2 gives no derivation. It says n "should be sufficiently larger than a reasonable guess at the correct L0" and then, in A.4, that the curve is "relatively flat in a region start at the correct L0 and extending to higher L0 values", so a minimum within a flat plateau cannot be located precisely, which conflicts with the "precisely" in the abstract. Because the metric takes the n-th largest projection per sample, for L0 > n it mechanically reads the projection of a firing latent. Figure 2 reports N=12 against a true L0 of 11, which is not "sufficiently larger" (see ERR-1). No estimator for the L0 (argmin, knee, smoothing) is defined.
- **Suggested fix:** define the estimator and its uncertainty; show s_dec_n against L0 for matched widths; analyze a simple analytic case (orthogonal features, known correlations) to explain why the minimum falls at the true L0. Cost: low.

**W4: Agreement with sparse probing is the only independent validation, and it is weak.** §4 and Figure 4 show F1 peaks "around 200-250" for k=1 and k=16, with no error bars (none in text or caption) and a vertical range of a few F1 points (axis ticks run about 0.68–0.76 for k=1 and 0.77–0.83 for k=16). Probing usefulness can rise with L0 for reasons unrelated to feature correctness (more information per token), and the benchmark has over 100 tasks that allow bootstrap intervals.
- **Suggested fix:** report task-level bootstrap CIs; add at least one correctness-oriented metric (absorption, concept-isolation tests); include a control metric that should not peak at the same L0. Cost: low to medium.

**W5: Headline wording runs ahead of the evidence (C4, abstract).** "We find that most commonly used SAEs have an L0 that is too low" rests on Appendix A.5 and Figure 9 (histograms of L0 for open-source SAEs across models, layers and widths) compared with a correct L0 estimated for one configuration. §6 itself says the correct L0 "depends on the dataset" and defers dependence on width, size and layer to future work. A.6 asserts "do not expect our findings to be meaningfully different" for JumpReLU and L1 SAEs with no experiment.
- **Suggested fix:** narrow the claim to the studied configuration, or add width/layer/architecture results. Cost: wording only, or as in W1.

*Minor:* typos ("We sampling", "our investigated", "to located"); symbols n/N/k are used interchangeably for the same quantity (Fig. 2 "N", Fig. 3 "N"/"k", A.7 "k").

### Claim-to-Evidence Map
| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|-------------|---------------------|---------|
| C1 | Wrong L0 breaks features (low: mixing; high: degenerate) | Abstract, §3 | Figure 1, three L0 values, one toy run | Partially (toy only; text concedes high L0 "still learns many correct latents") |
| C2 | MSE rewards incorrect latents at low L0 | §3.1, A.2 | MSE 2.73 vs 4.88; Figures 6–7 | Supported in the toy model |
| C3 | s_dec_n finds the correct L0 | §3.2, §4 | Figure 2 (toy), Figures 3–4 (one LLM config) | Partially (heuristic, single config, weak proxy) |
| C4 | Most public SAEs have too low an L0 | Abstract, §6, A.5 | Figure 9 histograms | Unsupported as worded (extrapolation) |

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | §3.2 vs Figure 2 caption | "for n = 18 and n = 22, with SAE L0 ranging from 2 to 25 in Figure 2" | Figure 2 caption and panel titles give N=12 and N=20 for the same plots | Cross-referenced two locations | High | MINOR | Make text and figure agree; confirm which n was used |
| ERR-2 | E8 | §3, A.1 (protocol sweep) | "we train SAEs on 15M synthetic samples using SAELens" | Toy SAE width, batch size, lr, steps are not stated for Figure 1/2, and the mixing mechanism depends on width | Searched §3, A.1–A.3 | High | MAJOR | State all toy hyperparameters |
| ERR-3 | E5 | §6, Abstract | "the L0 used by most SAEs is lower than it ideally should be" | Correct L0 is estimated for one layer/width/model; Figure 9 pools many | Compared §6/A.5 with §4/A.6 | High | MAJOR | Narrow wording or extend experiments |
| ERR-4 | E6 | A.3 vs §3.1 | "achieve a higher MSE loss than is achievable by the correct latents under the same L0 constraint" | §3.1 shows the incorrect latents have *lower* MSE (2.73 vs 4.88) | Cross-referenced | Medium (possibly a wording slip) | MINOR | Correct to "lower" |

### Questions for Authors
1. Which inputs is s_dec_n computed on (training batches, held-out tokens)? What batch size b enters Eq. 4? A held-out evaluation would raise my Experimental Validation score.
2. The expected number of firing features from the stated base probabilities is about 9.9 (derived: mean of 0.345 and 0.05 times 50 = 9.875), yet the true L0 is 11. How do correlations change the marginals? (Figure 5 labels them "base".)
3. Eq. 3 is written with a transpose on W_dec ∈ R^{d×h} (§2); the extracted text may have misplaced a symbol. Is the product dimensionally consistent as printed? In A.4 the bias term reads "−b dm/dL0" while the text says it is multiplied by the *magnitude*; was |·| dropped?
4. In A.7 the plots for k=5 and k=10 use n far below the claimed correct L0. Why would the n-th largest projection of an actively firing latent be minimized at L0 200–250?
5. How many seeds underlie each point in Figures 3–4?

### Limitations Assessment
**Partially.** A.6 states the single-layer and single-architecture limit but the Abstract and §6 do not carry it.

### Pool position and scores
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline LLM claim rests on one layer/width/seed and a heuristic metric with no uncertainty; the toy result is clean but narrow.

| NeurIPS-style | Score | Rationale |
|---|---|---|
| Quality | 2 | Clean toy result; LLM validation too thin for the claim |
| Clarity | 3 | Short and readable; notation drift |
| Significance | 3 | Practical message, if true, would matter |
| Originality | 2 | Close to feature hedging; new statistic |

| Dimension | Score | Descriptor | Rationale |
|---|---|---|---|
| Technical Rigor | 52 | Developing | Heuristic metric, no derivation, flat-plateau minimum |
| Clarity & Presentation | 66 | Competent | Clear core story; key result in appendix |
| Novelty & Originality | 54 | Developing/Competent | New statistic; mechanism overlaps hedging |
| Significance & Impact | 60 | Competent | Relevant to SAE practice |
| Experimental Validation | 42 | Developing | One config, one seed, one proxy, no variance |
| Reproducibility | 48 | Developing | Toy hyperparameters, hook point, seeds missing; code link removed |
| Ethical Compliance | 66 | Competent | Nothing at stake; limits partly discussed |

**Overall: 3** (Borderline Reject): a sound idea and a clean toy demonstration, but the claims in C3/C4 are not tested at the scale at which they are stated. **Confidence: 4** (checked all text and appendix; figures not visible).

---

## Reviewer 2 (Domain): Peer Review Report

**Paper:** Sparse but Wrong · **Reviewer:** Prof. Leilani Varga-Mendes, Domain (interpretability group, North America; fictional persona) · **Expertise:** dictionary learning, superposition, SAE literature · **Date:** 2026-11-10

### Summary
The paper argues that L0 is a determinant of SAE correctness, not a neutral dial. It builds on the observation that correlated features are merged when an SAE lacks capacity and characterizes low L0 as one source of that capacity shortage. It offers a diagnostic statistic and applies it to Gemma-2-2b, concluding that open-source SAEs generally use too little sparsity budget.

### Strengths
**S1: A timely question with practical bite.** The paper targets a decision every SAE trainer makes (footnote 1: "all SAE trainers must decide on the target L0") and questions the sparsity–reconstruction frontier as an evaluation criterion (§6, A.2).
**S2: A ground-truth experiment that isolates a mechanism.** The comparison of a learned SAE against a hand-constructed ground-truth SAE at equal L0 (A.2, Figure 6) is a neat way to show that reconstruction can reward wrong dictionaries.
**S3: Connects to existing failure modes.** §1 and §5 relate the finding to feature hedging [6], absorption [5] and invented features [18], so the reader can place it among known SAE pathologies.

### Weaknesses

**W1: The novelty delta against feature hedging is thin.** §1 states "We consider this to be a manifestation of feature hedging [6]" and §5 repeats "We consider our work a version of feature hedging due to low L0." The cited abstract of [6] says an SAE narrower than the number of true features, with correlated features, merges components of correlated features, a phenomenon "caused by SAE reconstruction loss". The paper's C1/C2 for the *low-L0* side is thus the same mechanism with L0 replacing width as the capacity constraint. The new content is the L0 framing, the reconstruction-cheating comparison (A.2), and the s_dec_n statistic. Feature hedging is a recent preprint (2025-05-16, under six months before the cutoff), so this is a *positioning* issue, never a required comparison and never a reason to lower a score on its own. It is MAJOR at most.
- **Suggested fix:** state precisely what is new relative to [6]: does L0 act independently of width? A 2-D sweep over (width, L0) in the toy model would show it.

**W2: Related work is four sentences (§5) and misses the nearest verified prior work.** Not discussed: Leask et al., *Sparse Autoencoders Do Not Find Canonical Units of Analysis* (ICLR 2025), whose decomposition and incompleteness findings bear directly on whether a single "true" feature set or "true L0" exists; Elhage et al., *Toy Models of Superposition* (2022), the standard toy setting (with overcomplete superposed features, unlike the orthogonal setup here); Karvonen et al., *SAEBench* (ICML 2025), which evaluates SAEs across many L0 values and metrics beyond sparse probing; Paulo & Belrose (2025) on SAEs trained on the same data learning different features, which questions the premise of a unique correct dictionary.
- **Suggested fix:** add and discuss these; see Missing References.

**W3: No baseline for choosing L0, and the "misleading tradeoff" framing partly argues against a straw man.** §1 says the literature treats the sparsity–reconstruction tradeoff "implying any L0 is equally valid", citing [10, 15] (and [7]); these works plot frontiers to compare architectures at matched L0, which is not the same as claiming any L0 is valid (I cannot verify their wording from the text provided, so I ask for quotes; see Question 1). More importantly, no competing selection rule appears in §3–§4: choosing L0 by an elbow of the MSE curve, by sparse-probing F1 alone, or by an absorption metric. Without them the added value of s_dec_n is unquantified. A line of 2025 work on adaptive-K and multi-sparsity SAEs (training one SAE across several sparsity budgets) is related and worth discussing; it is not a required comparison.
- **Suggested fix:** compare s_dec_n against simple selection baselines on the toy model (where truth is known) and on Gemma-2-2b (against probing).

*Minor:* citation [11]/[4] are used to support "too low an L0 leads to worse SAE performance" (§1); please quote the relevant result.

### Novelty and literature-check addendum
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 low L0 breaks features | Chanin et al., *Feature Hedging* (arXiv 2505.11756; recent preprint) | Correlated features merge when SAE is narrower than true features; caused by reconstruction loss | L0 (not width) as the trigger; high-L0 degeneracy | Cited, weakly differentiated ("a version of") |
| C2 reconstruction rewards wrong latents | same | Hedging driven by reconstruction loss (theory + LLM) | Explicit ground-truth-SAE MSE comparison (§3.1, A.2) | Partly |
| C3 s_dec_n estimator | none found (7 queries, arXiv only) | n/a | A decoder-projection statistic for L0 | n/a |
| C4 most SAEs too low | none found | n/a | Neuronpedia histogram vs one estimate | n/a |

Per-claim novelty (my verdict, from the script profile and the abstracts): C1 medium (script: high; I downgrade because the mechanism is acknowledged by the authors as hedging); C2 medium; C3 high (no close prior method found, arXiv only, so at most medium-high); C4 high but unsupported. Closest prior works for attribution: Leask et al. (cosine 0.249), Paulo & Belrose (0.219); no text overlap.

**Baseline scout.** The only external benchmark is sparse probing (Kantamneni et al., cited as [11]); the paper reports no baseline method numbers, so no under-reported baseline can be assessed.

**Field snapshot (as of the 2025-09-24 cutoff).** Three years ago SAE work centered on L1-penalized SAEs on small models; since 2024, TopK, BatchTopK, JumpReLU and gated variants made L0 directly controllable and benchmarks (sparse probing, SAEBench, steering comparisons) appeared. Open problems stated by recent work: SAEs underperform supervised baselines on probing, features are not canonical or atomic, and absorption and hedging corrupt monosemanticity; matryoshka and multi-sparsity variants are responses. What counts as a significant contribution now: a clear mechanism and a practical rule that changes how SAEs are trained (for example, a verified rule for width and L0, or a metric that predicts downstream quality across models), not another architecture with a small frontier gain. The paper's idea fits the "mechanism plus rule" pattern but, as written, provides the rule only for one configuration.

### Missing References (all verified by `related_search.py` unless marked)
| Priority | Reference | Why it matters |
|---|---|---|
| Important | Leask et al., "Sparse Autoencoders Do Not Find Canonical Units of Analysis", ICLR 2025 (https://arxiv.org/abs/2502.04878) | Whether a unique "correct" feature set (and L0) exists |
| Important | Karvonen et al., "SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability", ICML 2025 (https://arxiv.org/abs/2503.09532) | Multi-metric evaluation across L0; gives alternatives to probing |
| Important | Elhage et al., "Toy Models of Superposition", 2022 (https://arxiv.org/abs/2209.10652) | Standard toy setting with overcomplete features |
| Important | Paulo & Belrose, "Sparse Autoencoders Trained on the Same Data Learn Different Features", 2025 (https://arxiv.org/abs/2501.16615) | Non-uniqueness of learned dictionaries |
| Helpful | Makelov, Lange, Nanda, "Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control", 2024 (https://arxiv.org/abs/2405.08366) | Ground-truth style SAE evaluation |
| Helpful | Rajamanoharan et al., "Improving Dictionary Learning with Gated Sparse Autoencoders", 2024 (https://arxiv.org/abs/2404.16014) | Another way L0 is controlled (L1-style architectures) |
| Worth discussing (recent preprint, not required) | Balagansky et al., "Train One Sparse Autoencoder Across Multiple Sparsity Budgets…", 2025 (https://arxiv.org/abs/2505.24473) | Multi-sparsity SAEs |

**Citation check (E7).** [6] is described accurately (§5, matches its abstract); [5] and [18] are plausible. [10, 15, 7] as "implying any L0 is equally valid" and [11, 4] as supporting "too low an L0 leads to worse" could not be checked from the text: Questions, not errors.

### Questions for Authors
1. Quote the passages in [10], [15], [7] that imply any L0 is equally valid; absent them, the framing in §1 should be softened.
2. In the toy model, does L0 matter independently of SAE width? A (width, L0) grid would raise my Novelty and Technical scores.
3. How does your claim relate to Leask et al.'s finding that SAE latents are not atomic: if the "true feature set" is not canonical, what does "true L0" mean in an LLM?

### Limitations Assessment
**Partially.** A.6 is honest about scope; §6 says the correct L0 depends on the dataset but does not discuss that "true features" may not be unique.

### Pool position and scores
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful idea with a thin novelty delta against hedging and a related-work section that omits the closest verified prior work; evidence scale below the claim.

| NeurIPS-style | Score | Rationale |
|---|---|---|
| Quality | 2 | Heuristic metric; limited validation |
| Clarity | 3 | Readable |
| Significance | 3 | A practical lever for SAE trainers |
| Originality | 2 | Same mechanism as hedging, new framing/statistic |

| Dimension | Score | Descriptor | Rationale |
|---|---|---|---|
| Technical Rigor | 58 | Competent | Toy analysis sound; metric ungrounded |
| Clarity & Presentation | 66 | Competent | Clear but thin related work |
| Novelty & Originality | 54 | Developing/Competent | Overlaps hedging; new estimator |
| Significance & Impact | 62 | Competent | Matters if validated |
| Experimental Validation | 48 | Developing | One LLM configuration |
| Reproducibility | 52 | Developing | Missing details; code link removed |
| Ethical Compliance | 66 | Competent | Nothing at stake |

**Overall: 3.** **Confidence: 4** (field familiarity; abstracts of the prior work checked via the literature check).

---

## Reviewer 3 (Perspective): Peer Review Report

**Paper:** Sparse but Wrong · **Reviewer:** Dr. Ravindra Chaudhary-Holt, Perspective (signal processing / computational neuroscience; fictional persona) · **Expertise:** compressed sensing, sparse coding · **Date:** 2026-11-10

### Summary
This is an interesting paper that asks a question sparse-coding people have long asked, whether the sparsity level is a free parameter, in the new setting of SAEs on LLM activations. A synthetic study shows reconstruction can prefer wrong dictionaries at low L0, and a decoder-based statistic is proposed to locate the right sparsity in real models, giving about 200–250 for one Gemma-2-2b layer.

### Strengths
**S1: Re-poses a classical model-order question for modern interpretability.** §1 cites Olshausen and Field [14]; in that literature the sparsity level and recoverability are tied (the identifiability of a dictionary depends on how many atoms are active), and the paper's Figure 1 gives an accessible demonstration for SAEs.
**S2: Practical diagnostic.** The statistic needs only activations and decoder weights (Eq. 3–4), no labels.
**S3: The asymmetry in A.3 is a striking, actionable result.** Figure 8: starting from too-high L0 recovers; starting from too-low does not. This suggests a schedule recommendation (anneal downward), which A.4 begins to formalize.

### Weaknesses

**W1: The toy model lacks superposition, and the assumption of a single "true L0" is untested for LLMs.** §3 uses 50 orthogonal features in R^100, whereas LLM features outnumber dimensions and have heavy-tailed frequencies; the number of active features per token surely varies. Two hidden assumptions: (i) a fixed set of atomic features exists (Leask et al. question this), and (ii) the average firing count is a meaningful target. §6 hopes the method "may give us hints as to the true number of firing features in superposition", which would be a notable result, but nothing validates that reading.
- **Suggested fix:** a toy with overcomplete features (more features than dimensions), unequal and heavy-tailed frequencies, and token-varying active counts; relate to classical recovery conditions (coherence, restricted isometry).

**W2: The external check measures usefulness, not correctness.** §4 uses k-sparse probing F1 as confirmation. Probing may favor larger L0 because more information is available, independent of whether latents are monosemantic. Connect to downstream uses that depend on feature correctness (steering, circuit analysis, concept erasure) and to classical model-selection tools (information criteria, elbow or minimum-description-length arguments) as baselines.
- **Suggested fix:** evaluate on at least one downstream use beyond probing and compare with a model-order-selection baseline.

**W3: The practitioner path is incomplete, and the cost side is absent.** A.4 says the automatic procedure "works very well in toy models" but is fragile in LLMs, so a user cannot yet set L0 with the method. At L0 ≈ 200–250, SAEs are more expensive to run and possibly harder to interpret (200–250 is roughly 4–6 times the median L0 of 40.5 for the gemma-2-2b SAEs in Figure 9, a derived comparison); the paper does not discuss this trade-off. Neither does it discuss that "too-high" SAEs are not the same as "wrong" ones for some uses.
- **Suggested fix:** report compute and an interpretability measure at the suggested L0 versus a typical L0 (for example 50) and state which uses benefit.

### Cross-disciplinary connections
Dictionary identifiability under sparsity and coherence (compressed sensing); K-SVD and matching pursuit with known sparsity as references for "correct sparsity" in classical dictionary learning; population-sparseness measures in neural recordings as an analogue of "average active latents"; intrinsic-dimension and effective-rank estimators as alternative ways to estimate the number of active components without training many SAEs.

### Questions for Authors
1. In the toy model, what happens if features outnumber dimensions? A positive answer would raise my Significance score.
2. What does the s_dec_n curve look like if the true L0 varies by token (for example a mixture of two active-count regimes)?
3. Does the 200–250 optimum hold for a 16k-width SAE or a 131k-width one? (The paper suggests a dependence in §6.)

### Limitations Assessment
**Partially.** Single-layer scope is stated (A.6); the assumption that a true L0 exists is not discussed.

### Ethics Review Flag
**No.** No human data or misuse pathway. A mild note: over-confident claims about "correct" features could give false assurance in safety-motivated interpretability use.

### Pool position and scores
**Pool position:** better than about 68% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, practical insight on a question that matters for SAE training, with a clean ground-truth illustration, even though its evidence is narrow.

| NeurIPS-style | Score | Rationale |
|---|---|---|
| Quality | 2 | Narrow evidence |
| Clarity | 3 | Clear |
| Significance | 3 | Practical, widely relevant |
| Originality | 3 | New framing + estimator |

| Dimension | Score | Descriptor | Rationale |
|---|---|---|---|
| Technical Rigor | 62 | Competent | Sound toy logic; heuristic metric |
| Clarity & Presentation | 68 | Competent | Clear |
| Novelty & Originality | 66 | Competent | New framing for L0 and estimator |
| Significance & Impact | 72 | Competent/Strong | Affects how SAEs are trained |
| Experimental Validation | 54 | Developing/Competent | Narrow |
| Reproducibility | 58 | Competent | Details missing, code promised |
| Ethical Compliance | 68 | Competent | Nothing at stake |

**Overall: 4** (Borderline Accept): the question is important and the toy result is convincing; I weigh potential influence on SAE practice above the narrow validation. **Confidence: 3** (not an SAE specialist).

---

## Reviewer 4 (Generalist): Peer Review Report

**Paper:** Sparse but Wrong · **Reviewer:** Dr. Mei-Lin Abernathy-Zhou, Generalist (ML group, East Asia; fictional persona) · **Expertise:** representation learning · **Date:** 2026-11-10

### Summary
The paper tells practitioners that the sparsity level of an SAE should not be treated as a free choice. A synthetic experiment shows that when the sparsity is too low the SAE learns blended features that reconstruct better than the correct ones, and when too high it also produces blended solutions. A new score computed from decoder projections is minimized near the true sparsity in the toy case, and near L0 200–250 for a Gemma-2-2b SAE family, where sparse-probing performance also peaks. The authors conclude many public SAEs use too little sparsity budget.

### Strengths
**S1: A clear, memorable message that a non-specialist can follow.** Figure 1 (three heatmaps at L0 5, 11, 18) and the §3.1 sentence "MSE loss actively incentivizes low L0 SAEs to learn incorrect latents" convey the point immediately.
**S2: The paper is concise and the logical flow is easy to follow:** toy model → why MSE misleads → a metric → LLM check → implications (§3–§6).
**S3: Honest about the limits of the practical tool.** A.4 and A.6 state that the automatic procedure is hard to tune in LLMs and that only one layer was studied.

### Weaknesses

**W1: The LLM evidence is small relative to the claim being made to the community.** The LLM section (§4) is about one page with two figures: one model, one layer, one width, one training budget. A general reader would expect the headline statement "most commonly used SAEs have an L0 that is too low" to be backed by more than a histogram (Figure 9) and one estimate. ICLR accepts insight papers, but those typically verify the main claim across several settings.
- **Suggested fix:** add at least a second layer and a second width, and narrow the abstract if not.

**W2: Presentation: the central argument and the method sit in the appendix, and notation drifts.** The reconstruction-cheating comparison (A.2, Figure 6) is the strongest evidence for C2 but is outside the main text; the practical tuning procedure is in A.4. In the main text the justification for s_dec_n is verbal (§3.2), the quantity is called n, N and k in different places (Figure 2, Figure 3, A.7), and §3.2 text and Figure 2 give different values (n=18/22 vs N=12/20). Eq. 3 may carry a transpose inconsistent with the stated shape of W_dec (§2), which could be an extraction artifact. Related work is four sentences (§5).
- **Suggested fix:** move Figure 6 into the main text, unify notation, state hyperparameters and a one-paragraph intuition for the metric.

**W3: The abstract and discussion say more than the experiments show.** "if L0 is not set precisely" is not quantified (three L0 values in Figure 1; the metric is flat above the true L0 per A.4); "the same decoder patterns we observe in our toy model" is asserted in §1 for Gemma, while Figures 3–4 show only a curve minimum. §6's "important implications for the field" depends on C4.
- **Suggested fix:** qualify the abstract to the studied settings.

*Minor:* typos ("We sampling", "our investigated"); the acknowledgments section appears to identify a funded author, which an anonymization check should consider (no effect on my scores); no LLM-use or reproducibility statement found after search, so check the venue's current requirements.

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|---|---|---|
| Soundness: claims supported | Partly | C1/C2 yes (§3, A.2); C3/C4 partial (§4, A.5) |
| Presentation: clear, organized | Met | §1–§6; Figure 1 |
| Contribution: significant for the community | Partly | Practical message; narrow validation |
| Reproducibility | Partly | Code link removed; toy hyperparameters missing (§3) |
| Limitations stated | Partly | A.6 only |

### Contribution in one paragraph
SAE sparsity affects whether features are correct; the paper gives a toy proof of concept, a candidate detector and a one-model case study. If it holds up, it changes how SAE trainers choose L0.

### Questions for Authors
1. What would change your conclusion if a second layer gave a different optimum? (If not, state the claim only for layer 12.)
2. Can Figure 6 be moved into the main paper?
3. How was n=18/22 vs N=12/20 resolved?

### Limitations Assessment
**Partially** (A.6).

### Ethics Review Flag
**No.**

### Pool position and scores
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is clear and relevant and the weaknesses (single configuration, single seed, thin related work) are typical of accepted insight papers, although at the thin end.

| NeurIPS-style | Score | Rationale |
|---|---|---|
| Quality | 2 | Evidence narrower than claims |
| Clarity | 3 | Clear, appendix-heavy |
| Significance | 3 | Relevant to SAE practice |
| Originality | 3 | Fresh framing, new metric |

| Dimension | Score | Descriptor | Rationale |
|---|---|---|---|
| Technical Rigor | 60 | Competent | Sound toy; heuristic metric |
| Clarity & Presentation | 70 | Competent | Clear flow, small notation issues |
| Novelty & Originality | 62 | Competent | New framing |
| Significance & Impact | 68 | Competent | Practical |
| Experimental Validation | 52 | Developing/Competent | One configuration |
| Reproducibility | 56 | Competent | Gaps |
| Ethical Compliance | 66 | Competent | Nothing at stake |

**Overall: 4** (Borderline Accept): reasons to accept (clear, practically relevant insight) narrowly outweigh the thin validation. **Confidence: 4.**

---

## Devil's Advocate Report

**Paper:** Sparse but Wrong · **Reviewer:** Dr. Oluwaseun Brandt-Ferreira, Devil's Advocate (evaluation methodology, South America; fictional persona)

### Steelman
In a world where we know the true features, a too-low L0 makes reconstruction prefer blended features (§3.1: 2.73 vs 4.88), so loss-based comparisons across L0 are not trustworthy. A decoder-statistic minimum matches the true L0 in the toy, and in Gemma-2-2b it lines up with the best downstream probing, so real SAEs can be told to need far more active latents than commonly used.

### Core Argument Chain
1. P1: In a toy model with correlated features, low-L0 SAEs mix features while the correct dictionary has worse MSE (Fig. 1, §3.1, A.2).
2. P2: s_dec_n is minimized at the true L0 in the toy (Fig. 2).
3. P3: In Gemma-2-2b layer 12 (32k) s_dec_n is minimized at L0 ≈ 200–250 and probing F1 peaks there (Figs 3–4).
4. P4: Therefore 200–250 is the "correct" L0 for those SAEs.
5. P5: Most open-source SAEs use L0 < 100 (Fig. 9).
∴ Most commonly used SAEs have too low an L0 and learn incorrect features.

### Strongest Counter-Argument
The chain breaks at P3→P4→P5. In an LLM there is no true L0: the paper's "correct" value is defined by two coarse agreeing curves. The first, s_dec_n, has a minimum inside a flat plateau (A.4: "relatively flat in a region start at the correct L0 and extending to higher L0 values") on a grid of 10-step points, and its slope and shape change with the choice of n (§3.2, §4, Figure 3 caption). The second, k-sparse probing, can improve with L0 for reasons unrelated to feature correctness: more active latents carry more information per token. Two curves peaking in the same broad region is not evidence that either measures correctness. Moreover the entire LLM family has one width (32k), one layer and one 500M-token budget: the optimum of both curves plausibly depends on width (the paper's own cited hedging work shows width matters), training tokens and layer. Then P5 compares open-source SAEs of many widths, layers, models and architectures (Fig. 9: gemma-2-2b, gemma-2-9b, gpt2-small, Llama-3.1-8B) with a number valid at most for one configuration. The conclusion "most commonly used SAEs have an L0 that is too low" and the Discussion's "the L0 used by most SAEs is lower than it ideally should be" therefore are not tested. A final point: even if true, the paper offers no usable procedure; A.4 concedes it "requires a lot of hyperparameter tuning to work in real LLMs". The result as it stands is a clean toy lesson and a one-configuration observation, whereas its framing in the abstract is universal and normative.

### Issue List

#### CRITICAL Issues
**No CRITICAL issues found.** The toy result (C2) is internally sound and the LLM curves support at most a narrower claim; the problems are overclaiming and thin validation, which are fixable by narrowing claims or adding experiments (none meets criteria 1–7: no leakage, no contradiction of the paper's own results, no fabrication signal).

#### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic/Evidence | §4, Figs 3–4 | "Correct L0" in an LLM is defined only by two coarse, proxy-based minima/maxima; probing can favor larger L0 independent of correctness. Evidence supports a weaker claim ("both metrics peak near 200–250 for this SAE family"). | Add correctness-oriented metrics and CIs; narrow wording |
| DA-M2 | Scope | Abstract, §6, A.5, Fig. 9 | "Most commonly used SAEs have an L0 that is too low" extrapolates from one layer/width/model to all SAEs (E5). | Restrict, or add width/layer/architecture sweeps |
| DA-M3 | Evidence/Alt. explanation | §3, Fig. 1 | Toy has orthogonal features (no superposition) and unstated width; low-L0 "mixing" cannot be separated from width-driven hedging. | Width × L0 grid in toy; overcomplete features |
| DA-M4 | Logic | §3.2, A.4 | Metric minimum is in a flat region and depends on n; no derivation; for L0 > n the metric mechanically reads a firing latent. | Define estimator, analyze a case analytically, report uncertainty |
| DA-M5 | Evidence | §4 | One seed per L0, 500M tokens, 32k width; high-L0 SAEs may be under-trained; no variance. | Seeds and token-budget ablation |

#### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §3.2 vs Fig. 2 | n=18/22 in text vs N=12/20 in figure |
| DA-m2 | Consistency | A.3 vs §3.1 | "higher MSE loss" contradicts 2.73 < 4.88 |
| DA-m3 | Clarity | Figs 2–3, A.7 | n, N, k used interchangeably |
| DA-m4 | Utility | A.4 | Tuning procedure not demonstrated in LLMs |

### Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| True L0 of toy from stated probabilities (P0 = 0.345 → P49 = 0.05, linear, 50 features) | 11 | 50 × (0.345 + 0.05)/2 = 9.875 | No if these are marginals; unresolved because Fig. 5 labels them "base" probabilities (a question, not an error) |
| MSE ratio, learned vs ground-truth at L0 = 5 | 2.73 vs 4.88 ("much worse") | 4.88 / 2.73 ≈ 1.79× | Yes (consistent) |
| n used for Figure 2 | n=18, n=22 (§3.2) | Caption: N=12, N=20 | No |
| Gemma-2-2b Neuronpedia SAEs below L0 100 | "most" (A.5) | mean 93.0, median 40.5 (40 SAEs) | Plausible; layers/widths mixed |

### Claim Distortion Check (E5)
- "fails to learn the underlying features of the LLM" (Abstract): the LLM has no known underlying features; at most "the SAE's features degrade" is measurable in the toy → **overstated**.
- "most commonly used SAEs have an L0 that is too low": unsupported as worded → **MAJOR**.
- "finds the true L0 in toy models" (Abstract): one toy model, one run; the metric's minimum lies in a flat region → **partly supported**.
- "L0 too high ⇒ degenerate solutions": §3 itself says "when L0 is too high the SAE still learns many correct latents" → **partly supported**.

### Ignored Alternative Explanations
- Width, training tokens and decoder-normalization choices determine the apparent optimal L0; not varied.
- Probing performance rising with L0 because of information content, not feature correctness.
- s_dec_n reflecting latent density/frequency structure (dense latents project strongly on arbitrary inputs) instead of "mixing".
- In the toy: low-L0 mixing explained by width relative to the number of features (hedging) rather than L0.

### Missing Stakeholder Perspectives
Practitioners with public SAEs (they may retrain needlessly); safety-motivated users (false assurance about "correct" features); compute-constrained groups (higher L0 raises downstream cost).

### Observations (Non-Defects)
The comparison against a hand-built ground-truth SAE (A.2) is robust to most counter-arguments and is the paper's strongest evidence; the A.3 asymmetry is an interesting, falsifiable observation; limitations in A.6 are honestly stated.

### Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Heuristic metric, flat minimum |
| Clarity & Presentation | 66 | Clear but appendix-heavy |
| Novelty & Originality | 50 | Overlaps hedging; estimator is new |
| Significance & Impact | 58 | Relevant if validated |
| Experimental Validation | 40 | One configuration, no variance |
| Reproducibility | 50 | Missing toy hyperparameters |
| Ethical Compliance | 64 | Nothing at stake |

**Pool position:** better than about 48% of submissions. **Overall: 3 | Confidence: 4**

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W5 | kept | Specific, located, paper does not answer them |
| R1 | Draft "s_dec_n evaluated on training data, no held-out" | rewritten as Question 1 | The paper does not say which inputs; cannot assert |
| R1 | Eq. 3 transpose, A.4 formula | moved to Questions 3 | Possible extraction artifacts (Hard Rule 10) |
| R2 | W1 (hedging overlap) | rewritten | Initially "must be compared"; hedging is a *recent preprint*, so it is positioning only, and the claim now matches the cited abstract |
| R2 | W3 straw-man framing | rewritten as question | Cited papers' wording not verifiable from the provided text |
| R3 | W1–W3 | kept | Located; fixes given |
| R4 | W2 Eq. 3 notation | kept as "may" with extraction caveat | Not asserted as an error |
| R4 | Minor line (typos, anonymization note, LLM-use statement) | moved to Minor | Cosmetic |
| DA | DA-M1 "no error bars" | rewritten | Figures unavailable: now "no uncertainty stated in text or caption" |
| DA | DA-m2 | kept | Verified against §3.1 |

No scores were changed.

---

# Phase 2: EIC Meta-Review and Decision

*(Synthesizer part A: issue list and official score, then EIC.)*

### Synthesizer package: merged issues
| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | LLM validation: one layer/width/seed, no variance, proxy-only | R1-W1, R1-W4, R4-W1, DA-M1, DA-M5, R3-W2 | CONSENSUS-4 (hinge) |
| I2 | "Most SAEs too low" overclaim | R1-W5 (ERR-3), R4-W3, DA-M2, R3 (assumption audit) | CONSENSUS-4 (hinge) |
| I3 | Toy lacks superposition, hedging confound, unstated width | R1-W2 (ERR-2), R3-W1, DA-M3 | CONSENSUS-3 |
| I4 | s_dec_n heuristic, flat minimum, n-dependence | R1-W3, DA-M4, R4-W2 | CONSENSUS-3 (hinge) |
| I5 | Thin related work; hedging overlap; no selection baseline | R2-W1/W2/W3, R3-W2 | CONSENSUS-2 |
| I6 | No usable procedure to set L0; cost side | R3-W3, DA-m4 | CONSENSUS-2 |
| I7 | Significance/novelty weight | R3, R4 (positive) vs R1, R2, DA | SPLIT |
| — | DA-CRITICAL | none | none |

Official output (before EIC weights): ratings R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40; official composite 58.1; no consistency warnings; no dimension spread above 20.

### The Case For and Against
- **For acceptance:** The paper asks a question every SAE trainer faces and answers it with a crisp, controlled demonstration: with ground truth, a low-L0 SAE beats the correct dictionary on MSE (§3.1: 2.73 vs 4.88), and the sparsity–reconstruction tradeoff is thus a biased guide. The decoder-projection statistic is cheap, and the observation that its minimum and sparse-probing F1 line up in Gemma-2-2b is suggestive. If right, it changes practice.
- **Against acceptance:** The LLM claims (C3, C4) rest on a single model, layer, width and seed with no uncertainty and one proxy metric; the metric is a heuristic with no derivation and a flat minimum; the toy model lacks superposition and key hyperparameters; the headline "most commonly used SAEs have an L0 that is too low" is extrapolated from one configuration. The mechanism is acknowledged to be feature hedging.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Only one model/layer/width studied | R1-W1, R4-W1, DA-M5 | §4, A.6, Fig. 3 caption | Verified | "We limit our investigated to Gemma-2-2b layer 12" |
| Toy uses orthogonal features, no superposition | R1-W2, R3-W1, DA-M3 | §3 | Verified | "50 mutually orthogonal true features… ∈ R100" |
| Toy SAE width/lr/batch not stated | R1 ERR-2 | §3, A.1–A.3 | Verified | Text search found only 15M samples and A.3 steps |
| n=18/22 (text) vs N=12/20 (caption) | R1 ERR-1, DA-m1 | §3.2, Fig. 2 | Verified | Minor, reproducibility |
| Flat region above true L0 | R1-W3, DA-M4 | A.4 | Verified | "relatively flat in a region start at the correct L0…" |
| "Most SAEs too low" rests on pooled histograms plus one estimate | R1 ERR-3, DA-M2, R4-W3 | §6, A.5, Fig. 9 | Verified | A.5 sets "200-250" for layer 12 of Gemma-2-2b, then compares all Neuronpedia SAEs |
| No variance or error bars in §4 | R1-W1/W4, DA-M1 | §4, Figs 3–4 | Partly correct | Not stated in text or captions; figures unavailable |
| Low-L0 mixing is the hedging mechanism | R2-W1 | §1, §5, [6] | Verified (as positioning) | Cited abstract matches; differs on the capacity driver; recent preprint, so not a required comparison |
| Expected L0 from base probabilities ≈ 9.875 ≠ 11 | DA, R1 Q2 | §3, Fig. 5 | Partly correct | Plausible only if probabilities are marginals; question |
| A.3 "higher MSE loss" wording | R1 ERR-4, DA-m2 | A.3 vs §3.1 | Verified | Wording slip, minor |
| Eq. 3 transpose, A.4 bias formula | R1 Q3, R4-W2 | Eq. 3, A.4 | Unverifiable | Extraction artifact possible |
| Probing can rise with L0 independent of correctness | DA-M1, R3-W2 | §4 | Partly correct | Plausible mechanism, not shown in the paper |
| Text of Neuronpedia stats | DA table | A.5, Fig. 9 | Verified | mean 93.0, median 40.5 for 40 gemma-2-2b SAEs |

Literature check: no weakness rests on recent or concurrent work as a requirement (hedging is positioning only); all recommended references were found by the script or by `verify`; no text overlap; no under-reported baselines.

**Integrity note for the editor (factual, no score effect):** the integrity scan found no text addressed to reviewers or AI systems. The acknowledgments section names a funded author, which may bear on anonymization; this has no effect on any score or on the decision.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log entry checked and holds; decisive points (single config, missing toy hyperparameters, flat metric) verified; calibrated to ICLR. |
| R2 (Domain) | 3 | 4 | 1.0 | Hedging comparison stated faithfully to the abstract; references verified; one point (straw-man framing) is a question. |
| R3 (Perspective) | 4 | 3 | 1.0 | Fair, constructive; its assumption audit is verified; lenient on evidence scale but not wrong. |
| R4 (Generalist) | 4 | 4 | 1.0 | Sound, typical PC review; presentation points verified. |
| DA | 3 | 4 | 1.0 | Counter-argument survives checking; no CRITICAL claimed, consistent with the calibration. |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised (0 raised, 0 upheld). DA-M1 (LLM "correct L0" not independently validated) was checked against the AC test and the strict criteria: the evidence supports a weaker claim (both metrics peak near the same L0 for this SAE family), so it is a narrowing fix, not criterion 1 or 2. No selection on a reported test set was found (protocol sweep). **DA ceiling: none.**

### Final Decision and Justification
The EIC-weighted rating is 3.36 → starting point **3**; the composite cross-check (EIC 57.7, band 3) agrees, so no ⚠ flag. I keep the starting point. The core contribution is real and likely to be useful, and the toy result alone would be a nice workshop-level finding. For ICLR, however, the paper's own headline claims (C3, C4) are not tested at the scale they are stated: verified in §4/A.6 (single layer, width, seed), A.4 (flat minimum), A.5/§6 (extrapolation). The weaknesses are not the "ordinary" ones of accepted papers (single seed on a huge benchmark, a missing baseline), because the missing evidence is the evidence for the main practical claim. They are fixable by narrowing claims plus a moderate set of additional runs, so the paper is a plausible resubmission rather than a rejection on fundamentals; hence 3, not 2. **Pool position (EIC): better than about 56% of ICLR submissions**, deciding evidence: a clean toy demonstration and relevant question against single-configuration LLM validation with no variance. Judged as a simulation of how a careful panel might see this draft, not a prediction of any outcome.

**Final (EIC): 3.** Does not exceed the ceiling (no ceiling).

---

# Editorial Decision

**Paper:** Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders · **Date:** 2026-11-10 · **Target Venue:** ICLR | **Paper Type:** Analysis
**Review Team (fictional personas):** EIC Valdemar-Osei; R1 Okafor-Lindqvist (Methodology), R2 Varga-Mendes (Domain), R3 Chaudhary-Holt (Perspective), R4 Abernathy-Zhou (Generalist), DA Brandt-Ferreira

## Decision: Borderline Reject (3), ICLR label: 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); scale status: secondary

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 58.1
**EIC assessment** (internal): weighted rating 3.36 → starting point 3 · weighted composite 57.7 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3

### Score Summary: Official Scores and EIC Assessment (from `aggregate_scores.py`)
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|------|------|------|
| Technical Rigor | 52 | 58 | 62 | 60 | 50 | 56.4 | 56.2 | 12 |
| Clarity & Presentation | 66 | 66 | 68 | 70 | 66 | 67.2 | 67.2 | 4 |
| Novelty & Originality | 54 | 54 | 66 | 62 | 50 | 57.2 | 56.9 | 16 |
| Significance & Impact | 60 | 62 | 72 | 68 | 58 | 64.0 | 63.7 | 14 |
| Experimental Validation | 42 | 48 | 54 | 52 | 40 | 47.2 | 47.0 | 14 |
| Reproducibility | 48 | 52 | 58 | 56 | 50 | 52.8 | 52.6 | 10 |
| Ethical Compliance | 66 | 66 | 68 | 66 | 64 | 66.0 | 65.9 | 4 |
| **Composite** | 54.4 | 57.4 | 64.3 | 61.9 | 52.4 | **58.1 (before)** | **57.7 (after)** | |

Paper-type weights (analysis): rigor 0.25, clarity 0.10, novelty 0.20, significance 0.20, experimental validation 0.15, reproducibility 0.05, ethics 0.05. Reviewer weight shares after EIC weighting: R1 0.246, R2 0.197, R3 0.162, R4 0.197, DA 0.197. No dimension spread exceeds 20 and no consistency warnings were raised.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); recent analyses report the former for 2026, verify against the current form |
| Confidence | R1 4, R2 4, R3 3, R4 4, DA 4 |

*Not requested: Cross-Venue Outlook, journal recommendation, venue-format rendering.*

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders" to ICLR. The question you raise, whether SAE sparsity is a free parameter, is relevant to anyone training SAEs, and the paper is concise and clear.

**Overall Assessment:** The panel found the toy demonstration persuasive and the practical message valuable, but considered the LLM evidence for the headline claims too narrow, and the decoder-projection statistic under-justified.

**Key Strengths Identified by Reviewers:**
1. A controlled ground-truth experiment showing that a corrupted low-L0 dictionary beats the correct one on MSE (§3.1, A.2) (R1, R2, R4, DA).
2. A cheap, label-free statistic and an interesting asymmetry in recovery when L0 is adjusted during training (§3.2, A.3) (R1, R3).
3. Clear writing and honest limitations in A.4/A.6 (R4, R3).

**Key Concerns Requiring Attention:**
1. The LLM claims rest on one layer, width, seed and a proxy metric, with no variance (CONSENSUS-4: R1, R3, R4, DA).
2. "Most commonly used SAEs have an L0 that is too low" is extrapolated from one configuration (CONSENSUS-4: R1, R3, R4, DA).
3. The toy model has no superposition, an unstated width, and the minimum of s_dec_n is in a flat region and depends on n (CONSENSUS-3: R1, R3, DA / R1, R4, DA).
4. The mechanism overlaps feature hedging and related work is thin (R2, R3).

**Devil's Advocate:** No CRITICAL issue was raised. Its strongest objection, that "correct L0" in an LLM is defined by two coarse proxy curves and a single configuration, is rated MAJOR and must be addressed by narrowing claims or adding experiments.

**Decision: Borderline Reject.** The evidence supports a narrower paper than the one claimed. A revision that restricts the claims to what the studied setting shows, or adds layer, width and seed replication with correctness-oriented metrics, would materially change our view. Please see the Revision Roadmap.

Sincerely, Prof. Ingrid Valdemar-Osei, Editor-in-Chief (meta-reviewer, fictional persona)

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers)
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| Single-configuration, no-variance LLM validation | R1, R3, R4, DA | CONSENSUS-4 |
| "Most SAEs too low" overclaim | R1, R3, R4, DA | CONSENSUS-4 |
| Toy model realism/unstated hyperparameters | R1, R3, DA | CONSENSUS-3 |
| s_dec_n heuristic, flat minimum | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the paper's significance enough despite thin evidence? | R3, R4 (Overall 4) | R1, R2, DA (Overall 3) | The missing evidence is the evidence for the main practical claim, not a side result (verified); R1's weight is higher for verified points; decision 3 |
| Novelty vs feature hedging | R3, R4 positive | R2, DA | Positioning issue only (recent preprint); novelty is medium |

### Score Spread Discussion
No dimension exceeds the 20-point flag; the widest spreads are Novelty (16) and Significance (14), driven by R3 and R4 versus R1/DA.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Correct L0 defined by proxy curves | Yes (R1-W4, R3-W2) | n/a | New experiments |
| DA-M2 | MAJOR | Overextension to "most SAEs" | Yes (R1-W5, R4-W3) | n/a | Wording or experiments |
| DA-M3 | MAJOR | Toy without superposition/width control | Yes (R1-W2, R3-W1) | n/a | New experiments |
| DA-M4 | MAJOR | Metric minimum in flat region, n-dependence | Yes (R1-W3) | n/a | Analysis |
| DA-M5 | MAJOR | One seed, one budget | Yes (R1-W1) | n/a | New runs |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Narrow "most SAEs too low" and "precisely" to what is shown (E5) | R1-W5/ERR-3, DA-M2, R4-W3 | Abstract, §6, A.5 | Restrict to Gemma-2-2b layer 12, 32k, BatchTopK; label Fig. 9 as descriptive | Low | Yes |
| R2 | Replicate the LLM result across layers/widths with seeds and CIs | R1-W1, DA-M5, R4-W1 | §4, Figs 3–4 | ≥3 layers, ≥2 widths, 3 seeds on coarse grid, bootstrap minima (my estimate 100–300 GPU-h) | High | Partly (subset) |
| R3 | Add a correctness-oriented check beyond sparse probing and CIs for F1 | R1-W4, DA-M1, R3-W2 | §4, Fig. 4 | Absorption/concept-isolation metrics; task-level bootstrap | Medium (≈20–60 GPU-h) | Partly |
| R4 | Define the L0 estimator for s_dec_n and justify it | R1-W3, DA-M4, R4-W2 | §3.2, A.4 | Argmin/knee estimator with uncertainty; analytic toy case; fix n/N mismatch | Low–Medium | Yes |

### Priority 2: Strongly Suggested
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Toy model: overcomplete features, width × L0 grid, multiple seeds/correlation matrices, state all hyperparameters | R1-W2/ERR-2, R3-W1, DA-M3 | See W2 | Low (CPU/1 GPU) | Yes |
| S2 | Differentiate from feature hedging; add Leask et al., Elhage et al., SAEBench, Paulo & Belrose | R2-W1/W2 | State what is new; expand §5 | Low | Yes |
| S3 | Add L0-selection baselines (MSE elbow, probing-only, absorption) | R2-W3, R3-W2 | Compare on toy and on Gemma | Medium | Partly |
| S4 | Move Fig. 6 into the main text; unify notation | R4-W2 | Edit | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Cost/interpretability trade-off at L0 ≈ 200–250; utility of A.4 procedure | R3-W3, DA-m4 | Report cost and an interpretability measure |
| N2 | A.3 "higher MSE" wording; typos; Eq. 3 transpose; A.4 bias formula; anonymization check of acknowledgments | R1-ERR-4, DA-m2, R4 | Fix |
| N3 | Cross-field connections (model-order selection, identifiability conditions) | R3 | Discuss |

### Estimated Revision Effort
- Priority 1: 4 items, about 2–4 weeks (dominated by SAE training for R2/R3); R1 and R4 are days.
- Priority 2: 4 items, about 1 week.
- Priority 3: 3 items, 1–2 days.
- **Total:** roughly 3–5 weeks including compute (estimates, not measured).
