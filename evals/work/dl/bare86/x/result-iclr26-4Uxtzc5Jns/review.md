# Review: G-KV: Decoding-Time KV Cache Eviction with Global Attention

(Figures were not available; figure-dependent claims are judged from captions and text only. I read the first ~1000 lines of the extracted text, which covers the main paper and the start of the appendices.)

## Summary
The paper proposes G-KV, a decoding-time KV cache eviction method for reasoning LLMs. Instead of scoring tokens with attention from only the latest observation window (MorphKV, R-KV, SnapKV-decode), it keeps a recursively decayed "global score" F_t. The score is a max, mean or sum of the per-window normalized attention, with decay α, and it is used for top-k selection. The motivation is an overlap analysis (Fig. 1) showing that the last window's attended tokens are better covered by the union of earlier windows than by any single earlier window. G-KV is the global score combined with R-KV's redundancy term. The paper also proposes post-training adaptation to the compressed cache. This uses GRPO with generation under the compressed cache plus a sparse attention mask ("RL-Sparse"), and a KL-distillation variant. Experiments use DeepSeek-R1-Distill Qwen-7B and Llama-8B on AMC23, AIME24 and LiveCodeBench, with budgets of 256–2048. They report large gains at small budgets (about 20 points at 512 on AMC23), RL-Sparse gains over RL-Full, and throughput gains of up to about 12–20× over Full-KV (an OOM-limited comparison).

## Strengths
- The problem is well motivated. Decoding-time compression for long CoT is practically important, and the method is simple. It adds almost no overhead (about 5 ms per compression step, ~1% of decode time), and it plugs into R-KV and SnapKV.
- The ablations over the score form (max/mean/sum) and α are clear. The method is stable for α in [0.8, 0.9].
- The training component is a sensible idea. Rolling out and training under the same eviction policy removes the train/inference mismatch. RL-Sparse beats RL-Full in Table 1 in most cells.
- The position-distribution analysis (Fig. 7) offers a plausible mechanism: local scores bias retention toward recent tokens.
- Throughput and memory are reported on real hardware, and code is promised.

## Weaknesses
1. **Limited novelty.** A decayed, accumulated attention score is H2O (accumulated attention) with exponential forgetting. Scissorhands (persistence of importance), TOVA, and related history-aware scores are close precedents. The "max" form is a running max with decay. The paper's claim that H2O "easily ignores tail tokens" is not tested. H2O (or a decayed H2O) is not a baseline in the main comparison. The decay α is the only conceptual difference from H2O, and the paper does not isolate it.
2. **The motivating observation is weak.** The overlap in Fig. 1 is computed on only the last 512 generated tokens, split into 4 windows, for one model and one benchmark. Single windows overlap with the last window at roughly 0.8–0.95, which is high, so the claim that importance "shifts" is not obviously supported. The union of windows trivially has a larger overlap because it is a larger set, so the comparison is not size-matched. Observation 2 is therefore not evidence for the specific max/decay design. There is no controlled test (e.g., random sets of equal size, or an oracle).
3. **Experimental rigor and statistics.**
   - Gains are reported as single curves with no confidence intervals or seed variance. Pass@1 is averaged over 32 samples, but AIME24 has only 30 problems, and the differences between methods are often small.
   - α=0.8 was chosen on AMC23, which is also a headline test benchmark.
   - The AMC "2023" benchmark cites the 2023 AMC 8 wiki page, which is a middle-school contest, rather than AMC 12 (the standard AMC23 set used for these models). This needs clarification, since the benchmark description is inconsistent with common usage.
   - There is no cross-family or larger-model evidence beyond two 7–8B distills. Qwen3, QwQ and a 32B model are absent. LiveCodeBench results are shown for the Qwen model only. The training experiments cover one model.
4. **Baseline fairness.**
   - SnapKV and StreamingLLM were adapted ad hoc. The statement that "other parameters follow the paper" leaves unclear how R-KV hyperparameters (λ, thresholds) were chosen for the comparison.
   - G-KV is R-KV plus the global score. The headline "20% improvement" is claimed against baselines at a harsh 512 budget where baselines degrade sharply. At larger budgets the gaps appear small.
   - Comparisons with other decode-time eviction methods for reasoning (e.g., TOVA, LazyEviction-style or retrieval-based approaches) are missing.
5. **Token Retention Ratio is a confusing, possibly misleading metric.** It is computed only on correctly answered samples, so it is confounded by the correct set differing across methods. It is also a function of sequence length: methods that solve harder or longer problems have lower ratios. The claim that lower retention indicates "higher information density" is not justified. Generation length under compression (compressed models often produce longer or looping outputs) is not reported, yet it directly affects the real compute savings.
6. **Training section.**
   - Training uses a max length of 4096 and evaluation is restricted to 4096, while the main evaluation uses 16k/32k. The adapted models are never evaluated in the long-generation regime where compression matters. Their absolute accuracies (AIME24 11–27%) are far below Full-KV at normal lengths, so the improvement may partly reflect learning to be shorter or to fit the 4k limit. RL-Full gains may also reflect truncation-related effects.
   - RL-Sparse is trained with the G-KV cache at budget 2048 but evaluated at 512/1024/2048. The train/test budget mismatch is not discussed.
   - A distinct control is missing: RL-Sparse with the baseline eviction (R-KV or local score), to show the training benefit is not specific to G-KV.
   - Single run, no seeds. The distillation gains (+1.6 to +2.9) are within plausible noise on AIME24 (30 problems).
   - The implementation of the sparse mask during training (does the backward pass follow the exact per-head eviction schedule? how are RoPE positions handled?) is not described, and the cost is not reported. Zeroing advantages for truncated outputs under a 4k cap discards many trajectories.
   - The abstract and intro present training as a core contribution, but it is treated lightly in the paper.
7. **Efficiency claims.** The 12–19.7× throughput is compared with Full-KV at different batch sizes, where Full-KV is OOM. Same-batch gains are 2.7–5×. The comparison with R-KV at the same budget shows essentially no throughput difference, so the efficiency story comes from R-KV and not from this paper. Throughput counts tokens but does not account for accuracy, longer outputs under compression, or end-to-end time to solution.
8. **Limited mechanistic grounding.** No analysis explains when a global score hurts (e.g., stale tokens that were important early but are now irrelevant). Per-head normalization by the maximum score may be dominated by attention sinks, and the treatment of sink and prompt tokens is not described. Failure cases and per-layer/head behavior are not shown. The "human memory" analogy is only a motivation.
9. **Presentation.** Many claims are stated loosely ("significantly", "SOTA across most budgets"). There are typos ("A cases presented", "DeepSeek-Qwen-Llama-8B"). The conclusion mentions only AMC and AIME although LiveCodeBench is also used.

## Questions
1. How does G-KV compare to a decayed-H2O baseline (accumulated attention with the same decay, no redundancy term) and to H2O/TOVA directly? Does the redundancy term from R-KV account for part of the gain? Please report global score alone and R-KV alone at each budget on all benchmarks.
2. Please provide variance across seeds or bootstrap CIs, especially for AIME24 and the training table. Was α tuned on AMC23, and are the other benchmarks run with the same α?
3. Which AMC 2023 set was used (AMC 8 or AMC 12)? How many problems?
4. What are the generation lengths and the rate of non-terminating outputs for each method at each budget? Is the retention ratio computed on matched problems?
5. Do RL-Sparse/Distill models retain their gains at 16k/32k generation lengths? What about RL-Sparse trained with R-KV or the local score?
6. How are the initial tokens (sinks, the prompt) handled in the global score? Do the results hold for other models (Qwen3, larger models)?
7. How is RoPE position handled after eviction, and how is the sparse mask implemented efficiently in training?

## Soundness: 2
The core idea is plausible and the empirical evidence at the 7–8B scale is suggestive. The motivating analysis is not size-controlled, statistical rigor is missing, key baselines and controls are absent, and the training evaluation is limited to 4k.

## Presentation: 2
Generally readable, but claims are loosely worded, the metrics are nonstandard, and some experimental details are unclear.

## Contribution: 2
The global score is an incremental variant of accumulated-attention eviction. The RL/sparse-mask training idea is more interesting but thinly evaluated.

## Rating: 4

## Confidence: 4
