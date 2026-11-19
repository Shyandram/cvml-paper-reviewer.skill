# Peer Review: Dataset Distillers Are Good Label Denoisers In the Wild

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | analysis (an empirical study of existing dataset-distillation methods under label noise; no new algorithm is proposed) |
| Field, sub-area | machine learning / computer vision; learning with noisy labels × dataset distillation |
| Task | learning with noisy labels for image classification (adapted from "Image classification, representation learning" and "Robustness, safety, privacy, fairness" in `references/task_neighbors.md`; the task has no row of its own) |
| Neighboring fields | dataset distillation / condensation; data-centric ML: coreset selection and data pruning (added); memorization and early-learning theory (added); privacy-preserving ML (from the robustness/privacy row); large-scale web-supervised training (added); kernel / NTK methods (added, because RCIG uses them) |
| Target venue | ICLR 2026 (as the user stated). The extracted text uses a CVPR-style layout ("Figure 1." captions, numbered references); see R18 |
| Aspect ratio | `aggregate_scores.py ratio --paper-type analysis --venue iclr`: technical rigor 28%, novelty 20%, significance 20%, experimental validation 14%, clarity 10%, reproducibility 5%, ethics 4% |
| Literature check | did not run (no network access in this evaluation). Novelty reasons that rest on memory are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Figures note: only the extracted text was available. Every quantitative result of the paper is in Figures 2, 4 and 5, which are curves (accuracy vs. IPC). The paper has no table. All quantitative claims below are judged from the captions and the prose describing the figures, and this is said wherever it matters.

---

## 1. Paper memory

**Claims.**
- C1: under symmetric noise, existing dataset distillers (DATM, DANCE, RCIG) act as effective label denoisers. The distilled set beats training on the full noisy dataset, and at high noise one image per class suffices: "at noise rates of 0.6 and 0.8, a single distilled sample per class surpasses the baseline" (§4 Experiment-I, Observation-I, Insight-I, Fig. 2).
- C2: structured (asymmetric) noise is absorbed into the distilled samples, and the distillers do worse than full-data training. "Only the DATM method achieves comparable performance to the benchmark at noise rate τ = {0.2, 0.4}" (§4 Experiment-II, Observation-II, Insight-II, Fig. 4, Fig. 1b).
- C3: under natural (human-annotation) noise on CIFAR-10N/100N, the distillers "remain largely effective", especially at high noise rates (Worst), and struggle at low rates (Aggre) (§4 Experiment-III, Observation-III, Insight-III, Fig. 5).
- C4: clean but hard samples, such as tail classes in imbalanced data, undergo lossy compression during distillation (Abstract; Contributions bullet 3; §4: "We further hypothesize that challenging clean samples…"; §5).
- C5: the perspective "avoids the feedback loop common in existing techniques", improves training efficiency, and provides "strong privacy protection through offline processing" (Abstract; §1 Contributions bullet 1; §5).
- C6: Corollary-I (Eq. 10) gives an upper bound on the IPC that preserves clean information under symmetric noise. Corollary-II (Eq. 11) gives a probabilistic lower bound on the noise rate from the IPC at which accuracy matches the original dataset (§4).
- C7 (framing): "we propose a novel approach that leverages dataset distillation for noise removal" (Abstract); "We propose a new approach to model learning from noisy data" (§5); the title says "In the Wild".

**Setup facts.**
- Distillers: DATM (trajectory matching; in its memory-efficient variant from [9], "Benchmark-I referenced later denotes this accelerated version"), DANCE (distribution matching), RCIG (meta-learning with convexified implicit gradients) (§3.2).
- Datasets: CIFAR-10/100 and Tiny-ImageNet with synthetic symmetric and asymmetric noise. Asymmetric flips for CIFAR-10 are TRUCK→AUTOMOBILE, BIRD→AIRPLANE, DEER→HORSE, CAT↔DOG; for CIFAR-100 the flip goes to the next class within the same superclass (§4 Implementations). CIFAR-10N (Aggre τ = 9.03%, Random k τ ≈ 18%, Worst τ = 40.21%) and CIFAR-100N "fine" (40.20%) (§4 Experiment-III). Asymmetric noise is run on CIFAR-10/100 only (Fig. 4).
- Noise rates: symmetric τ ∈ {0.2, 0.4, 0.6, 0.8} (§4); asymmetric rates are not listed beyond {0.2, 0.4} in the text (Fig. 4 caption: "different noisy ratios").
- Architecture: "a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet" for distillation (§4). The architecture, schedule and stopping rule of the full-data baseline: not stated.
- Loss: cross-entropy by default (§4 Experiment-I).
- Evaluation: "test accuracy on distilled datasets, following the evaluation protocols of DATM, DANCE, and RCIG"; "Final test accuracies are reported throughout the distillation process" (§4). Figure captions say "validation performance". A validation split: not stated.
- Seeds, number of runs, variance: not stated after search. Hyperparameters (distillation iterations, learning rates, expert-trajectory epochs, IPC grid): not stated. Compute (hardware, time): not stated. Code availability: not stated. How expert models / trajectories are trained (on the noisy data or not): not stated.
- Appendix or supplement: none in the extracted text. The paper ends at the references (p. 11).

**Headline numbers.** The paper prints no accuracy value anywhere. The only numbers are the noise rates (above) and qualitative IPC thresholds: IPC = 1 beats the baseline at τ = 0.6, 0.8 on CIFAR-10 (Fig. 2a, §4); "fewer than 50 samples per class" beat it at τ = 0.2 (Fig. 2a, §4); "fewer than 10 distilled images per class" beat the CIFAR100N baseline under Worst/fine noise (Fig. 5, §4).

**Could not be read.** Figures 1–5 (only their captions are available; Fig. 1 axis labels appear in fragments). Eqs. 2, 5, 7, 8, 9 and 11 are partly garbled by extraction; their structure is readable enough for the checks made below. These are treated as unverifiable, never as the authors' errors.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | novelty (perspective) | Reframes learning with noisy labels as a data-condensation problem. Instead of detecting the noise first and then discarding, reweighting or relabeling, it synthesizes a small set from the common patterns, which sidesteps the "vicious cycle" of iterative noise estimation. Linking the DD objective to the memorization literature is a clean, disclosed transfer between two fields. | §1 Motivation: "dataset distillation attempts to synthesize common patterns shared across the dataset"; §3.1 Remark: "Why not directly distill a clean subset that enables effective training?" | moderate | R13 and R17 not upheld; the transfer shows something beyond what memorization theory already predicts |
| A2 | empirical breadth | Covers the three main DD families (parameter matching, distribution matching, meta-learning) under three noise types, on three synthetic-noise datasets plus CIFAR-10N/100N. | §3.2 "we select three representative state-of-the-art methods based on their categorization"; §4 Experiments I–III; Figs. 2, 4, 5 | moderate | the protocol is sound (R3, R12) |
| A3 | empirical strength | A striking positive finding: under heavy symmetric noise, one distilled image per class beats training on all 50k noisy images. | §4: "at noise rates of 0.6 and 0.8, a single distilled sample per class surpasses the baseline" (Fig. 2a; figure not seen) | moderate | the full-data baseline is reasonably trained (R2); the reported accuracy is not chosen on the test set (R3) |
| A4 | insight (negative result) | Reports and explains a failure mode honestly: structured asymmetric noise is distilled into the synthetic set, so "common pattern = clean" fails. This qualifies the paper's own thesis. | §4 Observation-II, Insight-II: "it is crucial not to assume that common patterns always reflect clean data"; Fig. 1(b), Fig. 4 | moderate | Fig. 4 shows what the text says (not seen) |
| A5 | empirical strength | Tests real human-annotation noise (CIFAR-10N Aggre/Random/Worst, CIFAR-100N), not only synthetic flips, and reports where it fails (Aggre, low noise). | §4 Experiment-III: "for lower noise ratio like Aggre, these distillation approaches struggle to perform well"; Fig. 5 | moderate | as A3 |
| A6 | clarity | Self-contained background: formal noise models (Eqs. 1–2) and the objectives of the three distillers (Eqs. 4–9), so a reader from noisy-label learning can follow the DD side. | §3.1, §3.2 | weak | — |
| A7 | qualitative evidence | Visualizes DATM's distilled images at τ = 0.0…0.8, one image per class, as evidence that discriminative features survive heavy noise. | Fig. 3 caption; §4: "a single distilled image retains discriminative features despite high noise ratios" (figure not seen) | weak | the images are representative and not curated |
| A8 | significance | Motivates a practical use: offline distillation as a preprocessing step for noisy data in privacy-sensitive settings. | §1: "These methods hold significant potential for application in high-privacy settings where data noise is prevalent" | weak | R7 and R8 not upheld |
| A9 | theory / open question | Poses a concrete open question, how much to distill for a given noise rate, and gives closed-form bounds linking IPC and τ (Corollaries I–II). | §4 Insight-I, Eq. 10, Eq. 11; Fig. 1(a) | weak | the corollaries are correct and consistent with the results (R5) |
| A10 | reproducibility | Follows the original evaluation protocols of DATM, DANCE and RCIG with the standard ConvNet backbones, so the settings are in principle recoverable from those papers. | §4 Implementations: "following the evaluation protocols of DATM, DANCE, and RCIG" | weak | the noisy-data specifics are stated (R14) |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | experimental validation | No learning-with-noisy-labels baseline. The paper presents "a new approach to model learning from noisy data", yet compares only against cross-entropy training on the full noisy set. Co-teaching [14], DivideMix [24], GCE [55], DISC [28] and others are cited in §1–2 and never evaluated. Without them the reader cannot tell whether distillation is competitive as a denoiser, which is the title claim. | Fig. 2 caption: "the horizontal dashed lines … indicate the performance of training on the full dataset at the corresponding noise rate"; §5: "We propose a new approach to model learning from noisy data" | gap | fatal | Add at least 3 standard LNL methods (e.g., Co-teaching, DivideMix, GCE/ELR-style) on the same ConvNet and data; report accuracy and the compute of each. A few GPU-days at CIFAR scale |
| R2 | technical rigor | No control that isolates "denoising" from simple data reduction or regularization. CE on the full noisy data with a small ConvNet memorizes the noise, so any small training set (a random subset of IPC images per class, a coreset, or the same data with early stopping) may also beat it. Without these controls, C1's mechanism ("captures common patterns while ignoring outliers") is not tested. | §4 Experiment-I: "training results after dataset distillation consistently outperform the baseline"; the baseline's schedule and stopping rule are not stated | gap | major | Add random-subset, herding/coreset, early-stopped-CE and clean-subset (oracle) rows at each IPC. Cheap: hours of GPU |
| R3 | technical rigor | Possible selection on the test set. Accuracy is reported "throughout the distillation process", the captions call it "validation performance", and no validation split is defined. If each curve point is the best test accuracy over distillation iterations, selection happens on the test set, which inflates gains most at small IPC. | §4: "Final test accuracies are reported throughout the distillation process."; Fig. 2/4 captions: "The validation performance" | question | fatal | State how the reported checkpoint is chosen; use a held-out validation split carved from the noisy training set (with noisy labels) for selection |
| R4 | technical rigor | The mechanism behind the "denoising" is not analyzed. DATM matches expert trajectories and DANCE uses trained expert encoders (Eqs. 6–7). The paper never says whether the experts are trained on the noisy labels, or for how many epochs. Early-epoch trajectories may carry the early-learning signal before memorization [1, 47], which would make the effect a form of early stopping rather than distillation. This also undercuts the claim that the approach avoids a noise-dependent feedback loop. | §3.2 Eqs. 4, 6, 7; §4 Implementations (no expert-training details) | gap | major | Report the expert-training data and epochs; ablate the matching range (early vs. late trajectories) and experts trained on clean vs. noisy labels |
| R5 | technical rigor | Corollary-II (Eq. 11) is unsupported and contradicted by the paper's own results. It has no proof and no assumptions; the bound τ ≥ 1 − C·IPC/|S̃| contains neither the accuracy condition it is conditioned on nor δ. Applied to the paper's own observations it gives impossible values (computed in P2): with the standard CIFAR-10 training set of 50,000 images (the size is not stated in the paper), IPC = 50 gives τ ≥ 0.99, yet §4 reports that "fewer than 50 samples per class significantly outperform the baseline" at τ = 0.2. For CIFAR-100N (C = 100, IPC = 10) it gives τ ≥ 0.98, against an actual 0.402. Its direction is also the reverse of Eq. 10 rearranged (τ ≤ 1 − C·IPC/|S̃|). | §4 Corollary-II: "we can infer with at least high probability 1 − δ that the noise rate τ of the dataset satisfies"; Eq. 10, Eq. 11; §4 Experiment-I, III | error | major | Remove Corollary-II, or state its assumptions, prove it, and check it against Figs. 2 and 5 |
| R6 | technical rigor | Corollary-I (Eq. 10) is trivial and ill-posed. IPC ≤ \|S̃\|(1 − τ)/C is just the number of clean samples per class, e.g. 4,000 for CIFAR-10 at τ = 0.2 (derived). It says nothing about distillation, and "the maximum number of distilled samples per class … required" mixes an upper bound with a requirement. No proof or assumption is given. | §4 Corollary-I, Eq. 10 | judgment | minor | Present it as a counting remark, or replace it with an analysis that predicts the IPC thresholds seen in Fig. 2 |
| R7 | significance / ethics | "Strong privacy protection" is claimed but never measured. There is no membership-inference test, no differential-privacy analysis and no discussion of the contested privacy of distilled data. The abstract and conclusion state privacy as a property of the approach. | Abstract: "while also providing strong privacy protection through offline processing"; §5: "ensures privacy protection through offline dataset distillation" | gap | major | Remove the claim, or add membership-inference attacks on models trained on the distilled sets vs. the full set. Moderate cost |
| R8 | significance | The training-efficiency claim is untested. No distillation or training time is reported. DATM needs expert trajectories trained on the full dataset, and RCIG is a bilevel method with NTK-style computations, so the end-to-end cost is plausibly higher than training once with CE. | Abstract: "enhances training efficiency"; §1 Contributions bullet 1; §5; §3.2 (DATM "faces significant scalability challenges") | gap | major | Report the wall-clock and GPU memory of distillation plus evaluation vs. CE and LNL baselines on the same hardware |
| R9 | significance (claim distortion) | The tail-class / imbalanced-data finding is stated in the abstract, the contributions and the conclusion, but no imbalanced dataset or tail-class experiment exists; §4 calls it a hypothesis. | §4: "We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets, are at risk of being lossy"; Abstract; §5 | gap | major | Run CIFAR-10/100-LT with noise, or demote the claim to future work in the abstract and contributions |
| R10 | significance (framing) | "In the Wild" and "real-world" are not backed by the setting. Natural noise is tested only on CIFAR-10N/100N (32×32 re-annotations of CIFAR). Clothing1M and WebVision are named as the classic real-world benchmarks and not used. | §3.1: "high-volume datasets like Clothing1M [48] and WebVision [27] serve as classic benchmarks"; §4 Experiment-III uses only CIFAR-N | judgment | major | Add Clothing1M or (mini-)WebVision, or retitle and narrow the claims |
| R11 | experimental validation / significance | The regime is small: 3–4-layer ConvNets on ≤ 64×64 images. Real noisy-label training uses ResNets or ViTs and pretrained models. Whether distilled sets denoise for those architectures (cross-architecture generalization is a known weakness of DD) is untested, so the conclusions may not transfer. | §4: "a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet" | gap | major | Evaluate the distilled sets on ResNet-18 (cross-architecture), and ideally distill with a larger backbone |
| R12 | experimental validation | No seeds, runs or variance. All results are single curves, and the claims rest on visual comparison with a dashed line. At small IPC, DD results vary notably across runs. | Omission sweep: "seed", "run", "std", "variance" not found; Figs. 2, 4, 5 captions | gap | major | Report the mean ± std over ≥ 3 distillation seeds at each IPC |
| R13 | novelty | The paper proposes no new method; it runs three existing distillers with their default protocols. "A novel approach" overstates a benchmark study. Closely related prior lines go undiscussed: coreset selection for robust training under noisy labels (Mirzasoleiman, Cao and Leskovec, "Coresets for Robust Training of Deep Neural Networks against Noisy Labels", NeurIPS 2020) and studies of dataset distillation/condensation under label noise [verify; no literature search ran]. | Abstract: "we propose a novel approach that leverages dataset distillation for noise removal"; §3.2: "we select three representative state-of-the-art methods"; §2 has no data-selection-under-noise discussion | judgment | major | Reframe as an empirical study, position it against coreset-under-noise and noisy-DD work, and/or propose a noise-aware distiller |
| R14 | reproducibility | Hyperparameters, distillation iterations, expert-training details, evaluation schedule and code availability are all absent, so the curves cannot be reproduced for the noisy setting. | Omission sweep: "hyperparam", "learning rate", "epoch", "GPU", "github" not found; §4 Implementations | gap | major | Add an implementation-details appendix and release code and distilled sets |
| R15 | clarity | Results are given only as plots; no accuracy number is in the text or a table, and key statements are qualitative ("significantly outperform", "comparable performance"). Readers cannot extract the effect sizes. | §4 Experiments I–III; no table in the paper | gap | minor | Add a table of accuracies at chosen IPCs (e.g., 1/10/50) for each method, dataset and noise rate |
| R16 | clarity | Small inconsistencies and typos: Eq. 4 uses θ̂_{t+N} while the text defines θ̂_{t+T}; "Both of which" refers to three noise types; "Realted Works", "bellow"; Experiment-III mixes "Worst" (a CIFAR-10N label set) with "the CIFAR100N baseline". | §3.2 Eq. 4 and preceding text; §3.1: "Both of which are widely employed in existing researches"; §2 heading; §1 "Contributions … bellow"; §4 Experiment-III | error | minor | Proofread; fix Eq. 4's index; split the CIFAR-10N and CIFAR-100N statements |
| R17 | significance / novelty (contribution check Q1) | The insights are largely predictable from the memorization literature the paper itself cites [1, 14, 47]: networks fit common patterns first, so a common-pattern compressor ignores random flips and keeps systematic flips. The paper offers no analysis of *why* or *when* beyond this restatement, e.g., no prediction of the IPC threshold as a function of τ that is checked against the data. | §3.1 Remark: "networks always first memorize training data of common patterns (e.g. clean labels) and then those of hard samples"; §4 Insight-I/II | judgment | major | Add a mechanism study (e.g., per-sample influence of noisy vs. clean images on the synthetic set; label-accuracy of DATM soft labels), or a validated predictive rule |
| R18 | clarity (format) | The extracted layout looks like a CVPR template (captions "Figure 1.", two-column numbered references, page numbers) rather than ICLR's. This could be a format violation, but it cannot be confirmed from extracted text. | p. 1 caption "Figure 1. (a) for symmetric noise…"; reference style | question | major | Re-typeset in the ICLR 2026 template |
| R19 | technical rigor | Does an explicit filtering step inside DATM do part of the "denoising"? As I recall the original DATM paper [13], it initializes the synthetic images with real samples that the expert classifies correctly and uses expert soft labels [verify]. That would be a noise-evaluation step, contrary to C5's "avoids the feedback loop". The paper does not discuss the initialization or label scheme used. | §3.2 Benchmark-I description (no initialization/label details); §1: "This method avoids the feedback loop" | question | major | State the initialization and label scheme for each distiller; ablate random-real vs. expert-filtered initialization |
| R20 (added in T3 review) | experimental validation | Insight-I proposes using distillation results to "estimate the proportion of noise in the data", and Corollary-II is offered for this, but no experiment estimates τ on any dataset and compares it with the known rate. | §4 Insight-I: "offering a way to estimate the proportion of noise in the data"; Corollary-II | gap | minor | Estimate τ on CIFAR-10N/100N from the IPC at which accuracy matches the baseline, and compare with the published rates |

### Answered

- "Only synthetic noise is tested": answered at §4 Experiment-III (CIFAR-10N Aggre/Random/Worst, CIFAR-100N), Fig. 5. The scale of that test remains R10.
- "Only one distillation family is tested": answered at §3.2 (parameter matching, distribution matching, meta-learning).
- "Only favorable results are reported (cherry-picking of noise types)": answered at §4 Experiment-II / Fig. 4, which reports the asymmetric-noise failure, and at Experiment-III, which reports the Aggre failure.
- "The asymmetric-noise construction is undefined": answered at §4 Implementations (explicit class-flip pairs for CIFAR-10; superclass-internal flips for CIFAR-100) and Eq. 2.

### Aspect coverage

- technical rigor: A9; R2, R3, R4, R5, R6, R19
- novelty: A1; R13, R17
- significance: A3, A4, A8; R7, R8, R9, R10, R17
- experimental validation: A2, A3, A5; R1, R11, R12, R20
- clarity: A6; R15, R16, R18
- reproducibility: A10; R14
- ethics: considered. No human subjects, personal data or deployment risk; R7 (unsupported privacy claim) bears on it. The conclusion acknowledges the limitations (asymmetric noise, lossy compression); no separate limitations or impact section.
- qualitative evidence (CV checklist §3): A7. Selection procedure of Fig. 3 is not stated; the figure was not seen.
- CV checklist confounds: backbone parity and baseline schedule → R2, R11; hyperparameter selection on test → R3; compute → R8.

### Pairs

- A1 ↔ R13, R17: is the DD-as-denoiser perspective a new insight or a restatement of memorization theory?
- A3 ↔ R2, R3: does IPC = 1 beating full-data CE show denoising, or a weak baseline / test selection?
- A2 ↔ R11, R1: breadth across DD families vs. narrowness of architecture and missing LNL comparisons.
- A5 ↔ R10: natural noise tested, but only on CIFAR-N.
- A8 ↔ R7, R8: privacy and efficiency motivations vs. no measurements.
- A9 ↔ R5, R6, R20: the corollaries as a contribution vs. their correctness and use.
- A4 ↔ R17: is the asymmetric-noise failure informative or expected?

---

## 3. Reorganized ledger and probes

Merges: none needed. R9 and R10 are kept separate (one is an untested claim, the other a scale/framing mismatch).

### By claim

**C1 (symmetric noise: DD denoises)**
- A2 (checked: §3.2 and §4 read in place), A3 ↔ R2 (checked after P4; high swing), A3 ↔ R3 (open after P1; question; high swing), R4 (open after P8; high swing), R19 (open after P8; question), R12 (checked after P10), A7 (open, figure unseen; low swing)

**C2 (asymmetric noise is absorbed)**
- A4 (checked against the text; figure unseen), A4 ↔ R17 (judgment; checked as to what the paper says)

**C3 (natural noise)**
- A5 (checked), A5 ↔ R10 (checked after P7), R11 (checked after P7)

**C4 (tail-class lossy compression)**
- R9 (checked after P6)

**C5 (avoids vicious cycle, efficiency, privacy)**
- A8 ↔ R7, R8 (checked after P5), R4/R19 (as under C1), R1 (checked after P3; worst case fatal)

**C6 (corollaries)**
- A9 ↔ R5 (checked after P2; error), R6 (checked; derived count), R20 (checked; added in T3 review)

**C7 (framing: novel approach, in the wild)**
- A1 ↔ R13 (partly checked after P9; prior-art part [verify]), R10

**General**
- A6 (checked), A10 ↔ R14 (checked after P10), R15 (checked), R16 (checked), R18 (open; question)

Swing ranking (high to low): R1, R3, R2, R5, R4, R13, R10, R11, R19, R7, R8, R9, R12, R14, R17; then the rest.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R3 (↔ A3) | Is the reported accuracy chosen on the test set, i.e., is a separate validation split used to select the distillation iteration or checkpoint? | Re-read §4 Implementations and the captions of Figs. 2, 4, 5; searched for "validation" and "test" | Cannot be settled from the paper. §4: "performance is evaluated based on test accuracy on distilled datasets" and "Final test accuracies are reported throughout the distillation process"; captions: "The validation performance". No validation split is defined anywhere. | R3 stays an open `question`; no type may grade it above minor. A3 keeps "moderate" but depends on R3 |
| P2 | R5 (↔ A9) | Is Corollary-II consistent with the paper's own reported results? | Recomputed Eq. 11's bound 1 − C·IPC/\|S̃\| for the settings in §4 (using the standard 50,000-image CIFAR training sets; the paper does not state the sizes) | Confirmed. CIFAR-10, IPC = 50 → τ ≥ 0.99, but at τ = 0.2 "fewer than 50 samples per class significantly outperform the baseline" (§4). CIFAR-100N, IPC = 10 → τ ≥ 0.98 vs. the actual 0.402 (§4 Experiment-III). The bound contains no accuracy or δ term, and Eq. 10 rearranged gives τ ≤ 1 − C·IPC/\|S̃\|, the reverse direction. | R5: question → `error` (checked). A9: weak → weak, condition failed |
| P3 | R1 | Does the paper compare with any learning-with-noisy-labels method anywhere? | Traced every baseline mention ("baseline" ×5) and every cited LNL method | Confirmed. LNL methods appear only in §1–2. Every baseline is "training on the full dataset at the corresponding noise rate" (Fig. 2, 4, 5 captions; §4 Observation-I: "the baseline trained on the entire noisy dataset"). | R1: open → checked (gap confirmed) |
| P4 | R2 (↔ A3) | Is there any control (random subset, coreset, early stopping, clean subset) that would separate denoising from data reduction or regularization, and is the baseline's training schedule stated? | Re-read §4 Implementations and Experiments I–III; searched for "random", "subset", "early", "epoch" | Confirmed absent. "random" occurs only in the noise definitions and the DANCE λ; "subset" only in the motivation; "early" only in reference titles; no epochs or stopping rule are stated for the baseline. | R2: open → checked. A3: moderate, now conditional on an untested control |
| P5 | R7, R8 (↔ A8) | Does the paper measure privacy or compute anywhere? | Searched "privacy" (6 occurrences) and "efficien" (5) and read each in place | Confirmed absent. All privacy mentions are claims (Abstract, §1 ×2, end of §3, §5 ×2); the efficiency mentions are claims or describe [9]. No timing, memory or attack is reported. | R7, R8: open → checked. A8: weak → weak (its condition fails) |
| P6 | R9 | Is there any experiment on imbalanced data or tail classes? | Searched "imbalanc" (4) and "tail" (5) | Confirmed absent. Every occurrence is in the Abstract, the Contributions, the §4 hypothesis ("We further hypothesize…") or §5. | R9: open → checked |
| P7 | R10, R11 | Which datasets and architectures are actually used for the "in the wild" claims? | Traced C3 → Experiment-III → Fig. 5; searched "Clothing", "WebVision", "ResNet" | Confirmed. Natural noise: CIFAR-10N and CIFAR-100N only. Clothing1M and WebVision appear only in §3.1 and the references. Architectures: the 3- and 4-layer ConvNets only. | R10, R11: open → checked |
| P8 | R4, R19 | How are the expert trajectories / encoders trained (noisy or clean labels, epochs), and how are the synthetic sets initialized and labeled? | Re-read §3.2 (Benchmark-I/II/III) and §4 Implementations | Cannot be settled from the paper. The objectives are given, but no expert-training data, epochs, initialization or label scheme is stated. | R4: stays an open `gap` (the omission itself is checked). R19 stays an open `question` (≤ minor) |
| P9 | R13 (↔ A1) | Does the paper propose a method beyond running existing distillers, and does it discuss data-selection-under-noise prior work? | Re-read the Abstract, §1 Contributions, §2, §3.2; no literature query (no network) | Partly. Confirmed: no new algorithm. §3.2 runs three existing methods "following the evaluation protocols of DATM, DANCE, and RCIG", and §2 has no coreset/data-selection-under-noise discussion. The prior-art part rests on memory and is marked [verify]. | R13: open → checked for the framing part; the prior-art part stays [verify] |
| P10 | R12, R14 | Are seeds, runs, variance, hyperparameters or code stated anywhere? | Omission sweep (text search over the full text) | Confirmed absent: "seed", "std", "hyperparam", "learning rate", "epoch", "GPU", "github" not found; no appendix. | R12, R14: open → checked |
| P11 (after reviews) | R2: T1 major vs. T5 minor | Is the full-data baseline trained with the same ConvNet, schedule and stopping rule as the evaluation of the distilled sets? T5 graded minor on the assumption that it is matched and early-stopped. | Re-read §4 Implementations, Experiment-I and the Fig. 2 caption | Cannot be settled: the baseline architecture, epochs and stopping are not stated. T5's assumption is unsupported. | T5: R2 minor → major (updated after P11). Not among T5's decisive items, so its scores are unchanged |

---

## 4. Reviewer roster

Aspects with ≥ 12% of the ratio: technical rigor (28%), novelty (20%), significance (20%), experimental validation (14%); each has at least one type. Clarity (10%), reproducibility (5%) and ethics (4%) have no type of their own; their items sit in other types' "Weighs most", and the script renormalizes those shares away.

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Noisy-label learning specialist | experimental_validation | the task (learning with noisy labels) | builds and benchmarks LNL methods on CIFAR-N, Clothing1M, WebVision | comparisons against strong LNL baselines under matched backbones; real-noise benchmarks | a weak CE baseline as the only comparison; test-set selection; single runs | R1, R2, R3, R10, R12, A3, A5 | high |
| T2 Dataset distillation specialist | technical_rigor | neighbor: dataset distillation / condensation | trajectory, distribution and kernel-based distillation | correct use of the distillers; expert-training and initialization details; cross-architecture tests | unexplained gains at tiny IPC; missing implementation details; ConvNet-only results | R4, R19, R11, R14, R16, A2, A6, A7, A10 | high |
| T3 Learning-theory and memorization theorist | technical_rigor | neighbor: learning theory (memorization, early learning) | label-noise theory, generalization bounds, early-learning dynamics | statements with assumptions and proofs that predict experiments | unproved "corollaries"; restating known phenomena as insight | R5, R6, R17, R20, R3, A9 | medium |
| T4 Data-centric ML and coreset-selection researcher | novelty | neighbor: coreset selection, data pruning, data valuation (added) | selecting or synthesizing training subsets, including under label noise | a clear delta over data-selection baselines; insight into *which* data are kept | DD gains that a random subset or coreset would also give; missing data-selection prior work | R13, R2, R17, R1, A1, A4 | medium |
| T5 Privacy and trustworthy-ML researcher | significance | neighbor: privacy-preserving ML | membership inference, differential privacy, privacy of synthetic data | privacy claims backed by attacks or guarantees; honest threat models | "privacy for free" claims for distilled data; efficiency claims without accounting | R7, R8, R9, A8 | low |
| T6 Large-scale robust-training practitioner | significance | neighbor: web-scale noisy training (added) | trains ResNet/ViT models on web-crawled noisy data | evidence on realistic data, architectures and compute budgets | CIFAR-only "in the wild" claims; unreported compute; plots without numbers | R10, R11, R8, R9, R15, R18, R2, A3, A5 | medium |

---

## 5. Reviews

### T1: Noisy-label learning specialist (experimental_validation; the task)

**Reading of the ledger.**
- Holds: A2 (the three families are covered, §3.2). A5 (CIFAR-N is the right first real-noise benchmark, and the Aggre failure is reported honestly). A4 (the asymmetric failure is a useful negative result).
- Discounts: A3. Beating CE on 50k noisy images with a ConvNet at τ = 0.8 is a low bar; CE without early stopping memorizes the noise, and the paper states no schedule (P4).
- R1: fatal. The paper calls itself "a new approach to model learning from noisy data" (§5) and compares against none of the methods it cites; the claim cannot be evaluated at all.
- R2: major. Without random-subset or early-stopped controls, "denoising" is not separated from "training on less data".
- R3: minor (unsettled question, P1). It would be critical if confirmed.
- R10: major. CIFAR-N alone does not support "in the wild".
- R12: major. At IPC = 1–10, DD curves are noisy; one curve per setting cannot carry "consistently outperform".
- R11: major. The field moved to ResNet-scale models long ago.

**Opinion.** As someone who works on label noise, I find the question interesting: can a condensed synthetic set stand in for sample selection? But the paper does not answer it in the terms my field uses. The only comparator is plain cross-entropy on the full noisy set, which is the weakest baseline in the literature and is known to collapse at high symmetric noise. Every LNL method the paper cites (Co-teaching, DivideMix, GCE, DISC) is absent from the experiments, so I cannot tell whether a distilled set is a competitive denoiser or merely better than doing nothing. The obvious controls (a random subset of the same size, early stopping) are also missing, as are seeds and any number I could compare. The natural-noise evidence is limited to CIFAR-N, while the benchmarks the paper itself names as "classic" for real noise are not used. What would change my mind: a table at IPC 10/50 against three LNL methods and a random-subset control on CIFAR-N and Clothing1M, with seeds, and a clear statement of how checkpoints were selected.

Decisive: R1 (fatal), R2 (major), R10 (major), R12 (major), A5 (moderate, held), A3 (discounted)

**Scores.** Pool position 15 (basis: R1, R2, R10). Bracket: above A (A4, A5: unlike A, there is a non-obvious positive observation tested on real annotation noise, with a reported failure mode); below B (R1, R2: B's formalism was sound but disconnected from the claim, while here the central empirical claim has no competitive comparison at all). Technical Rigor 34, Clarity 48, Novelty 38, Significance 36, Experimental Validation 28, Reproducibility 38, Ethics 55. Overall 2. Confidence 4.

### T2: Dataset distillation specialist (technical_rigor; neighbor: dataset distillation)

**Reading of the ledger.**
- Holds: A2 (sensible choice of one method per family, §3.2). A6 (the summaries of DATM, DANCE and RCIG are accurate enough to follow). A7 (weak; I would want to see Fig. 3 at more than IPC = 1).
- Discounts: A10. "Following the original protocols" does not cover the noisy-data choices that matter here (P8, P10).
- R4: major. Whether the experts were trained on noisy labels, and over which epochs DATM matches, determines whether this is early stopping in disguise.
- R19: minor (unsettled question, P8). If DATM's expert-filtered initialization is used, part of the denoising is explicit filtering.
- R14: major. No distillation iterations, learning rates, expert epochs or code.
- R11: major. ConvNet-only results; cross-architecture transfer is the known weak point of DD.
- R2: major. Random-real-image initialization at the same IPC is the standard DD control and is missing.
- R16: minor (the index in Eq. 4, typos).
- R12: minor. Small-IPC variance is real, but this is secondary to R4.

**Opinion.** The study uses the distillers competently at the level of description, but it does not open them up, and the claim lives inside them. Each of the three methods has a component that could do the denoising on its own: DATM's trajectory range and (I believe) its expert-based initialization, DANCE's trained expert encoders, RCIG's kernel regression on noisy labels. The paper never says how these were configured for noisy data, so the reader cannot tell whether "distillers are good denoisers" or "early-epoch experts are good denoisers". The missing controls that DD papers routinely include (random real images at the same IPC; evaluation on ResNet-18) make it impossible to separate synthesis from selection. I also could not find a single hyperparameter. What would change my mind: the expert and initialization details, an ablation over the matching range, a random-real-initialization control, and cross-architecture results.

Decisive: R4 (major), R14 (major), R11 (major), R2 (major), A2 (moderate, held)

**Scores.** Pool position 22 (basis: R4, R14, R11). Bracket: above A (A2, A4: a clean failure mode across three families is more than a formatting observation); below B (R4, R14: the mechanism is not even specified, so the link between evidence and claim is weaker than B's). Technical Rigor 36, Clarity 50, Novelty 40, Significance 38, Experimental Validation 34, Reproducibility 32, Ethics 58. Overall 2. Confidence 4.

### T3: Learning-theory and memorization theorist (technical_rigor; neighbor: learning theory)

**Reading of the ledger.**
- Holds: A4 (the asymmetric failure follows from the theory, which at least makes the study coherent).
- Discounts: A9. The corollaries do not deliver (P2).
- R5: major. Eq. 11 has no proof and no accuracy or δ term, and it gives τ ≥ 0.98–0.99 for the paper's own settings, where τ is 0.2–0.4. It is wrong as stated, but it is not the main claim.
- R6: minor. Eq. 10 is the clean-sample count per class.
- R17: major. The "insights" restate the early-learning / memorization picture of [1, 47]: random flips are not a common pattern, systematic flips are.
- R3: minor (unsettled question).
- New reason: **R20 (added in T3 review)**, gap, minor: Insight-I says distillation offers "a way to estimate the proportion of noise", but τ is never estimated. Graded minor.

**Opinion.** The paper invokes theory in two places, and neither holds up. Corollary-I is a counting identity, not a statement about distillation. Corollary-II is presented as a high-probability bound, but δ never enters the inequality, the accuracy condition never enters it either, and plugging in the paper's own reported thresholds gives absurd noise rates (≥ 98%) where the true rates are 20–40%. The direction is also the reverse of what Corollary-I implies. Beyond the corollaries, the conceptual story ("distillation captures common patterns, so random noise is filtered and structured noise is kept") is exactly what the memorization literature predicts, and the paper adds no quantitative prediction to test it, such as the IPC threshold as a function of τ and class count. I would move up for a correct, proved statement that predicts the curves in Fig. 2, or an analysis of which training points the synthetic set depends on.

Decisive: R5 (major), R17 (major), R6 (minor), A9 (discounted)

**Scores.** Pool position 15 (basis: R5, R17). Bracket: above A (A4: the paper does report a qualified, non-trivial pattern across noise types); below B (R5, R6: B had a clean formalism loosely tied to experiments; here the formal statements are trivial or contradicted by the experiments). Technical Rigor 30, Clarity 46, Novelty 36, Significance 34, Experimental Validation 36, Reproducibility 40, Ethics 56. Overall 2. Confidence 3.

### T4: Data-centric ML and coreset-selection researcher (novelty; neighbor: data selection)

**Reading of the ledger.**
- Holds: A1 (the framing is a disclosed transfer between two literatures that rarely talk, and that has some value). A4 (the observation that compression keeps systematic errors is relevant to data-selection work).
- R13: major. No new method. Coreset selection under noisy labels (Mirzasoleiman et al., NeurIPS 2020) is the closest line and is not discussed; noisy-DD studies may exist [verify].
- R2: major. From my field, the first control is a random subset and a coreset at equal size; without them the novelty of *synthesis* over *selection* is unshown.
- R17: major. Question 1 of the contribution check largely fails.
- R1: major. For my aspect, the missing LNL comparison limits the delta more than it invalidates it.

**Contribution check.** (1) What does a reader learn? That off-the-shelf distillers beat full-data CE under random noise and fail under structured noise. The second half is expected from R17, and the first is not separated from subset size (R2): largely fails. (2) Does the setting support the framing? "In the Wild" and "real-world" rest on CIFAR-N only (R10): fails. (3) Conceptual or refinement? It applies three existing distillers unchanged (R13): a refinement-level, benchmark-style delta. (4) Would the conclusions transfer? Not shown beyond small ConvNets (R11): doubtful. Questions 1 and 3 fail, so novelty sits in the lower half unless A1 carries a specific insight, which it does only modestly.

**Opinion.** The framing is the paper's best asset: data condensation as an alternative to the detect-then-correct pipeline is a reasonable idea worth an empirical look, and the asymmetric-noise negative result is worth recording. But as a novelty contribution it is thin. Nothing new is built, the closest neighbor (subset selection robust to noisy labels) is neither cited nor run as a baseline, and the insights restate what the memorization picture predicts. I lean further toward rejection than an ordinary borderline paper: the study does not yet show that synthesis matters beyond choosing fewer, cleaner examples. A version with random-subset and coreset controls, a noise-aware distiller, or a validated rule for choosing IPC from τ would be a real contribution.

Decisive: R13 (major), R2 (major), R17 (major), A1 (moderate, held)

**Scores.** Pool position 32 (basis: A1, A4 vs. R13, R2, R17). Bracket: above B (A1, A4: unlike B, the evidence here is in the setting the framing names, at least on CIFAR scale, and a clear failure mode is shown); below C (R13, R17: C was rigorous and tuned with care, but here the comparisons are not even controlled, and like C there is no "why"). Technical Rigor 44, Clarity 54, Novelty 46, Significance 44, Experimental Validation 42, Reproducibility 44, Ethics 60. Overall 3. Confidence 3.

### T5: Privacy and trustworthy-ML researcher (significance; neighbor: privacy-preserving ML)

**Reading of the ledger.**
- Discounts: A8. The privacy use case is asserted, not demonstrated (P5).
- R7: major. "Strong privacy protection" with no attack, no DP accounting and no threat model. The privacy of distilled data is contested in the literature (e.g., Dong, Zhao and Lyu, "Privacy for Free: How does Dataset Condensation Help Privacy?", ICML 2022, and a later rebuttal of its claims by Carlini et al. [verify]).
- R8: major. Efficiency is claimed with no accounting, while the distillers require expert training on the full data.
- R9: minor. A hypothesis in the abstract; for my aspect it matters less than R7.
- R2: minor initially, on the assumption that the baseline is matched and early-stopped. **Updated after P11: minor → major** (the baseline's training is not stated, so the assumption is unsupported).

**Opinion.** The paper's significance case rests on three practical promises: it avoids the noise-estimation loop, it is efficient, and it protects privacy. The last two are not tested at all. For privacy in particular, the claim is strong ("ensures privacy protection") and the paper offers no evidence. Distilled sets can leak membership, especially at the small IPCs at which the paper's best results occur, where individual training images can dominate a synthetic image. A privacy-motivated paper must at least report membership-inference success against models trained on the distilled set. As it stands, the privacy framing is a liability: an ICLR reader in my area would see an untested claim in the abstract. I would raise my score if the privacy and efficiency claims were either measured or removed and the significance argument rested on the denoising evidence alone.

Decisive: R7 (major), R8 (major), A8 (discounted)

**Scores.** Pool position 18 (basis: R7, R8). Bracket: above A (A3, if it holds, is a non-trivial empirical observation, which A lacked); below B (R7, R8: two of the three headline benefits are unsupported, a larger claim-evidence gap than B's). Technical Rigor 36, Clarity 50, Novelty 40, Significance 32, Experimental Validation 34, Reproducibility 40, Ethics 45. Overall 2. Confidence 3.

### T6: Large-scale robust-training practitioner (significance; neighbor: web-scale noisy training)

**Reading of the ledger.**
- Discounts: A3 (an effect on 32×32 CIFAR with a 3-layer ConvNet against plain CE does not tell me anything about my setting). A5 (CIFAR-N is a re-annotation of CIFAR, not "the wild").
- R10: major. Clothing1M and WebVision are named and not used.
- R11: major. Nothing at ResNet/ViT scale or with pretraining; DATM itself "faces significant scalability challenges on large-scale, real-world datasets like ImageNet" (§3.2).
- R8: major. Distillation cost is not reported, and for me it is the deciding cost.
- R9: major. An imbalance claim in the abstract with no experiment; real noisy data are long-tailed, so this matters to me.
- R2: major. Practitioners would compare with simply training on a cleaner random subset.
- R15: minor. No numbers, only curves.
- R18: minor (unsettled question about the template).

**Opinion.** The title promises denoising "in the wild", and I read it as a practitioner who trains on web-crawled, long-tailed, noisy data. The evidence is all at CIFAR scale with tiny ConvNets, and the paper itself notes that the distillers it relies on do not scale to ImageNet-sized data. The two real-noise benchmarks it names are not used. Real web noise is also long-tailed, and the one claim that bears on that (tail classes are lossily compressed) is a hypothesis. I also cannot read effect sizes: the paper has no table, and the reader is asked to judge curves against dashed lines. I see a reasonable workshop-level observation. To matter for practice it needs a Clothing1M- or WebVision-scale experiment, cost accounting against standard LNL training, and an imbalanced-noise experiment.

Decisive: R10 (major), R11 (major), R8 (major), R9 (major), A3 (discounted)

**Scores.** Pool position 15 (basis: R10, R11, R8). Bracket: above A (A2: three method families and three noise types are a real empirical effort, more than prompt formatting); below B (R10, R11: the setting is far from the regime the title names, a wider gap than B's toy-vs-real gap, without B's formal contribution). Technical Rigor 36, Clarity 46, Novelty 38, Significance 30, Experimental Validation 30, Reproducibility 36, Ethics 56. Overall 2. Confidence 4.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P11 | T1, T2, T4, T6 major vs. T5 minor on R2 | Is the full-data baseline trained with the same ConvNet and schedule, with early stopping? | Not stated anywhere in §4 or the captions: cannot be settled, so T5's assumption of parity is unsupported | T5: R2 minor → major (not decisive for T5; scores unchanged) |

Value splits that stay: R1 (T1 fatal, T4 major: whether the missing LNL comparison invalidates the claim or only limits the delta); R12 (T1 major, T2 minor); R9 (T6 major, T5 minor).

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 Noisy-label learning specialist | experimental_validation | 0.169 | 15 | 2 | 4 |
| T2 Dataset distillation specialist | technical_rigor | 0.169 | 22 | 2 | 4 |
| T3 Learning-theory and memorization theorist | technical_rigor | 0.169 | 15 | 2 | 3 |
| T4 Data-centric ML and coreset-selection researcher | novelty | 0.247 | 32 | 3 | 3 |
| T5 Privacy and trustworthy-ML researcher | significance | 0.124 | 18 | 2 | 3 |
| T6 Large-scale robust-training practitioner | significance | 0.124 | 15 | 2 | 4 |

- **Aspect-weighted rating:** 2.247 → **final rating 2 (Reject)**; ICLR 2026 label: **2 on {0, 2, 4, 6, 8, 10}** (3 on the earlier {1, 3, 5, 6, 8, 10} scale; the scale status is `secondary`, so verify it against the current form). ICLR sub-scores: Soundness 1, Presentation 2, Contribution 1.
- Weighted pool position 20.8; plain mean 2.17; spread 1 (2–3).
- Uncovered aspects and warnings: none. Clarity, reproducibility and ethics (19% together) have no type of their own and are renormalized away, as the roster rules allow for aspects below 12%.
- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

```
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Noisy-label learning specialist) | experimental_validation | 14% | 0.169 |
| T2 (Dataset distillation specialist) | technical_rigor | 28% | 0.169 |
| T3 (Learning-theory and memorization theorist) | technical_rigor | 28% | 0.169 |
| T4 (Data-centric ML and coreset-selection researcher) | novelty | 20% | 0.247 |
| T5 (Privacy and trustworthy-ML researcher) | significance | 20% | 0.124 |
| T6 (Large-scale robust-training practitioner) | significance | 20% | 0.124 |

**Final rating (aspect-weighted mean)**: **2.25** → **2 (Reject)** · plain mean 2.17 · weighted pool position 20.8

| Venue | Venue-weighted composite | Bar offset | Band | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|
| ICLR (2026) | 38.4 | +0 | 2 → 2 | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) | Soundness 1, Presentation 2, Contribution 1 | secondary |

Composite cross-check (0-100): official 38.7 → 2. Decision ceiling: none.
```

Full JSON: `aggregate.json` (with `--final 2`) and `before.json` in this directory.

</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R1 | 2 of 6 | T1 fatal, T4 major |
| R2 | 5 of 6 | T1 major, T2 major, T4 major, T5 major (after P11), T6 major |
| R3 | 2 of 6 | T1 minor, T3 minor (unsettled question) |
| R4 | 1 of 6 | T2 major |
| R5 | 1 of 6 | T3 major |
| R6 | 1 of 6 | T3 minor |
| R7 | 1 of 6 | T5 major |
| R8 | 2 of 6 | T5 major, T6 major |
| R9 | 2 of 6 | T5 minor, T6 major |
| R10 | 2 of 6 | T1 major, T6 major |
| R11 | 3 of 6 | T1 major, T2 major, T6 major |
| R12 | 2 of 6 | T1 major, T2 minor |
| R13 | 1 of 6 | T4 major |
| R14 | 1 of 6 | T2 major |
| R15 | 1 of 6 | T6 minor |
| R16 | 1 of 6 | T2 minor |
| R17 | 2 of 6 | T3 major, T4 major |
| R18 | 1 of 6 | T6 minor (question) |
| R19 | 1 of 6 | T2 minor (question) |
| R20 | 1 of 6 | T3 minor |
| A1 | 1 of 6 | T4 held |
| A2 | 2 of 6 | T1 held, T2 held |
| A3 | 3 of 6 | T1 discounted, T5 held (as bracket basis), T6 discounted |
| A4 | 3 of 6 | T1 held, T3 held, T4 held |
| A5 | 2 of 6 | T1 held, T6 discounted |
| A6 | 1 of 6 | T2 held |
| A7 | 1 of 6 | T2 held (weak) |
| A8 | 1 of 6 | T5 discounted |
| A9 | 1 of 6 | T3 discounted |
| A10 | 1 of 6 | T2 discounted |

### Key strengths

- A4: an honest, clearly stated failure mode. Structured asymmetric noise is distilled into the synthetic set (§4 Insight-II, Fig. 4). Held by 3 of 6 types.
- A2: the three main DD families under three noise types (§3.2, §4). Held by 2 of 6.
- A5: real human-annotation noise (CIFAR-10N/100N) is included, with the low-noise failure reported (§4 Experiment-III). Held by 1 of 6, discounted by 1.
- A1: a disclosed transfer of dataset distillation to label-noise learning (§1, §3.1 Remark). Held by the novelty type.

### Top concerns (at most five)

1. R2: no control separating denoising from data reduction (random subset, coreset, early-stopped CE, clean-subset oracle); the baseline's schedule is unstated (§4 Experiment-I, Fig. 2 caption). Fix: add those rows at each IPC; hours of GPU. Major for 5 of 6 types.
2. R11: only 3–4-layer ConvNets on ≤ 64×64 images; no cross-architecture or larger-backbone result (§4 Implementations). Fix: evaluate the distilled sets on ResNet-18 and distill with a larger backbone; about a GPU-day at CIFAR scale. Major for 3 of 6.
3. R1: no learning-with-noisy-labels baseline, although the paper presents "a new approach to model learning from noisy data" (§5; Figs. 2, 4, 5 captions). Fix: add Co-teaching, DivideMix and a robust-loss method on the same backbone, with compute; a few GPU-days. Fatal for T1, major for T4.
4. R10: "In the Wild" rests on CIFAR-10N/100N only; Clothing1M and WebVision are named in §3.1 and not used. Fix: add Clothing1M or mini-WebVision, or retitle and narrow the claims. Major for 2 of 6.
5. R8: the training-efficiency claim is unmeasured, and the distillers need expert training on the full data (Abstract, §1, §5). Fix: report the end-to-end wall-clock and memory against CE and LNL training. Major for 2 of 6.

(R17 is also major for 2 of 6: the insights restate memorization theory. R5 is a confirmed error in Corollary-II: τ ≥ 0.98–0.99 for the paper's own settings.)

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R1 | Compare against ≥ 3 LNL methods (e.g., Co-teaching, DivideMix, a robust loss) under the same ConvNet and data, plus a ResNet-18 setting | a few GPU-days |
| 1 | R2 | Add random-subset, coreset, early-stopped-CE and clean-subset controls at each IPC; state the baseline's schedule and stopping rule | hours of GPU |
| 1 | R11 | Cross-architecture evaluation (ResNet-18) and distillation with a larger backbone | ~1 GPU-day |
| 2 | R10 | Clothing1M or mini-WebVision experiment, or retitle and narrow "in the wild" / "real-world" | 1–3 GPU-days, or editing |
| 2 | R8 | End-to-end compute and memory accounting against CE and LNL methods | low (logging) |
| 2 | R7 | Membership-inference evaluation of models trained on distilled vs. full data, or remove the privacy claims | ~1 GPU-day, or editing |
| 2 | R17 | Mechanism study (influence of clean vs. noisy samples on the synthetic set; soft-label accuracy) or a validated rule predicting the IPC threshold from τ | moderate |
| 2 | R5 | Remove Corollary-II, or state its assumptions, prove it and check it against Figs. 2 and 5 | low |
| 2 | R4 | Report expert-training data and epochs; ablate the trajectory range and clean- vs. noisy-label experts | moderate |
| 2 | R9 | CIFAR-LT-with-noise experiment, or demote the tail-class claim to future work | moderate, or editing |
| 2 | R12 | Mean ± std over ≥ 3 distillation seeds per IPC | 3× the current compute |
| 2 | R13 | Reframe as an empirical study; discuss coreset-under-noise and noisy-DD prior work; or propose a noise-aware distiller | editing (low) to a new method (high) |
| 2 | R14 | Implementation-details appendix; release code and distilled sets | low |
| 3 | R3 | State how checkpoints are selected; use a held-out noisy validation split | low |
| 3 | R19 | State each distiller's initialization and label scheme; ablate expert-filtered vs. random-real initialization | low–moderate |
| 3 | R6 | Recast Corollary-I as a counting remark or replace it | low |
| 3 | R15 | Add accuracy tables at IPC 1/10/50 | low |
| 3 | R16 | Fix Eq. 4's index, "Both of which", the typos and the CIFAR-10N/100N sentence | low |
| 3 | R18 | Re-typeset in the ICLR template | low |
| 3 | R20 | Estimate τ on CIFAR-N from the matching IPC and compare with the known rates | low |

Priority 1: R1 (graded fatal by T1), R2 (graded major by 5 of 6 types) and R11 (graded major by 3 of 6 types, exactly half of all types).

---

## 8. Integrity signals and limitations

- **Integrity signals:** `integrity_scan.py --redact` found no reviewer-directed text or hidden characters. The redaction replaced one venue/acceptance mark inside reference [10]. Reading the text found no out-of-place instructions. Nothing here changes a score.
- **Limitations:**
  - Figures 1–5 could not be seen, and they hold all of the paper's quantitative results (there is no table). A3, A5, A7 and the descriptions of C1–C3 rely on the authors' prose about the figures.
  - Eqs. 2, 5, 7, 8, 9 and 11 are partly garbled by extraction. The checks in P2 use only the readable structure of Eqs. 10–11.
  - The training-set sizes used in P2 (50,000 for CIFAR-10/100) are the standard ones; the paper does not state them.
  - The literature check did not run (no network). The novelty and prior-art statements in R13 and R7, and the description of DATM's initialization in R19, rest on memory and are marked [verify] where uncertain.
  - The six types share one context and one reading. Their agreement (e.g., on R2) is not independent confirmation.
