# Review: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models

Note: figures were not available. Figures 1-3 are judged from captions and text only.

## Summary
The paper proposes ZSPAPrune, a training-free visual-token pruning method applied to the tokens fed to the LLM. The prompt's token embeddings are mean-pooled into one vector. The method keeps the top-k visual tokens by cosine similarity to that vector (the "core" set). It then adds diversity tokens by greedy max-min selection, which is the DivPrune-style step, starting from the core set. A coefficient k sets the core/diversity split. The paper evaluates at a 90% pruning rate on LLaVA-1.5-7B, LLaVA-NeXT-7B and Qwen2.5-VL-7B over six benchmarks: MMMU, GQA, AI2D, POPE, TextVQA and ChartQA. Baselines are the unpruned model, DivPrune and a self-built "relevance-only" baseline. The authors claim matching or better results than the state of the art, plus latency and memory savings.

## Strengths
- The problem is relevant, and training-free pruning is practical.
- Combining query relevance with diversity is intuitive and simple. It is easy to implement and needs no attention scores.
- The paper honestly reports cases where it loses to DivPrune (AI2D and TextVQA on Qwen). The relevance-only baseline does show that relevance alone is harmful.
- The k-sweep and the pooling ablation are in the spirit of analysis.

## Weaknesses
1. **Marginal novelty and weak positioning.** The method is a relevance top-k followed by the DivPrune-style max-min greedy step. Prompt-guided pruning already exists (PAR, GlimpsePrune, SparseVLM and related work), so the claim that existing work "neglects" the prompt is overstated. FastV is also mischaracterised: it uses LLM-layer attention after layer 2, not final-layer ViT attention. No prompt-aware method is compared against.
2. **Very thin baselines.** The only real baseline is DivPrune. FastV, SparseVLM, VisionZip, PDrop, PAR and GlimpsePrune are absent, so "state-of-the-art" claims are unsupported. The "relevance-only" baseline is a strawman built by the authors.
3. **Gains over DivPrune are negligible or inconsistent.**
   - On LLaVA-1.5 and LLaVA-NeXT the two methods are nearly identical. MMMU and GQA are exactly equal on both models. Other differences are at most 0.3 points, except TextVQA (ZSPAPrune worse) and ChartQA on LLaVA-1.5 (54.0 vs 51.5).
   - On Qwen, ZSPAPrune wins 4 of 6 benchmarks and loses AI2D and TextVQA. The margins are 1-3 points from single runs without variance.
   - Table 2 is the central evidence for prompt-awareness, and it does not support it. On GQA and POPE, accuracy falls nearly monotonically as more tokens go to relevance, so the best setting is the most diversity-heavy. On MMMU, k from 0.1 to 0.8 spans about 1 point. There is no k=0 (pure diversity under the same implementation) entry, so the prompt's contribution is never isolated. A control with a random or mismatched prompt is also missing.
4. **Per-benchmark k is tuned on the test set.** Section 4.2 uses "the optimal ratio for each specific benchmark". This is an oracle for ZSPAPrune that DivPrune does not get. It weakens the "zero-shot" claim, since a practitioner cannot know the best k for a new task. The conclusion that pruning must be "tailored to the benchmark" is circular. A fixed k, or one chosen on held-out data, is needed.
5. **Suspicious absolute numbers.**
   - Baselines are far from published values. LLaVA-1.5: MMMU 25.4 (about 35 expected), GQA 58.7 (about 62), TextVQA 39.5 (about 58 expected). AI2D is 29.1, near chance for four-way multiple choice, which points to a broken evaluation.
   - MMMU is said to use the "official test split", which has no public labels.
   - The +22.7% ChartQA "improvement" on LLaVA-1.5 from pruning is more likely an answer-parsing or format artefact than "noise reduction". The explanation is untested.
   - Qwen2.5-VL at 90% pruning drops POPE from 85.8 to 65-69, which is much worse than published pruning results. This suggests the Qwen setup (dynamic resolution, positions, token counts) is suboptimal, so DivPrune may be mis-reproduced too.
   - The "retains ~90% accuracy" claim fails in several cases: LLaVA-NeXT GQA is 68%, Qwen POPE is 80%, and TextVQA is 70-84%.
6. **The relevance score is questionable.** Cosine similarity is computed between mean-pooled prompt input embeddings and projected visual tokens, before the LLM. These spaces are not guaranteed to align, and the modality gap is well known. A mean over all prompt tokens, including template and stop words, is dominated by generic tokens. There is no qualitative or quantitative evidence that the scores are meaningful. The relevance-only collapse (TextVQA 11.6% on LLaVA-1.5) suggests they are not. Table 4 shows none/max/mean within about 2 points on one model and two benchmarks, which does not validate the pooling design.
7. **Weak efficiency analysis.**
   - Latency is a single number on LLaVA-1.5 and MMMU, with no variance, FLOPs or prefill breakdown.
   - ZSPAPrune is slower than DivPrune.
   - The memory table uses three samples, saving 172-234 MB on a ~14 GB peak (weights dominate), and the variation is attributed to output length.
   - No efficiency data is given for Qwen2.5-VL, where visual tokens are most numerous.
   - No cost comparison with other methods.
8. **No statistical rigour.** The reproducibility statement says a fixed seed makes inference deterministic, "so statistical significance tests or error bars are not required". This is wrong. Determinism of one run says nothing about sampling variability over the evaluation set, and the margins here are often under 1 point.
9. **Scope is overstated.** Only image benchmarks, 7B models and a single 90% ratio are reported. The abstract and text hint at video and high-resolution generality, but no video is evaluated and there are no accuracy-vs-ratio curves. Prompt-dependent pruning also prevents KV-cache reuse across multi-turn queries on the same image, which is not discussed.
10. **Presentation errors.** The appendix describes Qwen2.5-VL as using cross-attention (it uses an MLP merger). Relative percentages and absolute points are mixed. "MMVU" is a typo. MAE reconstruction is called a "theoretical basis". The symbol k denotes both a token count and a ratio, and k̃ is unclear. There is no pseudo-code or complexity analysis.

## Questions
1. What is the result with one globally fixed k across all benchmarks and models, and with k chosen on a held-out split?
2. How does the method compare with FastV, SparseVLM, VisionZip, PDrop, PAR and GlimpsePrune at the same budget, and at 50%, 75% and 95% pruning?
3. Why are baseline accuracies so far below published values (AI2D 29.1; MMMU test split)? Can you reproduce DivPrune's reported numbers in your framework?
4. Can you show the relevance scores are meaningful (selected-token visualisations, an unrelated or random prompt control, k=0)?
5. What are the confidence intervals, for example bootstrapped over the evaluation set?
6. Why does pruning improve LLaVA-1.5 ChartQA by 22.7%? Is it an answer-parsing artefact?

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- Rating: 4
- Confidence: 4

Justification: this is a simple, reasonable idea with little novelty beyond DivPrune plus a cosine-similarity top-k. The evidence rests on one real baseline, oracle per-benchmark tuning, results mostly indistinguishable from DivPrune, questionable baseline numbers and no statistical analysis. It is below the ICLR bar in its current form.
