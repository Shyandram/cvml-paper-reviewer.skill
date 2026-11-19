#!/usr/bin/env python3
"""Builds ledger.json and scores.json for iclr26-9R2iUHhVfr (written by the reviewing agent)."""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

A = [
 ("A1","significance","Timely need: SWE-Bench Verified is near saturation (>70% reported), so a harder issue-resolution benchmark with large headroom (best 23.3% Pass@1) restores signal for agent research.","§1 (\"over 70% pass rate on SWE-Bench-Verified\"); Table 1 (GPT-5 23.3)","strong","C4",None),
 ("A2","novelty","Contamination-mitigation design that is new for SWE benchmarks: copyleft (GPL) repositories for the public/held-out sets plus purchased private startup codebases, with three access tiers (public, held-out, commercial).","§1 contribution 1; §3.1; §3.3","moderate","C1",None),
 ("A3","significance","Tasks are substantially larger than SWE-Bench Verified: trivial edits excluded, reference patches average 107.4 LOC across 4.1 files, every task at least 10 changed lines.","§1 (\"107.4 lines of code across 4.1 files\"); Figure 3 caption","strong","C2",None),
 ("A4","experimental_validation","Scale and spread: 1,865 problems from 41 repositories (11+12+18), four languages, per-repository cap of 100 instances to limit single-repo overfitting.","Abstract; §1; §3.3 (731+276+858=1,865)","moderate","C2",None),
 ("A5","technical_rigor","Human augmentation adds a problem statement, test-grounded requirements and an explicit interface, removing a known false-negative mode (wrong class/function names) and under-specification of commit-derived tasks.","§3.2 Interface; §4.2; App. A.1-A.3; Table 4","moderate","C3",None),
 ("A6","technical_rigor","Test reliability controls: tests run 3 times and flaky ones dropped; annotators filter fail2pass tests that are too broad or irrelevant; problems dropped when no valid test remains.","§3.2 Tests (\"we run each set of tests 3 times\"); §4.3","moderate","C3",None),
 ("A7","reproducibility","Public set (731 instances) released; containerized per-language environments; one scaffold (SWE-Agent), one prompt, 200-turn cap, model versions dated; judge prompt given in full.","§3.3; §3.2 Environments; §5 Evaluation settings; App. B.1","moderate","general",None),
 ("A8","experimental_validation","Evaluates a broad model set under one scaffold: frontier closed models, open-weight models and a SWE-trajectory fine-tuned model (SWE-Smith-32B), on both public and commercial sets.","Table 1; Table 2; §5","moderate","C4",None),
 ("A9","significance","Diagnostic analyses beyond a single number: per-language and per-repository resolve rates and an LLM-judge failure taxonomy contrasting frontier (semantic/wrong solution) and small models (syntax, tool use, context).","§6.1; Figure 4; §6.2; Table 3","weak","C5",None),
 ("A10","significance","A private held-out set from separate repositories is kept to detect future overfitting to the public set.","§3.3 Held-Out; §1","moderate","C1",None),
 ("A11","ethics","Limitations are stated honestly: language coverage, issue-resolution scope only, dependence on tests, and over-prescriptive augmentation.","§7.1","moderate","general",None),
 ("A12","clarity","Task format is concrete and easy to follow, with a full worked example of problem statement, requirements and interface, and a before/after rewrite.","§3.2; App. A.1-A.3; Table 4","moderate","general",None),
 ("A13","significance","The commercial set gives enterprise codebases no public benchmark has, and the paper reports results on it (best 17.8%).","§3.3 Commercial; Table 2","moderate","C2",None),
]

R = [
 ("R1","experimental_validation","Table 3 counts are inconsistent with the evaluated set: per-model failure counts exceed both N=731 and the number of unresolved instances, so the unit of the failure analysis is unclear and its percentages cannot be interpreted.","Table 3; §6.2 \"we programmatically filter to only unresolved instances\". Recomputed: Opus 681+239=920, Gemini 491+424=915, GPT-4o 569+220=789, Qwen 386+406=792 > 731; expected unresolved for Opus 731x(1-0.227)=565.","error","major","State the unit (runs x instances?), recompute Table 3 on unresolved public instances only; hours.","C5"),
 ("R2","clarity","Results text contradicts Table 1: Sonnet 4 given as 16.3% (Table 1: 17.6) and GPT-4o as 3.9% (Table 1: 4.9).","§5 Results \"also achieves a 16.3% resolve rate\"; \"at 3.4% and 3.9% respectively\" vs Table 1. Cross-referenced.","error","minor","Correct the text; minutes.","C4"),
 ("R3","technical_rigor","The commercial set cannot satisfy the stated per-repository range: 276 problems over 18 repositories is about 15 per repository, against 'between 50 and 100 instances' per repository and 'a similar number of problems per repo'.","§1 \"Each repository contributes between 50 and 100 instances, with a strict cap of 100 instances\"; §3.3 (276 problems), Abstract (18 repositories). Recomputed 276/18=15.3.","error","major","Report per-repository counts for every subset and restrict the claim to the public/held-out sets; hours.","C2"),
 ("R4","technical_rigor","The headline 'contamination-resistant' claim is argued, not measured: no memorization probe, no public vs held-out comparison (the held-out set exists), and the GPL 'legal barrier' argument is asserted without evidence that copyleft code is absent from training corpora.","§3.1 \"the nature of these licenses creates legal barriers to their inclusion in commercial training corpora\"; Abstract \"contamination-resistant testbed\"; no contamination experiment in §5-§6 (text search).","gap","major","Report public vs held-out resolve rates for 2-3 models, add a memorization/completion probe on public repos (e.g., in the style of Golchin & Surdeanu 2024); about one GPU-week plus API cost.","C1"),
 ("R5","ethics","Evaluating closed API models on the private commercial and held-out sets sends that code to model providers; the paper does not discuss how this affects long-term contamination resistance or the data-use terms agreed with the startups.","§5 (closed models evaluated on commercial set, Table 2); §3.3; no discussion found.","gap","minor","Describe API data-retention settings and the agreements; a paragraph.","C1"),
 ("R6","experimental_validation","The 'substantially more challenging' comparison is not like-for-like: the >70% figure on SWE-Bench Verified comes from other reports and tuned scaffolds, while SWE-Bench Pro numbers use SWE-Agent with a basic prompt and 200 turns; the same harness is never run on Verified.","§1 \"substantially lower than the >70% Pass@1 reported on SWE-Bench Verified [15]\"; Figure 2 caption; §5. Text search: no Verified run.","gap","major","Run the same SWE-Agent configuration on SWE-Bench Verified for the Table 1 models; one to two days of API compute.","C4"),
 ("R7","experimental_validation","Single run, no variance or confidence intervals; with N=731 the 95% interval is about ±3.1 pp, so GPT-5 vs Opus 4.1 (23.3 vs 22.7) and the commercial ranking (17.8 vs 14.9, ±4.5 pp at N=276) are not separable, yet the abstract states a ranking.","Table 1; Table 2; Abstract \"GPT-5 achieving the highest score to date at 23.3%\". Binomial SE recomputed.","gap","major","Report 3 runs or bootstrap CIs; soften ranking language; one to three API-days.","C4"),
 ("R8","experimental_validation","Harness parity and settings are under-specified: open-weight models use 'syntax parsing' for tools while closed models use native tool calls; GPT-5 fails to submit on 63.1% of failures, 97.6% of them tool-use, which suggests a harness incompatibility; temperature, reasoning effort, context limits and cost caps are not stated.","§5 \"for open-weight models, we use syntax parsing to enable tool-use\"; Table 3 GPT-5 row; §6.2 \"GPT-5 indicates potential differences in effective-tool-use\".","gap","major","Report all decoding/agent settings; diagnose GPT-5 non-submissions; rerun with a fixed tool interface; days.","C4"),
 ("R9","significance","The 'long-horizon', 'hours to days' framing is not operationalized: no human solve-time is measured, and the evaluated setting supplies requirements and interfaces that name files, functions and expected strings, turning much of the search into specified implementation.","Abstract \"may require hours to days for a professional software engineer to complete\"; §5 Issue Ambiguity; App. A.2-A.3. Text search: no time measurement.","judgment","major","Measure expert solve time on a sample, or retitle/reframe; report task-length statistics (median LOC, files); weeks for a time study.","C2"),
 ("R10","experimental_validation","No ablation of the augmentation: models are never evaluated without requirements and/or interface, so how much of the task the augmentation gives away, and how hard the underlying issues are, is unknown.","§3.1 \"the setting without requirements is potentially interesting\"; §5 Issue Ambiguity (only the fully specified setting).","gap","major","Evaluate 2-3 models with statement-only and statement+requirements; one to two API-days.","C2"),
 ("R11","reproducibility","The human pipeline is undocumented: no annotator count, qualifications, time per task, agreement, QA protocol, or funnel counts (candidate commit pairs to final tasks) for the 'three-stage' process.","§1 \"We design a novel three-stage human-in-the-loop process\"; §4.2-§4.3. Text search: no annotator statistics.","gap","major","Add a datasheet-style section with funnel counts, annotator details and agreement; a few days of writing.","C3"),
 ("R12","technical_rigor","Resolvability is asserted but not validated: no human solves a sample, and no failed model patches are audited for false negatives, although tests are acknowledged as an imperfect verifier.","Abstract \"All tasks are human-verified and augmented with sufficient context to ensure resolvability.\"; §7.1 Dependency on Test Suite.","gap","major","Have engineers solve a random sample from the statement+requirements alone; audit ~100 failed patches; one to two weeks.","C3"),
 ("R13","technical_rigor","Figure 1 states 'difficulty filtering', but the text describes only a size filter; if tasks were filtered by model success, the low resolve rates are partly by construction.","Figure 1 caption \"We design the dataset with contamination resistance, difficulty filtering, and human augmentation/verification.\"; §4.","question","major","State every filter, and whether any model was used to select tasks; minutes.","C2"),
 ("R14","experimental_validation","The failure-mode analysis has weak validity: GPT-5 judges its own trajectories, only the last 20 turns are read, the human agreement behind the 20-turn choice is not reported (the 87% figure is borrowed from [22]), the prompt's 10 categories do not map stated onto Table 3's 9 columns, 'Other' is 63.4% of Sonnet's submitted failures, and the prompt hard-codes 'Final state: Failed (no successful patch generated)' even for submitted patches.","§6.2 \"utilizing GPT-5 as the judge\", \"We determined 20 turns to have the highest correspondence with human validations\"; Table 3; App. B.1.","gap","major","Report human agreement on a labelled sample, use a judge not under evaluation (or several), give the category mapping; days.","C5"),
 ("R15","clarity","Analysis text misreads Table 3: Qwen's tool-use share is 349/792=44.1%, not 42.0%, and it is not the highest (GPT-5: 446/724=61.6%).","§6.2 \"exhibits the highest tool error rate (42.0%)\"; Table 3 Qwen and GPT-5 rows. Recomputed.","error","minor","Correct the sentence; minutes.","C5"),
 ("R16","novelty","The delta over prior SWE benchmarks is a refinement: the commit-pair sourcing, fail2pass/pass2pass tests and human verification follow SWE-bench/SWE-Bench Verified; contamination-resistant and multi-language SWE benchmarks (SWE-bench-Live [25], Multi-SWE-bench [24], SWE-rebench, SWE-Lancer, LiveCodeBench) are not compared, and 'the first to systematically apply such a methodology' is not supported.","§1 \"to the best of our knowledge, this work is the first to systematically apply such a methodology\"; §2.1 (no comparison table); §4.1. Literature check offline: memory, [verify].","judgment","major","Add a comparison table vs prior SWE benchmarks (size, languages, LOC, contamination strategy) and narrow the 'first' claim; a day.","general"),
 ("R17","experimental_validation","The public-commercial gap is attributed to enterprise complexity without controls: the commercial set has no reported statistics (Figure 3 covers the public set only), languages or task sizes may differ, and Table 2 omits two Table 1 models.","§1 \"underscoring the greater complexity of enterprise codebases\"; §5; Table 2 vs Table 1; Figure 3 caption.","gap","major","Report commercial-set statistics and a size/language-matched comparison; a day.","C2"),
 ("R18","reproducibility","The held-out set is undescribed: no statistics or results, so 'mirroring the public set' cannot be checked.","§3.3 \"We hold out a set of 858 problems mirroring the public set but use a separate set of repositories.\"","gap","minor","Report summary statistics and one model's score; hours.","C1"),
 ("R19","significance","Language coverage is narrow (Python, JS, TS, Go), weaker than prior multi-language SWE benchmarks, which limits the 'diverse' claim.","§7.1 Limited Language Coverage; §2.1 Multi-SWE-bench covers seven languages.","judgment","minor","Narrow the diversity wording or add languages; months for new data.","C2"),
 ("R20","reproducibility","Commercial results cannot be reproduced by others by design; environments 'will be released'; agent configuration files are not given.","§3.2 \"All environments will be released as pre-built docker images\"; §3.3 Commercial.","gap","minor","Release images and configs; offer a hosted evaluation for the commercial set.","general"),
 ("R21","clarity","Citation errors: SWE-Bench is cited as [25] (SWE-bench goes live!) in the abstract; 'social media posts [1, 25]' cites two arXiv papers; SWE-Bench Verified is cited as [13] (original SWE-bench); SWE-Smith is evaluated but not cited.","Abstract \"builds upon the best practices of SWE-Bench [25]\"; §1 \"social media posts [1, 25]\"; §1 \"SWE-Bench Verified [13]\"; §5 SWE-Smith; References. Cross-referenced.","error","minor","Fix the references; minutes.","general"),
 ("R22","clarity","Presentation is thin for a main-track paper: short analysis, typos (\"models current perform better\"), inconsistent names (\"DeepSeek Qwen-3 32B\", 'private set' for held-out), Figure 4 caption refers to file/LOC bins it does not describe, and Table 3 columns are not defined.","Figure 4 caption; §5 \"earlier generation models like DeepSeek Qwen-3 32B\"; §5 \"we keep the private set held-out\"; Table 3.","gap","minor","Copy-edit; define columns; a day.","general"),
 ("R23","ethics","Data-governance details are missing: terms under which startup code was purchased and may be evaluated, contributor consent, annotator compensation, GPL compliance for the redistributed public set.","§3.1 \"where we contacted the company and purchased their engineering repos\"; §4.1. Text search: no ethics statement.","gap","minor","Add an ethics/data statement; hours.","general"),
 ("R24","ethics","Anonymization: the text names the organization whose employees founded some source startups, which identifies the authors in a double-blind venue. Flagged for the editor; not a scientific weakness.","§4.1 \"startups founded by Scale employees\"","gap","minor","Remove identifying text; minutes.","general"),
 ("R25","clarity","Only the mean patch size is given; with a 10-line minimum and only 'over 100 tasks' above 100 lines, the distribution is heavy-tailed and the median would say how many tasks are actually large.","§1 \"Every problem involves at least 10 lines of change, and over 100 tasks demand more than 100 lines of modification.\"; \"107.4 lines\"","question","minor","Report median and quartiles of LOC and files per subset; minutes.","C2"),
 ("R26","experimental_validation","Agentless is dismissed as producing 'low evaluation scores' without numbers, so scaffold sensitivity of the benchmark is not shown.","§5 Scaffold \"Agentless has difficulty in multi-file editing, thus, produces low evaluation scores\"","gap","minor","Report the Agentless numbers; hours.","C4"),
]

# added later
R_ADDED = [
 ("R27","technical_rigor","No date-based contamination check: commit dates of public and commercial tasks are not reported against model training cutoffs, so even a simple temporal check of the contamination claim is impossible.","§4.1 (commit-pair sourcing, no dates); §5 \"latest versions as of September 18th, 2025\". Text search: no commit dates.","gap","major","Report commit-date distributions and resolve rate before/after each model's cutoff; hours.","C1","T4"),
 ("R28","clarity","Description of the requirements contradicts the example: §4.2 and A.2 say requirements do not prescribe implementation or leak solutions, yet the A.2 example fixes file paths, a function name and a tuple's contents.","§4.2 \"does not prescribe how the solution should be implemented\"; App. A.2 \"Requirements never include specific code implementation and don’t leak solutions.\" vs A.2 example (`stage_from_google_books`, `STAGED_SOURCES`).","judgment","minor","Describe precisely what requirements may specify; quantify leakage via R10; hours.","C3","P8"),
]

answered = [
 {"reason":"Tasks may be trivial one-to-two-line edits as in SWE-Bench Verified","answered_at":"§1 \"Every problem involves at least 10 lines of change\"; §3.1"},
 {"reason":"Flaky tests could make outcomes noisy","answered_at":"§3.2 Tests (run 3 times, inconsistent tests filtered); §4.3 Environment verification"},
 {"reason":"A few repositories could dominate the public set","answered_at":"§1 cap of 100 per repository; §3.3 731 over 11 repositories = 66.5 average"},
 {"reason":"Correct patches could fail on naming mismatches with the tests","answered_at":"§3.2 Interface; App. A.3"},
 {"reason":"Analysis on the commercial set could leak its content","answered_at":"§5 \"For all analysis, we use the public set to avoid potential leakage with the commercial set.\""},
 {"reason":"Subset sizes may not add up to the stated totals","answered_at":"§3.3 and Abstract: 731+276+858=1,865 problems and 11+12+18=41 repositories (recomputed)"},
]

status_open = {"R13","R25"}
probes = [
 {"id":"P1","items":["R1"],"question":"Do Table 3 counts equal the unresolved public-set instances for each model?","method":"recompute: sum Submitted+Not-Submitted per row; compare with 731 x (1 - Table 1 rate)","result":"confirmed","location":"Table 3; Table 1; §6.2","change":"R1 question -> error (checked); A9 moderate -> weak","after_reviews":False},
 {"id":"P2","items":["R2"],"question":"Do the resolve rates in §5 Results match Table 1?","method":"cross-reference §5 text vs Table 1","result":"confirmed","location":"§5 Results; Table 1","change":"R2 open -> error (checked)","after_reviews":False},
 {"id":"P3","items":["R3","A4"],"question":"Can every subset satisfy 50-100 instances per repository?","method":"recompute 731/11, 858/12, 276/18","result":"confirmed","location":"§1; §3.1; §3.3; Abstract","change":"R3 open -> error (checked); A4 strong -> moderate","after_reviews":False},
 {"id":"P4","items":["R15"],"question":"Is Qwen's tool-use share 42.0% and the highest in Table 3?","method":"recompute tool-use / (Submitted+Not-Submitted) per row","result":"confirmed","location":"§6.2; Table 3","change":"R15 open -> error (checked)","after_reviews":False},
 {"id":"P5","items":["R4","A2"],"question":"Does the paper measure contamination anywhere (memorization probe, held-out vs public scores, dates)?","method":"re-read §3-§7 and appendix; text search for held-out results and contamination tests","result":"confirmed","location":"§3.1; §3.3; §5; §6","change":"R4 open -> checked (gap confirmed); A2 holds as design, not as measured resistance","after_reviews":False},
 {"id":"P6","items":["R6","A1"],"question":"Is SWE-Bench Verified run under the same scaffold and settings?","method":"text search for Verified; trace the >70% figure to [15]","result":"confirmed","location":"§1; Figure 2 caption; §5; ref [15]","change":"R6 open -> checked (no same-harness run); A1 holds for headroom, not for the size of the gap","after_reviews":False},
 {"id":"P7","items":["R7"],"question":"Are the reported rankings separable given N?","method":"binomial standard errors: N=731, p=0.233 -> ±3.06 pp; N=276, p=0.178 -> ±4.51 pp","result":"confirmed","location":"Table 1; Table 2; Abstract","change":"R7 open -> checked","after_reviews":False},
 {"id":"P8","items":["R9","R10","A3"],"question":"Does the paper measure human solve time or evaluate without requirements/interface?","method":"re-read §3.1, §4.2, §5, §7.1, App. A.2-A.3","result":"confirmed","location":"§3.1; §5 Issue Ambiguity; App. A.2","change":"R9, R10 open -> checked; new R28 (found by P8)","after_reviews":False},
 {"id":"P9","items":["R13"],"question":"What is the 'difficulty filtering' named in the Figure 1 caption?","method":"text search for difficulty/filter across all sections","result":"unsettled","location":"Figure 1 caption; §1; §4","change":"R13 stays question (open); capped at minor","after_reviews":False},
 {"id":"P10","items":["R11","R12","A5"],"question":"Are annotator statistics, funnel counts, agreement or a human-solve check reported?","method":"text search (annotator, agreement, verified, solve) and re-read §4","result":"confirmed","location":"§1; §3.2; §4.2-§4.3","change":"R11, R12 open -> checked; A5 holds as design only","after_reviews":False},
 {"id":"P11","items":["R14"],"question":"Is the judge validated on this data, and do its categories map onto Table 3?","method":"re-read §6.2 and App. B.1; compare 10 prompt categories with 9 table columns","result":"confirmed","location":"§6.2; Table 3; App. B.1","change":"R14 open -> checked","after_reviews":False},
 {"id":"P12","items":["R16"],"question":"Does the paper position itself against contamination-resistant and multi-language SWE benchmarks?","method":"re-read §1-§2; literature check offline (memory, [verify])","result":"partly","location":"§1; §2.1; refs [1], [24], [25]","change":"R16 open -> checked for the paper's own text; the external delta rests on memory","after_reviews":False},
 {"id":"P13","items":["R8"],"question":"Does the paper show that GPT-5's non-submissions reflect the model rather than the harness?","method":"re-read §5 Evaluation settings and §6.2; Table 3 GPT-5 row","result":"confirmed","location":"§5; §6.2; Table 3","change":"T1 grade of R8 updated after P13: minor -> major (not decisive for T1; scores unchanged)","after_reviews":True},
]

def acc(a):
    return {"id":a[0],"aspect":a[1],"reason":a[2],"location":a[3],"strength":a[4],"added_by":a[6],"claim":a[5],"status":"checked"}
def rej(r, added=None):
    d={"id":r[0],"aspect":r[1],"reason":r[2],"location":r[3],"kind":r[4],"worst_case":r[5],"fix":r[6],"added_by":added,"claim":r[7],"status":"open" if r[0] in status_open else "checked"}
    return d

reject=[rej(r) for r in R]+[rej(r[:8],r[8]) for r in R_ADDED]

types = [
 {"id":"T1","name":"SWE-agent and code-LLM benchmark specialist","likelihood":"high","aspect":"significance","field":"repository-level software-engineering agent evaluation (the task)",
  "grades":{"R4":"major","R6":"minor","R7":"minor","R8":"major","R9":"minor","R10":"minor","R12":"minor","R13":"minor","R16":"minor","R17":"minor","R19":"minor","R1":"minor","R14":"minor","R5":"minor"},
  "held":["A1","A2","A3","A4","A5","A8","A10","A13"],"discounted":["A9"],"decisive":["A1","A3","A2","R4"],"pool_position":66,"overall":4,"confidence":4,
  "scores":{"technical_rigor":58,"clarity":60,"novelty":60,"significance":72,"experimental_validation":58,"reproducibility":64,"ethics":62}},
 {"id":"T2","name":"Evaluation and measurement methodologist","likelihood":"high","aspect":"experimental_validation","field":"evaluation science / NLP benchmarking (neighbor)",
  "grades":{"R1":"major","R4":"major","R6":"major","R7":"major","R8":"major","R10":"major","R12":"major","R14":"major","R17":"major","R2":"minor","R13":"minor","R15":"minor","R18":"minor","R26":"minor"},
  "held":["A3","A6","A8"],"discounted":["A9","A1"],"decisive":["R6","R14","R1","R12","A3"],"pool_position":40,"overall":3,"confidence":4,
  "scores":{"technical_rigor":48,"clarity":54,"novelty":55,"significance":62,"experimental_validation":42,"reproducibility":58,"ethics":60}},
 {"id":"T3","name":"Empirical software-engineering researcher (mining repositories, test adequacy)","likelihood":"medium","aspect":"technical_rigor","field":"empirical software engineering / mining software repositories (neighbor)",
  "grades":{"R11":"major","R12":"major","R3":"major","R9":"major","R10":"major","R1":"major","R4":"minor","R25":"minor","R28":"minor","R2":"minor","R22":"minor","R26":"minor"},
  "held":["A5","A6","A3"],"discounted":["A12"],"decisive":["R11","R12","R9","R3","A6"],"pool_position":44,"overall":3,"confidence":4,
  "scores":{"technical_rigor":46,"clarity":55,"novelty":54,"significance":63,"experimental_validation":50,"reproducibility":54,"ethics":58}},
 {"id":"T4","name":"Data-contamination and training-data researcher","likelihood":"medium","aspect":"technical_rigor","field":"LLM data contamination and memorization (neighbor)",
  "grades":{"R4":"major","R27":"major","R5":"minor","R18":"minor","R16":"minor","R6":"minor","R13":"minor","R3":"minor","R21":"minor"},
  "held":["A2","A10","A13"],"discounted":[],"decisive":["R4","R27","A2","A10"],"pool_position":45,"overall":3,"confidence":4,
  "scores":{"technical_rigor":45,"clarity":56,"novelty":58,"significance":64,"experimental_validation":50,"reproducibility":55,"ethics":56}},
 {"id":"T5","name":"LLM-agent researcher, general ICLR reviewer","likelihood":"high","aspect":"clarity","field":"LLM agents and tool use (neighbor)",
  "grades":{"R1":"major","R9":"major","R6":"major","R14":"major","R2":"minor","R15":"minor","R21":"minor","R22":"minor","R24":"minor","R28":"minor","R25":"minor"},
  "held":["A12","A1"],"discounted":["A9"],"decisive":["R1","R14","R9","R2","A12"],"pool_position":48,"overall":3,"confidence":4,
  "scores":{"technical_rigor":50,"clarity":50,"novelty":56,"significance":64,"experimental_validation":50,"reproducibility":58,"ethics":60}},
 {"id":"T6","name":"Open-science and dataset-documentation reviewer","likelihood":"medium","aspect":"reproducibility","field":"datasets and benchmarks documentation / data governance (neighbor)",
  "grades":{"R11":"major","R8":"major","R20":"minor","R23":"minor","R18":"minor","R12":"minor","R24":"minor","R5":"minor"},
  "held":["A7","A12","A11"],"discounted":["A10"],"decisive":["R11","R8","A7"],"pool_position":50,"overall":3,"confidence":4,
  "scores":{"technical_rigor":54,"clarity":56,"novelty":56,"significance":65,"experimental_validation":52,"reproducibility":50,"ethics":54}},
 {"id":"T7","name":"Code-generation benchmark and program-synthesis researcher","likelihood":"medium","aspect":"novelty","field":"code generation benchmarks and program synthesis (neighbor)",
  "grades":{"R16":"major","R9":"major","R4":"major","R19":"minor","R6":"minor","R21":"minor","R17":"minor"},
  "held":["A2","A4","A13","A3"],"discounted":["A1"],"decisive":["R16","R4","A2","R9"],"pool_position":47,"overall":3,"confidence":4,
  "scores":{"technical_rigor":54,"clarity":58,"novelty":50,"significance":64,"experimental_validation":52,"reproducibility":58,"ethics":60}},
]

ledger={"accept":[acc(a) for a in A],"reject":reject,"answered":answered,"probes":probes,
        "types":[{k:v for k,v in t.items() if k!="scores"} for t in types]}
json.dump(ledger,open(os.path.join(OUT,"ledger.json"),"w"),indent=1,ensure_ascii=False)

scores={"paper_type":"benchmark","reviewers":[{"role":f"{t['id']} ({t['name']})","aspect":t["aspect"],"confidence":t["confidence"],"overall":t["overall"],"pool_position":t["pool_position"],"scores":t["scores"]} for t in types],"da_critical":[]}
json.dump(scores,open(os.path.join(OUT,"scores.json"),"w"),indent=1,ensure_ascii=False)

# sanity checks
ids={r["id"]:r for r in reject}
for t in types:
    for k,g in t["grades"].items():
        r=ids[k]; order=["not a concern","minor","major","fatal"]
        assert order.index(g)<=order.index(r["worst_case"]),(t["id"],k)
        if r["kind"]=="question" and r["status"]=="open": assert g in("minor","not a concern"),(t["id"],k)
allw=set()
for t in types: allw|=set(t["grades"])|set(t["held"])|set(t["discounted"])
missing=[x["id"] for x in ledger["accept"]+reject if x["id"] not in allw]
print("not weighed by any type:",missing)
from collections import Counter
maj=Counter();
for t in types:
    for k,g in t["grades"].items():
        if g in("major","fatal"): maj[k]+=1
print("major counts:",maj.most_common())
