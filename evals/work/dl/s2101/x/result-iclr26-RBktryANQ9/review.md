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

---

# Phase 1.5: Literature Check and Domain Reviewer Addendum (Prof. Xiulan Qiao)

*Mode: strict (cutoff 2025-09-24), arXiv API through `related_search.py`. 9 of 12 queries used: 7 claim, 1 baseline, 1 expansion; no refused queries; `coverage` reports no gaps; `similarity` run on the reviewer copy. Search covers arXiv only. No search used the paper's title, authors or method names. Sources are labelled as the script returned them.*

## Per-claim novelty (claim-level profile, `related_search.py novelty`)

| Claim | Dimension | Novelty | Top prior work (level, label, cited by paper?) | Reasoning |
|-------|-----------|---------|--------------------------------------------------|-----------|
| C1 offline dataset distillation as noise removal avoiding the feedback loop | method | **medium** | Coresets for Robust Training of Neural Networks against Noisy Labels (level 3, prior peer-reviewed, NeurIPS 2020, https://arxiv.org/abs/2011.07451v1), not cited | It also trains on a small, clean-ish selected subset to avoid memorising noise, with theory; the mechanism differs (selection vs synthesis). No search result applies dataset distillation to noisy labels ("no close prior work found in 9 queries, arXiv only"; a limit of the search, not proof of novelty). |
| C1b strong privacy through offline distillation | result | medium | A Comprehensive Study on Dataset Distillation: Performance, Privacy, Robustness and Fairness (level 3, prior arXiv-only, https://arxiv.org/abs/2305.03355v3), not cited | Its abstract reports that membership-inference attacks show that privacy risks remain for distilled data, which bears directly on a "strong privacy" claim. |
| C2 distillers denoise symmetric and natural noise | result | medium | Coresets (as above, level 3) | Same goal and CIFAR-10 80% noise setting; the paper does not compare to it. |
| C3 structured noise absorbed; tail classes lost | result | **incremental** | Distilling Long-tailed Datasets (level 4, prior peer-reviewed, CVPR 2025, https://arxiv.org/abs/2408.14506v2), not cited | Its abstract says that existing distillation methods struggle on long-tailed data through biased gradients and poor experts on tail classes, so the tail-class hypothesis in Insight-II is already studied. |

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
| CIFAR-10, 80% symmetric noise | Coresets… (https://arxiv.org/abs/2011.07451v1, prior peer-reviewed) | a roughly 6% accuracy gain on CIFAR-10 with 80% noisy labels over the then state of the art (relative to other methods; not an absolute number) | No | not tabulated (figures only) | Settings differ (ResNet vs ConvNet); a question, not an under-reported baseline. A missing-baseline MAJOR at most. |

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
