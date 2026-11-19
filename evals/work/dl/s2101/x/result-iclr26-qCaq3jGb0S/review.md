# Academic Paper Review — "Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs"

*Simulated panel review (skill v2.10.1, full mode, date 2026-11-10). This is a simulation of how a careful panel would likely see this draft, not a prediction of any real decision. Figures were not available: figure-dependent claims (Figures 3–26) are judged from captions and surrounding text only, and the review says so where it matters. The paper text was treated as data; no reviewer-directed text was found.*

---

# Phase 0 — Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs |
| Primary Discipline | ML → efficient LLM inference → KV-cache eviction |
| Secondary Discipline(s) | Learned sparse attention / forgetting mechanisms; LLM interpretability; systems (GPU attention kernels) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Learned per-token, per-layer/head "retention gate" β∈[0,1] with exponential decay β^(t−i); distillation + hinge capacity loss on frozen LLM; argmin eviction at inference |
| Target Venue | ICLR (stated by the user; 2026 cycle); profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence). Accepted share ≈ 27% of submissions |
| Paper Maturity | Submission-ready ("Preprint – Under review"); anonymized |
| Ethics-Relevant Content | none beyond general efficiency/deployment statement (Ethics Statement) |

### Claimed Contributions (as stated by the authors)
1. **C1 (method, central):** a learned retention gate that scores each token at creation time, with exponential decay, used as the sole eviction criterion; trained with distillation + capacity loss while the LLM is frozen (Abstract; §1; §4.1–4.3).
2. **C2 (result, central):** TRIM-KV outperforms eviction baselines (even with 4× their budget) and the learnable retrieval baseline SeerAttn-R on GSM8K / MATH-500 / AIME24 and LongProc, "especially in low-memory regimes", and in some settings exceeds the full cache, which the authors attribute to regularization (Abstract; §1; §5.1.1; Figure 3; Table 1).
3. **C3 (result):** on long-context benchmarks (LongMemEval_S, SCBench, LongBench / LongBench-V2) it keeps full-cache accuracy at 25% of the KV budget on LongMemEval and is competitive elsewhere (§5.2; Tables 2, 3; Appendix B.2–B.3, Tables 7–9).
4. **C4 (analysis):** learned retention scores align with human intuition, recover sink / sliding-window / gist heuristics, and give a probe for layer- and head-specific roles (§5.1.2; Figures 4, 5, 12–26).

### Paper memory (factual record shared with all reviewers)
- **Setup.** Base models: Qwen3-1.7B/4B/8B/14B, DeepSeek-R1-Distill-Qwen-7B, -Llama-8B (§5.1); Qwen3-4B-Instruct for long context (§5.2); Phi-3-mini-128K for chunked prefill (Appendix B.3). Gate = one-hidden-layer MLP d→512→h (h = KV heads), bias init b = 8.0, λ_cap = 1.0, training M = 512 (§5.1). Math gates trained on OpenR1-Math-220K (564M tokens), lr 2e-4, weight decay 0.01, batch 1/GPU × accumulation 4, max length 16,384, 4×H100 (Appendix B.1). Long-context gates: SynthLong, BookSum, Buddhi; 10,000 steps; max 128K; M = 4096 (Appendix B.2). Evaluation: pass@1 averaged over 64 samples (AIME24) and 8 (GSM8K, MATH-500); greedy for LongProc (§5.1).
- **Not stated after search** (protocol sweep for `seed`, `variance`, `std`, `validation`, `held-out`, `select`, `tuned`): number of gate-training steps for the math gates; training time / GPU-hours; random seeds; any variance or confidence interval; any validation split; baseline hyperparameters for H2O / SnapKV / StreamingLLM / R-KV; generation length cap and sampling parameters for math evaluation; code (promised "upon publication", Reproducibility Statement).
- **Selection/tuning statements.** No sentence says a configuration was selected by test score. Ablations of loss terms, gate architecture, M and training data are all reported on AIME24 (Table 4; Figures 8–11; Appendix B.4); the architecture ablation uses Qwen3-1.7B with greedy decoding (Figure 10).
- **Headline numbers:** "4× more KV budget"; "58.4% pass@1 gain" vs SeerAttn-R; "198% relative improvement" at 1024 (AIME24) / 128 (GSM8K, MATH-500) budget (Abstract, §1, §5.1.1; source Figure 3, not visible); LongMemEval 48.2 vs Full-KV 49.4 at 25% budget (Table 3); Table 4 AIME24 74.0 (TRIM-KV, 4096) vs 65.5 (Full KV, 32768); LongBench Δ −0.64% vs LocRet −4.82% (Table 8); LongBench-V2 +6.56% over Full KV (Table 9); ~2× throughput vs full cache (Table 5).
- **Appendix adds:** inference algorithm (A.1, Algorithm 1), throughput (A.2, Table 5), Qwen3-1.7B / R1-Distill AIME24 curves (Figure 6), KeyDiff comparison (Figure 7), LongProc full results (Table 6), LongMemEval per-type results (Table 7), chunked-prefill vs LocRet on Phi-3 (Tables 8, 9), ablations (Figures 8–11), 15 qualitative visualizations (Figures 12–26; all from the first AIME24 example, Appendix C).
- **Unverifiable here:** all figures (Figure 3 Pareto frontiers carry the headline math numbers), equation typesetting (parenthesization of Eq. 1 and Eq. 3 is ambiguous in the extracted text).

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text and no hidden characters. No out-of-place instructions were noticed while reading. Nothing to report to the editor.

### Literature check
Run in **strict** mode (cutoff 2025-09-24; arXiv only): 9 logged queries (7 claim, 1 baseline, 1 expansion), 36 kept results; the one baseline query and several concept queries returned nothing usable for the AIME24 / LongProc benchmarks, so no baseline-scout rows were produced. Gap left open: no prior work kept from 2021; claim C4 (interpretability) found no close prior work (search limit, not evidence of novelty). `similarity`: closest prior work KeyDiff (cosine 0.18, no text overlap, no flag). The per-claim novelty profile attributes the paper to Locret.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Tamsin Veldkamp, area-chair type, large public research university (Europe)
- **Seniority / Expertise**: Senior faculty / efficient inference, sequence models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR actually accepts; unmoved by headline relative gains without absolute numbers

### Reviewer 1 (Methodology): Dr. Kwabena Osei-Lindqvist, industrial research lab (Europe)
- **Seniority / Expertise**: Senior industry scientist / LLM evaluation protocols for reasoning models, KV-cache benchmarking
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on variance estimates and matched budgets; recomputes every delta

### Reviewer 2 (Domain): Dr. Mei-Ling Sandoval, vision/NLP group, large public research university (Latin America)
- **Seniority / Expertise**: Mid-career faculty / KV compression and sparse attention, long-context modelling
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Builds a prior-work delta table before reading the results

### Reviewer 3 (Perspective): Dr. Rafael Ostrowski-Nakamura, computer systems and cognitive-modelling lab, private research university (East Asia)
- **Seniority / Expertise**: Associate professor / cache-replacement policies, GPU serving systems, memory models in cognitive science
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive and expansive; optimistic about potential

### Reviewer 4 (Generalist): Dr. Priya Vandenberghe, ML group, mid-sized European university
- **Seniority / Expertise**: Mid-career / deep learning for language, generalist PC member
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Weighs weaknesses against what accepted ICLR papers typically carry

### Devil's Advocate: Dr. Anselm Okafor-Reid, evaluation-methodology group, public research institute (Africa/Europe)
- **Seniority / Expertise**: Senior researcher / causal inference for ML evaluation, ablation design
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; always asks "what else explains this?"

*Personas are fictional. Proceeding with the stated assumptions (target venue ICLR as stated; paper type empirical).*

---

# Phase 1 — Independent Reviews

*(Five role-based passes in one model context, performed one after another from the reviewers' copy and the paper memory; the passes share one context and are not independent agents. Each pass worked from its own angle.)*

---

## Reviewer 1 — Methodology

# Peer Review Report

## Paper: Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
## Reviewer: Dr. Kwabena Osei-Lindqvist, Methodology (industrial research lab, Europe; fictional persona)
## Expertise: evaluation protocols for reasoning LLMs; KV-cache benchmarking; ablation design
## Date: 2026-11-10

### Summary
The paper adds a small MLP "retention gate" to every attention layer of a frozen LLM. The gate maps a token's hidden state to a per-KV-head scalar β∈[0,1]; a token's effective weight at later steps decays as β^(t−i). Gates are trained with forward-KL distillation, next-token loss and a hinge capacity loss (Eq. 4–6), and at inference the token with the lowest β^(t−j) is evicted when the cache exceeds M. Experiments cover math reasoning (Qwen3 family), LongProc, LongMemEval_S, SCBench and, in the appendix, a chunked-prefill comparison with LocRet. The claim is that learned, creation-time retention beats attention-score heuristics and a learned retrieval baseline at small budgets, sometimes even beating the full cache.

### Strengths
**S1: Broad, relevant benchmark coverage with several base models.** Long-chain-of-thought math (§5.1.1, Figure 3), procedural generation (Table 1, Table 6), conversational memory (Table 3, Table 7), and multi-task long context (Table 2) are exercised, on six base models for math (Appendix B.1, Figure 6). This is a wider protocol than most eviction papers use.

**S2: The central comparison on math is run under a common budget axis and includes a learned competitor.** SeerAttn-R is trained on the same OpenR1-Math data as the gates (§5.1 Implementation Details), which partially addresses the usual "trained vs. training-free" objection for that baseline.

**S3: Informative ablations on the objective.** Table 4 shows the capacity loss is the essential term (AIME24 42.9 without L_cap vs 74.0) and that KL and NTP are each helpful; Figures 9–11 add reversed-KL, architecture and training-M ablations. The cross-domain gate-training ablation (Figure 8, Appendix B.4) is a valuable honest check on generalization.

**S4: Appendix is candid about limits.** Retrieval-heavy SCBench tasks fail for all eviction methods (§5.2), the LongBench full-KV discrepancy is disclosed (Appendix B.3), and per-head variable budgets are left as future work (§5.1.2).

### Weaknesses

**W1: No uncertainty estimates anywhere, on benchmarks where differences are small or the sample is tiny.** The paper reports no seeds, standard deviations or intervals (protocol sweep: not stated). AIME24 has 30 problems; averaging over 64 samples removes decoding noise but not the problem-set or gate-training-seed noise, and gates are trained once. The Table 4 ablation differences (74.0 vs 71.4 vs 70.7) are 2.6–3.3 points; Table 9 claims TRIM-KV "even surpass[es]" the full cache by +6.56% relative, which is +1.89 absolute (30.68 vs 28.79) on a small benchmark; LongMemEval SS-Pref has 30 questions (Table 7). Large margins (e.g., Table 1 Countdown 97.5 vs SnapKV 57.0) are likely robust, but the "surpasses full cache" statements are not.
- **Suggested Fix:** Train 3 gate seeds for Qwen3-4B (the paper's main model) and report mean ± std on AIME24 at two budgets; add paired bootstrap over problems for Table 4, Table 9 and the full-cache comparisons. Cost: 3 × the (unreported) math gate-training run plus ~10 GPU-hours of evaluation per budget.

**W2: The headline claim (learned *intrinsic* importance beats attention-based importance) is confounded with "task-matched training vs. training-free".** On math, gates are trained on OpenR1-Math-220K and evaluated on three math benchmarks (§5.1, Appendix B.1), while H2O, SnapKV, StreamingLLM and R-KV are training-free (§5.1 Baselines). The only trained comparator, SeerAttn-R, is a retrieval method with a different mechanism. No control isolates the specific design choice (creation-time score with decay) from "any distillation-trained policy". The cross-domain ablation (Figure 8) helps but shows weaker results under tight budgets ("their performance degrades more quickly under tighter KV budgets", Appendix B.4).
- **Suggested Fix:** Add one control trained with the identical loss and data, e.g., a learned per-head sink+window size, or an attention-statistics-based learned scorer, at 2 budgets on Qwen3-4B AIME24. Report gate-training cost (steps, GPU-hours) next to every baseline.

**W3: "Surpasses the full cache" is reported without establishing that the comparison is clean, and the explanation ("regularization") is untested.** Table 4: Full KV (budget 32768) 65.5 vs TRIM-KV (4096) 74.0; Table 6 HTML-to-TSV 0.5k at budget 8192: 58.2 vs Full KV 49.0. At inference TRIM-KV only evicts (§4.3); if the sequence is shorter than the budget it is identical to the full cache, so a +9.2 point gain at budget 8192 on a 0.5K-output task means either the contexts exceed 8192 tokens or something else differs. The full-KV reference configuration (generation cap, sampling, chat template, thinking mode) is not given; a capped full-cache run that truncates long chains of thought would look worse than a policy that shortens or breaks repetition loops.
- **Suggested Fix:** Report generation-length distributions and the fraction of truncated/looping outputs for Full KV vs TRIM-KV; state context lengths per LongProc tier; report Full KV with a larger cap. If the "regularization" explanation is kept, test it (e.g., random-eviction control at matched sparsity).

**W4: Baseline configuration is undocumented and some baseline numbers look implausibly low.** Table 1 shows StreamingLLM 7.0/5.0/5.0 and H2O 12.0/7.5/2.5 on Countdown at budget 2048, where TRIM-KV gets 97.5/93.5/66.0 and Full KV 96.0/90.0/69.0. Table 6 shows SnapKV 37.1 vs Full 49.0 on HTML-to-TSV 0.5k at budget 8192, and ~0 on Travel/Thought-of-Mind at 8k. Window size, sink size, pooling kernel, whether the "budget" includes the recent window, and the source of each implementation are not stated (not stated after search). Without a sanity check that each baseline equals the full cache when the budget exceeds the sequence length, a reader cannot tell whether the gaps reflect the policies or the setup.
- **Suggested Fix:** Add an appendix table of baseline settings and implementation sources; add the "budget ≥ length ⇒ identical to Full KV" sanity row; give R-KV/SnapKV their published recommended settings.

**W5: Relative-gain headlines are computed at the most favorable budgets and are not reproducible from the text.** "198% relative improvement" is quoted at 1024 (AIME24) and 128 (GSM8K/MATH-500) "over these baselines", and "58.4% pass@1 gain" vs SeerAttn-R is not defined as absolute or relative, nor averaged over which settings (§5.1.1; Abstract; §1). Ratios of small numbers at extreme budgets inflate such figures. Source numbers are in Figure 3 (not visible), so I treat them as unverifiable, not wrong.
- **Suggested Fix:** Put the underlying numbers in a table (budget × method × benchmark, absolute pass@1 with intervals) and state how each headline was computed.

**W6: Training/inference mismatch and an unverified capacity proxy.** Training uses soft, whole-sequence modulation β^(t−i) (Eq. 3) and a soft capacity penalty Σβ^(t−i) ≤ M (Eq. 5), up to length 16,384 (Appendix B.1); inference uses hard top-M eviction (§4.3) at budgets from 128 to 4096 and generation up to 32K (Table 4, Full KV 32768). Nothing shows that the soft sum predicts the quality of hard eviction, or that gates generalize beyond the trained length (the training-length cap is below the evaluated generation lengths). "Globally optimal caching policy" (§1, §4.2) is not supported by any analysis.
- **Suggested Fix:** Report output-distribution fidelity (KL to the full model) against budget for the hard-evicted model; evaluate length extrapolation (train at 16K, test at 2×); drop "globally optimal".

**W7: Reproducibility gaps.** Missing: number of math-gate training steps, wall-clock/GPU-hours, seeds, sampling parameters and generation cap for math evaluation, judge configuration beyond "Qwen3-4B-Instruct" for LongMemEval (§Appendix B.2). Code and checkpoints are promised only "upon publication".
- **Suggested Fix:** Add these to Appendix B.1; release an anonymized repository during review.

**Minor:** Table 5 context lengths 32786 / 16378 appear to be typos for 32768 / 16384; "Patero" in the Figure 3 / Figure 6 captions; "Lllam" in §5.1 Base Models.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | Appendix B.1 text vs Table 6 | "Across tasks and budgets, TRIM-KV achieves the best performance" | Table 6, Thought of Mind 0.5k at budget 8192: H2O 38.0 > TRIM-KV 32.5 (and > Full KV 33.0) | Cross-referenced the two locations | High | MINOR | Qualify the sentence ("best on most columns") |
| ERR-2 | E1/E6 | Table 8 | Full KV `lcc` = 33.35, identical to `gov_report` = 33.35 | Two different tasks with an identical Full-KV score to 2 decimals; the LocRet-paper reference row gives lcc 51.86 | Cross-referenced rows; Avg Δ recomputed from the printed numbers (−0.63 vs printed −0.64) so the printed Δ uses 33.35 | Medium | MINOR | Verify the lcc Full-KV number and recompute Δ if it was a copy error |
| ERR-3 | E1 | Table 7 (and Table 3) | "TRIM-KV32768 … 48.2" | Weighting the per-type accuracies by the question-type counts that reproduce the other rows (Full KV 49.43, StreamingLLM 27.80, SnapKV 27.60, TRIM-KV 4096 30.2) gives 47.98 for this row | Recomputed | Medium | MINOR | Check the per-type or overall value |
| ERR-4 | E6 | §1 vs Appendix A.1 | "with a preference toward more recently generated tokens" vs "does not add any extra recency bias" | The decay β^(t−j) used in the eviction rank (§4.3) is an explicit age term; the two statements conflict | Cross-referenced | High | MINOR | Reword A.1 (the base model's bias is not *added to*, but the rank does depend on age) |
| — | E1 (unverifiable) | Abstract/§1/§5.1.1 | "58.4% pass@1 gain"; "198% relative improvement" | Source is Figure 3 (not visible); cannot recompute | — | — | — | Provide the table |

### Questions for Authors
1. Eq. (1) as extracted places α_ti inside exp(·) multiplying q_t^⊤ k_i. Read literally, α = 0 gives weight exp(0) = 1 rather than removing the token, and Eq. (3)'s β^(t−i) would drive old tokens' logits toward 0, not their weights. §4.1 ("exp((t − i) log β_i)") suggests the intended form is a multiplicative weight β^(t−i) on exp(q^⊤k). *Is the extraction faithful?* If not, please state the precise form (and whether training uses a mask or a log-bias). Answer could change my Technical Rigor score.
2. What are the context lengths of each LongProc tier, and does eviction actually trigger at budget 8192 for the 0.5K tier (Table 6)? Which would raise or lower my reading of the "beats full cache" rows.
3. What are the generation cap, temperature/top-p and thinking mode for Full KV on AIME24? Is the Qwen3-4B full-cache figure of 65.5 comparable with the model's officially reported AIME24 number? [verify; I do not rely on a figure from memory]
4. How many steps / GPU-hours were used for the math gates, and what was the variance across gate-training seeds?
5. Were M = 512, λ_cap = 1.0, the MLP gate and b = 8.0 fixed before the AIME24 ablations, or chosen from them?

### Limitations Assessment
**Partially.** Retrieval-heavy failures and the per-head-budget gap are acknowledged; variance, training cost, peak memory during prefill and per-model retraining are not.

### Ethics Review Flag
**No**

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea and broad evaluation, but no uncertainty and an unisolated mechanism (Quality maps from TR 62 / EV 58 → 60, just under the 62 line) |
| Clarity | 3 | Readable; Eq. 1/3 and baseline setup need work |
| Significance | 3 | Practically useful at small budgets |
| Originality | 2 | Decay-gated learned scoring; close to learned-scorer work (see R2) |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: strong, wide empirical gains on math reasoning with sound ablations place it above the median; missing variance, undocumented baselines and an unisolated mechanism keep it below the typical accepted paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Method coherent; train/inference mismatch and Eq. 1/3 formulation questions (W6) |
| Clarity & Presentation | 66 | Competent | Clear narrative; method notation ambiguous; typos |
| Novelty & Originality | 60 | Competent | Meaningful but adjacent to learned-scorer work |
| Significance & Impact | 66 | Competent | Useful for reasoning-model serving |
| Experimental Validation | 58 | Competent | Wide but unreplicated; confound W2; baselines undocumented |
| Reproducibility | 62 | Competent | Hyperparameters largely given; steps/time/code missing |
| Ethical Compliance | 66 | Competent | Generic statement, no tension |

### Overall Score
**4 (Borderline Accept):** the evidence for the main practical claim (small-budget math reasoning) is strong enough to lean accept; I would raise to 5 with variance plus a control for W2, and lower to 3 if the Table 6/Table 1 baselines turn out to be misconfigured.

### Confidence
**4:** careful reading of tables; figures unavailable.

---

## Reviewer 2 — Domain

# Peer Review Report

## Paper: Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
## Reviewer: Dr. Mei-Ling Sandoval, Domain (vision/NLP group, large public university, Latin America; fictional persona)
## Expertise: KV-cache compression; sparse and learned attention; long-context modelling
## Date: 2026-11-10

### Summary
TRIM-KV proposes a learned "retention" score per token, per layer and KV head, with an exponential time decay, used to evict the lowest-scoring token when the cache exceeds a fixed budget. It is trained by distilling a frozen LLM's outputs with a capacity penalty, and evaluated primarily on reasoning-model generation under small budgets. The authors position it between heuristic attention-based eviction, compression/quantization, and retrieval/offloading methods, and in the appendix against the learned prefill-stage eviction method LocRet.

### Strengths
**S1: Clear positioning into three lines of work and a well-motivated gap (§1, §2).** The distinction between query-time attention scores (myopic) and creation-time long-horizon utility is stated crisply and motivates the design (§4.1, "Token Retention vs. Attention Scores").

**S2: Targets the generation stage, which learned eviction work has mostly skipped.** Related work notes that earlier learnable policies are designed for prefilling (§2); the paper evaluates long chain-of-thought generation (§5.1) as well as prefill-heavy settings (§5.2, Appendix B.3).

**S3: A like-for-like comparison with the closest learned eviction baseline.** Appendix B.3 trains on the same data as LocRet, matches chunk size and budget, and reports that LocRet's own hand-crafted sliding window is not needed (Tables 8, 9). This is good scientific hygiene.

**S4: Empirical story is coherent with the design.** Emergent window/sink structure (Figure 4) and the head-wise sparsity pattern (Figure 5c) are consistent with the claims about per-head specialization, and agree with prior descriptions of head heterogeneity (§5.1.2 cites Cai et al., 2024).

### Weaknesses

**W1: The novelty delta against the closest learned scorers is under-argued, and the key comparison is run only in the appendix on a different model.** The paper says learnable eviction work is "limited to the prefilling stage" (§1; §2). Locret, the closest prior work (per the claim-level profile), is described by the paper itself as assigning token-importance scores for eviction, with a hand-crafted sliding window (Appendix B.3); DMC (Nawrot et al., 2024) is cited in the eviction/merging list (§2) but neither differentiated nor compared. The real differences (decay term, end-to-end joint distillation with a capacity loss, use during generation) are legitimate, but the "new perspective" framing (§1) overstates the gap, and the Locret-style comparison is not run on the generation benchmarks (AIME24 / LongProc) that carry the main claim. This is a claim-level finding (C1 medium novelty), MAJOR at most.
- **Suggested Fix:** Run a retaining-head / learned-scorer baseline on Qwen3-4B AIME24 and LongProc at matched budgets, or ablate the decay term (learned scalar without β^(t−i)); add a sentence differentiating DMC and the A2SF-style forgetting-factor scoring (see literature addendum).

**W2: The main comparison omits adaptive-budget and learned head-level methods, and the strongest argument for the premise is untested against the literature.** The motivating claim is that attention-based scores are "unreliable proxies" (§1), but no experiment compares against the persistence-of-importance line (Scissorhands), head/layer-adaptive budget methods (Ada-KV; PyramidKV is cited only for a sparsity trend, §5.1.2), or the learned head-type split of DuoAttention. Budget-allocation methods matter here because TRIM-KV's own results show strongly head-specific behavior (Figures 4, 5c) while its evaluation uses a uniform per-head budget (§5.1.2).
- **Suggested Fix:** Add at least one adaptive-budget eviction baseline (Ada-KV-style) on Qwen3-4B AIME24 and a short discussion of the persistence-of-importance hypothesis (what it predicts for creation-time scoring).

**W3: Theoretical framing is overstated and the link between Eq. (2) and the training objective is not established.** Eq. (2) poses a hard constrained problem; §4.2 says the joint training yields "a coordinated, globally optimal caching policy" and the loss (Eq. 5) bounds a soft sum Σβ^(t−i) at one fixed M. No argument or experiment connects the optimum of Eq. (6) to the hard top-M rule's minimizer of Eq. (2), nor explains when a creation-time score can suffice when relevance depends on future queries. The authors' own SCBench result (Table 2: Retr.KV 0.00, Code.RepoQA 4.32 vs Full 53.86) is exactly the regime where it cannot, and is dismissed as "incompressible" (§5.2) without evidence.
- **Suggested Fix:** Replace "globally optimal" with the weaker claim, add a short analysis (or oracle experiment) of when query-independent scores can match query-aware ones, and test the "incompressible" assertion, e.g., with a retrieval-style method on the same budget.

**W4: "Newly observed" behaviors rest on one example and a different object than prior head analyses.** The claim that absence of a sliding window, multiple coexisting windows and context switching are "newly observed eviction patterns" (§5.1.2) is based on retention matrices of a single AIME24 example (Appendix C: "All visualizations are from the first example in the AIME24 dataset"), and prior head-pattern work analyzes attention, not learned retention.
- **Suggested Fix:** Quantify the patterns over many prompts (fraction of heads per pattern, stability across prompts and models) before claiming novelty; relate to prior head-role analyses.

### Missing References (literature check: strict, cutoff 2025-09-24, arXiv-only search; each entry confirmed with `related_search.py verify` unless marked)
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Liu et al., "Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time", 2023 (https://arxiv.org/abs/2305.17118) | Directly addresses whether past importance predicts future importance; relevant to the premise in §1 |
| Important | Feng et al., "Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference", 2024 (https://arxiv.org/abs/2407.11550) | Head-adaptive budgets; relevant to Figure 5c and the uniform-budget evaluation |
| Important | Xiao et al., "DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads", 2024 (https://arxiv.org/abs/2410.10819) | Learned head-level split between full-cache and sliding-window/sink behavior; overlaps with the "emergent heuristics" claims |
| Important | Ge et al., "Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs", 2023 (https://arxiv.org/abs/2310.01801) | Profile-based per-head eviction policies |
| Helpful | "CriticalKV: Optimizing KV Cache Eviction from an Output Perturbation Perspective", 2025 (https://arxiv.org/abs/2502.03805; prior, peer-reviewed label) | Eviction scored by effect on output rather than attention weight |
| Helpful | "A2SF: Accumulative Attention Scoring with Forgetting Factor for Token Pruning in Transformer Decoder", 2024 (https://arxiv.org/abs/2407.20485; prior, arXiv-only) | Forgetting-factor decay in eviction scoring (training-free), a close cousin of the decay design |
| Worth discussing (recent preprint / concurrent; never a weakness, no score effect) | "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning", 2025 (https://arxiv.org/abs/2506.15969); Bhaskar et al., "Cache Me If You Can: How Many KVs Do You Need for Effective Long-Context LMs?", 2025 (https://arxiv.org/abs/2506.17121); "EvolKV: Evolutionary KV Cache Compression for LLM Inference", 2025 (https://arxiv.org/abs/2509.08315) | Same sub-area, within six months of the cutoff |

### Literature-check addendum
**Per-claim novelty (claim-level profile, `related_search.py novelty`):**
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|--------------------------------------------|-----------|
| C1 | method | medium | Locret, level 3 (https://arxiv.org/abs/2410.01805v2; prior arXiv-only; cited) | A learned per-token importance scorer trained for eviction exists and is cited; differences are the decay, joint end-to-end training, and generation-stage use |
| C2 | result | high | CriticalKV, level 2 (not cited) | Topic overlap only |
| C3 | result | medium | Locret, level 3 (cited) | Prefill-stage learned eviction on long-context benchmarks |
| C4 | result | no close prior work found in 9 queries (arXiv only; at most medium) | — | A search limit, not evidence of novelty |

Paper reading: no established claim; the paper is not "known". Closest prior work (attribution): Locret.

**Novelty delta table**
| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|------------------------------|------------------|---------------------------|
| Creation-time learned retention gate for eviction | Locret (2410.01805) | Per the paper's own description (App. B.3): learned token-importance scores for eviction in chunked prefill, with a hand-crafted recent window | Exponential decay with per-token β, joint end-to-end training via distillation + capacity loss, generation-stage eviction, no hand-crafted window | Cited; differentiated only in Appendix B.3 |
| Decay of importance over time in eviction scoring | A2SF (2407.20485) | Training-free forgetting factor on accumulated attention scores | Learned decay rate per token and head | Not cited |
| Query-agnostic eviction | KeyDiff (2504.15364) | Key-similarity-based eviction | Learned rather than geometric | Cited; compared in Figure 7 |

**Baseline scout.** The baseline query for AIME24 returned nothing usable and no external benchmark rows were produced; no under-reported baseline can be claimed. Only prior work could be required comparisons; the recent preprints above are "worth discussing".

**Field snapshot (as of the cutoff).** Three years ago eviction was dominated by attention-score heuristics (heavy hitters, sinks, observation-window SnapKV-style scoring). Since then the field added budget allocation across layers and heads, query-agnostic and output-perturbation scoring, reasoning-specific methods for long generations (e.g., redundancy-aware eviction, lagged eviction), and learned or retrieval-style designs (retaining heads, learned sparse attention for reasoning). Open problems stated by recent work: robust performance on long reasoning traces at very small budgets, retrieval-heavy tasks where all eviction fails, fair comparison with unified metrics, and real-system speedups rather than token counts. In this sub-field, +1–2 points at a fixed budget over a training-free baseline is incremental; matching full-cache accuracy at 4–8× smaller budgets across several model sizes without a new inference stack, with real throughput gains, would be a clear contribution. I used this to score Novelty as incremental-to-moderate and Significance as moderate.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound design and ablations |
| Clarity | 3 | Well organized |
| Significance | 3 | Moderate-to-good impact |
| Originality | 2 | Adjacent to learned scorers (TR/EV drop to the 2 boundary on novelty 58) |

### Dimension Scores (0–100)
**Pool position:** better than about 68% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear and practical contribution with strong results; novelty is medium relative to Locret-type work and key adaptive-budget and learned baselines are absent from the main comparison.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Coherent method; theory claims overstated |
| Clarity & Presentation | 68 | Competent | Well-positioned related work |
| Novelty & Originality | 58 | Competent | Medium per-claim novelty (Locret) |
| Significance & Impact | 68 | Competent | Reasoning-model serving is timely |
| Experimental Validation | 62 | Competent | Broad but baseline set misses adaptive/learned methods |
| Reproducibility | 66 | Competent | Details mostly present |
| Ethical Compliance | 66 | Competent | Adequate statement |

### Questions for Authors
1. Can you run Locret (or a retaining-head variant) under your generation protocol on AIME24? A matching or better result for TRIM-KV would raise my Novelty and Experimental scores.
2. How does the method compare with an adaptive-budget baseline (Ada-KV-style) given the head heterogeneity in Figure 5c?
3. What does the persistence-of-importance hypothesis predict for your creation-time premise, and where does it fail (Table 2)?

### Limitations Assessment
**Partially.** No discussion of when query-independent importance is inadequate beyond a one-line attribution to "incompressible" contexts (§5.2).

### Ethics Review Flag
**No**

### Overall Score
**4 (Borderline Accept):** useful, timely and well positioned, with medium novelty and a baseline set that should include adaptive-budget and learned-scorer comparisons.

### Confidence
**4:** field known well; the literature check was arXiv-only and strict.

---

## Reviewer 3 — Perspective

# Peer Review Report

## Paper: Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
## Reviewer: Dr. Rafael Ostrowski-Nakamura, Perspective (computer-systems and cognitive-modelling lab, private university, East Asia; fictional persona)
## Expertise: cache-replacement policies; GPU serving systems; memory models in cognitive science
## Date: 2026-11-10

### Summary
The paper replaces recency/attention-based KV eviction with a learned, per-head retention score that decays with age, so a cache of fixed size holds the tokens judged most valuable. Beyond accuracy at small budgets, it argues that the scores reveal what individual heads "care about". From a systems point of view it is an inexpensive add-on to a frozen model, compatible with fused attention kernels, offering measured decode speed-ups (Appendix A.2, Table 5).

### Strengths
**S1: Practical deployability story.** Only a small gate is trained, FlashAttention-style kernels remain usable through FlexAttention plus a custom Triton loss kernel (§4.2 Hardware-aware Computation), and decode throughput is about 1.9× the full cache at 32K context (Table 5: 130.48 vs 68.44 tok/s). This is the kind of evidence a serving team looks for.

**S2: An elegant, minimal abstraction.** One scalar per token per head, an age-dependent comparison and an argmin (Algorithm 1) is easy to integrate, and Appendix A.2 estimates the memory overhead at ≈ 1/d_h.

**S3: Learned scores as a diagnostic.** The head-level views (Figures 4, 5c, 12–26) suggest a lightweight way to see which heads keep recency windows, sinks or operator tokens; this is a genuinely attractive by-product for interpretability and for budget allocation.

**S4: Transfer beyond the training domain.** Gates trained on math traces also help on LongProc (Table 1), and Figure 8 probes the reverse transfer, which is encouraging for a deployment where one gate set serves many tasks.

### Weaknesses (framed as opportunities)

**W1: Systems integration is incomplete, and peak memory is not reported.** The authors note that per-head variable-length caches are not supported by current kernels and leave heterogeneous budgets to future work (§5.1.2). The efficiency evidence is a single H200, batch 4–8, one generation length (Table 5), without R-KV or H2O, without variance, and with SnapKV slightly faster in one row (16K, batch 4: 153.21 vs 151.04 tok/s). More importantly, for long contexts (123K tokens, §5.2) it is not stated whether the prompt is prefilled in chunks with eviction or prefilled in full and then compressed; in the latter case peak memory is not bounded, which matters for a "memory-bounded" title.
- **Suggested Fix:** Report peak GPU memory and prefill protocol for Tables 2, 3 and 7; add a vLLM/PagedAttention-compatibility discussion; include a small batch-size sweep with error bars.

**W2: The "intrinsic importance at creation time" assumption is the paper's main bet and its limits are only partly examined.** A token's future relevance depends on future queries. The SCBench results in Table 2 (Retr.KV 0.00 for TRIM-KV, H2O and SnapKV; Code.RepoQA 4.32 vs Full KV 53.86) show where it breaks, and the explanation offered is that "the context is incompressible" (§5.2). A cross-disciplinary view helps: in classical cache replacement, Belady's optimal policy uses future knowledge, and learned replacement policies are typically evaluated by how close they get to that oracle; a similar "oracle retention" upper bound (using the full model's future attention) would show how much headroom a creation-time predictor has.
- **Suggested Fix:** Add an oracle-retention reference on AIME24 and on one SCBench retrieval task; discuss hybrid designs where a query-aware retrieval path handles retrieval-heavy requests.

**W3: Interpretability claims outrun the evidence.** The abstract speaks of "a new path toward LLM interpretability"; the supporting evidence is qualitative and drawn from the first AIME24 example (Appendix C), with hypotheses such as "periods act as implicit gist tokens" (§5.1.2) left unchallenged. The mechanistic interpretability literature (e.g., work on retrieval heads and induction heads) provides ready causal tests: ablate or force-retain the flagged heads and measure the effect.
- **Suggested Fix:** Aggregate pattern statistics over many prompts and run one causal intervention (e.g., force-evict periods in the heads flagged as gist heads) before presenting the interpretability claim.

**W4: Instruction retention and safety have not been examined.** If a gate assigns low retention to tokens that carry system or safety instructions, an evicted instruction can silently change behavior in long conversations (LongMemEval-style, §5.2). The Ethics Statement is generic.
- **Suggested Fix:** Test whether system-prompt and refusal-relevant tokens survive at small budgets in a multi-turn setting; report instruction-following and a small safety probe under eviction.

**W5: Scale and architecture coverage.** The method is shown on 1.7B–14B Qwen3 and two R1-distilled models for math and one 4B model for long context; the Ebbinghaus-style analogy (§4.1) is decorative, and there is no test on larger models, MoE or non-RoPE-style variants.
- **Suggested Fix:** Add one larger model or a different family at a single budget, and tone down the cognitive analogy to motivation.

### Missing References
Not a focus of this review. I suggest the authors connect the work to the classical caching literature (the Belady optimal-policy oracle and learned cache replacement / learning-augmented caching) and to head-function analyses in mechanistic interpretability, naming these as lines of work rather than specific papers.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound and deployable |
| Clarity | 3 | Clear |
| Significance | 3 | Real practical value (74 maps to 3, just under the 4 line) |
| Originality | 3 | Fresh framing for generation-stage eviction |

### Dimension Scores (0–100)
**Pool position:** better than about 77% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a simple, practical, well-motivated method with consistent gains at small budgets and a useful by-product; I weight deployment value and the clear idea more than the missing systems integration.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 70 | Competent | Sound; some theory overstated |
| Clarity & Presentation | 74 | Competent | Clear and well organized |
| Novelty & Originality | 68 | Competent | Fresh framing |
| Significance & Impact | 74 | Competent | Timely for reasoning serving |
| Experimental Validation | 66 | Competent | Broad evidence |
| Reproducibility | 70 | Competent | Details given; code promised |
| Ethical Compliance | 68 | Competent | Statement present, safety not probed |

### Questions for Authors
1. In Tables 2, 3 and 7, is prefill chunked with eviction or full prefill followed by compression, and what is peak memory? A bounded peak would raise my Significance score.
2. Do system-prompt tokens survive in multi-turn runs at the 4096 budget?
3. How far is TRIM-KV from an oracle retention policy on AIME24?

### Limitations Assessment
**Partially.** Future work on per-head budgets is acknowledged; query-dependence, prefill memory and safety interplay are not discussed.

### Ethics Review Flag
**No**

### Overall Score
**5 (Accept):** a simple, practical method with consistent gains and a useful interpretive by-product; the gaps are about extension and evidence, not soundness.

### Confidence
**3:** strong on systems and cognitive angles; did not verify the training details.

---

## Reviewer 4 — Generalist

# Peer Review Report

## Paper: Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
## Reviewer: Dr. Priya Vandenberghe, Generalist (ML group, mid-sized European university; fictional persona)
## Expertise: deep learning for language; broad PC member
## Date: 2026-11-10

### Summary
The paper tackles the growth of the KV cache in long reasoning and long-context generation. It trains small gates that assign each token a decaying retention score; the lowest-scoring token is evicted when the cache is full. The reported benefit is higher accuracy than heuristic eviction at small budgets on math reasoning and several long-context benchmarks, with throughput comparable to a heuristic method and notable qualitative structure in the learned scores.

### Strengths
**S1: Clear problem and a clear idea.** The motivation (attention-based eviction forgets tokens that matter later, §1) and the remedy (creation-time retention with decay, §4.1) are easy to state in one paragraph.

**S2: Strong, broad empirical story at small budgets.** Table 1 (Countdown 97.5/93.5/66.0 vs R-KV 88.5/81.0/63.0 at budget 2048), Table 3 (48.2 vs 49.4 full cache at 25% budget) and Figure 3 (math) show consistent advantages over eviction baselines; six base models are used (Appendix B.1).

**S3: Good fit for ICLR.** Representation-/inference-efficiency work with a learned component, ablations (Table 4; Figures 8–11) and analysis is within ICLR's usual scope.

**S4: Honest about some limits.** Failures on retrieval-heavy SCBench tasks and the full-KV discrepancy under different chat templates (Appendix B.3) are disclosed.

### Venue Criteria Checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly: strong core, but regularization, interpretability and "consistently" claims go beyond evidence | §5.1.1, §5.1.2, Abstract |
| Contribution: clear, useful to the community | Met | §1, Table 1, Table 3 |
| Presentation: self-contained, readable | Mostly met (Eq. 1/3 and the baseline setup need work) | §3.2, §4.1, §5.1 |
| Related work positioned, not only listed | Partly (learned-scorer comparison deferred to Appendix B.3) | §2, Appendix B.3 |
| Reproducibility (artifacts, hyperparameters) | Partly (hyperparameters yes; steps, time, code no) | Appendix B.1, Reproducibility Statement |

### Weaknesses
**W1: The abstract and introduction claim more than the tables show.** "TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines … long-context understanding (LongBenchV2 and SCBench)" (Abstract). In Table 2, TRIM-KV loses to SnapKV on Math.Find (13.80 vs 18.60) and to StreamingLLM on Retr.KV (0.00 vs 2.20), ties on ICL.ManyShot (100.00), and collapses on Code.RepoQA (4.32 vs Full 53.86); LongBench-V2 appears only in Appendix B.3 against one baseline on Phi-3 (Table 9). "Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization" states a mechanism that no experiment tests.
- **Suggested Fix:** Reword to "outperforms on math reasoning, LongProc and LongMemEval; competitive on most SCBench tasks, but fails on retrieval-dominated ones", and present "regularization" as a hypothesis.

**W2: Headline numbers live in figures and are hard to audit from the text.** The 198% and 58.4% gains (§5.1.1) and the "4× budget" statement come from Figure 3, with no table in the main text; the Pareto-frontier figure is the paper's central evidence, and its caption has a typo ("Patero"). Without a results table, a reader cannot check the claims or see budgets where the method does not win.
- **Suggested Fix:** Add a compact main-text table of absolute pass@1 per budget for Qwen3-4B and 8B.

**W3: The method section is harder to read than the rest.** Eq. (1) and Eq. (3) use α, ᾱ and β with similar notation; the form of the attention modulation is ambiguous (see R1 Q1); §4.2 mixes training and inference concepts; and the appendix claim of no extra recency bias (A.1) conflicts with the decay design stated in the introduction. Several sentences in §5.2 ("As shown in Table 3 and Table 2 show") need editing.
- **Suggested Fix:** Add a short "what is computed at training vs inference" box and state the exact attention formula, including how an evicted token is excluded.

**Minor:** "Patero" (Figures 3, 6), "Lllam" (§5.1), Table 5 lengths 32786 / 16378, Table 1 bold/underline legend lost in some renderings.

### Questions for Authors
1. What would a reader see in a table of absolute pass@1 per budget for the 4B model? Seeing the method also win at the largest budgets would raise my Experimental Validation score.
2. Is the full-cache number for the 4B model on AIME24 (65.5, Table 4) configured as in the official evaluation? A mismatch would lower my confidence in the "surpasses full cache" results.
3. Can you state the exact form of the attention modulation (Eq. 1 / 3) so evicted tokens are provably excluded?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No**

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid, with unverified claims |
| Clarity | 3 | Method section needs work |
| Significance | 3 | Moderate-to-high |
| Originality | 3 | Fresh combination |

### Dimension Scores (0–100)
**Pool position:** better than about 72% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea with wide, mostly consistent evidence puts it at the low end of typical accepted papers; overclaiming in the abstract and missing uncertainty keep it from the upper band.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 68 | Competent | Sound core; mechanism claims unsupported |
| Clarity & Presentation | 72 | Competent | Well written except the method section |
| Novelty & Originality | 62 | Competent | Incremental-to-moderate |
| Significance & Impact | 68 | Competent | Useful |
| Experimental Validation | 64 | Competent | Wide; no uncertainty |
| Reproducibility | 68 | Competent | Details present; code promised |
| Ethical Compliance | 66 | Competent | Basic compliance |

### Overall Score
**4 (Borderline Accept):** a clear, useful idea with good results whose weaknesses (overclaiming wording, missing variance) are typical of accepted ICLR papers; the community would lose a practical technique if it were rejected.

### Confidence
**4:** read the full paper including the appendix; figures unavailable.

---

## Devil's Advocate

# Devil's Advocate Report

## Paper: Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
## Reviewer: Dr. Anselm Okafor-Reid (evaluation-methodology group, public research institute; fictional persona)

## Steelman
A tiny learned gate, trained for a modest cost on a frozen model, produces a retention order that keeps long reasoning traces intact at 4–8× smaller caches, beating every training-free eviction heuristic and a learned retrieval baseline, with minimal overhead, and its learned scores reveal head-level structure. If the results are replicated, the method is a practical drop-in for serving reasoning models.

## Core Argument Chain
1. Attention-based importance is an unreliable proxy for future importance (§1).
2. A token's long-term utility is predictable at creation time from its hidden state (§1, §4.1).
3. A gate trained by distillation with a capacity loss learns that utility (§4.2, Table 4).
4. Evicting by the smallest decayed score preserves performance under small budgets (Table 1, Figure 3, Table 3).
5. The gains over baselines come from the retention mechanism, and exceeding full-cache accuracy reflects regularization (Abstract).
∴ Intrinsic, learned retention is a better basis for KV eviction than attention-guided heuristics.

## Strongest Counter-Argument
Premises 1→4 may all be true while the conclusion in 5 is not shown. What the experiments establish is that *a policy trained on in-distribution reasoning traces with a distillation + sparsity objective* beats *untrained heuristics that were not designed for 1k-token budgets on long chain-of-thought*. The paper never separates the three ingredients: (a) task-matched training, (b) a learned per-head sparsity pattern (the qualitative analysis itself says the result is sinks, sliding windows and A-shapes of per-head widths, Figure 4 and §5.1.2), and (c) creation-time scoring with decay. A simpler learned policy, such as a per-head learned window size plus sink count trained with the same loss, could recover most of the gain without claiming that "intrinsic token importance" is learned; indeed, the most striking behaviors are the *heuristics* the paper says it "recovers". The one place where the premise is directly tested is where it fails: in SCBench (Table 2), where relevance depends on the query, creation-time retention scores 0.00 on Retr.KV and 4.32 on Code.RepoQA against 66.00 and 53.86 for the full cache, and the authors attribute this to the contexts being "incompressible" without testing it. That the model exceeds the full cache on AIME24 (Table 4: 74.0 vs 65.5) and HTML-to-TSV 0.5K (Table 6: 58.2 vs 49.0 at budget 8192) is presented as regularization; equally plausible explanations are a poorly configured full-cache reference (truncation at the generation cap; repetition loops) or evaluations in which eviction rarely triggers. Without a control, the paper's causal narrative (§5.1.1, Abstract) rests on interpretation, not on evidence. The authors need a trained-control baseline, a stated full-cache configuration and a test of the regularization claim.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core empirical claim (TRIM-KV outperforms the training-free baselines on math reasoning at small budgets) survives: the paper's own tables support it at large margins, no selection statement on the reported test set is made, and each concern can be addressed by narrowing claims or adding controls.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (alternative explanation) | §5.1; Appendix B.1; Figure 8 | Trained, task-matched policy vs. training-free baselines; no control isolating creation-time retention (evidence supports a weaker claim: "a learned policy helps") | Add a trained learned-window/sink control with the same loss and data; report training cost |
| DA-M2 | Evidence (claim distortion, E5) | Abstract; §5.1.1; Table 4; Table 6 | "Surpasses full cache … regularization": mechanism untested; reference configuration unspecified; eviction may not trigger | Report generation lengths, truncation rates, context lengths; add a matched-sparsity random-eviction control; or present as hypothesis |
| DA-M3 | Protocol (test-set design choices) | Table 4; Figures 9–11; Figure 10; Appendix B.4 | Loss terms, gate architecture (greedy, Qwen3-1.7B), M and training data are all ablated on AIME24, which has no validation split and is also the headline benchmark. The paper does not state whether the final configuration was chosen from these. Not stated after the protocol sweep (no selection sentence); the headline M = 512 and λ = 1.0 appear fixed in advance | State the selection protocol; confirm the headline configuration on held-out data (e.g., a different AIME year or MATH-500) |
| DA-M4 | Logic (premise tested where it fails) | §5.2; Table 2 | Creation-time scores cannot capture query-dependent relevance; "incompressible" is asserted | Test with an oracle/query-aware method at the same budget; narrow the "intrinsic importance" claim |
| DA-M5 | Claim distortion (E5) | Abstract; Table 2; Table 6 | "consistently outperforms … SCBench"; "Across tasks and budgets … best": Table 2 Math.Find (13.80 vs 18.60) and Retr.KV (0.00 vs 2.20); Table 6 Thought-of-Mind 0.5k at 8192 (H2O 38.0 vs 32.5) | Reword the abstract/appendix statements to the cells actually won |
| DA-M6 | Logic (formulation) | Eq. (1); Eq. (3); §4.1 | Question: read literally, α_ti = 0 inside exp does not remove a token (weight exp(0) = 1); the soft form drives logits, not weights, to 0. The text in §4.1 suggests a different intended form; extraction may have dropped parentheses (unverifiable here) | State the exact attention form and how masking is implemented in training |
| DA-M7 | Efficiency claim | Appendix A.2; Table 5 | "even faster than SnapKV" holds in 2 of 3 rows (130.48 vs 124.67; 279.90 vs 244.60) but not at 16K, batch 4 (151.04 vs 153.21); single runs; training cost not counted | Add error bars, R-KV/H2O timing, peak memory |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §1 vs Appendix A.1 | Recency preference vs "no extra recency bias" |
| DA-m2 | Consistency | Table 8 | Full-KV `lcc` 33.35 equals `gov_report` 33.35; recompute Δ |
| DA-m3 | Evaluation | Appendix B.2 | LongMemEval judged by Qwen3-4B-Instruct (same family as the model under test); no agreement check with the benchmark's reference judge |
| DA-m4 | Overclaim | §1; §4.2 | "globally optimal caching policy" |
| DA-m5 | Generalization | Appendix B.2 / B.4 | Different gate sets per task family; the "one set of gates" implication is not tested |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| LongBench Avg Δ TRIM-KV (Table 8) | −0.64% | −0.63% (mean of 15 per-task relative changes) | Yes (rounding) |
| LongBench Avg Δ LocRet (Table 8) | −4.82% | −4.82% | Yes |
| LongBench-V2 gain (Table 9) | +6.56% | 30.68/28.79 − 1 = +6.56% (absolute +1.89) | Yes; absolute gain small |
| Throughput vs full cache (Table 5, 32K, batch 4) | "∼ 2×" | 130.48/68.44 = 1.91× | Approximately |
| Throughput vs SnapKV, 16K batch 4 | "even faster than SnapKV" | 151.04 vs 153.21 | No (slower in this row) |
| LongMemEval overall, TRIM-KV 32768 (Table 7) | 48.2 | 47.98 from per-type accuracies (other rows reproduce to ±0.03) | Off by 0.22 |
| Budget fraction (Table 3) | "just 25% of the KV budget" | 32768/131072 = 25% | Yes; accuracy 48.2 vs 49.4 |
| AIME24 gain over Full KV (Table 4) | 74.0 vs 65.5 | +8.5 points | Yes (single run) |
| "58.4%", "198%" | §5.1.1 | Figure 3 not visible | Unverifiable |

## Ignored Alternative Explanations
- Gains from a learned per-head window/sink pattern rather than from "intrinsic importance".
- Full-cache baseline hurt by length caps, repetition loops or template mismatch; TRIM-KV shortening outputs.
- Baselines under-tuned for budgets of 128–1024 on long reasoning traces (settings not given).
- Overlap between gate-training corpora (SynthLong, BookSum, Buddhi) and RULER/InfiniteBench-derived SCBench and LongMemEval content (no contamination analysis).
- Heavier-tailed variance than assumed on 30-problem AIME24.

## Missing Stakeholder Perspectives
Operators of multi-turn assistants (silent loss of system or safety instructions under eviction); practitioners who must retrain gates per model and per domain; interpretability researchers who would need causal evidence before using retention scores as head diagnostics.

## Observations (Non-Defects)
The method is simple, cheap to train and compatible with fused kernels; the objective ablation is informative (Table 4); reporting the failure on retrieval-heavy SCBench tasks and the LongBench discrepancy is honest; the paper includes the LocRet comparison with matched data (Appendix B.3), which is more than most.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 54 | Mechanism unisolated; formulation question; mismatch |
| Clarity & Presentation | 66 | Clear overall |
| Novelty & Originality | 56 | Adjacent to learned scorers |
| Significance & Impact | 60 | Useful if replicated |
| Experimental Validation | 50 | No variance, undocumented baselines, untested explanations |
| Reproducibility | 58 | Steps/time/code missing |
| Ethical Compliance | 62 | Generic |

**Pool position:** better than about 56% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: strong headline results but an unisolated mechanism and untested explanations place it just above the median and below the typical accepted paper.

## Overall: 3 | Confidence: 4

---

# Phase 1.6 — Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W7 | kept; ordered by severity | Each has a location and a fix; "surpasses full cache" is not answered in the paper |
| R1 | Q: Eq. 1 literal reading | kept as a question | Extraction ambiguity: cannot be an error (Hard Rule 10) |
| R1 | ERR-2, ERR-3 | kept in the Error Log as MINOR | Medium confidence; located and recomputed |
| R2 | W1 ("learnable policies limited to prefill") | rewritten | The statement is accurate for Locret per the paper's own Appendix B.3; DMC's mechanism could not be verified from an abstract here, so the weakness now reads "cited, not differentiated/compared" |
| R2 | W2 missing baselines | kept | Verified references; not tied to recent preprints |
| R2 | W4 "newly observed" | kept | Single-example evidence confirmed (Appendix C) |
| R3 | W5 (analogy, scale) | partly moved to Minor | Ebbinghaus analogy is cosmetic; scale kept |
| R3 | Missing references | kept as lines of work | No specific papers named (citation-integrity) |
| R4 | W3 + typos | typos moved to Minor | Presentation issues proportionate |
| DA | DA-M3 | rewritten | "Not stated after sweep" → question-level MAJOR; no selection sentence exists, so criterion 3 does not apply |
| DA | DA-M6 | kept as question | Same extraction caveat |
| DA | DA-M7 | kept | Verified from Table 5 |
| DA | DA-m3 | kept | Appendix B.2 statement confirmed |

---

# Phase 2 — Editorial Decision

## Synthesizer Part A — package for the EIC

**Consensus map.** CONSENSUS-3: no variance / unreplicated headline gains (R1-W1, R4-W2 in part, DA-M2); CONSENSUS-3: overclaimed wording of "surpasses full cache/regularization/consistently" (R1-W3, R4-W1, DA-M2, DA-M5); CONSENSUS-3: query-dependence of creation-time importance and retrieval failures (R2-W3, R3-W2, DA-M4); CONSENSUS-2: undocumented/weak baseline configuration and missing adaptive-budget/learned baselines (R1-W4, R2-W2); CONSENSUS-2: train/inference mismatch and Eq. 1/3 formulation (R1-W6, R4-W3, DA-M6); CONSENSUS-2: interpretability claim from one example (R2-W4, R3-W3); SPLIT: none explicit (R3 positive on deployability, R1/DA critical on efficiency evidence); SOLO: R3-W4 safety/instruction retention; DA-M3 test-set design choices; DA-M1 trained-control confound (partly R1-W2). **DA-CRITICAL:** none. Issues the outcome may hinge on: DA-M1/R1-W2 (confound), DA-M2/R1-W3 (full-cache claims), R1-W1 (no variance), Table 6/Table 1 baseline behavior.

**Official score (BEFORE: no `eic_weight`, `da_critical: []`).** Official ratings R1 4, R2 4, R3 5, R4 4, DA 3 → mean **4.00**; official composite **63.9**; EIC assessment without weights 63.7 (rating 3.96 → 4). No consistency warnings; largest dimension spreads 16 points (Technical Rigor, Experimental Validation), below the 20-point flag.

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A simple, cheap and practical learned retention policy gives large, consistent gains over training-free eviction on long-chain-of-thought math at very small budgets (Table 1, Figure 3, Table 3), generalizes to non-math tasks, runs at roughly twice full-cache decode speed (Table 5) and comes with informative ablations (Table 4) and a matched-data comparison with the closest learned method (Appendix B.3). Its weaknesses are the ordinary ones: single runs, some overclaiming, missing baselines.
- **Against acceptance:** The central mechanism claim (intrinsic creation-time importance beats attention-based importance) is not isolated from "any trained policy" or from learned per-head windows; the "surpasses full cache / regularization" explanation is untested; there is no variance estimate; baseline settings are undocumented; and the premise visibly fails on retrieval-heavy tasks (Table 2).

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "Across tasks and budgets, TRIM-KV achieves the best performance" contradicted by Table 6 (H2O 38.0 > 32.5, ToM 0.5k at 8192) | R1 ERR-1, DA-M5 | Appendix B.1; Table 6 | Verified | Text overstated; minor |
| Table 2: TRIM-KV loses to SnapKV (Math.Find 13.80 vs 18.60) and StreamingLLM (Retr.KV 0.00 vs 2.20); collapses on Code.RepoQA (4.32 vs 53.86) vs abstract's "consistently outperforms … SCBench" | R4-W1, DA-M5, R3-W2 | Table 2; Abstract | Verified | Abstract overstated; main text itself says "competitive … across most of the evaluated tasks" |
| Full-KV 65.5 vs TRIM-KV 74.0 on AIME24 (Qwen3-4B); mechanism untested | R1-W3, DA-M2 | Table 4; Abstract | Verified (numbers); interpretation unresolved | Not an error; a claim not supported |
| Trained policy vs training-free baselines confound | R1-W2, DA-M1 | §5.1 Baselines; Appendix B.1 | Partly correct | SeerAttn-R is a trained comparator and is outperformed per §5.1.1, but its mechanism differs; no trained control exists |
| Interpretability evidence is from one example | R2-W4, R3-W3 | Appendix C; §5.1.2 | Verified | "All visualizations are from the first example in the AIME24 dataset" |
| "Learnable policies limited to prefilling" | R2-W1 | §1, §2, Appendix B.3 | Partly correct | Accurate for Locret per Appendix B.3; DMC is cited but not differentiated; mechanism not verified by me from an abstract |
| Ablations (loss, architecture, M, data) on AIME24, selection protocol not stated | DA-M3 | Table 4; Figures 8–11 | Partly correct | Ablation facts confirmed; no selection statement; headline M = 512, λ = 1.0 stated in §5.1; MAJOR (question), not criterion 3 |
| Eq. (1)/(3) literal reading | R1 Q1, DA-M6, R4-Q3 | Eq. 1; Eq. 3; §4.1 | Unverifiable | Parenthesization is ambiguous in the extracted text; §4.1 text is consistent with a multiplicative weight; remains a question |
| Intro vs Appendix A.1 on recency bias | R1 ERR-4, DA-m1 | §1; Appendix A.1 | Verified | Minor wording conflict |
| Table 8 Full-KV lcc = gov_report = 33.35 | R1 ERR-2, DA-m2 | Table 8 | Verified (identical value); cause unknown | Printed Δ recomputes from the printed values |
| Throughput "even faster than SnapKV" | DA-M7, R3-W1 | Table 5; Appendix A.2 | Partly correct | 130.48 vs 124.67 and 279.90 vs 244.60 favor TRIM-KV; 151.04 vs 153.21 does not |
| Table 7 TRIM-KV 32768 overall 48.2 vs recomputed 47.98 | R1 ERR-3, DA numerical check | Table 7 | Verified (recomputation); minor | 0.22 difference exceeds rounding |
| Baselines at budget 2048 collapse implausibly (Table 1) | R1-W4 | Table 1; Table 6 | Unverifiable | Baseline settings are not in the paper; treated as a question |

Literature check: the missing-comparison weaknesses (R2-W2) rest on **prior** (peer-reviewed or 6+ month arXiv) work (Scissorhands, Ada-KV, DuoAttention, FastGen, CriticalKV, A2SF) and are MAJOR at most; the recent preprints (LazyEviction, Cache Me If You Can, EvolKV) are "worth discussing" and did not lower any score. Closest prior work (Locret) is cited and differentiated in Appendix B.3: no criterion-7 issue, no text-overlap flag.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 4 | 4 | 1.25 | Findings largely verified (ERR-1, ERR-2, ERR-4, Table 4/Table 6 checks); concrete fixes; one unverifiable extraction question handled correctly as a question |
| R2 (Domain) | 4 | 4 | 1.0 | Sound and well calibrated; the "limited to prefill" point needed rewording (accurate for Locret) |
| R3 (Perspective) | 5 | 3 | 0.75 | Rating leans on the interpretability/emergent-heuristics value, which I verified rests on one example (Appendix C); several suggestions generic; not penalized for being the positive reviewer |
| R4 (Generalist) | 4 | 4 | 1.0 | Typical well-calibrated review; abstract-overclaim finding verified |
| DA | 3 | 4 | 1.0 | Strong counter-argument partly verified (no trained control; untested regularization); no CRITICAL inflation; DA-M3 correctly stated as a question |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | n/a: the DA wrote "No CRITICAL issues found." I concur: no leakage statement exists (protocol sweep found no selection-on-test sentence), no result contradicts the main claim, and each MAJOR item is fixable by narrowing claims or adding a control | n/a |

### Final Decision and Justification
The official mean is 4.00 and the EIC-weighted rating is 3.92, giving the starting point **4 (Borderline Accept)**; the composite cross-check agrees (official 63.9, EIC-weighted 63.3, both band 4), so no flagged disagreement exists. I keep the starting point. I considered going up on the strength of the consistent small-budget gains and down on the missing control and variance, and found no verified, named issue that the ratings had not already accounted for: the two accept-leaning ratings (R3 at 5, weighted 0.75) rest partly on interpretability evidence I verified to be single-example, which is why R3's weight is reduced, while the lower ratings (R1, DA) rest on verified points (no variance, untested regularization explanation, no trained control) that the authors can address with narrower claims and one or two controls. These weaknesses (single runs, overclaimed wording, some missing baselines) are typical of papers accepted at ICLR, and the practical contribution is solid. **My pool position: better than about 70% of ICLR submissions** (accepted share ≈ 27%): at the low end of a typical accepted paper; the deciding evidence is the large, consistent math-reasoning gains with ablations and a matched-data learned-baseline comparison, against the unisolated mechanism. No DA ceiling applies. **Final Overall: 4 (ICLR: rating 6 on the {0,2,4,6,8,10} scale; Soundness 2, Presentation 3, Contribution 3, scale status secondary).**

## Synthesizer Part B — Score Summary (script output, run with the EIC weights and `--final 4`)

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 62 | 64 | 70 | 68 | 54 | 63.6 | 63.0 | 16 |
| Clarity & Presentation | 66 | 68 | 74 | 72 | 66 | 69.2 | 68.7 | 8 |
| Novelty & Originality | 60 | 58 | 68 | 62 | 56 | 60.8 | 60.2 | 12 |
| Significance & Impact | 66 | 68 | 74 | 68 | 60 | 67.2 | 66.6 | 14 |
| Experimental Validation | 58 | 62 | 66 | 64 | 50 | 60.0 | 59.4 | 16 |
| Reproducibility | 62 | 66 | 70 | 68 | 58 | 64.8 | 64.2 | 12 |
| Ethical Compliance | 66 | 66 | 68 | 66 | 62 | 65.6 | 65.4 | 6 |
| **Composite** | 62.3 | 64.1 | 69.7 | 66.5 | 56.8 | **63.9 (before)** | **63.3 (after)** | |
| Pool position (P%) | 66 | 68 | 77 | 72 | 56 | | EIC: 70 | |

EIC weights: R1 1.25, R2 1.0, R3 0.75, R4 1.0, DA 1.0 (shares of the EIC assessment 26% / 20% / 13% / 20% / 20%). Official rating 4.00; EIC-weighted rating 3.92.

### Target-Venue Scores (ICLR 2026, scale status: secondary; labels from the script, not official wording)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 3 / 3 |
| Rating (final Overall 4) | 6 on {0,2,4,6,8,10} (6 on the earlier {1,3,5,6,8,10} scale) |

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs" to ICLR. The paper addresses a timely problem: keeping KV caches bounded during long reasoning and long-context generation.

**Overall Assessment:** The panel found a simple, practical idea with consistent gains over heuristic eviction at small budgets and several well-chosen ablations. The concerns concentrate on isolating why it works, on statistical evidence, and on claims stated more strongly than the tables allow. As a simulation, this is how a careful panel would likely see this draft, not a prediction of any real outcome.

**Key Strengths Identified by Reviewers:**
1. Large, consistent small-budget gains on long chain-of-thought math and procedural generation, with six base models (R1, R4, R3).
2. A clean, cheap, kernel-compatible design with measured decode speed-ups (R3, R4).
3. Informative objective ablations and an honest matched-data comparison with the closest learned baseline (R1, R2).

**Key Concerns Requiring Attention:**
1. No variance or uncertainty; "surpasses the full cache" and "regularization" rest on single runs and an untested explanation, with the full-cache reference not specified (CONSENSUS-3: R1, R4, DA).
2. The mechanism is not isolated from a generic trained policy (no trained control; Locret-style learner and adaptive-budget baselines absent from the main comparison) (R1, R2, DA).
3. Abstract and appendix statements exceed the evidence ("consistently outperforms … SCBench", "best across tasks and budgets"); creation-time importance fails on retrieval-dominated tasks (Table 2) (CONSENSUS-3: R2, R3, R4, DA).

**Decision: Borderline Accept (4).** The practical contribution is real and the weaknesses are of the kind that accepted papers carry; what tipped the balance is that each is fixable with narrower wording and a small number of controls. Please see the Revision Roadmap.

Sincerely,
Dr. Tamsin Veldkamp
Editor-in-Chief (meta-reviewer; fictional persona)

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No variance/uncertainty; unreplicated headline gains | R1, R4, DA | CONSENSUS-3 |
| Overclaimed wording ("surpasses full cache/regularization", "consistently", "best across tasks and budgets") | R1, R4, DA (R2 on "newly observed") | CONSENSUS-3 |
| Creation-time importance cannot handle query-dependent relevance (Table 2) | R2, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Strength of the efficiency evidence | R3 (deployable, ~2×) | R1, DA (single GPU, one row slower than SnapKV, no peak memory) | Both partly right: ~1.9× over full cache is verified; "faster than SnapKV" is mixed; peak memory is unreported |
| Value of the interpretability result | R3 (attractive by-product) | R2, DA (single example, no causal test) | Verified single-example evidence; counted as a bonus, not as support for the rating |

### Score Spread Discussion
No dimension exceeds the 20-point flag. The 16-point spreads on Technical Rigor and Experimental Validation come from DA (54 / 50) vs R3 (70 / 66). The editor adopts the middle: the DA's concerns are verified in part (no control, no variance), R3's confidence is lowest.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Trained policy vs training-free baselines; no control | Yes (R1-W2) | n/a | New experiments (small) |
| DA-M2 | MAJOR | "Surpasses full cache / regularization" untested | Yes (R1-W3, R4-W1) | n/a | Analysis of existing runs plus a small control |
| DA-M3 | MAJOR | Design choices ablated on AIME24; selection protocol not stated | No | n/a (question) | Clarification plus a held-out check |
| DA-M4 | MAJOR | Premise tested where it fails (Table 2) | Yes (R2-W3, R3-W2) | n/a | Narrow the claim; oracle/query-aware control |
| DA-M5 | MAJOR | Claim distortion in abstract/appendix | Yes (R4-W1, R1 ERR-1) | n/a | Rewording |
| DA-M6 | MAJOR (question) | Eq. 1/3 literal reading | Yes (R1 Q1, R4-Q3) | n/a | Clarification |
| DA-M7 | MAJOR | Efficiency claim mixed | Yes (R3-W1) | n/a | Small additional measurements |

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No upheld DA-CRITICAL issues. The items below are verified issues that touch a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | No variance/uncertainty for headline comparisons; "surpasses full cache" rests on single runs | R1-W1, DA-M2, R4-W2 | Table 4; Table 9; Figure 3; Table 7 | 3 gate-training seeds for Qwen3-4B on AIME24 at 2 budgets; paired bootstrap over problems; absolute-number table for headline gains | Medium (≈ 3× gate-training run plus ~10 GPU-h evaluation per budget) | Partly (bootstrap yes; seeds if the gate run is short) |
| P1-2 | Mechanism not isolated from a trained policy; learned-scorer and adaptive-budget baselines missing from the main comparison | R1-W2, R2-W1, R2-W2, DA-M1 | §5.1; Appendix B.3; Figure 8 | Add a trained learned-window/sink control (same loss and data) and a Locret-style / Ada-KV-style baseline on Qwen3-4B AIME24 and LongProc; report gate-training cost | High (≈ 1–2 gate runs plus evaluation; tens of GPU-hours) | Partly |
| P1-3 | Full-cache claims unsupported: reference configuration, truncation, whether eviction triggers, regularization explanation | R1-W3, DA-M2, R4-Q2 | Table 4; Table 6; Abstract; §5.1.1 | Report generation caps, length distributions, truncation/loop rates, context length per LongProc tier; test or soften the regularization claim | Low–Medium (analysis of existing runs) | Yes |
| P1-4 | Abstract and appendix claims exceed the tables | R4-W1, DA-M5, R1 ERR-1 | Abstract; §5.1.1; Appendix B.1 / Table 6; Table 2 | Reword to the cells actually won; define "198%" and "58.4%" and provide the table | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Baseline settings undocumented; sanity check at budget ≥ length | R1-W4 | Appendix table of settings and sources; equality-with-Full-KV check | Low | Yes |
| S2 | Selection protocol for design choices ablated on AIME24 | DA-M3, R1 Q5 | State protocol; confirm the headline config on a held-out benchmark | Low–Medium | Yes |
| S3 | Eq. 1/3 formulation, train/inference mismatch, "globally optimal" | R1-W6, R2-W3, R4-W3, DA-M6 | State exact attention form; fidelity-vs-budget analysis; length-extrapolation test; drop "globally optimal" | Medium | Partly |
| S4 | Peak memory, prefill protocol, throughput error bars and extra baselines | R3-W1, DA-M7 | Report peak GPU memory; add R-KV/H2O timing | Low–Medium | Yes |
| S5 | Query-dependence limit and "incompressible" assertion | R2-W3, R3-W2, DA-M4 | Oracle-retention or query-aware reference on one SCBench retrieval task | Medium | Partly |
| S6 | Missing references: Scissorhands, Ada-KV, DuoAttention, FastGen (Important); CriticalKV, A2SF (Helpful); discuss LazyEviction and related recent preprints | R2 | Cite and differentiate | Low | Yes |
| S7 | Table 8 `lcc` and Table 7 value checks | R1 ERR-2, ERR-3 | Verify and correct | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Interpretability claim from one example | R2-W4, R3-W3 | Aggregate statistics over many prompts; one causal head intervention |
| N2 | Safety / instruction retention under eviction | R3-W4 | Probe system-prompt token survival in multi-turn runs |
| N3 | Scale and architecture coverage; Ebbinghaus analogy | R3-W5 | One larger or different-family model; tone down the analogy |
| N4 | LongMemEval judge is the same model family; contamination analysis of gate-training corpora | DA-m3, DA | Agreement check with the benchmark's reference judge; overlap analysis |
| N5 | Typos and presentation | R4, R1 | "Patero", "Lllam", Table 5 lengths, §5.2 grammar, A.1 recency sentence |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 1–2 weeks (seeds plus controls dominate; ≈ 50–150 GPU-hours depending on gate-training cost, which the paper does not report)
- Priority 2: 7 items, roughly 3–5 days
- Priority 3: 5 items, optional; N1 about 2 days
- **Total estimated revision time**: about 2–3 weeks; a rebuttal window can cover P1-3, P1-4, S1, S2, S4, S6, S7 and part of P1-1.

*A Post-Review Analysis (Gap Scout) and Phase 2.5 coaching were not requested and were not run.*
