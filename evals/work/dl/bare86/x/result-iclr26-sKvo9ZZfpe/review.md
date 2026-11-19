# Review: RRNCO: Neural Combinatorial Optimization for Real-World Routing (ICLR 2026)

Caveat: figures were not available. Fig. 4 (ablation) was judged from its caption and text only, and no numerical values could be read from it.

## Summary
The paper has two contributions.

1. A dataset and generator for "real-world" asymmetric VRPs. It uses 100 cities, each with 1000 points sampled from road networks (OSM) inside a 3x3 km box. A locally hosted OSRM supplies full 1000x1000 distance and duration matrices. Training instances are produced on the fly by subsampling indices from these matrices and adding demands and time windows.
2. RRNCO, an encoder-decoder NCO model. Its pieces are:
   - a MatNet-style row/column embedding;
   - a contextual gate fusing coordinate and (sampled) distance-matrix embeddings;
   - an Adaptation Attention Free Module (AAFM) whose heuristic bias (-alpha log N d_ij) is replaced by a learned bias computed from a distance matrix and an angle matrix, also gated;
   - a decoder borrowed from ReLD/MatNet.

It is evaluated on ATSP, ACVRP and ACVRPTW. Test splits are in-distribution cities, held-out cities, and a "cluster" distribution. RRNCO is compared against POMO, ELG, BQ-NCO, LEHD, MatNet, GOAL, GCN and others. It reports gaps of about 2–4%, against about 4–7% for MatNet.

## Strengths
- It addresses a real gap. Most NCO work uses Euclidean symmetric instances, and asymmetric, road-network-based instances with separate distance and duration matrices are a sensible target.
- An open, locally reproducible OSRM pipeline with fast online instance sampling is practically useful. It avoids commercial APIs and large static datasets. The release of code and data is a plus.
- The comparison set is broad and includes strong classical references (LKH3, PyVRP, OR-Tools), so gaps are measured against strong solvers.
- Training on one set of cities and testing on held-out cities is a sensible protocol, and the ablations (Table 2, Fig. 4) try to isolate the data generator, the gating and the NAB.

## Weaknesses
1. **The "real-world" claim is weak.**
   - Instances come from 3x3 km boxes around city centres, with 1000 candidate points per city. This is a very small spatial scale compared with real logistics: no depots outside the box, no inter-urban routes, no real customer distributions.
   - Points are sampled along road segments, weighted by length. Demands, time windows and "clusters" are synthetic.
   - Durations come from OSRM static speed profiles, with no traffic or time dependence. The asymmetry therefore comes mostly from one-way streets and turn restrictions.
   - The paper does not quantify how asymmetric the matrices actually are. It does not show that the asymmetry is large enough to hurt Euclidean-based solvers. No asymmetry statistics or comparison to real delivery data are given.
   - Points near bridges, tunnels, highways and water are removed, which further biases the data.
2. **The baseline comparison is not well controlled.**
   - Node-only baselines (POMO, MTPOMO, MVMoE, RF, ELG, BQ-NCO, LEHD) are *not retrained* and see only normalized coordinates. They cannot see the asymmetric matrices they are scored on. Their 20–50% gaps mostly show that they are blind to the matrix, not that RRNCO's architecture is better.
   - The meaningful comparisons are MatNet and GCN, the only models retrained on the new data, and the margin over MatNet is small (e.g., 3.98 vs 1.80 on ATSP in-distribution; 7.26 vs 3.45 on ACVRP).
   - Node-only baselines could be given the matrix (e.g., through a distance-aware compatibility) or be retrained. The claim of "consistently outperforming existing neural solvers" is overstated.
3. **The architectural novelty is incremental.**
   - RRNCO combines MatNet row/column encoding, the AAFM of ICAM (with the heuristic bias replaced by a small MLP on distance and angle), the ReLD decoder, and a sigmoid gate. Each piece is standard.
   - The angle feature is computed from coordinates, so it is unclear how it relates to asymmetric travel costs.
   - The inverse-distance sampling of k=25 neighbours (Eq. 4) is a design choice that is not ablated.
   - The ablation gives no seeds or variance, and the differences appear to lie within a narrow band (~3.5–4% gap range on the axis).
4. **The evaluation setup is under-specified.**
   - The problem sizes N used in training and testing are not clearly stated in the main text. No scaling results to larger N are given.
   - It is not clear whether the cost is distance, duration, or a mix, nor how the duration matrix enters the objective and the time-window constraints.
   - Demand and time-window generation is not described in the main paper.
   - The "cluster" OOD distribution is not defined in the main text.
   - Training compute (24 h on 4 A100s) is stated, but baseline budgets are not matched. No multiple training seeds or confidence intervals are reported.
5. **Efficiency claims are not apples-to-apples.** RRNCO is slower than POMO and MatNet in several settings (e.g., 35 s vs 17–18 s for POMO on ACVRPTW; 22 s vs 27 s for MatNet on ATSP is faster, though). Runtimes mix GPU neural solvers with hours-long classical solvers, and the time limits and threads for LKH3, PyVRP and OR-Tools are not specified. "Superior in computational efficiency" is not supported.
6. **Presentation and errors.**
   - Table 1, ATSP, POMO out-of-distribution (cluster): the cost is 30.051 and the gap is 146.926%. The value 30.051 also appears as POMO's OOD-city gap, which suggests a copy error.
   - The Fig. 3 architecture figure is hard to parse, and the ablation figure is hard to read and carries no numbers.
   - Sec. 5 is notation-heavy and inconsistent (e.g., W_D, W_Phi in R^E; the names "Adaption"/"Adaptation Attention Free Module" and "Attention Attention Free").
   - Table 2's "MatNet trained with the ATSP generator" row (110% gap) is an unsurprising result, because that generator never exposes the model to the real structure. A MatNet trained with the noisy generator, or with sparse real asymmetry, is a fairer control.
7. **Limited generalization evidence.**
   - There is no test on external real asymmetric benchmarks (e.g., Osaba, Lee & Chae, which the paper itself cites), no larger scale, and no transfer to commercial-API or traffic-dependent durations.
   - Test cities are 20 held-out cities drawn from the same pipeline and the same box size, so the distribution shift is mild.

## Questions
1. What are N (nodes) for training and testing in each task? Does RRNCO scale to N in the hundreds or thousands, given the B×N×N×E bias tensor?
2. How asymmetric are the matrices (e.g., mean |d_ij − d_ji| / d_ij), and how does a symmetric/Euclidean-trained model's gap change with the degree of asymmetry?
3. Can strong node-based baselines (POMO, ELG, MVMoE, RF) be retrained or given the matrix, so the architectural contribution can be isolated?
4. Which objective (distance or duration) is optimized in ACVRP/ACVRPTW, and how are time windows built on duration?
5. Please provide multiple seeds, and ablations of the angle feature, the k=25 sampling, depth, and the decoder components borrowed from ReLD.
6. Can you evaluate on existing real asymmetric benchmarks, or on regions larger than 3x3 km?
7. How were the time limits and thread counts for LKH3, PyVRP and OR-Tools set? (The LKH3 time is 1.6h in every column.)

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

Overall: a useful open data tool for a legitimate gap. However, the "real-world" framing is overstated, the baseline comparison is largely uncontrolled, the model is an incremental assembly, and the evaluation lacks variance and external validation. A revision with controlled baselines, asymmetry analysis, larger and external benchmarks, and seeds could be a solid dataset/benchmark contribution.
