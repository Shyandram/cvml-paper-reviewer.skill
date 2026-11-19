# Review: PGLearn – An Open-Source Learning Toolkit for Optimal Power Flow

(Figures were not available. Figure 2 is judged from its caption and the text only.)

## Summary
The paper presents PGLearn, a datasets-and-tools resource for ML for optimal power flow (OPF). It has three parts:
- **Datasets.** More than 10M OPF instances over 14 PGLib-style grids, from 14 to 23.6k buses. Each instance comes with primal and dual solutions for AC-OPF, SOC-OPF and DC-OPF, plus an N-1 variant (one generator or non-bridge branch removed). Texas7k and Midwest24k also carry synthetic yearly time series, interpolated to 5- or 10-minute resolution.
- **Generation code.** PGLearn.jl (Julia/JuMP) produces the data. Demand sampling uses a global scaling factor b ~ U[b_l, b_u] times per-load, per-component uniform noise of ±20%. The global range is chosen by scaling load in 10% steps until infeasibility. Splits are 80/20 with a fixed seed.
- **ML toolkit and metrics.** ML4OPF (PyTorch) provides parsers, differentiable constraint and objective layers, and a few reference proxy models. The paper also gives recommendations for reporting accuracy metrics (optimality gap, violations, distance to feasibility, distance to optimum) and computational metrics (data-generation, training and inference time, throughput).

## Strengths
- The resource addresses a real gap. ML-for-OPF papers each build their own incompatible datasets, and a shared, large-scale, maintained benchmark would be useful.
- Coverage is broad: 14 grids up to 23k buses, three formulations on the same inputs, and N-1 variants. Complete primal and dual solutions are rarely released. They support dual-proxy work and cross-formulation comparison on identical inputs.
- Global-plus-local correlated demand sampling is a sensible improvement over independent per-load perturbation. The paper motivates it with a concrete example on the 1354-bus system (Fig. 2).
- Time-series data for large systems (Texas7k, Midwest24k) is new for public OPF data.
- Reproducibility is good. Everything is MIT-licensed and uses open-source solvers (Ipopt/HSL MA27, Clarabel, HiGHS). The seed is fixed, the train/test split is fixed, and the data formats are documented in the appendix. Solve-time metadata is released, and the paper notes that these times are biased upward.
- The metric guidelines are reasonable. They stress reporting violations and feasibility distance, not optimality gap alone, and they ask for worst-case inference time.
- The limitations section is honest about synthetic data and limited topology variation.

## Weaknesses
1. **No empirical evaluation of the benchmark.**
   - The paper claims to "standardize performance evaluation" and enable "fair comparison", but reports no baseline results.
   - There are no results for the models in ML4OPF (Lagrangian dual framework, penalty method, E2ELR) on any PGLearn dataset, and no leaderboard or reference numbers.
   - A resource paper should show that the datasets are learnable and discriminative. It should show how difficulty varies with size and formulation, and that methods rank differently under the proposed metrics.
   - The central claim that correlated sampling matters for ML is supported only by a data-distribution illustration (total demand histogram, one branch flow). It is never shown that a model trained on uncorrelated data generalizes worse, or that PGLearn data changes conclusions.
2. **Weak validation of data "realism".**
   - The sampling is a uniform global scale plus i.i.d. uniform ±20% noise per load and component. This is arguably still simplistic. There is no spatial or temporal correlation structure, no region-level correlation, and no comparison with real load statistics.
   - The text says it "mimics real power system behavior", but the justification is indirect. The cited reason is that models are trained day-ahead on forecast ranges, which does not support the specific distribution chosen.
   - The global range is set by a heuristic. It has a fixed 40% width, with b_u found by 10% steps until infeasibility. This is not justified, and it differs per case, so the distributions are not comparable across cases.
   - Renewable generation variability, the stated motivation, is not modelled at all. Only demand varies.
   - The synthetic time series are hourly and cubic-spline interpolated to 5–10 minutes. Spline interpolation yields smooth profiles with no real sub-hourly dynamics, so the "realistic time-series" claim is overstated. It is unclear whether interpolated points are meaningfully different instances.
   - The paper does not specify how the time series are used for train/test splitting. A random 80/20 split over temporally adjacent samples leaks information.
3. **Data quality is under-documented.**
   - The paper gives no statistics on feasibility rates, the size of the "infeasible" split, solver failures, or convergence tolerances.
   - It gives no solve-time distributions per case or total compute.
   - It gives no checks on local optimality for AC-OPF. Ipopt returns local solutions, and the paper only cites past experience that they are close to optimal. Non-unique local optima would make "ground truth" ambiguous, and no verification (for example SOC gap, or a global solver on small cases) is reported.
   - Training and testing sets keep only samples feasible for all formulations. This biases the dataset toward easy instances and removes the hard cases that matter for evaluation. It also makes the sets differ from what a single-formulation user would see.
   - The "Global range" column says nothing about how often instances sit near the infeasibility boundary.
4. **Limited novelty versus OPFData.**
   - The incremental contributions are correlated sampling, DC/SOC formulations, duals, time series for two grids, and code. The N-1 sampling is copied from OPFData.
   - There is no head-to-head comparison with OPFData, such as a model trained on one and tested on the other.
   - The claim of being the "first" with realistic time series and duals is hard to check. The claims that OPFData lacks metadata and source code are fine, but the comparison with prior work is purely descriptive. Related-work claims, such as that none of the existing datasets is "actively maintained", are not supported.
5. **Scope of the benchmark is narrow.**
   - The problem is a single-period, linear-cost OPF with only active/reactive demand varying. There is no reserve, no piecewise-linear cost, no unit commitment, no security constraints, and no varying generator costs or limits. The paper itself says real market formulations are missing, and these are the cases where the DC/SOC motivation lies.
   - Topology variation is limited to a single removed element.
   - ML4OPF `formulations` assumes only pd and qd vary.
   - Large-system datasets without realistic multi-parameter variation limit the claim of closing the gap to industry practice.
6. **Metric guidelines are not operationalized.**
   - The metrics are standard and listed in prose, with no formal definitions. Normalization is not specified: is the optimality gap relative? Is violation per-unit? How are metrics aggregated across constraint groups?
   - Distance to the feasible set needs a projection per instance, which is expensive for large grids. No implementation is described and no cost is given. Hence "standardized evaluation" is a recommendation, not a protocol.
   - There is no discussion of aggregate scoring, of how feasibility and optimality trade off, or of a tolerance standard for deciding whether a prediction is feasible.
   - A wall-clock comparison against solvers is complicated by the single-thread solve times, which the paper admits are over-estimates. It gives no recommendation for a fair baseline.
7. **Fit with ICLR.**
   - The contribution is mainly engineering and data. It fits the datasets-and-benchmarks track, but the paper has little ML content and no ML experiments. It is written for a power-systems audience, and the main text defers all formulations to the appendix.
   - Presentation has minor issues: typos ("Scarsity", "slighly"), a possibly incorrect statement that Jabr's SOC relaxation is "proposed by Jabr [2006a]" (a radial-network paper) while the formulation is for meshed networks, the loosely worded Lagrangian-bound sentence in the appendix, and the ML-training-time sentence in Demand Sampling, which does not logically motivate the sampling scheme.

## Questions
1. Can you report baseline results (at least a simple MLP, penalty, and one feasibility-restoration method) across a few cases, for AC/SOC/DC? Do the metrics distinguish methods? How does difficulty scale from 14 to 23k buses?
2. Does training on uncorrelated (OPFData-like) versus PGLearn sampling change test performance on out-of-distribution total demand? Does a model trained on one dataset transfer to the other?
3. What are feasibility rates per case and formulation? What fraction of the data lies in "infeasible"? How much does the all-formulations-feasible filter change the input distribution?
4. How reliable are the Ipopt AC-OPF solutions? For example, what is the gap to SOC lower bounds on the large cases, and how often are results different under different starting points?
5. How are the time-series train/test splits done? Is the random shuffle split also used for them, and does it leak across neighbouring time steps? How were the synthetic load profiles per bus obtained from the source, and how much of the variance survives spline interpolation?
6. Why are ε = 20% noise and a 40% global range chosen for all cases? How sensitive are the results to them?
7. What are the dataset sizes per case (samples, GB), the storage and access format, and the plan for long-term hosting and versioning?
8. Will the evaluation metrics be released as code in ML4OPF, including the projection-based distance? Is there a reference evaluation script?

## Ratings
- **Soundness:** 2 (the data-generation pipeline looks sound, but the central claims on realism and standardization are not validated)
- **Presentation:** 3
- **Contribution:** 3 (a useful resource, but limited novelty over OPFData and no demonstration of impact)

**Rating:** 4 (marginally below the acceptance threshold; it would move to a 6 with baseline benchmarking results and validation of the sampling claims)

**Confidence:** 3
