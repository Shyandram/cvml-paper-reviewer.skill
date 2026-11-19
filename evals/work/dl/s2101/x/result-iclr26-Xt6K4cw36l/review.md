# Simulated ICLR Review — "Prompt reinforcing for long-term planning of large language models"

*Simulation, not a prediction: this is how a careful panel would likely see this draft. Date: 2026-11-10. Mode: full, venue ICLR, literature check requested as strict (cutoff 2025-09-24). Figures were not available (text extraction only); figure-dependent points are judged from captions and extracted labels and marked as such. The five reviewer passes were run one after another in a single shared context (no delegation), so they are role-based perspectives, not independent agents.*

---

# Phase 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Prompt reinforcing for long-term planning of large language models |
| Primary Discipline | NLP / LLM agents → automatic prompt optimisation for multi-turn interaction |
| Secondary Discipline(s) | Task-oriented dialogue systems; reinforcement learning (TD learning, experience replay); text-to-SQL; medical QA |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | LLM feedbacker + LLM rewriter that edit a system prompt from natural-language feedback; turn-level "temporal-difference-style" feedback; replay of past (prompt, feedback) pairs |
| Target Venue | ICLR (stated by the user); profile key `iclr`, 2026 cycle, accepted share about 27% of submissions |
| Venue-Specific Notes | none (ICLR; reviews are public and a revised PDF may be uploaded during discussion) |
| Paper Maturity | Submission-ready ("Preprint. Under review.") |
| Ethics-Relevant Content | Medical-advice generation (general medicine and traditional Chinese medicine) with human-expert evaluation; LLM-simulated users; LLM-generated data. No personal data. |

### Claimed Contributions (as stated by the authors, §1)
1. **C1:** RPO, "a meta-prompting framework that improves LLMs' long-term planning in multi-turn tasks by iteratively updating prompts based on natural language feedback" (§1, §3).
2. **C2:** TD-error-inspired turn-level feedback and experience replay in the rewriter, "enabling efficient and lower-variance prompt optimisation" (§1, §3.1–3.2, §5.2).
3. **C3:** The method "can leverage external expert reward signals without revealing the prompt" and is "flexible with respect to the choice of LLM backbones" for system and meta-prompting agents (§1, Tables 1–2, §5.3).
4. Implicit claims made elsewhere: lower serving cost and latency than self-refine pipelines (§3 intro, §6), and generalisation or robustness across agents (abstract, §5.1).

### Paper memory (factual record, shared with all reviewers)

| Item | Record (location) |
|------|-------------------|
| Tasks | Text-to-SQL: sharded Spider from Laban et al. (§4.1, Table 1), five system LLMs, functional accuracy. Task-oriented dialogue: MultiWOZ 2.1 via ConvLab-3, attraction/hotel/restaurant/train, system FnCTOD on GPT-4o mini, rule-based success rate (§4.1, Table 2). Medical QA: Huatuo-26M and ShenNong-TCM questions, GPT-4o mini system, pairwise expert preference (§4.1, §5.3, Fig. 5). |
| Optimisation loop | Feedbacker sees 10 interactions per epoch; rewriter generates 2 candidate prompts; the one with "the highest score on the validation set" is kept (§4.3). Rewriter output capped at 512 tokens (Figs. 7–8). About 100 dialogues per epoch (300 dialogues at epoch 3, App. B); Fig. 12 prompt is after 8 epochs. |
| Baselines | APO (binary success label), GPO (numeric score), MC-style / TextGrad (whole-dialogue textual feedback), plus unoptimised BaselineSharded and OracleFull (§4.3, Table 1). Replay is not stated to be applied to any baseline. |
| Headline numbers | Table 1 mean: 0.333 → 0.477, "+54.2%"; Oracle 0.743. Table 2: 0.420 → 0.619, "+47.3%". Fig. 5a: 86.7% win rate against HuatuoGPT-II in general medicine. |
| Seeds / sample sizes | Fig. 4 and Fig. 6: 4 seeds, "evaluated on 100 dialogues", standard error shown, for FnCTOD only. Tables 1–2: seeds, number of evaluation dialogues/instances, and train/validation/test split not stated after search (no occurrence of "test" or "split" in the body). Medical: 3 experts × 30 pairs per domain = "90 per domain" (§4.1). |
| Not stated | Which LLM acts as feedbacker/rewriter in Table 1; whether baseline/oracle rows in Table 1 are re-run or copied; user-simulator LLM; compute, token or API-call cost of optimisation or inference; number of epochs for tables; which epoch's prompt is reported. |
| Appendix | A: model versions (Table 3). B: training curves for four more LLMs (Fig. 6) plus a note on non-determinism. C: prompts for rewriter, feedbackers, FnCTOD before/after (Figs. 7–12). Code "will be released when this work is published" (Reproducibility Statement). |
| Unverifiable here | Figs. 4a/4b/6 curves and Fig. 4b ablation values (images not available); Fig. 5 bar order read from extracted labels (some labels garbled). |

**Integrity scan** (`integrity_scan.py`): no reviewer-directed text or hidden characters found. Reviewers read the (unchanged) redacted copy.
**Literature check:** requested as *strict* with cutoff 2025-09-24. The arXiv API returned HTTP 429 on both attempts (2 of 12 queries tried, 0 results). Per `literature_search.md` the phase falls back to `literature check: off`: no claim-level novelty profile, baseline scout or similarity run could be produced, and every recommended reference below is from knowledge and marked `[verify]`.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Halvard Meissen-Ortiz, senior faculty, public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty, former area chair / dialogue systems, LLM agents, evaluation methodology
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR actually accepts; weights reviewers by what they got right.

### Reviewer 1 (Methodology): Dr. Kenji Arakawa-Lindt, mid-career, industrial research lab (East Asia)
- **Seniority / Expertise**: Mid-career / prompt-optimisation evaluation, LLM-as-optimizer, experimental design for LLM agents
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched budgets and information access across baselines; recomputes every table.

### Reviewer 2 (Domain): Dr. Marisol Quispe-Valdés, senior faculty, large public university (South America)
- **Seniority / Expertise**: Senior faculty / task-oriented dialogue, RL for dialogue policy, text-to-SQL
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work first; asks what exactly differs from the closest method.

### Reviewer 3 (Perspective): Dr. Anders Thorvaldsen-Bell, associate professor, human–computer interaction group (Northern Europe)
- **Seniority / Expertise**: Associate professor / user simulation, human-centred evaluation, clinical decision support
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for what the idea could become.

### Reviewer 4 (Generalist): Dr. Fatou Mbengue-Hart, mid-career, ML department, private research university (North America)
- **Seniority / Expertise**: Mid-career / representation learning and NLP, typical programme-committee member, not a prompt-optimisation specialist
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Asks whether a non-specialist can follow it and whether ICLR readers would care.

### Devil's Advocate: Dr. Ruslan Okonkwo-Vale, senior industry scientist, evaluation and causal-inference team (Western Europe)
- **Seniority / Expertise**: Senior scientist / causal inference for ML evaluation, ablation design
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks what else could explain the result.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1 — Independent Reviews

## Reviewer 1 (Methodology)

# Peer Review Report

## Paper: Prompt reinforcing for long-term planning of large language models
## Reviewer: Dr. Kenji Arakawa-Lindt, Methodology (industrial research lab, East Asia; fictional persona)
## Expertise: prompt-optimisation evaluation; LLM-as-optimizer; experimental design for LLM agents
## Date: 2026-11-10

### Protocol sweep and omission sweep (summary)
Search of the full text, appendix included, for `test`, `split`, `validation`, `held-out`, `seed`, `epoch`, `selected`, `best`:
- Selection: "the one with the highest score on the validation set (based on automatic metrics or human experts…) is chosen for the next iteration" (§4.3). A validation set exists for candidate selection. **Which split the Table 1/2 numbers come from, and how large it is: not stated after search.** No sentence says anything was tuned on the reported split, so no leakage claim is made.
- Seeds/variance: present for Fig. 4 and Fig. 6 (4 seeds, 100 dialogues, standard error); not stated for Tables 1–2, Fig. 5.
- Baseline settings: baseline implementations described in a sentence each (§4.3); whether they use the same feedbacker inputs, number of candidates, epochs and selection rule: not stated.
- Compute / cost: not stated after search. Code: promised only (Reproducibility Statement). Model versions: present (Table 3).

### Claim-to-evidence map

| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|--------------|---------------------|---------|
| C1 | RPO improves multi-turn success by prompt rewriting | Abstract, §1 | Tables 1–2 (all rows above Baseline), Fig. 5 | Supported on these three tasks, single settings |
| C1' | improvement is due to "long-term planning" | Abstract, §1 | No planning-specific metric; Fig. 12 shows slot-tracking and API-validation rules | Unsupported as worded |
| C2a | TD-style feedback beats MC-style | §5.1–5.2 | Table 1: 0.408 vs 0.388; Table 2: 0.575 vs 0.565; Fig. 4a: "their final performances become comparable" | Partially (gap 0.010–0.020, no variance) |
| C2b | Replay gives the best result and stability | §5.1–5.2 | RPO_TD+replay vs RPO_TD: +0.069 (T1), +0.044 (T2) | Supported, but baselines get no replay |
| C2c | "efficient" | §1, §6 | No cost, latency or call count anywhere | Unsupported |
| C3 | Works with many system and meta LLMs | §5.1 | Table 1 varies the system LLM; Table 2 varies the meta-prompting LLM; never crossed | Partially |

### Summary
The paper proposes RPO, an iterative loop in which an LLM feedbacker critiques multi-turn dialogues turn by turn, an LLM rewriter edits the system prompt, and the rewriter can see earlier (prompt, feedback) pairs. It is evaluated on sharded text-to-SQL, MultiWOZ task-oriented dialogue and two Chinese medical QA sets, against APO, GPO and a whole-dialogue "MC-style" feedbacker. Success improves in every setting against these baselines, with the largest gains from the replay variant.

### Strengths
**S1: Diverse tasks and backbones.** Three task families, five system LLMs (Table 1) and five meta-prompting LLMs (Table 2), including open-weight models, make the effect unlikely to be a one-model artefact. Exact model versions are listed (Table 3).

**S2: Useful ablation of feedback inputs and honest limitation analysis.** §5.2 / Fig. 4b varies the information given to the feedbacker (dialogue only, plus user goal, plus API call), and §5.1/§5.3 openly report the gap to OracleFull (0.477 vs. 0.743) and weaker traditional-Chinese-medicine results.

**S3: Variance is shown at least for the training curves.** Fig. 4 and Fig. 6 report four seeds with standard error, and App. B states that LLM non-determinism "causes unavoidable variance", which is more than most prompt-optimisation papers show.

**S4: Concrete artefacts.** The before/after prompt (Figs. 11–12) and all meta-prompts (Figs. 7–10) are printed, so the method is reproducible in principle.

### Weaknesses

**W1: The gain is attributed to TD-style feedback, but the data point to replay, which baselines do not receive; feedbacker inputs may also differ.** RPO_TD alone beats the MC-style baseline by 0.020 (Table 1: 0.408 vs. 0.388) and 0.010 (Table 2: 0.575 vs. 0.565); §5.2 says "their final performances become comparable". Adding replay adds 0.069 (Table 1) and 0.044 (Table 2). Replay (Eq. 5) is orthogonal to the feedback style and could be attached to APO, GPO and MC-style, but no such row exists. In addition, Fig. 10 gives the TD feedbacker the user goal and the API call per turn, while the MC prompt (Fig. 9) names only "user goals" and the dialogue, and APO/GPO receive a binary or numeric label (§4.3); §5.2 states that "Both the user goal and the API call are essential".
- **Suggested Fix**: add MC-style+replay, APO+replay and GPO+replay rows, and give every feedbacker the same inputs (user goal, API calls) with the same number of candidates, epochs and rewriter context. About 3 methods × 5 LLMs × 4 seeds × 8 epochs on the dialogue task (API cost, no GPUs).

**W2: Tables 1–2 carry no sample size, seed count or interval, and differences among baselines are about 0.01–0.02.** The number of evaluation dialogues/instances and the split are not stated; the only stated size is "evaluated on 100 dialogues" in the Fig. 4 caption, where a success rate near 0.5 has a binomial standard error of about 0.05 (derived). Table 2 baselines span 0.552–0.565, and the claimed RPO_TD advantage over MC is 0.010. "Significant improvement" (abstract) is never tested.
- **Suggested Fix**: state evaluation sizes and splits; report mean ± s.d. over at least 3 seeds per cell, or paired bootstrap CIs over dialogues. Low effort for the text, medium for reruns.

**W3: Protocol details needed to interpret Table 1 are missing.** The LLM acting as feedbacker/rewriter in Table 1 is not named (§4.2 says only that they are built with closed- or open-source LLMs "More detail is shown in Table 3", which lists models, not roles). It is not said whether BaselineSharded and OracleFull are re-run or taken from Laban et al. (they are labelled with the citation), which epoch's prompt is reported, or which LLM simulates users in §4.1.
- **Suggested Fix**: add a protocol table (role per LLM, user simulator, epochs, candidates, selection rule, split, evaluation N), and state whether baseline rows were re-run under the same decoding settings.

**W4: Efficiency and cost claims have no measurement.** §3 says the approach "reduces serving costs and latency by lessening the need for a multi-agent-style feedback and rewriting pipeline", and §6 claims "reducing computational overhead and API call frequency during inference" and an "efficient approach". No self-refine baseline (Reflexion, LLM-augmenter) appears in any table, and the optimisation cost of RPO (per-turn feedback calls plus replay context growing every epoch) is not reported.
- **Suggested Fix**: report tokens and API calls for optimisation and per-dialogue inference for RPO, APO, GPO, MC and one self-refine baseline, or drop the efficiency claim.

**W5: Human evaluation is small and under-described.** §4.1: three experts compare "30 interaction pairs in general medicine and 30 in traditional Chinese medicine per expert (90 per domain in total)". No inter-rater agreement, blinding or significance test is given, and the same kind of expert who supplies training feedback ("provides feedback on 10 interactions", §4.1) may overlap with evaluators. In Fig. 5a the margin against GPO is 40.0% win vs. 26.7% lose; a sign test on 36 vs. 24 non-tied of 90 gives p ≈ 0.12 (derived).
- **Suggested Fix**: report agreement (e.g. Krippendorff's α), blinding, rater overlap, and a sign test with CIs.

**Minor**: §5.1 text says "+54.2% over BaselineSharded" for the average score, whereas Δ% is the mean of per-LLM relative gains (see ERR-1); "believe setting" (§5.2) is presumably "belief"; Fig. 5 order of segments should be stated in the caption; code is promised rather than released.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | §5.1 vs Table 1 | "an average score of 0.477 (+54.2% over BaselineSharded" | The average score rises from 0.333 to 0.477 = +43.2%. The printed +54.2% is the mean of per-LLM relative gains (e.g. Llama-8B 0.224→0.467 = +108.5%, Llama-4 0.206→0.383 = +85.9%), not the gain of the average | Recomputed all rows; the per-LLM mean gives 54.0, matching the printed value within rounding | High (computation), Medium (it is a labelling issue, since the caption defines Δ%) | MINOR | Say "mean per-LLM relative gain" and also report +43.2% |
| ERR-2 | E1 | §5.1 (Table 2 paragraph) vs Table 2 | "Our proposed methods consistently surpass these baselines." | On Llama-70B, RPO_TD is 0.556, below MC-style 0.572 and APO 0.560 | Cross-referenced Table 2 column by column | High | MINOR | Write "surpass on four of five meta-LLMs" |
| ERR-3 | E6 | §4.1 vs Fig. 5b | "(90 per domain in total)" | TCM percentages (42.4, 30.3, 27.3, 51.5, 21.2, 45.5, 24.2) are multiples of 1/99, not 1/90 (e.g. 51.5% × 90 = 46.4, not an integer) | Derived from printed percentages; figure labels read from extracted text | Medium | MINOR | State the real number of pairs in TCM |

### Questions for Authors
1. Do APO, GPO and MC-style receive the same inputs (user goal, API calls), candidates per epoch and rewriter context as RPO? Would adding replay to them close the gap? (Raises my score if the gap persists; lowers it if it closes.)
2. What are the evaluation sizes and splits behind Tables 1–2, and how many runs does each cell come from?
3. Which LLMs are feedbacker and rewriter in Table 1, and were the Baseline/Oracle rows re-run?
4. What is the cost (calls, tokens) of optimising and serving with RPO versus Reflexion-style loops?

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains are real in direction, but attribution and statistics are weak (W1, W2) |
| Clarity | 3 | Method and prompts are clear; protocol gaps (W3) |
| Significance | 2 | Moderate: gains over weak, un-replayed baselines |
| Originality | 2 | Feedback-rewrite is established; turn-level feedback and replay are incremental |

### Pool position
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: no variance or sample size for the main tables (W2) and no replay/information-matched baseline (W1); typical rejected-submission signals ("baselines weak… not tuned", "gain over the closest prior work… not shown").

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Mechanism attribution unsupported; Eq. 3 is an analogy, with V(s) "approximated by the previous turn-level feedback" and γ never set (W1) |
| Clarity & Presentation | 62 | Competent | Easy to follow; protocol details missing |
| Novelty & Originality | 50 | Developing | Incremental over APO/TextGrad with history |
| Significance & Impact | 52 | Developing | Useful if the cost story and baselines hold |
| Experimental Validation | 45 | Developing | No variance, unmatched baselines, small human study |
| Reproducibility | 52 | Developing | Prompts and versions given; split, N, roles, epochs missing; code promised |
| Ethical Compliance | 62 | Competent | Brief statement; medical-advice risk only partly discussed |

### Limitations Assessment
**Partially.** §5.1, §5.3 and §6 discuss the gap to the oracle and unseen topics; cost, simulator validity and real-user transfer are not discussed.

### Ethics Review Flag
**No**

### Overall Score
**3 (Borderline Reject)**: A plausible, practically useful idea with consistent gains, but the key comparisons are confounded by replay and feedbacker inputs and the main tables have no variance.

### Confidence
**4**: Tables recomputed; figures not viewable.

---

## Reviewer 2 (Domain)

# Peer Review Report

## Paper: Prompt reinforcing for long-term planning of large language models
## Reviewer: Dr. Marisol Quispe-Valdés, Domain (large public university, South America; fictional persona)
## Expertise: task-oriented dialogue; RL for dialogue policy; text-to-SQL
## Date: 2026-11-10

### Summary
RPO treats the system prompt as a textual parameter. An LLM writes turn-level critiques containing a predicted user emotion, a success forecast and a suggestion, a rewriter edits the prompt, and the rewriter may also read earlier prompts and critiques. The authors position it against single-turn prompt optimisers (APO, GPO, TextGrad) and self-refine agents, and show gains on sharded text-to-SQL, MultiWOZ and medical QA.

### Strengths
**S1: A well-motivated gap.** The multi-turn degradation reported by Laban et al. (cited in §1, §4.1) is a real problem, and §2 correctly notes that APO, OPRO, GPO and TextGrad "focus on single-turn tasks".

**S2: Sensible domain choice.** MultiWOZ with ConvLab-3 and FnCTOD (§4.1) is a standard, reproducible testbed, and the paper correctly observes that API-call correctness is the main failure source (§5.2).

**S3: Clear conceptual link to dialogue literature.** Using next-turn user sentiment as a short-term reward (§3.1, citing Ghazarian et al., 2022) connects to emotion-aware dialogue evaluation in a natural way.

**S4: Honest scoping on under-represented domains.** §5.3 ties weaker TCM results to prompting limits (Petrov et al., 2024), although this is a hypothesis, not a tested explanation.

### Weaknesses

**W1: The closest multi-turn and agent-level baselines are cited but not compared.** The paper claims existing methods work on "single-turn tasks" (§2), yet it cites Agent-Pro (Zhang et al., 2024), which builds policy-level reflections from environment feedback for multi-turn agents, and Reflexion (Shinn et al., 2023); neither is a baseline in Tables 1–2, although the paper's motivation (§1, §3) is the contrast with these pipelines. OPRO and PromptAgent (Wang et al., 2024) are also cited and not run.
- **Suggested Fix**: add at least Reflexion/Agent-Pro (as inference-time self-feedback) and OPRO with a trajectory-aware meta-prompt as baselines in Table 2.

**W2: Novelty of "experience replay" relative to history-conditioned prompt optimisers is not argued.** Eq. 5 conditions the rewriter on all earlier prompt–feedback pairs. §2 describes OPRO only as rewriting "based on a corresponding performance score". To my knowledge OPRO's meta-prompt already includes earlier candidate solutions with their scores [verify], and agent-memory methods such as ExpeL (see Missing References) reuse past experience in context; the delta to these is not stated. This cannot be checked offline (literature search failed), so I record it as a question, not as a defect.
- **Suggested Fix**: add a delta paragraph and a table: what each prior method conditions on (score, textual feedback, history), and an ablation replacing replay with OPRO-style score history.

**W3: The RL vocabulary is analogy, not theory, and the "long-term planning" framing is not tested.** Eq. 3 defines δ_t = r_t + γV(s_{t+1}) − V(s_t), but "V(s_t) is approximated by the previous turn-level feedback" is free text; γ and a value function are never defined and no TD update is performed. There is no measure of planning (turns to success, goal-slot recall over turns, recovery from early errors), and Fig. 12 shows an optimised prompt dominated by slot tracking, API validation and polite closure rules, which is compatible with fixing state-tracking errors rather than improving planning. The sense of "planning" also differs from PromptAgent (Wang et al., 2024), whose planning is over prompt-edit space; this should be disambiguated.
- **Suggested Fix**: measure planning-specific outcomes and test the claim directly, or reword to "multi-turn success" and "RL-inspired".

**W4: The predicted user emotion and success forecast are never validated.** §3.1 treats the LLM's predicted next-turn sentiment as a short-term reward, but no analysis compares predictions with the simulator's actual next utterance or the final outcome, so it is unknown whether the TD-style signal carries information or just structures the critique.
- **Suggested Fix**: report calibration/accuracy of the forecasts, and an ablation removing the emotion and forecast fields (keep only the suggestion).

### Missing References
*Verification could not be run (arXiv API returned HTTP 429); all entries are from knowledge and marked `[verify]`. No identifiers are given.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback", NeurIPS 2023 [verify] | The paper contrasts itself with "self-refine approaches" (§3) without citing it; natural inference-time baseline for the efficiency claim |
| Important | Yao et al., "Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization", ICLR 2024 [verify] | Learns from verbal feedback across episodes for agent prompts, close to RL-inspired prompt updating |
| Important | Zhao et al., "ExpeL: LLM Agents Are Experiential Learners", AAAI 2024 [verify] | Reuses past trajectories and insights in context; related to the replay component |
| Important | Zhou et al., "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL", ICML 2024 [verify] | Turn-level critic with a TD-style objective for multi-turn LLM agents; direct parametric counterpart of the TD analogy |
| Helpful | Khattab et al., "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines", ICLR 2024 [verify]; Opsahl-Ong et al., MIPRO, EMNLP 2024 [verify] | Strong multi-stage prompt optimisers, relevant to FnCTOD's two-prompt pipeline |
| Helpful | Guo et al., "EvoPrompt", ICLR 2024 [verify] | Evolutionary prompt optimisation; candidate-selection protocol comparison |

### Citation check (E7, from the paper's own text, no search)
- OPRO (Yang et al., 2024a) is described only by its performance-score input (§2); see W2 (unverified).
- PromptAgent (Wang et al., 2024) appears in a list of single-turn MC-style methods (§3.1); its "strategic planning" is about prompt-space search, and the label "single-turn" is acceptable but the planning link is unmentioned.
- The sentence "these self-feedback methods rely on frequent API calls since their original prompt is not optimal" (§2) is an assertion, not a cited finding.

### Novelty (knowledge-based claim profile, literature check unavailable)
| Claim | Dimension | Novelty | Closest prior work (unverified) | Reasoning |
|-------|-----------|---------|----------------------------------|-----------|
| C1 prompt rewriting from NL feedback for multi-turn | method | incremental | APO (Pryzant et al., 2023), TextGrad (Yuksekgonul et al., 2025) | Feedback → rewrite is the established loop; multi-turn input is the change |
| C2 turn-level TD-style feedback | method | medium | per-turn critiques in agent reflection [verify] | Structured per-turn sentiment/forecast/suggestion is new in this form; benefit over MC is within noise (R1-W1) |
| C2 replay | method | incremental | history-conditioned meta-prompts (OPRO, ExpeL) [verify] | Delta not argued |
| C3 black-box flexibility | resource/property | not a novelty claim | all black-box optimisers | Expected of the class |

### Field snapshot (from knowledge up to the cutoff, 150–250 words)
Automatic prompt optimisation moved from soft prompts (2021) to black-box LLM-in-the-loop methods: APE (2023), APO/ProTeGi (2023), OPRO and EvoPrompt (2024), DSPy/MIPRO-style program optimisers (2024) and TextGrad (2025). In parallel, agent work added verbal reflection across episodes (Reflexion, Retroformer, ExpeL, Agent-Pro) and parametric multi-turn RL for LLM agents (ArCHer and successors). Multi-turn degradation has become a named problem (Laban et al., 2025). Recent preprints that sit within months of the cutoff (for example reflective prompt-evolution methods such as GEPA [verify]) are "worth discussing", never required comparisons. At this venue a significant contribution in this sub-field now means a gain over strong, budget-matched prompt optimisers with variance reported, a cost story that is measured, or a mechanism that is actually isolated. A 0.01–0.02 gain over TextGrad-style feedback is incremental; a 0.04–0.07 gain from a history-conditioned rewriter is meaningful only if baselines get the same history.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Missing baselines and unvalidated signals |
| Clarity | 3 | Clear positioning |
| Significance | 2 | Moderate |
| Originality | 2 | Incremental over history-aware prompt optimisers |

### Pool position
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental novelty relative to APO/TextGrad/OPRO-style optimisation and no comparison with agent-level multi-turn baselines it cites.

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | TD analogy informal; method otherwise sound |
| Clarity & Presentation | 64 | Competent | Clear writing and figures (from captions) |
| Novelty & Originality | 48 | Developing | Combination of known pieces; delta not argued |
| Significance & Impact | 52 | Developing | Practical for black-box agents |
| Experimental Validation | 48 | Developing | Cited multi-turn baselines not run |
| Reproducibility | 52 | Developing | Prompts printed; protocol gaps |
| Ethical Compliance | 62 | Competent | Statement present; medical caveats thin |

### Questions for Authors
1. How exactly does your replay differ from conditioning the rewriter on scored candidate history as in OPRO? (A clear delta and ablation would raise Novelty.)
2. Can you show that predicted emotion and success forecasts are informative, e.g. correlation with the simulator's realised outcome?
3. Why were Reflexion/Agent-Pro not run, given they are the motivating comparison?

### Limitations Assessment
**Partially.** Novelty limits and baseline coverage are not discussed.

### Ethics Review Flag
**No**

### Overall Score
**3 (Borderline Reject)**: A reasonable engineering recipe for a real problem, positioned against single-turn methods but not against the multi-turn agent methods it cites; novelty is incremental and the TD framing is not tested.

### Confidence
**3**: Dialogue literature known well; prompt-optimisation specifics from memory and the literature search was unavailable.

---

## Reviewer 3 (Perspective)

# Peer Review Report

## Paper: Prompt reinforcing for long-term planning of large language models
## Reviewer: Dr. Anders Thorvaldsen-Bell, Perspective (HCI group, Northern Europe; fictional persona)
## Expertise: user simulation; human-centred evaluation; clinical decision support
## Date: 2026-11-10

### Summary
The paper proposes tuning a system prompt, not model weights, from turn-level natural-language feedback produced by an LLM or a human expert, so that API-only agents can improve over multi-turn interaction. It reports gains for tool-using dialogue, text-to-SQL and a medical-advice setting where human experts both supply feedback and evaluate.

### Strengths
**S1: Practical fit for black-box deployment.** Many practitioners cannot fine-tune; §1 and §6 position the method for API-only models, and Table 1 shows gains for both closed and open models.

**S2: Human experts in the loop.** §4.1 uses a physician-trained expert to give feedback and three experts to evaluate (Fig. 5), a rare and valuable setup in prompt-optimisation work; the paper also shows where it fails (TCM, §5.3).

**S3: Interpretable output.** The optimised prompt (Fig. 12) is human-readable, so a deployer can audit what changed, unlike weight updates.

**S4: Clear separation of roles.** Feedbacker, rewriter and system are separable (Fig. 1), which allows swapping a human for the feedbacker.

### Weaknesses

**W1: Simulated users are assumed to stand in for real users.** Optimisation and evaluation in §4.1 use simulated users (MultiWOZ user goals in ConvLab-3, sharded Spider instructions, LLM-simulated patients). The user-simulator LLM is not named, and prompts are optimised against the same simulator family that scores them, so improvements may reflect adaptation to simulator habits (for example never changing goals mid-dialogue). Connections: sim-to-real work in user modelling for dialogue evaluation, and domain-randomisation ideas from robotics.
- **Suggested Fix**: evaluate the optimised prompts with a different simulator and with a small real-user study; report the simulator LLM.

**W2: Deployment cost and drift are not discussed.** Optimising "in real time" with real users (Fig. 1) implies repeated prompt changes in production. Per-turn feedback calls, growing replay context and the 512-token prompt cap (Fig. 7) all matter for deployment, and prompt drift or regression across epochs is not studied (Fig. 4 shows training curves for one system only in the main text). From control theory: online adaptation needs a safe-update rule (rollback, held-out check).
- **Suggested Fix**: report per-epoch regression on a held-out set, a rollback rule, and costs per epoch.

**W3: Medical advice raises safety questions the Ethics Statement does not address.** The system recommends Chinese medicine or prescriptions (Fig. 3), evaluated on "safety, professionalism, and fluency" combined into one preference (Fig. 5). A prompt that optimises for expert preference could trade safety for helpfulness; safety is not scored separately, and the Ethics Statement only says "datasets should not be regarded as controversial" and that raters knew interactions were LLM-generated.
- **Suggested Fix**: report safety separately, add refusal/escalation behaviour, and state that outputs are not clinical advice.

**W4: The sentiment-as-reward assumption is cultural and linguistic.** The TD-style feedback predicts "user emotion" from a fixed label set (Fig. 10: Neutral, Fearful, …). Whether emotion forecasts are valid for Chinese medical dialogues or terse SQL requests is untested; a connection to affective computing validation practice (against annotated emotion) would help.
- **Suggested Fix**: validate the emotion field on a small annotated sample, per domain.

**Minor**: "believe setting" typo (§5.2); the main-text Fig. 4a covers only Gemini.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound on its own terms; gaps noted by others |
| Clarity | 3 | Readable |
| Significance | 3 | Practical black-box angle |
| Originality | 3 | A fresh combination for dialogue |

### Pool position
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practical, interpretable approach with consistent gains over three baselines on three task families, which most rejected submissions lack; I discount for simulator reliance.

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Sound loop; formalisation informal |
| Clarity & Presentation | 66 | Competent | Clear |
| Novelty & Originality | 60 | Competent | Novel framing for multi-turn |
| Significance & Impact | 66 | Competent | Useful to practitioners with API-only models |
| Experimental Validation | 58 | Competent | Broad, thin statistics |
| Reproducibility | 58 | Competent | Prompts printed; code promised |
| Ethical Compliance | 58 | Competent | Statement exists; medical risk understated |

### Questions for Authors
1. Do the optimised prompts transfer to a different user simulator or to real users? (A positive result would raise Significance.)
2. Is safety, scored on its own, preserved relative to the standard system in Fig. 5?
3. What happens to success if optimisation continues past 8 epochs?

### Limitations Assessment
**Partially.** Simulator dependence and medical-safety limits are missing.

### Ethics Review Flag
**No**: no personal data or human subjects beyond expert raters; the medical-advice framing deserves a safety paragraph but not an ethics board referral.

### Overall Score
**4 (Borderline Accept)**: A practical, interpretable approach with consistent gains; the weaknesses I see (simulator reliance, safety reporting) are addressable and typical of accepted papers.

### Confidence
**3**: Less familiar with prompt-optimisation baselines.

---

## Reviewer 4 (Generalist)

# Peer Review Report

## Paper: Prompt reinforcing for long-term planning of large language models
## Reviewer: Dr. Fatou Mbengue-Hart, Generalist (ML department, North America; fictional persona)
## Expertise: representation learning; NLP; programme-committee generalist
## Date: 2026-11-10

### Summary
The paper argues that LLMs fail at multi-turn tasks because they are trained on single-turn rewards, and proposes to improve them without touching weights: an LLM critiques each turn of past dialogues, a second LLM rewrites the instruction prompt, and a history of earlier rewrites is kept. Experiments show improved success on text-to-SQL, a dialogue benchmark and human-judged medical QA.

### Strengths
**S1: Clear problem and simple idea.** The one-paragraph pitch (§1, Fig. 1) is easy to grasp and the method is described in five short equations (Eqs. 1–5) plus printed prompts (App. C).

**S2: Broad evaluation relative to many prompt-optimisation papers.** Three tasks, five backbones and a human study (Tables 1–2, Fig. 5).

**S3: Honest about limits.** The gap to the oracle (0.477 vs 0.743, §5.1) and weaker TCM results (§5.3) are stated plainly.

**S4: Well organised, readable paper.** Experiments follow the stated claims (robustness, feedback style, under-represented topics); captions explain the tables.

### Weaknesses

**W1: The main claim is easier to read than to verify, because the central comparison is not controlled.** The paper presents TD-style feedback with replay as the answer, but its own numbers show most of the gain comes from replay (Table 1: +0.069 over RPO_TD; Table 2: +0.044) while the baselines have none, and TD vs. MC differ by only 0.010–0.020. A reader cannot tell which ingredient matters.
- **Suggested Fix**: add baselines with replay and report both ablation directions (TD without replay, MC with replay).

**W2: Venue fit is reasonable but the contribution is framed more broadly than it is shown.** "Long-term planning" (title, abstract) and "efficient" (§1, §6) are not measured; evidence supports "multi-turn task success on three benchmarks" for GPT-4o-mini-class systems. Fig. 4b and Table 2 are the only analyses of mechanism.
- **Suggested Fix**: narrow the title/abstract wording or add planning and cost measurements.

**W3: Reporting is thin for a venue that expects statistics.** Tables 1–2 give single numbers with no sample size, and Fig. 4's four seeds appear only for FnCTOD; reading Fig. 4a/6 requires the appendix. A presentation fix: one table of the protocol (splits, N, epochs, roles).
- **Suggested Fix**: add the table and error bars to Tables 1–2.

**Minor**: The Δ% column in Table 1 is easy to misread as the gain of the mean (it is the mean of gains); "believe setting" (§5.2); "Converage Analysis" (App. B title) is a typo for "Convergence".

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly | W1; efficiency and planning claims unsupported |
| Presentation | Met | Clear; protocol table missing |
| Contribution: significance to the community | Partly | Practical but incremental |
| Reproducibility | Partly | Prompts given; code promised; splits missing |
| Honest limitations | Met | §5.1, §5.3, §6 |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Controls missing |
| Clarity | 3 | Easy to read |
| Significance | 2 | Moderate |
| Originality | 2 | Incremental |

### Pool position
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear, broad, honest paper, but the central claim is not isolated and several framing claims are not measured; borderline-reject side.

### Dimension Scores (0–100)
| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Reasonable method; attribution gap |
| Clarity & Presentation | 66 | Competent | Clear, with a few typos and ambiguous Δ% |
| Novelty & Originality | 55 | Competent | Incremental combination |
| Significance & Impact | 58 | Competent | Useful but narrow tasks |
| Experimental Validation | 55 | Competent | Breadth, but no variance for main tables |
| Reproducibility | 55 | Competent | Prompts printed; code promised |
| Ethical Compliance | 62 | Competent | Statement and limitations present |

### Questions for Authors
1. Which single result would you show a sceptic to prove that the turn-level (TD) feedback, not replay or richer inputs, matters?
2. Can you state precisely what "long-term planning" means operationally in the experiments?
3. Why is the same GPT-4o mini used for all medical experiments?

### Limitations Assessment
**Yes** for model limits; **Partially** for cost and simulators.

### Ethics Review Flag
**No**

### Overall Score
**3 (Borderline Reject)**: A readable paper with a sensible method, but what the paper says it shows (planning, efficiency, TD benefit) is more than the experiments isolate.

### Confidence
**3**

---

## Devil's Advocate

# Devil's Advocate Report

## Paper: Prompt reinforcing for long-term planning of large language models
## Reviewer: Dr. Ruslan Okonkwo-Vale, Devil's Advocate (evaluation and causal-inference team, Western Europe; fictional persona)

---

## Steelman
RPO is a cheap, black-box way to improve multi-turn LLM agents: richer per-turn natural-language feedback plus a rewriter that remembers past edits raises success on three task families, across five system LLMs and five meta-LLMs, closing a large part of the gap to fully specified single-turn input (Tables 1–2).

---

## Core Argument Chain
1. Multi-turn tasks fail because of poor long-term planning and early wrong assumptions (§1).
2. TD-style turn-level feedback gives a planning-relevant signal that whole-dialogue (MC) feedback lacks (§3.1, Eq. 3).
3. Experience replay in the rewriter stabilises and strengthens the update (§3.2, §5.2).
4. RPO beats APO, GPO and MC-style baselines on Text-to-SQL, MultiWOZ and medical QA (Tables 1–2, Fig. 5).
5. RPO is cheaper at inference than self-refine pipelines (§3, §6).
∴ RPO is a robust, efficient RL-inspired way to improve LLM long-term planning by changing only the prompt.

---

## Strongest Counter-Argument
Even if every number is right, the experiments do not isolate the mechanism the title and abstract claim. Three differences between RPO and its baselines are entangled with "TD-style feedback for long-term planning". First, RPO's best variant adds replay, which no baseline receives; the data show replay delivers the bulk of the gain (+0.069 in Table 1, +0.044 in Table 2) whereas switching MC-style to TD-style yields +0.020 and +0.010, and §5.2 admits "their final performances become comparable". Second, the RPO feedbacker is given the user goal and the API call for every turn (Fig. 10), and the paper's own ablation says these are "essential"; the MC-style prompt (Fig. 9) shows only user goals and the dialogue, and APO and GPO get a binary or scalar label (§4.3). The comparison therefore conflates information access with feedback style. Third, nothing measures planning. The optimised prompt in Fig. 12 is mostly slot-tracking, API validation, fuzzy matching and polite-closure rules, which fits the paper's own statement that "the correctness of API calls is the main challenge in task-oriented dialogue" (§5.2). A good prompt-engineer could have written such rules after reading failures. So the evidence supports "an iterative history-conditioned prompt rewriter with rich feedback improves task success on these benchmarks", not "TD-error-style feedback improves long-term planning". Add to this that the "efficient" claim is not measured at all, no variance or evaluation size is given for the main tables, and the supposed benefits over self-refine are never compared with a self-refine baseline. The authors need to answer with matched-information, replay-for-all baselines and a planning-specific metric.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The evidence supports a weaker version of the main claim (task success improves), so each problem below is fixable by narrowing claims or adding controls; no leakage is stated (selection uses a validation set, §4.3), and no result contradicts the main claim.

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| – | – | – | none | – | – |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (confound; supported weaker, not contradicted) | Tables 1–2; §4.3; Figs. 9–10; §5.2 | Replay and richer feedbacker inputs are given only to RPO; the TD-vs-MC gap (0.010–0.020) is within plausible noise | Replay-for-all and information-matched baselines; both ablation directions |
| DA-M2 | Scope (claim as worded not supported) | §3 intro; §6 | "reduces serving costs and latency" / "reducing computational overhead and API call frequency during inference" have no measurement and no self-refine baseline | Measure tokens, calls, latency; add Reflexion-style baseline or delete |
| DA-M3 | Logic | Title; §1; Eq. 3; Fig. 12 | "Long-term planning" is not measured; Eq. 3 is an analogy (V is "approximated by the previous turn-level feedback", γ undefined); alternative explanation: prompt fixes API/slot errors | Planning metric (turns-to-success, early-error recovery); reword |
| DA-M4 | Evidence | Tables 1–2; Fig. 4 caption | No sample size or seeds for main tables; "evaluated on 100 dialogues" gives SE ≈ 0.05 (derived) for Fig. 4; baselines differ by 0.01–0.02 | Report N, seeds, CIs |
| DA-M5 | Evidence | §4.1; Fig. 5 | Medical study: n inconsistency (90 vs 99), no agreement or blinding, feedback expert and evaluators possibly overlapping, win margins vs GPO not significant (p ≈ 0.12, derived) yet text says "consistently outperforms" and "preferred" | Agreement, blinding, tests, narrow wording |
| DA-M6 | Overclaiming (E5) | §5.1 (Table 2 paragraph), §5.1 conclusion, §6 | "Our proposed methods consistently surpass these baselines." is false on Llama-70B for RPO_TD; "demonstrate the robustness of our approach" rests on single-run cells; "stable, practical, and efficient" is not demonstrated | Rewrite claims to match tables |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Reporting | Table 1, §5.1 | "+54.2%" is the mean of per-LLM relative gains (43.2% for the gain of the means); dominated by Llama-8B (+108.5%) and Llama-4 (+85.9%) |
| DA-m2 | Generalisation | Tables 1–2 | System-LLM variation (Table 1) and meta-LLM variation (Table 2) are never crossed; medical uses one model |
| DA-m3 | Typos | §5.2; App. B | "believe setting"; "Converage Analysis" |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Table 1 BaselineSharded mean | 0.333 | (0.402+0.514+0.206+0.224+0.318)/5 = 0.3328 | Yes |
| Table 1 RPO_TD+replay mean | 0.477 | 2.387/5 = 0.4774 | Yes |
| Table 1 gain of means | "+54.2%" in text | 0.477/0.333 − 1 = +43.2%; mean of per-LLM gains = 54.0 | Only under the per-LLM-mean definition |
| Table 2 RPO_TD mean and Δ | 0.575 / 37.0 | 2.876/5 = 0.5752; 0.575/0.420 = +36.9% (+37.0 from unrounded) | Yes |
| Table 2 RPO_TD+replay mean and Δ | 0.619 / 47.3 | 3.093/5 = 0.6186; +47.3% | Yes |
| "consistently surpass" (Table 2) | all five LLMs | Llama-70B: 0.556 vs MC 0.572, APO 0.560 | No |
| "86.7% win rate" (Fig. 5a) | 86.7% | consistent with 78/90 | Yes (n not independently confirmable) |

## Ignored Alternative Explanations
- Extra information in the feedbacker (user goal, API call) drives the gain, not the TD structure.
- Replay adds more context and more optimisation signal per epoch; any baseline with a history would gain.
- Two candidates per epoch with validation selection (§4.3) is a search procedure; if baselines get fewer candidates, RPO gets a larger search budget.
- Simulator adaptation: prompts learn the simulated user's habits.
- Fixing known API/slot-tracking bugs in FnCTOD's prompt (Fig. 11 vs. Fig. 12) rather than planning improvements; the original FnCTOD prompt is only six lines.
- Regression to the mean in selection: choosing the best of two candidates on a noisy validation score (non-batch-invariant LLMs, App. B) inflates validation scores.

## Missing Stakeholder Perspectives
Real users who change goals mid-dialogue; clinicians accountable for medical advice outputs; practitioners who need cost per dialogue; non-English-speaking users beyond the two Chinese medical sets.

## Observations (Non-Defects)
- The paper reports negative or modest results honestly (§5.1 gap to oracle, §5.3 TCM) and prints every meta-prompt and an example optimised prompt.
- Selection is done on a validation set (§4.3), and the paper does not state any tuning on a test split, so no leakage claim is made.
- The TD+replay gain over all baselines is consistent in sign across all ten (LLM × table) columns, which is hard to attribute to chance alone even without variance.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Mechanism attribution fails; TD analogy informal |
| Clarity & Presentation | 60 | Clear, with ambiguous Δ% and overclaiming sentences |
| Novelty & Originality | 48 | Incremental |
| Significance & Impact | 48 | Gains over uncontrolled baselines |
| Experimental Validation | 42 | No stats, no replay-for-all, no cost |
| Reproducibility | 50 | Prompts printed; protocol missing |
| Ethical Compliance | 58 | Medical risk understated |

## Overall: 3 | Confidence: 3

*Pool position: better than about 43% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline attribution is confounded and the efficiency claim has no measurement.*

---

# Phase 1.6 — Report Check (Editorial Synthesizer, Step 0)

Each weakness was tested for specificity, whether the paper already answers it, consistency with the paper, and actionability. Scores were not changed.

| Report | Weakness (as first drafted) | Action | Reason |
|--------|------------------------------|--------|--------|
| R1 | "No variance reported anywhere" | Rewritten (W2) | Fig. 4 and Fig. 6 report 4 seeds with standard error; the gap is Tables 1–2 and Fig. 5 |
| R4 | "No discussion of limitations" | Dropped | §5.1 (last paragraph), §5.3 and §6 discuss limits; kept only a note on cost and simulators |
| R2 | "OPRO already contains replay, so replay is not novel" | Rewritten as a hedged weakness and question (W2) | Cannot be matched against OPRO's abstract offline (literature check failed), so stated as unverified |
| DA | "Selection on the test set (criterion 3)" | Dropped | §4.3 states selection on a validation set; no test-split statement exists. Kept as a question about which split Tables 1–2 report |
| R3 | "No code released" | Moved to Minor (R1 Minor) | Code is promised in the Reproducibility Statement; prompts are in App. C |
| R1 | Error Log item on "n = 99" | Kept with Medium confidence | Arithmetic is checkable, but cause (extraction vs. manuscript) unknown |
| DA | "Eq. 3 is wrong" | Rewritten as DA-M3 | Eq. 3 is the standard TD error; the issue is that V is not a value function, not an algebra error |

Weaknesses were reordered by severity in every report; typos are on Minor lines.

---

# Phase 2 — EIC Meta-Review and Decision

## Synthesizer, Part A: package for the EIC

**Merged issue list**

| Issue | Sources | Class |
|-------|---------|-------|
| Replay and richer feedbacker inputs only for RPO; TD vs MC within noise | R1-W1, R4-W1, DA-M1, (R2-W2 partly) | CONSENSUS-4 |
| No sample size / seeds / CIs for Tables 1–2; protocol gaps | R1-W2, R1-W3, R4-W3, DA-M4 | CONSENSUS-3 |
| Efficiency/cost claims unmeasured; no self-refine baseline | R1-W4, R2-W1 (baselines), R3-W2, R4-W2, DA-M2 | CONSENSUS-4 |
| "Long-term planning" not measured; TD formalism informal | R2-W3, R4-W2, DA-M3 | CONSENSUS-3 |
| Closest multi-turn/agent baselines not compared | R2-W1, R1-W4 (partly) | CONSENSUS-2 |
| Medical evaluation small, undocumented, safety not separated | R1-W5, R3-W3, DA-M5 | CONSENSUS-3 |
| Simulator dependence | R3-W1, DA (alt. explanation) | CONSENSUS-2 |
| Emotion/success forecast unvalidated | R2-W4, R3-W4 | CONSENSUS-2 |
| Replay novelty vs history-conditioned optimisers | R2-W2 | SOLO (unverified) |
| Overclaiming wording ("consistently surpass") | R1 (ERR-2), DA-M6 | CONSENSUS-2 |

**DA-CRITICAL issues:** none. **SPLIT:** significance (R3 Overall 4 vs. four reviewers at 3). **Issues the outcome may hinge on:** the replay/information confound, the unmeasured efficiency claim, and the statistics gap.

**Official output (before EIC weights):** official rating mean 3.20, official composite 54.6; per-reviewer composites 52.3 / 53.4 / 60.7 / 57.5 / 49.2; dimension spreads all ≤ 18 (no ⚠); DA composite band 2 vs. Overall 3 (within ±1, no warning needed).

## EIC Meta-Review

# Editorial Decision

## Paper: Prompt reinforcing for long-term planning of large language models
## Submission ID: iclr26-Xt6K4cw36l
## Date: 2026-11-10
## Target Venue: ICLR (2026 cycle, scale status: secondary) | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Halvard Meissen-Ortiz; R1 Methodology Dr. Kenji Arakawa-Lindt, R2 Domain Dr. Marisol Quispe-Valdés, R3 Perspective Dr. Anders Thorvaldsen-Bell, R4 Generalist Dr. Fatou Mbengue-Hart, DA Dr. Ruslan Okonkwo-Vale

## Decision: Borderline Reject (3) — ICLR rating 4 on {0, 2, 4, 6, 8, 10} (5 on the earlier {1, 3, 5, 6, 8, 10} scale)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean 3.20 · official composite 54.6
**EIC assessment** (internal): weighted rating 3.18 → starting point 3 · weighted composite 54.4 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 47% of ICLR submissions.

### The Case For and Against
- **For acceptance:** A practical, black-box method for a real and recent problem (multi-turn degradation). It improves success in every reported cell over three baselines, across three task families and five backbones, prints all prompts, and discusses where it fails. TD+replay is above every baseline in all ten LLM columns of Tables 1–2.
- **Against acceptance:** The headline mechanism (TD-style feedback for long-term planning) is not what the experiments isolate: replay carries most of the gain and is given to no baseline, the TD-vs-MC gap is 0.010–0.020 with no variance, feedbacker inputs differ, planning is unmeasured, and the "efficient" claim has no measurement. A fixed set of controls would decide it, and those are not in the paper.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Replay not applied to baselines; TD vs MC gap small (0.020 / 0.010); replay adds 0.069 / 0.044 | R1-W1, R4-W1, DA-M1 | Tables 1–2; §5.2; Fig. 4a text | **Verified** | Recomputed from the tables; §5.2: "their final performances become comparable" |
| Feedbacker input asymmetry (user goal, API call) | R1-W1, DA-M1 | Figs. 9–10; §4.3; §5.2 | **Partly correct** | Fig. 10 includes API calls and user goal; Fig. 9 names user goals and "[DIALOG]" without saying whether API calls are in it; APO/GPO use binary/numeric labels (§4.3). The asymmetry is likely but not certain |
| Efficiency claims unmeasured | R1-W4, R4-W2, DA-M2 | §3 intro; §6; whole paper | **Verified** | No latency, token or call count anywhere; no self-refine baseline in Tables 1–2 |
| Evaluation size/split/seeds missing for Tables 1–2 | R1-W2, R1-W3, DA-M4 | Tables 1–2; §4; Fig. 4 caption | **Verified** | Text search finds no "test"/"split"; "validation" only in §4.3; Fig. 4: 4 seeds, 100 dialogues |
| Selection is on a validation set; no leakage statement | DA (dropped criterion 3) | §4.3 | **Verified** (no leakage claim stands) | Quote "the highest score on the validation set" is present |
| "consistently surpass" false on Llama-70B | R1 ERR-2, DA-M6 | Table 2 vs §5.1 | **Verified** | 0.556 vs 0.572 (MC) and 0.560 (APO) |
| "+54.2%" is mean of per-LLM gains; gain of means is 43.2% | R1 ERR-1, DA-m1 | Table 1, §5.1 | **Verified** (wording issue, MINOR) | Table 1 caption defines Δ% as relative improvement across LLMs; the §5.1 sentence reads as the gain of the average |
| Medical study n inconsistency (90 vs 99) | R1 ERR-3 | §4.1; Fig. 5b | **Partly correct** | Percentages are multiples of 1/99; the stated size is 90; cause unknown, figure labels read from extraction |
| Planning not measured; Fig. 12 prompt is slot/API rules | R2-W3, R4-W2, DA-M3 | Fig. 12; §5.2 | **Verified** | §5.2: "the correctness of API calls is the main challenge in task-oriented dialogue" |
| Predicted emotion/success never validated | R2-W4, R3-W4 | §3.1 | **Verified** | No analysis compares forecasts with outcomes |
| Replay is not novel because OPRO already conditions on history | R2-W2 | §2 | **Partly correct** (unverifiable offline) | Literature check failed; treated as a question; weight only on the stated delta being absent, which is verified |
| Medical win margins vs GPO not significant (p ≈ 0.12) | R1-W5, DA-M5 | Fig. 5a | **Verified** (derived) | 36 vs 24 non-tied; sign test; depends on n=90 and bar order from extracted labels |
| Simulator dependence | R3-W1 | §4.1 | **Verified** | Simulator LLM not named |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every MAJOR point verified, arithmetic correct; minor overstatement only (ERR-3 depends on an extracted figure) |
| R2 (Domain) | 3 | 3 | 1.0 | Sound; the OPRO point is unverifiable offline and is hedged |
| R3 (Perspective) | 4 | 3 | 1.0 | Constructive and mostly right; Overall 4 is on the lenient side but is the Perspective role's job, not a calibration error |
| R4 (Generalist) | 3 | 3 | 1.0 | Typical, well-calibrated generalist read |
| DA | 3 | 3 | 1.0 | No CRITICAL; the counter-argument survives my check in substance, with the input-asymmetry point only partly verified |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
The EIC-weighted rating is 3.18, giving a starting point of 3 (Borderline Reject); the composite cross-check (54.4, band 3) agrees, and there is no DA ceiling. I keep 3. I find no verified issue that the ratings failed to account for, and no low rating rests on a point the paper answers: R3's 4 is the only dissent and is based on practical value, which I accept as real but not enough to offset the verified attribution gap. My own pool position is about 47: the paper is above the median submission for breadth (three tasks, five LLMs used as system agents and as meta-prompting agents), but a typical accepted ICLR paper at this level has either budget-matched baselines or statistical reporting, and this one has neither for its decisive comparison. I weigh the issues as fixable, not fatal: matching baselines with replay, stating sample sizes and seeds, and measuring or dropping the efficiency claim need no new ideas, so a revised version with those controls could move to 4 or 5. This is a simulation of how a careful panel would likely see this draft, not a prediction of the actual outcome.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 55 | 60 | 56 | 48 | 54.2 | 54.0 | 12 |
| Clarity & Presentation | 62 | 64 | 66 | 66 | 60 | 63.6 | 63.4 | 6 |
| Novelty & Originality | 50 | 48 | 60 | 55 | 48 | 52.2 | 52.0 | 12 |
| Significance & Impact | 52 | 52 | 66 | 58 | 48 | 55.2 | 54.9 | 18 |
| Experimental Validation | 45 | 48 | 58 | 55 | 42 | 49.6 | 49.2 | 16 |
| Reproducibility | 52 | 52 | 58 | 55 | 50 | 53.4 | 53.3 | 8 |
| Ethical Compliance | 62 | 62 | 58 | 62 | 58 | 60.4 | 60.6 | 4 |
| **Composite** | 52.3 | 53.4 | 60.7 | 57.5 | 49.2 | **54.6 (before)** | **54.4 (after)** | |
| Pool position (P%) | 45 | 45 | 66 | 52 | 43 | | | |

Reviewer weights (EIC, internal): R1 0.85 × 1.25 (28% share); R2, R3, R4, DA 0.70 × 1.00 (18% each). Official reviewer ratings: 3, 3, 4, 3, 3 → mean **3.20**. EIC-weighted rating **3.18**. No spread above 20; no consistency warning.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}); recent analyses report the former for 2026, so treat as secondary. Venue-weighted composite 54.3, band 3 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Prompt reinforcing for long-term planning of large language models" to ICLR.

Your paper tackles a real and timely problem, the degradation of LLMs in multi-turn interaction, with a practical, black-box approach.

**Overall Assessment:** The reviewers agreed that the idea is simple, readable and useful for API-only models, and that the empirical breadth is a strength. They also agreed that the evidence does not yet isolate which ingredient produces the gains.

**Key Strengths Identified by Reviewers:**
1. Practical, interpretable prompt-level adaptation that works for closed and open models (R3, R4).
2. Breadth: three task families, five system LLMs, five meta-prompting LLMs, and human-expert evaluation (R1, R4).
3. Printed prompts and honest discussion of limits, including the gap to the oracle and the weaker traditional-Chinese-medicine results (R1, R4, DA observations).

**Key Concerns Requiring Attention:**
1. The decisive comparison is not controlled: replay and possibly richer feedbacker inputs are given only to RPO; TD-vs-MC differences are 0.010–0.020 with no variance (R1, R4, DA; CONSENSUS-4).
2. Tables 1–2 carry no evaluation size, seeds or intervals; protocol details (split, roles, epochs, simulator) are missing (R1, R4, DA; CONSENSUS-3).
3. Claims about efficiency and "long-term planning" are not measured (R1, R2, R4, DA; CONSENSUS-4/3).

**Decision: Borderline Reject (3)**

The core idea is sound and the gains are consistent in direction, but the paper currently supports a narrower claim than it makes. Matching the baselines on replay and information, reporting variance and sample sizes, and either measuring cost or removing the efficiency claim would likely move this to a Borderline Accept or higher. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Halvard Meissen-Ortiz
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Replay/information confound; TD vs MC gap small | R1, R4, DA (R2 partly) | CONSENSUS-4 |
| Efficiency/cost unmeasured | R1, R2, R3, R4, DA | CONSENSUS-4 (5 if counting R3-W2) |
| Statistics and protocol gaps | R1, R4, DA | CONSENSUS-3 |
| "Long-term planning" not measured | R2, R4, DA | CONSENSUS-3 |
| Medical evaluation weaknesses | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall level of significance | R3 (Overall 4, pool 66) | R1, R2, R4, DA (Overall 3, pools 43–52) | Spread of pool positions is 23 points, below the 30-point trigger; rulings follow the verified confound: the paper is useful but its central claim is not isolated |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. The widest (Significance, 18) reflects R3's practical-impact weighting against the others' view that baselines are weak; I side with the others on attribution and with R3 on practical value, which is reflected in the rating being 3.18, not lower.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Replay and input confound | Yes (R1-W1, R4-W1) | n/a | n/a |
| DA-M2 | MAJOR | Efficiency claim unmeasured | Yes (R1-W4, R4-W2, R3-W2) | n/a | n/a |
| DA-M3 | MAJOR | Planning unmeasured, Eq. 3 analogy | Yes (R2-W3, R4-W2) | n/a | n/a |
| DA-M4 | MAJOR | No N / seeds / CIs | Yes (R1-W2, R4-W3) | n/a | n/a |
| DA-M5 | MAJOR | Medical study | Yes (R1-W5, R3-W3) | n/a | n/a |
| DA-M6 | MAJOR | Overclaiming wording | Yes (R1 ERR-2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld. These items are verified issues that undermine the main attribution claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Replay and feedbacker inputs differ between RPO and baselines; TD vs MC gap within noise | R1-W1, R4-W1, DA-M1 | Tables 1–2, §4.3, Figs. 9–10, §5.2 | Add MC/APO/GPO+replay; give all feedbackers the same inputs, candidates, epochs and context; report both ablation directions | High (API cost: about 3 methods × 5 LLMs × 4 seeds × 8 epochs on the dialogue task, no GPUs) | Partly (dialogue task on 1–2 LLMs) |
| R2 | No evaluation size, seeds, intervals; missing protocol (split, roles, epochs, simulator, baseline re-run) | R1-W2, R1-W3, R4-W3, DA-M4 | Tables 1–2, §4, Fig. 4 | Protocol table; mean ± s.d. over ≥ 3 seeds or paired bootstrap CIs | Medium | Yes (text) / Partly (reruns) |
| R3 | Efficiency and cost claims unmeasured | R1-W4, R2-W1, R3-W2, R4-W2, DA-M2 | §3 intro, §6 | Measure tokens, calls and latency for optimisation and serving versus a self-refine baseline, or delete the claim | Medium | Yes |
| R4 | "Long-term planning" untested; Eq. 3 is an analogy | R2-W3, R4-W2, DA-M3 | Title, §1, §3.1, Fig. 12 | Add planning-specific metrics (turns-to-success, early-error recovery), or reword to "multi-turn task success" and "RL-inspired" | Medium | Yes (reword) |

### Priority 2 — Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Cited multi-turn and agent baselines not run (Reflexion, Agent-Pro, OPRO with history, PromptAgent) | R2-W1 | Add at least Reflexion/Agent-Pro and OPRO to Table 2 | Medium–High | Partly |
| S2 | Medical evaluation: agreement, blinding, rater overlap, n inconsistency (90 vs 99), significance, safety scored separately, wording "consistently outperforms" | R1-W5, R3-W3, DA-M5, ERR-3 | Report agreement, tests, separate safety; fix n; narrow wording | Medium | Partly |
| S3 | Overclaiming wording and Δ% definition | R1 ERR-1, ERR-2, DA-M6, DA-m1 | "four of five meta-LLMs"; report +43.2% for the gain of the mean alongside the mean of gains | Low | Yes |
| S4 | Replay novelty delta vs history-conditioned optimisers not argued | R2-W2 | Delta paragraph and OPRO-style score-history ablation | Low–Medium | Yes |
| S5 | TD signal never validated (emotion, success forecast) | R2-W4, R3-W4 | Forecast accuracy; ablate emotion and forecast fields | Medium | Partly |
| S6 | Critical/important missing references (`[verify]`): Self-Refine, Retroformer, ExpeL, ArCHer | R2 | Cite and differentiate | Low | Yes |

### Priority 3 — Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Simulator dependence; transfer to other simulators or real users | R3-W1 | Second simulator; small real-user study |
| N2 | Drift/regression across epochs; rollback rule | R3-W2 | Held-out regression check each epoch |
| N3 | Cross system-LLM × meta-LLM grid; more than one model for medical | DA-m2 | Add a small crossed grid |
| N4 | Helpful references: DSPy/MIPRO, EvoPrompt `[verify]` | R2 | Cite |
| N5 | Typos ("believe setting", "Converage Analysis"); code release | R1, R4, DA | Fix; release code |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–4 weeks (mostly API experiments; the dialogue-task subset about 1 week)
- Priority 2: 6 items, about 1–2 weeks
- Priority 3: 5 items
- **Total estimated revision time**: about 4–6 weeks; a rebuttal-window subset (Priority 1 items R2–R4 plus one replay-matched baseline on MultiWOZ with one or two LLMs) is feasible in about 1 week.

---

*Venue translation for ICLR: Soundness 2, Presentation 3, Contribution 2; rating 4 on {0, 2, 4, 6, 8, 10} (scale status: secondary; shown with the earlier-cycle value 5 on {1, 3, 5, 6, 8, 10}). Cross-Venue Outlook was not requested. The Gap Scout (post-review analysis) was not requested and was not run.*
