# Review: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for VLLMs

(Reviewed from extracted text; figures were not available, so figure-dependent claims are judged from captions and text only.)

## Summary
The paper proposes PureKV, which has two parts for video VLLMs.
1. **CLIE (cross-layer importance estimation).** Attention scores are computed only in a low layer (layer 1 or 2). They are accumulated over a recent window of queries, weighted by the L2 norm of V, and reused to select the top-h KV entries in every higher layer. Higher layers can then use FlashAttention or sparse kernels.
2. **ST-SpAttn.** A fixed, hand-designed sparse prefill pattern. Each token attends to the first frame, its own frame, and the corresponding token of the previous frame. It is claimed to "purify" the KV cache and to speed up prefill.

Experiments use VideoLLaMA2 and Qwen2.5-VL-7B on a subset of MVBench tasks, with cache budgets of 20% and 10%. The baselines are H2O, SnapKV, StreamingLLM, FastV and LOOK-M. The paper reports up to 5x KV compression and 3.16x prefill speedup, and gains over the baselines.

## Strengths
- The problem is practical. Score-based KV eviction does not work with FlashAttention-style kernels, so an eviction criterion that avoids high-layer attention matrices is useful.
- The method is simple and training-free, and could be implemented cheaply.
- The paper reports a rank-correlation analysis (Fig. 4) as a sanity check for reusing low-layer scores, and a layer-index sweep (Fig. 5).
- The appendix shows that CLIE/ST-SpAttn can be attached to other eviction methods (Table 6), and compares different sparse patterns (Table 7).

## Weaknesses
1. **The core claim for CLIE is overstated.**
   - The text calls low-layer scores a "sufficient statistic" and says the correlation "provides strong empirical support".
   - Fig. 4 reports Spearman correlations of about 0.4 in most layers and about 0.2 in the top layers. These are weak to moderate. Significance at p<0.05 over thousands of tokens says little about whether the selected top-h set is the right one.
   - A set-overlap or recall metric for the top-h tokens is the relevant measure. Output-error or attention-mass recovery would also help. The paper reports none of these.
   - No theory supports "sufficient statistic". The number of samples used for the correlation is not stated.
2. **The "purification" motivation for ST-SpAttn is not demonstrated.**
   - The claim is that dense attention "gradually confuses" important and unimportant information in high layers. It rests on a qualitative Fig. 1(c) and a causal-mixing argument.
   - That argument applies to any transformer and is not shown to hurt importance estimation. There is no measurement of importance-estimation quality with and without ST-SpAttn.
   - The improvement could come from other effects, for example the first-frame/previous-frame structure acting as an attention-sink-like prior.
3. **The ablations are too thin to support the component claims.**
   - Table 4 uses a single task (labelled "Action Sequence (AC)", whereas Table 1 uses AC for Action Count). The full-method numbers coincide with the single-task PureKV entries in Tables 1 and 2.
   - The differences are small (about 0.73 versus 0.75 on Qwen) and likely within noise on one task. No variance, seeds, or confidence intervals are given anywhere.
   - There is no configuration with ST-SpAttn but without CLIE.
   - The text says "CLIE does not cause degradation", but the ablation never shows a benefit from CLIE.
4. **The comparisons are not fair, and some results look suspicious.**
   - PureKV gets ST-SpAttn, which changes the prefill computation of the whole model, while the baselines keep dense prefill. Table 6 attempts to address this, but "+PureKV" is ambiguous (CLIE, ST-SpAttn, or both).
   - Table 1: at a 20% budget PureKV (0.5429) exceeds the **full cache** (0.5136) on average, with several tasks far above full cache. This is never discussed. It suggests high evaluation noise or a metric problem.
   - Table 1: LOOK-M scores about 0.01-0.06, which is essentially a broken baseline. This is more likely an integration failure than a true result, and it inflates the apparent margin.
   - Table 2: baselines collapse on VideoLLaMA2 (H2O 0.31, SnapKV 0.48 at 20%). PureKV leads by a huge margin on OE (0.72 versus 0.38 or lower). This is unusual for well-known methods and suggests the baselines (window size, handling of visual versus text tokens, GQA head pooling) were not tuned. Details are not given.
   - The abstract says "negligible quality degradation", but VideoLLaMA2 drops from 0.6635 to 0.6189 (20%) and 0.5047 (10%). A drop of about 16 points at 10% is not "stable performance".
5. **The evaluation is narrow and unconventional.**
   - It uses a subset of MVBench tasks. The paper lists 14 but the tables show 10, with different sets per model. Table 2 has "AC" twice, and the task names do not match the list. Why these tasks were chosen is not explained.
   - The metric is ROUGE on what are multiple-choice questions, which is non-standard. Accuracy is the usual metric.
   - No long-video benchmark (Video-MME, LongVideoBench, MLVU, EgoSchema) is used. KV compression matters most for long videos, and MVBench clips are short.
   - Only two models are tested, plus one AVSD experiment (Table 5) where PureKV (0.4265) is barely above SnapKV and FastV (0.4249, 0.4224) and well below full cache (0.4795). The text says it "significantly outperforms".
6. **The efficiency claims are not well supported.**
   - The headline "3.16x prefill acceleration" is from Table 3, in "ms/token" units with no sequence lengths, batch size or frame counts.
   - Prefill latency is nearly constant across budgets (0.0366 to 0.0355). So the speedup comes from ST-SpAttn and low-layer-only attention, not from KV compression, and the "5x compression and 3.16x speedup" are not clearly the same configuration.
   - There is no latency or throughput comparison to any baseline, yet the paper concludes "faster decoding than the comparison method". Peak memory is not reported.
   - It is unclear whether the sparse pattern uses a real block-sparse kernel or masking.
7. **Method details are underspecified.**
   - How "first frame" and "corresponding token in the previous frame" are defined for Qwen2.5-VL (merged patches, temporal patch size 2) is not explained.
   - It is unclear how text query tokens attend. The "recent window" in Eq. 2 is at the end of the sequence, which includes the question, so its interaction with ST-SpAttn is unknown.
   - Aggregation across heads and GQA groups, the choice of h and w, and per-layer budgets are omitted.
   - Selection happens after high-layer K/V are computed, so peak prefill memory is not reduced.
   - The best CLIE and ST-SpAttn layers in Fig. 5 appear to be selected on the same single task that is reported, which is tuning on the test set. CLIE layer 0 scores about 0.01, a catastrophic failure that suggests fragility.
8. **Novelty is limited.**
   - Reusing early-layer attention for token selection is related to FastV and GemFilter. V-norm weighting resembles ZipCache and VATP-style criteria. The 'first frame + local' pattern resembles StreamingLLM-style sinks and Sparse VideoGen. These are not discussed or compared, and neither are VL-Cache or MadaKV.
   - The claim that "no existing sparse attention scheme" interacts with KV compression is too strong.
9. **Presentation.**
   - There are inconsistencies. Section 4.3 cites Tables 1 and 2 in the wrong model order. Table 3 uses 5-50% budgets while the abstract's 5.0x corresponds to 20%. "AC" is used for different tasks.
   - Several references (3D Gaussian avatars, knowledge tracing, federated learning) are unrelated to the paper. No limitations section is given.

## Questions
1. What are the top-h overlap or recall between estimated and true high-layer importance sets, and the attention mass recovered, rather than only Spearman rho? How many samples were used in Fig. 4?
2. Why does PureKV at 20% on Qwen2.5-VL beat the full cache on average? Please report accuracy with confidence intervals and per-task sample sizes.
3. What does ST-SpAttn alone (sparse prefill, no eviction) score versus full cache? What do baselines score when given ST-SpAttn prefill, and what does CLIE alone score versus SnapKV?
4. Why are the LOOK-M numbers near zero? Were all baselines run with the same video handling and tuned?
5. Please report end-to-end TTFT, throughput, and peak GPU memory against baselines at several video lengths, and state which kernels were used.
6. Results on long-video benchmarks and more models would substantially strengthen the claims. How were the 10 MVBench tasks chosen out of 20?
7. How is ST-SpAttn defined for Qwen2.5-VL, and how do text tokens attend?

## Scores
- **Soundness:** 2
- **Presentation:** 2
- **Contribution:** 2
- **Rating:** 4 (marginally below the acceptance threshold)
- **Confidence:** 4

The idea is practical and the results look encouraging, but the evidence does not support the main claims. The central justification (low-layer proxy and "purification") is weakly validated. The ablations are on a single task with no variance, some baselines look broken, and the evaluation is narrow. Efficiency claims are not compared to any baseline. Stronger controls, long-video benchmarks and fair baselines could change my view.
