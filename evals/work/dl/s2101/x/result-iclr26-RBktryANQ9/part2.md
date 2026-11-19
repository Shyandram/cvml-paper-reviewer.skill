
---

# Phase 1.5: Literature Check and Domain Reviewer Addendum (Prof. Xiulan Qiao)

*Mode: strict (cutoff 2025-09-24), arXiv API through `related_search.py`. 9 of 12 queries used: 7 claim, 1 baseline, 1 expansion; no refused queries; `coverage` reports no gaps; `similarity` run on the reviewer copy. Search covers arXiv only. No search used the paper's title, authors or method names. Sources are labelled as the script returned them.*

## Per-claim novelty (claim-level profile, `related_search.py novelty`)

| Claim | Dimension | Novelty | Top prior work (level, label, cited by paper?) | Reasoning |
|-------|-----------|---------|--------------------------------------------------|-----------|
| C1 offline dataset distillation as noise removal avoiding the feedback loop | method | **medium** | Coresets for Robust Training of Neural Networks against Noisy Labels (level 3, prior peer-reviewed, NeurIPS 2020, https://arxiv.org/abs/2011.07451v1), not cited | It also trains on a small, clean-ish selected subset to avoid memorising noise, with theory; the mechanism differs (selection vs synthesis). No search result applies dataset distillation to noisy labels ("no close prior work found in 9 queries, arXiv only"; a limit of the search, not proof of novelty). |
| C1b strong privacy through offline distillation | result | medium | A Comprehensive Study on Dataset Distillation: Performance, Privacy, Robustness and Fairness (level 3, prior arXiv-only, https://arxiv.org/abs/2305.03355v3), not cited | Its abstract reports that membership-inference attacks show "privacy risks still remain" for distilled data, which bears directly on a "strong privacy" claim. |
| C2 distillers denoise symmetric and natural noise | result | medium | Coresets (as above, level 3) | Same goal and CIFAR-10 80% noise setting; the paper does not compare to it. |
| C3 structured noise absorbed; tail classes lost | result | **incremental** | Distilling Long-tailed Datasets (level 4, prior peer-reviewed, CVPR 2025, https://arxiv.org/abs/2408.14506v2), not cited | Its abstract says existing distillation methods "struggle with long-tailed datasets" through biased gradients and poor experts on tail classes, so the tail-class hypothesis in Insight-II is already studied. |

Script reading: "no central claim fully covered by prior work". One claim (C3) is established in part: this is a claim-level finding (MAJOR at most): cite and differentiate. It does not make the paper "known". Attribution (closest prior work to the paper as a whole): the NeurIPS 2020 coreset paper. `similarity`: no high conceptual overlap (cosines ≤ 0.27) and no text overlap.

## Novelty delta table

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| Train on a small subset to resist label noise | Coresets for Robust Training…Noisy Labels (NeurIPS 2020) | Selects weighted clean-ish subsets, proves GD on them does not overfit noisy labels, evaluated at 80% noise on CIFAR-10 | Uses synthetic distilled samples instead of selected real ones; no comparison | No |
| Synthetic samples help with noisy supervision | Mitigating Noisy Supervision Using Synthetic Samples with Soft Labels (arXiv 2024; level 3) | Builds synthetic samples from early-learning representations to reduce noisy-label impact | Uses off-the-shelf dataset distillers | No |
| Privacy benefit of distillation | A Comprehensive Study on Dataset Distillation (arXiv 2023) | Membership inference on distilled sets | Claims strong privacy without testing | No |
| Tail-class loss | Distilling Long-tailed Datasets (CVPR 2025) | Diagnoses and fixes tail bias in distillation | Hypothesis only here | No |

## Baseline scout (CIFAR-10, accuracy)

| Benchmark | Prior method (link, label) | Its reported number (abstract) | Compared in the paper? | Paper's number | Note |
|-----------|----------------------------|--------------------------------|------------------------|----------------|------|
| CIFAR-10, 80% symmetric noise | Coresets… (https://arxiv.org/abs/2011.07451v1, prior peer-reviewed) | "6% increase in accuracy on CIFAR-10 with 80% noisy labels" over the then state of the art (relative to other methods; not an absolute number) | No | not tabulated (figures only) | Settings differ (ResNet vs ConvNet); a question, not an under-reported baseline. A missing-baseline MAJOR at most. |

The paper reports no numeric tables, so no under-reported baseline can be assessed.

## Field snapshot (as of the cutoff)
Noisy-label learning moved from loss correction and transition matrices (2013–2018) to sample selection and semi-supervised pipelines (co-teaching, DivideMix-style, 2018–2020), early-learning regularisation (2020), and contrastive or representation-based methods (2021–2024); current work is evaluated on CIFAR-N and web-scale noisy sets with ResNet-type backbones. Dataset distillation matured from bi-level optimisation to trajectory and distribution matching and, by 2024–2025, to scalable, diffusion-based and long-tailed variants, and a line of work now probes its robustness, privacy and fairness. A significant contribution at this intersection would show a mechanism or a gain over selection-based baselines at ResNet scale or on a real noisy set; a ConvNet/CIFAR curve that beats full-data CE training is expected rather than significant.

## Missing references (verified with `related_search.py verify` or found by search)

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Mirzasoleiman, Cao, Leskovec. *Coresets for Robust Training of Neural Networks against Noisy Labels*. NeurIPS 2020 (https://arxiv.org/abs/2011.07451v1, prior peer-reviewed, found) | Same goal (small clean-ish subset), same CIFAR-10 high-noise setting; the natural baseline. |
| Important | Chen, Geng, Zhu, Woisetschlaeger, Li, Schimmler et al. *A Comprehensive Study on Dataset Distillation: Performance, Privacy, Robustness and Fairness*, arXiv 2023 (https://arxiv.org/abs/2305.03355v3, found) | Membership-inference evidence on distilled data, directly relevant to the privacy claim. |
| Important | Zhao, Wang, Shang, Wang, Yan. *Distilling Long-tailed Datasets*. CVPR 2025 (https://arxiv.org/abs/2408.14506v2, found) | Tail-class behaviour of distillers (Insight-II hypothesis). |
| Important | Liu, Niles-Weed, Razavian, Fernandez-Granda. *Early-Learning Regularization Prevents Memorization of Noisy Labels*. NeurIPS 2020 (https://arxiv.org/abs/2007.00151v2, verified found) | Early-learning account of noise memorisation, the paper's own premise; an obvious control family. |
| Important | Dong, Zhao, Lyu. *Privacy for Free: How does Dataset Condensation Help Privacy?* ICML 2022 (https://arxiv.org/abs/2206.00240v1, verified found) | Prior study of privacy properties of condensation. |
| Helpful | Lu, He. *Mitigating Noisy Supervision Using Synthetic Samples with Soft Labels*, arXiv 2024 (https://arxiv.org/abs/2406.16966v1, found) | Synthetic samples against noisy labels, a related line. |

Recent preprints and concurrent work in the search results (e.g., a 2025 active-learning-under-label-noise preprint, and an ICCV 2025 privacy-preserving distillation paper dated within 60 days of the cutoff) are "worth discussing" only and play no role in any score.

**Citation check (E7).** The text's use of DATM [13], DANCE [54] and RCIG [32] matches their bibliography entries. Looser fits: [40] (Sagun et al., a Hessian analysis) is the citation for the ConvNet architecture (Sec. 4 Implementations); [29] (an early-learning correction method for segmentation) supports label re-assignment for classification (Sec. 1). Treated as Minor.

---

# Phase 1.6: Report Check (Editorial Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6, Error Log | kept | Each has location, quote or cross-reference, fix. ERR-1's numeric absurdity depends on reading "matches the original dataset" and is flagged as intended-reading-dependent. |
| R1 | W3, "distiller literature commonly does this" | rewritten | The paper says only that it follows the protocols of the three methods; the best-checkpoint implication is a suspicion, now a question (Q1), while the omission remains a weakness. |
| R1 | W5, "pipeline costs more than training once" | rewritten | Sec. 3.2 shows experts trained on real images; the cost excess is inference. The absence of any cost measurement is the weakness. |
| R2 | W4 (citations) | moved to Minor | Loose fits, not errors. |
| R2 | W2 (framing only) | rewritten | The question is the missing mechanism-isolating experiments, not novelty alone. |
| R3 | W3 | kept | Actionable. |
| R3 | W4 (i) | kept | Verified by two quotes. |
| R4 | W4 | moved to Minor | Presentation details. |
| DA | DA-M2 | rewritten | The authors do label the IPC-vs-noise question open (Sec. 1, Insight-I), so the issue is the loop-avoidance claim in the Abstract and contribution 1, not a hidden contradiction. |
| DA | DA-M7 | kept | Mirrors R1-W3. |
| All | Figure-based statements | note | All curves unavailable; no weakness depends on a number read from a figure. |

---

# Phase 2: Synthesizer Part A (package for the EIC)

## Merged issue list and consensus map

| Issue | Sources | Class | Hinges? |
|-------|---------|-------|---------|
| I1 Attribution: only full-data CE baseline; no random-subset, early-stopping, hard-label or noisy-label-method control | R1-W1, R1-W2, R2-W2, R4-W2, DA-M1 | CONSENSUS-4 | **Yes** |
| I2 Protocol not stated (splits, checkpoint rule, test/validation naming, seeds, hyperparameters, compute, code) | R1-W3, R1-W4, R4-W2, R4-W4, DA-M7 | CONSENSUS-3 | **Yes** |
| I3 Claims without evidence: efficiency, privacy, tail classes | R1-W5, R1 ERR-2/3, R3-W1, DA-M4, DA-M5 | CONSENSUS-3 | **Yes** |
| I4 Corollaries (Eq. 10/11) unproven and inconsistent | R1-W5/ERR-1, R4-W3, DA-M6 | CONSENSUS-3 | Partly |
| I5 Title/abstract broader than evidence ("In the Wild", natural noise, asymmetric failure) | R1 ERR-4, R1-W6, R4-W1, R3-W4, DA-M3 | CONSENSUS-4 | **Yes** |
| I6 Positioning: no coreset/selection, no DD-under-noise, no privacy literature | R2-W1, R3-W3 | CONSENSUS-2 | No |
| I7 "Vicious cycle" avoided? IPC choice needs noise level | R2-W3, R3-W2, DA-M2 | CONSENSUS-3 | Partly |
| I8 Scale and cost (ConvNet/CIFAR; DATM scalability) | R3-W2, R2 Limitations | CONSENSUS-2 | No |
| I9 Mechanism asserted, not tested | R2-W5, DA ignored alternatives | CONSENSUS-2 | No |
| SPLIT | none (R3 rates 3, others 2; same issues, different weight) | n/a | |
| DA-CRITICAL | none raised | n/a | |

Official output: ratings 2, 2, 3, 2, 2 → mean 2.20; official composite 44.5 (`before.json`). No consistency warnings (all composites imply Overall 2; R3's 3 is within one step). Integrity scan: no findings.

---

# Phase 2: EIC Meta-Review (Prof. Halvard Lindqvist)

I read all five reports and the package first, then the paper (abstract, contributions, Secs. 3–5, captions, references).

## The Case For and Against
- **For acceptance:** The question is novel to this audience: does distillation filter label noise? Three distillers and three noise types are tried, and the failure under structured noise is reported honestly. A clean, short study could be useful to practitioners of both topics.
- **Against acceptance:** The central claim is tested only against a full-data CE ConvNet, with no random-subset, early-stopping or noisy-label-method control, no variance and no stated protocol. The abstract asserts efficiency, privacy and tail-class findings the paper never tests, the two Corollaries are unproven and mutually inconsistent, and the title claims "in the wild" while the only real-noise evidence is CIFAR-N and the realistic structured case fails.

## Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Only comparator is the full-data CE baseline; no subset, early-stopping or noisy-label controls | R1-W1/W2, DA-M1 | Sec. 4 Exp-I; Figs. 2, 4, 5 captions | Verified | Dashed lines are "training on the full dataset"; DivideMix [24], Co-teaching [14] are cited but not run. |
| Protocol not stated; "validation" in captions, "test" in text | R1-W3, DA-M7 | Sec. 4 Implementations; Fig. 2/4 captions; Cor-II | Partly correct | Omission and naming mismatch verified by text search. That the numbers are best-checkpoint test accuracies is a suspicion, not shown. |
| No seeds, variance, hyperparameters, compute, code | R1-W4 | whole paper | Verified | No appendix. |
| Eq. 10 vs Eq. 11 point in opposite directions; δ undefined; no proof | R1 ERR-1, R4-W3, DA-M6 | Sec. 4 Cor-I, Cor-II | Verified | Eq. 11 ⇔ IPC ≥ |S̃|(1−τ)/C; "τ ≥ 0.99 at IPC 50" depends on the reading of "matches the original dataset" and is not relied upon. |
| Tail-class loss presented as a finding but only hypothesised | R1 ERR-2, DA-M4 | Abstract; Sec. 1; Insight-II; Sec. 5 | Verified | No imbalanced dataset in Secs. 3–4; Insight-II says "further hypothesize that challenging clean samples". |
| Efficiency and privacy claimed without measurement | R1-W5/ERR-3, R3-W1, DA-M5 | Abstract; Sec. 1 contribution 1; Sec. 5 | Verified | No timing or privacy experiment; cost excess is an inference, not relied upon. |
| Natural-noise claim overstated: Aggre fails | R1 ERR-4, DA-M3 | Insight-III vs Obs-III | Verified | Obs-III: "like Aggre, these distillation approaches struggle to". |
| Intro says noise is "largely random"; Exp-II says corruption concentrates among similar classes | R3-W4, DA | Sec. 1; Sec. 4 Exp-II | Verified | |
| "Vicious cycle avoided" unsupported since IPC depends on noise level | R2-W3, DA-M2 | Sec. 1; Insight-I; Insight-III | Partly correct | Authors call it open (Sec. 1, Insight-I), so it is an overclaim in the Abstract, not a hidden contradiction. |
| Distillation = early stopping (DATM early trajectories) | R1-W1 | Sec. 2.2 | Partly correct | Plausible alternative explanation, not in the paper; it justifies the control, not a verdict. |
| Related work omits coreset selection, DD-under-noise, privacy studies | R2-W1 | Sec. 2 | Verified | Prior peer-reviewed coreset paper exists (literature check); labels respected. |
| Citation fits [40], [29] | R2-W4 | Sec. 4 Implementations; Sec. 1 | Partly correct | [40] is a Hessian paper as printed; minor. |
| Scale limits | R3-W2 | Sec. 3.2 | Verified | The paper itself notes DATM's "scalability challenges". |
| CIFAR-N rates | DA | Sec. 4 Exp-III | Verified | 9.03, 40.21, 40.20 as printed. |

Missing-comparison weaknesses rest on prior peer-reviewed work (NeurIPS 2020 coresets; CVPR 2025 long-tailed distillation), so the labels allow them as MAJOR-at-most points; no recent preprint or concurrent work was used against the paper. No weakness hinged on a figure value.

## Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Points verified at their locations; calibrated; two inferences (best-checkpoint, cost) were stated as likelier than shown. |
| R2 (Domain) | 2 | 3 | 1.0 | Positioning points verified and borne out by the literature check; citation point only partly right. |
| R3 (Perspective) | 3 | 3 | 1.0 | Accurate; the privacy and assumption points verified; rating one step more lenient, within the role. |
| R4 (Generalist) | 2 | 4 | 1.0 | Accurate and specific enough; largely overlaps R1. |
| DA | 2 | 4 | 1.0 | The strongest counter-argument survived in weaker form; DA-M2 partly overstated; pool position 17 a little harsh for a paper with an honest negative result. |

## DA-CRITICAL Rulings
None raised ("No CRITICAL issues found"). I agree with the DA that nothing meets the strict criteria: there is no test-set selection statement in the text (the checkpoint rule is unstated: a MAJOR question), the baseline weakness and missing controls are by rule MAJOR, and the claim–evidence gaps are fixable by narrowing the claims. DA ceiling: none.

## Final Decision and Justification
The EIC-weighted rating is 2.17, so the starting point is **2 (Reject)**; the composite cross-check (44.1, band 2) agrees. I do not depart. Four verified issues together decide: (1) the only comparator is a plain CE ConvNet trained to convergence, so the headline "denoiser" attribution is not separated from small-set and early-stopping effects (I1); (2) the protocol, selection rule and variance are not stated (I2); (3) three abstract-level claims have no evidence (I3); (4) the title and conclusion are broader than Fig. 4 and Observation-III permit (I5). Each is fixable, but together they need new experiments and a rewrite, which is more than a rebuttal supplies. In the pool, this sits in the lower-middle: **EIC pool position 25** (better than about 25% of ICLR submissions). Deciding evidence: a thin, single-baseline study whose abstract promises more than it measures; the honest negative result and the interesting question keep it above the clearly-below-bar cluster. Overall 3 (a typical rejected submission) would fit only if the controls were present; since they are absent, 2 is the honest reading. This does not exceed any ceiling (none applies).

---

# Score Summary

## Official Scores and EIC Assessment

*From `aggregate_scores.py scores.json --venue iclr --final 2`; the "before" run is `scores_before.json` (no EIC weights, `da_critical` empty).*

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 38 | 42 | 45 | 42 | 36 | 40.6 | 40.3 | 9 |
| Clarity & Presentation | 52 | 55 | 58 | 58 | 50 | 54.6 | 54.3 | 8 |
| Novelty & Originality | 48 | 50 | 55 | 50 | 45 | 49.6 | 49.3 | 10 |
| Significance & Impact | 42 | 45 | 50 | 45 | 40 | 44.4 | 44.1 | 10 |
| Experimental Validation | 35 | 40 | 42 | 38 | 33 | 37.6 | 37.2 | 9 |
| Reproducibility | 32 | 38 | 40 | 38 | 32 | 36.0 | 35.6 | 8 |
| Ethical Compliance | 55 | 55 | 50 | 52 | 48 | 52.0 | 52.1 | 7 |
| **Composite** | 42.3 | 45.6 | 48.9 | 45.5 | 40.0 | **44.5 (before)** | **44.1 (after)** | |
| Pool position | 20 | 28 | 35 | 27 | 17 | | EIC: 25 | |

No dimension has a spread above 20. Official ratings 2, 2, 3, 2, 2: mean **2.20**. EIC-weighted rating **2.17**. Final (EIC): **2**.

## Target-Venue Scores (ICLR 2026 cycle, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating | **2 on {0,2,4,6,8,10}** (3 on the earlier {1,3,5,6,8,10} scale) |
| Skill-internal label | Overall 2 = Reject |

*Verification status for the ICLR scale is "secondary": treat the labels as a translation, not official wording.*

---

# Editorial Decision

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: analysis
## Review Team (fictional personas): EIC Prof. Halvard Lindqvist; R1 Dr. Anjali Deshmukh-Rao (Methodology), R2 Prof. Xiulan Qiao (Domain), R3 Dr. Camila Ferreira-Nunez (Perspective), R4 Dr. Rafiq Haddad (Generalist), DA Prof. Elena Marchetti-Brandt

## Decision: Reject (2). ICLR rating 2 on {0,2,4,6,8,10}

**Official ratings** (shown to authors): R1 2, R2 2, R3 3, R4 2, DA 2 → mean 2.20 · official composite 44.5
**EIC assessment** (internal): weighted rating 2.17 → starting point 2 · weighted composite 44.1 → band 2 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 2

*This is how a careful panel would likely see this draft; it is a simulation, not a prediction.*

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Dataset Distillers Are Good Label Denoisers In the Wild" to ICLR. The question of whether dataset distillation filters label noise is interesting, and linking it to the memorisation literature is a good starting point.

**Overall Assessment:** The reviewers found the question fresh and the three-distiller design sensible, and they valued the honest report that structured asymmetric noise is absorbed. They agreed, however, that the evidence does not yet support the headline claims. We note that all curves (Figs. 2–5) were assessed from captions and text only.

**Key Strengths Identified by Reviewers:**
1. A clear, testable hypothesis across three distillation families and three noise types (R1, R2, R4).
2. Honest reporting of the failure under asymmetric noise (R1, R2, R3, DA).
3. A cross-community idea with potential practical interest (R2, R3).

**Key Concerns Requiring Attention:**
1. The only comparator is a plain cross-entropy ConvNet; no random-subset, early-stopping, hard-label or noisy-label-method control isolates the effect of distillation (CONSENSUS-4).
2. The protocol (splits, checkpoint rule, "validation" vs "test"), seeds, variance, hyperparameters and compute are not stated (CONSENSUS-3).
3. The efficiency, privacy and tail-class claims in the abstract have no supporting experiment, and Corollaries I–II are unproven and point in opposite directions (CONSENSUS-3).
4. The title and conclusion go beyond the evidence (asymmetric noise and the low-noise CIFAR-N setting both fail) (CONSENSUS-4).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection is that the gains may reflect small-set or early-stopping effects against a weak baseline, and that choosing IPC needs the very noise estimate the paper says it avoids; this is a MAJOR concern that the authors can address with controls and narrower claims.

**Decision: Reject (2)**

The weaknesses are fixable but together require new experiments and a reframing. A revised version with controls, a stated protocol with seeds, a narrowed title and abstract, and positioning against coreset selection and distillation-privacy work would be a much stronger submission. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Halvard Lindqvist, Editor-in-Chief (meta-reviewer, fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Missing attribution controls and weak baseline (I1) | R1, R2, R4, DA | CONSENSUS-4 |
| Title/abstract broader than evidence (I5) | R1, R3, R4, DA | CONSENSUS-4 |
| Protocol, seeds, variance not stated (I2) | R1, R4, DA | CONSENSUS-3 |
| Efficiency, privacy, tail-class claims untested (I3) | R1, R3, DA | CONSENSUS-3 |
| Corollaries unproven/inconsistent (I4) | R1, R4, DA | CONSENSUS-3 |
| "Vicious cycle" avoidance and IPC dependence on noise level (I7) | R2, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall rating | R3 (3) | R1, R2, R4, DA (2) | Same issues cited; R3 weighs the idea's potential more. Weighted outcome 2.17; the controls are absent, so 2 stands. |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag (maximum 10, Novelty and Significance).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Attribution controls | Yes (R1, R2, R4) | n/a | n/a |
| DA-M2 | MAJOR | Loop avoidance vs IPC-needs-τ | Yes (R2, R3) | n/a (Partly correct, see verification) | n/a |
| DA-M3 | MAJOR | Title/abstract scope | Yes (R1, R3, R4) | n/a | n/a |
| DA-M4 | MAJOR | Tail-class claim | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Efficiency/privacy claims | Yes (R1, R3) | n/a | n/a |
| DA-M6 | MAJOR | Eq. 10/11 | Yes (R1, R4) | n/a | n/a |
| DA-M7 | MAJOR | Protocol | Yes (R1, R4) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Attribution controls: random subset at same IPC, early-stopped (best and last epoch) full-data model, hard-label ablation, small-loss/coreset selection | R1-W1, R2-W2, R4-W2, DA-M1 | Figs. 2, 4, 5; Sec. 4 | Add the controls for all noise settings | Medium; ≈ 20–40 GPU-h | Yes (CIFAR-scale) |
| R2 | At least one noisy-label baseline on the same ConvNet (GCE, Co-teaching, DivideMix or ELR) | R1-W2, R2-W1 | Sec. 4 | Add and discuss | Medium; ≈ 20–60 GPU-h | Partly |
| R3 | State the protocol: splits, validation-based checkpoint rule, baseline epoch rule, seeds, hyperparameters, initialisation, soft-label use, compute; release code | R1-W3/W4, R4-W4, DA-M7 | Sec. 4 Implementations | Add a protocol paragraph/appendix; 3 seeds with mean ± std | High for DATM/RCIG on CIFAR-100/Tiny-ImageNet; ≈ 100–200 GPU-h | Partly |
| R4 | Narrow or substantiate claims: tail classes, efficiency, privacy, "in the wild", natural noise | R1 ERR-2/3/4, R3-W1, R4-W1, DA-M3/M4/M5 | Title, Abstract, Sec. 1, Sec. 5 | Either run CIFAR-LT, a cost table and a membership-inference test, or reword as hypotheses and restrict scope | Low (rewording) to Medium | Yes (rewording) |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Corollaries I–II: unproven, opposite directions, δ undefined | R1 ERR-1, R4-W3, DA-M6 | Derive and test on the existing curves, or relabel as heuristics | Medium | Yes |
| S2 | "Vicious cycle" avoided? IPC depends on noise level | R2-W3, R3-W2, DA-M2 | Show a noise-agnostic IPC rule (e.g., a small clean validation subset) or drop the claim | Medium | Partly |
| S3 | Positioning: coreset selection under noise (Mirzasoleiman et al., NeurIPS 2020), distillation privacy (Chen et al. 2023; Dong et al., ICML 2022), long-tailed distillation (Zhao et al., CVPR 2025), early-learning regularisation (Liu et al., NeurIPS 2020) | R2-W1, R3-W3 | Add a related-work paragraph and differentiate | Low | Yes |
| S4 | Mechanism diagnostics (nearest-neighbour label consistency, soft labels vs images) | R2-W5 | Add one diagnostic per distiller | Medium | Partly |
| S5 | Scope: one real-noise benchmark at feasible IPC; asymmetric noise on Tiny-ImageNet | R1-W6, R3-W2 | Add or narrow | Medium to High | No |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Notation: τ overloaded (Eq. 1 vs Eq. 8 text); θ̂_{t+N} vs θ̂_{t+T} (Eq. 4) | R1, DA-m1/m2 | Rename symbols |
| N2 | "Realted Works"; footnote caveats; Obs-III dataset wording | R1, R4, DA-m3/m4 | Fix |
| N3 | Citation fit of [40] and [29] | R2-W4 | Use the standard sources |
| N4 | Add a Limitations section | R3 | Short paragraph |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–3 weeks including 3-seed runs (≈ 150–300 GPU-h in total)
- Priority 2: 5 items, about 1–2 weeks
- Priority 3: 4 items, 1–2 days
- **Total estimated revision time**: roughly 4–6 weeks for a resubmission

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
