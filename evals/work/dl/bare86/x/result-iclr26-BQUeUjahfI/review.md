# Review: Learning Tractable Distributions of Language Model Continuations (LTLA)

Note: figures were not available. Figs 1, 3 and 4 are judged from captions and text only.

## Summary
Tractable-surrogate controlled generation (Ctrl-G, TRACE) uses an HMM distilled from an LM. The HMM's latent prior q(z_t | x_<t) is a fixed function of the prefix, so the surrogate is only weakly context aware. LTLA replaces the HMM's prefix encoder with a neural encoder. Three variants are used: a linear head on frozen LM hidden states, an extra trainable transformer layer, or a fully fine-tuned backbone. The head outputs a prior over the latent state. The HMM transition and emission parameters (the "decoder") stay fixed and shared across prefixes. The backward quantities, such as the DFA lookup tables of Ctrl-G, therefore remain precomputable. One encoder pass plus a single batched HMM forward step scores all V candidate tokens. The paper also proposes Monarch-structured HMMs and gives a short mutual-information bound, I(X_<t; X_>=t) <= log H.

Experiments cover three areas:
- Distillation perplexity on GPT-2-large samples, as a function of hidden size and continuation length.
- CommonGen with Ctrl-G.
- Detoxified image captioning with a Qwen2-VL-2B surrogate and a log-linear toxicity classifier (TRACE-style) on Hateful Memes.

The paper reports lower conditional perplexity than a plain HMM, especially for short continuations. It reports mixed gains on CommonGen and lower toxicity than prompting and Monte Carlo baselines on the VLM task.

## Strengths
- The design is simple and well motivated. Only the prior is made context dependent, so the HMM's backward/DFA precomputation and the O(n) rather than O(n^2) decoding cost are preserved. The comparison with "prefix-parameterized TPM" and "exhaustive rescoring" (Table 1, Sec. 3.1, App. C) states the tractability trade-off clearly.
- The observation that standard distilled HMMs barely react to the prefix (Fig. 1) is a real limitation of the Ctrl-G/TRACE line of work. Using the LM's own representation to fix it is a natural idea.
- The plug-in design also allows conditioning on a VLM's (visual) context. This extends tractable lookahead to a setting where a plain HMM cannot be used. It is a nice demonstration.
- The paper is candid about some negative results, e.g. Monarch HMMs are not better at matched compute, and neural reparameterization plus LVD hurt in their setting.

## Weaknesses
1. **Evidence for downstream benefit is thin and mixed.**
   - In the CommonGen table (Table 2), BLEU-4/CIDEr/ROUGE-L differences are in the second or third decimal place (e.g. 0.303 vs 0.301; ROUGE-L identical at 0.448). They are reported without seeds, variance or significance tests.
   - The "Transformer Block" variant is slightly worse than the standard HMM on BLEU-4 and CIDEr at length 20. The "Linear NN" variant has worse average perplexity at length 20 (41.99 vs 39.59).
   - The text claims "significant improvements in generation quality" and "slashing maximum perplexity by more than half". Max perplexity is a single-outlier statistic and is non-monotonic across rows (Linear NN 671 vs Transformer Block 1065 at length 32). The standard HMM's max perplexity is exactly 1569.51 at both lengths, which looks like the same outlier or a copy-paste issue. This needs explanation.
   - Under Ctrl-G, hard constraints are satisfied by construction. The abstract's "improves constraint satisfaction" is therefore not what Table 2 measures; it measures quality given satisfaction.
2. **The VLM experiment is small and under-specified.**
   - Table 3 compares a single configuration ("Neural Monarch HMM") against Vanilla, prompting and a 1-sample MC baseline. The toxicity values are small in absolute terms (0.087 -> 0.064). There are no confidence intervals, number of images/captions, number of samples, or classifier details.
   - The "Vanilla" perplexity is 2.36 versus 3.56 for the method. This is a roughly 50% increase, so "preserving fluency" and "comparable fluency" are overstated.
   - The MC baseline is capped at k=1, which makes it nearly a strawman (perplexity 43 and toxicity worse than vanilla). A fair comparison would include a standard controlled-decoding baseline such as FUDGE/GeDi-style classifier guidance or a TRACE variant with text-only context.
   - There is no ablation showing that visual context is what the HMM benefits from, e.g. standard HMM TRACE on the same captions.
   - Detoxification on Hateful Memes with the Perspective API is a weak testbed. Vanilla toxicity is already low, and the metric is noisy.
3. **Distillation results depend on figures only, and the headline claims are unquantified.** The text says "significantly boosts perplexity of tractable models over the prior state of the art". No numbers are given in text or tables, and no reference is given to the base LM's own continuation perplexity. The reader cannot judge how much of the gap to the LM is closed. The comparison to the Lee & Berg-Kirkpatrick method is dismissed in a paragraph, with the claim that "appropriate hyperparameters" fix the baseline, and no data are shown. Gains concentrating on the first few tokens also limit the benefit for constraints depending on the distant future, which is exactly where lookahead matters.
4. **Efficiency claims are not measured.** The abstract states "minimal inference overhead". The paper gives asymptotic tables, but I do not see wall-clock/memory numbers for the Ctrl-G or TRACE settings. The only measurement is the "10x" MC time. Variants (b) and (c) add a transformer layer or a fine-tuned backbone. A fine-tuned backbone (c) cannot "reuse the base LM" at decoding time unless it is the generator itself, which contradicts the paper's pitch of keeping the base LM fixed. How is (c) deployed?
5. **Limited novelty and theory.**
   - An LM-hidden-state-to-HMM-prior head is a modest extension of Ctrl-G/TRACE. The paper positions it against hybrid neural/tractable models (Shao et al., Dos Martires) without comparison.
   - Proposition 1 is the standard bound I <= H(Z) <= log|Z|. It is trivial and says nothing about when the neural encoder helps. Moreover it is also referred to as "Proposition 2" in the text and appendix.
   - There is no analysis of what is lost by keeping the transition and emission parameters fixed across prefixes. The expressiveness of a single latent prior followed by a fixed Markov chain is capped by log H nats of context information.
6. **Scope and generality.** There is a single base LM (GPT-2-large) for text and a 2B VLM. There are no modern, larger LMs, only a single CommonGen setting for Ctrl-G, and no TRACE experiment on text, even though TRACE is cited as a main framework. The one TRACE experiment is the VLM detoxification, and no comparison is made to the original TRACE numbers on RealToxicityPrompts.
7. **Presentation.**
   - Inconsistencies: Qwen2.5-VL-2B (datasets) vs Qwen2-VL-Instruct-2B (Sec 4.2).
   - Typos and duplicated reference (GeDi cited twice with different years).
   - Related work and conclusion are merged and very short.
   - Variant naming differs between Fig. 2 ("linear", "transformer layer", "finetune") and the tables ("Linear NN", "Transformer Block", "Neural Monarch HMM").
   - Datasets, training budgets, hidden sizes for the downstream experiments, and encoder training details are largely absent from the main text.

## Questions
1. Please report mean +/- std over seeds for Table 2 and Table 3, plus the number of instances. Why does the standard-HMM max perplexity stay at 1569.51 across lengths 20 and 32?
2. How much of the perplexity gap to the base LM does each LTLA variant close, in numbers? Please give a table of conditional perplexity for the HMM, LTLA(a/b/c) and the LM itself, per continuation length.
3. Please give wall-clock and memory overhead per decoding step for Ctrl-G and TRACE with variants (a), (b) and (c) against a standard HMM.
4. For the VLM task, what does a standard HMM/TRACE baseline (text-only context) achieve? What do TRACE and other classifier-guided baselines (e.g., FUDGE) achieve under the same classifier? What are the sample sizes and the number of constraint-satisfying captions? How is caption quality evaluated beyond perplexity under the base model?
5. Does variant (c) require a second copy of the backbone at inference? How is the "same base LM" claim consistent with it?
6. Does the benefit hold for TRACE on text-only RealToxicityPrompts/sentiment, and for larger base LMs?
7. Is there any mismatch between the encoder's latent prior and the fixed HMM transition (the HMM is trained jointly, but the prior at step t is only a function of x_<t)? Does the exact forward step handle this consistently when the prefix grows (p(z_{t-1}|x_<t) -> p(z_t|x_<=t))?

## Ratings
- Soundness: 2 (idea is sound, but empirical support is thin and some claims are not backed by the reported numbers)
- Presentation: 2
- Contribution: 2

**Rating: 4 (marginally below the acceptance threshold)**

**Confidence: 4**

Justification: the idea is clean and practically relevant, and could make a good workshop-level or incremental contribution. In its current form the downstream evidence is weak: differences are tiny and without variance, the VLM comparison is thin, claims on fluency and constraint satisfaction are overstated, and the efficiency claims are not measured. A stronger, better-quantified evaluation could raise my score.
