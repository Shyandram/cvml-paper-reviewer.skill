# Academic Paper Review: SAFA-SNN (full mode, target venue ICLR, literature check: strict, cutoff 2025-09-24)

Date: 2026-11-05. This is a simulation of how a careful panel would likely see this draft, not a prediction. The five reviewer passes were run one after another in a single model context (no subagents), so they are role-based passes, not independent agents. Figures were not available: figure-dependent claims are judged from captions and extracted text only, and E9 (figure integrity) was not checked.

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network |
| Primary Discipline | Machine learning → continual / few-shot class-incremental learning |
| Secondary Discipline(s) | Neuromorphic computing / spiking neural networks; edge computing |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | LIF spiking networks; firing-rate-aligned dynamic thresholds with a channel mask; zeroth-order (stochastic-perturbation) gradient estimate for the spike function; prototype classifier with projection onto the base-class subspace |
| Target Venue | ICLR (top-tier ML conference), stated by user; profile key `iclr` |
| Venue-Specific Notes | None (no contribution-type declaration). ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence |
| Paper Maturity | Submission-ready in form, with unfinished consistency of appendix tables |
| Ethics-Relevant Content | None directly (public benchmark datasets). The introduction mentions "intelligent surveillance systems" as a motivating example only |

### Claimed Contributions (as stated by the authors, §1)
- **C1** (practical problem + first SNN solution): emphasise on-device FSCIL and give "the first SNN-based solution towards general on-device FSCIL" (§1, contribution bullets 1–2).
- **C2** (method): sparsity-aware neuronal dynamics (channel-masked firing-rate-aligned thresholds, §5.3, Eq. 6–7), zeroth-order optimization within neuronal dynamics (§5.4, Eq. 8–12), and prototype subspace projection (§5.5, Eq. 14–15).
- **C3** (evidence): state-of-the-art accuracy on five datasets and several SNN backbones, with sparsity advantages and about 20% lower measured energy on a Jetson Orin AGX (Abstract, §6.2, Fig. 4–5).

### Paper memory (factual record, shared with reviewers)
- **Setup facts.** Datasets: CIFAR-100, Mini-ImageNet (eight 5-way 5-shot tasks, §6.1; base-class count not stated); CIFAR-10-DVS (four 1-way 1-shot), DVS128gesture (five 1-way 1-shot), N-Caltech101 (eight 5-way 5-shot) (§6.1). Backbones: Spiking VGG 5/9/11, ResNet 18/19/20, Spikingformer (§6.1, A.6). Optimizer Adam, 300 epochs (CIFAR-100, Mini-ImageNet), 100 epochs (neuromorphic), batch 128, learning rate/β/θ/S/δ = 0.001/1.2/0.001/5/0.5, three seeds (§6.1). Train/validation/test split and tuning split: no validation split is mentioned; hyper-parameter sweeps report test-session accuracy (A.11, Fig. 8, Table 14). η, γ, λ, α defaults: not stated after search. Code: "in the codes" (A.6), no link visible. Baseline training protocol (official code vs reimplementation, loss, epochs): not stated after search. Compute: Jetson AGX Orin (§6.1), training energy from "power (W) by time" (§6.2).
- **Headline numbers:** +4.01 last-session and +6.07 average over the second best on Mini-ImageNet (Table 1, §6.2); "20% lower energy" (Abstract; Fig. 4); "accuracy of 31.06%" for Table 3 (§6.2).
- **Appendix adds:** convergence assumptions and proof sketch (A.1–A.3), error-type analysis (Table 4–5, A.4), extra backbones (Tables 6–12), baselines description (A.7), theoretical inference energy (A.9, Table 13), shots, hyper-parameter, time-step and sparsity analyses (A.10–A.13, Fig. 8–11, Table 14), firing-rate plots (A.14).
- **Unverifiable:** all figures (Fig. 1–12); Fig. 4–5 bar labels are read from garbled extracted text. Equations were read from extracted text; the layout of Eq. 14 was not checked on the page image.

### Integrity signals (EIC only)
`integrity_scan.py` found only six soft-hyphen characters (typesetting artifacts). No text addressed to reviewers or AI systems. The reviewer copy was written (redacted copy identical in substance).

### Literature check (strict, cutoff 2025-09-24)
Fingerprint written; 8 of 12 queries used (claim ×5, baseline ×1, expansion ×2), 46 unique kept results. The arXiv search finds little SNN-FSCIL work (the SNN-FSCIL queries returned 0–1 results), so "no close prior work found" for the C1 *combination* is a limit of the search, not evidence of novelty. `similarity`: closest prior works are ALADE-SNN (cosine 0.164), compressed latent replays for SNNs (0.148) and DSD-SNN (0.146), all below the 0.30 overlap flag; the only shared 8-grams (with an SNN conversion paper) are the stock phrase "to the best of our knowledge this is the first", not copied content. `scout` for CIFAR-100 returned SNN papers without comparable FSCIL numbers (no under-reported-baseline check possible). `novelty` was handled by hand in the Domain addendum. Gaps left open: no arXiv hit for ANN-FSCIL reference numbers under matched backbones.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Anselm Varga, large public research university (Central Europe)
- **Seniority / Expertise**: senior faculty / continual learning, few-shot learning, evaluation protocols
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR accepts; moves weights only for verified reasons.

### Reviewer 1 (Methodology): Dr. Tomasz Brzezicki, industrial research lab (Europe)
- **Seniority / Expertise**: senior industry scientist / SNN training and surrogate gradients; FSCIL evaluation protocols
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table average; insists on matched training budgets.

### Reviewer 2 (Domain): Prof. Adaeze Nwosu-Hart, vision and learning group, public university (North America)
- **Seniority / Expertise**: associate professor / class-incremental and few-shot incremental learning; prototype methods
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work closely; asks what is new relative to the closest prior method.

### Reviewer 3 (Perspective): Dr. Ilan Peretz-Vasquez, embedded-systems and neuromorphic hardware lab (South America)
- **Seniority / Expertise**: mid-career researcher / edge deployment, event-based sensing, energy modeling
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what happens on real hardware.

### Reviewer 4 (Generalist): Dr. Sunita Raghavan-Moore, ML group, research university (South Asia)
- **Seniority / Expertise**: postdoc / deep learning for vision, generalist PC member
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Judges whether the story and the evidence line up for a non-specialist.

### Devil's Advocate: Dr. Keiko Maldonado-Reyes, evaluation-methodology group (East Asia)
- **Seniority / Expertise**: mid-career / causal attribution of gains, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Steelmans first; rigorous, never hostile.

*Personas are fictional. Proceeding with the stated assumptions (target venue ICLR as given by the user).*

---

# Phase 1: Independent Reviews

## Reviewer 1 (Methodology)

# Peer Review Report

## Paper: SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network
## Reviewer: Dr. Tomasz Brzezicki, Methodology Reviewer (industrial research lab, Europe; fictional persona)
## Expertise: SNN training and surrogate gradients; FSCIL evaluation
## Date: 2026-11-05

## Summary
The paper builds an SNN-based few-shot class-incremental learner meant to run on an edge device. During base training it uses a temporal-efficient-training plus MSE loss (Eq. 13) and a zeroth-order estimate of the spike derivative (Eq. 9–10). During incremental sessions the backbone is frozen, per-channel thresholds are nudged so that firing rates match the base session (Eq. 6–7), and new-class prototypes are mixed with their projection onto the base-prototype subspace (Eq. 14–15). It reports gains over SNN-converted FSCIL baselines on CIFAR-100, Mini-ImageNet and three event-camera datasets, plus a Jetson energy/time comparison.

## Strengths
### S1: Broad evaluation surface
Five datasets (§6.1), seven backbones including Spikingformer (A.6, Tables 6–12), three seeds with ± (§6.1), and 9–10 FSCIL baselines in Table 1/6. Extending FSCIL to event data (Table 2) is useful.
### S2: Useful diagnostic analysis
Table 4–5 split performance into seen/unseen and base/novel errors, which is more informative than average accuracy alone; the shot sweep (Fig. 7, A.10) and time-step study (A.12, Fig. 9) are reasonable extras.
### S3: Measured on-device cost is attempted
Energy and time are measured on a Jetson device (§6.2, Fig. 4–5), not only counted in FLOPs, and the authors also give the theoretical computation (A.9).

## Weaknesses
### W1: Appendix and main-table numbers are internally inconsistent (see Error Log ERR-1 to ERR-6)
Averages do not match their rows (Table 6: SAFA-SNN printed 56.59, recomputed 59.91; TEEN printed 59.34, recomputed 54.45; Tables 7, 9 and 10 also differ). Identical numeric rows appear in different settings: the SAFA-SNN rows of Table 7 (VGG-11) and Table 8 (ResNet-20) are identical; the SAFA-SNN row of Table 6 (CIFAR-100, VGG-9) equals Table 12 (Mini-ImageNet, ResNet-18); the SAVC row of Table 1 (Mini-ImageNet) equals Table 6 (CIFAR-100). The text cites "accuracy of 31.06%" for Table 3 but no such value appears. This undermines trust in the cross-backbone generalization evidence. Fix: regenerate every table from logs, report one script-produced number per cell, and state backbone/time step per table.
### W2: Baseline comparison is not shown to be fair, and several baseline rows look broken
The training protocol for baselines is not stated (official code or reimplementation, loss, epochs, time steps, base-class split); SAFA-SNN trains with its own TET+MSE loss (Eq. 13). Baseline rows show pathological curves: S3C accuracy oscillates (16.52 → 17.89 → 31.17 in Table 1), WARP drops from 66.58 to 6.12 after one session (Table 9), CEC has base accuracy 12.95 (Table 8), and the ASP row (Table 6) falls to 16.04. These are signs of failed ports, not of a competitive baseline. Table 3 compares SAFA-SNN with Early Bird and SLTT at different time steps (4/5/6) and backbones. Fix: a matched-protocol table (same loss, epochs, T, backbone, seeds) with a plain SNN prototype-classifier baseline and an ANN reference row.
### W3: The gain is concentrated in base-session accuracy, not in incremental learning
Table 1: SAFA-SNN beats the second-best method CLOSER by 8.78 points at session 0 (74.66 vs 65.88) but by 4.01 at session 8; Table 6: +6.16 over TEEN at session 0 (76.03 vs 69.87), +3.58 at session 8. Table 4: seen accuracy 73.57 vs 62.35 (+11.22) but unseen 15.43 vs 14.95 (+0.48); Table 5: novel-class accuracy gains of +0.55 to +3.80 without std. SAFA-SNN also loses more accuracy over the sessions (Table 1: 25.96 points vs 21.19 for CLOSER; Table 6: 27.94 vs 25.36 for TEEN). The ablation (Fig. 6) is curve-only and takes the SA-only model as its baseline, so the effect of the new losses and ZOO on base training is not separated from the incremental components. Fix: ablate against a plain SNN with the same base-session recipe, reporting base and novel accuracy separately in a table with std.
### W3b: Hyper-parameters were selected on the reported test split and the margin collapses off the optimum
No validation split is described. A.11 states "it achieves the best performance when δ = 0.5 and S = 5, γ = 0.01 and β = 1.2", and these values are the training defaults (§6.1). Read from Fig. 8's extracted values, last-session accuracy varies from about 44.5 to 51.7, while TEEN reaches 44.51 in Table 6, so the margin over the best baseline is about 0.04 points at the worst grid point. "Our method is robust to the choices of hyper-parameters" (A.11) is therefore too strong. Fix: select on a class-wise held-out validation split and report test numbers once.
### W4: Efficiency claims are not backed by the measurements
(a) Energy is "gauged by multiplying power (W) by time" (§6.2), on a GPU module running dense emulation, so any saving reflects wall-clock time, not spikes. (b) Table 13 (theoretical inference energy): the SNN/ANN ratio is 0.7826 for VGG-5, VGG-9 and VGG-11 (7916.53/10115.57, 3958.41/5057.97, 494.92/632.39). With E_AC=0.9 pJ, E_MAC=4.6 pJ and T=4 (Eq. 28–30), the ratio equals 4·ζ·0.9/4.6, which gives a firing rate ζ≈1.0, inconsistent with "The sparsity remain up to 80%" (A.13). Spiking VGG-5 (7916 J) costs 16× Spiking VGG-11 (494.9 J) and VGG-13/16 ANN values are identical (5689.97), so the table is not a consistent per-model estimate. (c) No memory footprint is reported although memory is the stated motivation ("limited memory capacity (i.e., 4–12 GB)", §1). Fix: report peak memory, per-session latency and energy for all methods under one protocol, and recompute Table 13 with measured layer firing rates.
### W5: Convergence analysis does not support the method
Eq. 11–12 give an O(δ²+1/b) bound on E‖g(u)‖² and an O(1/√T) rate on E[g(u_T)−g(u*)], but g is the surrogate gradient, not the training loss; no smoothness or variance assumptions are stated (A.2 lists four alternative convergence criteria, one of them convex); Eq. 12 is a convex-type rate while the text says the problem is non-convex; and A.3 as provided contains Definition 1, Theorem 1, Eq. 24 and Theorem 3 (taken from Mukhoty et al., 2023) but no derivation of Eq. 11–12. A.1 says the variance is ∝1/(4δ²b) while Eq. 16 grows with b. Fix: state assumptions and prove a statement about the training loss, or remove the claim.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Table 6, SAFA-SNN row | Avg 56.59 | Mean of the nine printed sessions is 539.19/9 = 59.91 | Recomputed | High | MAJOR | Correct the average |
| ERR-2 | E1 | Table 6, TEEN row | Avg 59.34 | Mean of its nine sessions is 490.09/9 = 54.45; as printed TEEN (59.34) would beat SAFA-SNN (56.59), contradicting the ranking | Recomputed | High | MAJOR | Correct the average |
| ERR-3 | E1 | Tables 7, 9, 10, SAFA-SNN rows | Avg 58.12 / 56.35 / 45.68 | Recomputed 59.65 / 58.05 / 45.46 | Recomputed | High | MAJOR | Regenerate |
| ERR-4 | E6 | Table 7 vs Table 8; Table 6 vs Table 12; Table 1 vs Table 6 | "76.95 71.20 66.00 61.81 58.14 54.74 51.94 49.16 46.90" | The same nine values for VGG-11 and ResNet-20; Table 6/12 SAFA rows identical across CIFAR-100/VGG-9 and Mini-ImageNet/ResNet-18; Table 1 SAVC equals Table 6 SAVC (41.75 … 25.05, avg 32.17) across datasets | Cross-referenced | High | MAJOR | Report which numbers belong to which run |
| ERR-5 | E1 | §6.2 vs Table 3 | "Table 3 shows that our method achieves accuracy of 31.06%" | Table 3 lists HAcc 27.32/24.67/14.47, Lst 46.47/49.25/35.65, Avg 56.72/60.98/41.67; none is 31.06 | Cross-referenced | High | MAJOR | State which quantity is meant |
| ERR-6 | E6 | Table 4 vs Table 5 | Unseen 15.43 vs NAcc 16.68 | Same method, session 8 CIFAR-100: Table 4 gives 15.43, Table 5 gives 16.68 | Cross-referenced | Medium | MINOR | Reconcile |
| ERR-7 | E2 | Eq. 7 | Θt+1 = Θt − A (r̄n − r̄b) | A>0 for β,γ>0; if r̄n>r̄b the threshold falls and firing rises, a positive feedback. Possibly a sign convention | Derived | Medium | MAJOR | Fix sign or define A<0 |
| ERR-8 | E6 | Table 3, Param Size | "106.87" vs "22.63" | Same Spiking VGG9 on Mini-ImageNet: baselines 106.87 M, SAFA-SNN 22.63 M | Cross-referenced | Medium | MINOR | Explain what is counted |
| ERR-9 | E6 | Alg. 1 line 2 vs §5.3 | "randomly setting η% adaptive neurons 1" | §5.3 defines a deterministic first-⌊ηC⌋-channels mask, Algorithm 1 a random one | Cross-referenced | Medium | MINOR | Align |

Minor: symbol clashes (γ is both the LIF time constant in Eq. 1 and a hyper-parameter in Eq. 6; λ in Eq. 13 and Theorem 1), θ in §6.1 is undefined, Theorem numbering skips 2.

## Dimension Scores (0–100)
**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: multiple verified table inconsistencies and duplicated rows, baselines with pathological behavior, and hyper-parameters chosen on the reported test split.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | Eq. 7 sign, Eq. 11–12 not proved, projection notation (see Questions) |
| Clarity & Presentation | 50 | Developing | Notation clashes, undefined parameters |
| Novelty & Originality | 46 | Developing | ZOO borrowed, projection close to prior art (per Domain) |
| Significance & Impact | 50 | Developing | Real but niche setting; gain unclear |
| Experimental Validation | 38 | Developing | Unmatched baselines, test-split tuning, inconsistent tables |
| Reproducibility | 44 | Developing | Default η, γ, λ, α missing; no code link; baseline protocol missing |
| Ethical Compliance | 60 | Competent | Limitations paragraph exists (§7) but short |

NeurIPS-style: Quality 2, Clarity 2, Significance 2, Originality 2.

## Questions for Authors
1. Which tables were generated from the same run logs? Please give the true rows for Tables 7/8, 6/12 and the Table 1 SAVC row. (Raises the score if they are correct and the headline is unaffected.)
2. Were baselines trained with the same loss, epochs and time steps as SAFA-SNN? Please show a baseline that uses the Eq. 13 loss.
3. Is Eq. 14 written for B̃ ∈ R^{B×D} as stated in §5.5? With B̃ of size B×D the product B̃(B̃⊤B̃)⁻¹B̃⊤ is not defined for B<D, and C̃G has mismatched dimensions (this may be a notation transposition; the page image was not checked).
4. In incremental sessions, do the updated thresholds also change the features of base classes whose prototypes were computed before the update?
5. What do Fig. 4's near-identical values (about 15,75x J for Spiking ResNet20, read from the extracted text) mean? Was power sampled at a fixed rate?

## Limitations Assessment
**Partially.** §7 mentions deep networks (ResNet-34) and fixed class counts. Missing: sensitivity to the test-selected hyper-parameters, baseline fairness, and the GPU-vs-neuromorphic gap for energy.

## Ethics Review Flag
**No**

## Overall Score
**2**: Reject. The idea is plausible and the evaluation wide, but the evidence has verified internal inconsistencies, unmatched baselines and test-split tuning.

## Confidence
**4**: Recomputed all appendix averages; could not see figures.

---

## Reviewer 2 (Domain)

# Peer Review Report

## Paper: SAFA-SNN
## Reviewer: Prof. Adaeze Nwosu-Hart, Domain Reviewer (vision and learning group, public university in North America; fictional persona)
## Expertise: class-incremental and few-shot incremental learning; prototype methods
## Date: 2026-11-05

## Summary
The paper moves few-shot class-incremental learning from ANNs to SNNs and adds three ingredients: firing-rate-aligned thresholds with a channel mask, zeroth-order estimation of the spike gradient, and a projection of new-class prototypes onto the base-class prototype subspace. It claims to be the first SNN approach to general on-device FSCIL.

## Strengths
### S1: A reasonable and under-explored setting
SNN-based FSCIL has little prior work in the venues I know, and §2.1 correctly notes that most FSCIL methods are ANN-based. Event-based data (Table 2) is a natural fit.
### S2: Closed-form, training-free prototype step
The incremental update needs no gradient steps (Alg. 1, lines 16–17), which fits the setting, and Table 4–5 analyse where errors go (base vs novel).
### S3: Related work on dynamic thresholds is relevant
§2.2 names BDETT, LTMD and soft-threshold pruning, and §2.3 cites SNN pruning and on-device SNN training.

## Weaknesses
### W1: The "first" claim and the on-device framing are overstated (C1)
The paper states "the first SNN-based solution towards general on-device FSCIL" (§1) while §2.1 says "Prior work focuses on a specific processor (Huo et al., 2025)", i.e., an SNN FSCIL on-chip learner already exists. The distinction (general vs specific device) is asserted, not tested: the experiments run on a single GPU-class module (Jetson AGX Orin, §6.1) and no other device. The paper also builds its baselines by converting ANN FSCIL methods to SNNs, so the task formulation is not new. Fix: narrow the claim to "SNN backbones for FSCIL with a measured cost study", and compare with an SNN class-incremental method for the cited ALADE-SNN in all tables.
### W2: The zeroth-order contribution is taken from prior work (C2)
§3.1 says the approach is "inspired by prior work (Mukhoty et al., 2023)". Eq. 9 and Appendix A.3 (Definition 1, Theorem 1, Eq. 24, Theorem 3, the Sigmoid example) restate that paper's local zeroth-order surrogate construction; I did not find a new estimator or a new theorem. The new element is applying it to FSCIL base training, and no experiment compares it with the standard surrogate gradient of the same network (the ablation Fig. 6 only removes ZOO from a combined model). Because Eq. 24 shows the expectation is a smooth (Gaussian-kernel) surrogate, the motivating claim that "surrogate functions introduce gradient errors" (§3.1) applies to the proposed estimate as well. Fix: add a direct surrogate-vs-ZOO comparison and credit the source construction explicitly in the method section.
### W3: Subspace projection is close to published FSCIL work that is not cited (C2/C3)
Eq. 14–15 pull each new prototype towards the span of base prototypes: P̃ = (1−α)C̃ + αC̃G. "Subspace Regularizers for Few-Shot Class Incremental Learning" (ICLR 2022; verified link below) proposes regularizers that "encourage weight vectors for new classes to lie close to the subspace spanned by the weights of existing classes." The paper cites Simon et al. (2020) and TEEN (prototype calibration) for related ideas but not this work. This is a claim-level finding (cite and differentiate), not a verdict on the paper. The motivation is also questionable: new classes carry information outside the base span; the projection removes it. A.4 reports unseen accuracy 15.43 vs 14.95 (Table 4) so the effect on novel classes is small.
### W4: Sparsity-aware dynamics: what exactly is learned is unclear
Eq. 6–7 shift thresholds by the gap between incremental and base firing rates, with a channel mask whose adaptive fraction is η. Table 14 shows η=0.5 gives 61.96 average vs 59.01–59.77 for other η, so the mask matters, but there is no comparison with simply freezing everything (the standard FSCIL practice cited in §5.1) or with the cited threshold methods (BDETT, LTMD). The claim that "most neurons remain stable" is supported only by Fig. 12 (not visible to me).
### W5: Missing comparison to ANN FSCIL results
The motivation is that ANN methods are unsuitable for devices (§1), yet no ANN number for the same benchmark is given. Without it, readers cannot tell what accuracy is given up for the energy saving. Fix: add ANN reference rows (even if copied from the original papers, marked as such).

## Missing References
*Verified with `related_search.py verify` against arXiv where noted.*
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Akyürek, Akyürek, Wijaya, Andreas. "Subspace Regularizers for Few-Shot Class Incremental Learning." ICLR 2022. https://arxiv.org/abs/2110.07059 (verified; abstract read) | Same idea as Eq. 14–15 (new-class weights close to the base-class subspace) |
| Important | "Hebbian learning based orthogonal projection for continual learning of spiking neural networks", ICLR 2024 (arXiv 2402.11984, verified; authors [verify]) | SNN continual learning with projection onto orthogonal subspaces: the closest SNN-side prior for the projection idea |
| Important | Yang, Yuan, Li, Lin, Torr, Tao. "Neural collapse inspired feature-classifier alignment for few-shot class incremental learning." ICLR 2023 (arXiv 2302.03004, verified) | Strong ANN FSCIL method missing from the baseline set |
| Helpful | "Online Pseudo-Zeroth-Order Training of Neuromorphic Spiking Neural Networks" (arXiv 2407.12516, 2024; verified, authors [verify]) | Another zeroth-order-style SNN training method, relevant to C2 |
| Helpful | Han, Zhao, Zeng, Pan, Shen. "Enhancing Efficient Continual Learning with Dynamic Structure Development of Spiking Neural Networks." IJCAI 2023 (arXiv 2308.04749, verified) | Efficient SNN continual learning with dynamic structure |
| Helpful | "Similarity-based context aware continual learning for spiking neural networks" (Han et al., arXiv 2411.05802, 2024; verified) | SNN continual learning, context-dependent neuron selection |

### Literature-check addendum

**Per-claim novelty (hand-written profile; arXiv abstracts only):**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 first SNN on-device FSCIL | problem | medium | Huo et al. 2025 (cited; level 3; on-chip SNN FSCIL); ALADE-SNN (https://arxiv.org/abs/2412.12696, level 3, prior arXiv-only, cited) | No arXiv hit for SNN-FSCIL in 5 claim queries; search limit, so at most medium |
| Sparsity-aware thresholds | method | medium | BDETT (https://arxiv.org/abs/2206.04426, level 3, peer-reviewed, cited) | Firing-rate-matching channel mask across sessions seems new; averages-based thresholds exist |
| ZOO for spikes | method | incremental / known mechanism | Mukhoty et al., local zeroth-order SNN training (cited as inspiration; NeurIPS 2023). The arXiv entry "Energy Efficient Training of SNN using Local Zeroth Order Method" (https://arxiv.org/abs/2302.00910, level 5 for the estimator) appears to be the same line of work [verify identity with the cited NeurIPS paper] | Same construction; new only in the FSCIL use |
| Prototype subspace projection | method | incremental | Akyürek et al. (https://arxiv.org/abs/2110.07059, level 4, peer-reviewed, **not cited**) | Same geometric idea with a closed-form projection |
| Result: SNN FSCIL SOTA | result | n/a | Baselines are SNN-converted; no ANN reference | Not comparable to published numbers |

Paper reading: one established claim (projection) and one largely borrowed claim (ZOO): MAJOR at most; not "known results presented as new" because the overall combination is not found.

**Novelty delta (closest prior works by similarity):** ALADE-SNN (cited): CIL, adaptive logit alignment on expandable SNNs; SAFA-SNN is few-shot with a frozen backbone. Compressed latent replays (not cited, memory-efficient SNN CL with replay on SHD): different protocol. DSD-SNN (not cited): task-incremental structure growth.

**Baseline scout:** no SNN-FSCIL benchmark numbers retrievable from arXiv abstracts; all baselines were converted by the authors, so under-reported baselines cannot be checked. A missing baseline is not claimed.

**Field snapshot.** Before the cutoff, SNN work targets direct training with surrogate gradients and attention/transformer variants (Spikingformer, QKFormer are cited in the paper). Continual learning with SNNs is typically task- or class-incremental with expandable structure or replay (DSD-SNN, SCA-SNN, ALADE-SNN, latent replay). FSCIL itself is dominated by prototype and calibration methods on ANNs (TEEN, CLOSER, SAVC, NC-FSCIL) and by prompt methods on pre-trained transformers (cited). In SNN-FSCIL a significant contribution is one that gives a protocol (matched backbones, ANN references) in which an SNN is competitive with an ANN at lower measured cost; a few points on converted baselines is incremental.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Related-work gaps and unverified baselines |
| Clarity | 2 | Claims vs evidence misaligned |
| Significance | 2 | Niche, measured gain unclear |
| Originality | 2 | Mostly recombination of cited and uncited prior ideas |

## Dimension Scores (0–100)
**Pool position:** better than about 40% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: the three components each have close prior work and no component is isolated against it; the setting is interesting enough to keep this above the weakest submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Reasoned design, but borrowed and unproven theory |
| Clarity & Presentation | 55 | Competent | Understandable contribution list |
| Novelty & Originality | 48 | Developing | See literature addendum |
| Significance & Impact | 52 | Developing | Niche but real setting |
| Experimental Validation | 46 | Developing | No ANN reference, converted baselines |
| Reproducibility | 50 | Developing | Hyper-parameter defaults missing |
| Ethical Compliance | 62 | Competent | No ethical issue |

## Questions for Authors
1. How does Eq. 14–15 differ from subspace regularization toward the base-class span (ICLR 2022)? A convincing difference would raise Novelty.
2. Please compare ZOO with the standard surrogate gradient in the same network and report base-session accuracy.
3. What is the SNN–ANN accuracy gap on the same benchmark and backbone?

## Limitations Assessment
**Partially.** §7 names deep networks and fixed class counts; the dependence on a single hardware platform is not mentioned.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A coherent but incremental recombination whose novelty is partly overstated and not isolated by ablation.

## Confidence
**4**

---

## Reviewer 3 (Perspective)

# Peer Review Report

## Paper: SAFA-SNN
## Reviewer: Dr. Ilan Peretz-Vasquez, Perspective Reviewer (embedded-systems and neuromorphic hardware lab, South America; fictional persona)
## Expertise: edge deployment; event-based sensing; energy modeling
## Date: 2026-11-05

## Summary
The paper argues that continual learning of new classes from few examples should happen on the device where the data arrive, and that SNNs are a good fit. It builds an FSCIL system on SNN backbones with threshold alignment and prototype projection, and measures training energy and time on a Jetson module.

## Strengths
### S1: A relevant deployment scenario
Years-long, privacy-sensitive, few-sample data collection on edge devices (Fig. 1, §1) is a real concern, and the focus on both training and inference on the device is welcome.
### S2: Event-camera datasets
Using CIFAR-10-DVS, DVS128gesture and N-Caltech101 (Table 2) tests the method on the data type SNNs are designed for, with a 1-way 1-shot protocol that is demanding.
### S3: Measured, not only modeled, cost
Energy and time on real hardware (Fig. 4–5) is a good practice; the paper also gives the theoretical model (A.9).
### S4: Sparsity analysis
Appendix A.13 and Fig. 10–11 give sparsity of 0.83–0.90 for the trained network and A.14 shows firing-rate traces, supporting the "mostly quiet neurons" story, if only qualitatively.

## Weaknesses
### W1: Energy claim crosses a hardware gap
The measured savings are on an Orin AGX GPU module (§6.1). On a GPU, spikes are executed as dense tensor operations, so event-driven savings are not realized; the energy figures reflect training time (Fig. 5) not synaptic operations. The 60 W / 15 W figures are the module's limits, not measurements of the runs. Opportunity: report neuromorphic-simulator or accelerator estimates (e.g., synaptic-operation counts with measured layer firing rates) next to the GPU number, and state that GPU energy is a proxy. I also note that Table 13's SNN/ANN ratio of 0.7826 implies a firing rate near 1.0 under Eq. 28–30 with T=4 (derived), which conflicts with the 0.83–0.90 sparsity of A.13.
### W2: Memory, the stated bottleneck, is not measured
The motivation is limited memory of 4–12 GB (§1) yet no peak-memory number appears for any method; the Orin AGX has considerably more memory than that range (to my knowledge, 32–64 GB; the authors should state their module). Opportunity: report peak memory and run on a smaller platform.
### W3: Base-session training is not "on device" in the sense used
Base training uses abundant data, 300 epochs (§6.1) on the same module, and Fig. 1 shows base training as a first stage. If the realistic deployment trains the base model off-device, the claim of "both training and inference are performed on resource-constrained devices" (§1) applies only to the incremental stage, which requires no gradient steps in SAFA-SNN (Alg. 1). Opportunity: separate base and incremental cost.
### W4: Assumptions about the data stream
Fixed N-way K-shot sessions with disjoint classes (§4, §7) are acknowledged as a simplification; real streams are imbalanced and may revisit classes. The authors state this as future work; a small imbalanced-stream experiment would increase impact.
### W5: Cross-disciplinary connections
Hebbian/local-learning rules and neuromorphic continual-learning chips are natural reference points; the paper cites one chip paper (Huo et al., 2025) and a Hebbian survey (Safa, 2024) but does not connect the threshold alignment to homeostatic plasticity beyond a sentence in §2.2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Energy evidence not tight |
| Clarity | 2 | Deployment story partly mismatched |
| Significance | 3 | Relevant scenario |
| Originality | 2 | Familiar components, new combination |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: a timely, well-motivated deployment setting and a wide dataset range; I weigh these more than the evidence gaps because many of the gaps (memory, hardware proxy) are fixable by additional measurement.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound design; energy modeling loose |
| Clarity & Presentation | 58 | Competent | Understandable, with notation clashes |
| Novelty & Originality | 60 | Competent | New setting for SNNs |
| Significance & Impact | 66 | Competent | Relevant scenario |
| Experimental Validation | 55 | Competent | Broad but not tight |
| Reproducibility | 58 | Competent | Code promised "in the codes" |
| Ethical Compliance | 66 | Competent | No ethical issues; limitations stated |

## Questions for Authors
1. What is the peak memory of SAFA-SNN versus an ANN FSCIL baseline and versus a prompt-based method on your device? A large gap would raise my score.
2. How were the energy values in Fig. 4 obtained (sampling rate, rails included)? The values read from extracted text for Spiking ResNet20 are almost identical across methods.
3. Would the method survive imbalanced sessions?

## Limitations Assessment
**Partially.** §7 lists limits on depth and fixed class counts; hardware generality and the GPU proxy for energy are not discussed.

## Ethics Review Flag
**No**: the surveillance example in §1 is motivating only; no personal data are used.

## Overall Score
**4**: Borderline Accept. The scenario and breadth are attractive and most gaps are fixable measurements, but I hold this lightly given the table issues other reviewers may find.

## Confidence
**3**: Hardware side is my strength; I did not recompute every table.

---

## Reviewer 4 (Generalist)

# Peer Review Report

## Paper: SAFA-SNN
## Reviewer: Dr. Sunita Raghavan-Moore, Generalist Reviewer (ML group, research university, South Asia; fictional persona)
## Expertise: deep learning for vision
## Date: 2026-11-05

## Summary
The paper proposes SAFA-SNN, an SNN-based few-shot class-incremental learner. It combines firing-rate-aligned thresholds (a fraction η of channels stays adaptive), a zeroth-order spike-gradient estimate and a prototype projection step. Results are given for five datasets, with improvements of about 4 points at the last session on Mini-ImageNet and a reported ~20% energy reduction on a Jetson device.

## Strengths
### S1: Clear problem statement and figure
Fig. 1 and §4 define on-device FSCIL clearly, and the contribution list (§1) maps onto three method subsections (§5.3–5.5).
### S2: Many experiments
Tables 1–3 and A-tables cover several datasets and backbones; hyper-parameter and time-step sweeps (A.11–A.12) are provided.
### S3: Sensible venue topic
SNN continual learning and efficient ML are in scope for ICLR; the on-device framing gives it a practical angle.

## Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly | Tables 1, 6–12 inconsistent; test-split tuning (A.11) |
| Presentation | Partly | §5 notation clashes; Eq. 14 sizes; undefined θ (§6.1) |
| Contribution: new insight | Partly | Combination of known pieces (§5.4 inspired by Mukhoty et al.) |
| Evidence breadth | Met | Five datasets (§6.1) |
| Limitations honest | Partly | §7 short |

## Weaknesses
### W1: Claims run ahead of the evidence
The abstract and §8 state that SAFA-SNN "outperforms existing FSCIL methods in both performance and energy efficiency". The comparison set is SNN-converted baselines only, several of which behave pathologically (S3C in Table 1; WARP in Table 9), and the efficiency evidence is measured on a GPU module. A narrower claim ("outperforms SNN-converted baselines on these protocols") would match the evidence. Fix: reword, and add an ANN reference row.
### W2: The method section is hard to follow and not self-consistent
§5.3 never says how thresholds are updated in an incremental session with only a few samples (Alg. 1 line 9 updates Θ once), nor whether the update changes the representation of the base classes. Eq. 7's sign is surprising (a higher incremental firing rate lowers the threshold). Eq. 14 is dimensionally inconsistent as stated for B̃ ∈ R^{B×D}. The loss in Eq. 13 mixes cross entropy and MSE, yet the interplay with ZOO is not discussed. Fix: a worked small example and an algorithm box with all parameters (η, γ, λ, α defaults).
### W3: Ablation is difficult to read
Fig. 6 shows curves only. "We can infer that SA has the worst performance" and treating SA as the baseline obscures what a no-component SNN gives. Fix: a table with all eight subsets including a vanilla SNN, with base and novel accuracy.
### W4: Appendix inconsistencies reduce trust
Averages in Tables 6, 7, 9, 10 do not match their rows (Methodology report ERR-1–3), identical rows recur across tables (ERR-4), and "accuracy of 31.06%" for Table 3 has no counterpart. A reader who finds one of these discounts the rest.

Minor: "hardens the ability of ANNs" (A.9), "ture gradient" (A.1), "firing rete" (A.14), "Table 3 shows … 31.06%".

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence partly inconsistent |
| Clarity | 2 | Method hard to reproduce from text |
| Significance | 2 | Niche, modest gain |
| Originality | 2 | Recombination |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted ≈ 27%). Deciding evidence: a clear topic and broad experiments put it above the median, while the inconsistencies and unclear method keep it below the 62–72 band of typical accepted papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Method partly unclear |
| Clarity & Presentation | 50 | Developing | Notation clashes, ablation as curves |
| Novelty & Originality | 50 | Developing | Recombination |
| Significance & Impact | 55 | Competent | Practical angle |
| Experimental Validation | 48 | Developing | Unmatched baselines, inconsistent tables |
| Reproducibility | 52 | Developing | Missing defaults, no link visible |
| Ethical Compliance | 60 | Competent | No issues |

## Questions for Authors
1. Please give the missing defaults (η, γ, λ, α) and where the base-class number is stated.
2. Which numbers in A.8's tables are from which runs?
3. How are baselines run (official code?).

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. Worthwhile topic; claims and evidence do not yet line up.

## Confidence
**3**

---

## Devil's Advocate

# Devil's Advocate Report

## Paper: SAFA-SNN
## Reviewer: Dr. Keiko Maldonado-Reyes, evaluation-methodology group (East Asia; fictional persona)

## Steelman
SNN backbones could make on-device FSCIL cheaper, and if a simple threshold-alignment plus prototype-projection recipe gives better last-session accuracy than SNN versions of the standard FSCIL methods on five datasets, that is a useful recipe for an under-explored setting.

## Core Argument Chain
1. SNNs are energy-efficient and suit edge devices (§1).
2. FSCIL's two problems are forgetting and overfitting (§1).
3. Aligning thresholds with a channel mask reduces forgetting (§5.3); ZOO avoids surrogate-gradient error (§3.1, §5.4); subspace projection reduces overfitting (§5.5).
4. SAFA-SNN beats SNN-converted FSCIL baselines on five datasets (Tables 1–2, 6–12) and uses less energy on a Jetson (Fig. 4–5).
∴ SAFA-SNN is a better solution for on-device FSCIL.

## Strongest Counter-Argument
Even if every number is right, the data do not show that the three named components do what they are claimed to do. The headline gap is largest at session 0, before any incremental learning happens: Table 1 shows +8.78 over CLOSER at session 0 (74.66 vs 65.88), shrinking to +4.01 at session 8; Table 6 shows +6.16 over TEEN at session 0 (76.03 vs 69.87) and +3.58 at session 8. SAFA-SNN also degrades more across sessions (Table 1: 25.96 points vs 21.19 for CLOSER; Table 6: 27.94 vs 25.36 for TEEN). So the sparsity-aware "forgetting mitigation" is not visible in the forgetting curve. The novel-class story is weak as well: Table 4 reports unseen accuracy 15.43 vs 14.95 (+0.48) and Table 5 reports novel accuracy gains of +0.55 to +3.80 without variance, while A.16 asserts that the method "significantly improves the recognition accuracy of new classes". The gain is most simply explained by a stronger base-session recipe (Eq. 13's TET+MSE loss, the different gradient estimator, more training), applied to SNN-converted baselines whose protocol is not stated and some of which collapse (WARP 66.58 → 6.12 in Table 9, CEC base 12.95 in Table 8). A plain SNN with a prototype classifier and the same base-session loss is the missing control; the ablation (Fig. 6) takes "SA" as its baseline instead. The efficiency half of the claim has a parallel problem: energy is power×time on a GPU module (§6.2), so it measures wall-clock time, and the theoretical table (A.9, Table 13) is consistent only with a firing rate of about 1.0, not the reported 80%+ sparsity. The authors must show, with matched protocols, that gains survive in the incremental sessions and are due to the proposed components.

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Integrity | Table 7 vs Table 8; Table 6 vs Table 12; Table 1 vs Table 6 | Identical nine-session SAFA-SNN rows for different backbones (VGG-11/ResNet-20) and for different dataset/backbone pairs (CIFAR-100 VGG-9 / Mini-ImageNet ResNet-18), and identical SAVC rows (41.75 … 25.05, Avg 32.17) in Mini-ImageNet Table 1 and CIFAR-100 Table 6; averages that do not match their rows (Table 6 TEEN 59.34 vs recomputed 54.45; SAFA-SNN 56.59 vs 59.91). Stated factually as a concern for the editor, not as an accusation: copy-paste or labeling errors are the likely cause, but as printed the cross-backbone evidence cannot be trusted. | Authors regenerate Tables 1, 6–12 from logs and state per-table backbone, dataset and T | Clarification / minor additions (corrected tables from existing logs) |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Tables 1, 4, 5, 6; A.16 | Gain concentrated at session 0 and in seen classes; novel-class gain +0.48 (Table 4) and +0.55–3.80 (Table 5) vs wording "significantly improves" new classes (A.16). Evidence supports a weaker claim | Narrow the claim; report base/novel/harmonic accuracy with std for all methods |
| DA-M2 | Logic | Fig. 6, §6.3 | No plain-SNN-plus-prototype control with the same base recipe; "SA" is taken as baseline; no ZOO-vs-surrogate-gradient comparison | Add the control and the surrogate comparison |
| DA-M3 | Evidence | §6.2, Tables 1, 6–10, A.7 | Baseline fairness: protocol unstated; pathological baseline rows; Table 2 compares only WARP and TEEN, not CLOSER, the second best in Table 1; Table 3 mixes time steps and backbones; ASP (a prompt method on frozen pre-trained backbones) appears only in Table 6 | Matched-protocol table; explain the SNN port of each baseline; add CLOSER to Table 2 |
| DA-M4 | Evidence | A.11, Fig. 8, Table 14, §6.1 | Hyper-parameters chosen as best on the reported test split (criterion-3 table, second row: the best-scoring option, but the comparison with TEEN still holds at every point read from Fig. 8, with a minimum margin of about 0.04 points); Table 14's best row (η=0.5, λ=0.05) gives Avg 61.96, above the headline 59.91 recomputed, so the headline is not the best-scoring configuration either. Reported as MAJOR | Validation split for selection; report test once |
| DA-M5 | Scope | §6.2 (Fig. 4–5), A.9 (Table 13), §6.3, A.13 | Efficiency claim not tested by the design: GPU power×time; Table 13 ratio 0.7826 = 4·ζ·0.9/4.6 implies ζ≈1.0 vs sparsity 0.83–0.90; no memory measurement though memory is the motivation; the "20% lower" figure cannot be reproduced from the extracted bar labels (figure unavailable) | Report memory, latency and measured-firing-rate energy per method |
| DA-M6 | Logic | Eq. 11–12, A.1–A.3 | Convergence claims about a surrogate gradient, no assumptions, a convex-type rate for a non-convex problem, no proof of Eq. 11–12 in A.3, and A.1 contradicts Eq. 16 on the dependence on b | Remove or restate with assumptions and a proof |
| DA-M7 | Novelty | §3.1, §5.4–5.5, A.3 | ZOO construction taken from Mukhoty et al. (2023); projection resembles ICLR 2022 subspace regularizers (uncited) | Cite, differentiate, and isolate new elements |
| DA-M8 | Logic | Eq. 7, Alg. 1 | Sign of the threshold update; Θ initialised to zero ("Initialize threshold Θ with zeros") so every neuron fires initially; one update per session | Clarify; show firing-rate convergence |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Clarity | Eq. 14 | Dimensions for B̃ ∈ R^{B×D} do not allow the product as written (notation; page image unchecked) |
| DA-m2 | Clarity | §6.1 | θ and η, γ, λ, α defaults not given |
| DA-m3 | Evidence | Table 4 vs Table 5 | Unseen 15.43 vs NAcc 16.68 for session 8 |
| DA-m4 | Evidence | Table 3 | Param size 22.63 M (SAFA VGG-9, Mini-ImageNet) vs 106.87 M (baseline VGG-9) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Table 1 last-session gain over CLOSER | +4.01 | 48.70 − 44.69 = 4.01 | Yes |
| Table 1 average gain over CLOSER | 6.07 (§6.2) | 59.45 − 53.38 = 6.07 | Yes |
| Table 1 SAFA-SNN average | 59.45 | (74.66+68.93+64.62+61.29+58.30+55.38+52.60+50.58+48.70)/9 = 59.45 | Yes |
| Table 6 SAFA-SNN average | 56.59 | 539.19/9 = 59.91 | No |
| Table 6 TEEN average | 59.34 | 490.09/9 = 54.45 | No |
| Table 7 SAFA-SNN average | 58.12 | 536.84/9 = 59.65 | No |
| Table 9 SAFA-SNN average | 56.35 | 522.46/9 = 58.05 | No |
| Table 13 SNN/ANN ratio | n/a | 494.92/632.39 = 0.7826 → ζ ≈ 1.0 at T=4 | Inconsistent with sparsity ≥ 80% |
| "accuracy of 31.06%" | §6.2 | Not present in Table 3 | No |

## Ignored Alternative Explanations
Stronger base-session training (Eq. 13, ZOO, more epochs) rather than threshold alignment; ANN-to-SNN porting quality of baselines; test-split hyper-parameter tuning; wall-clock rather than spike sparsity driving the energy number.

## Missing Stakeholder Perspectives
Practitioners with 4–12 GB devices: no memory result; users with imbalanced data streams (§7 acknowledges).

## Observations (Non-Defects)
The paper discloses its limitations on deep networks and fixed way/shot (§7), reports seed variance in Table 1/2/3, includes an error-type analysis (Table 4), and gives full backbone tables in the appendix, which is what made the inconsistencies detectable.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 38 | Eq. 7/14/11–12 problems |
| Clarity & Presentation | 48 | Method under-specified |
| Novelty & Originality | 42 | Borrowed ZOO, close projection |
| Significance & Impact | 45 | Gain unclear in incremental stage |
| Experimental Validation | 36 | Missing control, test-tuned, inconsistent |
| Reproducibility | 42 | Defaults missing |
| Ethical Compliance | 58 | No issues |

**Pool position:** better than about 27% of submissions to ICLR. Deciding evidence: verified inconsistent tables and a missing control that leaves the central attribution untested.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (inconsistent tables) | kept | Specific, recomputed, consistent with the paper |
| R1 | W4(b) Table 13 ratio | kept (derived) | Arithmetic reproduced from printed values |
| R1 | Fig. 4 near-identical values | moved to Questions | Figure unavailable; extracted labels only |
| R1 | Eq. 14 dimensions | moved to Questions | Possible extraction/notation artifact |
| R2 | W1 ("first" claim) | rewritten | Added location of the Huo et al. sentence (§2.1); keep as overclaim, not as known result |
| R2 | W3 (uncited projection prior) | kept | Abstract of the verified prior read; claim-level, MAJOR at most |
| R3 | W1–W2 | kept | Consistent with §6.1/§6.2; the "32–64 GB" memory figure is background knowledge, flagged as a question |
| R3 | W5 (cross-disciplinary) | moved to Minor | Expansion suggestion |
| R4 | W2 (method unclear) | kept | §5.3 and Alg. 1 confirm the gaps |
| R4 | typos | moved to Minor line | Cosmetic |
| DA | DA-C1 | kept as CRITICAL for EIC ruling | Has a location, quote and recomputation |
| DA | DA-M4 | kept | Fig. 8 numbers read from extracted text, noted |

Scores unchanged.

## Synthesizer package (Part A)

**Master issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Table/appendix inconsistencies, duplicated rows | R1-W1, R4-W4, DA-C1, DA-m3 | CONSENSUS-3 (+DA-CRITICAL) |
| Baselines unmatched / pathological / no ANN reference | R1-W2, R2-W5, R4-W1, DA-M3 | CONSENSUS-4 |
| Gain from base session, not incremental mechanism; no control | R1-W3, DA-M1, DA-M2, R4-W3 | CONSENSUS-3 |
| Test-split hyper-parameter selection | R1-W3b, DA-M4 | CONSENSUS-2 |
| Efficiency claim not supported (GPU proxy, Table 13, no memory) | R1-W4, R3-W1, R3-W2, DA-M5 | CONSENSUS-3 |
| Novelty: ZOO borrowed, projection prior uncited, "first" claim | R2-W1–W3, DA-M7 | CONSENSUS-2 |
| Convergence analysis unsupported | R1-W5, DA-M6 | CONSENSUS-2 |
| Method under-specified (Eq. 7, Eq. 14, defaults) | R1-ERR-7, R4-W2, DA-M8 | CONSENSUS-3 |
| SPLIT: R3 weighs deployment relevance and breadth positively (Overall 4) vs DA/R1 (Overall 2) | R3 vs R1, DA | SPLIT |

Hinge points for the EIC: table duplication (DA-C1), the base-session explanation of the gain, the test-split tuning, the Table 13 ratio.

**Official score (BEFORE EIC weights, DA-C1 provisionally upheld):** composite 50.3 official / 49.8 confidence-weighted; ratings 2, 3, 4, 3, 2 → mean 2.80; weighted 2.75 → starting point 3; provisional ceiling 4.

---

# Phase 2: EIC Meta-Review and Decision

# Editorial Decision

## Paper: SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network
## Submission ID: iclr26-9jcB40wjk3
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Anselm Varga; R1 Dr. Tomasz Brzezicki; R2 Prof. Adaeze Nwosu-Hart; R3 Dr. Ilan Peretz-Vasquez; R4 Dr. Sunita Raghavan-Moore; DA Dr. Keiko Maldonado-Reyes

---

## Decision: Borderline Reject (3); ICLR rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})

**Official ratings** (shown to authors): R1 2, R2 3, R3 4, R4 3, DA 2 → mean 2.80 · official composite 50.3
**EIC assessment** (internal): weighted rating 2.65 → starting point 3 · weighted composite 49.1 → band 2 (cross-check) · **DA ceiling**: none (DA-C1 downgraded) · **Final (EIC)**: 3
**EIC pool position:** about 38 (better than roughly 38% of ICLR submissions). Deciding evidence: a legitimate, under-explored setting with broad experiments, but verified inconsistencies in the appendix tables, no control isolating the proposed components, and test-split hyper-parameter selection.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** SNN-based FSCIL is under-explored; the paper evaluates on five datasets including event data, reports variance, and the main Mini-ImageNet table (Table 1) shows a verified +4.01 last-session and +6.07 average gain over the best SNN-converted baseline. R3 sees a relevant deployment scenario.
- **Against acceptance:** Gains concentrate in the base session and in seen classes, not in the incremental mechanism; baselines are unmatched and several look broken; efficiency claims rest on a GPU proxy and a theoretical table that implies a firing rate of ~1.0; each of the three components has close prior work (ZOO from Mukhoty et al., projection close to ICLR 2022 subspace regularizers); appendix tables contain wrong averages and duplicated rows.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 6 averages wrong (SAFA 56.59 vs 59.91; TEEN 59.34 vs 54.45) | R1-ERR-1/2, DA-C1 | Table 6 | Verified | Recomputed from printed rows |
| Identical SAFA rows in Tables 7/8 and 6/12; SAVC row in Tables 1/6 | R1-ERR-4, DA-C1 | Tables 1, 6, 7, 8, 12 | Verified | Values identical to the digit |
| Main Table 1 headline (+4.01, +6.07) | R1, R2, DA | Table 1, §6.2 | Verified | Arithmetic holds; SAVC row affects a weak baseline only |
| Gain largest at session 0; more forgetting than baselines | R1-W3, DA | Tables 1, 6 | Verified | +8.78 → +4.01; drops 25.96 vs 21.19 |
| Novel-class gain small (Table 4: +0.48; Table 5: +0.55–3.80) vs "significantly improves" (A.16) | DA-M1 | Table 4–5, A.16 | Verified | Wording overstated |
| Table 13 ratio implies ζ≈1.0 | R1-W4, R3-W1, DA-M5 | A.9, Table 13, Eq. 28–30 | Verified | 494.92/632.39 = 0.7826 = 4·ζ·0.9/4.6 for ζ=1.0 |
| "20% lower energy" reproduces from Fig. 4 | DA-M5 | Fig. 4, Abstract | Partly correct | Not checkable from extracted labels; the ratio 12,624/15,752 gives 19.9%, so the claim may refer to ResNet20 only; unverifiable |
| Hyper-parameters tuned on test (A.11) | R1-W3b, DA-M4 | A.11, Fig. 8 | Verified | Quote "it achieves the best performance when δ = 0.5 and S = 5"; defaults in §6.1 match; main comparison holds across the sweep read from the figure |
| ZOO borrowed | R2-W2, DA-M7 | §3.1, A.3 | Verified | "inspired by prior work (Mukhoty et al., 2023)" |
| Projection prior uncited | R2-W3 | Eq. 14–15 | Verified | Abstract of the ICLR 2022 work read |
| Eq. 7 sign | R1-ERR-7, R4-W2, DA-M8 | Eq. 6–7 | Partly correct | Sign as printed is destabilizing; may be convention |
| Eq. 14 dimensions | R1-Q3, R4, DA-m1 | §5.5 | Partly correct | Inconsistent if B̃ is B×D; fine if D×B; page not checked |
| Convergence claims unsupported | R1-W5, DA-M6 | Eq. 11–12, A.1–A.3 | Verified | No derivation of Eq. 11–12 in A.3 as provided |
| Table 3 "31.06%" | R1-ERR-5 | §6.2 vs Table 3 | Verified | Value absent |
| R3: "memory of the Orin AGX is larger than 4–12 GB" | R3-W2 | §1, §6.1 | Unverifiable from the paper | Background knowledge; treated as a question |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Every Error Log entry I checked held (recomputed averages, duplicates, Table 13 ratio); decisive for the outcome |
| R2 (Domain) | 3 | 4 | 1.0 | Literature points verified; sound and typical |
| R3 (Perspective) | 4 | 3 | 0.75 | Raised the energy and memory gaps but still rated Borderline Accept without weighing the verified table errors and the base-session explanation; pool position 65 sits above what the verified evidence supports |
| R4 (Generalist) | 3 | 3 | 1.0 | Calibrated; largely echoes R1 on inconsistencies |
| DA | 2 | 4 | 1.0 | Main arguments survived the check; DA-C1 was over-rated but its evidence is real, so scores keep full weight |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 (identical rows, wrong averages) | No: the duplicates and wrong averages are in appendix tables and in one weak baseline row of Table 1; the headline comparison with the best baseline (CLOSER, Table 1) recomputes correctly, and the evidence shows a reporting error, not demonstrated fabrication (criterion 4 requires concrete evidence of manipulation). | **Downgraded to MAJOR** | Clarification / minor additions (corrected tables from existing logs). Reported to the editor as a data-integrity concern for the authors to explain |

### Final Decision and Justification
The EIC-weighted rating is 2.65, giving a starting point of 3 (Borderline Reject). The composite cross-check (49.1) falls in band 2, a one-step difference within one point of the band edge at 50, so I do not depart on that basis. I name no verified issue that the ratings missed; the ratings already reflect the inconsistencies and the missing control. I keep 3 rather than 2 because the setting is legitimate, Table 1's headline comparison is arithmetically sound and the weaknesses are mostly fixable by regeneration of tables, matched baselines and one control experiment, not by a new idea; I do not go to 4 because three of four components lack isolation against close prior work and the efficiency claims are not demonstrated. No DA ceiling applies. Under the ICLR scale this paper would likely receive a rating of 4 on {0,2,4,6,8,10}. Hard Rule 4: this is a simulation, not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 40 | 50 | 62 | 52 | 38 | 48.4 | 46.7 | 24 ⚠ |
| Clarity & Presentation | 50 | 55 | 58 | 50 | 48 | 52.2 | 51.7 | 10 |
| Novelty & Originality | 46 | 48 | 60 | 50 | 42 | 49.2 | 48.1 | 18 |
| Significance & Impact | 50 | 52 | 66 | 55 | 45 | 53.6 | 52.3 | 21 ⚠ |
| Experimental Validation | 38 | 46 | 55 | 48 | 36 | 44.6 | 43.3 | 19 |
| Reproducibility | 44 | 50 | 58 | 52 | 42 | 49.2 | 48.1 | 16 |
| Ethical Compliance | 60 | 62 | 66 | 60 | 58 | 61.2 | 60.8 | 8 |
| **Composite** | 45.4 | 50.9 | 60.5 | 52.0 | 42.7 | **50.3 (before: confidence-weighted 49.8)** | **49.1 (after)** | |
| Pool position (P%) | 30 | 40 | 65 | 44 | 27 | | | |

Spread discussion: Technical Rigor (24) and Significance (21) diverge because R3 scores the scenario and breadth while R1/DA score the verified errors. I adopt R1/DA on Technical Rigor (checked) and the middle on Significance (setting relevant, gain unclear).

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); skill Overall 3 (Borderline Reject) |

*The ICLR scale is labelled `secondary`; check the current form before using these labels as official.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network" to ICLR.

The paper addresses few-shot class-incremental learning with spiking networks on edge devices, an under-explored and timely combination.

**Overall Assessment:**
The reviewers value the setting, the breadth of datasets (including event data) and the attempt to measure cost on hardware. They found, however, that the evidence does not yet isolate what the proposed components contribute, that several tables contain errors, and that the efficiency claims are not backed by the measurements.

**Key Strengths Identified by Reviewers:**
1. A relevant on-device FSCIL scenario and a broad dataset set including neuromorphic data (R3, R4, R1).
2. Seen/unseen error analysis and variance reporting in the main tables (R1, DA).
3. A closed-form incremental step suited to the setting (R2).

**Key Concerns Requiring Attention:**
1. Appendix tables with averages that do not match their rows and identical rows across settings (CONSENSUS-3; R1, R4, DA).
2. Unmatched, in places pathological, baselines and no ANN reference; the gain is largest at session 0 and the forgetting curve is worse than for baselines (CONSENSUS-4/3).
3. Efficiency claims (GPU power×time, Table 13 implying ζ≈1.0, no memory result) (CONSENSUS-3).
4. Component novelty: ZOO from Mukhoty et al. (2023); projection close to ICLR 2022 subspace regularizers; "first" claim (CONSENSUS-2).
5. Hyper-parameters selected on the reported test split (CONSENSUS-2).

**Critical Challenge (Devil's Advocate):**
The strongest objection is that the data do not show the three components cause the gain: it is already present at session 0, forgetting is not reduced, and the missing control (a plain SNN with the same base recipe) leaves the attribution untested. The DA's CRITICAL integrity issue was downgraded to MAJOR (reporting inconsistency, not demonstrated manipulation), but the editor asks that it be explained.

**Decision: Borderline Reject (3)**

This paper is not recommended for acceptance in its current form. A resubmission would need: regenerated and consistent tables; matched baselines with ANN references; a control isolating each component; hyper-parameters chosen on a validation split; measured memory and consistent energy accounting; and cited and differentiated prior work. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Anselm Varga
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Unmatched / broken baselines, no ANN reference | R1, R2, R4, DA | CONSENSUS-4 |
| Inconsistent appendix tables, duplicated rows | R1, R4, DA | CONSENSUS-3 |
| Gain not attributed to the proposed components; missing control | R1, R4, DA | CONSENSUS-3 |
| Efficiency claim not supported | R1, R3, DA | CONSENSUS-3 |
| Method under-specified (Eq. 7, Eq. 14, defaults) | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the paper at or above the accept bar? | R3 (4) | R1, DA (2) | R1/DA arguments verified; R3's points are fixable measurements, but they do not offset verified errors |
| Is DA-C1 fatal? | DA | R1 (MAJOR), EIC | Downgraded: reporting error in appendix; headline row recomputes |

### Score Spread Discussion
Technical Rigor (24): R1 and DA verified specific errors, R3 did not recompute; adopt R1/DA. Significance (21): R3 values the scenario; R1/DA doubt the measured gain; adopt a middle value.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Identical rows / wrong averages | Yes (R1, R4) | Downgraded to MAJOR: reporting error, headline unaffected | Clarification / minor additions |
| DA-M1 | MAJOR | Gain at session 0 and seen classes | Yes (R1) | n/a | n/a |
| DA-M2 | MAJOR | Missing plain-SNN control | Yes (R4) | n/a | n/a |
| DA-M3 | MAJOR | Baseline fairness | Yes (R1, R2, R4) | n/a | n/a |
| DA-M4 | MAJOR | Test-split tuning | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Efficiency claim | Yes (R1, R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Inconsistent / duplicated table rows, wrong averages, "31.06%" | R1-W1, R4-W4, DA-C1 (downgraded) | Tables 1, 3, 6–12; §6.2 | Regenerate from logs; per-table backbone/T; explain duplicates | Low–Med | Yes |
| R2 | Component attribution: no plain-SNN control, base vs novel accuracy | R1-W3, DA-M1, DA-M2 | Fig. 6, Tables 1, 4–6 | Eight-way ablation table with std; surrogate vs ZOO | Med (~30–60 GPU-h) | Partly |
| R3 | Baseline fairness and ANN reference | R1-W2, R2-W5, DA-M3 | §6.2, A.7, Tables 1–3, 6–10 | Matched loss/epochs/T; ANN rows; add CLOSER to Table 2 | High (~100+ GPU-h) | No |
| R4 | Efficiency claims | R1-W4, R3-W1/W2, DA-M5 | §6.2, A.9, Fig. 4–5, Table 13 | Peak memory, latency, energy with measured firing rates; fix Table 13 | Med | Partly |
| R5 | Hyper-parameter selection on test | R1-W3b, DA-M4 | A.11, Fig. 8, Table 14 | Validation split; report test once | Med | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Novelty positioning: cite and differentiate Akyürek et al. (ICLR 2022), Hebbian orthogonal projection (ICLR 2024), Mukhoty et al. as source of ZOO | R2-W2/W3, DA-M7 | Rewrite related work and contribution claims | Low | Yes |
| S2 | Convergence claims | R1-W5, DA-M6 | Remove or restate with assumptions and a proof | Low–Med | Yes |
| S3 | Method clarity: Eq. 7 sign, Eq. 14 dims, mask definition, defaults, base-class counts, threshold update procedure | R1-ERR-7/9, R4-W2, DA-M8 | Fix notation; add an algorithm table | Low | Yes |
| S4 | Narrow "first" and "outperforms existing FSCIL methods" wording | R2-W1, R4-W1 | Reword | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Imbalanced or revisiting streams | R3-W4 | Small experiment |
| N2 | Table 4 vs 5 mismatch; Table 3 parameter counts | R1-ERR-6/8 | Reconcile |
| N3 | Cross-disciplinary links (homeostatic plasticity, neuromorphic chips) | R3-W5 | Discuss |
| N4 | Typos | R4 | Fix |

## Estimated Revision Effort
- Priority 1: 5 items, about 3–5 weeks (mostly re-running baselines and an eight-way ablation).
- Priority 2: 4 items, about 3–5 days.
- Priority 3: 4 items.
- **Total estimated revision time**: about 4–6 weeks.

*Journal-style mapping is not required (conference target).*
