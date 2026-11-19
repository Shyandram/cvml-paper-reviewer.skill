# Academic Paper Reviewer v2.10.1: Full Review (simulation)

**Date:** 2026-11-10 · **Mode:** full · **Target venue:** ICLR (stated; profile key `iclr`, 2026 cycle, scale status *secondary*) · **Literature check:** requested `strict`, cutoff 2025-09-24. **Not run:** the network was unreachable (two `related_search.py` queries timed out), so per the skill the check fell back to `off`. Missing-reference suggestions below come from knowledge only, with `[verify]` where unsure. No baseline scout, similarity or claim-novelty script output exists.

**Process disclosure:** the five reviewer passes were done sequentially by one model context, each from its own role file. They are not independent agents. The EIC pass came last, after the five reports. Figures were not available, so figure-dependent claims are judged from captions and text only; where it matters this is stated.

**Integrity scan:** `integrity_scan.py` found no reviewer-directed text or hidden characters. The extracted text shows author names and affiliations. They were ignored and influenced no score. *Recognition note:* the title was familiar from prior knowledge. Its outcome is unknown to me, and the review is on the merits.

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation |
| Primary Discipline | Machine learning → dataset condensation / distillation (bilevel optimization) |
| Secondary Discipline(s) | Sharpness-aware optimization, hypergradient estimation, continual learning |
| Paper Type | Empirical (method with supporting propositions); composite weights: empirical |
| Core Technique(s) | Trajectory matching (MTT), SAM on the synthetic data, truncated unrolling, trajectory reuse, first-order learning-rate update |
| Target Venue | ICLR (stated by the user); profile key `iclr` |
| Venue-Specific Notes | None (ICLR form: Soundness, Presentation, Contribution, Rating, Confidence). Base rate: ≈27% of submissions accepted. |
| Paper Maturity | Submission-ready draft (code "will be released") |
| Ethics-Relevant Content | None (public image benchmarks, no human-subject data) |

### Claimed Contributions (as stated by the authors)
1. **C1:** SATM jointly minimises the sharpness of the outer-loop landscape and the trajectory distance, with a "tailored loss landscape smoothing strategy" (Section 1, Section 4.1).
2. **C2:** Two approximation strategies, truncated unrolling hypergradient (TUH) and trajectory reusing (TR), handle the cost of sharpness minimisation with "controllable memory cost" (Section 1, Section 4.2).
3. **C3:** A closed-form learning-rate update (Eq. 10), with "rigorous theoretical support by bounding the errors of" (Section 1).
4. **C4:** SATM outperforms trajectory-matching competitors in- and out-of-domain, with "noticeable improvement margins" on ImageNet-1K (Section 1, Tables 2–5).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Datasets are CIFAR-10/100, Tiny-ImageNet, four ImageNet subsets at 128×128 and ImageNet-1K (Appendix A.8). Experts are 3/4/5-layer ConvNets (A.8). ZCA is applied everywhere (Table 11). Hyperparameters are in Table 11, which has no ImageNet-1K row, no ImageNet-subset row and no Tiny-ImageNet IPC 50 row. ρ, γ, ι and τ values: not stated after search (τ = ι is stated in Section 4.2). Compute: V100/A100 GPUs for training (A.5), A6000 for timing (Section 5.2). Seeds and number of runs behind "±": not stated for the main tables. Appendix A.7 says "We repeat each method 5 times". Validation split or tuning split: not stated. Baseline numbers: "We cite the results of DC, DM and MMT from FTD" (Table 2 caption). Provenance of the TESLA, MDC and FTD numbers: not stated.
- **Headline numbers.** The abstract has none. Section 1 claims margins over TESLA in runtime "with comparable memory consumption". Table 2 (accuracy), Table 4 (ImageNet-1K vs TESLA), Table 6 (cost).
- **Appendix summary.** Proofs (A.1, A.2), pseudocode (A.3), learning-rate derivation (A.4, Fig. 3), compute (A.5), SATM-FI (A.6, Table 9), sharpness-optimiser compatibility (A.7, Table 10), datasets (A.8), hyperparameters (A.9), synthetic-image figures (A.10).
- **Unverifiable.** All figures (1, 2, 3, 4–7) and the visual claims about them. Fig. 1 has no numbers in the text. Some extracted equations (3, 8, 9) are garbled and are judged only where the structure is clear.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valdemar, optimisation and learning group, large public university (Northern Europe)
- **Seniority / Expertise:** senior faculty / bilevel optimisation, generalisation theory, dataset-efficient learning
- **Role:** reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style:** area chair who asks what the evidence supports, as opposed to what is claimed

### Reviewer 1 (Methodology): Dr. Tomasz Reyes-Anand, industry research lab (North America)
- **Seniority / Expertise:** mid-career / dataset-distillation evaluation protocols, hypergradient estimation
- **Review Focus:** research design, statistics, comparison fairness, reproducibility
- **Style:** recomputes every table delta, wants every component ablated

### Reviewer 2 (Domain): Dr. Farah Nasrallah-Ortega, vision and efficient-learning lab, public university (Middle East)
- **Seniority / Expertise:** senior postdoc / coreset selection, dataset condensation and ImageNet-scale distillation
- **Review Focus:** literature, theoretical framework, domain contribution
- **Style:** checks each novelty claim against what the cited work actually does

### Reviewer 3 (Perspective): Dr. Mateus Brandão-Ito, numerical optimisation and meta-learning group, university (South America)
- **Seniority / Expertise:** mid-career / loss-landscape theory, implicit differentiation, robust optimisation
- **Review Focus:** cross-disciplinary connections, deployment, assumptions, broader impact
- **Style:** constructive; looks for what the idea could become

### Reviewer 4 (Generalist): Dr. Sunniva Halvorsen, ML group, public university (Nordic Europe)
- **Seniority / Expertise:** mid-career / deep learning generalist, data-efficient training
- **Review Focus:** contribution clarity, venue fit, presentation
- **Style:** typical program-committee member, reads for the story and the evidence

### Devil's Advocate: Prof. Bernard Achterberg, statistical learning and evaluation methodology, university (Western Europe)
- **Seniority / Expertise:** senior faculty / causal attribution in ablations, evaluation validity
- **Review Focus:** core-argument challenges, logic, overclaiming
- **Style:** rigorous and fair; asks what else could explain the result

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Reviewer Reports

---

# Peer Review Report

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Reviewer: Dr. Tomasz Reyes-Anand, Reviewer 1 (Methodology) (industry research lab, North America; fictional persona)
## Expertise: dataset-distillation evaluation protocols; hypergradient estimation; ablation design
## Date: 2026-11-10

## Summary
The paper applies sharpness-aware minimisation to the synthetic images of trajectory-matching dataset condensation (MTT-style). The perturbation is a normalised hypergradient step (Eq. 7), preceded by Gaussian noise on the images (Section 4.1). Two devices cut the cost: backpropagating only through the last steps of the unrolled inner loop (TUH), and reusing the first trajectory's midpoint for the perturbed pass (TR). The learning rate is updated with a first-order rule (Eq. 10). Results are reported on CIFAR-10/100, Tiny-ImageNet, ImageNet subsets and ImageNet-1K, plus cross-architecture, continual-learning and cost studies.

## Strengths
### S1: Broad evaluation axes
In-domain accuracy (Tables 2–3), cross-architecture transfer (Table 5), continual learning (Fig. 1), ImageNet-1K vs TESLA (Table 4), and cost (Table 6) all appear. The set of axes suits the claim of "generalization".
### S2: Cost is measured, not only argued
Table 6 gives memory and runtime on one GPU type for MTT, TESLA and SATM. On CIFAR-100 SATM uses 5.7 GB against MTT's 17.1 GB at about equal runtime (12.0 s vs 12.1 s). This supports a real memory saving over MTT.
### S3: Useful appendix controls
Table 10 repeats five times and compares SAM, GSAM, ASAM and Vasso (with the smoothing removed) on a shared base. Table 8 gives a truncation sweep, which exposes the accuracy cost of truncation.
### S4: Honest sensitivity to truncation
Table 8 shows the method degrades sharply when too few steps are retained (CIFAR-100 50 IPC: 23.4 at 1/6 vs 50.9 at 1/3). Reporting this is useful.

## Weaknesses
### W1: The component contributions are not isolated (C1, C2, C3)
SATM bundles four changes relative to MTT: the SAM ascent step, Gaussian smoothing (Section 4.1), TUH/TR (Section 4.2) and the first-order learning-rate rule (Eq. 10). No table removes them one at a time. Table 10 is the closest: with smoothing removed, plain SAM already gets CIFAR-100 (1 IPC) from MTT's 24.3 to 25.7 and Tiny-ImageNet (3 IPC) from 10.5 to 12.3, against SATM's 26.1 and 13.6. Derived: SAM alone recovers about 78% and 58% of SATM's gain over MTT. The paper never shows the smoothing contribution alone, TUH/TR's effect on accuracy at equal compute, or the learned-rate effect. The attribution to "flatness" (Section 5.1, results attributed to flat minima) is therefore not tested. 
- **Suggested Fix:** a 2×2×2 ablation (smoothing, TUH/TR, Eq. 10 vs MTT's learned rate) on CIFAR-100 IPC 10 and Tiny-ImageNet IPC 1, plus "MTT + vanilla SAM, no TUH/TR". About 5–8 runs per cell, ≈ 60–100 GPU-hours.
### W2: Gains are mostly within the reported noise, but the wording is strong (C4)
Recomputed from Table 2, SATM's margin over the best baseline in each cell is +0.5, +0.4, +0.1 (CIFAR-10, IPC 1/10/50), +0.2, −0.3, +0.2 (CIFAR-100) and +0.5, +0.6, +1.2 (Tiny); mean +0.38, and 7 of 9 margins are ≤ 0.5. Typical stds are 0.2–0.8. Table 3 margins over FTD are +0.5, +0.6, +0.3, +2.1 with stds 0.5–2.2. Table 4 margins over TESLA are +1.2, +1.4, +1.3 with TESLA stds up to 1.3. The text claims results in "almost all the settings of the standard dataset condensation" and "Still, there are clear improvement margins over" competitors. The paper does not state what the ± covers (evaluation networks trained on one distilled set, or independent distillation runs).
- **Suggested Fix:** state what ± covers; run ≥3 independent distillations for the headline cells; add paired tests or CIs; word C4 as "comparable to or slightly above" where the margin is inside one std.
### W3: Hyperparameter and selection protocol are not stated
After the protocol sweep (`test set`, `validation`, `tuned`, `selected`, `best`), no validation split, tuning split or selection rule is stated. ρ and γ appear nowhere with values. ι/τ choices appear only through Table 8, where CIFAR-100 50 IPC at 1/3 (50.9) is both the best of the sweep and the number in Table 2, while for CIFAR-10 1 IPC 1/2 (49.2) beats the reported 49.0. Appendix A.7 says competitors' hyperparameters "are properly tuned", with no split named. Field practice for CIFAR-style condensation is to report test accuracy, but the tuning split should be stated and a held-out check shown.
- **Suggested Fix:** state the split used for each choice; report ρ, γ, ι, τ per setting; add a held-out (e.g., validation-carved) check for the ρ/γ/ι choices. Low cost.
### W4: Efficiency claims contain internal inconsistencies (C2)
Section 4.2 says "our model also achieves constant memory", but Table 1 gives O(P(N−ι)), and Section 5.2 says "at most only one-third of the inner" loop is retained, so memory scales with N/3. Table 1 gives time O(cN + cτ), above MTT's O(cN), while Table 6 and Section 5.2 report SATM equal to or faster than MTT ("SATM even consumes less time than MTT"). On ImageNet-1K SATM is 45.4 vs MTT 45.9 s (±0.4/0.5), which is not a distinguishable gap. Against TESLA, CIFAR-100 memory is 5.7 vs 3.6 GB (+58%, derived), which does not fit "comparable memory consumption" in Section 1. No row measures the naive "MTT + SAM" cost, so the saving TUH/TR gives over the direct application of SAM is not measured.
- **Suggested Fix:** reconcile the text with Table 1; add an "MTT + vanilla SAM" row to Table 6; define the cost model (forward vs backward steps). Low–medium cost.
### W5: Theory does not support the claim of bounded approximation errors (C3)
See ERR-2 and ERR-3 below. In short, Theorem 4.2's bound is linear in τ with an additive 2σ that does not vanish when ε = 0, so it says nothing about when reuse is accurate, and Proposition 4.1 assumes local strong convexity along a short non-converged trajectory. No bound or empirical error is given for Eq. 10. Fig. 3 is one setting, and shows learning-rate curves, not accuracy.
- **Suggested Fix:** measure ‖θ_τ(ϕ+ε) − θ̂_τ‖ and the truncation cosine error empirically; state assumptions as heuristics where they are not verified; drop "rigorous" for Eq. 10.
### W6: Reproducibility gaps
Table 11 omits ImageNet-1K, the ImageNet subsets and Tiny-ImageNet IPC 50. Training used three GPU types on different servers (Appendix A.5), and the outer loop is mini-batched for CIFAR-100 IPC 10/50 and Tiny-ImageNet IPC 1 where baselines run full batch ("we cannot run the full batch of synthetic dataset learning"). Code is only promised.
- **Suggested Fix:** complete Table 11; say whether the cited baselines were rerun under the same batching.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 5 vs Table 2 / Table 9 | (tables) | SATM on CIFAR-10 50 IPC, ConvNet: 74.2±0.3 in Table 5, 73.9±0.2 in Tables 2 and 9. MTT 10 IPC: 64.3±0.7 in Table 5, 65.4±0.7 in Table 2. | Cross-referenced two tables | High | MAJOR | Say which is correct or which runs differ |
| ERR-2 | E2 | Appendix A.1, Theorem 4.2 | "carefully chosen learning rate α" | The proof bounds ‖∇L(ϕ,θ̂ᵢ) − ∇L(ϕ,θᵢ)‖ by the constant 2σ although L is declared σ-smooth (gradient-Lipschitz), which would give σ‖Δθᵢ‖. A constant 2σ needs bounded gradients. The final bound is nonzero at ε = 0, where the two trajectories coincide. | Derived from the proof lines | Medium | MAJOR | Use the growth-recursion form or state a gradient-norm bound; show a non-vacuous regime |
| ERR-3 | E2 | Appendix A.2, Proposition 4.1 | "In the worst case, when LCE is K-smooth but nonconvex" | The proof stops after ‖Aᵢ‖ ≤ 2. The stated factor "2ι" is not derived; a product of up to ι matrices of norm ≤ 2 gives an exponential factor, not 2ι. The (1−αJ)^(N−ι+1) factor is near 1 for small α and J. | Re-derived from the proof | Medium | MAJOR | Complete the proof; evaluate the bound with measured α, J |
| ERR-4 | E6 | Section 4.2 vs Table 1, Section 5.2 | "our model also achieves constant memory" | Table 1 lists O(P(N−ι)), and Section 5.2 retains one-third of the loop, so memory grows with N. | Cross-referenced three locations | High | MAJOR | Reword to "reduced memory" or make N−ι fixed |
| ERR-5 | E6 | Figure 2 caption vs Section 5.2; Figure 1 caption vs Section 5.1 | "norm on Cifar100 with 10 IPC" | Caption says CIFAR-100 10 IPC; text says "Cifar100 with 3 IPC". Fig. 1 says class-incremental; text says "task incremental setting". | Cross-referenced | High | MINOR | Align |

## Missing References
*Not my role; see Reviewer 2.*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Components not isolated; gains within noise; theory loose. |
| Clarity | 2 | Notation (ι, τ, κ) and cost claims are inconsistent. |
| Significance | 2 | Small, uncertain gains on mature benchmarks. |
| Originality | 2 | SAM plus truncation and reuse; a combination, not isolated. |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline margins are mostly inside one std and the paper's own Table 10 attributes most of the gain to generic SAM, so the central causal claim is untested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Proof gaps (ERR-2, ERR-3), internal cost inconsistencies, selection protocol unstated. |
| Clarity & Presentation | 55 | Competent | Understandable, but notation and caption/text mismatches. |
| Novelty & Originality | 50 | Developing | Combination of known pieces; no ablation shows what is new. |
| Significance & Impact | 50 | Developing | Gains are small on benchmarks where +0.5 is incremental. |
| Experimental Validation | 45 | Developing | No component ablation; ± undefined; DATM missing from Tables 2–3. |
| Reproducibility | 42 | Developing | ρ, γ, ι, τ and ImageNet settings missing; code promised only. |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations paragraph is thin. |

## Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Sharpness minimisation + smoothing improves generalisation | Section 1, 4.1 | Tables 2, 5, 10; Fig. 2 | Partially: improvements exist, but attribution to flatness untested |
| C2 | TUH + TR cut cost with controllable memory | Section 4.2 | Table 6, Table 8, Table 1 | Partially: memory saving vs MTT real; "constant" wrong; accuracy cost under heavy truncation |
| C3 | Bounded errors, closed-form learning rate | Section 1, 4.2, A.4 | Thm 4.2, Prop 4.1, Fig. 3 | Unsupported as "rigorous" (no bound for Eq. 10; loose bounds elsewhere) |
| C4 | Outperforms TM competitors; noticeable margins on ImageNet-1K | Section 1, 5.1 | Tables 2–5 | Partially: best in 8 of 9 cells of Table 2 but margins mostly ≤ 1 std; scope excludes DATM/RDED |

## Questions for Authors
1. What does "±" cover in Tables 2–5, and how many independent distillations were run? (A paired result showing the Table 2 margins hold over ≥3 distillations would raise my score.)
2. On which split were ρ, γ, ι and the baselines' hyperparameters chosen, and what are their values? (A held-out result would remove my main reproducibility concern.)
3. What does SATM give with smoothing only, TUH/TR only, and Eq. 10 vs MTT's rate? (An ablation showing the smoothing and flatness are the cause would raise my score; a result where SAM alone matches SATM would lower it.)
4. Table 6 reports 26.6 GB for MTT, TESLA and SATM on ImageNet-1K, while Section 5.2 says MTT "required two A6000 GPUs". Is this per GPU, and was it measured the same way? (Low confidence, so a question rather than a weakness.)
5. Do Table 4's SATM numbers use any soft-label or relabelling step, and are TESLA's numbers copied from its paper or rerun?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. Section 6 says "these possibilities are not explored in this work" about extensions, but states no limitation of the method itself (accuracy collapse under heavy truncation in Table 8, ConvNet-only experts, small-scale benchmarks).

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: a plausible, broadly evaluated idea, but the evidence does not isolate what causes the gains, which are small relative to the noise, and the theory and cost claims overreach.

## Confidence
**4**: confident; I recomputed the tables, but the figures and some equations could not be inspected.

---

# Peer Review Report

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Reviewer: Dr. Farah Nasrallah-Ortega, Reviewer 2 (Domain) (vision and efficient-learning lab, Middle East; fictional persona)
## Expertise: dataset condensation and distillation; coreset selection; ImageNet-scale distillation
## Date: 2026-11-10

## Summary
SATM adds a sharpness-aware outer-loop step to MTT-style trajectory matching for dataset condensation and offers cheaper hypergradient estimation. The authors argue that flat outer-loop regions improve cross-architecture and continual-learning performance. The positioning is against the trajectory-matching lineage (MTT, FTD, TESLA, DATM) and, loosely, SAM variants. Literature check was unavailable (see header), so the novelty table below uses the paper's own related work and my knowledge.

## Strengths
### S1: Clear and relevant gap
Trajectory-matching methods overfit the expert architecture (Section 2.1). Targeting cross-architecture generalisation is a recognised weakness of the line.
### S2: Honest comparison with flat-trajectory work
Section 5.1 and Appendix A.6 compare to FTD and note that SATM is built on vanilla MTT without FTD's flat experts. The compatibility study (SATM-FI, Table 9) is a sensible check.
### S3: Positioning relative to SAM variants
Appendix A.7 and Table 10 compare SAM, GSAM, ASAM and Vasso on the same expert trajectories, with 5 repeats. This ties the work to the sharpness-aware literature.
### S4: Cross-architecture evidence
Table 5 at IPC 50 shows +3.1 (AlexNet) and +5.1 (VGG11) over FTD, the strongest evidence for the generalisation claim.

## Weaknesses
### W1: Novelty is incremental and not delineated from close prior work (C1, C2)
Per-claim view (knowledge-based, not script-derived):
- *C1 (method, SAM on synthetic data + noise):* SAM for bilevel problems is in Sharp-MAML (Abbas et al., 2022), which the paper cites, and the random smoothing before the ascent step follows Random SAM (Liu et al., 2022), also cited. The transfer to dataset condensation is new, but the delta is the application, and no table shows the smoothing's own effect. *Verdict: medium to incremental.*
- *C2 (TUH):* backpropagating only through the last steps of an unrolled inner loop is the truncated back-propagation of Shaban et al. (AISTATS 2019), which is not cited. TESLA already reaches constant memory. *Verdict: incremental.* The cited-and-differentiated column is "no" for Shaban.
- *C3 (Eq. 10):* learning-rate learning inside MTT already exists (MTT learns the synthetic step size by backprop); Eq. 10 drops the second-order term. *Verdict: incremental.*
- *C4 (result):* see W2.
This is MAJOR at most (cite, differentiate, narrow claims); it does not make the paper "known".
- **Suggested Fix:** add a novelty-delta paragraph against truncated backprop for bilevel, implicit-gradient condensation, and Random SAM; claim the application and the efficiency combination, not the individual parts.
### W2: The headline comparison set is narrower than the claim (C4)
Tables 2 and 3 omit DATM (ICLR 2024), which Section 2.1 lists with MTT, FTD and TESLA as trajectory-matching work. DATM appears only in Table 7, in a combined SATM-DA variant. There, SATM-DA is below DATM on Tiny-ImageNet IPC 1 (16.4 vs 17.1) and above on CIFAR-100 IPC 1 by 0.3 (inside the stds), and CIFAR-10 is missing. In the introduction, the statement that most existing methods fail to condense ImageNet-1K ignores decoupled and relabelling approaches for ImageNet scale, for example RDED, which the paper cites in Section 2.1 but does not compare to or discuss.
- **Suggested Fix:** add DATM to Tables 2–3 (with the soft-label difference marked), complete Table 7 with CIFAR-10, and qualify the ImageNet claim to bilevel/trajectory methods or add a protocol-matched comparison.
### W3: The theoretical link between data-space flatness and generalisation is assumed
SAM's generalisation argument is about flatness in model-parameter space. Here the perturbation is applied to the synthetic pixels ϕ of the outer objective (Eq. 5). Section 4.1 cites uni-level results (Petzka et al., 2021; Kaddour et al., 2022) and does not argue why flatness w.r.t. ϕ should transfer to networks of other architectures. Fig. 2 (from text and caption) reports hypergradient norms, which are not a sharpness measure, and the sharpness panel is labelled for SATM only.
- **Suggested Fix:** measure parameter-space sharpness of networks trained on SATM vs MTT sets, or state this as a hypothesis.
### W4: Citation and baseline provenance
The Table 2 caption says "We cite the results of DC, DM and MMT from FTD" (MMT is presumably MTT); the provenance of TESLA, MDC and FTD numbers is not stated, and Table 5's MTT 10 IPC value (64.3) differs from Table 2's (65.4) (see R1 ERR-1).
- **Suggested Fix:** mark copied vs reproduced rows (†) and the setting each came from.

## Missing References
*Literature check `off` (no network), so these are from knowledge. Titles I am confident of are given in full without links; the rest are marked `[verify]`. Only peer-reviewed work before the cutoff is listed as Critical or Important.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Shaban, Cheng, Hatch, Boots. "Truncated Back-propagation for Bilevel Optimization." AISTATS 2019 | Direct precedent of TUH and its error analysis; not cited |
| Important | Loo, Hasani, Lechner, Rus. "Dataset Distillation with Convexified Implicit Gradients." ICML 2023 | Implicit-gradient alternative to unrolling; the paper lists implicit gradients as future work |
| Important | Yin, Xing, Shen. "Squeeze, Recover and Relabel: Dataset Condensation at ImageNet Scale From A New Perspective." NeurIPS 2023 | Context for the ImageNet-1K claim |
| Important | Shao et al. "Generalized Large-Scale Data Condensation via Various Backbone and Statistical Matching." CVPR 2024 | ImageNet-scale condensation with cross-architecture transfer |
| Helpful | Liu, Wang, Yang, Ye, Wang. "Dataset Distillation via Factorization." NeurIPS 2022 | Compact parameterisation as another route to cross-architecture generalisation |
| Helpful | Liu et al. "Dataset Distillation by Automatic Training Trajectories." ECCV 2024 `[verify]` | Recent trajectory-matching variant |
| Helpful | Zhang et al. "Accelerating Dataset Distillation via Model Augmentation." CVPR 2023 `[verify]` | Cross-architecture robustness in trajectory-matching distillation |

## Field snapshot (knowledge-based, ≈160 words)
Trajectory matching (MTT, 2022) displaced gradient and distribution matching on CIFAR-scale ConvNet benchmarks, then FTD, TESLA and DATM refined it (flat experts, constant memory, curriculum plus soft labels). From 2023 onward, ImageNet-scale work moved to decoupled methods with pretrained teachers and relabelling, which report much higher ImageNet-1K numbers under different protocols (larger networks, soft labels). On CIFAR/Tiny with ConvNets, gains of 0.1–0.5 points are incremental; a meaningful contribution here is a clear cross-architecture gain, a new capability, or a large efficiency gain at equal accuracy. I used this to score Novelty and Significance below the accepted band. It is not from a search.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence does not isolate the mechanism. |
| Clarity | 2 | Positioning clear, notation uneven. |
| Significance | 2 | Marginal gains on mature benchmarks. |
| Originality | 2 | Application of known pieces; delta not delineated. |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: cross-architecture gains at IPC 50 are real, but the remaining evidence is small margins and an incomplete comparison set.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Sound idea; theory loose but not the core of the claim. |
| Clarity & Presentation | 55 | Competent | Reads fine; positioning adequate. |
| Novelty & Originality | 48 | Developing | Incremental per claim; no delta table in the paper. |
| Significance & Impact | 52 | Developing | Useful if cross-architecture gains hold. |
| Experimental Validation | 52 | Developing | Breadth good; comparison set incomplete. |
| Reproducibility | 50 | Developing | Missing hyperparameters. |
| Ethical Compliance | 62 | Competent | Nothing at stake. |

## Questions for Authors
1. Why are DATM and RDED excluded from the main tables, and how do results change when DATM's soft labels are matched? (A fair comparison where SATM stays ahead would raise my score.)
2. How does TUH differ from truncated backpropagation for bilevel optimisation (Shaban et al., 2019)? (A clear difference would raise my Novelty score.)
3. Can you show parameter-space sharpness of the downstream networks? (This would test the data-space-flatness premise.)

## Limitations Assessment
**Partially.** No method limitation is discussed; the ImageNet and cross-architecture scope is limited to ConvNet experts.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: an application of known components with some real cross-architecture gains; positioning and comparison set need work.

## Confidence
**4**: confident on the lineage; literature search unavailable, so some novelty statements rest on memory (marked).

---

# Peer Review Report

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Reviewer: Dr. Mateus Brandão-Ito, Reviewer 3 (Perspective) (numerical optimisation and meta-learning group, South America; fictional persona)
## Expertise: loss-landscape theory; implicit differentiation; robust optimisation
## Date: 2026-11-10

## Summary
The paper brings sharpness-aware minimisation into the outer loop of dataset condensation, where the "parameters" being perturbed are the synthetic images. To keep the doubled cost in check it truncates the unrolled differentiation and reuses part of the trajectory. The work sits at an interesting meeting point of meta-learning, hypergradient methods and flat-minima theory, and the practical aim is cheaper, more transferable condensed data.

## Strengths
### S1: A neat bridge between two literatures
Moving SAM from weights to data in a bilevel problem is a natural idea that has not obviously been tried for trajectory matching. It also allows ordinary SAM variants to plug in (Appendix A.7, Table 10), which shows that the idea is not tied to one optimiser.
### S2: Practical memory saving
Table 6 shows 5.7 GB vs 17.1 GB for MTT on CIFAR-100 at similar runtime. This matters for users with a single mid-range GPU.
### S3: Evidence beyond the usual single table
Cross-architecture (Table 5), continual learning (Fig. 1) and the compatibility study broaden the picture. At IPC 50 the transfer gains to VGG11 (+5.1 over FTD) and AlexNet (+3.1) are the most convincing evidence of practical value.
### S4: Useful negative information
Table 8 shows how quickly accuracy falls with heavy truncation, which tells practitioners how far the shortcut can be pushed.

## Weaknesses
### W1: The central assumption (flatness in data space implies transferable data) is not examined
In the usual story a flat weight-space minimum generalises because the test loss is insensitive to small weight shifts. Here the perturbation is in ϕ, and the object that must generalise is the downstream student network trained on ϕ. These are different objects. A direct test would measure the weight-space sharpness of networks trained on SATM vs MTT sets, or evaluate robustness under data-side perturbations. Fig. 2 is described via hypergradient norms, which are gradients rather than curvature; per the text and caption, the sharpness panel shows SATM only (figure not available to me).
- **Suggested Fix:** add the weight-space sharpness or robustness comparison; frame the flatness link as a hypothesis until then.
### W2: The theory is loose, and the closeness of the approximations is never measured
Theorem 4.2's bound grows linearly with τ and carries a 2σ term even when ε = 0, so it cannot tell a practitioner when trajectory reuse is safe. Proposition 4.1 assumes local strong convexity along the retained steps, while the inner loop in practice is a short non-converged segment from an expert checkpoint (Section 4.2: "in the setting where the synthetic trajectory is produced by" optimisation "until converge"). Measuring the actual discrepancy (cosine between truncated and full hypergradients; ‖Δθ_τ‖) on one setting would be more informative.
- **Suggested Fix:** report those two measured quantities across ι and τ, next to Table 8's accuracy.
### W3: Scale and deployment assumptions
All experts are 3–5-layer ConvNets (Appendix A.8), and the transfer targets are small (AlexNet, VGG11, ResNet18 on CIFAR-10 only). Nothing indicates how the method behaves with ResNet or ViT experts, or with larger images at low IPC, which is where distilled data would be used for architecture search or continual-learning replay buffers. Robustness of the distilled data (corruptions, label noise) is untested.
- **Suggested Fix:** one experiment with a ResNet-18 expert on CIFAR-100 and one corruption benchmark (CIFAR-10-C style).
### W4: Limited discussion of limitations and impact
Section 6 states future directions but no limitations of the method; there is no discussion of cost of generating expert trajectories or of misuse (negligible here, but the privacy claims in the introduction are not revisited).
- **Suggested Fix:** a short limitations paragraph (truncation sensitivity, ConvNet scope, hyperparameter sensitivity).

## Cross-disciplinary connections (suggestions)
- Implicit differentiation and Neumann-series hypergradients (as used in meta-learning) as an alternative to unrolling; the authors name implicit gradients as future work.
- Randomised smoothing and Gaussian-homotopy ideas for the data-side noise (Duchi et al., cited): analyse the smoothing as a stochastic relaxation with a tunable γ.
- Adversarial training and robust optimisation: the ascent step on ϕ is a data-side worst-case perturbation, so robustness results from that literature may transfer.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid experiments overall; theory loose. |
| Clarity | 3 | Understandable. |
| Significance | 3 | Useful for practitioners with limited memory. |
| Originality | 2 | Natural combination; moderate novelty. |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: broad evaluation axes and a real memory saving, outweighing the untested flatness premise for me; I weight potential impact more than the others do.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasonable construction; theory loose. |
| Clarity & Presentation | 60 | Competent | Clear enough. |
| Novelty & Originality | 60 | Competent | New transfer of an idea; incremental pieces. |
| Significance & Impact | 62 | Competent | Practical value for low-memory users. |
| Experimental Validation | 58 | Competent | Breadth good; attribution weak. |
| Reproducibility | 56 | Competent | Missing values; code promised. |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations thin. |

## Questions for Authors
1. Do networks trained on SATM sets sit in flatter weight-space regions than those trained on MTT sets? (A yes would strengthen my score; a no would not change it much but would change the framing.)
2. How accurate is truncated hypergradient vs full, measured? 
3. Does the method hold with a ResNet expert?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**: public image benchmarks, no human-subject data or misuse pathway.

## Overall Score
**4 (Borderline Accept)**: an interesting, useful bridge with real transfer gains; the weaknesses are of the kind common in accepted papers, though the causal story needs testing.

## Confidence
**3**: fairly confident; optimisation background is strong, dataset-condensation benchmarks less so.

---

# Peer Review Report

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Reviewer: Dr. Sunniva Halvorsen, Reviewer 4 (Generalist) (ML group, public university, Nordic Europe; fictional persona)
## Expertise: deep learning; data-efficient training
## Date: 2026-11-10

## Summary
The paper proposes SATM, a way to make synthetic datasets from trajectory matching generalise better by minimising sharpness of the outer-loop objective, and to do so without doubling the training cost. In my words: condensed data is only useful if it works for other networks and tasks, so the authors steer the data toward flat regions of the matching loss and test transfer across architectures and in continual learning. The reported gains are mostly modest, with larger ones in cross-architecture transfer at IPC 50.

## Strengths
### S1: A clear, relevant problem
The motivation in Section 1 (generalisation of condensed data; cost of unrolling) is easy to follow, and the proposed fix is simple to state.
### S2: Breadth of evaluation
In-domain (Tables 2–3), cross-architecture (Table 5), continual (Fig. 1) and cost (Table 6) results make the paper more than a leaderboard entry.
### S3: Plug-in flexibility
Appendices A.6–A.7 show that the approach composes with flat experts (FTD-style) and with other SAM variants.
### S4: Appendix content
The pseudocode (A.3), hyperparameter table (A.9) and proofs (A.1, A.2) make the contribution inspectable.

## Venue Criteria Checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness (claims supported) | Partly | Tables 2–6; no component ablation; theory loose |
| Presentation | Partly | Notation (ι, τ, κ), caption/text mismatches |
| Contribution (new idea or finding) | Partly | SAM-on-data is new for TM; pieces are known |
| Evidence breadth | Met | Sections 5.1–5.2 |
| Reproducibility information | Partly | Table 11 incomplete; ρ, γ missing; code promised |
| Honest limitations | Not met | Section 6 lists no limitations of the method |

## Weaknesses
### W1: The strength of the claims exceeds the margins (C4)
The claims "almost all the settings of the standard dataset condensation" and "Still, there are clear improvement margins over" competitors read stronger than Table 2 supports: 7 of 9 margins over the best baseline are 0.5 points or less, one is negative (CIFAR-100 IPC 10: 43.1 vs FTD 43.4), and stds are 0.2–0.8. A reader will come away expecting a bigger effect than the tables show.
- **Suggested Fix:** soften the wording and lead with the cross-architecture results, where the gain is clearest.
### W2: It is hard to tell what the contribution is, because components are bundled
Four changes are introduced together (SAM step, smoothing, TUH/TR, Eq. 10) and evaluated only as a package, so the reader cannot tell which matters (Section 4, Tables 2–6). This also makes the "efficient" claim hard to read: Table 6 compares with MTT and TESLA but not with the obvious "MTT + SAM".
- **Suggested Fix:** one ablation table and one extra row in Table 6.
### W3: Presentation of the method
Notation drifts: τ is a step index in Section 4.2 but Algorithm 1 uses θ_{t+κ} (κ is never defined) and loops "for i ← N − τ to N", while Table 1 charges cτ time; ι is "truncated steps" in the text of Eq. 8 though the sum runs from ι. Eq. 3 and the noise definition (N(0, γ‖ϕⱼ‖₂) in Section 4.1 vs N(0, γ‖ϕⱼ‖₂² I) in Algorithm 1) differ. These make the method hard to re-implement from the paper.
- **Suggested Fix:** one consistent notation table; align Algorithm 1 with Table 1 and the text.
### W4: Limitations are missing
Section 6 states future work but no limitations (truncation sensitivity in Table 8; ConvNet-only experts).
- **Suggested Fix:** add a limitations paragraph.
**Minor:** typos ("ImageWoor", "ImageNeow", "syntactic", "Vanilla MMT", "THU" for TUH, "Table A.7" for Table 10, "forage", "Shaprness"); Table 2 caption says MMT for MTT.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence supports a modest claim only. |
| Clarity | 2 | Notation inconsistencies. |
| Significance | 3 | Relevant problem. |
| Originality | 2 | Natural but incremental combination. |

## Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a relevant problem and broad evaluation, held back by overstated margins and unclear attribution.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Reasonable, but proofs and cost claims have gaps. |
| Clarity & Presentation | 52 | Developing | Method notation inconsistent; typos. |
| Novelty & Originality | 52 | Developing | Incremental combination. |
| Significance & Impact | 56 | Competent | Relevant, modest. |
| Experimental Validation | 54 | Developing | Broad but unattributed. |
| Reproducibility | 50 | Developing | Missing values. |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations missing. |

## Questions for Authors
1. Which of the four components gives most of the improvement? (A clean ablation would raise my score.)
2. Can you restate Algorithm 1 with the same τ, ι as in Table 1? 
3. What is the practical recommendation for ρ and γ?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: a relevant idea with broad but modestly convincing evidence; this paper is typical of submissions that fall just short, and the changes needed (ablation, honest wording, clearer method) are substantial but doable.

## Confidence
**3**: fairly confident; not a dataset-distillation specialist.

---

# Devil's Advocate Report

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Reviewer: Prof. Bernard Achterberg, Devil's Advocate (statistical learning and evaluation methodology, Western Europe; fictional persona)

## Steelman
SATM makes a sound observation: the outer loop of trajectory matching is a rough landscape over the synthetic pixels, and sharpness-aware updates plus cheaper hypergradient estimation can improve transfer at low cost. The cross-architecture results at IPC 50 (Table 5) and the ImageNet-1K gain over TESLA (Table 4) are consistent with this story, and the paper reports honestly how truncation degrades accuracy (Table 8).

## Core Argument Chain
1. The outer-loop landscape in the synthetic data ϕ is sharp, which limits generalisation (Section 1).
2. Minimising sharpness in ϕ (Eq. 5) yields a flatter solution (Fig. 2).
3. A flatter ϕ gives a dataset that generalises across architectures and tasks (Tables 2, 5, Fig. 1).
4. TUH and TR keep the cost low while the approximation error is bounded (Section 4.2, Thm 4.2, Prop 4.1).
∴ SATM improves generalisation of condensed datasets efficiently and with provable guarantees.

## Strongest Counter-Argument
The paper's causal story has a missing link at each end. At the start, premise 3 asks the reader to accept that flatness *in the synthetic pixels* is what helps a different network that is trained on those pixels. SAM's justification concerns flatness in the weights of the network being trained, and nothing in the paper connects the two: there is no weight-space sharpness measurement of the downstream networks, and the only "sharpness" evidence (Fig. 2) is hypergradient norm, which is a gradient size rather than curvature, and which could shrink for many reasons. The paper's own Table 10 shows that the generic SAM family, with the smoothing removed, recovers most of the improvement over MTT (+1.4 of +1.8 on CIFAR-100 1 IPC, +1.8 of +3.1 on Tiny-ImageNet 3 IPC, derived), so what remains for the "tailored" parts is a margin of 0.2–0.5 points that is inside the reported stds (0.2–0.4). At the other end, premise 4 relies on bounds that cannot be informative: Theorem 4.2's bound is nonzero at ε = 0 and linear in τ, Proposition 4.1's proof stops before the stated factor, and Eq. 10 has no bound at all although Section 1 promises "rigorous theoretical support by bounding the errors of". Meanwhile Table 8 shows that when the retained fraction drops to 1/6 the CIFAR-100 50 IPC accuracy falls from 50.9 to 23.4, which means the "limited error in practice" depends on a hyperparameter the paper does not say how it chose. The simplest alternative explanation for every positive result is that adding any regulariser or noise on ϕ, together with a different learned inner step size, helps a little on these small benchmarks. The paper has no experiment that could distinguish that explanation from the flatness story. The authors must show an attribution ablation and a direct flatness measurement, or narrow the claim to "an empirically useful, cheaper SAM-style regulariser for trajectory matching".

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim, that SATM gives modest improvements at lower memory than MTT, is supported in weaker form by Tables 2, 5 and 6, so every issue below is fixable by narrowing claims or adding experiments on existing setups, which makes them MAJOR, not fatal.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | Section 4.1, Fig. 2, Table 10 | Data-space flatness → generalisation is untested; generic SAM recovers most of the gain (evidence supports a weaker claim, not a contradicted one) | Weight-space sharpness of student nets; ablation of smoothing alone |
| DA-M2 | Evidence | Table 2, 3, 4; Section 5.1 | Margins mostly within one std; "almost all", "clear improvement margins", "noticeable" overstate (E5) | State ±; independent distillations; paired CI; rewrite wording |
| DA-M3 | Logic | Section 4.2, Table 1, Section 5.2, Table 6 | "constant memory" vs O(P(N−ι)); "less time than MTT" vs O(cN+cτ) and a 0.5 s (≈1%) ImageNet-1K gap | Reconcile the cost model; add "MTT + SAM" row |
| DA-M4 | Evidence | Thm 4.2, Prop 4.1, Eq. 10, Section 1 | Theory does not deliver "rigorous... bounding the errors" for all approximations | Measure errors; drop "rigorous"; complete proofs |
| DA-M5 | Integrity of protocol | Table 8, Table 2, Appendix A.7 | Choice of ι, ρ, γ and the baselines' tuning with no stated split; Table 8's CIFAR-100 50 IPC best value equals the Table 2 entry. Selection statement absent after the protocol sweep (criterion-3 table: "not stated" → MAJOR) | State the split; held-out check |
| DA-M6 | Scope | Section 1 (statement that most existing methods fail to condense ImageNet-1K), Section 2.1 | Overclaim given RDED cited but not compared; DATM absent from Tables 2–3 | Qualify scope; add comparisons |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 5 vs Table 2/9 | SATM 74.2 vs 73.9; MTT 64.3 vs 65.4 (same configurations) |
| DA-m2 | Claim | Appendix A.6 | "clear improvements in SATM-FI compared to both standard SATM" while SATM-FI is below SATM on CIFAR-10 IPC 1 (48.7 vs 49.0); other gains 0.2–0.8 |
| DA-m3 | Reporting | Fig. 1 | Text claims "SATM consistently outperforms other methods"; no numbers (figure unavailable to me) |
| DA-m4 | Consistency | Fig. 2 caption vs Section 5.2 | CIFAR-100 10 IPC vs 3 IPC |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| "almost all the settings of the standard dataset condensation" (Table 2) | best in 9 cells | best in 8 of 9; CIFAR-100 IPC 10: 43.1 < FTD 43.4; mean margin +0.38 | Partly |
| ImageNet-1K gain over TESLA (Table 4) | 8.9 vs 7.7; 19.2 vs 17.8; 29.2 vs 27.9 | +1.2, +1.4, +1.3; stds 0.2–1.3 | Yes, but within about one std at IPC 10/50 |
| Runtime vs TESLA (Table 6, ImageNet-1K) | 45.4 vs 47.4 | −4.2% (±0.4/0.7) | Yes, small |
| Memory vs TESLA (Table 6, CIFAR-100) | 5.7 vs 3.6 | +58% | Not "comparable" |
| SATM-FI vs SATM (Table 9) | "clear improvements" | −0.3, +0.8, +0.3, +0.5, +0.8, +0.5, +0.8, +0.2 | Partly |
| Table 5 SATM 50 IPC ConvNet | 74.2 | Table 2: 73.9 | No |

## Ignored Alternative Explanations
- Any noise or regulariser on ϕ plus a different learned step size could give the same small gain; not controlled.
- Gains at IPC 50 on AlexNet and VGG11 could come from the first-order learning-rate rule or from mini-batched outer loops (Appendix A.5) rather than flatness.
- Hyperparameters tuned per cell on the reported split (not stated) favour the method that has the extra knobs ρ, γ, ι, τ.
- Random-seed variation of the distillation itself is not separated from evaluation variance.

## Missing Stakeholder Perspectives
Practitioners with larger backbones or higher resolutions are not represented, since all experts are small ConvNets. Users of condensed data for privacy are mentioned in Section 1 without evidence.

## Observations (Non-Defects)
Table 8 honestly exposes the truncation sensitivity. The compatibility study (Table 10) is repeated five times, which most tables in the paper are not. The memory saving over MTT is real and well measured.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Proof gaps; unmeasured approximation errors |
| Clarity & Presentation | 50 | Readable; inconsistent notation |
| Novelty & Originality | 46 | Incremental; attribution unproven |
| Significance & Impact | 46 | Margins within noise on mature benchmarks |
| Experimental Validation | 44 | No attribution ablation; ± undefined |
| Reproducibility | 42 | Missing ρ, γ, ι, τ, ImageNet settings |
| Ethical Compliance | 60 | Nothing at stake |

**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the paper's own Table 10 and the margin analysis weaken the central claim and nothing tests the flatness mechanism.

## Overall: 2 | Confidence: 4

---

# Phase 1.5 / 1.6: Literature Check Status and Report Check

**Literature check:** requested `strict` (cutoff 2025-09-24). The fingerprint was written; two `search` calls (claim queries, 2 of the 12 allowed) timed out with no results, so the check was recorded as skipped. No labels, scout table or similarity output exist. Missing references are from knowledge, with `[verify]` where unsure. No reference was treated as a required comparison.

**Report check (Synthesizer, Step 0).**

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 theory (first draft listed "Theorem 4.2 is wrong") | Rewritten | The bound is valid if gradients are bounded; the defect is smoothness vs boundedness and looseness. Moved to Medium confidence in the Error Log. |
| R1 | Table 6 identical ImageNet-1K memory | Moved to Questions | Low confidence: possibly per-GPU measurement (Error-audit precision rule) |
| R2 | "paper does not compare to DATM" | Rewritten | Table 7 does compare, in the SATM-DA variant; restated as "absent from Tables 2–3, partial in Table 7" |
| R3 | Fig. 2 shows only SATM sharpness | Kept, flagged | Figure-dependent; based on caption and text only |
| R4 | Typos and Table 2 caption "MMT" | Moved to Minor | Cosmetic |
| DA | "SATM numbers in Table 4 use soft labels" | Dropped | Text says "without relying on soft-label fitting tricks"; remains a question for TESLA's provenance (R1 Q5) |
| DA | Selection on test split (candidate DA-C) | Kept as MAJOR | No selection statement found after the protocol sweep; criterion-3 table row "not stated" |

---

# Phase 2: EIC Meta-Review and Decision

*Synthesizer part A: master issue list.*

| Issue | Sources | Class | Hinges on outcome? |
|-------|---------|-------|--------------------|
| No isolating ablation; attribution to flatness untested | R1-W1, R2-W3, R3-W1, R4-W2, DA-M1 | CONSENSUS-4/5 | Yes |
| Gains within noise; claim wording overstated; "±" undefined | R1-W2, R4-W1, DA-M2 | CONSENSUS-3 | Yes |
| Cost claims inconsistent ("constant memory", vs-MTT runtime) | R1-W4/ERR-4, DA-M3, R4-W3 | CONSENSUS-3 | Medium |
| Theory loose / does not support "rigorous" claim | R1-W5/ERR-2/3, R3-W2, DA-M4 | CONSENSUS-3 | Medium |
| Hyperparameter/selection protocol not stated; ρ, γ, ι, τ missing | R1-W3/W6, DA-M5, R4 (Q3) | CONSENSUS-3 | Medium |
| Comparison set excludes DATM/RDED; ImageNet overclaim | R2-W2, DA-M6 | CONSENSUS-2 | Medium |
| Incomplete novelty positioning (Shaban, implicit gradients) | R2-W1 | SOLO | No |
| Table 5 vs Table 2 inconsistencies | R1-ERR-1, DA-m1 | CONSENSUS-2 | No |
| Scale/robustness (ConvNet-only) | R3-W3 | SOLO | No |
| Notation inconsistencies | R4-W3 | SOLO | No |

DA-CRITICAL issues: none raised. Official ratings: R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00; official composite 52.6 (before.json: 52.6; suggested Overall 3).

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** a natural, simple idea (SAM on the synthetic data in a bilevel loop) with a real memory saving over MTT (Table 6) and the best accuracy in 8 of 9 cells of Table 2, with notable cross-architecture transfer at IPC 50 (Table 5: +3.1 AlexNet, +5.1 VGG11 over FTD). The evaluation covers several axes.
- **Against acceptance:** the central causal claim (flatness in data space) is never tested, and the paper's own Table 10 shows generic SAM giving most of the gain; margins are mostly within one std and the wording overstates them; the efficiency and theory claims have internal inconsistencies; reproducibility and selection details are missing; the comparison set leaves out the strongest trajectory-matching baseline (DATM) in the main tables.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Margins in Table 2 mostly ≤ 0.5, one negative | R1-W2, R4-W1, DA-M2 | Table 2 | Verified | Recomputed: mean +0.38; CIFAR-100 IPC 10 is −0.3 vs FTD |
| No ablation separating smoothing, TUH/TR, Eq. 10 | R1-W1, DA-M1 | Section 4, Tables 2–10 | Verified | Only Table 10 (smoothing removed for competitors) and Table 8 (truncation) |
| SAM alone recovers most of SATM's gain over MTT | DA counter-argument, R1-W1 | Table 10 | Verified | 25.7 vs 24.3 vs 26.1 (CIFAR-100, 1 IPC); 12.3 vs 10.5 vs 13.6 (Tiny, 3 IPC). Whether SATM in Table 10 includes TUH/TR is not stated. |
| "constant memory" contradicts Table 1 | R1-ERR-4, DA-M3 | Section 4.2, Table 1, Section 5.2 | Verified | Memory O(P(N−ι)) with one-third retained |
| SATM faster than MTT | R1-W4, DA-M3 | Table 6, Table 1 | Overstated (by the paper) | Gap 0.5 s on ImageNet-1K, inside stds; Table 1 says O(cN+cτ) |
| Theorem 4.2 / Prop 4.1 proof defects | R1-ERR-2/3, R3-W2, DA-M4 | Appendix A.1, A.2 | Partly correct | Constant 2σ vs σ-smooth and Prop 4.1's missing step verified; the bound is valid under a bounded-gradient reading, so "wrong" is too strong; loose either way |
| Eq. 10 has no bound despite Section 1 | R1-W5, DA-M4 | Section 1, A.4 | Verified | A.4 treats the inner gradient as constant in α |
| Table 5 vs Table 2/9 numbers | R1-ERR-1, DA-m1 | Tables 5, 2, 9 | Verified | 74.2 vs 73.9; 64.3 vs 65.4 |
| No stated selection split / ρ, γ values | R1-W3, DA-M5 | whole text, Table 11 | Verified | Selection-statement search found none; no criterion-3 row beyond "not stated" |
| DATM absent from Tables 2–3 | R2-W2, DA-M6 | Tables 2, 3, 7 | Partly correct | Present in Table 7 only, via SATM-DA, where SATM-DA is below DATM on Tiny IPC 1 |
| SATM-FI "clear improvements" | DA-m2 | Appendix A.6, Table 9 | Verified | 48.7 vs 49.0 at CIFAR-10 IPC 1 |
| Fig. 2 shows sharpness for SATM only | R3-W1 | Figure 2 | Partly correct | From the caption and text only; figure unavailable |
| Table 6 identical memory 26.6 on ImageNet-1K | R1-Q4 | Table 6 | Verified (numbers); interpretation open | Remains a question |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Errors and recomputed margins verified; one proof point overstated in the draft but corrected in the log; well calibrated |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; DATM point partly correct; novelty statements from memory, flagged |
| R3 (Perspective) | 4 | 3 | 1.0 | Role-appropriate generosity; its points verified; rating does not account for the missing ablation and noise-level margins, but I do not move the weight for being positive |
| R4 (Generalist) | 3 | 3 | 1.0 | Verified points, balanced |
| DA | 2 | 4 | 0.75 | Arguments mostly survived, but Overall 2 and 44-level scores are harsher than its own "no CRITICAL, fixable by narrowing claims" text supports |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | n/a | n/a |

The DA's strongest objection (untested flatness mechanism) was checked against the paper. It is MAJOR: the results support a weaker claim (a useful, cheaper SAM-style regulariser for trajectory matching), they do not contradict the main claim, and no leakage or selection statement was found. The selection-protocol point is MAJOR ("not stated").

### Final Decision and Justification
The EIC-weighted rating is 3.02, so the starting point is 3 (Borderline Reject); the composite cross-check, 52.4, agrees (band 3), and there is no DA ceiling. I do not depart from the starting point. Pool position (EIC): better than about 48% of ICLR submissions. A typical accepted paper here has an idea or finding the field lacked, with evidence across settings and fair baselines; this paper has a combination of known parts, margins that are mostly inside the noise, and no experiment that identifies why it works, which are signals of a typical rejected submission. Against that, the cross-architecture gains at IPC 50 and the memory saving are real, and the problems are fixable (ablation, wording, protocol statement, cost-model fix) without new ideas, which is why this is not a 2. R3's 4 rests on potential impact and the breadth of axes; I weigh the verified attribution gap and the overstated wording more heavily. The final decision is 3, within the ceiling (none).

---

## Editorial Decision

## Paper: Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Ingrid Valdemar; R1 Dr. Tomasz Reyes-Anand (Methodology), R2 Dr. Farah Nasrallah-Ortega (Domain), R3 Dr. Mateus Brandão-Ito (Perspective), R4 Dr. Sunniva Halvorsen (Generalist), DA Prof. Bernard Achterberg

**Decision: Borderline Reject (3)** (ICLR rating 4 on {0, 2, 4, 6, 8, 10}; 5 on {1, 3, 5, 6, 8, 10}, scale status *secondary*). This is how a careful panel would likely see this draft, not a prediction.

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 52.6
**EIC assessment** (internal): weighted rating 3.02 → starting point 3 · weighted composite 52.4 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3

### Score Summary: official scores and EIC assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 48 | 55 | 60 | 54 | 44 | 52.2 | 52.1 | 16 |
| Clarity & Presentation | 55 | 55 | 60 | 52 | 50 | 54.4 | 54.5 | 10 |
| Novelty & Originality | 50 | 48 | 60 | 52 | 46 | 51.2 | 51.1 | 14 |
| Significance & Impact | 50 | 52 | 62 | 56 | 46 | 53.2 | 53.0 | 16 |
| Experimental Validation | 45 | 52 | 58 | 54 | 44 | 50.6 | 50.2 | 14 |
| Reproducibility | 42 | 50 | 56 | 50 | 42 | 48.0 | 47.6 | 14 |
| Ethical Compliance | 62 | 62 | 62 | 62 | 60 | 61.6 | 61.7 | 2 |
| **Composite** | 49.5 | 53.1 | 59.7 | 54.2 | 46.6 | **52.6** | **52.4** | |
| Pool position (P%) | 44 | 50 | 66 | 54 | 38 | | | |

No dimension has a spread above 20, and the script raised no warnings. Pool positions run from 38 to 66 (28 points, below the 30-point trigger).

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Enhancing Generalization via Sharpness-Aware Trajectory Matching for Dataset Condensation" to ICLR. Making condensed datasets transfer across architectures at modest cost is a worthwhile aim.

**Overall Assessment:** The reviewers saw a natural and simple idea with a real memory saving over MTT and clear cross-architecture gains at IPC 50. They were not convinced that the evidence identifies why it works, and the in-domain margins are small relative to the reported variation.

**Key Strengths Identified by Reviewers:**
1. Broad set of evaluation axes: in-domain, cross-architecture, continual learning, cost (R1, R3, R4).
2. Measured memory saving over MTT at similar runtime; honest truncation sweep (R1, R3, DA).
3. Cross-architecture transfer at IPC 50, +3.1 and +5.1 points over FTD on AlexNet and VGG11 (R2, R3).

**Key Concerns Requiring Attention:**
1. No ablation isolates the SAM step, the smoothing, TUH/TR or the learning-rate rule; Table 10 suggests generic SAM accounts for much of the gain (CONSENSUS-4/5).
2. Margins in Tables 2–4 are mostly within one std and the text overstates them; what "±" covers is not stated (CONSENSUS-3).
3. Cost and theory claims are inconsistent: "constant memory" vs O(P(N−ι)); bounds that are loose and an Eq. 10 without a bound (CONSENSUS-3).
4. Hyperparameter selection split and key values (ρ, γ, ι, τ) are not stated (CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** none was rated CRITICAL. The strongest objection, that data-space flatness is assumed and not shown to cause the gains, was ruled MAJOR; it must be addressed with an attribution ablation or a narrowed claim.

**Decision: Borderline Reject (3).** The remaining issues can be fixed without a new method: an attribution ablation, honest wording of the margins, a consistent cost model, and a stated protocol. If these were done and the gains held across independent distillations, the paper would move toward the accept side.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Valdemar
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Attribution/ablation missing; flatness link untested | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Margins within noise; wording overstated | R1, R4, DA | CONSENSUS-3 |
| Cost-claim inconsistencies | R1, R4, DA | CONSENSUS-3 |
| Theory loose / overclaimed | R1, R3, DA | CONSENSUS-3 |
| Protocol and hyperparameters not stated | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the paper clears the ICLR bar | R3 (4) | R1, R2, R4 (3), DA (2) | R3 rates potential and breadth; the verified attribution gap and noise-level margins weigh more. Decision 3. |
| Severity of the theory gaps | R1, DA (MAJOR) | R3 (constructive suggestion) | Partly correct: the proof gaps are real but the experiments do not depend on the bounds; MAJOR, not decisive. |

### Score Spread Discussion
No dimension has spread above 20 (largest 16). R3 is the high outlier on every dimension (≈ +6 to +10 over the mean) and the DA the low one; the EIC weights follow verification quality, not position.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Flatness mechanism untested; generic SAM recovers most gain | Yes (R1, R2, R3, R4) | n/a | n/a |
| DA-M5 | MAJOR | Selection split not stated | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No DA-CRITICAL issue was upheld. These are the issues the EIC verified as undermining the main claim as worded.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | No attribution of the gain to flatness; generic SAM gives most of it | R1-W1, R2-W3, R3-W1, R4-W2, DA-M1 | Section 4, Table 10 | Ablate smoothing, TUH/TR, Eq. 10, "MTT + vanilla SAM" on CIFAR-100 IPC 10 and Tiny IPC 1; add a weight-space sharpness comparison | High; ≈ 60–100 GPU-h | Partly |
| P1-2 | Margins within noise; "±" undefined; claims overstated | R1-W2, R4-W1, DA-M2 | Tables 2–4, Section 5.1 | State what ± covers; ≥3 independent distillations on headline cells; paired CIs; reword "almost all", "clear", "noticeable" | Medium; ≈ 30–50 GPU-h | Yes (wording) / Partly (runs) |
| P1-3 | Protocol and hyperparameters unstated | R1-W3/W6, DA-M5 | Table 11, Appendix A.7/A.9 | Report ρ, γ, ι, τ and ImageNet settings; state the tuning split; add a held-out check | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Cost claims inconsistent ("constant memory", faster than MTT) | R1-W4/ERR-4, DA-M3 | Reconcile with Table 1; add an "MTT + SAM" row to Table 6; define the cost model | Low–Medium | Yes |
| S2 | Theory loose; Eq. 10 unbounded; "rigorous" overclaimed | R1-W5/ERR-2/3, R3-W2, DA-M4 | Complete Prop 4.1's proof; fix the σ-smooth/bounded-gradient step; measure the discrepancies; reword | Medium | Yes |
| S3 | Comparison set: DATM in Tables 2–3, ImageNet-1K scope vs RDED | R2-W2, DA-M6 | Add DATM (mark soft labels); complete Table 7 with CIFAR-10; qualify the ImageNet claim | Medium | Partly |
| S4 | Table 5 vs Table 2/9 inconsistencies | R1-ERR-1, DA-m1 | Reconcile or explain | Low | Yes |
| S5 | Missing references and novelty delta (truncated backprop for bilevel optimisation, implicit-gradient condensation, ImageNet-scale methods) | R2-W1 | Cite and differentiate; claim the combination | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | ConvNet-only experts; no robustness test | R3-W3 | ResNet expert; corruption benchmark |
| N2 | Notation (ι, τ, κ), Eq. 3, noise definition | R4-W3 | One notation table; align Algorithm 1 with Table 1 |
| N3 | Limitations paragraph | R3-W4, R4-W4 | Add (truncation sensitivity, scope) |
| N4 | Typos and caption mismatches | R4, R1-ERR-5 | Fix |
| N5 | SATM-FI wording; Fig. 1 numbers | DA-m2, DA-m3 | Reword; add a table of numbers |

## Estimated Revision Effort
- Priority 1: 3 items, ≈ 1–2 weeks including ≈ 100–150 GPU-hours.
- Priority 2: 5 items, ≈ 1 week.
- Priority 3: 5 items, ≈ 2 days.
- **Total estimated revision time**: about 3 weeks.
