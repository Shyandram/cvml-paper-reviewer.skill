# Academic Paper Review — simulated ICLR panel (full mode)

*Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction of the outcome. Reviewer personas are fictional. Figures were not available (text extraction only): figure-dependent claims are judged from captions and surrounding text, and say so where it matters. All five reviewer passes were run one after another in a single model context (not independent agents).*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective |
| Primary Discipline | ML systems → LLM inference serving (KV-cache eviction, request routing) |
| Secondary Discipline(s) | Online algorithms / competitive analysis of paging; queueing and load balancing; online regression |
| Paper Type | System (algorithms with a formal competitive-analysis component, evaluated end to end in SGLang) (composite weights: system) |
| Core Technique(s) | Randomized marking-style leaf-token eviction in a radix-tree prefix cache (RLT); greedy latency-estimate routing with online linear residual regression and exponential load decay (LBGR) |
| Target Venue | ICLR (stated by the user), 2026 cycle; profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence; scale status *secondary*, labels not official wording) |
| Paper Maturity | Submission-ready |
| Ethics-Relevant Content | none (no human data); minor: multi-tenant prefix-cache sharing is not discussed |

### Claimed Contributions (as stated by the authors; Section 1)
- **C1**: "the first unified formal model for the KV cache-aware load balancing problem" (Section 1 contribution 1, Section 3.1).
- **C2**: a formal analysis showing the "theoretical limitations of existing system designs": Leaf-LRU has competitive ratio O(n) (Theorems 4, 5).
- **C3**: RLT, randomized leaf-token eviction, "worst-case competitive ratio of O(log n)", matched by a lower bound for any randomized algorithm (Theorems 6, 8, Corollaries 7, 9).
- **C4**: LBGR, an online-regression, latency-estimating greedy router that adapts better than static heuristics (Section 4.2, Algorithm 2).
- **C5**: extensive evaluation on 4 benchmarks and 3 prefix-sharing settings: "up to 6.92× in cache hit rate, 11.96× reduction in latency, 14.06× reduction in time-to-first-token (TTFT), and 77.4% increase in throughput" (Abstract, Section 5, Appendix B).

## Paper memory (factual record shared with all reviewers)

- **Setup facts.** Models: Llama-3.1-8B-Instruct (10 NVIDIA L40), Llama-3.1-70B-Instruct (FP8-quantized) and Mixtral-8×7B-Instruct (4 NVIDIA H200); 4 workers by default, 1–10 varied (Section 5, Appendix A). KV cache fixed at about 200k tokens per model (Appendix A). Implementation on SGLang-0.4.6; RLT in Cython, LBGR in the Rust router (Appendix A). Workloads: GSP (128 groups × 32 queries = 4096 queries; 5 prompt lengths 512–8192; prefix ratio 0.5), ShareGPT and UltraChat (128 clients, 2–8 rounds, 1024-token padded user turns), Loogle (512 documents truncated to 1024–8192 tokens). Default output length 4 tokens (varied to 128). Poisson arrivals, default 12 requests/s (4–20 varied). Two orders: random (default) and "worst-case" round-robin. Baselines: Random, Round-Robin, SGLang cache-aware routing, each with L-LRU; RLT is compared only with L-LRU. LBGR constants: αCACHED = 0, αMISS = 1000 ms per 1k tokens, ρ = 31/32 every 20 ms, 4-parameter linear regression, "learning rate of 0.992" (Appendix A).
- **Splits, tuning, seeds, variance.** There are no train/test splits (serving benchmark). How the LBGR constants and the baselines' thresholds were chosen: **not stated after full-text search** (searched: tuned, tuning, hyperparameter, validation, held-out, grid search). Seeds, repeated runs, error bars, confidence intervals: **not stated after search**. Code: anonymized repository in the supplement (Reproducibility Statement; not provided to the panel, so unverified).
- **Headline numbers and sources.** 6.92× hit rate and "77.4%" throughput: Appendix B text and Table 3 (single worker, round-robin order, GSP, 64 groups). 11.96× median latency and 14.06× median TTFT over Cache-Aware+LRU: Section 5, "End-to-End Performance", stated as averages over 4 benchmarks (Figure 2; the abstract says "up to"). 5.46× and 7.19× on 70B: Section 1 and Appendix B. Table 2 (GSP, default setting): median latency 26680.55 ms → 2263.61 ms (11.8×), median TTFT 25022.76 → 1088.57 ms (23×).
- **Appendix content.** A: setup and constants. B: extra models/benchmarks (Figures 8, 9), shared-prefix ratio, number of queries, output length, batch size (Figures 10–13), single-worker RLT vs L-LRU (Table 3), decay interval (Figure 14). C: all proofs. D: extended related work. E: global radix tree is character-level and may deviate from token-level truth. F: LLM usage statement.
- **Unverifiable.** All figures (Figures 2–14) are bar/line charts available only as extracted axis labels; per-benchmark numbers behind the "average" claims cannot be read. Algorithm 2 and some equations are partly garbled by extraction (treated as unverifiable, not as errors).

## Integrity signals

`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters; the reviewers worked from the redacted copy (identical to the original). No out-of-place instructions were noticed while reading. Nothing to report to the editor.

## Literature check status

Mode `strict`, cutoff 2025-09-24. The fingerprint was written and a concept-only query was attempted (`prefix cache LLM routing`), but the arXiv API returned HTTP 429 and then timed out; no query completed, so **no search results, similarity scores or verification links exist**. Per the skill, the literature check is skipped and the Domain Reviewer relies on knowledge: every recommended reference is marked `[verify]`, nothing is labelled as prior/recent/concurrent by the script, and the claim-level novelty verdicts are from the paper's own related work and the reviewer's knowledge. No baseline scout table, field-snapshot or `similarity` output was produced.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Henrietta Okonkwo-Bell, senior area chair profile (large public research university, Western Europe)
- **Seniority / Expertise**: Senior faculty / ML systems, online algorithms, conference area chairing
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR actually accepts; weights verified specifics over tone

### Reviewer 1 (Methodology): Dr. Kwabena Almeida-Ruiz (industrial systems research lab, North America)
- **Seniority / Expertise**: Senior industry scientist / LLM-serving benchmarking, tail-latency measurement, open-loop load testing
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; insists on sub-saturation load and repeated runs

### Reviewer 2 (Domain): Prof. Anneliese Torvaldsen-Mehta (technical university, Northern Europe)
- **Seniority / Expertise**: Senior faculty / competitive analysis of paging and caching, online algorithms with predictions
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads proofs line by line; asks what is new relative to the classical result

### Reviewer 3 (Perspective): Dr. Priyanka Delacroix-Nwosu (industrial cloud-infrastructure group, South Asia)
- **Seniority / Expertise**: Mid-career / queueing theory, locality-aware load balancing, multi-tenant cloud systems
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for deployment realities and neighbouring literatures

### Reviewer 4 (Generalist): Dr. Joon-ho Barrientos (university ML group, East Asia)
- **Seniority / Expertise**: Mid-career / efficient deep learning, representation learning (not LLM serving specifically)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Saoirse Lindqvist-Adeyemi (independent evaluation-methodology institute, Europe)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, causal confounds in systems benchmarks
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first

*Personas are fictional. Proceeding with the stated assumptions (venue stated; paper type "system" chosen because the contribution is two algorithms plus end-to-end serving evaluation, with theory as one pillar).*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Reviewer: Dr. Kwabena Almeida-Ruiz, Reviewer 1 (Methodology) (industrial systems research lab, North America; fictional persona)
## Expertise: LLM-serving benchmarking; open-loop load testing; tail-latency measurement
## Date: 2026-11-10

## Summary
The paper formalizes prefix-cache serving across M workers as a makespan problem (Section 3.1) and analyzes Leaf-LRU, the eviction policy of SGLang, in the radix-tree setting (Theorems 4–5). It proposes RLT, a randomized marking-style eviction rule, and LBGR, a router that predicts per-worker latency from a cached-token service-time model, a decayed load estimate and an online linear residual. Both are implemented in SGLang and evaluated on four workloads, three models and sweeps over request rate, workers and cache size. The reported gains over SGLang's cache-aware router are large (Table 2: median latency 26.7 s → 2.3 s on GSP).

## Strengths

### S1: Real implementation against the real state-of-the-art router
Both algorithms are implemented inside SGLang-0.4.6 and compared with its shipped routers (Section 5 "Baselines", Appendix A "Implementation"). Table 2 also reports per-query eviction and routing time, and the arithmetic holds (RLT 0.71 − 0.13 = 0.58 ms; LBGR 1.03 − 0.47 = 0.56 ms; total about 2 ms).

### S2: Broad one-factor sweeps
Request rate (Figure 5), workers (Figure 6), cache size (Figure 7), shared-prefix ratio, number of queries, output length and batch size (Figures 10–13) and decay interval (Figure 14) are all swept, on two orders (random and cyclic). Judged from the text, the sweeps are the right axes for a serving paper.

### S3: Component decomposition on the main workload
Table 2 separates RLT-only (Cache-Aware+RLT), LBGR-only (LBGR+LRU) and the combination. This makes the attribution visible: on GSP, LBGR alone gives −77.4% median latency, RLT alone −28.1%. I recomputed both (77.41%, 28.07%).

### S4: Disclosed limitations in Appendix E
The authors state that the global radix tree is character-level and "may deviate from the true cache hit rate", and that it is shared by all baselines.

## Weaknesses

### W1: Headline latency and TTFT gains come from an apparently saturated, 4-token-output regime
Section 5 "Workloads" fixes "The number of output tokens is varied from 4 to 128, with 4 used as the default", and the default arrival rate is 12 requests/s over 4096 GSP queries (Appendix A), about 341 s of load (derived). In Table 2 the strongest baseline sustains only 10.73 requests/s, below the 12 offered, and its median latency is 26.7 s for a 4-token reply. This is an overloaded queue, in which latency is dominated by queue build-up and small service-rate differences produce very large latency ratios (here 11.8× at +11% throughput, 11.92 vs 10.73; derived). The same table shows P95 latency improving only 3.05× and P95 TTFT 4.01× (derived), and Section 5 reports average P95 gains of 2.03× and 2.62× against 11.96× and 14.06× at the median. The abstract's headline figures are therefore measured where the effect is largest and least stable. Figure 5 (request-rate sweep) may address this, but the figure is not available to me and the text states only that LBGR+RLT is lowest "across all request rates".
- **Suggested Fix**: Report latency/TTFT vs offered load up to and below saturation for the main workloads, with output lengths of 128–512 as default in at least one figure, and goodput/SLO attainment. Cost: the GSP run is about 6 minutes of load per configuration; a 6-point load sweep × 4 workloads ≈ 4 GPU-days on the existing 10-L40 cluster at most.

### W2: Single runs, no variance, for a randomized algorithm under random arrivals
After the protocol sweep, no seed, repeat, error bar or confidence interval appears anywhere (searched: seed, variance, error bar, confidence interval, repeat, trials). RLT is itself randomized (Algorithm 1 line 15) and arrivals are Poisson, so run-to-run spread is part of the object being measured, especially for P95 and for the ratio statistics. The 6.92× hit-rate ratio compares 41.93% with 6.06% from one single-worker run (Table 3).
- **Suggested Fix**: Five repeats with different arrival seeds and RLT seeds, mean ± std for Table 2 and Table 3, shaded bands on Figures 5–7. About 5× the current compute of those experiments (hours, not days).

### W3: Baseline set is narrow for "state-of-the-art" claims, and baseline tuning is not described
Eviction is compared only with L-LRU (Section 5 "Baselines"); no other policy (frequency-based, segmented or adaptive recency/frequency, cost-aware) is run, though Section 1 argues the problem is recency's fragility. For routing, Section 1 says the alternatives are "a static linear score" (Dynamo, llm-d) and SGLang's threshold rule, but only the threshold rule (cache-aware) is evaluated; the linear-score family is described and not run. The SGLang cache-aware threshold is used at its default (not stated otherwise), while LBGR's constants were chosen by an undisclosed procedure (W5). Claim "Cache-Aware+LRU is the current state-of-the-art" (Section 5) is thus a claim about one open-source router.
- **Suggested Fix**: Add a tuned linear-score router (sweep the weight on load vs hit rate, as the baseline's own authors would), at least one non-recency eviction policy, and a prompt-scheduling system of the kind named in the Domain report. State the baseline configuration.

### W4: "Balances query load" is never measured
Section 3.1 defines the objective as makespan, "min_x max_i P_i^(N)", and the title and abstract claim learning "balances query load". Full-text search shows "makespan" occurs only in Sections 1, 3 and 3.1; no result reports makespan, per-worker queue length, load imbalance or utilization. The evaluated metrics (hit rate, latency, TTFT, throughput) cannot separate better balancing from better cache reuse.
- **Suggested Fix**: Add per-worker load (max/mean queue length or tokens in flight, Jain index) and realized makespan to Table 2 and Figure 6.

### W5: LBGR is under-specified and its constants are unexplained
Appendix A fixes αCACHED = 0 and "uncached token coefficient to αMISS = 1000 ms per 1k tokens", ρ = 31/32 every 20 ms, and a regression "updated online with a learning rate of 0.992" (a value above 0.99 is unusual for a gradient step size and may denote a forgetting factor; this is a question, not an error). How these were chosen and on which workloads is not stated. The only ablation is of the decay interval (Figure 14, "increasing ∆t leads to a drop in performance"); there is no ablation of the residual regression itself, of the service-time term or of the decay. Algorithm 2 uses ONLINEUPDATE, RELEASELOAD and ϕ, which are not defined in the main text.
- **Suggested Fix**: Ablate (a) no regression, (b) no decay, (c) token-count-only load; give the tuning protocol; define the subroutines (pseudo-code in the appendix).

### W6: Theory predictions are never tested, and the "worst-case" order is a benign adversary
Appendix B says the experiments "validate our theoretical analysis transferring in practice", but no experiment measures a competitive ratio (misses vs an offline Belady-style optimum) or uses the adversarial sequence of the lower-bound proofs. The round-robin order of Section 5 "Query Order" is the textbook cyclic scan on which any LRU variant is pathological, so a gain there is not evidence for the O(log n) bound. Benchmarks are also modified (Section 5: "We extend these benchmarks by introducing variability in prompt lengths", plus 1024-token padded turns, Appendix A), so ShareGPT/UltraChat are partly synthetic.
- **Suggested Fix**: Compute offline-optimal miss counts on the traces and report the empirical ratios of L-LRU and RLT; evaluate the Theorem 4 lower-bound sequence.

**Minor:** typos ("no dependent algorithm" in Section 4.1 should read randomized; "Mixtral-8×B" in Appendix B; baseline numbering "(iv)" in Appendix A; "∆t" notation).

### Claim-to-evidence map

| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|-------------|---------------------|---------|
| C1 | first unified model | Abstract, Section 1, Section 3.1 | Equations 1–3 | Partially (model exists; no joint analysis, see Domain report) |
| C2 | L-LRU competitive ratio O(n) | Section 1, Section 3.2 | Theorems 4–5, Appendix C.1 | Supported (proofs read; modulo classical results) |
| C3 | RLT O(log n), optimal among randomized | Section 4.1 | Theorems 6, 8, Appendix C.2 | Partially (proof dependency, see ERR-5 in the Domain report) |
| C4 | LBGR adapts better than static heuristics | Section 4.2 | Table 2, Figures 2–7 | Partially (one heuristic baseline, single runs, saturated default) |
| C5 | up to 6.92×, 11.96×, 14.06×, 77.4% | Abstract | Table 2, Table 3, Figure 2 | Partially (see ERR-1 and ERR-3) |

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Appendix B text vs Table 3 | "6.92× higher hit rate and a 77.4% increase in throughput" | Table 3 normalized throughput is 0.62 (L-LRU) vs 1.0 (RLT): 1/0.62 = 1.61, i.e. +61%, not +77.4%; 77.4% would print as 0.56. The hit-rate ratio is right (41.93/6.06 = 6.92). The same 77.4% appears in the abstract. | Recomputed from Table 3 | Medium (depends on the stated normalization) | MAJOR (headline number, conclusion intact) | Correct the abstract and text, or explain the normalization |
| ERR-2 | E1 | Appendix B text vs Table 3 | "RLT reduces median latency and TTFT by 45% and 47%, respectively." | Table 3 median TTFT 0.55 → 45%; P95 latency 0.53 → 47% while the text says "reducing P95 latency and P95 TTFT by 45% and 46%" (47% expected). | Recomputed from Table 3 | High | MINOR | Align text with Table 3 |
| ERR-3 | E1/E5 | Abstract and Section 1 vs Section 5 | "improvements of up to 6.92× in cache hit rate, 11.96× reduction in latency" | Section 5 states 11.96× and 14.06× as averages over four benchmarks ("On average … improves over the state-of-the-art Cache-Aware+LRU by 11.96×"), not maxima; Figure 2 carries per-benchmark annotations of 11.8× (GSP row) and 32.9× (Loogle row), though the reference method of each annotation is not readable from the extracted text; the abstract mixes a single-worker figure (6.92×) with multi-worker averages. | Cross-referenced (two locations) | High | MAJOR (wording of a headline claim) | State which setup each number comes from; give per-benchmark values in a table |
| ERR-4 | E6 | Section 3.1 Equation 2 vs Section 4.2 | "we apply exponential decay independently every ∆t > 0 time units" | The model's queue load is cumulative (Equation 2 adds service cost only), whereas LBGR decays it and also releases load on completion (Algorithm 2); the model that is analyzed and the algorithm that is evaluated differ, and the makespan objective is not what LBGR minimizes. | Cross-referenced (Equation 2, Algorithm 2, Section 4.2) | High | MAJOR | State that LBGR approximates a different (time-decayed) objective, or extend the model |

## Missing References
Methodology-level only; see Domain report. (No additions.)

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound components but single runs, a saturated default and a narrow baseline set |
| Clarity | 3 | Mostly clear; Algorithm 2 relies on undefined subroutines |
| Significance | 3 | A serving-stack gain would matter if it survives sub-saturation |
| Originality | 2 | Classical marking/paging adapted to a radix tree; a small regression on a hit-rate router |

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline effect is measured in an apparently overloaded 4-token regime with single runs, and the main claimed mechanism (load balancing) is not measured; typical accepted systems papers show at least repeat variance and a stronger baseline set.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Correct arithmetic in Table 2; ERR-1/3/4 and a model–algorithm mismatch |
| Clarity & Presentation | 62 | Competent | Clear narrative; headline numbers mix setups |
| Novelty & Originality | 55 | Competent | Incremental on classical paging and on hit-rate/load routers |
| Significance & Impact | 62 | Competent | Drop-in for a widely used stack, size of effect uncertain |
| Experimental Validation | 48 | Developing | W1–W4: regime, no variance, narrow baselines, no balance metric |
| Reproducibility | 60 | Competent | Constants and code reported; tuning protocol missing; supplement not provided (unverified) |
| Ethical Compliance | 65 | Competent | Limitations paragraph present; nothing at stake |

## Questions for Authors
1. What are latency and TTFT of all methods at an offered load where the best baseline is not saturated (for example 50–70% of its capacity) and with 128 output tokens? A consistent multi-fold gain there would raise my Experimental Validation score; a gain that shrinks toward the P95 ratios would lower it.
2. Over five arrival and eviction seeds, what is the spread of Table 2's P50/P95 and of the Table 3 hit-rate ratio?
3. How were αMISS = 1000, ρ = 31/32, 20 ms and the 0.992 value chosen, on which workloads, and was the SGLang threshold tuned equally?
4. What are the per-worker queue lengths and the realized makespan for the cache-aware router vs LBGR?
5. In ERR-1, what normalization gives 77.4%?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. Section 6 names multimodality and at most 10 workers; the saturated default, single runs and baseline coverage are not discussed.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. The idea is sound and the system real, but the evidence that matters most (sub-saturation behaviour, variance, load-balance effect, stronger baselines) is missing or not shown.

## Confidence
**4**: I recomputed the tables and read the appendix; I could not read any figure.

---

# Peer Review Report

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Reviewer: Prof. Anneliese Torvaldsen-Mehta, Reviewer 2 (Domain) (technical university, Northern Europe; fictional persona)
## Expertise: competitive analysis of paging and caching; online algorithms with predictions
## Date: 2026-11-10

## Summary
The paper models prefix-sharing KV caching as paging over a radix tree with leaf-only eviction. It shows that Leaf-LRU has competitive ratio about B_i − L + 1 to B_i − L + 2 (Theorem 4), that a randomized marking variant (RLT) is Θ(log(B_i − L))-competitive (Theorem 6) and that no randomized algorithm can beat this (Theorem 8). It also proposes a latency-predicting router and shows end-to-end improvements in SGLang.

## Strengths

### S1: A clean formalization of an engineering heuristic
Section 3.2 turns SGLang's leaf-LRU into a well-defined paging variant with token granularity, whole-path insertions (Γ_j = q_j ∥ a_j) and a batching extension (Theorem 5), which is a useful starting point for analysis.

### S2: The upper and lower bounds on L-LRU are stated tightly
Theorems 4 and 5 give both upper (B_i − L + 2) and lower (B_i − L + 1) bounds, and the proofs track the phase structure of the classical analysis carefully (Appendix C.1, Lemmas 1–3).

### S3: Theory and implementation are in the same paper
The marking algorithm is implemented as written (Algorithm 1 vs Appendix A "Implementation"), and the single-worker comparison in Appendix B (Table 3) isolates eviction from routing, which is the cleanest empirical test of C3.

### S4: Honest scope on one point
Appendix E discloses that the router's hit estimate comes from a character-level tree shared with all baselines.

## Weaknesses

### W1: The theory is a re-instantiation of classical paging results and is not positioned as such
Appendix C.2 follows Fiat et al. (1991) step by step ("Following the analysis in (Fiat et al., 1991)"), and the lower bound of Theorem 8 builds paths that share a prefix and differ in the last token: "each path shares a common prefix of length L − 1 but differs in the last" tail token. With B_i − L + 2 such paths and a cache that holds B_i tokens, this is classical paging with k = B_i − L + 1 evictable pages, whose deterministic bound (LRU is k-competitive, Sleator and Tarjan, 1985 [verify]) and H_k randomized lower bound are textbook. The contribution is the observation that this embedding captures radix-tree leaf-eviction and a ratio parameterized by the shortest path length L, not new competitive-analysis technique. The paper should say this plainly. Also, the headline contrast ("exponentially better than the O(n) achieved by the existing LRU-based eviction policy", Section 1) is between B_i ≈ 2×10^5 tokens (Appendix A: about 200k-token cache) and about ln B_i ≈ 12; Table 2 shows the measured gain of RLT over LRU under the same router is 28.1% median latency, so the asymptotic ratio says little about practice.
- **Suggested Fix**: State the reduction to paging explicitly, credit the classical bounds, and describe what the tree structure and path length change. Report the empirical ratio of misses to an offline optimum (see R1-W6).

### W2: "First unified model" and "limitations of existing systems" exceed what is analyzed
The abstract claims "the first unified mathematical model that captures the core trade-offs between KV cache eviction and query routing", and Section 1 says the analysis "reveals the inherent limitations of the LRU-based eviction policies". But (i) every theorem concerns one worker's eviction; none concerns routing or the coupling, and LBGR has no guarantee (no regret, no approximation ratio, no convergence); (ii) the model's objective is makespan, which LBGR does not minimize (R1 ERR-4); (iii) the closest formal precedent that the authors do cite, "Online scheduling for llm inference with kv cache constraints" (reference list; Jaillet et al.), appears only as a generic motivation for "LLM serving system" overhead (Section 1) and for quadratic cost (Appendix D), not in Section 2 or in a differentiation. Without a statement of what Section 3.1 adds over that model, "first" is not supported. In the related work, prior systems are said to "lack formal modeling" (Section 1: "Existing work, however, primarily relies on heuristics to address this problem"), which is not demonstrated for the cited scheduling-theory work.
- **Suggested Fix**: Narrow C1 to "a formal model used to analyze eviction", add a differentiation paragraph against the cited scheduling-with-KV-constraints work and against learning-augmented caching, or provide a result about the joint problem (even a lower bound for cache-affinity vs load).

### W3: Proof dependency in Theorem 6 (Medium confidence; see ERR-5)
The Theorem 6 proof bounds the number of stale tokens that can miss using a statement proven for L-LRU: "According to Theorem 4, the total number of misses in a phase is upper bounded by" min{B_i − L + c, B_i}. Theorem 4 and Lemma 2 are about L-LRU (and use Lemma 3, whose proof is specific to LRU's deterministic order), not about RLT, whose eviction is random. A trivial bound of B_i would give Θ(log B_i), which equals Θ(log(B_i − L)) only when L is a constant fraction of B_i or smaller; the stated parameterization in B_i − L is not established when L is close to B_i. In addition, "OPT" is defined as evicting "the leaf token whose next appear lies furthest in the future" (Section 3.2) without a proof that this is optimal for leaf-only eviction in a tree.
- **Suggested Fix**: Prove the stale-token bound for RLT directly or weaken the claim to Θ(log B_i); add a short optimality argument for the comparator or compare against any offline algorithm.

### W4: Assumptions that limit the batch theorems, and one edge case
Theorem 5 requires "we assume the queries within each batch are distinct" and βL_max ≤ B_i; Appendix C.1 argues this is "essential", but shared prefixes are the point of the setting, and identical in-flight requests are common. Algorithm 1 line 14 picks from "{leaf tokens in S} \ T"; whether this set can be empty (all leaves marked while internal nodes are unmarked after a phase reset) is not addressed (a question, not an error). The model drops decode cost (Section 3.2: "we ignore the hit cost and focus on the total number of token misses") and assumes identical workers (Section 3.1, footnote 1).
- **Suggested Fix**: Discuss when each assumption fails and what the bound becomes; show that U is never empty.

### W5: Citations that do not match the claims they support (E7; Medium confidence)
- "storing and reusing the key-value pairs … as reusable prefixes for future generation (Vaswani et al., 2017)" (Section 1): the cited paper introduces the Transformer, not KV caching as a prefix-reuse technique.
- "(Sun et al., 2024; Zheng et al., 2024; Lee et al., 2024)" are cited in Section 2 as KV-cache-aware load balancing works. Sun et al. is Llumnix (dynamic request migration/rescheduling), and the Lee et al. entry in the list is Infinigen (KV-cache management for long-context generation), neither of which is a KV-cache-aware router.
- Appendix D cites "Lin et al., 2016; Wu et al., 2020; Zhou et al., 2018; Jiang & Agrawal, 2018" for compressing cached KV values; the Wu et al. entry is "Integer quantization for deep learning inference: Principles and empirical evaluation" (weights and activations).
- Appendix D writes "SkyLB … (Xia et al., 2025)", while the bibliography entry is titled "Skywalker: A locality-aware cross-region load balancer for llm inference".
- **Suggested Fix**: Re-check these attributions; cite the correct sources for KV-cache-aware routing.

## Missing References
*Literature check unavailable (arXiv API unreachable), so none was verified by script; all entries are from knowledge and marked `[verify]`. Not required comparisons by label; they are recommendations to position the work.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Srivatsa et al., "Preble: Efficient Distributed Prompt Scheduling for LLM Serving", ICLR 2025 `[verify]` | Same problem (distributing requests across GPUs to trade prefix-cache reuse against load, with an explicit load model); neither cited nor compared |
| Important | Lykouris and Vassilvitskii, "Competitive Caching with Machine Learned Advice", ICML 2018 (J. ACM 2021) `[verify]` | Randomized marking with learned predictions; the natural frame for RLT plus a learned component |
| Important | Qin et al., "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving", FAST 2025 `[verify]` | Production prefix-cache-aware global scheduler with a load/hit trade-off |
| Important | Bienkowski et al., "Online Tree Caching", SPAA 2017 `[verify]` | Online caching with tree-structured dependency constraints, close to leaf-only eviction |
| Helpful | Sleator and Tarjan, "Amortized efficiency of list update and paging rules", CACM 1985 `[verify]` | Original k-competitiveness of LRU, the O(n) result being re-derived |
| Helpful | Line of work: prefix-cache-aware scheduling and eviction for hybrid or long-context models (several 2024–2025 systems papers) | Context for eviction alternatives beyond recency; described by line of work, not by title |

## Novelty Assessment (without a literature-check profile; from the paper's own related work and knowledge)

| Claim | Dimension | Novelty | Closest prior work (from knowledge, `[verify]`) | Cited and differentiated? |
|-------|-----------|---------|------------------------------------------------|---------------------------|
| C1 unified model | method/problem | medium–incremental | scheduling with KV-cache constraints (Jaillet et al., cited only generically) | Cited, not differentiated |
| C2 L-LRU O(n) | result | incremental | LRU k-competitive (Sleator–Tarjan); tree structure is the delta | Fiat et al. cited; Sleator–Tarjan not |
| C3 RLT O(log n) + lower bound | method/result | incremental | randomized marking and H_k bounds (Fiat et al., cited) | Cited, followed closely |
| C4 LBGR | method | incremental–medium | hit-rate/load routers (SGLang, Dynamo, llm-d); Preble `[verify]` | Heuristics cited; Preble not |

Paper reading: no claim is judged "known"; C2 and C3 are established up to the tree-structure delta, a MAJOR-at-most positioning issue. Prior work closest to the paper as a whole (attribution): Fiat et al. (1991) for the theory; SGLang's cache-aware router for the system.

### Error Log (Domain Reviewer)

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-5 | E2/E3 | Appendix C.2, Theorem 6 proof | "According to Theorem 4, the total number of misses in a phase is upper bounded by" | The bound is proven for L-LRU (Lemma 2, Lemma 3) and is applied to RLT, whose eviction differs | Cross-referenced (Theorem 4 statement, Lemma 2, Theorem 6 proof) | Medium | MAJOR (result stays Θ(log B_i), parameterization in B_i − L unproven) | Prove directly for RLT or state Θ(log B_i) |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory is correct in spirit; one dependency gap; empirical side single-run |
| Clarity | 3 | n undefined in the main-text bounds; otherwise readable |
| Significance | 3 | Useful formalization; practical gain plausible |
| Originality | 2 | Re-instantiation of classical results |

## Dimension Scores (0–100)

**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the formal results are adaptations of classical paging bounds and the joint claim is not analyzed, while the end-to-end gain is real in kind; this is a borderline systems-plus-theory paper that sits just below accepted-paper typicality.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Proofs follow classical structure; ERR-5 and untested comparator optimality |
| Clarity & Presentation | 64 | Competent | n in "O(n)" and "O(log n)" is undefined in Section 1 |
| Novelty & Originality | 52 | Developing | Classical paging embedded in a radix tree; incremental router |
| Significance & Impact | 62 | Competent | Useful to serving practitioners if gains hold |
| Experimental Validation | 55 | Competent | Wide sweeps, narrow baselines |
| Reproducibility | 65 | Competent | Algorithms and constants given; code in supplement (unverified) |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations stated |

## Questions for Authors
1. Is Theorem 8 anything more than the classical H_k paging lower bound with k = B_i − L + 1? If the tree structure changes the bound, where?
2. Can the Theorem 6 stale-token bound be proven for RLT without Theorem 4? Raises my Technical Rigor if yes.
3. How does Section 3.1 differ from the cited online-scheduling-with-KV-constraints model, and does any result of the paper hold for the joint problem?
4. Can U in Algorithm 1 line 14 be empty after a phase reset?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially: the theory's assumptions (distinct queries in a batch, identical workers, no decode cost) are stated but not discussed as limits.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A correct but largely classical theory, a joint claim not backed by a joint result, and missing positioning against closely related scheduling work.

## Confidence
**4**: I read all proofs in Appendix C; the related-work judgments rely on knowledge since the search tool was unavailable.

---

# Peer Review Report

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Reviewer: Dr. Priyanka Delacroix-Nwosu, Reviewer 3 (Perspective) (industrial cloud-infrastructure group, South Asia; fictional persona)
## Expertise: queueing theory; locality-aware load balancing; multi-tenant cloud systems
## Date: 2026-11-10

## Summary
The authors treat request routing for prefix-cached LLM serving as a trade-off between cache affinity and load balance, an old tension in distributed systems, and propose a router that learns a latency estimate online plus a randomized eviction rule. If the reported behaviour holds beyond the tested regime, the combination is attractive because it is a drop-in change to an open-source stack with about 2 ms of added overhead per query.

## Strengths

### S1: A real trade-off in a real stack
Figure 1 and Section 1 frame cache affinity vs global balance well, and the router change is a drop-in replacement in SGLang's Rust router (Appendix A). Practitioners could adopt it.

### S2: Overheads are measured
Table 2 reports eviction and routing time per query, and Section 5 argues the roughly 2 ms is negligible against seconds of latency. For serving papers this is more than usual.

### S3: Sweeps over scale axes
Workers (2–10, Figure 6), cache size (Figure 7), request rate (Figure 5) and model family (Figures 3, 8, 9) cover the operational knobs a cluster operator would turn. The limitations paragraph openly names the 10-worker ceiling (Section 6: "our available computation resources limit the experiments to at most 10 workers in a single-domain setup").

## Weaknesses

### W1: Queueing-regime reporting would make the result more useful
The default point (12 requests/s, 4-token outputs, Table 2) has the best baseline serving 10.73 requests/s, which is below the offered load. Queueing theory says latency near and past saturation is very sensitive to small service-rate differences, so ratios such as 11.8× say more about how far past the knee the baseline sits than about steady-state benefit. Operators care about the load at which each router meets an SLO.
- **Suggested Fix**: Plot latency percentiles against utilization for each router and report the maximum load that meets a given P95 TTFT SLO (goodput at SLO). This frames the same data in operator terms.

### W2: The affinity-vs-balance literature is not connected
Bounded-load consistent hashing and power-of-two-choices routing are the standard answers to "stay local unless the node is overloaded", and join-the-shortest-queue with affinity is analyzed in queueing theory; the paper's cache-aware heuristic and LBGR are instances of this family. Naming these baselines, even as a lightweight "locality with bounded load" router, would tell readers whether a learned estimator is needed. (No specific paper is claimed here beyond the method names.)
- **Suggested Fix**: Add a bounded-load or power-of-two-choices router as a baseline, and discuss the connection in Section 2.

### W3: Assumptions that will not survive deployment unexamined
Workers are assumed identical (Section 3.1 footnote 1: "assume all deployed LLMs are of the same type"), arrivals are Poisson, and the hit estimate comes from a character-level tree that "may deviate from the true cache hit rate" (Appendix E) through staleness under concurrent updates. At more than 10 workers, a single router and global tree are a central bottleneck and the estimate is staler; heterogeneous GPU generations change αMISS per worker (αMISS is a single fixed constant, Appendix A). Chunked prefill, offloaded KV tiers and prefill/decode disaggregation change what a "miss" costs.
- **Suggested Fix**: Evaluate with a heterogeneous worker pair (for example L40 + H200) and with bursty (non-Poisson) arrivals, or state them as limits.

### W4: Multi-tenant privacy and security are not discussed
Sharing prefix caches across users creates a timing side channel (a cache hit reveals that someone sent that prefix); locality-seeking routers make cross-user hits more likely. The paper has no broader-impact or ethics statement beyond the use of LLMs for polishing (Appendix F).
- **Suggested Fix**: Add a short discussion of tenancy isolation (per-tenant cache salts or partitions) and its cost to the proposed policies.

## Missing References
Optional; named only as methods: bounded-load consistent hashing; power-of-two-choices load balancing; prefix-cache timing side channels in LLM APIs `[verify]` (described by line of work, not by title).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Reasonable design, wide sweeps; regime caveats |
| Clarity | 3 | Motivation figure and algorithms are clear |
| Significance | 3 | Deployable improvement to a widely used stack |
| Originality | 3 | A fresh combination in this setting |

## Dimension Scores (0–100)

**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a deployable change to a major open-source serving stack with measured overhead and wide sweeps; typical accepted systems papers carry the same kind of gaps.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Sound design; gaps are in evaluation, not method |
| Clarity & Presentation | 68 | Competent | Clear motivation and algorithms |
| Novelty & Originality | 62 | Competent | New for this setting even if each piece is classical |
| Significance & Impact | 72 | Competent | Drop-in, measured overhead, relevant to a hot area |
| Experimental Validation | 60 | Competent | Many sweeps; saturated default |
| Reproducibility | 68 | Competent | Constants and implementation stated; code in supplement |
| Ethical Compliance | 62 | Competent | No ethics discussion of shared-cache side channels |

## Questions for Authors
1. What happens with two worker types or bursty arrivals (what would raise or lower my Significance score)?
2. What is the router's throughput ceiling in requests per second as workers grow past 10?
3. Does a per-tenant cache partition change RLT/LBGR gains?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially: scale and multimodality are named; heterogeneity, burstiness and tenancy are not.

## Ethics Review Flag
**No**: shared prefix-cache side channels are a design consideration, not a flagged concern for this paper.

## Overall Score
**4**: Borderline Accept. A deployable, measured improvement with typical systems-paper gaps.

## Confidence
**3**: Fairly confident; I focused on deployment and did not recompute the theory.

---

# Peer Review Report

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Reviewer: Dr. Joon-ho Barrientos, Reviewer 4 (Generalist) (university ML group, East Asia; fictional persona)
## Expertise: efficient deep learning; representation learning
## Date: 2026-11-10

## Summary
The paper argues that LRU eviction and heuristic routing in multi-worker LLM serving are both suboptimal. It builds a formal model, proves that Leaf-LRU can be very far from optimal in the worst case, proposes a randomized replacement (RLT) with a logarithmic bound and a learned latency-based router (LBGR), and shows large latency and TTFT reductions on four workloads in SGLang.

## Strengths

### S1: Clear problem statement
Figure 1 and the first page convey the two tensions (single-LLM eviction; multi-LLM affinity vs balance) to a non-specialist in a few sentences.

### S2: Two algorithms, each with a short algorithm box
Algorithm 1 (RLT) and Algorithm 2 (LBGR) are compact and easy to follow at the structural level; Section 4.1 explains the marking idea in plain words.

### S3: A useful ablation with overhead
Table 2 decomposes the gains by component and reports cost, which suits a venue that values understanding over leaderboard position.

### S4: A short, honest limitations paragraph and a reproducibility statement
Section 6 names multimodality and scale limits; the Reproducibility Statement lists code, configs and scripts in the supplement (unverified by me).

## Weaknesses

### W1: The headline numbers cannot be checked from the paper and mix setups
All main results (Figures 2–7) are normalized bar charts; the per-benchmark values behind "On average, LBGR+RLT achieves 30.9× and 44.49× improvements in median latency and TTFT" are not tabulated. The abstract says "up to 6.92× … 11.96×", while Section 5 gives 11.96× as an average, and 6.92× comes from a single-worker run (Table 3). A reader cannot tell which number belongs to which setting. Algorithm 2 also calls ONLINEUPDATE, RELEASELOAD and ϕ without definitions in the main text.
- **Suggested Fix**: Add one table with raw medians and P95 per benchmark and method (Llama-8B), and put the setup next to each abstract number. Define the subroutines.

### W2: The title and framing promise more than the content delivers
"A Joint Perspective" and "first unified mathematical model" suggest a joint treatment, but the theorems cover single-worker eviction only (Section 3.2, Section 4.1) and the router has no formal guarantee. "Learning" is a 4-parameter linear regression per worker (Appendix A), and in Table 2 LBGR gives most of the gain (−77.4% median latency vs −28.1% for RLT), so "Randomization Boosts KV Caching" is not the dominant effect on the main workload. In the introduction, "O(n)" and "O(log n)" use an undefined n (the theorems use B_i − L).
- **Suggested Fix**: Define n; reframe the claims around what is proved (eviction) and what is shown empirically (routing).

### W3: Evidence for generality is thinner than the text suggests
Section 5 says the algorithms' "generalizability" is shown across scales and architectures, but the main text covers 70B and Mixtral only on ShareGPT (Figure 3, reporting 38% and 44.87% reductions vs the best baseline); the larger factors (5.46×, 7.19× for 70B) and the 24.2% for Mixtral are in Appendix B as averages. The gains on the MoE model are modest relative to the 8B headline.
- **Suggested Fix**: Report 70B and Mixtral on all four benchmarks in the main text (or a table), state the factors consistently, and keep the headline for the setting it comes from.

### Venue criteria checklist (ICLR)
| Item | Grade | Location |
|------|-------|----------|
| Soundness: claims supported by evidence | Partly | Section 5; no variance; saturated default |
| Soundness: theory correct | Partly | Appendix C (Theorem 6 dependency) |
| Presentation | Partly | Headline numbers mix setups; undefined n |
| Contribution: new method or insight | Partly | Section 4; classical analysis, incremental router |
| Contribution: significance to ICLR audience | Met | Section 1; LLM serving is of broad interest |
| Reproducibility | Met (unverified) | Reproducibility Statement; Appendix A |

**Minor:** the figures are dense (seven panels per row); typos noted by Reviewer 1.

## Missing References
None added.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid components, gaps in evidence |
| Clarity | 3 | Understandable; mixed headline numbers |
| Significance | 3 | A widely used stack |
| Originality | 3 | A reasonable new combination |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a relevant problem, a working system and a clear ablation outweigh weaknesses (single runs, framing, narrow baselines) that many accepted ICLR systems papers share.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound but with gaps |
| Clarity & Presentation | 66 | Competent | Clear structure; headline numbers confusing |
| Novelty & Originality | 60 | Competent | Reasonable combination |
| Significance & Impact | 68 | Competent | Practical stack |
| Experimental Validation | 58 | Competent | Broad but single-run |
| Reproducibility | 68 | Competent | Constants and code statement |
| Ethical Compliance | 64 | Competent | Limitations present |

## Questions for Authors
1. Can you provide a table of raw per-benchmark values behind the 11.96× and 14.06× averages, with the setup of each abstract number?
2. What is n in the O(n) and O(log n) of Section 1?
3. Do the 70B and Mixtral gains hold on the other three benchmarks? A consistent factor would raise my Clarity and Significance scores.

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**4**: Borderline Accept. A relevant, working system with typical weaknesses; the framing and number reporting need tightening.

## Confidence
**4**: Confident on clarity and venue fit; I did not verify the proofs.

---

# Devil's Advocate Report

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Reviewer: Dr. Saoirse Lindqvist-Adeyemi (independent evaluation-methodology institute, Europe; fictional persona)

---

## Steelman
The authors identify a real inefficiency in widely deployed LLM-serving stacks, show that the recency policy has a poor worst-case guarantee, replace it with a policy that has a near-optimal guarantee, and add a cheap learned router. In an actual serving system, with overhead of about 2 ms per query, the combination reduces latency severalfold against the shipped router across models and workloads.

---

## Core Argument Chain
1. LRU eviction has competitive ratio O(n) in the radix-tree prefix cache (Theorems 4–5).
2. Randomized leaf-token eviction has O(log n) and is optimal among randomized algorithms (Theorems 6, 8).
3. Static cache-aware routing is heuristic and cannot adapt; an online latency-predicting router can (Section 4.2).
4. Experiments show gains of up to 11.96× in latency and 14.06× in TTFT over the state-of-the-art (Section 5).
5. The gains are explained by the formal model ("Our theoretical results are validated by extensive experiments", Abstract).
∴ A joint treatment of eviction and routing, built on a unified model, improves KV caching and balances load.

---

## Strongest Counter-Argument
Even if every proof is correct, the paper does not show that its theory or its "joint" model explains the gains it reports, and the gains themselves are measured where they are least informative. The headline factors come from a default configuration in which the strongest baseline serves 10.73 requests/s against 12 offered, outputs are 4 tokens, and median latency is 26.7 s (Table 2): a saturated open-loop queue, where latency is a steep function of service rate, so an 11% throughput difference becomes an 11.8× latency difference. The tail ratios (3.05× P95 latency, 4.01× P95 TTFT in Table 2 by my computation; 2.03× and 2.62× on average in Section 5) show how much of the median effect is queue build-up. The experiment that is called "worst-case" (round-robin order) is the textbook scan on which every recency policy fails, so it says nothing about the O(log n) bound, and no experiment measures a competitive ratio. The largest single effect on the main workload comes from the router (−77.4% median latency vs −28.1% for RLT, Table 2), and the router has no theory at all: its objective is not the makespan of Section 3.1 (load is decayed, Section 4.2, not cumulative, Equation 2), and makespan or load imbalance is never reported. The title's claim that learning "balances query load" is therefore untested; what is measured is that a different router yields lower queueing delay in an overloaded system, which any better load-aware router might do. The authors need to show, at sub-saturation load with realistic output lengths, with repeated runs and with a stronger routing baseline, that the joint design is what matters, and to measure load balance directly. Without that, the paper establishes a correct but classical eviction result and a promising but not isolated engineering gain.

---

## Issue List

### CRITICAL Issues

No CRITICAL issues found. The main claims are narrowed, not contradicted, by the evidence: the results support a weaker claim (gains over SGLang's router in the tested regime) and no test-set selection or leakage is stated (protocol sweep: no tuning or selection statement; a serving benchmark has no held-out split).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (regime) | Table 2, Section 5 "Workloads", Appendix A | Saturated default (10.73 vs 12 requests/s offered, 4-token outputs); median ratios vs P95 ratios; headline factors not representative of steady state | Sub-saturation load sweeps at 128+ output tokens; goodput at SLO |
| DA-M2 | Scope / logic | Abstract, Section 1, Section 3, Section 4.2 | "Unified/joint" model and "limitations of existing methods" claimed; theorems cover single-worker eviction only; LBGR has no guarantee and optimizes a different objective than Section 3.1 | Narrow to what is proved; or prove a joint result |
| DA-M3 | Evidence (claim wording) | Figure 2 caption, Section 5 "Number of Workers" | "Our algorithms consistently outperform all baselines across all benchmarks and metrics" and "consistently outperforms all baselines across all metrics and settings", while the same paragraph says "the throughput of all methods converges to the same value" at 6+ workers | Say "matches or exceeds"; state where methods tie |
| DA-M4 | Evidence (aggregation) | Section 5, abstract | Averages of per-benchmark ratios (30.9×, 44.49×, 11.96×, 14.06×) are dominated by the benchmarks with the largest ratios (Figure 2's extracted annotations show 11.8×, 23.0×, 32.9×, 29.4× on two benchmarks; the reference method of each is not readable from the text) and are labelled "up to" in the abstract; the 77.4% throughput figure does not match Table 3 (R1 ERR-1) | Report per-benchmark values, geometric means and medians; fix the throughput figure |
| DA-M5 | Alternative explanations / baselines | Section 5 "Baselines" | "State-of-the-art" is one open-source threshold router at default settings; LBGR's constants were chosen by an undisclosed procedure on, presumably, the evaluated workloads (GSP's lengths cycle through 5 values, Appendix A) | Tuned linear-score and bounded-load baselines; disclose tuning; evaluate on held-out workload shapes |
| DA-M6 | Logic | Section 1, Theorems 4, 6 | "Exponentially better" compares B_i ≈ 2×10^5 with ln B_i ≈ 12 in a worst-case adversarial model; measured gain of RLT is 28.1% (Table 2), and the "worst-case" experiment is a benign cyclic order | Present as asymptotic; add the empirical ratio vs an offline optimum on the traces |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | Section 4.1 | "no dependent algorithm" should read randomized |
| DA-m2 | Citation | Appendix D | "SkyLB" vs the bibliography entry "Skywalker" |
| DA-m3 | Consistency | Appendix B | Table 3 text percentages differ from the table (R1 ERR-2) |
| DA-m4 | Reproducibility | Appendix A | "learning rate of 0.992" for the regression is unusual; confirm the meaning |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Cache-Aware+RLT vs Cache-Aware+LRU, median latency | −28.1% | (26680.55 − 19191.25)/26680.55 = 28.07% | Yes |
| Same, median TTFT | −42.7% | (25022.76 − 14332.81)/25022.76 = 42.72% | Yes |
| LBGR+LRU, median latency / TTFT | −77.4% / −88.2% | 77.41% / 88.18% | Yes |
| LBGR+RLT, median latency / TTFT | 11.8× / 23× | 26680.55/2263.61 = 11.79; 25022.76/1088.57 = 22.99 | Yes |
| Eviction overhead (RLT − LRU) | 0.58 ms (Cache-Aware); 0.96 ms (LBGR) | 0.71 − 0.13 = 0.58; 1.05 − 0.09 = 0.96 | Yes |
| Routing overhead (LBGR − Cache-Aware) | 0.56 ms; 0.94 ms | 1.03 − 0.47 = 0.56; 1.45 − 0.51 = 0.94 | Yes |
| Hit rate, Table 3 | 6.92× | 41.93/6.06 = 6.92 | Yes |
| Throughput, Table 3 | +77.4% | 1.0/0.62 = 1.61 (+61%) | **No** |
| Median TTFT, Table 3 | −47% | 1 − 0.55 = 45% | **No** |
| P95 latency, Table 3 | −45% | 1 − 0.53 = 47% | **No** |
| Throughput, Table 2, LBGR+RLT vs Cache-Aware+LRU | not stated for GSP (Section 5 gives +36.51% averaged) | 11.92/10.73 = +11.1% (GSP only) | Not comparable (different aggregate) |
| P95 latency and TTFT, Table 2 | not stated | 46766.77/15334.89 = 3.05×; 46139.36/11495.05 = 4.01× | n/a |
| Duration of default GSP run | not stated | 4096/12 ≈ 341 s | n/a |

## Ignored Alternative Explanations
- Queue build-up in an overloaded open-loop system could account for most of the median latency and TTFT ratios, independent of eviction or learning.
- LBGR's gain could come from any load-aware estimate (token-count load plus decay) rather than from learning; there is no no-regression ablation.
- The GSP structure (groups of 32 queries with cyclic lengths) lets an online regression exploit regularity that real traffic may not have.
- The round-robin gain for RLT may reflect that any randomized or frequency-aware policy beats LRU on a cyclic scan.
- The hit-rate gains may come partly from routing co-locating same-prefix queries, not from eviction.

## Missing Stakeholder Perspectives
Operators of heterogeneous or multi-tenant clusters, for whom αMISS differs by worker and shared prefix caches raise isolation questions; users whose replies are long (decode-dominated), for whom the 4-token default is not representative.

## Observations (Non-Defects)
Arithmetic in Table 2 and its overhead breakdown is correct. The single-worker experiment (Table 3) is the cleanest isolation of eviction. The disclosure of the character-level tree bias (Appendix E) and the stated worker ceiling (Section 6) are honest. The claim "no randomized algorithm can do better" is a clean statement, even though it follows the classical bound.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Model–algorithm mismatch, proof dependency, unmeasured claimed mechanism |
| Clarity & Presentation | 62 | Readable; mixed headline numbers |
| Novelty & Originality | 52 | Classical analysis; incremental router |
| Significance & Impact | 60 | Plausibly useful; size uncertain |
| Experimental Validation | 44 | Saturated default, single runs, narrow baselines, no balance metric |
| Reproducibility | 62 | Constants given; tuning undisclosed |
| Ethical Compliance | 62 | Nothing at stake; no discussion of shared-cache risks |

## Overall: 3 | Confidence: 4

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claimed mechanism is not measured and headline gains sit in an overloaded regime; a typical accepted systems paper tests its stated mechanism and reports variance.

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

Scores were not changed. The table records what the four tests changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (saturated regime) | kept, rewritten | Added that Figure 5 may address it (unavailable); kept as the paper's text states only "lowest across all request rates" |
| R1 | W5 (LBGR constants) | kept | Appendix searched: no tuning protocol stated |
| R1 | Minor typos | moved to Minor | Cosmetic |
| R2 | W2 (Jaillet not differentiated) | kept | Verified: cited only at Section 1 and Appendix D, not in Section 2 |
| R2 | W3 (Theorem 6 dependency) | kept, confidence Medium noted | Interpretation of what Theorem 4 covers; Lemma 2 is stated for L-LRU |
| R2 | W4 empty-set edge case | rewritten as a question | Suspicion, not located error |
| R2 | W5 citations | kept, one bullet rewritten | "Infinigen" characterization relies on the entry title in the reference list; softened |
| R3 | W3 (more than 10 workers) | rewritten | Authors already state the 10-worker limit in Section 6; reframed around heterogeneity, router bottleneck |
| R3 | W2 (named literature) | rewritten | Names methods only, no unverified citations |
| R4 | "figures dense / hard to read" | moved to Minor | Figures not available; cannot be judged |
| DA | DA-M1 wording "artifact" | rewritten | Softened to "measured where least informative"; Figure 5 not readable |
| DA | DA-m2 SkyLB | kept as Minor | Naming mismatch only |

No weakness was dropped as already answered: the appendix was searched for each (variance, tuning, makespan, baseline configuration).

# Phase 2, Part A: Synthesizer Package

### Master issue list (deduplicated)

| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Saturated, 4-token default; ratios largest at the median | R1-W1, R3-W1, DA-M1 | CONSENSUS-3 (outcome may hinge) |
| I2 | Joint/unified claim exceeds analysis; model and LBGR objective differ | R2-W2, R4-W2, DA-M2, R1-ERR-4 | CONSENSUS-4 (outcome may hinge) |
| I3 | Number reporting: "up to" vs average, 77.4%, Table 3 text, mixed setups | R1-ERR-1/2/3, R4-W1, DA-M4 | CONSENSUS-3 |
| I4 | Narrow baselines; unexplained baseline and LBGR tuning; "state-of-the-art" | R1-W3, R1-W5, R2 (Preble), R3-W2, DA-M5 | CONSENSUS-4 |
| I5 | No variance or repeats (randomized algorithm) | R1-W2, DA (M4/M5 context) | CONSENSUS-2 |
| I6 | Load balance never measured | R1-W4, DA-M2 | CONSENSUS-2 |
| I7 | Theory is classical paging; "exponentially better" is asymptotic only | R2-W1, DA-M6 | CONSENSUS-2 |
| I8 | Theorem 6 proof dependency; OPT comparator unproven | R2-W3 (ERR-5) | SOLO |
| I9 | Theory not tested empirically; benign "worst case" | R1-W6, DA-M6 | CONSENSUS-2 |
| I10 | "Consistently outperform ... all metrics" wording | DA-M3 | SOLO |
| I11 | Citation mismatches | R2-W5, DA-m2 | CONSENSUS-2 |
| I12 | Heterogeneity, burstiness, tenancy, router bottleneck | R3-W3, R3-W4 | SOLO |
| I13 | Generality evidence thin in main text | R4-W3 | SOLO |

**SPLIT:** whether the experiments are "extensive" enough: R3 and R4 lean yes (breadth of sweeps); R1 and DA no (regime, variance, baselines). **DA-CRITICAL:** none raised.

### Official score (before EIC; `scores_before.json`, no EIC weights)

Plain mean of Overall ratings: R1 3, R2 3, R3 4, R4 4, DA 3 → **3.40**. Official composite **60.1** (before-composite). The script reported no warnings. Dimension spreads are all ≤ 16 (none flagged).

---

# Phase 2, Part B: EIC Meta-Review and Decision

# Editorial Decision

## Paper: Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective
## Submission ID: iclr26-R7fv5NWfMm
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: system
## Review Team (fictional personas): EIC (meta-reviewer) Henrietta Okonkwo-Bell; R1 Methodology Kwabena Almeida-Ruiz, R2 Domain Anneliese Torvaldsen-Mehta, R3 Perspective Priyanka Delacroix-Nwosu, R4 Generalist Joon-ho Barrientos, DA Saoirse Lindqvist-Adeyemi

---

## Decision: Borderline Reject (3)

**ICLR rating for this decision** (scale status: secondary; as labeled by the script, not official wording): **4 on {0,2,4,6,8,10}** (5 on {1,3,5,6,8,10}). ICLR sub-scores from the script: Soundness 2, Presentation 3, Contribution 2.

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40** · official composite **60.1**
**EIC assessment** (internal): weighted rating **3.33** → starting point **3** · weighted composite **59.6** → band 3 (cross-check agrees; official composite 60.1 sits on the band-3/4 edge, within 2 points, so the signals are not in conflict) · **DA ceiling**: none · **Final (EIC)**: **3**
**Journal recommendation:** not applicable (conference target).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A relevant problem in a widely used serving stack; a working implementation in SGLang with measured overhead; a clean single-worker isolation of eviction (Table 3) and a component ablation (Table 2); breadth of sweeps (Figures 5–7, 10–14); tight bounds for Leaf-LRU stated and proved.
- **Against acceptance:** The headline latency/TTFT factors are measured in an apparently overloaded, 4-token-output default with single runs; "balances query load" is never measured; the "unified/joint" framing is not backed by a joint result and the theory is a classical paging argument embedded in a tree, with a proof dependency; baselines are one threshold router and L-LRU; several headline numbers are inconsistent with the paper's own tables.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Throughput "+77.4%" does not match Table 3 (0.62 vs 1.0 → +61%) | R1 ERR-1, DA-M4 | Appendix B, Table 3; Abstract | **Verified** | Arithmetic holds; normalization not stated, so confidence stays Medium; the hit-rate ratio 6.92 is correct |
| Table 3 text percentages (47%, 45%) differ from the table (0.55 → 45%, 0.53 → 47%) | R1 ERR-2, DA-m3 | Appendix B | **Verified** | Minor |
| Abstract "up to" 11.96×/14.06× are averages in Section 5 | R1 ERR-3, DA-M4 | Abstract; Section 5 "End-to-End Performance" | **Verified** | Both locations read |
| Saturated default: baseline 10.73 vs 12 requests/s; 4 output tokens; P95 ratios far smaller | R1-W1, R3-W1, DA-M1 | Table 2; Section 5 "Workloads"; Appendix A | **Partly correct** | The numbers are verified; "artifact" (DA) is Overstated, since Figure 5 (rates 4–20) is said to show the same ordering and I could not read it; the headline ratios are certainly not steady-state values |
| Makespan never evaluated | R1-W4 | Sections 1, 3, 3.1 only (text search) | **Verified** | No load-balance metric anywhere |
| No seeds, repeats or variance | R1-W2, DA | Whole text (search) | **Verified** | |
| Theorem 6 proof uses Theorem 4 (L-LRU) | R2-W3, ERR-5 | Appendix C.2 | **Partly correct** | Dependency is real; result for L much smaller than B_i is unaffected, parameterization in B_i − L is not established |
| Theorem 8 is the classical paging lower bound in disguise | R2-W1 | Appendix C.2, construction of Theorem 8 | **Verified** | B_i − L + 2 paths sharing an (L − 1)-prefix; reduces to classical paging with k = B_i − L + 1 |
| Jaillet et al. cited only generically, not differentiated | R2-W2 | Section 1; Appendix D; reference list | **Verified** | Not in Section 2 |
| Preble missing | R2 Missing References | Reference list | **Partly correct** | Absence from the reference list verified; relevance is from reviewer knowledge, literature check unavailable, `[verify]`; at most a MAJOR positioning issue |
| LBGR optimizes a different objective than Section 3.1 | R1 ERR-4, R2-W2, DA-M2 | Equation 2; Section 4.2; Algorithm 2 | **Verified** | Cumulative vs decayed load |
| "Consistently outperform … all metrics and settings" vs throughput convergence | DA-M3 | Section 5 "Number of Workers" | **Verified** | The text itself says throughput converges at 6+ workers |
| 70B/Mixtral generality shown in main text only on ShareGPT | R4-W3, R3 (S3 wording) | Figure 3; Appendix B | **Verified** | The larger factors are in Appendix B as averages |
| "n" undefined in O(n)/O(log n) of Section 1 | R4-W2 | Section 1 | **Verified** | |
| Citation mismatches (Vaswani for KV caching; Infinigen/Llumnix as routing works; SkyLB vs Skywalker) | R2-W5 | Section 1; Section 2; Appendix D | **Partly correct** | The name mismatch and the Wu et al. entry are directly checkable; the characterization of Llumnix and Infinigen rests on their titles in the reference list |

**Errors and integrity.** MAJOR error-log entries ERR-1, ERR-3, ERR-4, ERR-5 were checked at their locations (verified or partly verified as above). No integrity signal was found; no reviewer-directed text was found by the scan or by reading.

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Recomputations and the missing-makespan and no-variance findings verified; one soft point (W6) |
| R2 (Domain) | 3 | 4 | **1.0** | Classical-reduction and joint-claim points verified; Theorem 6 gap real but smaller than worded; novelty verdicts partly from knowledge |
| R3 (Perspective) | 4 | 3 | **0.75** | Accepts "validated across scales" although the main text covers 70B/Mixtral on one benchmark; the saturation point is good but does not feed its score; largely generic deployment items |
| R4 (Generalist) | 4 | 4 | **1.0** | Verified clarity points (undefined n, mixed setups); well calibrated to the venue |
| DA | 3 | 4 | **1.0** | Arguments survived the check; wording "artifact" overstated, counterbalanced by verified numerical findings |

### DA-CRITICAL Rulings

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

The DA's strongest counter-argument (regime and attribution) was treated as a MAJOR issue: the evidence supports a narrower claim (a gain over SGLang's router in the tested regime), it does not contradict it.

### Final Decision and Justification

The EIC-weighted rating is 3.33, so the starting point is **3** (Borderline Reject); the weighted composite 59.6 falls in the same band (the official composite 60.1 is 0.1 above the band edge, which is the near-boundary case the standards describe, so no conflict). I keep the starting point and name no departure: no verified issue is missing from the ratings, and no low rating rests on a point the paper answers. My pool position is **57** (better than about 57% of ICLR submissions), on the reject side of the borderline range: the deciding evidence is that the paper's central mechanism claim ("learning balances query load") is unmeasured, the headline factors come from an apparently overloaded 4-token default with single runs and are mixed up in their reporting (ERR-1, ERR-3), and the "joint/unified" framing rests on a model that is analyzed only for single-worker eviction with a classical argument. The theory is correct in spirit, the system is real and the gains are probably genuine in the tested regime, so this is a close call; what moves it below the line is that the missing evidence (sub-saturation behaviour, repeats, a load-balance measurement, a stronger routing baseline) is exactly what a reader needs to know whether the claimed effect survives, and most of it is cheap to produce. No upheld DA-CRITICAL issue, so there is no ceiling; the decision does not exceed any ceiling. A revised version with those experiments and narrowed claims would plausibly be a Borderline Accept or higher.

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate.json`, venue `iclr`, `--final 3`)

Reviewer weight table:

| Reviewer | Composite | Overall | Confidence | Conf. weight | EIC weight | Weight share | Pool position |
|----------|-----------|---------|------------|--------------|------------|--------------|---------------|
| R1 (Meth.) | 57.2 | 3 | 4 | 0.85 | 1.25 | 0.257 | 52 |
| R2 (Domain) | 60.1 | 3 | 4 | 0.85 | 1.00 | 0.205 | 55 |
| R3 (Persp.) | 65.2 | 4 | 3 | 0.70 | 0.75 | 0.127 | 70 |
| R4 (Gen.) | 63.4 | 4 | 4 | 0.85 | 1.00 | 0.205 | 66 |
| DA | 54.6 | 3 | 4 | 0.85 | 1.00 | 0.205 | 48 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 55 | 60 | 64 | 62 | 50 | 58.2 | 57.6 | 14 |
| Clarity & Presentation | 62 | 64 | 68 | 66 | 62 | 64.4 | 64.0 | 6 |
| Novelty & Originality | 55 | 52 | 62 | 60 | 52 | 56.2 | 55.7 | 10 |
| Significance & Impact | 62 | 62 | 72 | 68 | 60 | 64.8 | 64.1 | 12 |
| Experimental Validation | 48 | 55 | 60 | 58 | 44 | 53.0 | 52.2 | 16 |
| Reproducibility | 60 | 65 | 68 | 68 | 62 | 64.6 | 64.1 | 8 |
| Ethical Compliance | 65 | 66 | 62 | 64 | 62 | 63.8 | 64.0 | 4 |
| **Composite** | 57.2 | 60.1 | 65.2 | 63.4 | 54.6 | **60.1** (before) | **59.6** (after) | |

Official rating (plain mean) 3.40; EIC-weighted rating 3.33. No dimension spread above 20, so no ⚠.

### Target-Venue Scores (ICLR, scale status: secondary; labels are not official wording)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating for final Overall 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

Cross-venue outlook: not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective" to ICLR.

The paper addresses a timely problem: prefix-cache eviction and request routing in multi-worker LLM serving. It combines a formal analysis of leaf-LRU, a randomized eviction rule, and a learned latency-estimating router implemented inside SGLang.

**Overall Assessment:** The panel saw a relevant, implemented system with measured overhead and wide sweeps, and a formal analysis stated tightly. The panel's concerns were about what the evidence establishes: the strongest numbers come from an apparently overloaded default, the load-balance mechanism is not measured, and the unified/joint framing is broader than the single-worker analysis.

**Key Strengths Identified by Reviewers:**
1. A real implementation in a widely used serving stack, with measured per-query overhead (R1, R3, R4).
2. Component decomposition (Table 2) and a clean single-worker isolation of eviction (Table 3) (R1, R2, R4).
3. Tight upper and lower bounds for leaf-LRU and a matching lower bound for randomized eviction (R2).

**Key Concerns Requiring Attention:**
1. Headline gains measured in a saturated, 4-token-output default; sub-saturation and longer outputs not shown (R1, R3, DA; CONSENSUS-3).
2. "Unified/joint" claims exceed the single-worker analysis; LBGR optimizes a different objective than the model; load balance is never measured (R2, R4, DA, R1; CONSENSUS-4).
3. Headline numbers are inconsistent or mix setups (77.4% vs Table 3; "up to" vs average) (R1, R4, DA; CONSENSUS-3).
4. Single runs for a randomized algorithm; narrow baselines (one threshold router, L-LRU only); unexplained constants (R1, R2, R3, DA).
5. The theory re-instantiates classical paging results and needs positioning; one proof step depends on a statement proven for a different algorithm (R2).

**Devil's Advocate:** no CRITICAL issue was raised. Its strongest objection (attribution of the gain and the operating regime) was treated as a major issue.

**Decision: Borderline Reject (3)** (ICLR rating 4 on {0,2,4,6,8,10}, secondary scale)

The reasons to reject outweigh the reasons to accept by a small margin, mostly because the evidence that would settle whether the claimed effect survives (sub-saturation load, repeats, balance measurement, a stronger routing baseline) is absent and cheap to add. Please refer to the Revision Roadmap below. This is a simulation of how a careful panel would likely see this draft, not a prediction of the outcome.

Sincerely,
Henrietta Okonkwo-Bell
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)

| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Saturated, 4-token default; headline ratios not steady-state | R1, R3, DA | CONSENSUS-3 |
| Unified/joint claim exceeds analysis; model–algorithm mismatch | R2, R4, DA, R1 | CONSENSUS-4 |
| Headline number reporting inconsistent | R1, R4, DA | CONSENSUS-3 |
| Narrow baselines and unexplained tuning | R1, R2, R3, DA | CONSENSUS-4 |

### Points of Disagreement

| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Experiments are "extensive" enough | R3, R4 | R1, DA | Breadth is real, but the weaknesses are in regime, variance, baselines and the unmeasured mechanism; the EIC sides with R1/DA on what is missing, and weights R3 down for accepting generality that the main text shows only on one benchmark |
| Severity of the theory gap | R2 (MAJOR), DA (M6) | R3, R4 (not raised) | Positioning issue and a proof dependency, MAJOR at most; does not alone decide |

### Score Spread Discussion
No dimension exceeded the 20-point spread. The widest, Experimental Validation (44–60), separates R1/DA (regime, variance, baselines) from R3/R4 (breadth); the editor adopts the lower view for the reasons above.

### Devil's Advocate Highlights

| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Saturated regime | Yes (R1, R3) | n/a | n/a |
| DA-M2 | MAJOR | Unified/joint overreach | Yes (R2, R4, R1) | n/a | n/a |
| DA-M3 | MAJOR | "Consistently … all metrics" wording | No | n/a | n/a |
| DA-M4 | MAJOR | Aggregation and numbers | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Baselines/tuning | Yes (R1, R2, R3) | n/a | n/a |
| DA-M6 | MAJOR | "Exponentially better" asymptotic only | Partly (R2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (must fix; issues the EIC verified as undermining a main claim)

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline gains in a saturated, 4-token default | R1-W1, R3-W1, DA-M1 | Table 2, Section 5 "Workloads", Appendix A | Load sweeps below and at saturation, 128–512 output tokens, goodput at SLO, in the main text | Medium; about 2–4 GPU-days on the existing cluster | Yes (partly) |
| R2 | "Balances query load" unmeasured; LBGR objective differs from the model | R1-W4, R1-ERR-4, R2-W2, DA-M2 | Sections 3.1, 4.2; Table 2; Figure 6 | Report per-worker load and makespan; narrow "unified/joint" claims or add a joint result | Low–Medium | Yes |
| R3 | Inconsistent headline numbers (77.4%, "up to" vs average, Table 3 text) | R1-ERR-1/2/3, R4-W1, DA-M4 | Abstract; Section 5; Appendix B; Table 3 | Correct numbers; table of per-benchmark raw values; state the setup beside each abstract figure | Low | Yes |
| R4 | No variance for a randomized algorithm | R1-W2, DA-M4 | Tables 2, 3; Figures 5–7 | Five repeats, mean ± std or CI; shaded bands | Low–Medium (hours) | Yes |

### Priority 2: Strongly suggested (should fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Narrow baselines; baseline and LBGR tuning undisclosed | R1-W3, R1-W5, DA-M5, R3-W2 | Tuned linear-score router, bounded-load or power-of-two router, one non-recency eviction policy; disclose tuning | Medium–High | Partly |
| S2 | Missing positioning: scheduling-with-KV-constraints work, prompt-scheduling systems, learning-augmented caching (all `[verify]`) | R2-W1, R2-W2, Missing References | Add differentiation paragraph and, where applicable, comparisons | Low–Medium | Yes (text) |
| S3 | LBGR ablations (no regression, no decay, token-count load); define subroutines | R1-W5, R4-W1 | Add ablation rows and appendix pseudo-code | Low–Medium | Yes |
| S4 | Theory: state the paging reduction; fix the Theorem 6 dependency; OPT optimality; define n | R2-W1, R2-W3, R4-W2 | Prove stale-token bound for RLT or state Θ(log B_i); define n | Medium (analysis) | Partly |
| S5 | Theory untested; benign "worst case" | R1-W6, DA-M6 | Empirical ratio vs offline optimum; evaluate the Theorem 4 lower-bound sequence | Medium | Yes |
| S6 | "Consistently outperform … all metrics" wording | DA-M3 | "Matches or exceeds"; state ties | Low | Yes |
| S7 | Generality shown on one benchmark in the main text | R4-W3 | 70B/Mixtral on all four benchmarks in the main text or a table | Low (data exist in Appendix B) | Yes |
| S8 | Citation mismatches | R2-W5, DA-m2 | Re-check Vaswani, Llumnix, Infinigen, Wu et al., SkyLB/Skywalker | Low | Yes |

### Priority 3: Nice to fix (optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Heterogeneous workers, bursty arrivals, router bottleneck beyond 10 workers | R3-W3 | Add one heterogeneous experiment or state as a limit |
| N2 | Multi-tenant cache side channels | R3-W4 | Short discussion of per-tenant isolation |
| N3 | Typos ("no dependent algorithm", "Mixtral-8×B", baseline numbering), meaning of "learning rate of 0.992" | R1, DA-m1/m4 | Fix |
| N4 | Edge case: can U in Algorithm 1 line 14 be empty? | R2-W4 | Add a one-line argument |

---

## Estimated Revision Effort
- Priority 1: 4 items, about 1–2 weeks (new load sweeps, repeats, balance metrics, text corrections).
- Priority 2: 8 items, about 2–3 weeks (baselines, ablations, proof fix).
- Priority 3: 4 items, about 2–3 days.
- **Total estimated revision time**: about 3–5 weeks, of which most is compute and running baselines.

---

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
