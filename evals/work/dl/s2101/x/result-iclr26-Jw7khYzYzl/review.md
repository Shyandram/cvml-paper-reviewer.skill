# Academic Paper Review: "Benchmarking Optimizers for Large Language Model Pretraining"

*Simulated peer review (a careful panel's likely view of this draft, not a prediction of any outcome). Date: 2026-11-05. Request: target venue ICLR, full review, skip confirmation, literature check strict, cutoff 2025-09-24. The five reviewer passes were run sequentially in one shared model context; they were not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only, and numbers read off plots are marked unverifiable.*

---

## Phase 0: Field Analysis and Reviewer Configuration

### 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Benchmarking Optimizers for Large Language Model Pretraining |
| Primary Discipline | Machine learning → optimization for LLM pretraining |
| Secondary Discipline(s) | Scaling laws / hyperparameter transfer; numerical linear algebra (orthogonalization, preconditioning); training systems |
| Paper Type | Benchmark (composite weights: benchmark); also carries an analysis/insight component |
| Core Technique(s) | AdamW, ADOPT, AdEMAMix, Lion, Signum, Muon/D-Muon, SOAP, Sophia, Schedule-Free AdamW, Prodigy, MARS; Llama-style dense models (124M–720M), a 520M MoE; FineWeb |
| Target Venue | ICLR (stated by the user); profile key `iclr`, scale status `secondary` |
| Venue-Specific Notes | None (no contribution-type or scope gate at ICLR). Accepted share ≈ 27% of submissions (venue_profiles.md) |
| Paper Maturity | Submission-ready (arXiv-style preprint, "Preprint. Under review.") |
| Ethics-Relevant Content | None (no human data; public web-text corpus FineWeb; compute/energy footprint of about 30000 GPU hours is stated) |
| Integrity scan | `integrity_scan.py`: no reviewer-directed text or hidden characters found. None noticed while reading. Reviewers read the redacted copy (identical to the source). |

### Claimed Contributions (as stated by the authors, "Contributions" list in §1)
1. **C1** (resource/result): "the first large-scale, controlled benchmark of 11 different optimization methods across diverse LLM training scenarios", dense and MoE, with "precise accounting for compute costs, and extensive hyperparameter tuning".
2. **C2** (result): "comprehensive ablations of critical training hyperparameters": warmup, initialization, gradient clipping, final learning rate, scheduler (plus weight decay, β's), giving "actionable insights".
3. **C3** (resource): an open-sourced benchmarking toolkit (training scripts, evaluation pipelines, hyperparameter configurations).

### Paper memory (factual record shared with all reviewers)
- **Setup (located):** Llama-like decoder with weight tying, SwiGLU, RMSNorm, RoPE; sizes 124M, 210M, 583M, 720M (§3, Table 1); 520M MoE with 8 experts, top-2 (§4.4, Table 47); FineWeb 100B-token subset, GPT-2 tokenizer, train/validation split (§3, App. C); sequence length 512 (§3); batch sizes 16k/131k/262k tokens (124M), 131k (210M, MoE), 2M (583M), 1M (720M) (§3). Durations 1–16.8B tokens (124M, 210M), 13B (583M), 8/16/48B (720M), 5.5/44B (MoE) (§3, Tables 3–6, 48). Chinchilla reference tokens 2.5B / 4.2B / 11.7B / 14.4B (Tables 3–6).
- **Tuning protocol:** hyperparameters swept at one near-Chinchilla horizon (2.1B tokens for 124M; 16B for 720M) and "kept" for longer runs (§3, App. E); 124M re-tuned partly at 16.8B (§4.1); 210M reuses 124M settings except LR (§4.2, App. E.2); 583M only z-loss ablation (App. E.3); MoE keeps dense hyperparameters untuned (§4.4). Cosine schedule and decay to 0.01 × γmax are the defaults (§3, §4.2). Effort: 2900 models, ~30000 GPU hours (§3, App. B).
- **Metric:** final validation loss on the full validation split (App. C); intermediate curves use a fixed set of 32 batches (App. C). No downstream evaluation (§5 Limitations).
- **Seeds/variance:** not stated for any benchmark run after search; only the wall-clock study uses 5 seeds (§4.3, Fig. 18).
- **Headline findings:** AdEMAMix best overall (Takeaway 1, 10, §5); MARS second at 720M/1M batch (Fig. 1, Takeaway 10); D-Muon consistent (Takeaway 10); SOAP strong at ≤ Chinchilla, AdamW narrows gap later (§4.3); sign-based methods benefit from larger batch but scale poorly with model size (Takeaways 2, 10); weight decay, β2/β3 re-tuning, warmup and final-LR matter (Takeaways 3, 5, 8, 14).
- **Appendix adds:** algorithm descriptions and implementation fixes (Sophia update rule, Signum weight decay and Nesterov; App. A), 2900-model breakdown (App. B), 124M/210M ablations (App. D.1, D.2), wall-clock (App. D.3), full hyperparameter tables (App. E, Tables 7–47). Code link anonymized in the provided text.
- **Unverifiable:** all figures (numerical gaps between optimizers, error-free curves), supplementary code.

### 👥 Review Team (fictional personas)

**EIC (meta-reviewer): Dr. Ingrid Valtonen-Okafor**, area-chair profile, optimization and training of large models (large public research university, Northern Europe). Senior / large-scale training, ML optimization theory. Reads all five reports first, checks decisive points, weights, decides. Style: asks "would this survive a different seed and scale?" but rewards useful, honest engineering science.

**Reviewer 1 (Methodology): Dr. Kwame Adjei-Lindqvist**, industrial research lab (North America). Senior scientist / hyperparameter tuning protocols, LLM training runs, optimizer evaluation. Focus: design, statistics, fairness, reproducibility. Style: insists on matched tuning budgets and variance estimates.

**Reviewer 2 (Domain): Prof. Ayelet Marchetti-Sun**, ML optimization group, public university (Middle East/Europe). Mid-career faculty / adaptive and second-order methods, scaling laws. Focus: literature, theory behind the optimizers, domain contribution. Style: checks every "first" against prior work.

**Reviewer 3 (Perspective): Dr. Joaquín Ferreyra-Holm**, national supercomputing and HPC center (Europe). Senior research engineer / numerical linear algebra, distributed training systems. Focus: deployment, sharding, cost, assumptions, broader impact. Style: constructive, thinks in terms of 100× scale and wall-clock.

**Reviewer 4 (Generalist): Dr. Lan Nguyen-Abara**, industrial LLM pretraining team (East Asia). Mid-career / LLM pretraining recipes, evaluation. Focus: clarity, venue fit, presentation. Style: typical program-committee member; reads as a practitioner.

**Devil's Advocate: Prof. Rhea Castellanos-Dubois**, statistics and evaluation methodology, public university (South America). Senior faculty / experimental design, benchmark validity. Focus: core-argument challenges. Style: rigorous, never hostile.

### Phase 1.5 Literature Check (strict, cutoff 2025-09-24; arXiv API)
Queries: 8 of 12 (6 claim: C1 ×4, C2 ×2; 1 baseline; 1 expansion); several over-long queries were refused and not counted. `benchmarks` found no external tabulated benchmark (the paper reports validation loss on its own runs), so the baseline scout has nothing to compare against (see addendum). `coverage` gaps closed except C3 (no close prior work found, arXiv only). `similarity`: no high conceptual overlap (cosine ≤ 0.27) and no text overlap (0 shared 8-grams). Closest prior works by similarity: "Muon is Scalable for LLM Training", "Surge Phenomenon in Optimal Learning Rate and Batch Size Scaling", "Power Lines: Scaling Laws for Weight Decay and Batch Size in LLM Pre-training"; by content the closest is Zhao et al. (cited as [161] in the paper).

---

## Phase 1: Independent Reviews

---

# Peer Review Report (Reviewer 1)

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Reviewer: Dr. Kwame Adjei-Lindqvist, Methodology (industrial research lab, North America; fictional persona)
## Expertise: LLM training protocols; hyperparameter tuning; optimizer evaluation
## Date: 2026-11-05

## Summary
The paper compares eleven optimizers (twelve counting plain Muon) for decoder-only pretraining on FineWeb at 124M–720M dense parameters and a 520M MoE, varying batch size and token budget from below to several times the Chinchilla horizon. Hyperparameters are tuned near the Chinchilla horizon and then reused. On top of the ranking the paper reports ablations on weight decay, warmup, scheduler, final LR, β2/β3, z-loss, and wall-clock. It concludes that AdEMAMix (and, at larger batch, MARS) beat a properly tuned AdamW while many methods do not.

## Strengths
### S1: A large, systematic tuning effort with full configurations
§3 and App. B report 2900 models and about 30000 GPU hours; App. E (Tables 7–47) lists the swept grids and the selected (bold) values per optimizer and scale. This is unusually complete for the area and supports Reproducibility.
### S2: A stronger AdamW baseline than several prior setups
§4.3 and Figure 16 show that a final LR of 0.01 × γmax, weight decay 0.1 and no z-loss change the AdamW-versus-SOAP ordering relative to a popular codebase setting. This is a concrete protocol finding (Takeaway 9) that matters for every future optimizer paper.
### S3: Informative ablations that expose protocol sensitivity
Figures 7, 10, 15, 21 and Takeaways 3, 5, 8, 14 show weight decay, warmup, final LR and β2/β3 re-tuning each moving the loss noticeably, and that the best value is optimizer- and horizon-dependent.
### S4: Honest scoping in several places
§5 states the 720M ceiling and the lack of downstream evaluation; §4.1 reports that Sophia diverges and removes it from the small-batch comparison rather than hiding it.

## Weaknesses
### W1: Rankings come from single runs with no variance estimate
Apart from the wall-clock study (times "with different seeds, compute the standard deviation"), none of the loss comparisons (Figures 1, 3, 5, 6, 13, 17, 19) reports seeds or error bars, and the paper does not state a seed policy. Several headline orderings are among a cluster of methods whose gaps (e.g., AdEMAMix vs SOAP vs D-Muon at 124M/210M, Figure 3(b), 14(c)) appear small in the plots (unverifiable from text). The scale here (124M–720M, ≤ 48B tokens) is small enough that variance is affordable, so this is not covered by the large-scale-single-run norm.
- **Suggested Fix:** 3 seeds for the top five and AdamW at 124M and 210M for two horizons ≈ 36 runs; using the paper's own average (≈ 30000/2900 ≈ 10 GPU-hours per run, derived) this is roughly 300–400 GPU-hours. Report mean ± std and mark which gaps exceed it.
### W2: Scheduler and final LR are chosen on AdamW and transferred, yet Takeaway 6 shows they are optimizer-specific
§4.2: "We study this effect on the AdamW method, and then apply the best-found heuristic to all other optimizers." The main rankings use cosine to 0.01 × γmax, but Takeaway 6 says "linear scheduler outperforms or matches cosine and WSD for sign-based methods, SOAP, and MARS", and footnote 2 notes the scheduler gap can reverse AdamW vs SF-AdamW. The main ranking is therefore not "carefully tuned" per method along this axis, and the tuning is arguably tilted toward the baseline.
- **Suggested Fix:** Report the main ranking at the best of {cosine, linear, WSD} per optimizer (≈ 2 extra runs per optimizer per setting at the headline scale) or state this as a limitation in §3 and soften "careful tuning of each method" in the abstract.
### W3: Tuning at one horizon and reusing settings favors optimizers whose optimum is horizon-invariant, and tuning effort differs across methods
§3: "we extensively tune optimization hyperparameters for a number of training tokens which" are near-Chinchilla, and "We then keep those hyperparameters when we increase the number of iterations." The paper itself shows β2 and β3 must be re-tuned for longer runs (Figure 21, Takeaway 14), but only SOAP/AdEMAMix/AdamW are shown re-tuned. App. B lists unequal counts (≈ 750 AdamW, 354 SOAP, 238 AdEMAMix, 135 D-Muon, 133 SF-AdamW, 20 MARS-Shampoo). Equal tuning effort is a stated pillar of the contribution (C1). It is unclear whether Figures 3(b)/5(b) use the 16.8B re-tuned values for every optimizer or only for some (§4.1 says methods are "additionally re-tuned", Table 7 lists the grids).
- **Suggested Fix:** Add a table of tuning budget per optimizer (runs, grid size, tuned horizon) and state exactly which results use 2.1B- versus 16.8B-tuned values. Re-tune the leading five at the longest horizon on equal budgets.
### W4: Transfer claims rest on thin evidence
Takeaway 2(II) says that after re-tuning "doubling of number of iterations does not affect the ranking of methods", from one 124M run at 33.6B tokens (§4.1, Figure 6 right); the Figure 6 caption itself says the SOAP–AdEMAMix gap narrows and then depends on β3. Takeaway 12 ("Benchmarking results obtained for dense models transfer to corresponding MoEs.") rests on one MoE configuration with untuned hyperparameters and a top-rank change at 336k steps (Figure 19 caption: "SOAP outperforms AdEMAMix in 336k steps run").
- **Suggested Fix:** Replace "does not affect" and "transfer" by "largely preserves the ordering in our two settings", and add one more scale at the long horizon if affordable.
### W5: The reported metric is also the tuning metric
Hyperparameters are chosen on final validation loss and the same loss is reported (§3, App. C). LM pretraining has no labelled test split and the validation set is large, so the risk is small, but the paper does not say whether the validation shard is fixed across all runs or disjoint from any data used for choices. Ask for a one-line statement and, ideally, a fresh held-out shard check for the top configurations.
- **Suggested Fix:** Evaluate the selected configurations on a second, untouched validation shard (negligible cost: inference only).

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E5 | Takeaway 1 vs §4.1, Fig. 19 | "AdEMAMix consistently achieves state-of-the-art performance and robust scaling with training duration" | §4.1 states D-Muon is best at the shortest 124M small-batch run and Fig. 19 caption says SOAP beats AdEMAMix at 336k steps | Cross-referenced (three locations) | High | MAJOR | Qualify "consistently" |
| ERR-2 | E4 | §4.2 | "We study this effect on the AdamW method, and then apply the best-found heuristic to all other optimizers." | Takeaway 6 shows per-optimizer scheduler optimum differs | Cross-referenced | High | MAJOR | See W2 |
| ERR-3 | E6 | §4.1 vs §5 | "and SF-AdamW perform better with a larger warmup of 8k steps" vs "large warmup of 25% of the total training duration T is beneficial for" | 8k steps is 6.25% of 128k; §5 says 25% (32k) | Computed from Figure 10 caption and §5 | Medium | MINOR | Align the recommendation |
| ERR-4 | E1 | App. B | "we trained a total of 2900 models" | The per-optimizer counts listed in App. B sum to 2966 (derived: 750+145+238+158+165+231+135+354+199+133+195+217+26+20) | Recomputed | Medium | MINOR | Say "about 3000" |

## Missing References (R1: optional)
See Reviewer 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Large, careful tuning, but single seeds and unequal axes |
| Clarity | 2 | 23 takeaways, dense, a few inconsistent statements |
| Significance | 3 | Practitioner-relevant, scale-limited |
| Originality | 2 | Benchmarks and ablations of existing methods |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: large, transparent tuning study with useful protocol findings, held back by single runs and a baseline-tilted shared schedule.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound design, notable gaps (W1–W3) |
| Clarity & Presentation | 58 | Competent | See R4; inconsistent recommendations |
| Novelty & Originality | 56 | Competent | Incremental by nature |
| Significance & Impact | 70 | Competent | Useful if it holds at scale |
| Experimental Validation | 62 | Competent | Breadth strong, variance missing |
| Reproducibility | 80 | Strong | Tables 7–47, code promised; link not visible |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations stated |

## Questions for Authors
1. Were any benchmark runs repeated with a different seed? A three-seed table for the top five would move my Overall up.
2. Do Figures 3(b)/5(b) use 2.1B-tuned or 16.8B-tuned hyperparameters for each optimizer?
3. What is the result when each optimizer gets its best scheduler of the three in the main ranking? A reordering among the top group would lower my score.
4. Is the validation shard used for selection the same one reported, and was it disjoint from any data used for intermediate evaluation?

## Limitations Assessment
**Partially.** §5 states the scale and no-downstream-evaluation limits. Missing: variance, equal tuning budgets, protocol transferred from AdamW.

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. The contribution is useful and thoroughly documented; the rankings need variance and per-method scheduler checks to carry the claims as worded.

## Confidence
**4**: Checked the protocol and appendix; figure values unverifiable.

---

# Peer Review Report (Reviewer 2)

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Reviewer: Prof. Ayelet Marchetti-Sun, Domain (ML optimization group, public university; fictional persona)
## Expertise: adaptive and second-order optimizers; scaling laws; LLM pretraining recipes
## Date: 2026-11-05

## Summary
The paper revisits optimizer comparison for LLM pretraining, bringing in newer methods (ADOPT, AdEMAMix, SOAP, Muon variants, Schedule-Free, Prodigy, MARS) than the earlier study it builds on, and recommends AdEMAMix, D-Muon and MARS over AdamW in specific regimes. It adds a catalogue of hyperparameter ablations and corrections to optimizer implementations.

## Strengths
### S1: A broader and more current method set than the closest prior benchmark
Zhao et al. [161] (ICLR 2025, cited) studied fewer methods; this paper adds second-order, matrix-based and parameter-free families and a MoE case (§2, §3), which is of practical interest.
### S2: Valuable corrections of prior descriptions
App. A shows that the code for Sophia and Muon differs from the published description ("The actual update rule of Sophia does not match its description in the original" paper, Takeaway 13), and that the standard Signum implementation breaks with weight decay (§4.1). These are specific, checkable contributions.
### S3: Constructive contradiction of prior guidance
§4.1 and App. D.1 test the claim of Zhang et al. [157] about 25% warmup ("our findings contradict this assertion") and the batch-size scaling of sign-based methods against [161, 157], and explain the setup differences to the SOAP paper [141] (§4.3, Figure 16). Taking on earlier claims with matched protocols is what a benchmark should do.
### S4: Good relation to ICLR's interests
The topic (training efficiency, optimizers, scaling) is squarely in scope.

## Weaknesses
### W1: The "first" claim and novelty relative to prior optimizer benchmarks are overstated
C1 says "the first large-scale, controlled benchmark of 11 different optimization methods". Zhao et al. [161] already compared SGD, Adafactor, Adam, Lion and Sophia (and a Signum variant) "across a range of model sizes, hyperparameters, and architecture variants" (abstract of the kept result), and the paper cites AlgoPerf [20] and others [60, 121] in §2. The new elements are the method set, the larger batch/duration grid and the protocol corrections, which is a real but incremental delta. The literature check (strict, arXiv API) finds Zhao et al. as the top prior (coverage 4/5, cited), and a concurrent preprint of closely related scope (below).
- **Suggested Fix:** Replace "first" by a delta table against [161] (methods, scales, tuning protocol) in §2.
### W2: Related work for the ablation claims is incomplete
The weight-decay/batch-size interaction and its scaling has a peer-reviewed predecessor not cited (Bergsma et al., "Power Lines", 2025, verified in the search), and the older line on how tuning protocols decide optimizer rankings is not discussed (Choi et al. 2019; Zhang et al. 2019). The §4.1 observation that large weight decay helps short horizons ("Larger weight decay achieves significantly better results", Figure 7) should be placed against these.
- **Suggested Fix:** Add and discuss the references below.
### W3: Some conclusions about optimizer behavior are asserted without a tested mechanism
§4.1 attributes Prodigy's good large-batch behavior to its effective learning rate (Figure 40, Takeaway 21); §5 says Lion's mechanism "appears similar to AdEMAMix". These are plausible but not tested against alternatives (e.g., giving AdamW the Prodigy-derived LR schedule), so they should be worded as hypotheses.
- **Suggested Fix:** Mark as hypotheses or add the one-run control.
### W4: Theory–practice discussion is thin
ADOPT's convergence guarantee, SOAP's preconditioner rationale and the AdEMAMix slow-EMA story are summarized (§2), but the results are not connected back to them beyond "re-tune β2 / β3". For a benchmark this is acceptable but limits the "directions for future optimization research" promised in the abstract.
- **Suggested Fix:** One paragraph in §5 stating which theoretical expectations the data support or contradict (e.g., β2(T) = 1 − 1/T not observed, App. D.1).

### Literature-check addendum (strict, cutoff 2025-09-24)
**Per-claim novelty (claim-level profile, `related_search.py novelty`).**

| Claim | Dim. | Verdict | Top prior (level, link, label, cited?) | Reasoning |
|-------|------|---------|----------------------------------------|-----------|
| C1 benchmark of 11 optimizers | resource | incremental | Zhao et al., "Deconstructing What Makes a Good Optimizer for Language Models" (4; arxiv.org/abs/2407.07972; prior, peer-reviewed; cited as [161]) | Same task and approach, fewer methods and smaller grids |
| C2 ablations + recommendations | result | medium | Bergsma et al., "Straight to Zero" (3; arxiv.org/abs/2502.15938; prior, peer-reviewed; cited as [7]) | Final-LR piece covered, other pieces new in the optimizer-conditioned form |
| C3 toolkit | resource | no close prior found in 25 results (arXiv only, at most medium) | none | Not assessable by abstracts |

Paper reading from the script: no central claim fully covered by prior work; attribution: Zhao et al. [161]. One claim (C1) is incremental, MAJOR at most, and it is differentiated in the paper's text only implicitly.

**Novelty delta table.**

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C1 | Zhao et al. [161] | Compares SGD, Adafactor, Adam, Lion, Sophia (plus Signum) across model sizes, hyperparameters and architecture variants; concludes no clear winner | 11–12 methods incl. second-order/matrix-based, larger batch and duration grid, MoE | Cited; differentiated by protocol corrections (§4.1, §4.3) but not by an explicit delta |
| C2 (weight decay) | Bergsma et al. "Power Lines" (2025) | Scaling laws for weight decay and batch size in LLM pretraining | Optimizer-by-optimizer sweep across methods | Not cited |
| C2 (final LR) | Bergsma et al. [7]; Hägele et al. [54] | Decay to zero / WSD cooldown | Optimizer-conditioned decay ablation | Cited |

**Baseline scout.** `benchmarks` found no external benchmark; the paper's baselines are the authors' own runs of the optimizers on FineWeb validation loss, so there are no prior-reported numbers to compare against and no under-reported baseline can be assessed. Not applicable.

**Field snapshot (as of 2025-09).** Until about 2023 AdamW was the default for LLM pretraining and most alternatives were evaluated on small models, short schedules or different codebases. Since 2024, matrix-based methods (Shampoo/SOAP, Muon and its scaled variants), sign-based and parameter-free methods, and variance-reduced or long-EMA variants (MARS, AdEMAMix) have reported speed-ups of up to about 1.4–2× over AdamW. Recent studies (Zhao et al., Dahl et al.'s AlgoPerf, Kaddour et al.) and concurrent work question whether those gains survive equal tuning and longer horizons; several show AdamW with tuned weight decay, β2 and decay schedule is a much harder baseline. Open problems named in this work and nearby ones include behavior beyond 1B parameters, token budgets well above Chinchilla, downstream effects, and implementation cost at scale. In this sub-field a benchmark is significant when it (i) equalizes tuning, (ii) covers more than one scale and horizon, and (iii) ships reproducible code; a +0.01 loss ordering among top optimizers is incremental unless shown across seeds and scales.

### Missing References (all verified with `related_search.py verify`)
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Shane Bergsma, Nolan Dey, Gurpreet Gosal, Gavia Gray, Daria Soboleva, Joel Hestness. "Power Lines: Scaling Laws for Weight Decay and Batch Size in LLM Pre-training", arXiv 2025 (https://arxiv.org/abs/2505.13738; label: prior, peer-reviewed) | Directly relevant to the weight-decay-versus-duration and batch-size findings (Fig. 7, 23; Takeaway 3) |
| Important | Dami Choi, Christopher J. Shallue, Zachary Nado, Jaehoon Lee, Chris J. Maddison, George E. Dahl. "On Empirical Comparisons of Optimizers for Deep Learning", arXiv 2019 (https://arxiv.org/abs/1910.05446) | Shows tuning protocol decides optimizer rankings, the central premise of the paper |
| Helpful | Guodong Zhang, Lala Li, Zachary Nado, James Martens, Sushant Sachdeva, George E. Dahl, Christopher J. Shallue, Roger Grosse. "Which Algorithmic Choices Matter at Which Batch Sizes? Insights From a Noisy Quadratic Model", NeurIPS 2019 (https://arxiv.org/abs/1907.04164) | Batch-size dependence of optimizer benefit |
| Discuss only (concurrent, not required) | Kaiyue Wen, David Hall, Tengyu Ma, Percy Liang. "Fantastic Pretraining Optimizers and Where to Find Them", arXiv 2025-09-02 (https://arxiv.org/abs/2509.02046) | Concurrent, closely related scope (ten optimizers, four scales, tuning fairness). Within 60 days of the cutoff, so never a weakness |

**Citation check (E7).** [161] is cited for batch-size sweeps of Lion, Signum and AdamW and for z-loss practice in §3 and §4.1; the abstract of [161] (kept result) covers language-model optimizer comparison, hyperparameter sensitivity and Signum, consistent with how it is used. One contrast worth stating: [161] reports that these algorithms "perform comparably" with "no single algorithm" a clear winner, whereas this paper reports clear gaps among newer methods; the paper should say which differences come from the method set and which from tuning. [141] (SOAP) is used for the "SOAP benefits from larger batch" claim in §4.3, which the paper then contests with its own setup; consistent.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Careful, not airtight |
| Clarity | 3 | Positioning could be sharper |
| Significance | 3 | Practical |
| Originality | 2 | Incremental over [161] |

## Dimension Scores (0–100)
**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the largest, best-documented optimizer comparison of its kind that I know of before the cutoff, with a real but incremental delta over the cited predecessor. (The script flagged an inconsistency between my earlier pool figure and my dimension scores; I corrected the pool figure to 70, keeping my dimension scores, because the scores are what I reasoned from.)

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Correct framing; protocol limits |
| Clarity & Presentation | 60 | Competent | Positioning vs [161] implicit |
| Novelty & Originality | 58 | Competent | Incremental (verdict above) |
| Significance & Impact | 72 | Strong-leaning | Practitioner and researcher use |
| Experimental Validation | 66 | Competent | Broad, single-run |
| Reproducibility | 78 | Strong | Tables 7–47 |
| Ethical Compliance | 66 | Competent | Nothing at stake |

## Questions for Authors
1. What is the explicit delta to [161] (methods, scales, tuning), and does a re-run of its setting with your protocol reproduce its conclusions? A clear delta raises my Novelty score.
2. How do your weight-decay findings relate to the weight-decay/batch-size scaling work above?
3. Can the Prodigy-effective-LR and Lion-AdEMAMix explanations be tested with one control run?

## Limitations Assessment
**Partially.** Scale and downstream limits are stated; the delta against prior benchmarks is not.

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. A solid and useful incremental benchmark; "first" should go, and related work needs the delta table.

## Confidence
**4**

---

# Peer Review Report (Reviewer 3)

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Reviewer: Dr. Joaquín Ferreyra-Holm, Perspective (national supercomputing center, Europe; fictional persona)
## Expertise: numerical linear algebra for training; distributed training systems
## Date: 2026-11-05

## Summary
The paper turns the question "is AdamW still the best?" into a systematic, tuned comparison at modest model scale, and extracts recipe-level guidance (weight decay, warmup, decay-to-0.01, β2) usable regardless of optimizer. For practitioners it gives a short list of candidates (AdEMAMix, D-Muon, MARS) and a warning that popular codebase defaults can reverse optimizer rankings.

## Strengths
### S1: The recipe-level takeaways are cheap to adopt
Takeaways 3, 8, 9 and 14 (decoupled weight decay 0.1, decay to 0.01 × γmax, drop z-loss, re-tune β2 with horizon) cost nothing to apply and affect all optimizers (§4.1–4.3).
### S2: A practical view of cost
The wall-clock study (§4.3, Figure 18, Takeaway 11) shows SOAP slows with model size while most others match AdamW, and the paper is candid that sharding support is missing for some optimizers (§5). That is how an engineering team decides.
### S3: Cross-method perspective across batch size
Showing sign-based methods and MARS improving with batch size (Figure 6, Takeaway 2) connects to critical-batch-size thinking, and is useful for teams choosing a batch size.
### S4: Thought-out scope on downstream and architecture
The MoE extension (§4.4) and the explicit statement that downstream performance is left aside (§5) are the right kind of boundaries.

## Weaknesses
### W1: Deployment-relevant cost is only partially measured
Wall-clock is measured on a single GPU for 100 iterations without `torch.compile` and at batch 16 (§4.3), whereas the ranking relies on large-batch multi-GPU training. Memory, communication, and optimizer-state cost (Signum/Lion single buffer versus SOAP preconditioners, §2) are discussed but not reported next to the loss ranking.
- **Suggested Fix:** Add a table with optimizer state memory per parameter and measured step time under DDP at the 720M scale, and a loss-per-GPU-hour view.
### W2: Scale-extrapolation assumption
The paper's own findings show rankings move with scale and batch (Sign-based methods fall behind from 210M to 720M, Takeaway 10; Muon degrades with model size, §4.3). Therefore the practitioners' advice ("which optimizer is best suited for each scenario", abstract) is an assumption for 7B+ models that the data cannot test. A cross-field analogue is hyperparameter-transfer work, where the shape of transfer (width, depth, horizon) is studied explicitly.
- **Suggested Fix:** Put a scale-transfer caveat in the abstract and add a small learning-rate-transfer check across widths if feasible.
### W3: Sensitivity of the ranking to implementation fixes
Several results rest on the authors' re-implementations (Signum with decoupled decay, Sophia update, D-Muon, Prodigy bias correction; App. A). A reader should know which fixes change a method's rank.
- **Suggested Fix:** A short table "published/default implementation vs. ours: ΔFinal loss" for the three affected methods.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Careful and broad |
| Clarity | 3 | Understandable with effort |
| Significance | 4 | Immediately actionable |
| Originality | 3 | New synthesis and corrections |

## Dimension Scores (0–100)
**Pool position:** better than about 78% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: broad, reusable, and transparent evidence that practitioners will use, at the cost of limited scale.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 70 | Competent | Thorough |
| Clarity & Presentation | 66 | Competent | Many takeaways, readable |
| Novelty & Originality | 66 | Competent | New synthesis |
| Significance & Impact | 80 | Strong | Recipe-level, field-wide |
| Experimental Validation | 72 | Competent | Breadth |
| Reproducibility | 82 | Strong | Configs and code |
| Ethical Compliance | 70 | Competent | Compute reported |

## Questions for Authors
1. What is the optimizer-state memory and step-time cost at 720M under DDP? This would strengthen the practitioner message.
2. Do the Takeaway 3/8/9 recipe changes shrink the optimizer gaps, i.e., how much of the "optimizer gain" is recipe gain?
3. Is the D-Muon implementation compatible with sharded training?

## Limitations Assessment
**Partially.** Compute cost and sharding are noted; memory and energy are not quantified.

## Ethics Review Flag
**No.** Energy use of about 30000 GPU hours is stated; a note on footprint would be welcome.

## Overall Score
**5**: Accept. A large, transparent and immediately useful study whose weaknesses (scale, variance) are typical of accepted empirical papers.

## Confidence
**3**: Cross-field reader; I did not audit the protocol in detail.

---

# Peer Review Report (Reviewer 4)

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Reviewer: Dr. Lan Nguyen-Abara, Generalist (industrial LLM pretraining team, East Asia; fictional persona)
## Expertise: LLM pretraining recipes, evaluation
## Date: 2026-11-05

## Summary
The paper asks whether recent optimizers beat a well-tuned AdamW in LLM pretraining, and answers with a grid over model size, batch size and training length, plus a long series of hyperparameter ablations. In the authors' setting, AdEMAMix, D-Muon and MARS are the most promising, sign-based methods need large batches, and several defaults from popular codebases hurt. The code and settings are promised to the community.

## Strengths
### S1: A clear, important question with a direct answer
The introduction frames "Is Adam still the most effective optimizer in the age of LLMs" as the practitioner question, and the takeaway boxes give a concrete answer per setting (Takeaways 1, 10).
### S2: Format that practitioners can use
The ranking figures (1, 5, 13, 17, 19) and the numbered Takeaway boxes make the paper easy to scan, and Tables 7–47 give the exact grids.
### S3: Good fit to ICLR
Optimization and training-efficiency studies with open code are well received at the venue, and reproducibility is above the venue's median.
### S4: Real engineering insight
Pointing out that standard PyTorch Signum and SGD momentum implementations interact badly with weight decay (§4.1, App. A.2) is exactly what a PC member wants to see.

## Weaknesses
### W1: The paper is hard to read as a single argument
There are 23 takeaways, the main text mixes benchmarks and ablations, and sections have to be cross-read (e.g., Figure 3/5/6/21 for one story about SOAP vs AdEMAMix). A reader cannot easily see which result depends on re-tuned β's. Some recommendations differ across sections (warmup: 8k steps in §4.1, 25% of T in §5; ERR-3 in R1).
- **Suggested Fix:** A one-page summary table (optimizer × regime: rank, key hyperparameters, caveats) in the main text; move most ablations to the appendix.
### W2: Claims are worded more strongly than the evidence
"consistently achieves state-of-the-art" (Takeaway 1) and "AdEMAMix remains the best optimizer overall" (§5) coexist with D-Muon winning the shortest 124M run (§4.1) and SOAP beating AdEMAMix on MoE at 336k steps (Fig. 19). Also, the scope is 124M–720M, a single dataset, sequence length 512, and validation loss only ("leaving aside downstream performances").
- **Suggested Fix:** State the regime next to each recommendation (≤ 720M, ≤ 48B tokens, FineWeb, loss only).
### W3: The significance for real-scale training is not shown
Practitioners train multi-billion-parameter models with longer context. The paper is honest about this in §5, but the "burning question" framing in §1 reads as general.
- **Suggested Fix:** Tone down §1 and add one multi-seed or larger-scale spot check.
**Minor:** "This includes includes nearly" (App. B); "greed searching" (App. E); "is far from being the best batch size for pretraining" refers to warmup (App. D.1); Figure 3 caption mixes "iterations" and tokens; several figure axes use awkward tick labels in the extracted text (unverifiable).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Strong effort, some gaps |
| Clarity | 2 | Dense and repetitive |
| Significance | 3 | Useful |
| Originality | 3 | New synthesis |

## Dimension Scores (0–100)
**Pool position:** better than about 72% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a typical accepted empirical paper at ICLR in scope and effort, with presentation as its weakest point.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 66 | Competent | Sound, with gaps |
| Clarity & Presentation | 58 | Competent | W1, Minor |
| Novelty & Originality | 62 | Competent | Useful synthesis |
| Significance & Impact | 72 | Strong-leaning | Recipe and ranking |
| Experimental Validation | 68 | Competent | Breadth |
| Reproducibility | 78 | Strong | Grids, code |
| Ethical Compliance | 66 | Competent | Nothing at stake |

## Questions for Authors
1. Can you give a one-table summary per regime with explicit caveats? That would raise Clarity.
2. How do you recommend a practitioner at 3B parameters use your ranking?

## Limitations Assessment
**Partially.** Good on the model-size/downstream limits; weaker on variance.

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. A useful, extensive study that most reviewers at ICLR would find worth sharing, with presentation and wording to fix.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Reviewer: Prof. Rhea Castellanos-Dubois (public university, South America; statistics and evaluation methodology; fictional persona)

## Steelman
A very large, transparently tuned study (2900 models, 30000 GPU hours) shows that recent optimizers can beat a carefully tuned AdamW at 124M–720M parameters and that popular codebase defaults, not just optimizers, drive many published gaps. Even if the exact ordering is imperfect, the takeaways on weight decay, final LR, warmup and β re-tuning are broadly useful.

## Core Argument Chain
1. P1: Hyperparameters tuned near the Chinchilla horizon transfer to other horizons and scales (§3, Takeaways 2, 4, 7).
2. P2: Under that protocol, the final validation loss ranks optimizers fairly (§3, Figures 1, 5, 13, 17).
3. P3: Rankings at ≤ 720M, ≤ 48B tokens, FineWeb inform which optimizer to use in practice (abstract, §1).
4. P4: Rankings are stable across batch sizes, model sizes, horizons and MoE once tuned (Takeaways 2(II), 7, 12).
∴ AdEMAMix (plus D-Muon/MARS) are the best choices and AdamW is no longer the default.

## Strongest Counter-Argument
The paper's own ablations show that the conditions under which the ranking is produced interact with optimizer identity. Scheduler preference is optimizer-specific (Takeaway 6: "linear scheduler outperforms or matches cosine and WSD for sign-based methods, SOAP, and MARS"), warmup preference is optimizer-specific (Takeaway 5), the weight-decay optimum depends on the horizon (Takeaway 3), and β2/β3 must be re-tuned with horizon (Takeaway 14); yet the main ranking uses one shared cosine schedule chosen on AdamW (§4.2: "We study this effect on the AdamW method, and then apply the best-found heuristic to all other optimizers"), tunes at one horizon and reuses the values ("We then keep those hyperparameters when we increase the number of iterations."), and runs each configuration once. Each of those choices moves the loss by an amount comparable to the gap inside the leading group: the SOAP–AdEMAMix order flips with β3 (Figure 6 right, Figure 21), flips again on MoE at 336k steps (Figure 19 caption) and D-Muon leads at 1B tokens (§4.1). Therefore the statement "AdEMAMix consistently achieves state-of-the-art" is not a property of the optimizers but of this protocol plus one seed. The result that survives is the weaker one: a tuned AdamW is a strong baseline, and several methods are close to or modestly above it in specific regimes. The authors can answer by adding seeds and per-optimizer scheduler selection at two scales, or by narrowing the wording; they cannot answer by adding more optimizer-hyperparameter grids at the same protocol.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in weaker form: the paper's data support "a well-tuned AdamW is a strong baseline and some methods beat it in the studied regimes", and nothing contradicts that. Selection on the reported validation loss is discussed as DA-M5 and is not criterion 3 (large held-out split, field-standard metric, no separate test split in LM pretraining; the ranking does not rest on a single selected configuration).

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| – | – | – | None | – | – |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Figures 1, 3, 5, 13, 17, 19; Takeaways 1, 10 | Single runs, no variance, for the claims "consistently" and "by far"; the evidence supports a weaker claim (not contradicted). | 3 seeds for top five and AdamW at two scales |
| DA-M2 | Logic | §4.2, Takeaway 6, footnote 2 | Shared scheduler/final-LR chosen on AdamW is applied to all; Takeaway 6 says the optimum differs for sign-based, SOAP and MARS | Best-of-three schedulers in the main ranking, or narrow wording |
| DA-M3 | Scope | Abstract; §1; §5 | "which optimizer is best suited for each scenario" over-generalizes from ≤ 720M, ≤ 48B tokens, seq 512, FineWeb, loss only | State regime on every recommendation |
| DA-M4 | Evidence | §4.4, Takeaway 12, Figure 19 | "transfer to corresponding MoEs" rests on one untuned configuration and a rank change at 336k steps | Re-word as partial transfer, or tune MoE |
| DA-M5 | Protocol | §3, App. C | Selection on the same final validation loss that is reported; no separate held-out shard stated | One-line statement plus fresh-shard check |
| DA-M6 | Novelty | C1 | "first" vs Zhao et al. [161] (cited) and a concurrent preprint | Delta table; drop "first" |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §4.1 vs §5 | Warmup recommendation 8k steps versus "25% of the total training duration T" |
| DA-m2 | Scope | Figure 16, §4.3 | The z-loss/weight-decay/final-LR comparison to [141] covers only AdamW and SOAP at one 583M setting |
| DA-m3 | Reporting | App. B | Model counts sum to 2966, not 2900 |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| 124M, 2.1B tokens at batch 32 × 512 | 128k iterations (§4.1) | 128,000 × 16,384 = 2.10B | Yes |
| 720M, 48k iterations at 1984 × 512 | "48B" (§3, Table 6) | 48,000 × 1,015,808 = 48.8B | Rounded (≈ 1.6% over) |
| 124M Chinchilla tokens | 2.5B (Table 3) | 20 × 124M = 2.48B | Yes |
| Total models | "2900" (§3, App. B) | Sum of listed per-optimizer counts = 2966 | Approximately (2.3% off; "nearly") |
| MoE tokens, 336k steps at 131k | "44B" (§4.4) | 336,000 × 131,072 = 44.0B | Yes |

Gap sizes between optimizers could not be recomputed (figures only).

## Ignored Alternative Explanations
- Rank differences within the leading group could be seed noise.
- Gains attributed to an optimizer may be recipe gains (weight decay 0.5 for short runs, β2 re-tuning) rather than algorithmic ones.
- The shorter-horizon advantage of many methods could reflect faster early progress at an LR tuned for 2.1B tokens, not a better optimum.
- Sophia and Signum divergence could reflect implementation or LR-range issues rather than the algorithms (the authors themselves found that the published Sophia update differs from the code, Takeaway 13).

## Missing Stakeholder Perspectives
Teams training at ≥ 7B parameters, practitioners with fixed codebases (the paper acknowledges sharding support in §5), and energy-conscious users (about 30000 GPU hours for the study).

## Observations (Non-Defects)
The honest handling of Sophia divergence, the explicit documentation of grids, the correction of earlier guidance with a matched-setup comparison (§4.3), and the choice of the short validation curves plus full final validation loss (App. C) are all robust against challenge.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 52 | Single seeds and shared protocol under-tune non-AdamW |
| Clarity & Presentation | 56 | Dense, inconsistent recommendations |
| Novelty & Originality | 52 | Incremental over [161] |
| Significance & Impact | 62 | Useful, scale-limited |
| Experimental Validation | 52 | No variance, one dataset |
| Reproducibility | 72 | Tables strong; link not visible |
| Ethical Compliance | 64 | Nothing at stake |

## Overall: 3 | Confidence: 4
**Pool position:** better than about 58% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline ranking claims are worded beyond what single-seed, shared-protocol evidence supports; the paper is above the median but not clearly above the bar.

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 (same metric used for tuning and reporting) | rewritten, kept as MAJOR-leaning question | The paper does say final validation loss is computed on the full validation split (App. C); the open point is only whether the shard is disjoint from other uses |
| R3 | "No code release" (considered) | dropped | Contribution 3 and App. B state code release; the link is anonymized in the provided text, so it is unverified, not missing |
| R4 | Typos and figure ticks | moved to Minor | Cosmetic |
| R3 | W3 (implementation fixes) | kept, reordered last | Valid but lower severity |
| DA | DA-M5 | kept as MAJOR | Not criterion 3; see EIC ruling |
| All | Missing references | checked against ledger labels | Power Lines is prior (peer-reviewed): Important; Wen et al. concurrent: discuss only |

Scores unchanged.

## Phase 2: Synthesizer Package (Part A)

**Official score (script, before EIC):** ratings R1 4, R2 4, R3 5, R4 4, DA 3 → mean 4.00; official composite 66.3 (before_composite). Script warning at that time: R2 pool position 67 inconsistent with its composite 67.0 (resolved by R2 correcting the pool figure to 70).

**Master issue list and consensus**
| Issue | Sources | Class |
|-------|---------|-------|
| Single runs / no variance | R1-W1, DA-M1 (R4-W3 partly) | CONSENSUS-3 |
| Shared scheduler/final-LR chosen on AdamW; unequal tuning | R1-W2, R1-W3, DA-M2 | CONSENSUS-2 |
| Over-worded claims ("consistently", "first", "transfer") | R1-W4/ERR-1, R2-W1, R4-W2, DA-M3/M4/M6 | CONSENSUS-4 |
| Scale and downstream limits | R3-W2, R4-W2/W3, DA-M3 | CONSENSUS-3 |
| Presentation (23 takeaways, inconsistencies) | R4-W1, R1 ERR-3, DA-m1 | CONSENSUS-3 |
| Missing related work | R2-W2 | SOLO |
| Cost/deployment | R3-W1 | SOLO |
| Selection on reported metric | R1-W5, DA-M5 | CONSENSUS-2 |
| DA-CRITICAL | none | – |
| SPLIT | Whether the paper is "Accept" (R3) vs borderline (R1, R2, R4) vs "reject-leaning" (DA) | SPLIT |

Issues the outcome may hinge on: variance/rankings (W1), shared protocol (W2), over-wording.

---

## Editorial Decision

## Paper: Benchmarking Optimizers for Large Language Model Pretraining
## Submission ID: iclr26-Jw7khYzYzl
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: Benchmark
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Ingrid Valtonen-Okafor; R1 Methodology Dr. Kwame Adjei-Lindqvist, R2 Domain Prof. Ayelet Marchetti-Sun, R3 Perspective Dr. Joaquín Ferreyra-Holm, R4 Generalist Dr. Lan Nguyen-Abara, DA Prof. Rhea Castellanos-Dubois

---

## Decision: Borderline Accept (4)  (ICLR label as translated by the script: "6 on {0,2,4,6,8,10}", "6 on {1,3,5,6,8,10}"; scale status secondary, not official wording)

**Official ratings** (shown to authors): R1 4, R2 4, R3 5, R4 4, DA 3 → mean 4.00 · official composite 66.3
**EIC assessment** (internal): weighted rating 3.89 → starting point 4 · weighted composite 65.5 → band 4 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 4
*Not a journal target.*

---

## EIC Meta-Review (Dr. Ingrid Valtonen-Okafor)

### The Case For and Against
- **For acceptance:** The most extensive, openly documented comparison of recent optimizers for LLM pretraining available at the cutoff (2900 models, full grids in App. E), with protocol findings that change published rankings (Takeaway 9, Figure 16) and cheap, general recipe advice (weight decay, decay-to-0.01, β2/β3 re-tuning). Its weaknesses (single runs, scale ≤ 720M, loss only) are typical of accepted empirical papers at ICLR.
- **Against acceptance:** The ranking is the headline, but it is produced by single runs, a shared AdamW-selected scheduler and one-horizon tuning, and the paper's own ablations show that each of those interacts with optimizer identity. "First", "consistently" and "transfer" are overstated, and the delta over Zhao et al. [161] and concurrent work is incremental.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "AdEMAMix consistently achieves state-of-the-art" is contradicted in places | R1 ERR-1, R4-W2, DA | Takeaway 1; §4.1; Fig. 19 caption; §5 | Verified | D-Muon best at 1B tokens (§4.1); "SOAP outperforms AdEMAMix in 336k steps run" (Fig. 19); the claim survives in weaker form |
| No seeds for loss comparisons | R1-W1, DA-M1 | §3, §4, App. B/E | Verified | Searched for "seed": only the wall-clock study (§4.3) uses seeds |
| Scheduler/final LR chosen on AdamW and applied to all | R1-W2, DA-M2 | §4.2; Takeaway 6 | Verified | Quote present verbatim; effect size unknown (figures) |
| One-horizon tuning, unequal budgets | R1-W3, DA | §3; App. B | Partly correct | Paper acknowledges horizon sensitivity (Fig. 21, "we found that the sensitivity to several hyperparameters can change"); counts unequal (750 AdamW vs 135 D-Muon) but AdamW has the most, which favors the baseline |
| "Transfers to MoE" overstated | R1-W4, DA-M4 | §4.4; Takeaway 12; Fig. 19 | Partly correct | Rankings "closely mirror" (caption) but top-1 differs at 336k; hyperparameters untuned by design |
| Selection on the reported validation loss | R1-W5, DA-M5 | §3; App. C | Partly correct | True, but validation split is large and field-standard; no labelled test split; not criterion 3 |
| "First" overstated vs [161] | R2-W1, DA-M6 | §1, §2 | Verified | [161] cited and covers the same task with fewer methods |
| Power Lines not cited | R2-W2 | References | Verified | Not in the reference list (searched); label prior, peer-reviewed → Important, not Critical |
| Warmup recommendations inconsistent | R1 ERR-3, DA-m1 | §4.1 vs §5 | Verified | 8k steps vs 25% of T |
| Model-count sum | R1 ERR-4, DA | App. B | Verified (derived) | 2966 vs "2900"; trivial |
| R3: sharding/energy not quantified | R3-W1 | §4.3, §5 | Verified | Single-GPU wall-clock only |
| R4: "no downstream evaluation" | R4-W2 | §5 | Verified | "leaving aside downstream performances" |

The literature check labels: Zhao et al. is prior and cited; Wen et al. is concurrent (discuss, not required); no missing-comparison weakness rests on a recent/concurrent paper. No text-overlap or integrity flags.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 4 | 4 | 1.25 | Central points (seeds, shared scheduler, wording) verified at their locations; calibrated; two minor overstatements (W3 budget direction) |
| R2 (Domain) | 4 | 4 | 1.0 | Literature points verified; sound, typical |
| R3 (Perspective) | 5 | 3 | 0.85 | Accept rating relies on "rankings transfer" and recipe value, partly overstated (Takeaway 12), and gave less weight to variance |
| R4 (Generalist) | 4 | 4 | 1.0 | Well calibrated, presentation points verified |
| DA | 3 | 4 | 1.25 | Counter-argument survived my check (all MAJORs verified or partly verified); no CRITICAL raised, tone proportionate |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so there is no ruling and no ceiling. I considered whether DA-M5 (selection on the reported validation loss) should have been CRITICAL under criterion 3: it is not, because the loss is measured on a large held-out split of the corpus that is the field's standard reporting metric (no labelled test split exists), the selected configuration is not the sole basis of the ranking, and the gaps between most methods are larger than selection effects would produce.

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| – | – | None raised | – |

### Final Decision and Justification
The official mean is 4.00 and the EIC-weighted rating 3.89, so the starting point is 4 (Borderline Accept); the composite cross-check (65.5, band 4) agrees, so I do not depart from it. My own pool position is about 70: better than about 70% of ICLR submissions (accepted share ≈ 27%), on the strength of scope, transparency of tuning and findings that change published rankings, but held below "solid accept" (pool ≥ 85) by single seeds, a shared protocol that is not tuned per optimizer on the scheduler axis, and moderate novelty over [161]. Reviewers' pool positions (66, 70, 78, 72, 58) span 20 points, under the 30-point threshold for a separate ruling; the disagreement between R3 and DA is about variance and over-wording, and I verified both. Weaknesses are typical of accepted empirical papers, but "typical" is not "none": the final score of 4 means the reasons to accept narrowly outweigh the reasons to reject, provided the claims are narrowed. The decision does not exceed any DA ceiling (none).

---

## Score Summary

### Official Scores and EIC Assessment

#### Reviewer weights (EIC, internal)
| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 19% |
| R3 (Persp.) | 3 | 0.70 | 0.85 | 14% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 19% |
| DA | 4 | 0.85 | 1.25 | 24% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 62 | 64 | 70 | 66 | 52 | 62.8 | 61.8 | 18 |
| Clarity & Presentation | 58 | 60 | 66 | 58 | 56 | 59.6 | 59.0 | 10 |
| Novelty & Originality | 56 | 58 | 66 | 62 | 52 | 58.8 | 57.9 | 14 |
| Significance & Impact | 70 | 72 | 80 | 72 | 62 | 71.2 | 70.2 | 18 |
| Experimental Validation | 62 | 66 | 72 | 68 | 52 | 64.0 | 62.9 | 20 |
| Reproducibility | 80 | 78 | 82 | 78 | 72 | 78.0 | 77.6 | 10 |
| Ethical Compliance | 66 | 66 | 70 | 66 | 64 | 66.4 | 66.1 | 6 |
| **Composite** | 65.3 | 67.0 | 73.2 | 67.8 | 58.2 | **66.3 (before)** | **65.5 (after)** | |
| Pool position (P%) | 66 | 70 | 78 | 72 | 58 | | | |

Ratings: official mean 4.00; EIC-weighted 3.89 → starting point 4; no spread above 20 flagged (Experimental Validation spread is exactly 20).

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 3 / 2 / 3 |
| Rating | 6 on {0,2,4,6,8,10} (6 on {1,3,5,6,8,10}); the skill's internal "Borderline Accept (4)" |
| Venue-weighted composite | 65.3 (band 4, no DA cap) |

*Labels are produced by `aggregate_scores.py`, not official ICLR wording (status: secondary).*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Benchmarking Optimizers for Large Language Model Pretraining" to ICLR.

Your paper addresses an important and timely question: whether the many recent optimizers really beat a properly tuned AdamW in LLM pretraining, and how much of the difference is recipe rather than algorithm.

**Overall Assessment:** The panel found the study extensive, transparent and useful, with several findings that change how future optimizer papers should set their baselines. Concerns focus on how strongly the rankings are worded relative to single-run evidence and a shared protocol, and on the scale of the experiments.

**Key Strengths Identified by Reviewers:**
1. A large, openly documented tuning effort with full grids (R1, R3, R4).
2. Protocol findings that reverse published comparisons (weight decay, final LR, z-loss; §4.3; R1, R2).
3. Cheap, general recipe advice and implementation corrections (R2, R3, R4).

**Key Concerns Requiring Attention:**
1. Single-run rankings without variance (CONSENSUS-3: R1, R4, DA).
2. A shared scheduler and final LR chosen on AdamW, and tuning at a single horizon (CONSENSUS-2: R1, DA).
3. Wording: "first", "consistently", "transfer to MoEs", "best suited for each scenario" (CONSENSUS-4).

No Devil's Advocate CRITICAL issue was raised.

**Decision: Borderline Accept (4).** The reasons to accept narrowly outweigh the reasons to reject: the contribution is real and useful, and the weaknesses are of the kind accepted empirical papers at this venue commonly have. What tipped the balance is the transparency and breadth of the tuning study. To secure acceptance, narrow the claims to the studied regime, add seeds for the leading methods and a per-optimizer scheduler check, and add the delta against prior optimizer benchmarks. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Ingrid Valtonen-Okafor
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Claims worded beyond the evidence | R1, R2, R4, DA | CONSENSUS-4 |
| Single runs, no variance | R1, R4 (scope), DA | CONSENSUS-3 |
| Scale/downstream limits | R3, R4, DA | CONSENSUS-3 |
| Presentation (many takeaways, inconsistent recommendations) | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Strength of the paper (Accept vs Borderline Reject) | R3 (5) | DA (3) | Both partly right: significance is high (R3) but rankings are over-worded (DA); resolves to 4 |
| Tuning-effort fairness | R1, DA (unequal, one horizon) | Paper (AdamW received the most runs) | Unequal effort is real but direction favors the baseline; the horizon-reuse point stands |
| Selection on the reported metric | DA-M5, R1-W5 (concern) | Field practice | MAJOR-to-minor question, not criterion 3 |

### Score Spread Discussion
No dimension exceeds 20 points; Experimental Validation spread is 20 (R3 72 vs DA 52). R3 weighs breadth of coverage; DA weighs absence of variance and per-method scheduler tuning. I adopt the middle (weighted 62.9) since the missing variance is real but the volume of controlled comparisons is a genuine strength.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Single runs | Yes (R1-W1) | n/a | New runs |
| DA-M2 | MAJOR | Shared scheduler | Yes (R1-W2) | n/a | New runs or narrowing |
| DA-M3 | MAJOR | Scope over-generalization | Yes (R3, R4) | n/a | Clarification |
| DA-M4 | MAJOR | MoE transfer | Yes (R1-W4) | n/a | Clarification |
| DA-M5 | MAJOR | Selection on reported loss | Yes (R1-W5) | n/a | Statement plus cheap check |
| DA-M6 | MAJOR | "First" | Yes (R2-W1) | n/a | Clarification |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No upheld DA-CRITICAL issue. The items below are verified issues that undermine the wording of the main claims.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Rankings stated as consistent/dominant rest on single runs | R1-W1, DA-M1, ERR-1 | Figs. 1, 3, 5, 13, 17; Takeaways 1, 10 | 3 seeds for top five + AdamW at 124M and 210M, two horizons; mark gaps within noise; qualify "consistently" | Medium; ≈ 300–400 GPU-h (derived from ≈ 10 GPU-h per run) | Yes (partly) |
| R2 | Shared scheduler/final LR chosen on AdamW | R1-W2, DA-M2 | §4.2; Takeaway 6 | Report each optimizer's best of cosine/linear/WSD in the main ranking, or state it as a limitation and soften "careful tuning of each method" | Medium; ≈ 2 extra runs × 11 optimizers at the 124M headline setting | Yes |
| R3 | Over-worded claims ("first", "consistently", "transfer", "best suited for each scenario") | R2-W1, R4-W2, DA-M3/M4/M6 | Abstract; §1; Takeaways 1, 2(II), 12; §5 | State the regime (≤ 720M, ≤ 48B tokens, FineWeb, loss only) with each recommendation; add delta table vs [161] | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Tuning budget and horizon of tuned values unclear/unequal | R1-W3, DA | Table of runs/grids/tuned horizon per optimizer; say which figures use 16.8B-tuned values | Low | Yes |
| S2 | MoE transfer with untuned hyperparameters | R1-W4, DA-M4 | Re-word or tune MoE for the top three | Low–Med | Partly |
| S3 | Selection on reported validation loss | R1-W5, DA-M5 | State shard policy; evaluate selected configs on a fresh shard | Low | Yes |
| S4 | Missing references (Important) | R2-W2 | Add and discuss Bergsma et al. 2025 ("Power Lines") and Choi et al. 2019; discuss concurrent Wen et al. 2025 | Low | Yes |
| S5 | Cost and deployment metrics | R3-W1 | Optimizer-state memory and DDP step time at 720M | Medium | Partly |
| S6 | Presentation: 23 takeaways, inconsistent warmup advice | R4-W1, ERR-3 | Summary table; align 8k vs 25% | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Mechanism claims for Prodigy and Lion untested | R2-W3 | Word as hypotheses |
| N2 | Theory connection | R2-W4 | One paragraph in §5 |
| N3 | Implementation-fix effect sizes | R3-W3 | Table of default-vs-fixed loss |
| N4 | z-loss comparison limited to AdamW/SOAP | DA-m2 | Extend or caveat |
| N5 | Typos ("includes includes", "greed searching", "batch size" for warmup) and model count 2966 vs 2900 | R4, R1 ERR-4 | Correct |
| N6 | Second dataset for the main ranking | R4, DA | Optional |

## Estimated Revision Effort
- Priority 1: 3 items, about 1–2 weeks (mostly new runs: roughly 400–600 GPU-hours in total, derived)
- Priority 2: 6 items, about 1 week
- Priority 3: 6 items, a few days
- **Total estimated revision time**: about 2–3 weeks, rebuttal-feasible in large part.
