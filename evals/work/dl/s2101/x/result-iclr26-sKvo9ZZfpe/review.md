# Academic Paper Review — RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization

*Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (user request).*
*Execution note: the five reviewer passes were run one after another in a single shared model context (no delegation); they are role-based passes, not independent agents. Figures were not available (text extraction only): figure-dependent claims are judged from captions and text and marked "unverifiable".*

---

# Phase 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization |
| Primary Discipline | Machine learning → neural combinatorial optimization (vehicle routing) |
| Secondary Discipline(s) | Operations research (VRP solvers); transportation / urban analytics (road-network data) |
| Paper Type | Empirical (composite weights: empirical). It has a resource half (dataset/generator) and a method half; the evaluation and the claimed SOTA concern the method, so the empirical weights are used. |
| Core Technique(s) | Autoregressive encoder–decoder RL (POMO-style REINFORCE), matrix (edge) encoding as in MatNet, attention-free transformer with learned adaptive bias, contextual gating, OSRM-derived instances |
| Target Venue | ICLR 2026 cycle (stated by the user); profile key `iclr` |
| Venue-Specific Notes | Public-review venue; submissions and reviews are public; ICLR rating {0,2,4,6,8,10} (scale status: secondary) |
| Paper Maturity | Submission-ready (full paper with appendix; no limitations section) |
| Ethics-Relevant Content | Web-scraped open map data (OpenStreetMap; licence conditions); geographic coverage and data-quality bias; no human subjects |

### Claimed Contributions (as stated by the authors; claim IDs used by every reviewer)
1. **C1 (resource):** a new, openly available real-world VRP dataset/generator with distance and duration matrices from 100 cities (Abstract; §1 bullet 1; §4; Appendix A).
2. **C2 (method):** an architecture with contextual gating of coordinate and distance embeddings and a Neural Adaptive Bias inside an Adaptation Attention-Free Module (Abstract; §1 bullet 2; §5, Eqs. 4–15).
3. **C3 (result):** "state-of-the-art performance on real-world VRP instances among NCO methods" on ATSP, ACVRP and ACVRPTW (§1 bullet 3; §6.2; Table 1).
4. **C4 (supporting claims):** the real-world generator is what makes learning work (Table 2, §6.3); one "unified framework" handles all problem types (§6.2).

### Paper memory (shared factual record, from the Phase-0 read)
- **Setup:** 100 cities, 80 train / 20 OOD-city test (Table 4; §6.1); 3×3 km window per city, 1000 sampled road points, full 1000×1000 OSRM distance and duration matrices per city (§4.2, Appendix A); instances of n = 100 nodes subsampled from the 1000 points (§4.3, Table 3); 100,000 instances per epoch, batch 256, Adam 4e-4, 200 epochs max, LR decay at 180/195 (§6.1, Table 3); 12 encoder layers, 128-d, 8 heads (Table 3); 4×A100 for under 24 h (§6.1); test on one A6000 with ×8 augmentation except supervised models (§6.1); 1,280 test instances (Table 3).
- **Not stated after search:** training seeds and number of runs; error bars; solver time limits/threads for LKH3, PyVRP and OR-Tools; what "cost" is for each task (distance or duration); the distributions of demands, capacities and time windows; how the "OOD (cluster)" instances are generated; the definition of the angle matrix; how durations enter the model; the "normalization strategy" for unreachable pairs; parameter counts or FLOPs of any model; dataset licence; a limitations section.
- **Headline numbers (Table 1, in-distribution gap to best-known):** ATSP RRNCO 1.797 vs MatNet 3.981; ACVRP RRNCO 3.450 vs MatNet 7.258 (OR-Tools 4.097); ACVRPTW RRNCO 3.928 (OR-Tools 1.377; no MatNet row). Table 2: MatNet trained on MatNet's ATSP generator 110.70, RRNCO with noise generator 7.72.
- **Appendix adds:** hyperparameters (Table 3), city table (Table 4), the statement that code is MIT-licensed and the dataset is on HuggingFace (links removed in the blinded copy).
- **Unverifiable:** Figures 1–4 (not available); Fig. 4's ablation values and the ">15%" statement.

### Integrity scan (EIC only)
`scripts/integrity_scan.py` found one soft-hyphen character (an extraction artifact) and **no text addressed to reviewers or AI systems**. The reviewer copy contains no redaction.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Adaeze Lindqvist-Roca, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty, repeated area chair / **Expertise**: learning-based optimization, benchmarks for ML-for-OR
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Calibrates against what the venue actually accepts; counts evidence, not heads

### Reviewer 1 (Methodology): Dr. Ines Thackeray-Moreau, industrial optimization lab (Western Europe)
- **Seniority / Expertise**: Mid-career industry scientist / RL for combinatorial optimization; evaluation protocols for neural solvers vs OR solvers
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched training data and matched time budgets against classical solvers

### Reviewer 2 (Domain): Prof. Dmitri Valeska-Okonkwo, operations research department, public university (Eastern Europe)
- **Seniority / Expertise**: Senior faculty / vehicle routing heuristics, asymmetric routing benchmarks, NCO literature
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks every novelty claim against what the abstract of the cited work actually says

### Reviewer 3 (Perspective): Dr. Priya Anantharam-Quill, urban mobility and transport analytics group (North America)
- **Seniority / Expertise**: Mid-career researcher / road-network data, travel-time estimation, logistics deployment
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive; asks what a dispatcher or planner would need

### Reviewer 4 (Generalist): Dr. Wen-Jie Torvaldsen, ML research lab, university in East Asia
- **Seniority / Expertise**: Postdoc / deep learning, generative sequence models; not a routing specialist
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: The typical program-committee member; weighs clarity and contribution against weaknesses

### Devil's Advocate: Dr. Oluwaseun Brandvold, evaluation-methodology group, industrial research lab (Africa/Europe)
- **Seniority / Expertise**: Senior scientist / causal evaluation, ablation design, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; looks for the confound behind the headline

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1 — Independent Reports

# Peer Review Report — Reviewer 1 (Methodology)

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Reviewer: Dr. Ines Thackeray-Moreau, Methodology Reviewer (industrial optimization lab, Western Europe; fictional persona)
## Expertise: RL for combinatorial optimization; evaluation of neural solvers against OR solvers
## Date: 2026-11-10

## Summary
The paper builds a generator of VRP instances from OSRM road distances and durations in 100 cities (§4), and an RL-trained encoder–decoder that fuses coordinate and distance-matrix embeddings with a learned gate and feeds a learned bias into an attention-free module (§5). On ATSP, ACVRP and ACVRPTW with n = 100 (Table 3), it reports gaps of about 2–4% to the best classical solution, versus 4–7% for MatNet and 9–46% for other neural solvers (Table 1), and shows that training on the generator matters (Table 2).

## Protocol sweep
Searched the full text and appendix for split, selection and tuning statements. Found: train/OOD city split in §6.1 and Table 4; "Val data size 1,280" and "Test data size 1,280" in Table 3; **no statement of selecting checkpoints, configurations or hyperparameters on the reported test instances**, and none of how hyperparameters were chosen. No test-set selection is evidenced.

## Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | open dataset bridging synthetic and real routing | Abstract, §1, §4 | §4.2, Appendix A; no validation that the data capture the claimed phenomena (asymmetry, traffic) | Partially |
| C2 | gating + NAB capture structure better | §1, §5 | Fig. 4 (unavailable); no AAFM-vs-attention or NAB-vs-heuristic-bias ablation; decoder also changed vs MatNet | Partially |
| C3 | SOTA among NCO | Abstract, §6.2 | Table 1, but baselines differ in training data; MatNet absent in ACVRPTW; single run | Partially (narrower claim supported) |
| C4a | generator is key | §6.3 | Table 2, one task, straw-man generator | Partially |
| C4b | single unified framework | §6.2 | §6.1 suggests per-task training | Unclear |

## Strengths
### S1: A reproducible, locally-hosted OSRM pipeline with fast online sampling
§4.2–4.3 describe a pipeline that builds 1000×1000 distance/duration matrices per city and subsamples instances online. This removes the commercial-API bottleneck the paper discusses in §2, and footnote 2 pins the OSRM version. Code and data are said to be public (Appendix, first paragraph).

### S2: Strong improvement over the closest edge-aware baseline at equal training data
Table 2 (row "MatNet / RRNCO data") and Table 1 give MatNet 3.981 → RRNCO 1.797 (ATSP, in-dist) and 7.258 → 3.450 (ACVRP). I recomputed RRNCO's ATSP gap from the printed costs (39.077 / 38.387 − 1 = 1.80%), and its ACVRP gap (72.145 / 69.739 − 1 = 3.45%): both match. The OOD-cluster gap difference (ACVRP 10.158 vs 3.224) is larger still.

### S3: The evaluation includes OOD-city and OOD-cluster tests against strong classical references
Table 1 reports three regimes and compares against LKH3, PyVRP and OR-Tools, which is more than a typical NCO paper.

### S4: Complete training hyperparameters
Table 3 and §6.1 give optimizer, schedule, batch size, depth, width, and compute (24 h on 4×A100).

## Weaknesses
### W1: Baselines are not trained on the same data, so Table 1 does not isolate "edge encoding" (MAJOR)
§6.1: "we do not retrain supervised-learning models", and node-only models (POMO, MTPOMO, MVMoE, RF, ELG) are evaluated without retraining because coordinates are normalized to [0,1]². Only RRNCO, MatNet and GCN are trained on the 80-city generator ("under the same settings for fair comparison for our model, MatNet for ATSP and ACVRP"). The 23–34% gaps of node-only models (Table 1, ACVRP) therefore mix two effects: lack of edge input and a mismatch between Euclidean-trained policies and an OSRM-cost reward. RL4CO (the paper's base framework, Appendix B) lets POMO/ELG/MVMoE train with a matrix-based reward on the same generator.
- **Suggested Fix**: Retrain at least POMO, ELG and MVMoE/RF with coordinates-only inputs but the OSRM cost on the 80 training cities (≈24 GPU-h each on the paper's setup), and fine-tune or clearly label GOAL/BQ-NCO/LEHD as zero-shot.

### W2: No variance or seeds anywhere (MAJOR)
No training seeds or repeated runs are stated (searched). RL training of NCO models is known to vary across seeds, and the ablation of §6.3 (Fig. 4, unavailable) reports no variance; the claim "NAB shows a relative improvement greater than 15%" (§6.3) cannot be checked without the figure (unverifiable).
- **Suggested Fix**: 3 training seeds for RRNCO and MatNet on ATSP and ACVRP, mean ± std, and a paired bootstrap over the 1,280 test instances. About 3 × 2 × 24 GPU-h for RRNCO alone.

### W3: Ablations do not isolate the claimed components (MAJOR)
RRNCO changes the encoder (gating, NAB, AAFM, 12 layers) and also the decoder, which "combines key elements from the ReLD [32] and MatNet [41]" with a −log(dist) logit heuristic (§5.2, Eq. 15). The MatNet baseline has neither. Fig. 4 ablates the initial context (coordinates / distance / CG) and NAB inside RRNCO only (caption). Missing: AAFM vs standard multi-head attention with the same bias; NAB vs the original heuristic bias −α·log N·d_ij (§5.1.2); RRNCO decoder on MatNet's encoder; effect of k = 25 neighbours (Eq. 4, Table 3); effect of removing the −log(dist) term.
- **Suggested Fix**: A 2×2 (encoder × decoder) grid plus the three single-component swaps above on ATSP/ACVRP.

### W4: "In-distribution" test instances are not independent of training instances (MAJOR)
Each city contributes one pool of 1000 points (Appendix A) and instances are 100-node subsamples of it (§4.3); in-distribution test instances are "new instances generated from the 80 cities seen during training" (§6.1). Training therefore sees every pairwise entry of the same 80 matrices. This supports the "effectively unlimited number of instances" wording only combinatorially, not geometrically, and it inflates the in-distribution columns of Table 1/2.
- **Suggested Fix**: Hold out 100–200 of each training city's 1000 points for test (no matrix entries shared), or report only OOD-city numbers as the main result.

### W5: Missing time-matched comparison with classical solvers (MAJOR)
Table 1 lists 1.6 h (LKH3) and 7 h (PyVRP/OR-Tools) against 22–35 s for RRNCO, but not the number of instances per timing, threads, or solver time limits (searched: not stated). On ACVRPTW OR-Tools reaches 1.377% vs RRNCO's 3.928% and on ACVRP-cluster 1.655% vs 3.224%, so the claim is about speed, which is untested at matched budgets. Both PyVRP and OR-Tools are anytime solvers.
- **Suggested Fix**: Report per-instance wall-clock, hardware and threads, and a quality-vs-time curve for PyVRP/OR-Tools at 1, 5, 20 s per instance.

### W6: Problem definitions needed to reproduce the benchmark are missing (MAJOR)
Not stated after search: the cost objective per task (distance or duration; costs differ by 70% between ACVRP 69.739 and ACVRPTW 118.056, Table 1); demand and capacity distributions; time-window generation and feasibility (§4.3 item 3 only defines W as an N×2 matrix); how OOD-cluster instances are made (§6.1); the "normalization strategy that addresses both unreachable destinations and abnormal travel times" (§4.2); how durations (as opposed to distances) enter the model (Eqs. 4–10 use only a distance matrix); the angle matrix of NAB (§5.1.2: "an angle matrix representing the angular relationships between nodes", no formula).
- **Suggested Fix**: Add a task-definition appendix with generators and equations for each; define the angle matrix and the use of the duration matrix.

### W7: Instance size and scope limit the "real-world" evidence (MINOR–MAJOR)
Only n = 100 (Table 3), 3×3 km downtown windows (§4.2), no larger sizes although the introduction motivates "large-scale and real-time applications" (§1), no external real benchmark such as the instances of [43] or [60] cited in §2.
- **Suggested Fix**: n = 200/500 generalization test and one external real-world benchmark.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E5 | §6.2 vs Table 1 | "consistently outperforming existing neural solvers in both solution quality and computational efficiency" | RRNCO is slower than POMO in every task: ATSP 22 s vs 10 s; ACVRP 25 s vs 16 s; ACVRPTW 35 s vs 18 s (also slower than LEHD 13 s on ATSP) | Cross-referenced Table 1 time columns | High | MINOR | Say "better quality at moderate extra time" |
| ERR-2 | E6 | §4.1 vs Table 4 | "20 small cities <100K" | Counting the "Population" column of Table 4 gives 9 Small, 19 Medium, 72 Large, not 20/30/50 | Counted rows of Table 4 (derived) | Medium (labels could use a different threshold) | MINOR | Reconcile text and table |
| ERR-3 | E4 | Table 1, ACVRPTW block vs ACVRP block | (table structure) | ACVRP block contains GCN, MatNet, ELG, BQ-NCO, LEHD; ACVRPTW block has none of them; MatNet (the closest edge-aware baseline) is absent where RRNCO's gain is claimed | Cross-referenced two table blocks | High | MAJOR | Add MatNet (and GCN) to ACVRPTW |
| ERR-4 | E5 | §6.2 | "our method effectively handles all routing problems within a single unified framework" | §6.1 trains per task ("for our model, MatNet for ATSP and ACVRP"); no single multi-task model is reported, while MTPOMO/MVMoE/RF/GOAL in the same table are multi-task. Ambiguous rather than contradicted | Cross-referenced §6.1/§6.2/Table 1 | Medium | MINOR–MAJOR (wording) | Clarify: one architecture, separate models; or train one model |

## Missing References
*(The Domain Reviewer owns this; none added by R1.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains over MatNet are real, but baselines, ablations and variance leave the attribution open |
| Clarity | 2 | Problem and generator definitions missing (W6) |
| Significance | 2 | Useful resource and direction; limited to n = 100, static OSRM |
| Originality | 2 | Recombination of MatNet/AAFM/ReLD ideas |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison rests on baselines trained differently from the proposed model (W1), the ablation does not isolate the claimed components (W3), and there is no variance; the useful resource and the MatNet gap keep it from the bottom of the pool.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound pipeline and training, but confounded attribution (W3), non-independent in-dist test (W4) |
| Clarity & Presentation | 56 | Competent | Readable; undefined objects (W6) |
| Novelty & Originality | 52 | Developing | Mostly recombination |
| Significance & Impact | 58 | Competent | Real need; scope narrow |
| Experimental Validation | 44 | Developing | W1, W2, W3, W5, ERR-3 |
| Reproducibility | 60 | Competent | Code/data promised, hyperparameters complete; task definitions missing |
| Ethical Compliance | 64 | Competent | No human data; no limitations section |

## Questions for Authors
1. Are node-only baselines' failures due to missing edge input or to Euclidean-trained policies? A POMO/ELG retrained with OSRM-cost reward would settle it; a gap below ~10% would lower my concern, a gap still above 20% would raise my score.
2. Is one RRNCO model trained for all three tasks, or three models (§6.1 vs §6.2)?
3. Eq. 4 sums over j = 1..N including j = i (d_ii = 0): how is self-distance handled, and is the neighbour sampling stochastic at test time?
4. What is the time limit and thread count behind the 1.6 h / 7 h entries, and for how many instances?
5. What are the ablation values in Fig. 4 and their seed variance?

## Limitations Assessment
**Partially.** Footnote 3 (§4.2) defers real-time traffic ("which we leave as future works"), but there is no limitations section covering n = 100, 3 km windows, static durations, or single runs.

## Ethics Review Flag
**No.**

## Overall Score
**3**: A useful pipeline and a real gain over MatNet, but the central comparison is not controlled enough to support the SOTA claim as worded.

## Confidence
**4**: Read all sections and the appendix; the figures were unavailable.

---

# Peer Review Report — Reviewer 2 (Domain)

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Reviewer: Prof. Dmitri Valeska-Okonkwo, Domain Reviewer (operations research department, public university, Eastern Europe; fictional persona)
## Expertise: vehicle routing heuristics; asymmetric routing benchmarks; NCO literature
## Date: 2026-11-10

## Summary
The paper argues that NCO for VRPs has been evaluated almost exclusively on Euclidean synthetic instances and offers (i) an OSRM-based instance generator for 100 cities and (ii) an encoder that processes matrix inputs. Its closest relatives are MatNet (matrix encoding for ATSP-type problems, [41]), the instance-conditioned attention-free module of [88], the ReLD decoder [32], and earlier real-road-network generators and benchmarks [1, 21, 43, 60].

## Strengths
### S1: A real gap is addressed
Training and benchmarking NCO on road-network distances rather than Euclidean ones matters for practice (§1, §3.1), and the paper compares to classical solvers (§6.1), which OR readers expect.
### S2: Honest differentiation from earlier real-data generators
§2 states concretely what [1] and [21] lack (commercial APIs, no durations, 20+ s per instance for n > 300, no released code); an open local-OSRM generator is a clear practical advance over those.
### S3: Sensible choice of model family to build on
Building on MatNet's row/column dual embeddings (§5.1.1, citing [41]) and a heuristic-bias attention-free module [88] is a reasonable fit for asymmetric matrices, and the paper credits sources (§5.1.2, §5.2).
### S4: Breadth of NCO baselines
Eleven learned baselines from several paradigms (§6.1).

## Weaknesses
### W1: Method novelty is incremental and its delta to the nearest ancestors is not tested (MAJOR)
The encoder is MatNet-style dual embeddings (Eqs. 9–10) feeding an AAFM whose bias was heuristic in [88] and is learned here (§5.1.2); the decoder is "ReLD + MatNet" (§5.2); gated fusion (Eq. 7 and the gate G in §5.1.2) is a standard mechanism. The paper itself says its contribution is replacing "−α·log N·d_ij" by a learned bias. Neither [88]'s heuristic-bias AAFM nor ReLD [32] appears as a baseline or ablation, so the specific novelty is unmeasured.
- **Suggested Fix**: Add ICAM-style heuristic-bias AAFM and ReLD (with matrix inputs) as rows, or ablations.

### W2: "Real-world" is narrower than the framing (MAJOR)
Instances come from 3×3 km windows around municipal centres (§4.2), n = 100 uniformly subsampled points (§4.3, Table 3), with synthetic demands and time windows. Asymmetry is attributed to "traffic patterns and road network constraints" (§3.1), yet no traffic data enter (footnote 3: "which we leave as future works"), so durations are static functions of the road graph. The paper never quantifies how asymmetric or non-metric its matrices are (e.g., |d_ij − d_ji|/d_ij, triangle-inequality violations, correlation between D and T).
- **Suggested Fix**: A dataset-statistics table per city (asymmetry, circuity vs Euclid, D–T correlation) and a toned-down framing ("road-network" rather than "real-world").

### W3: Related-work claims about prior edge-aware NCO are unsupported (MINOR–MAJOR)
§2 says existing approaches [18, 20, 21, 41, 44] have "inefficient learning of neural representations", without evidence; GOAL [18] and MatNet [41] are baselines whose relative standing is explained only by the authors' own runs (Table 1). Claims about what [1] and [21] omit should be stated against those papers' abstracts, which I could not verify from the manuscript alone.
- **Suggested Fix**: Remove or substantiate the assertion; add a feature table comparing [1], [21], [43], [60] and the new data.

### W4: Citation accuracy (MINOR)
§6.1 cites OR-Tools as [61], which is the CP-SAT entry ("Perron and Didier 2024. CP-SAT"), whereas the OR-Tools entry is [62]. §4.2 footnote 3 cites [63] ("Revisiting the correlation between simulated and field-observed conflicts…", Accident Analysis & Prevention) for "powerful traffic forecasting to obtain better-informed routing"; the title does not suggest a routing or forecasting source. Several entries are duplicated ([19]/[20], [51]/[52], [71]/[72], [81]/[82]). Haversine is sourced to a 2013 low-tier journal note [17].
- **Suggested Fix**: Correct citations and deduplicate.

### Missing References
*(Filled in the Phase 1.5 literature-check addendum below: verified entries only.)*

### Citation check (E7)
| ID | Cat. | Location | Quote | Why | Verified | Conf. | Sev. |
|----|------|----------|-------|-----|----------|-------|------|
| ERR-5 | E7 | §6.1 vs ref. list | "Google OR-Tools[61]" | [61] is "CP-SAT"; the OR-Tools entry is [62] | Cross-referenced text and bibliography | Medium | MINOR |
| ERR-6 | E7 | §4.2 footnote 3 vs [63] | "powerful traffic forecasting to obtain better-informed routing" | [63]'s title concerns simulated vs observed conflicts | Cross-referenced title | Medium (title only) | MINOR |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See R1; gains plausible but not attributed |
| Clarity | 3 | Positioning is clear |
| Significance | 2 | Narrow-scale proof of concept for a practical gap |
| Originality | 2 | Recombination; resource is the more novel part |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the resource fills a practical gap, but the method's novelty against AAFM/MatNet/ReLD is incremental and untested, and the "real-world" label outruns the data.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Standard, correctly applied pipeline |
| Clarity & Presentation | 58 | Competent | Positioning clear |
| Novelty & Originality | 52 | Developing | Incremental method, modest resource novelty |
| Significance & Impact | 60 | Competent | Useful sub-area contribution |
| Experimental Validation | 50 | Developing | Missing closest-ancestor baselines |
| Reproducibility | 64 | Competent | Code and data public |
| Ethical Compliance | 64 | Competent | Licence of derived data unstated |

## Questions for Authors
1. What does learned NAB add over [88]'s heuristic bias on the same data? (Raises my Novelty score if the gap is large.)
2. How asymmetric are the matrices? Report per-city statistics.
3. Which OSRM profile (car/bike) and which speed model produce durations?

## Limitations Assessment
**Partially.** Future work on traffic is mentioned in a footnote; the scope limits are not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**3**: A worthwhile resource attached to an incremental method with untested novelty claims.

## Confidence
**4**: Strong familiarity with routing; the literature check supplements, but does not replace, my reading.

---

# Peer Review Report — Reviewer 3 (Perspective)

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Reviewer: Dr. Priya Anantharam-Quill, Perspective Reviewer (urban mobility and transport analytics group, North America; fictional persona)
## Expertise: road-network data; travel-time estimation; logistics deployment
## Date: 2026-11-10

## Summary
The paper brings road-network travel distances and times into neural routing, so a learned solver can be trained and tested on instances closer to a dispatcher's actual cost matrices. It offers an open generator and an attention-free encoder that exploits edge matrices, and reports sub-5% gaps to strong classical solvers at seconds-level inference.

## Strengths
### S1: Practical orientation toward what planners actually have
Dispatch systems work from origin–destination matrices from routing engines; building the model around such matrices (§3.1, §5.1.1) is the right interface, and the OSRM table service (footnote 2, §4.2) is what many planners already use.
### S2: Geographic diversity as a design goal
Six continents, varied layouts and sizes (§4.1, Table 4) is rare in NCO benchmarks and enables OOD-city testing (Table 1).
### S3: Open and cheap to regenerate
Local OSRM hosting and ~1.5 GB of base maps (§4.3) lower the barrier for others to generate their own cities.
### S4: Seconds-scale inference
25–35 s for 1,280 instances (Table 1) suggests interactive re-planning potential, to be validated at larger n.

## Weaknesses
### W1: Static, uniform-sampled instances may not transfer to actual last-mile problems (MAJOR, framed as opportunity)
Customers are uniform samples of road points in a 3×3 km box (§4.2), n = 100 (Table 3), with synthetic demands/time windows (§4.3). Real delivery demand is clustered by land use and time-dependent travel times (rush hours) change the matrices. The paper frames travel-time asymmetry as a traffic effect (§3.1), though traffic is explicitly deferred (§4.2 footnote 3).
- **Suggested Fix**: Add land-use-weighted customer sampling and a time-of-day variant (e.g., speed profiles) to the generator, and report whether the ranking of methods is stable; link to time-dependent VRP literature from OR.

### W2: Data provenance, quality and licence are not discussed (MAJOR for a dataset contribution)
OpenStreetMap data were accessed "2025-02-06" ([59]); OSM completeness and tagging quality vary strongly across regions, and the paper claims to benefit "underprivileged areas" (§4.1), so data quality in Lagos/Dhaka/Kinshasa-type windows (Table 4) matters. Code is MIT-licensed (Appendix) but the dataset licence is not stated; OSM-derived databases carry attribution and share-alike conditions.
- **Suggested Fix**: A datasheet: licence and attribution, OSM snapshot date, per-city coverage statistics (road length, node count, share of unreachable pairs), and a note on where results may not transfer.

### W3: Cost definition and business objective unstated (MINOR–MAJOR)
Whether solutions minimize distance or duration is not stated for each task (Table 1 costs). Planners care about duration, distance, and hard time-window feasibility differently.
- **Suggested Fix**: State the objective per task and report both.

### W4: Broader-impact claims are rhetorical (MINOR)
§1: "improvements in routing efficiency can yield substantial cost savings and environmental benefits", with a market-size figure from a forecast (ref. [66] says 9.41 trillion in 2023 and an implied 10.5 trillion for 2025) presented as fact in "exceeding the 10 trillion USD mark in 2025".
- **Suggested Fix**: Rephrase as a forecast, and quantify any claimed benefit or drop it.

## Cross-disciplinary connections
- **Transportation / OR:** time-dependent and stochastic VRP; matrix-based local search (e.g., 2-opt/Or-opt, HGS-style neighbourhoods) as a polish step on top of NCO output; routing-engine-based travel-time variability.
- **Graph learning:** edge-conditioned message passing and graph transformers with edge/relative-position bias are the closest relatives of NAB; a comparison with a generic "relative-position bias" attention would show whether the angle input matters.
- **Urban science:** circuity factors and network-detour ratios are standard statistics that would characterize the instances (W2 of R2).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Same attribution issues |
| Clarity | 3 | Mostly clear |
| Significance | 3 | Valuable direction and resource |
| Originality | 2 | Incremental method |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a useful, open resource on a problem practitioners care about; held back by narrow instance realism and missing data documentation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound pipeline |
| Clarity & Presentation | 62 | Competent | Clear motivation |
| Novelty & Originality | 60 | Competent | Resource fills a gap |
| Significance & Impact | 70 | Competent | Practical direction |
| Experimental Validation | 55 | Competent | Limited n, no real external benchmark |
| Reproducibility | 68 | Competent | Code/data public |
| Ethical Compliance | 58 | Competent | Licence/data quality/limitations undiscussed |

## Questions for Authors
1. Does the ranking RRNCO > MatNet hold when customers are clustered and speeds are time-dependent? (A yes would raise my Significance score.)
2. What licence covers the released matrices?
3. How many of the 1000 points per city lie on the largest strongly connected component, and how are unreachable pairs handled?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.** Licence and data-quality documentation are requested, but no ethics-review trigger.

## Overall Score
**4**: The resource and direction outweigh the scope limits for an exploratory-but-useful ICLR paper.

## Confidence
**3**: Outside my core NCO expertise; the method details are reviewed lightly.

---

# Peer Review Report — Reviewer 4 (Generalist)

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Reviewer: Dr. Wen-Jie Torvaldsen, Generalist Reviewer (ML lab, university in East Asia; fictional persona)
## Expertise: deep learning, sequence models; not a routing specialist
## Date: 2026-11-10

## Summary
The paper proposes a dataset/generator of road-network VRP instances and an RL-trained solver using a gated fusion of coordinate and distance embeddings plus a learned attention bias. It reports that the solver closes most of the gap to classical solvers on asymmetric TSP/CVRP/CVRPTW at n = 100 and beats other neural solvers.

## Contribution in one paragraph
A practical benchmark plus a matrix-aware solver that improves on MatNet by roughly 2–4 gap points in-distribution and 3–7 on OOD clusters. Readers who need NCO that works with routing-engine matrices benefit; the research insight (what in the architecture matters) is thin.

## Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly (single run, confounded baselines) | Table 1, Fig. 4 |
| Presentation: clear and self-contained | Partly (undefined angle matrix, cost, generators) | §5.1.2, §4.3 |
| Contribution: significant to the community | Partly (useful resource; incremental method) | §1, §4 |
| Reproducibility: code and data | Met (promised, public) | Appendix |
| Relevance to ICLR audience | Met (NCO is a recurring topic) | — |

## Strengths
### S1: Clear motivation and an easy-to-follow problem statement (§1, Fig. 1, §3).
### S2: Strong numeric results against many baselines, with OOD tests (Table 1) and a data-generator study (Table 2).
### S3: Open code and data and a complete hyperparameter table (Appendix, Table 3).
### S4: Honest component ablation of context types (Fig. 4 caption) and a statement of the scope (autoregressive constructive models, §2).

## Weaknesses
### W1: Key technical objects are undefined (MAJOR for clarity)
The angle matrix that feeds NAB, a headline element of the abstract, has no formula (§5.1.2); the objective/cost per task, demand and time-window generation, and the OOD-cluster construction are missing (§4.3, §6.1); how duration (as opposed to distance) enters the model is unclear (Eqs. 4–10). A reader cannot reimplement §5 and §6 from the paper alone.
- **Suggested Fix**: Add formulas and a task-definition appendix.

### W2: Claims in §6.2 are worded more strongly than Table 1 supports (MAJOR for presentation honesty)
"consistently outperforming existing neural solvers in both solution quality and computational efficiency": RRNCO is slower than POMO in all three tasks (Table 1). "a single unified framework" is not shown by a single trained model (§6.1). "state-of-the-art" holds among the listed baselines, not under matched training.
- **Suggested Fix**: Narrow the wording to what is shown.

### W3: Ablation evidence is thin and its presentation hard to judge (MAJOR)
The main architectural claims rest on Fig. 4, which (judged from the caption and text only; the figure was unavailable) has no numeric table or error bars; §6.3 gives a single sentence of analysis, plus "relative improvement greater than 15%" with no number to check. A table with values per variant and task is needed, and an architecture-level ablation of AAFM vs standard attention.
- **Suggested Fix**: Tabulate Fig. 4 with seeds; add AAFM-vs-MHA.

### W4: Inconsistent figures in the dataset description (MINOR)
§4.1 states 50/30/20 large/medium/small cities, Table 4 labels about 72/19/9; §6.2 says Table 1 has "inference times indicated in parentheses" while they are a separate Time column; the reference list contains duplicates ([19]/[20], [51]/[52], [71]/[72], [81]/[82]).

**Minor:** typographic issues in the text extraction ("Adaption Attention-Free Module" vs "Adaptation Attention Free Module"; "Attention Attention Free Module" in §5.1.2).

## Questions for Authors
1. Could you provide Fig. 4's numbers per variant and seed? (Would move my Soundness up if the NAB gain is consistent.)
2. What exactly is the angle matrix?
3. Is there a single multi-task RRNCO model?

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains plausible, evidence thin |
| Clarity | 2 | Definitions missing |
| Significance | 3 | Useful resource |
| Originality | 2 | Recombination |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: solid practical motivation and results, but a typical ICLR reviewer would see an incremental architecture with an under-controlled comparison and under-specified method details.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Pipeline standard; gaps in controls |
| Clarity & Presentation | 54 | Developing | W1, W4 |
| Novelty & Originality | 55 | Competent | Resource plus recombined method |
| Significance & Impact | 62 | Competent | Narrow but real |
| Experimental Validation | 52 | Developing | Thin ablation, single run |
| Reproducibility | 62 | Competent | Public code/data |
| Ethical Compliance | 60 | Competent | No human data; no limitations section |

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3**: Reasons to reject slightly outweigh reasons to accept: a useful artifact, but the central comparison and details are not yet at the bar.

## Confidence
**3**: Not a routing specialist.

---

# Devil's Advocate Report

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Reviewer: Dr. Oluwaseun Brandvold, evaluation-methodology group, industrial research lab (fictional persona)

## Steelman
There is a real gap: neural routing solvers are almost always evaluated on Euclidean instances. The paper provides an open generator of road-network instances and shows that an encoder taking the matrices directly beats other neural solvers, including the matrix-aware MatNet, by large relative margins at seconds-level inference, with similar results out of distribution.

## Core Argument Chain
1. Existing NCO is evaluated on synthetic Euclidean instances (§1).
2. Real instances are asymmetric and edge-rich; node-only models cannot use that (§1, §3.1).
3. The new OSRM-based generator provides such instances (§4).
4. RRNCO's gating + NAB + AAFM encoder uses edge information better (§5; Fig. 4).
5. On Table 1 it beats all neural baselines, including edge-aware ones, in-distribution and OOD.
∴ RRNCO "achieves state-of-the-art results in real-world VRPs among NCO methods" and bridges the sim-to-real gap.

## Strongest Counter-Argument
The headline result does not isolate the thing the paper says it demonstrates. P5 compares RRNCO against baselines that are either not trained on the real-world generator at all (the five node-only models, plus GOAL, BQ-NCO, LEHD; §6.1) or trained as MatNet/GCN with a different architecture, decoder and, apparently, depth (Table 3 gives RRNCO 12 layers; no baseline sizes). The 23–46% gaps of the node-only models therefore measure a train/test cost mismatch more than "lack of edge encoding," and the 2–4 point margin over MatNet is confounded with a different decoder (ReLD-style residual MLP and the −log(dist) logit heuristic; §5.2, Eq. 15), a different encoder block (AAFM), and the gating. The ablation in Fig. 4 only varies components inside RRNCO. Whether the learned NAB, the angle input or the gating contributes at all, as opposed to the decoder and depth, is unknown. On top of that, "real-world" means 3×3 km downtown windows of static OSRM matrices (§4.2), n = 100 (Table 3), synthetic demands and time windows, one training run, and in-distribution tests built from the same 1000-point pools as training (Appendix A, §6.1). The conclusion that RRNCO "bridges the gap" is therefore supported only in the weaker form "a larger, deeper matrix-aware solver trained on OSRM-derived instances beats MatNet and untrained-for-this-data baselines at n = 100".

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The paper's evidence supports a narrower version of its main claim (the fix is to narrow the claim and add controls), and no test-set selection is stated.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence/Scope | §6.1, Table 1 | Baselines are trained differently from RRNCO ("we do not retrain supervised-learning models"; node-only models not retrained), so the SOTA claim is not a controlled comparison; MatNet absent from ACVRPTW | Retrain node-only RL baselines on the generator; add MatNet/GCN to ACVRPTW |
| DA-M2 | Logic (confound) | §5.2, Eq. 15, Table 3, Fig. 4 | Gains cannot be attributed to gating/NAB: decoder, depth and encoder block all differ from MatNet; the ablation is internal only | Encoder×decoder grid; AAFM vs MHA; heuristic-bias vs NAB; parameter-matched MatNet |
| DA-M3 | Scope | §4.2, §3.1, footnote 3 | "Real-world" asymmetry is described as traffic-driven, but only static OSRM matrices in 9 km² windows are used; no asymmetry statistics | Dataset statistics; reframe as road-network |
| DA-M4 | Evidence | Appendix A, §6.1, §4.3 | In-distribution test shares the 1000-point pools of training; "effectively unlimited" instances are subsamples of 100-node instances from 1000-point pools | Hold out points; emphasize OOD |
| DA-M5 | Statistics | §6.1, Fig. 4 | Single run, no seeds, no variance for the ablation | 3 seeds, paired bootstrap |
| DA-M6 | Overclaim (E5) | Abstract, §6.2 | "state-of-the-art", "consistently … computational efficiency", "single unified framework" go beyond Table 1 | Narrow wording |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of claims | §1, ref. [66] | The 2025 market size is a forecast presented as fact |
| DA-m2 | Citations | §6.1 [61], §4.2 fn 3 [63] | OR-Tools cited as CP-SAT entry; [63] looks unrelated to traffic forecasting |
| DA-m3 | Consistency | §4.1 vs Table 4 | Population counts differ |
| DA-m4 | Clarity | §6.2 vs Table 1 | "inference times indicated in parentheses" but Table 1 has a separate Time column |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| RRNCO ATSP in-dist gap | 1.797 | 39.077/38.387 − 1 = 1.80% | Yes |
| MatNet ACVRP in-dist gap | 7.258 | 74.801/69.739 − 1 = 7.26% | Yes |
| OR-Tools ACVRPTW gap | 1.377 | 119.681/118.056 − 1 = 1.38% | Yes |
| RRNCO ACVRPTW cluster gap | 4.647 | 41.077/39.253 − 1 = 4.65% | Yes |
| POMO ATSP cluster gap | 146.926 | 30.051/12.170 − 1 = 146.9% | Yes |
| Cities by continent | 100 | 25+21+15+15+14+10 = 100 | Yes |
| City sizes in §4.1 | 50/30/20 | Table 4 labels 72/19/9 (my count) | No |
| "NAB … greater than 15%" | >15% | Fig. 4 unavailable | Unverifiable |
| Efficiency claim | "consistently … computational efficiency" | RRNCO slower than POMO in all three tasks | No |

## Ignored Alternative Explanations
1. Decoder, depth or parameter count drive the margin over MatNet (not NAB or gating).
2. Node-only failures stem from an Euclidean-trained policy facing an OSRM-cost objective rather than from the lack of edge features.
3. If OSRM durations are near-proportional to distances, the duration matrix adds little beyond distance and the "distance vs duration" distinction is not tested.
4. In-distribution results are inflated by shared point pools.

## Missing Stakeholder Perspectives
Dispatchers who need time-dependent travel times; practitioners in regions where OSM coverage is incomplete; carriers with n ≫ 100.

## Observations (Non-Defects)
- All printed gaps I recomputed are consistent with the printed costs.
- The unusually complete hyperparameter table and the release of code and data are strong practice.
- No test-set selection is stated.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Confounded attribution; independent-test issue |
| Clarity & Presentation | 55 | Undefined objects; overstated wording |
| Novelty & Originality | 48 | Recombination; untested novelty |
| Significance & Impact | 56 | Narrow scope |
| Experimental Validation | 42 | Baseline training mismatch; single run |
| Reproducibility | 58 | Code public; definitions missing |
| Ethical Compliance | 58 | Licence/limitations missing |

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison is not controlled (DA-M1, DA-M2).

## Overall: 3 | Confidence: 4

---

# Phase 1.5 — Literature Check (Domain Reviewer addendum to Report R2)

**Run:** `scripts/related_search.py`, mode **strict** (everything after the cutoff 2025-09-24 dropped), cutoff 2025-09-24. Six queries of the 12 allowed: 3 claim (C1, C2, C3), 1 baseline (ATSP neural solvers), 2 expansion. `benchmarks` found no external benchmark (the paper's instances are its own), so `scout` was not applicable. `coverage` reported no gaps by count, but several queries returned mostly off-topic traffic/ML results (C1 and the travel-time expansion); for those claims "no close prior work found in this search (arXiv only)" is a limit of the search, not evidence of novelty. Reference verification: `verify` for Arnold et al. found nothing (kept `[verify]`); the other recommended entries come straight from kept search results with links. 33 candidates were scored by `similarity`; none reached the high-overlap threshold (cosine ≥ 0.30; maximum 0.184). The only "text overlap" flag (MVMoE, 2 shared 8-grams) is the title of the MVMoE entry in the paper's own reference list [89], i.e., a cited title, **not an integrity concern**.

## Per-claim novelty (claim-level profile; `related_search.py novelty`)

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 open real-world VRP dataset/generator | resource | **medium** (script: high; capped because the search covers arXiv only and returned no close prior) | Instance generation tool for on-demand transportation problems (L2; https://arxiv.org/abs/2208.12225v1; prior arXiv-only; not cited). Worth discussing: SVRPBench (https://arxiv.org/abs/2505.21887v2; recent preprint) | No close prior work found in 22 results. Paper itself differentiates [1], [21], [43], [60] in §2. |
| C2 gated fusion + learned bias in attention-free module | method | **medium** | GREAT, edge attention for asymmetric-cost routing (L3; https://arxiv.org/abs/2408.16717v4; prior arXiv-only; not cited); GASE (L3; https://arxiv.org/abs/2405.12475v1); ICAM (L3; https://arxiv.org/abs/2405.01906v3; prior peer-reviewed; cited as [88]). Worth discussing: EFormer (https://arxiv.org/abs/2506.16428v1; recent preprint) | Edge/matrix-aware neural routing and learned or heuristic biases in attention exist; the specific combination is new but incremental. |
| C3 SOTA among NCO on road-network ATSP/ACVRP/ACVRPTW | result | **medium** (script: high; new benchmark, so no prior numbers exist) | Routing Arena (L2; https://arxiv.org/abs/2310.04140v1; cited as [71], [72]) | No prior result for the same setting; a result claim on a new benchmark is inherently uncontested. |

Paper reading from the script: "no central claim fully covered by prior work". No claim is "known"; there is no criterion-7 candidate. Closest prior work as a whole (script attribution): **GREAT** (edge-attention network for asymmetric, road-topology-derived costs; not cited).

## Novelty delta table

| Claimed contribution | Closest prior work (link) | What it already does | What is new here | Cited? |
|----------------------|---------------------------|----------------------|------------------|--------|
| C2 | GREAT, https://arxiv.org/abs/2408.16717v4 | Edge-attention encoder for asymmetric, non-Euclidean edge costs in an electric-vehicle routing problem (per its abstract) | Attention-free module with learned bias and coordinate/matrix gating; different problems (ATSP, ACVRP, ACVRPTW) | No |
| C2 | GASE, https://arxiv.org/abs/2405.12475v1 | Fuses edge information into graph-attention encoders for VRPs (per abstract) | Different fusion, learned bias | No |
| C2 | ICAM, https://arxiv.org/abs/2405.01906v3 | Source of the attention-free adaptation module with distance-based bias | Learned bias replaces the heuristic; matrix inputs | Yes [88] |
| C1 | Instance generation tool for on-demand transportation, https://arxiv.org/abs/2208.12225v1 | Generator of realistic instances for transportation problems (per abstract) | OSRM-based matrices for NCO training with online sampling | No |

## Baseline scout
Not applicable: no external benchmark (`benchmarks` returned none); the paper's data is its own.

## Field snapshot (kept results, as of the cutoff)
Around 2019–2021 the dominant approach was coordinate-only attention models trained with RL on Euclidean uniform instances; MatNet (2021) was the main matrix-aware exception. By 2024–2025 the field emphasised generalisation and multi-task solvers (MVMoE at ICML 2024, architecture-level generalisation methods such as ICAM and the entropy-scaling/distribution-specific decoder work), benchmarking suites (Routing Arena), and a small but growing line of edge- or matrix-based models for non-Euclidean, asymmetric costs (GREAT, GASE; EFormer in mid-2025) together with realistic benchmarks (SVRPBench, mid-2025). Open problems stated by recent work: non-Euclidean and asymmetric costs, time-dependent or stochastic travel, and scaling beyond a few hundred nodes. A paper in this sub-field is significant when it either delivers a clear gain over matrix-aware baselines at matched model size on benchmarks others can adopt, or opens a capability (realistic travel times, large n) that coordinate-only models cannot handle. A 2-point gap improvement over MatNet at n = 100 is moderate rather than decisive; the benchmark's adoption potential is the larger source of value. This snapshot calibrated Novelty (52) and Significance (60).

## Missing References (verified entries first; citation-integrity rule applied)

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important (prior, arXiv-only) | Lischka, Rydin, Wu, Chehreghani, Kulcsár. "GREAT: A Graph Edge Attention Network for the Electric Vehicle Routing Problem with Asymmetric Costs", arXiv 2024 (https://arxiv.org/abs/2408.16717v4) | Learns from asymmetric, road-topology edge costs; closest prior work as a whole |
| Important (prior, arXiv-only) | Wang, Bai, Khan, Ozcan, Zhang. "GASE: Graph Attention Sampling with Edges Fusion for Solving Vehicle Routing Problems", arXiv 2024 (https://arxiv.org/abs/2405.12475v1) | Edge-fusion encoder for VRPs |
| Important (peer-reviewed prior) | Xiao, Wang, Wu, Wu, Li, Du. "Improving Generalization of Neural Vehicle Routing Problem Solvers Through the Lens of Model Architecture", Neural Networks (https://arxiv.org/abs/2406.06652v3) | Architecture-level generalisation methods relevant to the OOD claims |
| Helpful (worth discussing; recent preprints, never a weakness) | Meng, Cao, Wu, Hou, Ge, Zhang. "EFormer: An Effective Edge-based Transformer for Vehicle Routing Problems", arXiv 2025 (https://arxiv.org/abs/2506.16428v1); Heakl et al. "SVRPBench", arXiv 2025 (https://arxiv.org/abs/2505.21887v2) | Edge-only inputs for VRPs; realistic stochastic benchmark |
| Helpful `[verify]` | Arnold, Gendreau, Sörensen. "Efficiently solving very large-scale routing problems", Computers & Operations Research, 2019 | Large realistic routing instances from road data; not found on arXiv by title, kept as `[verify]` |

No recommendation of a recent preprint, concurrent or newer work lowers any score.

---

# Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W2 (originally an inference from extracted axis ticks about Fig. 4) | rewritten | The inference was not verifiable without the figure; the ablation margins are treated as "unverifiable" and only the verified no-variance point is kept |
| R1 | ERR-4 ("unified framework") | rewritten | §6.1 does not say a single model is not used; it is ambiguous. Kept as an ambiguity (clarity/overclaim), not a contradiction |
| R1 | W7 (n = 100, scope) | kept, merged with R2-W2, R3-W1, DA-M3 | Duplicate theme (realism and scale) |
| R2 | W3 ("inefficient learning" assertion) | kept | Quote verified in §2 |
| R2 | W4 (citations) | moved to Minor | Cosmetic; ERR-5 verified, ERR-6 rests on the title only |
| R3 | W3 (cost definition) | merged into R1-W6 | Same omission |
| R3 | W4 (forecast presented as fact) | moved to Minor | Cosmetic wording; verified against ref. [66] |
| R4 | W3 (originally a Fig. 4 axis-range inference) | rewritten | Same reason as R1-W2 |
| R4 | W4 | moved to Minor | Cosmetic |
| DA | DA-M5 (single run + in-dist overlap) | kept, split into variance (DA-M5) and in-distribution independence (DA-M4) | Two different problems |
| all | none dropped as already answered | — | The appendix does not state seeds, task generators, time-window generation, OOD-cluster construction or the dataset licence |

Scores were not changed.

---

# Phase 2 — EIC Meta-Review and Decision

# Editorial Decision

## Paper: RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization
## Submission ID: iclr26-sKvo9ZZfpe
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: Empirical (with a resource component)
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Adaeze Lindqvist-Roca; R1 Methodology Dr. Ines Thackeray-Moreau, R2 Domain Prof. Dmitri Valeska-Okonkwo, R3 Perspective Dr. Priya Anantharam-Quill, R4 Generalist Dr. Wen-Jie Torvaldsen, DA Dr. Oluwaseun Brandvold

*How a careful panel would likely see this draft; a simulation, not a prediction of any real outcome.*

---

## Decision: Borderline Reject (3) — ICLR label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean **3.20** · official composite **55.9**
**EIC assessment** (internal): weighted rating **3.16** → starting point **3** · weighted composite **55.3** → band 3 (agrees with the rating; no cross-check flag) · **DA ceiling**: none (no CRITICAL raised) · **Final (EIC)**: **3**
**EIC pool position:** better than about **50%** of ICLR submissions (accepted share ≈ 27%); a typical rejected submission (30–54 band). Deciding evidence: a useful open resource and a clear gain over MatNet, but the headline SOTA comparison is not controlled (baseline training, encoder/decoder confound), there is no variance, and the method is incremental.
**Journal-style recommendation:** not applicable (conference target).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The paper targets a recognised gap (neural routing on road-network, asymmetric costs), ships an open, fast OSRM-based generator and code, reports a consistent improvement over the closest matrix-aware baseline MatNet (e.g., 3.981 → 1.797 on ATSP in-distribution; 7.258 → 3.450 on ACVRP; larger on OOD clusters), and includes OOD-city/cluster tests and classical references. For a first benchmark of this kind, that is more than many accepted NCO papers provide.
- **Against acceptance:** The central comparison is confounded: node-only and supervised baselines are not trained on the generator (§6.1), MatNet is missing for ACVRPTW (Table 1), the decoder and depth differ from MatNet and the ablation only varies components inside RRNCO (§5.2, Fig. 4), there are no seeds or error bars, the in-distribution test shares point pools with training (Appendix A), and "real-world" is static 3×3 km OSRM data at n = 100. The method is a recombination of MatNet, ICAM-style attention-free modules and a ReLD-style decoder.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Node-only and supervised baselines not retrained; only RRNCO, MatNet, GCN trained on the generator | R1-W1, DA-M1 | §6.1 ("we do not retrain supervised-learning models"; "same settings … MatNet for ATSP and ACVRP") | **Verified** | Large node-only gaps (Table 1, ACVRP 23–34%) cannot be attributed to missing edge input alone |
| MatNet/GCN/ELG/BQ-NCO/LEHD absent from ACVRPTW block | R1 ERR-3 | Table 1 | **Verified** | MatNet is the closest edge-aware baseline |
| Decoder differs from MatNet (ReLD residual + MLP, −log dist logit term); ablation internal only | R1-W3, DA-M2 | §5.2 Eq. 13–15; Fig. 4 caption | **Verified** (confound exists; its size is unknown; Fig. 4 numbers unverifiable) | The paper does say the decoder "combines" ReLD and MatNet elements |
| No seeds / variance | R1-W2, DA-M5 | §6.1, Table 3 (searched) | **Verified** | |
| In-distribution test from the same 1000-point pools | R1-W4, DA-M4 | Appendix A; §6.1 | **Partly correct** | Test instances are new subsets, so this is non-independence, not label leakage; it weakens only the in-distribution columns |
| Efficiency claim "consistently … computational efficiency" | R1 ERR-1, R4-W2, DA-M6 | §6.2 vs Table 1 times | **Verified** | RRNCO slower than POMO in all three tasks |
| "Single unified framework" | R1 ERR-4, R4-W2 | §6.1/§6.2 | **Partly correct** | Ambiguous rather than contradicted; the table includes multi-task baselines |
| Population counts 50/30/20 vs Table 4 | R1 ERR-2, DA-m3 | §4.1; Table 4 | **Verified** (my count 72/19/9) | Cosmetic |
| "traffic patterns" cited as source of asymmetry, traffic deferred to future work | R2-W2, R3-W1, DA-M3 | §3.1; §4.2 footnote 3 | **Verified** | Durations are static road-graph quantities as far as the text shows |
| Missing task definitions (cost, demands, time windows, OOD-cluster, angle matrix, use of durations) | R1-W6, R4-W1, R3-W3 | §4.3, §5.1.2, §6.1 | **Verified** | Searched the appendix: not stated |
| No time-matched comparison with PyVRP/OR-Tools; OR-Tools better on ACVRPTW | R1-W5 | Table 1 | **Verified** | OR-Tools 1.377 vs RRNCO 3.928 (ACVRPTW in-dist) |
| OR-Tools cited as [61] (CP-SAT entry); [63] cited for traffic forecasting | R2 ERR-5/6, DA-m2 | §6.1; §4.2 footnote 3 | ERR-5 **Verified**; ERR-6 **Partly correct** (judged from the title only) | Minor |
| Market-size forecast presented as fact | R3-W4, DA-m1 | §1; [66] | **Verified** | Minor |
| ICAM / ReLD not compared | R2-W1 | §5.1.2, §5.2 | **Partly correct** | Both are cited and credited; the gap is the missing ablation, not a missing required baseline |
| "Missing" GREAT/GASE | R2 addendum | literature check | **Verified as prior but arXiv-only**; at most Important | Cannot lower a score on its own |

No errors in the reviewers' recomputed numbers were found; all recomputed gaps match the printed costs.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Decisive points (W1, W3, W4, ERR-3) verified against §6.1, §5.2 and Table 1; one figure-based inference was withdrawn in the report check |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly verified; novelty reading fair; one citation point rests on a title |
| R3 (Perspective) | 4 | 3 | 1.0 | Role-appropriate optimism; weaknesses verified; Overall consistent with its own scores |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound, partly overlapping others |
| DA | 3 | 4 | **1.25** | Counter-argument survives the check: no CRITICAL, evidence supports the narrower claim; DA-M1–M4, M6 verified, M5 verified for variance |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised ("No CRITICAL issues found") | I agree: the evidence supports a narrower claim (RRNCO beats MatNet and untuned baselines on OSRM-derived n = 100 instances); no test-set selection is stated; the experiment can test the claim | n/a | n/a |

### Final Decision and Justification
The EIC-weighted rating (3.16 → 3) and the weighted composite (55.3, band 3) agree, so I keep the starting point. I considered going up to Borderline Accept because the resource is useful, the gap to MatNet is large and the issues (retrain baselines, seeds, ablation grid) are rebuttal-feasible, but those fixes have not been shown in the draft, and the method novelty is incremental (literature check: medium; closest prior GREAT/GASE/ICAM-style edge and bias mechanisms). The deciding verified issues are the uncontrolled baseline training (§6.1, Table 1) and the unattributed gain (§5.2, Fig. 4 caption); a typical accepted ICLR paper would have controlled the first. The decision does not exceed the DA ceiling (none). R3's more positive recommendation (4) rests on resource value, which I credit in the Roadmap rather than in the number. Borderline signal: composite and rating both sit near the middle of the band-3 range (55–56), not at a boundary.

---

## Score Summary

### Official Scores and EIC Assessment (from `aggregate_scores.py`, with EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 52 | 56 | 62 | 56 | 48 | 54.8 | 54.0 | 14 |
| Clarity & Presentation | 56 | 58 | 62 | 54 | 55 | 57.0 | 56.8 | 8 |
| Novelty & Originality | 52 | 52 | 60 | 55 | 48 | 53.4 | 52.8 | 12 |
| Significance & Impact | 58 | 60 | 70 | 62 | 56 | 61.2 | 60.5 | 14 |
| Experimental Validation | 44 | 50 | 55 | 52 | 42 | 48.6 | 47.7 | 13 |
| Reproducibility | 60 | 64 | 68 | 62 | 58 | 62.4 | 61.9 | 10 |
| Ethical Compliance | 64 | 64 | 58 | 60 | 58 | 60.8 | 60.9 | 6 |
| **Composite** | 53.7 | 56.6 | 61.7 | 56.8 | 50.7 | **55.9 (before)** | **55.3 (after)** | |

No dimension spread exceeds 20 points; no consistency warnings. Reviewer pool positions: 45, 50, 66, 52, 40 (spread 26, below the 30-point rule).

### Target-Venue Scores (ICLR, scale status: secondary; "as labeled on recent forms, verify against the current form")

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating (decision 3, internal Borderline Reject) | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |
| Venue composite | 55.2 (band 3) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization" to ICLR.

Bringing road-network distances and durations into neural routing, and releasing a fast open generator for it, addresses a real gap between neural solvers and practice.

**Overall Assessment:** The panel found the problem well motivated, the pipeline useful and the gains over MatNet consistent in-distribution and out of distribution. The main reservations concern whether the headline comparison isolates what the paper claims, and how far "real-world" extends.

**Key Strengths Identified by Reviewers:**
1. A locally hosted, versioned OSRM pipeline with fast online instance sampling and public code and data (R1-S1, R2-S2, R3-S3).
2. A clear and consistent improvement over MatNet, with OOD-city and OOD-cluster tests and classical references (R1-S2, R4-S2).
3. Complete training hyperparameters and compute, and a practical orientation toward the matrices planners actually have (R1-S4, R3-S1).

**Key Concerns Requiring Attention:**
1. Baselines are trained differently (node-only and supervised models are not retrained; MatNet/GCN are absent from ACVRPTW), and the gain over MatNet is confounded with a different decoder and depth; the ablation does not isolate the gating, NAB or AAFM (CONSENSUS-4: R1, R2, R4, DA).
2. "Real-world" is narrower than framed: static OSRM matrices in 3×3 km windows, n = 100, synthetic demands/time windows; no asymmetry statistics; traffic deferred (CONSENSUS-4: R1, R2, R3, DA).
3. No seeds or error bars; key definitions missing (angle matrix, cost objective, time windows, OOD-cluster construction, use of durations) (CONSENSUS-3).
4. Wording stronger than the evidence ("consistently … computational efficiency", "single unified framework", "state-of-the-art").

**Critical Challenge (Devil's Advocate):** none rated critical. The DA's strongest objection is that the 23–46% gaps of node-only baselines measure a train/test cost mismatch, and the margin over MatNet cannot be assigned to NAB/gating rather than to the decoder or depth.

**Decision: Borderline Reject (3).** The contribution is real, but the evidence in the draft does not yet support the claim as worded. A revision that retrains the baselines on the generator, adds the missing ablations and seeds, and defines the task generators would likely move this to Borderline Accept or higher.

Sincerely,
Prof. Adaeze Lindqvist-Roca
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Baseline training parity and unattributed gains (decoder/depth confound, missing ablations, MatNet absent in ACVRPTW) | R1, R2, R4, DA | CONSENSUS-4 |
| "Real-world" realism overstated (static OSRM, 3 km windows, n = 100, no traffic) | R1, R2, R3, DA | CONSENSUS-4 |
| Missing seeds / variance | R1, R4, DA | CONSENSUS-3 |
| Undefined task/generator details | R1, R3, R4 | CONSENSUS-3 |
| Overclaiming in wording | R1, R4, DA | CONSENSUS-3 |
| In-distribution test non-independence | R1, DA | CONSENSUS-2 |
| Citation errors | R2, DA | CONSENSUS-2 |
| Dataset licence/documentation; time-matched classical comparison | R3; R1 | SOLO |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Does the resource's value outweigh the evidence gaps? (Overall 4 vs 3) | R3 | R1, R2, R4, DA | The resource is real, but the baseline and attribution gaps affect the paper's main claim; the EIC sides with 3 and credits the resource in the Roadmap |

### Score Spread Discussion
No dimension is flagged (all spreads ≤ 14). Pool positions range 40–66 (spread 26): R3 sits above the others because it weighs the resource and applies the Perspective role's optimism; the EIC places the paper at about 50.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Baseline training disparity | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Encoder/decoder/depth confound | Yes (R1-W3, R2-W1) | n/a | n/a |
| DA-M3 | MAJOR | "Real-world" narrower than framed | Yes (R2-W2, R3-W1) | n/a | n/a |
| DA-M4 | MAJOR | In-distribution overlap | Yes (R1-W4) | n/a | n/a |
| DA-M5 | MAJOR | No variance | Yes (R1-W2) | n/a | n/a |
| DA-M6 | MAJOR | Overclaim | Yes (R1 ERR-1, R4-W2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*Verified issues that undermine the main claim (C3); no upheld DA-CRITICAL item exists.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Baselines not trained on the same data; MatNet/GCN missing for ACVRPTW | R1-W1, ERR-3, DA-M1 | §6.1, Table 1 | Retrain POMO, ELG, MVMoE/RF (coordinates + OSRM-cost reward) on the 80 cities; add MatNet and GCN to ACVRPTW; label GOAL/BQ-NCO/LEHD as zero-shot | High, ≈100–150 GPU-h | Partly (one task) |
| R2 | Gains not attributed to gating/NAB/AAFM | R1-W3, DA-M2, R2-W1 | §5, Fig. 4 | Encoder × decoder grid; AAFM vs MHA; NAB vs heuristic bias; parameter-matched MatNet; k and −log(dist) ablations; tabulate Fig. 4 | High, ≈150 GPU-h | Partly |
| R3 | No variance | R1-W2, DA-M5 | §6.1, Table 1, Fig. 4 | ≥ 3 seeds, mean ± std, paired bootstrap | Medium–High, ≈3× training | Partly |
| R4 | Claims stronger than evidence | DA-M6, ERR-1, ERR-4, R4-W2 | Abstract, §6.2 | Narrow "SOTA", "efficiency", "unified framework", "real-world" | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Missing task and generator definitions (cost, demand, TW, OOD-cluster, angle matrix, duration usage, normalisation) | R1-W6, R4-W1, R3-W3 | Add a task-definition appendix | Low | Yes |
| S2 | No time-matched comparison with classical solvers; solver settings absent | R1-W5 | Report per-instance time, threads and quality-vs-time curves for PyVRP/OR-Tools | Medium | Yes |
| S3 | In-distribution test shares point pools | R1-W4, DA-M4 | Hold out points per city, or lead with OOD results | Medium | Yes |
| S4 | Realism: no asymmetry statistics, static durations, n = 100 | R2-W2, R3-W1, DA-M3, R1-W7 | Dataset statistics table; n = 200/500 test; optional time-of-day or clustered-customer variant | Medium | Partly |
| S5 | Data documentation: licence, OSM snapshot, per-city quality | R3-W2 | Datasheet and licence statement | Low | Yes |
| S6 | Related work: GREAT, GASE, architecture-generalisation work; unsupported "inefficient learning" assertion | R2-W1, R2-W3 | Cite, differentiate or soften | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Forecast presented as fact; [61]/[63] citation mismatches; duplicate references; population-count mismatch; "in parentheses" wording | R2, R3, R4, DA | Correct |
| N2 | Cross-disciplinary extensions (time-dependent VRP, local-search polish, edge-biased attention comparison) | R3 | Mention as future work |
| N3 | Discuss EFormer and SVRPBench (recent preprints) | R2 addendum | Optional |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 1–2 weeks including ≈300–400 GPU-hours (4×A100 class); items R1–R3 can be partly addressed within a rebuttal window on one task.
- Priority 2: 6 items, roughly 3–5 days.
- Priority 3: 3 items, roughly 1 day.
- **Total estimated revision time**: about 2 weeks.

*No Post-Review Analysis (Gap Scout) was requested or run.*
