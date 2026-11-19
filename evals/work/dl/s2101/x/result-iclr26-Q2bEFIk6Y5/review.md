# Academic Paper Review — "PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow"

*Simulated panel review (mode: full; target venue ICLR; literature check: strict, cutoff 2025-09-24). The outcome is a simulation of how a careful panel would likely see this draft, not a prediction. Date: 2026-11-10. The five reviews were written as five sequential role passes sharing one model context; they are not independent agents. Figures were unavailable, so figure claims are judged from captions and text only.*

**Literature check status.** `related_search.py` was run in strict mode. Two queries reached the API and both failed with `HTTP 429` (arXiv rate limiting); one further query was refused for having 5 concept words. No results were kept, so Phase 1.5 produced no ledger, no novelty profile, no baseline-scout table. Per the skill's fallback, the Domain Reviewer relies on knowledge and every recommended reference is marked `[verify]`. The integrity scan (`integrity_scan.py`, Phase 0) found no reviewer-directed text or hidden characters; the reviewers read the redacted copy.

---

## 📋 Phase 0 — Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow |
| Primary Discipline | Machine learning → ML for optimization / learning-to-optimize, power-systems datasets |
| Secondary Discipline(s) | Power systems operations (OPF), conic and nonlinear optimization |
| Paper Type | Dataset (with a software toolkit and evaluation guidelines); composite weights: dataset |
| Core Technique(s) | Demand-sampling data augmentation of PGLib-type snapshots; AC/SOC/DC-OPF solving (Ipopt, Clarabel, HiGHS); primal and dual solution storage; PyTorch layers for optimization proxies |
| Target Venue | ICLR (stated by user); profile key `iclr`; cycle 2026, scale status secondary |
| Venue-Specific Notes | none; ICLR reviewers see Soundness/Presentation/Contribution and a rating on {0,2,4,6,8,10}. A datasets-and-benchmarks contribution is judged on usefulness plus evidence that it works as intended |
| Paper Maturity | Submission-ready in form, but no experimental section ("Preprint." footer on p. 1) |
| Ethics-Relevant Content | none (synthetic or public grid test cases; no personal data). Environmental cost of data generation is reported in Appendix C |

### Claimed Contributions (as stated by the authors, §1.3)
- **C1.** Standardized datasets of large-scale OPF instances, "over 10,000,000 OPF samples", from a "realistic and reproducible data augmentation methodology", with a train/test split.
- **C2.** "the first OPF dataset to incorporate realistic time-series data for large-scale power systems" (Texas7k, Midwest24k).
- **C3.** Complete primal and dual solutions for AC, SOC and DC formulations, "a unique feature compared to existing literature".
- **C4.** Evaluation metrics for "objective and fair comparison", with guidelines on benchmarking (§5).
- **C5.** The `PGLearn.jl` data-generation library and the `ML4OPF` PyTorch library (§4).

### Paper memory (factual record shared with all reviewers)
- **Data/setup:** 15 snapshots in Table 1 (6 small, 4 medium, 3 large, 2 extra-large; §3 text says "14"). Demand sampling: Algorithm 1, global factor `b ~ U(bl,bu)` times per-load, per-component `U(1-ε,1+ε)` noise, ε = 20% for all cases; global range width fixed at 40% (Table 1 "Global range"); `bu` found by stepping reference load in 10% steps until infeasible (§3). N−1 status sampling follows OPFData (§3). Time series: one synthetic year at hourly resolution, cubic-spline interpolated to 5 min (Texas7k) and 10 min (Midwest24k) (§3). Split: feasible-for-all-formulations samples, shuffled with `MersenneTwister(42)`, first 80% train, rest 20% test, plus an `infeasible` set (§3). Solvers: Ipopt + MA27, Clarabel, HiGHS (App. A.2). Compute: 29,876.65 CPU-hours, 2.2 TB (App. C). Licence: code MIT (§4); data licence not stated.
- **Headline numbers:** >10,000,000 samples (Abstract-level claim in §1.3, §7); 29,876.65 CPU-hours (App. C).
- **No experiments:** the paper contains no trained ML model, no baseline result, no solver-versus-proxy timing and no statistics on feasibility rates or sample counts per case. Tables are dataset statistics (Table 1) and file formats (Tables 2–7).
- **Appendix:** full AC/SOC/DC formulations and duals (Models 1–5), file formats, compute resources.
- **Unverifiable:** Figure 1 and Figure 2 (not available); code and data links were removed in the blinded copy.

### 👥 Review Team (fictional personas)

**EIC (meta-reviewer): Dr. Ingrid Valtonen**, area chair, large public research university (Northern Europe). Senior faculty; learning-to-optimize, ML benchmarks. Style: asks whether the evidence supports each stated purpose before weighing novelty.
**Reviewer 1 (Methodology): Dr. Anselm Okoro**, optimization and ML lab, national research institute (West Africa/Europe). Mid-career; optimization proxies, evaluation protocols, solver-generated labels. Style: wants every dataset claim backed by a measurement.
**Reviewer 2 (Domain): Prof. Lucía Brandvold**, power-systems group, technical university (South America). Senior faculty; OPF data generation, grid test cases, ML for OPF literature. Style: checks positioning against prior datasets and baselines.
**Reviewer 3 (Perspective): Dr. Rashid Teixeira**, system-operations team, independent system operator (North America). Senior industry scientist; market clearing, forecasting. Style: constructive, asks how it would be used in operations.
**Reviewer 4 (Generalist): Dr. Hana Ostrowski**, ML group, mid-size university (Central Europe). Mid-career; deep learning generalist. Style: typical programme-committee member; weighs clarity and venue fit.
**Devil's Advocate: Prof. Tomás Eriksen-Adeyemi**, evaluation-methodology and causal-inference group, research university (East Asia). Senior faculty. Style: rigorous, never hostile; attacks the logic of "standardization".

*Personas are fictional. Assumptions: paper type dataset; venue as stated; ICLR base rate ≈ 27% accepted.*

---

# Phase 1 — Five Reports

---

# Peer Review Report

## Paper: PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow
## Reviewer: Dr. Anselm Okoro, Reviewer 1 — Methodology (optimization and ML lab, national research institute; fictional persona)
## Expertise: optimization proxies, evaluation protocols for learned solvers, solver-generated labels
## Date: 2026-11-10

## Summary
The paper releases datasets of OPF instances and solutions for 15 grid snapshots (14–23,643 buses) under AC, SOC and DC formulations, including primal and dual solutions, generated with a demand-sampling scheme that adds a global scale factor to per-load noise (§3, Algorithm 1). It also releases a Julia generator and a PyTorch library, and gives prose guidance on metrics for optimization proxies (§5). The paper argues this will standardize evaluation and make comparison fair.

## Strengths
### S1: Scale and breadth of the artifact
Table 1 spans 15 snapshots from 14 to 23,643 buses, with three formulations per instance; Appendix C reports 29,876.65 CPU-hours, so the generation effort is substantial and reusable.
### S2: Complete label schema including duals
Appendix B (Tables 2–7) documents every primal and dual key and its constraint number, and `meta.h5` stores termination status, solve time and dual objective (Table 3). This is a useful, well-specified schema.
### S3: Reproducible generation and split
Seeded generation (`MersenneTwister(42)`, §3), open-source solvers and stated hardware (App. C) make regeneration plausible; the instruction to keep the test split untouched (§3 "Train-Test Split") is correct practice.
### S4: Sensible thinking about what to measure
§5.1 notes that optimality gap alone is unfair when predictions are infeasible, and §5.2 separates data-generation, training, inference and throughput; the caveat that solver times in the metadata are over-estimates (§5.2) is honest.

## Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | realistic, standardized datasets, >10M samples | §1.3, §3 | Table 1 (snapshot stats only); Algorithm 1 | Partially: scale asserted, no per-case counts; "realistic" untested |
| C2 | first realistic large-scale time series | §1.3, §3 "Time-Series Sampling" | cubic-spline interpolation of synthetic hourly data | Partially: synthetic and interpolated; "realistic" untested |
| C3 | complete primal/dual solutions | §2.2, App. B | Tables 4–6 schema | Supported as schema; label quality (tolerances, gaps) not reported |
| C4 | metrics for objective, fair comparison | §5 | prose descriptions | Unsupported: no formulas, no reference numbers, never applied |
| C5 | tooling | §4 | module list | Supported as description; no usage evidence |

## Weaknesses
### W1: The paper contains no experiment showing the datasets and metrics do what is claimed
The central purpose is "fair comparison of various methodologies" (Abstract), yet no model from ML4OPF (§4.2 lists the Lagrangian Dual Framework, a penalty method and E2ELR) is trained or evaluated, and none of the §5 metrics is ever computed. Without a baseline table the community cannot tell whether the datasets are learnable, whether the metrics separate methods, or how hard each case is.
- **Suggested Fix**: Add a benchmark section: at least three ML4OPF models on 4+ cases (one per size class) for AC, SOC and DC, with all §5 metrics, mean ± std over ≥3 seeds, and solver reference times. Roughly 150–300 GPU-hours.

### W2: The "realistic" sampling is asserted, and its benefit over uncorrelated sampling is not measured
Algorithm 1 uses a single scalar `b` and independent uniform per-load noise, so all samples lie within ±20% of a ray through the reference demand; the claim that this "mimics real power system behavior" rests on a non sequitur about day-ahead training (§3 "Demand Sampling"). The only evidence is Figure 2, whose caption describes limitations of uncorrelated sampling, not PGLearn's own distribution (figure unavailable; judged from caption).
- **Suggested Fix**: Compare total-demand and spatial-correlation statistics of PGLearn samples with real load data (the public sources named in §3 "Time-Series Sampling"), and train one proxy on uncorrelated versus PGLearn data and test across demand ranges.

### W3: Train/test split is a random shuffle, with no treatment of the time-series datasets
§3 "Train-Test Split" shuffles all feasible samples and takes 80%/20%. For Texas7k and Midwest24k the samples are 5- and 10-minute spline interpolations of hourly knots (§3), so a test sample is a smooth function of the same hourly values that adjacent training samples are built from. This risks near-duplicate leakage and optimistic test results. The text does not say whether time-series datasets are split differently.
- **Suggested Fix**: For time-series data, split by contiguous blocks (e.g., by week or month) and state this; report a leakage check (nearest training sample distance for test inputs).

### W4: Missing label-quality and dataset-composition statistics (E8)
Table 1 gives no samples per case, no train/test/infeasible counts, no feasibility rate. The "global range" is set by stepping the noiseless reference load until infeasible (§3), but ε = 20% noise is applied on top, so the infeasible fraction is unknown. Solver tolerances are not stated; AC solutions come from a local solver and "global optimality of AC-OPF solutions is not guaranteed" (App. A.2.1); no primal-dual gap statistics for SOC/DC are given although `dual_objective_value` is stored (Table 3). Also, only samples feasible for all three formulations are kept (§3), which can bias the set toward easier inputs.
- **Suggested Fix**: Add a per-case table (counts by split, infeasible fraction, mean/max solve time, optimality tolerance, primal-dual gap distribution, AC-versus-SOC gap).

### W5: Evaluation "tools" are prose guidelines
§5 describes optimality gap, constraint violations, distance to feasibility and distance to optimum in words only; there are no formulas, normalisation conventions (per-unit, relative versus absolute), aggregation rules or reference values. §4.2 lists parsers, layers, functional, formulations and models but names no metrics module, while the Abstract promises tools for "training, evaluating, and benchmarking". Distance to feasible set requires a projection solve (§5.1) whose cost at 13,659 buses is not discussed.
- **Suggested Fix**: Define each metric mathematically, release a reference implementation, and publish reference numbers.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E6 | §3 vs Table 1 | "PGLearn considers a total of 14 snapshots" | Table 1 lists 15 cases; the size categories are 6+4+3+2 = 15 | Counted rows and category list | High | MINOR | State 15 or explain |
| ERR-2 | E6 | App. A.2.2 | "(11b), (11c), (11d), (11e), (11f), (11e)" | (11e) repeated; the sixth should refer to (11g) by Model 2's numbering | Cross-referenced Model 2 | High | MINOR | Correct reference |

**Recomputed:** Global-range widths in Table 1 are 40 percentage points for all 15 cases (matches §3). CPU-hours: 19,196.26 + 2,199.04 + 8,481.34 = 29,876.64 versus 29,876.65 stated (rounding; fine).

**Minor:** typos "Scarsity" (§1.1 heading), "slighly" (App. A.2.2), "prepring" (reference list).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound generation pipeline, but no validation of claims |
| Clarity | 3 | Clear prose and schema |
| Significance | 2 | Useful if validated; narrow audience |
| Originality | 2 | Incremental over OPFData |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a dataset paper with no model results or validation of its central "realistic/standardized" claims sits with typical rejected submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Solid solver setup; unvalidated sampling, leakage risk, missing tolerances |
| Clarity & Presentation | 64 | Competent | Clear structure; prose-only metrics |
| Novelty & Originality | 50 | Developing | Sampling tweak plus duals and formulations |
| Significance & Impact | 58 | Competent | Real utility to a sub-community |
| Experimental Validation | 30 | Developing | No experiments at all |
| Reproducibility | 66 | Competent | Seeds, hardware, open solvers; links blinded, tolerances missing |
| Ethical Compliance | 62 | Competent | Limitations section present; low stakes |

## Questions for Authors
1. What are the sample counts and infeasible fractions per case and split? (A table would remove my main reproducibility concern.)
2. How are time-series datasets split? A block split with unchanged conclusions would raise my score.
3. Which solver tolerances were used, and what is the distribution of primal-dual gaps for SOC/DC?
4. Can you show one proxy trained on PGLearn versus uncorrelated data, evaluated across total-demand ranges?
5. What do the metrics in §5 give for the three ML4OPF models, so reviewers can see that they discriminate?

## Limitations Assessment
**Partially.** §6 covers synthetic data and limited topology variation, but not the absence of validation, the single-scalar correlation structure, local-optimum AC labels, or linear-only costs (App. A.2.1).

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): A valuable artifact whose central claims (realism, fair comparison) are not tested by any experiment.

## Confidence
**4**: Read the paper and appendix fully; did not see the figures or the released artifacts.

---

# Peer Review Report

## Paper: PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow
## Reviewer: Prof. Lucía Brandvold, Reviewer 2 — Domain (power-systems group, technical university; fictional persona)
## Expertise: OPF data generation, grid test cases, ML for OPF
## Date: 2026-11-10

## Summary
The paper positions itself against earlier OPF datasets and generators (OPFSampler, OPFLearn, OPFData) and claims the first collection that is maintained, large-scale and uses "realistic sampling schemes" (§1.2). Its differences from the closest work, OPFData, are correlated demand sampling, DC and SOC formulations, dual solutions, time-series data for two systems and released generation code.

## Strengths
### S1: Clear gap statement against the nearest dataset
§1.2 states concretely what OPFData lacks (uncorrelated perturbations, AC only, no duals or solve-time metadata, no source code), which makes the delta checkable.
### S2: Right grid cases
The snapshots (§3) include PGLib-style European and French cases, NewYork2030, Texas7k and Midwest24k, and the smaller IEEE cases used in earlier ML-for-OPF work, so results can be linked to prior literature.
### S3: Dual information is a timely addition
§2.2 connects duals to recent dual-proxy work (Qiu et al.; Tanneau and Van Hentenryck; Kotary and Fioretto) and to price formation; the weak-duality remark in App. A.1.2 for bounded formulations is correct and useful.
### S4: Honest scope on topology
§6.1 admits that only single line or generator removals are modelled.

## Weaknesses
### W1: Novelty over OPFData is modest and the "realistic" claim is not demonstrated
The differentiators are one sampling knob (a global scale factor, §3 Algorithm 1), additional formulations and released code. The paper does not show that correlated sampling yields more realistic or more useful data than OPFData's scheme; it argues this through Figure 2, whose caption only concerns uncorrelated sampling. Per-claim verdicts (knowledge only, no literature check): C1 incremental; C2 medium; C3 medium; C4 incremental; C5 medium.
- **Suggested Fix**: Add a quantitative comparison with OPFData's sampling on one shared case (same size, distributions, difficulty for a proxy).

### W2: The time-series claim is stronger than the construction
C2 says "realistic time-series data", but §3 uses one synthetic year at hourly resolution cubic-spline interpolated to 5 or 10 minutes. Interpolation adds no sub-hourly variability, so the data cannot represent ramps or forecast errors, which matter in real-time operation. The paper cites Chatzos et al. [2022] on time-series reconstruction (§1.2) as industry-data work but does not discuss how its approach differs from interpolation.
- **Suggested Fix**: Reword to "synthetic, interpolated time series", or add stochastic sub-hourly variation; compare with Chatzos et al.

### W3: Related work omits the ML-for-OPF methods and benchmark practice the datasets target
§1.2 lists data generators only. The learning-side literature (DeepOPF-style direct predictors, GNN-based OPF, Lagrangian-dual training) appears only as citations in passing (§2.2, §4.2), and no benchmark conventions from other ML domains are discussed. A reader cannot tell which methods the benchmark is designed to rank.
- **Suggested Fix**: Add a paragraph mapping method families to the datasets, and say which families PGLearn supports out of the box.

### W4: Citation and attribution issues (E7)
Jabr [2006a] and Jabr [2006b] are the same paper listed twice (both "Radial distribution load flow using conic programming", IEEE TPS 21(3)); §2.1 attributes the SOC-OPF to [2006a], a radial-network paper, while App. A.2.2 cites [2006b, 2007] (the meshed-network paper is the 2007 one). OPFData is cited as an arXiv preprint (Lovett et al., 2024); the final venue should be checked and cited [verify].
- **Suggested Fix**: Merge duplicate entries; cite the meshed-network paper in §2.1.

### W5: "Largest/first" positioning is unverifiable as worded
The Abstract and §1.3 say "for the first time" and "unique feature"; §1.2 says no prior dataset is "actively maintained, considering large power networks, and using realistic sampling schemes" at once. These conjunctions of qualifiers make the claim unfalsifiable. A literature check was not possible (HTTP 429), so I could not verify prior datasets beyond those cited.
- **Suggested Fix**: State precisely what is new per property (formulations, duals, time series, correlated sampling) rather than a conjunction.

## Missing References
*No literature check results were available (arXiv HTTP 429). Entries below are from knowledge; all are `[verify]` and none is claimed as a required comparison.*
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Pan, Zhao, Chen — DeepOPF line of direct DC/AC-OPF prediction (IEEE Smart Grid conferences, c. 2019–2021) `[verify]` | Standard supervised OPF baselines the datasets should support |
| Important | Fioretto, Mak, Van Hentenryck — "Predicting AC optimal power flows: combining deep learning and Lagrangian dual methods", AAAI 2020 `[verify]` | Original conference version of the cited Lagrangian dual framework |
| Important | Zamzam and Baker — "Learning optimal solutions for extremely fast AC optimal power flow", SmartGridComm 2020 `[verify]` | Early large-sample AC-OPF learning with its own sampling scheme |
| Important | Owerko, Gama, Ribeiro — "Optimal power flow using graph neural networks", ICASSP 2020 `[verify]` | Graph-based OPF learning; relevant to the data format |
| Helpful | Varbella, Gjorgiev, Sansavini — "PowerGraph: A power grid benchmark dataset for graph neural networks" (2024) `[verify]` | Adjacent power-grid ML benchmark |
| Helpful | Takamoto et al. — "PDEBench" (NeurIPS 2022 Datasets and Benchmarks) `[verify]` | Example of a dataset paper with standard metrics and baseline tables |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Pipeline sound; claims untested |
| Clarity | 3 | Well organized |
| Significance | 2 | Useful, narrow |
| Originality | 2 | Incremental over OPFData |

## Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the delta to the closest prior dataset is real but small, and nothing shows it matters downstream.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Correct formulations; unvalidated sampling |
| Clarity & Presentation | 66 | Competent | Clear |
| Novelty & Originality | 48 | Developing | Incremental over OPFData; combination of features |
| Significance & Impact | 58 | Competent | Useful for the sub-field; narrow venue audience |
| Experimental Validation | 35 | Developing | No model or baseline evidence |
| Reproducibility | 68 | Competent | Open code, seeds, hardware |
| Ethical Compliance | 64 | Competent | Limitations discussed |

## Questions for Authors
1. Which datasets does the "first" in C2 refer to, and how do the time series differ from Chatzos et al. [2022]? A precise answer would raise my novelty score.
2. How does PGLearn's total-demand distribution compare with OPFData's for the same case?
3. Is the SOC-OPF defined per branch (App. A.2.2) giving different relaxations from PowerModels on meshed networks with parallel branches?

## Limitations Assessment
**Partially.** Data limits are acknowledged (§6.1); limits of interpolated time series are not.

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): Useful artifact; incremental delta over the closest dataset, with positioning claims that outrun the evidence.

## Confidence
**4**: Know the OPF literature well; no literature search results were available, so some positioning judgements rest on memory.

---

# Peer Review Report

## Paper: PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow
## Reviewer: Dr. Rashid Teixeira, Reviewer 3 — Perspective (system-operations team, independent system operator; fictional persona)
## Expertise: market clearing, load forecasting, operations practice
## Date: 2026-11-10

## Summary
The paper offers the ML community a ready-made collection of OPF problems at realistic grid sizes, with multiple formulations and dual values, plus code to regenerate or extend it. From an operations viewpoint, the main contribution is lowering the cost of experimenting at scale, since real operator data cannot be shared (§1.1).

## Strengths
### S1: Addresses a real access problem
§1.1 correctly notes that operator data is restricted and that each team regenerating data wastes compute; Appendix C (29,876.65 CPU-hours, 2.2 TB) shows how large that cost is.
### S2: DC and SOC variants match what markets actually solve
§1 notes that operators solve convex or linear formulations; providing DC and SOC solutions alongside AC lets researchers study the formulations that matter in practice.
### S3: Dual solutions connect to prices
§2.2 observes that duals underlie price formation, opening a path to market-oriented learning research.
### S4: Open licensing of code and honest limitations
Code is MIT-licensed (§4); §6 lists data and topology limitations and planned reserve products and piecewise-linear costs (§6.2).

## Weaknesses
### W1: Only load varies, and costs are linear — far from market-clearing problems
Samples vary active and reactive demand (and single outages, §3); `formulations` assumes "only pd and qd vary per sample" (§4.2); App. A.2.1 says "PGLearn currently supports linear objective functions" and Table 7 lists only `c1`. Real clearing problems have renewable injections, quadratic or piecewise-linear costs, reserves and unit commitment, so models trained here may not transfer.
- **Suggested Fix**: Add generation-side variability (renewable availability) and quadratic costs in the next release; state this prominently in the abstract.

### W2: Demand correlation structure is not grounded in observed behaviour
One global factor with independent ±20% per-load noise (Algorithm 1) yields a rank-one correlation structure. Real demand has regional and sectoral structure (weather zones, time of day). The paper cites public time series (§3 "Time-Series Sampling") but does not use them to calibrate the noise level ε = 20%, set identically for all cases.
- **Suggested Fix**: Calibrate or at least sensitivity-test ε and spatial correlation against public load data.

### W3: Ability of the benchmark to indicate operational usefulness is unclear
Metrics (§5) include optimality gap, violations and timing, which is good, but no threshold is proposed for what counts as operationally acceptable (e.g., violation tolerances operators accept) and no discussion of how a proxy would be used (warm start, screening, direct dispatch).
- **Suggested Fix**: Add a short "intended use" section with tolerance guidance, framed as examples.

### W4: Assumption that AC-OPF solutions from a local solver are ground truth
Ipopt solutions may be local optima (App. A.2.1 acknowledges this). For learning, label noise of this kind matters for evaluating "optimality gap".
- **Suggested Fix**: Report the AC–SOC gap per case as a sanity bound.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | No experiments, but sound engineering |
| Clarity | 3 | Clear |
| Significance | 3 | Strong practical access value |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 62% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: genuine community utility and a large, careful artifact outweigh the missing validation for me, though not decisively.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Correct formulations and pipeline |
| Clarity & Presentation | 70 | Competent | Clear |
| Novelty & Originality | 58 | Competent | Combination of features |
| Significance & Impact | 68 | Competent | Lowers the barrier for ML-for-OPF research |
| Experimental Validation | 45 | Developing | No evidence beyond dataset statistics |
| Reproducibility | 72 | Competent | Seeds, open solvers, documented schema |
| Ethical Compliance | 68 | Competent | Compute cost reported; limitations honest |

## Questions for Authors
1. Do you plan renewable-generation variability, and would the schema (Table 2) accommodate it without breaking compatibility?
2. What total-demand range does a typical day-ahead operator forecast cover relative to your 40% width? A match would raise my significance score.
3. How will versions of the datasets be managed so that published results stay comparable (§6.2 says datasets will be "updated over time")?

## Limitations Assessment
**Partially.** Good on data limitations; silent on cost structure and on generation-side uncertainty, which matter for deployment.

## Ethics Review Flag
**No.**

## Overall Score
**4** (Borderline Accept): A useful, carefully built resource whose practical value for the community outweighs, narrowly, the lack of experiments.

## Confidence
**3**: Strong on operations; less sure how ICLR weighs software and dataset papers.

---

# Peer Review Report

## Paper: PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow
## Reviewer: Dr. Hana Ostrowski, Reviewer 4 — Generalist (ML group, mid-size university; fictional persona)
## Expertise: deep learning, constrained learning
## Date: 2026-11-10

## Summary
PGLearn is a package of OPF datasets (15 grids, AC/SOC/DC, primal and dual solutions, some time series), a Julia generator and a PyTorch toolkit, together with advice on how to evaluate optimization proxies. The goal is a common basis for ML-for-OPF research.

## Strengths
### S1: Clear motivation and a gap that is easy to grasp
§1.1 explains why fragmented sampling blocks comparison, and Figure 2's caption conveys the point about narrow total-demand ranges (figure unavailable).
### S2: Well-organized, readable paper
The flow from formulations (§2) to data (§3) to tools (§4) to metrics (§5) to limitations (§6) is easy to follow; Table 1 is an effective summary of the collection.
### S3: Concrete, reusable artifacts
Appendix B documents file layout and schemas, and App. C reports the compute budget.
### S4: Useful guidance on what makes OPF learning different
§5 stresses reporting constraint violations and data-generation time, which general ML readers would otherwise miss.

## Venue fit — criteria checklist (ICLR, assumed profile)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Not met | no experiments; §1.3 claims untested |
| Presentation | Met | whole paper |
| Contribution to ICLR audience (representation learning, optimization, datasets) | Partly | §1, §2.2 |
| Dataset/benchmark expectations: baselines, documentation, licensing | Not met | no baselines; data licence not stated (only code is MIT, §4) |
| Reproducibility: code, seeds, hardware | Met (links blinded) | §3, §4, App. C |

## Weaknesses
### W1: Reads as a technical report; the ML contribution is not demonstrated
Section 4.2 describes implemented models and layers and §5 discusses metrics, but nothing is trained or measured. A typical ICLR dataset or benchmark paper shows that the data supports learning and that results differ between methods.
- **Suggested Fix**: Add an experiments section with at least three baselines on several cases (see R1-W1).

### W2: Dataset documentation is incomplete for a dataset paper
There is no per-case sample count, no feasibility statistics, no licence for the data (only "MIT-licensed open-source repositories", §4), no hosting or versioning plan beyond "updated over time" (§6.2), and no datasheet-style summary.
- **Suggested Fix**: Add a datasheet in the appendix: counts, licence, hosting, versioning, intended and unintended uses.

### W3: Overstated framing relative to content
The Abstract describes "a robust toolkit for training, evaluating, and benchmarking" and "standardizing performance evaluation across the field", while §4.2 names no metrics module and §5 offers recommendations, not a standard. Terms like "democratizing" sit alongside a 2.2 TB collection (App. C).
- **Suggested Fix**: Tone down to "guidelines", or release and demonstrate reference metric code.

**Minor:** "14 snapshots" versus 15 in Table 1; typos ("Scarsity", "slighly").

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | No evidence of claims |
| Clarity | 3 | Clear |
| Significance | 2 | Useful, narrow |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: well-presented and useful, but missing the empirical component typical of accepted dataset papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound pipeline, untested claims |
| Clarity & Presentation | 70 | Competent | Well organized; minor typos |
| Novelty & Originality | 52 | Developing | Incremental |
| Significance & Impact | 60 | Competent | Useful niche resource |
| Experimental Validation | 36 | Developing | None |
| Reproducibility | 70 | Competent | Seeds, hardware, schema |
| Ethical Compliance | 64 | Competent | Basic |

## Questions for Authors
1. Is the data licence the same as the code licence? Clarifying would resolve a reproducibility concern.
2. What did the authors learn from running ML4OPF models on PGLearn that motivated the guidelines in §5?
3. Is the linear solver stack fully open? §1.3 says it "relies only on open-source solvers" while App. A.2.1 names MA27 through LibHSL, which I believe has its own licence [verify].

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3** (Borderline Reject): Useful and clear, but without the baseline evidence and documentation expected of a dataset paper at this venue.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow
## Reviewer: Prof. Tomás Eriksen-Adeyemi (evaluation-methodology and causal-inference group, research university; fictional persona)

## Steelman
A large, carefully engineered, open collection of OPF instances with duals, multiple formulations and generation code removes a real barrier: most teams cannot afford 30k CPU-hours, and fragmented sampling prevents comparison. Even without experiments, a schema-complete release with seeds and open solvers is a useful public good.

## Core Argument Chain
1. ML-for-OPF progress is hindered by the lack of standardized data and metrics (Abstract, §1.1).
2. Prior datasets use uncorrelated sampling that gives narrow, simplistic distributions (§1.1, Figure 2).
3. PGLearn's sampling (global factor plus local noise, Algorithm 1) is "realistic" and gives wider coverage (§3).
4. PGLearn adds formulations, duals, time series, and code (§1.3).
5. The §5 guidelines make evaluation objective and fair.
∴ PGLearn standardizes the field and accelerates research.

## Strongest Counter-Argument
"Standardization" is a claim about the field's behaviour, and the paper provides no evidence for any link in its chain. (a) The superiority of the sampling scheme is argued only against a straw distribution: Figure 2's caption describes "limitations of sampling strategies that do not consider correlations", not PGLearn's own samples, and no real load data is used for comparison. A single scalar times independent uniform noise is a rank-one correlation structure; it widens the total-demand range, but it is not shown to be closer to operations. (b) Nothing demonstrates that rankings of methods on PGLearn are meaningful: no model is trained, no metric is computed, no variance across seeds or cases is shown, so the claim that the benchmark enables "fair comparison" has no observation behind it. A benchmark whose difficulty is unmeasured can mislead as easily as a fragmented ecosystem. (c) The random 80/20 shuffle (§3) applied to interpolated time-series samples risks near-duplicates across splits, so even the test protocol may inflate scores for exactly the datasets advertised as novel. (d) Labels are local-optimum AC solutions with unreported tolerances (App. A.2.1), and AC duals are not certificates (App. A.1.1: Lagrangian bound is NP-hard to evaluate), so "complete primal and dual solutions" does not mean "reliable". The authors can survive this by running a modest benchmark and a distributional comparison; without them the central claims are assertions.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The collection exists and the claims can be narrowed (to "a large public collection and guidelines") without contradiction from the paper's own evidence; the gaps are missing evidence, not contradicted claims.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §1.3 C1, §3, Figure 2 caption | "Realistic" sampling asserted, never compared with real data or with prior sampling downstream | Distribution comparison plus downstream experiment |
| DA-M2 | Evidence/Scope | Abstract, §5, §7 | "fair comparison" and "standardizing" claims have no benchmark results; evidence supports a weaker claim (narrow wording) | Baseline table, or reword |
| DA-M3 | Logic/Protocol | §3 "Train-Test Split", "Time-Series Sampling" | Random shuffle of interpolated samples; possible leakage in the datasets claimed as novel | Block split by time; leakage check |
| DA-M4 | Evidence | App. A.2.1, A.1.1, §2.2 | Label quality: local AC optima, unreported tolerances and gaps; AC duals not certificates | Report gaps and tolerances; caveat AC duals |
| DA-M5 | Overclaim | Abstract, §1.3 "first" | "first ... realistic time-series" for synthetic, interpolated data; unfalsifiable conjunction in §1.2 | Narrow wording per property |
| DA-M6 | Selection bias | §3 "Train-Test Split" | Only samples feasible for all three formulations are retained, which may bias toward easier inputs | Report the infeasible share and its demand distribution |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §3 vs Table 1 | "14 snapshots" versus 15 rows |
| DA-m2 | Scope | §1.3 vs App. A.2.1 | "relies only on open-source solvers" while MA27/LibHSL is named; licensing should be clarified |
| DA-m3 | Citation | References | Jabr 2006a/2006b duplicate entry |
| DA-m4 | Claim | §7 "democratizing" vs App. C | 2.2 TB and heavy generation cost limit access for small teams; framing should acknowledge it |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Number of snapshots | 14 (§3) | 15 rows in Table 1; 6+4+3+2 | No |
| Global range width | 40% (§3) | all 15 rows of Table 1 are 40 points | Yes |
| Total CPU-hours | 29,876.65 (App. C) | 19,196.26 + 2,199.04 + 8,481.34 = 29,876.64 | Yes (rounding) |
| Time-series points (derived) | not stated | Texas7k 5-min year ≈ 365×288 = 105,120; Midwest24k 10-min ≈ 365×144 = 52,560; ≈ 1.6% of 10M | Derived; shows time series are a small share of the collection |

## Ignored Alternative Explanations
- Differences in model performance across datasets could arise from distribution width and noise level rather than from "realism".
- Low-variance data (the authors' complaint about prior work) may be easier to learn; a wider range may be harder without being more useful.
- Random-split accuracy on interpolated series may mostly reflect memorization of neighbouring samples.

## Missing Stakeholder Perspectives
Operators who would rely on tolerance thresholds, researchers with limited storage and compute (2.2 TB), and users who need versioned datasets to keep published results comparable.

## Observations (Non-Defects)
- Seeds, solver versions and hardware are recorded; the test-set instruction is correct.
- Limitations section is present and candid about topology (§6.1).
- The warning that solver times are inflated by congested nodes (§5.2, App. C) is a model of honest reporting.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Untested sampling claim; leakage risk; label quality unreported |
| Clarity & Presentation | 64 | Clear |
| Novelty & Originality | 44 | Incremental over OPFData |
| Significance & Impact | 54 | Useful but unproven |
| Experimental Validation | 26 | None |
| Reproducibility | 62 | Seeds and hardware; missing tolerances and licence |
| Ethical Compliance | 60 | Limitations present |

**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central claims are untested and the test protocol has an unaddressed leakage risk.

## Overall: 2 | Confidence: 4

---

# Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness (as first drafted) | Action | Reason |
|--------|-----------------------------|--------|--------|
| R1 | "No code or data link given" | Dropped | Links are removed in the blinded copy ("[link removed]"); treated as unverified, not missing |
| R1 | "Compute cost not reported" | Dropped | Appendix C reports 29,876.65 CPU-hours and hardware |
| R3 | "No discussion of limitations or environmental cost" | Dropped / rewritten | §6 and App. C exist; rewritten as W1/W4 about the specific missing limitations |
| R2 | "Time-series prior work ignored" | Rewritten | Chatzos et al. [2022] is cited in §1.2; reworded to "cited but not differentiated" |
| DA | "No limitations section" | Dropped | §6 exists |
| R4 | Typos as a weakness | Moved to Minor | Cosmetic |
| R3 | W3 (intended-use section) | Kept, ordered last | Actionable; lower severity |
| R1 | Fig. 2 "does not show PGLearn's own distribution" | Rewritten as caption-based, flagged "figure unavailable" | Figure could not be inspected |

Scores were not changed.

---

# Phase 2 — Synthesizer Part A: Package for the EIC

**Merged issues and classes.**
| Issue | Sources | Class |
|-------|---------|-------|
| No experiments or baselines; claims of fair comparison untested | R1-W1, R4-W1, DA-M2, R2-W1 (partly) | CONSENSUS-4 (hinge) |
| "Realistic" sampling untested against real data or prior sampling | R1-W2, R2-W1, R3-W2, DA-M1 | CONSENSUS-4 (hinge) |
| Time-series split/interpolation leakage and "realistic" wording | R1-W3, R2-W2, DA-M3, DA-M5 | CONSENSUS-3 (hinge) |
| Missing dataset statistics and documentation (counts, tolerances, licence, datasheet) | R1-W4, R4-W2, DA-M4, DA-M6 | CONSENSUS-3 |
| Evaluation tools are prose only; overstated framing | R1-W5, R4-W3 | CONSENSUS-2 |
| Limited problem scope (load-only, linear costs) | R3-W1, R1 minor | SOLO |
| Related work gaps; citation issues | R2-W3, R2-W4 | SOLO |
| 14 versus 15 snapshots | R1 ERR-1, R4 minor, DA-m1 | CONSENSUS-3 (cosmetic) |
| SPLIT | R3 (positive on practical value) versus R1/R4/DA (evidence missing) | SPLIT |
| DA-CRITICAL | none raised | — |

**Official score** (script, BEFORE run without EIC weights, `da_critical: []`): official composite 56.8; official rating 3.00; no warnings; dimension spreads all ≤ 19 (largest: Experimental Validation 19, below the 20 flag).

---

# Phase 2 — EIC Meta-Review

*Written by Dr. Ingrid Valtonen (EIC, meta-reviewer). I read the five reports and the package first, then re-read the paper's abstract, §1.3, §3, §4.2, §5, §6, Table 1, App. A.2 and App. C.*

### The Case For and Against
- **For acceptance:** A large, carefully specified public resource (15 grids to 23,643 buses, three formulations, primal and dual labels, schema, seeds, open-source generators) fills a real access gap in ML for OPF, and the authors are candid about topology and data limitations. Dataset papers at ICLR are valued for usefulness, and this one is clearly useful to a community.
- **Against acceptance:** The paper has no experimental content: no model is trained, no metric computed, no comparison of the "realistic" sampling with real data or with OPFData's scheme, and no sample counts or label-quality statistics. The headline purposes, "fair comparison" and "standardizing evaluation", are therefore untested; the time-series datasets use a random split over interpolated samples.

### Verification of Decisive Points
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| No trained model, baseline table or computed metric | R1-W1, R4-W1, DA-M2 | §4.2, §5, §7; Tables 1–7 | Verified | Paper ends at §7; tables are statistics and schemas only |
| "Realistic" sampling not validated; Figure 2 caption concerns uncorrelated sampling | R1-W2, DA-M1 | §3 Demand Sampling, Fig. 2 caption | Verified (caption-based; figure not seen) | §3 text says "as shown in Figure 2"; caption describes only the limitation of uncorrelated sampling |
| Random shuffle split may leak for interpolated time series | R1-W3, DA-M3 | §3 Train-Test Split, Time-Series Sampling | Partly correct | Shuffle and spline interpolation are both stated; the paper does not say time-series sets are split differently, so the leakage is a risk, not a demonstrated error |
| Per-case counts, feasibility fractions, tolerances missing | R1-W4, R4-W2 | Table 1, §1.3, §7, App. A | Verified | Only "over 10,000,000" appears; searched for tolerance, licence, datasheet: none |
| "14 snapshots" versus 15 in Table 1 | R1 ERR-1, DA-m1 | §3, Table 1 | Verified | Cosmetic |
| Evaluation "tools" are prose; no metrics module in §4.2 | R1-W5, R4-W3 | §4.2, §5, Abstract | Partly correct | §4.2 lists `functional` constraint and objective implementations from which violations can be computed; no reference metric code or numbers are described |
| Only load varies; linear costs | R3-W1 | §4.2, App. A.2.1, Table 7 | Verified | Quote "currently supports linear objective functions" |
| AC labels are local optima; duals for AC not certificates | R1-W4, DA-M4 | App. A.2.1, A.1.1 | Verified | The authors state this themselves |
| Time series is "realistic" | R2-W2, DA-M5 | §1.3, §3 | Overstated claim by the authors; reviewers correct | Synthetic hourly data, spline interpolated |
| Jabr duplicate citation | R2-W4 | References | Verified | Same title and volume under two keys |
| "Relies only on open-source solvers" versus MA27/LibHSL | R4 question, DA-m2 | §1.3, App. A.2.1 | Unverified | Licence status outside the paper; kept as a question |
| 29,876.65 CPU-hours | DA | App. C | Verified | Components sum to 29,876.64 |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC weight | Reason |
|----------|---------|------------|-----------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Decisive points (no experiments, missing counts and tolerances, split issue) verified; error log entries hold; claims are measured, not overstated |
| R2 (Domain) | 3 | 4 | 1.0 | Positioning points sound but rest on memory (no literature check); one overstated line on novelty |
| R3 (Perspective) | 4 | 3 | 1.0 | Operations points verified; the positive rating weights practical value, and I do not penalize the role |
| R4 (Generalist) | 3 | 4 | 1.0 | Venue-fit and documentation points verified; one point partly overstated (tools) |
| DA | 2 | 4 | 1.0 | All six MAJOR issues verified or partly verified; Overall 2 is a little low given the contribution but within its role |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

No ceiling applies. DA-M1 to DA-M6 all stay MAJOR: each is a missing-evidence issue that narrows to a weaker claim (a public collection with guidelines), which the evidence does support.

### Final Decision and Justification
Official ratings are R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00; official composite 56.8. With the EIC weights above the EIC-weighted rating is 2.97, composite 56.4, band 3, so the starting point is **3 (Borderline Reject)** and the composite cross-check agrees (no ⚠). I do not depart from it. I considered the case for 4: the artifact is large, useful and well documented in schema, and many accepted dataset papers have single weaknesses. But here three of the four core purposes of the paper (realistic sampling, fair comparison, evaluation standard) have no measurement behind them, the time-series split has an unaddressed leakage risk, and basic dataset documentation (counts, licence, tolerances) is missing. These are fixable within a revision cycle without new datasets, which is why this is a close call and not a clear reject. Judged against the ICLR pool, I place the paper at about the 47th percentile (pool position 47): better than a typical weak submission because the artifact is real and useful, but below the bar of a typical accepted dataset paper. DA ceiling: none. Final (EIC): **3**, which the script maps to an ICLR rating of 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); ICLR sub-scores Soundness 1, Presentation 3, Contribution 2 (scale status: secondary).

---

## Score Summary

### Official Scores and EIC Assessment
| Reviewer | Overall | Conf. | EIC weight | Weight share |
|----------|---------|-------|-----------|--------------|
| R1 | 3 | 4 | 1.25 | 0.246 |
| R2 | 3 | 4 | 1.0 | 0.197 |
| R3 | 4 | 3 | 1.0 | 0.162 |
| R4 | 3 | 4 | 1.0 | 0.197 |
| DA | 2 | 4 | 1.0 | 0.197 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 52 | 56 | 62 | 58 | 48 | 55.2 | 54.8 | 14 |
| Clarity & Presentation | 64 | 66 | 70 | 70 | 64 | 66.8 | 66.6 | 6 |
| Novelty & Originality | 50 | 48 | 58 | 52 | 44 | 50.4 | 50.1 | 14 |
| Significance & Impact | 58 | 58 | 68 | 60 | 54 | 59.6 | 59.2 | 14 |
| Experimental Validation | 30 | 35 | 45 | 36 | 26 | 34.4 | 33.8 | 19 |
| Reproducibility | 66 | 68 | 72 | 70 | 62 | 67.6 | 67.4 | 10 |
| Ethical Compliance | 62 | 64 | 68 | 64 | 60 | 63.6 | 63.4 | 8 |
| **Composite** | 54.5 | 56.5 | 63.5 | 58.4 | 51.0 | **56.8 (before)** | **56.4 (after)** | |

Official rating (plain mean of Overall): 3.00. EIC-weighted rating: 2.97.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 3 / 2 |
| ICLR rating for the final Overall 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |
| ICLR-weighted composite | 56.3 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow" to ICLR. A large public collection of OPF problems with solutions and generation code addresses a real obstacle for machine-learning work on power systems.

**Overall Assessment:** The panel found the resource useful, well organized and carefully specified, but the draft contains no experimental evidence that the datasets and metrics achieve their stated aims. Reviewers were close to unanimous that the evidence does not yet support the claims of realism, fair comparison and standardization.

**Key Strengths Identified by Reviewers:**
1. Scale and breadth: 15 grids up to 23,643 buses, three formulations, primal and dual labels (R1, R2, R3).
2. Reproducible generation: seeds, open solvers, documented schema and compute budget (R1, R3, R4).
3. Honest framing of topology and data limitations (R2, R3, DA).

**Key Concerns Requiring Attention:**
1. No baseline results or computed metrics; the "fair comparison" claim is untested (CONSENSUS-4).
2. "Realistic" demand sampling and time series are asserted, not validated against real data or prior sampling (CONSENSUS-4/3).
3. Random split over interpolated time-series samples risks leakage; dataset statistics, tolerances and licence are missing (CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** The DA argued that "standardization" requires evidence that rankings on the benchmark are meaningful and that its distribution is closer to operations than predecessors'; nothing in the draft measures either. This was ruled MAJOR, not critical, because the claims can be narrowed or supported with a modest benchmark.

**Decision: Borderline Reject (3).** The reasons to reject, namely missing evidence for the central purposes and incomplete dataset documentation, outweigh the real usefulness of the artifact. They are fixable without new data generation. A revision with a baseline table, a distributional comparison, a block-based split for time series, per-case statistics and a datasheet would change the assessment.

Please refer to the Revision Roadmap below for prioritized guidance.

Sincerely,
Dr. Ingrid Valtonen
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No experiments or baselines | R1, R4, DA (+R2 partly) | CONSENSUS-4 |
| Realism untested | R1, R2, R3, DA | CONSENSUS-4 |
| Time-series construction and split | R1, R2, DA | CONSENSUS-3 |
| Missing dataset statistics/documentation | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is practical value enough without experiments? | R3 (Overall 4) | R1, R2, R4, DA | Value is real, but a dataset paper's claims still need evidence; EIC sides with the majority |

### Score Spread Discussion
No dimension exceeded the 20-point flag; Experimental Validation had the widest spread (19, R3 45 versus DA 26). R3 weighs the artifact's engineering; the others weigh the absence of any experiment. The EIC adopts the lower view, since the paper has no experimental section.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Realism untested | Yes (R1, R2, R3) | n/a | n/a |
| DA-M2 | MAJOR | Fair-comparison claim without results | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Time-series split leakage risk | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Label quality unreported | Yes (R1, R3) | n/a | n/a |
| DA-M5 | MAJOR | "first" wording | Yes (R2) | n/a | n/a |
| DA-M6 | MAJOR | Feasible-only filtering | No | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | No baselines or computed metrics; fair-comparison claim untested | R1-W1, R4-W1, DA-M2 | §4.2, §5 | Benchmark table: ≥3 ML4OPF models, 4+ cases across size classes, AC/SOC/DC, all §5 metrics, ≥3 seeds | High; ~150–300 GPU-h | Partly (reduced version on small and medium cases) |
| R2 | "Realistic" sampling not validated | R1-W2, R2-W1, R3-W2, DA-M1 | §3, Fig. 2 | Compare demand statistics with real load data; train on PGLearn versus uncorrelated data across demand ranges | Medium; ~50 GPU-h | Yes (one case) |
| R3 | Split and interpolation for time series | R1-W3, R2-W2, DA-M3 | §3 | Contiguous-block split; leakage check; reword "realistic" | Low–Medium | Yes |
| R4 | Missing dataset statistics and documentation | R1-W4, R4-W2, DA-M4, DA-M6 | Table 1, §3, App. C | Per-case counts, infeasible shares, tolerances, primal-dual gaps; data licence and datasheet | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Evaluation guidelines prose only | R1-W5, R4-W3 | Formal metric definitions; reference code and numbers | Medium | Yes |
| S2 | "first/unique" wording; time-series novelty | R2-W5, DA-M5 | Narrow to per-property claims | Low | Yes |
| S3 | Related work: learning-side methods and benchmark practice | R2-W3 | Add a paragraph; consider the `[verify]` references from R2 | Low | Yes |
| S4 | Citation fixes (Jabr duplicate, OPFData venue) | R2-W4 | Merge entries; update venue after checking | Low | Yes |
| S5 | Load-only variation, linear costs | R3-W1 | State prominently in Abstract; roadmap | Low (text) | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | "14 snapshots" versus 15; (11e) reference; typos | R1, R4, DA | Correct |
| N2 | Intended-use and tolerance guidance | R3-W3 | Add short section |
| N3 | LinearSolver licence statement ("only open-source") | R4, DA-m2 | Clarify |
| N4 | Dataset versioning and hosting plan | R3, R4 | State |
| N5 | "democratizing" versus 2.2 TB | DA-m4 | Provide subsets or download-size guidance |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–3 weeks including experiments (R1 dominates).
- Priority 2: 5 items, about 2–3 days.
- Priority 3: 5 items, under a day.
- **Total estimated revision time**: about 3 weeks.

---

*Provenance notes:* literature check unavailable (arXiv HTTP 429), so no reference was verified; all recommended references are marked `[verify]`. Reports were produced in five sequential passes in one shared context.
