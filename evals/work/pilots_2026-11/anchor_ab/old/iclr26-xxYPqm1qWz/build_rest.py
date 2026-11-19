import json, re, os
D = os.path.dirname(os.path.abspath(__file__))
paper = open(os.path.join(D, "reviewer_copy.txt")).read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("-\n", "-")).strip()
P = norm(paper)
quotes = ["eliminating the need for manual annotation", "millisecond-precision temporal localization",
 "extracts structured parameters like click coordinates and typed text with high fidelity",
 "creating such datasets through manual annotation is extraordinarily expensive",
 "Because ground-truth object boxes are unavailable, we evaluate only on unseen web tutorials",
 "any temporal overlap", "teaches the model to decompose complex tasks into subgoals",
 "For the 50-step budget, we perform a single run", "license/PII checks",
 "augmented with a small number of GUI grounding pairs", "then apply identical Stage-2 SFT to each variant",
 "typically lacks precise temporal boundaries or action parameters",
 "Our dense detector is trained on 512,000 screen-capture clips", "We visualize the data sample in Figure",
 "lilybloom123.", "This consistent improvement", "solid recall (0.71)", "inevitably contain residual noise",
 "approximately 840 hours of video per GPU-day", "downsample videos to 4 fps", "temporal patch size of 2 frames",
 "strong finetuning basis", "true test-time scaling", "we conduct three independent runs per model and report the average Task SR",
 "screened by cursor gating, license/PII checks, and downstream detectors", "0%, 50%, and 100% of the video tokens",
 "clear relationship between pretraining data size"]
missing = [q for q in quotes if norm(q) not in P]
print("missing quotes:", missing)
nums = [
 ("OSWorld-Verified base model task SR","4.5",False),("OSWorld-Verified SFT-only (stage2 only)","9.3",False),
 ("OSWorld-Verified stage1+stage2, 20 steps","14.13",False),("OSWorld-Verified stage1+stage2, 50 steps","15.78",False),
 ("Relative improvement claimed","70%",False),("AgentNetBench base / SFT-only / full step SR","38.5 / 64.1 / 69.3",False),
 ("Stage2-only 20-step runs","9.42, 9.13, 9.42",False),("Stage1+2 20-step runs","14.68, 13.57, 14.13",False),
 ("Stage2-only 50-step","9.27",False),("Mean of stage2-only 20-step runs","9.32",True),
 ("20-step run spread for stage1+2","1.11 pt",True),("Gain at 50 steps over the 20-step mean, in tasks of 361","+1.65 pt ~ 6 tasks",True),
 ("Gain at 50 steps over the best 20-step run","+1.10 pt",True),("Stage1+2 vs SFT-only 20-step difference in tasks","~17 tasks (4.8 pt)",True),
 ("15.78/9.27 ratio","1.70",True),("Implied OSWorld-Verified denominator","361",True),
 ("Table 4 bucket denominators sum","359",True),("Stage2-only 50-step solved / SR recomputed","33 = 9.14%",True),
 ("Table 1 total predictions printed","17,298",False),("Table 1 predictions column sum","16,298",True),
 ("Table 1 total P/R/F1","0.88 / 0.70 / 0.78",False),("Text recall","0.71",False),("Press recall","0.08",False),
 ("Table 2 overall accuracy","0.658",False),("Table 2 recomputed overall","330/500 = 0.660",True),
 ("Drag accuracy, 22 samples","0.366 (8/22 = 0.364)",True),("Press / drag accuracy","0.362 / 0.366",False),
 ("Table 6 sum","53,375 vs 55,603",True),("Table 8 printed total","1,547,092",False),("Table 8 sum","1,560,464",True),
 ("Mouse move / drag shares recomputed","0.5% / 0.4% (printed 0.1%)",True),("Table 3 moveTo and dragTo counts","32,840",False),
 ("Videos processed / steps","39,000 / 1.52 million",False),("Average trajectory length","39.25",False),("AgentNet avg steps","18.6",False),
 ("Downloaded videos","55,603",False),("Hours retained by ScreenFilter","7,377 of 10,000",False),
 ("Stage-1 tokens","26B",False),("Grounding tokens","~1B",False),("Stage-2 tokens","8B",False),
 ("Stage-1 GPU-hours (32 H100 x ~60 h)","~1,920 H100-h",True),("Held-out detector test set","23 hours, 20,282 events",False),
 ("Parameterization samples","500",False),("In-the-wild detector videos / recovery","10 / ~70%",False),
 ("Terminate step SR SFT-only vs full","0.588 -> 0.237",False),("ScreenFilter throughput","~840 h per GPU-day",False),
 ("AgentNetBench gain","5.2 pt",False),("AgentNetBench action types improved","8 of 9 comparable",True),
 ("50% -> 100% step OSWorld / AgentNetBench","+2.4 / +1.2",True),("Scaling numbers","9.3/13.3/15.7; 64.1/68.1/69.3",False),
 ("Detector sampling","4 fps, 2-frame temporal patch (0.5 s)",True)]
ev = {"locations": ["Abstract","Section 1","Section 2.1","Section 2.1.2","Section 2.1.3","Section 2.2","Section 2.2.1","Section 2.2.2","Section 2.2.3",
  "Section 2.3","Section 2.3.1","Section 2.3.2","Section 3","Section 3.1","Section 3.1.1","Section 3.1.2","Section 3.2","Section 3.2.1","Section 3.2.2",
  "Section 4","Section 4.1","Section 4.2","Section 5","Section 6","Appendix A","Appendix B","Appendix C","Appendix D","Appendix E","Appendix F","Appendix G","Appendix H",
  "Table 1","Table 2","Table 3","Table 4","Table 5","Table 6","Table 7","Table 8","Table 9","Table 10",
  "Figure 1","Figure 2","Figure 4","Figure 5","Figure 6","Figure 8","Figure 9","Figure 10","Figure 11","Figure 12"],
  "quotes": quotes,
  "numbers": [{"claim":c,"value":v,"derived":d} for c,v,d in nums],
  "references": []}
json.dump(ev, open(os.path.join(D,"evidence.json"),"w"), indent=1, ensure_ascii=False)
L = json.load(open(os.path.join(D,"ledger.json")))
agg = json.load(open(os.path.join(D,"aggregate.json")))
ratio = {"technical_rigor":0.2264,"clarity":0.1038,"novelty":0.1557,"significance":0.1557,"experimental_validation":0.1887,"reproducibility":0.0943,"ethics":0.0755}
ov=[t["overall"] for t in L["types"]]
summ = {"id":"iclr26-xxYPqm1qWz","mode":"full (ledger)","paper_type":"empirical","final_overall":agg["ledger"]["suggested_overall"],
 "venue_recommendation":agg["venue_views"][0]["label"],
 "task":["Computer-use / GUI agents (not listed; adapted from 'Vision–language models, multimodal LLMs')","Video understanding, tracking","Reinforcement learning (imitation from observation)"],
 "neighboring_fields":["VLM/MLLM pretraining and data curation","temporal action localization / video grounding","imitation learning from observation / inverse dynamics (robotics, VPT-style)","LLM/VLM agent evaluation science","web and GUI trajectory synthesis","responsible web-scale data collection and privacy"],
 "aspect_ratio":ratio,"ledger_rating":agg["ledger"]["venue_rating"],"ledger_pool_position":agg["ledger"]["venue_pool_position"],
 "official_rating":sum(ov)/len(ov),"n_types":len(L["types"]),"n_accept":len(L["accept"]),"n_reject":len(L["reject"]),
 "n_answered":len(L["answered"]),"n_probes":len(L["probes"]),
 "top_concerns":["R1: SFT-only baseline lacks Stage-1 compute and OSWorld-G grounding pairs; no matched control (Sec. 2.3; Fig. 6)",
  "R8: no ablation of monologue, ScreenFilter, IDM label quality or action labels vs raw frames (Sec. 4)",
  "R15: low absolute OSWorld-Verified performance (15.8%), single 7B base model, transfer to stronger recipes untested",
  "R2: no comparison with published agents or alternative data sources (Fig. 5; Table 4)",
  "R3: action parameters validated only by lenient manual plausibility (0.658), not against exact held-out logs (Table 2)"],
 "recognized":True,"injection_found":None,
 "notes":"Recognized the title from prior knowledge, outcome not known or used. The rule that Overall 4 needs pool >= 65 and the 55-69 'borderline' band leave little room for a borderline pool position with Overall 3 vs 4; T5's update after P11 crossed that line. The reject 'Worst case' column and 'question' cap interact oddly for R7 (worst case major, but capped at minor while unsettled). The template asks for the aggregation Markdown output, but the script's Markdown output also prints panel-mode EIC sections that do not apply in ledger mode; I excerpted the ledger-mode part. Clarity and reproducibility (10%, 9%) have no type and were renormalized away without a warning. The task row for computer-use agents is not in task_neighbors.md."}
json.dump(summ, open(os.path.join(D,"summary.json"),"w"), indent=1, ensure_ascii=False)
print(summ["final_overall"], summ["venue_recommendation"], summ["official_rating"])
