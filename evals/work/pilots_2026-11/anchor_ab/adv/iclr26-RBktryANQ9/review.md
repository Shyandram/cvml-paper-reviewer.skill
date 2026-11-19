# Peer Review: Dataset Distillers Are Good Label Denoisers In the Wild

| | |
|---|---|
| Date | 2026-11-19 |
| Mode | full (ledger review) |
| Paper type | analysis (empirical benchmarking of existing methods to derive insights; no new method) |
| Field, sub-area | machine learning / computer vision; learning with noisy labels, dataset distillation |
| Task | Learning with noisy labels for image classification (adapted from "Image classification, representation learning"); second task: dataset distillation / condensation (not listed; generated) |
| Neighboring fields | data-centric ML: coreset selection and data pruning (listed as "data-centric ML", expanded); learning theory of memorization and early learning (listed as "learning theory"); privacy-preserving ML (from the "Robustness, safety, privacy" row, generated from the paper's privacy claim); dataset distillation (generated) |
| Target venue | ICLR 2026 (stated by the user). The layout looks like a CVF-style template rather than ICLR's (see R18); ICLR profile used. |
| Aspect ratio | (`aggregate_scores.py ratio --paper-type analysis --venue iclr`) technical_rigor 28%, novelty 20%, significance 20%, experimental_validation 14%, clarity 10%, reproducibility 5%, ethics 4% |
| Literature check | not run: no network access in this evaluation. Novelty reasons that rest on memory are marked [verify]. |

One context: the reviewer types share one model and one reading, so their judgments are not independent.

The paper text was extracted from the PDF and the figures were not available. Every result in the paper is reported only as curves in Figures 2, 4 and 5; there are no tables. Figure-dependent claims are judged from the captions and the prose alone, and this is noted where it matters.

---

## 1. Paper memory

**Claims.**
- C1: "for symmetric noise, existing dataset distillation methods serve as effective denoising tools" (Abstract; Section 1 Empirical Insights (I); Section 4 Observation-I / Insight-I; Figure 2).
- C2: Structured asymmetric noise "can also be absorbed into the distilled samples, which hinders robust training" (Abstract; Section 1 (II); Section 4 Observation-II / Insight-II; Figure 4).
- C3: Under real-world natural noise, dataset distillation "remain[s] effective even in the presence of an unknown fixed noise rate" (Title "In the Wild"; Section 1 (III); Section 4 Observation-III / Insight-III; Figure 5).
- C4: Clean but challenging samples (tail classes of imbalanced datasets) "may undergo lossy compression during distillation" (Abstract; Contributions bullet 3; Section 4 Insight-II; Section 5).
- C5: The perspective "avoids the feedback loop" of noise-evaluation methods, "enhances training efficiency" and provides "strong privacy protection through offline processing" (Abstract; Contributions bullet 1; Section 5).
- C6: Corollary-I bounds the IPC needed to keep clean information (Eq. 10); Corollary-II gives a probabilistic lower bound on the noise rate from the IPC at which accuracy matches the full data (Eq. 11) (Section 4).

**Setup facts.**
- Distillers: DATM (memory-efficient variant of Cui et al. [9], "Benchmark-I"), DANCE, RCIG (Section 3.2).
- Datasets: CIFAR-10, CIFAR-100, Tiny-ImageNet (symmetric); CIFAR-10, CIFAR-100 (asymmetric); CIFAR-10N (Aggre 9.03%, Random k ≈ 18%, Worst 40.21%), CIFAR-100N fine 40.20% (Section 4 Implementations, Experiment-III).
- Asymmetric flips: TRUCK→AUTOMOBILE, BIRD→AIRPLANE, DEER→HORSE, CAT↔DOG on CIFAR-10; next subclass within superclass on CIFAR-100 (Section 4 Implementations).
- Noise rates: symmetric τ ∈ {0.2, 0.4, 0.6, 0.8} (Section 4 Observation-I text; Figure 3 shows τ = 0.0–0.8); asymmetric includes τ = {0.2, 0.4} (Experiment-II); full range not stated in text.
- Backbone: 3-layer ConvNet (CIFAR), 4-layer ConvNet (Tiny-ImageNet) (Section 4 Implementations).
- Baseline: training on the full noisy dataset with cross-entropy, drawn as dashed lines (Section 4 Experiment-I; Figure 2/4/5 captions). Its architecture, epochs, early stopping: not stated.
- Evaluation: "following the evaluation protocols of DATM, DANCE, and RCIG", RCIG with augmentation; "Final test accuracies are reported throughout the distillation process" (Section 4 Implementations). Captions call the plotted quantity "validation performance".
- Seeds, runs, variance: not stated after search. Distillation hyperparameters: not stated. Compute: not stated. Code: not stated. Expert training on noisy data / synthetic label handling: not stated.
- Appendix or supplement: none in the manuscript.

**Headline numbers.** No numeric result appears in the text apart from noise rates. Qualitative headline claims: at τ = 0.6 and 0.8 on CIFAR-10, "a single distilled sample per class surpasses the baseline"; at τ = 0.2, "fewer than 50 samples per class significantly outperform the baseline" (Section 4 Observation-I, Figure 2(a)); on CIFAR-100N, all three methods surpass the baseline "using fewer than 10 distilled images per class" under Worst (Section 4 Observation-III, Figure 5).

**Could not be read.** Figures 1–5 (curves and images); hence every accuracy value. Some equations are garbled by extraction (Eq. 2, 5, 9); they are treated as unverifiable, not as errors.

---

## 2. Ledger

### Accept reasons

| ID | Aspect | Reason | Evidence | Strength | Depends on |
|---|---|---|---|---|---|
| A1 | novelty | Reframes noisy-label learning as distilling a compact clean support set, sidestepping per-sample noise estimation; ties the memorization literature to what distillation synthesizes. | Section 1 Motivation; Section 3.1 Remark ("Why not directly distill a clean subset") | moderate | R12 not upheld |
| A2 | empirical breadth | Three distillation families (parameter matching, distribution matching, meta-learning), three datasets, symmetric τ 0.2–0.8, IPC sweeps. | Section 3.2; Section 4 Implementations; Figure 2 | moderate | R6, R14 not upheld |
| A3 | empirical strength | At high symmetric noise one distilled image per class beats full noisy-data training. | Section 4 Observation-I ("a single distilled sample per class surpasses the baseline") | weak (after P10) | R2 not upheld; figure readable |
| A4 | analysis | Informative negative result: asymmetric noise is absorbed; "Only the DATM method achieves comparable performance" at τ = {0.2, 0.4}. | Section 4 Experiment-II, Observation-II, Insight-II; Figure 4 | moderate | — |
| A5 | empirical realism | Human-annotation noise (CIFAR-10N, CIFAR-100N) with noise rates stated. | Section 4 Experiment-III; Figure 5 | moderate | — |
| A6 | analysis | Noise/IPC trade-off: distillation helps at high noise but "struggle[s]" at low noise (Aggre) because clean samples are lossily compressed. | Section 4 Observation-III, Insight-III | weak | — |
| A7 | clarity | Noise models and the three distillation objectives are formally stated. | Section 3.1 Eq. 1–2; Section 3.2 Eq. 4–9 | moderate | — |
| A8 | qualitative | DATM distilled images retain discriminative features at τ up to 0.8. | Figure 3; Section 4 Observation-I | weak | figure readable |
| A9 | significance | A small distilled set can be shared offline; framed for high-privacy settings. | Abstract; Section 1; Section 5 | weak | R9 not upheld |
| A10 | reproducibility | Public data, published methods, original evaluation protocols. | Section 4 Implementations | weak | R15 not upheld |
| A11 | significance | Opens the question of how much to distill given noise, and of estimating the noise rate from distillation. | Section 1 ("remains an open question"); Section 4 Insight-I | weak | R4 not upheld |

### Reject reasons

| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |
|---|---|---|---|---|---|---|
| R1 | experimental validation | No noisy-label method is compared; the only reference is CE on the full noisy data, so "good label denoisers" is shown only against the weakest baseline. Co-teaching [14] and DivideMix [24] are cited but never run. | Section 4 Observation-I ("over the baseline trained on the entire noisy dataset"); Figures 2, 4, 5 captions | gap | fatal | Add co-teaching, DivideMix and a transition-matrix or robust-loss method on the same ConvNet and on ResNet; ~1–2 GPU-weeks |
| R2 | experimental validation | Baseline protocol (architecture, epochs, early stopping) not stated; no early-stopped CE, random subset or coreset at matched IPC, so the gain cannot be attributed to distillation. | Section 4 Experiment-I ("We use Cross-Entropy loss by default"); Figure 2 caption | gap | major | State the protocol; add the three controls; hours per setting |
| R3 | technical rigor | The mechanism ("captures common patterns while ignoring outliers") is asserted, not tested; denoising may come from matching early expert trajectories / early-trained encoders (early learning before memorization). No ablation of expert epochs or trajectory range. | Section 4 Insight-I; Section 3.2 Benchmark-I/II | gap | major | Ablate expert range and training epochs under noise; moderate |
| R4 | technical rigor | Corollary-II contradicts the paper's own results (check below). | Section 4 Eq. 10, Eq. 11, Observation-I, Observation-III. Check: CIFAR-10, |S̃| = 50,000, C = 10, IPC = 1 → Eq. 11 gives τ ≥ 1 − 10/50,000 = 0.9998, while Observation-I says IPC = 1 already surpasses the baseline at τ = 0.6. CIFAR-100N, IPC = 10 → τ ≥ 0.98 vs stated 40.20%. Eq. 10 rearranged gives τ ≤ 1 − C·IPC/|S̃|, the opposite direction. | error | major | Correct or remove Corollary-II and derive it; no compute |
| R5 | technical rigor | Neither corollary has a proof, assumptions or definitions; δ is undefined; Eq. 10 is just the number of clean samples per class. | Section 4 Corollary-I ("the maximum number of distilled samples per class"), Corollary-II | gap | major | Provide definitions and proofs or recast as heuristics |
| R6 | statistical rigor | No seeds, runs, variance or tables; claims of "significantly outperform" and "consistently" have no test. Multiple seeds are expected at CIFAR scale. | Section 4 Observation-I; Figures 2, 4, 5 captions | gap | major | Mean ± std over ≥ 3 seeds in tables; a few GPU-days |
| R7 | claim scope | "In the Wild" rests on CIFAR-10N/100N only; Clothing1M and WebVision are introduced and never evaluated. | Title; Section 3.1 ("Clothing1M [48] and WebVision [27]"); Section 4 Experiment-III | gap | major | Run Clothing1M or mini-WebVision, or retitle |
| R8 | claim scope | "enhances training efficiency" is never measured; the cost of expert training plus distillation is not reported. | Abstract; Contributions bullet 1; Section 5 | gap | major | Report end-to-end GPU hours or drop the claim |
| R9 | claim scope / ethics | "strong privacy protection" asserted with no threat model or attack; the condensation-privacy debate is not cited. | Abstract ("providing strong privacy protection through offline processing"); Section 5 | gap | major | Membership-inference evaluation or remove; cite Dong et al. 2022 and Carlini et al. 2022 [verify] |
| R10 | claim scope | Tail-class/imbalance finding is in the abstract and contributions but only hypothesized in the body; no imbalanced experiment. | Abstract; Contributions bullet 3; Section 4 ("We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets") | gap | major | Long-tailed noisy CIFAR experiment, or reword as hypothesis |
| R11 | soundness of argument | The "vicious cycle" is argued but not demonstrated, and distillation does not escape noise estimation: IPC must be chosen according to the unknown noise level. | Section 1 Status Quo; Section 1 ("the relationship between the amount of data to be distilled and the level of noise remains an open question"); Insight-I, Insight-III | judgment | major | Show the cycle failing; give a noise-free IPC rule, or tone down |
| R12 | novelty | No new method. Selecting a small clean-dominated subset under label noise is studied in data selection (e.g. coresets for robust training against noisy labels, Mirzasoleiman et al., NeurIPS 2020), and early learning before memorization is established (e.g. ELR, Liu et al., NeurIPS 2020); neither is cited or compared. [verify] (from memory; no search ran) | Section 1 Contributions; Section 2.1; References [1]–[61] | judgment | major | Position against and compare with coreset/data-pruning methods at matched size |
| R13 | experimental validation | Asymmetric noise only on CIFAR-10/100; natural noise only CIFAR-N. | Section 4 Experiment-II; Figure 4 caption | gap | minor | Tiny-ImageNet asymmetric runs |
| R14 | evaluation protocol | Captions say "The validation performance"; text says test accuracies are "reported throughout the distillation process". If the best test value over iterations is plotted, selection is on test. | Figure 2/4 captions; Section 4 Implementations | question | major | Name the selection split; report held-out test |
| R15 | reproducibility | No distillation hyperparameters, no expert-training details under noise, no compute, no code. | Section 4 Implementations | gap | major | Implementation appendix; release code |
| R16 | technical rigor | Not stated whether experts are trained on noisy labels, how real images are grouped per class, or whether DATM's soft labels come from noisy experts. | Section 3.2 Benchmark-I; Section 4 Implementations | question | major | Specify the pipeline per method |
| R17 | clarity | "Realted Works", "bellow", "Both of which are widely employed in existing researches" (three noise types), Eq. 4 uses θ̂_{t+N} while text defines T steps; two pages of method recap vs two of results. | Section 2 heading; Section 1 Contributions; Section 3.1; Section 3.2 Eq. 4 | gap | minor | Proofread; move recaps to appendix; add tables |
| R18 | format | Layout (Figure 1 beside the abstract, CVF-style headings) suggests a non-ICLR template; unverifiable from extracted text. | Page 1; Section headings | question | minor | Use the ICLR 2026 template |
| R19 | significance | Contribution check Q1/Q3: insights are largely expected (the paper says Observation-II "is consistent with intuition"); the delta is a re-run of existing distillers on noisy CIFAR variants. | Section 4 ("This phenomenon is consistent with intuition"); Insight-I, Insight-II | judgment | major | A non-obvious finding: which family is robust and why, or a fix for the asymmetric failure |
| R20 | significance | Contribution check Q4: benefit is limited to high noise; at realistic low noise (Aggre 9.03%) distillation underperforms the full noisy data, and ConvNet-on-distilled-data accuracy is far below standard noisy-label practice. | Section 4 Observation-III ("these distillation approaches struggle to"), Insight-III | judgment | major | Show a realistic-noise regime where it beats strong LNL methods, or reframe |
| R21 | experimental validation | Only 3/4-layer ConvNets; no cross-architecture evaluation of the distilled sets. | Section 4 Implementations ("a simple ConvNet [40] architecture") | gap | major | Evaluate on ResNet-18 vs LNL methods |
| R22 | experimental validation | (added in T1 review) "Denoiser" is measured only via downstream accuracy; no direct measure of the distilled set's label quality (e.g. a clean-trained classifier's agreement with synthetic labels, inherited confusions under asymmetric flips). | Section 4 Observations I–III; Figure 3 (qualitative only) | gap | major | Classify synthetic images with a clean model; report agreement; cheap |

### Answered

- DATM would not scale to Tiny-ImageNet — answered at Section 3.2: the memory-efficient variant of Cui et al. [9] is used ("Unless otherwise specified, Benchmark-I referenced later denotes this accelerated version").
- Only synthetic noise is studied — answered at Section 4 Experiment-III and Figure 5 (CIFAR-10N/100N). The scale concern remains as R7.
- Distillers run outside their published protocols — answered at Section 4 Implementations ("following the evaluation protocols of DATM, DANCE, and RCIG").
- Failure modes are hidden — answered at Section 4 Observation-II/Insight-II and Observation-III/Insight-III.

### Aspect coverage

- Novelty: A1; R12, R19.
- Technical rigor / soundness: A7; R3, R4, R5, R11, R16.
- Experimental validation: A2, A3, A4, A5, A6, A8; R1, R2, R6, R13, R14, R21, R22.
- Significance: A9, A11; R19, R20.
- Claim scope (claim distortion, E5): R7, R8, R9, R10.
- Clarity: A7; R17, R18.
- Reproducibility: A10; R15.
- Ethics / limitations: R9 (privacy claim); limitations are discussed as pitfalls (Insight-II, Insight-III). Considered, no further reason: no human data, no deployment risk.
- Statistical rigor: R6.
- Omission sweep (error_audit §4): split and selection → R14; seeds → R6; baseline settings → R2; hyperparameters → R15; compute → R8, R15; licence/consent → considered, no reason (public benchmarks); limitations → present (Insight-II, III); code → R15.

### Pairs

- A3 ↔ R2, R1: whether "beats the full noisy baseline" is meaningful (C1).
- A2 ↔ R6, R14: whether the breadth is statistically and protocol-sound (C1).
- A1 ↔ R12, R11: whether the perspective is new and actually avoids noise estimation (C1, C5).
- A5 ↔ R7: real noise, but small-scale (C3).
- A6 ↔ R20: trade-off as insight vs. as limit on usefulness (C3).
- A11 ↔ R4, R5: the noise-rate estimation idea vs. its formalization (C6).
- A9 ↔ R9: privacy framing (C5).

---

## 3. Reorganized ledger and probes

### By claim

No duplicates required merging (R4 and R5 both concern the corollaries but one is an error, the other a gap; kept separate).

**C1: distillers denoise symmetric noise**
- A2 (checked), A3 (checked, weak after P10), A8 (open, figure unavailable)
- R1 (checked by P1, high swing, worst fatal), R2 (checked by P2, high swing; decides A3 ↔ R2), R3 (checked by P9, high swing), R6 (checked; P12 after reviews), R14 (open, question, P5 unsettled), R16 (open, question), R12 (checked by P11, novelty pair with A1), R21 (checked), R22 (checked, added by T1)

**C2: asymmetric noise is absorbed**
- A4 (checked); R13 (checked), R19 (checked, judgment)

**C3: effective in the wild**
- A5 (checked), A6 (checked); R7 (checked by P7, high swing on the title claim), R20 (checked, judgment)

**C4: tail-class lossy compression**
- R10 (checked by P6)

**C5: avoids vicious cycle, efficiency, privacy**
- A9 (checked); R8, R9 (checked by P8), R11 (checked, judgment)

**C6: corollaries**
- A11 (checked); R4 (checked by P3, error), R5 (checked by P4)

**General**
- A7, A10 (checked); R15 (checked), R17 (checked), R18 (open, question, low swing)

Swing ranking (highest first): R1, R2, R4, R3, R14, R6, R12, R7, R10, R5, R16, R8/R9.

### Probes

| ID | Item | Question | Method | Result | Change |
|---|---|---|---|---|---|
| P1 | R1 | Does any result compare distillation with a noisy-label method rather than plain CE on full noisy data? | Re-read Section 4 and captions; search for [14], [24], [28], [33], [39], [41] outside Sections 1–2 | confirmed — only "the baseline trained on the entire noisy dataset" (Section 4); LNL methods appear only in Sections 1–2 | R1 open → checked (gap) |
| P2 | R2 (A3) | Is the baseline protocol stated; is any matched-size random/coreset subset reported? | Re-read Section 4 Implementations, Experiment-I, captions | confirmed — only "We use Cross-Entropy loss by default"; dashed lines = full dataset; no controls | R2 → checked; A3 remains dependent on R2 |
| P3 | R4, A11 | Is Eq. 11 consistent with Eq. 10 and with Observations I and III? | Recompute (|S̃| taken as the standard 50,000 CIFAR training images; not printed in the paper) | confirmed — CIFAR-10, IPC = 1: τ ≥ 0.9998 vs τ = 0.6 at which IPC = 1 beats baseline; CIFAR-100N, IPC = 10: τ ≥ 0.98 vs 40.20%; Eq. 10 rearranged gives τ ≤ 1 − C·IPC/|S̃| | R4 → error (confidence medium-high: depends on reading "matches" as including "surpasses") |
| P4 | R5 | Any proof, assumptions, or δ definition? | Search "proof", "assum", "δ", "appendix" | confirmed — none; no appendix | R5 → checked |
| P5 | R14 | Is accuracy selected over distillation iterations on the test set? | Re-read Section 4 Implementations and captions | cannot be settled — "Final test accuracies are reported throughout the distillation process" vs captions "The validation performance" | R14 stays question; graded ≤ minor |
| P6 | R10 | Is the imbalance/tail claim tested? | Search "imbalanc", "tail" | confirmed — Abstract, Contributions, Insight-II ("We further hypothesize"), Section 5 only | R10 → checked |
| P7 | R7 | Are Clothing1M/WebVision evaluated? | Search | confirmed — Section 3.1 only | R7 → checked |
| P8 | R8, R9 | Are efficiency or privacy measured? | Search "efficien", "privacy", "GPU", "membership" | confirmed — assertions only (Abstract, Section 1, Section 3.2 Remark, Section 5) | R8, R9 → checked |
| P9 | R3, R16 | Are expert training under noise, synthetic-label handling or trajectory range described or ablated? | Re-read Section 3.2 and Section 4 | partly — no ablation (R3 confirmed); pipeline details absent (R16 unsettled) | R3 → checked; R16 stays question |
| P10 | A3, A8 | Are the IPC = 1 and Figure 3 claims backed by numbers in the text? | Trace claim → figure → number | partly — prose only; figures unavailable | A3 moderate → weak; A8 stays open |
| P11 | R12 | Does the paper cite or compare with data selection / coresets under noisy labels? | Read references [1]–[61]; no network search | partly — absence confirmed; existence of the prior work rests on memory [verify] | R12 → checked (absence); novelty basis marked [verify] |

---

## 4. Reviewer roster

Aspects at ≥ 12% of the ratio: technical_rigor (28%), novelty (20%), significance (20%), experimental_validation (14%); each has at least one type. Clarity (10%), reproducibility (5%) and ethics (4%) have no type; their reasons sit in other types' "Weighs most" and the script renormalizes their share away.

| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |
|---|---|---|---|---|---|---|---|
| T1 Noisy-label learning specialist | experimental_validation | learning with noisy labels (task) | robust training, CIFAR-N/Clothing1M/WebVision benchmarks | comparisons with strong LNL baselines on standard settings | weak CE baselines, CIFAR-only "real-world" claims | R1, R2, R6, R7, R13, R14, R20, R21, R22; A4, A5 | high |
| T2 Dataset distillation specialist | technical_rigor | dataset distillation (method's field, generated) | trajectory, distribution and kernel/meta-learning distillation | correct use of distillers; ablations of distillation components | unexplained pipelines, missing hyperparameters | R1, R3, R4, R6, R13, R15, R16, R17, R19; A2, A7, A8, A10 | high |
| T3 Learning-theory / memorization researcher | technical_rigor | learning theory of label noise and memorization (neighbor) | early learning, memorization, generalization under noise | precise statements with proofs; tested mechanisms | unproven "corollaries", untested causal stories | R3, R4, R5, R11, R12, R14, R17; A1, A11 | medium |
| T4 Data-centric ML / coreset researcher | novelty | data selection, coresets, data pruning (neighbor, expanded from "data-centric ML") | subset selection under noise, data pruning | novelty measured against selection baselines at matched size | known ideas renamed, missing matched-size controls | R1, R2, R6, R12, R19, R20, R21; A1, A4 | medium |
| T5 Privacy and trustworthy-ML researcher | significance | privacy-preserving ML (neighbor, generated from C5) | membership inference, privacy of synthetic data | claims backed by threat models; scoped significance | "privacy for free" claims; untested practical benefits | R7, R8, R9, R10, R11, R20; A9 | low |
| TA advocate | significance | noisy labels × dataset distillation (champion) | — | the strongest accept case if answerable reasons are answered | — | all reasons graded fatal/major by others; A1, A3, A4, A5 | medium |

---

## 5. Reviews

### T1: Noisy-label learning specialist (experimental_validation; learning with noisy labels)

**Reading of the ledger.**
- Holds: A4 (the asymmetric failure is a real, useful negative result), A5 (CIFAR-N with correct noise rates is the right first step). Discounts: A2 (breadth over distillers, not over noisy-label methods), A3 (beating CE-on-everything at τ = 0.8 is expected of almost any noise-robust procedure; P2 shows the baseline is not described).
- R1: fatal (the paper's title claim is relative to the noisy-label field, and no member of that field is compared). R2: major (no early-stopped CE or matched-size random subset; these are the first controls I would ask for). R6: major (CIFAR-scale, cheap seeds). R7: major ("In the Wild" without Clothing1M/WebVision). R11: major (choosing IPC requires knowing τ). R13: minor. R14: minor (unsettled question, capped). R20: major (no benefit at realistic Aggre noise). R21: major (ConvNet-only results say nothing about the ResNet settings our field reports).
- New reason: R22 added to the ledger (the distilled set's label quality is never measured directly). R22: major.

**Opinion.** As someone who works on learning with noisy labels, I find the question interesting: whether a distilled set filters label noise is worth knowing. But the evidence does not reach the bar for the paper's claim. "Good label denoisers" is a comparative statement, and the only comparator is plain cross-entropy on the full noisy dataset (R1), with an unstated protocol and none of the trivial controls: early stopping, a random subset, or a coreset of the same size (R2). At τ = 0.8 symmetric, a model trained on any small, reasonably balanced subset will likely beat a memorizing CE baseline, so A3 does not distinguish distillation from subsampling. The real-world evidence is CIFAR-N only (R7), and there the method loses at the realistic Aggre noise level (R20). Results are curves without seeds (R6), on a 3-layer ConvNet (R21), and the "denoiser" is never inspected directly (R22). I would move up substantially with a table against co-teaching, DivideMix and early-stopped CE on ResNet-18, CIFAR-N and Clothing1M, with seeds.

Decisive: R1 (fatal), R2 (major), R22 (major), A5 (holds, moderate)

**Scores.** Pool position 15 (basis: R1, R2, R22). Technical Rigor 35, Clarity 52, Novelty 35, Significance 30, Experimental Validation 25, Reproducibility 38, Ethics 55. Overall 2. Confidence 4.

### T2: Dataset distillation specialist (technical_rigor; dataset distillation)

**Reading of the ledger.**
- Holds: A2 (the three families are well chosen), A4, A7 (the method recaps are accurate where legible), A10. Discounts: A3 and A8 (figures not readable here; the text gives no numbers), and A8 is a single-image visualization.
- R1: major (needed for the claim, though my main concern is internal). R3: major (DATM's difficulty alignment matches early trajectories for small IPC and DANCE uses early-trained encoders; the denoising could be inherited from early learning, and no ablation tests it). R4: major (I recomputed Eq. 11 as P3 did; it cannot hold for the paper's own IPC = 1 result). R6: major. R13: minor. R15: major (no distillation iterations, learning rates, synthetic-label settings, or how experts were trained on noisy labels). R16: minor (unsettled question, capped). R17: minor. R19: major (re-running three distillers is moderate novelty at best).

**Opinion.** The study is a reasonable first experiment, but it treats the distillers as black boxes and so cannot say why they denoise. For a distillation reviewer the interesting part is which component filters noise: the expert trajectory range in DATM, the expert-encoder interpolation in DANCE (Eq. 6), or the kernel regression in RCIG (Eq. 9). The paper ablates none of these (R3) and does not even say whether experts are trained on noisy labels or how soft labels are produced (R15, R16). Without this, Insight-I is a restatement of the curves. Corollary-II is wrong as stated (R4), which undermines the one formal contribution. I value the breadth (A2) and the asymmetric failure (A4), and a version that dissected each family's behavior under noise, with tables and seeds, would be a solid workshop-to-conference paper. As submitted, it is below the ICLR bar.

Decisive: R3 (major), R1 (major), R15 (major), A2 (holds, moderate)

**Scores.** Pool position 25 (basis: R3, R1, R15; A2). Technical Rigor 38, Clarity 55, Novelty 40, Significance 40, Experimental Validation 36, Reproducibility 36, Ethics 55. Overall 2. Confidence 4.

### T3: Learning-theory and memorization researcher (technical_rigor; learning theory of noise and memorization)

**Reading of the ledger.**
- Holds: A4 (the absorbed-pattern explanation for asymmetric noise is plausible and consistent with Eq. 2). Discounts: A1 (the "common patterns first" intuition is the memorization literature [1, 25, 47], restated rather than extended), A11 (the noise-rate estimation idea rests on R4).
- R3: major (the mechanism is a causal claim with no test). R4: major (error; the bound contradicts the paper's own Observation-I and the direction of Eq. 10). R5: major (no proof, δ undefined, "perfectly preserve the sample information" undefined). R11: major (the claimed escape from noise evaluation is not established; IPC selection needs τ). R12: major (early learning before memorization is established theory; the paper does not position against it). R14: minor (question). R17: minor.

**Opinion.** The paper presents two "corollaries" as formal take-aways, but there is no theorem they follow from, no assumptions, and δ is never defined (R5). Corollary-I says that you cannot keep more clean samples per class than exist, which is true but not about distillation. Corollary-II is worse: taking CIFAR-10 at IPC = 1, it claims τ ≥ 0.9998 with high probability, while the paper reports that one image per class already beats the baseline at τ = 0.6 (R4). Its inequality also runs opposite to Eq. 10. The conceptual story, that distillation keeps common patterns and drops noise, is the early-learning phenomenon by another route and is never tested (R3). The vicious-cycle argument in Section 1 is rhetorical (R11). I would change my view with correct, proved statements tied to a measurable quantity, and an experiment separating distillation from early learning.

Decisive: R4 (major, error), R5 (major), R3 (major)

**Scores.** Pool position 18 (basis: R4, R5, R3). Technical Rigor 30, Clarity 48, Novelty 35, Significance 35, Experimental Validation 38, Reproducibility 40, Ethics 55. Overall 2. Confidence 3.

### T4: Data-centric ML / coreset-selection researcher (novelty; data selection and coresets)

**Contribution check.**
1. What does a reader learn? That distillers trained on symmetric-noise data outperform CE on the full data at high noise and fail under structured noise (A4). The why is not established (R3), so the insight is mostly a ranking against one baseline (R19).
2. Does the setting support the framing? No: "In the Wild" is CIFAR-N (R7); "denoisers" is not measured directly (R22).
3. Conceptual or refinement? A re-run of three existing distillers on noisy CIFAR variants; moderate novelty (R19). Selecting a compact clean-dominated subset under noise is studied in data selection, e.g. coresets for robust training (Mirzasoleiman et al., NeurIPS 2020) [verify], and not cited (R12).
4. Would it transfer? Probably not to practice: no gain at low noise (R20), ConvNet only (R21).

**Reading of the ledger.**
- Holds: A4. Discounts: A1 (the perspective is a reframing of subset selection under noise; the paper does not argue what distillation adds over selection).
- R12: major (cross-field prior art not engaged). R19: major. R2: major (the missing random/coreset control at matched IPC is exactly what would show distillation's added value). R1: major. R6: minor, assuming the adopted DATM/DANCE/RCIG protocols average several evaluation runs (updated after P12, see below). R20: major. R21: major.

**Opinion.** From the data-selection side, the natural question is whether synthesizing samples beats choosing real ones. The paper never asks it: there is no random subset, no coreset, no data-pruning baseline at the same number of images per class (R2), and the selection-under-noise literature is absent from the related work (R12). Without that comparison, the novelty is the observation that a known class of methods behaves on noisy data roughly as intuition predicts, and the paper says as much for Observation-II (R19). The asymmetric-noise result (A4) is the most useful finding and could anchor a sharper paper: show which distiller absorbs structured flips, why, and how to prevent it. As it stands, the contribution sits in the lower part of the pool.

Decisive: R12 (major), R2 (major), R19 (major)

**Scores.** Pool position 22 (basis: R12, R2, R19). Technical Rigor 40, Clarity 55, Novelty 33, Significance 38, Experimental Validation 35, Reproducibility 40, Ethics 55. Overall 2. Confidence 4.

### T5: Privacy and trustworthy-ML researcher (significance; privacy-preserving ML)

**Contribution check.**
1. What does a reader learn? Not what the abstract promises on privacy and efficiency: neither is tested (R8, R9).
2. Setting vs framing: "strong privacy protection" and "high-privacy environments" have no threat model; "in the wild" is CIFAR-N (R7); the imbalance finding is a hypothesis (R10).
3. Delta: a re-run of existing distillers (R19, not graded by me).
4. Transfer: the benefit appears only at high noise (R20); in a practical high-privacy setting, who distills, on what compute, and with what leakage is unaddressed.

**Reading of the ledger.**
- Holds: A4. Discounts: A9 (the privacy framing is an assertion, not a result).
- R9: major (privacy of condensed data is contested; e.g. Dong, Zhao and Lyu, "Privacy for Free: How does Dataset Condensation Help Privacy?", ICML 2022, argued for it, and a follow-up by Carlini, Feldman and Nasr (2022) [verify] disputed its evaluation; neither is cited). R8: major. R10: major (abstract-level claim with no experiment). R7: major. R20: major. R11: minor (a framing issue from my perspective).

**Opinion.** The paper's significance case rests heavily on two practical promises, efficiency and "strong privacy protection through offline processing", and neither is supported by any measurement (R8, R9). Dataset condensation's privacy properties are an open, contested question, and a paper that wants to claim them must state a threat model and run at least a membership-inference test. The imbalanced-data claim is presented as a finding in the abstract but is only a hypothesis in Section 4 (R10). Stripped of these, what remains is a scoped empirical observation on CIFAR-scale data whose practical benefit vanishes at realistic noise rates (R20). I would raise my score if the claims were either evidenced or removed, but removal would leave a narrow contribution.

Decisive: R9 (major), R8 (major), R10 (major)

**Scores.** Pool position 20 (basis: R9, R8, R10). Technical Rigor 38, Clarity 52, Novelty 38, Significance 32, Experimental Validation 36, Reproducibility 38, Ethics 48. Overall 2. Confidence 3.

### TA: advocate (significance)

**Blocking vs answerable** (reasons another type graded fatal or major):
- Blocking, grade kept: R1 (fatal; new experiments against LNL methods are needed), R2 (major; new controls), R3 (major; new ablation), R4 (major; `error`, never answerable), R6 (major; new seeded runs), R12 (major; novelty judgment against prior art), R19 (major), R20 (major), R21 (major; new architecture runs), R22 (major; new measurement).
- Answerable without new science, graded minor: R5 (recast corollaries as heuristics or drop them), R7 (retitle; "In the Wild" → CIFAR-N), R8 and R9 (remove or qualify the efficiency and privacy claims), R10 (state the tail-class point as a hypothesis), R11 (tone down the vicious-cycle framing), R15 (add an implementation appendix from runs already done).

**Accept case at its strongest.** A1 and A4. The paper asks a clean question no LNL paper usually asks (can distillation itself act as the filter?), and gives a clear, honest answer with a boundary: yes for random noise, no for structured flips, where the noise pattern is absorbed into the synthetic data (A4). A3 and A5 show the effect is large at high noise and survives human-annotation noise on CIFAR-N. An ICLR reader would gain a well-posed hypothesis and a warning for anyone using distilled data from noisy sources.

**Opinion.** I would champion the question and the asymmetric-noise finding. Even with every answerable reason fixed, though, the central comparative claim still lacks its comparators (R1), the matched-size controls (R2), and a test of the mechanism (R3), and the one formal result is wrong (R4). Those are blocking, and R1 is fatal for the claim as titled. The honest advocate position is that this is a promising workshop paper or a first draft of a stronger analysis paper, below the ICLR line in this form.

Decisive: A4 (holds, moderate), A1 (holds, moderate), R1 (fatal, blocking), R2 (major, blocking)

**Scores.** Pool position 30 (basis: A4, A1 vs R1, R2; capped at 30 by the blocking fatal R1). Technical Rigor 42, Clarity 58, Novelty 45, Significance 45, Experimental Validation 40, Reproducibility 45, Ethics 60. Overall 3. Confidence 3. (Overall 3 sits one step above the composite-implied 2 because the champion credits the question and A4; within the ±1 tolerance.)

### Settling factual splits

| Probe | Split | Fact checked | Result | Grades updated |
|---|---|---|---|---|
| P12 | T4 (R6 minor) vs T1, T2, TA (R6 major) | Does the paper state multiple runs, seeds or variance anywhere, e.g. by adopting the DATM/DANCE/RCIG multi-run evaluation? | confirmed absent — Section 4 Implementations names the protocols but no runs; the Figure 2, 4, 5 captions describe only solid and dashed lines; no "seed", "std" or "mean" in the text | T4: R6 updated after P12: minor → major. R6 was not among T4's decisive items, so its scores are unchanged. |

Value splits that remain: R11 (T1, T3 major vs T5 minor, TA minor as answerable); R7 (T1, T5 major vs TA minor as answerable by retitling).

---

## 6. Scores and decision

| Type | Aspect | Weight | Pool position | Overall | Confidence |
|---|---|---|---|---|---|
| T1 Noisy-label learning specialist | experimental_validation | 0.169 | 15 | 2 | 4 |
| T2 Dataset distillation specialist | technical_rigor | 0.169 | 25 | 2 | 4 |
| T3 Learning-theory / memorization | technical_rigor | 0.169 | 18 | 2 | 3 |
| T4 Data-centric / coreset | novelty | 0.247 | 22 | 2 | 4 |
| T5 Privacy / trustworthy ML | significance | 0.124 | 20 | 2 | 3 |
| TA advocate | significance | 0.124 | 30 | 3 | 3 |

- **Aspect-weighted rating:** 2.124 → **final rating 2 (Reject)**; ICLR's own scale: **2 on {0, 2, 4, 6, 8, 10}** (3 on the earlier {1, 3, 5, 6, 8, 10} scale). ICLR scale status is *secondary*: recent forms use this scale; verify against the current form. ICLR sub-scores from the script: Soundness 1, Presentation 2, Contribution 1.
- Weighted pool position 21.4; plain mean 2.17; spread 1 (2 to 3).
- Uncovered aspects and warnings: none. Clarity, reproducibility and ethics (19% combined) have no type and were renormalized away, as the procedure allows for aspects below 12%.
- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.

<details><summary>Aggregation output</summary>

```
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Noisy-label learning specialist) | experimental_validation | 14% | 0.169 |
| T2 (Dataset distillation specialist) | technical_rigor | 28% | 0.169 |
| T3 (Learning-theory and memorization researcher) | technical_rigor | 28% | 0.169 |
| T4 (Data-centric ML / coreset-selection researcher) | novelty | 20% | 0.247 |
| T5 (Privacy and trustworthy-ML researcher) | significance | 20% | 0.124 |
| TA (advocate) | significance | 20% | 0.124 |

Final rating (aspect-weighted mean): 2.12 -> 2 (Reject) · plain mean 2.17 · weighted pool position 21.4

Composite cross-check (0-100): official 39.5 -> 2
Per-type composites: T1 35.4, T2 41.0, T3 36.8, T4 39.7, T5 38.4, TA 45.5

Cross-Venue Outlook
| ICLR (2026) | composite 39.2 | bar +0 | band 2 -> 2 | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) | Soundness 1, Presentation 2, Contribution 1 | secondary |
```

Full JSON: `aggregate.json` (and `before.json` without `--final`).

</details>

---

## 7. Consensus map, strengths, concerns, roadmap

### Consensus map

| Item | Types naming it | Grades (or held / discounted) |
|---|---|---|
| R1 | 4 of 6 | T1 fatal, T2 major, T4 major, TA fatal |
| R2 | 3 of 6 | T1 major, T4 major, TA major |
| R3 | 3 of 6 | T2 major, T3 major, TA major |
| R4 | 3 of 6 | T2 major, T3 major, TA major |
| R5 | 2 of 6 | T3 major, TA minor |
| R6 | 4 of 6 | T1 major, T2 major, T4 major (after P12), TA major |
| R7 | 3 of 6 | T1 major, T5 major, TA minor |
| R8 | 2 of 6 | T5 major, TA minor |
| R9 | 2 of 6 | T5 major, TA minor |
| R10 | 2 of 6 | T5 major, TA minor |
| R11 | 4 of 6 | T1 major, T3 major, T5 minor, TA minor |
| R12 | 3 of 6 | T3 major, T4 major, TA major |
| R13 | 2 of 6 | T1 minor, T2 minor |
| R14 | 2 of 6 | T1 minor, T3 minor (question) |
| R15 | 2 of 6 | T2 major, TA minor |
| R16 | 1 of 6 | T2 minor (question) |
| R17 | 2 of 6 | T2 minor, T3 minor |
| R18 | 0 of 6 | — |
| R19 | 3 of 6 | T2 major, T4 major, TA major |
| R20 | 4 of 6 | T1 major, T4 major, T5 major, TA major |
| R21 | 3 of 6 | T1 major, T4 major, TA major |
| R22 | 2 of 6 | T1 major, TA major |
| A1 | 3 of 6 | TA held; T3, T4 discounted |
| A2 | 2 of 6 | T2 held; T1 discounted |
| A3 | 3 of 6 | TA held; T1, T2 discounted |
| A4 | 6 of 6 | held by all |
| A5 | 2 of 6 | T1, TA held |
| A7, A10 | 1 of 6 | T2 held |
| A8 | 1 of 6 | T2 discounted |
| A9 | 1 of 6 | T5 discounted |
| A11 | 1 of 6 | T3 discounted |

### Key strengths

- A4: asymmetric/structured noise is absorbed into distilled data, an informative failure mode — held by 6 of 6 types.
- A5: evaluation on human-annotation noise (CIFAR-10N/100N) — held by 2 of 6.
- A1: a clean reframing of noisy-label learning as distilling a clean support set — held by the advocate, discounted by the theory and data-selection types.

### Top concerns (at most five)

Ranked by the number of types grading fatal or major, then worst grade; ties at three types broken in favor of the verified error and the control that decides A3.

1. R1: No noisy-label learning baseline; only CE on the full noisy data (Section 4 Observation-I; Figures 2, 4, 5). Fix: compare with co-teaching, DivideMix and a robust-loss/transition method on ConvNet and ResNet-18; ~1–2 GPU-weeks.
2. R6: No seeds, variance or tables (Section 4; captions of Figures 2, 4, 5). Fix: mean ± std over ≥ 3 seeds in tables; a few GPU-days.
3. R20: Benefit limited to high noise; underperforms at realistic Aggre noise (Section 4 Observation-III, Insight-III). Fix: show a realistic-noise regime where distillation beats strong LNL methods, or reframe the paper as an analysis of distillation's robustness.
4. R4: Corollary-II (Eq. 11) contradicts the paper's own results and the direction of Eq. 10 (Section 4). Fix: correct or remove it and give a proof; no compute.
5. R2: No matched-size controls (early-stopped CE, random subset, coreset) and an unstated baseline protocol (Section 4 Experiment-I). Fix: add the controls; hours per setting.

### Revision Roadmap

Priority 1 = graded fatal by any type, or major by at least 3 of the 6 types.

| Priority | Ledger ID | Fix | Cost |
|---|---|---|---|
| 1 | R1 | Add LNL baselines (co-teaching, DivideMix, robust loss / transition matrix) at matched backbone | ~1–2 GPU-weeks |
| 1 | R6 | Seeds, mean ± std, numeric tables | a few GPU-days |
| 1 | R20 | Demonstrate a practical regime or reframe the significance claim | moderate |
| 1 | R2 | State baseline protocol; add early-stopped CE, random and coreset subsets per IPC | hours per configuration |
| 1 | R4 | Correct or remove Corollary-II; derive formally | none |
| 1 | R3 | Ablate expert trajectory range / expert epochs to separate distillation from early learning | moderate |
| 1 | R12 | Position against and compare with coreset / data-selection under noise [verify the cited works] | moderate |
| 1 | R19 | Deliver a non-obvious finding (per-family mechanism, or a fix for asymmetric absorption) | moderate–high |
| 1 | R21 | Cross-architecture evaluation (ResNet-18) | moderate |
| 2 | R7 | Clothing1M or mini-WebVision, or retitle | high / none |
| 2 | R11 | Demonstrate the vicious cycle or tone down; IPC rule without τ | low–moderate |
| 2 | R5 | Definitions and proofs, or recast corollaries as heuristics | none |
| 2 | R8 | Report end-to-end GPU hours or drop the efficiency claim | low |
| 2 | R9 | Membership-inference evaluation or drop the privacy claim; cite the condensation-privacy debate | low–moderate |
| 2 | R10 | Long-tailed noisy experiment or reword as hypothesis | low |
| 2 | R15 | Implementation appendix and code | low |
| 2 | R22 | Measure label agreement of synthetic images with a clean-trained classifier | low |
| 3 | R13 | Tiny-ImageNet asymmetric runs | low |
| 3 | R14 | State the checkpoint-selection split; report held-out test | none |
| 3 | R16 | Describe noisy-expert training, per-class grouping, soft labels | none |
| 3 | R17 | Proofread; move method recaps to appendix | none |
| 3 | R18 | Use the ICLR template (not graded by any type) | none |

**Missing references** (Hard Rule 2):
- B. Mirzasoleiman, K. Cao, J. Leskovec. "Coresets for Robust Training of Deep Neural Networks against Noisy Labels." NeurIPS 2020. (R12)
- S. Liu, J. Niles-Weed, N. Razavian, C. Fernandez-Granda. "Early-Learning Regularization Prevents Memorization of Noisy Labels." NeurIPS 2020. (R3, R12)
- T. Dong, B. Zhao, L. Lyu. "Privacy for Free: How does Dataset Condensation Help Privacy?" ICML 2022. (R9)
- N. Carlini, V. Feldman, M. Nasr. "No Free Lunch in 'Privacy for Free: How does Dataset Condensation Help Privacy'." arXiv 2022. [verify] (R9)
- Line of work, not a specific title: recent studies of dataset distillation or condensation trained on noisy-label data. [verify]

---

## 8. Integrity signals and limitations

- **Integrity signals:** `integrity_scan.py` found no reviewer-directed text or hidden characters, and none was seen while reading. The bracket "[REDACTED: venue/acceptance mark]" in reference [10] comes from the blinding of the provided text, not from the authors. These findings never change a score.
- **Limitations:**
  - Figures 1–5 were not available, and every result in the paper is a figure. Accuracy values, the IPC at which curves cross the baseline, and the Figure 3 images could not be checked (A3, A8, P10).
  - Eq. 2, 5 and 9 are partly garbled by extraction and are treated as unverifiable.
  - R4's check takes |S̃| = 50,000, the standard CIFAR training-set size, which the paper does not print.
  - The literature check did not run because there was no network access. The novelty basis of R12 and the privacy references in R9 rest on memory, with the uncertain entries marked [verify].
  - All six types share one context and one reading, so their agreement (for example on R1 and A4) is not independent confirmation.
  - The paper's title was vaguely familiar. Nothing about its reception or outcome was used, and the review is based on the manuscript alone.
