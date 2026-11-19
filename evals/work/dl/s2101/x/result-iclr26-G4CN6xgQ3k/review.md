# Review of "Failure Modes of Maximum Entropy RLHF" (ICLR, full mode)

Date: 2026-11-10. Request: "Review this paper. Target venue: ICLR. Full review, skip confirmation, literature check: strict, cutoff date 2025-09-24."

**Run disclosures.**
- The five reviewer passes were run one after another in a single model context. They are role-based passes, not independent agents. Each pass worked from the reviewers' copy and the shared paper memory, and never saw the other reports.
- The integrity scan (`scripts/integrity_scan.py --redact`) found no reviewer-directed text or hidden characters.
- Figures are not available. Figure-dependent claims are judged from captions, legends and surrounding text only. No E9 (figure integrity) check was possible.
- **Literature check (strict, cutoff 2025-09-24) could not be run.** The fingerprint was written. The arXiv API returned HTTP 429 and then timed out on every query attempt (0 of 12 queries completed). Per the skill, the review falls back to `literature check: off`. All recommended references below come from knowledge and are marked `[verify]`. No baseline-scout or claim-level novelty profile exists, and no "newer" or "concurrent" labels were assigned.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Failure Modes of Maximum Entropy RLHF |
| Primary Discipline | Machine learning → LLM alignment / preference optimization |
| Secondary Discipline(s) | Reinforcement learning (entropy-regularized RL, control as inference) |
| Paper Type | Analysis/Insight (composite weights: analysis). It has a short derivation (§3, App. D) and a small empirical study (§4, App. B/C). |
| Core Technique(s) | SimPO, DPO, KL-regularized and entropy-regularized RLOO/PPO, Pythia 1B and 2.8B, TL;DR summarization, GPT-4o-mini win-rate judge |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status "secondary") |
| Venue-Specific Notes | Public reviews. Accepted share about 27% of submissions. Soundness / Presentation / Contribution on 1–4, rating on {0,2,4,6,8,10}. |
| Paper Maturity | Early draft / workshop-level (the PDF is marked "Preprint"). The Minimum Entropy section reports no numbers. |
| Ethics-Relevant Content | None specific: public data (TL;DR), small open models. A generic dual-use note is in the Ethics Statement. |

### Claimed Contributions (as stated by the authors, §1 and Abstract)
- **C1**: SimPO "can be derived as" Maximum Entropy RL with length-normalized (adaptive) temperature, giving it a theoretical foundation (Abstract, §3.2, Eq. 10–16, App. D).
- **C2**: Online MaxEnt RLHF consistently shows overoptimization and unstable KL dynamics, even at very low learning rates, while KL-constrained RLHF stays stable (Abstract, §4.2.1, Fig. 1–3, 5).
- **C3**: Entropy "correlates with" and may exacerbate reward hacking (§4.2.1; Abstract: "appears to correlate").
- **C4**: SimPO succeeds offline because of "dataset constraints and target margins" that approximate a reference model's regularization (§1, §4.3, §5, App. B, Fig. 4, 6–9).

### Paper memory (shared with all reviewers)
- **Setup.**
  - RLOO in TRL, following the recipe of Huang et al. (2024). Pythia 1B and 2.8B. TL;DR. GPT-4o-mini win rate against reference summaries, greedy decoding (§4.1).
  - Entropy coefficients {0.01, 0.05, 0.1, 0.25, 0.5, 1.0} (Fig. 1, 2 legends), "selected via a simple grid search" (§4.2.1). About 250 steps (Fig. 1–3 x-axes).
- **Learning rates.**
  - MaxEnt, 1B: 1e-6 and 1e-7. MaxEnt, 2.8B: 1e-7 and 5e-8.
  - KL-constrained, 1B: 1e-6 (β = 0.05 and 0.07, Fig. 3 and 5 legends). KL-constrained, 2.8B: 3e-6 (β = 0.15 and 0.20, Fig. 3 and 5 legends).
- **Not stated after a full-text search.**
  - The reward model (architecture, training data, accuracy) and the TL;DR train/validation/test split used for training and evaluation.
  - The number of seeds or runs, variance, and compute.
  - Response length |y|, held-out evaluation and sample outputs.
  - Code release. Despite this, the Reproducibility Statement says "our results are fully reproducible".
- **Headline numbers (all from figure legends, no table).**
  - 1B, lr 1e-6: win rates 0.3–2.3% for every entropy coefficient (Fig. 1 left).
  - 1B, lr 1e-7: 51.3% (coefficient 0.01) falling to 33.4% (coefficient 1.0) (Fig. 1 right).
  - 2.8B, lr 1e-7: 5.0–7.5% (Fig. 2 left). 2.8B, lr 5e-8: 16.6–20.7% (Fig. 2 right).
  - SFT baseline 30–35%. "Well-behaved KL runs" 50–55% (§4.2.1).
- **Appendix.** It adds a related-work paragraph (A), SimPO on Pythia-1B/TL;DR with γ ∈ {0, 0.25, 0.5, 1, 2} at lr 2e-7 (good, Fig. 6, 7) and 1e-6 (overoptimized, Fig. 8) (B), extra figures (C), and the derivations (D).
- **Unverifiable.** All figure content (curves, bars); the claimed "quadratic clipping behavior" and the ε = 1e-4 clipping experiment, for which no figure is shown.

## Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Tomasz Lindqvist-Abara, area chair profile (Northern Europe, public research university)
- **Seniority / Expertise**: Senior faculty / RL theory, alignment evaluation
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Verifies derivations himself; unimpressed by accept-leaning scores that rest on an unchecked claim

### Reviewer 1 (Methodology): Dr. Imani Okafor-Delacroix, industrial research lab (West Africa / Europe)
- **Seniority / Expertise**: Senior industry scientist / RLHF training stability, reward-model overoptimization measurement
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched tuning budgets and variance; recomputes everything

### Reviewer 2 (Domain): Prof. Haruto Sakamoto-Weiss, large public research university (East Asia)
- **Seniority / Expertise**: Senior faculty / direct alignment algorithms, soft-optimal control
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads derivations line by line; checks that claimed novelty matches cited work

### Reviewer 3 (Perspective): Dr. Lucía Montenegro-Hale, optimization and decision-theory group (South America)
- **Seniority / Expertise**: Mid-career / bandits, exploration, Goodhart effects
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions
- **Style**: Constructive; looks for what the finding implies beyond the experiment

### Reviewer 4 (Generalist): Dr. Evangeline Roux-Nakamura, university ML group (North America)
- **Seniority / Expertise**: Postdoc / ML broadly, NLP applications
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; reads for the story and the clarity of claims

### Devil's Advocate: Dr. Bartholomew Achterberg, evaluation-methodology group (Western Europe)
- **Seniority / Expertise**: Senior researcher / causal inference for ML evaluation, ablation design
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; asks what else could produce the same curves

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reports

# Peer Review Report

## Paper: Failure Modes of Maximum Entropy RLHF
## Reviewer: Dr. Imani Okafor-Delacroix, Reviewer 1 (Methodology) (industrial research lab; fictional persona)
## Expertise: RLHF training stability; reward-model overoptimization measurement; experimental design
## Date: 2026-11-10

## Summary
The paper (i) argues that SimPO's objective follows from maximum-entropy RL if the temperature is set to α = β/|y| and a margin is appended (§3.2, Eq. 10–16, App. D). It then (ii) tests online MaxEnt RLHF (an RLOO reward minus a length-normalized log-probability bonus, Eq. 18) against KL-regularized RLOO on TL;DR with Pythia 1B and 2.8B (§4.1, §4.2.1, Fig. 1–3). It reports that MaxEnt runs overoptimize or drift in KL while KL-regularized runs are better behaved. It also (iii) tries "Minimum Entropy" RL (§4.2.2) and (iv) offers an explanation for SimPO's offline success based on margins and dataset constraints (§4.3, App. B).

## Strengths
### S1: A clear, falsifiable empirical question
§4 asks whether the entropy bonus can replace a KL anchor in online RLHF. The 1B vs 2.8B contrast, the learning-rate sweeps (Fig. 1, 2) and the consecutive-policy KL diagnostic (Fig. 3, bottom) are sensible instruments. Tracking KL(π_t‖π_{t−1}) and PPO clipping is more informative than final win rate alone.

### S2: Honest scale statement and useful negative framing
§4.1 states that the aim is not state of the art and that compute limits scale. Win rates are printed in the legends (Fig. 1, 2). Reporting that a baseline mechanism fails is valuable when the evidence is clean.

### S3: Authors report partial self-critique
The 1B lr 1e-7 runs are acknowledged to be "reasonably strong" and the authors note that KL regularization is itself highly sensitive to β (§4.2.1, "KL Budget"). App. B also reports that SimPO overoptimizes at lr 1e-6. These admissions help a reader calibrate, even where the headline claims are stronger.

## Weaknesses

### W1: The derivation that SimPO "is" MaxEnt RL fails for the y-dependent temperature it uses (E2)
Eq. 11–15 derive the optimal policy and cancel log Z(x) for a constant α. §3.2 then sets α = β/|y|, where |y| differs between y_w and y_l. The cancelling step in Eq. 14–15 requires the same α on both responses. With α_w = β/|y_w| and α_l = β/|y_l|, the residual is (β/|y_w| − β/|y_l|)·log Z(x) ≠ 0. Z(x) in Eq. 11 also depends on α, so it is not one partition function. App. D.2 itself concedes the result is the loss "without target margin γ and length normalization". The margin is added by analogy to ψPO, and length normalization is declared to be an "adaptive temperature". The claim "SimPO is equivalent to Maximum Entropy RL" is therefore supported only for the constant-α, margin-free case. That case is the known uniform-reference reading of DPO, which the authors attribute to Liu et al. (2024) in §3. The "theoretical guarantees" paragraph (§3.2; Lemma 1–2, Thm 1, App. D.5–6) is likewise proved for constant α, and Prop. 1 sums over y with a fixed α.
- **Suggested Fix**: Either give a derivation in which the length-dependent temperature is a property of the objective (e.g., a token-level MDP or a per-length family with its own partition functions), or restate C1 as "SimPO's un-normalized, margin-free core is the uniform-reference special case of the DPO derivation". Cost: no compute.

### W2: The experiments do not test the MaxEnt-vs-KL question under matched conditions (E4)
KL-regularized runs use lr 1e-6 (1B) and 3e-6 (2.8B). MaxEnt runs use 1e-7 and 5e-8 (§4.2.1, Fig. 3 and 5 legends), 10–60× lower. The entropy-coefficient grid is {0.01…1.0} on a per-token-normalized bonus (Eq. 18). If |y| is about 50 tokens (not stated in the paper), the effective sequence-level bonus is at most about 0.02, below the KL β values that work (0.05–0.2, Fig. 3 legend). So the sweep may never reach a regularization strength comparable to a working KL setting. The MaxEnt and KL objectives also differ by two things at once: the +β log π_ref term and the 1/|y| scaling (Eq. 17 vs 18). The study cannot attribute the difference to "entropy" rather than to the missing reference term or the scaling.
- **Suggested Fix**: A 2×2 design (reference term on/off × length scaling on/off) at one shared learning rate and a coefficient sweep extending past 1.0 (and a sequence-level, un-normalized variant). Cost: for 1B, roughly 8 runs × 250 steps, on the order of 50–100 GPU-hours [estimate]; the 2.8B model about 3×.

### W3: The "asymmetry" between offline SimPO and online MaxEnt is not shown, and the paper's own App. B contradicts its simplest form (E5)
The Conclusion claims "a striking asymmetry between offline and online performance". Yet App. B reports that on the same Pythia-1B/TL;DR setup "all SimPO models exhibit overoptimization regardless of the γ" at lr 1e-6, and that SimPO works at lr 2e-7 (Fig. 6, 7, 8). MaxEnt online at 1B also works at lr 1e-7 (Fig. 1 right: 42.5–51.3% for coefficients ≤ 0.5). So at 1B both families fail at high lr and succeed at low lr, which is a learning-rate effect, not an offline/online asymmetry. The one clear failure, 2.8B online (Fig. 2), has no offline SimPO counterpart: App. B uses Pythia-1B only.
- **Suggested Fix**: Run SimPO on Pythia-2.8B/TL;DR over the same lr grid as Fig. 2. Cost: low (offline, ≈ 10–20 GPU-hours [estimate]).

### W4: Causal claims about entropy rest on correlation and an unshown control (E5, E8)
§4.2.1 states "even with an entropy coefficient of 0, the model still achieves roughly a 50% win rate", and "indicating that entropy actually exacerbates reward hacking rather than mitigating it". The coefficient-0 run does not appear in Fig. 1 or Fig. 2, whose legends list 0.01–1.0 only. A rising entropy bonus is also what a degenerating policy looks like: high-NLL samples score a higher bonus (−log π), so entropy tracks collapse regardless of which causes which. The only dose-response is Fig. 1 right (51.3 → 33.4% as the coefficient rises), and at lr 1e-6 there is none (win rates 0.3–2.3%, non-monotonic). At 2.8B, win rate is flat in the coefficient (Fig. 2: 16.6–20.7% at 5e-8).
- **Suggested Fix**: Show the coefficient-0 curves in Fig. 1–2 with the entropy trace, plus a run with the bonus clipped or frozen at the coefficient-0 trajectory, then restate the claim as correlational unless an intervention supports it.

### W5: Single runs, no variance, unspecified reward model and evaluation split (E8)
No seeds, run counts or intervals appear anywhere. Many headline numbers are differences within 1–3 points (e.g., 18.4 vs 19.9 vs 18.9%, Fig. 2 right). The reward model and the TL;DR split are not specified. The evaluator (GPT-4o-mini vs reference summaries) is not validated, and there is no human check or sample output. "Overoptimization" is read from win-rate collapse alone (0.3–2.3%, Fig. 1 left), which could also be an invalid-output or EOS pathology.
- **Suggested Fix**: 3 seeds for the 2–3 key configurations at 1B (≈ 3× cost of those runs), report the reward model and split, include ~50 sampled outputs and length statistics for the collapsed runs.

### W6: Sections with claims but no shown evidence (E8)
§4.2.2 reports that Minimum Entropy RL "prevents overoptimization and achieves competitive performance with Pythia-1B", but shows no figure or table. The "quadratic clipping behavior" and the ε = 1e-4 experiment (§4.2.1) have no figure. The inability to reproduce Huang et al. (2025) (§4.3) is stated without any detail.
- **Suggested Fix**: Add the missing figures or remove the claims.

**Minor**: Eq. 17 prints the KL term without the bracket that makes it β(log π_θ − log π_ref) (possibly an extraction artifact, so unverifiable); "AC2" (§4.2.1) should read A2C; "standart" (§2.1); "REPRODUCIBIBLITY".

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2 | §3.2, Eq. 14–15 | "where β is a scaling factor and \|y\| provides length normalization" | log Z(x) cancels only for equal α; α = β/\|y\| differs between y_w, y_l, leaving β(1/\|y_w\| − 1/\|y_l\|) log Z(x) | Derived by substitution into Eq. 12 and 13 | High | CRITICAL (handed to DA) | Re-derive or narrow C1 |
| ERR-2 | E5 | App. D.2 vs §3.2 | "without target margin γ and length normalization" | The appendix result lacks exactly the two ingredients that make it SimPO | Cross-referenced (D.2 vs §3.2/Eq. 16) | High | MAJOR | State as special case |
| ERR-3 | E5 | Abstract vs §4.2.1 | "Maximum Entropy RL consistently exhibits overoptimization and unstable KL dynamics, even at very low learning rates" | §4.2.1: "the policy does not become overoptimized, but its KL grows in a nearly linear fashion"; Fig. 1 right 42.5–51.3% | Cross-referenced | High | MAJOR | Qualify to 2.8B / high lr |
| ERR-4 | E6 | §4.2.1 vs Fig. 3 legend | "a higher learning rate of 1 × 10−6" | Fig. 3 and Fig. 5 legends give "LR=3e-06" for the 2.8B KL runs | Cross-referenced | Medium (legend extraction) | MINOR | Correct whichever is wrong |
| ERR-5 | E5 | §4.2.1 | "indicating that entropy actually exacerbates reward hacking rather than mitigating it" | Correlation from curves; coefficient 0 not in Fig. 1/2 | Searched legends | High | MAJOR | Add control or weaken |
| ERR-6 | E8 | §4.2.1 | "even with an entropy coefficient of 0, the model still achieves roughly a 50% win rate" | No coefficient-0 run in Fig. 1–2 legends | Searched text and legends | Medium (may exist elsewhere) | MAJOR | Show it |

### Claim-to-evidence map
| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|--------------|---------------------|---------|
| C1 | SimPO is MaxEnt RL with adaptive temperature | Abstract, §3.2 | App. D.2 yields only the constant-α, margin-free case | Partially supported / contradicted as worded |
| C2 | MaxEnt online consistently overoptimizes | Abstract, §4.2.1 | Fig. 1 (1e-6 yes; 1e-7 no), Fig. 2 (2.8B yes) | Partially supported (2.8B and high lr) |
| C3 | Entropy exacerbates reward hacking | §4.2.1 | Fig. 1 right dose-response only | Weakly supported, correlational |
| C4 | Margins and dataset constraints explain offline success | §1, §4.3, App. B | Fig. 4 (DPO ref margins, 1B), Fig. 6–8 | Unsupported ("dataset constraints" untested) |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Derivation flaw, unmatched comparison, no variance. |
| Clarity | 2 | Readable but figure-dependent and claims outrun shown evidence. |
| Significance | 2 | Question is relevant; evidence too thin to change practice. |
| Originality | 2 | Uniform-reference MaxEnt reading known; length-normalized extension unsound. |

## Dimension Scores (0–100)
**Pool position:** better than about 25% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main theory claim does not follow, and the empirical comparison confounds learning rate, coefficient scale and the reference term.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | ERR-1/ERR-2; objective in Eq. 18 is not the one derived. |
| Clarity & Presentation | 52 | Developing | Understandable, but claim wording contradicts body. |
| Novelty & Originality | 42 | Developing | Known reading plus unsound extension. |
| Significance & Impact | 40 | Developing | Negative result at 1B/2.8B, one dataset. |
| Experimental Validation | 36 | Developing | Single runs, unmatched lr, missing control and model details. |
| Reproducibility | 40 | Developing | No RM, split, seeds, code; yet "fully reproducible". |
| Ethical Compliance | 62 | Competent | Nothing at stake; brief honest statement. |

## Questions for Authors
1. Can you give the coefficient-0 (no regularization) curves for both model sizes? A matching entropy trace would settle whether entropy rises as a cause or a symptom.
2. What is the average |y| and what is the reward model? How does β/|y| compare with the KL β in sequence-level units?
3. Do SimPO runs on Pythia-2.8B/TL;DR at 1e-7 / 5e-8 reproduce the "offline works" side of the asymmetry?
4. Is Fig. 3's KL-constrained 2.8B lr 1e-6 (text) or 3e-6 (legend)?
5. A KL(π_t‖π_{t−1}) above 1 at lr 5e-8 (Fig. 3 right, y-axis to 1.25) is surprising. Was an implementation check (sign of the bonus, dtype, normalization) run? A yes would raise my score.

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. §4.1 states scale limits. Missing: single seed, one dataset and algorithm, an unvalidated judge, and the lr mismatch.

## Ethics Review Flag
**No**: public data, small models.

## Overall Score
**2**: C1 does not follow as derived and C2–C4 are confounded or unshown; fixable only with new derivation and new runs.

## Confidence
**4**: Re-derived the key step and recomputed the legends; figures themselves were unavailable.

---

# Peer Review Report

## Paper: Failure Modes of Maximum Entropy RLHF
## Reviewer: Prof. Haruto Sakamoto-Weiss, Reviewer 2 (Domain) (large public research university, East Asia; fictional persona)
## Expertise: direct alignment algorithms; soft-optimal control and control-as-inference
## Date: 2026-11-10

## Summary
The paper presents SimPO as the closed-form solution of an entropy-regularized RL objective, mirrors DPO's derivation, and then studies online entropy-regularized RLOO on TL;DR. The authors conclude that reference-free regularization (entropy) is insufficient in online RLHF and attribute SimPO's offline success to margins and data constraints.

## Strengths
### S1: Pertinent question linking two literatures
Asking whether a reference-free (entropy) regularizer can replace KL online (§1, §4) connects the direct-alignment line (Rafailov et al. 2024c; Meng et al. 2024) with the soft-RL line cited in §3.1 (Ziebart et al. 2008; Haarnoja et al. 2018). The question is natural and under-examined.

### S2: Fair attribution of the starting observation
§3 credits Liu et al. (2024) with noting that "posterior probability rewards correspond to Maximum Entropy RL". The paper does not present the basic MaxEnt/DPO parallel as entirely new.

### S3: Related work on direct alignment and overoptimization is reasonably broad
App. A covers RRHF, SLiC-HF, ORPO, CPO, SimPO variants, and the DAA overoptimization papers (Azar et al. 2023; Rafailov et al. 2024a; Huang et al. 2025). The coverage is current up to mid-2025.

## Weaknesses

### W1: C1 is not a derivation of SimPO, and what remains is a known reading
(See also R1-W1.) The constant-α MaxEnt reparameterization r = α log π + α log Z (Eq. 12) gives a Bradley–Terry loss on log-probability differences, which is the DPO derivation with a uniform reference, the connection the paper already credits to Liu et al. (2024). SimPO's two distinguishing features are not derived: the 1/|y| factor makes α depend on y and breaks the log Z cancellation in Eq. 14–15, and the margin γ is added "following ψPO (Azar et al., 2023)". App. D.2 states the derived loss is "without target margin γ and length normalization". The §3.2 sentence "SimPO is equivalent to Maximum Entropy RL under the contextual bandit formulation with adaptive temperature and target margin augmentation" is therefore not supported. Novelty of C1 is at most incremental, and its added part is unsound.
- **Suggested Fix**: Position C1 as the special case it proves, contrast it explicitly with Liu et al. (2024), and either derive length normalization properly or drop the equivalence wording.

### W2: The theoretical framing does not connect to the experiments
Eq. 18 adds −(β/|y|)·log π_θ(y|x) to the reward for a sampled response. By the paper's own optimal-policy derivation (Eq. 11, App. D.1), π ∝ exp(r/α) requires a constant α, so the optimum of the Eq. 18 objective is not the policy of Eq. 11. The online experiment is "a length-weighted entropy bonus", not "the objective whose closed form is SimPO". That undermines the inference "SimPO's offline success vs MaxEnt's online failure" (Abstract, Conclusion). Moreover the contextual-bandit view is justified with Elwood et al. (2023), an exploration-in-contextual-bandits paper (by its title) rather than an RLHF source.
- **Suggested Fix**: State which objective the online runs optimize and why it corresponds to SimPO; cite RLHF-specific sources for the bandit view.

### W3: Directly relevant prior work is cited but not engaged
"Zhang et al., 2025" (title: *When maximum entropy misleads policy optimization*) sits in the §3.1 citation cluster and is never discussed, though by its title it bears on the paper's finding. The finding that entropy regularization can fail is also not placed against the overoptimization literature (Gao et al. 2022; Rafailov et al. 2024a) beyond a one-line "unsurprising" (§4.2.1: "which is ultimately unsurprising"). The paper's own statement that the result is unsurprising reduces its novelty claim for C2.
- **Suggested Fix**: A dedicated comparison paragraph with what those works already show and what is new here.

### W4: "Dataset constraints" (C4) is asserted, not examined
§4.3 and the Conclusion credit "dataset constraints and target margins". Fig. 4 shows only DPO reference-log-ratio margins on Pythia-1B, and §4.3 concludes that margins "fall within a relatively narrow range". No experiment varies the dataset's coverage or on-policy-ness. The claim that "reference models are neither necessary nor sufficient" (§4.3) is not tested.
- **Suggested Fix**: Compare SimPO on on-policy vs off-policy preference data, or soften to a hypothesis.

### Missing References
*Literature check could not run (arXiv 429/timeouts); all entries from knowledge and marked `[verify]`.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Liu, Liu, Cohan, "Understanding Reference Policies in Direct Preference Optimization" (2024), cited by the paper | Closest prior work for C1: the authors must say exactly what is added beyond it (not a missing reference, an under-differentiated one) |
| Important | Tajwar et al., "Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data", ICML 2024 `[verify]` | On-policy vs offline preference data; bears on C4 and the offline/online contrast |
| Important | Xu et al., "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study", ICML 2024 `[verify]` | Online-vs-offline comparison under controlled settings |
| Important | Park et al., "Disentangling Length from Quality in Direct Preference Optimization", Findings of ACL 2024 `[verify]` | Length handling in DAAs; relevant to the 1/|y| claim |
| Helpful | Tang et al., "Generalized Preference Optimization: A Unified Approach to Offline Alignment", ICML 2024 `[verify]` | Family of regularized DAAs |
| Helpful | Coste et al., "Reward Model Ensembles Help Mitigate Overoptimization", ICLR 2024 `[verify]` | Alternative to KL for overoptimization |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory step fails; empirical evidence thin. |
| Clarity | 2 | Claim wording and body diverge. |
| Significance | 2 | Narrow setting. |
| Originality | 1 | Known reading, unsound extension. |

## Dimension Scores (0–100)
**Pool position:** better than about 28% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: C1 is mostly known and its new part is unsound; C2 is, in the authors' own words, "unsurprising".

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | Cancellation fails under y-dependent α. |
| Clarity & Presentation | 55 | Competent | Derivation readable; overall framing overreaches. |
| Novelty & Originality | 38 | Developing | Uniform-reference MaxEnt reading already credited to Liu et al. |
| Significance & Impact | 44 | Developing | Relevant question, limited answer. |
| Experimental Validation | 42 | Developing | Not matched to the theory. |
| Reproducibility | 50 | Developing | Open models and library, but missing RM/split/seeds. |
| Ethical Compliance | 62 | Competent | Nothing at stake. |

## Questions for Authors
1. Can you give a derivation (token-level or per-length) that yields the 1/|y| factor and γ, or confirm the claim is for constant α only?
2. What does your work add beyond Liu et al. (2024) in the constant-α case?
3. Which prior results on entropy-regularization failure (including Zhang et al. 2025) do your runs confirm or contradict?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. The theoretical scope limit (constant α) is not stated.

## Ethics Review Flag
**No**.

## Overall Score
**2**: The central theoretical claim is not established and the empirical contribution is acknowledged as unsurprising.

## Confidence
**4**: Verified the derivation; could not run the literature check, so novelty relative to uncited work is from knowledge.

---

# Peer Review Report

## Paper: Failure Modes of Maximum Entropy RLHF
## Reviewer: Dr. Lucía Montenegro-Hale, Reviewer 3 (Perspective) (optimization and decision-theory group, South America; fictional persona)
## Expertise: bandits and exploration; Goodhart effects in optimization
## Date: 2026-11-10

## Summary
The paper asks whether the entropy-regularization view that rationalizes SimPO's reference-free design survives in online RLHF. Experiments on small Pythia models suggest that an entropy bonus alone does not stop reward hacking and may amplify it, and that a KL anchor matters. The paper closes with a hypothesis about why offline methods look better behaved.

## Strengths
### S1: A useful practical message
If it holds, the message in §4.2.1 and §5 that a bare entropy bonus is not a safe substitute for a KL anchor is practically relevant to anyone dropping the reference model to save memory and compute (§1).

### S2: Sensible use of the Goodhart lens
The paper correctly frames overoptimization as proxy-reward drift (§4.2.1, citing Gao et al. 2022). The KL-budget discussion ("KL Budget of the Optimization", §4.2.1), including KL growth that is "nearly linear", is a good intuition pump about trust regions.

### S3: Interesting side-direction
The Minimum Entropy experiment (§4.2.2) is an unconventional idea, tying to recent entropy-minimization work (Agarwal et al. 2025), and suggests that the sign of the entropy term should be treated as a design variable.

## Weaknesses

### W1: Entropy of what, over what? The core assumption is not examined
The paper takes the entropy of the whole-sequence distribution (Eq. 10, contextual bandit). In token-level RLHF the entropy bonus acts on each token. A sampled-sequence bonus −β/|y|·log π(y|x) is a per-token average negative log-likelihood. It pays more for low-probability tokens, so degenerate or out-of-distribution continuations earn more bonus. Connections to exploration bonuses and to extremal Goodhart (optimizing a proxy beyond its support) would make the observed "entropy rises as the policy collapses" (§4.2.1) expected rather than paradoxical. Without discussing this, the Conclusion's "entropy regularization paradoxically correlating with rather than preventing reward hacking" is under-explained.
- **Suggested Fix**: Add a short analysis relating the bonus to support expansion, and test with a token-level entropy bonus (a distinct, standard form of MaxEnt RL) as a comparison.

### W2: Scale and domain assumptions are not discussed
All evidence comes from two small Pythia models on one summarization dataset with a GPT-4o-mini judge (§4.1). The abstract and conclusion generalize to "reference-free approaches" and "online training scenarios" (§5). The authors note SimPO's strong results are with larger chat models (App. B notes "larger models are less prone to common overfitting behaviors"), so the answer may depend on scale in the opposite direction from what the title implies.
- **Suggested Fix**: Narrow the title/abstract wording to the tested regime, or add a ≥7B model and a second task.

### W3: Practical guidance is absent
The paper does not say what a practitioner should do: which learning-rate window, how to detect the onset (KL(π_t‖π_{t−1}) as an early warning?), or whether a small KL term plus entropy helps. Converting Fig. 3's drift diagnostic into an actionable monitor would raise the paper's usefulness.
- **Suggested Fix**: Report a diagnostic (e.g., consecutive-policy KL threshold) that predicts collapse before win rate does, evaluated across the runs already collected.

**Minor**: The Ethics Statement is generic; a sentence on the limited external validity (and on the judge model) would be more informative.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence limited and confounded. |
| Clarity | 2 | Readable, some claims unsupported in-body. |
| Significance | 2 | Narrow regime. |
| Originality | 2 | Modest. |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a relevant question with a plausible but thinly evidenced answer in one small regime.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Reasoning plausible; controls missing. |
| Clarity & Presentation | 58 | Competent | Generally clear. |
| Novelty & Originality | 50 | Developing | Modest. |
| Significance & Impact | 52 | Developing | Practical relevance if it generalizes. |
| Experimental Validation | 44 | Developing | Small scale. |
| Reproducibility | 52 | Developing | Public components; details missing. |
| Ethical Compliance | 68 | Competent | Nothing at stake; limitations partly stated. |

## Questions for Authors
1. Does a token-level entropy bonus behave like your sequence-level, length-normalized one?
2. Does the failure persist at ≥7B with the same lr ratio to the KL baseline? A yes would substantially raise my score.
3. Would a tiny KL term plus an entropy bonus stabilize 2.8B?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (scale mentioned, regime not).

## Ethics Review Flag
**No**.

## Overall Score
**3**: A relevant but thinly evidenced finding; reasons to reject outweigh reasons to accept in the current form.

## Confidence
**3**: I did not re-derive §3 in detail and could not see figures.

---

# Peer Review Report

## Paper: Failure Modes of Maximum Entropy RLHF
## Reviewer: Dr. Evangeline Roux-Nakamura, Reviewer 4 (Generalist) (university ML group, North America; fictional persona)
## Expertise: machine learning generally; NLP applications of RL
## Date: 2026-11-10

## Summary
The paper revisits SimPO through a maximum-entropy lens and reports online experiments suggesting that entropy regularization is not enough to prevent overoptimization, unlike KL regularization. It ends with a discussion of why offline SimPO can nonetheless work.

## Strengths
### S1: Accessible motivation and an organized flow
§1 poses three questions and §2 recaps RLHF, DPO and SimPO compactly (Eq. 1–8). A non-specialist can follow why reference-free methods are interesting.

### S2: A concrete, reproducible-in-spirit setup
TL;DR, Pythia 1B/2.8B, RLOO in TRL, a published recipe (§4.1). Win rates are printed in the figure legends, which helps reading.

### S3: Candid framing of purpose
§4.1: "our aim is not to train state-of-the-art competitive models". Negative-result analyses are welcome at ICLR when evidence is strong.

## Weaknesses

### W1: Claims in the abstract and conclusion outrun the evidence shown
"Consistently exhibits overoptimization" (Abstract) vs. the 1B lr 1e-7 runs reaching 42.5–51.3% (Fig. 1 right) and the body's own statement that "the policy does not become overoptimized" (§4.2.1). The Conclusion's "fundamental limitations in online training scenarios" extrapolates from two small models and one dataset. The Abstract's last sentence ("reference-free approaches may face distinct challenges when applied to online or offline preference learning") is vague.
- **Suggested Fix**: Rewrite the abstract to the tested regime and to what each figure shows.

### W2: Presentation hides the main evidence
Fig. 1–3 are dense multi-panel plots with legends carrying the numbers (win rates in legends; β and LR in Fig. 3 legends). The text refers to Fig. 5 (an appendix figure) for a key KL claim (§4.2.1), and to Fig. 3 for another. §4.2.1 interleaves the 1B result, the 2.8B result, the KL budget and the clipping analysis under a single heading, and §4.2.2 contains no figure. A compact table (model × lr × coefficient × win rate × final KL × seed count) would carry the key evidence.
- **Suggested Fix**: One main results table and one figure per claim; move the clipping and Minimum Entropy material to separate, evidenced subsections or the appendix.

### W3: Venue fit depends on the strength of the insight
ICLR rewards findings that change understanding. The paper's own text calls the high-lr result "ultimately unsurprising" (§4.2.1), and the novel parts (the 2.8B failure and its explanation) are single-run and unexplained. The "theoretical foundation" claim carries the paper's framing (title of §3: "SimPO is the Maximum Entropy RL").
- **Suggested Fix**: Foreground the one robust, new observation (the 2.8B failure at tiny lr, with controls) and explain it.

**Minor**: typos ("standart", "REPRODUCIBIBLITY", "AC2"); inconsistent use of "KL-constrained" vs "KL-regularized"; Eq. 17 bracket (possibly extraction).

### Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported | Partly | §3.2, §4.2.1 |
| Presentation: clear and organized | Partly | §4.2.1, Fig. 1–3 |
| Contribution: significant and new | Partly / not met for C1 | §1, §5 |
| Reproducibility | Not met | Reproducibility Statement |
| Limitations stated | Partly | §4.1 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thin for the claims. |
| Clarity | 2 | Claims and figures hard to match. |
| Significance | 2 | Narrow. |
| Originality | 2 | Modest. |

## Dimension Scores (0–100)
**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a thin-evidence, narrow-regime analysis with overstated headline wording, typical of a rejected submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | Single runs; theory accepted as stated. |
| Clarity & Presentation | 50 | Developing | Claim–evidence gaps and dense figures. |
| Novelty & Originality | 45 | Developing | Mostly known; one new observation. |
| Significance & Impact | 48 | Developing | Relevant but narrow. |
| Experimental Validation | 42 | Developing | Small scale, one dataset. |
| Reproducibility | 50 | Developing | Open models; missing details. |
| Ethical Compliance | 66 | Competent | Fine for a no-risk paper. |

## Questions for Authors
1. What exactly is the take-away for a practitioner who wants to drop the reference model?
2. Could a single table with seeds replace Fig. 1–3's legends?
3. Where does the Minimum Entropy evidence appear? Showing it could raise my score.

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**.

## Overall Score
**3**: A relevant analysis whose headline wording and theoretical framing outrun a thin, single-regime experiment.

## Confidence
**4**: Clear reading of the story; I did not check derivations in detail (Reviewer 1's role).

---

# Devil's Advocate Report

## Paper: Failure Modes of Maximum Entropy RLHF
## Reviewer: Dr. Bartholomew Achterberg, Devil's Advocate (evaluation-methodology group, Western Europe; fictional persona)

## Steelman
Entropy-regularized RL gives a clean reparameterization of rewards in terms of policies. If SimPO sits inside that family, the paper's empirical finding (that an entropy bonus without a reference does not prevent online reward hacking, and may aggravate it) offers a tidy explanation of why reference-free methods need extra scaffolding (margins, low lr, offline data).

## Core Argument Chain
1. SimPO's objective is the closed-form solution of MaxEnt RL with α = β/|y| and a margin (§3.2).
2. So online MaxEnt RLHF (Eq. 18) is the natural online counterpart of SimPO.
3. Online MaxEnt RLHF overoptimizes even at very low lr, while KL-constrained RLHF is stable (§4.2.1).
4. Entropy rises with overoptimization, so entropy exacerbates reward hacking.
5. SimPO nevertheless works offline, so offline data constraints and margins must supply the missing regularization (§4.3).
∴ Reference-free approaches face fundamental limits in online training (§5).

## Strongest Counter-Argument
Premise 1 is false as derived, and without it premises 2 and 5 lose their link. Eq. 14–15 cancel the partition function Z(x) only when α is the same for both responses. With α = β/|y| (§3.2) it is not, and App. D.2 says the cancellation yields a loss "without target margin γ and length normalization". So SimPO is not shown to be MaxEnt RL, and "online MaxEnt RLHF" is not "the online version of SimPO". It is a different object: a reward with a length-weighted bonus (Eq. 18) that does not have Eq. 11 as its optimum.

Even granting the link, premise 3 is confounded. The MaxEnt and KL runs differ by learning rate (10–60×), by coefficient scale (per-token vs per-sequence), and by the presence of the log π_ref term, so "entropy" is not isolated. The only comparison that could speak to SimPO's setting is offline SimPO on the same model, and the authors' own App. B shows SimPO overoptimizing at lr 1e-6 on the same Pythia-1B/TL;DR setup and working at 2e-7, which is the same learning-rate pattern as the online runs (Fig. 1 right works at 1e-7). The "striking asymmetry" is thus not demonstrated, and no SimPO run exists at 2.8B where the online failure occurs.

Premise 4 inverts causality plausibly: an overoptimized policy drifts to low-likelihood outputs, and a −log π bonus is larger for exactly those outputs. The paper's own control ("even with an entropy coefficient of 0") is not displayed. Then premise 5 ("dataset constraints") has no experiment at all. So the chain from the title claim to the conclusion has a broken link at 1, a confound at 3, a causal gap at 4 and an untested step at 5. What survives is a single-seed observation that a 2.8B model collapses under a tiny-lr, sequence-normalized entropy bonus.

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Logic / Evidence | §3.2 Eq. 14–15; App. D.2 ("without target margin γ and length normalization") | C1 (SimPO ≡ MaxEnt RL with adaptive temperature) is the paper's first contribution and the premise linking theory to experiments. The derivation cancels log Z(x) only for constant α; with α = β/\|y\| the residual β(1/\|y_w\| − 1/\|y_l\|) log Z(x) remains, and the appendix concedes the derived loss lacks both length normalization and the margin. The paper's own text contradicts the equivalence as worded. | Give a correct derivation for the length-normalized case or restrict C1 to constant α and drop the "SimPO is MaxEnt RL" framing and the experiment-to-SimPO inference | New derivation / redesign of the paper's framing |

*Why DA-C1 is CRITICAL:* it invalidates a main claim (error category E2) and the only theory contribution. The corrected paper would lose its first contribution and the stated link between the SimPO analysis and §4. Alternatively, only the 2.8B online observation survives.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Fig. 1–3; §4.2.1 | Learning rate (1e-7/5e-8 vs 1e-6/3e-6), coefficient scale and the log π_ref term all differ between MaxEnt and KL runs; "entropy" is not isolated. | 2×2 ablation at matched lr; extend coefficient range |
| DA-M2 | Logic | §5 "striking asymmetry" vs App. B | App. B shows SimPO overoptimizing at lr 1e-6 and working at 2e-7 on the same setup; no 2.8B SimPO run. | SimPO on 2.8B over the Fig. 2 lr grid |
| DA-M3 | Causality | §4.2.1 | "entropy actually exacerbates reward hacking" is read from correlated curves; the coefficient-0 run is not shown. | Show coefficient-0; intervene on the entropy trace |
| DA-M4 | Scope (E5) | Abstract vs §4.2.1 | "Consistently exhibits overoptimization" contradicted by 1B lr 1e-7 runs (42.5–51.3%). | Qualify |
| DA-M5 | Evidence | §4.2.2; §4.2.1 clipping | "Minimum Entropy" and clipping results are described without data. | Add figures or delete |
| DA-M6 | Stats | Fig. 1–2 | No seeds or variance; differences of 1–3 points interpreted. | ≥3 seeds on the key configurations |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §4.2.1 vs Fig. 3 | Text says KL baseline at 2.8B used lr 1e-6; legend shows 3e-6. |
| DA-m2 | Citation | §3.2 | Contextual-bandit view of RLHF cited to Elwood et al. (2023) (by its title an exploration-in-bandits paper). |
| DA-m3 | Wording | Reproducibility Statement | "fully reproducible" while RM, split, seeds, code absent. |
| DA-m4 | Typos | §2.1, §4.2.1 | "standart", "AC2", "REPRODUCIBIBLITY". |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| 1B lr 1e-7: drop in win rate from coefficient 0.01 to 1.0 | 51.3% → 33.4% | 51.3 − 33.4 = 17.9 points | Yes |
| 1B lr 1e-7 mean win rate across 6 coefficients | not stated | (51.3+49.0+47.8+45.9+42.5+33.4)/6 = 44.98 | derived |
| 2.8B lr 5e-8 mean win rate | not stated | (18.4+19.9+18.9+19.4+20.7+16.6)/6 = 18.98; best (20.7) is below the stated SFT 30–35% by 9.3–14.3 points | Consistent with "none outperform SFT" (§4.2.1) |
| 2.8B lr 1e-7 mean win rate | not stated | (6.0+5.0+6.5+7.5+6.9+5.4)/6 = 6.22 | derived |
| Learning-rate ratio KL vs MaxEnt | text: 1e-6 "higher" | 1e-6/5e-8 = 20×; legend 3e-6/5e-8 = 60× | text and legend disagree |
| Abstract "consistently overoptimizes" | all runs | 1B lr 1e-7: 33.4–51.3% (not collapsed) | No |

## Ignored Alternative Explanations
- Overoptimized policies have high entropy because they drift to low-probability text, so entropy is a symptom.
- The missing +β log π_ref term, not the presence of entropy, is what destabilizes the Eq. 18 runs (the KL objective contains the same −β log π_θ term).
- The coefficient grid maps to a much weaker per-sequence regularizer than the working KL β values (if |y| ≈ 50, which is not stated).
- Implementation or numerical issues: KL(π_t‖π_{t−1}) near or above 1 at lr 5e-8 (Fig. 3 right axis to 1.25) is hard to reconcile with a 60×-lower lr than a stable KL run.
- Reward-model or judge idiosyncrasies at 2.8B (one RM, one judge, one seed).

## Missing Stakeholder Perspectives
Practitioners dropping the reference model to save memory would act on a conclusion drawn from two small models and one task. The paper offers no guidance on when the conclusion holds.

## Observations (Non-Defects)
Reporting a negative result with win rates in the legends; tracking consecutive-policy KL and clipping; admitting that KL regularization is itself sensitive to β; App. B's honest note that SimPO overoptimizes at high lr.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 34 | Broken derivation step; objective mismatch. |
| Clarity & Presentation | 52 | Readable; wording outruns evidence. |
| Novelty & Originality | 38 | Known reading plus unsound extension. |
| Significance & Impact | 40 | Narrow regime. |
| Experimental Validation | 32 | Confounded, single-seed, controls missing. |
| Reproducibility | 42 | Missing RM, split, seeds, code. |
| Ethical Compliance | 62 | Nothing at stake. |

**Pool position:** better than about 18% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline theory claim is wrong as derived and the headline empirical claim is confounded.

## Overall: 2 | Confidence: 4

---

# Phase 1.5: Literature check status
Not run: the arXiv API returned 429 and then timed out (0 of 12 queries). Mode requested: strict, cutoff 2025-09-24. Gaps left open: all claims (C1–C4), the TL;DR benchmark scout, and the similarity/text-overlap check. The Domain Reviewer's novelty judgments rest on the paper's own related work and knowledge, with `[verify]` marks. The EIC treated no "missing comparison" as required.

# Phase 1.6: Report Check (Synthesizer, Step 0)
| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W2 (unmatched lr/coefficient/reference term) | Kept, rewritten | The |y| value is not stated in the paper; the "≈ 0.02" figure is now conditional ("if |y| ≈ 50") |
| R1 | W5 (no seeds/RM/split) | Kept | Confirmed by full-text search (no seed, split or RM statement found) |
| R2 | W3 (Zhang et al. 2025 not engaged) | Rewritten | Content of that paper not stated from memory; the weakness now rests on its title and its position in a citation cluster (§3.1) |
| R2 | W4 ("dataset constraints" untested) | Kept | Fig. 4 and App. B contain no coverage experiment |
| R3 | W3 (no practical guidance) | Moved to Minor-level priority | Suggestion rather than a flaw |
| R3 | Minor ethics-statement line | Kept as Minor | Cosmetic |
| R4 | W3 (venue fit) | Rewritten | Reworded to tie to the paper's own "unsurprising" sentence, not to a judgment of the authors |
| R4 | typos | Moved to Minor line | Cosmetic |
| DA | DA-M5 (Min Entropy / clipping data) | Kept | App. B/C contain no such figures (checked Fig. 5–9 captions) |
| DA | Ignored-alternatives bullet on implementation issues | Kept as question-level | Suspicion, not an error; no Error Log entry |

Scores were not changed.

---

# Phase 2: Synthesizer Package (Part A)

### Merged issue list
| Issue | Source IDs | Class |
|-------|-----------|-------|
| Derivation of SimPO from MaxEnt RL fails for y-dependent α; appendix concedes margin/length missing | R1-W1/ERR-1/ERR-2, R2-W1, DA-C1 | DA-CRITICAL (+ CONSENSUS-3 on substance) |
| Online MaxEnt vs KL not matched (lr, coefficient scale, reference term) | R1-W2, DA-M1 | CONSENSUS-2 |
| "Asymmetry" offline vs online not shown; contradicted by App. B; no 2.8B SimPO | R1-W3, DA-M2, R2-W2 (theory-experiment link) | CONSENSUS-3 |
| Causal entropy claim; coefficient 0 missing | R1-W4, DA-M3, R3-W1 | CONSENSUS-3 |
| No seeds/variance; RM, split, judge unspecified | R1-W5, DA-M6, R4 (table request) | CONSENSUS-3 |
| Claims without data (Min Entropy, clipping) | R1-W6, DA-M5, R4-W2 | CONSENSUS-3 |
| Abstract overclaims ("consistently") | R1 ERR-3, R4-W1, DA-M4 | CONSENSUS-3 |
| Scale/domain generalization | R3-W2, R4-W1 | CONSENSUS-2 |
| C1 novelty (known reading) | R2-W1 | SOLO (overlaps with the derivation issue) |
| Relevant cited work not engaged | R2-W3 | SOLO |
| SPLIT | none: no reviewer praised the derivation as sound | n/a |

**Hinge issues:** DA-C1 (derivation), asymmetry vs App. B, matched-lr confound.

### Official score (before EIC; `scores_before.json`)
See "Score Summary" below for the script output (BEFORE: no eic_weight, DA-C1 provisionally upheld).

---

# EIC Meta-Review (Dr. Tomasz Lindqvist-Abara)

### The Case For and Against
- **For acceptance:** The question is natural and under-examined, the paper reports a negative result in a candid way, and the 2.8B collapse at tiny lr with a stable KL baseline is an interesting, if unexplained, observation. Consecutive-policy KL is a good diagnostic.
- **Against acceptance:** The first contribution (SimPO as MaxEnt RL) does not follow as derived, and the rest of the story is linked to it. The empirical comparison is unmatched in lr, coefficient scale and reference term, rests on single runs with an unspecified reward model, and the offline/online "asymmetry" is contradicted by the authors' own App. B. Several claims have no data in the paper.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| log Z(x) cancels only for constant α; α = β/\|y\| breaks Eq. 14–15 | R1-W1, R2-W1, DA-C1 | §3.2 Eq. 12–15, App. D.2 | **Verified** | I redid the substitution: r_i = α_i log π_i + α_i log Z; the difference carries (α_w − α_l) log Z(x). App. D.2 states "without target margin γ and length normalization" |
| "Guarantees" proved only for constant α | R1-W1 | App. D.5–D.6 | **Verified** | Lemma 2 and Prop. 1 use a single α and sum over y |
| Abstract "consistently exhibits overoptimization" vs 1B lr 1e-7 | R1 ERR-3, R4-W1, DA-M4 | Abstract; §4.2.1; Fig. 1 right | **Verified** | Text: "the policy does not become overoptimized"; legends 33.4–51.3% |
| Offline/online asymmetry contradicted by App. B; no 2.8B SimPO | R1-W3, DA-M2 | §5; App. B; Fig. 6–8 | **Verified** | "all SimPO models exhibit overoptimization regardless of the γ" at lr 1e-6; App. B runs Pythia-1B only |
| Coefficient 0 not shown | R1-W4/ERR-6, DA-M3 | §4.2.1; Fig. 1–2 | **Partly correct** | Legends list only 0.01–1.0; the claim may rest on an unshown run (treated as unverified, not fabricated) |
| Learning-rate mismatch | R1-W2, DA-M1 | §4.2.1; Fig. 3, 5 legends | **Verified** | 1e-7/5e-8 vs 1e-6/3e-6; text says 1e-6 for the 2.8B KL baseline, legend says 3e-6 |
| Coefficient grid is weaker than working KL β | R1-W2, DA ignored-alt. | Fig. 1–3 | **Partly correct** | Depends on |y|, which the paper does not state; presented conditionally |
| Minimum Entropy results absent | R1-W6, DA-M5 | §4.2.2 | **Verified** | No figure/table in §4.2.2 or App. B/C |
| R3: Minimum Entropy "promising"; evidence | R3-S3 | §4.2.2 | **Overstated** | Text only; no data |
| R4: derivation accepted as the paper's "theory" | R4 (implicit in S1, W3) | §3.2 | **Incorrect** | C1 is not established |
| R1: KL(π_t‖π_{t−1}) > 1 at lr 5e-8 is surprising | R1-Q5 | Fig. 3 (axis to 1.25) | Unverifiable | Judged from axis ticks in extracted text only; kept as a question |

No integrity signals: the scan found no text addressed to reviewers or AI systems.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Derivation step and the App. B contradiction both verified; the conditional |y| point is flagged as such |
| R2 (Domain) | 2 | 4 | 1.0 | Derivation point verified; positioning claims reasonable; literature check unavailable |
| R3 (Perspective) | 3 | 3 | 0.75 | Strengths rest on unshown Minimum Entropy results and on the paper's theory framing; did not examine the derivation |
| R4 (Generalist) | 3 | 4 | 1.0 | Presentation and overclaiming points verified; accepted the derivation without checking (role: not derivation-level) |
| DA | 2 | 4 | 1.0 | Counter-argument verified at its key links; the implementation-bug alternative is speculative and treated as a question |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes. The paper's first contribution is a derivation that fails at the step it relies on, the appendix concedes the missing ingredients, and the theory is the stated link to the experiments. Even fixed in every other respect, the paper's framing and title claim would not stand. It meets the criteria (invalidates a main claim; E2). | **Upheld** | New data/experiments or redesign: a corrected derivation (or a restructured paper) is needed, not a rewording |

DA ceiling: **3** (Borderline Reject).

### Final Decision and Justification
The official mean rating is 2.40 and the EIC-weighted rating is 2.33, so the starting point is **2 (Reject)**. The weighted composite is 43.9 (official 44.5), also in the Reject band, so the two signals agree and the script raised no cross-check flag. I do not depart from the starting point, and the decision (2) does not exceed the DA ceiling (3).

Two reviewers (R3, R4) rated 3 without engaging the derivation, and their strengths partly rest on C1 and on Minimum Entropy results that the paper does not show. The verified points (ERR-1/2, the App. B contradiction, the unmatched lr and coefficient scale) weigh against those two ratings. Judged against the accepted papers at ICLR, which carry real weaknesses but a sound central claim, this paper's first contribution does not hold, and its empirical evidence is a single-seed, two-model study that cannot attribute the observed collapse to entropy. My pool position is about 22%. What remains is a modest, potentially interesting observation about 2.8B at tiny lr that needs controls, a corrected or narrowed theory section, and a SimPO-at-2.8B comparison. This is a simulation of how a careful panel would likely see this draft, not a prediction.

---

## Score Summary

Official scores and EIC assessment come from `aggregate.json` / `before.json` (script runs below).

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 38 | 40 | 48 | 46 | 34 | 41.2 | 40.5 | 14 |
| Clarity & Presentation | 52 | 55 | 58 | 50 | 52 | 53.4 | 53.0 | 8 |
| Novelty & Originality | 42 | 38 | 50 | 45 | 38 | 42.6 | 42.0 | 12 |
| Significance & Impact | 40 | 44 | 52 | 48 | 40 | 44.8 | 44.0 | 12 |
| Experimental Validation | 36 | 42 | 44 | 42 | 32 | 39.2 | 38.7 | 12 |
| Reproducibility | 40 | 50 | 52 | 50 | 42 | 46.8 | 46.0 | 12 |
| Ethical Compliance | 62 | 62 | 68 | 66 | 62 | 64.0 | 63.6 | 6 |
| **Composite** | 41.6 | 43.8 | 50.8 | 47.2 | 39.3 | **44.5** (before) | **43.9** (after) | |

Official mean Overall = (2 + 2 + 3 + 3 + 2) / 5 = 2.40. EIC-weighted rating = 2.33 (weights R1 1.25, R2 1.0, R3 0.75, R4 1.0, DA 1.0, times confidence). Composite before/after: 44.5 → 43.9. DA ceiling 3 (Borderline Reject); final EIC decision 2.

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 1 |
| Rating | 2 on {0,2,4,6,8,10} (3 on the earlier {1,3,5,6,8,10} scale) |
| Venue-weighted composite | 43.6 |

Labels are as printed by the script. The ICLR scale has "secondary" status, so verify against the current form.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Failure Modes of Maximum Entropy RLHF" to ICLR.

The paper asks whether the entropy-regularization view behind SimPO carries over to online RLHF, a worthwhile question with practical bearing on reference-free alignment.

**Overall Assessment:** Reviewers found the question relevant, the setup simple, and the negative-result framing honest. They also found that the theoretical claim and the experimental comparison do not support the headline conclusions.

**Key Strengths Identified by Reviewers:**
1. A clear question and useful diagnostics, notably consecutive-policy KL and clipping (R1-S1, R3-S2).
2. A candid statement of scale and purpose, and credit to prior work for the basic MaxEnt/DPO link (R4-S3, R2-S2).
3. An interesting observation: a 2.8B model collapsing at tiny learning rates while the KL baseline is stable (Fig. 2, §4.2.1).

**Key Concerns Requiring Attention:**
1. The derivation of SimPO from MaxEnt RL fails when the temperature depends on |y|; the appendix states its result lacks length normalization and the margin (R1, R2, DA; CONSENSUS-3 on substance).
2. MaxEnt and KL runs differ in learning rate, coefficient scale and the reference term; entropy is not isolated, and the offline/online "asymmetry" is contradicted by App. B (R1, DA; CONSENSUS-3).
3. Single runs, no seeds, unspecified reward model and split, and several claims without data (Minimum Entropy, clipping, coefficient 0) (R1, DA, R4).

**Critical Challenge (Devil's Advocate):** The derivation (§3.2, Eq. 14–15) cancels log Z(x) only for constant α; with α = β/|y| it does not. This invalidates the equivalence between SimPO and MaxEnt RL as stated, and with it the link between the theory and §4. It must be resolved with a corrected derivation or a restructured claim.

**Decision: Reject (2)**

The central theoretical claim is not established and the empirical evidence does not isolate entropy. A revision with a corrected or narrowed theory section, matched-lr controls, seeds, and a SimPO comparison at 2.8B would form a different and stronger paper. Please see the Revision Roadmap.

Sincerely,
Dr. Tomasz Lindqvist-Abara
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Derivation of C1 fails or is overstated | R1, R2, DA | CONSENSUS-3 |
| Offline/online asymmetry unsupported | R1, R2, DA | CONSENSUS-3 |
| Causal entropy claim / coefficient 0 missing | R1, R3, DA | CONSENSUS-3 |
| No seeds / variance / RM / split | R1, R4, DA | CONSENSUS-3 |
| Claims without shown data | R1, R4, DA | CONSENSUS-3 |
| Abstract overclaims | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the paper's theory section is sound | (R3, R4 implicitly accept it) | R1, R2, DA | EIC verified the algebra: unsound for y-dependent α |
| Overall level (3 vs 2) | R3, R4: 3 | R1, R2, DA: 2 | EIC weights and the verified derivation flaw favor 2 |

### Score Spread Discussion
No dimension spread exceeds 20 points; the largest is Technical Rigor (14, R3 48 vs DA 34), reflecting R3 and R4 not checking §3.2.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Derivation fails for y-dependent α | Yes (R1, R2) | Upheld | New data/experiments or redesign |
| DA-M1 | MAJOR | Unmatched lr/coefficient/reference term | Yes (R1) | n/a | n/a |
| DA-M2 | MAJOR | Asymmetry vs App. B | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | Causal claim, coefficient 0 | Yes (R1, R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | SimPO ≡ MaxEnt RL derivation fails for α = β/\|y\|; guarantees only for constant α | DA-C1, R1-W1, R2-W1 | §3.2, Eq. 14–15, App. D.2, D.5–D.6 | Correct derivation (e.g., per-length/token-level) or restate C1 as the constant-α special case and drop the equivalence wording; contrast with Liu et al. (2024) | Medium (no compute) | Partially (narrowing yes; new derivation uncertain) |
| R2 | Entropy not isolated: lr, coefficient scale and log π_ref term all differ | R1-W2, DA-M1 | §4.2.1, Fig. 1–3, 5; Eq. 17 vs 18 | 2×2 ablation (reference term × length scaling) at one lr; extend coefficient range | High (≈ 50–100 GPU-h at 1B [estimate]) | Partly |
| R3 | Offline/online asymmetry unsupported | R1-W3, DA-M2 | §5, App. B, Fig. 2, 6–8 | Run SimPO on Pythia-2.8B/TL;DR over Fig. 2's lr grid; or drop "asymmetry" | Medium (≈ 10–20 GPU-h [estimate]) | Yes |
| R4 | Causal entropy claim without coefficient-0 control | R1-W4, DA-M3, R3-W1 | §4.2.1, Fig. 1–2 | Show coefficient-0 with entropy traces; weaken wording unless an intervention supports it | Low–Medium | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No seeds/variance; RM, split, judge, |y| not stated | R1-W5, DA-M6 | 3 seeds on key configs; specify RM, split, |y|; add sample outputs and human spot-check | Medium | Partly |
| S2 | Min Entropy, clipping, "quadratic clipping" claims without data | R1-W6, DA-M5, R4-W2 | Add figures or remove | Low | Yes |
| S3 | Abstract/Conclusion overclaim ("consistently", "fundamental") | R1 ERR-3, R4-W1, DA-M4 | Narrow to tested regime (1B/2.8B, TL;DR) | Low | Yes |
| S4 | Scale/domain generalization | R3-W2 | ≥ 7B model or a second task, or narrow title | High | No |
| S5 | Cited work not engaged (Zhang et al. 2025 `[verify]`); related literature | R2-W3 | Add comparison paragraph; consider Tajwar et al. 2024, Xu et al. 2024 `[verify]` | Low | Yes |
| S6 | "Dataset constraints" (C4) untested | R2-W4 | On-policy vs off-policy SimPO data, or soften | Medium | Partly |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Consecutive-policy-KL as early-warning monitor | R3-W3 | Evaluate predictive value across existing runs |
| N2 | Presentation: one results table, one figure per claim | R4-W2 | Reorganize §4.2.1 |
| N3 | Typos and Eq. 17 bracket; "AC2"; Elwood et al. as bandit-view citation | R1, R4, DA-m1–m4 | Fix; Fig. 3 lr text/legend mismatch |
| N4 | Ethics statement specificity | R3 | One sentence on external validity |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–4 weeks (derivation 1 week; ablations and SimPO-2.8B ≈ 100–150 GPU-hours [estimate]).
- Priority 2: 6 items, about 1–2 weeks plus any scale-up.
- Priority 3: 4 items, about 1–2 days.
- **Total estimated revision time**: roughly 4–6 weeks.
