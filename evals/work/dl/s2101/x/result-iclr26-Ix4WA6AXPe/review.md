# Simulated Review: "Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models"

*Date: 2026-11-10. Full mode, target venue ICLR, literature check: strict (cutoff 2025-09-24). The five reviews were written one after another in a single model context (no subagents), so they are role-based passes and not independent agents. The decision is a simulation of how a careful panel might see this draft, not a prediction. Figures were not available (text extraction only); figure-dependent claims are judged from captions and text.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models |
| Primary Discipline | ML / NLP → LLM unlearning (evaluation + objective design) |
| Secondary Discipline(s) | Retrieval-augmented generation; knowledge distillation / KL regularization; AI privacy and compliance |
| Paper Type | Empirical (composite weights: empirical). It mixes an evaluation finding and a method. |
| Core Technique(s) | Gradient-based and representation-based unlearning (NPO, RMU, UNDIAL, GradAscent, GradDiff, DPO) on TOFU; KL-consistency term against the frozen original model; LLM-as-judge evaluation |
| Target Venue | ICLR 2026 (stated by the user); profile key `iclr`; scale status secondary |
| Venue-Specific Notes | none; the paper is single-column ICLR style ("Preprint") |
| Paper Maturity | Submission-ready draft with a narrow evaluation |
| Ethics-Relevant Content | none directly (fictitious TOFU authors); the privacy and legal motivation is relevant to Reviewer 3 |

### Claimed Contributions (as stated by the authors)
1. **C1 (problem/finding)**: In a systematic evaluation of six unlearning methods, "they consistently impair such contextual utility" (Abstract, §1, §3, Fig. 2, Table 1).
2. **C2 (method)**: A plug-in context term (KL to the frozen original model on forget questions paired with their gold context) that "restores contextual utility to near original levels" while keeping forgetting and retain-set utility (Abstract, §4.2, §5, Table 2).
3. **C3 (result)**: The fix holds across forget ratios (1/5/10%; §6.1, Fig. 4) and context variants (§6.2, Table 4) and is insensitive to λc (§4.2, App. A.4, Fig. 9).

### Paper memory (factual record shared with all reviewers)
- **Setup:** TOFU, forget ratios 1/5/10%; Gemma-2B-IT and Qwen3-8B (§3). Main results at 5% only; 1% and 10% on Gemma only (§6.1, App. A.2.2). AdamW, weight decay 0.01, lr 1e-5, effective batch 32, 20 epochs instead of TOFU's 5, A100s (App. A.1.1). Contextual QA prompt gives the gold answer sentence for each forget question (§3, Fig. 5). Judge: Claude 3.5 Sonnet v2, binary 0/1 (App. A.1.2). Metrics: ROUGE-L, LLM-Judge, model utility; probability metrics omitted (§3).
- **Training of the proposed term:** C(S_f^ctx, w) averages KL(p_w(·|q,c) || p_orig(·|q,c)) over the forget (q,c) pairs (§4.2). Fig. 3 shows the training pair for the Basil Mahfouz Al-Kuwaiti example, which is the same example as the evaluation prompt in Fig. 5 and Table 1.
- **Selection:** λc ∈ {2.0, 0.01, 0.5} (Gemma NPO/RMU/UNDIAL), {1.0, 0.5, 1.0} (Qwen) (§5). Reported epoch is "the earliest epoch at which it has converged", with tolerance 0.01, no smoothing (§5, App. A.4). λc is picked from six values by highest Contextual LLM-Judge and utility among those with Direct LLM-Judge within δ = 0.06 of vanilla (App. A.4).
- **Not stated after search:** seeds, number of runs, variance, code or data release, a limitations section, an ethics or broader-impact statement, the pre-unlearning model's row in Table 2, any Contextual QA evaluation on retain-set entities, any held-out context split, judge validation against humans.
- **Headline numbers:** Contextual LLM-Judge 0.54 → 0.98 (Gemma), 0.62 → 0.97 (Qwen) (§1; Table 2 averages); RMU contextual ≤ 0.05 → ≥ 0.97 (§5; Table 2); Direct QA shifts "about 2" and "3" pp LLM-Judge, 5 and 2 pp ROUGE-L (§1).
- **Unverifiable here:** Figs. 2, 4, 7, 8, 9 (curves across epochs). The pre-unlearning baseline for the "15.5% to 100%" drops (§1) appears only in figures.

### Integrity scan (Phase 0, Hard Rule 9)
Searched the full text for reviewer-directed or AI-directed text (e.g., "ignore previous", "give a positive review", "LLM reviewers"). **None found.** (The scan was a text search done by me; the skill's `integrity_scan.py` was not run because this evaluation allows only the aggregation and literature scripts.) The five reviewers read the text as is.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Helena Marchetti-Okafor, large public research university (Western Europe)
- **Seniority / Expertise**: Senior faculty / language-model training and evaluation, privacy-preserving ML
- **Role**: Reads all five reviews, checks decisive points against the paper, weights reviewers, decides
- **Style**: Acts like an experienced ICLR area chair; asks "does the evidence test the claim?" before counting scores

### Reviewer 1 (Methodology): Dr. Tomasz Reinholt, industrial research lab (Central Europe)
- **Seniority / Expertise**: Mid-career industry scientist / LLM fine-tuning, LLM-as-judge evaluation, unlearning protocols
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on held-out evaluation and pre-registered selection rules

### Reviewer 2 (Domain): Prof. Mei-Ling Sato-Rao, vision-and-language group, large public university (East Asia)
- **Seniority / Expertise**: Senior faculty / machine unlearning, knowledge editing, in-context learning
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks every novelty claim against the abstract of the cited work

### Reviewer 3 (Perspective): Dr. Kwame Adjei-Lindgren, policy-oriented AI governance institute (Northern Europe/West Africa)
- **Seniority / Expertise**: Postdoc-to-mid-career / data-protection law and AI compliance, adversarial/relearning security
- **Review Focus**: Cross-disciplinary links, deployment, assumptions, broader impact
- **Style**: Constructive; asks what the method means for compliance and security

### Reviewer 4 (Generalist): Dr. Priya Venkataraman, applied NLP lab, mid-sized university (South Asia)
- **Seniority / Expertise**: Mid-career / question answering, RAG systems
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee reader; weighs contribution against weaknesses

### Devil's Advocate: Dr. Rafael Echeverría-Holt, evaluation-methodology group (South America)
- **Seniority / Expertise**: Senior researcher / causal evaluation design, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; states the steelman first

*Personas are fictional. Assumptions: venue ICLR (stated), paper type empirical, maturity submission-ready.*

---

# Phase 1: Independent Reviews

## Reviewer 1 (Methodology): Dr. Tomasz Reinholt

### Summary
The paper studies "contextual utility": whether an unlearned model can still answer a TOFU forget-set question when the gold answer sentence is placed in the prompt. Across six unlearning methods on Gemma-2B-IT and Qwen3-8B, contextual QA collapses for most methods (Fig. 2, Table 1). The authors add a KL term that keeps the model's output distribution on (question, gold-context) prompts close to the frozen original model, and report that contextual LLM-Judge rises to ≥ 0.95 for NPO, RMU and UNDIAL while Direct QA and utility change little (Table 2).

### Strengths
- **S1: A real blind spot is named and measured (§3, Fig. 1).** Unlearning evaluations on TOFU ignore whether the model still reads supplied evidence. The Contextual QA setting is cheap to run and easy to reuse.
- **S2: Consistent headline arithmetic.** The averages in §1 reproduce from Table 2: Gemma contextual LLM-Judge (0.81+0.00+0.82)/3 = 0.54 and (0.98+0.99+0.98)/3 = 0.98; Qwen (0.84+0.05+0.97)/3 = 0.62 and (0.95+0.97+0.98)/3 = 0.97. Utility changes (−0.007 Gemma, 0.00 Qwen) also reproduce.
- **S3: Disclosure of selection rules (App. A.4).** The convergence criterion, tolerance and λc grid are stated, which makes the protocol auditable, even though I object to it below.
- **S4: Useful diagnostics beyond averages.** Tables 1 and 3 show the failure modes (gibberish, hallucination), and App. A.3 offers per-objective explanations.

### Weaknesses

### W1: Contextual QA for the proposed method is evaluated on the prompts it is trained on (most severe)
The context term is trained on "the forget examples paired with their ground-truth context" (§4.2); the evaluation prompt is "the ground-truth answer to each question" for the same forget questions (§3), and §5 states "We use the same datasets, models, metrics, and training settings as described in Section 3." Fig. 3 (bottom) is the Basil Mahfouz example, which is also the evaluation prompt in Fig. 5 and Table 1, with the same template. No held-out split of questions, contexts or templates is described anywhere (protocol sweep: not stated after search). The ≥ 0.95 numbers in Table 2 therefore measure fit on training prompts. The vanilla methods have the same exposure to the forget set, but only the proposed term trains directly on the evaluated input-output behavior.
- **Suggested Fix:** Split the forget set (or the contexts) into train and held-out parts; train the context term on one part and report Contextual QA on the other, plus held-out templates and paraphrased contexts (§6.2 does this for one example only). Cost: three methods × two models × one rerun, about 30–60 A100-hours at the reported scale.

### W2: Epoch and λc are selected on the reported metrics, with no validation split
The reported epoch is "the earliest epoch at which it has converged" (§5), defined relative to the "global best" of each series over 20 epochs with "no smoothing" (App. A.4). λc is chosen as "the one with the highest Contextual QA score (LLM-Judge) and model utility jointly" among values whose Direct LLM-Judge is within δ = 0.06 of vanilla (App. A.4); the chosen λc produce Table 2. TOFU has no validation split, so this is selection on the evaluation set. The authors say the method is "stable and insensitive to" λc (§4.2), but λc differs by 200× across methods (0.01 to 2.0, §5), which is not what insensitivity looks like. δ = 0.06 equals the Direct LLM-Judge increase for NPO on both models (0.19→0.25; 0.14→0.20, Table 2), so the chosen runs sit exactly at the allowed slack.
- **Suggested Fix:** Fix λc and the epoch on a validation subset of forget questions, report all epochs and all six λc as curves with the test numbers at the pre-fixed choice, and add 3–5 seeds.

### W3: The contextual-failure diagnosis lacks the control that separates "forget-specific suppression" from general breakdown
Contextual QA is only run on forget-set questions (§3). Vanilla outputs such as "des of demon demon..." or "patrie" (Table 1, Table 4) look like generation collapse, and model utility is measured with direct QA only. Without Contextual QA on retain-set entities and on the original model's row (absent from Table 2), the claim that unlearning "suppresses" use of forgotten knowledge in context (§4.1) is not separated from a model that no longer follows the instruction-plus-context format. The mechanism text in §4.2 ("this penalty propagates into inference-time conditioning") and App. A.3 ("causing contextual collapse") is asserted, not tested (no probing or layer analysis).
- **Suggested Fix:** Add Contextual QA on retain entities and on world-knowledge questions, add the original model's row to Table 2, and either test the mechanism (e.g., activation-distance on forget tokens in context) or soften §4.2 and A.3.

### W4: Forgetting strength is not controlled across methods or between vanilla and context-aware runs
UNDIAL "remain[s] above the retrain-on-retain" baseline, "suggesting under-unlearning" (App. A.2.1), and vanilla UNDIAL keeps contextual LLM-Judge 0.82/0.97 (Table 2), so its "better preservation" (§3) may just be weak forgetting. For RMU on Gemma, Direct ROUGE-L goes from 0.04 to 0.13 with the context term (Table 2). The statement "The effects on forgetting and utility are marginal and largely neutral" (§5) rests on averages; NPO's Direct LLM-Judge rises by 0.06 on both models (+32% and +43% relative, derived). Table 2 shows no retrain-on-retain reference.
- **Suggested Fix:** Report Direct QA relative to the retrain-on-retain reference, show forget-vs-contextual trade-off curves, and extend the claim only where forgetting is matched.

### W5: Single run, narrow scope, judge not validated
No seeds or variance are reported anywhere (not stated after search), the comparison rests on one benchmark of fictitious authors with single-sentence gold contexts, two models, and a single binary LLM judge with no human agreement check (App. A.1.2). Main results are at 5% only. The abstract's "Extensive experiments" and "practical, general augmentation" (§1) cover three of the six methods studied (GradAscent, GradDiff, DPO are not extended).
- **Suggested Fix:** Seeds, a second benchmark (e.g., MUSE, cited in §2.1), human or second-judge agreement on a sample, and either extend to all six methods or narrow "general".

### Error Log

| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E4 | §4.2 vs §3, §5, Fig. 3 vs Fig. 5 | "denotes the forget examples paired with their ground-truth context" | Training pairs for the context term are the evaluation prompts | Cross-referenced four locations | High | MAJOR | Held-out evaluation |
| ERR-2 | E4 | §5; App. A.4 | "select the one with the highest Contextual QA score (LLM-Judge) and model utility jointly" | Hyperparameter and epoch chosen on the reported metrics; TOFU has no validation split | Cross-referenced §5 and A.4 | High | MAJOR | Validation split; fixed protocol |
| ERR-3 | E1 | §5 vs Table 2 | "increases by about 17% and 10% on average for NPO and UNDIAL across the two models" | Table 2 deltas average to 0.14 (NPO: 0.17, 0.11) and 0.09 (UNDIAL: 0.16, 0.02) | Recomputed | High | MINOR | Correct the text |
| ERR-4 | E8 | §1; Table 2 | "reduce Contextual QA performance by 15.5% to 100%" | The pre-unlearning baseline behind these ratios is not in any table | Searched text and tables | Medium | MINOR | Add the original-model row |

### Claim-to-Evidence Map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Existing methods impair contextual utility | Abstract, §3 | Fig. 2 (figure unseen), Table 1 (one example), Table 2 vanilla rows | Supported for the forget set on TOFU; specificity untested (W3) |
| C2 | Context term restores contextual utility near original | Abstract, §5 | Table 2 | Partially: measured on training prompts (W1), selected on test metrics (W2) |
| C3 | Robust to forget ratio, context variants, λc | §6.1, §6.2, App. A.4 | Fig. 4 (unseen), Table 4 (one example), Fig. 9 (unseen) | Partially: one hand-modified example; Gemma only |

### Questions for Authors
1. Are the contexts used in training the context term the same text as those in the Contextual QA evaluation? A "yes, but results hold on a held-out split" answer would raise my rating to 4; confirmation of full overlap lowers it.
2. What do the original model's contextual numbers look like in the 5% setting, and what does a vanilla-unlearned model score on retain-entity contextual prompts?
3. How does "within δ of vanilla" (A.4) interact with the NPO Direct deltas of +0.06?

### Limitations Assessment
Partially. The paper has no limitations section (not stated after search). It should discuss the train/eval overlap, the single benchmark, the fictitious data and the selection protocol.

### Pool position
Better than about 45% of ICLR submissions (accepted share ≈ 27%). Deciding evidence: the central positive result is measured on training prompts with test-metric selection, and the claim is only tested on one fictitious-data benchmark.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Overlap and selection issues (W1, W2) |
| Clarity | 3 | Clear, protocol details in appendix |
| Significance | 2 | Narrow evidence base |
| Originality | 2 | Useful framing, incremental method |

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | W1, W2; sound loss definitions otherwise |
| Clarity & Presentation | 66 | Competent | Clear; Table 4 caption duplicates Table 3 |
| Novelty & Originality | 52 | Developing | New angle, standard KL regularizer |
| Significance & Impact | 55 | Competent | Relevant to RAG-era use, evidence narrow |
| Experimental Validation | 40 | Developing | No held-out, no seeds, one benchmark, no retain-entity control |
| Reproducibility | 55 | Competent | Hyperparameters stated; no code, seeds or λ-per-run curves |
| Ethical Compliance | 65 | Competent | Low risk; no limitations paragraph |

**Overall Score: 3** (Borderline Reject). A useful problem with an evaluation that cannot yet support the main positive claim.
**Confidence: 4.**
**Ethics Review Flag:** No.

---

## Reviewer 2 (Domain): Prof. Mei-Ling Sato-Rao

### Summary
The paper argues that unlearning evaluation should include a "contextual utility" test and proposes adding a KL term anchored to the original model on forget questions with gold context. I read it for positioning, novelty and citation accuracy; a literature check (strict, cutoff 2025-09-24) was run after drafting.

### Strengths
- **S1: The framing is timely.** RAG and prompt-supplied evidence are common (§1), and "unlearned model, evidence in prompt" is a distinct scenario from prior work on prompts that induce forgetting (§2.2: Pawelczyk et al., Muresanu et al.) or that resurface forgotten facts (Shumailov et al., Cooper et al.).
- **S2: Honest about related directions.** §2.2 separates this work from in-context unlearning and relearning attacks.
- **S3: Broad method coverage for the diagnosis.** Six methods spanning gradient ascent, preference, relabeling and representation methods are evaluated (§3).

### Weaknesses

### W1: The method is a standard retain-style KL regularizer applied to a new set of prompts
The paper motivates the term by "KL-regularization in RLHF" and alignment (§1) and writes the objective as one extra term (§4.2). Given that a gold-context prompt is an easy input for the original model (near-ceiling LLM-Judge), the term effectively distills the original model on those prompts. The novelty is the choice of prompts and the diagnosis, which is a modest but real contribution; it is not a new mechanism. The §4.2 phrase "explicitly rewards correct responses" also does not describe a KL term, which penalizes divergence from the original model, including its mistakes.
- **Suggested Fix:** Position the method as a data-selection extension of retain regularization, and add ablations that separate "KL on contexts" from simply fine-tuning on (q, c) → a and from adding retain-style contextual examples from retain entities.

### W2: Relation to context-conditioned unlearning and "pretend to forget" findings is not discussed
The paper cites relearning and in-context resurfacing (§2.2) but not work that fine-tunes models to forget or reveal depending on the prompt context (see Missing References). A model trained to answer from context while giving wrong answers without it (Table 4) is exactly a context-conditioned switch, which raises the question of whether knowledge was removed or hidden (the concern behind Hu et al. 2025 and Cooper et al. 2024, both cited in §2.1).
- **Suggested Fix:** Discuss this line, and test whether the context-aware model recovers forgotten facts under partial or related-but-answer-free contexts.

### W3: Claims of "state-of-the-art" breadth outrun the benchmark choice
The §1 framing is about real-world regulations and RAG, but the only benchmark is fictitious TOFU with one-sentence gold contexts. Related evaluation suites that the paper cites (MUSE, WMDP, OpenUnlearning; §1, §2.1) are not used.
- **Suggested Fix:** Add one non-fictitious or multi-document setting, or restrict the wording.

### Error Log (citation check, E7)
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-5 | E7 | §3 Metrics vs References | "We also follow TOFU (Touvron et al., 2023) in reporting model utility" | The cited Touvron et al. 2023 entry in References is the Llama 2 report, not TOFU (Maini et al., 2024) | Compared in-text citation with the bibliography entry | High | MINOR | Cite Maini et al., 2024 |

Other citation checks: Zhang et al. 2024a (NPO), Dong et al. 2025 (UNDIAL), Li et al. 2024 (WMDP, cited as the source of RMU in §2.1) and Maini et al. 2024 correspond to what the text says. The §1 attribution of "KL-regularization ... related alignment techniques" to Maini et al. 2024 is loose (TOFU is a benchmark paper); I leave it as a question.

### Literature-check addendum (strict mode, cutoff 2025-09-24)
Run: 6 queries counted of 12 (5 claim, 1 baseline), 39 unique kept results; `coverage` reported no relevant gap (the only flagged gap was no prior work from 2021–2022, which predates LLM unlearning); `similarity` flagged no text overlap (0 shared 8-grams) and low conceptual overlap (cosine ≤ 0.17 for the top 3 prior works). The search covers arXiv only.

**Per-claim novelty**
| Claim | Dimension | Novelty | Top prior work (verified link, label, cited?) | Reasoning |
|-------|-----------|---------|-----------------------------------------------|-----------|
| C1 | problem/result | medium to high | Takashiro et al., "Answer When Needed, Forget When Not" (arXiv 2410.00382, prior peer-reviewed, ACL Findings 2025), not cited; level 2 (shared topic and benchmark, opposite direction: forgetting conditioned on context) | No kept paper measures loss of contextual use after unlearning; "no close prior work found in 39 results" (arXiv only, so at most medium to high) |
| C2 | method | incremental | Prior KL-anchored regularizers in unlearning and RLHF as the paper itself says (§1); level 3 from the paper's own framing; no single uncited prior work covers it | Mechanism is a standard anchor; the prompt choice is new |
| C3 | result | medium | none | Robustness claims are the paper's own experiments |

No claim reaches level 5, so no "known results" finding (DA criterion 7 not applicable).

**Novelty delta table (closest prior works)**
| Claimed contribution | Closest prior work (link) | What it already does | What is new here | Cited and differentiated? |
|----------------------|---------------------------|----------------------|------------------|---------------------------|
| Context-aware unlearning | "Is Retain Set All You Need in Machine Unlearning?" (arxiv.org/abs/2404.12922, prior arXiv-only), cosine 0.17 | Image-domain unlearning with retain-set effects | Different modality and goal | No (different area; not a required citation) |
| Contextual evaluation on TOFU | TOFU (arxiv.org/abs/2401.06121) | Source benchmark | New evaluation mode | Yes (Maini et al., 2024) |
| Side effects of unlearning | "Not All Data Are Unlearned Equally" (arxiv.org/abs/2504.05058, prior peer-reviewed) | Studies how data frequency affects unlearning | Different side effect | No |

**Baseline scout:** the only external benchmark is TOFU (a benchmark the paper uses as is). The search surfaced no prior (peer-reviewed or 6+ month arXiv) TOFU method that is clearly stronger than the three extended methods and missing from the comparison; recent preprints (e.g., "DUSK", "UIPE") are "worth discussing" only.

**Field snapshot.** Around 2023–2024 the field moved from gradient ascent to preference-style (NPO) and representation-based (RMU) objectives, evaluated on TOFU, MUSE and WMDP. By mid-2025 attention was on robustness of forgetting (relearning, extraction, "obfuscation") and on side effects on related or shared knowledge. Open problems listed by recent work include evaluation beyond direct recall and the gap between suppressing and removing knowledge. A significant contribution now is a new failure mode shown across several methods with a method-agnostic fix and evidence beyond a single benchmark; a one-benchmark finding with a hyperparameter-tuned regularizer is incremental. This calibrates Novelty and Significance below.

### Missing References
| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | S. Takashiro, T. Kojima, A. Gambardella, Q. Cao, Y. Iwasawa, Y. Matsuo, "Answer When Needed, Forget When Not: Language Models Pretend to Forget via In-Context Knowledge Unlearning", ACL Findings 2025 (arXiv 2410.00382; verified by search) | Uses TOFU and fine-tunes models to forget or reveal depending on prompt context; the "pretend to forget" finding is directly relevant to what the context term teaches |
| Important | A. Lynch et al., "Eight Methods to Evaluate Robust Unlearning in LLMs", 2024 (arXiv 2402.16835; found by `verify`; arXiv-only, prior) | Broader evaluation of unlearning beyond direct QA |
| Helpful | "Do LLMs Really Forget? Evaluating Unlearning with Knowledge Correlation and Confidence Awareness", 2025 (arXiv 2506.05735; verified, peer-reviewed as labelled by the search) | Evaluation of unlearning beyond direct recall |
| Worth discussing (recent preprint, never a weakness) | "DUSK: Do Not Unlearn Shared Knowledge", 2025 (arXiv 2505.15209) | Another side-effect on preserved knowledge; recent preprint |

### Questions for Authors
1. Does the context-aware model still refuse or fail when the context does not contain the answer? If it answers from memory, the forgetting is only conditional.
2. Why is KL to the original model preferable to plain supervised fine-tuning on (q, c) → a?
3. §A.2.1 describes the retain baseline as "a model retrained from scratch on only the retain set"; TOFU's retain model is, as I recall, a fine-tune of the base model on the retain split `[verify]`. Which one is used?

### Limitations Assessment
Partially. No limitations section, no discussion of how the conditional behavior relates to true removal.

### Pool position
Better than about 52% of ICLR submissions (accepted ≈ 27%). Deciding evidence: a clear and relevant new evaluation angle, but an incremental method, and positioning that omits the context-conditioned-unlearning line.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Methodological gaps noted by R1 |
| Clarity | 3 | Clear |
| Significance | 2 | Narrow benchmark |
| Originality | 2 | New angle, standard mechanism |

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Objective is sound; mechanistic story asserted |
| Clarity & Presentation | 68 | Competent | Clear exposition |
| Novelty & Originality | 55 | Competent | New diagnosis (medium), method incremental |
| Significance & Impact | 58 | Competent | Practically motivated |
| Experimental Validation | 50 | Developing | One benchmark, no external baselines for the fix |
| Reproducibility | 58 | Competent | Settings given, no code |
| Ethical Compliance | 65 | Competent | Low risk |

**Overall Score: 3** (Borderline Reject). **Confidence: 4.** **Ethics Review Flag:** No.

---

## Reviewer 3 (Perspective): Dr. Kwame Adjei-Lindgren

### Summary
The paper looks at a deployment scenario that compliance-minded teams will recognize: after removing outdated or sensitive knowledge, can a user or a retrieval system still supply that information in the prompt and get a correct answer? The authors show that common unlearning methods break this, and propose a KL term that restores it.

### Strengths
- **S1: The scenario is practically important.** The tax-regulation example (§1) is exactly the kind of "do not recall, do read" requirement found in compliance, legal and enterprise settings. The separation of "memory" from "evidence" is the right conceptual distinction.
- **S2: Plug-in design.** The term is added to the objective with one coefficient (§4.2), which suits deployment where an unlearning method is already in place.
- **S3: Clear failure illustrations.** Tables 1, 3 and 4 make the user-visible symptoms concrete.
- **S4: Case study on context variants (§6.2, Table 4)** is a good start toward robustness.

### Weaknesses

### W1: The unstated assumption that "can use when supplied" is compatible with "forgotten"
The method trains the model to reproduce the removed fact when it appears in context. For privacy or copyright removal, this is exactly the behavior an adversary can exploit: if the context term teaches a switch that treats the forgotten entity's text as trusted evidence, partial contexts or related-fact contexts may lead the model to reconstruct the removed content. The paper tests only gold contexts (§3, §5) and the single-example variants in Table 4. §2.2 acknowledges attacks that resurface knowledge, but they are not evaluated against the proposed model.
- **Suggested Fix:** Evaluate answer-free, partial, distractor and misleading contexts, and a relearning attack from the cited Hu et al. line (§2.1), on the vanilla and context-aware models.

### W2: Deployment realism: contexts are one-sentence gold answers
TOFU contexts are the answer sentence itself (Fig. 5). Real RAG contexts are long, noisy, multi-document, and may conflict. The §1 motivation (retrieval-augmented systems) is not tested with a retrieval pipeline.
- **Suggested Fix:** Add a RAG-style test with retrieved passages (gold plus distractors) and long contexts.

### W3: The "insensitive to λc" practicality claim
The appendix suggests practitioners can pick λc using the forget and retain sets (A.4), but in deployment, the forget set's gold contexts are the same data the term trains on, so a practitioner using them to choose λc has no held-out check. Cross-method λc values in §5 vary from 0.01 to 2.0.
- **Suggested Fix:** Offer a recipe with a validation split.

### Missing connections
Connect to **knowledge-conflict research in RAG** (models weighing parametric versus contextual knowledge; I describe the line of work rather than citing specific papers), to **conditional/gated behavior** in safety training (refusal under specific triggers), and to **data-protection practice**, where "erasure" of a person's data and the ability to process a document the user supplies are treated as separate obligations.

### Questions for Authors
1. What happens when the supplied context is partially correct, outdated or contradicts the original (pre-unlearning) knowledge? A graceful "context wins" behavior would raise my score.
2. Does Direct QA leakage increase when the prompt contains related but answer-free evidence?
3. How do you see this being used with legal "erasure" requirements, given that the model's context behavior is restored?

### Limitations Assessment
Partially. No limitations or broader-impact text. A paragraph on the conditional-forgetting interpretation is needed.

### Pool position
Better than about 68% of ICLR submissions (accepted ≈ 27%). Deciding evidence: a relevant, cleanly stated deployment problem with a simple fix that mostly works on its benchmark; the evidence is narrow but typical of accepted analysis-plus-method papers.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Narrow evaluation |
| Clarity | 3 | Clear |
| Significance | 3 | Relevant to deployment |
| Originality | 3 | Fresh framing |

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 63 | Competent | Sound as an objective |
| Clarity & Presentation | 72 | Competent | Good figures and examples (from captions) |
| Novelty & Originality | 62 | Competent | New problem framing |
| Significance & Impact | 68 | Competent | Important scenario, untested at deployment realism |
| Experimental Validation | 56 | Competent | Narrow, gold contexts only |
| Reproducibility | 60 | Competent | Settings stated, no code |
| Ethical Compliance | 62 | Competent | No ethics text; dual-use of conditional forgetting not discussed |

**Overall Score: 4** (Borderline Accept). **Confidence: 3.** **Ethics Review Flag:** No (no human data; the concern in W1 is scientific).

---

## Reviewer 4 (Generalist): Dr. Priya Venkataraman

### The contribution in one paragraph
Standard unlearning evaluation checks that the forgotten fact is gone and that other knowledge survives. This paper adds a third check: if the fact is given in the prompt, is the model still able to use it? It shows that most methods fail this check on TOFU and that adding a KL term toward the original model on forget questions with gold context repairs it for NPO, RMU and UNDIAL, with little change in forgetting or utility.

### Strengths
- **S1: Very readable.** Fig. 1 (from its caption) and Fig. 3 explain the three settings and the training examples in a few lines; the structure (§3 diagnosis, §4 fix, §5 results) is easy to follow.
- **S2: A clean, memorable message.** "Forget to know, remember to use" is a crisp framing, and the plug-in view (§4.2) is easy to adopt.
- **S3: Consistent positive signal in Table 2.** Contextual LLM-Judge improves for every method on both models (+0.02 to +0.99), including RMU 0.00 → 0.99 on Gemma.
- **S4: Fits ICLR's audience.** An LLM-safety/unlearning evaluation paper with a simple method suits the venue; reviews at ICLR for such papers reward clear new evaluation axes.

### Weaknesses

### W1: The central evidence is thin for a method paper
Table 2 covers one forget ratio (5%), three methods and two models, one run each; §6.1 adds Gemma only. Table 4 (§6.2) is a single example. "Extensive experiments" (Abstract) overstates this. The other reviewers' concerns about evaluating on training prompts apply: the generalist reader will ask whether a held-out question would also work.
- **Suggested Fix:** Report 1% and 10% on both models in a table, add seeds, and a held-out split.

### W2: Presentation details that make the evidence hard to read
Table 2 omits the original model's row, so "near original levels" (Abstract) cannot be checked from the table; Table 4's caption repeats Table 3's caption although Table 4 includes a Direct QA row; the text says RMU contextual is "below 0.05" (§1) while Table 2 prints 0.05 for Qwen vanilla; §5 gives "about 17% and 10%" which does not match the Table 2 deltas (0.14 and 0.09 averages, derived). There is also a mis-citation of TOFU (§3, Touvron et al., 2023).
- **Suggested Fix:** Add the original row, fix captions and numbers.

### W3: No limitations discussion and a loosely specified evaluation
No limitations section (the checklist-style statement is absent); the LLM-judge is a single binary judge (App. A.1.2) with no agreement check, and contexts are the gold sentence.
- **Suggested Fix:** Add a limitations paragraph, a judge-agreement sample, and one realistic RAG setting.

### Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | Table 2 vs. overlap and selection (§4.2, App. A.4) |
| Presentation | Met | §3–§5 |
| Contribution: new insight useful to community | Met (new evaluation axis) | §3 |
| Reproducibility signals | Partly | App. A.1; no code, seeds |
| Limitations honestly stated | Not met | No section |

### Questions for Authors
1. Can you show Table 2 for 1% and 10% on Qwen3-8B and a second seed?
2. Can the Contextual QA numbers be given for the original model for all rows?
3. What would you cut from the claims if held-out results are weaker?

### Limitations Assessment
No. There is no dedicated discussion.

### Pool position
Better than about 66% of ICLR submissions (accepted ≈ 27%). Deciding evidence: a clear, useful new evaluation axis and simple fix, with weaknesses (single benchmark, single run, some overclaiming) that are typical of accepted papers at ICLR; I weigh them against clarity and relevance and lean toward accept.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation gaps |
| Clarity | 3 | Very readable |
| Significance | 3 | Useful axis |
| Originality | 3 | New angle |

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound objective |
| Clarity & Presentation | 72 | Competent | Clear, a few number and caption slips |
| Novelty & Originality | 60 | Competent | Fresh axis |
| Significance & Impact | 64 | Competent | Relevant to RAG-era LLMs |
| Experimental Validation | 55 | Competent | Narrow |
| Reproducibility | 62 | Competent | Hyperparameters stated |
| Ethical Compliance | 66 | Competent | Low risk, no limitations text |

**Overall Score: 4** (Borderline Accept). **Confidence: 4.** **Ethics Review Flag:** No.

---

## Devil's Advocate Report

**Paper:** Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models
**Reviewer:** Dr. Rafael Echeverría-Holt, evaluation-methodology group (South America)

### Steelman
Unlearning papers evaluate whether a fact is gone but not whether the model still reads a fact placed in the prompt. The authors show a measurable and, for RMU, near-total loss of that ability, and a one-line KL term brings it back on all three tested methods without visible loss of forgetting or utility.

### Core Argument Chain
1. P1: Unlearning objectives penalize behavior on the forget set (§4.1).
2. P2: This penalty also suppresses use of the same facts when supplied as context (§3, Table 2 vanilla rows).
3. P3: A KL term to the original model on (q, c) prompts removes that suppression (Table 2).
4. P4: It does so without weakening forgetting or utility (Table 2, §5).
5. P5: The result is robust (forget ratio, context variants, λc) (§6, A.4).
∴ Context-aware unlearning "restores contextual utility to near original levels" and is a general plug-in.

### Strongest Counter-Argument
The proposed fix is evaluated on the exact prompts it is trained on. The context term minimizes KL between the unlearned and original model on the forget questions with their gold contexts (§4.2); Contextual QA is then scored on those same questions and contexts (§3, §5), and the gold prompt in Fig. 3 is the very one scored in Fig. 5 and Table 1. For a model whose original behavior on these prompts is near-perfect, matching the original on them is the same as scoring near-perfectly on them. The result is a statement about fit on training data. It says nothing about the property the paper cares about: that a user can supply forgotten information in a new prompt and obtain a correct answer.

The alternative readings are not excluded. The model may have learned a template-conditioned switch ("when the prompt starts with 'Answer the question based on given context', copy"), since training and test use one template (Fig. 3, Fig. 5). It may have memorized the few hundred forget-set (q, c) pairs. Table 4 is the only out-of-training probe: one question, two manually written contexts ("manually modify the context to probe robustness"), and no counts. The selection of epoch and λc by Contextual LLM-Judge on these same prompts (A.4) compounds this: the numbers in Table 2 are the best-scoring configuration on the evaluated prompts, with ε = 0.01 and "no smoothing" so that selection exploits epoch-to-epoch noise. Finally, the vanilla baselines that show "contextual collapse" were never tested on retain-set prompts, so the diagnosis may reflect general breakdown (gibberish outputs, Table 1) rather than forget-specific suppression. The paper would be convincing if held-out contexts, held-out questions and retain controls gave the same picture; as written, the main positive claim is untested.

### CRITICAL Issues

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence | §4.2 vs §3, §5; Fig. 3 vs Fig. 5, Table 1; Table 2 | The context term is trained on the forget (q, c) pairs on which Contextual QA is scored ("denotes the forget examples paired with their ground-truth context"; "The input prompt explicitly provides the ground-truth answer to each question"). The experiment cannot test that contextual use generalizes to new prompts (criterion 2: evaluation on the training inputs of the proposed term). The table shows no held-out result. | Split the forget questions/contexts into train and held-out halves, train the term on one, evaluate on the other plus new templates and paraphrases; report with seeds | New data/experiments |

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §5; App. A.4 | Epoch and λc selected on the reported metrics: "select the one with the highest Contextual QA score (LLM-Judge) and model utility jointly". The chosen λ gives Table 2. TOFU has no validation split. Per the decision table, A.4 says other λ "also work well", which supports the claim at other values (so MAJOR, not CRITICAL, for this issue alone) | Fix choices on a validation subset; show all λ |
| DA-M2 | Logic | §3, §4.1, App. A.3 | The mechanism ("this penalty propagates into inference-time conditioning"; "causing contextual collapse") is asserted but untested; no retain-entity control, no original-model row | Retain-entity contextual QA; activation analysis; soften wording |
| DA-M3 | Scope | Abstract, §1 | "Extensive experiments", "a practical, general augmentation": three of six methods, one benchmark, two models, one seed; no RAG pipeline | Narrow or extend |
| DA-M4 | Evidence | Table 2, §5, App. A.2.1 | "marginal and largely neutral": NPO Direct LLM-Judge +0.06 on both models, RMU Gemma Direct ROUGE-L 0.04→0.13; UNDIAL under-unlearns (comparison at unequal forgetting) | Match forgetting strength; report against retrain-on-retain |
| DA-M5 | Ethics/Logic | §2.2, §6.2 | Conditional behavior (answer with context, wrong without) is evidence of suppressing, not removing; leakage under answer-free or partial contexts is untested | Add controls |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | §5 vs Table 2 | "about 17% and 10%" vs recomputed 0.14 and 0.09 |
| DA-m2 | Citation | §3 | "TOFU (Touvron et al., 2023)" |
| DA-m3 | Presentation | Table 4 caption | Duplicates Table 3's caption |
| DA-m4 | Evidence | Table 2 | Qwen UNDIAL contextual LLM-Judge delta printed +0.02 but 0.98 − 0.97 = 0.01 (rounding of underlying values cannot be excluded) |
| DA-m5 | Evidence | A.3 (GD) | The printed GD loss has the sign pattern of an objective to maximize while §4.1's L(w) is minimized; may be an extraction artifact (unverifiable) |

### Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Gemma contextual LLM-Judge, vanilla avg | 0.54 | (0.81+0.00+0.82)/3 = 0.543 | Yes |
| Gemma, context-aware avg | 0.98 | (0.98+0.99+0.98)/3 = 0.983 | Yes |
| Qwen vanilla avg / context-aware avg | 0.62 / 0.97 | 0.62 / 0.967 | Yes |
| Gemma utility change | −0.7% | (0.00−0.03+0.01)/3 = −0.007 | Yes |
| Contextual gain NPO and UNDIAL "about 17% and 10%" | 17%, 10% | NPO mean(0.17, 0.11) = 0.14; UNDIAL mean(0.16, 0.02) = 0.09 | No |
| Direct ROUGE-L shift Gemma | 5 pp | (0.05+0.09+0.01)/3 = 0.05 | Yes |
| Direct LLM-Judge shift overall | ~2 pp | (0.06+0.01−0.01+0.06+0.01+0.01)/6 = 0.023 | Yes |
| RMU below 0.05 (intro) | "below 0.05" | Qwen vanilla prints 0.05 | Minor mismatch |

### Ignored Alternative Explanations
- The model learned a template switch or memorized the forget (q, c) pairs (train/eval overlap).
- Differences in vanilla contextual preservation reflect how much each method forgets, not objective type (UNDIAL under-unlearns).
- General collapse of generation under the prompt format, not forget-specific suppression.
- Selection effect: best epoch of 20 with ε = 0.01 and no smoothing.

### Missing Stakeholder Perspectives
Data subjects whose information was removed (the fix makes forgotten facts recoverable from any prompt that contains them); operators who need a "no answer from memory" guarantee; users of RAG systems with conflicting or poisoned context.

### Observations (Non-Defects)
The averages in §1 are internally consistent with Table 2; the paper reports selection rules openly; the contextual setting is well motivated; and the case studies are candidly shown, including failures of the baselines.

### Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 45 | DA-C1, DA-M1 |
| Clarity & Presentation | 66 | Clear |
| Novelty & Originality | 50 | Incremental method |
| Significance & Impact | 55 | Relevant scenario, thin proof |
| Experimental Validation | 36 | Train/eval overlap, selection, single run |
| Reproducibility | 55 | No code, seeds |
| Ethical Compliance | 62 | Conditional-forgetting risk undiscussed |

**Pool position:** better than about 48% of ICLR submissions. Deciding evidence: the main result is measured on training prompts.
**Overall: 3 | Confidence: 4**

---

# Phase 1.5: Literature Check (summary)

Mode strict, cutoff 2025-09-24; 6 of 12 queries used (5 claim, 1 baseline), 39 unique kept results (11 prior peer-reviewed, 13 prior arXiv-only, 9 recent preprints, 6 concurrent); no text overlap and no result at novelty level 5. One uncited related prior work (Takashiro et al., ACL Findings 2025) is listed under Missing References; no Critical missing reference was found. The search was arXiv-only and cannot show absence of related work.

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 (single run, narrow scope, judge) | rewritten and ordered last | Four distinct points; severity below W1–W4 |
| R2 | W3 (breadth outruns benchmark) | kept, shortened | Overlaps R4-W1 and DA-M3; classified CONSENSUS |
| R2 | Question about retain baseline | kept as question | Low confidence, `[verify]` |
| R3 | W3 (λc practicality) | merged with R1-W2 | Same underlying selection issue |
| R4 | W3 limitations | moved to Minor line in package | Cosmetic relative to W1 |
| DA | DA-m4, DA-m5 | kept under Minor; DA-m5 flagged "unverifiable (extraction)" | Hard Rule 10 |
| All | Appendix answers? | none dropped | Searched: no held-out split, no seeds, no retain-entity control anywhere in the appendix |

Scores were not changed.

# Phase 2: Synthesizer Package (Part A)

| Issue | Sources | Class |
|-------|---------|-------|
| Contextual QA evaluated on training prompts | R1-W1, R4-W1 (partly), DA-C1 | DA-CRITICAL (CONSENSUS-3 in substance) |
| Selection of epoch / λc on reported metrics | R1-W2, R3-W3, DA-M1 | CONSENSUS-3 |
| Narrow scope, single run, "extensive" overclaim | R1-W5, R2-W3, R4-W1, DA-M3 | CONSENSUS-4 |
| No retain-entity / original-model control; mechanism asserted | R1-W3, DA-M2, R4-W2 | CONSENSUS-3 |
| Forgetting not matched; "marginal" Direct QA shifts | R1-W4, DA-M4 | CONSENSUS-2 |
| Conditional forgetting / leakage under partial context | R3-W1, R2-W2, DA-M5 | CONSENSUS-3 |
| Realistic RAG contexts untested | R3-W2, R2-W3 | CONSENSUS-2 |
| Missing context-conditioned unlearning citation | R2-W2 | SOLO |
| Numerical and citation slips | R1 ERR-3, ERR-4; R2 ERR-5; R4-W2; DA-m1, DA-m2 | CONSENSUS-3 (minor) |

Hinges for the outcome: DA-C1 and the selection issue. Official output of the first aggregation run (no EIC weights, DA-C1 provisionally upheld) is in `before.json`.

---

# Editorial Decision

## Paper: Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: Empirical
## Review Team (fictional personas): EIC Prof. Helena Marchetti-Okafor; R1 Methodology Dr. Tomasz Reinholt; R2 Domain Prof. Mei-Ling Sato-Rao; R3 Perspective Dr. Kwame Adjei-Lindgren; R4 Generalist Dr. Priya Venkataraman; DA Dr. Rafael Echeverría-Holt

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40
**Official composite** 57.1 (before EIC weights) · **EIC assessment** (internal): weighted rating 3.36 → starting point 3 · weighted composite 56.6 → band 3 (cross-check agrees, no ⚠) · **DA ceiling**: 3 (DA-C1 upheld, needs new experiments) · **Final (EIC): 3**. ICLR label for the final decision: "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" (scale status: secondary); ICLR sub-scores Soundness 2, Presentation 3, Contribution 2.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** The paper names a real, easily understood blind spot in unlearning evaluation (the model must still read evidence placed in the prompt), shows it across six methods, and offers a simple plug-in term whose headline averages reproduce from Table 2 (0.54→0.98 on Gemma; 0.62→0.97 on Qwen). The framing is useful for compliance and RAG settings and the paper is well written.
- **Against acceptance:** The positive result for the method is measured on the same (q, c) prompts the term is trained on, and epoch and λc are chosen on the reported metrics. There are no seeds, one benchmark of fictitious authors, two models, three of six methods extended, no retain-entity control and no test of whether the fix reopens leakage. Claims ("extensive", "general", "near original levels") exceed the evidence.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Training pairs of the context term are the evaluation prompts | DA-C1, R1-W1 | §4.2, §3, §5, Fig. 3 vs Fig. 5/Table 1 | Verified | §4.2 "denotes the forget examples paired with their ground-truth context"; §5 "same datasets ... as described in Section 3"; Fig. 3 bottom example equals Fig. 5 and Table 1 example. No held-out split described in the appendix either. Table 4 gives one out-of-training probe (one example), so the overlap is not total evidence-free |
| Selection on reported metrics | R1-W2, DA-M1, R3-W3 | §5, App. A.4 | Verified | Quote found in A.4. Chosen λ is the highest-scoring one among those within δ, and gives Table 2. A.4 states other λ "also work well", Fig. 9 unseen, so the claim at other λ is plausible; MAJOR |
| "about 17% and 10%" | R1 ERR-3, DA-m1, R4-W2 | §5 vs Table 2 | Verified | Recomputed 0.14 and 0.09 |
| TOFU mis-citation | R2 ERR-5 | §3 vs References | Verified | Touvron et al. 2023 is the Llama 2 entry |
| NPO Direct shifts not "marginal" | R1-W4, DA-M4 | Table 2, §5 | Partly correct | +0.06 on both models equals δ; the average statement itself (about 2 pp) is correct |
| No retain-entity control, no original row | R1-W3, DA-M2, R4-W2 | §3, Table 2 | Verified | Not stated after search. Mechanism claims are untested; the diagnosis (C1) itself still holds for the forget set |
| Leakage under answer-free/partial contexts untested | R3-W1, DA-M5 | §3, §5, §6.2 | Verified (as an omission) | Raised as a question; no evidence either way |
| GD loss sign (A.3) | DA-m5 | App. A.3 | Unverifiable | Likely extraction or sign-convention artifact; not counted |
| Missing context-conditioned unlearning reference | R2-W2 | §2.2 | Verified | Takashiro et al. is peer-reviewed prior to the cutoff and uses TOFU; discussion, not a required comparison |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Central points (overlap, selection) verified at their locations; rating matches the evidence; error log held up (ERR-1 to ERR-4) |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; citation catch verified; literature addendum accurate; the novelty verdict is somewhat conservative but within bounds |
| R3 (Perspective) | 4 | 3 | 1.0 | Constructive points verified as omissions; rating did not account for the train/eval overlap, which is a role feature, not a flaw |
| R4 (Generalist) | 4 | 4 | 1.0 | Fair clarity and venue judgment; numeric slips verified; leans accept despite the evaluation gap |
| DA | 3 | 4 | 1.0 | DA-C1 verified; a few counter-argument points (template switch, memorization) are plausible but untested by the DA, so no extra weight |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes. The method's main evidence (Table 2) is scored on the inputs the context term is trained on, so it cannot show that supplied-context use generalizes, which is the claim. Even with every other item fixed, the paper would still lack the experiment that tests C2. Meets criterion 2 | **Upheld** | New data/experiments (held-out contexts/questions, new templates) |

I considered downgrading because the vanilla failure (C1) is real and Table 4 shows novel contexts working on one example. I did not, because Table 4 is a single hand-picked example, and the quantitative table is the evidence the abstract cites. The cap is 3.

### Final Decision and Justification
The reviewers' ratings (3, 3, 4, 4, 3) give an EIC-weighted rating of 3.36, so the starting point is 3 (Borderline Reject). The composite cross-check (56.6, band 3) agrees with the rating, so there is no disagreement to explain. The upheld DA-C1 requires new experiments, so the ceiling is Borderline Reject (3), and the final decision is 3, equal to the ceiling and to the starting point. My own pool position is **better than about 50% of ICLR submissions**: the diagnosis is a real contribution, but a typical rejected submission is one whose main claim is not tested by its experiments, which applies to C2 here; the accepted-paper pattern (clear idea plus evidence across settings with strong baselines) is only half met. The accept-leaning ratings (R3, R4) rest on clarity and relevance and did not account for the overlap and selection; they are not wrong, but they are not enough to move the decision. The paper is a good candidate for a resubmission with held-out evaluation, seeds, a retain control and a second benchmark.

---

## Score Summary

### Official Scores and EIC Assessment
See `aggregate.json` for the exact script output (venue: ICLR, `--final 3`). Dimension scores per reviewer:

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) |
|-----------|----|----|----|----|----|---------------------|
| Technical Rigor | 50 | 58 | 63 | 62 | 45 | 55.6 |
| Clarity & Presentation | 66 | 68 | 72 | 72 | 66 | 68.8 |
| Novelty & Originality | 52 | 55 | 62 | 60 | 50 | 55.8 |
| Significance & Impact | 55 | 58 | 68 | 64 | 55 | 60.0 |
| Experimental Validation | 40 | 50 | 56 | 55 | 36 | 47.4 |
| Reproducibility | 55 | 58 | 60 | 62 | 55 | 58.0 |
| Ethical Compliance | 65 | 65 | 62 | 66 | 62 | 64.0 |

| **Composite** | 52.6 | 57.7 | 62.7 | 62.0 | 50.2 | **57.1 (before)** | **56.6 (after, EIC-weighted)** |

Official rating (plain mean of Overall): 3.40. EIC-weighted rating: 3.36 (weights R1 1.25, others 1.0, each times confidence). `before.json`: composite 57.1, suggested Overall 3, DA cap 3. `aggregate.json` (`--final 3`): ICLR Soundness 2 / Presentation 3 / Contribution 2; ICLR rating label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})". No consistency warnings were raised.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models" to ICLR. The paper addresses an under-examined question: whether a model that has unlearned a fact can still use it when it is supplied in the prompt.

**Overall Assessment:** The panel found the question well motivated and the paper clearly written. Reviewers agreed that the observed contextual failure of several unlearning methods is a useful finding. The panel's main reservation is about whether the evidence shows that the proposed context-aware term generalizes beyond the prompts it is trained on.

**Key Strengths Identified by Reviewers:**
1. A new, practically motivated evaluation axis and a method-agnostic framing (R1, R2, R3, R4).
2. A simple plug-in objective with consistent gains in Table 2 and internally consistent headline averages (R1, R4).
3. Clear exposition and instructive case studies (R3, R4).

**Key Concerns Requiring Attention:**
1. Contextual QA is evaluated on the same forget questions and gold contexts used to train the context term; no held-out split (R1, R4, DA; CONSENSUS).
2. Epoch and λc are selected on the reported metrics, with no seeds (R1, R3, DA; CONSENSUS-3).
3. Narrow scope: one fictitious-data benchmark, two models, three of six methods extended; no retain-entity or original-model control; mechanism asserted (R1, R2, R4, DA; CONSENSUS-4).
4. Whether the fix reopens leakage, and how the conditional behavior relates to removal, is not tested (R2, R3, DA).

**Critical Challenge (Devil's Advocate):** The method's central evidence tests the fit of the model on its training prompts; it must be shown on held-out questions, contexts and templates.

**Decision: Borderline Reject (3).** The paper is close to the bar on motivation and clarity, but the main positive claim is not yet tested by the experiments. A revision with a held-out evaluation, a validation-based selection protocol, seeds, retain-entity controls and a second benchmark would likely change the assessment materially. This is a simulation of how a careful panel might see this draft, not a prediction of any real outcome.

Sincerely,
Prof. Helena Marchetti-Okafor, Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|----------------|
| Narrow scope, single run, "extensive/general" overclaim | R1, R2, R4, DA | CONSENSUS-4 |
| Selection of epoch/λc on reported metrics | R1, R3, DA | CONSENSUS-3 |
| Overlap of training and evaluation prompts | R1, R4, DA | CONSENSUS-3 (as DA-CRITICAL) |
| Missing controls (retain entities, original-model row), mechanism asserted | R1, R4, DA | CONSENSUS-3 |
| Leakage / conditional forgetting untested | R2, R3, DA | CONSENSUS-3 |
| Numerical and citation slips | R1, R2, R4, DA | CONSENSUS-4 (minor) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the evidence enough for a borderline accept? | R3, R4 | R1, R2, DA | The overlap and selection issues were verified and the accept-leaning ratings did not account for them; ratings weighted accordingly |

### Score Spread Discussion
Experimental Validation (36 to 56, spread 20) is at the flag threshold; it follows how much weight each reviewer put on the train/eval overlap. The EIC adopts the lower view because the overlap was verified. Pool positions span 45 to 68 (23 points); the evidence behind the gap is the overlap, ruled on above.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Evaluation on training prompts | Yes (R1-W1; R4-W1 partly) | Upheld | New data/experiments |
| DA-M1 | MAJOR | Selection on reported metrics | Yes (R1-W2, R3-W3) | n/a (MAJOR, row "main claim holds at other λ" per A.4) | n/a |
| DA-M2 | MAJOR | Mechanism and control missing | Yes (R1-W3) | n/a | n/a |
| DA-M3 | MAJOR | Scope overclaim | Yes (R2, R4) | n/a | n/a |
| DA-M4 | MAJOR | Forgetting not matched | Yes (R1-W4) | n/a | n/a |
| DA-M5 | MAJOR | Conditional forgetting | Yes (R3-W1, R2-W2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Contextual QA scored on the training prompts of the context term | DA-C1, R1-W1, R4-W1 | §4.2, §3, §5, Table 2 | Held-out split of forget questions/contexts; new templates and paraphrases; report with seeds | Medium; about 30–60 A100-hours | Yes (Gemma-2B first) |
| R2 | Epoch and λc selected on reported metrics | R1-W2, DA-M1, R3-W3 | §5, App. A.4 | Validation subset; pre-fixed protocol; show all λ and epochs with seeds | Medium | Yes |

### Priority 2: Strongly Suggested
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No retain-entity or original-model contextual control; mechanism asserted | R1-W3, DA-M2 | Add rows and retain-entity prompts; probe or soften §4.2, A.3 | Low–Medium | Yes |
| S2 | Forgetting not matched; "marginal" claim | R1-W4, DA-M4 | Report vs retrain-on-retain; trade-off curves | Medium | Yes |
| S3 | Leakage under answer-free, partial, distractor contexts; relearning | R3-W1, R2-W2, DA-M5 | New controls on vanilla and context-aware models | Medium | Partly |
| S4 | Scope: second benchmark (e.g., MUSE), 1% and 10% on Qwen, all six methods or narrow "general", seeds, judge agreement | R1-W5, R2-W3, R4-W1, DA-M3 | Extend or reword | High | Partly |
| S5 | Ablate KL against SFT on (q, c) → a and retain-style contextual data | R2-W1 | Add ablation | Low–Medium | Yes |
| S6 | Related work: context-conditioned unlearning (Takashiro et al.), Lynch et al. | R2 | Discuss | Low | Yes |
| S7 | Realistic RAG contexts (noisy, multi-document) | R3-W2 | Add retrieval test | Medium | Partly |

### Priority 3: Nice to Fix
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | "about 17% and 10%" vs Table 2 | R1 ERR-3, DA-m1 | Correct to 14% and 9%, or define the quantity |
| N2 | TOFU cited as Touvron et al., 2023 | R2 ERR-5 | Cite Maini et al., 2024 |
| N3 | Table 4 caption duplicates Table 3; "below 0.05" vs 0.05 | R4, DA-m3 | Fix |
| N4 | Add a limitations paragraph; clarify "rewards correct responses" for a KL term | R4, R2 | Rewrite |
| N5 | Check the GD loss sign in App. A.3 and the +0.02 delta (Qwen UNDIAL) in Table 2 | DA-m4, DA-m5 | Verify (unverifiable from extraction) |

## Estimated Revision Effort
- Priority 1: 2 items, about 1–2 weeks including compute.
- Priority 2: 7 items, about 2–4 weeks.
- Priority 3: 5 items, under 1 day.
- **Total estimated revision time**: roughly 3–5 weeks.

*Gap Scout (post-review analysis) was not requested and was not run.*
