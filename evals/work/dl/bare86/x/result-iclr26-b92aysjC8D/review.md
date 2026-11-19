# Review: Self-Reflective Generation at Test Time (SRGen)

*Note: the extracted text has no appendices (proof, baseline scope, prompts, entropy profiles) and no figures. I judged Figures 2–5 from captions and surrounding text only.*

## Summary
SRGen is a test-time decoding method. At each step it tracks token entropy over a sliding window of N=25 steps. When the current entropy exceeds mean + k·std (k=4), it optimizes a transient vector δ for 3 gradient steps. δ is added to the final hidden state before the LM head. The loss is (1−λ)·NLL of the already-generated prefix under the same δ, plus λ·entropy of the next-token distribution. The vector is then discarded. The authors present this as "proactive" self-reflection, in contrast to post-hoc refinement and RL-trained self-correction. They report Avg@5, Cons@5 and Pass@5 on AIME24/25, HMMT25 and AMC for four models (Qwen2.5-Math-7B, R1-Distill-Qwen-7B, R1-Distill-Llama-8B, Qwen3-32B). Gains are mostly positive, up to +12 Avg@5 and +13 Cons@5 on AIME24 with Distill-Qwen-7B. They also report about 50% latency overhead, composition with SLOT, and a hyperparameter ablation on 100 MATH500 problems. Theorem 1 claims the hybrid loss is "equivalent" to a constrained optimization problem.

## Strengths
- The idea is simple, training-free, model-agnostic and needs no extra samples. Triggering optimization only on entropy spikes is sensible, and sensitivity to the trigger rate (N, k) is examined.
- It is evaluated on four models across two families, including long-CoT reasoning models up to 32B, with several benchmarks and three metrics. The Pass@k analysis (Fig. 3) honestly shows that Pass@k converges to the base as k grows, so SRGen mainly sharpens the distribution.
- The method composes with SLOT, and the cost is reported (about +50% time).
- The paper is easy to read and the algorithm is clearly specified.

## Weaknesses
1. **No baselines.** The comparison is only against the unmodified model. The paper claims superiority over reactive/post-hoc refinement and RL self-correction (Table 1), but no such method is run. Table 1's "Training cost / Latency / Composability" ratings are qualitative assertions. Appendix D reportedly discusses "baseline scope", but I could not see it. Obvious missing controls:
   - Lower temperature, or sharpened sampling (SRGen is itself an entropy-reducing intervention, so this is the natural control). Greedy decoding results for the reasoning models are also missing.
   - Entropy/confidence-aware decoding such as DeepConf (cited), or forking/branching at high-entropy tokens.
   - Entropy-minimization test-time methods (TENT-style / EM-based inference).
   - Budget-matched alternatives. +50% compute could instead buy more samples for majority voting (Cons@7–8) or a longer budget.
   - A random-trigger or fixed-interval ablation, which would test whether the entropy trigger matters.
2. **Statistical reliability.**
   - AIME24/25 and HMMT have 30 problems, and Avg@5 is over 5 samples. One problem is 3.3 points. Cons@5 changes such as 6.7→23.3 are decided by a handful of problems and by tie-breaking among 5 votes. No seeds, confidence intervals or significance tests are reported.
   - Several entries are inconsistent with 30 problems (e.g., Pass@5 of 13.0, 53.0, 33.0, 6.0), so the metric computation or rounding is unclear.
   - The base Cons@5 of Qwen2.5-Math-7B on AIME24 (6.7) is far below its Avg@5 (14.6), which shows how noisy and tie-sensitive the metric is.
3. **Baseline numbers look low or unusual, and truncation may confound the gains.**
   - Qwen2.5-Math-7B is evaluated with a 4,096-token cap. Its poor base numbers come largely from truncation and repetition loops. An entropy-reducing intervention can shorten outputs or break loops, which would improve scores without any "reflection". There is no output-length or truncation-rate analysis.
   - Reported base numbers for the distilled models and Qwen3-32B (e.g., Distill-Qwen-7B on AMC, 51.0) appear lower than commonly reported values. This suggests a non-standard prompt or evaluation setup, and gains on an under-tuned baseline may not transfer to a well-tuned one. Gains on AMC are near zero for the distilled models. The paper does not say whether Qwen3-32B is in thinking mode.
4. **The mechanism is not shown to be "reflection".** δ is added to the last hidden state only, so it acts as an input-specific bias W·δ on the logits of one token. The loss is NLL of the prefix plus entropy minimization. Learning δ this way is effectively data-dependent logit sharpening, not a retrospective analysis of reasoning. There is no analysis showing that:
   - the corrected token is more often correct than the uncorrected one;
   - intervention at critical tokens is what produces the gain (e.g., the fraction of flipped argmax tokens and their correctness);
   - the entropy-spike tokens are actually the "error" points.
   The λ=0 ablation (CE only) already gives "substantial gains", which sits oddly with the claim that entropy minimization is the key. The "proactive vs. reactive" framing is rhetorical.
5. **Theorem 1 is oversold and adds little.** A minimizer of (1−λ)f+λg also solves min g s.t. f ≤ f(δ*). This is a textbook scalarization fact. ε is defined by the solution itself, so the theorem gives no guidance on setting λ, no guarantee about error reduction, and no convergence guarantee for the 3-step non-convex optimization actually used. Calling it "theoretical guarantees" in the reproducibility statement is an overstatement. Applying the same δ to all earlier hidden states in L_CE is a design choice that is neither justified nor compared with alternatives.
6. **Efficiency claims are under-supported.**
   - Latency is measured only on Qwen2.5-Math-7B, with greedy decoding, a 4k cap and about 6 activations per task. The "bounded ~50%" claim is not shown for 32k-token reasoning traces on the 7–32B models, where activation counts and prefix length (the L_CE cost grows with the prefix) are much larger.
   - Eq. 10 ignores the cost of the prefix-wide loss. The paper does not say whether cached hidden states are used.
   - Memory overhead is not reported.
   - The 50% overhead is not set against equal-compute baselines (see point 1).
7. **Hyperparameter selection and ablation scope.** All ablations use 100 MATH500 problems, one model (Qwen2.5-Math-7B) and greedy decoding. Accuracy is flat (~71%) across settings, which supports robustness. But a +7-point gain from a single iteration also hints that the effect may be a generic perturbation or sharpening. Hyperparameters (k=4, N=25, λ=0.05, 3 steps) are applied unchanged to reasoning models with very different entropy profiles, without sensitivity checks there. SLOT combination results are only on the 4k-capped Qwen2.5-Math-7B with greedy decoding.
8. **Scope and text inconsistencies.** Only exact-answer math benchmarks are used. There is no code or general reasoning task, even though the paper claims broad "reliable LLM reasoning" and "plug-and-play" applicability. Sec. 5.2 says "only DeepSeek-R1-Llama-7B shows a decrease" in Cons@5, but Table 2 shows Distill-Llama-8B rising on AIME24 (+16.6) and having no Cons@5 decrease in any row. The Pass@k claim "higher in most" hides many zero-change entries. Diversity loss from entropy reduction is only briefly discussed.
9. **Reproducibility.** Code is promised only after review. Evaluation details (answer extraction, prompt templates, seeds) are relegated to appendices.

## Questions
1. How does SRGen compare against budget-matched alternatives: Cons@k with 1.5× more samples, lower temperature/greedy, DeepConf, and entropy-guided branching? Please show a compute vs. accuracy plot.
2. What is the effect of SRGen on output length and truncation rate (especially for Qwen2.5-Math-7B at 4k)? Do the gains survive when the length cap is large?
3. What fraction of intervention points changes the argmax token, and how often is the changed token correct? Does a random trigger or a trigger on low-entropy tokens perform similarly?
4. Please give confidence intervals or results over many seeds (e.g., 16–64 samples) for AIME/HMMT. Why do some Pass@5 values (e.g., 13.0, 53.0) not correspond to multiples of 1/30?
5. Please report wall-clock overhead, number of activations and memory on the 32k-token settings for the 7B–32B reasoning models.
6. What does Theorem 1 give beyond standard scalarization? Can it say anything about how to choose λ or about the quality of the 3-step solution?
7. Why was δ applied only to the final hidden state? What about earlier layers?
8. Do the gains hold on non-math benchmarks (GPQA, LiveCodeBench) and with Qwen3 in thinking mode using official sampling settings?

## Ratings
- Soundness: 2
- Presentation: 3
- Contribution: 2
- Rating: 4
- Confidence: 4
