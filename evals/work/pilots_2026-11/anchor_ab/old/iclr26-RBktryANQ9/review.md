# Peer Review: Dataset Distillers Are Good Label Denoisers In the Wild

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | analysis (an empirical study of existing dataset-distillation methods under label noise; no new method is proposed) |
| Field, sub-area | machine learning / computer vision; learning with noisy labels, dataset distillation |
| Task | Image classification, representation learning (adapted: learning with noisy labels); Efficient models, compression (adapted: dataset distillation / condensation) |
| Neighboring fields | dataset distillation / condensation; learning theory of memorization and early learning (from row: learning theory); data-centric ML, coreset selection and data pruning (generated beyond the file); privacy-preserving ML (generated, from the robustness/privacy row); ML evaluation methodology (generated); semi-supervised learning as used by noisy-label methods (generated) |
| Target venue | ICLR 2026 (stated by the user) |
| Aspect ratio | `aggregate_scores.py ratio --paper-type analysis --venue iclr`: technical_rigor 28%, novelty 20%, significance 20%, experimental_validation 14%, clarity 10%, reproducibility 5%, ethics 4% |
| Literature check | off: no network access in this run; novelty reasons that rest on memory are marked [verify] |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

Input note: the manuscript was available only as extracted text. Figures 1-5 (which carry every quantitative result) could not be seen; figure-dependent claims are judged from captions and text only, and this is said where it matters.

---

## 1. Paper memory

**Claims.**
- C1: Dataset distillation is "a novel approach that leverages dataset distillation for noise removal" that "avoids the feedback loop common in existing techniques and enhances training efficiency, while also providing strong privacy protection through offline processing" (Abstract; Sec. 1 Contributions; Sec. 5).
- C2: Under symmetric noise, existing distillers (DATM, DANCE, RCIG) are effective denoisers: once noise passes a threshold they "consistently demonstrate significant performance gains" over training on the full noisy set (Sec. 4 Experiment-I, Observation-I, Insight-I; Figure 2).
- C3: Structured (asymmetric) noise is absorbed into the distilled samples and hurts training. Tail-class clean samples may be lossily compressed (Abstract; Sec. 4 Experiment-II, Observation-II, Insight-II; Figure 4).
- C4: On real-world natural noise (CIFAR-10N/100N), distillation "remain[s] largely effective even in the presence of an unknown fixed noise rate", especially at high noise (Sec. 4 Experiment-III, Observation-III, Insight-III; Figure 5). The title frames this as "In the Wild".
- C5: Two corollaries: an upper bound on IPC to preserve clean information (Corollary-I, Eq. 10) and a probabilistic noise-rate bound from distillation (Corollary-II, Eq. 11).

**Setup facts.**
- Datasets: CIFAR-10/100, Tiny-ImageNet (symmetric noise); CIFAR-10/100 (asymmetric); CIFAR-10N (Aggre 9.03%, Random k ~18%, Worst 40.21%), CIFAR-100N fine (40.20%) (Sec. 4 Implementations, Experiment-III).
- Noise construction: symmetric per Eq. 1. Asymmetric: CIFAR-10 TRUCK->AUTOMOBILE, BIRD->AIRPLANE, DEER->HORSE, CAT<->DOG; CIFAR-100 next class within its superclass (Sec. 4 Implementations). Noise rates: symmetric 0.2/0.4/0.6/0.8 (Sec. 4 Exp-I); asymmetric 0.2/0.4 at least (Sec. 4 Exp-II).
- Distillers: DATM, in fact "this accelerated version" based on [9] (Sec. 3.2); DANCE; RCIG (Sec. 3.2).
- Architecture: "a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet" (Sec. 4 Implementations).
- Evaluation: each distiller's original protocol; augmentation for RCIG; "Final test accuracies are reported throughout the distillation process" (Sec. 4). Captions say "validation performance" (Figs. 2, 4).
- Baseline: CE training on the full noisy set (dashed lines, Figs. 2/4/5); its protocol is not stated.
- IPC grid, distillation iterations, expert epochs, learning rates: not stated.
- Seeds, runs, variance: not stated.
- Compute: not stated.
- Code: not stated.
- Train/validation/test split and selection split: not stated (test set used for reporting).

**Headline numbers.**
- IPC=1 beats the full-noisy-data baseline at tau = 0.6 and 0.8 on CIFAR-10 (Sec. 4 Exp-I; Figure 2(a)).
- Fewer than 50 IPC beat the baseline at tau = 0.2 (Figure 2(a)).
- On CIFAR-100N (40.20% noise), all three distillers surpass the baseline with fewer than 10 IPC (Sec. 4 Exp-III; Figure 5).
- Under asymmetric noise, only DATM matches the baseline, at tau in {0.2, 0.4} with large IPC (Sec. 4 Exp-II; Figure 4).
- No accuracy value is printed anywhere in the paper.

**Appendix and supplement.** None in the provided text.

**Could not be read.**
- Figures 1-5: all curves and the distilled-image grid.
- Eqs. 2, 5, 8 and 9 are partly garbled by extraction. Their structure is readable, so they were not used for any error.
- No supplement was provided.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | novelty | Reframes learning with noisy labels as a dataset-distillation problem: distil a compact synthetic support set from the noisy data and train on it, sidestepping the noise-estimation step of selection/re-weighting/re-labelling pipelines. This links two literatures that rarely meet. | Abstract; Sec. 1 (Motivation); Sec. 3.1 Remark: "Why not directly distill a clean subset that enables effective training?" | moderate | R12 and R15 not upheld; the framing is backed by evidence |
| A2 | experimental_validation | Covers the three main families of dataset distillation with one representative each: parameter/trajectory matching (DATM), distribution matching (DANCE), meta-learning/kernel (RCIG), so conclusions are not tied to one distiller. | Sec. 3.2, Benchmark-I/II/III, Eqs. 4-9 | moderate | each method run with its original protocol |
| A3 | experimental_validation | Symmetric noise is swept over several rates (tau = 0.2, 0.4, 0.6, 0.8) and IPC values on three datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet), giving accuracy-vs-IPC curves against a full-data reference. | Sec. 4 Experiment-I; Figure 2(a)-(c) captions | moderate | R4 and R9 not upheld |
| A4 | significance | Striking headline effect: at high symmetric noise a single distilled image per class beats training on the full noisy set, and at tau=0.2 fewer than 50 IPC do. | Sec. 4 Experiment-I: "at noise rates of 0.6 and 0.8, a single distilled sample per class surpasses the baseline" | moderate | full-data baseline trained sensibly (R4); numbers verifiable (R9) |
| A5 | technical_rigor | Reports a negative result honestly: under asymmetric (class-pair) noise most distillers fall below the full-data baseline, and only DATM matches it at tau in {0.2, 0.4} with large IPC. This bounds the method's applicability. | Sec. 4 Experiment-II, Observation-II; Figure 4: "Only the DATM method achieves comparable performance to the benchmark at noise rate" | moderate | none |
| A6 | experimental_validation | Tests human-annotation noise (CIFAR-10N Aggre/Random/Worst, CIFAR-100N fine, tau up to 40%), not only synthetic flips, and reports where distillation helps (Worst) and where it does not (Aggre). | Sec. 4 Experiment-III; Figure 5 | moderate | R8 not upheld (scale of 'in the wild') |
| A7 | significance | Identifies an IPC-noise trade-off: small IPC removes noise but also compresses clean information, which explains why distillation underperforms at low noise (Aggre, 9%). | Sec. 4 Insight-III: "This is why data distillation often yields suboptimal results in low-noise settings" | weak | read from figures not available to this review |
| A8 | clarity | Self-contained recap of the noise models (Eqs. 1-2) and the three distillation objectives (Eqs. 4-9) lets a noisy-label reader follow the distillers. | Sec. 3.1 Eqs. 1-3; Sec. 3.2 Eqs. 4-9 | moderate | none |
| A9 | experimental_validation | Qualitative evidence: distilled DATM images at IPC=1 shown across tau=0.0-0.8, claimed to retain discriminative features under heavy noise. | Figure 3 caption; Sec. 4: "a single distilled image retains discriminative features despite high noise ratios" | weak | figure not available to this review |
| A10 | significance | Poses open problems with potential follow-up value: how much to distil from a noisy set, and whether distillation behaviour can estimate the noise rate. | Sec. 4 Insight-I; Corollary-II, Eq. 11 | weak | R1, R2 not upheld |
| A11 | reproducibility | Uses public datasets, public noise constructions (CIFAR-10 class mappings, CIFAR-100 superclass flips given) and the original evaluation protocols of the three public distillers with the standard ConvNet. | Sec. 4 Implementations: "a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet" | moderate | R20 not upheld |
| A12 | significance | Distillation is a one-off offline step yielding a tiny training set, which could make downstream training cheap and the raw data unnecessary after distillation. | Abstract; Sec. 1 Contributions; Sec. 5 | weak | R5 and R6 not upheld |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | technical_rigor | Corollary-II contradicts the paper's own results. For a dataset where IPC images per class already match the full-data accuracy it gives tau >= 1 - C*IPC/\|S\|, which is near 1 for every setting the paper reports as successful. | Corollary-II, Eq. 11: "the validation accuracy matches that of the original dataset"; check: CIFAR-10 (\|S\|=50,000, standard size, not stated in the paper), C=10, IPC=50 gives tau >= 0.99, but Sec. 4 Exp-I reports success at tau=0.2 with <50 IPC; CIFAR-100N (C=100, IPC<10) gives tau >= 0.98 vs the stated 40.20%. Eq. 11 also inverts the direction of Eq. 10 (which implies tau <= 1 - C*IPC/\|S\|). | error | major | Withdraw Corollary-II or restate it with a proof and assumptions under which it is consistent with Figs. 2/5; low cost (text) or moderate (new theory) |
| R2 | technical_rigor | Both corollaries are given without proof, assumptions or definitions ('perfectly preserve the sample information', delta, the probability space). Eq. 10 reduces to 'IPC is at most the number of clean samples per class' (4,000 on CIFAR-10 at tau=0.2) and so never constrains the IPC range 1-50 studied. | Corollary-I, Eq. 10: "This corollary succinctly states the upper bound"; Sec. 4 Exp-III, Eq. 11; recomputed \|S\|(1-tau)/C = 50,000*0.8/10 = 4,000 | gap | major | Either prove the statements with explicit assumptions or relabel them as conjectures/heuristics; low-moderate |
| R3 | experimental_validation | The paper presents distillation as 'a new approach to model learning from noisy data' but compares it with no noisy-label method. The only reference is CE training on the full noisy set. The cited sample selection (Co-teaching [14]), semi-supervised (DivideMix [24]), robust-loss (GCE [55]) and early-learning (ELR-style [47]) methods are never run, so it is unknown whether distillation is competitive with the methods it claims to replace. | Sec. 5: "We propose a new approach to model learning from noisy data that avoids vicious cycles"; Figure 2 caption: dashed lines are "training on the full dataset at the corresponding noise rate"; no other baseline in Sec. 4 | gap | fatal | Add at least 3-4 standard noisy-label baselines (CE+early stopping, Co-teaching, GCE, DivideMix) on the same ConvNet and on a standard ResNet; moderate (CIFAR-scale, a few GPU-days) |
| R4 | experimental_validation | The full-data reference is under-specified: architecture, epochs, augmentation, learning rate and especially whether early stopping or a clean validation set was used are not stated. CE without early stopping memorises noisy labels, which can inflate the distillation-vs-baseline gap that A4 rests on. | Figure 2/4/5 captions (dashed lines); Sec. 4 Implementations (no baseline settings); search for 'epoch', 'learning rate', 'early stop' finds none in Sec. 4 | gap | major | State the baseline protocol; add CE with early stopping on a held-out noisy validation split; low |
| R5 | technical_rigor | The privacy claim ('strong privacy protection', 'ensures privacy protection') is untested: there is no threat model, membership-inference or reconstruction attack, or formal guarantee. Whether distilled data protects privacy is contested in the distillation literature. | Abstract: "providing strong privacy protection through offline processing"; Sec. 5: "ensures privacy protection through offline dataset distillation"; text search: 'privacy' occurs only in claims (Abstract, Sec. 1, Sec. 3.2 Remark, Sec. 5), never in an experiment | error | major | Remove the privacy claim or add a membership-inference evaluation against the distilled sets; low (remove) or moderate (evaluate) |
| R6 | technical_rigor | The efficiency claim ('enhances training efficiency') is unmeasured. No distillation time, GPU memory or expert-trajectory cost is reported, and distillation itself (DATM needs expert trajectories trained on the full noisy data) is far costlier than one CE training run. | Abstract: "avoids the feedback loop common in existing techniques and enhances training efficiency"; search for 'GPU', 'hour', 'time' finds no measurement; Sec. 3.2 notes DATM's "significant scalability challenges" | error | major | Report end-to-end wall-clock and memory (expert training + distillation + student training) against CE and a noisy-label baseline; low |
| R7 | technical_rigor | The abstract and contributions state as a finding that tail-class clean samples are lossily compressed in imbalanced datasets, but Sec. 4 only hypothesises this; no imbalanced or long-tailed experiment exists. | Abstract: "clean but challenging samples, such as those from tail classes in imbalanced datasets, may undergo lossy compression"; Sec. 4: "We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets, are at risk" | error | major | Either run a long-tailed noisy experiment (e.g., CIFAR-10-LT with noise) or move the statement to future work; low-moderate |
| R8 | significance | The title's 'In the Wild' and the 'real-world' framing rest on CIFAR-10N/100N only (32x32 images re-annotated by crowd workers). The large real-noise benchmarks named in Sec. 3.1 (Clothing1M, WebVision) are not evaluated, and Tiny-ImageNet is used only with synthetic symmetric noise. | Title; Sec. 3.1: "high-volume datasets like Clothing1M [48] and WebVision [27] serve as classic benchmarks"; Sec. 4 Exp-III uses only CIFAR-10N/100N | judgment | major | Add Clothing1M or WebVision (mini) results, or retitle; moderate-high (DATM scalability) |
| R9 | experimental_validation | No result is given as a number: the paper has no tables, and every quantitative claim ('consistently outperform', 'significant performance gains') refers to curves in Figures 2, 4 and 5. Gains cannot be checked or compared with other work. | Text search: no 'Table' in the manuscript; Sec. 4 Observation-I: "consistently demonstrate significant performance gains" | gap | major | Add tables with accuracy per method x dataset x tau x IPC, and the baseline; low |
| R10 | experimental_validation | Seeds, number of runs and variance are not stated anywhere. At CIFAR scale several seeds are the norm, and some claimed effects (DATM 'comparable' under asymmetric noise; crossings near the dashed line) are of a size where run-to-run noise matters. | Text search: 'seed', 'runs', 'std' not found; Figure 2/4/5 captions describe only "solid lines" and "dashed lines" | gap | major | Report mean +- std over >= 3 seeds for distillation and baselines; moderate compute |
| R11 | technical_rigor | Possible selection on the test set: accuracies are 'reported throughout the distillation process' on the test set, and the figure captions call the same quantity 'validation performance'. If the best test accuracy over distillation iterations is reported, the curves are optimistically biased. | Sec. 4 Implementations: "Final test accuracies are reported throughout the distillation process"; Figure 2 caption: "The validation performance over symmetric noise" | question | major | State which checkpoint is reported and how it is chosen; use a held-out split for selection; low |
| R12 | novelty | The related work omits the closest prior art: robust subset/coreset selection under label noise (e.g., Mirzasoleiman, Cao, Leskovec, 'Coresets for Robust Training of Neural Networks against Noisy Labels', NeurIPS 2020) and prior studies of dataset distillation/condensation with noisy labels [verify]. Without them the novelty of 'a new perspective' cannot be placed. | Sec. 2.1-2.2 discuss noisy-label methods and distillation separately; no work combining the two is cited; literature check not run (no network) | judgment | major | Add a related-work paragraph on coreset selection under noise and on noisy-label dataset distillation, and position the delta; low |
| R13 | technical_rigor | The mechanism is asserted, not tested. 'Distillation captures common patterns while ignoring outliers such as noise' and 'asymmetric noise is absorbed into the distilled samples' are inferred from accuracy curves only. Nothing measures the label content of the distilled images, the influence of noisy samples, or the role of experts trained on noisy labels (DATM trajectories, DANCE phi_expert). | Sec. 4 Insight-I: "the distillation process primarily captures common patterns while ignoring outliers such as noise"; Sec. 4 Observation-II; Eqs. 4, 6-7 (experts trained on the noisy set) | gap | major | Add analyses: expert-epoch ablation for DATM, a probe of distilled-image class evidence (e.g., a clean-trained classifier on the synthetic set), influence of noisy samples; moderate |
| R14 | technical_rigor | The claim of avoiding the 'vicious cycle' is not demonstrated. The distillers depend on models trained on the noisy labels (DATM expert trajectories, DANCE's trained encoders), so the noise still shapes the result, only implicitly. No experiment contrasts the feedback-loop failure of existing methods with distillation. | Abstract: "This method avoids the feedback loop common in existing techniques"; Sec. 3.2 Eqs. 4, 6-7 | judgment | major | Narrow the claim, or show a setting where noise-estimation methods fail through their feedback loop and distillation does not; low (narrow) or moderate |
| R15 | significance | Contribution check: the paper proposes no method and benchmarks three existing distillers on noisy CIFAR-scale data. Its insights (symmetric noise averages out; structured noise is preserved; small IPC loses information) are close to what a reader would guess. The delta over distillation and noisy-label work is a refinement-level empirical study. | Sec. 2.2: "This work first benchmarks existing representative distillation approaches"; Sec. 1 Empirical Insights (I)-(III) | judgment | major | Turn the observations into a method (e.g., noise-aware distillation for structured noise) or a deeper analysis explaining when and why distillation denoises; high |
| R16 | significance | There is no practical recipe. The paper says choosing IPC depends on the unknown noise rate and leaves it open, so a practitioner cannot apply the approach without tuning on clean labels. | Sec. 4 Insight-I: "How much data should be distilled from a noisy dataset to create a meaningful distilled set?"; Insight-III | gap | minor | Propose and test an IPC-selection rule using only noisy data; moderate |
| R17 | experimental_validation | The evaluation is narrow by distillation standards: only the ConvNet used for distillation, with no cross-architecture evaluation of the distilled sets (standard in the distillation literature). Asymmetric and natural noise are not run on Tiny-ImageNet. | Sec. 4 Implementations (ConvNet only); Figure 4 (CIFAR-10/100 only); Figure 5 (CIFAR-N only) | gap | minor | Evaluate the distilled sets on ResNet-18/VGG; add Tiny-ImageNet asymmetric runs; moderate |
| R18 | clarity | Presentation slips: 'Realted Works', 'contributions bellow', 'Both of which' for three noise types; Eq. 4 uses theta-hat_{t+N} while the text defines theta-hat_{t+T}; 'Benchmark-I' is said to denote the accelerated variant of [9], not DATM itself; test vs validation wording is inconsistent (see R11). | Sec. 2 heading: "Realted Works"; Sec. 1: "major contributions bellow"; Sec. 3.1: "Both of which are widely employed"; Sec. 3.2 Eq. 4; Sec. 3.2: "Benchmark-I referenced later denotes this accelerated version" | error | minor | Proofread; clarify which DATM variant is used; low |
| R19 | clarity | The extracted layout (two columns, Figure 1 beside the abstract, bracketed numeric citations) suggests the manuscript is not in the ICLR template, which could be a formatting violation. This cannot be confirmed from extracted text. | Page 1 layout: abstract and Figure 1 caption interleaved in two columns | question | minor | Reformat in the ICLR 2026 template; low |
| R20 | reproducibility | Key distillation hyperparameters are missing: IPC grid, distillation iterations, expert epochs and trajectories for DATM, learning rates, augmentation for evaluation (except RCIG), and compute. No code release is mentioned. | Sec. 4 Implementations; search for 'epoch', 'iteration', 'learning rate', 'github' finds none | gap | major | Add a hyperparameter table per method/dataset and release code and noisy-label files; low |
| R21 | ethics | There is no limitations section. The privacy framing ('high-privacy environments') is promotional and its risks are not discussed: distilled images can leak training data, and Figure 3 is presented as recognisable images. | Abstract: "especially in high-privacy environments where noise is prevalent"; Sec. 5; Figure 3 | gap | minor | Add a limitations paragraph covering privacy leakage and scale; low |

### Answered

- Only symmetric noise is studied.: answered at Sec. 4 Experiment-II (asymmetric, Figure 4) and Experiment-III (CIFAR-10N/100N, Figure 5).
- Conclusions rest on a single distillation method.: answered at Sec. 3.2: DATM, DANCE and RCIG, one per family.
- The asymmetric noise construction is unspecified.: answered at Sec. 4 Implementations: TRUCK -> AUTOMOBILE, BIRD -> AIRPLANE, DEER -> HORSE, CAT <-> DOG; CIFAR-100 superclass flips.
- The CIFAR-N label sets and their noise rates are unspecified.: answered at Sec. 4 Experiment-III: Random k (~18%), Worst (40.21%), Aggre (9.03%), CIFAR-100N fine (40.20%).
- Is the evaluation protocol of each distiller altered?: answered at Sec. 4 Implementations: "following the evaluation protocols of DATM, DANCE, and RCIG, with data augmentation applied for RCIG as recommended".

### Aspect coverage

- novelty: A1; R12, R15
- technical soundness / theory: A5; R1, R2, R13, R14
- claim accuracy (E5): R5, R6, R7, R8
- experimental validation: A2, A3, A6, A9; R3, R4, R9, R10, R17
- evaluation protocol / leakage: R11 (question)
- significance: A4, A7, A10, A12; R15, R16
- clarity: A8; R18, R19
- reproducibility: A11; R20
- ethics / privacy / limitations: R5, R21
- statistical reporting: R10
- efficiency: A12; R6
- dataset licence / human subjects: considered, no reason (public benchmarks only; CIFAR-N annotations are public)
- figure integrity (E9): considered, not checkable (no page images)

Omission sweep (error_audit §4):
- Splits and selection split: not stated after search (R11).
- Seeds and variance: not stated (R10).
- Baseline settings: not stated (R4).
- Hyperparameters: not stated (R20).
- Compute: not stated (R6, R20).
- Licence: public data, no issue.
- Failure cases and limitations: asymmetric failure present (A5); no limitations section (R21).
- Code: not stated (R20).

### Pairs

- A4 ↔ R3, R4: whether the high-noise gain is meaningful against a fair or strong baseline (C2).
- A1 ↔ R12, R15: novelty of the distillation-as-denoiser perspective (C1).
- A12 ↔ R5, R6: the privacy and efficiency benefits (C1).
- A10 ↔ R1, R2: the corollaries' value (C5).
- A6 ↔ R8: 'in the wild' (C4).
- A3 ↔ R9, R10: whether the sweep can be checked (C2).
- A5 ↔ R13: the asymmetric-noise finding vs its asserted mechanism (C3).

---

## 3. Reorganized ledger and probes

### By claim

No duplicates were found that needed merging. The privacy part of R21 overlaps R5 but is kept separate: R21 is about the missing limitations discussion.

**C1: distillation as a new noisy-label approach that avoids the vicious cycle, improves efficiency, protects privacy**
- A1 (checked, high swing), A12 (checked), R3 (checked, high swing), R5 (checked, high swing), R6 (checked, high swing), R12 (open, high swing), R14 (checked, high swing), R15 (checked, high swing), R21 (checked)

**C2: symmetric-noise denoising**
- A2 (checked), A3 (open), A4 (open, high swing), A9 (open), R4 (checked, high swing), R9 (checked, high swing), R10 (checked), R11 (open, high swing), R13 (checked, high swing), R17 (checked)

**C3: asymmetric noise absorbed; tail classes compressed**
- A5 (checked), R7 (checked, high swing)

**C4: real-world natural noise ('in the wild')**
- A6 (checked), A7 (open), R8 (checked, high swing), R16 (checked)

**C5: Corollaries I-II**
- A10 (checked), R1 (checked, high swing), R2 (checked)

**general: General**
- A8 (checked), A11 (checked), R18 (checked), R19 (open), R20 (checked)

Swing ranking (highest first): R3, R15, R1, R4/A4, R5, R6, R7, R8, R9, R13, R14, R12, R11, A1. Every reason with worst case fatal (R3) was probed.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R1, R2, A10 | Is Corollary-II (Eq. 11) consistent with the settings the paper reports as successful, and with Corollary-I (Eq. 10)? | Recompute the bounds with the standard training-set sizes (CIFAR-10/100: 50,000; not stated in the paper) for the settings quoted in Sec. 4 Exp-I and Exp-III; compare the inequality directions of Eqs. 10 and 11. | confirmed: Corollary-II, Eq. 11; Sec. 4 Exp-I/III. Eq. 11 at CIFAR-10, IPC=50 gives tau >= 0.99 vs the reported success at tau=0.2; CIFAR-100N, IPC<10 gives tau >= 0.98 vs 40.20%. Eq. 10 rearranges to tau <= 1 - C*IPC/\|S\|, the reverse of Eq. 11. Eq. 10 gives IPC <= 4,000 at tau=0.2, vacuous for IPC 1-50. No proof anywhere. | R1 open -> checked (error confirmed by recomputation); R2 open -> checked; A10 weak (condition fails) |
| P2 | R3, A4 | Does Sec. 4 compare distillation with any noisy-label learning method beyond CE on the full noisy set? | Re-read Sec. 4 and all figure captions; search for the cited methods (Co-teaching, DivideMix, GCE, DISC) outside Sec. 2. | confirmed: Figure 2/4/5 captions; Sec. 4. The only reference line is "training on the full dataset at the corresponding noise rate". Cited methods appear only in Sec. 1-2. | R3 open -> checked (gap confirmed); A4 depends on R4 |
| P3 | R4, A4 | Is the full-data baseline's training protocol (architecture, epochs, early stopping, augmentation) given anywhere? | Search the full text for 'epoch', 'learning rate', 'early stop', 'augmentation', 'baseline'. | confirmed: Sec. 4 Implementations. No baseline protocol is given. 'Early stopping' appears only in reference [25]; augmentation is mentioned only for RCIG's distilled-set evaluation. | R4 open -> checked; A4 stays moderate but conditional |
| P4 | R5, R6, A12, R21 | Is there any experiment or measurement behind the privacy and efficiency claims? | Search for 'privacy', 'efficien', 'GPU', 'hour', 'time', 'memory', 'attack', 'membership'. | confirmed: Abstract; Sec. 1; Sec. 3.2 Remark; Sec. 5. 'Privacy' occurs 6 times, all in claims. 'Efficien' occurs only in claims and in describing [9] and [30]. No timing, memory or attack results. | R5, R6 open -> checked (E5 claim distortion confirmed); A12 weak |
| P5 | R7 | Does any experiment test the imbalanced/tail-class claim made in the abstract and contributions? | Search for 'imbalanc', 'tail', 'long-tail'; re-read Sec. 4. | confirmed: Sec. 4 after Insight-II. All 4 'imbalanc' hits are claims or the hypothesis: "We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets...". No experiment. | R7 open -> error (checked) |
| P6 | R11 | Is the reported accuracy the final, a fixed-iteration or the best test accuracy over distillation, and is any validation split used for selection? | Re-read Sec. 4 Implementations and the figure captions. | unsettled: Sec. 4 Implementations; Figure 2/4 captions. "Final test accuracies are reported throughout the distillation process" can mean either a final-iteration value or a running maximum. The captions say 'validation performance'; no validation split is defined. | R11 stays open (question; no grade above minor) |
| P7 | R9, R10 | Does the paper give numbers or variance for any result? | Search for 'Table', 'seed', 'runs', 'std', 'mean'; read the captions of Figures 2, 4, 5. | confirmed: whole manuscript. No tables. No seeds or runs stated. The captions describe solid trend lines and dashed reference lines only; whether the plots show bands cannot be seen. | R9 open -> checked; R10 open -> checked (not stated after search) |
| P8 | R8, A6 | Which real-noise datasets are actually evaluated? | Trace C4 from Sec. 3.1 to Sec. 4 Exp-III and Figure 5. | confirmed: Sec. 3.1; Sec. 4 Exp-III; Figure 5. Only CIFAR-10N and CIFAR-100N. Clothing1M and WebVision are introduced in Sec. 3.1 but never used. | R8 open -> checked; A6 moderate (limited scale) |
| P9 | R12, A1 | Is there prior work on distillation or subset selection for learning with noisy labels that the paper omits? | Re-read Sec. 2; literature query not possible (no network). Rely on memory, with [verify] where unsure. | unsettled: Sec. 2.1-2.2. No combined work is cited. From memory, robust coreset selection under label noise (Mirzasoleiman, Cao, Leskovec, NeurIPS 2020) is directly related. Prior noisy-label dataset-distillation studies may exist [verify]. Not settled without a search. | R12 stays open (judgment, novelty rests on memory, [verify]) |
| P10 | R13, R14 | Are the distillers' teacher/expert models trained on the noisy labels, so that noise enters distillation implicitly? | Re-read Sec. 3.2: Eq. 4 (expert trajectories theta*), Eqs. 6-7 (phi_expert), Eqs. 8-9 (RCIG trained against L_T on the full noisy training set); check for an analysis of this. | confirmed: Sec. 3.2 Eqs. 4, 6-9; Sec. 3.1 Training Protocol. Experts are 'trained on real images', which in this setup are the noisy set S-tilde. L_T is the loss on the full training set. No ablation of expert epochs or of the expert's noise exposure. | R13 open -> checked; R14 open -> checked |
| P11 | A3, A4, A7, A9 | Can the figure-based accept reasons be verified from the text? | Trace each claim to its figure; check the textual statements for internal consistency. | partly: Sec. 4 Exp-I/III; Figures 2, 3, 5. The text statements agree with one another (gain grows with noise; Aggre is the weak case). The magnitudes and the curves themselves cannot be read from the extracted text. | A3, A4, A7, A9 stay open (figure-dependent) |

P1 computation: Eq. 11 bound = 1 - C·IPC/|S̃|. CIFAR-10, C=10, IPC=50, |S̃|=50,000 gives 0.99. IPC=1 gives 0.9998. CIFAR-100N, C=100, IPC=10 gives 0.98. Eq. 10, |S̃|(1-τ)/C at τ=0.2, gives 4,000. Training-set sizes are the standard ones; the paper does not state them.

---

## 4. Reviewer roster

Aspects with ≥ 12% of the ratio are technical_rigor (28%), novelty (20%), significance (20%) and experimental_validation (14%); each has at least one type. Clarity (10%), reproducibility (5%) and ethics (4%) fall below 12%. Their reasons sit in T2's, T4's and T6's 'Weighs most', and the script renormalizes their shares away.

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Learning-with-noisy-labels specialist | experimental_validation | the task: learning with noisy labels | robust training under label noise (sample selection, robust losses, semi-supervised correction) on CIFAR-N/Clothing1M/WebVision | competitive comparison with standard noisy-label baselines on standard benchmarks and backbones | weak CE baselines without early stopping; CIFAR-only 'real-world' claims; no numbers | R3, R4, R8, R9, R10, R11, R16, A3, A4, A6 | high |
| T2 Dataset distillation researcher | novelty | neighbor: dataset distillation / condensation | trajectory-, distribution- and kernel-based dataset distillation; evaluation protocols of DD benchmarks | a new mechanism or a new understanding of what distilled data encodes; standard DD protocols (cross-architecture, multiple IPC) | benchmark-only studies of existing distillers; missing cross-architecture evaluation; unexplained mechanisms | R12, R13, R15, R17, R18, A1, A2, A8, A9 | high |
| T3 Learning-theory reviewer (memorization and generalization under label noise) | technical_rigor | neighbor: learning theory | theory of memorization, early learning and generalization with noisy labels | precise statements with assumptions and proofs; theory consistent with experiments | 'corollaries' with no derivation; probabilistic statements with undefined probability spaces | R1, R2, R13, R14, R7, A10, A5 | medium |
| T4 Evaluation and protocol methodologist | technical_rigor | neighbor: ML evaluation methodology | experimental protocol, claim-to-evidence tracing, statistical reporting | every claim backed by a reported, reproducible measurement with variance and a clean selection protocol | claims in the abstract with no experiment; test-set selection; figures without numbers | R5, R6, R7, R9, R10, R11, R19, R20, A11, A2 | medium |
| T5 Data-centric ML researcher (coreset selection and data pruning) | significance | neighbor: data-centric ML, coreset selection / data pruning | subset selection, data pruning and data valuation, including under label noise | a usable data-curation recipe that beats selection baselines at matched budget | ignoring selection baselines at the same budget; no recipe for choosing the budget | R12, R15, R16, R3, R6, A4, A7, A12 | medium |
| T6 Privacy and trustworthy-ML researcher | significance | neighbor: privacy-preserving ML | membership inference, data reconstruction, privacy of synthetic and distilled data | privacy claims backed by a threat model and attacks, or a formal guarantee | 'privacy for free' claims from synthetic data; promotional framing | R5, R21, R6, R8, R15, A10, A12 | low |

Mix: T1 is the task specialist. T2-T6 are outside types drawn from the neighbors identified in Step 0. Every ledger item appears in at least one type's 'Weighs most'.

---

## 5. Reviews

### T1: Learning-with-noisy-labels specialist (experimental_validation; the task: learning with noisy labels)

**Reading of the ledger.**
- Holds A3 (the sweep over tau and IPC is the right shape of experiment) and A6 (CIFAR-N is the community's standard human-noise test).
- Discounts A4: a single CE run on the full noisy set, of unstated protocol (R4), is the weakest reference available. Co-teaching- or DivideMix-style methods, cited in Sec. 2.1, are the obvious stronger references, and the paper never runs them. Discounts A1: a framing that is never compared against the methods it critiques cannot show it is better.
- R3: fatal. The paper's stated contribution is 'a new approach to model learning from noisy data' (Sec. 5), and no noisy-label method is run.
- R4: major. Without early stopping, CE memorises noise, so the dashed lines may be artificially low.
- R8: major. 'In the Wild' rests on 32x32 CIFAR-N; Clothing1M/WebVision are named but not run.
- R9: major. Without tables I cannot compare against any published number.
- R10: minor. Single runs are common in distillation papers and the claimed gaps at high noise are large. (Updated after P12: minor -> major; R10 is not decisive for T1, so the scores are unchanged.)
- R11: minor (unsettled question).
- R16: minor. Choosing IPC without knowing tau is an open problem the paper names honestly.

**Opinion.** From the noisy-label side, the question is simple: if I have a noisy CIFAR-10, should I distil it instead of running a standard robust-training method? The paper cannot answer this, because the only comparison is against vanilla cross-entropy on the full noisy data, with an unreported protocol (R3, R4). Beating that reference at tau=0.8 with IPC=1 (A4) is interesting, but it mostly restates that unregularised CE memorises noise, which the paper itself cites [1, 47]. The experiments have the right shape (A3, A6), but they report no numbers (R9) and the 'wild' setting is CIFAR-N only (R8). Asymmetric noise, the common case in practice, is where distillation fails (A5), which further limits its practical use. What would change my mind: a table on CIFAR-10N/100N and one large real-noise set, with CE+early stopping, Co-teaching, GCE and DivideMix on the same and on a standard backbone. Distillation would need to be competitive, or to offer a clearly argued trade-off such as cost or privacy, measured.

Decisive: R3 (fatal), R4 (major), R9 (major), A6 (moderate, held)

**Scores.** Pool position 15 (better than about 15% of ICLR 2026 submissions; basis: R3 (fatal), R4 (major), R9 (major), A6 (moderate, held)). Technical Rigor 40, Clarity 52, Novelty 45, Significance 38, Experimental Validation 30, Reproducibility 42, Ethics 58. Overall 2 (Reject). Confidence 4.

### T2: Dataset distillation researcher (novelty; neighbor: dataset distillation / condensation)

**Reading of the ledger.**
- Holds A1: framing distillation as a denoiser is a genuinely new use of the tool in this literature. Holds A2: one method per family is the right design. Holds A8.
- Discounts A9: one IPC=1 image grid (not visible here) is not evidence of what the synthetic set encodes.
- R12: minor. Coreset selection under noise is a different mechanism (selection, not synthesis), so I see the transfer to synthetic distillation as the paper's delta. Noisy-label DD prior work is unverified.
- R13: major. DATM matches early segments of expert trajectories, and early training is known to fit clean labels first. That alone could explain Insight-I, and the paper never ablates it.
- R15: major. The study runs existing distillers with no modification.
- R17: major. Cross-architecture evaluation is standard in DD; a ConvNet-only result says little.
- R18: minor.

**Opinion.** I find the core observation, that distillers act as implicit label denoisers under symmetric noise, a worthwhile idea for the distillation community (A1), studied across the three main families (A2). But the paper stops at the observation. Contribution check: (1) What does a reader learn? That symmetric noise mostly averages out in distillation and structured noise does not. This is plausible a priori, and no 'why' is established (R13). (2) Does the setting support 'in the wild'? No, only CIFAR-N (R8). (3) The delta is a refinement: existing DATM/DANCE/RCIG, unmodified, on noisy CIFAR (R15). (4) Transfer to practical settings is doubtful without cross-architecture and larger-scale results (R17). The obvious next step is missing: a noise-aware distiller that handles the asymmetric case, which the paper's own Insight-II motivates. It would turn this into a method paper. As it stands it is an interesting workshop-level study. I would raise my view with a mechanism analysis (expert-epoch ablation, label content of the distilled images) and a modest method for structured noise.

Decisive: R15 (major), R13 (major), A1 (moderate, held), A2 (held)

**Scores.** Pool position 30 (better than about 30% of ICLR 2026 submissions; basis: R15 (major), R13 (major), A1 (moderate, held), A2 (held)). Technical Rigor 46, Clarity 56, Novelty 50, Significance 46, Experimental Validation 45, Reproducibility 48, Ethics 60. Overall 3 (Borderline Reject). Confidence 4.

### T3: Learning-theory reviewer (memorization and generalization under label noise) (technical_rigor; neighbor: learning theory)

**Reading of the ledger.**
- Holds A5: the asymmetric-noise failure is an honest and informative negative result.
- Discounts A10: the noise-rate estimate is built on Eq. 11, which P1 shows is inconsistent with the data.
- R1: major. Eq. 11 yields tau >= 0.99 for CIFAR-10 at IPC=50, contradicting Sec. 4; it is not a main claim, but it is presented as a result.
- R2: major. Neither corollary has a proof or assumptions; Eq. 10 is vacuous.
- R13: major. The 'common patterns first' mechanism is borrowed from memorization theory [1] but never tested in distillation.
- R14: major. The experts see noisy labels, so the noise is not avoided.
- R7: minor. The tail-class claim is an overstatement, but it is labelled a hypothesis in Sec. 4.

**Opinion.** The paper's conceptual link between memorization (networks fit common patterns first) and distillation (distillers synthesise common patterns) is suggestive. The formal content does not hold up. Corollary-I (Eq. 10) is the trivial statement that one cannot keep more clean samples per class than exist, and it never constrains the IPC range studied (R2). Corollary-II (Eq. 11) reverses that inequality without derivation. With the paper's own settings it predicts noise rates of 98-99.98% whenever a few distilled images match full-data accuracy, contradicting the reported tau=0.2 and 40% cases (R1). Neither has a proof, a probability space or a definition of delta. The mechanism claims (R13, R14) are the interesting science here, and they are only asserted: an expert-trajectory-length ablation would directly test whether distillation inherits early-learning robustness. I would need the corollaries removed or proved correctly, and one mechanistic experiment, before I could see the paper as sound.

Decisive: R1 (major), R2 (major), R13 (major)

**Scores.** Pool position 15 (better than about 15% of ICLR 2026 submissions; basis: R1 (major), R2 (major), R13 (major)). Technical Rigor 32, Clarity 48, Novelty 44, Significance 38, Experimental Validation 38, Reproducibility 40, Ethics 55. Overall 2 (Reject). Confidence 4.

### T4: Evaluation and protocol methodologist (technical_rigor; neighbor: ML evaluation methodology)

**Reading of the ledger.**
- Holds A11 (public data and public distillers make re-running possible) and A2.
- R5: major. A headline claim in the abstract and conclusion with zero evidence (P4).
- R6: major. Same; and distillation cost likely exceeds plain training.
- R7: major. The abstract reports as a finding what Sec. 4 calls a hypothesis (P5).
- R9: major. No tables at all.
- R10: major. CIFAR-scale experiments should report >= 3 seeds.
- R11: minor (unsettled; the wording is ambiguous).
- R19: minor (unverifiable from text).
- R20: major. Hyperparameters for three distillers on three datasets are absent.

**Opinion.** I traced each claim in the abstract to its evidence. 'Denoises symmetric noise' leads to Figure 2, with curves but no numbers. 'Struggles with asymmetric noise' leads to Figure 4. 'Effective on natural noise' leads to Figure 5, CIFAR-N only. 'Tail classes are lossily compressed' leads to no experiment (R7). 'Enhances training efficiency' leads to no measurement (R6). 'Strong privacy protection' leads to no analysis (R5). So three of the six abstract claims have no supporting experiment, and the other three are supported only by figures, with no numbers (R9), no variance (R10) and an ambiguous checkpoint-selection protocol (R11). Reproduction would also be hard: no IPC grid, no iteration counts, no expert settings (R20). Fixing the reporting is cheap: tables, seeds, a selection statement, and narrowing the abstract. Fixing the evidence for privacy and efficiency is moderate work. Until then I cannot treat the conclusions as established.

Decisive: R5 (major), R7 (major), R9 (major), R20 (major)

**Scores.** Pool position 15 (better than about 15% of ICLR 2026 submissions; basis: R5 (major), R7 (major), R9 (major), R20 (major)). Technical Rigor 34, Clarity 46, Novelty 45, Significance 40, Experimental Validation 34, Reproducibility 35, Ethics 48. Overall 2 (Reject). Confidence 4.

### T5: Data-centric ML researcher (coreset selection and data pruning) (significance; neighbor: data-centric ML, coreset selection / data pruning)

**Reading of the ledger.**
- Holds A4 (the high-noise effect is surprising to a data-pruning reader) and A7 (the trade-off is real and worth stating).
- Discounts A12: there is no cost accounting (R6).
- R12: major. Robust coreset selection under label noise addresses the same goal, a small subset that trains well despite noise, and it is the natural matched-budget baseline. Its absence leaves the delta unplaced.
- R15: major. No method.
- R16: major. Without an IPC rule the approach is not usable, and this is central to significance.
- R3: major. Selection and noisy-label baselines are both missing.
- R6: major.

**Opinion.** To a data-curation reader, the paper's real claim is that synthesis beats selection or full data under heavy symmetric noise. That is worth knowing (A4), but the matched-budget comparison is missing: a coreset or small-loss selection at the same IPC (R12, R3). Without it, the effect might come from compressing the data, not from distilling it. Significance is limited further because the budget (IPC) has to be chosen with knowledge of tau, which the paper admits is open (R16), and because the failure under asymmetric noise covers much of practical label noise. Contribution check: the reader learns a plausible regularity, not why it holds; the delta is an application of existing distillers; and transfer to large, realistic noisy datasets is untested (R8). I would move up with a matched-budget selection baseline and a noisy-data-only IPC rule.

Decisive: R12 (major), R16 (major), R15 (major), A4 (held)

**Scores.** Pool position 22 (better than about 22% of ICLR 2026 submissions; basis: R12 (major), R16 (major), R15 (major), A4 (held)). Technical Rigor 42, Clarity 52, Novelty 42, Significance 40, Experimental Validation 40, Reproducibility 45, Ethics 58. Overall 2 (Reject). Confidence 3.

### T6: Privacy and trustworthy-ML researcher (significance; neighbor: privacy-preserving ML)

**Reading of the ledger.**
- Discounts A12 and A10: the privacy and efficiency benefits are asserted, not shown.
- R5: major. 'Ensures privacy protection' is a strong claim, and whether distilled data protects membership privacy is contested in the literature, so it needs evidence.
- R21: minor. No limitations discussion of leakage.
- R6: minor (outside my expertise).
- R8: minor.
- R15: major. Without the privacy evidence, what remains is a benchmark of existing distillers.

**Opinion.** The paper sells its approach partly on privacy: it 'ensures privacy protection through offline dataset distillation' and suits 'high-privacy environments'. Nothing in the manuscript tests this (R5). There is no threat model, no membership-inference or reconstruction attack on the distilled sets, and no differential-privacy accounting. The distillers also need full access to the raw labelled data, which is where the privacy risk lies. Figure 3 is described as showing recognisable class images, so leakage is at least plausible and deserves a limitations paragraph (R21). If the privacy claim were removed, my significance assessment would rest on the denoising observation alone, which I see as modest (R15). Adding a standard membership-inference evaluation, or dropping the claim, would remove my main objection.

Decisive: R5 (major), R15 (major)

**Scores.** Pool position 22 (better than about 22% of ICLR 2026 submissions; basis: R5 (major), R15 (major)). Technical Rigor 40, Clarity 54, Novelty 46, Significance 40, Experimental Validation 40, Reproducibility 45, Ethics 45. Overall 2 (Reject). Confidence 3.

Contribution check. T2 and T5 answer the four questions inside their opinions. T6, the other significance type, answers them here:
1. What does a reader learn? A plausible regularity, not why it holds (R13, R15).
2. Does the setting support the framing? No: 'in the wild' and 'privacy' are not operationalized (R8, R5).
3. Is the delta conceptual or a refinement? A refinement: existing distillers applied unmodified (R15).
4. Would the conclusions transfer? Doubtful beyond CIFAR-scale ConvNets (R8, R17).

T1, T3 and T4 do not score novelty or significance as their primary aspect.

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P12 | T1 (minor) vs T4 (major) on R10 | Do the captions or text of Figures 2, 4 and 5 indicate variance bands or multiple runs (T1 assumed variance might be shown in the figures; T4 assumed it is absent)? | partly: The captions describe only solid accuracy lines and dashed full-data lines. Nothing mentions bands, means or runs, and the plots cannot be seen. | T1: R10 minor -> major (updated after P12); not decisive for T1, so T1's scores are unchanged |

Value splits that stay:
- R3: T1 fatal, T5 major. Both agree on the fact (P2); they differ on how central a noisy-label comparison is to an analysis paper.
- R12: T2 minor, T5 major. Whether coreset selection under noise covers synthetic distillation is a matter of field perspective.
- R6: T4 and T5 major, T6 minor.
- R8: T1 major, T6 minor.

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 | experimental_validation | 0.169 | 15 | 2 | 4 |
| T2 | novelty | 0.247 | 30 | 3 | 4 |
| T3 | technical_rigor | 0.169 | 15 | 2 | 4 |
| T4 | technical_rigor | 0.169 | 15 | 2 | 4 |
| T5 | significance | 0.124 | 22 | 2 | 3 |
| T6 | significance | 0.124 | 22 | 2 | 3 |

- **Aspect-weighted rating:** 2.25 → **final rating 2 (Reject)**. ICLR's own label: **2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10})**. ICLR sub-scores: Soundness 1, Presentation 2, Contribution 1. Scale status: secondary (recent analyses), so check it against the current form.
- Weighted pool position 20.4; plain mean 2.17; spread 1 (2 to 3).
- Uncovered aspects and warnings: none. Clarity, reproducibility and ethics fall below 12% and have no type; their shares were renormalized away by design.
- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

**Paper type**: analysis  
**Weights**: Technical Rigor 0.25, Clarity & Presentation 0.10, Novelty & Originality 0.20, Significance & Impact 0.20, Experimental Validation 0.15, Reproducibility 0.05, Ethical Compliance 0.05

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| T1 (Learning-with-noisy-labels specialist) | 4 | 0.85 | 1.00 | 18% |
| T2 (Dataset distillation researcher) | 4 | 0.85 | 1.00 | 18% |
| T3 (Learning-theory reviewer (memorization and generalization under label noise)) | 4 | 0.85 | 1.00 | 18% |
| T4 (Evaluation and protocol methodologist) | 4 | 0.85 | 1.00 | 18% |
| T5 (Data-centric ML researcher (coreset selection and data pruning)) | 3 | 0.70 | 1.00 | 15% |
| T6 (Privacy and trustworthy-ML researcher) | 3 | 0.70 | 1.00 | 15% |

*No EIC quality weights given yet: the EIC assessment uses confidence only. Add `eic_weight` (0.5-1.5) per reviewer after the EIC's meta-review.*

#### Official scores and EIC assessment

| Dimension | T1 (Learning-with-noisy-labels specialist) | T2 (Dataset distillation researcher) | T3 (Learning-theory reviewer (memorization and generalization under label noise)) | T4 (Evaluation and protocol methodologist) | T5 (Data-centric ML researcher (coreset selection and data pruning)) | T6 (Privacy and trustworthy-ML researcher) | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 40 | 46 | 32 | 34 | 42 | 40 | 39.0 | 38.9 | 14 |
| Clarity & Presentation | 52 | 56 | 48 | 46 | 52 | 54 | 51.3 | 51.2 | 10 |
| Novelty & Originality | 45 | 50 | 44 | 45 | 42 | 46 | 45.3 | 45.4 | 8 |
| Significance & Impact | 38 | 46 | 38 | 40 | 40 | 40 | 40.3 | 40.4 | 8 |
| Experimental Validation | 30 | 45 | 38 | 34 | 40 | 40 | 37.8 | 37.7 | 15 |
| Reproducibility | 42 | 48 | 40 | 35 | 45 | 45 | 42.5 | 42.3 | 13 |
| Ethical Compliance | 58 | 60 | 55 | 48 | 58 | 45 | 54.0 | 54.2 | 15 |
| **Composite** | 41.3 | 48.5 | 39.7 | 39.4 | 43.2 | 43.1 | **42.5** | **42.5** | |
| Pool position (P%) | 15 | 30 | 15 | 15 | 22 | 22 | | | |

#### Ratings (the decision's starting point)

**Official reviewer ratings (Overall 1-6)**: T1 (Learning-with-noisy-labels specialist) 2, T2 (Dataset distillation researcher) 3, T3 (Learning-theory reviewer (memorization and generalization under label noise)) 2, T4 (Evaluation and protocol methodologist) 2, T5 (Data-centric ML researcher (coreset selection and data pruning)) 2, T6 (Privacy and trustworthy-ML researcher) 2 → official mean **2.17**  
**EIC-weighted rating** (internal): **2.18** (+0.01 vs. official) → starting point **2 (Reject)**

⚠ = spread > 20 points: discuss this disagreement in the decision.

**Composite cross-check (0-100)**: official 42.5 → 2 · EIC-weighted 42.5 → 2 (+0.0 vs. official)  
**Decision ceiling**: none (no upheld DA-CRITICAL issue). The EIC's decision starts from the EIC-weighted rating and may depart from it in either direction, with a written reason.
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Learning-with-noisy-labels specialist) | experimental_validation | 14% | 0.169 |
| T2 (Dataset distillation researcher) | novelty | 20% | 0.247 |
| T3 (Learning-theory reviewer (memorization and generalization under label noise)) | technical_rigor | 28% | 0.169 |
| T4 (Evaluation and protocol methodologist) | technical_rigor | 28% | 0.169 |
| T5 (Data-centric ML researcher (coreset selection and data pruning)) | significance | 20% | 0.124 |
| T6 (Privacy and trustworthy-ML researcher) | significance | 20% | 0.124 |

**Final rating (aspect-weighted mean)**: **2.25** → **2 (Reject)** · plain mean 2.17 · weighted pool position 20.4
### Cross-Venue Outlook

| Venue | Venue-weighted composite | Bar offset | Venue shift | Band → with DA cap | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|---|
| ICLR (2026) | 42.3 | +0 | +0 | 2 → 2 | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) | Soundness 1, Presentation 2, Contribution 1 | secondary |

Emphasis weights are this skill's heuristics, not official venue weights. Scale status: official / confirmed / secondary / assumed / unpublished (see references/venue_profiles.md). Upheld DA-CRITICAL caps apply to every venue.

- **ICLR**: Soundness/Presentation/Contribution 1-4 and Confidence 1-5 are long-standing. Overall rating reported as {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}. Both are shown.


</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| A1 | 2 of 6 | T1 discounted, T2 held |
| A2 | 2 of 6 | T2 held, T4 held |
| A3 | 1 of 6 | T1 held |
| A4 | 2 of 6 | T1 discounted, T5 held |
| A5 | 1 of 6 | T3 held |
| A6 | 1 of 6 | T1 held |
| A7 | 1 of 6 | T5 held |
| A8 | 1 of 6 | T2 held |
| A9 | 1 of 6 | T2 discounted |
| A10 | 2 of 6 | T3 discounted, T6 discounted |
| A11 | 1 of 6 | T4 held |
| A12 | 2 of 6 | T5 discounted, T6 discounted |
| R1 | 1 of 6 | T3 major |
| R2 | 1 of 6 | T3 major |
| R3 | 2 of 6 | T1 fatal, T5 major |
| R4 | 1 of 6 | T1 major |
| R5 | 2 of 6 | T4 major, T6 major |
| R6 | 3 of 6 | T4 major, T5 major, T6 minor |
| R7 | 2 of 6 | T3 minor, T4 major |
| R8 | 2 of 6 | T1 major, T6 minor |
| R9 | 2 of 6 | T1 major, T4 major |
| R10 | 2 of 6 | T1 major, T4 major |
| R11 | 2 of 6 | T1 minor, T4 minor |
| R12 | 2 of 6 | T2 minor, T5 major |
| R13 | 2 of 6 | T2 major, T3 major |
| R14 | 1 of 6 | T3 major |
| R15 | 3 of 6 | T2 major, T5 major, T6 major |
| R16 | 2 of 6 | T1 minor, T5 major |
| R17 | 1 of 6 | T2 major |
| R18 | 1 of 6 | T2 minor |
| R19 | 1 of 6 | T4 minor |
| R20 | 1 of 6 | T4 major |
| R21 | 1 of 6 | T6 minor |

### Key strengths

- A2: the study covers the three main distillation families. Held by T2 and T4 (2 of 6).
- A1: a new perspective, distillation as an implicit label denoiser. Held by T2, discounted by T1.
- A4: under heavy symmetric noise, IPC=1 beats the full noisy-data baseline. Held by T5, discounted by T1 because of R4.
- A5 and A6: an honest negative result under asymmetric noise, and a human-noise test on CIFAR-N. Held by T3 and T1 respectively.

No accept reason was held by a majority of types.

### Top concerns (at most five)

1. R15: no method; existing distillers are benchmarked on noisy CIFAR, and the insights are close to expected (Sec. 2.2; Sec. 1 Insights I-III). Graded major by 3 of 6 types (T2, T5, T6). Fix: develop a noise-aware distiller for structured noise, or a mechanistic analysis; high cost.
2. R3: no noisy-label baselines. The only reference is CE on the full noisy set (Figure 2/4/5 captions; Sec. 5). Graded fatal by T1 and major by T5. Fix: add CE+early stopping, Co-teaching, GCE and DivideMix on the same backbone; a few GPU-days.
3. R5: the privacy claim ('strong privacy protection', 'ensures privacy protection') is untested (Abstract; Sec. 5; P4). Graded major by T4 and T6. Fix: remove it or run membership inference; low to moderate.
4. R13: the mechanism is asserted, not tested, and the experts are trained on noisy labels (Sec. 4 Insight-I; Eqs. 4, 6-7; P10). Graded major by T2 and T3. Fix: expert-epoch ablation and an analysis of the distilled images' label content; moderate.
5. R9: no tables; every result is a curve in Figures 2, 4 and 5 (P7). Graded major by T1 and T4. Fix: tables of accuracy per method, dataset, tau and IPC; low.

Also graded major by two types: R6, efficiency unmeasured (T4, T5); R10, no seeds or variance (T4, and T1 after P12).

### Revision Roadmap

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R3 | Compare with standard noisy-label methods (CE+early stopping, Co-teaching, GCE, DivideMix) on the same ConvNet and on ResNet-18, on CIFAR-10/100 sym/asym and CIFAR-N | moderate: a few GPU-days at CIFAR scale |
| 1 | R15 | Turn the observations into a contribution beyond benchmarking: a noise-aware distiller (e.g., one handling structured noise), or a mechanistic account of when and why distillation denoises | high |
| 2 | R1, R2 | Remove Corollary-II or prove both corollaries with stated assumptions consistent with Figs. 2/5 | low (remove) to moderate |
| 2 | R4 | State the baseline protocol; add CE with early stopping on a noisy validation split | low |
| 2 | R5, R21 | Drop the privacy claim, or add a membership-inference evaluation and a limitations paragraph | low / moderate |
| 2 | R6 | Report end-to-end cost (expert trajectories + distillation + training) against CE | low |
| 2 | R7 | Run a long-tailed noisy experiment, or move the tail-class statement out of the abstract | low to moderate |
| 2 | R8 | Add Clothing1M or (mini-)WebVision, or retitle away from 'In the Wild' | moderate to high |
| 2 | R9, R10 | Add tables of accuracies with mean ± std over ≥ 3 seeds | low to moderate |
| 2 | R12 | Discuss coreset selection under noise and prior noisy-label distillation work; add a matched-budget selection baseline | low to moderate |
| 2 | R13, R14 | Ablate expert epochs and expert noise exposure; analyse the label content of the distilled images; narrow the 'avoids the vicious cycle' claim | moderate |
| 2 | R16 | Propose an IPC-selection rule that uses only noisy data | moderate |
| 2 | R17 | Evaluate the distilled sets across architectures; add Tiny-ImageNet asymmetric runs | moderate |
| 2 | R20 | Add a hyperparameter table for each method and dataset; release code and noisy labels | low |
| 3 | R11 | State the checkpoint-selection protocol and use a held-out split | low |
| 3 | R18, R19 | Proofread, fix notation (Eq. 4), and use the ICLR template | low |

---

## 8. Integrity signals and limitations

- **Integrity signals:** `integrity_scan.py` found nothing (0 findings). No text addressed to reviewers or AI systems was seen while reading. The '[REDACTED: venue/acceptance mark]' in reference [10] comes from blinding and is not an injection. These never change a score.
- **Limitations of this review:**
  - Figures 1-5 were unavailable, so every quantitative statement was judged from text and captions (A3, A4, A7, A9 stay open). Whether the plots carry variance bands is unknown (P12).
  - Some equations were partly garbled by extraction and were not used for any error. Eqs. 10 and 11 were readable.
  - P1 uses the standard CIFAR training-set sizes, which the paper does not state.
  - The literature check did not run (no network). R12's novelty basis rests on memory and is marked [verify] where unsure.
  - The template inference (R19) comes from the extracted layout only.
  - The six types share one context, so their agreement is not independent confirmation.
  - The paper's title was familiar from prior knowledge. Nothing about its reception or outcome was used.
