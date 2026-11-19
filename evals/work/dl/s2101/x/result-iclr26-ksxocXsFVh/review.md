# Academic Paper Review: "Context Tuning for In-Context Optimization" (ICLR, full mode)

*Simulation of how a careful panel would likely see this draft; not a prediction. Date: 2026-11-10. The five reviewer passes were run one after another in a single shared model context (no subagents), so they are role-based perspectives, not independent agents. Figures were not available (text extraction only): figure-dependent claims (Figures 1, 2, 4, 5, 6) are judged from captions and text. The supplementary material is not provided beyond the appendix in the text. Literature check: strict mode, cutoff 2025-09-24. Integrity scan: done by manual text search only (no reviewer-directed or AI-directed text found; the `integrity_scan.py` script was not run in this evaluation, so hidden-character checks were not performed).*

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Context Tuning for In-Context Optimization |
| Primary Discipline | Machine learning → NLP → few-shot adaptation of LLMs (parameter-efficient tuning, in-context learning) |
| Secondary Discipline(s) | Test-time training / test-time adaptation; abstract-reasoning benchmarks (ARC) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Prompt Tuning, Prefix Tuning on a KV cache initialized from demonstrations, leave-one-out masking, token dropout, LoRA-based Test-Time Training |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none; ICLR submissions are public, authors can revise the PDF during discussion |
| Paper Maturity | Submission-ready |
| Ethics-Relevant Content | none (public NLP benchmarks, no human subjects, no deployment-risk content) |

### Claimed Contributions (as stated by the authors; the paper has no bullet list, so these are taken from Abstract and §1)
1. **C1.** Initializing a trainable prompt or prefix (CT-Prompt, CT-KV) from the few-shot demonstrations and optimizing it outperforms Prompt Tuning and Prefix Tuning (Abstract, §1, Table 1, §5.4).
2. **C2.** CT-KV is competitive with Test-Time Training (TTT) at ≤ half the training time, with linear rather than quadratic cost in the number of demonstrations (Abstract, §1, Table 1, §5.4, Appendix A, Table 5).
3. **C3.** Leave-One-Out Masking and Token Dropout are "crucial" design choices (§4.3, §5.5, Table 2).
4. **C4.** CT-KV applied after TTT (TTT+CT-KV) gives additional gains, so context and weight adaptation are complementary (§1, §5.4, Table 1).
5. **C5.** ICL encodes an "incomplete" task representation in its KV cache, which CT-KV repairs; and the "In-Context Optimization (ICO)" framework unifies TTT and Context Tuning (§4.1, §5.7, Table 4).

### Paper memory (shared with all reviewers)
- **Setup facts.** NLP-LR (26 tasks from CrossFit/UnifiedQA, k = 16, GPT-2; size not stated; §5.1, §5.2). MMLU (57 tasks, k = 16, Llama3.2-3B). BBH (27 tasks, k = 10 per §5.1, instructions made trainable, Llama3-8B). ARC (400 evaluation tasks, < 4 demonstrations, Llama3.2-1B fine-tuned on the 400-task ARC training split, no augmentation or voting; §5.2). 5 random demonstration sets per task, except ARC (fixed demonstrations, single run) (§5.3, Table 1 caption). Hardware: one A100 (RTX8000 for NLP-LR) (§5.3, Appendix C). Hyperparameter grid and chosen values: Appendix C, Table 7. The split used for hyperparameter and design selection is **not stated after search**. Source of the demonstration pairs on NLP-LR/MMLU (disjoint from the evaluated queries?) is not stated. Code release not stated.
- **Headline numbers (Table 1).** CT-KV: 44.2 (NLP-LR), 43.7 (MMLU), 57.9 (BBH), 23.8 (ARC). TTT: 44.1, 43.6, 57.8, 23.8. ICL: 35.6, 41.2, 50.4, 13.3. TTT+CT-KV: 47.6, 44.1, 58.2, 25.8. Training time per task, CT-KV vs TTT: 145 s vs 342 s, 9 vs 30, 7 vs 14, 26 vs 56. MetaICL comparison in §5.4: 44.2 vs a "reported" 43.3.
- **Appendix content.** A: attention-cost analysis (Table 5). B: other initializations for baselines (Table 6). C: hyperparameters, batch sizes (Table 7). D: parameter-efficient variants CT-V, CT-Prefix, Fisher analysis (Tables 8, 9). E: trainable-parameter counts (Table 10). F: qualitative traces (Figures 5, 6). G: demonstration examples (Figures 7–9).
- **Unverifiable parts.** All figures; no supplement; the paper's code.

### Integrity signals
None found by manual search of the extracted text (no text addressed to reviewers or AI systems).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Halvard Teixeira, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / language-model adaptation, evaluation methodology
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Calibrates against what the venue actually accepts; downgrades points that rest on unverified speculation.

### Reviewer 1 (Methodology): Dr. Oksana Brandvold, industrial research lab (Europe)
- **Seniority / Expertise**: Mid-career industry scientist / parameter-efficient fine-tuning protocols, few-shot evaluation, test-time adaptation
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Searches the whole text for split and selection statements; insists on matched tuning budgets.

### Reviewer 2 (Domain): Prof. Jiahao Verbeek, NLP group, large public university (East Asia)
- **Seniority / Expertise**: Senior faculty / in-context learning, prompt-based adaptation, meta-learning for NLP
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Judges novelty claim by claim against the closest prior work.

### Reviewer 3 (Perspective): Dr. Amara Nwosu-Castellanos, cognitive-computing and systems lab (North America)
- **Seniority / Expertise**: Mid-career researcher / associative memory and fast-weight models, ML systems and serving
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; frames weaknesses as opportunities.

### Reviewer 4 (Generalist): Dr. Lucas Fenwick-Ibarra, public research institute (Latin America)
- **Seniority / Expertise**: Mid-career / general ML and NLP; typical program-committee member
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Weighs weaknesses against what ICLR papers typically contain.

### Devil's Advocate: Dr. Saoirse Kapoor-Ng, independent research lab (Oceania)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, causal inference for ML claims
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; states the steelman first.

*Personas are fictional. Proceeding with stated assumptions (target venue ICLR as requested; paper type empirical).*

---

# Phase 1: Five Reports

# Peer Review Report (Reviewer 1)

## Paper: Context Tuning for In-Context Optimization
## Reviewer: Dr. Oksana Brandvold, Methodology Reviewer (industrial research lab, Europe; fictional persona)
## Expertise: parameter-efficient fine-tuning protocols; few-shot evaluation; test-time adaptation
## Date: 2026-11-10

## Summary
The paper proposes Context Tuning: initialize a soft prompt (CT-Prompt) or a per-layer key-value prefix (CT-KV) from the activations the model produces on k demonstrations, then optimize it by gradient descent on the demonstrations themselves, with a leave-one-out mask and token dropout. It is compared with ICL, Prompt/Prefix Tuning and LoRA-based Test-Time Training on four benchmarks, each with a different model (GPT-2, Llama3.2-3B, Llama3-8B, Llama3.2-1B). The authors report gains over prompt/prefix tuning, parity with TTT at roughly half the training time, and further gains when CT-KV is run after TTT.

## Strengths
### S1: Clear, cheap, well-motivated idea with consistent gains over the natural baselines
CT-KV beats Prefix Tuning (m = 32) by +2.2/+3.8/+5.2/+14.5 and CT-Prompt beats Prompt Tuning by +1.8/+4.4/+5.5/+10.5 on NLP-LR/MMLU/BBH/ARC (Table 1, recomputed). The sign is the same on all four benchmarks.
### S2: Multi-seed reporting where it is cheap
Table 1 and Table 2 report mean ± std over 5 demonstration sets on three benchmarks, which is above the norm for few-shot papers; ARC is single-run and says so.
### S3: Useful ablation and parameter-matched baselines
Table 2 separates Leave-One-Out Masking from Token Dropout, and "m = # demo" baselines match trainable parameters (§5.4, Table 10). Appendix B–E (initializations, hyperparameter grid in Table 7, parameter counts) improve transparency.
### S4: Honest negative cases
§5.6 and Table 3 report 9 ARC tasks that ICL solves and CT-KV loses; Table 2 reports that removing masking helps on ARC.

## Weaknesses

### W1: The selection protocol for hyperparameters and design choices is unstated, and tuning budgets are unequal (MAJOR)
Protocol sweep (full-text search for validation, held-out, test set, select, tuned, checkpoint): no sentence says on which split learning rates, iteration counts, dropout rates, or the masking choice were chosen. Appendix C only says "For fair comparison, hyperparameter sweeps are performed for all methods." The grid for the Context Tuning variants has a third axis (Token Dropout ∈ {0, 0.05, 0.1}) that Prompt/Prefix Tuning do not have (36 vs 12 configurations). TTT does not appear to be in the grid: its LoRA learning rate is fixed to 1e-4 ("we follow Akyürek et al."), which is outside the stated grid {3e-4, 1e-3, 3e-3}, and Table 7 lists 8 iterations for TTT on BBH versus a stated BBH grid of {12, 16, 20, 24}. TTT+CT-KV uses 5 iterations and LR 1e-4 on MMLU, also outside the grids. If selection used the reported evaluation accuracy, all numbers in Table 1 are optimistically biased, and not equally for all rows.
- **Suggested Fix**: State the selection split per benchmark; select on held-out demonstrations (e.g., a leave-one-out score on the k demonstrations) or on a split disjoint from the evaluated queries; give TTT and the prompt baselines the same number of configurations (add Token Dropout to the baselines). About 1–2 GPU-days on the 1B–3B settings.

### W2: Attribution of the gain to "demonstration initialization" is not isolated by the paper's own numbers (MAJOR)
The "Neither" row of Table 2 (demonstration initialization without masking or dropout) gives 41.0/40.2/51.4/21.0, whereas Prefix Tuning with m = # demo and random-token initialization gives 41.1/38.8/52.8/20.5 (Table 1). That is no gain on NLP-LR and BBH and ≤ 1.4 points elsewhere. The advantage of CT-KV therefore comes from Leave-One-Out Masking plus Token Dropout, not from demonstration initialization alone, which is the framing of the Abstract and §5.4 ("This highlights the effectiveness of leveraging the model's ICL capabilities by initializing the prompt or prefix with demonstration tokens"). Token Dropout was not given to the baselines, and there is no control with demonstrations from another task or with shuffled labels.
- **Suggested Fix**: add (i) Prefix Tuning (m = # demo, random tokens) + Token Dropout, (ii) CT-KV initialized from demonstrations of a different task, (iii) CT-KV with shuffled labels. 3 variants × 3 benchmarks × 5 sets, ≈ 20 GPU-hours on the 1B–3B models.

### W3: ARC conclusions rest on a single run and a design choice selected on the evaluation tasks (MAJOR)
§5.3 states that masking is applied "across all datasets, except ARC, where performance improves without it", and Table 2 shows 23.8 (no masking) vs 22.5 (both components) on ARC. The headline ARC number for CT-KV in Table 1 (23.8) is the no-masking configuration. ARC has fixed demonstrations and one run; 23.8% of 400 tasks is 95 tasks (Table 3: 44 + 51), and the binomial standard error is ≈ 2.1 points, so the 1.3-point difference (5 tasks) that decided the setting is within noise. All ARC claims of parity (23.8 vs 23.8) and of the ablation are likewise below resolution. The ARC evaluation labels are public and the test split hidden, so this is field practice (MAJOR, not fatal), but a held-out check is needed.
- **Suggested Fix**: choose the setting on a subset of the 400 ARC training tasks; report paired bootstrap or McNemar over the 400 tasks for each ARC comparison; add demonstration-set resampling where tasks have > k pairs.

### W4: The efficiency claim is confounded and the "linear vs quadratic" statement is loosely worded (MAJOR)
Wall-clock times are measured at the "largest batch size possible", and TTT/CT-Prompt are limited to "batch sizes to 4 for NLP-LR, MMLU, and ARC" versus 16, 8 (with accumulation 2), and full batch for CT-KV (Appendix C). MMLU and BBH also use gradient checkpointing. The 2–3× time ratios (145/342, 9/30, 7/14, 26/56) therefore mix algorithmic cost with batch size and memory settings, and the attention-only analysis of Appendix A is offered as the explanation ("This k-fold reduction in self-attention complexity"). Appendix A gives per-step, per-example cost; per full pass over k examples the totals are k·(kℓ)² = k³ℓ² for TTT versus k·kℓ² = k²ℓ² for CT-KV, so "quadratic vs linear training time" (§1, §5.4) holds per step only. No experiment varies k (k is 16, 10, or < 4), no FLOPs or peak memory are reported, and at ARC's k < 4 a 2× gap cannot be the k-fold effect. Inference-time memory of the stored prefix (Table 10: 21.9–58.5 M parameters per task for CT-KV) is not discussed.
- **Suggested Fix**: report time at matched batch size and checkpointing, plus FLOPs and peak memory; add a plot of time vs k ∈ {4, 8, 16, 32, 64} on one benchmark; reword the complexity statement to "per optimization step".

### W5: "Competitive with TTT" and "complementary" are asserted without paired statistics, and the complementary gains are mostly within noise (MAJOR)
CT-KV − TTT is +0.1, +0.1, +0.1, 0.0 on the four benchmarks with stds 0.5–1.1 (Table 1): parity is plausible, but no equivalence interval or paired test is given. For TTT+CT-KV − TTT the gains are +3.5 (NLP-LR), +0.5 (MMLU; stds 0.38/0.55), +0.4 (BBH; 0.73/1.13), +2.0 (ARC, single run). §5.4 states "leading to higher performance on all benchmarks with minimal additional training time", which is supported clearly only on NLP-LR. The combination also uses its own tuned settings (Table 7) and extra compute (+30 s, +4 s, +3 s, +7 s).
- **Suggested Fix**: paired differences with 95% CIs over tasks × demonstration sets; narrow the claim to NLP-LR (and ARC if significant).

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E8/E4 | Appendix C | "hyperparameter sweeps are performed for all methods" | No selection split stated; TTT LR 1e-4 and 8 BBH iterations are outside the stated grids (Table 7) | Protocol sweep; Table 7 vs Appendix C text | High (unstated), Medium (effect) | MAJOR | State split; equalize budgets |
| ERR-2 | E4 | §5.3 vs Table 2 | "except ARC, where performance improves without it" | Setting chosen by its evaluation score; Table 1 headline (23.8) equals the "No Leave-One-Out Masking" row of Table 2 | Cross-referenced Table 1, Table 2, §5.3 | High | MAJOR (public-label evaluation split, field practice) | Select on ARC train tasks |
| ERR-3 | E5 | §5.4 | "leading to higher performance on all benchmarks with minimal additional training time" | Recomputed gains vs TTT: +3.5, +0.5, +0.4, +2.0; two are within one std | Recomputed from Table 1 | High | MAJOR | Narrow the claim |
| ERR-4 | E6 | §5.1 vs Figure 6 caption | "we sample k = 10 demonstration pairs per task" | Figure 6 caption says "We omit showing the 16 demonstration pairs of each task" for a BBH task | Cross-referenced two locations | High | MINOR | Correct one |
| ERR-5 | E5 | §1, §5.4 vs Appendix A | "CT-KV achieves linear training time complexity" | Per-step cost only; per full pass k³ℓ² vs k²ℓ² | Derived from Table 5 | Medium | MINOR | Say "per step" |

**Recomputed headline deltas (E1):** CT-KV − ICL = +8.6, +2.5, +7.5, +10.5; CT-KV − TTT = +0.1, +0.1, +0.1, 0.0; CT-KV/TTT time = 0.42, 0.30, 0.50, 0.46. These match the qualitative claims "comparable" and "at most half". The text–table numbers checked (Table 3 totals 400; 53 ICL-solved = 13.3%; Table 9 ARC 23.8 = Table 1; Table 6 token rows = Table 1) are consistent.

**Claim-to-evidence map (compressed).**
| ID | Claim | Evidence | Verdict |
|----|-------|----------|---------|
| C1 | beats Prompt/Prefix Tuning | Table 1 | Supported (margin small on NLP-LR; attribution to initialization only partial, W2) |
| C2 | ≈ TTT at ≤ ½ time | Table 1, App. A/C | Partially (parity yes; time ratio confounded by batch size, W4) |
| C3 | masking and dropout crucial | Table 2 | Supported on 3 benchmarks; dropout effect ≤ 0.3–1.1 and often within std; reversed on ARC |
| C4 | complementary with TTT | Table 1 | Partially (NLP-LR, ARC) |
| C5 | ICL cache incomplete | Table 4 | Unsupported as a mechanism (see DA, R2) |

**Minor:** Table 1 caption says each cell is "delimited by /" but the table has separate columns; Table 10 has an unlabeled "Context Tuning" row (exactly half of CT-KV's count, presumably CT-V); Table 6 prints "10.22" and "11.03" with two decimals; GPT-2 size and Llama3 base-vs-instruct variants are not stated.

## Missing References
Not my role; see Reviewer 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea, but unstated selection split, unequal tuning, and single-run ARC (Rigor 56, Exp. 52) |
| Clarity | 3 | Clear writing; a few inconsistencies |
| Significance | 2 | Parity with TTT, modest gains vs ICL on MMLU |
| Originality | 2 | Combines known pieces (Prefix Tuning, KV cache, TTT's leave-one-out) |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the unstated selection protocol with unequal tuning budgets, and a TTT parity result that is not the headline gain a reader needs for a method of this size; offset by consistent gains over prompt/prefix tuning and good ablations.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Method is clear; leave-one-out mechanism and selection protocol not fully specified |
| Clarity & Presentation | 66 | Competent | Easy to follow; some cross-section inconsistencies |
| Novelty & Originality | 52 | Developing | Incremental relative to Prefix Tuning and TTT |
| Significance & Impact | 52 | Developing | Useful, but parity not superiority over TTT |
| Experimental Validation | 52 | Developing | Four benchmarks, 5 sets, but W1–W5 |
| Reproducibility | 62 | Competent | Table 7 grid and chosen values; no code, GPT-2 size missing |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations section is thin |

## Questions for Authors
1. On which split were learning rate, iterations, Token Dropout and the ARC masking choice selected for each benchmark, and where do the k demonstrations of NLP-LR and MMLU come from relative to the evaluated queries? (A split disjoint from evaluation would remove W1 and raise my score by about one band.)
2. Is Θ⁻ⁱ_CT obtained by re-running the model on C⁻ⁱ, or by masking pair i out of the KV cache computed on the full C? In the latter case the K/V of later pairs were computed while attending to pair i (causal attention), so pair i's answer is not fully hidden when solving pair i. How does masking behave then?
3. What do TTT and CT-KV cost at the same batch size and without gradient checkpointing, and does the ratio grow with k?

## Limitations Assessment
**Partially.** §6 mentions only overfitting on some tasks. Missing: white-box access requirement, per-task prefix storage (Table 10), single-seed ARC, models ≤ 8B, sensitivity to k.

## Ethics Review Flag
**No**: public benchmarks, no human data.

## Overall Score
**3**: Borderline Reject. A clean, plausible method with real but modest gains, whose comparison with TTT and baselines is not yet protocol-safe (W1, W3) and whose headline mechanism is not isolated (W2).

## Confidence
**4**: Confident; I searched the full text and recomputed the headline deltas, but could not see figures or code.

---

# Peer Review Report (Reviewer 2)

## Paper: Context Tuning for In-Context Optimization
## Reviewer: Prof. Jiahao Verbeek, Domain Reviewer (NLP group, large public university, East Asia; fictional persona)
## Expertise: in-context learning; prompt-based adaptation; meta-learning for NLP
## Date: 2026-11-10

## Summary
The paper places prompt/prefix tuning and Test-Time Training under a label, "In-Context Optimization", and proposes to tune a context representation derived from demonstrations rather than model weights. Its positioning is that prompt-based methods start from "irrelevant tokens" while ICL alone is a single forward pass; Context Tuning combines both. Evidence comes from NLP-LR, MMLU, BBH and ARC.

## Strengths
### S1: A natural and well-chosen bridge between ICL and PEFT
Initializing a KV prefix from the forward pass on the demonstrations (§4.3, Figure 2) is a simple idea that frames a real question: how much can gradient steps on the context improve on one forward pass.
### S2: Appropriate closest-work comparison
TTT (Akyürek et al., 2024) is correctly identified as the nearest relative (§1, §2, §4.2) and is run as a baseline on all four benchmarks, including the combination experiment, which is a good way to place the contribution.
### S3: The related work is accurate on the PEFT line
Prompt Tuning, Prefix Tuning, P-Tuning/v2, AutoPrompt and Instruction Prompt Tuning are described correctly and differentiated in §2.
### S4: The attribution of what is new is honest in the text
§4.3 states that the leave-one-out technique is TTT's idea transferred to a frozen-model setting ("In contrast to TTT's leave-one-out technique…").

## Weaknesses

### W1: Novelty is incremental, and the claimed "framework" adds little (MAJOR for Novelty, not fatal)
By hand-built claim profile (see addendum): C1 is incremental-to-medium (nearest: Instruction Prompt Tuning, cited in §2 but not compared; SPoT-style prompt initialization from other tasks); C3's leave-one-out idea is TTT's (§4.2, §4.3). The ICO definition (§4.1, Eq. 3) is a relabeling: Prompt/Prefix Tuning are excluded "by definition" and TTT is included, so the framework does not generate a prediction or a new method beyond the authors' own. The related work also omits the demonstration-to-representation line (task vectors, function vectors, gist tokens, context distillation) that directly concerns how much a context can be compressed into a learned state.
- **Suggested Fix**: add these lines to §2, and compare empirically with at least one context-compression or few-shot-PEFT baseline (below). Medium effort.

### W2: Missing empirical comparisons against the closest non-TTT alternatives (MAJOR)
§2 discusses Instruction Prompt Tuning ("expert-curated few-shot demonstrations are prepended to a learned soft prompt") but it is not a baseline, although it is the nearest "demonstrations plus soft prompt" method. There is also no comparison with few-shot LoRA/(IA)³-style fine-tuning without context (the standard PEFT alternative to ICL) and no ICL with more compute (e.g., majority vote over demonstration orderings). Without them, "outperforms traditional prompt-based adaptation" is a statement about random-init prompts and prefixes only.
- **Suggested Fix**: add (i) LoRA fine-tuning on the k demonstrations without context, (ii) hard demonstrations prepended to a trainable soft prompt (the Instruction Prompt Tuning recipe). ~10 GPU-hours on the 1B–3B models.

### W3: The §5.7 account of why CT-KV beats ICL is not supported by the diagnostic (MAJOR)
Table 4 shows ICL accuracy on the demonstration pairs themselves of 81.9/84.1/89.3/22.6 (NLP-LR/MMLU/BBH/ARC), read as "performance surprisingly remains far from perfect, suggesting that the KV cache often fails to encode the task adequately." Accuracy on demonstration pairs of 82–89%, against 35.6/41.2/50.4 on queries (Table 1), shows the cache retains the demonstrations well and generalizes poorly; recall of the training pairs is not task encoding, and no experiment measures whether CT-KV makes the cache encode the task better (e.g., probing, or accuracy of the cache on held-out pairs as optimization proceeds). The Conclusion's "more accurate representation for steering the model" is therefore a hypothesis. Also, at GPT-2 scale ICL is barely above zero-shot (35.6 vs 34.9, Table 1), so the premise "leveraging the model's inherent ICL ability" is weak exactly where CT-KV's gain over ICL is largest (+8.6).
- **Suggested Fix**: reword §5.7 as a hypothesis, or add a held-out-pair probe across training iterations.

### W4: Citation and attribution inconsistencies (MINOR–MAJOR as a group)
§1 attributes ICL to Brown et al. (2020) ("a process known as In-Context Learning (ICL)") but §2 says "Introduced by Radford et al. (2019)". "In-Context Vectors" (Liu et al., 2024b) is cited as an example of test-time training for "controllable language generation", although it derives a latent steering vector from demonstrations, which is directly the ICL-representation question the paper studies, and is not compared. Franzen et al. (2024) is listed with arXiv number 2505.07859.
- **Suggested Fix**: unify the ICL attribution; discuss In-Context Vectors as a related demonstration-derived representation; check the Franzen entry year.

## Literature-check addendum
Mode: **strict**, cutoff 2025-09-24. Queries (4 counted): soft-prompt/demonstration initialization (C1), test-time training/demonstrations (C2), key-value prefix optimization (C3), ARC test-time adaptation (benchmark); 2 further queries refused by the script (5 words; title overlap). `coverage` and expansion rounds were not run (arXiv keyword search returned mostly off-topic results; stopped early), so the gaps listed in `coverage` are left open. arXiv-only search, so "no close prior work found" is not evidence of novelty. `similarity`: closest prior works (by TF-IDF) are TTT (cosine 0.335, cited and differentiated), "On the Role of Attention in Prompt-tuning" (0.312, an analysis of attention in prompt-tuning; different contribution) and SPoT (0.217). No text overlap (0 shared 8-grams). No recent-preprint or concurrent item was required as a comparison.

**Per-claim novelty (rated by hand from the kept abstracts; the `novelty` script was not run).**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------------|-----------|
| C1 demo-initialized prompt/prefix | method | medium | Soft Prompt Transfer (SPoT), level 2, https://arxiv.org/abs/2110.07904v2, prior (peer-reviewed), not cited | Prompt initialization from a source task's learned prompt, not demonstrations of the target task; Instruction Prompt Tuning (cited) is closer, level 3 |
| C2 CT-KV vs TTT efficiency | result | medium | TTT (Akyürek et al.), level 3, https://arxiv.org/abs/2411.07279v2, prior (arXiv-only, 6+ months), cited | Same objective and leave-one-out idea; tunes context instead of LoRA weights |
| C3 masking and dropout | method | incremental | TTT, level 4 for the leave-one-out idea | Cited and differentiated in §4.3 |
| C4 TTT + CT-KV | result | medium | none found | A combination result |
| C5 ICO framework / cache-incompleteness | problem/resource | incremental | none found at level ≥ 4 | Relabeling; mechanism untested |

**Novelty delta (closest prior works).**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| Tune a context built from demonstrations | TTT, https://arxiv.org/abs/2411.07279v2 | Gradient steps on demonstrations with leave-one-out, tuning LoRA weights | Tunes the KV prefix with frozen weights | Yes |
| Demonstration-derived soft prompts | Instruction Prompt Tuning (cited in §2) | Prepends curated demonstrations to a learned prompt | Initializes from and then optimizes the demonstration KV | Yes, but no empirical comparison |
| Prompt initialization | SPoT, https://arxiv.org/abs/2110.07904v2 | Initializes the target prompt from source-task prompts | Initializes from target demonstrations | No (Helpful) |

**Baseline scout.** TTT reports results on ARC and BBH in its own setting (larger models, augmentation); the paper compares in a different setting (1B model, no augmentation or voting for ARC, §5.2). A gap in numbers between settings is not a missing baseline and no under-reported baseline can be asserted; the same-setting TTT run in Table 1 is the right control.

**Field snapshot (as of the cutoff).** About four years ago the dominant approach to frozen-model adaptation was soft-prompt and prefix tuning (Prompt Tuning, Prefix Tuning, P-Tuning v2), with few-shot PEFT (T-Few) shown to rival ICL; the shift since has been toward ICL at scale, meta-trained in-context learners (MetaICL, in-context tuning), analyses of what ICL encodes (task and function vectors, implicit gradient descent views), and, in 2024, test-time training with LoRA as the state of the art on ARC. Open problems named by recent work: efficient per-task adaptation at test time, robustness of ICL to demonstration choice, and what the context compresses. For this sub-field a significant contribution is either a new capability on a hard benchmark (ARC) or a clear efficiency gain at matched accuracy against TTT with matched tuning; +0.5 points on MMLU is incremental, while a 2× training-time reduction at equal accuracy is meaningful provided the cost is measured under matched settings.

## Missing References
*All entries below were verified with `related_search.py verify` (found on arXiv); venue/year as I recall them.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Liu, Tam, Muqeeth, Mohta, Huang, Bansal, Raffel. "Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning" (NeurIPS 2022). https://arxiv.org/abs/2205.05638v2 | Standard few-shot PEFT alternative to ICL; a missing baseline family |
| Important | Hendel, Geva, Globerson. "In-Context Learning Creates Task Vectors" (Findings of EMNLP 2023). https://arxiv.org/abs/2310.15916v1 | Directly about the task information held in representations derived from demonstrations (cf. §5.7) |
| Important | Mu, Li, Goodman. "Learning to Compress Prompts with Gist Tokens" (NeurIPS 2023). https://arxiv.org/abs/2304.08467v3 | Learned compressed context states for a frozen model |
| Helpful | Todd et al. "Function Vectors in Large Language Models" (ICLR 2024). https://arxiv.org/abs/2310.15213v2 | Demonstration-derived functional representations |
| Helpful | Snell, Klein, Zhong. "Learning by Distilling Context" (arXiv 2022). https://arxiv.org/abs/2209.15189v1 | Moves context into parameters; relevant to CT vs TTT framing |
| Helpful | Vu, Lester, Constant, Al-Rfou, Cer. "SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer" (ACL 2022). https://arxiv.org/abs/2110.07904v2 | Prompt initialization from learned prompts |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mechanism claims in §5.7 not supported |
| Clarity | 3 | Well written |
| Significance | 2 | Moderate for a sub-area |
| Originality | 2 | Incremental over TTT and prefix tuning |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is a sensible recombination (TTT's leave-one-out + Prefix Tuning on a demonstration KV cache) with parity, not superiority, against its closest relative, and the framework and mechanism sections do not add insight.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound objective; mechanism in §5.7 weakly argued |
| Clarity & Presentation | 68 | Competent | Clear, with attribution slips |
| Novelty & Originality | 50 | Developing | Incremental claims; framework is a relabeling |
| Significance & Impact | 54 | Developing | Practical if the efficiency claim holds under matched settings |
| Experimental Validation | 55 | Competent | Missing non-TTT PEFT and Instruction-Prompt-Tuning baselines |
| Reproducibility | 62 | Competent | Hyperparameters given |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. What does Instruction Prompt Tuning (hard demonstrations + learned soft prompt) score in your setting? A result close to CT-KV would lower my Novelty score; a clear gap would raise it.
2. Do you see the same gains with k larger than 16 or with instruction-tuned models, where ICL is already strong?
3. Can a held-out-pair probe show the cache encodes the task better after optimization (§5.7)?

## Limitations Assessment
**Partially.** The thin limitations paragraph does not mention that gains are over random-init prompts only.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. A tidy method whose novelty is incremental and whose positioning relies on baselines that are not the closest ones.

## Confidence
**4**: Confident on the PEFT/ICL literature; the literature check is arXiv-only and shallow.

---

# Peer Review Report (Reviewer 3)

## Paper: Context Tuning for In-Context Optimization
## Reviewer: Dr. Amara Nwosu-Castellanos, Perspective Reviewer (cognitive-computing and systems lab, North America; fictional persona)
## Expertise: associative memory and fast-weight models; ML systems and serving
## Date: 2026-11-10

## Summary
The paper treats a transformer's KV cache over demonstrations as an adjustable memory and refines it by gradient descent, giving a per-task adaptation that does not change weights. It is shown to beat random-init prompt/prefix tuning and to match TTT at lower cost, with benefits on both language-understanding and abstract-reasoning benchmarks.

## Strengths
### S1: A useful conceptual move toward "memory you can train"
Treating the cache as trainable state (§4.3, Figure 2 caption) connects to fast-weights and associative-memory views of attention, a link the authors touch on in §2 via Zhao (2023). It suggests a cheap, per-task, swappable adapter.
### S2: Practical attraction of weight-free adaptation
Frozen weights mean one base model can serve many tasks with per-task state (Table 10 gives the parameter count of that state), which is attractive for multi-tenant serving and avoids weight-merge conflicts.
### S3: Evidence across very different task types
NLP-LR/MMLU (knowledge, classification) and ARC/BBH (symbolic) suggest the effect is not benchmark-specific (Table 1), and the traces in Figures 5–6 (Appendix F; judged from captions) are illustrative of learning dynamics.
### S4: Good complementarity story
The TTT+CT-KV result (+3.5 on NLP-LR) hints that context and weight updates can carry different information.

## Weaknesses

### W1: Deployment costs are not reported (opportunity)
CT-KV's per-task state is 21.9 M (ARC) to 58.5 M (BBH) parameters (Table 10), comparable to TTT's LoRA (47.2 M–157.3 M) and far above Prefix Tuning (m = 32). For serving, what matters is per-task optimization latency, KV memory per task, whether the cache can be quantized or compressed (§6 mentions this only as future work), and the break-even number of queries per task versus plain ICL. The paper reports training seconds but not inference memory or latency.
- **Suggested Fix**: add a cost table (state size in MB, optimization time, per-query latency, break-even queries) and test with KV compression as proposed in §6.

### W2: Assumptions about the demonstrations (opportunity)
Three assumptions are implicit: (i) the k demonstrations are clean and from one task (label noise would be memorized; masking only partly protects), (ii) the evaluation queries are i.i.d. with the demonstrations, and (iii) the model's ICL is a useful starting point (at GPT-2 scale ICL ≈ zero-shot on NLP-LR, Table 1). §5.6 shows overfitting (9 ARC tasks lost). A stress test with noisy labels, distribution shift between demonstrations and queries, and larger or instruction-tuned models would show where the method stops helping.
- **Suggested Fix**: add one robustness experiment (label noise 10–30%, or demonstrations from a neighboring task) and one larger-model run.

### W3: Access and privacy considerations
CT-KV needs white-box access to layerwise activations and gradient computation, so it does not apply to API-only models, and stored per-task prefixes encode the demonstrations (which may be private). A short broader-impact note would fit.
- **Suggested Fix**: add a paragraph on applicability (white-box only) and on privacy of stored caches.

**Connections to other fields.** (1) Associative memory / fast weights: gradient steps on a cache as a delta-rule-like update. (2) Meta-learning: leave-one-out training of an adapter resembles cross-validation inside an inner loop, and MAML-style learning of an initialization for the cache would be a natural step. (3) Systems: KV-cache compression and eviction methods cited in §6 could be tested as initializers. Future directions: composing or merging prefixes across tasks, amortizing the optimization with a hypernetwork that predicts the cache update from the demonstrations.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Reasonable evidence with caveats |
| Clarity | 3 | Clear |
| Significance | 3 | Practical for per-task adaptation |
| Originality | 2 | Recombination, interesting framing |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a simple, practical idea with consistent gains across heterogeneous benchmarks and honest failure cases; its remaining gaps (deployment cost, assumptions) are typical of accepted empirical papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Sound approach with typical gaps |
| Clarity & Presentation | 70 | Competent | Readable, well organized |
| Novelty & Originality | 60 | Competent | Useful reframing |
| Significance & Impact | 64 | Competent | Moderate, practical |
| Experimental Validation | 60 | Competent | Wide benchmark set, standard baselines |
| Reproducibility | 62 | Competent | Table 7 and Appendix C |
| Ethical Compliance | 62 | Competent | Low-risk work; no impact statement |

## Questions for Authors
1. What is the break-even number of queries per task versus ICL once optimization time is counted? A favorable value would raise my Significance score.
2. How sensitive is CT-KV to wrong labels among the k demonstrations?
3. Can a cache optimized on one model size or checkpoint be reused or distilled?

## Limitations Assessment
**Partially.** §6 covers overfitting only.

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. A practical, simple idea with consistent gains whose open questions are mostly extensions.

## Confidence
**3**: Fairly confident; I did not audit the experimental protocol in depth (Reviewer 1's role).

---

# Peer Review Report (Reviewer 4)

## Paper: Context Tuning for In-Context Optimization
## Reviewer: Dr. Lucas Fenwick-Ibarra, Generalist Reviewer (public research institute, Latin America; fictional persona)
## Expertise: general ML and NLP; typical program-committee member
## Date: 2026-11-10

## Summary
The paper proposes tuning a context, initialized from few-shot demonstrations (as soft prompt tokens or as a KV prefix), instead of tuning model weights. CT-KV matches test-time training on four benchmarks at roughly half the per-task training time and improves on random-initialization prompt and prefix tuning; it can also be applied after TTT.

## Strengths
### S1: Contribution is easy to state and the paper is well organized
Background (§3) → framework (§4) → experiments (§5) → analysis (§5.7) is easy to follow, notation is minimal, and Figure 2's caption explains the masking.
### S2: Convincing breadth for a method paper
Four benchmarks, four models (1B–8B), 5 demonstration sets where feasible, parameter-matched baselines, ablations (Table 2), parameter-efficient variants (Table 9) and a trainable-parameter table (Table 10).
### S3: Clear practical message
CT-KV ≈ TTT accuracy at ≤ ½ the time (Table 1) is a message a practitioner can use.
### S4: Candid treatment of a failure mode
§5.6 and Figure 4 show where CT-KV loses to ICL.

## Weaknesses

### W1: Several headline phrases are stronger than the tables (MAJOR for presentation honesty)
"By a wide margin across all benchmarks" (§5.4) is +2.2 on NLP-LR for CT-KV vs Prefix Tuning and +1.8 for CT-Prompt vs Prompt Tuning (Table 1). "Leading to higher performance on all benchmarks" for TTT+CT-KV rests on +0.5 and +0.4 on MMLU/BBH (stds 0.4–1.1). "Significantly" is used without any test.
- **Suggested Fix**: reword to the effect sizes shown, or add paired tests.

### W2: The framework and §5.7 take space but add little for the reader (MINOR–MAJOR)
The ICO section (§4.1) mainly relabels TTT and the proposed methods; §5.7's "two-stage" diagnostic (Table 4) is not tied to any result about CT-KV. A reader who wants to know why masking and dropout, rather than initialization, drive the gain (compare "Neither" in Table 2 with the m = # demo rows in Table 1) gets no answer.
- **Suggested Fix**: shorten §4.1 and §5.7; use the space for the ablation that isolates initialization.

### W3: Model/benchmark pairing hides scale effects (MAJOR for interpretation)
Each benchmark uses a different model (GPT-2, Llama3.2-3B, Llama3-8B, Llama3.2-1B; §5.2), so "works across model sizes" (§5.3) cannot be separated from "works across benchmarks". GPT-2's size is unstated.
- **Suggested Fix**: run at least two models on one benchmark (e.g., MMLU with 1B, 3B, 8B); state all checkpoints.

### Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Claims supported by evidence (soundness) | Partly | Table 1, Table 2; §5.7 mechanism unsupported |
| Significance of contribution | Partly | Parity with TTT, gains over weak baselines |
| Presentation | Met | §3–§5 |
| Reproducibility (ICLR encourages code, details) | Partly | Table 7, Appendix C; no code statement, GPT-2 size missing |
| Honest limitations | Partly | §6, §5.6 (thin) |
| Ethics statement | Not met but nothing at stake | none |

**Typical-accepted-paper test.** Weaknesses such as missing a baseline family, an unstated selection protocol and overclaimed wording are common among accepted ICLR papers; the combination with a tuning-protocol gap is borderline.

**Minor:** Table 1 caption mentions a "/" delimiter that is not in the table; label inconsistencies ("Prefix-Tuning" in Figure 1, "Context Tuning" row in Table 10); BBH k = 10 (§5.1) vs 16 (Figure 6 caption); Franzen et al. year vs arXiv number.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid with caveats |
| Clarity | 3 | Good |
| Significance | 3 | Useful |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear idea, consistent gains over standard baselines on four benchmarks with multi-seed reporting; weaknesses typical of accepted papers, though close to the line.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound and standard |
| Clarity & Presentation | 72 | Competent | Clear, minor inconsistencies |
| Novelty & Originality | 58 | Competent | Incremental but useful |
| Significance & Impact | 62 | Competent | Moderate |
| Experimental Validation | 60 | Competent | Breadth good; baselines limited |
| Reproducibility | 64 | Competent | Details present, no code |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Which of the three components (initialization, masking, dropout) is responsible for the gain over m = # demo Prefix Tuning? A clean decomposition would raise my score.
2. Will code and per-task prefixes be released?
3. Which GPT-2 size and which Llama3 variants (base/instruct) were used?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. The community would benefit from a cheap alternative to TTT; the weaknesses are fixable in revision.

## Confidence
**4**: Confident; did not re-derive the complexity analysis in detail.

---

# Devil's Advocate Report

## Paper: Context Tuning for In-Context Optimization
## Reviewer: Dr. Saoirse Kapoor-Ng, Devil's Advocate (independent research lab, Oceania; fictional persona)

## Steelman
CT-KV is a simple gradient-based refinement of the demonstration KV cache that closes most of the gap to LoRA-based TTT at under half the training time, and consistently beats random-init prompt and prefix tuning, with a leave-one-out mask and token dropout as two non-obvious ingredients that the ablations show to matter on three of four benchmarks.

## Core Argument Chain
1. Prompt/prefix tuning initialize from irrelevant tokens; ICL uses demonstrations only through a forward pass.
2. Initializing a trainable prefix from the demonstration KV cache lets gradient descent start from a task-aware point (Table 1: beats Prefix/Prompt Tuning).
3. Leave-one-out masking and token dropout prevent retrieval and overfitting (Table 2).
4. CT-KV matches TTT's accuracy at ≤ ½ the training time, because its per-step cost is linear in k (Table 1, Appendix A).
5. ICL's cache is an incomplete task encoding, which gradient steps repair (Table 4).
∴ Optimizing the context, rather than the weights, is an effective and efficient way to adapt LLMs to few-shot tasks.

## Strongest Counter-Argument
The paper's causal story is "demonstration initialization turns ICL into a head start for optimization," but its own tables say something different. With demonstration initialization, no masking and no dropout ("Neither", Table 2), CT-KV scores 41.0/40.2/51.4/21.0, indistinguishable from Prefix Tuning with random-token initialization and the same number of parameters (41.1/38.8/52.8/20.5, Table 1). The gain appears only when two training-time devices are added, and neither is tested on the baselines (token dropout) or can be applied to them (masking). On NLP-LR, where GPT-2's ICL is nearly zero-shot (35.6 vs 34.9), the model that is supposedly extracting "task-specific information" from the demonstrations barely does; yet CT-KV adds +8.6. A simpler account is that any prefix trained for a few hundred steps on k = 16 examples, with dropout and with each example evaluated against the remaining ones, behaves like a small-data PEFT method, and that what is credited to ICL is regularization. Under that account the headline comparison is against baselines that were not given the same regularizer and were tuned with one third of the configurations (12 vs 36, Appendix C), the parity with TTT is a parity between two tuned PEFT methods, and §5.7's claim that the "KV cache fails to encode the task" is a story told on top of a retrieval diagnostic (82–89% of demonstration answers recovered) that shows the opposite of loss. A skeptic would say the paper has shown a useful PEFT recipe, not that Context Tuning (the idea of initializing from the context) is what works. To rebut, the authors need the three controls listed in R1-W2 and a protocol that selects hyperparameters on data disjoint from the evaluated queries, because the paper does not say what that data was.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main comparisons with ICL and with Prompt/Prefix Tuning hold in the full configuration at every benchmark (Table 1), and the unstated selection split is a question on protocol (MAJOR); the one explicit selection by score (masking off on ARC) concerns a public-label evaluation split where the test labels are hidden and, at the other value (22.5), CT-KV still beats ICL (13.3) and Prefix Tuning (20.5), so the main claim survives.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic/Evidence (alternative explanation) | Table 1 vs Table 2; §5.4 | "Neither" (41.0/40.2/51.4/21.0) ≈ Prefix Tuning m = # demo (41.1/38.8/52.8/20.5); the claimed benefit of "initializing with demonstration tokens" is not isolated. Evidence supports a narrower claim (the full recipe helps). | Controls: token dropout on baselines; other-task and shuffled-label initialization |
| DA-M2 | Evidence (protocol) | Appendix C; §5.3; Table 7 | Selection split not stated (protocol sweep: no "validation"/"held-out"/"test set" statement); CT variants get 36 configurations vs 12; TTT LR and BBH iterations (1e-4; 8) lie outside the stated grids; ARC masking choice made by its eval score: "except ARC, where performance improves without it" (Table 1 CT-KV ARC 23.8 = Table 2 "No Leave-One-Out Masking"). Selection decision-table row: ARC chosen value is best-scoring and gives the headline, but the main claim holds at 22.5 → MAJOR. | State split; equal budgets; select on ARC train tasks |
| DA-M3 | Overclaiming (E5) | §5.4; Table 1 | "Leading to higher performance on all benchmarks": +0.5 (MMLU, stds 0.38/0.55) and +0.4 (BBH, 0.73/1.13); "both by a wide margin" vs +2.2 and +1.8 on NLP-LR; "significantly" without a test. Evidence supports a weaker claim, does not contradict. | Paired tests; narrow wording |
| DA-M4 | Logic (§5.7 mechanism) | §5.7, Table 4, §6 | Table 4's 81.9/84.1/89.3 on demonstration pairs show the cache retains the demonstrations; "the KV cache often fails to encode the task adequately" and "more accurate representation" are not measured after CT-KV. | Probe held-out pairs across iterations, or reword as hypothesis |
| DA-M5 | Evidence (efficiency) | Appendix A, C; Table 1; §1 | Batch size 4 (TTT, CT-Prompt) vs 16/8/full (CT-KV) and gradient checkpointing on MMLU/BBH; attention-only per-step analysis used to explain wall-clock ratios; per-pass totals are k³ℓ² vs k²ℓ²; no k sweep (ARC k < 4 also shows a 2× gap). | Matched-batch timings, FLOPs, memory, k sweep |
| DA-M6 | Logic (validity of masking) | §4.3; Figure 2 caption; Eq. for CT-KV | The paper does not say how Θ⁻ⁱ is built: if it is the full-context KV with pair i's entries masked, later pairs' K/V (computed with causal attention over pair i) still carry pair i's answer, so "prevents the model from simply retrieving" (Figure 2 caption) holds only partly. Unverifiable from the text, so raised as a question for the authors, not an error. | Describe the construction; if full-context, recompute K/V on C⁻ⁱ and report both |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §5.1 vs Figure 6 caption | BBH k = 10 vs "16 demonstration pairs" |
| DA-m2 | Consistency | Appendix A | "TTT prepends p trainable tokens" contradicts §4.2 where TTT trains LoRA and conditions on C⁻ⁱ (cost analysis unaffected) |
| DA-m3 | Consistency | Table 1 caption; Table 10 | "delimited by /" vs separate columns; unlabeled "Context Tuning" row (half of CT-KV, presumably CT-V) |
| DA-m4 | Citation | §1 vs §2; References | ICL "known as … (Brown et al., 2020)" vs "Introduced by Radford et al. (2019)"; Franzen et al. year vs arXiv number |
| DA-m5 | Comparison | §5.4 | MetaICL's "reported 43.3% accuracy" compared with CT-KV's 44.2 without stating model size or metric equivalence (a 0.9-point difference vs a single published number) |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| CT-KV at most half of TTT's time | 145/342, 9/30, 7/14, 26/56 | 0.42, 0.30, 0.50, 0.46 | Yes (BBH exactly half) |
| CT-KV vs TTT "comparable" | 44.2/43.7/57.9/23.8 vs 44.1/43.6/57.8/23.8 | +0.1, +0.1, +0.1, 0.0 | Yes |
| TTT+CT-KV higher "on all benchmarks" | 47.6/44.1/58.2/25.8 vs 44.1/43.6/57.8/23.8 | +3.5, +0.5, +0.4, +2.0 | Higher numerically; two within one std |
| ARC CT-KV 23.8 = 95 tasks | Table 3: 44 + 51 | 95/400 = 23.75 | Yes |
| ICL ARC 13.3 | Table 3: 44 + 9 = 53 | 53/400 = 13.25 | Yes |
| Table 3 total | 44 + 51 + 9 + 296 | 400 | Yes |
| CT-KV beats Prefix Tuning "by a wide margin" | NLP-LR 44.2 vs 42.0 | +2.2 | Overstated for NLP-LR |

## Ignored Alternative Explanations
- Regularization (token dropout, per-example evaluation against the rest) rather than ICL-derived initialization drives the gains (DA-M1).
- Differences in tuning effort and batch settings explain part of the efficiency and accuracy ordering (DA-M2, DA-M5).
- ARC differences of 1–2 points are within sampling noise of 400 tasks (≈ 2.1 points).
- ICL's low demonstration-pair accuracy on ARC (22.6) may reflect ARC's difficulty for a 1B model, not cache incompleteness.

## Missing Stakeholder Perspectives
Practitioners who need a fixed per-query latency budget, API-only users who cannot use white-box methods, and owners of private demonstration data stored as per-task caches.

## Observations (Non-Defects)
Leave-one-out masking and the honest ARC reversal in Table 2, the parameter-matched baselines, the explicit failure analysis in Table 3/Figure 4, and the appendix that reports alternative baseline initializations (Table 6) all make the paper more checkable than most.

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline mechanism is not isolated and the tuning protocol is unstated.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Mechanism and selection issues (DA-M1, M2, M6) |
| Clarity & Presentation | 66 | Readable; overclaimed phrases |
| Novelty & Originality | 50 | Incremental over TTT/Prefix Tuning |
| Significance & Impact | 50 | Parity with TTT; modest absolute gains on MMLU |
| Experimental Validation | 48 | Baselines under-tuned and incomplete; ARC single run |
| Reproducibility | 60 | Table 7 and Appendix C present; no code |
| Ethical Compliance | 60 | Nothing at stake |

## Overall: 3 | Confidence: 4

---

# Phase 1.5/1.6: Literature Check Summary and Report Check

**Literature check (Phase 1.5).** Strict mode; cutoff 2025-09-24; 4 counted queries (C1, C2, C3, one benchmark query); 2 refused by the script's guardrails; 5 references verified (all found); `similarity` run (closest: TTT, 0.335; no text overlap); `coverage`, `scout` and `novelty` scripts not run, gaps left open (arXiv keyword search returned mostly off-topic results). Fingerprint, kept results and ledger are in the results folder.

**Report check (Phase 1.6).** Each weakness tested for specificity, whether the paper already answers it, consistency with the paper, and actionability. Scores were not changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Parameter counts not reported (considered during drafting) | Dropped | Appendix E/Table 10 reports them |
| R1 | "Complexity is quadratic vs linear" as an error (ERR-5) | Rewritten as MINOR wording point | §4.3 says "for each optimization step"; only §1/§5.4 wording is loose |
| R4 | "No limitations discussion" (considered) | Rewritten as "limitations thin" | §6 has a Limitations paragraph (overfitting) |
| R2 | TTT not compared (considered) | Dropped | TTT is a baseline in Table 1 |
| DA | DA-M6 (masking leakage) | Kept, wording changed from error to question | The construction of Θ⁻ⁱ is not stated, so it cannot be verified (Hard Rule 10) |
| R3 | Corruption-robustness and fairness items (considered) | Dropped | Not applicable to this text-only few-shot setting |
| R1/R4/DA | Typos and caption slips | Moved to Minor lines | Cosmetic |

---

# Phase 2: Synthesizer Package (Part A)

**Merged issue list and classes**

| Issue | Sources | Class |
|-------|---------|-------|
| Selection split unstated; unequal tuning budgets | R1-W1, DA-M2 | CONSENSUS-2 (hinges) |
| Gain not attributed to demonstration initialization | R1-W2, R4-W2 (partly), DA-M1 | CONSENSUS-3 (hinges) |
| ARC single run and masking choice on eval | R1-W3, DA-M2 | CONSENSUS-2 |
| Efficiency confounds and complexity wording | R1-W4, DA-M5 | CONSENSUS-2 (hinges) |
| TTT parity / complementarity overstated | R1-W5, R4-W1, DA-M3 | CONSENSUS-3 |
| §5.7 mechanism unsupported | R2-W3, R4-W2, DA-M4 | CONSENSUS-3 |
| Missing baselines (Instruction Prompt Tuning, few-shot PEFT) and related lines | R2-W1, R2-W2 | SOLO |
| Deployment cost, assumptions, white-box access | R3-W1–W3 | SOLO |
| Model/benchmark pairing | R4-W3 | SOLO |
| Masking construction may leak (question) | R1-Q2, DA-M6 | CONSENSUS-2 |
| Novelty incremental | R2-W1, R1 novelty score | SPLIT with R3 (R3 sees "useful reframing") |
| Minor inconsistencies | R1, R2, R4, DA | CONSENSUS-4 (cosmetic) |

DA-CRITICAL: none. SPLIT: overall judgment (R3, R4: 4; R1, R2, DA: 3).

**Official output (provisional, before EIC weights; `scores_before.json` → `before.json`):** official ratings R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40; composite 58.4 → band 3. No consistency warnings.

---

# Phase 2: EIC Meta-Review (Prof. Halvard Teixeira)

*I read all five reports and the package first, then re-read the abstract, §1, §4.3, Table 1, Table 2, §5.3–5.7, Appendix A/C/E.*

## The Case For and Against
- **For acceptance:** A simple, well-motivated adaptation method with consistent gains over the standard prompt/prefix baselines on four benchmarks, 5-set variance reporting on three of them, a useful ablation, a candid failure analysis, and a TTT-parity result at roughly half the time that is of practical interest.
- **Against acceptance:** The comparison protocol is not stated (selection split, unequal tuning), the paper's own ablation shows the gain does not come from demonstration initialization alone (Table 2 "Neither" ≈ Table 1 Prefix Tuning m = # demo), the efficiency and "complementary" claims are weaker than worded, and the closest alternatives (Instruction Prompt Tuning, few-shot PEFT) are not baselines.

## Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "Neither" ≈ Prefix Tuning (m = # demo) | R1-W2, DA-M1 | Table 1, Table 2 | **Verified** | 41.0/40.2/51.4/21.0 vs 41.1/38.8/52.8/20.5; supports a narrower claim, does not contradict the paper's main result (the full method still wins) |
| Selection split for hyperparameters not stated | R1-W1, DA-M2 | App. C, §5.3 | **Verified** | Text search finds no validation/held-out statement; supplement not provided, so partly a question |
| TTT outside the stated grids; 3× tuning configurations for CT variants | R1-W1, DA-M2 | App. C, Table 7 | **Partly correct** | The text says TTT follows Akyürek et al. (LR 1e-4), so a separate protocol is plausible, but it conflicts with "sweeps are performed for all methods" |
| ARC masking choice made by its eval score | R1-W3, DA-M2 | §5.3, Table 1, Table 2 | **Verified** | 23.8 (no masking) in Table 1 = Table 2 row; ARC test labels are hidden, public-label eval split: field practice. At 22.5 the main claim holds (CT-KV > ICL 13.3, Prefix 20.5), so MAJOR, not critical |
| TTT+CT-KV gains within noise on MMLU/BBH | R1-W5, R4-W1, DA-M3 | §5.4, Table 1 | **Verified** | +0.5, +0.4 vs stds ≥ 0.38 |
| "Wide margin" on NLP-LR | R4-W1, DA-M3 | §5.4, Table 1 | **Verified** | +2.2/+1.8 (≈ 2 stds); wording overstated |
| Batch-size confound in timing | R1-W4, DA-M5 | App. C | **Verified** | 4 vs 16/8/full; the paper acknowledges the memory difference |
| "Quadratic vs linear training time" is per-step only | R1 ERR-5, DA-M5 | §1, §4.3, App. A | **Overstated** | §4.3 and App. A state per optimization step; only §1 and §5.4 wording is loose, and the direction of the claim is right |
| §5.7 retrieval diagnostic does not test cache incompleteness | R2-W3, DA-M4 | §5.7, Table 4 | **Partly correct** | Table 4 vs Table 1 supports the reading that the cache retains demonstrations; the authors' inference is a hypothesis, but not contradicted |
| Masking may leak pair i via later pairs' K/V | R1-Q2, DA-M6 | §4.3, Fig. 2 | **Partly correct** | Construction of Θ⁻ⁱ is not stated; a legitimate question, not an error |
| GPT-2 ICL ≈ zero-shot undermines the "ICL ability" premise | DA, R3-W2 | Table 1 | **Partly correct** | 35.6 vs 34.9 verified; the inference is one explanation among others |
| Per-task state 21.9–58.5 M parameters (CT-KV) | R3-W1 | Table 10 | **Verified** | |
| ICL attribution inconsistency (Brown vs Radford) | R2-W4 | §1, §2 | **Verified** | Minor |
| BBH k = 10 vs 16 | R1 ERR-4, DA-m1 | §5.1, Fig. 6 caption | **Verified** | Minor |
| Limitations paragraph is thin | R4 | §6 | **Verified** | |

Literature ledger check: R2's missing-comparison points rest on peer-reviewed prior work (T-Few NeurIPS 2022, SPoT ACL 2022, Gist tokens NeurIPS 2023) and are at most Important; none rests on a recent preprint or concurrent work. All five recommended references are marked as found by `verify`.

## Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Decisive points (W1–W3, W5) verified at their locations; one overstatement (complexity wording) |
| R2 (Domain) | 3 | 4 | 1.0 | Sound and mostly verified; the §5.7 point partly correct; novelty verdict reasonable |
| R3 (Perspective) | 4 | 3 | 1.0 | Role-appropriate and positive; deployment points verified (Table 10) but not decisive |
| R4 (Generalist) | 4 | 4 | 1.0 | Wording points verified; calibration reasonable |
| DA | 3 | 4 | 1.0 | DA-M1, M2, M3 verified; DA-M5 partly overstated; DA-M6 unverifiable (raised as a question) |

## DA-CRITICAL Rulings
None raised. The DA's strongest objection (DA-M1) and the selection-protocol issue (DA-M2) were checked against the criteria for CRITICAL: the evidence does not contradict the main claim (the full method beats the baselines on every benchmark), the experiments can test the claim, and for the one explicit selection by score (ARC masking) the field-practice rule and the decision table's second row apply (main claim holds at the other value). No ceiling.

## Final Decision and Justification
Official ratings are 3, 3, 4, 4, 3 (mean 3.40). With the EIC weights the weighted rating is 3.36, so the starting point is **3 (Borderline Reject)**; the composite cross-check is 58.1 (band 3), in agreement, with no ⚠. I keep the starting point. The two accept-leaning reports (R3, R4) rest on the consistent gains over standard baselines, which I verified, but their scores do not account for two verified issues that the reject-leaning reports rest on: the attribution gap (Table 2 "Neither" vs Table 1) and the unstated, unequal tuning protocol. Neither is fatal, and all are fixable without new methodology, but together they leave the central claims ("initialization from demonstrations is the key", "competitive with TTT with half the time", "complementary") only partly supported as written. Weaknesses such as a missing baseline or single-run ARC are typical of accepted papers; the combination with an unstated selection split, parity (not superiority) with the closest relative and an incremental contribution places this just below the bar for ICLR. **My pool position: better than about 54% of submissions** (the top of the typical-rejected band, close to borderline). A revision that states a clean selection protocol, adds the controls of R1-W2, matched-batch timings and the missing baselines would plausibly move it to Borderline Accept. No DA ceiling applies; the decision does not exceed any ceiling. The simulation reflects how a careful panel would likely see this draft, not a prediction.

---

# Editorial Decision

## Paper: Context Tuning for In-Context Optimization
## Submission ID: iclr26-ksxocXsFVh (blinded)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Halvard Teixeira; R1 Methodology Dr. Oksana Brandvold, R2 Domain Prof. Jiahao Verbeek, R3 Perspective Dr. Amara Nwosu-Castellanos, R4 Generalist Dr. Lucas Fenwick-Ibarra, DA Dr. Saoirse Kapoor-Ng

---

## Decision: Borderline Reject (3); ICLR label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" (scale status: secondary; ICLR scale is as reported by secondary sources, verify against the current form)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 58.4
**EIC assessment** (internal): weighted rating 3.36 → starting point 3 · weighted composite 58.1 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3

---

## Score Summary

### Official Scores and EIC Assessment (from `aggregate_scores.py`, with EIC weights)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 56 | 58 | 64 | 62 | 50 | 58.0 | 57.7 | 14 |
| Clarity & Presentation | 66 | 68 | 70 | 72 | 66 | 68.4 | 68.2 | 6 |
| Novelty & Originality | 52 | 50 | 60 | 58 | 50 | 54.0 | 53.7 | 10 |
| Significance & Impact | 52 | 54 | 64 | 62 | 50 | 56.4 | 55.9 | 14 |
| Experimental Validation | 52 | 55 | 60 | 60 | 48 | 55.0 | 54.7 | 12 |
| Reproducibility | 62 | 62 | 62 | 64 | 60 | 62.0 | 62.0 | 4 |
| Ethical Compliance | 62 | 62 | 62 | 62 | 60 | 61.6 | 61.6 | 2 |
| **Composite** | 56.2 | 57.4 | 62.8 | 62.2 | 53.2 | **58.4 (before)** | **58.1 (after)** | |
| Pool position (P%) | 52 | 50 | 66 | 66 | 48 | | EIC: 54 | |

No dimension has a spread > 20; no consistency warnings.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue-weighted composite 58.0 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Context Tuning for In-Context Optimization" to ICLR. The question of whether a context built from demonstrations can be refined cheaply, without touching model weights, is timely and practical.

**Overall Assessment:**
The panel found a clear and simple method with consistent gains over prompt and prefix tuning on four benchmarks and a useful parity-at-lower-cost result against test-time training. The panel was divided on whether the evidence supports the paper's framing, and the majority view was that the protocol and the attribution of the gains need work before the central claims can be accepted as stated.

**Key Strengths Identified by Reviewers:**
1. A simple, well-motivated idea with consistent gains over parameter-matched prompt/prefix baselines (R1, R2, R3, R4).
2. Multi-seed reporting where feasible, informative ablations, a parameter-efficient variant study and candid failure analysis (R1, R4, DA).
3. Practical appeal of weight-free per-task adaptation and complementarity with TTT on NLP-LR (R3, R4).

**Key Concerns Requiring Attention:**
1. The split used to select hyperparameters and design choices is not stated, tuning budgets differ across methods (TTT, baselines), and the ARC masking choice was made on the evaluation tasks (R1, DA; CONSENSUS-2).
2. The paper's own ablation indicates that demonstration initialization alone gives no gain over equal-size random-token prefix tuning; the benefit comes from masking and dropout, which are not tested on the baselines (R1, R4, DA; CONSENSUS-3).
3. Efficiency, "competitive with TTT" and "complementary" claims need matched-batch timings and paired statistics; two of four complementary gains are within noise (R1, R4, DA; CONSENSUS-2/3).
4. Mechanism claims in §5.7 are not tested; closest alternatives (Instruction Prompt Tuning, few-shot PEFT) are not baselines (R2, DA).

**Critical Challenge (Devil's Advocate):** none rated CRITICAL. The strongest objection, that regularization rather than ICL-derived initialization explains the gain, was ruled a MAJOR issue because the full method still outperforms the baselines at every benchmark.

**Decision: Borderline Reject (3)**

The panel's view is that the contribution is real but the evidence is not yet protocol-clean or attributed. To move toward acceptance: state and fix the selection protocol with equal budgets, add the three controls (token dropout on baselines, other-task and shuffled-label initialization), report matched-batch timings and paired statistics, and add at least one non-TTT baseline. These are mostly doable within a revision period.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Halvard Teixeira
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Gain not isolated to demonstration initialization | R1, R4, DA | CONSENSUS-3 |
| TTT parity/complementarity and wording overstated | R1, R4, DA | CONSENSUS-3 |
| §5.7 mechanism unsupported | R2, R4, DA | CONSENSUS-3 |
| Selection split unstated, tuning unequal | R1, DA | CONSENSUS-2 |
| Efficiency confounds | R1, DA | CONSENSUS-2 |
| Minor inconsistencies (k, captions, citations) | R1, R2, R4, DA | CONSENSUS-4 (cosmetic) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall bar | R3, R4 (Borderline Accept) | R1, R2, DA (Borderline Reject) | The accept-leaning reports do not account for the verified attribution and protocol gaps; the reject-leaning reports do not account for the consistent gains. Net: just below the bar. |
| Novelty | R3 (useful reframing, 60) | R1, R2, DA (incremental, 50–52) | Verified: leave-one-out idea is TTT's; the novelty is a recombination. Adopted the lower view, but novelty alone is not decisive at ICLR. |

### Score Spread Discussion
No dimension exceeded the 20-point spread (largest 14 on Technical Rigor and Significance, between DA and R3).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Initialization not isolated | Yes (R1, R4) | n/a | New controls |
| DA-M2 | MAJOR | Selection split, tuning budgets, ARC choice | Yes (R1) | n/a (not CRITICAL: public-label eval split; main claim holds at the other value) | Clarification and a small held-out check |
| DA-M3 | MAJOR | Overclaimed wording | Yes (R4, R1) | n/a | Rewording / paired tests |
| DA-M4 | MAJOR | §5.7 mechanism | Yes (R2) | n/a | Rewording or probe |
| DA-M5 | MAJOR | Efficiency confounds | Yes (R1) | n/a | Re-timing |
| DA-M6 | MAJOR | Masking construction (question) | Yes (R1-Q2) | n/a | Clarification |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No upheld DA-CRITICAL issues. These items the EIC verified as undermining the main claims.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Selection split and tuning budgets unstated/unequal; TTT outside grids | R1-W1, DA-M2 | App. C, Table 7, §5.3 | State the split; select on held-out demonstrations or a disjoint split; give TTT and baselines equal configuration counts (add Token Dropout to baselines); re-run Table 1 | Medium; ~30–50 GPU-h | Partly (statement: yes; reruns: partly) |
| P1-2 | Gain not attributed to initialization | R1-W2, DA-M1, R4-W2 | Table 1 vs Table 2, §5.4, Abstract | Add: baseline + Token Dropout; other-task and shuffled-label initializations; reword the framing if the gain comes from masking/dropout | Medium; ~20 GPU-h | Yes |
| P1-3 | ARC choice on eval tasks and single run | R1-W3, DA-M2 | §5.3, Table 2, Table 1 | Select on ARC train tasks; paired bootstrap/McNemar over 400 tasks | Low–Medium; ~5–10 GPU-h | Yes |
| P1-4 | Efficiency claim confounded | R1-W4, DA-M5 | App. A/C, Table 1, §1 | Matched batch size/checkpointing timings, FLOPs, memory, k sweep; say "per step" | Medium; ~10 GPU-h | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | "Competitive with TTT" and "complementary" without paired statistics | R1-W5, R4-W1, DA-M3 | Paired differences with CIs; narrow wording | Low | Yes |
| S2 | Add non-TTT baselines: Instruction Prompt Tuning recipe, few-shot LoRA without context | R2-W2 | Two baselines on 1–2 benchmarks | Medium; ~10 GPU-h | Partly |
| S3 | §5.7 mechanism claim | R2-W3, DA-M4 | Reword or add a held-out-pair probe | Low–Medium | Yes |
| S4 | Describe the construction of Θ⁻ⁱ (leakage question) | R1-Q2, DA-M6 | Describe; if full-context KV, recompute on C⁻ⁱ and report both | Low–Medium | Yes |
| S5 | Related work: task/function vectors, gist tokens, few-shot PEFT (T-Few), context distillation, In-Context Vectors, SPoT | R2-W1, W4 | Add and discuss (references verified, see R2) | Low | Yes |
| S6 | Model/benchmark pairing | R4-W3 | Two or more model sizes on one benchmark; state GPT-2 size and Llama variants | Medium | Partly |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Deployment cost table (state MB, latency, break-even queries), KV compression test | R3-W1 | Add a cost table |
| N2 | Robustness to noisy labels, demonstration shift; larger models | R3-W2 | One robustness experiment |
| N3 | White-box access and privacy note | R3-W3 | A short paragraph |
| N4 | Typos and inconsistencies: BBH k, Table 1 caption, Table 10 label, Appendix A TTT wording, ICL attribution, Franzen year, MetaICL metric/model parity | R1, R2, R4, DA | Fix |
| N5 | Shorten §4.1/§5.7 | R4-W2 | Edit |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 1–2 weeks including reruns (≈ 65–90 GPU-hours).
- Priority 2: 6 items, roughly 1 week.
- Priority 3: 5 items, 1–2 days.
- **Total estimated revision time**: ≈ 2–3 weeks.
