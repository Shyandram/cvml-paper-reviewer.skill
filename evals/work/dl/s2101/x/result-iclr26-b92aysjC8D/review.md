# Review of "Self-Reflective Generation at Test Time" (SRGen)

Date: 2026-11-10 · Mode: full · Target venue: ICLR · Literature check: strict, cutoff 2025-09-24 · Figures were not available (text extraction only): claims that depend on Figures 2–9 are judged from captions and surrounding text and flagged where it matters. All five reviewer passes and the EIC were performed by one model in one shared context, one after another (no subagents); independence is by role-based separation only. The outcome is a simulation of how a careful panel might see this draft, not a prediction.

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Self-Reflective Generation at Test Time |
| Primary Discipline | Machine learning → LLM reasoning, inference-time (training-free) methods |
| Secondary Discipline(s) | Test-time adaptation / optimization; uncertainty estimation and decoding; test-time scaling |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Entropy-triggered (rolling mean + k·std) detection of uncertain tokens; per-trigger optimization of a transient hidden-state vector δ with a prefix cross-entropy + next-token entropy loss; Avg@k / Cons@k / Pass@k on competition math |
| Target Venue | ICLR (stated by the user); profile key `iclr`. Base rate ≈ 27% accepted at ICLR 2026 |
| Venue-Specific Notes | None. ICLR form: Soundness, Presentation, Contribution (1–4), Rating, Confidence. Scale status: secondary |
| Paper Maturity | Submission-ready (preprint-style template, anonymized, appendix with theory/case study) |
| Ethics-Relevant Content | None (public math benchmarks, open-weight models); an Ethics Statement is present |

**Paper memory** (factual record shared with all reviewers; locations in parentheses)
- Claims: C1 a "new paradigm of proactive, test-time self-reflection" that corrects at uncertain tokens before they are emitted (Abstract; §1; Table 1). C2 dynamic entropy thresholding detects critical tokens (§3.2, Eq. 3; App. F). C3 the hybrid loss "is not a heuristic" but a Lagrangian of a constrained problem (§4.2, Theorem 1; App. B.1). C4 consistent gains in Avg@5 and Cons@5 on 4 models × 4 benchmarks, e.g. +12.0 Pass@1 and +13.3 Cons@5 on AIME2024 for DeepSeek-R1-Distill-Qwen-7B (Abstract; Table 2). C5 "bounded overhead" of about 50% (Abstract; §4.3; §5.3; §6). C6 plug-and-play and composable with SLOT and training-time methods (§5.5; Fig. 4).
- Setup: models Qwen2.5-Math-7B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, Qwen3-32B (§5.1); benchmarks AIME2024, AIME2025, HMMT2025, AMC; MATH500 only in §5.5/§5.6 (§5.1). Max length 4,096 (Qwen2.5-Math-7B) and 32,768 (others); temperature 0.6, top-p 0.95; A800 GPUs; t=3, η=0.01, N=25, k=4, λ=0.05 (§5.1, §5.6). Number of problems per benchmark, number of runs per cell beyond k=5, seeds, chat template and thinking mode of Qwen3-32B: not stated after search. Base vs. +SRGen only; no other method is compared in Table 2 (App. D). Hyperparameter sweep on the first 100 MATH500 problems, Qwen2.5-Math-7B, greedy (§5.6). Efficiency measured on Qwen2.5-Math-7B, AIME2024, greedy (§5.3). Code: "available at [link removed]" (Abstract) but also "will release anonymized code ... after the review process" (Ethics Statement).
- Headline numbers: Abstract +12.0 / +13.3 → Table 2 DeepSeek-R1-Distill-Qwen-7B, AIME2024 (49.3→61.3; 50.0→63.3). §1 Qwen3-32B +6 / +10 (76.7→82.7; 80→90). §5.3 ≈6 activations per task, ≈50% extra time.
- Appendix: Theorem proof and practical guidance (B), Algorithm 1 (B/C), baseline scope (D), prompts (E), entropy statistics (F), critical-token frequencies (G), loss curves (H), two greedy case studies (I). No limitations section.
- Unverifiable: Figures 1–9 (images unavailable); only captions and text read.

**Integrity scan** (`scripts/integrity_scan.py --redact`): no reviewer-directed text or hidden characters found; nothing out of place noticed while reading. The five reviewers read the redacted copy (identical to the original here).

**Literature-check fingerprint** written (title, method/loss names, three distinctive phrases, cutoff 2025-09-24).

### Claimed Contributions (as stated by the authors)
1. C1: a lightweight, proactive test-time framework that reflects before generating at uncertain points.
2. C2: dynamic entropy thresholding and a per-token corrective vector trained with a hybrid loss, justified theoretically (Theorem 1).
3. C4–C6: consistent gains across models/benchmarks, better self-consistency, bounded overhead, composability.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Halvard Ketterling-Osei, senior area chair profile (research university, northern Europe)
- Seniority / Expertise: senior faculty / language-model evaluation, decoding, test-time compute
- Role: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- Style: decides on what the evidence supports; accepts ordinary weaknesses but not an untested central mechanism

### Reviewer 1 (Methodology): Dr. Oluwaseun Adebayo-Reyes (industrial research lab, West Africa/Europe)
- Seniority / Expertise: mid-career industry scientist / evaluation protocols for math-reasoning LLMs, sampling variance, inference-cost measurement
- Review Focus: research design, statistics, comparison fairness, reproducibility
- Style: insists on compute-matched baselines and variance estimates; recomputes every delta

### Reviewer 2 (Domain): Prof. Linnea Hartvigsen-Moreau (large public research university, northern Europe)
- Seniority / Expertise: senior faculty / test-time adaptation and entropy-based objectives; LLM reasoning and critical-token literature
- Review Focus: literature, theoretical framework, domain contribution
- Style: reads related work closely, checks that novelty statements match the cited abstracts

### Reviewer 3 (Perspective): Dr. Kenji Matsuoka-Delgado (applied optimization group, research institute, East Asia/Latin America)
- Seniority / Expertise: postdoc-to-mid-career / online/convex optimization, control, deployment of inference-time adaptation
- Review Focus: cross-disciplinary connections, deployment, assumptions, broader impact
- Style: constructive; the most positive voice on the panel, but names what is missing

### Reviewer 4 (Generalist): Dr. Anneliese Brandvold (vision-and-language group, mid-sized university, North America)
- Seniority / Expertise: mid-career faculty / multimodal and language models, not decoding specifically
- Review Focus: contribution clarity, venue fit, presentation
- Style: the typical PC member; weighs weaknesses against what accepted ICLR papers usually carry

### Devil's Advocate: Dr. Rafael Zuberbühler-Nakamura (statistics and evaluation methodology group, European institute)
- Seniority / Expertise: senior researcher / causal attribution of gains, evaluation methodology, overclaiming
- Review Focus: core-argument challenges, logic, overclaiming
- Style: rigorous and fair; asks whether the evidence shows the stated mechanism

*Personas are fictional. Assumptions: venue = ICLR (stated), type = empirical.*

---

# Phase 1: Independent Reviews

# Peer Review Report (Reviewer 1: Methodology)

## Paper: Self-Reflective Generation at Test Time
## Reviewer: Dr. Oluwaseun Adebayo-Reyes, Methodology (industrial research lab; fictional persona)
## Expertise: evaluation protocols for math-reasoning LLMs; sampling variance; inference-cost measurement
## Date: 2026-11-10

## Summary
SRGen monitors next-token entropy during decoding. When the entropy exceeds a rolling mean plus k standard deviations (§3.2, Eq. 3), it runs a few gradient steps on a vector δ added to the last hidden state, using a loss that mixes the prefix negative log-likelihood (with δ applied to every earlier hidden state) and the entropy of the current next-token distribution (§3.3, Eqs. 4–7), then samples from the corrected logits. Table 2 compares each of four models with and without SRGen on four competition-math benchmarks using Avg@5, Cons@5 and Pass@5. The paper also reports an overhead of about 50% (§5.3), an orthogonality study with SLOT (§5.5) and a hyperparameter sweep (§5.6).

## Protocol sweep (quoted statements, full text incl. appendix)
- Split/selection: "we evaluate on the first 100 instances of the MATH500 benchmark" for the hyperparameter study, Qwen2.5-Math-7B, greedy (§5.6). No statement says how the final values (t=3, η=0.01, N=25, k=4, λ=0.05; §5.1) were chosen. Headline benchmarks (AIME2024/2025, HMMT2025, AMC) are not used for any sweep that I can find. Not stated after search: number of problems per benchmark, seeds ("fixed random seeds" are mentioned in the Reproducibility Statement but not given), chat template, Qwen3-32B thinking mode.

## Strengths
### S1: Consistent direction across models and benchmarks
All 16 Avg@5 cells in Table 2 are non-negative and 14 are above +1.0 point (derived), across two families and sizes 7B–32B. A positive sign in every cell is harder to attribute to noise than any single large gain, even though individual cells are noisy.
### S2: Honest reporting of null cells and a Pass@k check
Table 2 prints "→ 0.0" cells (6 of 16 for Cons@5, 5 of 16 for Pass@5; derived) and §5.2/§5.4 examine whether Pass@k shrinks. The authors did not hide that Cons@5 and Pass@5 often do not move.
### S3: Efficiency is at least measured, with a mechanism-level cost model
§4.3 and §5.3 separate monitoring cost from optimization cost, and report activations per task (~6) and wall-clock. This is more than most test-time methods report.
### S4: Hyperparameters transfer across models
The same (N, k, λ, η, t) are used for all four models (§5.1), which argues against per-model tuning.

## Weaknesses
### W1: The only comparison is "base vs. base + SRGen"; no baseline controls what the gain is attributed to
Table 2 and App. D ("we do not include such comparisons in the main tables and instead measure the SRGen-only effect") contain no other method. The claim is that proactive, uncertainty-triggered *reflection* improves reasoning (Abstract, §1, Table 1), but the experiments cannot distinguish this from simpler explanations that cost similar compute: (a) a sharper distribution (lower temperature or top-p, or other entropy-reducing decoding) for the T=0.6 runs; (b) any small hidden-state perturbation at ~6 positions; (c) the same δ-optimization at random positions or at every position; (d) a static entropy threshold (App. F argues one is inadequate but never tests it); (e) ~1.5× more samples for Cons@k, since SRGen adds ~50% time. The sweep itself is informative: Table 3 gives 70–72 for every cell with iterations 1–9 and η 0.01–0.10 (total step size varying by ~90×; derived), and §5.6 reports substantial gains even at λ=0 and λ=1. Insensitivity to the step size and to which loss terms are on is what one would expect if the optimized objective is not what drives the gain.
- **Suggested Fix**: add (i) random-δ and random-position controls with matched trigger count, (ii) static-threshold and trigger-every-token variants, (iii) the temperature/top-p sweep for the baseline at T∈{0.2,0.4,0.6}, (iv) Cons@k at equal wall-clock (baseline k≈8 vs. SRGen k=5). Cost: Qwen2.5-Math-7B and one 7B R1-distill on AIME24/25, 5 runs each, ≈60–120 A800-hours. Rebuttal-feasible for the 7B models.
### W2: Statistical support is thin for several cells and no variance is reported
AIME and HMMT have 30 problems (count not stated; implied by the 3.3-point granularity of Cons@5 cells such as 6.7→23.3). With 5 samples per problem, the sampling standard deviation of Avg@5 on AIME is up to about 4 points if per-problem success probabilities are near 0.5 (derived: √(30·0.25/5)/30 ≈ 0.041), so the difference between two independent runs has SD ≈ 5–6 points. Gains of 0.2 (Distill-Qwen-7B AMC), 0.6 (Distill-Llama-8B AMC), 2.0 (several cells) are well inside this; even +4.7 (Distill-Llama-8B AIME2024) is within about one SD of the difference. One problem is 3.3 points of Cons@5. The abstract's headline is the largest cell (+12.0; median gain over the 16 cells is +4.0, mean +4.39; derived). No CIs, no repeated runs, no paired test.
- **Suggested Fix**: report 3 independent repetitions of the k=5 protocol (or k=16 samples) with mean ± SD or a paired bootstrap over problems for each cell; report the median gain rather than the best cell in the abstract. ≈100–200 A800-hours for all 16 cells with the 7–8B models; Qwen3-32B can be limited to AIME24/25.
### W3: The overhead claim is under-measured and its cost model omits a prefix-length term
§4.3 states "the overhead of our SRGen scales only with the number of critical interventions", with Overhead ≈ N_act × T × C_bp (Eq. 10). But L_CE (Eq. 6, Algorithm 1 line 10) sums over *all* t−1 prefix positions and every inner step recomputes W(h_i+δ) for all of them, so C_bp grows with the current prefix length (derived from Eq. 6; the vocabulary projection is O(t·d·V) per step). On the 32,768-token budgets used for 12 of the 16 cells in Table 2 (§5.1; App. F quotes ~11,174-step sequences for Distill-Llama-8B) this is not "bounded" by construction. The measurement that supports "≈50%" is Qwen2.5-Math-7B, greedy, AIME2024, capped at 4,096 tokens (§5.1, §5.3); Figure 2 (not available) is described as plateauing as iterations increase, which is itself surprising since time per activation should grow with T. No measurement is given for R1-distill or Qwen3-32B, where Table 2's largest gains are claimed, and Table 1's "Low (bounded)" is unsupported there.
- **Suggested Fix**: report activations per task, mean tokens, wall-clock and peak memory for every model in Table 2 at the T=0.6 setting, and cache/truncate the prefix (e.g., a window) if needed to keep the cost bounded. ≈20 A800-hours.
### W4: Truncation and degenerate-output confounds are not ruled out
Max length is 4,096 for Qwen2.5-Math-7B and 32,768 for the R1 models (§5.1). Entropy minimization and hidden-state perturbation can alter repetition loops, truncation and answer-format compliance, which directly change Avg@5 on a boxed-answer metric (App. E prompt). The case study shows how fragile the baseline is: Example 1's "Original Response" restates a different question ("The sum of the first N positive even numbers is 110.") and Example 2's original response calls for running Python (App. I). Gains for Qwen2.5-Math-7B may therefore reflect format/degeneration repair rather than "reflection".
- **Suggested Fix**: report truncation rate, mean length and format-failure rate with and without SRGen per model; re-evaluate Qwen2.5-Math-7B with its standard chat template and a rule-based extractor. Cost: analysis of existing generations (low).
### W5: Selection protocol and a subset overlap are unclear
The only sweep uses MATH500[:100] with Qwen2.5-Math-7B (§5.6); MATH500 is also reported in §5.5 ("from 63.8% to 70.6%"). The paper never says that the final values were picked on this subset, but also never says how they were chosen. The overlap affects only a secondary result, not the Table 2 benchmarks, so I treat this as a protocol question rather than leakage.
- **Suggested Fix**: state the selection procedure; report §5.5 results on MATH500[100:] or on a different benchmark.

**Minor:** the text in §5.2 says "only DeepSeek-R1-Llama-7B shows a decrease" while Table 2 has no Cons@5 decrease (ERR-1); some Pass@5/Cons@5 values (e.g. 6.0, 13.0, 33.0, 73.0) are not multiples of 1/30 or are truncated (Questions); Fig. 3/4/5 legends should state k and n_runs.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1/E6 | §5.2 Cons@k vs. Table 2 | "only DeepSeek-R1-Llama-7B shows a decrease" | Table 2 shows no Cons@5 decrease in any of the 16 cells; Distill-Llama-8B AIME2024 is 46.7→63.3; the model is 8B in §5.1 | Cross-referenced both locations | High | MINOR | Correct the sentence |
| ERR-2 | E5/E2 | §4.3, Eq. 10 vs. Eq. 6 | "the overhead of our SRGen scales only with the number of critical interventions" | Eq. 6 sums over the whole prefix, so the per-activation cost grows with prefix length; Eq. 10 treats C_bp as constant | Derived from Eqs. 6, 10 and Algorithm 1 line 10 | High (reading), Medium (magnitude) | MAJOR | Include a t-dependent term and measure on long traces |
| ERR-3 | E5 | Abstract, §6 vs. §5.3 | "stabilizing at approximately 50%" | The 50% figure is measured only for Qwen2.5-Math-7B, greedy, 4,096-token cap; extended to all models | Cross-referenced §5.1, §5.3, §6 | High | MAJOR | Measure each model or restrict the claim |

## Claim-to-evidence map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Proactive reflection prevents errors | Abstract, §1, Table 1 | Table 2 (base vs. SRGen only); case study (2 examples, App. I) | Partially: accuracy gains shown, mechanism untested |
| C2 | Dynamic threshold needed | §3.2, App. F | Entropy statistics; k and N ablation (Fig. 5, unavailable) | Partially: no static-threshold or random-trigger control |
| C3 | Hybrid loss is principled (Thm 1) | §4.2, App. B.1 | Proof | Proof correct but only about exact minimizers; algorithm takes 3 steps from δ=0 |
| C4 | Consistent gains | Abstract, §5.2 | Table 2 | Supported in direction; magnitude noisy (W2) |
| C5 | Bounded overhead ≈50% | Abstract, §4.3, §5.3 | Fig. 2 (one model, greedy) | Partially / Unsupported for long-CoT models |
| C6 | Composable with SLOT | §5.5 | Fig. 4 (one model, greedy, MATH500 overlaps §5.6 subset) | Partially |

## Missing References
*(Domain reviewer's job; none added here.)*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Direction is consistent, but attribution controls and variance are missing (W1, W2) |
| Clarity | 3 | Clear method and algorithm; some text/table mismatches |
| Significance | 2 | Useful if the gain survives matched controls |
| Originality | 2 | A reasonable combination; see R2 |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the only comparison is base vs. base+method with no variance and no controls for the central mechanism or compute; these are signals of a typical rejected submission, offset by a consistent sign across 16 cells.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Theorem about exact minimizers does not describe the 3-step algorithm; overhead model omits prefix length (ERR-2); mechanism untested |
| Clarity & Presentation | 68 | Competent | Easy to follow; minor inconsistencies |
| Novelty & Originality | 55 | Competent | Reasonable combination of known pieces |
| Significance & Impact | 56 | Competent | Training-free and simple; value depends on controls |
| Experimental Validation | 44 | Developing | No baselines, no variance, single-model efficiency measurement |
| Reproducibility | 55 | Competent | Hyperparameters and prompts given; seeds, problem counts, template, thinking mode and code not available |
| Ethical Compliance | 70 | Competent | No ethical stakes; statement present |

## Questions for Authors
1. What happens with a random δ of the same norm applied at the same number of random positions? A gain close to SRGen's would lower my score; a clear gap would raise it.
2. What are the per-model mean activations per task, mean tokens, truncation rate and wall-clock at T=0.6 with 32,768 tokens? Overhead ≤ ~50% on R1-distill models would remove W3.
3. How many problems does each benchmark have, and why are some Pass@5/Cons@5 entries (6.0, 13.0, 33.0, 73.0) not multiples of 1/30? (Low-confidence: may be rounding.)
4. The base accuracies of the R1-distill models and Qwen3-32B on AIME2024 (49.3, 48.0, 76.7) look lower than values commonly reported for these models [verify]; was the official chat template/thinking mode used, and how many tokens were truncated?
5. How were t, η, N, k, λ selected, and was any benchmark in Table 2 used in that process?

## Limitations Assessment
**Partially.** There is no limitations section. Please state the 4,096-token cap for the 7B math model, greedy-only efficiency/ablations, one-model composability tests, and the lack of non-math evidence.

## Ethics Review Flag
**No**

## Overall Score
**3**: A simple, plausible method with direction-consistent gains, but no baseline, control or variance supports the attribution to "reflection" or the "bounded" cost claim.

## Confidence
**4**: I recomputed every delta in Table 2 (all agree); the efficiency figure was not visible, so W3 rests on Eq. 6/Eq. 10 and the text.

---

# Peer Review Report (Reviewer 2: Domain)

## Paper: Self-Reflective Generation at Test Time
## Reviewer: Prof. Linnea Hartvigsen-Moreau, Domain (large public research university; fictional persona)
## Expertise: test-time adaptation and entropy objectives; critical tokens in LLM reasoning
## Date: 2026-11-10

## Summary
The paper positions SRGen between post-hoc self-refinement (Self-Refine, Reflexion, TextGrad) and RL-trained self-correction, as a "proactive" token-level test-time method (Table 1, §2, App. A). It reuses SLOT's idea of a transient vector injected into hidden states and the observation that high-entropy tokens are decision points, adds a dynamic threshold for triggering, a prefix-likelihood regularizer, and a theorem relating the loss to a constrained problem.

## Strengths
### S1: Well-motivated gap and clean positioning against SLOT
App. A explains that SLOT applies a sample-level vector over the prompt, whereas SRGen computes a vector per trigger; §5.5 tests the combination. The relation to the nearest hidden-state method is stated, not hidden.
### S2: Sensible use of the critical-token literature
§1 and App. A collect entropy/confidence/mutual-information signals (Wang et al., Fu et al., Qian et al.) and turn them into a decoding-time trigger rather than a training or filtering signal. The reuse is acknowledged.
### S3: The dynamic threshold is motivated with evidence
App. F shows entropy scales that differ by orders of magnitude across models and temperatures (e.g. ≈0.0002 vs. ≈0.3145 final-step entropy at T=0.6), which is a real reason a fixed threshold is awkward.
### S4: A theoretical remark with a correct proof
App. B.1's proof of Theorem 1 is correct, and the λ↔α map (λ=1/(1+α)) checks out.

## Weaknesses
### W1: The "new paradigm" claim is not positioned against entropy-minimization at test time
The paper says "We introduce a new paradigm for the use of critical tokens" (App. A) and "a new paradigm of proactive, test-time self-reflection" (§1). Per the literature check, "The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning" (Agarwal et al., arXiv 2505.15134, May 2025) describes EM-INF, an inference-time logit adjustment that reduces entropy, and reports gains on math tasks; and Tent (ICLR 2021) established entropy minimization as a test-time objective. Neither is cited. Because EM-INF is a recent preprint (about 4 months before the cutoff), this is a "worth discussing" point and does not lower my score, but the framing of LLM-reasoning entropy sharpening as new needs to be differentiated: SRGen's AEM term is the same objective, applied at triggered tokens with a prefix-likelihood regularizer.
- **Suggested Fix**: add a related-work paragraph and, ideally, an entropy-minimization-at-every-token baseline, to show what triggering and the prefix loss add.
### W2: "Reflection" is a metaphor the method does not implement
No part of SRGen inspects, critiques or revisits earlier reasoning; it sharpens the next-token distribution under a regularizer. Table 1's "Proactive" vs. "Reactive" and the "Operating mode" row are conceptual labels, not measured properties. The paper's own results, with Cons@5 rising while Pass@5 is flat in 5 of 16 cells (Table 2), look like distribution sharpening. The framing around self-reflection can mislead readers about what the method does.
- **Suggested Fix**: describe it as uncertainty-triggered test-time logit/hidden-state optimization, and discuss the relation to self-reflection explicitly.
### W3: Theorem 1 is weaker than its framing
§4.2 calls it "a strong theoretical grounding", but the statement (any minimizer of a weighted sum solves the ε-constrained problem with ε=L_CE(δ*), and is Pareto-optimal) is the standard weighted-sum/ε-constraint fact. It says nothing about how to pick λ or ε, and the converse needs convexity, which App. B.1 concedes is not available for L_AEM. Moreover it concerns exact minimizers, whereas Algorithm 1 takes T≈3 gradient steps from δ=0, so the property does not describe the produced δ. The Joint-Descent Lemma's acute-angle assumption is checked only empirically (App. H, Fig. 9, unavailable).
- **Suggested Fix**: present the theorem as an interpretation, not as a justification; or provide a statement about the finite-step iterate.
### W4: Baselines and related approaches named in the paper's own framing are never compared
Self-Refine, Reflexion and TextGrad are positioned as the contrast (Table 1) and App. D declines to compare. Deep think with confidence (Fu et al., 2025) and confidence-weighted voting (Taubenfeld et al., 2025) are cited as consumers of the same token-uncertainty signal and are natural comparators for the Cons@k claim. Only SLOT is tested, in one model and greedy decoding (§5.5).
- **Suggested Fix**: add at least one decoding-level baseline (EM-INF-style logit sharpening or confidence-guided voting) and one outer-loop refinement baseline at matched compute, even on a single model.

**Minor:** citation mismatch for the Qwen2.5-Math model (ERR-4); MATH500 is used without citation.

## Literature-check addendum (strict; cutoff 2025-09-24; arXiv-only search; 8 queries, 2 refused as too long)

**Per-claim novelty** (`related_search.py novelty`, profile in `novelty_profile.json`):
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 proactive token-level hidden-state correction | method | high (script) | Tent, level 2, arxiv.org/abs/2006.10726v3, prior (peer-reviewed), not cited | The Tent-type objective is the same family (entropy minimization at test time) but in a different setting. The closest LLM work is EM-INF (below), only a recent preprint, so it sets no verdict |
| C2 dynamic entropy threshold | method | medium | "Beyond the 80/20 Rule", level 3, arxiv.org/abs/2506.01939v2, prior (peer-reviewed), cited | High-entropy tokens as forking points are known; the rolling mean + k·std rule appears to be the paper's own |
| C3 loss as Lagrangian (Theorem 1) | method | high (script) | Tent, level 2, not cited | No close prior found in 3 results; the underlying fact is textbook, so this is not a novelty gain (W3). Search covers arXiv only |

Paper reading from the script: "no central claim fully covered by prior work". Attribution (closest prior work as a whole): Tent. No text overlap was found (all candidates ≤ 0.16 cosine, 0 shared 8-grams).

**Novelty delta table**
| Claimed contribution | Closest prior work (link) | What that work already does | What is actually new here | Cited and differentiated? |
|---|---|---|---|---|
| Entropy-sharpening at test time for reasoning | Agarwal et al. 2025, arxiv.org/abs/2505.15134v1 (recent preprint; worth discussing) | Per its abstract, EM-INF performs inference-time logit adjustment to reduce entropy and improves math/physics/coding performance | Triggering at entropy spikes, optimizing a hidden-state vector with a prefix loss | No |
| Entropy-based critical tokens | Wang et al. 2025 (80/20 rule), arxiv.org/abs/2506.01939v2 | Shows a minority of high-entropy tokens act as critical forks in CoT, used for RL | Uses them as decoding-time triggers | Yes (cited) |
| Hidden-state vector at test time | SLOT (Hu et al. 2025, arXiv 2505.12392; cited) | Sample-specific vector optimized on the prompt | Per-trigger vector at generation time | Yes |
| Uncertainty-triggered decoding for reasoning | Xie et al., Self-Evaluation Guided Beam Search, NeurIPS 2023, arxiv.org/abs/2305.00633v3 | Step-level guidance to counter error accumulation in multi-step reasoning | Different mechanism (no search or evaluator) | No |

**Baseline scout.** The AIME `scout` query returned only the 80/20 RL paper (no comparable decoding-time numbers) and a speculative-decoding paper (recent preprint); no required baseline is missing on this evidence, and no under-reported baseline can be assessed. The comparison gap (W4) rests on the paper's own cited methods, not on the scout.

**Field snapshot** (from kept results, before the cutoff). By mid-2025 the reasoning-model literature had converged on two things relevant here. First, token-level uncertainty is a recognized signal: high-entropy minority tokens act as forks (Wang et al., 2025), and entropy minimization alone, including inference-time logit adjustment, was reported to improve math reasoning (Agarwal et al., 2025). Second, a family of training-free decoding interventions (layer-contrast and logit-trajectory decoding, e.g. DeLTa, 2025; entropy-guided refinement loops, Aug 2025) compete for the "free" accuracy gain, and test-time scaling by sampling and voting is the default compute-matched alternative. In this setting, a few points on a 30-problem benchmark are weak evidence; what counts as significant is an improvement that survives compute-matched voting and a simple sharpening baseline, ideally with a mechanism shown (not asserted). I used this to score Significance and Novelty as moderate, not to raise the bar above what ICLR accepts.

## Missing References
*Verified with `related_search.py verify` where a link is given; others marked [verify].*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | none | — |
| Important (worth discussing; recent preprint, not required) | Agarwal, Zhang, Yuan, Han, Peng. "The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning", arXiv 2025 (arxiv.org/abs/2505.15134) | Inference-time entropy reduction with reported math gains; the closest LLM-side relative of the AEM term |
| Important | Xie, Kawaguchi, Zhao, Zhao, Kan, He. "Self-Evaluation Guided Beam Search for Reasoning", NeurIPS 2023 (arxiv.org/abs/2305.00633) | Decoding-time handling of error accumulation in multi-step reasoning |
| Helpful | Wang, Shelhamer, Liu, Olshausen, Darrell. "Tent: Fully Test-time Adaptation by Entropy Minimization", ICLR 2021 (arxiv.org/abs/2006.10726) | Origin of the test-time entropy-minimization objective and its collapse failure mode (relevant to λ→1) |
| Helpful | Lightman et al. "Let's Verify Step by Step", ICLR 2024 (arxiv.org/abs/2305.20050) | Source of MATH500, used in §5.5/§5.6 without citation |
| Helpful (concurrent, discuss only) | Li et al. "Spectral Logit Sculpting: Adaptive Low-Rank Logit Transformation for Controlled Text Generation", arXiv Sept 2025 (arxiv.org/abs/2509.25204) | Concurrent lightweight inference-time entropy-based method |
| Helpful | Qwen team (Yang et al.), "Qwen2.5-Math Technical Report" (2024) [verify] | The model used is Qwen2.5-Math-7B but the cited report is Qwen2 |

**Citation check (E7).** The text says "Qwen2.5-Math-7B (Team, 2024)" (§5.1) and the bibliography entry is "Qwen Team. Qwen2 technical report" (ERR-4, Low severity, High confidence; it names a different report than the model). The characterizations of Wang et al. 2025 (entropy), Fu et al. 2025 (confidence) and Qian et al. 2025 (mutual information) match the titles/abstracts I could check (Wang et al. verified via abstract).

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-4 | E7 | §5.1 vs. References | "Qwen2.5-Math-7B (Team, 2024)" | Entry points to "Qwen2 technical report", not to a Qwen2.5-Math report | Cross-referenced text and bibliography | High | MINOR | Cite the correct report |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory is correct but oversold; no matched controls |
| Clarity | 3 | Positioning is explicit, related work is organized |
| Significance | 2 | Useful if differentiated from entropy sharpening |
| Originality | 2 | Combination of SLOT-style vectors, entropy triggers and EM objective |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is a recombination of three known ingredients, the "new paradigm" framing is not differentiated from entropy minimization, and the theory is standard; but no central claim is fully covered by prior work.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Correct but oversold theorem; mismatch between exact-minimizer theory and 3-step practice |
| Clarity & Presentation | 66 | Competent | Positioning is clear; "reflection" language over-reaches |
| Novelty & Originality | 52 | Developing | Incremental combination (SLOT + entropy trigger + EM objective); medium at claim level |
| Significance & Impact | 54 | Developing | Modest, pending comparisons |
| Experimental Validation | 46 | Developing | No competing method at all in Table 2 |
| Reproducibility | 58 | Competent | Hyperparameters and prompts given |
| Ethical Compliance | 70 | Competent | Nothing at stake |

## Questions for Authors
1. How does SRGen differ, empirically, from applying inference-time entropy minimization (as in EM-INF) at every token or at the same triggered tokens without the prefix loss? A comparison that shows an advantage would raise my novelty score.
2. Does Theorem 1 say anything about the δ produced after T=3 steps from δ=0? If not, please reframe it.
3. Why is the Qwen2 report cited for Qwen2.5-Math-7B?

## Limitations Assessment
**Partially.** No limitations section; missing discussion of the relation to entropy-minimization methods and of settings where sharpening hurts (diversity).

## Ethics Review Flag
**No**

## Overall Score
**3**: A reasonable, simple idea, but the novelty framing is stronger than the delta from entropy minimization and SLOT, and there is no comparison to any competing method.

## Confidence
**4**: I verified the key related work through the literature check; EM-INF's details are taken from its abstract only.

---

# Peer Review Report (Reviewer 3: Perspective)

## Paper: Self-Reflective Generation at Test Time
## Reviewer: Dr. Kenji Matsuoka-Delgado, Perspective (applied optimization research institute; fictional persona)
## Expertise: online optimization and control; deployment of inference-time adaptation
## Date: 2026-11-10

## Summary
SRGen can be seen as a tiny model-predictive-style correction: observe a statistic of the process (entropy spike), run a short inner optimization on a low-dimensional control (δ), apply it for one step and discard it. The paper shows it improves accuracy of several open-weight reasoning models on competition math and reports moderate overhead.

## Strengths
### S1: A small, interpretable control in a low-dimensional space
δ is a single d-dimensional vector applied at the final hidden state, discarded after use (§3.3, Algorithm 1 line 15). This keeps the intervention local, does not change weights or the KV cache, and is easy to deploy on top of an existing decoder.
### S2: Wide applicability across training regimes
Table 2 spans a math-specialized base model, two distilled models and an RL-trained model; the same hyperparameters work for all (§5.1). For practitioners, a method that does not need per-model tuning is attractive.
### S3: Honest treatment of a failure mode
§5.6, App. B.2 and App. H discuss entropy collapse for large λ and give practical guidance (small λ, trust region, diagnostics), which will help adopters.
### S4: Good ablation instincts
The study of λ, N and k (Fig. 5, text only) shows that too small a k triggers too often and too large misses critical tokens.

## Weaknesses
### W1: Assumptions about entropy as an error signal are not tested
The method assumes that entropy spikes mark tokens where an error is about to occur and that lowering entropy at that token makes the continuation more likely correct. App. G shows triggers concentrate on function words and discourse connectives ("the", "so", "but", "wait"), which are high-entropy by nature; no evidence links spikes to actual errors, and sharpening at "wait" could suppress the self-verification behavior that long-CoT models use. A simple diagnostic (error rate after triggered vs. non-triggered positions, or whether triggers precede divergences from correct solutions) would test the assumption.
- **Suggested Fix**: correlate trigger positions with first-error positions on a labelled subset; report whether "wait"-type tokens being sharpened changes the rate of self-correction.
### W2: Deployment cost under realistic serving
Per-trigger backprop-style inner loops break batched decoding and fused kernels, and the prefix term (Eq. 6) re-projects the whole prefix. §5.3 reports one batch-free, greedy, single-model measurement. A practitioner would want throughput at batch sizes 1, 8, 32, and memory, since most serving stacks are throughput-bound.
- **Suggested Fix**: add a throughput/memory table by batch size and context length for one R1-distill model.
### W3: Scope of the evidence
All evidence is on competition mathematics where answers are exact (§5.1). The broader claim in the Abstract ("reliable LLM reasoning") and the Ethics Statement's caution about open-domain use are not backed by any non-math evaluation, such as code or science QA. Entropy-based triggers may behave differently where uncertainty is aleatoric (open-ended text).
- **Suggested Fix**: add one code or science benchmark, or state the scope explicitly.
### W4: Sharpening reduces diversity at large k
Fig. 3 (text) says Pass@k "gradually converges" to the base. Practitioners using best-of-n or RL rollouts want diversity; the paper would be more useful with an analysis of diversity (e.g., distinct answers per problem) beyond Pass@k.
- **Suggested Fix**: report answer-diversity statistics at k=16–64 for one model.

**Minor:** the Ethics Statement mentions "recommending safety filters and uncertainty calibration" without detail; the paper does not use any LLM-generated labels.

## Missing References (optional)
Control-theoretic analogues (model-predictive control and receding-horizon optimization) and online test-time adaptation under distribution shift are natural bridges; I name the lines of work rather than specific papers.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound mechanics; evaluation gaps noted by others |
| Clarity | 3 | Clear |
| Significance | 3 | Practical, training-free plug-in with plausible uptake |
| Originality | 3 | Fresh combination with a clear design |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a simple, training-free, broadly applicable method whose gains are consistent in direction across four models, though the supporting controls are thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound mechanics; some claims untested |
| Clarity & Presentation | 70 | Competent | Easy to follow |
| Novelty & Originality | 62 | Competent | New combination in a timely setting |
| Significance & Impact | 66 | Competent | Plug-in value for reasoning models |
| Experimental Validation | 58 | Competent | Multi-model, but no baselines |
| Reproducibility | 62 | Competent | Details given; code promised |
| Ethical Compliance | 72 | Competent | Statement present; nothing at stake |

## Questions for Authors
1. Do triggered positions precede actual errors? A positive correlation would raise my score; none would lower it.
2. What is throughput at batch 8–32 with SRGen on?
3. Does SRGen help on a non-math reasoning task?

## Limitations Assessment
**Partially.** Add a limitations paragraph (scope, serving cost, diversity).

## Ethics Review Flag
**No**

## Overall Score
**4**: A practical, plausible plug-in with consistent gains; the weaknesses are of the kind many accepted papers carry, though I would like stronger controls.

## Confidence
**3**: I am an outsider to LLM decoding; I trust the other reviewers on the math-benchmark protocol.

---

# Peer Review Report (Reviewer 4: Generalist)

## Paper: Self-Reflective Generation at Test Time
## Reviewer: Dr. Anneliese Brandvold, Generalist (university vision-and-language group; fictional persona)
## Expertise: language and multimodal models (not decoding specifically)
## Date: 2026-11-10

## Summary
The paper proposes SRGen: during decoding, detect unusually high next-token entropy using a rolling window, and then briefly optimize a vector added to the hidden state so that the next-token distribution becomes more confident while still explaining the prefix. On four math benchmarks and four models, accuracy of single samples and of 5-sample majority voting mostly improves, at about 50% extra time in one measurement.

**The contribution in one paragraph:** a training-free, plug-in, entropy-triggered test-time correction for reasoning LLMs, with consistent small-to-large accuracy gains and a theoretical interpretation of its loss. The community would gain a cheap trick worth trying if the gain holds against simple alternatives; it would lose little if the paper were rejected, since the idea is easy to re-derive.

## Venue Criteria Checklist (ICLR, from `references/venue_profiles.md`)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness: claims supported by evidence | Partly | Table 2 supports the accuracy gain; the "reflection/proactive" mechanism and "bounded overhead" are not tested (§5.3, §5.6) |
| Presentation | Met | Clear structure, Table 1 and Algorithm 1; minor text/table slips (§5.2) |
| Contribution: significant and new | Partly | Recombination of SLOT-style vectors, entropy triggers and entropy minimization; modest delta |
| Evaluation breadth | Partly | 4 models × 4 math benchmarks; no non-math, no competing method (App. D) |
| Reproducibility | Partly | Prompts and hyperparameters given; code only promised |
| Ethics / limitations | Partly | Ethics statement present; no limitations section |

## Strengths
### S1: A clear, readable method with a precise algorithm
§3 and Algorithm 1 let a non-specialist follow the loop: monitor, trigger, optimize δ, sample. Figure 1's caption states the two stages.
### S2: Broad model coverage for a training-free method
Table 2 covers two families and 7B–32B, including a distilled and an RL-trained model (§5.1). That breadth is more than typical for an inference-time paper.
### S3: Useful ablations and appendices
§5.6 and App. F–H give entropy statistics, a loss-curve study and a critical-token frequency list that make the method easier to understand and to adopt.
### S4: Timely problem
Making long chain-of-thought more reliable is of wide interest to the ICLR audience (§1).

## Weaknesses
### W1: The main table has no competitor, so the size of the contribution cannot be judged
Table 2 only compares base vs. +SRGen. App. D justifies this by prompt-design difficulty for post-hoc refinement, which is fair for Self-Refine-style methods but does not explain why no decoding-level alternative (a different temperature, EM-style logit sharpening, confidence-guided voting) or compute-matched voting is included. A reader cannot tell if +4.4 Avg@5 on average (derived) is a lot for ~50% more time.
- **Suggested Fix**: add a compute-matched Cons@k comparison and at least one decoding-level baseline on two models.
### W2: Claims are stated more strongly than the evidence
"Consistently strengthen" and "reducing the probability of errors at highly uncertain points" (Abstract) rest on Avg@5/Cons@5 gains; 6 of 16 Cons@5 cells and 5 of 16 Pass@5 cells show no change (Table 2), and the "reflection" framing is not tested (see R2-W2, R1-W1). §1 itself softens this to "consistent gains in most settings".
- **Suggested Fix**: tone down the framing to what is measured; add a limitations paragraph.
### W3: Text/table slips and unclear reporting
§5.2 says a Cons@5 decrease occurs for "DeepSeek-R1-Llama-7B" while Table 2 shows none (and the model is 8B); Pass@5/Cons@5 entries such as 6.0, 13.0, 33.0 do not match the 30-problem granularity; the number of problems per benchmark is not given; the Abstract says code "is available" while the Ethics Statement says it will be released after review.
- **Suggested Fix**: fix the text, state n per benchmark, and make the code statement consistent.

**Minor:** typos ("Many prior works tackles"), mixed use of "epochs" and "iterations" for the inner steps (§5.1 vs. Table 3), "Cons@k"/"Avg@k" defined in §5.1 but Pass@k's estimator (unbiased vs. empirical) is not stated.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains shown; attribution and variance missing |
| Clarity | 3 | Readable, with slips |
| Significance | 3 | Plausible practical value |
| Originality | 2 | Incremental recombination |

## Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: I place it just below the median of accepted-vs-rejected because the only comparison is against itself; a typical accepted ICLR method paper compares to at least one alternative.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound mechanics, untested mechanism |
| Clarity & Presentation | 70 | Competent | Clear; minor slips |
| Novelty & Originality | 56 | Competent | Incremental |
| Significance & Impact | 58 | Competent | Useful if robust |
| Experimental Validation | 50 | Developing | No competitor, no variance |
| Reproducibility | 58 | Competent | Details given; code promised |
| Ethical Compliance | 70 | Competent | No stakes; statement present |

## Questions for Authors
1. How does SRGen compare with plain majority voting over 7–8 samples at equal wall-clock? A win would raise my score; a loss would lower it.
2. What does a lower baseline temperature do to Avg@5/Cons@5?
3. Can you add a Limitations paragraph?

## Limitations Assessment
**No.** There is no dedicated limitations section.

## Ethics Review Flag
**No**

## Overall Score
**3**: A clear and useful idea with consistent gains, but a single self-comparison and unmeasured mechanism put it just below what ICLR typically accepts.

## Confidence
**4**: I read the whole paper and appendix; I did not re-derive the theorem.

---

# Devil's Advocate Report

## Paper: Self-Reflective Generation at Test Time
## Reviewer: Dr. Rafael Zuberbühler-Nakamura, statistics and evaluation methodology group (European institute; fictional persona)

## Steelman
SRGen is a cheap, training-free intervention that is applied only when the model's own entropy spikes, and across four models and four hard benchmarks it improves single-sample accuracy in every one of 16 cells, with larger gains in majority voting and no sign of reduced Pass@5. Its hyperparameters are shared across models and its overhead is a moderate ~50%.

## Core Argument Chain
1. LLM errors cascade, and tokens with high entropy are decision points (§1, §3.2).
2. Lowering entropy at those points, regularized by the prefix likelihood, "reflects" and makes the next token more trustworthy (§3.3, §4.2).
3. Applying this at a few triggered tokens improves accuracy across models (Table 2) without hurting exploration (§5.4) and at bounded cost (§5.3).
4. Therefore SRGen is a proactive, plug-and-play form of self-reflection that improves reliability of reasoning.

## Strongest Counter-Argument
The evidence supports "adding this procedure raises Avg@5 on these benchmarks, probably", but not "because it reflects" and not "at bounded cost". Three observations from the paper itself are better explained by a generic sharpening or perturbation effect. First, in §5.6 the Table 3 results sit at ≈71 for every learning rate (0.01–0.10) and iteration count (1–9), a roughly 90-fold range in total step size, and the text reports substantial gains even at λ=0 (no entropy term) and λ=1 (no prefix term). An effect that survives dropping either half of the objective and a 90× change in optimization strength is not obviously an effect of optimizing that objective. Second, Cons@5 rises while Pass@5 is flat or equal in 5 of 16 cells (for instance Qwen2.5-Math-7B AIME2024: Avg@5 14.6→22.0, Pass@5 40.0→40.0), which is the signature of concentration of probability mass on already-reachable answers, exactly what lower temperature or entropy-minimization decoding is known to do; no baseline lowers the temperature, and the greedy results (Table 3, Fig. 4) are measured only on a model whose baseline output in App. I Example 1 is a different, unrelated question, which suggests format fragility that any perturbation could repair. Third, the cost claim is "bounded" only because it was measured on one 4,096-token greedy setting; Eq. 6 makes the per-activation cost grow with the prefix, and the R1-distill and Qwen3 models with the largest claimed gains run up to 32,768 tokens. A paper that titles itself "reflection" and claims a new paradigm must show that triggering at uncertain positions, the prefix loss, and the entropy term each matter. The authors need random-position, random-δ, static-threshold, temperature and compute-matched-voting controls in their response.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core accuracy claim is supported in direction by Table 2 (16 of 16 non-negative Avg@5 cells) and is only narrowed, not contradicted, by the issues below; no test-set selection of the headline numbers is stated (protocol sweep found a hyperparameter sweep only on MATH500[:100], §5.6, which is not a Table 2 benchmark).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Alternative explanations | §5.6, Table 3, Fig. 5 text, Table 2 | Gains are insensitive to step size and to dropping either loss term; Pass@5 flat in 5/16 cells; consistent with generic sharpening or perturbation; the central "reflection" mechanism is untested (evidence supports a weaker claim: improvement from an uncertain-position intervention) | Random-δ / random-position / static-threshold / trigger-every-token / temperature controls |
| DA-M2 | Evidence | Table 2, Abstract | Headline +12.0/+13.3 is the best cell; median +4.0; run-to-run SD ≈ 4 points on AIME (derived); no repeated runs | Report repeats, CIs, median gains |
| DA-M3 | Scope/Evidence | §4.3, Eq. 6, Eq. 10, §5.3, Table 1 | "Bounded overhead" is measured for one model/greedy/4,096 tokens; cost model omits prefix term | Measure all models at 32,768 tokens; add a prefix-length term |
| DA-M4 | Fairness | Table 2, App. D | No compute-matched comparison (≈1.5× samples), no decoding-level or confidence-voting baseline; App. D explicitly declines comparisons | Add Cons@k at equal wall-clock; one decoding baseline |
| DA-M5 | Logic | §4.2, Theorem 1, App. B.1, Alg. 1 | Theorem concerns exact minimizers; method uses 3 steps from δ=0; "strong theoretical grounding" overclaims; converse needs convexity not available | Reframe as interpretation or prove a finite-step statement |
| DA-M6 | Overclaiming | Abstract, §1, App. A | "a new paradigm" with no differentiation from test-time entropy minimization (Tent; EM-INF recent preprint) and no mechanism evidence for "reflection" | Narrow the framing; add related work |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §5.2 vs. Table 2 | "only DeepSeek-R1-Llama-7B shows a decrease" but no Cons@5 decrease exists; model is 8B |
| DA-m2 | Reporting | Table 2 | Pass@5/Cons@5 values (6.0, 13.0, 33.0, 73.0) inconsistent with 30-problem granularity (Question) |
| DA-m3 | Selection | App. I | Two case studies at the first divergence under greedy; selection procedure not stated |
| DA-m4 | Citation | §5.1 | Qwen2.5-Math-7B cited as Qwen2 report |
| DA-m5 | Consistency | Abstract vs. Ethics Statement | Code "is available" vs. "will release ... after the review process" |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Abstract: Pass@1 gain, Distill-Qwen-7B AIME2024 | +12.0 | 61.3 − 49.3 = 12.0 | Yes |
| Abstract: Cons@5 gain, same cell | +13.3 | 63.3 − 50.0 = 13.3 | Yes |
| §1: Qwen3-32B Cons@5, 80→90 | +10 | 90.0 − 80.0 = 10.0 | Yes |
| All 16×3 deltas in Table 2 | as printed | recomputed from the Base and SRGen columns | Yes (all agree) |
| Mean Avg@5 gain over 16 cells | not stated | 70.3 / 16 = 4.39 (median 4.0) | derived |
| Mean Cons@5 gain over 16 cells | not stated | 93.5 / 16 = 5.84 | derived |
| §5.2 "Pass@k ... higher in most" | "comparable ... in some cases and higher in most" | 11 higher, 5 equal, 0 lower of 16 | Yes (consistent) |
| §5.2 "only DeepSeek-R1-Llama-7B shows a decrease" | decrease | Cons@5: 46.7→63.3 for Distill-Llama-8B; no decrease anywhere | **No** |
| §5.3 overhead | ≈50% | not recomputable (Fig. 2 unavailable) | unverifiable |

## Ignored Alternative Explanations
- Distribution sharpening: lower temperature / top-p or EM-style logit adjustment would raise Avg@5 and Cons@5 without raising Pass@5.
- A generic hidden-state perturbation at a handful of positions changes greedy trajectories and may repair degenerate baselines (App. I Example 1).
- Reduced repetition loops or truncation under 32,768-token caps (§5.1) changing boxed-answer extraction.
- A model-specific effect: Qwen2.5-Math-7B (4,096-token cap; baseline format fragility) contributes the largest Cons@5 gains.
- Prompt sensitivity: a single system prompt per benchmark (App. E).

## Missing Stakeholder Perspectives
Practitioners running batched serving (the inner loop breaks batching, see R3-W2), and researchers using diverse sampling for RL rollouts (sharpening reduces diversity at large k).

## Observations (Non-Defects)
- The direction is consistent in all 16 Avg@5 cells, and the same hyperparameters are used across models, which argues against per-model tuning.
- The case-study mathematics (Example 2: d = 35/64) is correct, and the Theorem 1 proof is correct as stated.
- The authors do not hide null cells and they separate Avg@5, Cons@5 and Pass@5.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Mechanism untested; theorem overreach; cost model omits prefix |
| Clarity & Presentation | 66 | Clear; framing over-reaches |
| Novelty & Originality | 52 | Recombination; not differentiated from EM |
| Significance & Impact | 52 | Depends on controls |
| Experimental Validation | 40 | No baselines or variance; single-setting efficiency |
| Reproducibility | 55 | Hyperparameters given; seeds, n, template, code unavailable |
| Ethical Compliance | 68 | Nothing at stake |

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central mechanism and the cost claim are asserted, not tested.

## Overall: 3 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W5 (selection protocol) | rewritten | Paper states a sweep on MATH500[:100] (§5.6) but not the selection rule; reframed as a protocol question, not leakage |
| R1 | Minor line (§5.2 text vs. Table 2) | moved to Minor | Cosmetic; kept as ERR-1 |
| R2 | W1 (no EM citation) | rewritten | Based on a recent preprint (label: recent preprint); stays "worth discussing", not a required comparison |
| R2 | W2 ("reflection" is a metaphor) | kept | Consistent with Table 1 and §3 |
| R3 | "No discussion of broader impact" (draft) | dropped | Paper has an Ethics Statement; replaced by a Minor remark |
| R3 | W4 (diversity) | rewritten | Paper reports Pass@k convergence in §5.4; reframed to ask for diversity statistics |
| R4 | W1 (no competitor) | rewritten | App. D explains why post-hoc refinement is omitted; sharpened to decoding-level and compute-matched baselines |
| DA | M1 ("no trigger ablation") | rewritten | The paper has k and N sweeps (§5.6); the issue is missing random/static-trigger controls |
| DA | M4 vs. R1-W1, R4-W1 | merged in Phase 2 | Same underlying issue |

Scores were not changed.

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer package (Part A)

**Master issue list**
| Issue | Sources | Class | Hinge? |
|-------|---------|-------|--------|
| I1 No competing baseline / compute-matched or sharpening controls; mechanism untested | R1-W1, R2-W4, R4-W1, DA-M1, DA-M4 | CONSENSUS-4 | Yes |
| I2 Variance / noise; headline is best cell | R1-W2, DA-M2, R4-W2 | CONSENSUS-3 | Yes |
| I3 Overhead measured in one setting; cost model omits prefix term | R1-W3 (ERR-2, ERR-3), DA-M3, R3-W2 | CONSENSUS-3 | Yes |
| I4 Theorem 1 oversold; exact-minimizer vs. 3 steps | R2-W3, DA-M5, R1 claim map | CONSENSUS-3 | No |
| I5 "New paradigm"/reflection framing; EM and Tent not discussed | R2-W1, R2-W2, DA-M6 | CONSENSUS-2 | No |
| I6 Entropy-as-error-signal assumption; sharpening "wait"-type tokens | R3-W1 | SOLO | No |
| I7 Truncation / degenerate-output confound | R1-W4, DA alt. explanations | CONSENSUS-2 | Partly |
| I8 Scope: math only; limitations section absent | R3-W3, R4 limitations, R1 limitations | CONSENSUS-3 | No |
| I9 Selection protocol / MATH500 overlap | R1-W5 | SOLO | No |
| I10 Text/table and citation slips | R1 ERR-1, R2 ERR-4, R4-W3, DA-m1..m5 | CONSENSUS-3 | No |
| SPLIT | R3 (Overall 4) vs. R1, R2, R4, DA (Overall 3) on whether the gains justify acceptance despite thin controls | SPLIT | Yes |

**DA-CRITICAL:** none raised.
**Integrity-scan findings:** none.
**Official output (before EIC weights):** official mean Overall 3.20, official composite 56.8, ICLR composite 56.3; no warnings. The scripted run is in `before.json`.

## EIC Meta-Review (Dr. Halvard Ketterling-Osei)

### The Case For and Against
- **For acceptance:** A simple, training-free, plug-in method gives non-negative Avg@5 changes in all 16 model-benchmark cells, with the same hyperparameters across four models and two families, and it is described clearly with an algorithm, theory remark and appendices. If the gains survive the controls requested below, the method would be useful to the reasoning-model community.
- **Against acceptance:** Table 2 contains no comparator, no variance and no compute-matched or sharpening control, so neither the "reflection" mechanism nor "bounded overhead" is established. The insensitivity to step size and loss composition in §5.6 points to a possibly generic effect, the cost model omits a prefix term that matters at 32k tokens, and the novelty framing ignores entropy-minimization-based test-time methods.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 2 has no competitor; only base vs. +SRGen | R1-W1, R2-W4, R4-W1, DA-M4 | Table 2; App. D | Verified | App. D: "we do not include such comparisons in the main tables"; SLOT is only in Fig. 4 (one model, greedy) |
| Table 3 is flat at ≈71 over lr 0.01–0.10 and iterations 1–9 | R1-W1, DA-M1 | §5.6, Table 3 | Verified | Values 70–72 for all 15 cells with iterations ≥ 1 (baseline 64.0); n=100 so ±1 is one problem |
| Gains "even at the extremes" λ=0 and λ=1 | R1-W1, DA-M1 | §5.6 text (Fig. 5 unavailable) | Verified (text) | Text says "SRGen yields substantial gains over the baseline"; the figure could not be inspected |
| Pass@5 equal in 5 of 16 cells; Cons@5 equal in 6 | R1-S2, DA | Table 2 | Verified | Recounted; none decreases |
| Gains inside noise for several cells; headline is the best cell | R1-W2, DA-M2 | Table 2, Abstract | Partly correct | Deltas verified; noise SD ≈ 4 is derived under a stated assumption and the number of problems is not printed; the direction (16/16) is robust, magnitudes are not |
| Eq. 6 sums over the whole prefix, so cost grows with t; Eq. 10 omits it | R1 ERR-2, DA-M3 | §4.3, Eq. 6, Eq. 10, Alg. 1 line 10 | Verified | Alg. 1 line 10 sums j=0..t−2; Eq. 10 has only N_act·T·C_bp. The paper may intend cached h_i, but the projection W(h_i+δ) still depends on δ and must be recomputed per step |
| "Bounded overhead ≈50%" measured only for Qwen2.5-Math-7B, greedy, 4,096 tokens | R1 ERR-3, DA-M3 | §5.1, §5.3, §6 | Verified | Figure 2 unavailable; the text matches the claim |
| §5.2 "decrease" vs. Table 2 | R1 ERR-1, R4-W3, DA-m1 | §5.2, Table 2 | Verified | Table has no Cons@5 decrease; also "Llama-7B" vs. 8B |
| Theorem 1 is the standard weighted-sum/ε-constraint equivalence; converse needs convexity | R2-W3, DA-M5 | §4.2, App. B.1 | Verified | Proof is correct; footnote 1 in App. B.1 concedes no convexity; algorithm takes T≈3 steps |
| EM-INF is uncited prior work | R2-W1, DA-M6 | App. A; literature check | Partly correct | Per the abstract, it is a recent preprint (2025-05-21); "worth discussing", not a required comparison, and it does not lower any score |
| Qwen2.5-Math-7B cited as Qwen2 report | R2 ERR-4 | §5.1; References | Verified | Cosmetic |
| Code "is available" vs. "will release" | R4-W3, DA-m5 | Abstract; Ethics Statement | Verified | Minor consistency |
| Case-study Example 1's original output restates another problem | R1-W4, DA | App. I | Verified | Quote: "The sum of the first N positive even numbers is 110." Example selection is not stated |
| Trigger tokens are mostly function words and connectives | R3-W1 | App. G | Verified (text) | Figure 7 unavailable; the text lists "the, so, but … wait" |

No reviewer made an Incorrect claim. R3-W1's inference that sharpening "wait" could suppress self-verification is a hypothesis (not an error claim) and is treated as a question.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every delta recomputed; prefix-cost and Table 3 observations verified against Eq. 6, Alg. 1 and §5.6; ERR-1/2/3 hold (one tempered as Medium confidence on magnitude) |
| R2 (Domain) | 3 | 4 | 1.0 | Sound and correctly labelled the EM paper as a recent preprint; theorem critique verified; no verification gaps |
| R3 (Perspective) | 4 | 3 | 1.0 | Positive role, calibrated at the borderline; points are expansion suggestions, none incorrect, few bear on the decision |
| R4 (Generalist) | 3 | 4 | 1.0 | Typical sound review; venue checklist and slips verified |
| DA | 3 | 4 | 1.0 | Strongest counter-argument largely verified (Table 3, Table 2 pattern) but partly inferential; rightly no CRITICAL |

### DA-CRITICAL Rulings
No CRITICAL issue was raised, so there is nothing to rule on. For completeness: the AC test on the DA's strongest counter-argument (mechanism untested) gives "No, not fatal on its own": Table 2's direction supports a narrower claim; the fix is controls and a reframing, not a different paper. No upheld issue; ceiling: none.

### Final Decision and Justification
The EIC-weighted rating is 3.16, so the starting point is 3 (Borderline Reject); the composite cross-check (56.4, band 3) agrees, and the official mean is 3.20. I keep 3. The deciding evidence is verified and specific: Table 2 has no comparator; §5.6/Table 3 show an effect that does not depend on step size or on which loss term is on; the cost claim rests on one 4,096-token greedy measurement while Eq. 6/Algorithm 1 line 10 make the per-activation cost prefix-dependent; and the headline cell is the best of 16 with an estimated noise SD of several points. None of these is fatal. A typical accepted ICLR paper carries a missing baseline or single-run results, and I weigh the consistent direction across 16 cells, the clear writing, and the honest null cells in the paper's favor, which is why this is not a 2. But a typical accepted paper also supports its central claim with at least one competing method or control, and here the "reflection/proactive" claim is only asserted. My pool position for this draft is **better than about 50% of ICLR submissions** (deciding evidence: consistent direction across 16 cells versus the absence of any control, variance or compute-matched comparison). Reviewer pool positions span 40–66 (spread 26, under the 30-point disagreement threshold; R3's 66 rests on plausibility of uptake, not on verified controls). The decision does not exceed any ceiling (none applies). EM-INF and Tent were treated as "worth discussing" only and did not influence the decision.

*ICLR label (secondary scale status): rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) for Overall 3, Soundness 2, Presentation 3, Contribution 2.*

---

# Editorial Decision

## Paper: Self-Reflective Generation at Test Time
## Submission ID: not provided (anonymized)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Dr. Halvard Ketterling-Osei; R1 Methodology Dr. Oluwaseun Adebayo-Reyes; R2 Domain Prof. Linnea Hartvigsen-Moreau; R3 Perspective Dr. Kenji Matsuoka-Delgado; R4 Generalist Dr. Anneliese Brandvold; DA Dr. Rafael Zuberbühler-Nakamura

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean 3.20 · official composite 56.8
**EIC assessment** (internal): weighted rating 3.16 → starting point 3 · weighted composite 56.4 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR venue label** (scale status: secondary): rating "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"; Soundness 2, Presentation 3, Contribution 2.

## Score Summary

### Official Scores and EIC Assessment

#### Reviewer weights (EIC, internal)
| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 50 | 54 | 62 | 56 | 48 | 54.0 | 53.5 | 14 |
| Clarity & Presentation | 68 | 66 | 70 | 70 | 66 | 68.0 | 67.9 | 4 |
| Novelty & Originality | 55 | 52 | 62 | 56 | 52 | 55.4 | 55.2 | 10 |
| Significance & Impact | 56 | 54 | 66 | 58 | 52 | 57.2 | 56.8 | 14 |
| Experimental Validation | 44 | 46 | 58 | 50 | 40 | 47.6 | 47.1 | 18 |
| Reproducibility | 55 | 58 | 62 | 58 | 55 | 57.6 | 57.3 | 7 |
| Ethical Compliance | 70 | 70 | 72 | 70 | 68 | 70.0 | 69.9 | 4 |
| **Composite** | 54.8 | 55.3 | 63.6 | 58.1 | 52.1 | **56.8 (before)** | **56.4 (after)** | |
| Pool position (P%) | 42 | 48 | 66 | 54 | 40 | | | |

No dimension spread exceeds 20 points; no consistency warnings.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Self-Reflective Generation at Test Time" to ICLR. The paper addresses the reliability of long chain-of-thought decoding with a training-free intervention, which is a timely and practically attractive goal.

**Overall Assessment:**
The panel found the method clear and the direction of the gains consistent: Avg@5 does not decrease in any of the 16 model-benchmark cells, and the same hyperparameters are used across four models. The panel was not persuaded that the evidence isolates why it works, or that the cost stays bounded for long-CoT models, because the main table has no comparator, no variance and no compute-matched control.

**Key Strengths Identified by Reviewers:**
1. A clear, simple, plug-in method with an explicit algorithm and appendix (R1, R3, R4).
2. Consistent direction across models and families, with honest null cells and a Pass@k check (R1, R3, DA).
3. A useful practical analysis of λ, entropy collapse and critical-token frequencies (R3, R4, R2).

**Key Concerns Requiring Attention:**
1. No competing baselines or controls (random δ/positions, static threshold, lower temperature, compute-matched voting); results are also consistent with generic sharpening (CONSENSUS-4: R1, R2, R4, DA).
2. No variance; the headline +12.0/+13.3 is the best of 16 cells, median +4.0 (CONSENSUS-3: R1, R4, DA).
3. "Bounded overhead" is measured only for Qwen2.5-Math-7B, greedy, 4,096 tokens, and the cost model omits the prefix-length term in Eq. 6 (CONSENSUS-3: R1, R3, DA).
4. Theorem 1 and the "new paradigm / reflection" framing overreach; entropy minimization at test time is not discussed (CONSENSUS-2/3: R2, DA).

**Decision: Borderline Reject (3)**

The idea is plausible and the writing is clear, but at this stage the central mechanism and the cost claim are asserted more than shown. The panel's view of the Priority 1 items below is that they are feasible to address with existing infrastructure; if the controls show a gap from random/static/temperature baselines and an equal-compute advantage, the case would change materially. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Halvard Ketterling-Osei
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No comparator / controls for the mechanism | R1, R2, R4, DA | CONSENSUS-4 |
| Variance, noise and best-cell headline | R1, R4, DA | CONSENSUS-3 |
| Overhead measured in one setting; prefix cost | R1, R3, DA | CONSENSUS-3 |
| Theorem 1 oversold | R2, DA, R1 (claim map) | CONSENSUS-3 |
| No limitations section / scope | R1, R3, R4 | CONSENSUS-3 |
| Slips (text vs. table, citation, code statement) | R1, R2, R4, DA | CONSENSUS-4 (minor) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Do the gains justify acceptance despite thin controls? | R3 (4) | R1, R2, R4, DA (3) | The EIC verified that the controls are absent and Table 3 is flat across a 90× step range; plausibility of uptake does not substitute for them. Kept at 3 |

### Score Spread Discussion
No dimension spread exceeds 20 points (largest: Experimental Validation, 18, R3 58 vs. DA 40). The EIC adopts the lower range because the missing baseline/variance is verified in Table 2 and App. D.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Gains consistent with generic sharpening/perturbation | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Best-cell headline, no variance | Yes (R1-W2, R4-W2) | n/a | n/a |
| DA-M3 | MAJOR | Overhead measured in one setting | Yes (R1-W3, R3-W2) | n/a | n/a |
| DA-M4 | MAJOR | No compute-matched comparison | Yes (R1, R4, R2) | n/a | n/a |
| DA-M5 | MAJOR | Theorem vs. 3-step algorithm | Yes (R2-W3) | n/a | n/a |
| DA-M6 | MAJOR | "New paradigm" framing | Yes (R2-W1) | n/a | n/a |
| (CRITICAL) | — | None raised | — | — | — |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No upheld DA-CRITICAL issue; these are issues the EIC verified as bearing on the main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Mechanism untested; no controls (random δ, random positions, static threshold, trigger-every-token, EM-style logit sharpening, baseline temperature sweep) | R1-W1, R2-W4, R4-W1, DA-M1, DA-M6 | §5.6, Table 2, App. D | Add the controls on Qwen2.5-Math-7B and one R1-distill model, AIME24/25, 5 runs | Medium; ≈60–120 A800-h | Yes (7–8B) |
| P1-2 | Compute-matched comparison for Cons@k | R1-W1, R4-W1, DA-M4 | Table 2, Fig. 3 | Baseline Cons@k at equal wall-clock (≈ k=8 vs. SRGen k=5), plus one outer-loop or decoding baseline | Medium; ≈40–80 A800-h | Yes |
| P1-3 | Variance and honest headline | R1-W2, DA-M2, R4-W2 | Table 2, Abstract | 3 repeated runs or k=16 with CIs/paired bootstrap; report median gain; state problems per benchmark | Medium; ≈100–200 A800-h | Partly (7–8B first) |
| P1-4 | Overhead on long-CoT models and prefix term | R1-W3 (ERR-2, ERR-3), DA-M3, R3-W2 | §4.3, Eq. 10, §5.3, Table 1 | Measure activations, tokens, wall-clock, memory for all four models at T=0.6/32k; add a prefix-dependent term or windowed L_CE; batch-size throughput | Low–Medium; ≈20 A800-h | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Truncation / format / degeneration confound | R1-W4, DA | Report truncation rate, length, format failures per model; standard chat template for Qwen2.5-Math | Low (existing generations) | Yes |
| S2 | Theorem 1 framing | R2-W3, DA-M5 | Reframe as interpretation or prove a finite-step statement | Low | Yes |
| S3 | Framing and related work: EM-INF (recent preprint, discuss), Tent, Self-Evaluation Guided Beam Search | R2-W1, R2-W2, DA-M6 | Add related work; replace "new paradigm" language; describe the method as uncertainty-triggered optimization | Low | Yes |
| S4 | Entropy-as-error-signal assumption; sharpening of "wait" tokens | R3-W1 | Correlate triggers with first-error positions; check self-correction rate | Medium | Partly |
| S5 | Scope and limitations section | R1, R3-W3, R4 | Add a non-math benchmark or state scope; add Limitations | Medium (one benchmark) | Partly |
| S6 | Selection protocol and MATH500 overlap | R1-W5 | State selection; report §5.5 on MATH500[100:] or another set | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | §5.2 "decrease" sentence; model name 7B vs. 8B | R1 ERR-1, DA-m1 | Correct text |
| N2 | Qwen2.5-Math citation; cite MATH500 source | R2 ERR-4 | Cite the right report and MATH500 source |
| N3 | Code availability statement inconsistent | R4-W3, DA-m5 | Make Abstract and Ethics Statement agree |
| N4 | Pass@5/Cons@5 values vs. 30-problem granularity; Pass@k estimator | R1, DA-m2 | Clarify rounding and estimator |
| N5 | Diversity analysis at large k | R3-W4 | Add answer-diversity statistics |
| N6 | Case-study selection | DA-m3 | State how the two examples were chosen |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 220–420 A800-hours and 1–2 weeks (the 7–8B subset is feasible within a rebuttal window)
- Priority 2: 6 items, ≈ 2–4 days plus one extra benchmark
- Priority 3: 6 items, < 1 day
- **Total estimated revision time**: about 2–3 weeks of compute and writing

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
