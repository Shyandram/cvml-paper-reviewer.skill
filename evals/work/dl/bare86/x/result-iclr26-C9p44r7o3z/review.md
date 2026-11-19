# Review: Adamas: Hadamard Sparse Attention for Efficient Long-context Inference (ICLR 2026)

*Figures are not available in the extracted text. I judged Figures 3–6 from captions, text and the appendix tables (6 and 7) only.*

## Summary
Adamas is a training-free, query-aware, token-level sparse attention method for decoding. Each key (and the query) is rotated with a Hadamard transform. The result is bucketized into 2-bit codes with fixed thresholds (for example [-10, 0, 10] in Figure 2). The codes are packed and stored in the KV cache. At decode time, the negative L1 (Manhattan) distance between the query code and every key code is used as a proxy for q·k. The top-k tokens are selected, and exact attention is computed over them. The authors write custom CUDA kernels. They evaluate on LongChat-7B-32k and Yarn-Llama-2-7B-128k, with PG19 perplexity, passkey retrieval and six LongBench tasks. They compare against StreamingLLM and Quest. They claim accuracy close to full attention at 64–128 token budgets, up to 8× higher sparsity than Quest, 4.4× attention-kernel speedup and 1.5× end-to-end speedup at 32K, and perplexity "lower than full attention".

## Strengths
- The problem is practically relevant. The design is simple and training-free, and it needs little extra cache (2 bits per key channel).
- Combining a Hadamard rotation with very low-bit codes for retrieval is reasonable and easy to implement. The ablation shows the rotation is the key enabler: without it, bucketization collapses (GovReport at 128 tokens: 0.64 vs 30.44, Table 7).
- Token-level selection beats page-level Quest at small budgets on LongBench (Table 6). On GovReport at budget 64, Adamas scores 30.4 vs 3.3 for Quest. Kernel-level and end-to-end latency are reported, and the appendix has a FLOP and memory-access analysis.
- The ablations over bit-width and distance metric (1/2/3-bit, L1 vs L2) are informative. They show the method is not very sensitive to those choices.

## Weaknesses
1. **Baselines are thin and dated.** Only StreamingLLM and Quest are compared. Quest is one specific page-level design.
   - Many closely related training-free methods that approximate q·k with compressed keys or channels, or select tokens, are not compared. Examples are SparQ, Double Sparsity, Loki, InfiniGen, MagicPIG, RetrievalAttention, PQCache and ShadowKV. Most are not even cited. They are direct competitors.
   - "Up to 8× higher sparsity than prior SOTA" is therefore relative only to Quest. It is measured at budgets where Quest is handicapped by page granularity. Quest's page size and configuration are not stated, nor whether the first layers are kept dense as in the original Quest. Quest's collapse below 128 tokens (for example 3.3 on GovReport at 64) is partly an artifact of the page-granularity budget: with 16-token pages, a 64-token budget is only 4 pages.
2. **The approximation is weakly justified.**
   - The "theoretical perspective" (Eq. 3) only shows that rotation preserves q·k before quantization. The actual estimator is the L1 distance between 2-bit codes of Q and K. That is not monotone in the inner product, and no bound, recall analysis or error analysis is given. The paper never measures how well Adamas recovers the true top-k or attention mass, vs the exact top-k or vs Quest. This is the most direct evidence for the central claim of "high recall", and it is missing.
   - L1 and L2 behave alike, and no inner-product-type estimator on the same 2-bit codes (for example a lookup-table dot product) is tried. Such a comparison is needed to justify Manhattan distance.
   - The explanation of L1 vs L2 differences ("L2 emphasizes global geometric consistency … L1 is more robust to noise") is speculation. The differences in Table 7 look like noise.
3. **Under-specified method details that affect reproducibility and validity.**
   - How are the thresholds B1–B3 chosen? Are they fixed globally, or per layer or head? Is calibration data used? Fixed values such as [-10, 0, 10] depend on the model's activation scale.
   - Are keys quantized before or after RoPE? Is the query quantized with the same thresholds as the keys? Which layers use sparse attention and which stay dense?
   - GQA is not discussed, although it is the norm in current models.
   - The "w/o Hadamard" ablation applies the same fixed thresholds to raw activations with outliers. That looks like a strawman, since the thresholds were not re-tuned. "Hadamard is critical" may reflect this mismatch rather than an intrinsic need. A per-channel scaled or calibrated no-rotation baseline is needed.
4. **Narrow, old model and task coverage.**
   - Only two 2023-era Llama-2-7B-based long-context models are used. There is no GQA model (Llama-3.x, Qwen), no larger model, and no reasoning or long-generation task.
   - Only six LongBench tasks are used (no code or synthetic tasks). There is no RULER, no needle-in-a-haystack grid and no multi-key or variable-tracking task. Passkey is easy and single-needle. Quest is already near-saturated at small budgets in the 10K setting (99% at 64 vs 93% for Adamas).
   - No variance or seeds are reported. Many LongBench differences in Table 6 are fractions of a point, while the text says "consistently surpasses".
5. **Overstated and ambiguous claims.**
   - "Matches full attention with only 64 tokens" holds only on some LongBench tasks. At 64 tokens, TriviaQA is 78.9 vs 84.3 and MultiFieldQA is 36.6 vs 41.6. Passkey at 64 is 93% at 10K and 54% at 100K (Table 1), not full accuracy. Adamas also trails Quest at budget 64 on 10K passkey (93 vs 99).
   - "Perplexity lower than full attention" is presented as a feature. A sparse approximation beating dense attention suggests either a regularizing effect or an evaluation artifact. No analysis is offered, and the claim is visible only from a figure at larger budgets. "Outperforming prior SOTA by more than 2×" on perplexity is not defined.
   - Fig. 1 reports PPL and accuracy for a single unspecified setup. It is presented as an illustration but reads as evidence.
6. **The efficiency evaluation has gaps.**
   - Estimation is still O(s) over all keys per decoded token (3bsh in Table 4), so the cost stays linear in sequence length. The 4.4× applies to the attention kernel at a 256-token budget on one GPU (RTX A6000). The Hadamard transform and bucketization are omitted as "negligible" rather than included.
   - Table 2 reports latency in "us" with values of 26–54. A full decode step of a 7B model cannot take about 30 µs. This is presumably ms, which shows carelessness.
   - End-to-end gains are modest: 1.5× at 32K, and about 1.0–1.2× at 8K–16K. There is one hardware configuration, no latency comparison against Quest or other sparse baselines, and no batched-serving throughput. Memory is not saved (the KV cache is not reduced and a 2-bit copy is added). Prefill is not addressed.
   - "Cache grows by only 1/16" should be made precise. It is about 1/16 of the key cache, or 1/32 of K+V in fp16.
7. **Novelty is moderate.** Hadamard rotation before low-bit quantization is established (QuaRot). Approximate, compressed-key scoring for top-k selection exists in several of the works named above. The contribution is mostly an engineering combination. That is fine if backed by strong empirical and systems comparison, but that comparison is limited here. Related work also mislabels H2O and infLLM as "static sliding-window" methods. H2O is a score-based eviction method.

## Questions
1. What is the top-k recall (or attention-mass recall) of Adamas vs the exact top-k and vs Quest at various budgets, per layer? Does it explain the accuracy gap?
2. How are the thresholds set, and how sensitive are results to them across models, layers and heads? Please add a no-rotation ablation with calibrated or re-scaled thresholds.
3. What are Quest's page size and budget accounting, and which layers are dense for each method? Please add comparisons to some of SparQ, Double Sparsity, Loki, MagicPIG, RetrievalAttention, ShadowKV and PQCache.
4. Does the method work on GQA models (Llama-3.1, Qwen2.5) and larger models, and on RULER and long-generation or reasoning tasks?
5. Why would sparse attention give lower perplexity than full attention? Which layers or heads are kept dense?
6. Please fix the units in Table 2 and report latency including Hadamard and bucketization overhead, alongside Quest's latency and batched throughput.

## Scores
- **Soundness: 2** (reasonable heuristic, but no recall analysis, missing key details, weak baseline set, unsupported explanations)
- **Presentation: 2** (readable, but missing method details, unit errors, imprecise claims, thin related work)
- **Contribution: 2** (practical but incremental combination, with limited empirical evidence against the state of the art)

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**
