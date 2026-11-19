# Simulated Review: "Sample-efficient and Scalable Exploration in Continuous-Time RL"

Date: 2026-11-05 · Mode: full · Target venue: ICLR (profile `iclr`, 2026 cycle, scale status *secondary*) · Literature check: strict, cutoff 2025-09-24
*This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome. Figures were not available (text extraction only); figure-dependent claims are judged from captions and text and flagged where it matters.*

---

# Phase 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Sample-efficient and Scalable Exploration in Continuous-Time RL |
| Primary Discipline | Machine learning → model-based reinforcement learning (continuous-time, exploration) |
| Secondary Discipline(s) | Optimal control / nonlinear systems; Gaussian-process bandit theory; active learning / system identification |
| Paper Type | Empirical (method + benchmark evaluation), with a substantial theory component (composite weights: empirical) |
| Core Technique(s) | Reward + epistemic-uncertainty objective (COMBRL); GP and probabilistic-ensemble dynamics; iCEM / SAC planning; measurement selection strategies (MSS) and TaCoS |
| Target Venue | ICLR (top-tier ML conference) (stated); profile key `iclr` |
| Venue-Specific Notes | none (ICLR: public reviews, authors may upload revisions during discussion; ≈27% accepted share of submissions) |
| Paper Maturity | Submission-ready (full appendix, code link) |
| Ethics-Relevant Content | none (simulated control benchmarks only) |

### Claimed Contributions (as stated by the authors)
1. **C1** — COMBRL: a continuous-time optimistic MBRL algorithm that balances reward and epistemic uncertainty with one scalar λ, covering reward-driven and unsupervised learning (Abstract; §1 Contributions; §3, Eq. 3, Algorithm 1).
2. **C2** — Sublinear regret in the reward-driven case, in terms of model complexity I_N (Theorem 1, §3.3; proof in App. B).
3. **C3** — A sample-complexity bound for the unsupervised case (λ→∞) (Theorem 2, §3.3; App. B).
4. **C4** — Strong empirical results: "scales better", "more sample-efficient than prior methods", outperforms baselines on deep RL tasks, generalizes to unseen downstream tasks, and works with adaptive sensing (TaCoS) (Abstract; §4, Figures 1–5).

### Paper memory (shared factual record)
- **Setup facts.** No train/val/test split (RL; evaluation in the training environment). Seeds: 5 (Figure 1), 10 (Figure 2, Figure 5/6); **not stated** for Figures 3 and 4. GP experiments use two self-implemented continuous-time tasks (App. C.1, Table 1: N=12/15 episodes, ν=20/1 s⁻¹); deep experiments use Gym/DMC with a 5-member ensemble, SAC, finite-difference derivative estimates, synthetic-transition augmentation, soft resets (App. C.4, Table 4). λ: hand-tuned/static (C.1, Table 1: 1.0 and "106"), auto-tuned following MaxInfoRL (C.3, Eq. 8), per-environment "optimized" values (Table 5). Compute: RTX 2080 Ti (Table 3). Code: project website + repository.
- **Headline numbers.** "roughly 3× lower computational cost" than OCORL (Figure 1 caption; Table 3: 10.8 vs 30.6 min; 1.29 vs 4.55 h). No other numbers in abstract/introduction; all other results are curves/bars (not readable from text).
- **Appendix adds.** Related work (A), assumptions restated and GP analysis, Theorem 3 (QP projection), Lemmas 4–5, proofs of Theorems 1–2 (B), hyperparameters and task definitions (C), TaCoS details and Figure 6 (C.6).
- **Unverifiable.** All figure content (Figures 1–6); some equations are partly garbled in extraction but the statements used below are legible.

### Integrity signals
Manual scan of the manuscript text for text addressed to reviewers or AI systems: **none found** (`scripts/integrity_scan.py` was not run: the evaluation rules limited tool use to file access and the aggregation/search scripts). The literature-check `similarity` run flagged **text overlap** between the opening sentence of this paper's abstract and that of a cited prior paper (Treven et al., "Efficient Exploration in Continuous-time Model-based Reinforcement Learning", https://arxiv.org/abs/2310.19848): 3 shared 8-word sequences (e.g., "are often continuous in time in this paper"), cosine 0.31. The prior paper is cited throughout and is the closest baseline; overlap in a one-sentence motivation is reported factually for the editor and changes no score. A project-website link and a repository name are visible in the text (§1; Reproducibility Statement), which a double-blind venue may regard as a non-anonymized link; author identities were not considered in any score.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Helena Varga-Ndlovu, public research university (Central Europe)
- **Seniority / Expertise**: senior faculty / learning-based control, exploration theory, RL evaluation. 
- **Role**: reads all five reviews, checks decisive points against the paper, weights reviewers, decides.
- **Style**: wants the decisive claim tested directly; tolerant of ordinary weaknesses, intolerant of untested headline claims.

### Reviewer 1 (Methodology): Dr. Ilse Brandvold, industrial research lab (Northern Europe)
- **Seniority / Expertise**: mid-career industry scientist / deep model-based RL evaluation, RL statistics, ensemble uncertainty.
- **Review Focus**: design, statistics, fairness of comparison, reproducibility.
- **Style**: insists on matched tuning and compute across baselines; re-derives key proof steps.

### Reviewer 2 (Domain): Prof. Daichi Morales-Ferrante, public research university (East Asia)
- **Seniority / Expertise**: senior faculty / regret theory for GP-based RL and bandits, optimism-based exploration.
- **Review Focus**: literature, theoretical framework, domain contribution.
- **Style**: compares each theorem to the nearest published bound.

### Reviewer 3 (Perspective): Dr. Priya Anand-Whitcombe, engineering department, large public university (North America)
- **Seniority / Expertise**: associate professor / event-/self-triggered control, system identification, robotics.
- **Review Focus**: cross-disciplinary links, deployment, assumptions, broader impact.
- **Style**: constructive; asks what happens on real hardware.

### Reviewer 4 (Generalist): Dr. Lucas Ferreira Okafor, ML group at a mid-size university (South America)
- **Seniority / Expertise**: postdoc / representation learning and RL applications (not exploration theory).
- **Review Focus**: contribution clarity, venue fit, presentation.
- **Style**: typical PC member; weighs contribution against ordinary weaknesses.

### Devil's Advocate: Dr. Sana Haddad-Lindgren, statistics and evaluation methodology group (Middle East / Northern Europe)
- **Seniority / Expertise**: mid-career / evaluation methodology, causal attribution of gains, ablation design.
- **Review Focus**: core-argument challenges, logic, overclaiming.
- **Style**: asks "what would the result look like if the claimed mechanism were irrelevant?"

*Personas are fictional. Reviewers read the manuscript (no injected text was found, so the redacted copy equals the original) plus the paper memory; the five passes below were performed one after another in one model context, not by independent agents.*

---

# Phase 1 — Independent Reviews

*(Five role-based passes that share one model context; independence was preserved by writing each report without reference to the others.)*

---

# Peer Review Report

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Reviewer: Dr. Ilse Brandvold, Reviewer 1 (Methodology) (industrial research lab; fictional persona)
## Expertise: deep model-based RL evaluation; RL statistics; ensemble uncertainty
## Date: 2026-11-05

---

## Summary
The paper proposes COMBRL, which plans in a learned continuous-time model with a reward-plus-epistemic-uncertainty objective (Eq. 3, Algorithm 1), controlled by a scalar λ. For GP dynamics it gives a regret bound in terms of model complexity (Theorem 1) and, with λ→∞, an uncertainty-reduction bound (Theorem 2). Experiments compare against a mean planner, PETS and OCORL on two low-dimensional GP tasks (Figure 1), against the mean planner and PETS with ensemble models on Gym/DMC tasks (Figure 2), on zero-shot downstream tasks (Figure 3, Figure 4), and in the adaptive-sensing TaCoS setting (Figure 5).

## Strengths

### S1: Simple, implementable objective with a clear knob
Eq. 3 and Algorithm 1 are short, and §3.2 distinguishes greedy, balanced and unsupervised regimes with static, annealed and auto-tuned λ. This makes the method easy to reproduce and ablate (Figure 4).

### S2: Broad evaluation axes
The study covers GP and ensemble models, reward-driven and zero-shot settings, and an adaptive-sampling variant (Figure 5, App. C.6), with 10 seeds and standard errors in Figures 2 and 5. Self-implemented GP tasks are disclosed (App. C.1).

### S3: Useful reporting of cost and settings
Table 3 reports training time with standard errors and hardware; Tables 1, 2, 4, 5, 6 give hyperparameters; code is linked (Reproducibility Statement).

## Weaknesses

### W1: The analyzed algorithm is not the evaluated algorithm (MAJOR)
Theorem 1 is proven for planning with a Lipschitz model f_n obtained from the QP in Eq. 6 (Theorem 3) and for λ_n set as in Lemma 4 (a multiple of β_n, L_r and e^{L*(1+L_π)T}). The experiments plan with the posterior mean ("using µn works well", §3.1; footnote 2: "Even though the mean model might not lie in Mn−1 ∩ F"), use a 5-member ensemble whose uncertainty is raw member disagreement (App. C.4, no re-calibration although §2.3 says "re-calibration techniques (Kuleshov et al., 2018) can be used"), and use λ values from 0.17 to "106" (Table 5, Table 1). Eq. 6 is not mentioned in §4 or App. C. In addition, §3.3 states "hence |Sn| must increase with n", yet Table 1 fixes ν (50 measurements per episode for Pendulum-GP, 200 for MountainCar-GP; derived from T×ν) so the per-episode budget is constant. The guarantees therefore say little about the reported runs.
- **Suggested Fix**: State plainly that the guarantees cover the GP/QP variant; add a GP experiment that actually solves Eq. 6, uses the prescribed λ_n and a growing MSS (even at toy scale, a few GPU-hours), or show how far the deployed algorithm departs.

### W2: Baseline coverage and tuning parity in the deep-RL experiments (MAJOR)
OCORL appears only in Figure 1 (two low-dimensional tasks) and in Figure 5. Figures 2–4 compare only against a mean planner and PETS. The closest method named in the paper, the discrete-time Sukhija et al. (2025b) (§2.1), and the auto-tuning method it borrows (Sukhija et al., 2025a) are never run as baselines, nor is any strong deep MBRL method cited in App. A.1 (e.g., TD-MPC2, DreamerV3). App. C.4 says COMBRL uses synthetic-transition augmentation, a raised update-to-data ratio and soft resets, but never says the mean-planner/PETS baselines receive the same SAC budget, UTD, resets and tuning effort. λ is hand-tuned or per-environment "optimized" (Table 5), with no matched tuning for baselines (e.g., exploration noise).
- **Suggested Fix**: Add the discrete-time counterpart and a plain-bonus ablation (same code, discrete-time model), and state the UTD/reset/tuning budget for each baseline. About 3 methods × 8 tasks × 5 seeds on existing code.

### W3: "Scales better" rests on a runtime ratio on two tiny systems (MAJOR)
The scalability claim (Abstract; §4: "Thus our algorithm scales better and is more computationally efficient than the state of the art") is supported by Table 3 only: 10.8 ± 0.13 vs 30.6 ± 0.4 min (2.83×, derived) and 1.29 vs 4.55 h (3.53×, derived), on a 3-dimensional and a 2-dimensional state. There is no sweep over state/action dimension and no OCORL run on any Gym/DMC task, so the dependence of the gap on dimension (the claimed mechanism: du→du+dx reparametrization, §3.1) is untested. Table 3 also mixes "total training time" (Pendulum) with "training time per episode" (MountainCar) in footnotes a/b.
- **Suggested Fix**: Report time vs. d_x on a family of systems (e.g., chain of pendulums) for COMBRL and OCORL, or soften the claim to "≈3× cheaper on two low-dimensional tasks".

### W4: Statistical reporting is incomplete for the main claims (MAJOR)
The number of seeds is not stated for Figures 3 and 4. The claim that the unsupervised variant "performs best on the downstream task across all seven evaluated domains" (§4) rests on bar/curve figures with standard errors, with no table of final returns and no aggregate measure (e.g., normalized scores with bootstrap CIs). "Sample-efficient" is never quantified (no episodes-to-threshold); Figure 5 shows only final returns.
- **Suggested Fix**: Add a table of final and area-under-curve returns with n and CIs for Figures 2–5; state seeds for Figures 3–4.

### W5: Proof steps that are not justified as written (MAJOR, medium confidence)
In the proof of Lemma 5 the last step requires Σ_n(π_n, f_n) − Σ_n(π_n, f*) ≤ λ_n Σ_n(π_n, f*), but Lemma 4 bounds the difference of *returns* J, not of uncertainty integrals, and λ_n contains L_r, not L_σ. The proof of Theorem 2 likewise invokes "Theorem 4" (Lemma 4) to compare Σ under f_n and f*, and in that setting r=0 makes L_r=0 so λ_n=0 under Lemma 4's formula, while the proof keeps factors (1+λ_N)² and the main text writes λ_n→∞. The conclusion may still hold (an L_σ-based argument seems plausible) but the argument as printed does not establish it.
- **Suggested Fix**: Add the Lipschitz-of-σ lemma with its constant, state λ_n in the theorem statement, and rewrite Theorem 2's proof for r=0.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E3 | §3.3 vs Table 1 | "hence |Sn| must increase with n" | Table 1 fixes measurement/control frequency ν, so m_n = T·ν is constant across episodes | Cross-referenced | High | MAJOR | State condition fails in experiments or grow S_n |
| ERR-2 | E2 | App. B.2, proof of Lemma 5 | "≤ (λ2n + 2λn )Σn (πn , f ∗ )" | Final step needs a Σ-difference bound not supplied by Lemma 4 | Re-derived | Medium | MAJOR | Add lemma with L_σ |
| ERR-3 | E6 | §3.3 Theorem 1 vs App. B.2 | "Under regularity assumptions (Ass. 1 to 3)" | Appendix restates Theorem 1 under "Assumption 2 and Assumption 4"; Assumption 4 (RKHS) is not in the main statement | Cross-referenced | High | MINOR | Align statements |
| ERR-4 | E6 | App. B.2, Lemma 4 | "λn = 2βn Lr (1 + Lπ )eL∗(1+Lπ)T" | The proof's inequality carries an extra factor T (…Lr (1 + Lπ )T e…); the statement omits it | Cross-referenced | High | MINOR | Fix constant |
| ERR-5 | E5 | §4, TaCoS paragraph | "which is shown by the higher returns in Figure 5 and in turn, demonstrates sample efficiency" | Figure 5 reports "Final performance at convergence", which does not measure the number of interactions | Cross-referenced to caption | Medium | MAJOR | Report interaction counts / returns per interaction |

**Minor:** proofs cite "Theorem 4/5" for Lemmas 4/5; the line "(λ2N + λN)" then "(λ2N + 2λN)" in the proof of Theorem 1 is inconsistent; Eq. 3 uses σ_{n−1} while Eq. 7 uses σ_n; Appendix uses expectations for a deterministic system (§2).

### Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | One scalar balances reward/uncertainty; supports both settings | §3 | Alg. 1, Fig. 2–4 | Supported |
| C2 | Sublinear regret | §3.3 | Thm 1 (GP only) | Partially (GP variant; gaps W1, W5) |
| C3 | Sample complexity unsupervised | §3.3 | Thm 2 | Partially (proof gap W5) |
| C4a | "scales better" | Abstract, §4 | Table 3 | Partially (2 low-dim tasks) |
| C4b | "more sample-efficient than prior methods" | Abstract | Fig. 1, 2 | Partially (OCORL on 2 tasks; no discrete-time or strong deep MBRL baselines) |
| C4c | Generalizes to unseen tasks | §4 | Fig. 3, 4 | Partially (see Questions) |

### Protocol sweep and omission sweep
- Split/selection statements found: "static, hand-tuned hyperparameter" (§4); "We use a hand-tuned static regime for the internal reward weight" (App. C.1); "the optimized internal reward weight" (Table 5 caption). **On which metric or task Table 5's λ was optimized is not stated after search.** RL has no held-out split; the zero-shot downstream task is the held-out element, so this matters (a question, not an error).
- Seeds: present for Figures 1, 2, 5; not stated for Figures 3–4. Baseline settings: partly (Table 1; no UTD/tuning for baselines). Compute: present (Table 3). Code: present (project website). Limitations: **not stated after search** (no limitations section).

## Missing References
*(Domain reviewer's responsibility; none added.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory–practice gaps and thin baselines (W1, W2, W5) |
| Clarity | 3 | Clear method; reporting gaps |
| Significance | 2 | Sub-area value but headline claims untested |
| Originality | 2 | Incremental over closest prior work |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central scalability/sample-efficiency claims are tested only against weak or low-dimensional baselines, and the guarantees do not cover the evaluated algorithm.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | W1, W5; correct core ideas inherited from prior analyses |
| Clarity & Presentation | 66 | Competent | Easy to follow; notation slips (ERR-3, ERR-4) |
| Novelty & Originality | 50 | Developing | See R2 |
| Significance & Impact | 52 | Developing | Depends on untested scaling claim |
| Experimental Validation | 45 | Developing | W2–W4 |
| Reproducibility | 62 | Competent | Code and tables, but baseline budgets and seeds missing |
| Ethical Compliance | 65 | Competent | Nothing at stake; no limitations section |

## Questions for Authors
1. Which task/metric was used to pick the per-environment λ in Table 5? If downstream returns were used, would the ranking in Figure 3 hold with λ chosen on the primary task only? (Would raise my score if held.)
2. Do PETS and the mean planner in Figures 2–4 share SAC budget, UTD ratio, synthetic data and soft resets with COMBRL?
3. What does COMBRL give over the same bonus in a discrete-time model on the same tasks?
4. Can you run OCORL (or a reduced variant) on at least one ≥10-dimensional task?
5. Is the step in Lemma 5 resolved by an L_σ argument? Please give the constant.

## Limitations Assessment
**Partially.** No limitations section; theory–practice gaps (mean model, ensembles, λ choice, fixed ν) are not acknowledged. Suggest a short paragraph.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: sound idea and honest setup, but the headline claims are not tested against the right baselines and the proofs do not cover what was run.

## Confidence
**4**: read the appendix and proofs; figure contents unavailable.

---

# Peer Review Report

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Reviewer: Prof. Daichi Morales-Ferrante, Reviewer 2 (Domain) (public research university, East Asia; fictional persona)
## Expertise: regret theory for GP-based RL; optimism-based exploration
## Date: 2026-11-05

---

## Summary
COMBRL augments the reward with a scaled epistemic-uncertainty bonus in a continuous-time model-based setting. It inherits the setup (MSS, model complexity I_N, calibrated models) from Treven et al. (2023) and the reward-plus-uncertainty idea from the discrete-time Sukhija et al. (2025b), and adds a regret bound and an unsupervised uncertainty-reduction bound.

## Strengths

### S1: Honest positioning against the closest works
§2.1 and App. A.2 state that the work is "closely related to Sukhija et al. (2025b), who study the problem in the discrete-time setting", and describe OCORL and Yildiz et al. (2021) accurately at the level of their approach. The statement of what changes (no optimization over plausible dynamics) is clear.

### S2: A coherent theoretical frame
Definition 1 (MSS), Eq. 4 (model complexity) and Theorem 1 connect the objective to the sample-complexity machinery for continuous time; the GP model-selection QP (Eq. 6, Theorem 3) is a thoughtful device to keep the Lipschitz constant independent of n.

### S3: Unsupervised and reward-driven settings under one objective
Treating λ→∞ as active exploration (§3.2) and giving a corresponding bound (Theorem 2) is a tidy unification.

## Weaknesses

### W1: Novelty is incremental relative to two cited works (MAJOR)
The contribution is mostly the transposition of the reward+bonus objective of the discrete-time work to the continuous-time framework of OCORL. The proof of Theorem 1 follows the Curi et al. (2020)/Treven et al. (2023) template: Lemma 4 reuses "Treven et al. (2023) Lemma 4", and the final regret step uses "Treven et al. (2023), Proposition 1". App. A.2 says the analysis is "significantly different", but the delta is not located in the proofs. The effect on the field depends on whether continuous-time matters for the bonus objective, which the experiments do not test (see W2).
- **Suggested Fix**: Add a paragraph and a proof-sketch table stating which steps are new vs. imported, and which lemma is the continuous-time-specific contribution.

### W2: No empirical comparison against the closest prior works (MAJOR)
The discrete-time Sukhija et al. (2025b) and its auto-tuning relative (Sukhija et al., 2025a) are the nearest methods, but neither is run, and OCORL appears only on two GP tasks (Figure 1) and TaCoS (Figure 5). Figures 2–4 compare with a mean planner and PETS, which are weaker, older baselines. The claim of being "more sample-efficient than prior methods" (Abstract) therefore compares mostly against methods that do not explore with a bonus at all.
- **Suggested Fix**: Add the discrete-time bonus method and OCORL (where feasible) to Figures 2–3.

### W3: The "first" claim and the bound's shape (MAJOR, claim-level)
"To the best of our knowledge, we are the first to show this for continuous-time RL" (§3.3) concerns Theorem 2. The bound hides the factor (1+λ_N)² (App. B.2, last lines of Theorem 2's proof), which with λ→∞ is not bounded unless λ is set as in Lemma 4; the statement therefore needs to say which λ it refers to. The related unsupervised discrete-time result (Sukhija et al., 2023) is cited, and the literature check found no closer continuous-time prior work in arXiv (limit of the search, not evidence of novelty).
- **Suggested Fix**: Restate Theorem 2 with explicit λ and the "first" claim limited to the stated setting.

### W4: Citation and characterization checks (MINOR–MAJOR)
App. A.1 says recent deep MBRL "often rel[ies] on naive exploration heuristics such as Boltzmann exploration (Hansen et al., 2024; Hafner et al., 2025)". I cannot confirm that TD-MPC2 and DreamerV3 use Boltzmann exploration (to my knowledge they use sampled/noisy actions or entropy terms); this should be checked or reworded. §2.1 says OCORL "does not scale to higher dimensional systems", but the paper itself does not run OCORL in high dimension.
- **Suggested Fix**: Reword or support with measurements.

### Minor
Related-work characterizations in A.3 are brief; the sentence "Earlier work has shown that continuous-time formulations can outperform discrete-time counterparts in sample efficiency" (§4) has no citation.

## Literature-check addendum (strict, cutoff 2025-09-24)
Mode: strict. Queries: 3 claim queries logged (C1, C2, C3), 1 baseline query, plus 3 further attempts that returned nothing usable (refused or empty), 6 `verify` calls; `similarity` run. Gaps left open: the Gym/DMC benchmarks yield no published numbers to scout (the paper reports only its own re-runs), so no baseline-scout table is possible; `coverage` flagged only the missing baseline query.

**Per-claim novelty (claim-level profile)**
| Claim | Dim. | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|------|---------|----------------------------------------------|-----------|
| C1 (reward+bonus continuous-time objective) | method | medium | Treven et al. 2023, level 3, https://arxiv.org/abs/2310.19848, prior (arXiv-only, 6+ months), cited | Same continuous-time MBRL setting with optimism and calibrated models; the bonus formulation differs from optimistic dynamics. The discrete-time work (Sukhija 2025b) is cited but post-cutoff on arXiv, so judged only from the paper's own description ("a similar reward formulation in the discrete-time setting", A.2). |
| C2 (regret bound) | result | incremental | Treven et al. 2023, level 4, same link, cited | Abstract: regret bounds that "surface the importance of the measurement selection strategy"; this paper's bound has the same ingredients with an added λ factor. |
| C3 (unsupervised bound) | result | medium | none found in 2 queries (arXiv only); Sukhija et al. 2023 cited by the paper | "No close prior work found in this search"; at most medium. |
| C4 (empirical) | result | not rated | – | Not a novelty claim. |

**Novelty delta table**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| Continuous-time optimistic MBRL | Treven et al. 2023 (OCORL) | ODE dynamics, calibrated models, optimism, MSS-dependent regret | Bonus objective replaces optimization over plausible dynamics; unsupervised variant | Yes (§2.1) |
| Reward + uncertainty objective with scalar λ | Sukhija et al. 2025b (as described in the paper; not read) | Same objective in discrete time | Continuous-time analysis and experiments with TaCoS | Yes (§2.1, A.2) |
| Adaptive sensing compatibility | Treven et al. 2024 (TaCoS) | Time-adaptive planning framework | Plugging COMBRL into it | Yes (§4, C.6) |

**Attribution (closest to the paper as a whole):** Treven et al. 2023; text overlap in the opening sentence of the abstract (reported to the EIC; not a score matter).

**Field snapshot (as of the cutoff; partly from kept results, partly from knowledge, marked where uncertain).** Roughly 2018–2020, deep MBRL with ensembles (PETS, MBPO) dominated sample-efficient continuous control, while theory-backed exploration (optimistic or hallucinated dynamics; Curi 2020, Kakade 2020) was confined to low-dimensional or GP settings. From 2023 the continuous-time line (Treven 2023, 2024) and active exploration (Sukhija 2023) added guarantees with measurement selection; 2025 work focused on making optimistic exploration cheap to run (reward-bonus formulations; auto-tuned bonuses). Current expectations at ICLR for this sub-field: a clear mechanism, a guarantee for a tractable variant, and a demonstration against strong deep MBRL baselines on standard benchmarks. A pure re-implementation of a bonus in a new time formalism is incremental unless it shows a continuous-time-specific benefit (e.g., robustness to discretization, adaptive sensing gains); that calibration places C1–C3 at medium-incremental.

## Missing References
*(Verified with `related_search.py verify` where a link is given; recommendations follow Hard Rule 2.)*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Fan & Ming, "Model-based Reinforcement Learning for Continuous Control with Posterior Sampling", ICML 2021 — https://arxiv.org/abs/2012.09613 (found) | Prior (peer-reviewed). Alternative exploration principle with regret analysis in continuous-control MBRL; natural comparison point. |
| Important | Tallec, Blier & Ollivier, "Making Deep Q-learning methods robust to time discretization", ICML 2019 — https://arxiv.org/abs/1901.09732 (found) | Prior. Motivates and gives tests of discretization sensitivity, which would test the continuous-time benefit claim. |
| Helpful | Shyam, Jaśkowski & Gomez, "Model-Based Active Exploration", ICML 2019 — https://arxiv.org/abs/1810.12162 (found) | Prior. Ensemble-uncertainty active exploration; baseline for the unsupervised variant. |
| Helpful | Munos, "Policy Gradient in Continuous Time", JMLR 2006 [verify] | Classic continuous-time RL reference absent from App. A.3. |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Proof gaps and thin comparison (mean of 58, 50 = 54) |
| Clarity | 3 | Well organized |
| Significance | 2 | Incremental in sub-area |
| Originality | 2 | Transposition of a known objective |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the novelty delta to two cited works is small and the closest discrete-time work is not compared.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound framework; steps imported from prior bounds |
| Clarity & Presentation | 68 | Competent | Clear positioning |
| Novelty & Originality | 50 | Developing | W1 |
| Significance & Impact | 55 | Competent | Useful sub-area, narrow |
| Experimental Validation | 50 | Developing | W2 |
| Reproducibility | 64 | Competent | Code and tables |
| Ethical Compliance | 65 | Competent | Nothing at stake |

## Questions for Authors
1. Which proof steps are new relative to Treven et al. (2023)? A table would help.
2. What is the expected gap between COMBRL and the same bonus in discrete time on your tasks? A negligible gap would lower my novelty score; a clear gap would raise it.
3. Please check the characterization of TD-MPC2 and DreamerV3 exploration in A.1.

## Limitations Assessment
**Partially.** Related-work claims on scalability should be measured or softened.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a clean but incremental extension whose key comparison (against the discrete-time counterpart) is missing.

## Confidence
**4**

---

# Peer Review Report

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Reviewer: Dr. Priya Anand-Whitcombe, Reviewer 3 (Perspective) (engineering department, public university, North America; fictional persona)
## Expertise: event-/self-triggered control; system identification; robotics
## Date: 2026-11-05

---

## Summary
The paper brings epistemic-uncertainty-driven exploration to continuous-time control, with applications ranging from reward-driven tasks to unsupervised system identification. It relates to event-triggered control through the TaCoS experiments and offers a regret bound for GP dynamics.

## Strengths

### S1: A natural bridge to system identification and active learning
App. A.2 notes that the unsupervised case "reduces to active learning" (uncertainty sampling). The unsupervised variant's use as an exploration policy for zero-shot adaptation (Figure 3) is a practical pitch for control engineers who need models before they know the task.

### S2: Compatibility with adaptive sensing and control
Figure 5 and App. C.6 show COMBRL operating with TaCoS, where each interaction has a cost C (Table 6). Combining uncertainty-driven exploration with event-triggered-style scheduling (the related line in App. A.3) is relevant for hardware with costly sensing.

### S3: Transparent handling of derivative estimates
App. C.4 states derivatives are approximated by a finite-difference filter and App. C.1 assumes direct derivative access for GP tasks; these are the right assumptions to be explicit about for control audiences.

## Weaknesses

### W1: Gap between ODE-based assumptions and real sensing (MAJOR for significance)
Assumption 2 requires i.i.d. sub-Gaussian noise on derivative measurements, but finite-difference derivative estimates are biased and correlated over time (App. C.4). Derivative noise and filtering interplay with model uncertainty and thus with the bonus itself, so uncertainty-seeking may be driven by noise amplification. No experiment adds measurement noise, actuation delay or model mismatch, which are the reasons to use continuous-time methods on physical systems.
- **Suggested Fix**: Add a noise/delay sweep on one GP task and one Gym task; discuss derivative filtering (e.g., Kalman-type estimators from system identification).

### W2: Deployment considerations are not discussed (MAJOR for significance)
Exploration with a large λ drives the system into poorly known regions, which in robotics is a safety issue; there is no discussion of constraints, safe exploration, or hardware (the paper's motivation, §1, mentions robots and medicine). The Lipschitz and RKHS assumptions (Assumptions 1, 4) are said to be "satisfied for many real-world applications" without evidence; contact-rich systems (HalfCheetah, Hopper, Pusher) are non-smooth, so the Lipschitz constant in e^{L(1+Lπ)T} may be very large.
- **Suggested Fix**: State where Assumptions 1 and 4 are plausible, and add a limitations paragraph on safety and non-smooth contact.

### W3: Is "continuous-time" doing the work? (question-level)
All benchmarks are run in discrete simulators with fixed dt, with continuous time emulated by "a fine time discretization" (App. C.1) or finite differences. The paper does not show a case where discretization sensitivity or variable-rate sensing matters for COMBRL beyond Figure 5. This is a missed connection to the discretization-robustness literature (see Missing References by R2).
- **Suggested Fix**: A sweep of control rate (e.g., 5× coarser) for COMBRL vs a discrete-time baseline would show the benefit.

### Minor
Connections to dual control / exploration-exploitation in adaptive control (the paper cites Zhao et al. 2025a;b) could be expanded.

## Missing References
Line of work: classical dual-control and active system identification (experiment design with Fisher information) — a natural baseline for the unsupervised variant, described rather than cited.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Mean of 66 and 60 = 63 |
| Clarity | 3 | Clear |
| Significance | 3 | Relevant bridge for control; real-world unproven |
| Originality | 3 | Fresh combination |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a well-motivated, usable method with a broad set of settings; significance rests on the claimed scalability, which I take at face value more than the other reviewers do.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 66 | Competent | Standard assumptions, correct core |
| Clarity & Presentation | 70 | Competent | Easy to follow |
| Novelty & Originality | 60 | Competent | New combination |
| Significance & Impact | 66 | Competent | Control community interest |
| Experimental Validation | 60 | Competent | Broad but light on noise/robustness |
| Reproducibility | 68 | Competent | Code and tables |
| Ethical Compliance | 68 | Competent | Simulated only; safety unmentioned |

## Questions for Authors
1. How does the bonus behave when derivative measurements are noisy or filtered? A robust result would raise my significance score.
2. Can COMBRL be combined with constraints on exploration?
3. Is there any hardware or high-fidelity-simulator result?

## Limitations Assessment
**Partially.** Safety, noise, and smoothness assumptions are not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: a useful, well-motivated method for continuous-time control exploration whose practical significance is plausible but unproven.

## Confidence
**3**: not an RL-exploration specialist.

---

# Peer Review Report

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Reviewer: Dr. Lucas Ferreira Okafor, Reviewer 4 (Generalist) (ML group, mid-size university, South America; fictional persona)
## Expertise: RL applications; representation learning
## Date: 2026-11-05

---

## Summary
The paper adds an uncertainty bonus to the reward in continuous-time model-based RL, shows regret and sample-complexity bounds for GP models, and reports experiments on classic control, Gym/DMC and a time-adaptive setting. The pitch: simple, scalable, theoretically grounded exploration for continuous-time systems.

## Strengths

### S1: Clear exposition
The problem setting (§2), the algorithm (§3, Algorithm 1) and the three regimes of λ (§3.2) can be followed by a non-specialist; the structure "question → experiment" in §4 is easy to read.

### S2: Theory and experiments pull in the same direction
Figure 4 shows that moderate λ preserves primary-task performance while improving downstream generalization; this matches the exploration-breadth story of §3.2.

### S3: Complete appendix and code link
Tables 1–6 and App. C.5 (task definitions) give enough to rerun the work.

### S4: Honest scoping on some points
The text states "For the Pendulum experiments, all algorithms solve the task of swinging up", acknowledging the gain is mainly computational there.

## Weaknesses

### W1: Headline claims exceed the evidence shown (MAJOR)
The abstract's "scales better, is more sample-efficient than prior methods, and outperforms baselines across several deep RL tasks" is supported by a 3× runtime ratio on two low-dimensional systems (Table 3) and by curves against only a mean planner and PETS (Figure 2). In §4 the "sample-efficient" label for TaCoS is derived from final returns (Figure 5), not interaction counts. A reader cannot tell from the main text how large the gains are: Figure 2's caption says "COMBRL achieves the largest performance gains in sparse or underactuated tasks" but no numbers are given.
- **Suggested Fix**: Add a main-text results table with numbers and soften the abstract.

### W2: Venue-fit concern: the theory does not describe the main experiments (MAJOR)
For an ICLR audience the paper is positioned as theory + scalable deep RL, but the guarantees are for GP models (§3.3, "in the GP setting"), while the deep results use ensembles with no calibration (App. C.4). The "model-agnostic" language of the abstract and conclusion ("agnostic to the statistical model") reads as covering guarantees as well.
- **Suggested Fix**: Separate "guarantee holds for" and "method applies to" statements.

### W3: No limitations section (MINOR–MAJOR)
No limitations discussion: λ tuning effort, derivative estimation, reliance on simulators.
- **Suggested Fix**: Add a short limitations paragraph.

### Minor
Fig. 2–5 captions should state seeds and whether bands are standard errors (Figures 3–4 omit n). The project website link and repository name in §1 and the Reproducibility Statement are not anonymized (readiness item; no effect on score). "Theorem 4/5" cross-references in App. B should read "Lemma".

### Venue criteria checklist (ICLR form)
| Item | Grade | Location |
|------|-------|----------|
| Soundness: claims supported | Partly | W1; Fig. 2 vs abstract |
| Soundness: theory correct | Partly | App. B Lemma 5 step unclear |
| Presentation: clear and organized | Met | §2–§4 |
| Contribution: new and significant | Partly | Incremental over cited work |
| Reproducibility: code and settings | Met | Reproducibility Statement, App. C |
| Anonymity / format | Partly | project link in §1 |

## Missing References
*(none added; see R2)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Mean of 62 and 58 = 60 (one-step deviation noted: sound but thin) |
| Clarity | 3 | Clear |
| Significance | 3 | Useful sub-area |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clearly written, complete package with experiments across settings; weaknesses (untested scalability, limited baselines) are those that many accepted papers share.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound core, partial coverage |
| Clarity & Presentation | 72 | Competent | Easy to follow; captions miss n |
| Novelty & Originality | 58 | Competent | Incremental |
| Significance & Impact | 62 | Competent | Moderate |
| Experimental Validation | 58 | Competent | Broad, light |
| Reproducibility | 66 | Competent | Good |
| Ethical Compliance | 66 | Competent | No limitations section |

## Questions for Authors
1. Can you give a table of final returns with n seeds for Figures 2–5? Clear numbers would raise my Experimental Validation score.
2. Which results would still hold if only ensemble models (no theory) were considered?
3. Where would you place the paper relative to the discrete-time method it builds on?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: clear, well-organized and broadly evaluated; the weaknesses are ordinary for the venue, but the claims should be narrowed.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Reviewer: Dr. Sana Haddad-Lindgren, Devil's Advocate (evaluation methodology group; fictional persona)

---

## Steelman
A reward-plus-uncertainty objective gives a one-parameter family that interpolates between exploitation and pure active learning, is cheaper than optimizing over plausible dynamics (≈3× in Table 3), has regret and sample-complexity guarantees for GP models, and delivers better primary and zero-shot downstream performance than reward-greedy baselines in simulation.

## Core Argument Chain
1. P1: Optimism via a reward+σ bonus can replace optimization over plausible dynamics (§3.1) and is cheaper (Table 3).
2. P2: For GP models the bonus yields sublinear regret and an uncertainty-reduction rate (Theorems 1–2).
3. P3: In deep settings the same bonus (ensemble disagreement) improves return and generalization over mean/PETS (Figures 2–4).
4. P4: The method is applicable to continuous-time, including adaptive sensing (Figure 5).
∴ COMBRL is a scalable, sample-efficient continuous-time exploration method that outperforms prior methods.

## Strongest Counter-Argument
Suppose the continuous-time structure were irrelevant to the result. What would the experiments look like? Almost exactly as they do. In the deep experiments, Gym and DMC environments are discrete-time simulators; derivatives are obtained "by approximating the derivatives using a finite difference filter" (App. C.4); the measurement/control frequency "is given by the duration of an environment step" (App. C.4); and planning uses SAC on the mean model, with the bonus being ensemble disagreement. That is a discrete-time MBRL agent with an ensemble-disagreement reward bonus, a design the paper itself describes as existing in discrete time ("similar reward formulation in the discrete-time setting", A.2). Nothing is compared against that discrete-time agent. The scalability claim then reduces to a runtime ratio against OCORL on two 2–3-dimensional systems, and the theory is for a different algorithm (QP-projected Lipschitz model, λ_n a multiple of β_n e^{LT}, growing S_n), none of which is used in the experiments. The one place where continuous time clearly matters, adaptive sensing (Figure 5), compares COMBRL-TaCoS with OTaCoS and TaCoS variants whose adaptive scheduling is inherited from prior work, so the contribution of the bonus to that benefit is not isolated either. The zero-shot result (Figure 3) compares an exploration-driven agent with agents that never see anything but the primary reward, on downstream tasks defined as the reverse of the primary task (App. C.5, Table 5); better coverage will help on reversed tasks regardless of how uncertainty is defined. The authors need to show (i) a discrete-time counterpart on the same tasks and (ii) an exploration baseline for Figure 3, (iii) a claim list that separates what is proven from what is applied.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The claims are narrower than stated but supported in weaker form: the evidence does not contradict the main claim, and no leakage, fabrication or fatal experiment design is shown.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic/Evidence | §4; App. C.4; A.2 | Continuous-time contribution not isolated: no discrete-time bonus baseline, environments run at fixed dt with finite-difference derivatives. Evidence supports "bonus helps", not "continuous-time bonus helps". | Add discrete-time counterpart and a control-rate sweep. |
| DA-M2 | Scope | Theorem 1–2; §3.1 fn. 2; App. C.4; Table 1/5 | Guarantees cover GP+QP+prescribed λ_n+growing S_n; experiments use mean model/ensembles, arbitrary λ, fixed ν. Abstract/Conclusion say "model-agnostic". | Restrict claims or add a GP experiment that matches the theory. |
| DA-M3 | Evidence | §4 (Fig. 3); App. C.5 Table 5 | Downstream tasks are reversals of the primary task; compared agents only see the primary reward; no exploration baseline (e.g., ensemble disagreement without reward, random-coverage). λ per environment "optimized" on unstated criterion. | Add exploration baselines and downstream tasks not defined as reversals; state λ selection. |
| DA-M4 | Overclaiming (E5) | Abstract; §4 | "scales better … than prior methods": evidence is 2 low-dimensional runtime ratios; no OCORL on deep tasks; "more sample-efficient than prior methods" lacks a sample-efficiency metric. | Narrow wording or add a dimension sweep and episodes-to-threshold. |
| DA-M5 | Logic (E5) | §4 TaCoS; Fig. 5 | "fewer interactions" inferred from higher final returns at convergence; interaction counts are set by TaCoS (Table 6: 40–200 steps), not by COMBRL. | Report interactions and ablate the bonus within TaCoS. |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | App. B | "Theorem 4/5" labels for Lemmas 4/5; (λ²+λ) vs (λ²+2λ) inconsistency in the proof of Theorem 1 |
| DA-m2 | Reproducibility | Figs. 3–4 | Seeds not stated |
| DA-m3 | Evidence | Table 3 | Footnotes a/b mix total time and per-episode time |
| DA-m4 | Scope | §2.3 | Finite-difference derivative noise is not i.i.d. sub-Gaussian (Assumption 2) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| ≈3× lower cost, Pendulum-GP | 10.8 ± 0.13 vs 30.6 ± 0.4 min | 30.6/10.8 = 2.83× | Yes ("around 3×") |
| ≈3× lower cost, MountainCar-GP | 1.29 ± 0.01 vs 4.55 ± 0.1 h/episode | 4.55/1.29 = 3.53× | Yes, slightly above 3× |
| PETS cost vs OCORL | 30.78 vs 30.6 min | ratio 1.01 | Consistent with "PETS ≈ OCORL cost" (not discussed) |
| Measurements per episode (fixed) | ν = 20 s⁻¹, T = 2.5 s; ν = 1 s⁻¹, T = 200 s | 50 and 200, constant over episodes | Contradicts the growth condition of §3.3 |

## Ignored Alternative Explanations
- Gains over PETS/mean come from the bonus in any time formalism, not from continuous time.
- Gains in Figure 2 may come from UTD ratio, synthetic data and soft resets (App. C.4) if baselines lack them.
- Downstream gains in Figure 3 may be a coverage effect on reversed tasks; an exploration-only baseline would show this.
- λ chosen per environment (Table 5) adds degrees of freedom absent from baselines.

## Missing Stakeholder Perspectives
Practitioners with noisy sensors and safety limits (large λ drives systems into unknown regions); users who need the discrete-time method's performance at less complexity.

## Observations (Non-Defects)
Honest disclosure of self-implemented GP tasks and finite-difference derivatives; a runtime table with standard errors; open code; a candid "all algorithms solve the task of swinging up" for Pendulum.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Theory–practice mismatch; proof gaps |
| Clarity & Presentation | 66 | Clear; overclaiming in abstract |
| Novelty & Originality | 48 | Transposition of known objective |
| Significance & Impact | 50 | Contingent on untested claims |
| Experimental Validation | 44 | Missing key comparisons |
| Reproducibility | 60 | Code and tables, missing n and budgets |
| Ethical Compliance | 62 | No limitations section |

**Pool position:** better than about 44% of submissions to ICLR.

## Overall: 3 | Confidence: 4

---

# Phase 1.5 / 1.6 — Report Check

**Literature check.** Strict mode, cutoff 2025-09-24: 5 logged queries (claims C1–C3: 3 purposes; baseline: 1; expansion attempts returned nothing usable) and 6 `verify` calls. The Gym/DMC benchmark scout was not applicable (no published baseline numbers are quoted). Gap left open: C3 has no close prior work in the arXiv results ("limit of the search, not evidence of novelty"). The paper's closest discrete-time work (Sukhija et al., 2025b, NeurIPS 2025 per the bibliography) has an arXiv date after the cutoff and was not read; it is judged only from the paper's own description.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Theorem/Lemma label mismatch, (λ²+λ)/(λ²+2λ) slip, σ_{n−1} vs σ_n, expectations on a deterministic system | moved to Minor | Cosmetic |
| R1 | Seeds missing for Figs. 3–4 (W4) | kept | Verified in captions |
| R1 | Eq. 6 not used (W1) | kept | Searched §4 and App. C, no mention |
| R2 | W3 "first" claim | rewritten | Narrowed to the λ-dependence of the stated bound |
| R2 | W4 TD-MPC2/DreamerV3 "Boltzmann" characterization | rewritten as question-level | Cannot verify without the prior works' abstracts; Hard Rule 2 and 10 |
| R3 | W3 "is continuous-time doing the work" | kept as question-level | Not an error |
| R3 | Deployment on hardware | rewritten | Phrased as question, not a flaw |
| R4 | No limitations section | kept | Searched the paper, none found |
| DA | DA-M4 "scales better" | kept | Matches R1-W3, R4-W1 |
| DA | Anonymity link | moved to Minor (R4) | Readiness item, no score effect |

---

# Phase 2 — EIC Meta-Review and Decision

## Synthesizer package (part A)

**Merged issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Guarantees do not cover the evaluated algorithm (mean model, ensembles, λ, fixed ν) | R1-W1, R4-W2, DA-M2 | CONSENSUS-3 |
| Missing/weak baselines (no discrete-time counterpart; OCORL absent from deep tasks; baselines' tuning parity) | R1-W2, R2-W2, DA-M1 | CONSENSUS-3 |
| "Scales better"/"sample-efficient" overclaimed | R1-W3, R4-W1, DA-M4 | CONSENSUS-3 |
| Incremental novelty over cited works | R2-W1, R4 (Originality 2), R1 (Originality 2), DA | CONSENSUS-4 |
| Statistical reporting gaps (seeds in Figs. 3–4, no numeric tables) | R1-W4, R4-W1, DA-m2 | CONSENSUS-3 |
| Downstream-task design favors exploration; λ selection unstated | R1-Q1, DA-M3 | CONSENSUS-2 |
| Proof steps unjustified | R1-W5, DA-m1 (labels) | SOLO (R1) |
| Interaction-count inference in Figure 5 | R1 (ERR-5), R4-W1, DA-M5 | CONSENSUS-3 |
| Noise/safety/deployment | R3-W1, W2 | SOLO |
| No limitations section | R1, R2, R3, R4 | CONSENSUS-4 |
| DA-CRITICAL | none | – |

**Official score (script, before EIC).** Plain mean Overall 3.40 (R1 3, R2 3, R3 4, R4 4, DA 3); official composite 58.1; no consistency warnings; no spread flagged.

**Hinge points for the EIC:** (a) is scalability/sample-efficiency shown; (b) does the theory cover what was run; (c) does the continuous-time aspect matter; (d) the unresolved Lemma 5 step.

## EIC Meta-Review (signed by Dr. Helena Varga-Ndlovu)

### The Case For and Against
- **For acceptance:** A tidy, easily implemented objective that unifies reward-driven and unsupervised continuous-time exploration, with a guarantee for the GP case, a computational saving (≈3×) over the optimistic-dynamics predecessor, open code and a broad range of settings (GP, ensembles, TaCoS). Clear writing and honest disclosure of implementation choices.
- **Against acceptance:** The contribution is a continuous-time transposition of a reward-bonus objective whose discrete-time version the authors cite as closely related; the headline scalability and sample-efficiency claims are tested only against weak or low-dimensional comparisons; the proofs apply to a variant that the experiments do not run; and the closest discrete-time method is never run, so the benefit of continuous time is untested outside TaCoS.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Compute gain ≈3× vs OCORL | R1-W3, DA, R4 | Table 3, Fig. 1 caption | Verified | 2.83× and 3.53× on 3-/2-dim systems only |
| "Scales better" shown across dimension | Abstract; R1-W3, DA-M4 | §4, Table 3 | Verified as unsupported | No dimension sweep; OCORL absent from Figs. 2–4 |
| Mean model/ensembles used rather than analyzed f_n | R1-W1, DA-M2 | §3.1 fn. 2; App. C.4; Eq. 6 | Verified | Eq. 6 not referenced in §4 or App. C |
| Fixed ν vs "|Sn| must increase with n" | R1 ERR-1 | §3.3; Table 1 | Verified | m_n = T·ν constant |
| Figure 5 "fewer interactions" from final returns | R1 ERR-5, DA-M5 | §4; Fig. 5 caption | Partly correct | Interaction savings come from TaCoS (Table 6 min/max steps) and the text does link them to returns; a legitimate comparison with the fixed-rate variant exists but does not quantify interactions |
| Lemma 5 last step unjustified | R1 ERR-2 | App. B.2 | Partly correct | The needed Σ-difference bound is not in Lemma 4; a standard L_σ argument could fill it, but it is absent |
| Downstream tasks are reversals; baselines see only primary reward | DA-M3 | App. C.5, Table 5 | Verified | Table 5 also lists per-environment "optimized" λ with no stated criterion |
| Seeds for Figs. 3–4 | R1-W4, DA-m2 | captions | Verified | Not stated |
| TD-MPC2/DreamerV3 "Boltzmann" characterization | R2-W4 | App. A.1 | Unverifiable here | Kept as a question, not an error |
| Overlap of the abstract's opening sentence with the cited Treven 2023 | similarity flag | Abstract | Verified (overlap) | Integrity note to the editor; prior work is cited; no score effect |
| No CRITICAL issue | DA | – | Verified | Claims survive in weaker form |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points (W1–W4, ERR-1) verified at their locations; ERR-2 only partly. |
| R2 (Domain) | 3 | 4 | 1.0 | Sound positioning and novelty delta; one characterization point unverifiable. |
| R3 (Perspective) | 4 | 3 | 0.75 | Significance score rests on the scalability claim, which I found unsupported; constructive points otherwise valid. |
| R4 (Generalist) | 4 | 4 | 1.0 | Balanced; accurately lists unsupported claims, but scores them as typical-accepted. |
| DA | 3 | 4 | 1.25 | Counter-argument survives verification (discrete-time structure of the experiments, theory scope); no CRITICAL overreach. |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised; nothing to uphold. The ceiling is none.

### Final Decision and Justification
The official ratings average 3.40; the EIC-weighted rating is 3.32 (starting point 3), with an EIC composite of 57.1 (band 3) against an official composite of 58.1, so the two signals agree and no cross-check conflict arises. I keep the starting point: there is no verified, named issue that the ratings failed to account for. The decisive facts are all verified: the claim of scalability rests on two low-dimensional runtime ratios, OCORL is absent from the deep experiments, the closest (discrete-time) method is not compared, and the guarantees cover a GP/QP variant rather than what is run. Those are weaknesses that most rejected submissions share, whereas typical accepted papers at ICLR demonstrate the central claim against strong baselines. The positive points (clear exposition, correct core idea, open code, TaCoS integration) put the paper above the median but short of the accept line: my pool position is about 50 (better than ≈50% of submissions, below the ≈73% needed for acceptance). The paper is fixable in a revision, mostly without new theory: narrowing claims, adding the discrete-time comparison and a dimension sweep. The decision does not exceed any DA ceiling (none applies). **Final Overall: 3 (Borderline Reject).** ICLR rating label: 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}).

---

## Editorial Decision

## Paper: Sample-efficient and Scalable Exploration in Continuous-Time RL
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: empirical (with theory component)
## Review Team (fictional personas): EIC Dr. Helena Varga-Ndlovu; R1 Brandvold (Methodology), R2 Morales-Ferrante (Domain), R3 Anand-Whitcombe (Perspective), R4 Okafor (Generalist), DA Haddad-Lindgren

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 58.1
**EIC assessment** (internal): weighted rating 3.32 → starting point 3 · weighted composite 57.1 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** 50

### Score Summary

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 58 | 66 | 62 | 50 | 57.6 | 56.3 | 16 |
| Clarity & Presentation | 66 | 68 | 70 | 72 | 66 | 68.4 | 68.0 | 6 |
| Novelty & Originality | 50 | 50 | 60 | 58 | 48 | 53.2 | 52.3 | 12 |
| Significance & Impact | 52 | 55 | 66 | 62 | 50 | 57.0 | 55.7 | 16 |
| Experimental Validation | 45 | 50 | 60 | 58 | 44 | 51.4 | 50.1 | 16 |
| Reproducibility | 62 | 64 | 68 | 66 | 60 | 64.0 | 63.4 | 8 |
| Ethical Compliance | 65 | 65 | 68 | 66 | 62 | 65.2 | 64.8 | 6 |
| **Composite** | 54.0 | 57.1 | 64.7 | 62.4 | 52.3 | **58.1 (before)** | **57.1 (after)** | |

Script flags: no consistency warnings; no dimension spread above 20.

### Target-Venue Scores (ICLR, scale status: secondary — confirm against the current form)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| ICLR composite (venue-weighted) | 56.9 |
| Rating for final Overall 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Sample-efficient and Scalable Exploration in Continuous-Time RL" to ICLR. Exploration in continuous-time model-based RL, with a single knob between reward-driven and unsupervised learning, is a worthwhile and ambitious topic.

**Overall Assessment:** The panel found the paper clearly written and the objective easy to implement and reason about, with a guarantee for the GP case, a computational saving over optimistic-dynamics planning and a good range of settings. The panel also found that several central claims (scalability, sample-efficiency relative to prior methods, the value of continuous time) are not yet tested against the comparisons they require, and that the guarantees do not describe the algorithm used in most experiments. This is how a careful panel would likely see this draft, not a prediction.

**Key Strengths Identified by Reviewers:**
1. A simple, flexible objective unifying exploration regimes with a clear ablation of λ (R1, R3, R4).
2. Breadth of setting: GP and ensemble models, zero-shot downstream tasks and a time-adaptive variant (R1, R3, R4).
3. Transparent reporting of implementation choices, a compute table and released code (R1, R2, R4).

**Key Concerns Requiring Attention:**
1. The evaluated algorithm differs from the analyzed one: mean model and uncalibrated ensembles, arbitrary λ, fixed measurement frequency (R1, R4, DA; CONSENSUS-3).
2. Missing comparisons: the discrete-time counterpart of the same objective, OCORL on deep tasks, strong deep MBRL, and exploration baselines for the zero-shot test (R1, R2, DA; CONSENSUS-3).
3. "Scales better" and "more sample-efficient than prior methods" rest on two low-dimensional runtime ratios and curves against mean/PETS (R1, R4, DA; CONSENSUS-3).
4. Incremental novelty over cited works (R1, R2, R4, DA).

**Critical Challenge (Devil's Advocate):** The panel raised no CRITICAL issue. The DA's strongest challenge is that the experiments would look the same if continuous time were irrelevant, since the deep benchmarks are discrete simulators with finite-difference derivatives and no discrete-time counterpart is run. This must be answered with a direct comparison.

**Decision: Borderline Reject (3)**

The paper is near the line; what keeps it below is that the headline claims are untested against the right baselines, not any fatal flaw. A revision that narrows the claims or adds the comparisons below would materially change the assessment. Please refer to the Revision Roadmap.

Sincerely,
Dr. Helena Varga-Ndlovu
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Incremental novelty over cited works | R1, R2, R4, DA | CONSENSUS-4 |
| No limitations section / theory–practice gaps unacknowledged | R1, R2, R3, R4 | CONSENSUS-4 |
| Guarantees do not cover the evaluated algorithm | R1, R4, DA | CONSENSUS-3 |
| Missing/weak baselines | R1, R2, DA | CONSENSUS-3 |
| Scalability/sample-efficiency overclaimed | R1, R4, DA | CONSENSUS-3 |
| Interaction-count inference in Figure 5 | R1, R4, DA | CONSENSUS-3 |
| Statistical reporting gaps | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is significance high enough for ICLR? | R3, R4 (Overall 4) | R1, R2, DA (Overall 3) | The EIC verified that scalability is untested, which is the basis of R3's significance score; weights 0.75 vs 1.25/1.0. |
| Are the proofs sound? | R2 (framework sound), R3 | R1 (gap in Lemma 5 step) | Partly correct: the step is unjustified as printed, probably repairable; counted as MAJOR, not CRITICAL. |

### Score Spread Discussion
No dimension exceeds the 20-point flag. The largest spreads (16) are Technical Rigor, Significance and Experimental Validation, where R3/R4 take the stated scalability at face value while R1/DA score against what was demonstrated; the EIC adopts the latter on verified evidence.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Continuous-time contribution not isolated | Yes (R1, R2) | n/a | n/a |
| DA-M2 | MAJOR | Theory scope vs experiments | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Downstream tasks / baselines / λ selection | Partly (R1 Q1) | n/a | n/a |
| DA-M4 | MAJOR | "Scales better" overclaim | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Figure 5 inference | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*(Issues verified as undermining a main claim; no DA-CRITICAL issue exists.)*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Continuous-time benefit untested: no discrete-time counterpart | DA-M1, R1-W2, R2-W2 | §4; Figs. 2–3 | Run the same bonus in a discrete-time model on the same tasks; add a control-rate sweep | Med; ~100–200 GPU-h | Partly (subset of tasks) |
| R2 | "Scales better"/"sample-efficient" unsupported | R1-W3, R4-W1, DA-M4 | Abstract; §4; Table 3 | Dimension sweep for COMBRL vs OCORL; episodes-to-threshold; or narrow wording | Med; ~50 GPU-h or Low (rewording) | Yes (rewording) / Partly |
| R3 | Theory covers a different algorithm | R1-W1, R4-W2, DA-M2 | Thms 1–2; §3.1 fn. 2; App. B–C | State scope; add a GP experiment solving Eq. 6 with prescribed λ_n and growing S_n, or label experiments as heuristic | Med | Yes (statement) / Partly |
| R4 | Proof gaps | R1-W5 (ERR-2, ERR-4) | App. B.2 Lemma 4–5, Thm 2 | Add the Σ-difference lemma with L_σ, state λ_n in Thm 1, rewrite Thm 2 for r=0 | Med (theory only) | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Zero-shot design: reversal tasks, no exploration baselines, λ selection unstated | DA-M3, R1-Q1 | Add ensemble-disagreement-only and random-coverage baselines; non-reversal downstream tasks; state λ criterion | Med | Partly |
| S2 | Baseline tuning parity and training budget unstated | R1-W2 | Table of UTD/resets/tuning per baseline | Low | Yes |
| S3 | Reporting: seeds for Figs. 3–4, numeric tables with CIs | R1-W4, DA-m2 | Add tables | Low | Yes |
| S4 | Figure 5 claim | R1 ERR-5, DA-M5 | Report interactions, ablate bonus within TaCoS | Med | Partly |
| S5 | Noise/safety/smoothness discussion and limitations section | R3-W1, W2, R4-W3 | Noise sweep; limitations paragraph | Low–Med | Yes |
| S6 | Missing references: Fan & Ming 2021; Tallec et al. 2019 | R2 | Cite and discuss | Low | Yes |
| S7 | Check characterization of TD-MPC2/DreamerV3 and OCORL scalability statements | R2-W4 | Reword or support | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Helpful references (Shyam et al. 2019; Munos 2006 [verify]) | R2 | Cite |
| N2 | Label/constant slips ((λ²+λ) vs (λ²+2λ); "Theorem 4/5"; σ_{n−1} vs σ_n; Table 3 footnotes) | R1, DA | Fix |
| N3 | Anonymize project link | R4 | Use anonymized repository |
| N4 | Dual-control / experiment-design baselines | R3 | Discuss |
| N5 | Abstract opening-sentence overlap with the cited prior paper | similarity flag | Rephrase; editor's concern only |

## Estimated Revision Effort
- Priority 1: 4 items, ≈2–4 weeks (one compute-heavy item; theory edits ≈2–3 days).
- Priority 2: 7 items, ≈1–2 weeks.
- Priority 3: 5 items, ≈1 day.
- **Total estimated revision time**: ≈4–6 weeks including new experiments.
