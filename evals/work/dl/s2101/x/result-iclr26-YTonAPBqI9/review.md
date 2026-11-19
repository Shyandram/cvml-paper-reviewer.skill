# Simulated Panel Review: "EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus"

*Date: 2026-11-10. Mode: full, target venue ICLR (stated), literature check requested `strict` with cutoff 2025-09-24. This is a simulation of how a careful panel would likely see this draft, not a prediction of an outcome. Figures were not available (text extraction only); figure-dependent claims (Figures 1–4) are judged from captions and text. Text extraction garbled Table 3 and the percent sign in Section 3.5; those are treated as "unverifiable", not as authors' errors.*

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

### 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus |
| Primary Discipline | NLP / LLMs → educational dialogue, synthetic data for tutoring |
| Secondary Discipline(s) | Learning sciences (Bloom's taxonomy, ZPD), LLM-as-judge evaluation |
| Paper Type | Dataset (with a trained model and an evaluation framework as secondary contributions); composite weights: dataset |
| Core Technique(s) | LLM-generated multi-agent dialogue synthesis (o1), SFT + DPO with QLoRA on QwQ-32B-Preview, GPT-4o plus human rubric evaluation |
| Target Venue | ICLR 2026 (stated); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none (no ECCV/ACM MM/TPAMI rule applies) |
| Paper Maturity | Submission-ready in form, with a "Preprint" header; no limitations section |
| Ethics-Relevant Content | Simulated students only (no human subjects). Textbook-derived content, MOOC videos analysed, and o1/GPT-4o outputs used as training data (licensing/terms not discussed). Pedagogical-equity risk of ability-labelled teaching strategies |

### Paper memory (factual record shared with all reviewers)

**Claims.** C1 (resource): EduDial, "345 core knowledge points" and "34,250 dialogue sessions", five teaching stages, ten questioning strategies, three student levels (Abstract, §1, §3.2, §3.6). C2 (method/result): EduDial-LLM 32B by SFT then DPO "consistently outperforming all baselines across all metrics" (Abstract, §4.2, Table 2). C3 (resource): an 11-dimensional evaluation framework with human and GPT-4o raters (§3.5, Table 1, Appendix evaluation prompt). C4 (analysis): ablations show SFT and DPO both matter (§4.3, Table 3). C5 (result): general mathematical reasoning is "acceptable" after training (Table 4).

**Setup facts.**
- Data: K-12 mathematics, 345 knowledge points in 173 chapters; split 8:2 by chapter, 137 train chapters (275 points) and 36 test chapters (70 points) (§3.6).
- MTI: 100 dialogues per train chapter = 13,700 dialogues, ~11 rounds each. PDTS: 50 instructions per student role per chapter = 20,550 preference pairs (§3.6).
- Generator: o1 (§3.3). Verifier: GPT-4o plus unspecified "experts" (§3.3).
- Training: QwQ-32B-Preview teacher; Qwen2.5-32B/14B/7B student simulators (Table 5). QLoRA r=64, α=16; SFT lrs in Table 5; DPO lr 5e-7, β=0.1, 2 epochs; 2×A100; 45 h SFT and 8 h DPO (§4.1).
- Evaluation: 36 scenarios per model, each with three student agents, up to 15 rounds (§3.6). Five human experts; GPT-4o five times, averaged (§3.5). Baselines: 9 closed and 8 open models (§4.1).
- Selection: "All hyperparameters are empirically determined via grid search on the test set." (§4.1). No validation split is described anywhere (§3.6 lists train and test only).
- Not stated after search: seeds, number of runs, confidence intervals, inter-rater agreement, expert qualifications, verification pass rates, dataset licence, language of the dialogues, which models play the students at evaluation time, baseline system prompts and decoding settings, the model that generates "chosen" PDTS responses (§3.3 says only "LLMs"), a limitations section.

**Headline numbers → source.** EduDial-LLM AVG 4.47 (machine) / 4.36 (human), Table 2. Best baseline AVG 4.19 / 4.22 (Gemini-2.5-Pro-Exp), Table 2. Base QwQ-32B-Preview AVG 2.75 / 2.53, Table 2. Pearson 0.90, Spearman 0.91 across 18 models, §4.3 (Figure 4 not visible). Math500 91.12 → 87.54, AIME2024 43.33 → 33.33, Table 4.

**Appendix summary.** Tables 5–8 (SFT parameters, questioning strategies, role profiles, strategy table), a case study (Normal Distribution), the generation prompts, and the full evaluation prompt. No extra experiments, no statistics on the verification loop, no human-study details.

**Unverifiable.** Figures 1–4 (not available); Table 3's column alignment (extraction) and whether it is machine or human; the dropped "%" in §3.5.

### Integrity signals
`scripts/integrity_scan.py` was **not run**: this evaluation restricted tools to reading files and running the aggregation and literature scripts. A manual full-text search for reviewer-directed text ("ignore", "reviewer", "give a positive", "strong accept", AI-system addresses) found **no matches**; no hidden-text signal could be checked beyond the extracted text. Reviewers read the unmodified text (no redaction needed).

### Literature check status (Phase 1.5)
Mode `strict`, cutoff 2025-09-24. A fingerprint was written. **The arXiv API was unreachable**: the first search query returned HTTP 429 and a second timed out; 2 claim queries were attempted (C1), 0 results kept, 0 baseline/expansion queries ran. Per `references/literature_search.md`, the check fell back to `off`: all reference recommendations below come from the reviewers' knowledge and are marked `[verify]`; no novelty verdict rests on a search result.

### 👥 Review Team (fictional personas)

**EIC (meta-reviewer): Dr. Helena Okonkwo-Vance**, large public research university (Europe). Senior faculty; NLP, evaluation of generative models, educational technology. Role: reads all five reviews, checks decisive points, weights, decides. Style: reads tables first; asks whether a headline claim survives a one-minute recomputation.

**Reviewer 1 (Methodology): Dr. Tomasz Heilmann**, industrial research lab (Europe). Senior industry scientist; LLM post-training (SFT/DPO), LLM-as-judge validity. Focus: design, statistics, comparison fairness, reproducibility. Style: runs the protocol sweep before reading the results.

**Reviewer 2 (Domain): Dr. Mei-Ling Arvanitis**, NLP group, mid-sized university (East Asia). Mid-career; dialogue tutoring datasets, math word problems, synthetic data. Focus: literature, theory, domain contribution. Style: lists the closest prior dataset and asks what differs.

**Reviewer 3 (Perspective): Dr. Rafael Quispe-Dunmore**, school of education, large public university (South America). Mid-career; learning sciences, formative assessment, classroom discourse. Focus: pedagogical validity, deployment, equity, assumptions. Style: constructive, asks what a teacher would do differently.

**Reviewer 4 (Generalist): Dr. Sung-Min Aaltonen**, ML department, research university (Northern Europe). Mid-career; representation learning and language models, not tutoring. Focus: contribution clarity, venue fit, presentation. Style: typical program-committee member; writes the contribution in one paragraph first.

**Devil's Advocate: Dr. Idris Valcourt-Nair**, statistics and evaluation methodology group (North America). Senior; causal inference, measurement validity. Focus: core-argument challenges, overclaiming. Style: rigorous, never hostile.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Five Independent Reports

*(One model context performed five separate role-based passes; they are not independent agents, and this is disclosed. Each pass was written from the paper and its own role file, without reading the others' reports.)*

---

# Peer Review Report: Reviewer 1 (Methodology)

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Reviewer: Dr. Tomasz Heilmann, Methodology Reviewer (industrial research lab, Europe; fictional persona)
## Expertise: LLM post-training (SFT/DPO), LLM-as-judge validity, evaluation protocols
## Date: 2026-11-10

### Protocol sweep (Step 0)
Searched the full text for split, tuning and selection statements. Found: "We split the dataset at an 8:2 ratio by chapter" (§3.6), train and test only, no validation split; "All hyperparameters are empirically determined via grid search on the test set." (§4.1); "evaluating model performance every 500 steps" (§4.1; the split used for this monitoring is not stated, and checkpoint choice is not stated). Seeds, number of runs, intervals: not stated after search. Passed to the Devil's Advocate.

## Summary
The paper builds a synthetic K-12 mathematics teacher–student dialogue corpus with an LLM (o1), organised by a five-stage teaching process, ten question types and three student profiles. It trains a 32B teacher model with SFT on multi-turn dialogues and DPO on strategy-conditioned preference pairs, and proposes 11 rating dimensions scored by five human experts and GPT-4o. On 36 simulated teaching scenarios per model, the trained model has the highest average rating of 18 models (Table 2), and ablations (Table 3) attribute gains to SFT and DPO. A reasoning check (Table 4) shows a drop relative to the base model.

## Strengths
### S1: A concrete, reusable pedagogical scaffold
Table 6 and the prompt templates in the appendix (pp. 16–19) make the five-stage/ten-strategy design inspectable and reproducible in principle; this is more transparent than most synthetic-dialogue papers.

### S2: Large headline gain over the base model, with a sensible ablation grid
Table 2 gives QwQ-32B-Preview AVG 2.75 (machine) and EduDial-LLM 4.47. Table 3 separates SFT-only, DPO-only and both, and the text claim that DPO mainly lifts thinking and adaptability is consistent with the printed numbers (SFT-only vs complete, excellent-student row: THK 3.92→4.27, ADP 4.17→4.78).

### S3: Honest disclosure of a capability cost and of compute
Table 4 reports a drop on Math500 and AIME2024, and §4.1 reports hardware and hours (45 h SFT, 8 h DPO), which are consistent with Table 5 (15 total epochs × 3 h = 45 h).

## Weaknesses

### W1 (CRITICAL candidate, E4): Hyperparameters were selected on the test set that produces every reported number
§4.1: "All hyperparameters are empirically determined via grid search on the test set." The test set is the 36-chapter/70-knowledge-point split of §3.6; no validation split exists. Table 2, Table 3 and Table 4 numbers for EduDial-LLM come from the configuration so selected, while baselines receive no tuning. Disclosure does not make the numbers valid. The sweep itself is not shown, so it cannot be checked whether the gap to the best baseline (4.47 vs 4.19 machine; 4.36 vs 4.22 human, derived) survives other grid points.
- **Suggested Fix**: carve a validation set from the 137 training chapters, redo the grid search and checkpoint selection there, and rerun Tables 2–3 once on the untouched test chapters. Cost: roughly 53 GPU-hours per configuration on the stated hardware (45 h + 8 h from §4.1, derived), times grid size; a reduced grid on the 14B student base is a cheaper proxy.

### W2 (E5): The abstract's central claim is contradicted by Table 2
Abstract: "consistently outperforming all baselines across all metrics". Machine scores in Table 2 show EduDial-LLM below at least one baseline on RES (4.12 vs 4.63 Claude-3-7-Sonnet-Thinking), EMO (4.10 vs 4.67 Gemini-2.5-Pro-Exp), FLU (4.43 vs 4.67 Gemini-2.5-Pro-Exp), REL (4.83 vs 4.95 Gemini-2.5-Pro-Exp) and COV (91.83 vs 96.16 Gemini-2.0-Flash-Exp). Human COV is 88.29 vs 94.84 for the same baseline. §4.2 states "Regarding content quality, our scores match the best baseline models", which COV does not support.
- **Suggested Fix**: restate the claim as "highest average over the nine overall-quality dimensions", report per-dimension ranks, and discuss the losses (emotional support, fluency, coverage).

### W3 (E1/E6): Table 3 is not reconcilable with Table 2 for the base model
Table 3 base-model rows give AVG 3.10 (E), 2.88 (M), 2.99 (S), mean 2.99. Table 2 gives QwQ-32B-Preview AVG 2.75 (machine) and 2.53 (human); neither matches. The Table 3 rows' own AVGs are internally correct (e.g., excellent-student row: nine dimensions sum to 27.91, /9 = 3.10, recomputed). For the complete model the student-type mean of AVG (4.477) matches Table 2 (4.47), but dimension-level means differ (e.g., INT: Table 3 mean 4.33 vs Table 2 4.64; FLU 4.79 vs 4.43). Table 3 does not say whether it is machine or human. Confidence is Medium because of table-extraction alignment.
- **Suggested Fix**: state the rater type in Table 3's caption and explain the differences (different scenario draws? different students?).

### W4: No variance, no seeds, no uncertainty on any comparison
36 scenarios per model and one run (no seeds, intervals or tests anywhere). The human-rated margin over the best baseline is 0.14 on a 5-point scale (4.36 vs 4.22, derived). LLM-judge scores are averaged over five GPT-4o calls but no spread is given. Table 4's AIME2024 drop is 10.00 points (43.33→33.33, consistent with 13/30 vs 10/30 problems), which is described as "this difference falls within the expected range" (§4.3) without a basis.
- **Suggested Fix**: bootstrap over scenarios for every Table 2 AVG, report judge-repeat spread, run ≥3 training seeds for the 14B proxy, and replace "within the expected range" by the measured drop with a CI.

### W5: Fairness of the baseline comparison is undefined
Not stated after search: the system prompt given to baselines, whether baselines received the five-stage teaching prompt, decoding settings, API versions and dates (§4.1 lists names only), and which models play the three students at test time (§3.6: "Each model acts as the teacher, engaging with three students of varying cognitive levels."). If the students are the EduDial-trained simulators of Table 5, the evaluation distribution equals the training distribution of EduDial-LLM and not of the baselines. The missing control for the paper's own stated purpose (§3.4: "performance gains stem from data quality rather than algorithmic innovations") is the same base fine-tuned on an existing dialogue dataset, and a baseline prompted with the five-stage template.
- **Suggested Fix**: add (a) QwQ-32B-Preview and o1 prompted with the MTI template, (b) the same base SFT/DPO-trained on MathDial or the SocraticLM data, (c) a fixed, released student pool for all teachers. Cost: ~53 GPU-h for (b) per dataset, plus API cost for (a).

### W6 (E2): Eqs. (3)–(5) do not match the DPO described in §4.1
Eq. (3)–(5) define the loss from raw sequence log-probabilities with no reference policy and no β, while §4.1 says "we set β to 0.1". Either the equations are not the implemented objective or the implemented objective is not DPO as named; length normalisation is also unspecified. The method cannot be reproduced from the text on this point.
- **Suggested Fix**: give the actual objective (reference model, β, length handling) and cite the original DPO paper (not cited in the reference list).

**Minor**: "18 large language models as baselines, including nine closed-source and eight open-source models" (§4.1) is 17 baselines, the Abstract says 17, Table 2 and Figure 4 say 18 (including EduDial-LLM); §4.3's heading "Ablation Study" also holds the judge-validation analysis; the percent sign is lost in §3.5 (extraction).

### Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | 34,250 dialogue sessions, 345 knowledge points | Abstract, §3.6 | 13,700 dialogues + 20,550 preference pairs (derived: 34,250); 275+70=345 | Partially: 20,550 are preference pairs, not sessions |
| C2 | Outperforms all baselines on all metrics | Abstract | Table 2 | Contradicted as worded; supported for AVG only |
| C3 | Judge reliability | §4.3 | Fig. 4 (not visible), Pearson 0.90 | Partially: correlation over 18 model means only |
| C4 | SFT and DPO each help | §4.3 | Table 3 | Partially: test-selected, no variance, base AVG mismatch |
| C5 | Reasoning "acceptable" | §4.3 | Table 4 | Partially: −3.58 and −10.00 points |

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E4 | §4.1 | "All hyperparameters are empirically determined via grid search on the test set." | Selection on the held-out split that yields all headline numbers | Protocol sweep; §3.6 has no validation split | High | CRITICAL | Re-tune on a validation split |
| ERR-2 | E5 | Abstract vs Table 2 | "consistently outperforming all baselines across all metrics" | RES, EMO, FLU, REL, COV lower than a baseline (4.12<4.63; 4.10<4.67; 4.43<4.67; 4.83<4.95; 91.83<96.16) | Compared rows of Table 2 | High | MAJOR | Narrow the claim |
| ERR-3 | E1/E6 | Table 3 vs Table 2 | (table values) base AVG 3.10/2.88/2.99 vs 2.75 (M), 2.53 (H) | Same model, different AVG | Recomputed row means; cross-referenced | Medium | MAJOR | State rater type, reconcile |
| ERR-4 | E2/E6 | Eqs. 3–5 vs §4.1 | "we set β to 0.1" | Equations contain no β and no reference policy | Cross-referenced | High | MAJOR | Correct the objective, cite DPO |
| ERR-5 | E1 | Abstract vs §3.6 | "34,250 dialogue sessions generated through interactions between teacher and student agents" | 20,550 of 34,250 are preference pairs (13,700 dialogues) | Derived: 13,700+20,550 | High | MINOR | Report dialogues and pairs separately |
| ERR-6 | E6 | §4.1 vs Abstract | "We select 18 large language models as baselines, including nine closed-source and eight open-source models." | 9+8=17 | Counted | High | MINOR | Fix count |
| ERR-7 | E5 | §4.3 | "this difference falls within the expected range" | AIME drop of 10 points called "slightly below"; no expectation is given | Recomputed 43.33−33.33 | Medium | MINOR | Report CI, soften |

## Missing References
*(Methodology reviewer: optional.)* See Reviewer 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Test-set selection, no variance, contradicted headline claim |
| Clarity | 3 | Readable; undefined baseline and student setup |
| Significance | 2 | Useful resource, unvalidated measure |
| Originality | 2 | Incremental over existing LLM-simulated tutoring corpora |

## Dimension Scores (0–100)
**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: test-set tuning (§4.1) plus a headline claim that Table 2 contradicts, with no variance and a judge/data-generator family overlap.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | W1, W3, W6; method equation mismatch |
| Clarity & Presentation | 62 | Competent | Clear structure; missing setup, count inconsistencies |
| Novelty & Originality | 45 | Developing | Pipeline combines known ideas |
| Significance & Impact | 48 | Developing | Niche; value depends on unvalidated evaluation |
| Experimental Validation | 35 | Developing | W1, W2, W4, W5 |
| Reproducibility | 48 | Developing | Prompts and Table 5 present; evaluation setup, selection sweep, baseline prompts, seeds missing; code only promised (capped) |
| Ethical Compliance | 55 | Competent | No human data; thin ethics (see R3) |

## Questions for Authors
1. Which model plays each student during evaluation, and is the same pool used for every teacher? (A fixed, external pool would lower my concern in W5; EduDial-trained students would raise it.)
2. What was the grid, and what do Table 2's AVG values look like at the non-selected grid points? (Robustness across the grid would move me from 2 toward 3.)
3. Is Table 3 machine or human, and why does the base model's AVG differ from Table 2?
4. What is the exact DPO objective (reference model, β, length normalisation)?

## Limitations Assessment
**Partially.** There is no limitations section; Table 4 is the only candid cost. Add limits on the simulation, the judge, the math-only scope and the single base model.

## Ethics Review Flag
**No.**

## Overall Score
**2 (Reject)**: the headline numbers rest on test-set selection and are overstated in the abstract; the evaluation does not isolate the contribution (data) from design choices or judge/student alignment.

## Confidence
**4**: confident on W1–W4 and W6, which are located and quoted; the setup details in W5 are inferred from omissions.

---

# Peer Review Report: Reviewer 2 (Domain)

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Reviewer: Dr. Mei-Ling Arvanitis, Domain Reviewer (NLP group, mid-sized university, East Asia; fictional persona)
## Expertise: dialogue tutoring datasets, math reasoning data, synthetic data generation
## Date: 2026-11-10

## Summary
EduDial presents LLM-generated K-12 mathematics tutoring dialogues built around a Bloom-inspired five-stage teaching sequence, ten question types and three simulated student levels, a preference set for strategy-conditioned DPO, and a rubric for evaluating teachers. The positioning (§2) is that earlier educational dialogue sets "employ rigid questioning strategies and ignore cognitive differences among students".

## Strengths
### S1: A clear gap statement and a well-motivated design
§2 and §3.2 tie the five stages to Bloom's levels and to ten named question types (Table 6); a reader can state the intended gap in one sentence: stage-aware questioning plus student-level-conditioned strategies.

### S2: Pairing a dialogue corpus with a preference set
PDTS (§3.3) encodes strategy adherence as chosen/rejected pairs, which is a sensible use of DPO for pedagogy and an element prior tutoring corpora such as MathDial (cited, §2) do not provide to my knowledge `[verify]`.

### S3: Domain content tied to a curriculum
345 knowledge points from textbooks, with 173 chapters and a chapter-level split (§3.2, §3.6), avoid within-chapter leakage between training and test chapters.

## Weaknesses

### W1: The key novelty claim against prior corpora is asserted, not tested
§2 characterises existing datasets as "rigid" and student-agnostic, with no table comparing EduDial to MathDial, CIMA, TalkMoves or SocraticLM's data on size, student types, strategies, or measured diversity. SocraticLM appears only as a baseline in Table 2 and as related work (§2). To my knowledge SocraticLM also builds an LLM-simulated multi-agent math teaching corpus `[verify]`, so the difference rests on the stage/strategy design, which is not isolated empirically. The paper's own purpose statement, "performance gains stem from data quality rather than algorithmic innovations" (§3.4), requires training the same base on competing data.
- **Suggested Fix**: add a comparison table of corpora and a controlled experiment (same base and recipe, different data).

### W2: Pedagogical grounding is thinner than presented
Bloom's levels are mapped to the five stages (§3.2), but the stage order puts "analyze" (deep understanding) before "apply and evaluate", whereas Bloom's usual order places "apply" before "analyze"; "reflection and summary" is mapped to "create". The strategy list "derive[s] from extensive analysis of MOOC instructional videos and in-depth discussions with experienced mathematics teachers" (§3.2) with no counts, no protocol, and no comparison with real transcripts such as TalkMoves (cited). "Better capturing authentic classroom interactions" (Abstract) is therefore unsupported: all dialogues are o1 outputs.
- **Suggested Fix**: compare move distributions with a real-classroom corpus, or reword to "pedagogically structured synthetic dialogues".

### W3: The three student levels are model-size proxies, not validated cognitive profiles
Table 5 builds students from Qwen2.5-32B, 14B and 7B bases, so "struggling" behaviour is partly smaller-model behaviour. No analysis shows these simulators produce the error patterns listed in Table 7 or Table 8 (e.g., "the expansion of (a+b)² is 2a+2b" appears only as a prompt example).
- **Suggested Fix**: annotate a sample of simulated student turns for error type and compare with published misconception taxonomies or real student data.

### W4: Scope is broader in wording than in content
Title and abstract say teacher–student dialogue and "intelligent education"; the data are K-12 mathematics only (§3.2). The base model for every experiment is one model (QwQ-32B-Preview), so "effectiveness of our approach" is demonstrated on one base and one subject.
- **Suggested Fix**: retitle/rescope, or add a second subject or base model.

### W5: Citation and background accuracy
The intro cites "MT-Bench (Bai et al., 2024)", but the bibliography entry is "Mt-bench-101: A fine-grained benchmark" (a different benchmark from the original MT-Bench). SocraticLM appears twice as Liu et al. 2024b and 2025a with an identical NeurIPS 37 entry. DPO is used but its source paper is not cited. AlpacaEval is described as assessing "multi-turn instruction-following" (§1); to my knowledge it targets single-turn instructions `[verify]`, so this is a question, not an error claim.

## Missing References
*Literature check unavailable (arXiv API unreachable): every entry is from knowledge, marked `[verify]`, and no identifiers are given. All are prior to the 2025-09-24 cutoff.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", NeurIPS 2023 `[verify]` | The method used for the DPO stage is uncited, and Eqs. 3–5 differ from it |
| Important | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks `[verify]` | The MT-Bench the paper names; standard reference for LLM-judge bias and agreement analysis |
| Important | Panickssery et al., "LLM Evaluators Recognize and Favor Their Own Generations", NeurIPS 2024 `[verify]` | Self-preference bias is relevant because o1 data and GPT-4o verification/judging overlap |
| Important | Maurya et al., an evaluation taxonomy for the pedagogical ability of LLM tutors with human/judge agreement (NAACL 2025) `[verify]` | Closest prior tutor-evaluation rubric work |
| Important | Macina et al., "Opportunities and challenges in neural dialog tutoring", EACL 2023 `[verify]` | Prior study of LLM tutoring dialogue properties and evaluation |
| Helpful | Jurenka et al., "Towards Responsible Development of Generative AI for Education: An Evaluation-Driven Approach", 2024 `[verify]` | Tutor evaluation with educators |
| Helpful | Tack and Piech, "The AI Teacher Test: Measuring the Pedagogical Ability of Blenderbot and GPT-3 on Educational Dialogues", BEA 2022 `[verify]` | Early pedagogical-ability rating protocol |

### Literature-check addendum (knowledge-only, since the search failed)
| Claim | Type | Novelty | Closest prior (all `[verify]`) | Reasoning |
|-------|------|---------|-------------------------------|-----------|
| C1 corpus | resource | medium-incremental | MathDial (cited), SocraticLM data (cited as baseline) | Same task and generation pattern; new = five-stage plus ten strategies plus three student levels |
| C2 SFT+DPO teacher | method | incremental | standard SFT and DPO | Recipe is standard by the authors' own statement (§3.4) |
| C3 11-dim rubric | resource | incremental | tutor-evaluation taxonomies, MT-Bench-style judging | Rubric is a reasonable combination; no validation novelty |

No candidate for "known results presented as new". No baseline scout table (no search results). Field snapshot (knowledge only, `[verify]`): 2023–2025 work on LLM tutoring moved from small human-annotated corpora (CIMA, TalkMoves) to LLM-simulated corpora (MathDial, SocraticLM) and to judge-based tutor evaluation; what counts as significant now is validated pedagogical evaluation (learning gains or expert-validated judges) and controlled data comparisons, not a larger synthetic corpus.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in controls and validation |
| Clarity | 3 | Clear gap and structure |
| Significance | 3 | Useful resource if validated |
| Originality | 2 | Incremental design variation |

## Dimension Scores (0–100)
**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental over existing LLM-simulated tutoring corpora, with the novelty claim untested against them.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Pedagogical mapping loose; citation errors |
| Clarity & Presentation | 62 | Competent | Clear positioning |
| Novelty & Originality | 46 | Developing | Incremental (W1) |
| Significance & Impact | 52 | Developing | Niche, real audience |
| Experimental Validation | 44 | Developing | No data-level comparison |
| Reproducibility | 52 | Competent | Prompts and Table 5 present |
| Ethical Compliance | 55 | Competent | Basic |

## Questions for Authors
1. How does EduDial differ from SocraticLM's training data in size, student types and question types, and what happens if you train the same base on that data? (A controlled result would move me up a point.)
2. How were the ten strategies derived from MOOC videos (how many videos, who coded them)?
3. Are the simulated students validated against real student errors?

## Limitations Assessment
**No.** There is no limitations discussion of simulation realism, subject scope or single-base results.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a coherent, well-motivated design whose novelty over existing corpora and whose central "data quality" claim are untested.

## Confidence
**4**: confident on positioning; prior-work descriptions are from memory and marked `[verify]`.

---

# Peer Review Report: Reviewer 3 (Perspective)

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Reviewer: Dr. Rafael Quispe-Dunmore, Perspective Reviewer (school of education, public university, South America; fictional persona)
## Expertise: classroom discourse, formative assessment, learning sciences
## Date: 2026-11-10

## Summary
The paper proposes a synthetic corpus and a tuned teacher model that asks stage-appropriate questions of three simulated student levels, and a rating framework for teaching quality. It is an interesting attempt to bring Bloom/ZPD ideas into LLM tutoring data, and could become more valuable with outcome-based validation.

## Strengths
### S1: Pedagogy is taken seriously as a design input
The stage-wise question strategies (Table 6) and the strategy-per-student-level table (Table 8) turn well-known classroom practice into explicit, inspectable prompts.

### S2: A multi-dimensional rubric rather than a single score
Table 1's dimensions (insight, feedback, emotional support, adaptability) go beyond answer correctness, which matters for tutoring and is rare in dialogue benchmarks.

### S3: Human raters and machine raters are both reported
Table 2 reports M and H columns, and §4.3 reports Pearson 0.90 and Spearman 0.91 between them over 18 models; ranking agreement at that level suggests the judge orders systems plausibly.

### S4: The case study is instructive
The "Normal Distribution" comparison (Appendix A.2) shows the intended behaviour difference (eliciting prior knowledge vs. presenting the formula).

## Weaknesses

### W1: No outcome or learner-facing evidence
All evidence is ratings of simulated dialogues by experts and GPT-4o. There is no measure of student understanding (a simulated post-test, learning gain, or teacher-reported usefulness), so "more targeted teaching guidance" (Abstract) is not measured. Some rubric items reward surface behaviours, e.g., the Interactivity dimension (Table 1, "frequency and quality of interactions") when the data teach the model to ask on average 14.2 questions per dialogue (§3.6); the Response item in the appendix prompt rewards "recommends relevant resources". Excessive questioning is something a teacher may regard as a defect (the paper's own §1 notes frequent questioning can disrupt comprehension).
- **Suggested Fix**: add a small teacher-in-the-loop study (e.g., 10 teachers rating preference between pairs) and a simulated-learner post-test.

### W2: Differentiated teaching by ability label carries equity risks that are not discussed
The "confidence-building strategy" for struggling students emphasises "repeated explanation of basic knowledge" (appendix, pp. 17–19). Systematically lowering challenge for students labelled struggling can entrench low expectations; the model also needs to infer the level from a few turns. The ethics statement concludes the design "eliminat[es] privacy concerns" and mitigates bias, but there is no bias analysis of the simulated personas or the generated feedback.
- **Suggested Fix**: add an analysis of whether the model's challenge level tracks inferred ability too strongly, and a limitations paragraph on equity and on misclassifying students.

### W3: The judge-validation is overstated as "reliability"
Correlation across 18 model means (§4.3) tests whether the judge ranks systems as humans do, not whether it is reliable on individual dialogues. Table 2 itself shows large cell-level gaps: Llama-3.3-70B-Instruct RES 3.08 (M) vs 1.97 (H); GPT-4o EMO 3.47 vs 2.80; Qwen-2.5-72B-Math INS 2.02 vs 3.06. The five experts' qualifications and agreement are not given. Yet the paper concludes "we employ machine ratings as the primary assessment method in subsequent experiments" (§4.3).
- **Suggested Fix**: report scenario-level agreement and expert inter-rater agreement, with expert background.

### W4: Cross-disciplinary assumption: Bloom's linear stages
Classroom discourse research treats questioning timing as responsive to student state rather than a fixed five-stage script; the paper's own first challenge ("optimal timing for teacher questioning", §1) is solved by a fixed sequence of stages, not by adaptive timing.
- **Suggested Fix**: analyse whether the trained model deviates from the stage script when students' answers warrant it.

### W5: Data provenance
Textbook-derived content and outputs of commercial models (o1, GPT-4o) are used for training; no licence, terms-of-use or copyright discussion is given. The language of the dialogues is not stated.
- **Suggested Fix**: add a datasheet.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Validation gaps |
| Clarity | 3 | Accessible |
| Significance | 3 | Real application relevance |
| Originality | 2 | Design is a combination of familiar classroom ideas |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: relevant application and thoughtful rubric, but no outcome or educator validation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Evidence is rating-only |
| Clarity & Presentation | 65 | Competent | Accessible |
| Novelty & Originality | 50 | Developing | Combination of known ideas |
| Significance & Impact | 56 | Competent | Education is an impactful domain, if validated |
| Experimental Validation | 44 | Developing | No outcome measure |
| Reproducibility | 55 | Competent | Prompts released in appendix |
| Ethical Compliance | 48 | Developing | Thin ethics, equity not discussed |

## Questions for Authors
1. Did any practising teachers review the generated dialogues or model outputs beyond the five raters?
2. Does the model's questioning density adapt to the student, or is it uniformly high?
3. What are the licence and terms for releasing o1/GPT-4o-derived data?

## Limitations Assessment
**No.** Simulation validity, equity and outcome evidence are missing.

## Ethics Review Flag
**No.** No human data; the concerns above are limitations, not review-worthy violations.

## Overall Score
**3 (Borderline Reject)**: a promising application with the right rubric ambitions, but without outcome evidence or educator validation.

## Confidence
**3**: strong on pedagogy; less checked on training details.

---

# Peer Review Report: Reviewer 4 (Generalist)

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Reviewer: Dr. Sung-Min Aaltonen, Generalist Reviewer (ML department, research university, Northern Europe; fictional persona)
## Expertise: language models, representation learning (not tutoring)
## Date: 2026-11-10

## Summary
The paper's contribution in one paragraph: a synthetic, pedagogically structured corpus for math tutoring dialogues, a 32B teacher trained on it with SFT+DPO, and an 11-dimension rating scheme; the trained model scores best on average among 18 LLMs under human and GPT-4o rating.

## Strengths
### S1: A clearly framed problem
§1 states two concrete challenges (timing and strategy of questioning), and Figures 1–3 (judged from captions) illustrate single-turn versus multi-turn teaching, the pipeline and the DPO data construction.

### S2: Complete pipeline from data to model to evaluation
Generation prompts (Appendix, pp. 16–19), training settings (Table 5, §4.1) and the evaluation prompt (Appendix, pp. 20–22) are all given, which helps a non-specialist follow the work.

### S3: Useful ablation structure and honest reasoning check
Table 3 isolates SFT and DPO; Table 4 reports the Math500/AIME2024 cost.

### S4: Large gap over the same base model
QwQ-32B-Preview AVG 2.75 → EduDial-LLM 4.47 (machine, Table 2) is a large effect compared with the 0.28 margin over the best baseline.

## Weaknesses

### W1: The abstract overstates what Table 2 shows
"consistently outperforming all baselines across all metrics" (Abstract) is not what Table 2 shows; e.g., content quality is lower than several baselines (COV 91.83 vs 96.16 for Gemini-2.0-Flash-Exp, machine). The §4.2 sentence "our scores match the best baseline models" is also too generous for COV. The balanced claim, highest average on nine overall-quality dimensions, is still notable.
- **Suggested Fix**: reword the abstract and conclusion ("consistently achieves superior performance across all evaluation dimensions", §5).

### W2: Venue fit as a dataset/benchmark contribution is weakened by the evaluation design
ICLR's bar for a dataset/benchmark paper is a validated measure and a fair comparison. The evaluation is a single interactive protocol with 36 scenarios per model and no release of a fixed test suite is described; the benchmark claim ("developing a benchmark", §1) depends on stable student simulators that are not specified.
- **Suggested Fix**: release the 36 scenarios, student simulators and judge prompts, and report run-to-run noise.

### W3: Presentation of results hides the per-dimension picture
Table 2 is a dense 12-column, two-rater table with no bolding of best entries, so the reader cannot see where the model loses (EMO, RES, FLU, COV). Table 3 does not say which rater it uses.
- **Suggested Fix**: bold best/second best, add a per-dimension rank column, and state rater type in captions.

### W4: The Table 4 trade-off is framed as acceptable without a baseline
A 10-point AIME2024 drop (43.33→33.33) and −3.58 on Math500 (derived) are called "slightly below the baseline ... within the expected range". Math accuracy matters for a math tutor: an incorrect hint is a pedagogical failure, and Table 2 does not measure correctness separately.
- **Suggested Fix**: add a correctness-of-explanations metric and compare with a model that only receives SFT/DPO LoRA with a smaller learning rate or reasoning-preserving mixing.

**Minor**: "18 ... baselines" vs 17 (§4.1); §4.3 heading mixes ablation with judge validation; typos ("mutil-turn", Figure 1 caption; "Reprodicibility statement").

### Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported | Partly (abstract claim contradicted; test-set selection) | Abstract, §4.1, Table 2 |
| Presentation | Met with gaps | §3–4, Table 2 |
| Contribution: new resource that others can use | Partly (release promised) | Reproducibility statement |
| Reproducibility | Partly | Table 5, appendix prompts |
| Honest limitations | Not met (no limitations section) | — |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation gaps |
| Clarity | 3 | Easy to follow |
| Significance | 2 | Narrow validation |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear pipeline and a real gap over the base model, but an overstated headline claim and an unvalidated evaluation put it on the rejected side of a typical dataset paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Standard recipe, thin controls |
| Clarity & Presentation | 60 | Competent | Clear but dense tables, overclaim wording |
| Novelty & Originality | 48 | Developing | Incremental |
| Significance & Impact | 52 | Developing | Niche but real |
| Experimental Validation | 42 | Developing | Single run, no variance |
| Reproducibility | 52 | Competent | Details mostly present, release promised |
| Ethical Compliance | 55 | Competent | Basic |

## Questions for Authors
1. Will the 36 test scenarios and student simulators be released unchanged? (Yes would raise my Significance.)
2. Why is COV, which is the easiest dimension to measure objectively, lower than that of several baselines?
3. Would the ranking hold if the judge were not an OpenAI model?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: reasons to reject (overclaiming, unvalidated evaluation) slightly outweigh a clear, useful pipeline.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Reviewer: Dr. Idris Valcourt-Nair, Devil's Advocate (statistics and evaluation methodology group, North America; fictional persona)

## Steelman
A carefully structured, curriculum-anchored synthetic corpus plus preference data teaches a 32B model to teach in a student-adaptive, question-driven way. Under both human and GPT-4o ratings it has the highest average among 18 models, with a large margin over its own base (2.75→4.47), at a modest cost to math reasoning.

## Core Argument Chain
1. P1: Good teaching is multi-turn, stage-structured questioning adapted to student level (§1, §3.2).
2. P2: EduDial encodes this structure (Tables 6–8), so training on it transfers it (§3.3–3.4).
3. P3: The 11-dimension rubric, scored by GPT-4o and validated by correlation with five experts, measures teaching ability (§3.5, §4.3).
4. P4: EduDial-LLM scores highest, and the ablations show SFT and DPO each contribute (Tables 2–3).
5. P5: The gain is due to data quality, not to algorithmic choices (§3.4).
∴ EduDial-LLM is "consistently" better at teaching across all metrics (Abstract).

## Strongest Counter-Argument
Even if every number were correct, Table 2 cannot support the conclusion, because the chain is circular at three points. First, P2→P3: the rubric rewards what the data teach. Interactivity is "the frequency and quality of interactions" (Table 1), and the training dialogues were generated from prompts that require stage-wise questioning with "at least two rounds of dialogue per phase" (appendix prompt); the model is trained to ask 14.2 questions per dialogue (§3.6). Baselines are, as far as the paper states, not given this scaffold, so a low score for plain o1 (AVG 3.47 machine) versus 4.47 for a model trained on o1's own structured outputs mostly shows that o1 was not told to teach in this style. Second, the judge: GPT-4o performs "automatic verification" of the training data (§3.3) and also scores the output (§3.5), and the data generator o1 is one of the evaluated baselines; no non-OpenAI judge is used, and "five experts" are given no qualification or agreement statistic. The 0.90 correlation is computed over 18 model means, where a few terrible models (Qwen-2.5-72B-Math, Llama) drive the correlation, and cell-level gaps reach 1.11 points. Third, the evaluation is run with simulated students whose identity is not stated (§3.6); if they are the EduDial-trained simulators of Table 5, the test distribution is the training distribution. On top of that, every hyperparameter was selected on the test chapters (§4.1). The comparison that would test P5, the same base trained on another corpus or the baselines given the same pedagogical prompt, is absent. What the evidence supports is a narrower claim: fine-tuning on structured, in-style synthetic dialogues makes a model score higher on a rubric aligned with that style, as judged by a related model.

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Integrity of evaluation (criterion 3) | §4.1; §3.6; Tables 2–4 | "All hyperparameters are empirically determined via grid search on the test set." The reported split is the 36-chapter test set; §3.6 describes no validation split; the selected configuration produces the Table 2 row that is quoted in the abstract. The best-scoring grid point is by construction chosen on those scores, and no sweep is shown to establish that the comparison with baselines (4.47 vs 4.19 machine, 4.36 vs 4.22 human) holds at other values. Per decision-table row 3, selection on the reporting split of the headline configuration. | Hold out validation chapters from the 137 training chapters, redo selection there, rerun Tables 2–3 once on the test chapters. | New data/experiments (re-selection and rerun) |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Claim distortion (E5) | Abstract; §4.2; Table 2 | "consistently outperforming all baselines across all metrics" is contradicted for RES, EMO, FLU, REL and COV (e.g., 91.83 vs 96.16 COV). Weaker claim (highest AVG) survives, hence MAJOR not CRITICAL. | Narrow the claim |
| DA-M2 | Construct validity | §3.3, §3.5, Table 1, §4.1 | Circularity: rubric and training prompts share the questioning scaffold; GPT-4o verifies training data and judges outputs; o1 generates data and is a baseline; students unspecified. | Independent judge family, fixed external students, blind human pairwise preferences |
| DA-M3 | Missing controls | §3.4, §4.1, Table 2 | No same-base training on other corpora; no prompted-with-scaffold baselines; baselines' prompts not stated. The statement "performance gains stem from data quality" is untested. | See R1-W5 |
| DA-M4 | Uncertainty | Table 2, Table 4 | No variance anywhere; 0.14 human margin; 10-point AIME drop called slight. | CIs, seeds |
| DA-M5 | Scope/claims | Abstract, §3.2, §3.6 | "34,250 dialogue sessions" mixes 13,700 dialogues and 20,550 preference pairs; "authentic classroom interactions" for o1-generated text; math-only scope. | Report counts separately; reword |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Reporting | §4.1 vs Abstract | "18 ... baselines" is 17 |
| DA-m2 | Citations | §1; reference list | "MT-Bench (Bai et al., 2024)" points to the MT-Bench-101 entry; SocraticLM listed twice |
| DA-m3 | Equation | Eqs. 3–5 | No β or reference policy though β=0.1 is stated |
| DA-m4 | Table 3 | Table 3 vs Table 2 | Base AVG 2.99 (mean) vs 2.75/2.53 |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Dataset size | 34,250 sessions | 13,700 + 20,550 = 34,250 | Yes, but 20,550 are preference pairs |
| Knowledge points | 345 | 275 + 70 = 345; chapters 137 + 36 = 173 | Yes |
| EduDial-LLM AVG (machine) | 4.47 | (4.58+4.12+4.62+4.55+4.64+4.10+4.60+4.43+4.56)/9 = 4.467 | Yes |
| EduDial-LLM AVG (human) | 4.36 | 39.28/9 = 4.364 | Yes |
| Margin over best baseline | not stated | 4.47−4.19 = 0.28 (M); 4.36−4.22 = 0.14 (H) | Derived |
| Base QwQ AVG (Table 3 vs 2) | 3.10/2.88/2.99 vs 2.75 (M), 2.53 (H) | row sums 27.91, 25.89, 26.89 over 9 | Rows internally consistent; do not match Table 2 |
| Table 4 | 91.12→87.54; 43.33→33.33 | −3.58; −10.00 | Drop larger than "slightly" implies |
| Compute | 45 h SFT | (2+3+5+5) epochs × 3 h = 45 | Yes |
| Baseline count | 18 baselines | 9 + 8 = 17 | No |

## Ignored Alternative Explanations
Style alignment (the model imitates the rubric-friendly style of its o1 teacher); judge self-preference/family bias; student-distribution match; question-count inflation lifting Interactivity/Thinking; baselines handicapped by unspecified prompts; hyperparameters tuned on test.

## Missing Stakeholder Perspectives
Teachers (are 14 questions per dialogue plausible in class?), students labelled "struggling", and parents/curriculum owners.

## Observations (Non-Defects)
Table 4 is an honest cost disclosure; hyperparameters and compute are reported; Table 3's internal AVG arithmetic is correct; DPO ablation numbers agree with the text description of where DPO helps.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 30 | DA-C1, equation mismatch |
| Clarity & Presentation | 58 | Overclaiming wording |
| Novelty & Originality | 42 | Incremental |
| Significance & Impact | 45 | Unvalidated measure |
| Experimental Validation | 28 | Circular evaluation, test-set tuning |
| Reproducibility | 45 | Evaluation setup incomplete |
| Ethical Compliance | 50 | Thin |

**Pool position:** better than about 20% of submissions to ICLR (accepted share ≈ 27%).

## Overall: 2 | Confidence: 4

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 baseline fairness | Rewritten | Original draft asserted students are EduDial simulators; the paper does not say, so it became a conditional ("if...") plus a question |
| R1 | Original draft "no code or data released" | Dropped | Reproducibility statement promises release; supplement/links not provided, so unverified, not missing |
| R2 | "SocraticLM already contains multi-level students" | Rewritten to question/`[verify]` | Not verifiable from the paper or search; novelty statements about prior work must match that work's abstract |
| R2 | "AlpacaEval is single-turn" | Moved to Questions-level wording in W5 | Cannot be checked against the paper or a kept abstract |
| R3 | Ethics-statement thinness | Kept, merged into W2/W5 | Specific quote and location exist |
| R3 | "No limitations section" | Moved to Minor/Limitations Assessment | Cosmetic relative to substantive issues |
| R4 | Typos | Moved to one Minor line | Cosmetic |
| DA | Table 3 vs Table 2 | Kept as MINOR | Medium confidence; extraction layout |
| All | "Single seed" as a standalone weakness | Reordered below W1/W2 | Ordered by severity; scale of the experiment allows reruns of evaluation, so kept |

Scores were not changed in this step.

---

## Phase 2: EIC Meta-Review and Decision

### Synthesizer Part A: Package

**Issue map.**
| Issue | Sources | Class |
|-------|---------|-------|
| Test-set selection | R1-W1/ERR-1, DA-C1 | DA-CRITICAL (also CONSENSUS-2 in substance) |
| Abstract claim vs Table 2 | R1-W2, R4-W1, DA-M1 | CONSENSUS-3 |
| Baseline fairness / missing controls / students unspecified | R1-W5, R2-W1, DA-M3 | CONSENSUS-3 |
| Judge validity and circularity | R1 (Q), R3-W3, DA-M2 | CONSENSUS-3 |
| No variance / uncertainty | R1-W4, R4-W4, DA-M4 | CONSENSUS-3 |
| Table 3 vs Table 2 mismatch | R1-W3, DA-m4 | CONSENSUS-2 |
| Equation/DPO mismatch | R1-W6, DA-m3, R2-W5 (DPO uncited) | CONSENSUS-3 |
| No outcome or educator validation | R3-W1, DA (counter-argument) | CONSENSUS-2 |
| Equity/ethics thinness | R3-W2/W5 | SOLO |
| Student levels as model-size proxies | R2-W3 | SOLO |
| Pedagogical grounding of Bloom mapping | R2-W2 | SOLO |
| SPLIT | R3-S3 praises judge validation, R1/DA criticise it | SPLIT |

Hinge issues: DA-C1, the abstract claim, judge circularity.

**Official score** (aggregate_scores.py, BEFORE run, no EIC weights, DA-C1 provisionally upheld): official mean rating 2.60; before composite 48.6 → band 2 (Reject); EIC-weighted rating 2.59 with equal weights → starting point 3.

### EIC Meta-Review (Dr. Helena Okonkwo-Vance)

# Editorial Decision

## Paper: EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: dataset
## Review Team (fictional): EIC (meta-reviewer) Dr. Helena Okonkwo-Vance; R1 Methodology Dr. Tomasz Heilmann; R2 Domain Dr. Mei-Ling Arvanitis; R3 Perspective Dr. Rafael Quispe-Dunmore; R4 Generalist Dr. Sung-Min Aaltonen; DA Dr. Idris Valcourt-Nair

## Decision: Reject (2)

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60 · official composite 48.6
**EIC assessment** (internal): weighted rating 2.54 → starting point 3 · weighted composite 48.2 → band 2 (cross-check) · **DA ceiling**: 3 · **Final (EIC)**: 2
**ICLR (scale status: secondary)**: rating 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}); Soundness 1, Presentation 2, Contribution 2.

### The Case For and Against
- **For acceptance:** A transparent, curriculum-anchored recipe (prompts, strategy tables, hyperparameters) for pedagogically structured synthetic tutoring dialogue, a sensible DPO preference construction, and a large gap over the model's own base (AVG 2.75→4.47); the authors also report the reasoning cost (Table 4).
- **Against acceptance:** Every headline number comes from a test set on which all hyperparameters were tuned (§4.1); the abstract's "all metrics" claim is contradicted by Table 2; the evaluation is circular (rubric aligned with the training scaffold, a GPT-4o judge that also verified the data, o1 both generator and baseline, unspecified student simulators); there is no variance, no controlled data comparison, and no outcome or educator validation.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Grid search on the test set | R1-W1, DA-C1 | §4.1 (quote present); §3.6 (train/test only) | **Verified** | No validation split anywhere; no sweep reported |
| "All metrics" claim contradicted | R1-W2, R4-W1, DA-M1 | Abstract; Table 2 | **Verified** | Recomputed: RES 4.12<4.63, EMO 4.10<4.67, FLU 4.43<4.67, REL 4.83<4.95, COV 91.83<96.16 (machine); human COV 88.29<94.84. AVG claim holds (4.47 vs 4.19; 4.36 vs 4.22) |
| §4.2 "our scores match the best baseline models" (content quality) | R1-W2, R4-W1 | §4.2, Table 2 | **Verified** (overstated by authors) | Human COV is below 9 of 17 baselines |
| Table 3 base AVG vs Table 2 | R1-W3, DA-m4 | Tables 2–3 | **Partly correct** | Mismatch holds against both M (2.75) and H (2.53); dimension-level comparison affected by extraction layout; severity MAJOR → MINOR/MAJOR boundary, treated as MAJOR with Medium confidence |
| Eqs. 3–5 vs β=0.1 | R1-W6, DA-m3 | Eqs. 3–5, §4.1 | **Verified** | Equations contain no β or reference policy; implementation may differ, which is itself the problem |
| Judge/data/generator overlap | DA-M2, R1-Q1 | §3.3 ("automatic verification by GPT-4o"), §3.5, §4.1 (o1 baseline) | **Verified** (facts); impact **unproven** | Overlap is stated in the paper; magnitude of bias is not measurable from the text |
| Students at evaluation time unspecified | R1-W5, DA-M2 | §3.6 | **Verified (omission)** | Whether they are Table 5's simulators is unknown: treated as a question, not as a finding |
| Judge "reliability" from Pearson 0.90 | R3-S3, R3-W3 | §4.3 | **Partly correct** | R3's strength S3 is **Overstated**; R3's weakness W3 is correct (cell gaps: Llama RES 3.08 vs 1.97) |
| Table 4 drop described as "slightly below" | R1-W4, R4-W4, DA-M4 | Table 4 | **Verified** | −3.58 and −10.00 points |
| "34,250 dialogue sessions" | DA-M5, R1 ERR-5 | Abstract; §3.6 | **Verified** | 20,550 are preference pairs |
| "MT-Bench (Bai et al., 2024)" vs bibliography entry | R2-W5, DA-m2 | §1; references | **Verified** | Entry is MT-Bench-101 |
| AlpacaEval is single-turn | R2-W5 | §1 | **Unverifiable from the paper** | Kept as a question; not counted against any reviewer |
| "SocraticLM already builds a simulated multi-agent corpus" | R2-W1 | §2 | **Unverifiable** (lit check unavailable) | Kept as `[verify]`; not used in the decision |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error-log entries ERR-1, 2, 4, 5, 6, 7 verified at their locations; decisive for the outcome; calibration fits the venue |
| R2 (Domain) | 3 | 4 | 1.00 | Sound, typical; prior-work statements unverifiable and correctly marked |
| R3 (Perspective) | 3 | 3 | 0.75 | Strength S3 treats the 18-model correlation as judge validation (overstated, contradicted by her own W3 evidence); did not catch test-set tuning |
| R4 (Generalist) | 3 | 4 | 1.00 | Sound overall; verified abstract-claim point; missed test-set tuning, expected for a generalist pass |
| DA | 2 | 4 | 1.00 | DA-C1 and DA-M1 verified; DA-M2 impact is conjecture, so no extra weight |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 (grid search on the test set) | Yes under criterion 3: the paper states it tuned on the held-out test set it reports, and disclosure is not a reason to downgrade. I searched for the quote: present verbatim in §4.1. The sweep table is not provided, so I cannot show the comparison holds at other grid values (decision-table row 3 vs row 2): the chosen configuration is by construction the best-scoring on that set and produces Table 2's headline row. No separate validation split exists (§3.6), which rules out the "not an issue" row. | **Upheld** | New experiments (re-selection on a validation split and one rerun on the test chapters) |

### Final Decision and Justification
The EIC-weighted rating (2.54) rounds to a starting point of 3, while the composite cross-check (48.2) sits in band 2 (⚠). I trust the composite here, and I depart one step from the starting point to **2 (Reject)** for named, verified issues that the 3-rated reports did not fully price in: (i) the test-set selection in §4.1, which R2, R3 and R4 did not raise and which invalidates the reported numbers until re-run (DA-C1, upheld); (ii) the abstract's "all metrics" claim, contradicted in five of eleven dimensions in Table 2 (R3 did not check it); (iii) a circular measurement chain (rubric, judge and training scaffold aligned; GPT-4o as verifier and judge; unspecified student simulators) that means even a clean re-run would not yet show that the data improve teaching rather than rubric-fit. The rating of 3 given by R2–R4 rests on a headline that Table 2 only partly supports. The decision does not exceed the DA ceiling of 3. **My pool position: better than about 25% of ICLR submissions** (deciding evidence: test-set selection plus unvalidated measurement in a dataset paper whose value is the measurement). R1/DA disagree with R3 by 22 pool points; I rule on the verified evidence above, not on the count. The resource itself has value and a corrected resubmission (validation-split tuning, an independent judge, a controlled data comparison, an honest abstract) could sit in the borderline range; I would weigh that favourably, as a first paper on structured tutoring data, once the evaluation is sound.

### Score Summary

#### Official scores and EIC assessment
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 38 | 48 | 52 | 48 | 30 | 43.2 | 42.2 | 22 ⚠ |
| Clarity & Presentation | 62 | 62 | 65 | 60 | 58 | 61.4 | 61.1 | 7 |
| Novelty & Originality | 45 | 46 | 50 | 48 | 42 | 46.2 | 45.8 | 8 |
| Significance & Impact | 48 | 52 | 56 | 52 | 45 | 50.6 | 50.0 | 11 |
| Experimental Validation | 35 | 44 | 44 | 42 | 28 | 38.6 | 38.0 | 16 |
| Reproducibility | 48 | 52 | 55 | 52 | 45 | 50.4 | 49.9 | 10 |
| Ethical Compliance | 55 | 55 | 48 | 55 | 50 | 52.6 | 53.1 | 7 |
| **Composite** | 46.7 | 51.0 | 52.5 | 50.8 | 42.0 | **48.6** (before) | **48.2** (after) | |
| Pool position | 30 | 35 | 42 | 38 | 20 | | | |

Reviewer-weight shares of the EIC assessment: R1 26%, R2 20%, R3 13%, R4 20%, DA 20%. Spread discussion: Technical Rigor (22 ⚠) diverges because R1 and DA weigh test-set tuning and the equation mismatch as rigor failures, while R2–R4 score rigor on the recipe's standard form; the editor adopts the lower view, since the test-set selection is verified. (A first scoring pass flagged R1's pool position (25) as inconsistent with a composite of 46.7; it was moved to 30 before the runs reported here, with no dimension score changed.)

#### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}); venue-weighted composite 48.0 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "EduDial: Constructing a Large-scale Multi-turn Teacher–Student Dialogue Corpus" to ICLR. Structured, pedagogically informed tutoring data for LLMs is a worthwhile direction, and the paper shares its prompts and settings openly.

**Overall Assessment:** The panel found a coherent design and a large improvement over the base model, but could not accept the headline evidence as it stands: the selection of all hyperparameters on the test set, an abstract that claims superiority on all metrics where Table 2 shows losses, and an evaluation whose rubric, judge and student simulators are not independent of the training data.

**Key Strengths Identified by Reviewers:**
1. A transparent five-stage, ten-strategy, three-student-level scaffold with prompts and training settings in the appendix (R1, R2, R3, R4).
2. A preference set that encodes strategy adherence, and an ablation grid showing where SFT and DPO help (R1, R2, R4).
3. A multi-dimensional teaching rubric and honest reporting of the reasoning cost in Table 4 (R3, R1).

**Key Concerns Requiring Attention:**
1. Hyperparameter grid search on the test set (§4.1); all headline numbers must be re-derived (R1, DA; DA-CRITICAL).
2. The abstract's "all metrics" claim versus Table 2 (R1, R4, DA; CONSENSUS-3).
3. Circular/underspecified evaluation and missing controls: no same-base comparison on other corpora, no prompted baselines, unspecified students, GPT-4o as verifier and judge (R1, R2, DA; CONSENSUS-3).
4. No variance or uncertainty; no outcome or educator validation (R1, R3, R4, DA).

**Critical Challenge (Devil's Advocate):** the model may be learning the rubric-friendly style of its o1 teacher, so higher scores need not mean better teaching; only an independent judge, fixed external students and a controlled data comparison can distinguish the two.

**Decision: Reject (2).** This is the panel's view of this draft, not a prediction. A resubmission that re-selects hyperparameters on a validation split, narrows the claims, adds the controls and independent evaluation described in the Roadmap, and documents the dataset would be assessed afresh.

Sincerely,
Dr. Helena Okonkwo-Vance
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Abstract/"all metrics" claim not supported by Table 2 | R1, R4, DA | CONSENSUS-3 |
| Missing controls / unfair or undefined baseline setup | R1, R2, DA | CONSENSUS-3 |
| Judge validity and circularity | R1, R3, DA | CONSENSUS-3 |
| No variance or uncertainty | R1, R4, DA | CONSENSUS-3 |
| DPO equation/description mismatch and missing DPO citation | R1, R2, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Judge validated by 0.90 correlation | R3 (S3) | R1, DA | Correlation over 18 model means shows ranking agreement only; cell gaps up to 1.11 (Table 2); R3's view is overstated |
| Overall level | R2, R3, R4 give 3 | R1, DA give 2 | Verified test-set tuning and the contradicted headline favour 2; starting-point rounding (2.54→3) is within 0.04 of the x.5 boundary and the composite band is 2 |

### Score Spread Discussion
Technical Rigor spread of 22 ⚠: see above; editor adopts the lower view for the verified issues.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Hyperparameter grid search on the test set | Yes (R1) | Upheld | New experiments |
| DA-M1 | MAJOR | "All metrics" claim contradicted | Yes (R1, R4) | n/a | n/a |
| DA-M2 | MAJOR | Circular evaluation | Partly (R1, R3) | n/a | n/a |
| DA-M3 | MAJOR | Missing same-base data control and prompted baselines | Yes (R1, R2) | n/a | n/a |
| DA-M4 | MAJOR | No uncertainty | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Dataset-count and "authentic" wording, math-only scope | Partly (R1, R2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Test-set hyperparameter/checkpoint selection | DA-C1, R1-W1 | §4.1; Tables 2–4 | Hold out validation chapters from the 137 training chapters; redo the grid there; rerun Tables 2–3 once on test chapters; report the sweep | High; ≈53 GPU-h per configuration (45 h + 8 h, §4.1) × grid size | Partly (reduced grid on a smaller base) |
| R2 | Abstract/conclusion claim contradicted by Table 2 | DA-M1, R1-W2, R4-W1 | Abstract; §4.2; §5 | Reword to "highest average over nine overall-quality dimensions"; add per-dimension ranks; discuss losses on EMO, FLU, RES, COV | Low | Yes |
| R3 | Evaluation validity (circularity) | DA-M2, R1-W5, R3-W3 | §3.3, §3.5, §3.6, §4.3 | Fixed, released student pool; non-OpenAI judge; expert agreement and scenario-level human–judge agreement; blind pairwise human preference | High; API cost plus rater time | Partly |
| R4 | Controls for "data quality" claim | DA-M3, R1-W5, R2-W1 | §3.4, Table 2 | Same-base training on MathDial/SocraticLM data; baselines prompted with the MTI template | High; ≈53 GPU-h per corpus | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Variance and uncertainty | R1-W4, DA-M4 | Bootstrap over scenarios, repeat judge spread, ≥3 seeds on a smaller base, CI on Table 4 | Medium | Partly |
| S2 | Table 3 vs Table 2 mismatch; rater type | R1-W3 | Reconcile and label | Low | Yes |
| S3 | DPO objective and citation | R1-W6, R2-W5 | Give exact objective; cite DPO | Low | Yes |
| S4 | Dataset documentation and scope | DA-M5, R2-W4, R3-W5 | Datasheet (licence, language, verification pass rates, expert qualifications), report dialogues and pairs separately, rescope title/abstract to math | Medium | Yes |
| S5 | Pedagogical validation | R3-W1, R2-W2, R2-W3 | Teacher-in-the-loop study; student-simulator error validation; compare move distributions with real transcripts | High | Partly |
| S6 | Missing references | R2 | DPO (Critical `[verify]`); MT-Bench; LLM self-preference; tutor-evaluation taxonomies | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Equity analysis of ability-labelled strategies | R3-W2 | Add a limitations/equity paragraph |
| N2 | Citation slips and counts | R2-W5, DA-m1/m2 | Fix MT-Bench vs MT-Bench-101, duplicate SocraticLM entry, "18 baselines" |
| N3 | Table formatting | R4-W3 | Bold best/second-best; add rank column |
| N4 | Stage-order rationale | R2-W2 | Justify the analyze-before-apply ordering |
| N5 | Math-accuracy cost | R4-W4 | Add a correctness metric and a reasoning-preserving training variant |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 2–4 weeks (re-tuning, independent judge, controls).
- Priority 2: 6 items, roughly 1–2 weeks.
- Priority 3: 5 items, days.
- **Total estimated revision time**: about 4–6 weeks.

*Gap Scout (post-review analysis) was not requested and was not run.*
