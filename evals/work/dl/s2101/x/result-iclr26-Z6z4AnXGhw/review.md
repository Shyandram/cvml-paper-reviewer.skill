# Academic Paper Review: "Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization"

*Simulated panel review, full mode, target venue ICLR (stated by user), literature check: strict, cutoff 2025-09-24. Date: 2026-11-05. The outcome is a simulation of how a careful panel would likely see this draft, not a prediction. Figures were not available (text extraction only): figure-dependent claims are judged from captions and text and flagged. The five reviewer passes shared one model context; they were run one after another from their own role files and did not see each other's reports. No subagents were used.*

---

## Phase 0: Field Analysis and Reviewer Configuration

### Paper Analysis

| Item | Finding |
|------|---------|
| Title | Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization |
| Primary Discipline | Evolutionary computation → quality-diversity optimization |
| Secondary Discipline(s) | Meta-learning / learned optimizers (meta-black-box optimization, evolution strategies); neuroevolution and robotics control (Brax) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Transformer (4 layers, 16 features, 4 heads, ≈5,000 parameters) as a learned "competition function" over (fitness, descriptor); meta-optimized with Sep-CMA-ES on BBOB functions; compared with MAP-Elites, Dominated Novelty Search, GA, Novelty Search |
| Target Venue | ICLR, top-tier conference (stated by user); profile key `iclr`. The manuscript is typeset in the ACM `acmart` style (CCS concepts, keywords, template dates), not the ICLR style; recorded, not scored |
| Venue-Specific Notes | None (no ECCV/ACM-MM/TPAMI-type rules apply). ICLR form: Soundness / Presentation / Contribution (1–4), Rating, Confidence. Accepted share ≈ 27% of submissions |
| Paper Maturity | Submission-ready draft with notable evaluation gaps |
| Ethics-Relevant Content | None (synthetic benchmarks and simulated robots) |

**Integrity scan** (`integrity_scan.py`): no reviewer-directed text and no hidden characters found. The reviewers read the (unchanged) redacted copy. **Injection found: none.** Similarity check (below, Phase 1.5) found two shared generic 8-grams with a cited prior paper; it is reported to the EIC as a factual note only.

### Claimed Contributions (as stated by the authors, Section 1)
1. **C1**: Learned Quality-Diversity (LQD), "a flexible framework that can represent any QD algorithm" by parameterizing the competition function with a transformer (Sections 1, 4.1).
2. **C2**: Learned algorithms "match or exceed the performance of established baselines" such as MAP-Elites and Dominated Novelty Search (Section 1; Sections 5.2–5.3).
3. **C3**: Strong generalization to higher dimensions, larger populations and robot control (Sections 5.2–5.3, Figures 4–6).
4. **C4** (analysis claim): Even when meta-trained for fitness only, LQD "naturally" maintains diversity, "rediscovering" that diversity is an instrumental goal (Section 6.1, abstract, conclusion).

### Paper memory (factual record shared with all reviewers)

- **Setup facts.** Meta-task: 22 BBOB functions (Table 2), dimension 2–12, noise models (uniform, Gaussian, Cauchy), random rotations; descriptors from a random matrix `d_i = N x_i` (Section 4.2.1, D not stated). Meta-ES: Sep-CMA-ES, σ_init 0.1, M = 256, K = 256, 16,384 meta-generations; inner loop N = 128, B = 32, T = 256 generations (Table 1, Section 4.2.3). Three objectives: fitness, novelty, "QD score" = "maximum fitness multipled by the average" dominated novelty score (Section 4.2.2). Parameter set chosen by the "held-out tasks" used for validation (Section 4.2.3; the validation tasks are not defined). Evaluation: 32 replications; Wilcoxon–Mann–Whitney U with Holm-Bonferroni correction (Section 5). Hardware: 8 H100 GPUs, wall-clock not stated.
- **Not stated after search:** the reproduction operator (only "mechanisms like crossover and mutation", Section 3.2); baseline hyperparameters (ME grid size/centroid count and descriptor bounds, k of NS and DNS, mutation settings); descriptor dimension D during training; population size and generation count for the robot runs; number of independent meta-training runs; validation-task definition; wall-clock or FLOP cost of LQD vs baselines; code availability; a limitations section.
- **Headline numbers:** p < 10⁻⁹ (LQD(N) vs NS novelty), p < 10⁻¹⁰ (LQD(F) vs GA fitness), p < 10⁻⁷ (LQD(F+N) vs ME novelty), all on the meta-training tasks (Section 5.2, Figure 3); robot aggregate "p < 0.005" against all baselines except GA (Section 5.3, Figure 1); "approximately 40%" of ME's novelty for LQD(F) on Walker2d vs "less than 10%" for GA (Section 6.1, Figure 7).
- **Appendix adds:** Table 1 hyperparameters, Figure 10 (meta-training-task results), Figure 11 (descriptor ablation, six robot tasks), Tables 2–4 (task lists; Table 4 lists six robot rows with genotype sizes 8–584).
- **Unverifiable:** all figures (bars, heatmaps, curves, aggregate Figure 1) were read from captions only.

### Review Team (fictional personas)

**EIC (meta-reviewer): Prof. Katarzyna Wójcik-Almeida**, large public research university (Europe). Senior faculty; evolutionary computation, ML optimization. Role: reads all five reviews, checks decisive points, weights reviewers, decides. Style: serves as area chair; asks what the evidence supports, not what the title promises.

**Reviewer 1 (Methodology): Dr. Anand Subramaniyan**, industrial research lab (South Asia). Mid-career industry scientist; benchmarking of evolutionary and black-box optimizers, learned optimizers. Focus: design, comparison fairness, statistics, reproducibility. Style: insists on tuned, compute-matched baselines.

**Reviewer 2 (Domain): Prof. Elodie Marchetti**, research university (Southern Europe). Senior faculty; quality-diversity, novelty search, illumination algorithms. Focus: literature, theory, domain contribution. Style: checks every "rediscovered" and "first" against the literature.

**Reviewer 3 (Perspective): Dr. Kwame Boateng-Lindholm**, theoretical-ecology and complex-systems institute (Northern Europe / West Africa). Mid-career; evolutionary biology, niche theory, AutoML. Focus: cross-disciplinary links, assumptions, broader impact. Style: constructive and expansive.

**Reviewer 4 (Generalist): Dr. Mei-Ling Okafor**, ML department, large university (North America). Mid-career; deep learning and RL, not QD. Focus: contribution clarity, venue fit, presentation. Style: typical program-committee member; reads for the main claim and its evidence.

**Devil's Advocate: Prof. Rafael Ostrowski-Tan**, statistics and evaluation-methodology group (Latin America). Senior faculty; experimental design, causal inference for ML. Focus: core argument, overclaiming. Style: rigorous, never hostile.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reviews

# Peer Review Report: Reviewer 1 (Methodology)

## Paper: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization
## Reviewer: Dr. Anand Subramaniyan, Methodology (industrial research lab, South Asia; fictional persona)
## Expertise: benchmarking of black-box optimizers; learned optimizers; evaluation of evolutionary algorithms
## Date: 2026-11-05

### Summary
The paper replaces the fitness-adjustment ("competition") step of a genetic algorithm with a small permutation-equivariant transformer that maps standardized (fitness, descriptor) rows to a scalar used for top-N truncation. Its ≈5,000 parameters are meta-trained with Sep-CMA-ES over 22 noisy, rotated BBOB functions, with descriptors produced by random linear projection of the genotype. Three meta-objectives (fitness, novelty, a product "QD score") give three variants. These are compared with GA, NS, ME, DNS and a random-selection control on training functions, six out-of-distribution functions, a population-size/dimension sweep, and robot-control tasks.

### Strengths
**S1: Clean, minimal formulation.** Only the competition function is learned (Algorithm 3), so the experiment isolates one component and keeps the rest of the GA loop fixed. This is an easy design to reason about.
**S2: A useful control for descriptor use.** Section 6.3 / Figure 9 and Figure 11 compare LQD with task descriptors, LQD with random descriptors and GA. The random-descriptor curve returns to GA level. This is the one experiment that probes *why* LQD works, and it points toward descriptor use.
**S3: Replication and testing basics are present.** 32 seeds, non-parametric tests with Holm-Bonferroni correction (Section 5) and shaded 95% CIs on robot curves (Figures 6, 7, 9). Honest negative result: LQD(F+N) does not match DNS (Section 5.2; conclusion).
**S4: A genuinely out-of-distribution transfer test.** Moving from 2–12-dimensional BBOB with N = 128 to 584-parameter Brax policies with semantic descriptors is a large shift (Section 5.3, Table 4).

### Weaknesses
**W1: Baselines are untuned and underspecified while LQD received an enormous tuning budget.** The meta-training loop runs 16,384 × 256 × 256 ≈ 1.07×10⁹ inner-loop runs of 256 generations each (Section 4.2.3, Table 1), on the order of 10¹³ function evaluations (derived). The baselines' hyperparameters (ME grid resolution and descriptor bounds on random-projection spaces, k for NS and DNS, mutation scale, the shared reproduction operator) are not given anywhere (Section 5.1; Algorithm 1 says only "mechanisms like crossover and mutation"). With the in-distribution comparison in Figure 3 (e.g., LQD(N) vs NS, p < 10⁻⁹), "meta-learning beats the baselines" cannot be separated from "tuned beats untuned". The novelty comparison is also against the very metric that LQD(N) is trained on. *Fix:* state all baseline settings and give GA, NS, ME and DNS a comparable tuning effort on the same meta-training distribution (e.g., a random or CMA-ES search over k, mutation scale and grid size with the same evaluation budget, ≈ 1–2 GPU-days on the stated 8 H100s). Report the result next to Figure 3.
**W2: The generalization claim in Figure 5 uses training functions, one baseline and one variant.** The sweep over population sizes (64–1024) and dimensions (2–32) shows only Schaffers F7 and Katsuura, and both appear in the meta-training set (Table 2). Only LQD(F) vs ME is plotted, not GA or DNS. The text concludes the rules "capture fundamental principles that generalize" far beyond their training conditions (Section 5.2). Scaling in N and D is out-of-range, but not out-of-distribution in function class. *Fix:* repeat the sweep on the held-out Gallagher functions and the four Jamil–Yang functions (Table 3), include GA and DNS, and report the plotted quantity's units (the colorbar is unlabeled in the caption). ≈ 0.5 GPU-day.
**W3: Evaluation metrics do not test the "QD" claim and are not comparable across algorithms.** The robot results (Figure 6) report only "Fitness" and LQD(F) is the only variant used; diversity appears in Figure 7 for two tasks as novelty normalized to ME. Standard QD measures (archive QD score, coverage) are absent, and the authors themselves note that ME's "partially-filled populations" can inflated novelty (Section 5.2), yet Section 6.1 then normalizes diversity to ME. The BBO "QD score" is a non-standard product of max fitness and mean dominated novelty on a 128-member population (Section 4.2.2). Because the QD baselines are not optimizing max fitness, a fitness-only variant beating them says little about QD quality; the aggregate shows it is not distinguishable from GA (the gain over GA is reported as not statistically significant, Section 5.3). *Fix:* report archive-based QD score and coverage (with a common descriptor discretization applied post hoc to all methods), for LQD(F), (N) and (F+N), on the robot tasks and BBO. Mostly re-analysis of stored populations if archives were logged, otherwise ≈ 1 GPU-day.
**W4: Statistical reporting covers inference runs of one learned algorithm, not the learning procedure.** "we conduct 32 independent replications of each" (Section 5) vary the inner-loop seed. How many independent meta-training runs exist, how the "best-performing parameter set" was chosen, and what the "held-out tasks" for validation are, is not stated (Section 4.2.3). If validation used the same six out-of-distribution functions that are later reported (Table 3), the OOD results would be selected on; this cannot be determined from the text. The aggregation behind Figure 1 and "p < 0.005" (how tasks and seeds are pooled) is not described. *Fix:* report ≥ 3 meta-training seeds per variant with the spread of the downstream scores, define the validation set, and describe the aggregation. 3 × the meta-training cost.
**W5: The Johnson–Lindenstrauss justification does not apply as stated.** Section 4.2.1 says the lemma "random projections approximately preserve" pairwise distances with high probability. The lemma gives guarantees when the target dimension is of order log N/ε², whereas the genotypes here have n = 2–12 and D is never stated. The descriptors are then a fixed random linear map of the genotype, so "diversity" is genotype-space spread; the training signal never contains a nonlinear or semantic descriptor–fitness relationship, which the robot tasks then do. *Fix:* state D, drop or soften the theoretical claim, and add a training variant with nonlinear random descriptors. Low effort for the first two.

**Minor:** the robot task count is inconsistent (Appendix C.3 "six robotic control tasks implemented in the Brax physics simulator [15] and one arm reaching task" vs Table 4's six rows in total and six panels in Figure 6); template placeholder dates "revised 12 March 2009; accepted 5 June 2009" remain in the final page; "multipled" typo (Section 4.2.2).

### Error Log

| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E8 | Section 3.2, Section 5.1 | "generated through mechanisms like crossover and mutation" | The reproduction operator and every baseline hyperparameter are missing; all comparisons depend on them | Protocol sweep (grep: crossover, mutation, centroid, "k =") found nothing further | High | MAJOR | List all settings; add tuned baselines |
| ERR-2 | E4 | Figure 5 caption, Table 2 | "LQD (F) outperforms ME across almost" | The two functions shown (Schaffers F7, Katsuura) are both meta-training functions in Table 2, yet the result supports the claim of generalization far beyond the training conditions | Cross-referenced Figure 5 caption with Table 2 rows | High | MAJOR | Use held-out functions; add GA, DNS |
| ERR-3 | E5 | Section 1 vs Section 5.2 | "advance the state-of-the-art in Quality-Diversity optimization" | The only QD-objective variant is stated to fall short: "LQD (F+N) approaches but does not quite match" DNS | Two locations compared | High | MAJOR | Narrow the claim or add evidence |
| ERR-4 | E3 | Section 4.2.1 | "random projections approximately preserve" pairwise distances with high probability | Lemma regime (target dimension ~ log N/ε²) vs genotype dimension n ≤ 12; D unstated | Derived from the lemma's statement | Medium | MINOR | State D; soften |
| ERR-5 | E6 | Appendix C.3 vs Table 4 | "six robotic control tasks implemented in the Brax physics simulator [15] and one arm reaching task" | Table 4 lists 5 Brax rows and 1 Arm row (6 in total), matching Figure 6's six panels | Counted Table 4 rows | High | MINOR | Fix the text |

### Questions for Authors
1. How many independent meta-training runs exist per variant, and what are the "held-out tasks" used for validation (disjoint from Table 3)? A disjoint validation set and a seed spread would raise Experimental Validation; overlap with Table 3 would lower it substantially.
2. What are the robot-run population size and generation count? a "budget of 1 million evaluations" with B = 32 is ≈ 31,000 generations (derived), versus T = 256 in training. And Figure 6's Arm panel axis is labeled ×10⁴ to 8 rather than ×10⁶ (read from extracted axis text; unverifiable): is the budget the same?
3. How is the fixed-width embedding layer applied to descriptor dimensions that differ between random-projection training and each robot task (Table 4)?
4. How are the ratios "relative to random" in Figures 3, 4 and 10 computed when fitness values can be zero or negative (axes reach 10⁵)?

### Limitations Assessment
**Partially.** The conclusion admits that F+N "remains challenging", but there is no limitations section and the compute cost of meta-training and of the transformer at inference (quadratic in population size) is not discussed.

### Ethics Review Flag
**No**

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Untuned baselines, undefined validation, claims beyond the evidence |
| Clarity | 3 | Readable method, missing operational details |
| Significance | 2 | Useful if the QD claims hold; evidence is thin |
| Originality | 2 | Natural extension of the LES/LGA recipe to QD |

### Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: untuned baselines against a 10¹³-evaluation tuning budget, and generalization shown only on training functions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound formulation; JL misuse; unspecified selection protocol |
| Clarity & Presentation | 62 | Competent | Method clear; key operational details absent |
| Novelty & Originality | 55 | Competent | Incremental over LGA/LES; see R2 |
| Significance & Impact | 52 | Developing | Impact depends on QD claims that are not yet tested |
| Experimental Validation | 46 | Developing | Weak baselines, non-QD metrics, training-function generalization |
| Reproducibility | 42 | Developing | No code, operator and baseline settings missing |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations only briefly discussed |

### Overall Score
**3 (Borderline Reject)**: The idea is interesting and honestly reported in places, but the central comparisons are not controlled well enough to support the stated claims. A tuned-baseline control and a standard QD evaluation would move this up.

### Confidence
**4**: I checked setup statements by text search and recomputed derived figures; figures were not visible.

---

# Peer Review Report: Reviewer 2 (Domain)

## Paper: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization
## Reviewer: Prof. Elodie Marchetti, Domain (research university, Southern Europe; fictional persona)
## Expertise: quality-diversity and illumination algorithms; novelty search; unstructured archives
## Date: 2026-11-05

### Summary
The paper frames a QD algorithm as a GA whose only distinguishing feature is the competition function, replaces that function with a learned transformer, and argues the meta-learned rules both rediscover known mechanisms (novelty search) and yield new fitness-sensitive diversity behavior. It positions itself against grid-based (MAP-Elites) and nearest-neighbor (DNS) competition and against earlier meta-black-box-optimization work on learned GAs and ES.

### Strengths
**S1: A good conceptual unification.** Algorithms 1–2 and Sections 3.3.1–3.3.3 cast GA, ME, NS and DNS as different `competition(f, d)` functions followed by top-N truncation. This is a clean, pedagogically useful view of local competition and the clearest contribution to the QD discussion.
**S2: Right choice of baselines inside the framework.** ME and DNS are the natural population-based competition schemes to compare against (Section 5.1), and the DNS authors' evaluation protocol (competition as the unit) is respected.
**S3: Honest about LQD(F+N).** The paper says that a joint objective "remains challenging" (Section 5.2; conclusion), which is the right reading of its own results.
**S4: Interesting empirical observation.** Fitness-only meta-training producing selection that is descriptor-sensitive (Figure 8, Section 6.3) is a finding the QD community will want to examine, despite the interpretation issues below.

### Weaknesses
**W1: Differentiation from the closest prior work (LGA, LES) is thin and there is no empirical comparison.** Section 2 says "related to our work are LES [30] and LGA [29]" and that "meta-optimize a parametrized Transformer model to discover". The recipe (Section 4.2: "procedure introduced by Lange et al. [29, 30]"), the permutation-equivariant attention and the evaluation functions are shared with LGA, which already meta-learns an attention-based GA operator. What is new is (i) the descriptor input, (ii) QD-style meta-objectives. Neither the delta nor an LGA/LES-style baseline is given. *Fix:* add a delta paragraph and run an LGA-style selection operator (fitness input only) as a baseline and as the "no-descriptor" ablation on BBO tasks.
**W2: "Represents any QD algorithm" and "searching through all archive mechanisms" are not true of this parameterization.** Section 4 says LQD is "a flexible framework that can represent any QD algorithm" and Section 4.1 says it is "effectively searching through all archive mechanisms". The network scores each current population member from standardized (fitness, descriptor) rows (Featurize step, Figure 2); standardization removes absolute descriptor positions (so fixed-centroid grids such as the CVT of ME [48] are not expressible as such), there is no state across generations beyond the population, and the reproduction operator is fixed. Expressivity of a 5,000-parameter network is asserted, not shown. *Fix:* show by construction or distillation that the network can reproduce NS, DNS and ME, or restrict the claim to "population-based fitness-adjustment rules".
**W3: "Discovered novel QD algorithms" is not demonstrated.** Section 6.2 gives qualitative heatmaps (Figure 8): LQD(N) "rediscovering the core principle of novelty search"; LQD(F)'s rule is described as "fitness-sensitive reward patterns around promising solutions"; LQD(F+N) is described as combining the two. No rule is extracted, compared with a hand-designed mechanism, or transferred back into a closed-form algorithm. The result that the only QD-targeting variant (F+N) does not beat DNS is not consistent with "discovering" new state-of-the-art QD mechanisms (see C2 profile below). *Fix:* extract a symbolic or distilled rule for LQD(F) and show that it, not the network, explains the diversity; otherwise recast as "learned selection with descriptor-aware behavior".
**W4: Missing QD comparisons and related work (verified where possible, see addendum).** Baselines omit emitter-based QD methods that are the usual strong competitors in continuous domains, and the paper does not discuss earlier meta-evolution of QD algorithms.

**Minor:** "equivariance" and "invariance" of attention are used interchangeably (Sections 2 and 3.4).

### Literature-check addendum (strict mode, cutoff 2025-09-24)
7 arXiv queries (6 claim, 1 expansion; the baseline query was refused for exceeding the 4-word limit, so there is **no baseline scout table**: the paper's benchmarks are BBOB and Brax tasks, which the script's benchmark list did not detect). 84 kept results; `similarity` over the reviewer copy. Gaps left open: no benchmark scout; the C4 query found no relevant work (arXiv only: not evidence of novelty).

**Per-claim novelty (claim-level profile; `related_search.py novelty`):**

| Claim | Dim. | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|------|---------|---------------------------------------------|-----------|
| C1 learned transformer QD competition | method | medium | LGA, level 3, arxiv.org/abs/2304.03995, prior (arXiv-only), cited | Same meta-BBO recipe and attention-based operator; QD descriptors and QD meta-objectives are the delta |
| C2 match/exceed ME and DNS | result | high | DNS, level 2, arxiv.org/abs/2502.00593, prior (arXiv-only), cited (as a baseline) | Result claim; no prior work reports it |
| C3 generalization | result | medium | LES, level 3, arxiv.org/abs/2211.11260, prior (peer-reviewed), cited | Generalization via attention is shown in LES/LGA; the QD setting is new |
| C4 emergent diversity | result | no close prior work found (at most medium) | none | Search limited to arXiv; niching/fitness sharing [16] are conceptually adjacent |

No claim is established by an uncited prior work, so no "known results" concern. **Attribution:** the paper as a whole sits closest to LGA (script attribution).

**Novelty delta table:**

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C1 | LGA (2304.03995) | Meta-learns an attention-based GA operator over fitness with the same meta-ES recipe | Descriptor input; QD-style competition and meta-objectives | Cited; differentiation weak (Section 2) |
| C1 | QD meta-evolution (Bossens & Tarapore, arXiv 2109.03918) | Meta-evolves components of a QD algorithm (the behaviour space) against a meta-objective | Learns the competition rule rather than the behavior space | **Not cited** |
| C2 | DNS (2502.00593) | The QD baseline; local competition by distance to fitter neighbors | n/a (baseline) | Cited |

**Field snapshot (from kept results, ≈170 words).** Three to five years ago, meta-black-box optimization learned optimizers for low-dimensional BBO (meta-learned RNN optimizers, step-size control) and then attention-based GA/ES operators (LES, 2022; LGA, 2023). Kept 2024–2025 results show the area moving toward benchmark platforms (MetaBox and MetaBox-v2), learned landscape features, surrogate learning, and LLM-assisted algorithm generation (one concurrent preprint within 60 days of the cutoff: worth discussing only). In QD, recent work targets local competition itself (DNS, 2025) and limited-resource archives (2024). Open problems stated by recent work: generalization of learned optimizers across problem classes and compute-efficiency. What counts as a significant contribution here now: a learned rule that clearly beats well-tuned strong baselines on standard QD metrics, or a rule that can be extracted and understood. A new combination of existing parts with fitness-only gains is incremental.

**Text-overlap flag (for the EIC, factual only):** `similarity` found 2 shared 8-grams with LGA (a cited prior paper that shares an author with this paper): a generic "fundamentally different approach" sentence and the same generic sentence. This is generic phrasing, shown for completeness; it is not treated as a concern about content. `similarity` also flagged DNS for high conceptual overlap (cosine 0.494); DNS is the cited baseline whose abstract frames QD as local competition, so this is expected.

### Missing References

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | D. M. Bossens and D. Tarapore, "Quality-Diversity Meta-Evolution: customising behaviour spaces to a meta-objective", 2021 (arXiv 2109.03918, found by `verify`/search) | Prior meta-optimization of a QD algorithm; must be differentiated |
| Important | M. C. Fontaine, J. Togelius, S. Nikolaidis, A. K. Hoover, "Covariance Matrix Adaptation for the Rapid Illumination of Behavior Space", GECCO 2020 (arXiv 1912.02400, found) | Standard emitter-based QD method for continuous domains; strong fitness+QD comparison |
| Important | M. C. Fontaine and S. Nikolaidis, "Covariance Matrix Adaptation MAP-Annealing", GECCO 2023 (arXiv 2205.10752, found) | Successor of CMA-ME; the standard strong QD baseline in QDax-style benchmarks |
| Important | Z. Ma et al., "MetaBox: A Benchmark Platform for Meta-Black-Box Optimization with Reinforcement Learning", NeurIPS 2023 Datasets & Benchmarks (arXiv 2310.08252, found, peer-reviewed label) | Standard platform and baselines for MetaBBO; positions the evaluation |
| Helpful | Nilsson and Cully, "Policy Gradient Assisted MAP-Elites", GECCO 2021 `[verify]` (not found on arXiv by title) | Strong robot-control QD baseline, relevant to Section 5.3 |
| Helpful | Metz et al., "VeLO: Training Versatile Learned Optimizers by Scaling Up", 2022 (arXiv 2211.09760, found) | Learned optimizer at scale; relevant to the compute-cost discussion |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claim-evidence gaps (see R1) |
| Clarity | 3 | Good unified framing |
| Significance | 2 | Depends on a QD advantage that is not shown |
| Originality | 2 | Medium novelty at claim level (C1), thin differentiation |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the method is a medium-novelty extension of LGA, and the QD-targeting variant does not beat the strongest QD baseline.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Principled setup; "any QD algorithm" claim unsupported |
| Clarity & Presentation | 65 | Competent | Clear unified framing |
| Novelty & Originality | 52 | Developing | Medium at C1; unclear delta vs LGA; missing QD meta-evolution citation |
| Significance & Impact | 55 | Competent | Interesting direction, narrow evidence |
| Experimental Validation | 52 | Developing | Few QD baselines; non-QD metrics |
| Reproducibility | 50 | Developing | Settings missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

### Questions for Authors
1. What is the concrete difference from LGA beyond the descriptor input, and how does an LGA-style operator (fitness only) perform on your BBO tasks? A strong answer with numbers would raise my Novelty score.
2. Can the network (as parameterized) reproduce ME's fixed-centroid competition after standardization? If not, which QD algorithms can it represent?
3. Why are CMA-ME / CMA-MAE absent from the baseline set for the robot tasks?

### Limitations Assessment
**Partially.** See R1.

### Ethics Review Flag
**No**

### Overall Score
**3 (Borderline Reject)**: A nicely framed idea at medium novelty over LGA, whose main empirical claim (beating QD baselines) is not yet convincing.

### Confidence
**4**: Familiar with QD baselines; literature facts were checked with the search tool where possible.

---

# Peer Review Report: Reviewer 3 (Perspective)

## Paper: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization
## Reviewer: Dr. Kwame Boateng-Lindholm, Perspective (theoretical-ecology and complex-systems institute; fictional persona)
## Expertise: niche theory and speciation; evolutionary dynamics; AutoML
## Date: 2026-11-05

### Summary
The authors ask whether the competition rule at the heart of QD algorithms can be learned rather than designed. A tiny attention network assigns each individual a competition score from its fitness and its position in a behavior-descriptor space; training on abstract optimization tasks yields rules that transfer to physics-simulated robots. A recurring finding is that a rule trained only to maximize fitness also keeps a more diverse population than a plain GA.

### Strengths
**S1: A compelling bridge to ecology.** The introduction ties local competition to niche structure and "stepping stones" (Section 1). The finding that fitness-only training yields selection that depends on neighbors (Sections 6.1–6.2, Figure 8) echoes classic ecological results on niche partitioning and crowding.
**S2: Transfer beyond the training regime.** The same ≈5,000-parameter network, trained on 2–12-dimensional functions with random-projection descriptors, runs on Brax policies with up to 584 parameters and semantic descriptors (Section 5.3, Table 4). That is non-trivial and rarely shown for learned evolutionary operators.
**S3: Scaling in population and dimension.** Figure 5 reports gains growing with population size and dimension on two functions, relevant to practical large-scale use (read from the caption and text).
**S4: Tiny, cheap-to-deploy model.** A learned selection rule with ≈5,000 parameters (Appendix B) could be plugged into existing QD libraries (QDax is already used, Section 5).

### Weaknesses
**W1: The "diversity as an instrumental goal" story needs an ecological control.** In ecology, diversity under competition is shown by removing the mechanism. Here Section 6.1 compares novelty of LQD(F) with GA and ME, and the conclusion states "meta-learning rediscovers diversity as an instrumental goal for achieving peak performance". A GA with a diversity-preserving but non-learned mechanism (fitness sharing or crowding, both cited in Section 2 [16], or lower selection pressure) is the natural comparison and is missing. *Fix:* add fitness-sharing and tuned-GA baselines in Figure 7; show that the learned rule's performance advantage disappears when its descriptor sensitivity is removed (a stronger form of Section 6.3).
**W2: Assumption: descriptors encode useful stepping stones.** In training the descriptor is a fixed random linear projection of the genotype (Section 4.2.1), so "neighbors in descriptor space" are neighbors in a rotated genotype space; on robots the descriptors are behavioral. The paper's reading that the rules exploit that it exploits meaningful relationships captured by the descriptor space (Section 6.3) is plausible but the ablation feeds standard-normal noise at test time, an input the network never saw in training. *Fix:* use a descriptor-shuffling control (permute descriptors across individuals within a population) so that the input distribution stays in range.
**W3: Deployment realism.** Cost of the learned rule is not reported: the transformer is quadratic in population size, and meta-training used 8 H100 GPUs (Section 5); the net benefit for a practitioner (wall-clock to a given fitness) is not shown. *Fix:* add a wall-clock and evaluation-matched comparison; discuss when the meta-training cost amortizes.
**W4: Other directions.** Interesting extensions: unsupervised or learned descriptors (AURORA-style, already cited as [7, 18]), multi-objective and open-ended settings, and comparison with niche-based dynamics from theoretical ecology.

**Minor:** the paper has no explicit limitations or societal-impact paragraph; for a benchmark-optimization paper this is a low-severity point.

### Questions for Authors
1. Does the learned rule with shuffled descriptors (not noise) still show diversity? Persistence would indicate diversity arises from the rule's fitness dependence, not descriptor structure.
2. What does the rule do as a function of local density of *fitter* neighbors, in a one-dimensional toy setting? A simple summary statistic would make Figure 8 interpretable.
3. How does wall-clock per generation compare with ME and DNS at N = 1024?

### Limitations Assessment
**Partially.** Same as R1; the limitation that fitness-trained rules are tested without QD-specific metrics is not discussed.

### Ethics Review Flag
**No**: Simulated and synthetic benchmarks only; no dual-use or data concern.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid core, gaps in controls |
| Clarity | 3 | Clear narrative |
| Significance | 3 | Interesting for evolutionary computation and AutoML |
| Originality | 3 | New use of meta-learning for QD |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a creative, well-motivated direction with a non-trivial transfer result; weaknesses are of the kind many accepted papers share.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound core with unexamined assumptions |
| Clarity & Presentation | 68 | Competent | Easy to follow |
| Novelty & Originality | 64 | Competent | New for QD, incremental for MetaBBO |
| Significance & Impact | 66 | Competent | Interesting to several communities |
| Experimental Validation | 56 | Competent | Few controls |
| Reproducibility | 55 | Competent | Small model, settings partly missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

### Overall Score
**4 (Borderline Accept)**: A creative direction with a notable transfer result whose weaknesses are fixable by controls; I lean toward acceptance.

### Confidence
**3**: Outside the exact sub-area; I did not verify protocol details at the same depth as R1.

---

# Peer Review Report: Reviewer 4 (Generalist)

## Paper: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization
## Reviewer: Dr. Mei-Ling Okafor, Generalist (ML department, large North American university; fictional persona)
## Expertise: deep learning, reinforcement learning, optimization
## Date: 2026-11-05

### Summary
LQD turns the selection-scoring step of a genetic algorithm into a small transformer that is meta-trained on synthetic benchmark functions. The authors report that trained variants match or beat MAP-Elites and Dominated Novelty Search on benchmark functions, transfer to larger populations and robot control, and display "emergent diversity" when trained for fitness only.

### Strengths
**S1: A clear, simple idea with a good one-paragraph pitch.** "Learn the competition function" is easy to state, and Algorithms 1–3 make the single changed line obvious.
**S2: Well-organized paper.** Research questions (Section 5), results, analysis (Section 6), and appendix tables map cleanly; most results are in the main text.
**S3: Fair statement of the negative case.** LQD(F+N) is reported as not matching DNS (Section 5.2).
**S4: Relevant to ICLR audiences.** Learned optimizers and meta-learned algorithm discovery are an established ICLR topic.

### Weaknesses
**W1: Claims in the abstract and introduction are broader than the results.** The abstract promises "demonstrate competitive or superior performance" compared with established QD baselines, the introduction says the results "advance the state-of-the-art in Quality-Diversity optimization", and the framework "can represent any QD algorithm" (Section 4). Section 5.2 shows the QD-targeting variant does not match DNS, and Section 5.3 uses the fitness-only variant and reports no significant gain over GA (a gain over GA that is reported as not statistically significant). *Fix:* align the abstract, contributions and conclusion with what is shown, e.g., "a learned, descriptor-aware selection rule that is a competitive fitness optimizer and keeps more diversity than GA".
**W2: Key quantities are hard to interpret from the main text.** The "QD score" is "maximum fitness multipled by the average" dominated novelty score (Section 4.2.2); results are shown "relative to random GA" with axes up to 10⁵ (Figures 3, 4); the aggregate in Figure 1 and its p-value are explained only in a caption and one sentence. A non-specialist cannot tell what the typical improvement is. *Fix:* add one table with absolute numbers (median and IQR) for each algorithm and task, and define each normalization.
**W3: Venue fit and format.** The manuscript is in the ACM `acmart` style (CCS Concepts, keywords, the placeholder line "Received 29 January 2025; revised 12 March 2009; accepted 5 June 2009") rather than the ICLR style. The audience fit is good for ICLR; the format issue is minor.

### Venue Criteria Checklist (ICLR)
| Item | Grade | Location |
|------|-------|----------|
| Soundness: claims supported by evidence | Partly | Sections 5.2–5.3, 6; see W1 |
| Soundness: baselines and controls | Partly | Section 5.1 (no tuning described) |
| Presentation: clear to a non-specialist | Mostly met | Sections 3–4; W2 on metrics |
| Contribution: significance to the community | Partly | Section 6, F+N result |
| Reproducibility: details/code | Not met | No code statement; Table 1 only |
| Limitations stated | Partly | Conclusion paragraph only |

### Questions for Authors
1. Can you give a table of absolute numbers and effect sizes for the six robot tasks (LQD, ME, DNS, GA)? A table showing LQD ahead of GA on most tasks would raise my score; parity would keep it where it is.
2. Why are the robot experiments run only with the fitness variant, and what do LQD(N) and LQD(F+N) do there?
3. Will code and trained weights be released?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No**

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps between claim and evidence |
| Clarity | 3 | Clear organization |
| Significance | 3 | Relevant topic |
| Originality | 2 | Incremental over prior meta-BBO |

### Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean idea whose headline claims outrun a small set of evaluations.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound core, claims stretched |
| Clarity & Presentation | 66 | Competent | Well organized; metrics opaque |
| Novelty & Originality | 56 | Competent | Incremental combination |
| Significance & Impact | 58 | Competent | Narrow audience |
| Experimental Validation | 50 | Developing | Controls missing |
| Reproducibility | 48 | Developing | No code, missing settings |
| Ethical Compliance | 60 | Competent | Nothing at stake |

### Overall Score
**3 (Borderline Reject)**: A tidy idea with a real chance, but the paper claims more than it demonstrates.

### Confidence
**4**

---

# Devil's Advocate Report

## Paper: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization
## Reviewer: Prof. Rafael Ostrowski-Tan, Devil's Advocate (statistics and evaluation-methodology group; fictional persona)

### Steelman
A small learned selection rule, trained once on cheap synthetic tasks, runs unchanged on much larger problems and on robot control, where it beats the QD baselines on fitness while also retaining more population diversity than a GA. Removing meaningful descriptors makes the benefit vanish, which suggests the network is using descriptor structure the way QD algorithms intend.

### Core Argument Chain
1. A QD algorithm is a GA with a different competition function (Section 3).
2. A transformer over (fitness, descriptor) can represent any such function (Section 4.1).
3. Meta-training on BBOB with random-projection descriptors finds good rules (Section 5.2).
4. These rules match or beat ME and DNS and transfer to robots (Sections 5.2–5.3).
5. LQD(F) keeps more diversity than GA without being trained for it, and loses its edge with random descriptors (Sections 6.1, 6.3).
∴ Meta-learning discovers QD algorithms, and diversity is rediscovered as instrumental for performance.

### Strongest Counter-Argument
Even if every number is right, the data do not show that a *QD algorithm* was discovered. The robot experiments use the variant trained for fitness alone (LQD(F)) and score it on maximum fitness, a metric the QD baselines are not built to maximize; the aggregate result is statistically indistinguishable from the plain GA (the gain over GA is reported as not statistically significant, Section 5.3). The one variant meant to be a QD algorithm, LQD(F+N), "approaches but does not quite match" DNS (Section 5.2). So the supported statement is that a descriptor-aware selection rule can be a competitive fitness optimizer, not that learned QD algorithms advance the state of the art in QD. Second, the comparison is lopsided: LQD gets ≈1.07×10⁹ inner-loop runs of tuning (16,384 meta-generations × 256 candidates × 256 tasks, Section 4.2.3) and untuned, unspecified baselines. That is exactly the setting in which "learned beats hand-designed" can come from search effort alone. Third, the "emergent diversity" story has simpler explanations: a selection rule that is noisier or softer than truncation keeps more of the population spread out under a novelty measure computed on a random linear projection of the genotype, whether or not diversity is "instrumental". The authors' own caveat that ME's novelty is inflated by partially-filled populations (Section 5.2) is then followed by normalizing everything to ME in Section 6.1. Finally, the descriptor ablation (Section 6.3) replaces descriptors with standard-normal noise, an input never seen in training, so the authors' reading that LQD falls back to global competition and "the network is out of range" are indistinguishable. The authors would need tuned baselines, standard QD metrics for all variants, and an in-distribution descriptor-shuffling control to support the central claim.

### Issue List

#### CRITICAL Issues
No CRITICAL issues found. The central claims are overstated, but the evidence supports a narrower version (a competitive learned selection rule with descriptor-dependent behavior), and the paper's own results already state the negative cases; every fix below is a narrowing of claims or an additional control. No test-set selection is stated: the only selection statement (the "held-out tasks" used for validation) leaves the validation set undefined, which is a question (DA-M3), not a documented leak.

#### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Scope / claim distortion (E5) | Abstract; Section 1 ("advance the state-of-the-art in Quality-Diversity optimization"); Section 5.2 | The QD claim is not what was shown: F+N does not match DNS; the robot results use only LQD(F) | Narrow the claims or evaluate all variants with QD metrics on the robot tasks |
| DA-M2 | Evidence (fairness) | Section 4.2.3, Table 1; Section 5.1 | Search effort ≈ 10¹³ evaluations (derived) vs no stated tuning of baselines | Compute-matched tuning of GA/NS/ME/DNS |
| DA-M3 | Protocol | Section 4.2.3 | the "held-out tasks" used for validation: which tasks; how many meta-training runs; was selection done on Table 3 functions? | Define; ≥ 3 meta-training seeds; disjoint validation set |
| DA-M4 | Logic (alternative explanation) | Section 6.1; conclusion | "Diversity as instrumental goal" not tested against softer selection or fitness sharing | Add controls; report the selection-pressure profile of the learned rule |
| DA-M5 | Evidence | Section 6.3, Figure 9 | Random-descriptor control feeds out-of-range inputs; "significantly outperforms" is stated without a test | Descriptor-shuffling control; report tests |
| DA-M6 | Generalization claim | Section 5.2, Figure 5 | Generalization to N and D shown on two *training* functions against ME only | Held-out functions; GA and DNS curves |

#### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Appendix C.3 vs Table 4 | Task count (six Brax + one arm vs six rows) |
| DA-m2 | Metrics | Figures 3, 4, 10 | Normalization to Random (axes to 10⁵) undefined for non-positive values |
| DA-m3 | Reporting | Section 5.3, Figure 1 | Aggregation behind "p < 0.005" not described |

### Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Inner-loop runs in meta-training | M = 256, K = 256, 16,384 meta-generations | 16,384 × 256 × 256 = 1,073,741,824 | Derived (consistent) |
| Evaluations per inner run | N = 128, B = 32, T = 256 | 128 + 256 × 32 = 8,320; total ≈ 8.9×10¹² | Derived |
| Robot budget in generations | "a budget of 1 million evaluations" | ≈ 31,250 generations at B = 32 (if B is unchanged; not stated) vs T = 256 in training | Derived; B unknown |
| Brax task count | Appendix C.3: six Brax + one arm = 7 | Table 4: 5 Brax rows + 1 arm = 6 (six panels in Figure 6) | Mismatch (minor) |
| Parameter count | "approximately 5,000" (Appendix B) | Not independently checkable (embed/MLP widths not given) | Unverifiable |

### Ignored Alternative Explanations
- Search effort rather than the learning formulation explains the gain over untuned baselines.
- A softer or noisier selection (lower effective selection pressure) explains higher novelty without any "diversity-aware" mechanism.
- Descriptor use in robots may reflect that feet-contact and velocity descriptors correlate with fitness (locomotion), not stepping-stone discovery.
- ME's novelty and population size differ from the 128-member populations used for the other methods.

### Missing Stakeholder Perspectives
Practitioners of QD in robotics who care about archive coverage and QD score rather than best fitness; maintainers of QD libraries who need to know the compute cost of the learned operator.

### Observations (Non-Defects)
The paper states that F+N does not match DNS; the descriptor ablation is a good idea; the minimal "only the competition function is learned" design is robust against several confounds (same reproduction operator for all methods, assuming it is shared).

### Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Overclaiming, untested alternative explanations |
| Clarity & Presentation | 62 | Clear narrative |
| Novelty & Originality | 52 | Medium at C1 |
| Significance & Impact | 50 | Depends on narrowing the claims |
| Experimental Validation | 42 | Baselines, metrics and controls |
| Reproducibility | 44 | No code; missing settings |
| Ethical Compliance | 58 | Nothing at stake |

**Overall: 3 | Confidence: 4** (**Pool position:** better than about 44% of submissions to ICLR; accepted share ≈ 27%. Deciding evidence: the headline QD claim is not supported by the variant and metric used.)

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Arm panel budget vs "1 million evaluations" | moved to Questions | Read from extracted axis labels; unverifiable |
| R1 | JL criticism ("does not apply") | rewritten | D is not stated; reworded to "not informative in the n ≤ 12 regime" |
| R1 | Task-count mismatch | moved to Minor | Cosmetic |
| R2 | "Missing PGA-ME" | kept as Helpful `[verify]` | Not found on arXiv by title |
| R2 | Missing QD baselines | rewritten | Phrased as Important, not required; none depends on a recent preprint |
| R3 | No societal-impact paragraph | moved to Minor | Nothing at stake |
| R4 | ACM template instead of ICLR | moved to Minor (W3 keeps venue fit) | Format only |
| DA | "Random-descriptor control is out of range" | kept | Section 6.3 states standard-normal sampling; Section 4.2.1 states projection descriptors in training |
| All | Points answered in the appendix | none dropped | Appendix B/C answer only Table 1/2/3/4 questions |

Scores unchanged.

## Phase 2: EIC Meta-Review and Decision

### Synthesizer Part A: issue map

| Merged issue | Sources | Class |
|--------------|---------|-------|
| QD claim exceeds evidence (F+N vs DNS; fitness-only robot evidence; GA parity) | R1-W3, R2-W3, R4-W1, DA-M1, R1 ERR-3 | CONSENSUS-4 |
| Untuned or unspecified baselines vs large meta-training search | R1-W1, DA-M2, R4 (Reproducibility), R2 Q3 | CONSENSUS-3 |
| Generalization shown on training functions, one baseline (Figure 5) | R1-W2, DA-M6, R3-S3 (credited it) | SPLIT (R3 credits; R1, DA object) |
| Emergent-diversity interpretation untested | R3-W1, DA-M4, R2-W3 | CONSENSUS-3 |
| Descriptor ablation out of range | R3-W2, DA-M5 | CONSENSUS-2 |
| Differentiation from LGA/LES; missing QD meta-evolution citation | R2-W1, R2-W4 | SOLO |
| Validation/meta-training protocol undefined | R1-W4, DA-M3 | CONSENSUS-2 |
| "Any QD algorithm" expressivity claim | R2-W2, R4-W1 | CONSENSUS-2 |
| DA-CRITICAL | none | n/a |

Official score (script, before): ratings 3, 3, 4, 3, 3, mean 3.2; official composite 55.0; band 3; no warnings.

### EIC Meta-Review (Prof. Katarzyna Wójcik-Almeida)

#### The Case For and Against
- **For acceptance:** A neat unification of QD as "GA plus a competition function", a minimal learnable parameterization, a real out-of-regime transfer to 584-parameter robot policies, and honest negative results. The descriptor-ablation direction is the right kind of analysis, and a learned rule that depends on neighbors despite fitness-only training is intriguing.
- **Against acceptance:** The headline QD claim does not match the evidence: the QD-targeting variant does not match DNS, the robot results use the fitness variant and are not significantly better than GA, baselines are untuned against a huge search budget and unspecified, generalization is shown on training functions, and the "emergent diversity" reading lacks controls. Code and key settings are absent.

#### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Baseline hyperparameters and reproduction operator not stated | R1-W1, ERR-1, DA-M2 | Sections 3.2, 5.1; Table 1 | Verified | Text search found only "mechanisms like crossover and mutation"; Table 1 lists no baseline settings |
| Figure 5 functions are training functions | R1-W2, ERR-2, DA-M6 | Figure 5, Table 2 | Verified | Schaffers F7 and Katsuura are both Table 2 rows; plot is vs ME only; generalization in N and D is genuinely out-of-range, so R3's S3 is Partly correct |
| QD claim vs F+N result | DA-M1, R4-W1, ERR-3 | Section 1 (final paragraph); Section 5.2 | Verified | "advance the state-of-the-art in Quality-Diversity optimization" vs "LQD (F+N) approaches but does not quite match" DNS |
| Robot aggregate not significantly better than GA | DA, R1-W3, R4-W1 | Section 5.3 | Verified | a gain over GA that is reported as not statistically significant |
| Robot runs use only the fitness variant | DA, R4 Q2 | Section 5.3 ("we tested LQD (F)") | Verified | Fig. 7 reports novelty for two tasks only (R1 stated this correctly) |
| Selection of the parameter set on "held-out tasks" undefined | R1-W4, DA-M3 | Section 4.2.3; Appendix C | Verified as an omission | No statement that Table 3 tasks were used; the DA's concern is a question, not a leak |
| JL lemma cited for a map from n ≤ 12 dimensions | R1-W5, ERR-4 | Section 4.2.1 | Partly correct | D is not stated, so "does not apply" cannot be shown; the lemma adds no information in this regime |
| Random-descriptor control uses standard-normal inputs | R3-W2, DA-M5 | Section 6.3 | Verified | descriptors drawn from a standard normal distribution; training descriptors are projections of genotypes (Section 4.2.1) |
| "Any QD algorithm" claim | R2-W2 | Section 4, Section 4.1 | Verified (as wording) | The text says so; whether ME can be expressed after standardization is argued, not proven, by R2: treated as a claim to narrow |
| Task-count mismatch | R1 Minor, ERR-5 | Appendix C.3, Table 4 | Verified | Minor |
| LGA delta is thin | R2-W1 | Section 2 | Partly correct | Section 2 names LGA and LES as most closely related and states the QD setting; no empirical comparison and no explicit delta list |
| Text overlap with LGA | Similarity flag | Section 1 vs LGA | Verified but immaterial | Two generic shared 8-grams with a cited work; reported to the editor, no score effect |

#### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log entry I checked held at its location; central claims decisive and well calibrated |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly verified; the ME-expressivity point is argued, not demonstrated |
| R3 (Perspective) | 4 | 3 | 0.75 | Rating leans on Figure 5 scaling and "rediscovers a principle" readings that Step 2 found overstated (training functions; no causal control); pool position 66 sits above what the verified evidence supports |
| R4 (Generalist) | 3 | 4 | 1.0 | Sound, typical review; claims checks verified |
| DA | 3 | 4 | 1.0 | Arguments mostly survived; the alternative-explanation list is partly speculative but flagged as such |

#### DA-CRITICAL Rulings
None raised ("No CRITICAL issues found"). I checked the protocol statement behind the leakage question (Section 4.2.3): the validation tasks are undefined, so the criterion-3 table row is "not stated after the protocol sweep: MAJOR (a question)", not CRITICAL. **DA ceiling: none.**

#### Final Decision and Justification
Official ratings 3, 3, 4, 3, 3 (mean 3.2). With confidence × EIC weights, the EIC-weighted rating is 3.13, which rounds to a starting point of **3**; the 0–100 composite is 54.3 (band 3), so there is no cross-check disagreement. I do not depart from the starting point. The decisive verified issues (QD claim vs the F+N result and the GA-parity aggregate, untuned and unspecified baselines against a ~10¹³-evaluation search, generalization shown on training functions) are already reflected in four of the five ratings. R3's higher rating is down-weighted because its main support was found overstated, not because it is lenient by role. My own pool position: **better than about 50% of submissions to ICLR** (accepted share ≈ 27%): the idea is attractive and the writing is clear, but the main comparisons are not controlled well enough, and the paper is on the rejected side of the bar at present. The needed fixes (tuned baselines, standard QD metrics, held-out generalization, protocol details) are new experiments, but all are standard and bounded, so a revised version would be competitive. The decision does not exceed any DA ceiling (none).

**Final (EIC): 3, Borderline Reject. ICLR rating label (scale status: secondary): "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})".**

---

## Score Summary

### Official Scores and EIC Assessment (output of `aggregate_scores.py`, with EIC weights; `--venue iclr --final 3`)

| Reviewer | Overall | Confidence | EIC weight | Weight share | Own composite | Pool position |
|----------|---------|------------|------------|--------------|---------------|---------------|
| R1 (Methodology) | 3 | 4 | 1.25 | 0.257 | 52.1 | 45 |
| R2 (Domain) | 3 | 4 | 1.0 | 0.205 | 55.8 | 50 |
| R3 (Perspective) | 4 | 3 | 0.75 | 0.127 | 61.6 | 66 |
| R4 (Generalist) | 3 | 4 | 1.0 | 0.205 | 55.7 | 54 |
| DA | 3 | 4 | 1.0 | 0.205 | 49.7 | 44 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 58 | 62 | 56 | 48 | 55.2 | 54.5 | 14 |
| Clarity & Presentation | 62 | 65 | 68 | 66 | 62 | 64.6 | 64.2 | 6 |
| Novelty & Originality | 55 | 52 | 64 | 56 | 52 | 55.8 | 55.1 | 12 |
| Significance & Impact | 52 | 55 | 66 | 58 | 50 | 56.2 | 55.2 | 16 |
| Experimental Validation | 46 | 52 | 56 | 50 | 42 | 49.2 | 48.5 | 14 |
| Reproducibility | 42 | 50 | 55 | 48 | 44 | 47.8 | 46.9 | 13 |
| Ethical Compliance | 60 | 62 | 62 | 60 | 58 | 60.4 | 60.3 | 4 |
| **Composite** | 52.1 | 55.8 | 61.6 | 55.7 | 49.7 | **55.0 (before)** | **54.3 (after)** | |

No dimension is flagged for spread > 20. Consistency warnings: none (the DA's composite implies band 2 against an Overall of 3, a gap of one, which is within tolerance).

### Target-Venue Scores (ICLR, scale status: secondary; shown with that caveat)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

*Cross-venue comparison was not requested.*

---

## Editorial Decision Letter

# Editorial Decision

**Paper:** Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization · **Target venue:** ICLR · **Paper type:** empirical · **Date:** 2026-11-05
**Review team (fictional personas):** EIC Prof. Katarzyna Wójcik-Almeida; R1 Dr. Anand Subramaniyan; R2 Prof. Elodie Marchetti; R3 Dr. Kwame Boateng-Lindholm; R4 Dr. Mei-Ling Okafor; DA Prof. Rafael Ostrowski-Tan.

**Decision: Borderline Reject (3)**
**Official ratings:** R1 3, R2 3, R3 4, R4 3, DA 3 → mean 3.20 · official composite 55.0
**EIC assessment (internal):** weighted rating 3.13 → starting point 3 · weighted composite 54.3 → band 3 · **DA ceiling:** none · **Final (EIC):** 3
*How a careful panel would likely see this draft; a simulation, not a prediction.*

Dear Authors,

Thank you for submitting "Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization" to ICLR. Learning the competition rule of a quality-diversity algorithm is an attractive question, and your framing of QD as a GA with a different competition function is clear and useful.

**Overall Assessment:** The reviewers agreed the idea is neat, the formulation is minimal and well explained, and the transfer of a ≈5,000-parameter rule to 584-parameter robot policies is a real result. They also agreed that the evidence supports a narrower claim than the one made: a learned, descriptor-aware selection rule that is a competitive fitness optimizer and retains more diversity than a GA.

**Key Strengths Identified by Reviewers:**
1. A clean unification and minimal learnable parameterization (R1, R2, R4).
2. Non-trivial transfer from 2–12-dimensional BBOB to robot control, and the descriptor ablation as an analysis tool (R1, R3).
3. Honest reporting that LQD(F+N) does not match DNS (R2, R4).

**Key Concerns Requiring Attention:**
1. The QD claim exceeds the evidence: the QD-targeting variant does not match DNS (Section 5.2), robot results use only the fitness variant and are not significantly better than GA (Section 5.3), and no archive QD metrics are reported (CONSENSUS-4).
2. Baselines are unspecified and apparently untuned while LQD received ≈10⁹ inner-loop runs of meta-training (CONSENSUS-3).
3. Generalization in population size and dimension is shown on two training functions against ME only (Figure 5; SPLIT between R3 and R1/DA, resolved by the EIC in favor of R1/DA); "emergent diversity" and "any QD algorithm" are not tested with controls (CONSENSUS-3 and -2).

No CRITICAL challenge was raised by the Devil's Advocate; its strongest objection (that no QD algorithm was demonstrated to be discovered) is resolved by narrowing the claim or adding the evidence listed in the roadmap.

**Decision: Borderline Reject (3).** The reasons to reject presently outweigh the reasons to accept, mainly because the central comparison is not controlled. A revision that narrows the claims or adds tuned baselines, standard QD metrics for all variants on the robot tasks, held-out generalization sweeps, and the missing protocol details would likely be competitive. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Katarzyna Wójcik-Almeida
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers)
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| QD claim exceeds the evidence | R1, R2, R4, DA | CONSENSUS-4 |
| Untuned or unspecified baselines vs large meta-training search | R1, R4, DA (R2 asks for strong baselines) | CONSENSUS-3 |
| Emergent-diversity interpretation untested | R2, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Figure 5 shows strong generalization | R3 | R1, DA | Scaling in N and D is out-of-range (credited), but the two functions are training functions and only ME is compared; claim far beyond training conditions is Overstated |

### Score Spread Discussion
No dimension is flagged above a 20-point spread; the largest spread is Significance (16: R3 66 vs DA 50). The EIC adopts the lower end because Significance depends on the QD claims that were not verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | QD claim not what was shown | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Search effort vs untuned baselines | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | Validation and meta-training protocol | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Alternative explanation for diversity | Yes (R3) | n/a | n/a |
| DA-M5 | MAJOR | Out-of-range descriptor control | Yes (R3) | n/a | n/a |
| DA-M6 | MAJOR | Figure 5 on training functions | Yes (R1) | n/a | n/a |
| (CRITICAL) | none raised | | | | |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | QD claim exceeds the evidence | DA-M1, R1-W3, R2-W3, R4-W1, ERR-3 | Abstract; Sections 1, 5.2, 5.3; conclusion | Narrow claims, or report archive QD score and coverage for LQD(F), (N), (F+N) on robot and BBO tasks | Med; ≈ 1–2 GPU-days | Partly (wording: yes; new metrics: likely) |
| P1-2 | Baselines untuned/unspecified vs large search | R1-W1, DA-M2, ERR-1 | Sections 3.2, 5.1; Table 1 | Report all settings; compute-matched tuning of GA, NS, ME, DNS | Med–High; ≈ 1–3 GPU-days | Partly |
| P1-3 | Generalization shown on training functions, vs ME only | R1-W2, DA-M6, ERR-2 | Figure 5; Table 2, Table 3 | Repeat on held-out functions with GA and DNS; label the plotted quantity | Low–Med; ≈ 0.5 GPU-day | Yes |
| P1-4 | Protocol: validation tasks, number of meta-training runs, D, robot N/budget | R1-W4, DA-M3 | Section 4.2.3; Sections 4.2.1, 5.3 | State them; ≥ 3 meta-training seeds with spread | Med; ≈ 3× meta-training cost | Partly (statements yes; seeds maybe) |
| P1-5 | Closest prior work not compared | R2-W1 | Section 2 | Add LGA-style (fitness-only) operator as baseline and no-descriptor ablation; delta paragraph | Med | Partly |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | "Emergent diversity" without controls | R3-W1, DA-M4 | Fitness-sharing and tuned-GA baselines; selection-pressure profile of the learned rule | Med | Yes |
| S2 | Out-of-range descriptor ablation, no test | R3-W2, DA-M5 | Descriptor-shuffling control; report tests for "significantly" | Low | Yes |
| S3 | "Any QD algorithm" expressivity | R2-W2 | Show reproduction of NS, DNS, ME or restrict the claim | Low–Med | Yes |
| S4 | Missing QD baselines and related work | R2-W4 | CMA-ME, CMA-MAE; cite QD meta-evolution and MetaBox | Med | Partly |
| S5 | Metrics undefined, normalization to Random, aggregate in Figure 1 | R4-W2, DA-m2, DA-m3 | Table with absolute medians and IQR; define normalization and aggregation | Low | Yes |
| S6 | Cost of the learned rule | R3-W3 | Wall-clock and evaluation-matched comparison | Low–Med | Yes |
| S7 | JL justification | R1-W5 | State D; soften the claim | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Task-count mismatch, template dates, typo "multipled", acmart format | R1, R4 | Fix |
| N2 | No limitations paragraph; code release | R1, R3, R4 | Add limitations; release code and weights |
| N3 | Extensions (learned descriptors, multi-objective) | R3 | Mention as future work |
| N4 | Helpful references (PGA-ME `[verify]`, VeLO) | R2 | Cite where relevant |

## Estimated Revision Effort
- Priority 1: 5 items, ≈ 1–2 weeks including ≈ 5–8 GPU-days on the stated hardware (estimate)
- Priority 2: 7 items, ≈ 2–4 days, mostly re-analysis and small controls
- Priority 3: 4 items, < 1 day
- **Total estimated revision time:** ≈ 2–3 weeks

*Integrity note for the editor: no reviewer-directed text was found; two generic shared 8-grams with a cited prior paper (LGA) were noted in Reviewer 2's addendum and carry no score effect. Literature check: strict mode, 7 queries (6 claim, 1 expansion), 84 kept results; no baseline scout was possible (query refused for length); gaps open: baseline scout, and C4 novelty (arXiv-only search).*
