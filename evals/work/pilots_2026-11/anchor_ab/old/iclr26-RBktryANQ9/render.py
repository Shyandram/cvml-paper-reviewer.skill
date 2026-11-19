import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
import build as B
L = json.load(open(os.path.join(D, "ledger.json")))
AG = json.load(open(os.path.join(D, "aggregate.json")))
AGMD = open(os.path.join(D, "_aggregate.md")).read()
cons = json.load(open(os.path.join(D, "_consensus.json")))
esc = lambda s: str(s).replace("|", "\\|")
o = []
w = o.append

w("# Peer Review: Dataset Distillers Are Good Label Denoisers In the Wild\n")
w("| | |\n|---|---|")
w("| Date | 2026-11-19 |")
w("| Mode | full (ledger review) |")
w("| Paper type | analysis (an empirical study of existing dataset-distillation methods under label noise; no new method is proposed) |")
w("| Field, sub-area | machine learning / computer vision; learning with noisy labels, dataset distillation |")
w("| Task | Image classification, representation learning (adapted: learning with noisy labels); Efficient models, compression (adapted: dataset distillation / condensation) |")
w("| Neighboring fields | dataset distillation / condensation; learning theory of memorization and early learning (from row: learning theory); data-centric ML, coreset selection and data pruning (generated beyond the file); privacy-preserving ML (generated, from the robustness/privacy row); ML evaluation methodology (generated); semi-supervised learning as used by noisy-label methods (generated) |")
w("| Target venue | ICLR 2026 (stated by the user) |")
w("| Aspect ratio | `aggregate_scores.py ratio --paper-type analysis --venue iclr`: technical_rigor 28%, novelty 20%, significance 20%, experimental_validation 14%, clarity 10%, reproducibility 5%, ethics 4% |")
w("| Literature check | off: no network access in this run; novelty reasons that rest on memory are marked [verify] |")
w("\nOne context: the reviewer types share one model and one reading, so their judgments are not independent.\n")
w("Input note: the manuscript was available only as extracted text. Figures 1-5 (which carry every quantitative result) could not be seen; figure-dependent claims are judged from captions and text only, and this is said where it matters.\n")
w("---\n\n## 1. Paper memory\n")
w("**Claims.**")
w("- C1: Dataset distillation is \"a novel approach that leverages dataset distillation for noise removal\" that \"avoids the feedback loop common in existing techniques and enhances training efficiency, while also providing strong privacy protection through offline processing\" (Abstract; Sec. 1 Contributions; Sec. 5).")
w("- C2: Under symmetric noise, existing distillers (DATM, DANCE, RCIG) are effective denoisers: once noise passes a threshold they \"consistently demonstrate significant performance gains\" over training on the full noisy set (Sec. 4 Experiment-I, Observation-I, Insight-I; Figure 2).")
w("- C3: Structured (asymmetric) noise is absorbed into the distilled samples and hurts training. Tail-class clean samples may be lossily compressed (Abstract; Sec. 4 Experiment-II, Observation-II, Insight-II; Figure 4).")
w("- C4: On real-world natural noise (CIFAR-10N/100N), distillation \"remain[s] largely effective even in the presence of an unknown fixed noise rate\", especially at high noise (Sec. 4 Experiment-III, Observation-III, Insight-III; Figure 5). The title frames this as \"In the Wild\".")
w("- C5: Two corollaries: an upper bound on IPC to preserve clean information (Corollary-I, Eq. 10) and a probabilistic noise-rate bound from distillation (Corollary-II, Eq. 11).")
w("\n**Setup facts.**")
w("- Datasets: CIFAR-10/100, Tiny-ImageNet (symmetric noise); CIFAR-10/100 (asymmetric); CIFAR-10N (Aggre 9.03%, Random k ~18%, Worst 40.21%), CIFAR-100N fine (40.20%) (Sec. 4 Implementations, Experiment-III).")
w("- Noise construction: symmetric per Eq. 1. Asymmetric: CIFAR-10 TRUCK->AUTOMOBILE, BIRD->AIRPLANE, DEER->HORSE, CAT<->DOG; CIFAR-100 next class within its superclass (Sec. 4 Implementations). Noise rates: symmetric 0.2/0.4/0.6/0.8 (Sec. 4 Exp-I); asymmetric 0.2/0.4 at least (Sec. 4 Exp-II).")
w("- Distillers: DATM, in fact \"this accelerated version\" based on [9] (Sec. 3.2); DANCE; RCIG (Sec. 3.2).")
w("- Architecture: \"a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet\" (Sec. 4 Implementations).")
w("- Evaluation: each distiller's original protocol; augmentation for RCIG; \"Final test accuracies are reported throughout the distillation process\" (Sec. 4). Captions say \"validation performance\" (Figs. 2, 4).")
w("- Baseline: CE training on the full noisy set (dashed lines, Figs. 2/4/5); its protocol is not stated.")
w("- IPC grid, distillation iterations, expert epochs, learning rates: not stated.")
w("- Seeds, runs, variance: not stated.")
w("- Compute: not stated.")
w("- Code: not stated.")
w("- Train/validation/test split and selection split: not stated (test set used for reporting).")
w("\n**Headline numbers.**")
w("- IPC=1 beats the full-noisy-data baseline at tau = 0.6 and 0.8 on CIFAR-10 (Sec. 4 Exp-I; Figure 2(a)).")
w("- Fewer than 50 IPC beat the baseline at tau = 0.2 (Figure 2(a)).")
w("- On CIFAR-100N (40.20% noise), all three distillers surpass the baseline with fewer than 10 IPC (Sec. 4 Exp-III; Figure 5).")
w("- Under asymmetric noise, only DATM matches the baseline, at tau in {0.2, 0.4} with large IPC (Sec. 4 Exp-II; Figure 4).")
w("- No accuracy value is printed anywhere in the paper.")
w("\n**Appendix and supplement.** None in the provided text.")
w("\n**Could not be read.**")
w("- Figures 1-5: all curves and the distilled-image grid.")
w("- Eqs. 2, 5, 8 and 9 are partly garbled by extraction. Their structure is readable, so they were not used for any error.")
w("- No supplement was provided.")
w("\n---\n\n## 2. Ledger\n\n### Accept reasons\n")
w("| ID | Aspect | Reason | Evidence | Strength | Depends on |\n|---|---|---|---|---|---|")
for a in L["accept"]:
    w(f"| {a['id']} | {a['aspect']} | {esc(a['reason'])} | {esc(a['location'])} | {a['strength']} | {esc(a['depends_on'])} |")
w("\n### Reject reasons\n")
w("| ID | Aspect | Reason | Evidence | Kind | Worst case | Fix |\n|---|---|---|---|---|---|---|")
for r in L["reject"]:
    w(f"| {r['id']} | {r['aspect']} | {esc(r['reason'])} | {esc(r['location'])} | {r['kind']} | {r['worst_case']} | {esc(r['fix'])} |")
w("\n### Answered\n")
for x in L["answered"]:
    w(f"- {x['reason']}: answered at {x['answered_at']}.")
w("\n### Aspect coverage\n")
cov = {
 "novelty": "A1; R12, R15",
 "technical soundness / theory": "A5; R1, R2, R13, R14",
 "claim accuracy (E5)": "R5, R6, R7, R8",
 "experimental validation": "A2, A3, A6, A9; R3, R4, R9, R10, R17",
 "evaluation protocol / leakage": "R11 (question)",
 "significance": "A4, A7, A10, A12; R15, R16",
 "clarity": "A8; R18, R19",
 "reproducibility": "A11; R20",
 "ethics / privacy / limitations": "R5, R21",
 "statistical reporting": "R10",
 "efficiency": "A12; R6",
 "dataset licence / human subjects": "considered, no reason (public benchmarks only; CIFAR-N annotations are public)",
 "figure integrity (E9)": "considered, not checkable (no page images)",
}
for k, v in cov.items(): w(f"- {k}: {v}")
w("\nOmission sweep (error_audit §4):")
w("- Splits and selection split: not stated after search (R11).")
w("- Seeds and variance: not stated (R10).")
w("- Baseline settings: not stated (R4).")
w("- Hyperparameters: not stated (R20).")
w("- Compute: not stated (R6, R20).")
w("- Licence: public data, no issue.")
w("- Failure cases and limitations: asymmetric failure present (A5); no limitations section (R21).")
w("- Code: not stated (R20).")
w("\n### Pairs\n")
w("- A4 ↔ R3, R4: whether the high-noise gain is meaningful against a fair or strong baseline (C2).")
w("- A1 ↔ R12, R15: novelty of the distillation-as-denoiser perspective (C1).")
w("- A12 ↔ R5, R6: the privacy and efficiency benefits (C1).")
w("- A10 ↔ R1, R2: the corollaries' value (C5).")
w("- A6 ↔ R8: 'in the wild' (C4).")
w("- A3 ↔ R9, R10: whether the sweep can be checked (C2).")
w("- A5 ↔ R13: the asymmetric-noise finding vs its asserted mechanism (C3).")
w("\n---\n\n## 3. Reorganized ledger and probes\n\n### By claim\n")
w("No duplicates were found that needed merging. The privacy part of R21 overlaps R5 but is kept separate: R21 is about the missing limitations discussion.\n")
byc = {}
for x in L["accept"] + L["reject"]: byc.setdefault(x["claim"], []).append(x)
swing_high = {"R3","R1","R4","R5","R6","R7","R8","R9","R11","R12","R13","R14","R15","A4","A1"}
names = {"C1":"distillation as a new noisy-label approach that avoids the vicious cycle, improves efficiency, protects privacy","C2":"symmetric-noise denoising","C3":"asymmetric noise absorbed; tail classes compressed","C4":"real-world natural noise ('in the wild')","C5":"Corollaries I-II","general":"General"}
for c in ["C1","C2","C3","C4","C5","general"]:
    w(f"**{c}: {names[c]}**")
    w("- " + ", ".join(f"{x['id']} ({x['status']}{', high swing' if x['id'] in swing_high else ''})" for x in byc.get(c, [])))
    w("")
w("Swing ranking (highest first): R3, R15, R1, R4/A4, R5, R6, R7, R8, R9, R13, R14, R12, R11, A1. Every reason with worst case fatal (R3) was probed.\n")
w("### Probes\n")
w("| ID | Item | Question | Method | Result | Change |\n|---|---|---|---|---|---|")
for p in L["probes"]:
    if p["after_reviews"]: continue
    w(f"| {p['id']} | {', '.join(p['items'])} | {esc(p['question'])} | {esc(p['method'])} | {p['result']}: {esc(p['location'])}. {esc(p['finding'])} | {esc(p['change'])} |")
w("\nP1 computation: Eq. 11 bound = 1 - C·IPC/|S̃|. CIFAR-10, C=10, IPC=50, |S̃|=50,000 gives 0.99. IPC=1 gives 0.9998. CIFAR-100N, C=100, IPC=10 gives 0.98. Eq. 10, |S̃|(1-τ)/C at τ=0.2, gives 4,000. Training-set sizes are the standard ones; the paper does not state them.\n")
w("---\n\n## 4. Reviewer roster\n")
w("Aspects with ≥ 12% of the ratio are technical_rigor (28%), novelty (20%), significance (20%) and experimental_validation (14%); each has at least one type. Clarity (10%), reproducibility (5%) and ethics (4%) fall below 12%. Their reasons sit in T2's, T4's and T6's 'Weighs most', and the script renormalizes their shares away.\n")
w("| Type | Aspect | Field | Expertise | Values | Distrusts | Weighs most | Likelihood |\n|---|---|---|---|---|---|---|---|")
for t in B.T:
    w(f"| {t['id']} {t['name']} | {t['aspect']} | {t['field']} | {t['expertise']} | {t['values']} | {t['distrusts']} | {', '.join(t['weighs'])} | {t['likelihood']} |")
w("\nMix: T1 is the task specialist. T2-T6 are outside types drawn from the neighbors identified in Step 0. Every ledger item appears in at least one type's 'Weighs most'.\n")
w("---\n\n## 5. Reviews\n")
for t in B.T:
    w(f"### {t['id']}: {t['name']} ({t['aspect']}; {t['field']})\n")
    w("**Reading of the ledger.**")
    for line in t["reading"]: w(f"- {line}")
    w(f"\n**Opinion.** {t['opinion']}\n")
    if t["aspect"] in ("novelty", "significance"):
        pass
    w(f"Decisive: {t['decisive']}\n")
    s = t["scores"]
    w(f"**Scores.** Pool position {t['pool']} (better than about {t['pool']}% of ICLR 2026 submissions; basis: {t['decisive']}). Technical Rigor {s['technical_rigor']}, Clarity {s['clarity']}, Novelty {s['novelty']}, Significance {s['significance']}, Experimental Validation {s['experimental_validation']}, Reproducibility {s['reproducibility']}, Ethics {s['ethics']}. Overall {t['overall']} ({'Borderline Reject' if t['overall']==3 else 'Reject'}). Confidence {t['confidence']}.\n")
w("Contribution check. T2 and T5 answer the four questions inside their opinions. T6, the other significance type, answers them here:")
w("1. What does a reader learn? A plausible regularity, not why it holds (R13, R15).")
w("2. Does the setting support the framing? No: 'in the wild' and 'privacy' are not operationalized (R8, R5).")
w("3. Is the delta conceptual or a refinement? A refinement: existing distillers applied unmodified (R15).")
w("4. Would the conclusions transfer? Doubtful beyond CIFAR-scale ConvNets (R8, R17).")
w("\nT1, T3 and T4 do not score novelty or significance as their primary aspect.\n")
w("### Settling factual splits\n")
w("| Probe | Split | Fact checked | Result | Grades updated |\n|---|---|---|---|---|")
for p in L["probes"]:
    if p["after_reviews"]:
        w(f"| {p['id']} | T1 (minor) vs T4 (major) on R10 | {esc(p['question'])} | {p['result']}: {esc(p['finding'])} | {esc(p['change'])} |")
w("\nValue splits that stay:")
w("- R3: T1 fatal, T5 major. Both agree on the fact (P2); they differ on how central a noisy-label comparison is to an analysis paper.")
w("- R12: T2 minor, T5 major. Whether coreset selection under noise covers synthetic distillation is a matter of field perspective.")
w("- R6: T4 and T5 major, T6 minor.")
w("- R8: T1 major, T6 minor.")
w("\n---\n\n## 6. Scores and decision\n")
lw = {x["role"].split(" ")[0]: x["weight"] for x in AG["ledger"]["type_weights"]}
w("| Type | Aspect | Weight | Pool position | Overall | Confidence |\n|---|---|---|---|---|---|")
for t in B.T:
    w(f"| {t['id']} | {t['aspect']} | {lw[t['id']]:.3f} | {t['pool']} | {t['overall']} | {t['confidence']} |")
Lg = AG["ledger"]
ov = [t["overall"] for t in B.T]
vv = AG["venue_views"][0]
w(f"\n- **Aspect-weighted rating:** {Lg['venue_rating']:.2f} → **final rating {Lg['suggested_overall']} (Reject)**. ICLR's own label: **{vv['label']}**. ICLR sub-scores: Soundness {vv['subscores']['Soundness']}, Presentation {vv['subscores']['Presentation']}, Contribution {vv['subscores']['Contribution']}. Scale status: secondary (recent analyses), so check it against the current form.")
w(f"- Weighted pool position {Lg['venue_pool_position']}; plain mean {Lg['plain_rating']}; spread {max(ov)-min(ov)} (2 to 3).")
w("- Uncovered aspects and warnings: none. Clarity, reproducibility and ethics fall below 12% and have no type; their shares were renormalized away by design.")
w("- This is a simulation of how a careful set of reviewers would likely see this draft, not a prediction of the outcome.\n")
w("<details><summary>Aggregation output</summary>\n")
w(AGMD)
w("\n</details>\n")
w("---\n\n## 7. Consensus map, strengths, concerns, roadmap\n\n### Consensus map\n")
w("| Item | Types naming it | Grades (or held / discounted) |\n|---|---|---|")
order = [a["id"] for a in L["accept"]] + [r["id"] for r in L["reject"]]
for k in order:
    v = cons.get(k, [])
    w(f"| {k} | {len(v)} of 6 | {', '.join(v) if v else 'not named (neutral)'} |")
w("\n### Key strengths\n")
w("- A2: the study covers the three main distillation families. Held by T2 and T4 (2 of 6).")
w("- A1: a new perspective, distillation as an implicit label denoiser. Held by T2, discounted by T1.")
w("- A4: under heavy symmetric noise, IPC=1 beats the full noisy-data baseline. Held by T5, discounted by T1 because of R4.")
w("- A5 and A6: an honest negative result under asymmetric noise, and a human-noise test on CIFAR-N. Held by T3 and T1 respectively.")
w("\nNo accept reason was held by a majority of types.\n")
w("### Top concerns (at most five)\n")
w("1. R15: no method; existing distillers are benchmarked on noisy CIFAR, and the insights are close to expected (Sec. 2.2; Sec. 1 Insights I-III). Graded major by 3 of 6 types (T2, T5, T6). Fix: develop a noise-aware distiller for structured noise, or a mechanistic analysis; high cost.")
w("2. R3: no noisy-label baselines. The only reference is CE on the full noisy set (Figure 2/4/5 captions; Sec. 5). Graded fatal by T1 and major by T5. Fix: add CE+early stopping, Co-teaching, GCE and DivideMix on the same backbone; a few GPU-days.")
w("3. R5: the privacy claim ('strong privacy protection', 'ensures privacy protection') is untested (Abstract; Sec. 5; P4). Graded major by T4 and T6. Fix: remove it or run membership inference; low to moderate.")
w("4. R13: the mechanism is asserted, not tested, and the experts are trained on noisy labels (Sec. 4 Insight-I; Eqs. 4, 6-7; P10). Graded major by T2 and T3. Fix: expert-epoch ablation and an analysis of the distilled images' label content; moderate.")
w("5. R9: no tables; every result is a curve in Figures 2, 4 and 5 (P7). Graded major by T1 and T4. Fix: tables of accuracy per method, dataset, tau and IPC; low.")
w("\nAlso graded major by two types: R6, efficiency unmeasured (T4, T5); R10, no seeds or variance (T4, and T1 after P12).")
w("\n### Revision Roadmap\n")
w("| Priority | Ledger ID | Fix | Cost |\n|---|---|---|---|")
w("| 1 | R3 | Compare with standard noisy-label methods (CE+early stopping, Co-teaching, GCE, DivideMix) on the same ConvNet and on ResNet-18, on CIFAR-10/100 sym/asym and CIFAR-N | moderate: a few GPU-days at CIFAR scale |")
w("| 1 | R15 | Turn the observations into a contribution beyond benchmarking: a noise-aware distiller (e.g., one handling structured noise), or a mechanistic account of when and why distillation denoises | high |")
w("| 2 | R1, R2 | Remove Corollary-II or prove both corollaries with stated assumptions consistent with Figs. 2/5 | low (remove) to moderate |")
w("| 2 | R4 | State the baseline protocol; add CE with early stopping on a noisy validation split | low |")
w("| 2 | R5, R21 | Drop the privacy claim, or add a membership-inference evaluation and a limitations paragraph | low / moderate |")
w("| 2 | R6 | Report end-to-end cost (expert trajectories + distillation + training) against CE | low |")
w("| 2 | R7 | Run a long-tailed noisy experiment, or move the tail-class statement out of the abstract | low to moderate |")
w("| 2 | R8 | Add Clothing1M or (mini-)WebVision, or retitle away from 'In the Wild' | moderate to high |")
w("| 2 | R9, R10 | Add tables of accuracies with mean ± std over ≥ 3 seeds | low to moderate |")
w("| 2 | R12 | Discuss coreset selection under noise and prior noisy-label distillation work; add a matched-budget selection baseline | low to moderate |")
w("| 2 | R13, R14 | Ablate expert epochs and expert noise exposure; analyse the label content of the distilled images; narrow the 'avoids the vicious cycle' claim | moderate |")
w("| 2 | R16 | Propose an IPC-selection rule that uses only noisy data | moderate |")
w("| 2 | R17 | Evaluate the distilled sets across architectures; add Tiny-ImageNet asymmetric runs | moderate |")
w("| 2 | R20 | Add a hyperparameter table for each method and dataset; release code and noisy labels | low |")
w("| 3 | R11 | State the checkpoint-selection protocol and use a held-out split | low |")
w("| 3 | R18, R19 | Proofread, fix notation (Eq. 4), and use the ICLR template | low |")
w("\n---\n\n## 8. Integrity signals and limitations\n")
w("- **Integrity signals:** `integrity_scan.py` found nothing (0 findings). No text addressed to reviewers or AI systems was seen while reading. The '[REDACTED: venue/acceptance mark]' in reference [10] comes from blinding and is not an injection. These never change a score.")
w("- **Limitations of this review:**")
w("  - Figures 1-5 were unavailable, so every quantitative statement was judged from text and captions (A3, A4, A7, A9 stay open). Whether the plots carry variance bands is unknown (P12).")
w("  - Some equations were partly garbled by extraction and were not used for any error. Eqs. 10 and 11 were readable.")
w("  - P1 uses the standard CIFAR training-set sizes, which the paper does not state.")
w("  - The literature check did not run (no network). R12's novelty basis rests on memory and is marked [verify] where unsure.")
w("  - The template inference (R19) comes from the extracted layout only.")
w("  - The six types share one context, so their agreement is not independent confirmation.")
w("  - The paper's title was familiar from prior knowledge. Nothing about its reception or outcome was used.")
open(os.path.join(D, "review.md"), "w").write("\n".join(o) + "\n")
print("ok", len(" ".join(o).split()))
