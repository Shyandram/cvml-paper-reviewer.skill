import json, sys
out = sys.argv[1]
A = [
 ("A1","novelty","Reframes noisy-label learning as data condensation, sidestepping the detect-then-correct vicious cycle; disclosed transfer from dataset distillation","Section 1 Motivation; Section 3.1 Remark","moderate","C7","checked"),
 ("A2","experimental_validation","Covers three DD families (DATM, DANCE, RCIG) under symmetric, asymmetric and natural noise on CIFAR-10/100, Tiny-ImageNet, CIFAR-10N/100N","Section 3.2; Section 4; Figures 2, 4, 5","moderate","C1","checked"),
 ("A3","significance","Under heavy symmetric noise one distilled image per class beats training on the full noisy set","Section 4 Experiment-I; Figure 2(a)","moderate","C1","open"),
 ("A4","significance","Honest negative result: structured asymmetric noise is absorbed into the distilled set, qualifying the thesis","Section 4 Observation-II, Insight-II; Figure 1(b); Figure 4","moderate","C2","checked"),
 ("A5","experimental_validation","Tests real human-annotation noise (CIFAR-10N/100N) and reports the low-noise (Aggre) failure","Section 4 Experiment-III; Figure 5","moderate","C3","checked"),
 ("A6","clarity","Self-contained background: noise models and the three distillers' objectives","Section 3.1 Eq. 1-2; Section 3.2 Eq. 4-9","weak","general","checked"),
 ("A7","experimental_validation","Visualization of DATM distilled images across noise rates","Figure 3; Section 4","weak","C1","open"),
 ("A8","significance","Practical motivation: offline distillation as preprocessing in privacy-sensitive noisy settings","Section 1","weak","C5","checked"),
 ("A9","technical_rigor","Poses how much to distill per noise rate and gives closed-form IPC/noise bounds","Section 4 Insight-I; Eq. 10; Eq. 11; Figure 1(a)","weak","C6","checked"),
 ("A10","reproducibility","Follows original DATM/DANCE/RCIG evaluation protocols with standard ConvNets","Section 4 Implementations","weak","general","checked"),
]
R = [
 ("R1","experimental_validation","No learning-with-noisy-labels baseline; only CE on the full noisy set, although the paper claims a new approach to learning from noisy data","Figure 2 caption; Section 5; Sections 1-2 (cited LNL methods)","gap","fatal","Add >=3 LNL methods on the same backbone and data, with compute; a few GPU-days","C5","checked",None),
 ("R2","technical_rigor","No control separating denoising from data reduction/regularization (random subset, coreset, early-stopped CE, clean subset); baseline schedule not stated","Section 4 Experiment-I; Figure 2 caption","gap","major","Add those controls at each IPC; hours of GPU","C1","checked",None),
 ("R3","technical_rigor","Possible selection on the test set: accuracies reported throughout distillation, captions say validation, no validation split defined","Section 4 Implementations; Figure 2 and 4 captions","question","fatal","State checkpoint selection; use a held-out noisy validation split","C1","open",None),
 ("R4","technical_rigor","Mechanism unanalyzed: expert trajectories/encoders' training data and epochs unstated; effect may be early-learning/early stopping","Section 3.2 Eq. 4, 6, 7; Section 4 Implementations","gap","major","Report expert training; ablate trajectory range and clean vs noisy experts","C1","open",None),
 ("R5","technical_rigor","Corollary-II unproved, lacks accuracy and delta terms, contradicted by the paper's own results (tau >= 0.99 for CIFAR-10 IPC 50; >= 0.98 for CIFAR-100N IPC 10) and reversed relative to Eq. 10","Section 4 Corollary-II, Eq. 11; Eq. 10; Section 4 Experiments I, III","error","major","Remove or prove and check against Figures 2 and 5","C6","checked",None),
 ("R6","technical_rigor","Corollary-I is a counting identity (clean samples per class) and ill-posed as a requirement","Section 4 Corollary-I, Eq. 10","judgment","minor","Recast as a remark or replace with a predictive analysis","C6","checked",None),
 ("R7","significance","Strong privacy protection claimed but never measured (no membership inference, no DP)","Abstract; Section 5","gap","major","Remove or add membership-inference evaluation","C5","checked",None),
 ("R8","significance","Training efficiency claimed but no distillation/training cost reported; distillers need full-data expert training","Abstract; Section 1; Section 5; Section 3.2","gap","major","Report end-to-end wall-clock and memory vs CE and LNL","C5","checked",None),
 ("R9","significance","Tail-class/imbalance lossy-compression claim in abstract, contributions, conclusion, but only hypothesized; no experiment","Section 4 (We further hypothesize); Abstract; Section 5","gap","major","Run CIFAR-LT with noise or demote the claim","C4","checked",None),
 ("R10","significance","'In the Wild' backed only by CIFAR-10N/100N; Clothing1M and WebVision named but unused","Section 3.1; Section 4 Experiment-III","judgment","major","Add Clothing1M/mini-WebVision or retitle","C3","checked",None),
 ("R11","experimental_validation","Only 3-4-layer ConvNets on <=64x64 images; no cross-architecture or larger-backbone evaluation","Section 4 Implementations","gap","major","Evaluate on ResNet-18; distill with larger backbone; ~1 GPU-day","C3","checked",None),
 ("R12","experimental_validation","No seeds, runs or variance; claims rest on single curves","Figures 2, 4, 5; omission sweep","gap","major","Mean +- std over >=3 seeds","C1","checked",None),
 ("R13","novelty","No new method; 'novel approach' overstates a benchmark of three existing distillers; coreset-under-noise and noisy-DD prior work not discussed [verify]","Abstract; Section 3.2; Section 2","judgment","major","Reframe; position against prior work; or propose a noise-aware distiller","C7","checked",None),
 ("R14","reproducibility","No hyperparameters, distillation iterations, expert details or code","Section 4 Implementations; omission sweep","gap","major","Implementation appendix; release code and distilled sets","general","checked",None),
 ("R15","clarity","Results only as plots; no accuracy numbers or tables","Section 4; Figures 2, 4, 5","gap","minor","Add accuracy tables at IPC 1/10/50","general","checked",None),
 ("R16","clarity","Eq. 4 uses t+N vs text t+T; 'Both of which' for three noise types; typos; Worst vs CIFAR100N mix-up","Section 3.2 Eq. 4; Section 3.1; Section 2 heading; Section 1; Section 4 Experiment-III","error","minor","Proofread and fix","general","checked",None),
 ("R17","significance","Insights restate memorization/early-learning theory; no quantitative why/when analysis","Section 3.1 Remark; Section 4 Insight-I, Insight-II","judgment","major","Mechanism study or validated predictive rule","C2","checked",None),
 ("R18","clarity","Layout appears to be a CVPR-style template rather than ICLR's; cannot confirm from extracted text","Figure 1 caption; reference style","question","major","Re-typeset in ICLR template","general","open",None),
 ("R19","technical_rigor","Whether DATM's expert-filtered initialization/soft labels [verify] perform explicit noise filtering, contrary to 'avoids the feedback loop'","Section 3.2 Benchmark-I; Abstract","question","major","State init/label scheme; ablate","C5","open",None),
 ("R20","experimental_validation","Insight-I proposes estimating the noise proportion from distillation, but tau is never estimated","Section 4 Insight-I; Corollary-II","gap","minor","Estimate tau on CIFAR-N and compare with known rates","C6","checked","T3"),
]
answered = [
 {"reason":"Only synthetic noise is tested","answered_at":"Section 4 Experiment-III; Figure 5 (CIFAR-10N/100N)"},
 {"reason":"Only one distillation family is tested","answered_at":"Section 3.2 (parameter matching, distribution matching, meta-learning)"},
 {"reason":"Only favorable results are reported","answered_at":"Section 4 Experiment-II / Figure 4 (asymmetric failure); Experiment-III (Aggre failure)"},
 {"reason":"Asymmetric-noise construction undefined","answered_at":"Section 4 Implementations; Eq. 2"},
]
probes = [
 ("P1",["R3","A3"],"Is the reported accuracy chosen on the test set; is a validation split used?","re-read Section 4 and figure captions; text search","unsettled","Section 4 Implementations; Figure 2/4 captions","R3 open question -> stays open question (<= minor)",False),
 ("P2",["R5","A9"],"Is Corollary-II consistent with the paper's own results?","recompute Eq. 11 bound for reported settings","confirmed","Section 4 Corollary-II; Experiments I, III","R5 open -> error (checked); A9 weak, condition failed",False),
 ("P3",["R1"],"Does the paper compare with any LNL method?","trace every baseline mention","confirmed","Figures 2, 4, 5 captions; Section 4 Observation-I","R1 open -> checked gap",False),
 ("P4",["R2","A3"],"Is there any random-subset/coreset/early-stopping/clean-subset control, and is the baseline schedule stated?","re-read Section 4; text search","confirmed","Section 4 Implementations, Experiments I-III","R2 open -> checked; A3 conditional",False),
 ("P5",["R7","R8","A8"],"Does the paper measure privacy or compute anywhere?","text search and in-place reading","confirmed","Abstract; Section 1; Section 3.2; Section 5","R7, R8 open -> checked; A8 condition fails",False),
 ("P6",["R9"],"Is there any imbalanced-data or tail-class experiment?","text search","confirmed","Abstract; Section 1; Section 4; Section 5","R9 open -> checked",False),
 ("P7",["R10","R11"],"Which datasets and architectures support the in-the-wild claims?","trace C3 -> Experiment-III -> Figure 5; text search","confirmed","Section 3.1; Section 4","R10, R11 open -> checked",False),
 ("P8",["R4","R19"],"How are experts trained and synthetic sets initialized/labeled?","re-read Section 3.2 and Section 4","unsettled","Section 3.2; Section 4 Implementations","R4 stays open gap; R19 stays open question (<= minor)",False),
 ("P9",["R13","A1"],"Does the paper propose a new method and discuss data-selection-under-noise prior work?","re-read Abstract, Section 1-3; no literature query (no network)","partly","Abstract; Section 2; Section 3.2","R13 open -> checked for framing; prior art stays [verify]",False),
 ("P10",["R12","R14"],"Are seeds, variance, hyperparameters or code stated?","omission sweep text search","confirmed","whole text","R12, R14 open -> checked",False),
 ("P11",["R2"],"Is the full-data baseline trained with matched ConvNet, schedule and early stopping (T1/T2/T4/T6 major vs T5 minor)?","re-read Section 4 and Figure 2 caption","unsettled","Section 4 Implementations, Experiment-I; Figure 2 caption","T5 R2 minor -> major",True),
]
types = [
 dict(id="T1",name="Noisy-label learning specialist",likelihood="high",grades={"R1":"fatal","R2":"major","R3":"minor","R10":"major","R12":"major","R11":"major"},held=["A2","A5","A4"],discounted=["A3"],aspect="experimental_validation",field="the task: learning with noisy labels",decisive=["R1","R2","R10","R12","A5","A3"],pool_position=15,overall=2,confidence=4),
 dict(id="T2",name="Dataset distillation specialist",likelihood="high",grades={"R4":"major","R19":"minor","R14":"major","R11":"major","R2":"major","R16":"minor","R12":"minor"},held=["A2","A6","A7"],discounted=["A10"],aspect="technical_rigor",field="dataset distillation / condensation",decisive=["R4","R14","R11","R2","A2"],pool_position=22,overall=2,confidence=4),
 dict(id="T3",name="Learning-theory and memorization theorist",likelihood="medium",grades={"R5":"major","R6":"minor","R17":"major","R3":"minor","R20":"minor"},held=["A4"],discounted=["A9"],aspect="technical_rigor",field="learning theory (memorization, early learning)",decisive=["R5","R17","R6","A9"],pool_position=15,overall=2,confidence=3),
 dict(id="T4",name="Data-centric ML and coreset-selection researcher",likelihood="medium",grades={"R13":"major","R2":"major","R17":"major","R1":"major"},held=["A1","A4"],discounted=[],aspect="novelty",field="coreset selection, data pruning, data valuation",decisive=["R13","R2","R17","A1"],pool_position=32,overall=3,confidence=3),
 dict(id="T5",name="Privacy and trustworthy-ML researcher",likelihood="low",grades={"R7":"major","R8":"major","R9":"minor","R2":"major"},held=["A3"],discounted=["A8"],aspect="significance",field="privacy-preserving ML",decisive=["R7","R8","A8"],pool_position=18,overall=2,confidence=3),
 dict(id="T6",name="Large-scale robust-training practitioner",likelihood="medium",grades={"R10":"major","R11":"major","R8":"major","R9":"major","R2":"major","R15":"minor","R18":"minor"},held=["A2"],discounted=["A3","A5"],aspect="significance",field="web-scale noisy-label training",decisive=["R10","R11","R8","R9","A3"],pool_position=15,overall=2,confidence=4),
]
d = {
 "accept":[dict(id=i,aspect=a,reason=r,location=l,strength=s,added_by=None,claim=c,status=st) for i,a,r,l,s,c,st in A],
 "reject":[dict(id=i,aspect=a,reason=r,location=l,kind=k,worst_case=w,fix=f,added_by=ab,claim=c,status=st) for i,a,r,l,k,w,f,c,st,ab in R],
 "answered":answered,
 "probes":[dict(id=i,items=it,question=q,method=m,result=res,location=l,change=ch,after_reviews=ar) for i,it,q,m,res,l,ch,ar in probes],
 "types":types,
}
# sanity: grades never exceed worst case; questions <= minor
rank={"not a concern":0,"minor":1,"major":2,"fatal":3}
wc={x["id"]:x for x in d["reject"]}
for t in types:
    for k,g in t["grades"].items():
        assert rank[g]<=rank[wc[k]["worst_case"]],(t["id"],k)
        if wc[k]["kind"]=="question": assert rank[g]<=1,(t["id"],k)
json.dump(d,open(out,"w"),indent=1,ensure_ascii=False)
print(len(d["accept"]),len(d["reject"]),len(answered),len(d["probes"]))
