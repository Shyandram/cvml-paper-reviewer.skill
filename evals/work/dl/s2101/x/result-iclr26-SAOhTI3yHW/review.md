# Simulated Panel Review: "RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation"

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested).
This is a simulation of how a careful panel would likely see this draft. It is not a prediction of an outcome. Figures were not available; figure-dependent claims are judged from captions and text only (Fig. 1–8 are unverified visually, so E9 was not checked).

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation |
| Primary Discipline | ML / RL → autonomous-driving traffic simulation (closed-loop behavior models) |
| Secondary Discipline(s) | Robotics / AV safety evaluation; transportation engineering (surrogate safety measures) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | IL-pretrained multimodal trajectory model (Pluto), GRPO-style group-relative advantage, Dual-Clip PPO, hand-built state-wise reward, CARLA / Bench2Drive |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status secondary) |
| Venue-Specific Notes | None. Reviews and submissions public at ICLR; revised PDF allowed during discussion |
| Paper Maturity | Submission-ready (preprint "under review") |
| Ethics-Relevant Content | None beyond simulation; Appendix E discusses sim-to-real gap |

### Claimed Contributions (as stated by the authors, §1)
- **C1** Dual-stage AV-centered framework: open-loop IL pre-training in a data-driven simulator for "trajectory-level realism and multimodality", then closed-loop RL fine-tuning in a physics-based simulator for controllability and covariate shift.
- **C2** RIFT: "GRPO-style group-relative advantage" over all candidate trajectories (preserves multimodality), with KL replaced by a dual-clip objective (stability, controllability) (§4.2, Eq. 6–8, App. A).
- **C3** "Extensive experiments" show realistic, controllable scenarios and improved reliability of AV evaluation (Tables 1–3, §5.3).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Pre-training: released Pluto checkpoint trained on nuPlan (§5.1; not retrained). Fine-tuning: CARLA with Bench2Drive; "Fine-tuning is conducted on 2× Bench2Drive220, while evaluation is performed on dev10" (App. B.4). Fine-tuned module: trajectory scoring head only for all fine-tuned methods (Fig. 2 caption, §5.1, B.4). Compute: ~8 h on one RTX 4090D per run (B.4). Seeds: "three random seeds" in Tables 1–3; whether seeds are training or evaluation seeds is not stated. Hyperparameters: Tables 4–6 (ε = 0.2, c = 3, γ = 0.98, N_lon = 12; N_ref not stated). Code: not stated in the text (links removed).
- **Headline numbers** (Table 1, PDM-Lite AV): RIFT-Pluto ORR 0.36, CPK 6.83, RP 995.33, 2D-TTC 2.74, ACT 2.71, Speed SW 0.97, WD 4.46, Acc SW 0.93. Table 2 (PDM-Lite): DS 94.78, RC 94.78, IS 1.00, BR 0.00; (PlanT): DS 44.28, RC 61.94, IS 0.64, BR 40.00.
- **Appendix adds:** convergence analysis under a binary reward (A), CBV identification (B.2), algorithm (B.3), baselines (B.5), reward model (B.6, Table 6), metric definitions (B.7), AV metrics (C), qualitative controllability (D.1), comfort results (D.2, Table 7), more visuals (D.3), social impact (E).
- **Unverifiable:** Figures 1–8 (not available); equation layout in A.4–A.5 is partly garbled by extraction, so only derivations that are legible were checked.

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. Reviewers read the redacted copy (identical to the original). No injection was found while reading either.

### Literature-check status (strict, cutoff 2025-09-24)
`related_search.py` was run with `--mode strict`. The arXiv API was rate-limited (HTTP 429) or timed out on most calls. Completed: 1 claim query (C1, "traffic simulation reinforcement learning": 25 returned, 20 kept, almost all traffic-*signal* control, off-topic) and 1 baseline query ("CARLA background vehicle behavior": 1 kept). No C2/C3 query, `scout`, `coverage`, `similarity` or `novelty` run completed. The `benchmarks` command found no external benchmark to scout. **Gaps left open:** C2, C3, baseline scout, similarity. Per-claim novelty below is therefore from the paper's own related work and the reviewers' knowledge, with `[verify]` markers. Nothing from this check was used to lower a score.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ingrid Valsamaki, senior area chair profile (Europe)
- Seniority / Expertise: senior / RL for robotics, simulation-based AV validation
- Role: reads all five reviews, checks decisive points, weights reviewers, decides
- Style: weighs what the paper's own tables show over what its prose says

### Reviewer 1 (Methodology): Dr. Tomasz Okonkwo-Reyes, industrial research lab (North America)
- Seniority / Expertise: senior industry scientist / policy-gradient RL, offline-to-online fine-tuning, closed-loop evaluation protocols
- Review Focus: design, statistics, comparison fairness, reproducibility
- Style: recomputes every table delta; insists on matched tuning budgets and seed-level variance

### Reviewer 2 (Domain): Prof. Mei-Lin Harrington, vision/driving group, large public university (East Asia)
- Seniority / Expertise: senior faculty / multi-agent traffic simulation (WOSAC-style), motion forecasting
- Review Focus: literature, theory, domain contribution
- Style: reads the bibliography against the claims; expects the standard sim-agent metrics

### Reviewer 3 (Perspective): Dr. Anselm Bhattacharya, transportation-safety and vehicle-dynamics lab (South Asia)
- Seniority / Expertise: mid-career / surrogate safety measures, driver behavior modeling, controller-level vehicle dynamics
- Review Focus: cross-disciplinary links, deployment, assumptions, broader impact
- Style: constructive; asks whether metrics mean in practice what they are called

### Reviewer 4 (Generalist): Dr. Camila Strand-Oyelaran, ML group, mid-size research university (Latin America)
- Seniority / Expertise: mid-career / representation learning and general deep RL, not driving specifically
- Review Focus: contribution clarity, venue fit, presentation
- Style: typical program-committee reader; judges whether the story is easy to follow and fits ICLR

### Devil's Advocate: Prof. Jun-ho Albrecht-Nwosu, evaluation-methodology researcher (Europe)
- Seniority / Expertise: senior faculty / benchmark validity, causal inference for evaluation
- Review Focus: core-argument challenges, logic, overclaiming
- Style: rigorous and fair; separates "unsupported as worded" from "contradicted"

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reports

(Five separate role-based passes in one model context; they are not independent agents and share one model context.)

---

# Peer Review Report (Reviewer 1: Methodology)

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Reviewer: Dr. Tomasz Okonkwo-Reyes, Methodology (industrial research lab; fictional persona)
## Expertise: policy-gradient RL; offline-to-online fine-tuning; closed-loop evaluation protocols
## Date: 2026-11-10

## Summary
The paper builds closed-loop traffic simulation around a single AV with rule-based background vehicles, and replaces one or more "critical" background vehicles (CBVs) by a pre-trained multimodal trajectory generator (Pluto). It then fine-tunes only the generator's trajectory scoring head with a GRPO-like objective over the fixed set of N_ref×N_lon candidate trajectories, using a hand-designed state-wise reward, no KL term and a dual-clip surrogate. On CARLA/Bench2Drive the authors compare against IL, RL, SFT and hybrid baselines and report better route progress and safety-time metrics, and better AV driving scores when the AV is evaluated against RIFT-driven CBVs.

## Strengths
### S1: Matched fine-tuning module across baselines
All fine-tuned baselines train the same trajectory scoring head from the same checkpoint (§5.1, App. B.5), which removes the largest architectural confound in the RLFT comparison (PPO-/REINFORCE-/GRPO-Pluto vs RIFT).
### S2: Informative ablation axes and honest negative results
Table 3 isolates clip type, fine-tuned module and reward style with signed deltas, and the arithmetic of the deltas is correct (e.g., RP 995.33 − 339.94 = 655.39; CPK 6.83 − 4.80 = 2.03). App. D.2/Table 7 reports a comfort failure of RIFT openly.
### S3: Light compute and clear hyperparameters
~8 h on one GPU per run (B.4) and hyperparameters in Tables 4–6 make an independent rerun plausible for RIFT itself.

## Weaknesses

### W1: The central methodological claim (KL → dual-clip, group-relative advantage) is not isolated by any experiment
The abstract and C2 credit RIFT's gains to group-relative advantage plus "replacing KL regularization with the dual-clip mechanism". The only controlled comparison is GRPO-Pluto (PPO-Clip *and* KL) vs RIFT-Pluto, which changes two things at once (App. B.5: "GRPO-Pluto utilizes the basic GRPO algorithm [20] … while incorporating the standard PPO-Clip"). Table 3 varies clip type but does not add KL back to RIFT, and does not replace the group-relative advantage with a per-executed-trajectory advantage inside the same framework. Moreover, RIFT vs GRPO-Pluto in Table 1 is mostly within one standard deviation: ORR 0.36 ± 0.20 vs 0.10 ± 0.08 (GRPO better), CPK 6.83 ± 2.62 vs 7.24 ± 4.04, 2D-TTC 2.74 ± 1.30 vs 2.65 ± 1.44, Acc SW 0.93 vs 0.96 (GRPO better); only RP (995.33 ± 84.62 vs 892.65 ± 65.27, a recomputed +102.68, +11.5%) and Speed WD (4.46 ± 0.43 vs 4.96 ± 0.89) separate. The text's "enhancing controllability and training stability" is also not backed by any learning curve.
- **Suggested Fix**: add (i) RIFT + KL(β sweep), (ii) RIFT with PPO-Clip and no KL (already partly there) and (iii) group-relative vs executed-trajectory advantage, each with ≥ 5 training seeds, plus reward/learning curves. About 4 variants × 5 seeds × 8 GPU-h ≈ 160 GPU-h.

### W2: Statistical support is thin and the seed semantics are unstated
Tables 1–3 use "three random seeds"; the paper never says whether seeds change training, evaluation rollouts, or both (omission sweep: not stated). Evaluation is on a single development subset: "evaluation is performed on dev10" (App. B.4). Table 2 block rates are consistent with a handful of discrete events: BR values are multiples of 3.33 (e.g., 6.67 ± 5.77, 13.33 ± 5.77), which suggests 10 routes × 3 seeds (derived, not stated). RIFT's headline "BR 0.00 ± 0.00" would then be 0 events vs 2 for GRPO-Pluto (6.67), i.e., not distinguishable. DS differences are also within spread: RIFT 94.78 ± 1.37 vs REINFORCE-Pluto 92.17 ± 3.45. No significance test or CI is given anywhere.
- **Suggested Fix**: state seed semantics; report training-seed variance for the RL-fine-tuned methods (RL is high-variance); evaluate on ≥ 50 routes (e.g., a larger Bench2Drive subset) and give bootstrap CIs. ~30–60 GPU-h of CARLA evaluation.

### W3: Baselines are adapted, tuned by unknown effort, and entangled with the evaluation AV
RTR-Pluto and RS-Pluto "replace" human or ground-truth supervision by PDM-Lite (B.5), and SFT-Pluto uses PDM-Lite as "the expert model, providing supervision at the target speed level". PDM-Lite is also the AV in Table 1 and the first AV in Table 2. The SFT/hybrid baselines are therefore trained to imitate the same planner they are tested against, which makes their infraction and progress numbers hard to interpret; tuning budgets for any baseline are not stated, and Table 5 gives a single hyperparameter set "of RIFT or RL baselines". The RL baselines (PPO, FREA, FPPO-RS) are adversarial scenario generators from another paper (B.5) used with their own objectives, so they are not realism-oriented comparators.
- **Suggested Fix**: report tuning effort per baseline; evaluate SFT/hybrid baselines against an AV other than their teacher in every table; add a realism-oriented comparator trained on the same reward (e.g., KL-anchored RLFT).

### W4: Method definition gaps that block reproduction of RIFT
(i) π_θ(τ|s) in Eq. 7–8 is never defined for a *scoring head*; Eq. 5 gives confidences S = MLP(Q_dec), but no softmax or sampling distribution is stated. (ii) Eq. 7 assumes {τ_i} ∼ π_θold, whereas the group is the fixed decoder output (G = N_ref × N_lon) and the executed one is "the highest-scoring trajectory" (§4.2), so the importance ratio is not that of a sampling policy; (iii) Eq. 6 divides by std(R) with no ε guard, which is unstable for groups with near-identical rewards; (iv) N_ref is not given. See Error Log ERR-1 for the dual-clip expression.
- **Suggested Fix**: define the candidate distribution and the sampling/execution rule; give N_ref; state ε in the normalization.

### W5: Reward–metric overlap
The training reward (Table 6, App. B.6) includes velocity, progress-like and collision terms; the headline controllability metrics RP and WD (speed vs CARLA target speed) and the collision metrics measure largely the same quantities. A method that optimizes the reward well will look best on these metrics regardless of "controllability" or "realism". The only controllability experiment is a single change of two reward weights (Table 6: α_collision 20→5, α_velocity 0.1→0.2).
- **Suggested Fix**: evaluate on metrics not in the reward (e.g., human-log distributional metrics on nuPlan, see R2) and add a held-out reward style.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | Eq. 8, Eq. 10; Table 5 | "max min ... Âi , clip ... Âi , c Âi" (Eq. 8); "Dual-clip ratio c = 3" | As printed, the outer max with cÂ_i applies for every i. For Â_i > 0, min(·) ≤ (1+ε)Â_i = 1.2 Â_i < 3 Â_i, so f = cÂ_i is constant in θ: zero gradient for all positive-advantage trajectories. Dual-Clip PPO applies it only for Â < 0 (App. Eq. 18 is restricted to Â_i < 0). | Derived from Eq. 8 with ε = 0.2, c = 3 | Medium (likely notational, depends on the implementation) | MAJOR if implemented as printed, MINOR if typo | State the sign condition in Eq. 8/10; confirm the code |
| ERR-2 | E1 | Table 3, row "w/ All-head", RP | "827.12 (168.21)" | Sign missing: 995.33 − 827.12 = 168.21, so the delta is −168.21; every other row prints signs | Recomputed | High | MINOR | Print −168.21 |
| ERR-3 | E6 | §4.1 vs App. B.2 | "The vehicle with the highest interaction probability is selected as the CBV" vs "included in the CBV set C" | §4.1 selects one CBV by a "probability"; B.2 defines a deterministic distance-to-goal threshold (δ = 15 m) that yields a set | Cross-referenced two locations | High | MINOR–MAJOR (affects what the experiments simulate) | Define the number of CBVs and the selection rule once |
| ERR-4 | E5 | §5.2 | "RIFT consistently outperforms all baselines in both aspects across most settings" | In Table 1 RIFT is best on 4 of 8 metrics (RP, 2D-TTC, ACT, Speed SW); worse than Pluto on ORR (0.36 vs 0.24) and CPK (6.83 vs 5.06), worse than RS-Pluto on CPK (4.11), worse than GRPO-Pluto on Acc SW; WD is a tie with PPO (4.46 vs 4.45) | Recomputed from Table 1 | High | MAJOR (overclaim, survives in weaker form) | Narrow to "best progress and speed-distribution scores; infraction rates comparable to RLFT baselines and above the IL base" |

### Claim-to-evidence map (compressed)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Dual-stage framework balances realism and controllability | Abstract, §1 | Tables 1–3 | Partially (realism not measured against human data) |
| C2 | Group-relative advantage preserves multimodality; dual-clip replaces KL and improves stability/controllability | §4.2, App. A | Table 3 (clip), Table 1 | Partially; multimodality and stability untested; KL and group-advantage not ablated |
| C3 | Realistic, controllable scenarios; improved AV-evaluation reliability | Abstract, §5.2–5.3 | Tables 1–3, 7 | Partially; Table 2 PlanT contradicts "near-optimal" wording |

## Questions for Authors
1. What do the three seeds vary (training, evaluation, or both), and how many routes and episodes are in each Table 1–2 cell? A single answer showing ≥ 20 routes with consistent ordering would raise my score.
2. How is π_θ(τ|s) defined for the scoring head, and does the code apply the c-clip only for Â < 0? An implementation applying Eq. 8 literally would lower my score.
3. What happens to Table 1 if KL(β>0) is kept in RIFT, or if the advantage is computed only on the executed trajectory?

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Key mechanisms not isolated; thin statistics |
| Clarity | 2 | Method gaps (W4) |
| Significance | 2 | Practical but narrow evidence |
| Originality | 2 | Adaptation of known objectives |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution that the abstract credits (KL→dual-clip, group advantage) is not isolated, and the evaluation uses ~10 routes with large std.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | ERR-1, undefined π_θ, off-policy mismatch |
| Clarity & Presentation | 55 | Competent | Key facts in captions/appendix |
| Novelty & Originality | 48 | Developing | See R2 |
| Significance & Impact | 52 | Developing | Single simulator, narrow evidence |
| Experimental Validation | 45 | Developing | W1, W2, W3 |
| Reproducibility | 60 | Competent | Hyperparameters given; code not stated; N_ref missing |
| Ethical Compliance | 65 | Competent | Limitations and Appendix E present |

## Limitations Assessment
**Partially.** The authors state the state-wise reward limitation (§6, D.2). Missing: single-simulator scope, tiny evaluation set, no realism check against human data.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: a plausible, cheap method whose headline attribution and statistics do not yet support the claims.
## Confidence
**4**: read all tables and the appendix and recomputed deltas; the figures were unavailable.

---

# Peer Review Report (Reviewer 2: Domain)

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Reviewer: Prof. Mei-Lin Harrington, Domain (vision/driving group, large public university; fictional persona)
## Expertise: multi-agent traffic simulation and sim-agent evaluation; motion forecasting
## Date: 2026-11-10

## Summary
RIFT couples an IL-pretrained trajectory generator with RL fine-tuning of its scoring head in CARLA, to produce background-vehicle behavior that is both "realistic" and "controllable" for evaluating AV planners. The main differentiating ideas are the group-relative (GRPO-style) advantage across candidate trajectories and a dual-clip surrogate instead of KL.

## Strengths
### S1: A relevant gap
Closed-loop traffic agents are either log-trained (covariate shift) or RL-trained (unnatural); an AV-centered, reward-steerable agent is a practical need (§1, Fig. 1).
### S2: Related-work coverage of the three sub-areas
§2 covers generative realism (SMART, GUMP, Trajeglish, MotionLM), controllable generation (CTG, ProSim, SceneControl) and closed-loop fine-tuning (RTR [21], RS [22], CAT-K [44], TrafficRLHF [45]).
### S3: Appropriate IL base
Pluto is a strong, open vectorized planner with a modular decoder that makes head-only fine-tuning natural (§3.2).

## Weaknesses

### W1: "Realism" is never measured against human behavior
The paper's own text says it extends WOSAC but then drops WOSAC's log-based realism: "since all our experiments are conducted in the CARLA simulator without expert demonstrations, we adopt distribution-level metrics" (App. B.7). The two substitutes are the Shapiro–Wilk test "to assess the normality of speed and acceleration" (§5.1) and a Wasserstein distance to "the target speed in the CARLA". Normality of a speed histogram is not a property of human driving (mixtures of stopping and cruising are legitimately non-normal), and distance to a simulator's configured target speed rewards rule-following, not human-likeness. Yet the title, abstract ("significantly improves the realism") and the conclusion treat these as realism. The framework's own motivation (pre-training on nuPlan for realism) is never evaluated where logs exist: no evaluation of the fine-tuned model on nuPlan/Waymax-type closed-loop sim with WOSAC-style likelihood metrics, no minADE/JSD of kinematics against logs. §5.1 also states WOSAC "evaluates behavior controllability and realism"; to my knowledge WOSAC is a realism benchmark (kinematic, interactive, map-based likelihood metrics), so the description appears mistaken `[verify]`.
- **Suggested Fix**: add log-based realism on nuPlan (or Waymo) for the pre-trained and fine-tuned models, or rename the claim ("kinematic plausibility in CARLA"). Medium cost: re-running Pluto/RIFT scoring in an existing nuPlan closed-loop harness.

### W2: Novelty relative to the closest cited work is not shown
The paper's framing ("previous approaches [21, 22] typically fine-tune only the best-performing trajectory or action") is the main differentiator. RS [22] (RL fine-tuning of a pre-trained IL traffic model) and RTR [21] already do IL pre-training followed by closed-loop RL, and Lu et al. [43] does IL+RL for driving. What is new is the group-relative advantage over the *candidate set* and dual-clip, applied to a scoring head. Both components exist elsewhere (GRPO [20], Dual-Clip PPO [60]). The paper does not give a side-by-side of what RS/RTR optimize versus RIFT beyond one sentence, and its baselines RS-/RTR-Pluto are re-implementations with PDM-Lite supervision (B.5), so the empirical differentiation from [21, 22] is indirect. The first contribution (C1, the "dual-stage framework") is essentially the standard pre-train-then-RL recipe and the pre-training stage is a downloaded checkpoint (§5.1), not part of the work.
- **Suggested Fix**: state in a table what is optimized (executed action, best trajectory, all candidates), what supervision and what update rule each of [21, 22, 43, 44, 45] uses; reduce C1 to a system description.

### W3: Missing comparisons and the "controllable" literature are cited but not engaged
§2 lists controllable generators (CTG [35], CTG++ [37], ProSim [39], SceneControl [40], RealGen [41], CCDiff [42]) and says they are "limited to open-loop or simplified environments". But the claim of controllability is only evaluated against the paper's own reward-weight switch (Table 3, Fig. 6), with no comparison on control success to any conditional generator, and CAT-K [44] and TrafficRLHF [45] are dismissed in §2 ("rely on expert demonstrations", "demands costly human input") yet never run, even though SFT-Pluto with PDM-Lite is a comparable supervised signal.
- **Suggested Fix**: add one closed-loop fine-tuned data-driven baseline (CAT-K-style supervised fine-tuning) and one steerability comparison on a shared control target.

### W4: The theory does not connect to the paper's claims
App. A analyzes a binary reward, no KL and an idealized "success-probability" map; the experiments use a continuous 7-term reward (Eq. 20). The maximized surrogate Φ(p) = 2ε√(p(1−p)) (Eq. 14) does not contain c at all, so Theorem A.4(c) ("The dual-clip term eliminates gradient explosions caused by negative advantages, guaranteeing stable learning") is not derived from the analysis; and the contraction in Theorem A.4 is assumed ("If |h_ε(p) − h_ε(p′)| ≤ λ|p − p′| …"). It also says nothing on realism, multimodality or the KL removal (see DA-M3).
- **Suggested Fix**: either relocate the analysis to a remark with its limits stated, or prove a statement involving c and the real objective.

### W5: Citation accuracy (E7)
Supporting references for "pre-training and fine-tuning in LLMs [18–20]" are DPO, DAPO and DeepSeekMath, none a pre-train/fine-tune reference; REINFORCE is cited to Sutton et al. 1999 [59] (policy-gradient theorem). Minor, but it shows loose citation practice in a paper whose novelty statements rest on [21, 22].

### Missing References
*A literature check was attempted under strict mode but the arXiv API was rate-limited; entries below are marked as found by the script or `[verify]`.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | S. Shiroshita, S. Maruyama, D. Nishiyama, M. Ynocente Castro, K. Hamzaoui, G. Rosman, "Behaviorally Diverse Traffic Simulation via Reinforcement Learning", IROS 2020 (found by the script: https://arxiv.org/abs/2011.05741v1; prior, peer-reviewed) | RL for diverse, controllable traffic agents with a policy-selector over a skill set: direct precedent for multimodality-plus-RL in traffic simulation |
| Helpful | P. Li, A. Kusari, D. J. LeBlanc, "A Novel Traffic Simulation Framework for Testing Autonomous Vehicles Using SUMO and CARLA", 2021 (found by the script: https://arxiv.org/abs/2110.07111v1; arXiv-only prior) | BV naturalistic behavior in CARLA for AV testing |
| Important | A. Z. Ren et al., "Diffusion Policy Policy Optimization", ICLR 2025 `[verify]` | PPO-style fine-tuning of multimodal generative policies; relevant to "preserve multimodality" |
| Helpful | Zhou et al., "BehaviorGPT: Smart Agent Simulation for Autonomous Driving with Next-Patch Prediction", NeurIPS 2024 `[verify]` | Strong data-driven sim-agent baseline family on WOSAC |
| Helpful | Guo et al., "Bench2Drive-R: Turning Real World Data into Reactive Closed-Loop Autonomous Driving Benchmark by Generative Model", 2024 `[verify]` | Reactive agents inside the Bench2Drive setting the paper builds on |

No *Critical* missing comparison could be confirmed. Per the labels, none of the above is a required comparison; newer or recent work is "worth discussing" only.

### Novelty delta (from the paper's own related work and knowledge; `[verify]`)
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 dual-stage IL→RL | RS [22], RTR [21], Lu et al. [43] | IL-pretrained driving/traffic model fine-tuned with closed-loop RL | Transfer of a nuPlan-trained planner to CARLA CBVs; AV-centered CBV selection (after [1], [57]) | Cited; differentiated by one sentence |
| C2 group-relative + dual-clip | GRPO [20], Dual-Clip PPO [60] | Group-normalized advantage; clipped negative-advantage surrogate | Applied to a scoring head over fixed candidates, KL dropped | Cited; combination not ablated |
| C3 results | none | | CARLA table of CBV methods | n/a |

Per-claim verdict: C1 incremental (level ≈ 4), C2 medium (combination of two known components), C3 result-type (no prior claim to compare). With only two completed queries, "no close prior work found" is a limit of the search, not evidence of novelty.

### Error Log (domain checks)
| ID | Category | Location | Verbatim quote | Why | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|-----|--------------|-----------|----------|-----|
| DERR-1 | E7 | §5.1 | "evaluates behavior controllability and realism" | WOSAC [34] is a realism benchmark, not a controllability one | From knowledge of [34]; not in kept abstracts | Medium | MINOR | Correct the description `[verify]` |
| DERR-2 | E7 | §1, ref. [18–20] | "pre-training and fine-tuning” paradigm in large language models (LLMs) [18–20]" | The cited papers are preference/RL-for-reasoning methods | Cross-referenced with the bibliography entries | Medium | MINOR | Cite a pre-train/fine-tune reference |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Realism not measured; theory disconnected |
| Clarity | 2 | Gaps in method definition |
| Significance | 2 | Useful tool; weak evidence of benefit |
| Originality | 2 | Known components combined |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an incremental adaptation of GRPO/Dual-Clip to a head over fixed candidates, with "realism" asserted by metrics that need no human data.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Theory not tied to claims |
| Clarity & Presentation | 58 | Competent | Readable; framing clear |
| Novelty & Originality | 50 | Developing | Incremental over [21, 22] |
| Significance & Impact | 55 | Competent | Useful sub-area tool |
| Experimental Validation | 48 | Developing | No log-based realism; narrow baselines |
| Reproducibility | 60 | Competent | |
| Ethical Compliance | 65 | Competent | |

## Questions for Authors
1. Can you report WOSAC-style or log-likelihood realism for Pluto vs RIFT on nuPlan? Positive evidence would raise Novelty/Significance; a drop vs Pluto would lower both.
2. What exactly in RS [22] and RTR [21] prevents them from using all candidate trajectories?
3. Is "preserving multimodality" measured anywhere (diversity of executed behaviors, scoring-distribution entropy)?

## Limitations Assessment
**Partially.** Missing the realism-measurement limitation and the nuPlan→CARLA gap.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: sensible direction, but "realistic" and the novelty relative to [21, 22] are not demonstrated.
## Confidence
**4**: familiar with sim-agent benchmarks; literature search incomplete.

---

# Peer Review Report (Reviewer 3: Perspective)

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Reviewer: Dr. Anselm Bhattacharya, Perspective (transportation-safety and vehicle-dynamics lab; fictional persona)
## Expertise: surrogate safety measures; driver behavior modeling; vehicle controllers
## Date: 2026-11-10

## Summary
RIFT proposes to make the other road users in an AV test more human-like and steerable by RL-tuning a pre-trained generator. From a transportation-safety viewpoint, the interesting claim is that AV evaluation becomes "more reliable" in these scenarios (§5.3).

## Strengths
### S1: Candid analysis of execution-level discomfort
App. D.2 decouples planned trajectories from PID-executed actions and identifies discontinuous reference speeds amplified by binary throttle/brake as a cause of discomfort across all CBV methods. That is the kind of vehicle-dynamics reality check simulation papers usually omit.
### S2: Explicit reward styles
Table 6 and Fig. 6 make the reward → behavior mapping inspectable (normal vs aggressive), which is a sensible way to expose a "knob".
### S3: Downstream use in AV testing
Evaluating two AVs (rule-based PDM-Lite, learned PlanT) in §5.3 / Table 2 connects the method to its purpose rather than stopping at agent-level metrics.

## Weaknesses

### W1: Surrogate safety metrics are used inconsistently with how the paper reads them
§5.2 states RIFT "achieves superior safety performance, as reflected by higher 2D-TTC and ACT", reading higher as safer. Yet in Table 3 the *aggressive* reward, which raises ORR 0.36→0.91 and CPK 6.83→8.41, also *raises* 2D-TTC (+0.19) and ACT (+0.17). B.7 describes ACT as "reflecting the interaction intensity introduced by CBVs", a different reading. Values are also averaged with spreads of ±1.3–1.6 on means of 2.4–2.9 (Table 1) with no definition of the aggregation window. As defined, these metrics do not track the behavior they are used to rank, so the "safety" ordering in Table 1 is unreliable.
- **Suggested Fix**: define the aggregation (min per event vs mean), report a distribution or exceedance rate below a threshold (e.g., TTC < 1.5 s), and use collisions/near-misses with CIs as the safety statistic.

### W2: More benign scenarios are not "more reliable evaluation"
In Table 2 the PDM-Lite AV scores DS 94.78 with BR 0.00 under RIFT versus DS 77.84 / BR 23.33 under Pluto CBVs. A test generator that makes the AV nearly perfect may be less discriminative: nothing shows that RIFT scenarios separate AV quality better, remain interactive, or exercise failure modes. For PlanT the claim reverses: RIFT's IS is the lowest in the column (0.64) and DS is below GRPO-Pluto and REINFORCE-Pluto (44.28 vs 47.24, 45.25), so §5.3's "near-optimal Driving Score (DS), Route Completion (RC), and Infraction Score (IS)" holds for PDM-Lite only.
- **Suggested Fix**: show discriminative power (e.g., rank correlation of AV orderings with a ground-truth/hand-crafted adversarial suite) and report AV failure categories per generator.

### W3: Controllability is one scalar knob in one setting
"Controllable" is shown by one alternative reward style evaluated over the same ten routes and one qualitative stop-sign scenario (Fig. 6, D.1). Real controllability would be a multi-dimensional, user-specified target (e.g., desired gap acceptance or aggression level) with a measured response curve, ideally compared with baselines trained on the same two reward styles.
- **Suggested Fix**: sweep α_collision/α_velocity over 4–5 values and plot the behavior response for RIFT and the RL baselines.

### W4: Comfort and dynamics gaps undercut "realistic"
Table 7 (D.2) gives RIFT UCR 76.90 % (PDM-Lite) and 72.41 % (PlanT) versus Pluto 56.45 % and 50.26 %; only GRPO-Pluto (78.58 %) is worse. So CBVs are outside expert comfort bounds for about three quarters of the simulation time. The main text does not mention this; the text of D.2 attributes it partly to the reward model and the PID controller, which are outside the paper's claimed contribution but inside the "realistic" claim. The signed mean "Jerk" (values around 0 ± 4) is not a comfort measure (signs cancel).
- **Suggested Fix**: bring Table 7 into the main text, use |jerk| or RMS jerk, and apply a smooth tracking controller as a sensitivity check.

### W5: Scope assumptions
The framework needs fully observable vectorized input (§6 limitation) and a single CBV per route (§4.1) or a distance-to-goal set (B.2); neither the sim-to-real gap (App. E) nor the nuPlan→CARLA domain shift is quantified.
- **Suggested Fix**: add a 2–3 CBV scenario and a nuPlan→CARLA transfer diagnostic.

## Questions for Authors
1. How exactly are 2D-TTC and ACT aggregated over time and vehicles? If the aggressive style legitimately has higher TTC, what are these metrics measuring?
2. Do RIFT scenarios rank AVs the same way as a safety-critical adversarial suite? A yes would raise Significance.
3. Is a lower DS for the AV under a generator a desirable property (harder scenarios) or an undesirable one (unrealistic)? How do you decide?

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Metrics inconsistently interpreted |
| Clarity | 3 | Readable; honest appendix |
| Significance | 3 | Useful if validated |
| Originality | 2 | Known pieces |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically useful direction with transparent limitations, but its safety and evaluation-reliability claims rest on metrics that are not validated.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | |
| Clarity & Presentation | 62 | Competent | |
| Novelty & Originality | 55 | Competent | |
| Significance & Impact | 60 | Competent | Practical interest |
| Experimental Validation | 52 | Developing | |
| Reproducibility | 62 | Competent | |
| Ethical Compliance | 68 | Competent | Appendix E honest about sim-to-real gap |

## Limitations Assessment
**Partially.** App. D.2 and §6 are honest; the main text should carry them.

## Ethics Review Flag
**No**: simulation only; the sim-to-real gap is acknowledged (App. E).

## Overall Score
**3 (Borderline Reject)**: a useful direction whose headline evidence (safety metrics, AV-evaluation reliability) is not yet interpretable.
## Confidence
**3**: strong on safety metrics, less on RL fine-tuning details.

---

# Peer Review Report (Reviewer 4: Generalist)

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Reviewer: Dr. Camila Strand-Oyelaran, Generalist (ML group, mid-size research university; fictional persona)
## Expertise: deep RL and representation learning (not traffic simulation)
## Date: 2026-11-10

## Summary
The paper argues that traffic simulation needs both log-derived realism and steerability. It pre-trains a multimodal trajectory model on logs, then fine-tunes only the head that scores candidate trajectories with a GRPO-like loss and a user-chosen reward, and shows improved progress and safety-timing numbers in CARLA and better AV scores against its generated traffic.

## Strengths
### S1: Clear problem and tidy storyline
Fig. 1 and §1 present a clean realism–controllability trade-off and a modular fix. The problem matters for AV testing, and the sequence IL → RL is easy to follow.
### S2: Balanced baseline panel
Table 1 covers pure RL/IL, SFT, RLFT and hybrid baselines; RIFT is best or second best on 6 of 8 metrics (best on RP, 2D-TTC, ACT, Speed SW; second on WD and tied second on Acc SW), a verified summary of the table.
### S3: Cheap and honest
8 GPU-hours per run (B.4), explicit limitation paragraph (§6), and a comfort analysis (D.2) that admits where RIFT falls short.

## Weaknesses

### W1: The decisive implementation fact is buried
Only Fig. 2's caption says "only the trajectory scoring head is fine-tuned, with the rest of the pre-trained network kept frozen". The abstract and §1 describe fine-tuning "a trajectory generation model" with "preserves the trajectory-level multimodality". With the head-only design the candidate set is fixed by the frozen decoder and the executed trajectory is the arg-max ("The highest-scoring trajectory is selected for closed-loop execution", §4.2); "preserving multimodality" is then close to true by construction, and a reader unfamiliar with the Pluto decoder cannot tell what is actually learned.
- **Suggested Fix**: state this in the abstract and §1, and explain what multimodality exists at execution time.

### W2: Claims are written more strongly than the tables allow
"Extensive experiments demonstrate that RIFT significantly improves the realism and controllability" (Abstract) and "RIFT consistently outperforms all baselines in both aspects across most settings" (§5.2); "RIFT strikes a more favorable balance between safety and interactivity" is argued on 2D-TTC/ACT while the infraction columns favor several baselines (ORR 0.36 vs 0.06–0.10 for SFT/PPO-/GRPO-Pluto; CPK 6.83 vs Pluto 5.06). Evidence supports a narrower claim: best progress and speed-distribution scores with infraction rates in the range of the other fine-tuned baselines.
- **Suggested Fix**: align abstract, §5.2 and conclusion with the table (see R1 ERR-4).

### W3: Presentation of results hides variance and the evaluation set size
Seeds are mentioned in captions only; ±std are large (e.g., 2D-TTC 2.74 ± 1.30, CPK 6.83 ± 2.62); dev10 appears only in App. B.4; "best and second-best" highlighting cannot be checked without it. A non-specialist cannot judge whether differences are real.
- **Suggested Fix**: put the evaluation size and what a seed is in §5.1, and state which differences exceed the spread.

### W4: Venue fit and ICLR audience
The ML contribution (dual-clip + group advantage on a scoring head) is small and its theory (App. A) is detached from the experiments; the domain contribution (CARLA CBV pipeline) is solid engineering. ICLR readers will ask for what generalizes: a statement of which part transfers to other candidate-ranking policies.
- **Suggested Fix**: add one experiment on a second domain or a second pre-trained model, or position the paper as an application.

**Minor:** "Fine-tune initial LR 1 × e−4" (Table 4) should read 1×10⁻⁴; "GPRO" typo (D.2); Table 3's missing minus sign (ERR-2); "iteraction" in Algorithm 1.

## Questions for Authors
1. Is the candidate distribution a softmax over scores? What is G (N_ref)?
2. Which two or three design choices would you keep if a reviewer made you drop one component?
3. Is the benchmark (CBV generation on Bench2Drive) going to be released?

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid but uneven evidence |
| Clarity | 3 | Mostly clear; key fact buried |
| Significance | 3 | Practical interest |
| Originality | 2 | Known components |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a complete, readable application paper with a broad baseline panel and honest limitations, whose weaknesses (3 seeds, narrow evaluation) are common among accepted ML-for-driving papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | |
| Clarity & Presentation | 66 | Competent | |
| Novelty & Originality | 58 | Competent | |
| Significance & Impact | 64 | Competent | |
| Experimental Validation | 60 | Competent | |
| Reproducibility | 62 | Competent | |
| Ethical Compliance | 68 | Competent | |

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**

## Overall Score
**4 (Borderline Accept)**: a practical, readable application paper whose reasons to accept (useful pipeline, broad baselines, candor) narrowly outweigh its overclaiming.
## Confidence
**3**: not a driving specialist; did not re-derive the proofs.

---

# Devil's Advocate Report

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Reviewer: Prof. Jun-ho Albrecht-Nwosu, Devil's Advocate (evaluation-methodology researcher; fictional persona)

## Steelman
Fine-tuning only the scoring head of a log-pretrained model with a reward that encodes user preferences is a cheap way to steer a realistic prior toward a desired driving style. Against matched-head baselines, RIFT gets the highest route progress and speed-distribution scores, and AVs run through its CBVs obtain high driving scores with few blocks, suggesting a usable test generator.

## Core Argument Chain
1. IL pre-training on nuPlan yields realistic, multimodal candidate trajectories (C1).
2. Fine-tuning only the scoring head with group-relative advantage preserves that realism and multimodality (C2).
3. Dual-clip in place of KL stabilizes training and increases controllability (C2).
4. SW normality, WD to target speed and the infraction/progress metrics measure realism and controllability (C3).
5. Higher AV scores and fewer blocks under RIFT show more reliable AV evaluation (C3).
∴ RIFT yields realistic, controllable scenarios and a robust platform for AV evaluation.

## Strongest Counter-Argument
Steps 1 and 4 are not tested, and steps 2 and 3 are not isolated. Realism is measured by (a) a normality test on speed and acceleration and (b) distance to the simulator's configured target speed (§5.1, B.7). Neither compares anything to human data; B.7 states there are none ("without expert demonstrations"). A policy that tracks the target speed with Gaussian jitter scores best on both, and the reward (Table 6: velocity, centering, comfort terms) is largely what these metrics and RP and the collision statistics reward, so the winner is the method that optimizes the reward best. The only part of the pipeline that comes from real data is the downloaded Pluto checkpoint, whose realism is never evaluated before or after fine-tuning, and in CARLA it operates outside its training distribution. Meanwhile, the one experiment that touches real-world-like behavior (App. D.2, Table 7) shows RIFT among the *least* comfortable CBVs (UCR 76.90 % vs 56.45 % for the un-fine-tuned model). For the AV-evaluation claim, the evidence is that the AV looks *better* under RIFT (DS 94.78 vs 77.84, BR 0.00 vs 23.33). That is what one would also see if RIFT's CBVs were simply more yielding; it is not evidence of reliability, and for PlanT the effect disappears or reverses (IS 0.64, the lowest). Finally, the paper credits KL removal and dual-clip for the gains but never runs RIFT with KL, and its closest controlled comparison (GRPO-Pluto) differs in two respects and is within one standard deviation on most metrics. The surviving claim is therefore: "RL fine-tuning of a scoring head with a hand-built reward increases progress and smooths speed distributions in CARLA", not "realistic and controllable" scenario generation.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main weakness (realism and evaluation-reliability claims not supported by their metrics) survives in a narrower form that the data do support (progress and speed-distribution improvements from RL fine-tuning of a scoring head under a given reward); the fix is to narrow the claim and add log-based realism, which is MAJOR.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (E5) | Abstract; §5.1; App. B.7 | "Realism" is measured with normality (Shapiro–Wilk) and distance to a simulator target speed, not against human behavior. Evidence supports "speed-distribution smoothness/target tracking", not "realistic". Not contradicted. | Add log-based realism (nuPlan/WOSAC-style) or narrow the claim |
| DA-M2 | Logic | §5.3, Table 2 | AV-evaluation "reliability" is inferred from the AV performing better and fewer blocks; this is equally explained by yielding CBVs, and the claim fails for PlanT (IS 0.64 lowest; DS 44.28 < 47.24). | Show discriminative power and AV failure categories |
| DA-M3 | Attribution | §4.2; Table 1; Table 3 | KL removal and group advantage are credited but not ablated; GRPO-Pluto differs in two respects and is within noise on most metrics; no learning curves for "stability". | See R1-W1 |
| DA-M4 | Logic/Theory | App. A (Eq. 14, Thm A.4) | Theorem A.4(c) is claimed without c appearing in Φ(p); the contraction is assumed; the maximized surrogate Φ(p) = 2ε√(p(1−p)) is maximized at p = ½, so the "fixed point" of a gradient step is not a high-success policy. The theory does not support "guaranteeing stable learning". | Remove or restate; prove a result involving c and the actual objective |
| DA-M5 | Statistics | Tables 1–2; App. B.4 | Evaluation on dev10 with 3 seeds; BR values quantized to 3.33; "BR 0.00" is 0 vs 2 events for GRPO-Pluto (derived); no tests. | More routes, CIs, training-seed variance |
| DA-M6 | Overclaim | §5.2 | "RIFT consistently outperforms all baselines …" is false on ORR, CPK, Acc SW (see ERR-4). | Narrow the wording |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 3, App. D.1 | Aggressive reward raises 2D-TTC/ACT (+0.19/+0.17) while raising collisions; "higher TTC = safer" (§5.2) is then inconsistent |
| DA-m2 | Presentation | Table 3 | RP delta missing minus sign |
| DA-m3 | Reporting | Table 7 | Signed mean "Jerk" is not a comfort statistic |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| RIFT RP gain over GRPO-Pluto | 995.33 vs 892.65 | +102.68 (+11.5 %) | Yes (std 84.62 / 65.27) |
| Table 3 PPO-Clip deltas | RP 655.39 (−339.94) | 995.33 − 339.94 = 655.39 | Yes |
| Table 3 All-head RP delta | 827.12 (168.21) | 995.33 − 827.12 = 168.21, sign should be negative | Sign missing |
| RIFT CPK vs Pluto | 6.83 vs 5.06 | +1.77 (+35 %) worse | Not "outperforms all" |
| Table 2 PDM-Lite DS, RIFT vs REINFORCE-Pluto | 94.78 vs 92.17 | +2.61 < 3.45 std | Within noise |
| Table 2 BR 0.00 vs GRPO 6.67 | | consistent with 0 vs 2 events of 30 (derived) | Not significant |

## Ignored Alternative Explanations
- Yielding or slow CBVs produce high AV DS and low BR without being realistic or reliable (Table 2).
- Reward-metric overlap (Table 6 vs RP/WD/CPK) explains the winner without any realism gain.
- Head-only fine-tuning keeps the decoder candidates, so "preserving multimodality" holds by construction.
- Evaluation-AV and SFT teacher are the same planner (PDM-Lite).

## Missing Stakeholder Perspectives
AV test engineers who need *adversarial yet plausible* behavior, not benign flow; safety assessors who need statistically meaningful event counts.

## Observations (Non-Defects)
Matched-head baselines; signed ablation deltas whose arithmetic is right; an open comfort analysis (D.2); a clear statement of the state-wise reward limitation (§6). The core engineering is robust against the strongest objection in its narrow form.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 45 | Theory detached; mechanism not isolated |
| Clarity & Presentation | 55 | Overclaiming wording |
| Novelty & Originality | 45 | Known components |
| Significance & Impact | 48 | Evidence of benefit unclear |
| Experimental Validation | 42 | Metrics do not measure the claims |
| Reproducibility | 58 | Hyperparameters given; code not stated |
| Ethical Compliance | 62 | Limitations present |

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 attribution not isolated | kept | Verified against Table 1/3, B.5 |
| R1 | W2 statistics | kept | dev10 stated in B.4; quantization is derived and labelled so |
| R1 | W3 baselines/teacher entanglement | kept | B.5 quotes verified |
| R1 | W4 definition gaps | kept; (iv) N_ref moved to Questions | N_ref not stated, appendix searched |
| R1 | W5 reward–metric overlap | rewritten as inference | Reward terms (Table 6) vs metrics (B.7) verified; effect size is an inference |
| R1 | ERR-1 (Eq. 8) | kept as Medium confidence | Depends on implementation; App. Eq. 18 restricts to Â<0 |
| R2 | W1 realism | kept | B.7 quote verified; WOSAC description marked `[verify]` |
| R2 | W2 novelty | rewritten | Statement of prior work limited to what the paper itself says about [21, 22] |
| R2 | W3 missing comparisons | kept as MAJOR at most | No verified prior-labelled missing baseline |
| R2 | W4 theory | kept | Eq. 14 and Thm A.4 verified |
| R2 | W5 citation accuracy | moved to Minor | Cosmetic |
| R3 | W1 metric reading | kept | Table 3 vs §5.2 verified |
| R3 | W2 benign scenarios | kept | Table 2 verified |
| R3 | W3 controllability | kept | |
| R3 | W4 comfort | kept | Table 7 verified |
| R3 | W5 scope | kept | |
| R4 | W1 buried fact | kept | Fig. 2 caption, §4.2 verified |
| R4 | W2 overclaim | kept | |
| R4 | W3 variance presentation | kept | |
| R4 | W4 venue fit | rewritten | Judgment, not an error |
| DA | M1–M6 | kept | All checked at location |

---

# Phase 2: Synthesizer Part A (package for the EIC)

**Issue list and classes**
| Issue | Sources | Class |
|-------|---------|-------|
| Realism not measured against human behavior; metrics circular | R2-W1, R1-W5, DA-M1, R3-W4 (partly) | CONSENSUS-4 |
| Group advantage/KL/dual-clip not isolated, theory disconnected | R1-W1, R2-W4, DA-M3, DA-M4 | CONSENSUS-3 |
| Thin statistics, dev10, 3 seeds | R1-W2, R4-W3, DA-M5 | CONSENSUS-3 |
| Overclaim vs Table 1/2 | R1-ERR-4, R4-W2, DA-M6, R3-W2 | CONSENSUS-4 |
| AV-evaluation reliability not shown | R3-W2, DA-M2 | CONSENSUS-2 |
| Safety metric (TTC/ACT) misread | R3-W1, DA-m1 | CONSENSUS-2 |
| Baseline entanglement with PDM-Lite | R1-W3 | SOLO |
| Method undefined (π_θ, N_ref) | R1-W4, R4-Q1 | CONSENSUS-2 |
| Comfort failure of RIFT | R3-W4 | SOLO |
| DA-CRITICAL | none | n/a |

**Hinging issues:** realism metrics; AV-evaluation reliability; isolation of the RIFT components.
**Official ratings:** R1 3, R2 3, R3 3, R4 4, DA 2 → mean 3.00; official composite 55.1 (script, before EIC weights). Pool positions 38/42/52/66/33. No warnings.

---

# Phase 2: EIC Meta-Review

## The Case For and Against
- **For acceptance:** A cheap, practical recipe that steers a log-pretrained trajectory model with a user reward, with a matched-head baseline panel, ablations and an honest comfort/limitation analysis; best progress and speed-distribution numbers among fine-tuned baselines; downstream AV evaluation shows a usable pipeline.
- **Against acceptance:** The title claims (realistic, controllable, reliable AV evaluation) are measured with metrics that cannot establish them; the components credited in the abstract (KL→dual-clip, group advantage) are not isolated and differences vs GRPO-Pluto are mostly within noise; evaluation is ≈10 routes × 3 seeds; PlanT results and comfort results contradict the prose; theory does not support its stated conclusion.

## Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Realism measured by SW normality and WD to target speed; no human data | R2-W1, DA-M1 | §5.1; App. B.7 | Verified | B.7: "without expert demonstrations" |
| RIFT best on 4 of 8 Table 1 metrics; "consistently outperforms all baselines" overstated | R1-ERR-4, R4-S2, DA-M6 | Table 1; §5.2 | Verified | R4's "6 of 8 best or second" also correct |
| ORR/CPK worse than Pluto; WD tie with PPO | R1, DA | Table 1 | Verified | 0.36 vs 0.24; 6.83 vs 5.06; 4.46 vs 4.45 |
| "near-optimal DS, RC, IS … lowest BR" fails for PlanT | R3-W2, DA-M2 | Table 2; §5.3 | Verified | IS 0.64 lowest; DS below GRPO and REINFORCE |
| Eq. 8 gives zero gradient for Â>0 as printed | R1 ERR-1 | Eq. 8, Table 5; App. Eq. 18 | Partly correct | True as printed; App. Eq. 18 restricts to Â<0, likely notation |
| Thm A.4(c) not derived; c absent from Φ; contraction assumed | R2-W4, DA-M4 | Eq. 14; Thm A.4 | Verified | Garbled A.4 layout, but statements legible |
| Aggressive reward raises 2D-TTC and ACT | R3-W1, DA-m1 | Table 3 | Verified | +0.19, +0.17 |
| Dev10 evaluation; BR quantization → 0 vs 2 events | R1-W2, DA-M5 | App. B.4; Table 2 | Partly correct | dev10 stated; quantization/event count is derived, not stated |
| RIFT UCR 76.90 % vs Pluto 56.45 % | R3-W4 | Table 7 | Verified | Appendix only |
| §4.1 single CBV vs B.2 set | R1-ERR-3 | §4.1; App. B.2 | Verified | |
| π_θ(τ\|s) undefined for scoring head | R1-W4 | §4.2, Eq. 5–8 | Verified | |
| WOSAC "evaluates behavior controllability" | R2 DERR-1 | §5.1 | Partly correct | Quote verified; the characterization of WOSAC rests on knowledge `[verify]` |
| Table 3 All-head RP sign | R1 ERR-2 | Table 3 | Verified | Minor |
| DA: "BR 0.00 shows scenarios are benign" | DA-M2 | Table 2 | Overstated | An alternative reading (CBVs interact less) is also possible; the paper's own argument is equally unsupported |

## Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error log and recomputations hold; ERR-1 flagged with the right caveat |
| R2 (Domain) | 3 | 4 | 1.0 | Realism and theory points verified; WOSAC statement unverifiable from the text |
| R3 (Perspective) | 3 | 3 | 1.0 | Verified points on TTC, Table 2 and Table 7; sound |
| R4 (Generalist) | 4 | 3 | 0.75 | Accurate on table counts, but calibration is lenient: does not engage with the metric-validity problem, and a pool position of 66 is not supported by the verified issues |
| DA | 2 | 4 | 1.0 | Arguments survived the check; the benign-scenario inference is overstated but not decisive |

## DA-CRITICAL Rulings
The DA raised no CRITICAL issue and I found none that meets the strict criteria. The realism and evaluation-reliability issues would be criterion 2 only if no weaker claim survived; the data do support progress and speed-distribution improvement under the stated reward, so they remain MAJOR (narrow the claim). No DA ceiling applies.

## Final Decision and Justification
Official ratings are R1 3, R2 3, R3 3, R4 4, DA 2 (mean 3.00). The EIC-weighted rating, with confidence × quality weights, is 2.92, and rounds to the starting point **3**. The composite cross-check (54.2, band 3) agrees, and the script shows no warning. I keep the starting point. No verified issue is missing from the ratings that would justify moving up: R4's more favorable rating rests on reasons that I verified (clear story, broad baselines, candor) but it does not account for the verified metric-validity and attribution problems. I also found no verified point that would move it down: the Eq. 8 problem is probably notational and the DA's CRITICAL bar is not met. My own pool position is about **45**: the contribution is a competent adaptation with a useful pipeline, but its three headline claims are each narrower in the evidence than in the words, and a typical rejected submission at ICLR shares that profile; accepted papers usually have at least one component that is cleanly isolated, which this one lacks. Confirmed not above the DA ceiling (none). In ICLR terms the script gives rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); the ICLR scale status is *secondary*, so verify against the current form.
**Final Overall: 3 (Borderline Reject).** A revised version that adds log-based realism, a KL/group-advantage ablation and a larger evaluation could move to 4–5.

---

# Editorial Decision

## Paper: RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Ingrid Valsamaki; R1 Methodology Dr. Tomasz Okonkwo-Reyes, R2 Domain Prof. Mei-Lin Harrington, R3 Perspective Dr. Anselm Bhattacharya, R4 Generalist Dr. Camila Strand-Oyelaran, DA Prof. Jun-ho Albrecht-Nwosu

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 3, R4 4, DA 2 → mean 3.00 · official composite 55.1
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 54.2 (band 3, agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR rating (secondary scale):** see aggregate.json (printed below in the score block).

## Score Summary

### Official Scores and EIC Assessment (before = official raw mean; after = EIC-weighted; see `before.json`, `aggregate.json`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 52 | 56 | 62 | 45 | 53.0 | see aggregate.json | 17 |
| Clarity & Presentation | 55 | 58 | 62 | 66 | 55 | 59.2 | | 11 |
| Novelty & Originality | 48 | 50 | 55 | 58 | 45 | 51.2 | | 13 |
| Significance & Impact | 52 | 55 | 60 | 64 | 48 | 55.8 | | 16 |
| Experimental Validation | 45 | 48 | 52 | 60 | 42 | 49.4 | | 18 |
| Reproducibility | 60 | 60 | 62 | 62 | 58 | 60.4 | | 4 |
| Ethical Compliance | 65 | 65 | 68 | 68 | 62 | 65.6 | | 6 |
| **Composite** | 52.0 | 54.1 | 58.1 | 62.3 | 48.9 | **55.1** | **54.2** | |

No dimension has a spread above 20.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 (from the script's venue-weighted composite, 54.4) |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); verify against the current form |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation" to ICLR. Building steerable, closed-loop traffic agents from a log-pretrained model is a worthwhile goal for AV testing.

**Overall Assessment:** The panel found a practical, inexpensive pipeline with a sensible baseline panel and unusually candid appendices. It also found that the three headline claims (realism, controllability, reliable AV evaluation) are supported by metrics that cannot establish them as worded, and that the components credited for the gains were not isolated experimentally.

**Key Strengths Identified by Reviewers:**
1. Matched-head fine-tuning baselines and signed ablation deltas (R1, R4).
2. Honest comfort and limitation analysis (R1, R3, R4).
3. A relevant, well-motivated problem with a cheap training recipe (R2, R3, R4).

**Key Concerns Requiring Attention:**
1. "Realism" is measured by normality and distance to a simulator target speed, with no comparison to human data (R2, DA, R1; CONSENSUS-4).
2. KL removal, dual-clip and group-relative advantage are not ablated; theory in App. A does not support its conclusion; Eq. 8 as printed needs correction (R1, R2, DA; CONSENSUS-3).
3. Evaluation on dev10 with three seeds; wording ("consistently outperforms") exceeds Tables 1–2, notably for PlanT (R1, R3, R4, DA).

**Decision: Borderline Reject (3).** The panel sees a reasonable contribution whose evidence does not yet match its claims. Narrowing the claims, adding log-based realism, isolating the RIFT components and enlarging the evaluation would change the assessment.

Sincerely,
Dr. Ingrid Valsamaki, Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Realism claim not supported by metrics | R2, R1, DA, R3 | CONSENSUS-4 |
| Overclaim vs Tables 1–2 | R1, R3, R4, DA | CONSENSUS-4 |
| Components not isolated; theory detached | R1, R2, DA | CONSENSUS-3 |
| Thin statistics / small evaluation set | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the paper above the ICLR bar? | R4 (4) | R1, R2, R3 (3), DA (2) | The EIC sides with the majority because R4's reasons do not cover the verified metric-validity issues |
| Is Eq. 8 an error? | R1 | (none) | Likely notational; confirm in code (Priority 2) |

### Score Spread Discussion
No dimension exceeded the 20-point spread flag. The largest spread is Experimental Validation (18): R4 gives 60 because baselines are broad; R1/DA give 42–45 because the metrics and statistics cannot support the claims. The EIC adopts the latter after verifying Table 1/2/3 and B.7.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Realism measured without human data | Yes (R2-W1, R1-W5) | n/a | New experiments (log-based metrics) or narrowing the claim |
| DA-M2 | MAJOR | AV-evaluation reliability not shown | Yes (R3-W2) | n/a | New analysis/experiments |
| DA-M3 | MAJOR | RIFT components not isolated | Yes (R1-W1) | n/a | New ablations |
| DA-M4 | MAJOR | Theory disconnected | Yes (R2-W4) | n/a | Rewrite |
| DA-M5 | MAJOR | Evaluation size/statistics | Yes (R1-W2) | n/a | New evaluation |
| DA-M6 | MAJOR | Overclaim in §5.2 | Yes (R1-ERR-4, R4-W2) | n/a | Rewording |
(No DA-CRITICAL issue.)

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | "Realistic" not evidenced against human behavior | R2-W1, DA-M1, R1-W5 | Abstract; §5.1; App. B.7 | Add log-based realism (nuPlan/WOSAC-style) for Pluto vs RIFT, or narrow to "kinematic plausibility in CARLA" | Medium–High; ≈ 20–40 GPU-h or rewording | Partly |
| R2 | RIFT components not isolated | R1-W1, DA-M3 | §4.2; Table 1/3 | Add RIFT + KL, executed-trajectory advantage, learning curves; ≥ 5 training seeds | High; ≈ 160 GPU-h | Partly |
| R3 | Evaluation too small; claims exceed tables | R1-W2, DA-M5, DA-M6, R4-W2 | §5.2–5.3; Tables 1–2; B.4 | State seed semantics; ≥ 50 routes; CIs; reword "consistently outperforms" and §5.3 "near-optimal" | Medium; 30–60 GPU-h | Rewording yes; reruns partly |

### Priority 2: Strongly suggested
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | AV-evaluation reliability unshown | R3-W2, DA-M2 | Discriminative-power analysis; AV failure categories; PlanT discussion | Medium | Partly |
| S2 | Surrogate safety metrics misread | R3-W1, DA-m1 | Define aggregation; use exceedance rate / near-miss; reconcile Table 3 | Low | Yes |
| S3 | Method definition gaps and Eq. 8 | R1-W4, ERR-1 | Define π_θ for the scoring head; sign condition; N_ref; ε in std | Low | Yes |
| S4 | Theory disconnected | R2-W4, DA-M4 | Restate or prove a result involving c; state the binary-reward limitation | Medium | Yes (rewrite) |
| S5 | Baseline entanglement and tuning | R1-W3 | Evaluate SFT/hybrid baselines with a non-teacher AV; report tuning effort | Medium | Partly |
| S6 | Novelty vs [21, 22, 43–45]; missing comparisons | R2-W2, R2-W3 | Comparison table; one CAT-K-style baseline | Medium | Partly |
| S7 | Controllability evidence | R3-W3 | Multi-value reward sweep with RIFT and baselines | Medium | Partly |
| S8 | CBV definition inconsistency | R1-ERR-3 | One definition (§4.1 vs B.2) | Low | Yes |

### Priority 3: Nice to fix
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Comfort results only in appendix; signed jerk | R3-W4 | Move Table 7 to main text; use RMS jerk |
| N2 | Buried head-only design | R4-W1 | State in abstract/§1 |
| N3 | Citations [18–20], [59], WOSAC description | R2-W5 | Correct |
| N4 | Table 3 sign; typos | R1 ERR-2, R4 | Fix |
| N5 | Additional references | R2 | Discuss Shiroshita et al. 2020 and DPPO `[verify]` |

## Estimated Revision Effort
- Priority 1: 3 items, ≈ 1–2 weeks (≈ 200–250 GPU-h plus writing)
- Priority 2: 8 items, ≈ 1 week
- Priority 3: 5 items, ≈ 1 day
- **Total estimated revision time**: ≈ 3 weeks

*The Gap Scout (Post-Review Analysis) was not requested and was not run.*
