# Simulated Peer Review: Adamas (ICLR, full mode)

Date: 2026-11-10. Request: "Review this paper. Target venue: ICLR. Full review, skip confirmation, literature check: strict, cutoff date 2025-09-24."
This is a simulation of how a careful panel would likely see this draft, not a prediction of any outcome. All five reviewer passes and the EIC pass were run sequentially by one model in one context (no subagents), so they share a model context. Figures were not available: every judgment about Figures 1, 3, 4, 5 and 6 rests on captions, text and the appendix tables (Tables 6 and 7), which carry the data behind Figures 3 and 6.

**Literature check status (Phase 1.5):** attempted in `strict` mode with cutoff 2025-09-24. The arXiv API returned HTTP 429 and 503 on three of four search attempts, one call timed out, and one `verify` call timed out. No result was kept, so no `novelty`, `similarity`, `scout` or `coverage` output exists. Per the skill's fallback, the literature check is treated as **off**. Recommended references come from knowledge and are all marked `[verify]`. No claim below is labelled "known" from a search. Search queries used concept words only; the paper itself was never searched for.

**Integrity scan (Phase 0):** `integrity_scan.py` found no reviewer-directed text or hidden characters. The reviewers' copy was identical to the paper text.

---

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Adamas: Hadamard Sparse Attention for Efficient Long-context Inference |
| Primary Discipline | ML → efficient LLM inference → training-free sparse attention / KV selection for decoding |
| Secondary Discipline(s) | GPU kernel engineering; quantization (Hadamard rotation, low-bit codes); approximate nearest-neighbour search |
| Paper Type | Empirical (method + benchmarks, with a kernel/latency component) (composite weights: empirical) |
| Core Technique(s) | Hadamard transform of Q and K, 3-threshold bucketization to 2-bit codes, Manhattan-distance scoring on packed codes, top-k token selection, fused CUDA kernels |
| Target Venue | ICLR 2026 (stated by the user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none. Reviews are public; authors may upload a revised PDF during discussion |
| Paper Maturity | Submission-ready |
| Ethics-Relevant Content | none (no human data, no deployment-risk content) |

### Claimed Contributions (as stated by the authors, §1)
1. **C1**: A sparse-attention mechanism combining Hadamard transform, bucketization, 2-bit compression and a Manhattan-distance estimator, "achieving 8× higher sparsity than prior SOTA methods while preserving comparable accuracy with full attention" at a 128-token budget (abstract: matches full attention at 64, near-lossless at 128; PPL "comparable or even lower" than full attention).
2. **C2**: High-performance GPU kernels giving up to 4.4× self-attention and 1.5× end-to-end speedups over full attention at 32K.
3. **C3**: Ablations show every component (Hadamard, bucketization, compression, estimation) contributes.

### Paper memory (shared with all reviewers)
- **Setup facts.** Models: LongChat-v1.5-7b-32k (most experiments) and Yarn-Llama-2-7b-128k (100K passkey) (§4.1). Tasks: PG19 PPL at 32K, passkey at 10K and 100K, six LongBench datasets (§4.1). Baselines: StreamingLLM and Quest only (§4.1). Efficiency: one RTX A6000, FlashInfer dense baseline (§4.3). Budgets: 16–512 (passkey 10K), 64–4096 (passkey 100K, LongBench), 256–2048 (PPL, Figure 4).
- **Not stated after a protocol sweep** (searched for test/validation/tuned/selected/hyperparameter/seed/batch): bucketization thresholds B1–B3 (only the Figure 2 illustration uses [-10, 0, 10]); how thresholds were chosen or whether they differ per layer, head or for Q vs K; Quest page size; whether the first layers or an attention-sink/local window are always dense and whether they count toward the budget; batch size in Table 2; decoding settings and number of passkey trials; hardware for accuracy runs; whether baselines were rerun or copied; any tuning split (no tuning is described, so no test-set selection is claimed or evident).
- **Headline numbers and sources.** 64-token budget "matches" full attention (abstract; Table 1a, Table 6); 8× sparsity (abstract, §1; Table 6); 4.4× self-attention (Figure 5, §4.3); 1.5× end-to-end (Table 2); PPL ≥2× better than prior SOTA (§1; Figure 1: 15.3 vs 7.09).
- **Appendix.** A: analytical FLOPs and memory-access tables for full attention, Quest, Adamas (Tables 3–5). B: Table 6, LongBench numbers behind Figure 3. C: Table 7, ablation numbers behind Figure 6. No limitations section, no extra protocol details.
- **Unverifiable:** all figure content (Figures 1, 3–6), including per-component speedup labels in Figure 5.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Solheim-Marek, public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / ML systems, efficient Transformers, area chair at major ML venues
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Cares whether a headline claim survives a close read of the tables; calibrated to what ICLR accepts

### Reviewer 1 (Methodology): Dr. Anselm Vorster, industrial research lab (Western Europe)
- **Seniority / Expertise**: Senior industry scientist / LLM inference kernels, latency measurement, long-context evaluation protocols
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes tables; insists on matched budgets and measured latency

### Reviewer 2 (Domain): Prof. Priyanka Valsan, public university (South Asia)
- **Seniority / Expertise**: Mid-career faculty / KV-cache compression and sparse attention, long-context benchmarks
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work against the bibliography entries

### Reviewer 3 (Perspective): Dr. Camila Ordoñez-Pruitt, national research laboratory (North America)
- **Seniority / Expertise**: Research scientist / hardware-aware algorithms, approximate nearest-neighbour search, signal processing
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for what the idea could become

### Reviewer 4 (Generalist): Dr. Wei-Lin Tsao, public university (East Asia)
- **Seniority / Expertise**: Mid-career faculty / general deep learning, NLP applications
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Odalys Brenner-Achebe, university research group (Western Africa / Europe)
- **Seniority / Expertise**: Senior researcher / evaluation methodology, claim verification
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; checks every superlative against a table

*Personas are fictional. Assumptions: venue ICLR as stated; paper type empirical.*

---

# Phase 1: Reviewer Reports

---

# Peer Review Report

## Paper: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference
## Reviewer: Dr. Anselm Vorster, Methodology (industrial research lab, Western Europe; fictional persona)
## Expertise: LLM inference kernels; latency measurement; long-context evaluation
## Date: 2026-11-10

## Summary
The paper proposes a training-free method to choose which keys a decoding query attends to. Queries and keys are rotated with a Hadamard matrix, quantized to 2-bit codes with fixed thresholds, and scored by negative L1 distance on the packed codes; the top-k tokens then go through ordinary sparse attention (§3.2, Algorithm 1). On two Llama-2-based 7B models it is compared with StreamingLLM and Quest on PG19 perplexity, passkey retrieval and six LongBench tasks, and with FlashInfer dense attention for latency. The main result is that accuracy stays close to full attention at budgets of 64–128 tokens, where Quest collapses.

## Strengths
### S1: Large, consistent gains over Quest at small budgets
Table 6 shows Adamas at budget 64 averaging 37.4 across the six LongBench tasks against 6.4 for Quest, and at 128 averaging 39.1 against 19.6 (recomputed). The effect is large, spans all six tasks, and is far outside any plausible noise.
### S2: Ablation of the rotation is decisive
Table 7 shows that without the Hadamard transform the scores are near zero at small budgets (for example 0.60 on GovReport at budget 16) and recover only at 4096. This supports the intuition that raw 2-bit quantization of queries and keys is damaging.
### S3: A real kernel implementation with a component breakdown
§4.3 and Figure 5 report kernel-level latency against a strong dense baseline (FlashInfer) and Table 2 reports end-to-end decode time. Efficiency claims in this area often lack measured latency; here they are present, with hardware named.
### S4: Cheap storage overhead, checkable
§3.2 states the 2-bit codes add 1/16 to the KV cache. I verified this: 2 bits against 16-bit keys is 1/8 of K, which is 1/16 of K+V.

## Weaknesses
### W1: The headline accuracy claims are stronger than Table 1 and Table 6 support
The abstract says Adamas "matches the accuracy of full attention with only a 64-token budget". Table 6 at budget 64 shows MultifieldQA 36.60 vs 41.64 (−5.04), NarrativeQA 17.81 vs 21.23 (−3.42) and TriviaQA 78.91 vs 84.25 (−5.34); the six-task mean is 37.37 vs 39.70 (−2.33, recomputed). Table 1a at 64 gives 93% for Adamas against 99% for Quest. On the 100K model, Table 1b gives 71% at 128 and 87% at 256, so "near-lossless at 128" does not hold there; Adamas reaches 100% only at 2048, while Quest has 99% at 1024. The claims hold at 128–256 on LongBench and 10K passkey.
- **Suggested Fix**: Restate the claim as "within about 1.4% of full attention on LongBench at 128 tokens", add a full-attention row to Table 1, and report the 100K result as a limitation (wording change plus one extra table row).
### W2: No test of the central mechanism (recall of true top-k) and an unmotivated estimator
§1 argues prior methods suffer "low recall", and §3.1 argues the Hadamard transform preserves similarity via Eq. 3. But Eq. 3 holds only before bucketization; the actual score is −‖Ĥ_Q − Ĥ_K‖₁ on 3-threshold codes (Eq. 6), which is not monotone in q·k (it ignores key norm and treats dimensions as ordinal). The paper never measures recall or attention-mass coverage against exact top-k, and never runs the obvious alternative of an inner-product score on the same codes. Table 7 also shows L2 ≈ L1, so "Manhattan" is not itself shown to matter.
- **Suggested Fix**: Report top-k recall and softmax-mass coverage versus an exact-score oracle at each budget, and add an "oracle top-k" and a "quantized inner product" row to Table 7 (about 5 GPU-hours on LongChat-7B, rebuttal-feasible).
### W3: The ablation of the Hadamard transform may be confounded by threshold choice
The thresholds B1–B3 are never stated (§3.2, Eq. 5; Figure 2 uses [-10, 0, 10] only as an illustration). If the same fixed thresholds are applied to raw Q and K in "w/o Hadamard", the collapse in Table 7 may reflect scale mismatch and outlier channels, not the value of rotation. The text's conclusion that the model "fails to generate accurate answers without the Hadamard transform" (§4.4) is therefore not isolated.
- **Suggested Fix**: State how B1–B3 are set (fixed, per-layer calibrated, quantile-based?) and add a "no Hadamard, per-channel or quantile thresholds" variant.
### W4: Efficiency comparison omits the main baseline and leaves the setting underspecified
Figure 5 and Table 2 compare only with dense attention. Quest is never timed, although Table 4 and Table 5 imply Adamas's selection stage costs at least as much as Quest's: with Quest page size 16 (assumed, not stated), Quest's selection is about 0.26·s·bh FLOPs against about 3.25·s·bh for Adamas (derived from Table 4 at k=256, d=128), with equal read volume (Table 5). Batch size is not stated for Table 2, the caption's unit "us" cannot be right for end-to-end decoding of a 7B model, and speed is measured only up to 32K although accuracy is claimed at 100K (the 100K KV cache of this MHA model would not fit a 48 GB A6000, so no 100K latency is possible on this hardware). Prefill cost of rotating and packing all prompt keys is not reported.
- **Suggested Fix**: Time Quest with its public kernels under identical hardware/batch settings, state batch size and units, and report prefill overhead (about 1 GPU-day).
### W5: Narrow experimental scope for an ICLR claim of general superiority
Two baselines (StreamingLLM, Quest), two 2023-era MHA Llama-2 models, six LongBench tasks and a synthetic retrieval task. "Adamas consistently surpasses these prior SOTA methods across all datasets" (§4.2) is also contradicted at large budgets: from Table 6, Quest's six-task mean is 40.81 at 2048 and 40.34 at 4096, above Adamas (39.58 and 39.52) and above full attention (39.70).
- **Suggested Fix**: Add a GQA model (Llama-3.1-8B-class or Qwen-class), RULER or a multi-needle retrieval test, and token-level baselines (see R2's list). Qualify "consistently" to the low-budget regime.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5/E1 | Abstract vs Table 6, Table 1a | "matches the accuracy of full attention with only a 64-token budget" | Table 6 (64): Multifield −5.04, NarrativeQA −3.42, TriviaQA −5.34; mean 37.37 vs 39.70; Table 1a: 93% | Recomputed from Table 6 | High | MAJOR | Narrow claim |
| ERR-2 | E1 | §4.4 vs Table 7 | "remains below the baseline" | Table 7 Qasper "w/o Hadamard" is 31.08 at 2048 and 30.14 at 4096, above Adamas (29.26, 28.65) and full attention (28.89) | Cross-referenced Table 7 | High | MINOR | Say "on most tasks" |
| ERR-3 | E1/E6 | Table 2 caption | "End-to-end decoding latency (us)" | 26–54 µs per token is impossible for a 7B model; values fit milliseconds | Plausibility (memory-bandwidth bound ≈ 17 ms for 13 GB weights at 768 GB/s) | Medium | MINOR | Correct unit |
| ERR-4 | E6 | Figure 1 vs Table 1 | StreamingLLM "Acc:30%" (Figure 1 labels, extracted text) | Table 1 gives StreamingLLM ≤5% (10K) and ≤4% (100K) at every budget; Figure 1's task, length and budget are not defined | Cross-referenced | Medium | MINOR | State the setting |
| ERR-5 | E2 | Table 4 vs §2 | "Hadamard transform 2bh" | §2 gives O(d log2 d) per vector; for d=128 an FWHT costs about 7 adds per element per tensor, so about 14bh for Q and K, not 2bh. Dense-matrix cost would be 2bhd | Derived from §2 | Medium | MINOR | Correct entry |

### Minor
Typos ("SparseAttenion", "Bucketizaion", "dynamical"); Figure 3 axis reads "F1 score" for GovReport although LongBench scores summarization with ROUGE-type metrics (unverifiable from text); Table 1 lacks a full-attention row.

## Missing References
Deferred to Reviewer 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Large low-budget gains, but headline claims overstate, no recall analysis, partial ablation controls |
| Clarity | 3 | Short, readable paper; setup details missing |
| Significance | 2 | Useful, but practical benefit of extreme sparsity is small in the paper's own Table 2 |
| Originality | 2 | Recombination of known pieces with one non-obvious ingredient (rotation before coarse codes) |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: only one real baseline and two old models back a "prior SOTA" claim; the abstract's 64-token claim is contradicted by Table 6 and Table 1a.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Estimator not tied to q·k; no recall measurement; threshold confound |
| Clarity & Presentation | 62 | Competent | Clear exposition; key settings unstated |
| Novelty & Originality | 50 | Developing | Engineering-leaning recombination |
| Significance & Impact | 52 | Developing | Real but narrow practical gain |
| Experimental Validation | 46 | Developing | Two baselines, two models, no variance, no oracle |
| Reproducibility | 52 | Developing | Code stated available; thresholds, page size, layers, batch size missing |
| Ethical Compliance | 60 | Competent | Nothing at stake; no limitations discussion |

## Questions for Authors
1. What are B1–B3 and how were they set (per layer/head, Q vs K)? If they were calibrated on LongBench or passkey data, my score would drop; if fixed and data-independent, it would rise.
2. Does the 64/128/256 budget include dense layers, the attention sink and a local window for all methods identically? A different convention for Quest or StreamingLLM would change the comparison.
3. In Figure 5, are ×3.0, ×3.6 and ×4.4 per-stage speedups, and is the "4.4× self-attention" claim the total of all three stages? From the text alone this is ambiguous.
4. At 32K, Table 2 shows an 18.8 ms saving (53.7 → 34.9), which equals about 35% of the dense time; with a 4.4× attention speedup this implies attention is about 45% of decode time at 32K, not the stated 30–40% (§4.3). Which is right, and which length does 30–40% refer to?
5. What is Quest's latency in your kernels, and what are its LongBench scores at page size 4 or 8?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. There is no limitations discussion: the 100K passkey weakness, MHA-only models, decode-only speedup, and no capacity saving (full KV cache retained, plus 1/16) are not mentioned.

## Ethics Review Flag
**No**: nothing at stake.

## Overall Score
**3**: Borderline Reject. Strong low-budget numbers against one baseline, but headline claims overreach and the mechanism and efficiency comparison are untested against the right alternatives.

## Confidence
**4**: Tables recomputed; figures unavailable.

---

# Peer Review Report

## Paper: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference
## Reviewer: Prof. Priyanka Valsan, Domain (public university, South Asia; fictional persona)
## Expertise: KV-cache compression; sparse attention; long-context benchmarks
## Date: 2026-11-10

## Summary
Adamas is positioned as a token-level, training-free alternative to page-level selection (Quest) and static patterns (StreamingLLM). Its distinguishing idea is to compress rotated queries and keys into 2-bit codes and select by L1 distance. The authors claim up to 8× higher sparsity than prior SOTA at comparable accuracy and kernel speedups at 32K.

## Strengths
### S1: A clear, well-targeted gap versus page-level selection
§1 and Figure 1 identify that page granularity wastes budget on unrelated tokens, and Table 6 shows the failure of Quest below 512 tokens. The motivation matches the data.
### S2: Sensible reuse of an idea from quantization
Using a Hadamard rotation to flatten outliers before coarse quantization (citing QuaRot, §1, §3.1) is a transferable and well-motivated import; Table 7 shows it is necessary in this pipeline.
### S3: Honest ablation across bit width and metric
Table 7 reports 1/2/3-bit and L1/L2 variants, which shows diminishing returns beyond 2 bits.

## Weaknesses
### W1: "Prior SOTA" is represented by one method; the closest token-level methods are absent
Related work (§5) places all dynamic methods in Quest, MInference, FlexPrefill and SeerAttention, and the experiments use only Quest. Training-free token-level selection from approximate scores is an established family: channel- or low-rank-based scoring (SparQ Attention, Loki, Double Sparsity), hashing/LSH-based selection (MagicPIG), compressed-key retrieval (ShadowKV), and offloading-oriented selection (InfiniGen). These are the natural comparisons for "token-level, training-free, high sparsity", and "8× higher sparsity than prior SOTA" is not established without them. (All `[verify]`, see list below; from my knowledge they are published at ICML 2024, NeurIPS 2024, ICLR 2025, ICML 2025 and OSDI 2024, i.e. before the cutoff.)
- **Suggested Fix**: Compare against at least two of these at matched budgets, or restrict the claim to "versus Quest".
### W2: Two related-work descriptions and one bibliography entry look wrong
(a) §5 says the Mixture-of-Attention method "MOA (Wang et al., 2024a)" profiles heads "across layers to adjust the window span", but the bibliography entry for Wang et al., 2024a is "Mixture-of-attention for subject-context disentanglement in personalized image generation" (SIGGRAPH Asia 2024), an image-generation paper. The intended LLM method appears to be a different paper (MoA: Mixture of Sparse Attention for Automatic LLM Compression `[verify]`). High confidence on the mismatch, because both texts are in the paper. (b) §5 groups "H2O (Zhang et al., 2023) and infLLM (Xiao et al., 2024)" under "the sliding window pattern"; from the titles in the bibliography, H2O is heavy-hitter-based eviction and InfLLM is a context-memory retrieval method, which are score- or retrieval-based and not static windows. Medium confidence: I could not check the abstracts (literature check unavailable). (c) The related-work taxonomy omits KV quantization (e.g., KIVI), the closest relative of 2-bit key storage.
- **Suggested Fix**: Correct the Wang et al. entry, re-describe H2O and InfLLM after checking their abstracts, and add a KV-quantization paragraph.
### W3: Novelty is mostly in the combination, and the one component named as a contribution is not shown to matter
The rotation comes from QuaRot/Hadamard-quantization work; low-bit codes for approximate scoring are established; token-level top-k is not new. The contribution framed as "Manhattan-distance estimator" is shown to be interchangeable with L2 in Table 7 (differences of 0–3 F1 in both directions across tasks). The explanation offered ("L2 distance emphasizes global geometric consistency", §4.4) is conjecture. Novelty is therefore: rotation + coarse codes for token retrieval, a modest but real engineering-flavoured advance.
- **Suggested Fix**: Add a novelty-delta paragraph against SparQ/Loki/ShadowKV and frame the contribution as "rotation makes 1–2 bit retrieval codes viable", with the L1 choice presented as a design option.
### W4: Theoretical framing overstates what Eq. 3 gives
§3.1 says the transform "does not incur any information loss", which is true of the orthogonal map and false of the pipeline after Eq. 5 and Eq. 6. The paper provides no bound on ranking error under bucketization.
- **Suggested Fix**: Restrict the statement to the transform, and add either a simple distortion argument (random rotation makes coordinates near-Gaussian, so fixed thresholds are well-matched) or empirical rank-correlation plots.

## Missing References
*No literature check output exists (arXiv unreachable); all entries are from memory and marked `[verify]`.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Ribar et al., "SparQ Attention: Bandwidth-Efficient LLM Inference", ICML 2024 `[verify]` | Training-free token-level selection from approximate scores |
| Critical | Singhania et al., "Loki: Low-rank Keys for Efficient Sparse Attention", NeurIPS 2024 `[verify]` | Approximate key scoring for top-k token selection |
| Critical | Yang et al., "Post-Training Sparse Attention with Double Sparsity", 2024 `[verify]` | Token-level selection with channel-sparse approximate scores |
| Critical | Chen et al., "MagicPIG: LSH Sampling for Efficient LLM Generation", ICLR 2025 `[verify]` | Hash-based approximate retrieval; closest to compact binary codes |
| Critical | Sun et al., "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference", ICML 2025 `[verify]` | Compressed-key selection with measured throughput |
| Important | Lee et al., "InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management", OSDI 2024 `[verify]` | Dynamic token selection by approximate scores |
| Important | Liu et al., "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache", ICML 2024 `[verify]` | 2-bit key storage; contrast quantization for storage vs for scoring |
| Important | Li et al., "SnapKV: LLM Knows What You are Looking for Before Generation", NeurIPS 2024 `[verify]` | Widely used KV selection baseline |
| Important | Fu et al., "MoA: Mixture of Sparse Attention for Automatic Large Language Model Compression", 2024 `[verify]` | Likely the intended "MOA" in §5 |
| Helpful | Ailon and Chazelle, "Approximate nearest neighbors and the fast Johnson–Lindenstrauss transform", STOC 2006 `[verify]` | Hadamard-based randomized embeddings for fast distance estimation |
| Helpful | Jégou, Douze and Schmid, "Product quantization for nearest neighbor search", TPAMI 2011 `[verify]` | Compact-code distance estimation; ties the method to ANN search |

### Novelty delta table (from the paper's own related work and knowledge; `[verify]`)
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 token-level selection with compact codes | Quest (cited); Loki/SparQ/MagicPIG `[verify]` | Dynamic selection from approximate scores (page-level in Quest, token-level in the others) | Rotation + 2-bit L1 codes as the scoring channel | Quest yes; others not cited |
| Hadamard to tame outliers | QuaRot (cited) | Rotation before 4-bit quantization of weights/activations/KV | Applied to Q and K for retrieval, not for storage | Yes |
| C2 kernels | FlashInfer (cited), Quest kernels | Fused sparse attention kernels | Packed-code L1 kernel | Partly |

### Per-claim novelty (no search output; judgement only)
C1 method: medium (incremental recombination); C2 resource/kernel: medium; C3 ablation: not a novelty claim. "No close prior work found" cannot be stated since no search ran.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in baselines and in mechanism evidence |
| Clarity | 3 | Clear writing; a wrong bibliography entry and mis-grouped related work |
| Significance | 2 | Useful in the low-budget regime only |
| Originality | 2 | Incremental recombination |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: only one dynamic baseline, uncited token-level relatives, incremental novelty. Field snapshot (from knowledge, no search): training-free decode-time sparse attention is crowded; a significant contribution now is a clear gain over several token-level baselines on modern GQA models with measured end-to-end latency.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Mechanism untested; theory over-read |
| Clarity & Presentation | 62 | Competent | Clear, minor citation errors |
| Novelty & Originality | 46 | Developing | Recombination of known pieces |
| Significance & Impact | 52 | Developing | Narrow regime of benefit |
| Experimental Validation | 48 | Developing | One baseline, two old models |
| Reproducibility | 55 | Competent | Code stated available; details missing |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. How does Adamas compare, at equal budgets, with SparQ, Loki or ShadowKV? A win would raise my novelty and significance scores; parity would lower them.
2. Which paper does "MOA (Wang et al., 2024a)" refer to?
3. Did you evaluate any model with grouped-query attention?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No (no section).

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A real but incremental idea with thin positioning against the token-level literature.

## Confidence
**3**: No literature search output was available.

---

# Peer Review Report

## Paper: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference
## Reviewer: Dr. Camila Ordoñez-Pruitt, Perspective (national research laboratory, North America; fictional persona)
## Expertise: hardware-aware algorithms; approximate nearest-neighbour search; signal processing
## Date: 2026-11-10

## Summary
The paper turns attention-key selection into a compact similarity-search problem: rotate with a Hadamard matrix to even out coordinates, quantize to a few levels, and rank by an integer distance computed with bit operations. It shows that this retrieves useful tokens at very small budgets, and ships a kernel.

## Strengths
### S1: A clean bridge to approximate nearest-neighbour search
Rotation then coarse scalar quantization then cheap integer distance is the pattern of fast-JL/sign-sketch and product-quantization pipelines; applying it to per-step key retrieval is a natural and effective transfer (§3).
### S2: Deployment-friendly design
Training-free, only 1/16 extra cache (§3.2), no change to the model, and an integer kernel. The method is easy to adopt for practitioners with memory-bandwidth-bound decoding.
### S3: Low-budget robustness
Adamas is near-lossless at 128 tokens (Abstract, Table 1) and its Table 6 curves are flat from 64 to 4096 on GovReport, which suggests retrieval quality, not tuning, is doing the work.

## Weaknesses
### W1: The assumptions behind coarse scoring are not examined
Three implicit assumptions: attention mass concentrates on few tokens at all layers and heads; coordinates after a fixed (deterministic) Hadamard matrix are well-modelled by the same thresholds for Q and K; and L1 on codes ranks like q·k. Randomized Hadamard transforms (random sign flips) are standard in the quantization and sketching literature to guard against adversarial structure; the paper uses a fixed H (Eq. 4) without comment. Layer-wise and head-wise sparsity profiles would show where the assumptions break.
- **Suggested Fix**: Report per-layer attention-mass coverage of the selected set, and test a randomized Hadamard.
### W2: Deployment evidence is limited to one GPU, batch size unstated, and decode-only
Practical long-context serving is batched, often GQA-based, and often limited by KV capacity. Adamas keeps the whole cache (plus 1/16) and gives no capacity saving; the e2e gain (Table 2: 1.16× at 8K, 1.30× at 16K, 1.54× at 32K, derived) grows with length but is measured only to 32K. Energy and prefill overhead are absent.
- **Suggested Fix**: Add a batched GQA measurement, and combine with offloading or cache-eviction to show capacity benefits.
### W3: Little guidance on when the method should not be used
A "budget" of 64–256 is only worth it if it saves latency; Table 2 shows the 256→4096 budgets differ by 10.6% in latency (34.9 → 38.6, derived), so most of the speedup is available at budgets where Quest is already competitive. A practitioner would want a quality-latency Pareto plot.
- **Suggested Fix**: Plot LongBench mean vs end-to-end latency for Adamas, Quest and dense.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good core evidence, limited scope |
| Clarity | 3 | Clear |
| Significance | 3 | Useful to practitioners |
| Originality | 2 | Transfer of known sketching ideas |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an easy-to-adopt, training-free method with large low-budget gains over its baseline.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound pipeline, mechanism lightly examined |
| Clarity & Presentation | 70 | Competent | Clear and compact |
| Novelty & Originality | 56 | Competent | Cross-field transfer, incremental |
| Significance & Impact | 66 | Competent | Practical for decode-bound serving |
| Experimental Validation | 58 | Competent | Adequate for the main claim; narrow |
| Reproducibility | 60 | Competent | Code stated available |
| Ethical Compliance | 66 | Competent | Nothing at stake |

## Questions for Authors
1. What is the e2e latency at batch sizes 8–32? A flat gain would raise my significance score; a vanishing gain would lower it.
2. Does a randomized Hadamard change results?
3. Can Adamas's codes also serve as a compressed key store to save capacity?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially, no limitations section.

## Ethics Review Flag
**No**

## Overall Score
**4**: Borderline Accept. A practical, simple, effective idea; weaknesses are typical of accepted efficiency papers.

## Confidence
**3**: Not a sparse-attention specialist.

---

# Peer Review Report

## Paper: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference
## Reviewer: Dr. Wei-Lin Tsao, Generalist (public university, East Asia; fictional persona)
## Expertise: deep learning and NLP applications
## Date: 2026-11-10

## Summary
Adamas selects, for each decoding query, the keys whose 2-bit Hadamard-rotated codes are closest in L1 distance, then attends only to them. The authors report accuracy near full attention at 64–128 tokens, large gains over Quest at small budgets, and up to 1.5× end-to-end speedup at 32K on a single GPU.

## Strengths
### S1: Clear problem and contribution statement
§1 states the gap (static patterns vs page granularity) and the three contributions; a non-specialist can follow the idea from Figure 2 and Algorithm 1.
### S2: Results are easy to read and the appendix gives the numbers
Tables 6 and 7 give the numbers behind Figures 3 and 6, which makes the claims checkable.
### S3: Appropriate venue fit
ICLR audiences care about efficient long-context inference; the work is a method paper with measured speed.

## Weaknesses
### W1: Claims in the abstract and conclusion are worded more strongly than the results
"Matches the accuracy of full attention with only a 64-token budget", "near-lossless at 128" and "perplexity even lower than full attention … surpassing prior SOTA by more than 2×" (abstract, §6) are not what Table 1, Table 6 and the Figure 1 numbers say: at 64 several tasks are 3–5 F1 below full attention, 100K passkey is 71% at 128, and in Figure 1 Adamas's PPL (7.09) is above full attention's (6.81). The ">2×" holds only against Quest in Figure 1 (15.3/7.09 = 2.16, derived) and its setting is not defined.
- **Suggested Fix**: Align each superlative with a table cell and name the setting.
### W2: Missing settings make the comparison hard to trust
Quest's page size, what the budget includes, bucketization thresholds, decoding settings and batch size are not stated (§4.1, §4.3). Figure 1's "Acc" and "PPL" numbers have no stated task or budget.
- **Suggested Fix**: Add an "Experimental details" appendix.
### W3: Scope is narrow for a general method claim
Two Llama-2 models and one long-context benchmark subset. No limitations section.
- **Suggested Fix**: Add a modern GQA model and a limitations paragraph.

**Venue criteria checklist (ICLR):** Soundness (partly: large gains, but mechanism and baselines thin); Presentation (met: clear, short); Contribution (partly: practical, incremental); Claims supported (partly: abstract overreaches); Reproducibility (partly: code stated, details missing); Significance to the community (partly: crowded sub-area).

### Minor
Typos; Figure 3 "F1" label; Table 1 lacks a full-attention row.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Overstated claims and narrow scope |
| Clarity | 3 | Clear |
| Significance | 2 | Moderate |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the gain is real, but one baseline and old models are typical of rejected efficiency submissions; the abstract overclaims.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Sound pipeline, limited validation |
| Clarity & Presentation | 68 | Competent | Clear writing |
| Novelty & Originality | 52 | Developing | Incremental |
| Significance & Impact | 56 | Competent | Moderate |
| Experimental Validation | 50 | Developing | Narrow |
| Reproducibility | 56 | Competent | Details missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. What exactly are the Figure 1 settings (task, length, budget)? Matching Table 1 would raise my confidence.
2. Can you show results on one GQA model?
3. Would you rephrase the abstract to match Table 6?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. Sound and useful, but the evidence and wording do not yet reach ICLR's bar for a general claim.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference
## Reviewer: Dr. Odalys Brenner-Achebe (university research group; fictional persona)

## Steelman
For decoding-time sparse attention, token-level selection beats page-level selection at tiny budgets, and a Hadamard rotation makes extremely coarse codes usable. Table 6 shows 64–128-token budgets matching Quest at 1024, which is an 8× reduction at equal LongBench accuracy, with a working kernel.

## Core Argument Chain
1. Page-level selection wastes budget; token-level is better (§1, Figure 1).
2. Hadamard rotation preserves q·k exactly (Eq. 3) and flattens outliers, so 2-bit codes keep enough information (§3.1).
3. L1 distance on codes ranks keys well enough to recall the critical ones (Eq. 6).
4. Therefore accuracy matches full attention at 64–128 tokens (Tables 1, 6), giving up to 8× higher sparsity than prior SOTA.
5. Sparse selection on packed codes is cheap, so kernels deliver 4.4× attention and 1.5× end-to-end speedups (Figure 5, Table 2).
∴ Adamas is a better sparse-attention mechanism than prior SOTA.

## Strongest Counter-Argument
Step 3 is never tested, and step 4's "prior SOTA" is one method. The paper's own ablation says Manhattan distance is interchangeable with L2 (Table 7), 1-bit equals 2-bit at budgets of 256 and above, and the only component that is clearly necessary is the rotation, whose ablation does not state how the thresholds were set for the no-rotation variant. So the accuracy result could be explained by something much simpler than the proposed design: "any reasonable approximate score on rotated codes picks the top tokens", which the paper never separates from the specific 2-bit L1 recipe because it has no oracle top-k, no recall measurement and no inner-product-on-codes variant. Next, the practical payoff of the headline sparsity is small in the paper's own numbers: Table 2 at 32K shows 34.9 (256) vs 35.8 (1024), so going from the budget where Quest is competitive (§4.2: "exceeds 1024") to Adamas's 128–256 saves about 0.9 of 53.7, about 1.7% of dense time. And Quest is never timed, even though Tables 4–5 imply Adamas's selection costs at least as much as Quest's (about 12× more FLOPs and equal memory reads at page size 16, assumed). So the case reduces to: accuracy is better at budgets that barely change latency, against one baseline, on two old models. The authors can answer this by adding the oracle and Quest-latency rows and narrowing "SOTA" and "8×" to the Quest comparison on LongBench.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim (Adamas retains LongBench accuracy at far smaller budgets than Quest) survives in weaker form: Table 6 supports it at 128–256, so the overstatements are narrowing fixes, not contradictions (criterion 1 requires the evidence to contradict the main claim; it supports a weaker version).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (E5) | Abstract; Table 1a; Table 6 | "Matches full attention at 64" is not supported: LongBench mean 37.37 vs 39.70 (−2.33), three tasks −3.4 to −5.3; passkey 10K at 64: 93% vs Quest 99%. At 100K, 128-token passkey is 71% (Table 1b). | Narrow to 128–256 on LongBench and 10K passkey; add full-attention row |
| DA-M2 | Logic | §3.1, Eq. 3, Eq. 6 | Exactness of Eq. 3 is invoked for a pipeline that quantizes and uses L1; "does not incur any information loss" applies only to the unquantized rotation | Restrict statement; add recall and rank-correlation evidence |
| DA-M3 | Scope | §4.1, §5 | "Prior SOTA" = Quest only; token-level training-free methods (SparQ, Loki, Double Sparsity, MagicPIG, ShadowKV; `[verify]`) absent | Add comparisons or narrow claim |
| DA-M4 | Evidence | §4.3, Figure 5, Table 2, Tables 4–5 | No Quest latency; paper's own FLOPs show Adamas selection ≈ 12.6× Quest's (derived); sparsity gain 256 vs 1024 is ≈1.7% latency | Time Quest; show quality-latency frontier |
| DA-M5 | Alternative explanation | Table 7, §4.4 | Rotation ablation confounded by thresholds; no quantized-inner-product or oracle top-k control; L1≈L2 | Add controls |
| DA-M6 | Claim distortion | Abstract, Figure 4, Figure 1 | "Even lower perplexity than full attention" appears only in Figure 4's larger budgets (not readable here); Figure 1 shows 7.09 vs 6.81 for full; ">2×" is vs Quest in one undefined setting | State setting; provide PPL table |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | §4.4 vs Table 7 | "remains below the baseline" is false for Qasper (30.14 at 4096 vs 28.89 full) |
| DA-m2 | Evidence | §4.4 | "most memory-efficient choice" is wrong: 1-bit is smaller and matches 2-bit at budgets ≥256 |
| DA-m3 | Evidence | Table 2 | Unit "us" implausible |
| DA-m4 | Citation | §5, References | Wang et al., 2024a is an image-generation paper; H2O/InfLLM mis-grouped (verify) |
| DA-m5 | Evidence | Table 4 | "Hadamard transform 2bh" inconsistent with §2 |
| DA-m6 | Statistics | Tables 1, 6, 7 | No variance, trials, or bootstrap CIs; single-task differences of ≈1 F1 (e.g., HotpotQA 31.41–33.06 around full 31.07) are within plausible noise, yet "better than full attention" is implied |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| LongBench mean at 64, Adamas vs full | "matches" | 37.37 vs 39.70 (−2.33) | No |
| LongBench mean at 128, Adamas vs full | "near-lossless" | 39.14 vs 39.70 (−0.56) | Yes |
| 8× sparsity vs Quest | 128 vs 1024 | Adamas@128 39.14 vs Quest@1024 39.18 | Yes (LongBench, one baseline) |
| 1.5× end-to-end at 32K | 1.5× | 53.7/34.9 = 1.54 (256); 1.39 at 4096 | Yes (256 budget only) |
| Cache overhead | 1/16 | 2 bits vs 16-bit K and V: 1/16 | Yes |
| PPL ">2×" vs prior SOTA | >2× | 15.3/7.09 = 2.16 (Figure 1 only) | Yes, in that one setting |
| Quest vs full at ≥2048 | not discussed | Quest 40.81 and 40.34 vs full 39.70 | Quest above full |

## Ignored Alternative Explanations
- Rotation + any reasonable approximate score (inner product on codes, sign codes) may do equally well; L2≈L1 and 1-bit≈2-bit at ≥256 suggest the specific recipe is not the cause.
- Low-budget success on GovReport (64–4096 almost flat: 30.41–31.18) suggests several LongBench tasks are insensitive to long-range retrieval; the benchmark may not discriminate at low budgets, while StreamingLLM's collapse at the same budget suggests budget accounting may differ across methods (unstated).
- Quest's low-budget failure may reflect page size 16 against budgets below 64, not a limit of page-level methods.

## Missing Stakeholder Perspectives
Practitioners with GQA models, batched serving, or KV-capacity limits; none is covered.

## Observations (Non-Defects)
Honest component ablations over bit width and metric; a verifiable appendix with numbers behind each figure; an analytical FLOPs/memory model that is internally consistent (the Adamas total in Appendix A sums correctly from Table 4); the storage-overhead claim is exact.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Mechanism untested; theory over-read |
| Clarity & Presentation | 60 | Clear but overclaiming |
| Novelty & Originality | 46 | Recombination |
| Significance & Impact | 48 | Small latency benefit of the headline sparsity |
| Experimental Validation | 42 | One baseline, no oracle, no variance |
| Reproducibility | 50 | Key settings missing |
| Ethical Compliance | 58 | Nothing at stake; no limitations section |

**Pool position:** better than about 38% of submissions to ICLR. Deciding evidence: the headline claims fail a close read of Table 1 and Table 6, and the main baseline set is a single method.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "Single run, no variance" as a stand-alone weakness | Moved to Minor (DA-m6 carries it) | Evaluation on LongBench is likely deterministic under greedy decoding (not stated); not decisive |
| R1 | "Code unavailable" (draft point) | Dropped | The abstract states code is publicly available; only unverifiable |
| R1 | W4 batch size / units | Rewritten | Added the specific unit contradiction and the 100K memory constraint |
| R2 | W2(b) H2O/InfLLM mischaracterization | Kept, hedged | Test 3: abstracts not checked; marked medium confidence |
| R3 | "Hadamard overhead unmeasured" | Merged into R1-W4 | Same point |
| R4 | "Figure 5 ambiguous" | Rewritten as R1 Question 3 | Figure not available; unverifiable, not a weakness |
| DA | DA-M5 vs R1-W2/W3 | Kept (overlap) | Merged in Phase 2 |
| DA | Hadamard FLOP count | Moved to Minor | Cosmetic, does not affect conclusions |

Scores unchanged.

---

# Phase 2: Synthesizer Package (Part A)

**Master issue list (deduplicated):**

| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Abstract/conclusion overclaims vs Tables 1, 6, Figure 1 | R1-W1, R4-W1, DA-M1, DA-M6 | CONSENSUS-3 |
| I2 | Only Quest as baseline; token-level relatives absent; narrow models/benchmarks | R1-W5, R2-W1, R3-W2, R4-W3, DA-M3 | CONSENSUS-4/5 |
| I3 | No recall/oracle analysis; estimator not tied to q·k; theory over-read | R1-W2, R2-W4, R3-W1, DA-M2, DA-M5 | CONSENSUS-4/5 |
| I4 | Rotation ablation confounded by unstated thresholds | R1-W3, DA-M5 | CONSENSUS-2 |
| I5 | No Quest latency; underspecified efficiency setting; sparsity gain barely changes latency | R1-W4, R3-W2/W3, DA-M4 | CONSENSUS-3 |
| I6 | Missing setup details (thresholds, page size, budget definition, batch size) | R1, R4-W2 | CONSENSUS-2 |
| I7 | Citation error (Wang et al.) and mis-grouped related work | R2-W2, DA-m4 | CONSENSUS-2 |
| I8 | Novelty incremental | R2-W3, R1, R3 | CONSENSUS-3 |
| I9 | Reviewer disagreement: R3 (Overall 4) vs others (3, 2) | R3 vs R1/R2/R4/DA | SPLIT |

DA-CRITICAL: none. Issues the outcome may hinge on: I1, I2, I5. Official output: see Score Summary (before run: composite 54.0, mean rating 3.00, no ceiling).

---

# Phase 2: EIC Meta-Review

## Editorial Decision

**Paper**: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference | **Date**: 2026-11-10 | **Target Venue**: ICLR (2026 cycle) | **Paper Type**: empirical
**Review Team (fictional)**: EIC Prof. Ingrid Solheim-Marek; R1 Dr. Anselm Vorster; R2 Prof. Priyanka Valsan; R3 Dr. Camila Ordoñez-Pruitt; R4 Dr. Wei-Lin Tsao; DA Dr. Odalys Brenner-Achebe

### Decision: Borderline Reject (3), ICLR rating 4 on {0, 2, 4, 6, 8, 10} (5 on the earlier {1, 3, 5, 6, 8, 10} scale)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 54.0
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 53.2 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position**: better than about 46% of ICLR submissions (accepted share ≈ 27%).

### The Case For and Against
- **For acceptance:** A simple, training-free, practical method with a large and consistent advantage over Quest below 512 tokens on all six LongBench tasks (Table 6), a verified small storage overhead, a real kernel with measured latency, and a clean ablation showing the rotation is essential (Table 7).
- **Against acceptance:** The headline claims ("matches full attention at 64", "8× over prior SOTA", "PPL lower than full") are narrower in the tables than in the abstract; "SOTA" rests on one baseline on two 2023-era MHA models; the proposed estimator is not tested against an oracle or an inner-product alternative; and the latency benefit of the extreme sparsity is about 2% in the paper's own Table 2, with the main baseline never timed.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| 64-token "matches full attention" overstated | R1-W1, DA-M1, R4-W1 | Abstract; Table 1a; Table 6 | **Verified** | 64: LongBench mean 37.37 vs 39.70; Multifield 36.60 vs 41.64; TriviaQA 78.91 vs 84.25; passkey 10K 93% vs Quest 99% |
| 100K passkey not near-lossless at 128 | R1-W1 | Table 1b | **Verified** | Adamas 71% at 128, 100% only at 2048; Quest 99% at 1024 |
| 8× sparsity holds vs Quest on LongBench | DA numeric check | Table 6 | **Verified (narrow)** | Adamas@128 39.14 vs Quest@1024 39.18; not shown vs other methods |
| Quest above Adamas at large budgets | R1-W5 | Table 6 | **Verified** | Means 40.81 and 40.34 vs 39.58 and 39.52 at 2048 and 4096 |
| Wang et al. 2024a is a different paper | R2-W2(a) | §5; References | **Verified** | Entry is an image-generation paper; text describes an LLM sparse-attention method |
| H2O/InfLLM described as sliding-window methods | R2-W2(b) | §5 | **Partly correct** | Text does say so; whether that is wrong rests on those papers' abstracts, which I could not check; keep as a "please check" |
| "w/o Hadamard remains below the baseline" | DA-m1 | §4.4; Table 7 | **Verified** | Qasper 30.14 > 28.89 |
| Table 4 implies Adamas selection costs far more than Quest's | R1-W4, DA-M4 | Table 4, Table 5 | **Partly correct** | Depends on Quest's page size (not stated; 16 assumed). Memory reads equal; FLOPs ≈ 12.6× if p=16. Real latency may differ |
| 256→1024 budget saves ≈1.7% | DA | Table 2 | **Verified** | (35.8−34.9)/53.7; but Quest's own overhead at 1024 is not measured, so this understates what Adamas gains over Quest in practice |
| Table 2 implies attention ≈45% of time at 32K, not 30–40% | R1 Q4 | §4.3; Table 2 | **Partly correct** | Arithmetic holds; the 30–40% figure may refer to shorter lengths; left as a question |
| Estimator not tied to q·k; no recall measurement | R1-W2, R2-W4, DA-M2 | §3.1, Eq. 3, Eq. 6 | **Verified** | No recall or oracle experiment anywhere in §4 or the appendix |
| R3: "near-lossless at 128 (Table 1)" | R3-S3 | Table 1b | **Overstated** | Holds for 10K (98%), not 100K (71%) |
| Table 2 unit "us" wrong | R1 ERR-3 | Table 2 caption | **Partly correct** | Implausible as written; the true unit is not determinable from the text |
| Figure 1 accuracy values not in Table 1 | R1 ERR-4, R4-W2 | Figure 1; Table 1 | **Partly correct** | Figure labels come from extracted text; setting undefined; unverifiable |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Errors and recomputations verified at their locations; well calibrated; one speculative point (units) hedged |
| R2 (Domain) | 3 | 3 | 1.25 | Citation mismatch verified; the H2O/InfLLM point is hedged; no literature search available lowers certainty but the verified error is decisive for weight |
| R3 (Perspective) | 4 | 3 | 0.75 | A central premise ("near-lossless at 128 (Table 1)") is overstated for the 100K model, and the pool position of 66 is generous given the verified gaps |
| R4 (Generalist) | 3 | 4 | 1.00 | Sound, typical review; overclaim point verified |
| DA | 2 | 4 | 1.00 | Arguments largely verified; Overall 2 is somewhat harsh, but the weight is kept at default because DA-M1–M5 hold |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | No DA-CRITICAL issue was raised. The strongest DA issue (DA-M1, overclaim) would not make the paper unpublishable if fixed; evidence supports a weaker version of the claim (criterion 1 not met) | n/a |

### Final Decision and Justification
The EIC-weighted rating is 2.92, so the starting point is 3, and the composite cross-check (53.2, band 3) agrees; I do not depart from it. The case against rests on named, verified points: the abstract's 64-token and "near-lossless at 128" claims are contradicted for several tasks and for the 100K model (Table 6, Table 1), "prior SOTA" means one baseline, and the mechanism and the efficiency comparison with Quest are untested. None is fatal, and all are fixable; the gain over Quest at small budgets is real. My pool position is about 46: below the typical accepted efficiency paper because a typical accepted paper in this crowded sub-area compares against several token-level baselines and a modern GQA model, but above the median because the effect is large and the method is simple and useful. The point most likely to move the decision up in a rebuttal is a comparison with two token-level baselines plus Quest latency under identical settings; adding a GQA model and recall/oracle analysis would raise it further. The decision does not exceed any ceiling (none exists).

---

## Score Summary

### Official Scores and EIC Assessment (from `aggregate_scores.py`, with `eic_weight`, `--final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 48 | 52 | 62 | 54 | 46 | 52.4 | 51.4 | 16 |
| Clarity & Presentation | 62 | 62 | 70 | 68 | 60 | 64.4 | 63.8 | 10 |
| Novelty & Originality | 50 | 46 | 56 | 52 | 46 | 50.0 | 49.5 | 10 |
| Significance & Impact | 52 | 52 | 66 | 56 | 48 | 54.8 | 53.8 | 18 |
| Experimental Validation | 46 | 48 | 58 | 50 | 42 | 48.8 | 47.9 | 16 |
| Reproducibility | 52 | 55 | 60 | 56 | 50 | 54.6 | 54.0 | 10 |
| Ethical Compliance | 60 | 60 | 66 | 62 | 58 | 61.2 | 60.8 | 8 |
| **Composite** | 51.5 | 52.4 | 61.9 | 55.6 | 48.5 | **54.0 (before)** | **53.2 (after)** | |

No dimension spread exceeds 20. Pool positions: R1 42, R2 44, R3 66, R4 50, DA 38 (spread 28, below the 30-point threshold); EIC 46.

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 3 / 2 |
| Rating | 4 on {0, 2, 4, 6, 8, 10} (5 on {1, 3, 5, 6, 8, 10}) |
| Venue-weighted composite | 53.1 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Adamas: Hadamard Sparse Attention for Efficient Long-context Inference" to ICLR. Efficient long-context decoding is an important topic, and a training-free, token-level selection scheme with a kernel is a practical contribution.

**Overall Assessment:** The panel saw a simple and effective idea whose advantage over Quest at small budgets is large and consistent, but felt that the abstract's headline claims go beyond the tables, that "prior SOTA" is represented by a single baseline on two older models, and that the central mechanism and the efficiency comparison are not tested against the most informative alternatives. This is how a careful panel would likely see this draft; it is a simulation, not a prediction.

**Key Strengths Identified by Reviewers:**
1. Large, consistent gains over Quest at budgets of 64–256 across all six LongBench tasks (R1, R2, R4).
2. A well-motivated import of Hadamard rotation, with an ablation showing it is essential, and a kernel with measured latency (R1, R2, R3).
3. Low storage overhead (1/16), training-free, easy to adopt (R1, R3).

**Key Concerns Requiring Attention:**
1. Headline claims overreach (64-token parity, 100K near-lossless, PPL lower than full attention) (R1, R4, DA; CONSENSUS-3).
2. Baselines and scope: only Quest, two Llama-2 MHA models, no token-level methods such as SparQ, Loki, MagicPIG or ShadowKV `[verify]` (R1, R2, R3, R4, DA; CONSENSUS-5).
3. The mechanism is untested: no recall or oracle top-k, no quantized-inner-product control, threshold values unstated (R1, R2, R3, DA; CONSENSUS-4).
4. Efficiency: no Quest latency, unclear settings, small latency gain from the extreme sparsity (R1, R3, DA).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection is that the accuracy result may be explained by any reasonable approximate score on rotated codes, which the paper does not separate from its specific recipe.

**Decision: Borderline Reject (3).** What would change the decision: a comparison against at least two token-level training-free baselines and Quest latency under identical settings, a recall/oracle analysis, one GQA model, and claims rewritten to match the tables. These are feasible within a discussion period.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Solheim-Marek
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Baselines/scope too narrow | R1, R2, R3, R4, DA | CONSENSUS-5 |
| Mechanism untested (recall, oracle, estimator) | R1, R2, R3, DA | CONSENSUS-4 |
| Abstract overclaims | R1, R4, DA | CONSENSUS-3 |
| Efficiency comparison incomplete | R1, R3, DA | CONSENSUS-3 |
| Incremental novelty | R1, R2, R3 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the paper is above the bar | R3 (4) | R1, R2, R4 (3), DA (2) | R3's premise on near-lossless behaviour is overstated for 100K; the weaknesses are those a typical accepted paper does not share (single-baseline "SOTA"). Sided with 3 |

### Score Spread Discussion
No dimension flagged ⚠ (largest spread 18, Significance). Pool positions differ by 28 points between R3 and DA; the evidence behind the difference (the practical value of the low-budget gain vs the narrowness of evidence) is covered in the arbitration above.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | 64-token parity overstated | Yes: R1, R4 | n/a | n/a |
| DA-M2 | MAJOR | Eq. 3 exactness over-read | Yes: R2 | n/a | n/a |
| DA-M3 | MAJOR | Prior SOTA = Quest only | Yes: R1, R2, R3, R4 | n/a | n/a |
| DA-M4 | MAJOR | Quest latency missing; payoff small | Yes: R1, R3 | n/a | n/a |
| DA-M5 | MAJOR | Alternative explanations / ablation confound | Yes: R1 | n/a | n/a |
| DA-M6 | MAJOR | PPL claim | Partly: R4 | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
No upheld DA-CRITICAL issues. These are the issues the EIC verified as undermining a main claim as worded:

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline accuracy claims exceed Tables 1 and 6 (64-token parity, 100K near-lossless, PPL lower than full) | R1-W1, R4-W1, DA-M1, DA-M6 | Abstract, §1, §6, Table 1, Table 6, Figure 1 | Rewrite claims to the supported regime; add full-attention row; PPL table with settings | Low | Yes |
| R2 | "Prior SOTA" / "8×" rests on one baseline | R1-W5, R2-W1, DA-M3 | §4.1, §5, Abstract | Add ≥2 token-level baselines (e.g., SparQ, Loki, MagicPIG, ShadowKV `[verify]`) at matched budgets, or restrict claim to Quest | Medium (≈20–40 GPU-h) | Partly |
| R3 | Efficiency comparison omits Quest and settings | R1-W4, R3-W3, DA-M4 | §4.3, Figure 5, Table 2 | Time Quest with identical hardware/batch; state batch size, unit; quality-latency Pareto plot; prefill overhead | Medium (≈1 GPU-day) | Partly |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | No recall/oracle analysis; estimator vs q·k; add quantized-inner-product control | R1-W2, R2-W4, DA-M2, DA-M5 | Recall and softmax-mass coverage vs exact top-k; oracle row in Table 7 | Low–Medium (≈5 GPU-h) | Yes |
| S2 | Rotation ablation confounded by thresholds | R1-W3, DA-M5 | State thresholds; add per-channel/quantile-threshold no-rotation variant | Low | Yes |
| S3 | Missing setup details | R1, R4-W2 | Appendix: thresholds, page size, budget accounting, layers, batch, decoding, trials | Low | Yes |
| S4 | Narrow models/benchmarks; GQA | R1-W5, R3-W2, R4-W3 | Add a GQA model and RULER/multi-needle test | Medium–High | Partly |
| S5 | Citation error and mis-grouped related work; KV-quantization omitted | R2-W2, DA-m4 | Fix Wang et al. entry; check H2O/InfLLM abstracts; add references (all `[verify]`) | Low | Yes |
| S6 | Missing limitations section (100K, MHA, decode-only, no capacity saving) | R1, R3, R4 | Add limitations | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | "w/o Hadamard remains below baseline" false for Qasper | DA-m1 | Say "on most tasks" |
| N2 | "Most memory-efficient" 2-bit wording (1-bit is smaller) | DA-m2 | Reword |
| N3 | Table 4 Hadamard FLOPs entry; Table 2 unit; typos; Figure 3 metric label | R1, DA | Correct |
| N4 | Randomized Hadamard; layer-wise coverage | R3-W1 | Optional study |
| N5 | Variance/CI for LongBench | DA-m6 | Bootstrap CIs |

## Estimated Revision Effort
- Priority 1: 3 items, about 3–5 days including baselines.
- Priority 2: 6 items, about 3–6 days (S4 dominates).
- Priority 3: 5 items, under 1 day.
- **Total estimated revision time**: about 1–2 weeks.
