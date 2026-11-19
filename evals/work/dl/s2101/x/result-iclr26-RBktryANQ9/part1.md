# Academic Paper Review: "Dataset Distillers Are Good Label Denoisers In the Wild"

*Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Simulation of a review panel, not a prediction. All five reviewer passes and the EIC share one model context; they are role-based passes, not independent agents.*

*Figures were not available (text extraction only). All empirical evidence in this paper is in Figures 2, 4 and 5 (curves) and Figure 3 (images). I judged them from captions and the surrounding text only. Where a point depends on a curve I say so.*

---

## 📋 Phase 0: Paper Analysis

| Item | Finding |
|------|---------|
| Title | Dataset Distillers Are Good Label Denoisers In the Wild |
| Primary Discipline | Machine learning → learning with noisy labels |
| Secondary Discipline(s) | Dataset distillation / condensation; data-centric ML; privacy-preserving learning |
| Paper Type | Analysis / insight (empirical study of three existing methods; composite weights: analysis) |
| Core Technique(s) | Trajectory-matching (DATM), distribution-matching (DANCE) and implicit-gradient meta-learning (RCIG) dataset distillation, applied to label-noise benchmarks |
| Target Venue | ICLR (stated by the user); profile key `iclr` |
| Venue-Specific Notes | none. ICLR 2026 pool: ≈27% accepted; Soundness / Presentation / Contribution (1–4), rating on {0,2,4,6,8,10} |
| Paper Maturity | Early draft / workshop-level study (11 pages incl. references, no appendix, no tables) |
| Ethics-Relevant Content | none directly; the paper asserts strong privacy protection (Abstract) without studying it |
| Integrity scan | `integrity_scan.py`: no reviewer-directed text or hidden characters found. Author names and affiliations are visible in the extracted text and were ignored. |

### Claimed Contributions (as stated by the authors)
1. **C1** A new perspective on learning from noisy data via offline dataset distillation that "avoids the issue of vicious cycles" and "improves training efficiency and provides strong privacy" (Abstract; Sec. 1, contribution 1; Sec. 5).
2. **C2** Dataset distillers serve as effective label denoisers under random noise, and this also holds for natural noise (Sec. 1, contribution 2; Observation-I, Observation-III; Figs. 2, 5).
3. **C3** Pitfalls: structured asymmetric noise is absorbed into the distilled samples, and clean hard samples such as tail-class data in imbalanced datasets "are at risk of being lossy" compressed (Sec. 1, contribution 3; Observation-II; Insight-II; Fig. 4).
4. **C4** (implicit) Corollary-I (Eq. 10) and Corollary-II (Eq. 11): a bound on the IPC needed to preserve clean information and a probabilistic bound on the noise rate inferred from distillation accuracy (Sec. 4).

### Paper memory (shared factual record)
- **Data:** CIFAR-10, CIFAR-100, Tiny-ImageNet with synthetic symmetric noise (Eq. 1; τ = 0.2, 0.4, 0.6, 0.8, Sec. 4 Experiment-I); asymmetric noise on CIFAR-10/100 only (Sec. 4 Implementations, Experiment-II); CIFAR-10N (Aggre 9.03%, Random ≈18%, Worst 40.21%) and CIFAR-100N fine (40.20%) (Sec. 4 Experiment-III). Clothing1M and WebVision are described (Sec. 3.1) but not used.
- **Model / method:** 3-layer ConvNet (CIFAR), 4-layer ConvNet (Tiny-ImageNet) (Sec. 4); DATM (accelerated variant of [9]), DANCE, RCIG, following the evaluation protocols of those three methods, augmentation for RCIG (Sec. 4). Baseline: "training on the full dataset" with cross-entropy (Sec. 4 Experiment-I, dashed lines in Figs. 2, 4, 5).
- **Not stated after search:** train/validation/test split and which split is reported; how checkpoints or IPC points were chosen; seeds, number of runs, variance; hyperparameters of the distillers; how real images/labels initialise the synthetic set; whether learned soft labels are used; expert-trajectory training on noisy data; compute or GPU-hours; code; baseline training epochs and whether the baseline is reported at best or final epoch.
- **Headline numbers:** none in the abstract. Text numbers: "fewer than 50 samples per class" beat the baseline at τ = 0.2; one distilled sample per class beats the baseline at τ = 0.6 and 0.8 (Sec. 4 Observation-I); fewer than 10 distilled images per class beat the CIFAR-100N baseline (Sec. 4 Observation-III).
- **Appendix / supplement:** none. **Unverifiable:** all curves and images (Figs. 2–5).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Halvard Lindqvist, ML group, large public research university (Northern Europe)
- **Seniority / Expertise**: senior faculty / learning theory, generalization and data-centric ML
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Calibrated to what ICLR accepts; discounts points the paper already answers.

### Reviewer 1 (Methodology): Dr. Anjali Deshmukh-Rao, industrial research lab (South Asia)
- **Seniority / Expertise**: mid-career industry scientist / label-noise benchmarks, evaluation protocols for small-scale vision
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched controls and stated selection protocols.

### Reviewer 2 (Domain): Prof. Xiulan Qiao, vision & learning group, large public research university (East Asia)
- **Seniority / Expertise**: senior faculty / dataset distillation and condensation; learning with noisy labels
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks each cited method against what it actually does.

### Reviewer 3 (Perspective): Dr. Camila Ferreira-Nunez, privacy and data-centric ML institute (South America)
- **Seniority / Expertise**: mid-career researcher / privacy attacks on synthetic data, coreset selection, robust statistics
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for what the idea could become.

### Reviewer 4 (Generalist): Dr. Rafiq Haddad, mid-size university (Middle East)
- **Seniority / Expertise**: postdoc / deep learning for vision, not label noise or distillation specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; reads for the one-paragraph takeaway.

### Devil's Advocate: Prof. Elena Marchetti-Brandt, university statistics and ML department (North America)
- **Seniority / Expertise**: senior faculty / evaluation methodology, causal attribution in ablations
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, asks "what else explains this curve?"

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reports

# Peer Review Report

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Reviewer: Dr. Anjali Deshmukh-Rao, Methodology (industrial research lab, South Asia; fictional persona)
## Expertise: label-noise benchmarks; evaluation protocols for small-scale vision; reproducibility
## Date: 2026-11-10

## Summary
The paper applies three existing dataset-distillation methods (DATM, DANCE, RCIG) to CIFAR-10/100 and Tiny-ImageNet with synthetic symmetric and asymmetric label noise, and to CIFAR-N human noise. It compares test accuracy of ConvNets trained on small distilled sets (varying images per class, IPC) with a ConvNet trained on the full noisy set. It concludes that distillation helps under symmetric noise and often under natural noise, fails to filter structured asymmetric noise, and may lose hard clean samples. Two "corollaries" (Eqs. 10–11) relate IPC to noise rate. All evidence is in curves (Figs. 2, 4, 5), which I could not see; I read captions and text.

## Strengths
### S1: A clear, testable hypothesis with a sensible first design
Sec. 1 and Sec. 3.2 state the idea that distillation keeps "common patterns" and drops noise. Sec. 4 tests it across three distillation families (parameter, distribution, meta-learning matching) and three noise types, so the finding does not rest on a single distiller.
### S2: Honest reporting of a negative case
Experiment-II / Observation-II (Fig. 4, Sec. 4) report that most distillers do worse on asymmetric-noise data than the full-data baseline, and that only DATM matches the baseline at τ = {0.2, 0.4}. Reporting the failure mode is valuable.
### S3: Noise models are standard and defined
Eqs. 1–2 define symmetric and asymmetric noise; the CIFAR-10 class flips (TRUCK→AUTOMOBILE, BIRD→AIRPLANE, DEER→HORSE, CAT↔DOG) and the CIFAR-100 superclass flips are given (Sec. 4 Implementations). The CIFAR-N rates (Aggre 9.03%, Worst 40.21%) are stated.

## Weaknesses
### W1: The denoising attribution is not isolated: no control separates "distillation" from "training on a small set / early in training"
The only comparison in Figs. 2, 4, 5 is the dashed line "training on the full dataset" with cross-entropy (Sec. 4 Experiment-I). A ConvNet trained to convergence on 80% symmetric noise memorises noise (the paper itself says so in Sec. 3.1 *Remark*: networks "first memorize" common patterns and only then hard samples such as noisy labels). Any small subset, early-stopped training, or learned soft labels could beat that line. DATM, per the paper's own Sec. 2.2 description, matches early trajectories for small sets, which acts like early stopping. Without (a) a random subset of the noisy data at the same IPC, (b) an early-stopped full-data baseline, and (c) a small-loss / coreset selection baseline, the conclusion "dataset distillers serve as effective label denoisers" (Sec. 1, contribution 2) is not established.
- **Suggested Fix**: add random-subset, early-stopped (best-epoch and last-epoch), and small-loss selection controls at the same IPC for all noise settings. Cost: small ConvNets, roughly 20–40 GPU-hours total.
### W2: The baseline is weak and no label-noise method is compared, yet the paper claims promise for robust model training
The paper cites DivideMix [24], Co-teaching [14], DISC [28] and others (Sec. 2.1, Sec. 1) but compares with none; the baseline is a 3-layer ConvNet with plain CE. A comparison to even one standard robust-loss or sample-selection method with the same ConvNet is the minimum to support "effective denoising tools" (Insight-I) and the Conclusion (Sec. 5).
- **Suggested Fix**: add GCE [55], Co-teaching [14] and DivideMix [24] (or ELR-style early-learning regularisation) on the same ConvNet and noise settings, and report them next to the distillers.
### W3: The evaluation protocol is not stated, and wording hints that the reported split and checkpoint may be test-selected
After a protocol sweep (terms: test, validation, select, best, checkpoint, seed, tuning, epoch) the paper says only that performance is "evaluated based on test accuracy" on distilled datasets, following the protocols of DATM, DANCE and RCIG, and that "Final test accuracies are" reported throughout the distillation process (Sec. 4 Implementations). Figure 2 and 4 captions say "validation performance", and Corollary-II says "validation accuracy matches that of the original" dataset (Eq. 11 paragraph). It is not stated whether there is a validation split, whether the curves are best-over-checkpoints or final, or whether the full-data baseline is reported at the same kind of checkpoint. CIFAR has no separate validation split, and its test labels are public, so a best-checkpoint number would be selection on the test set (the distiller literature commonly does this). If the distiller points are best-over-checkpoint and the baseline is last-epoch (post-memorisation), the gap is inflated by the protocol.
- **Suggested Fix**: state splits and the checkpoint rule; hold out a validation split from the training set for checkpoint choice; report baseline at last epoch and at best-validation epoch.
### W4: No variance, seeds, hyperparameters or implementation details, on CIFAR-scale experiments
Not stated after search: seeds, repeats, error bars, distiller hyperparameters, synthetic-set initialisation (real noisy images? noise?), whether DATM's learned soft labels are used (soft labels can themselves denoise), how experts are trained on noisy data, compute. At CIFAR scale, ≥3 seeds is the field norm (`statistical_reporting_standards.md`). Several claims are about crossing points (at a noise rate of 0.2, "fewer than 50 samples per class" are said to "significantly outperform" the baseline, Sec. 4 Observation-I), and "significantly" is used without a test.
- **Suggested Fix**: 3 seeds × 3 distillers × 3 datasets with mean ± std; a hyperparameter table; release code. Cost: DATM/RCIG on CIFAR-100 and Tiny-ImageNet dominate, on the order of 100–200 GPU-hours.
### W5: Secondary claims (efficiency, privacy, Corollaries) have no supporting experiment, and the Corollaries are internally inconsistent (see Error Log)
The efficiency claim ("improves training efficiency and provides strong privacy", Sec. 1 contribution 1; also the Abstract) has no timing; Sec. 3.2 defines the experts as trained on real images (the full noisy data), so the pipeline costs more than training once. The privacy claim has no analysis. Eq. 10 and Eq. 11 have no derivation, δ is undefined, and their inequality directions are opposed.
- **Suggested Fix**: either remove these claims or add measured distillation + training cost, a membership-inference test on the distilled sets, and proofs or empirical checks of Eqs. 10–11.
### W6: Scope does not match "In the Wild"
Natural noise is only CIFAR-N (human relabelling of CIFAR), no Clothing1M or WebVision though Sec. 3.1 introduces them; asymmetric noise is not run on Tiny-ImageNet; no imbalanced dataset is run although it is claimed as a finding (see Error Log).
- **Suggested Fix**: narrow the title and claims, or add one real-noise benchmark at feasible IPC.

**Minor:** "Realted Works" (Sec. 2 heading); Eq. 4 uses θ̂_{t+N} while the text defines θ̂_{t+T}; τ denotes the noise rate (Eq. 1) and the RCIG temperature ("is the learnable" temperature, Eq. 8 text); ConvNet cited to [40] (Sagun et al., a Hessian paper) rather than the usual ConvNet source; figures say "validation" where the text says "test".

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E2/E6 | Eq. 10 vs Eq. 11, Sec. 4 | "IPC ≤ |S̃|·(1−τ)/C" ; "τ ≥ (1 − C·IPC/|S̃|)" | Eq. 11 rearranges to IPC ≥ |S̃|(1−τ)/C, the opposite direction of Eq. 10. Literal use is also absurd: CIFAR-10 (|S̃| = 50,000, C = 10), IPC = 50 gives τ ≥ 0.99, yet the text says IPC < 50 already beats the baseline at τ = 0.2 | Algebra; numeric substitution (dataset size is the standard CIFAR-10 training size, not printed in the paper) | High (algebra), Medium (intended reading) | MAJOR | Give derivations, define δ and "matches the original dataset", test on the existing curves |
| ERR-2 | E5 | Abstract, Sec. 1 contribution 3, Sec. 4 Insight-II, Sec. 5 | "further hypothesize that challenging clean samples" | The abstract and conclusion state tail-class loss as a finding; Sec. 4 calls it a hypothesis and no imbalanced dataset is run | Cross-referenced Sec. 4 Experiments I–III (CIFAR-10/100, Tiny-ImageNet, CIFAR-N only) | High | MAJOR | Run CIFAR-LT or reword as hypothesis |
| ERR-3 | E5 | Abstract, Sec. 1, Sec. 5 vs Sec. 3.2 | "improves training efficiency and provides strong privacy" | No cost measurement anywhere; Sec. 3.2 says experts are trained on real images, so distillation adds cost | Full-text search for time/GPU/hours: none | High | MAJOR | Report distillation + training cost against full training |
| ERR-4 | E5 | Sec. 4 Insight-III vs Observation-III vs Sec. 5 | "remain largely effective even in the presence" | Observation-III itself says "like Aggre, these distillation approaches struggle to" perform well | Cross-referenced two sentences in Sec. 4 | High | MAJOR | State the noise-rate range where it works |

## Claim-to-Evidence Map
| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|-------------|---------------------|---------|
| C1a | Avoids "vicious cycles" | Abstract, Sec. 1 | None tested; Insight-I and Sec. 1 admit "how much data should be distilled" is open, i.e. a noise-level dependence remains | Unsupported |
| C1b | Improves efficiency; strong privacy | Abstract, Sec. 5 | None | Unsupported |
| C2a | Effective denoiser for symmetric noise | Obs-I, Fig. 2 | Curves vs weak CE baseline only (caption-level) | Partially (confounded) |
| C2b | Holds for natural noise | Obs-III, Fig. 5 | CIFAR-N Worst/100N only; fails on Aggre | Partially |
| C3a | Asymmetric noise absorbed | Obs-II, Fig. 4 | Curves below baseline except DATM at τ ≤ 0.4 | Supported (caption-level) |
| C3b | Tail classes lossy | Abstract, Insight-II | No experiment | Unsupported |
| C4 | Eq. 10, Eq. 11 | Sec. 4 | No proof, no test | Unsupported / inconsistent |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Missing controls and protocol; Corollaries inconsistent |
| Clarity | 2 | Readable, but protocol and Corollaries unclear |
| Significance | 2 | Idea of interest, evidence too weak to change practice |
| Originality | 2 | New angle on an existing pair of topics; no new method |

## Dimension Scores (0–100)
**Pool position:** better than about 20% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline claim is tested only against a plain CE baseline with no random-subset, early-stopping or noisy-label-method control, and no variance or protocol is given.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | Confounded attribution; inconsistent Corollaries |
| Clarity & Presentation | 52 | Developing | Understandable; protocol and notation gaps |
| Novelty & Originality | 48 | Developing | Fresh framing, no new method or tool |
| Significance & Impact | 42 | Developing | Limited by weak baselines and ConvNet/CIFAR scale |
| Experimental Validation | 35 | Developing | No controls, variance, or LNL baselines |
| Reproducibility | 32 | Developing | No hyperparameters, seeds, code, compute |
| Ethical Compliance | 55 | Competent | Nothing at stake; unexamined privacy claim and no limitations section |

## Questions for Authors
1. Are the plotted points the final or best-over-checkpoint test accuracies, and is the full-data baseline reported at the same kind of checkpoint? (A best-vs-final mismatch would lower my score; a validation-split protocol would raise it.)
2. How does a random subset of the noisy data at the same IPC, and an early-stopped full-data model, perform in Fig. 2? (If they match the distillers, the central claim fails.)
3. Does DATM's learned soft label account for the denoising? (An ablation with hard labels would be informative.)
4. In Observation-III, the "Worst" scenario is CIFAR-10N but the comparison is to "the CIFAR100N baseline": which datasets does this refer to?
5. How many seeds underlie each curve?

## Limitations Assessment
**Partially.** Sec. 4 Insight-II and Sec. 5 acknowledge structured noise and hard samples, but there is no discussion of the baseline's weakness, of scale (ConvNet/CIFAR), of the cost of distillation, or of the untested privacy claim.

## Ethics Review Flag
**No**

## Overall Score
**2**: The question is interesting, but the central claim is not isolated from simpler explanations, the protocol and variance are missing, and several abstract claims have no evidence.

## Confidence
**4**: I read all text and checked the protocol with text search; I could not see the curves.

---

# Peer Review Report

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Reviewer: Prof. Xiulan Qiao, Domain (vision & learning group, large public research university, East Asia; fictional persona)
## Expertise: dataset distillation and condensation; learning with noisy labels
## Date: 2026-11-10

## Summary
The paper proposes using dataset distillation as an offline pre-processing step to obtain a small, clean-ish synthetic set for training under label noise, arguing it avoids the "vicious cycle" of noise estimation and re-labelling. It benchmarks three distillers on synthetic and human label noise and reports that they help for random noise, struggle with structured noise, and may compress hard samples lossily. It adds two probabilistic-looking corollaries that link IPC and noise rate.

## Strengths
### S1: The connection is intuitive and potentially useful
Linking the "common patterns first, noise later" memorisation account (Sec. 3.1 *Remark*, citing [1, 14, 15, 25, 47, 53]) to what distillation preserves is a reasonable hypothesis and links two communities.
### S2: Distiller selection spans the standard families
Sec. 3.2 picks one method each from parameter matching (DATM [13]), distribution matching (DANCE [54]) and meta-learning (RCIG [32]), and the descriptions in Sec. 3.2 and 2.2 are broadly accurate (e.g., DATM aligns trajectories and sets size by difficulty).
### S3: The asymmetric-noise analysis is mechanistically sensible
Sec. 4 Experiment-II explains why a distribution-matching objective carries class-conditional flips into the distilled set (the distilled labels keep the same transition pattern). It matches what a class-conditional matching objective should do, and it names the limit of the idea.

## Weaknesses
### W1: Related work does not position the contribution against the closest literatures
Sec. 2 lists noisy-label methods and distillation methods separately. It does not discuss (i) prior work that applies dataset distillation/condensation to noisy or corrupted data, (ii) coreset or sample-selection methods for noisy labels, which pursue the same "small clean-ish subset" goal that Sec. 1 *Motivation* describes, or (iii) work on privacy properties of condensed data (the basis of the privacy claim). The gap the paper fills ("a new perspective") cannot be judged. See literature-check addendum.
- **Suggested Fix**: add a paragraph and a comparison to coreset/selection methods under label noise, and to any distillation-under-noise work.
### W2: The stated contribution is a framing, and the framing is only partly new in kind
No new method, objective or algorithm is proposed; the contribution is an empirical observation that existing distillers behave differently under three noise types. That kind of analysis can be valuable, but the paper must then be held to the bar of a thorough analysis (controls, scale, variance), which it does not reach (see R1).
- **Suggested Fix**: frame as an analysis paper and add mechanism-isolating experiments (soft labels vs images, early trajectories vs full trajectories).
### W3: The "vicious cycle" argument is motivated rhetorically and the new approach reintroduces a noise-level dependence
Sec. 1 *Status Quo* argues that noise evaluation and strategy are causally entangled. But Sec. 1 *Empirical Insights* says the relationship between the amount of data to be distilled and the level of noise "remains an open question", and Insight-I asks "How much data should be distilled" from a noisy set, i.e. choosing IPC needs the noise level, which is what existing pipelines estimate. Insight-III also says that distillation "often yields suboptimal results in low-noise" settings. So the approach does not remove the need for a noise estimate; it moves it.
- **Suggested Fix**: show a noise-level-agnostic IPC selection rule, or drop the claim.
### W4: Prior-work descriptions and one citation need checking
Sec. 2.1 cites [29] (an adaptive early-learning correction for *segmentation*) and [52] (biased complementary labels) for classification noise-handling families; [40] (a Hessian analysis) is cited as the ConvNet architecture. These are weak or loose fits for the claims they support (Sec. 1 first paragraph, Sec. 2.1, Sec. 4 Implementations).
- **Suggested Fix**: use the standard source for each (ELR-type early-learning regularisation for correction; the usual ConvNet source for [40]).
### W5: Claims about distillation's mechanism are asserted, not shown
The mechanism in Insight-I (distillation captures common patterns and ignores outliers such as noise) is asserted. The visual evidence is one image per class (Fig. 3, caption). A quantitative check (fraction of synthetic images whose nearest real neighbour is mislabelled, label consistency of distilled data) would test it.
- **Suggested Fix**: add one mechanism diagnostic per distiller.

**Minor:** "Realted Works"; the contribution list uses footnotes 1–2 to carry caveats ("for now, we will set aside the potential role of slight noise perturbations") that belong in the text.

## Missing References
*See the literature-check addendum below, produced by `related_search.py` and verified; entries are only listed there.*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Analysis lacks mechanism-isolating controls |
| Clarity | 3 | Mostly clear |
| Significance | 2 | Limited without stronger evidence |
| Originality | 2 | New framing, no new technique |

## Dimension Scores (0–100)
**Pool position:** better than about 28% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is a framing plus a small empirical study against a weak baseline, with no positioning against coreset or noisy-label methods.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Claims outrun evidence; Corollaries unproven |
| Clarity & Presentation | 55 | Competent | Clear narrative; positioning thin |
| Novelty & Originality | 50 | Developing | Interesting link; limited new content |
| Significance & Impact | 45 | Developing | Niche without stronger baselines |
| Experimental Validation | 40 | Developing | Three distillers, one weak baseline |
| Reproducibility | 38 | Developing | Hyperparameters and code missing |
| Ethical Compliance | 55 | Competent | Limitations partly discussed |

## Questions for Authors
1. Which prior work, if any, applies dataset distillation or condensation to noisy labels, and how does this study differ? (A clear delta would raise Originality.)
2. How would one choose IPC without knowing τ? (A workable rule would raise my Significance score.)
3. How does a coreset/small-loss selection baseline at the same size compare?

## Limitations Assessment
**Partially.** Failure modes are discussed (Insight-II), but not scale limits of distillation (the paper notes DATM's "scalability challenges on large-scale, real-world datasets like ImageNet", Sec. 3.2) which directly constrain the "in the wild" claim.

## Ethics Review Flag
**No**

## Overall Score
**2**: Reasonable idea, thin positioning and thin evidence; below the ICLR bar in its present form.

## Confidence
**3**: I know both literatures but the literature check and the missing figures limit my certainty.

---

# Peer Review Report

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Reviewer: Dr. Camila Ferreira-Nunez, Perspective (privacy and data-centric ML institute, South America; fictional persona)
## Expertise: privacy attacks on synthetic data; coreset selection; robust statistics
## Date: 2026-11-10

## Summary
The paper suggests that compressing a noisy dataset into a few synthetic images can act as a denoiser, with side benefits of efficiency and privacy. It runs three distillation methods under three kinds of label noise and reports where this works (random noise, high human-noise rates) and where it does not (structured noise, low noise rates).

## Strengths
### S1: An appealing data-centric angle
Treating the training set as an object to be transformed offline, before any model sees it (Sec. 1, *Motivation*), fits data-centric ML and could matter when the raw data cannot be shared.
### S2: The negative result on structured noise is practically important
Real annotation errors are often class-conditional; Experiment-II (Sec. 4) says distillation absorbs them. That is a useful warning for anyone considering the approach.
### S3: Natural-noise rates are used sensibly
Using CIFAR-N Worst/Aggre/Random (Sec. 4 Experiment-III) gives a range of noise rates (9–40%) and shows the technique's dependence on rate. This is the right kind of sweep.

## Weaknesses
### W1: The privacy claim is the headline application but is never examined
The Abstract claims strong privacy protection through offline processing, Sec. 1 contribution 1 says distillation "provides strong privacy", and the Conclusion points to "high-privacy environments". No threat model, membership-inference test, or comparison with differentially private alternatives is given. Distilled images are optimised against the real images; whether they leak training samples is an empirical question that the paper does not ask. "Offline" only removes the need to ship data during training; the distilling party still sees all noisy and private data.
- **Suggested Fix**: add a threat model and a membership-inference or reconstruction test on the distilled sets, or drop the privacy claim from Abstract and contributions.
### W2: Deployment realism: distillation cost, scale and the need to know the noise rate
Sec. 3.2 notes DATM's "scalability challenges" on large-scale real-world datasets like ImageNet. Real noisy corpora (web-scale) are far beyond ConvNet/CIFAR scale. Choosing IPC needs the noise rate (Insight-I, Insight-III); in practice the noise rate is unknown. The paper does not discuss cost or practical selection of IPC.
- **Suggested Fix**: report distillation wall-clock and memory, and propose or test an IPC rule that works without knowing τ (e.g., a clean validation subset).
### W3: Cross-disciplinary context is missing
The idea resembles coreset selection, robust statistics (trimmed estimators), and early-learning regularisation: each already offers "keep what is consistent, drop the rest". Positioning against them would show what distillation adds beyond them.
- **Suggested Fix**: add a short comparison with selection-based coresets under noise, and with early-learning-based correction methods.
### W4: Assumption audit: the three working assumptions are not all supported
(i) Sec. 1 says real-world "data noise is" "largely random", which conflicts with Sec. 4 Experiment-II: "label corruption tends to occur" primarily among visually similar classes. (ii) Clean data is the "common" mode (Sec. 3.1 Remark), which fails when a minority class is rare, as the authors acknowledge for tail classes without testing it. (iii) A class-balanced dataset is assumed in Corollary-I.
- **Suggested Fix**: reconcile (i) in the Introduction, test (ii) with an imbalanced set, and state (iii) as a limitation.

**Minor:** The paper has no explicit Limitations or Broader Impact section.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thin for the claims |
| Clarity | 3 | Readable |
| Significance | 2 | Potential, not demonstrated |
| Originality | 3 | Fresh angle |

## Dimension Scores (0–100)
**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an interesting practical idea with honest failure cases, but the application claims (privacy, efficiency, in the wild) are untested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 45 | Developing | Claims untested |
| Clarity & Presentation | 58 | Competent | Easy to follow |
| Novelty & Originality | 55 | Competent | Fresh cross-community angle |
| Significance & Impact | 50 | Developing | Real question; limited demonstrated impact |
| Experimental Validation | 42 | Developing | Narrow scale, weak baseline |
| Reproducibility | 40 | Developing | Details missing |
| Ethical Compliance | 50 | Developing | Privacy asserted without analysis; no limitations section |

## Questions for Authors
1. What attacker model underlies the claimed strong privacy protection? (A membership-inference result would raise Significance and Ethics.)
2. How would a practitioner choose IPC when τ is unknown?
3. How does the finding change for imbalanced data, which you flag as a risk?

## Limitations Assessment
**Partially.** Failure modes are discussed; scale, cost and the privacy assumption are not.

## Ethics Review Flag
**No**: no data or deployment concern, but an unsupported privacy claim.

## Overall Score
**3**: A promising angle with honest negative findings, but the application claims are unexamined and the evidence base is small.

## Confidence
**3**: Privacy and coresets are my area; label-noise benchmarks less so.

---

# Peer Review Report

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Reviewer: Dr. Rafiq Haddad, Generalist (mid-size university, Middle East; fictional persona)
## Expertise: deep learning for vision (broad area, not label noise or distillation specifically)
## Date: 2026-11-10

## Summary
The paper asks whether dataset distillation, which compresses a dataset into a few synthetic images, also removes label noise. Three distillers are tried on CIFAR-10/100 and Tiny-ImageNet with symmetric, asymmetric and human noise. Distillation helps under random noise and high human noise rates, but not with structured noise. The authors present this as a new perspective on noisy-label learning with privacy and efficiency benefits.

## Strengths
### S1: A one-sentence takeaway a PC member remembers
The takeaway that distillation can denoise random label noise but absorbs structured noise (Sec. 1 Empirical Insights, Insights I–III) is crisp and memorable.
### S2: Well-organised short paper
Sec. 3 sets out noise types and distillers, Sec. 4 pairs each experiment with an Observation and an Insight, making the claim-evidence chain easy to follow.
### S3: Balanced reporting
The paper states where the idea works, where it fails (Observation-II, Insight-III low-noise), and calls for future work, rather than a uniform success story.

## Weaknesses
### W1: Evidence does not match the headline ("Good Label Denoisers In the Wild")
Experiments are CIFAR/Tiny-ImageNet with a ConvNet and a plain CE baseline; the only human noise is CIFAR-N. Observation-III reports that distillation approaches "struggle to" perform at Aggre (9%), and Observation-II that they fail under asymmetric noise, which the paper says is the typical real-world pattern (Sec. 4, Experiment-II: "label corruption tends to occur" among similar classes). The title and abstract should be narrowed ("random noise at moderate-to-high rates on small benchmarks").
- **Suggested Fix**: retitle and rewrite the abstract so every sentence maps to a figure.
### W2: Evaluation is thin for ICLR: a single baseline type, no variance, no stated protocol
Beyond what Reviewer 1 details, as a PC member I would expect at least one noisy-label method as a comparison, and error bars. Without them I cannot judge whether the curve crossings in Figs. 2, 4 and 5 are meaningful.
- **Suggested Fix**: add one robust-learning baseline and 3 seeds.
### W3: Clarity of the theoretical part
Corollaries I and II (Sec. 4) have no preceding theorem or proof, use "δ" without definition, and read as opposite inequalities (Eq. 10: IPC ≤ …; Eq. 11 implies IPC ≥ …). A reader cannot tell what is claimed or how it was checked against the experiments.
- **Suggested Fix**: either prove and test them, or relabel as heuristics with a worked example.
### W4: Presentation details hide the setup
Footnotes in the contributions list carry key caveats; Fig. 2/4 captions say "validation", the text says "test"; hyperparameters are absent.

**Minor:** "Realted Works"; symbol τ overloaded (noise rate vs RCIG temperature, Eq. 8); Eq. 4 notation (N vs T).

### Venue Criteria Checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported by evidence | Not met | Abstract vs Sec. 4 (efficiency, privacy, tail classes unsupported) |
| Soundness: fair, controlled comparison | Not met | Figs. 2, 4, 5 dashed baseline only |
| Presentation: self-contained, protocol clear | Partly | Sec. 4 Implementations |
| Contribution: a finding the field lacked | Partly | Observations I–III |
| Contribution: significance for the community | Partly | Sec. 5 |
| Honest limitations | Partly | Insight-II |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims outrun controls |
| Clarity | 3 | Clear narrative |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Framing only |

## Dimension Scores (0–100)
**Pool position:** better than about 27% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: claims in the title and abstract exceed what small ConvNet/CIFAR curves against a CE baseline can show.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Corollaries unclear; confounds |
| Clarity & Presentation | 58 | Competent | Clear narrative, setup hidden |
| Novelty & Originality | 50 | Developing | New framing |
| Significance & Impact | 45 | Developing | Narrow |
| Experimental Validation | 38 | Developing | One baseline type, no variance |
| Reproducibility | 38 | Developing | Details missing |
| Ethical Compliance | 52 | Developing | Privacy asserted only |

## Questions for Authors
1. Which of the three distillers would you recommend, and at what IPC, for a practitioner with a 20% noisy dataset? (A concrete, validated recipe would raise my rating.)
2. Can the title and abstract be restricted to what Figs. 2, 4 and 5 show?
3. What is the role of Corollaries I and II in the experiments?

## Limitations Assessment
**Partially.** Failure modes are given; scope limits are not.

## Ethics Review Flag
**No**

## Overall Score
**2**: A clear, interesting short study whose claims are broader than its evidence; it needs controls and a narrower framing for ICLR.

## Confidence
**4**: The issues are visible without specialised knowledge; I did not see the figures.

---

# Devil's Advocate Report

## Paper: Dataset Distillers Are Good Label Denoisers In the Wild
## Reviewer: Prof. Elena Marchetti-Brandt, statistics and ML department (North America; fictional persona)

---

## Steelman
Label noise is mostly memorised late in training, while distillation matches early, common structure. Hence compressing a noisy set into a few synthetic samples should discard much of the noise. Figures 2 and 5 are said to show this across three distillers at moderate-to-high noise, and Figure 4 shows the exact condition (structured noise) under which it should fail, which is a sign the effect is real and mechanistically sensible.

---

## Core Argument Chain
1. P1: Networks learn common patterns first and memorise noise later (Sec. 3.1 *Remark*).
2. P2: Dataset distillation synthesises "common patterns shared across the dataset" (Sec. 1 *Motivation*).
3. P3: Distilled-set training beats full-noisy-data training under symmetric noise (Obs-I, Fig. 2) and high human noise (Obs-III, Fig. 5).
4. P4: It fails under structured noise (Obs-II, Fig. 4) because structure is a common pattern.
5. P5: Distillation needs no noise estimate, so it avoids the feedback loop; it is also efficient and private (Abstract, Sec. 1).
∴ "Dataset distillers are good label denoisers in the wild", a promising route for robust training, especially for privacy.

---

## Strongest Counter-Argument
The strongest objection is one of attribution plus relocation. The only comparator in Figs. 2, 4 and 5 is a ConvNet trained on the full noisy set with cross-entropy (Sec. 4 Experiment-I), a model that by the paper's own Sec. 3.1 Remark memorises noise. Any procedure that trains on fewer samples, stops earlier, or uses soft labels would beat it as noise grows; the paper's observation "as noise increases, distillation achieves better performance with fewer distilled samples" (Observation-I) is exactly what an early-stopping or subset effect predicts, since the noisy baseline gets worse while the small-set method is insensitive. The paper never runs a random subset at the same IPC, an early-stopped baseline, or a hard-label ablation, so P3 does not support "denoiser", only "smaller training sets help a weak baseline under heavy noise".

Second, P5 contradicts the paper's own text. The claimed advantage is escaping the loop "evaluate noise → choose strategy". But Sec. 1 admits the amount of data to be distilled versus the noise level "remains an open question", and Insight-III says that in low-noise settings distillation "often yields suboptimal results". So the user must know the noise level to choose whether and how much to distil. Corollary-II tries to infer the noise rate from accuracy, which would restore the very evaluation step the paper says is a vicious cycle, and the inequality as printed (Eq. 11) gives τ ≥ 0.99 for CIFAR-10 at IPC = 50, which cannot be right. Finally, the evidence for the intended "in the wild" use is the weakest: asymmetric noise is, by the paper's own words, the typical form (Sec. 4 Experiment-II: "label corruption tends to occur" among visually similar classes), and that is the case in which the method fails. The title therefore claims the opposite of what Fig. 4 shows for the typical case. The authors can answer by narrowing the claim and adding controls, so this is MAJOR, not CRITICAL.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core finding (distillers help under symmetric noise relative to the paper's baseline, and fail under structured noise) is supported in a weaker form by what is reported; every problem below is fixable by narrowing claims or adding controls, and none meets the strict criteria (no test-selection statement exists in the text, the baseline weakness and missing controls are explicitly MAJOR-or-below by the rules).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (alternative explanation) | Figs. 2, 4, 5; Sec. 4 Exp-I | Only a full-data CE baseline; no random subset, early-stopped, hard-label or noisy-label-method control (Observation-I, where distillation "achieves better performance with fewer distilled" samples as noise grows, is what a subset effect predicts) | Add those four controls at the same IPC |
| DA-M2 | Logic | Sec. 1 *Status Quo* vs *Empirical Insights*; Insight-I; Insight-III; Cor-II | "Avoids the feedback loop" but IPC selection needs the noise level; Cor-II would estimate τ | Remove claim, or show an IPC rule that is noise-agnostic |
| DA-M3 | Scope / claim distortion | Title; Abstract; Sec. 4 Exp-II, Obs-III; Sec. 5 | The title ("In the Wild") and the conclusion that distillation denoises random and natural noise vs failure on asymmetric noise (the paper's own typical case) and on Aggre (9%); only CIFAR-N, no Clothing1M/WebVision | Narrow the title and abstract to small-scale, moderate-to-high symmetric noise |
| DA-M4 | Evidence | Abstract; Sec. 1 contribution 3; Insight-II; Sec. 5 | Tail-class lossy compression stated as a finding; Sec. 4 says "further hypothesize that challenging clean samples"; no imbalanced experiment | Run CIFAR-LT or reword as a hypothesis |
| DA-M5 | Evidence | Abstract; Sec. 1 contribution 1; Sec. 5 | "improves training efficiency and provides strong privacy" without any measurement; experts are trained on real (noisy) data (Sec. 3.2) | Measure cost; add membership-inference test; or drop |
| DA-M6 | Technical | Eq. 10, Eq. 11, Sec. 4 | Opposite inequality directions; undefined δ; no derivation; literal use gives τ ≥ 0.99 at IPC = 50 on CIFAR-10 | Derive and test, or relabel as heuristic |
| DA-M7 | Protocol | Sec. 4 Implementations; Fig. 2/4 captions | Test vs validation naming; "Final test accuracies are" reported throughout distillation; baseline reported at which epoch? Not stated; no seeds or variance | State protocol; validation-based checkpointing; 3 seeds |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Notation | Eq. 1 vs Eq. 8 text | τ is both noise rate and RCIG temperature |
| DA-m2 | Notation | Eq. 4 vs Sec. 3.2 text | θ̂_{t+N} in Eq. 4 vs θ̂_{t+T} in the text |
| DA-m3 | Presentation | Sec. 2 heading; Sec. 1 footnotes | "Realted Works"; caveats hidden in footnotes |
| DA-m4 | Clarity | Sec. 4 Obs-III | Observation-III discusses the "Worst" scenario (CIFAR-10N) yet compares to "the CIFAR100N baseline": dataset ambiguous |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Corollary-I clean images per class, CIFAR-10, τ = 0.8 | not given | 50,000 × 0.2 / 10 = 1,000 (derived; |S̃| not printed in the paper) | n/a |
| Corollary-II bound at CIFAR-10, IPC = 50 | not given | 1 − 10·50/50,000 = 0.99, so "τ ≥ 0.99" | Inconsistent with the stated τ = 0.2 behaviour in Obs-I |
| CIFAR-N rates | Aggre 9.03%, Worst 40.21%, 100N fine 40.20% (Sec. 4 Exp-III) | agree with the CIFAR-N benchmark's published rates [46] as I know them | Consistent |
| Eq. 10 vs Eq. 11 direction | IPC ≤ … vs τ ≥ 1 − C·IPC/|S̃| | Eq. 11 ⇔ IPC ≥ |S̃|(1−τ)/C | Opposite |

No headline percentage appears in the abstract, so no further recomputation was possible; no tables exist.

## Ignored Alternative Explanations
- Training-set size and early stopping (smaller sets limit memorisation).
- Learned soft labels (DATM, RCIG) acting as label smoothing or relabelling.
- Early-trajectory matching in DATM for small IPC acting as an early-learning regulariser.
- Expert-trajectory or kernel quality: experts trained on noisy data are themselves noisy; the paper does not say when they are stopped.
- Baseline reported at last epoch (post-memorisation) vs distilled sets reported at best checkpoint.
- Weak ConvNet capacity changing the noise-memorisation behaviour compared with ResNets used in the noisy-label literature.

## Missing Stakeholder Perspectives
Practitioners with unknown, instance-dependent noise; data owners relying on the privacy claim; anyone with imbalanced data, where the paper itself warns of loss.

## Observations (Non-Defects)
Reporting the failure under asymmetric noise is a strength; the three-family design avoids dependence on one distiller; the explanation of why class-conditional noise is carried over is mechanistically sensible.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 36 | Confounded attribution; inconsistent Corollaries |
| Clarity & Presentation | 50 | Claim-evidence mismatch obscures what was shown |
| Novelty & Originality | 45 | A framing, not a new technique |
| Significance & Impact | 40 | Narrow, weak baseline |
| Experimental Validation | 33 | No controls, variance, or LNL baselines |
| Reproducibility | 32 | Nothing about hyperparameters, seeds, code |
| Ethical Compliance | 48 | Unsupported privacy claim; no limitations section |

**Pool position:** better than about 17% of submissions to ICLR. Deciding evidence: central claim untested against simple controls; several abstract claims have no evidence at all.

## Overall: 2 | Confidence: 4
