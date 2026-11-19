# Academic Paper Review: Adversarial Reinforcement Learning for Large Language Model Agent Safety

**Date:** 2026-11-10 · **Mode:** full · **Target venue:** ICLR (stated by user) · **Literature check:** strict, cutoff 2025-09-24 · **Execution note:** all five reviewer passes and the EIC pass were run sequentially by one model in a shared context (no subagents); they are role-based perspectives, not independent agents. Figures were not available as images: Figures 3, 4 and 6 (heat maps) were read as extracted text (numbers legible, column labels partly garbled); Figures 1, 2, 5, 7 (diagram, UMAP, APD curve) were judged from captions and text only.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Adversarial Reinforcement Learning for Large Language Model Agent Safety |
| Primary Discipline | ML → LLM agent security (indirect prompt-injection defense) via multi-agent RL post-training |
| Secondary Discipline(s) | Multi-agent RL / self-play; automated red-teaming; web agents |
| Paper Type | Empirical (method + benchmark evaluation); composite weights: empirical |
| Core Technique(s) | Attacker–agent co-training with GRPO, SFT warm-up from larger teachers, population-based opponent sampling, LoRA |
| Target Venue | ICLR (stated); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none; ICLR form: Soundness / Presentation / Contribution, Rating, Confidence |
| Paper Maturity | Submission-ready (complete 9-page body + appendix; thin evaluation section) |
| Ethics-Relevant Content | Dual-use: trains an LLM that generates effective prompt injections (Sec. 3, App. A); synthetic private data only; no human subjects |

**Integrity scan** (`integrity_scan.py`, reviewer copy written to `reviewer_copy.txt`): no reviewer-directed text or hidden characters found. Reading found none either. Anonymity note for the editor only (no score effect): the first-page footnote and Section 6 contain affiliation/conflict-of-interest wording that may breach double-blind formatting; the Submission-Readiness point is mentioned once in R4's Minor line.

### Claimed Contributions (as stated by the authors, Section 1)
1. **C1** ARLAS: an adversarial RL framework that co-trains an attacker and an agent, "enabling the automatic discovery of diverse attacks".
2. **C2** Population-based training: the agent is optimized against all previous attacker checkpoints for "robust defense against a wide spectrum of attack patterns".
3. **C3** On BrowserGym and AgentDojo ARLAS "significantly reduces attack success rates while maintaining high task completion".
4. **C4** Analysis showing the adversarial process generates "an increasingly diverse set of attacks" (Sec. 4.3).

### Paper Memory (factual record shared with all reviewers)
- **Setup facts.** Models: Gemma3 12B and Qwen3 14B (Sec. 4). Environment: BrowserGym, simplified-HTML/AXTree text observations (Sec. 4.1); episode max length L = 5 (Table 2). Synthetic user info; leakage = string match of "any subset" of the private info in generated tool parameters (Sec. 3.1, 4.1). Imitation data: 10K episodes from Gemma-3-27B / Qwen-3-32B teachers, filtered to successful episodes (Sec. 4.1, B.1). RL: 128 training tasks × 16 episodes (Table 2), "subset of solvable tasks … Gemma-3-27B achieved … >20%" (App. B.1); GRPO with LoRA r=128 (Table 3). Evaluation: "unseen test tasks" of BrowserGym (Sec. 4.1/4.2; count and identity **not stated**); AgentDojo as out-of-distribution transfer (suite, attack type, ASR definition **not stated**). Seeds: "3 random seeds" (Fig. 3, 4, Table 1; what varies **not stated**). Compute, N_iter, N_epi, G: **not stated**. Code/data link: **not stated** after search.
- **Headline numbers.** Fig. 4: average ASR 19 (base) → 12 (ARLAS); ARLAS attacker reaches 55% ASR against the base agent. Table 1: Gemma3 ASR 6.3 → 5.4±0.1, TSR 24.4 → 25.8±0.1; Qwen3 ASR 1.6 → 1.4±0.1, TSR 30.2 → 31.2±0.8. Fig. 5 right: APD rises over RL stages (values not legible).
- **Appendix adds:** prompts and one example episode (A), hyperparameters (Tables 2, 3), the Qwen3 heat map (Fig. 6), a second UMAP (Fig. 7), LLM-assistance disclosure (C). No extra baselines, no per-task results, no safety evaluation of anything beyond string-match leakage.
- **Unverifiable:** all UMAP panels, Fig. 5 values, the column labels of Fig. 4 (garbled in extraction; identities inferred from the text and from the printed averages), Fig. 1/2 diagrams.

### Review Team (fictional personas; descriptive affiliations only)

**EIC (meta-reviewer): Dr. Marguerite Anselmi, senior faculty, large public research university (Western Europe).** Senior / ML security and learning-theory-minded RL; experienced ICLR area chair. Style: asks "what would the field lose?" and trusts verified evidence over tone.

**Reviewer 1 (Methodology): Dr. Tobias Lindqvist-Okoye, industrial research lab (Northern Europe).** Mid-career industry scientist / RL post-training for LLMs, evaluation protocols for agents. Style: recomputes every table, insists on matched baselines and variance.

**Reviewer 2 (Domain): Prof. Anselmo Ferreira-Duarte, ML-security group, public research university (South America).** Senior faculty / prompt-injection attacks and defenses, red-teaming with LLMs. Style: reads related work against the bibliography entry by entry.

**Reviewer 3 (Perspective): Dr. Mei-Ling Abara, systems-security and verification institute (East Asia).** Mid-career researcher / sandboxing, access control, security engineering for deployed software agents. Style: constructive; asks what an attacker or an operator would actually do.

**Reviewer 4 (Generalist): Dr. Odalys Rennick, applied NLP team, mid-sized technology company (North America).** Senior industry scientist / LLM post-training, program-committee regular. Style: judges clarity and fit, weighs weaknesses against what accepted ICLR papers usually carry.

**Devil's Advocate: Dr. Yevgenia Marlowe, statistical methodology department, medical school (North America).** Senior / evaluation methodology, causal inference, robustness. Style: rigorous, never hostile; goes after what the evidence does not show.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Reviewer Reports

---

# Peer Review Report

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Reviewer: Dr. Tobias Lindqvist-Okoye, Methodology (industrial research lab, Northern Europe; fictional persona)
## Expertise: RL post-training of LLMs; evaluation protocols for tool-using agents; statistical reporting
## Date: 2026-11-10

## Summary
The paper trains two LLMs, an attacker that writes prompt injections appended to web-page observations and an agent that must finish BrowserGym tasks without leaking synthetic user data. Both are warmed up by SFT on teacher demonstrations and then trained with GRPO, with the agent facing a uniformly sampled past attacker checkpoint (a "population"). Results are shown as agent-vs-attacker heat maps on held-out BrowserGym tasks (Fig. 3, 4, 6) and as a transfer test on AgentDojo (Table 1). A closing analysis reports embedding-space diversity of the attacks (Fig. 5).

## Protocol Sweep (Step 0)
Search of the full text including appendices for split/selection statements. Found: "unseen test tasks" (Sec. 4.1, 4.2); training tasks restricted to "a subset of solvable tasks" defined by Gemma-3-27B success >20% (App. B.1); 128 RL tasks (Table 2); evaluation stages "5, 10, and 15 training iterations" (Sec. 4.2). **Not stated after search:** the number and identity of test tasks, whether any validation split exists, how the "final model" used in Fig. 4 and Table 1 was chosen, how hyperparameters (Table 3) were selected, and what the 3 seeds vary. There is no statement of selecting on the reported split, so no leakage claim is made; the missing selection protocol is a Question (Q2).

## Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Automatic discovery of diverse, effective attacks | Sec. 1, 4.3 | Fig. 3/4 (attacker ASR 55% vs base agent), Fig. 5 | Partially: strength shown; diversity shown only as cumulative APD with no baseline attacker |
| C2 | Population-based learning gives robustness and prevents cycling | Sec. 3.3, 4.2 | Fig. 4 and Table 1 ablation vs "w/o PBL" | Partially: no evidence that cycling occurred; ablation attackers differ 4–5× in strength, which the method description does not explain |
| C3 | Significantly lower ASR, maintained TSR, on BrowserGym and AgentDojo | Abstract, Sec. 4.2 | Fig. 4, Table 1 | Supported on BrowserGym against strong attackers; Weak on AgentDojo (≤0.9 pt, no test) |
| C4 | Attacks become increasingly diverse | Sec. 4.3 | Fig. 5 right | Partially (see W3) |

## Strengths
### S1: A clean, well-specified training loop with a sensible warm-up
Algorithm 1, Eq. (1)–(2), Table 2 and Table 3 specify the pipeline (SFT on filtered teacher episodes, then GRPO with LoRA) well enough to re-implement it; the prompts of both players are given in Appendix A.

### S2: Informative agent-vs-attacker matrices
Fig. 3 and 4 report every agent against every attacker rather than a single number. This exposes that the agent gets safer against fixed attackers and that attackers get stronger against fixed agents. It is the most useful evaluation design in the paper, and the 3-seed standard errors are shown.

### S3: Two base models and an out-of-distribution transfer test
Gemma3 12B and Qwen3 14B (Sec. 4) and the AgentDojo transfer (Table 1) go beyond a single in-domain setup, and the Qwen3 result is honestly reported as a small effect (App. B.2, Sec. 4.2).

## Weaknesses
### W1: The main safety result is measured mostly against attackers produced by the method itself
In Fig. 4 (left) the attackers in rows are base, SPAG, ARLAS w/o PBL and ARLAS (ART is not a row although Sec. 4.2 says "against every other model"). The non-ARLAS attackers reach only 3–13% ASR, so the agents differ by a few points; essentially all separation comes from the ARLAS attacker (55 → 34). I recomputed the printed averages: base (2+9+11+55)/4 = 19.25, ARLAS (3+6+6+34)/4 = 12.25 (both match "19" and "12"). Excluding the ARLAS row, the average ASR is ≈7.3 for the base agent and ≈5.0 for the best agent. The headline "safest agent … regardless of the specific attacker faced" (Sec. 4.2) is therefore a statement about robustness to the method's own attacker. 
- **Suggested Fix:** add attackers the method never trained against: the human-written or template attacks of AgentDojo and other injection benchmarks, and an independently trained RL attacker. Cost: inference only, ≈ a few GPU-hours.

### W2: AgentDojo does not support the "significantly lower ASR" and "generalizes" claims
Table 1: Gemma3 ASR 6.3 → 5.4 (Δ = 0.9 pt), TSR 24.4 → 25.8 (+1.4); Qwen3 ASR 1.6 → 1.4 (Δ = 0.2 pt), TSR 30.2 → 31.2. The base-model rows have no ± while the others do, SPAG matches ARLAS exactly in ASR (5.4) and exceeds it in TSR (26.2), and no significance test is given. The abstract's "significantly lower attack success rate" and Sec. 4.2's "ARLAS effective generalizes to the unseen AgentDojo environment" are not backed by this table. The AgentDojo protocol (suite, attack, how "ASR" maps to the string-match leakage used in training) is also not stated.
- **Suggested Fix:** state the protocol; report paired bootstrap CIs over AgentDojo user/injection task pairs for base vs ARLAS vs SPAG; narrow the wording. Cost: Low.

### W3: The diversity analysis does not test the diversity claim
Eq. (3) defines APD over the cumulative union E^{1:i} of attacks from checkpoints 1..i. A union of samples from different checkpoints is more spread out than any single set even if every checkpoint is individually narrow, so a rising curve (Fig. 5 right) is expected by construction. There is no baseline (ART, SPAG, the SFT attacker's own diversity), no per-checkpoint APD, no error bars, only the stages "original SFT / RL iter 5 / RL iter 10" (Fig. 5 shows no iter 15), the plotted axis spans only 0.825–1.0, and embedding distance of whole prompts does not show distinct attack strategies. The paper's motivating claim (manual red-teaming limits diversity, Sec. 1) is never compared against.
- **Suggested Fix:** report per-checkpoint APD, the same metric for ART/SPAG/SFT attackers, and a strategy-level count (e.g., LLM-labelled attack types). Cost: Low.

### W4: The ablation changes more than the stated component; the PBL conclusion is under-identified
Sec. 3.3 says that in both settings the attacker is "paired exclusively with the latest agent", yet the attacker from ARLAS w/o PBL reaches only 6–13% ASR while the ARLAS attacker reaches 34–55% (Fig. 4). A less robust latest agent should make attacks easier, not weaker; either implementation details differ or training diverged, and no training curves are shown to demonstrate cycling in the baseline. Also in Table 1 SPAG, which is not population-based, matches ARLAS, which contradicts "training the agent against a population of attackers is critical" (Sec. 4.2). Finally, GRPO groups collect G episodes per task, but opponents are sampled per episode (Sec. 3.3), so group-normalised advantages mix opponent strength with action quality.
- **Suggested Fix:** training curves for both variants; fixed-opponent-per-group sampling; an ablation sampling uniformly vs from the most recent k checkpoints. Cost: Medium (≈ 1 rerun of RL per variant).

### W5: TSR gains are confounded with in-domain task training, and baseline coverage is thin
The base model is not fine-tuned on BrowserGym tasks; ARLAS adds SFT from 27B/32B teachers and 128 training tasks. The no-attack TSR rises 38 → 56 (Fig. 4 right), but a task-only variant is as good (a column at 59±1), so the TSR improvement says nothing about safety training. For defense, only automated-attack-trained variants are compared; no instruction-hierarchy or preference-optimization defenses trained on fixed injection data (the exact approach Sec. 1 argues against) and no deployment-style mitigations are included.
- **Suggested Fix:** add a baseline fine-tuned on the same teacher data with a fixed human/LLM-written injection set (e.g., a SecAlign/StruQ-style recipe), and report TSR relative to the task-only agent. Cost: Medium (≈ 1–2 days on the same hardware).

### W6: Reproducibility and statistics gaps
N_iter, N_epi, G, compute, number of test tasks, and what "3 random seeds" varies are not stated; standard errors of "±0" for many cells suggest evaluation-only seeds, which cannot show training stability for an adversarial game known to be unstable. No code link. The final-model choice is not specified (Fig. 3 reaches iteration 15; Fig. 5 stops at 10).
- **Suggested Fix:** report ≥3 independent training runs for at least the main Gemma3 configuration, or state clearly that seeds are evaluation-only; release code. Cost: ≈ 3× the RL training cost (not stated in the paper).

**Minor:** Eq. (2) prints `min(R·A, −clip(R,…)·A)` while stating that it is minimised; check the sign. Fig. 4 reports ASR averages over the four attacker rows but TSR averages over five rows including "no attack" (see ERR-3). Typos: "focuese", "seciton", "founed", "repeatition", "pretty safe".

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5/E2 | Sec. 3.1 (reward cases) vs. Abstract | "if the task fails or truncates" (both rewards are −1 in that case) vs "two-player zero-sum game" | In the task-fails case both players get −1 (sum −2); the game is not zero-sum as stated | Cross-referenced the reward cases (sums: 0, 0, −2) | High | MINOR (framing; no numbers affected) | Say "adversarial, non-zero-sum" or redefine rewards |
| ERR-2 | E7 | Sec. 2.2 vs References | "SPAG (Chen et al., 2024)" | The bibliography entry "Chen et al." is arXiv:2401.01335 (self-play fine-tuning, a different method); SPAG is Cheng et al. NeurIPS 2024 (used correctly in Sec. 4.1) | Cross-referenced text and bibliography | High | MINOR | Cite Cheng et al. in Sec. 2.2 |
| ERR-3 | E1/E6 | Fig. 4 (bottom rows) | "average 19 19 16 15 15 12" (ASR) and "31 44 44 47 48 48" (TSR) | ASR average omits the no-attack row; TSR average includes it: e.g., first column (38+31+34+38+15)/5 = 31.2 vs (31+34+38+15)/4 = 29.5 | Recomputed from printed cells | High | MINOR (ranking unchanged: 4-row TSR averages 29.5, 40.3, 42.3, 44.8, 45.8, 45.8) | Use one definition |
| ERR-4 | E5 | Abstract, Table 1 | "achieve a significantly lower attack success rate than the original model" | Table 1 gains: 0.9 pt (Gemma3) and 0.2 pt (Qwen3), no test; base rows have no ± | Recomputed 6.3−5.4, 1.6−1.4 | High | MAJOR | Narrow wording, add CIs |
| ERR-5 | E2 | Eq. (2) | "−clip(Rt,j , 1 − ϵlow , 1 + ϵhigh )At,j" (as extracted) | Sign inconsistent with a loss that "encourages actions that lead to higher-than-average final rewards"; probable typo | Read against standard clipped objective; extraction cannot rule out a rendering issue | Medium | MINOR | Check and correct |

## Missing References (Methodology view; the Domain Reviewer owns this list)
None additional.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Core gains are real vs strong attackers but measured on the method's own attackers; AgentDojo claim unsupported |
| Clarity | 3 | Method is easy to follow; protocol details missing |
| Significance | 2 | Timely, but evidence of real-world robustness is thin |
| Originality | 2 | Combination of known ingredients (self-play, opponent pool, GRPO) in a new application |

## Dimension Scores (0–100)
**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline robustness gain is against attackers the method trained itself, and the out-of-distribution transfer is ≤ 1 point without a significance test; both are typical of rejected submissions.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Non-zero-sum mislabeling, mixed-opponent advantage normalisation, ablation that does not isolate PBL |
| Clarity & Presentation | 66 | Competent | Readable; protocol gaps |
| Novelty & Originality | 54 | Developing | See R2 |
| Significance & Impact | 56 | Competent | Relevant problem; small, single-environment evidence |
| Experimental Validation | 44 | Developing | Own-attacker evaluation; weak baselines; negligible OOD effect |
| Reproducibility | 46 | Developing | Hyperparameters and prompts given; N_iter, test set, seeds, compute, code missing |
| Ethical Compliance | 60 | Competent | Synthetic data; no dual-use discussion |

## Questions for Authors
1. How many test tasks and episodes underlie Fig. 3/4 and Table 1, and what do the 3 seeds vary (training, evaluation, or both)? Training-seed variance with a few points of effect would change my view of W6.
2. How was the evaluated checkpoint chosen (iteration 15? best of 5/10/15?) and was any validation split used? A test-selected checkpoint would be a serious issue.
3. Why is the ARLAS w/o PBL attacker so much weaker than the ARLAS attacker if both pair the attacker with the latest agent? An explanation or a training curve could raise my Technical Rigor score.
4. What does "ASR" mean on AgentDojo, and which attack was used? How do AgentDojo's tool-call injection goals map onto string-matched leakage?

## Limitations Assessment
**Partially.** Sec. 5 acknowledges only model count and VLMs. Missing: single simulated environment with L=5, string-match leakage only, evaluation against own-method attackers, no discussion of the attacker model as a dual-use artifact.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject):** A reasonable pipeline whose central evidence is internal to the method and whose out-of-distribution evidence is negligible; fixable with inference-only experiments and a narrowed claim, but not as submitted.

## Confidence
**4:** I recomputed the tables I could read; Fig. 4 column labels were garbled in extraction.

---

# Peer Review Report

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Reviewer: Prof. Anselmo Ferreira-Duarte, Domain (ML-security group, public research university, South America; fictional persona)
## Expertise: prompt-injection attacks and defenses; LLM red-teaming; adversarial training
## Date: 2026-11-10

## Summary
The authors propose to harden a tool-using LLM agent against indirect prompt injection by training an LLM attacker and the agent jointly with RL, sampling from a growing pool of past attackers during agent training. They position this against fine-tuning on fixed attack sets and against evolutionary automated red-teaming, and show gains on a BrowserGym test split and a small gain on AgentDojo. Related work is a half-page and the novelty argument rests on automation of attacks and on population-based opponent sampling.

## Strengths
### S1: A well-chosen problem and a natural formulation
Indirect prompt injection is a leading practical risk for agents (Sec. 1, citing Greshake et al.), and learning the attacker rather than hand-writing mutations (Sec. 2.1) is a sensible way to avoid the template-diversity ceiling of fixed datasets.

### S2: A relevant baseline family is adapted fairly openly
SPAG, automated red-teaming with a frozen attacker, and ablations without population or adversarial learning are all included (Sec. 4.1), and the way the authors adapted SPAG (iterative learning, offline RL objective) is disclosed.

### S3: Sensible use of the opponent pool idea
Sampling uniformly from previous attacker checkpoints (Sec. 3.3, Fig. 2) is a straightforward remedy to forgetting in self-play, and the reasoning is stated clearly.

## Weaknesses
### W1: Related work omits the closest bodies of work, so the novelty delta is unclear
Sec. 2 cites two red-teaming papers and SPAG. It does not discuss adversarial-RL or self-play training of LLMs for safety (attacker/defender self-play for harmful-content safety; multi-round automatic red-teaming with adversarial fine-tuning; curiosity- and diversity-driven RL red-teamers), nor the established prompt-injection training defenses (structured-query fine-tuning, preference-optimization defenses, instruction-hierarchy training), nor web-agent injection benchmarks. Without these, the paper's central contrast "existing work … is limited by its reliance on human-defined templates" (Sec. 2.1) is shown against only one line of work. 
- **Suggested Fix:** add the references under "Missing References", state the exact delta for each, and compare empirically with at least one fixed-data fine-tuning defense.

### W2: Population-based learning is presented as a contribution, but is a known technique and its benefit is not isolated
Sec. 3.3 attributes "population-based training" to Rosin & Belew (1997) and also cites Fictitious Self-Play and PBT in Sec. 2.2 (which is a different technique). Training against a pool of past opponents is standard in competitive co-evolution and league/PSRO-style self-play. The paper's own evidence for its value is the Fig. 4/Table 1 ablation, where SPAG (no population) matches ARLAS on AgentDojo. 
- **Suggested Fix:** position PBL as an application of known pool-based self-play, and show a targeted ablation (pool vs latest vs last-k).

### W3: Novelty claims about "diverse" attacks are not tested against the prior art they contrast with
The claim that manual mutation design "limits attack diversity" (Sec. 1) is never measured: ART's attack diversity is not computed (Sec. 4.3). The SFT attacker is itself initialized from a hand-written prompt telling the model to "be as creative as possible" and describing exploit styles (App. A), so manual design is relocated rather than removed.
- **Suggested Fix:** measure diversity for ART/SPAG/SFT attackers; tone down "reducing human effort".

### W4: Citation accuracy
Sec. 2.2 "SPAG (Chen et al., 2024)" resolves to the wrong bibliography entry (a different self-play method); Sec. 1 cites Rafailov et al. (2023, DPO) as an example of fine-tuning on malicious instructions to refuse them, though that paper is a general preference-optimization method; Sec. 2.1 says sandboxing is exemplified by Wen et al. (2025), whose title ("Defending against indirect prompt injection by instruction detection") describes a detection-based defense.
- **Suggested Fix:** correct the citations and cite the defense papers listed below.

### Per-claim novelty (knowledge-based; see addendum for the verified literature check)
| Claim | Dimension | Novelty | Reasoning |
|-------|-----------|---------|-----------|
| C1 attacker–agent co-training for agent safety | method/problem | medium | Co-training attackers and defenders for LLM safety exists for harmful-content safety; applying it to indirect injection in web agents is new |
| C2 population-based opponent sampling | method | incremental | Standard in self-play and co-evolution |
| C3 results | result | n/a | Depends on evidence, see R1 |
| C4 diversity analysis | result | incremental | Metric is not new; no baseline |

## Missing References
*Citation-integrity rule applied; see the verified addendum in Phase 1.5 for link status.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Liu et al., "Chasing Moving Targets with Online Self-Play Reinforcement Learning for Safer Language Models", arXiv 2025 | Attacker/defender self-play RL for LLM safety, closest conceptual prior work |
| Critical | Chen et al., "StruQ: Defending Against Prompt Injection with Structured Queries", USENIX Security 2025 | Fine-tuning defense for prompt injection, the fixed-data approach the paper argues against |
| Critical | Chen et al., "SecAlign: Defending Against Prompt Injection with Preference Optimization", 2024/2025 | Same, preference-optimization variant |
| Important | Ge et al., "MART: Improving LLM Safety with Multi-round Automatic Red-Teaming", NAACL 2024 | Iterative attacker–target adversarial fine-tuning |
| Important | Wallace et al., "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions", 2024 | Training defense against injected instructions |
| Important | Hong et al., "Curiosity-driven Red-teaming for Large Language Models", ICLR 2024 | RL red-teamer with diversity objective, direct counterpart of C1/C4 |
| Important (worth discussing only: recent preprint, 2025-04) | Evtimov et al., "WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks", 2025 | Web-agent injection benchmark closer to the BrowserGym setting; verified on arXiv, labelled recent preprint, so not a required comparison |
| Helpful | Lanctot et al., "A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning", NeurIPS 2017 | Policy-pool training in games (PSRO) for positioning PBL |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence is thinner than the claims |
| Clarity | 3 | Clear; related work too short |
| Significance | 2 | Problem important; demonstrated gain small outside the self-trained attacker |
| Originality | 2 | Known ingredients, new application |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the application is new and timely, but the method is a combination of established ideas, key neighbouring work is uncited, and a fixed-data defense baseline is absent.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound basics, framing errors |
| Clarity & Presentation | 68 | Competent | Clear writing |
| Novelty & Originality | 50 | Developing | Incremental combination; no delta table in the paper |
| Significance & Impact | 60 | Competent | Important problem |
| Experimental Validation | 50 | Developing | Missing the strongest defense baselines |
| Reproducibility | 50 | Developing | Details missing |
| Ethical Compliance | 62 | Competent | Little at stake in the experiments |

## Questions for Authors
1. What exactly separates ARLAS from attacker/defender self-play RL for LLM safety? A clear delta would raise my Novelty score.
2. Why is no fixed-attack fine-tuning defense (structured-query or preference-optimization style) compared, given Sec. 1's central argument?
3. Why was ART's diversity not measured in Sec. 4.3?

## Limitations Assessment
**Partially.** No discussion of threat-model limits (random-line injection, single objective).

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject):** Timely application of a known recipe with unclear novelty delta, missing the key comparison families, and modest evidence outside the self-trained attacker.

## Confidence
**4:** I know this literature well; I judged citations from memory and the bibliography, to be re-checked in Phase 1.5.

---

# Peer Review Report

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Reviewer: Dr. Mei-Ling Abara, Perspective (systems-security and verification institute, East Asia; fictional persona)
## Expertise: agent sandboxing and access control; security engineering of deployed software agents
## Date: 2026-11-10

## Summary
The paper proposes to make an LLM web agent resistant to injected instructions by letting a learned attacker probe it during RL training. The attacker may only append text to page content and wins when the agent emits any of the user's synthetic private data. The authors argue that this scales better than hand-crafted attack sets and show a reduction in leakage on held-out browsing tasks, plus modest transfer to AgentDojo.

## Strengths
### S1: Adversarial training is a good complement to system-level defenses
The paper explicitly scopes itself to model-level hardening (Sec. 2.1) and notes the extension to other reward functions (Sec. 3.1); a learned red-teamer is a practical way to generate hard test cases for any agent, an idea security engineers will recognize from fuzzing.

### S2: The metric pair (ASR and TSR) keeps safety honest about utility
Reporting TSR alongside ASR (Sec. 4.2, Fig. 3–4) prevents the degenerate "refuse everything" defense, and the no-attack row shows what the agent can do without an adversary.

### S3: The synthetic-data design avoids real-data risks
Private information is synthetic (Sec. 3.1, App. A), so the experiments themselves raise no privacy concern.

## Weaknesses
### W1: The threat model is narrow, and the paper claims more than it covers
Injections are appended to "a random line in the webpage’s content" (Sec. 3.1), the attacker sees only the page, the only goal is string-matched leakage of user fields, and episodes last at most five steps (Table 2). Real injections target tool calls (send email, transfer money), persist across pages, hide in markup, and are tailored to the user's actual task. Sec. 3.1's statement that ARLAS "can be easily extended to other environments and risks … by revising the reward function" is untested; AgentDojo, which has such goals, shows ≤ 0.9 pt change (Table 1).
- **Suggested Fix:** a second reward (e.g., unauthorized tool call) in at least one setting, or a clearly narrowed claim.

### W2: Dual-use and release implications of the attacker model are not discussed
The trained attacker reaches 55% ASR against the base agent (Fig. 3, last row). Sec. 5 and App. C contain no statement on whether the attacker is released, how it could be misused against deployed agents, or how the authors weigh that. ICLR expects a short discussion for security artifacts.
- **Suggested Fix:** add a paragraph on release policy, rate-limiting/gating of the attacker, and defender-only release options.

### W3: Residual risk at the end of training is large and under-discussed
After 15 iterations the agent still leaks in 37% of episodes against the contemporaneous attacker (Fig. 3, last cell) and 34% against the final ARLAS attacker (Fig. 4). An operator reading "significantly more robust" (Sec. 5) could treat this as a deployable defense. Also, the evaluated attackers come from the same optimization that trained the agent; a deployed agent will meet attackers that adapt to its policy, so an adaptive-attack evaluation after training would be the realistic test.
- **Suggested Fix:** report the residual ASR prominently, add an adaptive-attacker round after the agent is frozen, and state the trade-off against deterministic mitigations (sandboxing, tool allow-lists).

### W4: Assumption: string match as a proxy for harm
Sec. 3.1 and 4.1 define leakage as containing "any subset" of the private fields in generated tool parameters. A one-token overlap (e.g., a first name that a legitimate form legitimately needs) counts as success for the attacker; encoded or paraphrased exfiltration does not. 
- **Suggested Fix:** report a stricter metric (full-field match) and a paraphrase/encoding test.

### Cross-disciplinary connections
Fuzzing/grammar-based test generation (diversity measured over program behaviours, not text embeddings), quality-diversity search, and capability-based access control for agents (the CaMeL line of work) are the natural companions; both would give the "diversity" claim a behavioural, not only embedding, meaning.

**Minor:** Fig. 1 is clear; no deployment latency or cost figures for the training pipeline.

## Missing References
Defer to R2. Optional pointers: the CaMeL-style "defeating prompt injections by design" system defense, which a deployment-minded reader would ask to be contrasted with learned defenses [verify].

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence below the framing |
| Clarity | 3 | Clear |
| Significance | 3 | Strong relevance to deployed agents |
| Originality | 2 | Application of known pieces |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, practical problem and a clean, readable approach that gives real in-domain gains; weaknesses (narrow threat model, modest OOD effect) are common among accepted papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Reasonable method, framing slips |
| Clarity & Presentation | 70 | Competent | Easy to follow |
| Novelty & Originality | 60 | Competent | New application of known ideas |
| Significance & Impact | 68 | Competent | Relevant to deployed agents |
| Experimental Validation | 54 | Developing | Weak outside self-trained attacker |
| Reproducibility | 52 | Developing | Several settings missing |
| Ethical Compliance | 56 | Developing | No dual-use discussion |

## Questions for Authors
1. Will the attacker model be released, and under what conditions? A well-argued answer would lift my Ethics score.
2. How does the trained agent behave against attacks it has never seen in kind, such as multi-page or markup-hidden injections? An adaptive-attack result would raise my Significance score.
3. What fraction of "leaks" involve fields the task legitimately needed?

## Limitations Assessment
**Partially.** Sec. 5 discusses scale and VLMs only.

## Ethics Review Flag
**No:** low risk given synthetic data, but a short dual-use statement is expected for a trained attacker.

## Overall Score
**4 (Borderline Accept):** A useful, practical idea with real in-domain gains; the weaknesses are of the kind accepted ICLR papers carry, and most can be repaired with narrower claims and one or two added evaluations.

## Confidence
**3:** Security-engineering perspective; I did not audit RL details.

---

# Peer Review Report

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Reviewer: Dr. Odalys Rennick, Generalist (applied NLP team, mid-sized technology company, North America; fictional persona)
## Expertise: LLM post-training; instruction-following; program-committee generalist
## Date: 2026-11-10

## Summary
The paper presents ARLAS, a method that trains a web agent to resist prompt injections by training a second LLM to produce them. Both are fine-tuned with GRPO after an SFT warm-up, and the agent faces all earlier attacker checkpoints. On held-out BrowserGym tasks the agent leaks less private data under attack and completes more tasks than the base model; on AgentDojo the effect is small. The authors also show that attack embeddings spread out during training.

## Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | AgentDojo claim vs Table 1 |
| Presentation: clear, self-contained | Met | Sec. 3, Algorithm 1 |
| Contribution: significance to the community | Partly | Sec. 1, 4 |
| Reproducibility: details and code | Partly | Table 2, 3; no code, no N_iter |
| Honest limitations | Partly | Sec. 5 |

## Strengths
### S1: Clear contribution in one paragraph
Within a page the reader knows what is trained, against what, and what the reward is (Sec. 3.1). Figure 1 and Figure 2 (from captions) show the loop and the population idea simply.

### S2: Relevance to ICLR's audience
LLM agent safety and RL post-training are both core ICLR topics, and an RL-based red-team-and-defend recipe on open models is of interest to this community.

### S3: A pleasant, mostly honest evaluation narrative
The heat-map design (Fig. 3) makes the co-evolution visible, the Qwen3 result is reported as small (Sec. 4.2), and the Appendix provides complete prompts and hyperparameters.

## Weaknesses
### W1: The evidence does not match the strength of the wording
Abstract: "significantly lower attack success rate"; conclusion: "significantly more robust against a wide range of injection attacks" (Sec. 5). On AgentDojo the effect is 0.9 and 0.2 percentage points (Table 1) and in BrowserGym the agent still leaks in about a third of episodes against the final attacker (Fig. 4: 34±2). "A wide range" is evaluated against four attacker models, three of which are weak (≤13% ASR).
- **Suggested Fix:** narrow wording; report residual ASR; add independent attacks.

### W2: Missing comparison with the defense paradigm the paper argues against
Sec. 1 argues fine-tuning on fixed attack datasets is limited, but no such defense is trained on the same budget, so the benefit of learning the attacker is not isolated. 
- **Suggested Fix:** a fixed-injection-dataset baseline trained on the same teacher data.

### W3: Presentation of results leaves the reader to decode the main figure
Fig. 4's panels have 6×5 cells with abbreviated, ordered-by-performance column labels, no ART attacker row, and averages computed over different row sets for ASR and TSR (see R1's ERR-3). The test-set size, the AgentDojo protocol and the "final" checkpoint are not stated, which a general reader needs in order to interpret any number.
- **Suggested Fix:** a small table of the main comparison (agents × {no attack, own-method attacker, independent attacker}), with test-set size and seeds.

**Minor:** typos ("focuese", "seciton", "founed"); acknowledgments and the first-page footnote may reveal affiliations, so check anonymization before submission; Eq. (2) sign.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound design, evidence needs narrowing |
| Clarity | 3 | Clear |
| Significance | 3 | Timely |
| Originality | 2 | Known components |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea on a hot topic with real in-domain gains and a clean write-up; weaknesses (wording, missing baseline, small OOD effect) are ordinary for accepted papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound basics |
| Clarity & Presentation | 72 | Competent | Clear; some missing protocol |
| Novelty & Originality | 60 | Competent | New application of known ideas |
| Significance & Impact | 68 | Competent | Topical |
| Experimental Validation | 56 | Competent | Limited baselines and OOD |
| Reproducibility | 58 | Competent | Prompts and hyperparameters present |
| Ethical Compliance | 62 | Competent | Little at stake |

## Questions for Authors
1. Can you provide a compact table of the main comparison with test-set size and seeds? That would move my Presentation and Soundness views.
2. Would you narrow the abstract to what Fig. 4 shows?
3. What would the result be with a fixed injection dataset of the same size used for SFT/DPO?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept):** The topic fits, the idea is clear and the in-domain result is solid; I would want narrower claims and one more baseline, but these are typical of ICLR acceptances.

## Confidence
**4:** Confident about venue fit and clarity; less about the security literature.

---

# Devil's Advocate Report

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Reviewer: Dr. Yevgenia Marlowe, Devil's Advocate (statistical methodology department, medical school, North America; fictional persona)

---

## Protocol Sweep
Same search as R1: no statement of training, tuning or selection on the reported split is present; the "final" checkpoint rule and the test set are unspecified. No criterion-3 evidence exists, so no leakage claim is made.

## Steelman
Learning the attacker rather than writing it removes the diversity ceiling of fixed-data defenses; an opponent pool prevents the cycle in which the agent forgets old attacks; the agent-vs-attacker matrices show that the final agent is markedly harder to attack than the base while remaining task-capable, and the attacker itself keeps improving.

## Core Argument Chain
1. P1: Fixed or hand-mutated attack sets limit diversity and leave agents vulnerable to novel injections (Sec. 1).
2. P2: A learned attacker co-evolving with the agent generates diverse and increasingly strong attacks (Sec. 4.2, 4.3).
3. P3: Training the agent against all previous attacker checkpoints prevents cycling and promotes generalization (Sec. 3.3).
4. P4: The resulting agent leaks less under attack than the base model without losing task ability (Fig. 3, 4, Table 1).
∴ ARLAS yields a more robust agent against "a wide range of injection attacks" than the base model (Sec. 5).

## Strongest Counter-Argument
The conclusion needs robustness against attacks the training process did not itself produce, yet nearly all of the demonstrated improvement is against attackers trained by the same procedure. In Fig. 4 the three non-ARLAS attackers achieve 3–13% ASR against every agent; only the ARLAS attacker produces separation, and the final agent was trained against a pool of that very attacker's ancestors. This is an in-distribution result: the agent has learned to resist the output distribution of one family of attackers, and the benchmark that is *not* from that family (AgentDojo, Table 1) shows 0.9 and 0.2 percentage points, with SPAG (no population) equal to ARLAS and no variance reported for the base rows. In other words, the evidence for P3 (the population is what helps) and for the "wide range" in the conclusion is weak: the ablation attackers are an order of magnitude weaker than the ARLAS attacker although Sec. 3.3 describes the same attacker-side pairing, so the ablation does not isolate PBL, and the one out-of-distribution comparison does not separate ARLAS from a non-population baseline. A skeptic would also point out that the base-to-ARLAS TSR gain in the no-attack row (38 → 56) is explained by in-domain SFT and RL, so "improving task success" is not evidence about safety, and that the final agent still leaks in 34–37% of episodes against the strongest attacker. What survives is a narrower and still useful claim: RL against a learned attacker lowers leakage against that attacker family on in-domain tasks. The paper should be framed that way, with an independent-attack evaluation to support anything broader.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The BrowserGym results do support a weaker version of the main claim, no test-set selection is stated, and the problems are overclaims and missing controls, which are MAJOR.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / Scope | Fig. 4 (left), Sec. 4.2 | "Regardless of the specific attacker faced": separation exists only against the method's own attacker; other attackers ≤13% ASR. Evidence supports a weaker claim (narrow it); it does not contradict the main claim. | Add independent attackers (AgentDojo-style templates, an externally trained RL attacker) and report per-attacker results |
| DA-M2 | Evidence | Abstract, Table 1, Sec. 4.2 | "Significantly lower ASR" and "generalizes to the unseen AgentDojo": Δ = 0.9 and 0.2 pt, no test, base rows without variance, SPAG equal | Paired bootstrap CIs; narrow wording |
| DA-M3 | Logic | Sec. 4.2 (PBL claim), Table 1 | "Training against a population … is critical": SPAG (not population-based) equals ARLAS in ASR (5.4 vs 5.4); ablation attackers differ 4–5× in strength though Sec. 3.3 describes identical attacker pairing | Training curves, pool-vs-latest-vs-last-k ablation, explain attacker-strength gap |
| DA-M4 | Logic | Sec. 4.3, Eq. (3), Fig. 5 | Cumulative APD rises by construction when pooling checkpoints; no baseline attacker, no per-checkpoint APD, 3 stages only, no link between diversity and robustness | Per-checkpoint APD, baselines, diversity ablation |
| DA-M5 | Alternative explanation | Fig. 4 right, Sec. 4.1 | TSR gain is from SFT on teacher episodes and RL on in-domain tasks (a task-only agent is at least as good with no attack), not evidence of safety | Report TSR relative to the task-only agent; match SFT data for all baselines |
| DA-M6 | Scope | Sec. 3.1, 4.1 | Leakage = "any subset" of private strings in tool parameters; AgentDojo ASR mapping not stated; legitimate uses of user data may count as "attacks" | Stricter metric; state AgentDojo protocol |
| DA-M7 | Logic | Sec. 3.1 reward cases; Abstract | "Two-player zero-sum game": the fail/truncate case gives both players −1, so the game is not zero-sum, and the cyclic-dynamics motivation for PBL assumes a zero-sum structure | Redefine rewards or drop the zero-sum claim |
| DA-M8 | Missing control | Sec. 1, 4.1 | No fixed-injection-dataset fine-tuning baseline trained on equal budget; the central motivation is untested | Add one (SecAlign/StruQ-style recipe) |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | Fig. 3 | After SFT the agent is *more* vulnerable than base against weaker attackers (2→6 vs base attacker; 16→22 vs SFT attacker); undiscussed |
| DA-m2 | Reporting | Fig. 4 | ASR averages over 4 rows, TSR over 5 rows (includes no-attack) |
| DA-m3 | Citations | Sec. 2.2, Sec. 1, Sec. 2.1 | SPAG cited as Chen et al. (a different bibliography entry); DPO cited for a prompt-injection defense line; sandboxing attributed to a detection paper |
| DA-m4 | Eq. | Eq. (2) | Sign of the clipped term |
| DA-m5 | Reporting | Fig. 3, 4, Table 1 | "3 random seeds": what varies is not stated; many "±0" |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Fig. 4 ASR average, base column | 19 | (2+9+11+55)/4 = 19.25 | Yes (4 rows) |
| Fig. 4 ASR average, best column | 12 | (3+6+6+34)/4 = 12.25 | Yes |
| Fig. 4 TSR average, first column | 31 | (38+31+34+38+15)/5 = 31.2 (5 rows); 29.5 over 4 rows | Yes, but a different row set than ASR |
| Table 1, Gemma3 ASR improvement | 6.3 → 5.4 | Δ = 0.9 pt = 14% relative | Real but small; no test |
| Table 1, Qwen3 ASR improvement | 1.6 → 1.4 | Δ = 0.2 pt = 12.5% relative | Real but within reasonable noise of a 1–2% base rate |
| Fig. 4 ASR vs ARLAS attacker | 55 → 34 | −21 pt = −38% relative | Yes |
| Fig. 4 ASR excluding ARLAS attacker | not reported | ≈7.3 (base) vs ≈5.0 (best) | Derived |

## Ignored Alternative Explanations
- The agent may be learning surface features of the ARLAS attacker's phrasing (e.g., the "technical support ticket … hidden field" style in App. A) rather than a general refusal of injected instructions.
- Lower ASR may partly reflect more conservative handling of private fields in all contexts (the agent's TSR under strong attack is still 35% vs 56% unattacked).
- A larger share of the "unseen" test tasks may be near-duplicates of the training task families in MiniWoB-style environments (test identity not stated).

## Missing Stakeholder Perspectives
Operators who must decide whether a 12–14B open model hardened this way is safe to deploy; third parties affected by a released attacker model; users whose legitimate requests need the very fields the agent is trained not to emit.

## Observations (Non-Defects)
The full cross-play matrices (Fig. 3, 4, 6), the disclosure of how SPAG was adapted, the honest Qwen3 reporting, and complete prompts in App. A are good practice and make the weaknesses above checkable.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Non-zero-sum framing, mixed-opponent advantages, ablation not isolating PBL |
| Clarity & Presentation | 68 | Clear text; unstated protocol |
| Novelty & Originality | 52 | Known ingredients |
| Significance & Impact | 54 | Gains small outside the own-attacker setting |
| Experimental Validation | 42 | Self-attacker evaluation, no independent attacks, missing baseline |
| Reproducibility | 50 | Several settings missing |
| Ethical Compliance | 58 | No dual-use discussion |

**Pool position:** better than about 46% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central robustness claim rests on attackers the method created, and the out-of-distribution test shows almost no effect.

## Overall: 3 | Confidence: 4

---

# Phase 1.5: Literature Check (Domain Reviewer addendum)

**Mode:** strict (cutoff 2025-09-24; results after the cutoff are dropped). **Queries:** 9 counted against the budget of 12 (claim: 5, baseline: 2, expansion: 1, plus one further claim query); two other queries returned nothing (C2 "multi-round" phrasing, "opponent pool selfplay"). Gaps left open: no prior work retrieved for 2021–2022, and no direct retrieval for population-based opponent sampling (C2); the search covers arXiv only. `similarity`: no high conceptual overlap (cosine ≥ 0.30) and no text overlap (shared 8-grams = 0) with any kept abstract. The `benchmarks` command found no benchmark names automatically; AgentDojo was scouted by hand with `scout`. Searches never used the paper's title, method name or authors (fingerprint exclusion active).

**Closest prior work (by similarity):** (1) Task Shield (2024-12, agent defense on AgentDojo, cosine 0.20); (2) Diverse and Effective Red Teaming with Auto-generated Rewards and Multi-step RL (2024-12, cosine 0.18); (3) AgentDojo (2024-06, cosine 0.17). By concept, the nearest is Self-RedTeam (online self-play MARL, attacker and defender co-evolve), which the paper does not cite.

## Per-claim novelty (claim-level profile, `novelty_profile.json`)
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 co-train attacker + agent for agent safety | method | medium | Self-RedTeam, level 3, https://arxiv.org/abs/2506.07468v4, prior (peer-reviewed), not cited | Same co-evolving attacker/defender RL mechanism but for chat-model harmful-content safety, not tool-using agents under indirect injection; other related work (multi-round multi-agent red-team games, 2023; diverse RL red-teaming, 2024) also level 3 |
| C2 population of past attackers | method | high (search-limited) | Self-RedTeam, level 2 | No retrieved prior work covers the pool idea in this setting; the technique is established in game-playing RL (PSRO, league training), outside this arXiv-limited search, so my judgment is at most medium |
| C3 lower ASR, maintained TSR | result | high | SecAlign, level 2 | Different models and benchmarks; numbers not comparable |
| C4 attack diversity rises | result | high (search-limited) | Learning diverse attacks (GFlowNet), level 2 | Diversity-seeking red-teaming exists; the paper's measurement has no baseline |

Script reading: no claim is "known"; no candidate for DA criterion 7. Attribution: the nearest whole-paper neighbours to position against are Self-RedTeam (method) and SecAlign/StruQ (defense).

## Novelty delta table
| Claimed contribution | Closest prior work | What it already does | What is actually new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|---------------------------|---------------------------|
| C1 | Chasing Moving Targets with Online Self-Play RL for Safer Language Models (arXiv 2025-06) | Online self-play MARL; attacker and defender co-evolve (per its abstract) | Tool-using web agents, indirect prompt injection, leakage reward | No (not cited) |
| C1/C4 | Diverse and Effective Red Teaming with Auto-generated Rewards and Multi-step RL (arXiv 2024-12) | RL red-teamer rewarded for diversity | Attacker trained against a co-adapting agent | No |
| C3 (defense) | SecAlign (CCS 2025), StruQ (USENIX Security 2025) | Fine-tuning defenses against prompt injection on fixed injection data | Learns the attacks instead of fixing them | No; Sec. 1 argues against this family without comparing |

## Baseline scout (AgentDojo)
| Benchmark / metric | Prior method (link, label) | Its reported number | Compared in the paper? | Paper's number | Note |
|--------------------|----------------------------|---------------------|------------------------|----------------|------|
| AgentDojo ASR | Task Shield, https://arxiv.org/abs/2412.16682v1, prior (arXiv-only) | 2.07% ASR / 69.79% utility on GPT-4o | No | 5.4% / 25.8% (Gemma3 12B) | Different model and setting; not an under-reported baseline; shows how far the paper's AgentDojo absolute numbers are from closed-model defenses |
| AgentDojo ASR | MELON (ICML 2025), RTBAS, DRIFT (NeurIPS 2025), CaMeL (arXiv 2025-03) | closed-model settings | No | n/a | Prior; a missing comparison is MAJOR at most; the model-level vs system-level distinction should be discussed |
| AgentDojo / injections | SecAlign (CCS 2025), StruQ | fine-tuned open models | No | n/a | Prior; the most directly relevant missing baseline family |
| Web-agent injections | WASP (2025-04), Meta-SecAlign (2025-07) | n/a | No | n/a | Recent preprints: worth discussing only |

## Field snapshot (as of the cutoff)
Three to five years ago prompt-injection work consisted of demonstrations and hand-written attack catalogues (Greshake et al. 2023). In 2024, fixed-data training defenses (StruQ, instruction-hierarchy training, SecAlign) and the AgentDojo benchmark made agent-level evaluation standard. In 2025, system-level defenses (CaMeL, MELON, Task Shield, RTBAS, DRIFT) reported low ASR with small utility loss on closed models, adaptive-attack work showed that many defenses break under tailored attacks, and RL-based red-teaming (diverse-attack RL, self-play safety) matured for chat models. Open problems named by recent work: robustness to adaptive attackers, utility preservation, transfer across agent frameworks. What counts as significant now: a defense that stays effective under adaptive, independently generated attacks on a standard benchmark such as AgentDojo, or a learned-attacker method that beats fixed-data fine-tuning at equal budget; a one-point ASR change on a benchmark with a 1–6% base rate is not significant.

## Verified missing references (final list, replacing the provisional table in R2's report)
| Priority | Reference | Link / status |
|----------|-----------|---------------|
| Critical | Liu et al., "Chasing Moving Targets with Online Self-Play Reinforcement Learning for Safer Language Models" (2025) | https://arxiv.org/abs/2506.07468v4 (found; prior, peer-reviewed) |
| Critical | Chen et al., "SecAlign: Defending Against Prompt Injection with Preference Optimization" (CCS 2025) | https://arxiv.org/abs/2410.05451v3 (found; prior) |
| Critical | Chen et al., "StruQ: Defending Against Prompt Injection with Structured Queries" (USENIX Security 2025) | https://arxiv.org/abs/2402.06363v2 (found; prior) |
| Important | Ge et al., "MART: Improving LLM Safety with Multi-round Automatic Red-Teaming" (NAACL 2024) | https://arxiv.org/abs/2311.07689v1 (found) |
| Important | Wallace et al., "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions" (2024) | https://arxiv.org/abs/2404.13208v1 (found) |
| Important | Hong et al., "Curiosity-driven Red-teaming for Large Language Models" (ICLR 2024) | https://arxiv.org/abs/2402.19464v1 (found) |
| Important | Lee et al., "Learning diverse attacks on large language models for robust red-teaming and safety tuning" (ICLR 2025) | https://arxiv.org/abs/2405.18540v3 (found) |
| Important | Debenedetti et al., "Defeating Prompt Injections by Design" (CaMeL, 2025) | https://arxiv.org/abs/2503.18813v2 (found; prior arXiv-only) |
| Important (discuss only) | Evtimov et al., "WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks" (2025) | https://arxiv.org/abs/2504.18575v3 (found; recent preprint) |
| Helpful (discuss only) | Chen et al., "Meta-SecAlign: Training LLMs against Prompt Injection for Robust Agents" (2025) | https://arxiv.org/abs/2507.02735v4 (found; recent preprint) |
| Helpful | Lanctot et al., "A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning" (NeurIPS 2017) | https://arxiv.org/abs/1711.00832v2 (found) |

## Citation check (E7), against the bibliography and kept abstracts
- Sec. 2.2 "SPAG (Chen et al., 2024)": the "Chen et al." bibliography entry is arXiv:2401.01335 (self-play fine-tuning); SPAG is "Cheng et al., 2024" (listed, and correctly used in Sec. 4.1). **Verified wrong cite.**
- Sec. 2.1 "sandboxing the agent, where its actions are monitored and restricted within a secure environment (Wen et al., 2025)": the Wen et al. abstract (arXiv:2505.06311) describes detecting instructions in external content from changes in the LLM's behavioural state, a detection defense, not sandboxing. **Verified mismatch** (abstract read).
- Sec. 1 "fine-tune the LLM agent on datasets of malicious instructions … (Rafailov et al., 2023)": the reference is the general DPO method; the prompt-injection fine-tuning defenses are the missing StruQ/SecAlign line. **Weak support.**
- Sec. 3.3 credits "population-based training" to Rosin & Belew (1997) while Sec. 2.2 cites Jaderberg et al. (2017) "Population Based Training", a different technique (hyperparameter optimisation); terminology is confusable, not an error by itself.

*Scores were assigned before the search and are not changed by the addendum.*

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 own-attacker evaluation | kept | Specific, verified from Fig. 4 cells; not answered in the paper |
| R1 | W2 AgentDojo | kept | Matches Table 1; sentences quoted |
| R1 | W3 diversity analysis | kept | Eq. (3) and Fig. 5 caption checked |
| R1 | W4 ablation / PBL | rewritten | The "attacker weaker although pairing identical" point is kept as an unexplained inconsistency (the paper does not say the w/o PBL variant changes attacker pairing) rather than as an error |
| R1 | W5 TSR confound + baselines | kept | Specific |
| R1 | W6 reproducibility | kept | Not answered in the appendix (searched) |
| R1 | ERR-1..5 | kept | All quotes found; ERR-5 (Eq. 2 sign) medium confidence |
| R2 | W1 related-work gaps | kept | Verified in the literature check (links above) |
| R2 | W2 PBL known technique | rewritten | Softened to "application of known pool-based self-play" |
| R2 | W3 manual design relocated | kept | App. A prompt quoted |
| R2 | W4 citations | kept | Two of three verified; the DPO one is weak support, not an error |
| R3 | W1 threat model | kept | Sec. 3.1 quoted |
| R3 | W2 dual-use | kept | Sec. 5 and App. C searched: no statement |
| R3 | W3 residual risk | kept | Fig. 3 last cell (37) and Fig. 4 (34) |
| R3 | W4 string-match proxy | kept | Sec. 3.1/4.1 |
| R4 | W1 wording vs evidence | kept | |
| R4 | W2 missing baseline | kept | |
| R4 | W3 presentation of Fig. 4 | moved/kept | Cosmetic parts moved to Minor; missing test-set size kept as substantive |
| DA | DA-M1..M8, DA-m1..m5 | kept | DA-M7 (zero-sum) is MAJOR by the DA's rating; the EIC may weigh it as framing |

No weakness was dropped as already answered (the appendix has no test-set size, N_iter, AgentDojo protocol or release policy). Scores unchanged.

# Synthesizer Package (Part A)

| ID | Issue | Sources | Class | Hinges? |
|----|-------|---------|-------|---------|
| I1 | Safety gain measured mainly against the method's own attackers; no independent attacks | R1-W1, R3-W3, R4-W1, DA-M1 | CONSENSUS-4 | **Yes** |
| I2 | AgentDojo effect negligible; "significantly"/"generalizes" overclaimed; protocol unstated | R1-W2, R1-ERR-4, R4-W1, DA-M2 | CONSENSUS-3 | **Yes** |
| I3 | Missing fixed-data fine-tuning defense baseline (StruQ/SecAlign family) | R1-W5, R2-W1, R4-W2, DA-M8 | CONSENSUS-4 | **Yes** |
| I4 | PBL benefit not isolated (SPAG equals ARLAS on AgentDojo; ablation attackers 4–5× weaker) | R1-W4, R2-W2, DA-M3 | CONSENSUS-3 | Yes |
| I5 | Diversity analysis lacks baseline / per-checkpoint metric | R1-W3, R2-W3, DA-M4 | CONSENSUS-3 | No |
| I6 | Reproducibility / protocol gaps (test size, seeds, N_iter, code) | R1-W6, R4-W3, DA-m5 | CONSENSUS-3 | No |
| I7 | Novelty delta vs self-play safety RL; thin related work; citation errors | R2-W1, R2-W4, R1-ERR-2, DA-m3 | CONSENSUS-2 | No |
| I8 | Narrow threat model; string-match leakage proxy | R3-W1, R3-W4, DA-M6 | CONSENSUS-2 | No |
| I9 | Dual-use / release not discussed | R3-W2 | SOLO | No |
| I10 | TSR gain confounded by in-domain training | R1-W5, DA-M5 | CONSENSUS-2 | No |
| I11 | "Zero-sum" mislabel | R1-ERR-1, DA-M7 | CONSENSUS-2 | No |
| I12 | Eq. (2) sign; Fig. 4 averaging; typos | R1-ERR-3, ERR-5, R4 minor | SOLO | No |

**SPLIT:** none explicit; R3 and R4 (Overall 4) and R1, R2, DA (Overall 3) agree on the facts and differ on how much weight the missing baseline and the OOD result deserve. **DA-CRITICAL:** none raised. **Integrity scan:** no reviewer-directed text found; anonymity note only.

---

# Phase 2: EIC Meta-Review and Editorial Decision

# Editorial Decision

## Paper: Adversarial Reinforcement Learning for Large Language Model Agent Safety
## Submission ID: iclr26-tguzk54PbV (blinded)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Marguerite Anselmi; R1 Methodology (T. Lindqvist-Okoye), R2 Domain (A. Ferreira-Duarte), R3 Perspective (M.-L. Abara), R4 Generalist (O. Rennick), DA (Y. Marlowe)

---

## Decision: Borderline Reject (3) — ICLR rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); scale status: secondary

*How a careful panel would likely see this draft; a simulation, not a prediction.*

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 56.4
**EIC assessment** (internal): weighted rating 3.34 → starting point 3 · weighted composite 56.0 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 52% of ICLR submissions (accepted share ≈ 27%). Deciding evidence: the in-domain gain against strong attackers is real, but the headline robustness is measured against the method's own attackers, the one independent benchmark shows ≤ 0.9 points, and the central motivating comparison (learned attacks vs fixed-data fine-tuning) is absent. That puts it just below the borderline band, in the upper part of the typical rejected range.

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely problem and a clean, readable recipe (SFT warm-up, GRPO co-training, opponent pool) with complete prompts and hyperparameters; the cross-play matrices (Fig. 3, 4, 6) are an honest evaluation format; against strong attackers the final agent roughly cuts ASR by a third (55 → 34 against the ARLAS attacker, average 19 → 12) while keeping task ability; the Qwen3 result is reported honestly as small.
- **Against acceptance:** Nearly all separation between methods comes from attackers trained by the same procedure; the one external benchmark (AgentDojo, Table 1) moves by 0.9 and 0.2 points with no test, with SPAG tied to ARLAS; the PBL ablation does not isolate the pool idea; no fixed-data fine-tuning defense (StruQ/SecAlign family) is compared although the paper's motivation is exactly that contrast; the closest conceptual neighbour (online attacker/defender self-play for LLM safety) is uncited; abstract and conclusion use "significantly" and "wide range" beyond the evidence.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Separation only vs the method's own attacker; other attackers ≤ 13% ASR | R1-W1, R4-W1, DA-M1, R3-W3 | Fig. 4 (left) | **Verified** | Cells read from extraction: base/SPAG/w/o PBL rows 2–13; ARLAS row 34–55. Column labels garbled, identities inferred from text and printed averages; averages recomputed (19.25, 12.25) |
| AgentDojo gain is 0.9 / 0.2 pt, no test, SPAG tied | R1-W2, DA-M2, R4-W1 | Table 1, Sec. 4.2 | **Verified** | 6.3→5.4, 1.6→1.4; SPAG 5.4 ± 0.0 |
| "Population critical" is not isolated | R1-W4, R2-W2, DA-M3 | Sec. 4.2, Sec. 3.3, Table 1 | **Verified** (ablation attackers 4–5× weaker is an unexplained gap) | R1's inference that a weaker agent should make attacks easier is a reasonable expectation, not a verified error: **Partly correct**; DA's "order of magnitude" is **Overstated** (4–5×) |
| Not zero-sum | R1-ERR-1, DA-M7 | Sec. 3.1 reward cases | **Verified** (both −1 when the task fails) | Framing issue; does not change any number |
| Diversity metric rises by construction | R1-W3, DA-M4 | Eq. (3), Fig. 5 | **Partly correct** | Cumulative union does inflate distance, but the rise is expected, not guaranteed ("by construction" is a bit strong); the missing baseline and per-checkpoint metric are verified omissions |
| TSR gain reflects in-domain SFT/RL | R1-W5, DA-M5 | Fig. 4 right, Sec. 4.2 | **Verified** | Sec. 4.2: "ARLAS performs comparably to ARLAS w/o AL" with no attack |
| Residual leakage 34–37% vs strongest attacker | R3-W3 | Fig. 3 last cell (37±4), Fig. 4 (34±2) | **Verified** | |
| Citation errors: SPAG cite, Wen et al. | R1-ERR-2, R2-W4 | Sec. 2.2, Sec. 2.1, References | **Verified** | Wen et al. abstract is a detection method; DPO-as-defense is weak support, not an error |
| Missing Self-RedTeam, SecAlign, StruQ etc. | R2-W1 | Sec. 2 | **Verified** (links in Phase 1.5) | All three Critical items are labelled prior; WASP and Meta-SecAlign are recent preprints (discuss only, not held against the paper) |
| Eq. (2) sign | R1-ERR-5 | Eq. (2) | **Partly correct** | Sign as printed is odd; extraction may contribute; MINOR |
| ASR/TSR averaged over different row sets | R1-ERR-3 | Fig. 4 | **Verified** | Ranking unchanged |
| No dual-use / release statement | R3-W2 | Sec. 5, App. C | **Verified** | |
| No selection on the reported split | R1 protocol sweep, DA | whole text | **Verified** (not stated) | Checkpoint choice unspecified: a question, not an issue |

**Error Logs:** R1's ERR-1…5 checked at their locations: none Incorrect; ERR-5 medium confidence. Report-check table: nothing dropped as already answered. Integrity: no reviewer-directed text; anonymity wording noted for the editor (no score effect).

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error log verified at each location; recomputations correct; one phrase ("by construction") slightly strong |
| R2 (Domain) | 3 | 4 | 1.25 | Missing references and two citation mismatches verified against abstracts; novelty delta grounded in a verified neighbour |
| R3 (Perspective) | 4 | 3 | 1.0 | Points verified and constructive; moderate confidence; several points are suggestions rather than defects |
| R4 (Generalist) | 4 | 4 | 1.0 | Facts verified; the pool position (65) is somewhat generous given the own-attacker issue, within normal role variation |
| DA | 3 | 4 | 1.0 | Strong counter-argument verified; "order of magnitude" overstated; no CRITICAL inflation |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | The DA stated "No CRITICAL issues found"; the EIC agrees: the BrowserGym results support a weaker version of the main claim, no test-set selection is stated, and the defects are overclaims and missing controls | n/a |

### Final Decision and Justification
The EIC-weighted rating is 3.34, so the starting point is 3 (Borderline Reject); the 0–100 composite (56.0) falls in the same band, so the signals agree and there is no cross-check conflict. I do not depart from the starting point. The two accept-leaning reviewers (R3, R4) rate the paper as having weaknesses typical of accepted ICLR papers, and in isolation several are: single environment, small models, honest limitations. What keeps me below that line is a verified combination rather than any one flaw: (i) the safety result is measured chiefly against the method's own attackers (Fig. 4), (ii) the only independent benchmark shows ≤ 0.9 points with SPAG tied (Table 1), contradicting the inference that the population is critical, and (iii) the baseline that the introduction positions itself against (fixed-data fine-tuning) is not run. These are repairable with inference-only experiments and a narrower claim, so this is a Borderline Reject with a clear path, not a Reject. The decision does not exceed the DA ceiling (none applies). Literature-check items were applied by label: missing-comparison points rest on prior work (SecAlign, StruQ, Self-RedTeam); recent preprints (WASP, Meta-SecAlign) did not lower any score.

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate.json`, final run `--venue iclr --final 3`)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.25 | 24% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 19% |
| DA | 4 | 0.85 | 1.00 | 19% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 56 | 62 | 62 | 48 | 55.6 | 55.1 | 14 |
| Clarity & Presentation | 66 | 68 | 70 | 72 | 68 | 68.8 | 68.6 | 6 |
| Novelty & Originality | 54 | 50 | 60 | 60 | 52 | 55.2 | 54.7 | 10 |
| Significance & Impact | 56 | 60 | 68 | 68 | 54 | 61.2 | 60.7 | 14 |
| Experimental Validation | 44 | 50 | 54 | 56 | 42 | 49.2 | 48.8 | 14 |
| Reproducibility | 46 | 50 | 52 | 58 | 50 | 51.2 | 50.9 | 12 |
| Ethical Compliance | 60 | 62 | 56 | 62 | 58 | 59.6 | 59.9 | 6 |
| **Composite** | 52.5 | 55.7 | 60.2 | 62.0 | 51.5 | **56.4 (before)** | **56.0 (after)** | |
| Pool position (P%) | 46 | 50 | 66 | 65 | 46 | | | |

No dimension has a spread above 20 (no ⚠). Script warnings: none. Before run (confidence only): EIC composite 56.2, EIC rating 3.38.

### Target-Venue Scores (ICLR 2026 cycle; scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue-weighted composite 56.1; skill label Borderline Reject (3) |

*Scale status is secondary: the label is a translation of the skill's internal score, not official ICLR wording.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Adversarial Reinforcement Learning for Large Language Model Agent Safety" to ICLR. Training a learned attacker against a tool-using agent is a timely idea for a problem that matters.

**Overall Assessment:** The panel found the paper clear and the training recipe well specified, with real in-domain robustness gains against strong attackers. It was less convinced that the evidence supports the broader claims: the safety gains are measured mainly against attackers the method trains itself, and the independent benchmark (AgentDojo) shows very small changes.

**Key Strengths Identified by Reviewers:**
1. A clearly specified co-training recipe with prompts and hyperparameters in the appendix (R1-S1, R4-S1, R4-S3).
2. Full agent-vs-attacker cross-play matrices that make the co-evolution visible (R1-S2, DA observations).
3. A timely problem and a practical idea of interest to the ICLR audience (R2-S1, R3-S1, R4-S2).

**Key Concerns Requiring Attention:**
1. Robustness is shown mostly against the method's own attackers (CONSENSUS-4: R1, R3, R4, DA).
2. AgentDojo effects are 0.9 and 0.2 points with no test, and "significantly"/"generalizes" overstate them (CONSENSUS-3: R1, R4, DA).
3. A fixed-data fine-tuning defense, the paper's own foil, is not compared; the closest self-play safety work and the prompt-injection fine-tuning defenses are not cited (CONSENSUS-4: R1, R2, R4, DA).
4. The population-based contribution is not isolated (CONSENSUS-3: R1, R2, DA).

No Devil's Advocate CRITICAL issue was raised.

**Decision: Borderline Reject (3).** The contribution is real but the central claims are ahead of the evidence. A revision that adds independent attacks, a fixed-data baseline and confidence intervals on AgentDojo, and narrows the wording, would likely move this to a borderline-accept discussion. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Marguerite Anselmi
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Evaluation mainly against the method's own attackers | R1, R3, R4, DA | CONSENSUS-4 |
| Missing fixed-data fine-tuning defense baseline / related work | R1, R2, R4, DA | CONSENSUS-4 |
| AgentDojo effect negligible; overclaimed wording | R1, R4, DA | CONSENSUS-3 |
| PBL benefit not isolated | R1, R2, DA | CONSENSUS-3 |
| Diversity analysis lacks baseline | R1, R2, DA | CONSENSUS-3 |
| Reproducibility / protocol gaps | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Do the weaknesses outweigh the contribution? | R3, R4 (Overall 4) | R1, R2, DA (Overall 3) | Same facts; the EIC sides with the lower ratings because items I1–I3 together bear on the central claim and are not ordinary accepted-paper weaknesses; the gap is a one-step difference, near the 3/4 boundary (weighted 3.34) |

### Score Spread Discussion
No dimension exceeded the 20-point spread flag. The largest spreads (14) are Technical Rigor, Significance and Experimental Validation, split between R3/R4 (higher) and R1/DA (lower); the EIC adopts the lower Experimental Validation view (verified own-attacker evaluation) and the higher Clarity view.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | agreed | n/a |
| DA-M1 | MAJOR | Own-attacker evaluation | Yes (R1, R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | AgentDojo overclaim | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | PBL not isolated | Yes (R1, R2) | n/a | n/a |
| DA-M8 | MAJOR | No fixed-data baseline | Yes (R1, R2, R4) | n/a | n/a |
| DA-M7 | MAJOR (EIC: framing) | Not zero-sum | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Robustness shown mainly against own attackers | R1-W1, R3-W3, R4-W1, DA-M1 | Fig. 4, Sec. 4.2 | Evaluate all agents against independent attackers (AgentDojo's own attacks, templates, an externally trained attacker); report per-attacker ASR and the average excluding the ARLAS attacker; add an adaptive attack on the frozen final agent | Medium; a few GPU-hours (inference only) | Yes |
| R2 | AgentDojo effect negligible, wording overclaimed, protocol unstated | R1-W2, R1-ERR-4, R4-W1, DA-M2 | Abstract, Table 1, Sec. 4.2, Sec. 5 | State suite/attack/ASR mapping; paired bootstrap CIs and a significance test for base vs ARLAS vs SPAG; replace "significantly" and "generalizes" with what the data support | Low | Yes |
| R3 | Missing fixed-data fine-tuning defense baseline | R1-W5, R2-W1, R4-W2, DA-M8 | Sec. 1, 4.1 | Add a StruQ/SecAlign-style baseline on the same teacher data and budget, and report TSR relative to a task-only agent | Medium–High; ≈ 1–2 days of the paper's training pipeline (compute not stated in paper) | Partly |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | PBL not isolated; ablation attackers 4–5× weaker | R1-W4, R2-W2, DA-M3 | Training curves for both variants; pool vs latest vs last-k ablation; fix opponent sampling within GRPO groups; explain the attacker-strength gap | Medium; ≈ 1 RL rerun per variant | Partly |
| S2 | Diversity analysis lacks baselines | R1-W3, R2-W3, DA-M4 | Per-checkpoint APD, same metric for SFT/ART/SPAG attackers, strategy-level labels, add iteration 15 | Low | Yes |
| S3 | Reproducibility gaps: test-set size, checkpoint choice, N_iter, N_epi, G, compute, seeds, code | R1-W6, R4-W3, DA-m5 | Add a protocol table; state what seeds vary; ≥3 training runs for the main configuration if feasible; anonymized code | Low–High (training seeds ≈ 3× training cost) | Partly |
| S4 | Related work: Critical/Important missing references (all verified, prior) | R2-W1 | Cite and differentiate Self-RedTeam, SecAlign, StruQ, MART, instruction hierarchy, curiosity-driven and diverse-attack RL red-teaming, CaMeL | Low | Yes |
| S5 | Citation errors | R1-ERR-2, R2-W4 | Fix the SPAG cite (Cheng et al.), the Wen et al. description, the DPO attribution | Low | Yes |
| S6 | Narrow threat model; string-match leakage proxy; residual 34–37% leakage | R3-W1, R3-W3, R3-W4, DA-M6 | Report a stricter metric and residual ASR prominently; discuss threat-model limits; test a second reward if feasible | Low–Medium | Partly |
| S7 | TSR gain confounded by in-domain training | R1-W5, DA-M5 | Report TSR vs the task-only agent; match SFT data across baselines | Low | Yes |
| S8 | "Zero-sum" mislabel | R1-ERR-1, DA-M7 | Say "adversarial, non-zero-sum" or redefine rewards | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Dual-use / release policy for the trained attacker | R3-W2 | Add a short statement (ICLR expects one for security artifacts) |
| N2 | Eq. (2) sign; Fig. 4 average definitions; typos | R1-ERR-3, ERR-5, R4 minor | Correct and unify |
| N3 | Helpful/discuss-only references (WASP, Meta-SecAlign, PSRO) | R2 | Mention for awareness; not required |
| N4 | Post-SFT agent more vulnerable than base against weak attackers | DA-m1 | Comment on the SFT stage's effect |
| N5 | Anonymity wording in footnote and acknowledgments | R4 minor | Check anonymization |

## Estimated Revision Effort
- Priority 1: 3 items, ≈ 3–5 days (inference-only evaluations plus one baseline training run).
- Priority 2: 8 items, ≈ 3–7 days (the training-seed repeat dominates).
- Priority 3: 5 items, < 1 day.
- **Total estimated revision time**: ≈ 1.5–2.5 weeks of work; Priority 1 items R1 and R2 are feasible within a one-week rebuttal window.
