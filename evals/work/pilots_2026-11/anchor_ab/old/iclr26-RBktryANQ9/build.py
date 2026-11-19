import json, os
D = os.path.dirname(os.path.abspath(__file__))

A = [
 ("A1","novelty","Reframes learning with noisy labels as a dataset-distillation problem: distil a compact synthetic support set from the noisy data and train on it, sidestepping the noise-estimation step of selection/re-weighting/re-labelling pipelines. This links two literatures that rarely meet.","Abstract; Sec. 1 (Motivation); Sec. 3.1 Remark: \"Why not directly distill a clean subset that enables effective training?\"","moderate","R12 and R15 not upheld; the framing is backed by evidence","C1"),
 ("A2","experimental_validation","Covers the three main families of dataset distillation with one representative each: parameter/trajectory matching (DATM), distribution matching (DANCE), meta-learning/kernel (RCIG), so conclusions are not tied to one distiller.","Sec. 3.2, Benchmark-I/II/III, Eqs. 4-9","moderate","each method run with its original protocol","C2"),
 ("A3","experimental_validation","Symmetric noise is swept over several rates (tau = 0.2, 0.4, 0.6, 0.8) and IPC values on three datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet), giving accuracy-vs-IPC curves against a full-data reference.","Sec. 4 Experiment-I; Figure 2(a)-(c) captions","moderate","R4 and R9 not upheld","C2"),
 ("A4","significance","Striking headline effect: at high symmetric noise a single distilled image per class beats training on the full noisy set, and at tau=0.2 fewer than 50 IPC do.","Sec. 4 Experiment-I: \"at noise rates of 0.6 and 0.8, a single distilled sample per class surpasses the baseline\"","moderate","full-data baseline trained sensibly (R4); numbers verifiable (R9)","C2"),
 ("A5","technical_rigor","Reports a negative result honestly: under asymmetric (class-pair) noise most distillers fall below the full-data baseline, and only DATM matches it at tau in {0.2, 0.4} with large IPC. This bounds the method's applicability.","Sec. 4 Experiment-II, Observation-II; Figure 4: \"Only the DATM method achieves comparable performance to the benchmark at noise rate\"","moderate","none","C3"),
 ("A6","experimental_validation","Tests human-annotation noise (CIFAR-10N Aggre/Random/Worst, CIFAR-100N fine, tau up to 40%), not only synthetic flips, and reports where distillation helps (Worst) and where it does not (Aggre).","Sec. 4 Experiment-III; Figure 5","moderate","R8 not upheld (scale of 'in the wild')","C4"),
 ("A7","significance","Identifies an IPC-noise trade-off: small IPC removes noise but also compresses clean information, which explains why distillation underperforms at low noise (Aggre, 9%).","Sec. 4 Insight-III: \"This is why data distillation often yields suboptimal results in low-noise settings\"","weak","read from figures not available to this review","C4"),
 ("A8","clarity","Self-contained recap of the noise models (Eqs. 1-2) and the three distillation objectives (Eqs. 4-9) lets a noisy-label reader follow the distillers.","Sec. 3.1 Eqs. 1-3; Sec. 3.2 Eqs. 4-9","moderate","none","general"),
 ("A9","experimental_validation","Qualitative evidence: distilled DATM images at IPC=1 shown across tau=0.0-0.8, claimed to retain discriminative features under heavy noise.","Figure 3 caption; Sec. 4: \"a single distilled image retains discriminative features despite high noise ratios\"","weak","figure not available to this review","C2"),
 ("A10","significance","Poses open problems with potential follow-up value: how much to distil from a noisy set, and whether distillation behaviour can estimate the noise rate.","Sec. 4 Insight-I; Corollary-II, Eq. 11","weak","R1, R2 not upheld","C5"),
 ("A11","reproducibility","Uses public datasets, public noise constructions (CIFAR-10 class mappings, CIFAR-100 superclass flips given) and the original evaluation protocols of the three public distillers with the standard ConvNet.","Sec. 4 Implementations: \"a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet\"","moderate","R20 not upheld","general"),
 ("A12","significance","Distillation is a one-off offline step yielding a tiny training set, which could make downstream training cheap and the raw data unnecessary after distillation.","Abstract; Sec. 1 Contributions; Sec. 5","weak","R5 and R6 not upheld","C1"),
]

R = [
 ("R1","technical_rigor","Corollary-II contradicts the paper's own results. For a dataset where IPC images per class already match the full-data accuracy it gives tau >= 1 - C*IPC/|S|, which is near 1 for every setting the paper reports as successful.","Corollary-II, Eq. 11: \"the validation accuracy matches that of the original dataset\"; check: CIFAR-10 (|S|=50,000, standard size, not stated in the paper), C=10, IPC=50 gives tau >= 0.99, but Sec. 4 Exp-I reports success at tau=0.2 with <50 IPC; CIFAR-100N (C=100, IPC<10) gives tau >= 0.98 vs the stated 40.20%. Eq. 11 also inverts the direction of Eq. 10 (which implies tau <= 1 - C*IPC/|S|).","error","major","Withdraw Corollary-II or restate it with a proof and assumptions under which it is consistent with Figs. 2/5; low cost (text) or moderate (new theory)","C5"),
 ("R2","technical_rigor","Both corollaries are given without proof, assumptions or definitions ('perfectly preserve the sample information', delta, the probability space). Eq. 10 reduces to 'IPC is at most the number of clean samples per class' (4,000 on CIFAR-10 at tau=0.2) and so never constrains the IPC range 1-50 studied.","Corollary-I, Eq. 10: \"This corollary succinctly states the upper bound\"; Sec. 4 Exp-III, Eq. 11; recomputed |S|(1-tau)/C = 50,000*0.8/10 = 4,000","gap","major","Either prove the statements with explicit assumptions or relabel them as conjectures/heuristics; low-moderate","C5"),
 ("R3","experimental_validation","The paper presents distillation as 'a new approach to model learning from noisy data' but compares it with no noisy-label method. The only reference is CE training on the full noisy set. The cited sample selection (Co-teaching [14]), semi-supervised (DivideMix [24]), robust-loss (GCE [55]) and early-learning (ELR-style [47]) methods are never run, so it is unknown whether distillation is competitive with the methods it claims to replace.","Sec. 5: \"We propose a new approach to model learning from noisy data that avoids vicious cycles\"; Figure 2 caption: dashed lines are \"training on the full dataset at the corresponding noise rate\"; no other baseline in Sec. 4","gap","fatal","Add at least 3-4 standard noisy-label baselines (CE+early stopping, Co-teaching, GCE, DivideMix) on the same ConvNet and on a standard ResNet; moderate (CIFAR-scale, a few GPU-days)","C1"),
 ("R4","experimental_validation","The full-data reference is under-specified: architecture, epochs, augmentation, learning rate and especially whether early stopping or a clean validation set was used are not stated. CE without early stopping memorises noisy labels, which can inflate the distillation-vs-baseline gap that A4 rests on.","Figure 2/4/5 captions (dashed lines); Sec. 4 Implementations (no baseline settings); search for 'epoch', 'learning rate', 'early stop' finds none in Sec. 4","gap","major","State the baseline protocol; add CE with early stopping on a held-out noisy validation split; low","C2"),
 ("R5","technical_rigor","The privacy claim ('strong privacy protection', 'ensures privacy protection') is untested: there is no threat model, membership-inference or reconstruction attack, or formal guarantee. Whether distilled data protects privacy is contested in the distillation literature.","Abstract: \"providing strong privacy protection through offline processing\"; Sec. 5: \"ensures privacy protection through offline dataset distillation\"; text search: 'privacy' occurs only in claims (Abstract, Sec. 1, Sec. 3.2 Remark, Sec. 5), never in an experiment","error","major","Remove the privacy claim or add a membership-inference evaluation against the distilled sets; low (remove) or moderate (evaluate)","C1"),
 ("R6","technical_rigor","The efficiency claim ('enhances training efficiency') is unmeasured. No distillation time, GPU memory or expert-trajectory cost is reported, and distillation itself (DATM needs expert trajectories trained on the full noisy data) is far costlier than one CE training run.","Abstract: \"avoids the feedback loop common in existing techniques and enhances training efficiency\"; search for 'GPU', 'hour', 'time' finds no measurement; Sec. 3.2 notes DATM's \"significant scalability challenges\"","error","major","Report end-to-end wall-clock and memory (expert training + distillation + student training) against CE and a noisy-label baseline; low","C1"),
 ("R7","technical_rigor","The abstract and contributions state as a finding that tail-class clean samples are lossily compressed in imbalanced datasets, but Sec. 4 only hypothesises this; no imbalanced or long-tailed experiment exists.","Abstract: \"clean but challenging samples, such as those from tail classes in imbalanced datasets, may undergo lossy compression\"; Sec. 4: \"We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets, are at risk\"","error","major","Either run a long-tailed noisy experiment (e.g., CIFAR-10-LT with noise) or move the statement to future work; low-moderate","C3"),
 ("R8","significance","The title's 'In the Wild' and the 'real-world' framing rest on CIFAR-10N/100N only (32x32 images re-annotated by crowd workers). The large real-noise benchmarks named in Sec. 3.1 (Clothing1M, WebVision) are not evaluated, and Tiny-ImageNet is used only with synthetic symmetric noise.","Title; Sec. 3.1: \"high-volume datasets like Clothing1M [48] and WebVision [27] serve as classic benchmarks\"; Sec. 4 Exp-III uses only CIFAR-10N/100N","judgment","major","Add Clothing1M or WebVision (mini) results, or retitle; moderate-high (DATM scalability)","C4"),
 ("R9","experimental_validation","No result is given as a number: the paper has no tables, and every quantitative claim ('consistently outperform', 'significant performance gains') refers to curves in Figures 2, 4 and 5. Gains cannot be checked or compared with other work.","Text search: no 'Table' in the manuscript; Sec. 4 Observation-I: \"consistently demonstrate significant performance gains\"","gap","major","Add tables with accuracy per method x dataset x tau x IPC, and the baseline; low","C2"),
 ("R10","experimental_validation","Seeds, number of runs and variance are not stated anywhere. At CIFAR scale several seeds are the norm, and some claimed effects (DATM 'comparable' under asymmetric noise; crossings near the dashed line) are of a size where run-to-run noise matters.","Text search: 'seed', 'runs', 'std' not found; Figure 2/4/5 captions describe only \"solid lines\" and \"dashed lines\"","gap","major","Report mean +- std over >= 3 seeds for distillation and baselines; moderate compute","C2"),
 ("R11","technical_rigor","Possible selection on the test set: accuracies are 'reported throughout the distillation process' on the test set, and the figure captions call the same quantity 'validation performance'. If the best test accuracy over distillation iterations is reported, the curves are optimistically biased.","Sec. 4 Implementations: \"Final test accuracies are reported throughout the distillation process\"; Figure 2 caption: \"The validation performance over symmetric noise\"","question","major","State which checkpoint is reported and how it is chosen; use a held-out split for selection; low","C2"),
 ("R12","novelty","The related work omits the closest prior art: robust subset/coreset selection under label noise (e.g., Mirzasoleiman, Cao, Leskovec, 'Coresets for Robust Training of Neural Networks against Noisy Labels', NeurIPS 2020) and prior studies of dataset distillation/condensation with noisy labels [verify]. Without them the novelty of 'a new perspective' cannot be placed.","Sec. 2.1-2.2 discuss noisy-label methods and distillation separately; no work combining the two is cited; literature check not run (no network)","judgment","major","Add a related-work paragraph on coreset selection under noise and on noisy-label dataset distillation, and position the delta; low","C1"),
 ("R13","technical_rigor","The mechanism is asserted, not tested. 'Distillation captures common patterns while ignoring outliers such as noise' and 'asymmetric noise is absorbed into the distilled samples' are inferred from accuracy curves only. Nothing measures the label content of the distilled images, the influence of noisy samples, or the role of experts trained on noisy labels (DATM trajectories, DANCE phi_expert).","Sec. 4 Insight-I: \"the distillation process primarily captures common patterns while ignoring outliers such as noise\"; Sec. 4 Observation-II; Eqs. 4, 6-7 (experts trained on the noisy set)","gap","major","Add analyses: expert-epoch ablation for DATM, a probe of distilled-image class evidence (e.g., a clean-trained classifier on the synthetic set), influence of noisy samples; moderate","C2"),
 ("R14","technical_rigor","The claim of avoiding the 'vicious cycle' is not demonstrated. The distillers depend on models trained on the noisy labels (DATM expert trajectories, DANCE's trained encoders), so the noise still shapes the result, only implicitly. No experiment contrasts the feedback-loop failure of existing methods with distillation.","Abstract: \"This method avoids the feedback loop common in existing techniques\"; Sec. 3.2 Eqs. 4, 6-7","judgment","major","Narrow the claim, or show a setting where noise-estimation methods fail through their feedback loop and distillation does not; low (narrow) or moderate","C1"),
 ("R15","significance","Contribution check: the paper proposes no method and benchmarks three existing distillers on noisy CIFAR-scale data. Its insights (symmetric noise averages out; structured noise is preserved; small IPC loses information) are close to what a reader would guess. The delta over distillation and noisy-label work is a refinement-level empirical study.","Sec. 2.2: \"This work first benchmarks existing representative distillation approaches\"; Sec. 1 Empirical Insights (I)-(III)","judgment","major","Turn the observations into a method (e.g., noise-aware distillation for structured noise) or a deeper analysis explaining when and why distillation denoises; high","C1"),
 ("R16","significance","There is no practical recipe. The paper says choosing IPC depends on the unknown noise rate and leaves it open, so a practitioner cannot apply the approach without tuning on clean labels.","Sec. 4 Insight-I: \"How much data should be distilled from a noisy dataset to create a meaningful distilled set?\"; Insight-III","gap","minor","Propose and test an IPC-selection rule using only noisy data; moderate","C4"),
 ("R17","experimental_validation","The evaluation is narrow by distillation standards: only the ConvNet used for distillation, with no cross-architecture evaluation of the distilled sets (standard in the distillation literature). Asymmetric and natural noise are not run on Tiny-ImageNet.","Sec. 4 Implementations (ConvNet only); Figure 4 (CIFAR-10/100 only); Figure 5 (CIFAR-N only)","gap","minor","Evaluate the distilled sets on ResNet-18/VGG; add Tiny-ImageNet asymmetric runs; moderate","C2"),
 ("R18","clarity","Presentation slips: 'Realted Works', 'contributions bellow', 'Both of which' for three noise types; Eq. 4 uses theta-hat_{t+N} while the text defines theta-hat_{t+T}; 'Benchmark-I' is said to denote the accelerated variant of [9], not DATM itself; test vs validation wording is inconsistent (see R11).","Sec. 2 heading: \"Realted Works\"; Sec. 1: \"major contributions bellow\"; Sec. 3.1: \"Both of which are widely employed\"; Sec. 3.2 Eq. 4; Sec. 3.2: \"Benchmark-I referenced later denotes this accelerated version\"","error","minor","Proofread; clarify which DATM variant is used; low","general"),
 ("R19","clarity","The extracted layout (two columns, Figure 1 beside the abstract, bracketed numeric citations) suggests the manuscript is not in the ICLR template, which could be a formatting violation. This cannot be confirmed from extracted text.","Page 1 layout: abstract and Figure 1 caption interleaved in two columns","question","minor","Reformat in the ICLR 2026 template; low","general"),
 ("R20","reproducibility","Key distillation hyperparameters are missing: IPC grid, distillation iterations, expert epochs and trajectories for DATM, learning rates, augmentation for evaluation (except RCIG), and compute. No code release is mentioned.","Sec. 4 Implementations; search for 'epoch', 'iteration', 'learning rate', 'github' finds none","gap","major","Add a hyperparameter table per method/dataset and release code and noisy-label files; low","general"),
 ("R21","ethics","There is no limitations section. The privacy framing ('high-privacy environments') is promotional and its risks are not discussed: distilled images can leak training data, and Figure 3 is presented as recognisable images.","Abstract: \"especially in high-privacy environments where noise is prevalent\"; Sec. 5; Figure 3","gap","minor","Add a limitations paragraph covering privacy leakage and scale; low","C1"),
]

ANSWERED = [
 ("Only symmetric noise is studied.","Sec. 4 Experiment-II (asymmetric, Figure 4) and Experiment-III (CIFAR-10N/100N, Figure 5)"),
 ("Conclusions rest on a single distillation method.","Sec. 3.2: DATM, DANCE and RCIG, one per family"),
 ("The asymmetric noise construction is unspecified.","Sec. 4 Implementations: TRUCK -> AUTOMOBILE, BIRD -> AIRPLANE, DEER -> HORSE, CAT <-> DOG; CIFAR-100 superclass flips"),
 ("The CIFAR-N label sets and their noise rates are unspecified.","Sec. 4 Experiment-III: Random k (~18%), Worst (40.21%), Aggre (9.03%), CIFAR-100N fine (40.20%)"),
 ("Is the evaluation protocol of each distiller altered?","Sec. 4 Implementations: \"following the evaluation protocols of DATM, DANCE, and RCIG, with data augmentation applied for RCIG as recommended\""),
]

# status after Step 2
CHECKED = {"A2","A5","A6","A8","A11","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R14","R15","R17","R18","R20","R21","R16","A1","A10","A12","R13"}
# open: A3,A4,A7,A9 (figures unavailable), R11 (unsettled), R12 (no literature check), R19 (layout)

PROBES = [
 ("P1",["R1","R2","A10"],"Is Corollary-II (Eq. 11) consistent with the settings the paper reports as successful, and with Corollary-I (Eq. 10)?","Recompute the bounds with the standard training-set sizes (CIFAR-10/100: 50,000; not stated in the paper) for the settings quoted in Sec. 4 Exp-I and Exp-III; compare the inequality directions of Eqs. 10 and 11.","confirmed","Corollary-II, Eq. 11; Sec. 4 Exp-I/III","Eq. 11 at CIFAR-10, IPC=50 gives tau >= 0.99 vs the reported success at tau=0.2; CIFAR-100N, IPC<10 gives tau >= 0.98 vs 40.20%. Eq. 10 rearranges to tau <= 1 - C*IPC/|S|, the reverse of Eq. 11. Eq. 10 gives IPC <= 4,000 at tau=0.2, vacuous for IPC 1-50. No proof anywhere.","R1 open -> checked (error confirmed by recomputation); R2 open -> checked; A10 weak (condition fails)"),
 ("P2",["R3","A4"],"Does Sec. 4 compare distillation with any noisy-label learning method beyond CE on the full noisy set?","Re-read Sec. 4 and all figure captions; search for the cited methods (Co-teaching, DivideMix, GCE, DISC) outside Sec. 2.","confirmed","Figure 2/4/5 captions; Sec. 4","The only reference line is \"training on the full dataset at the corresponding noise rate\". Cited methods appear only in Sec. 1-2.","R3 open -> checked (gap confirmed); A4 depends on R4"),
 ("P3",["R4","A4"],"Is the full-data baseline's training protocol (architecture, epochs, early stopping, augmentation) given anywhere?","Search the full text for 'epoch', 'learning rate', 'early stop', 'augmentation', 'baseline'.","confirmed","Sec. 4 Implementations","No baseline protocol is given. 'Early stopping' appears only in reference [25]; augmentation is mentioned only for RCIG's distilled-set evaluation.","R4 open -> checked; A4 stays moderate but conditional"),
 ("P4",["R5","R6","A12","R21"],"Is there any experiment or measurement behind the privacy and efficiency claims?","Search for 'privacy', 'efficien', 'GPU', 'hour', 'time', 'memory', 'attack', 'membership'.","confirmed","Abstract; Sec. 1; Sec. 3.2 Remark; Sec. 5","'Privacy' occurs 6 times, all in claims. 'Efficien' occurs only in claims and in describing [9] and [30]. No timing, memory or attack results.","R5, R6 open -> checked (E5 claim distortion confirmed); A12 weak"),
 ("P5",["R7"],"Does any experiment test the imbalanced/tail-class claim made in the abstract and contributions?","Search for 'imbalanc', 'tail', 'long-tail'; re-read Sec. 4.","confirmed","Sec. 4 after Insight-II","All 4 'imbalanc' hits are claims or the hypothesis: \"We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets...\". No experiment.","R7 open -> error (checked)"),
 ("P6",["R11"],"Is the reported accuracy the final, a fixed-iteration or the best test accuracy over distillation, and is any validation split used for selection?","Re-read Sec. 4 Implementations and the figure captions.","unsettled","Sec. 4 Implementations; Figure 2/4 captions","\"Final test accuracies are reported throughout the distillation process\" can mean either a final-iteration value or a running maximum. The captions say 'validation performance'; no validation split is defined.","R11 stays open (question; no grade above minor)"),
 ("P7",["R9","R10"],"Does the paper give numbers or variance for any result?","Search for 'Table', 'seed', 'runs', 'std', 'mean'; read the captions of Figures 2, 4, 5.","confirmed","whole manuscript","No tables. No seeds or runs stated. The captions describe solid trend lines and dashed reference lines only; whether the plots show bands cannot be seen.","R9 open -> checked; R10 open -> checked (not stated after search)"),
 ("P8",["R8","A6"],"Which real-noise datasets are actually evaluated?","Trace C4 from Sec. 3.1 to Sec. 4 Exp-III and Figure 5.","confirmed","Sec. 3.1; Sec. 4 Exp-III; Figure 5","Only CIFAR-10N and CIFAR-100N. Clothing1M and WebVision are introduced in Sec. 3.1 but never used.","R8 open -> checked; A6 moderate (limited scale)"),
 ("P9",["R12","A1"],"Is there prior work on distillation or subset selection for learning with noisy labels that the paper omits?","Re-read Sec. 2; literature query not possible (no network). Rely on memory, with [verify] where unsure.","unsettled","Sec. 2.1-2.2","No combined work is cited. From memory, robust coreset selection under label noise (Mirzasoleiman, Cao, Leskovec, NeurIPS 2020) is directly related. Prior noisy-label dataset-distillation studies may exist [verify]. Not settled without a search.","R12 stays open (judgment, novelty rests on memory, [verify])"),
 ("P10",["R13","R14"],"Are the distillers' teacher/expert models trained on the noisy labels, so that noise enters distillation implicitly?","Re-read Sec. 3.2: Eq. 4 (expert trajectories theta*), Eqs. 6-7 (phi_expert), Eqs. 8-9 (RCIG trained against L_T on the full noisy training set); check for an analysis of this.","confirmed","Sec. 3.2 Eqs. 4, 6-9; Sec. 3.1 Training Protocol","Experts are 'trained on real images', which in this setup are the noisy set S-tilde. L_T is the loss on the full training set. No ablation of expert epochs or of the expert's noise exposure.","R13 open -> checked; R14 open -> checked"),
 ("P11",["A3","A4","A7","A9"],"Can the figure-based accept reasons be verified from the text?","Trace each claim to its figure; check the textual statements for internal consistency.","partly","Sec. 4 Exp-I/III; Figures 2, 3, 5","The text statements agree with one another (gain grows with noise; Aggre is the weak case). The magnitudes and the curves themselves cannot be read from the extracted text.","A3, A4, A7, A9 stay open (figure-dependent)"),
]

# Reviewer types
T = [
 dict(id="T1",name="Learning-with-noisy-labels specialist",aspect="experimental_validation",field="the task: learning with noisy labels",likelihood="high",
      expertise="robust training under label noise (sample selection, robust losses, semi-supervised correction) on CIFAR-N/Clothing1M/WebVision",
      values="competitive comparison with standard noisy-label baselines on standard benchmarks and backbones",
      distrusts="weak CE baselines without early stopping; CIFAR-only 'real-world' claims; no numbers",
      weighs=["R3","R4","R8","R9","R10","R11","R16","A3","A4","A6"],
      grades={"R3":"fatal","R4":"major","R8":"major","R9":"major","R10":"minor","R11":"minor","R16":"minor"},
      held=["A3","A6"],discounted=["A4","A1"],
      reading=["Holds A3 (the sweep over tau and IPC is the right shape of experiment) and A6 (CIFAR-N is the community's standard human-noise test).",
               "Discounts A4: a single CE run on the full noisy set, of unstated protocol (R4), is the weakest reference available. Co-teaching- or DivideMix-style methods, cited in Sec. 2.1, are the obvious stronger references, and the paper never runs them. Discounts A1: a framing that is never compared against the methods it critiques cannot show it is better.",
               "R3: fatal. The paper's stated contribution is 'a new approach to model learning from noisy data' (Sec. 5), and no noisy-label method is run.",
               "R4: major. Without early stopping, CE memorises noise, so the dashed lines may be artificially low.",
               "R8: major. 'In the Wild' rests on 32x32 CIFAR-N; Clothing1M/WebVision are named but not run.",
               "R9: major. Without tables I cannot compare against any published number.",
               "R10: minor. Single runs are common in distillation papers and the claimed gaps at high noise are large. (Updated after P12: minor -> major; R10 is not decisive for T1, so the scores are unchanged.)",
               "R11: minor (unsettled question).",
               "R16: minor. Choosing IPC without knowing tau is an open problem the paper names honestly."],
      opinion="From the noisy-label side, the question is simple: if I have a noisy CIFAR-10, should I distil it instead of running a standard robust-training method? The paper cannot answer this, because the only comparison is against vanilla cross-entropy on the full noisy data, with an unreported protocol (R3, R4). Beating that reference at tau=0.8 with IPC=1 (A4) is interesting, but it mostly restates that unregularised CE memorises noise, which the paper itself cites [1, 47]. The experiments have the right shape (A3, A6), but they report no numbers (R9) and the 'wild' setting is CIFAR-N only (R8). Asymmetric noise, the common case in practice, is where distillation fails (A5), which further limits its practical use. What would change my mind: a table on CIFAR-10N/100N and one large real-noise set, with CE+early stopping, Co-teaching, GCE and DivideMix on the same and on a standard backbone. Distillation would need to be competitive, or to offer a clearly argued trade-off such as cost or privacy, measured.",
      decisive="R3 (fatal), R4 (major), R9 (major), A6 (moderate, held)",
      pool=15, scores=dict(technical_rigor=40,clarity=52,novelty=45,significance=38,experimental_validation=30,reproducibility=42,ethics=58), overall=2, confidence=4),
 dict(id="T2",name="Dataset distillation researcher",aspect="novelty",field="neighbor: dataset distillation / condensation",likelihood="high",
      expertise="trajectory-, distribution- and kernel-based dataset distillation; evaluation protocols of DD benchmarks",
      values="a new mechanism or a new understanding of what distilled data encodes; standard DD protocols (cross-architecture, multiple IPC)",
      distrusts="benchmark-only studies of existing distillers; missing cross-architecture evaluation; unexplained mechanisms",
      weighs=["R12","R13","R15","R17","R18","A1","A2","A8","A9"],
      grades={"R12":"minor","R13":"major","R15":"major","R17":"major","R18":"minor"},
      held=["A1","A2","A8"],discounted=["A9"],
      reading=["Holds A1: framing distillation as a denoiser is a genuinely new use of the tool in this literature. Holds A2: one method per family is the right design. Holds A8.",
               "Discounts A9: one IPC=1 image grid (not visible here) is not evidence of what the synthetic set encodes.",
               "R12: minor. Coreset selection under noise is a different mechanism (selection, not synthesis), so I see the transfer to synthetic distillation as the paper's delta. Noisy-label DD prior work is unverified.",
               "R13: major. DATM matches early segments of expert trajectories, and early training is known to fit clean labels first. That alone could explain Insight-I, and the paper never ablates it.",
               "R15: major. The study runs existing distillers with no modification.",
               "R17: major. Cross-architecture evaluation is standard in DD; a ConvNet-only result says little.",
               "R18: minor."],
      opinion="I find the core observation, that distillers act as implicit label denoisers under symmetric noise, a worthwhile idea for the distillation community (A1), studied across the three main families (A2). But the paper stops at the observation. Contribution check: (1) What does a reader learn? That symmetric noise mostly averages out in distillation and structured noise does not. This is plausible a priori, and no 'why' is established (R13). (2) Does the setting support 'in the wild'? No, only CIFAR-N (R8). (3) The delta is a refinement: existing DATM/DANCE/RCIG, unmodified, on noisy CIFAR (R15). (4) Transfer to practical settings is doubtful without cross-architecture and larger-scale results (R17). The obvious next step is missing: a noise-aware distiller that handles the asymmetric case, which the paper's own Insight-II motivates. It would turn this into a method paper. As it stands it is an interesting workshop-level study. I would raise my view with a mechanism analysis (expert-epoch ablation, label content of the distilled images) and a modest method for structured noise.",
      decisive="R15 (major), R13 (major), A1 (moderate, held), A2 (held)",
      pool=30, scores=dict(technical_rigor=46,clarity=56,novelty=50,significance=46,experimental_validation=45,reproducibility=48,ethics=60), overall=3, confidence=4),
 dict(id="T3",name="Learning-theory reviewer (memorization and generalization under label noise)",aspect="technical_rigor",field="neighbor: learning theory",likelihood="medium",
      expertise="theory of memorization, early learning and generalization with noisy labels",
      values="precise statements with assumptions and proofs; theory consistent with experiments",
      distrusts="'corollaries' with no derivation; probabilistic statements with undefined probability spaces",
      weighs=["R1","R2","R13","R14","R7","A10","A5"],
      grades={"R1":"major","R2":"major","R13":"major","R14":"major","R7":"minor"},
      held=["A5"],discounted=["A10"],
      reading=["Holds A5: the asymmetric-noise failure is an honest and informative negative result.",
               "Discounts A10: the noise-rate estimate is built on Eq. 11, which P1 shows is inconsistent with the data.",
               "R1: major. Eq. 11 yields tau >= 0.99 for CIFAR-10 at IPC=50, contradicting Sec. 4; it is not a main claim, but it is presented as a result.",
               "R2: major. Neither corollary has a proof or assumptions; Eq. 10 is vacuous.",
               "R13: major. The 'common patterns first' mechanism is borrowed from memorization theory [1] but never tested in distillation.",
               "R14: major. The experts see noisy labels, so the noise is not avoided.",
               "R7: minor. The tail-class claim is an overstatement, but it is labelled a hypothesis in Sec. 4."],
      opinion="The paper's conceptual link between memorization (networks fit common patterns first) and distillation (distillers synthesise common patterns) is suggestive. The formal content does not hold up. Corollary-I (Eq. 10) is the trivial statement that one cannot keep more clean samples per class than exist, and it never constrains the IPC range studied (R2). Corollary-II (Eq. 11) reverses that inequality without derivation. With the paper's own settings it predicts noise rates of 98-99.98% whenever a few distilled images match full-data accuracy, contradicting the reported tau=0.2 and 40% cases (R1). Neither has a proof, a probability space or a definition of delta. The mechanism claims (R13, R14) are the interesting science here, and they are only asserted: an expert-trajectory-length ablation would directly test whether distillation inherits early-learning robustness. I would need the corollaries removed or proved correctly, and one mechanistic experiment, before I could see the paper as sound.",
      decisive="R1 (major), R2 (major), R13 (major)",
      pool=15, scores=dict(technical_rigor=32,clarity=48,novelty=44,significance=38,experimental_validation=38,reproducibility=40,ethics=55), overall=2, confidence=4),
 dict(id="T4",name="Evaluation and protocol methodologist",aspect="technical_rigor",field="neighbor: ML evaluation methodology",likelihood="medium",
      expertise="experimental protocol, claim-to-evidence tracing, statistical reporting",
      values="every claim backed by a reported, reproducible measurement with variance and a clean selection protocol",
      distrusts="claims in the abstract with no experiment; test-set selection; figures without numbers",
      weighs=["R5","R6","R7","R9","R10","R11","R19","R20","A11","A2"],
      grades={"R5":"major","R6":"major","R7":"major","R9":"major","R10":"major","R11":"minor","R19":"minor","R20":"major"},
      held=["A11","A2"],discounted=[],
      reading=["Holds A11 (public data and public distillers make re-running possible) and A2.",
               "R5: major. A headline claim in the abstract and conclusion with zero evidence (P4).",
               "R6: major. Same; and distillation cost likely exceeds plain training.",
               "R7: major. The abstract reports as a finding what Sec. 4 calls a hypothesis (P5).",
               "R9: major. No tables at all.",
               "R10: major. CIFAR-scale experiments should report >= 3 seeds.",
               "R11: minor (unsettled; the wording is ambiguous).",
               "R19: minor (unverifiable from text).",
               "R20: major. Hyperparameters for three distillers on three datasets are absent."],
      opinion="I traced each claim in the abstract to its evidence. 'Denoises symmetric noise' leads to Figure 2, with curves but no numbers. 'Struggles with asymmetric noise' leads to Figure 4. 'Effective on natural noise' leads to Figure 5, CIFAR-N only. 'Tail classes are lossily compressed' leads to no experiment (R7). 'Enhances training efficiency' leads to no measurement (R6). 'Strong privacy protection' leads to no analysis (R5). So three of the six abstract claims have no supporting experiment, and the other three are supported only by figures, with no numbers (R9), no variance (R10) and an ambiguous checkpoint-selection protocol (R11). Reproduction would also be hard: no IPC grid, no iteration counts, no expert settings (R20). Fixing the reporting is cheap: tables, seeds, a selection statement, and narrowing the abstract. Fixing the evidence for privacy and efficiency is moderate work. Until then I cannot treat the conclusions as established.",
      decisive="R5 (major), R7 (major), R9 (major), R20 (major)",
      pool=15, scores=dict(technical_rigor=34,clarity=46,novelty=45,significance=40,experimental_validation=34,reproducibility=35,ethics=48), overall=2, confidence=4),
 dict(id="T5",name="Data-centric ML researcher (coreset selection and data pruning)",aspect="significance",field="neighbor: data-centric ML, coreset selection / data pruning",likelihood="medium",
      expertise="subset selection, data pruning and data valuation, including under label noise",
      values="a usable data-curation recipe that beats selection baselines at matched budget",
      distrusts="ignoring selection baselines at the same budget; no recipe for choosing the budget",
      weighs=["R12","R15","R16","R3","R6","A4","A7","A12"],
      grades={"R12":"major","R15":"major","R16":"major","R3":"major","R6":"major"},
      held=["A4","A7"],discounted=["A12"],
      reading=["Holds A4 (the high-noise effect is surprising to a data-pruning reader) and A7 (the trade-off is real and worth stating).",
               "Discounts A12: there is no cost accounting (R6).",
               "R12: major. Robust coreset selection under label noise addresses the same goal, a small subset that trains well despite noise, and it is the natural matched-budget baseline. Its absence leaves the delta unplaced.",
               "R15: major. No method.",
               "R16: major. Without an IPC rule the approach is not usable, and this is central to significance.",
               "R3: major. Selection and noisy-label baselines are both missing.",
               "R6: major."],
      opinion="To a data-curation reader, the paper's real claim is that synthesis beats selection or full data under heavy symmetric noise. That is worth knowing (A4), but the matched-budget comparison is missing: a coreset or small-loss selection at the same IPC (R12, R3). Without it, the effect might come from compressing the data, not from distilling it. Significance is limited further because the budget (IPC) has to be chosen with knowledge of tau, which the paper admits is open (R16), and because the failure under asymmetric noise covers much of practical label noise. Contribution check: the reader learns a plausible regularity, not why it holds; the delta is an application of existing distillers; and transfer to large, realistic noisy datasets is untested (R8). I would move up with a matched-budget selection baseline and a noisy-data-only IPC rule.",
      decisive="R12 (major), R16 (major), R15 (major), A4 (held)",
      pool=22, scores=dict(technical_rigor=42,clarity=52,novelty=42,significance=40,experimental_validation=40,reproducibility=45,ethics=58), overall=2, confidence=3),
 dict(id="T6",name="Privacy and trustworthy-ML researcher",aspect="significance",field="neighbor: privacy-preserving ML",likelihood="low",
      expertise="membership inference, data reconstruction, privacy of synthetic and distilled data",
      values="privacy claims backed by a threat model and attacks, or a formal guarantee",
      distrusts="'privacy for free' claims from synthetic data; promotional framing",
      weighs=["R5","R21","R6","R8","R15","A10","A12"],
      grades={"R5":"major","R21":"minor","R6":"minor","R8":"minor","R15":"major"},
      held=[],discounted=["A10","A12"],
      reading=["Discounts A12 and A10: the privacy and efficiency benefits are asserted, not shown.",
               "R5: major. 'Ensures privacy protection' is a strong claim, and whether distilled data protects membership privacy is contested in the literature, so it needs evidence.",
               "R21: minor. No limitations discussion of leakage.",
               "R6: minor (outside my expertise).",
               "R8: minor.",
               "R15: major. Without the privacy evidence, what remains is a benchmark of existing distillers."],
      opinion="The paper sells its approach partly on privacy: it 'ensures privacy protection through offline dataset distillation' and suits 'high-privacy environments'. Nothing in the manuscript tests this (R5). There is no threat model, no membership-inference or reconstruction attack on the distilled sets, and no differential-privacy accounting. The distillers also need full access to the raw labelled data, which is where the privacy risk lies. Figure 3 is described as showing recognisable class images, so leakage is at least plausible and deserves a limitations paragraph (R21). If the privacy claim were removed, my significance assessment would rest on the denoising observation alone, which I see as modest (R15). Adding a standard membership-inference evaluation, or dropping the claim, would remove my main objection.",
      decisive="R5 (major), R15 (major)",
      pool=22, scores=dict(technical_rigor=40,clarity=54,novelty=46,significance=40,experimental_validation=40,reproducibility=45,ethics=45), overall=2, confidence=3),
]

POST = [("P12",["R10"],"Do the captions or text of Figures 2, 4 and 5 indicate variance bands or multiple runs (T1 assumed variance might be shown in the figures; T4 assumed it is absent)?","Re-read every figure caption and Sec. 4 for 'mean', 'std', 'shaded', 'runs', 'seeds'.","partly","Figure 2/4/5 captions; Sec. 4","The captions describe only solid accuracy lines and dashed full-data lines. Nothing mentions bands, means or runs, and the plots cannot be seen.","T1: R10 minor -> major (updated after P12); not decisive for T1, so T1's scores are unchanged")]

def main():
    led = {"accept":[], "reject":[], "answered":[], "probes":[], "types":[]}
    for a in A:
        led["accept"].append(dict(id=a[0],aspect=a[1],reason=a[2],location=a[3],strength=a[4],depends_on=a[5],claim=a[6],
                                  status="checked" if a[0] in CHECKED else "open",added_by=None))
    # strength updates after probes
    for e in led["accept"]:
        if e["id"] in ("A10","A12"): e["strength"]="weak"
    for r in R:
        led["reject"].append(dict(id=r[0],aspect=r[1],reason=r[2],location=r[3],kind=r[4],worst_case=r[5],fix=r[6],claim=r[7],
                                  status="checked" if r[0] in CHECKED else "open",added_by=None))
    for q,loc in ANSWERED:
        led["answered"].append(dict(reason=q,answered_at=loc))
    for p in PROBES:
        led["probes"].append(dict(id=p[0],items=p[1],question=p[2],method=p[3],result=p[4],location=p[5],finding=p[6],change=p[7],after_reviews=False))
    for p in POST:
        led["probes"].append(dict(id=p[0],items=p[1],question=p[2],method=p[3],result=p[4],location=p[5],finding=p[6],change=p[7],after_reviews=True))
    for t in T:
        g = dict(t["grades"])
        if t["id"]=="T1": g["R10"]="major"  # updated after P12
        dec = [x.split(" ")[0] for x in t["decisive"].split(", ")]
        led["types"].append(dict(id=t["id"],name=t["name"],likelihood=t["likelihood"],grades=g,held=t["held"],discounted=t["discounted"],
                                 aspect=t["aspect"],field=t["field"],decisive=dec,pool_position=t["pool"],overall=t["overall"],confidence=t["confidence"],
                                 weighs_most=t["weighs"]))
    json.dump(led, open(os.path.join(D,"ledger.json"),"w"), indent=1, ensure_ascii=False)
    sc = {"paper_type":"analysis","reviewers":[dict(role=f'{t["id"]} ({t["name"]})',aspect=t["aspect"],confidence=t["confidence"],overall=t["overall"],
            pool_position=t["pool"],scores=t["scores"]) for t in T],"da_critical":[]}
    json.dump(sc, open(os.path.join(D,"scores.json"),"w"), indent=1)
    # coverage check
    ids = {a[0] for a in A}|{r[0] for r in R}
    covered = set().union(*[set(t["weighs"]) for t in T])
    print("uncovered:", sorted(ids-covered))
    # consensus
    cons = {}
    for t in led["types"]:
        for k,v in t["grades"].items(): cons.setdefault(k,[]).append(f'{t["id"]} {v}')
        for k in t["held"]: cons.setdefault(k,[]).append(f'{t["id"]} held')
        for k in t["discounted"]: cons.setdefault(k,[]).append(f'{t["id"]} discounted')
    json.dump(cons, open(os.path.join(D,"_consensus.json"),"w"), indent=1)
    n=len(T)
    for r in R:
        gs=[t["grades"].get(r[0]) for t in led["types"]]
        nf=gs.count("fatal"); nm=gs.count("major")
        pr = 1 if nf>0 or nm>=n/2 else (2 if nm>0 else (3 if "minor" in gs else "-"))
        print(r[0], "fatal",nf,"major",nm,"P",pr)
main()
